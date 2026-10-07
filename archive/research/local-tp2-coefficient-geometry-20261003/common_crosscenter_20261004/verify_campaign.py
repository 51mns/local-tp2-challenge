"""Replay frozen exact certificates and independent audits, not full closure."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
GENERATORS = [
    ('root_central_trace_verify.py', 'root_central_trace_results.json'),
    ('packet_algebra_verify.py', 'packet_algebra_results.json'),
    ('packet_spectral_verify.py', 'packet_spectral_results.json'),
    ('proxy_algebra_verify.py', 'proxy_algebra_results.json'),
    ('proxy_character_verify.py', 'proxy_character_results.json'),
    ('falsification_crosscenter.py', 'falsification_crosscenter_results.json'),
]
AUDITS = [
    ('audit_dependency_verify.py', 'audit_dependency_results.json'),
    ('falsification_spectral_audit.py', 'falsification_spectral_audit_results.json'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((HERE / name).read_text())


def check_item(item, root):
    path = root / item['file']
    assert sha(path) == item['sha256'], str(path)
    if 'bytes' in item:
        assert path.stat().st_size == item['bytes'], str(path)


def check_manifests():
    f = read('falsification_manifest.json')
    for item in f['owned_files']:
        check_item(item, HERE)
    for item in f['readonly_sources']:
        check_item(item, HERE.parent)
    audit = read('audit_manifest.json')
    for item in audit['files'] + audit['audited_sources']:
        check_item(item, HERE)


def replay(job):
    script, output = job
    before = sha(HERE / output)
    process = subprocess.run([sys.executable, str(HERE / script)], cwd=HERE,
                             capture_output=True, text=True)
    assert process.returncode == 0, (script, process.stderr[-4000:])
    after = sha(HERE / output)
    assert before == after, (script, 'replay changed frozen output', before, after)
    return {'script': script, 'exit_code': 0, 'output': output,
            'sha256': after, 'identical_output_bytes': True}


def main():
    check_manifests()
    with ThreadPoolExecutor(max_workers=4) as pool:
        primary = list(pool.map(replay, GENERATORS))
    with ThreadPoolExecutor(max_workers=2) as pool:
        audits = list(pool.map(replay, AUDITS))
    check_manifests()
    result = {
        'status': 'PASS_EXACT_DETERMINISTIC_REPLAY',
        'replays': primary + audits,
        'frozen_manifests_verified': ['falsification_manifest.json', 'audit_manifest.json'],
        'arithmetic': 'Python exact integers/Fractions and sparse formal polynomial identities',
        'full_tree_Local_TP2': 'OPEN',
        'remaining_P_D_closure_types': ['BOTH changed-center paired MP_sharp',
                                      'BOTH strict Q<D'],
        'scope': 'Finite replay verifies saved algebra/certificates; arbitrary-parent conclusions require the independently audited analytic arguments. Counterexamples retain their stated relaxed domains.',
    }
    (HERE / 'replay_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'replays': len(primary) + len(audits),
                      'identical_output_files': len(primary) + len(audits),
                      'full_tree_Local_TP2': 'OPEN'}, indent=2))


if __name__ == '__main__':
    main()
