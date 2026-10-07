"""Replay the frozen defect campaign without upgrading its proof scope."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
JOBS = [
    ('root_obstruction_audit.py', 'root_obstruction_audit_results.json'),
    ('packet_algebra_verify.py', 'packet_algebra_results.json'),
    ('packet_spectral_sparse_verify.py', 'packet_spectral_sparse_results.json'),
    ('proxy_algebra_verify.py', 'proxy_algebra_results.json'),
    ('proxy_character_verify.py', 'proxy_character_results.json'),
    ('falsification_defect.py', 'falsification_defect_results.json'),
    ('falsification_weakening_audit.py', 'falsification_weakening_audit_results.json'),
    ('audit_packet_weakening_verify.py', 'audit_packet_weakening_results.json'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest(name):
    manifest = json.loads((HERE/name).read_text())
    checked = []

    def visit(node):
        if isinstance(node, list):
            for item in node:
                visit(item)
        elif isinstance(node, dict):
            if 'file' in node and 'sha256' in node:
                choices = [HERE/node['file'], HERE.parent/node['file']]
                valid = [p for p in choices if p.is_file()]
                assert valid, (name, node['file'], 'missing')
                path = valid[0]
                assert sha(path) == node['sha256'], (name, node['file'])
                if 'bytes' in node:
                    assert path.stat().st_size == node['bytes']
                checked.append(node['file'])
            for value in node.values():
                if isinstance(value, (list, dict)):
                    visit(value)

    visit(manifest)
    return {'manifest': name, 'verified_entries': len(checked)}


def replay(job):
    script, output = job
    original = sha(HERE/output)
    result = subprocess.run([sys.executable, str(HERE/script)], cwd=HERE,
                            capture_output=True, text=True)
    assert result.returncode == 0, (script, result.stderr[-4000:])
    assert sha(HERE/output) == original, (script, 'saved output changed')
    return {'script': script, 'output': output, 'sha256': original,
            'exit_code': 0, 'identical_output_bytes': True}


def main():
    inputs = {p.name: sha(p) for p in HERE.iterdir()
              if p.is_file() and p.name not in
              ('replay_results.json', 'checkpoint_manifest.json')}
    manifests = [verify_manifest(name) for name in
                 ('falsification_manifest.json', 'audit_manifest.json')]
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(replay, JOBS))
    for name, checksum in inputs.items():
        assert sha(HERE/name) == checksum, ('frozen file changed', name)
    for name in ('falsification_manifest.json', 'audit_manifest.json'):
        verify_manifest(name)
    result = {
        'status': 'PASS_EXACT_DETERMINISTIC_REPLAY',
        'replays': records, 'manifests': manifests,
        'frozen_input_files_unchanged': len(inputs),
        'arithmetic': 'Exact Python integer, rational and formal polynomial arithmetic',
        'full_tree_Local_TP2': 'OPEN',
        'remaining_closure_types': ['BOTH paired MP_0', 'BOTH strict Q<D'],
        'scope': 'Finite replay checks identities and witness certificates. Universal conclusions require the independently audited analytic arguments; each obstruction retains its explicitly stated domain.',
    }
    (HERE/'replay_results.json').write_text(json.dumps(result, indent=2)+'\n')
    files = [{'file': p.name, 'bytes': p.stat().st_size, 'sha256': sha(p)}
             for p in sorted(HERE.iterdir())
             if p.is_file() and p.name != 'checkpoint_manifest.json']
    manifest = {
        'private_base_commit': '457e1588d0106c9a9262e6a38d9e882e9678990d',
        'public_reference': '6e770f3b3e3f26af5df5308572917559343b68f4',
        'files': files, 'full_tree_Local_TP2': 'OPEN',
        'scope': 'Complete campaign snapshot; only this self-hashing manifest is excluded.',
    }
    (HERE/'checkpoint_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'replays': len(records),
                      'identical_outputs': len(records),
                      'full_tree_Local_TP2': 'OPEN'}))


if __name__ == '__main__':
    main()
