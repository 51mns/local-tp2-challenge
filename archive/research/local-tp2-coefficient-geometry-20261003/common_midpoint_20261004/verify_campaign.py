"""Replay the frozen exact certificates; this is not a full-tree proof."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import gzip
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(name):
    return json.loads((HERE / name).read_text())


def check_hash(name, expected, size=None):
    data = (HERE / name).read_bytes()
    assert digest(data) == expected, name
    if size is not None:
        assert len(data) == size, name


def check_manifests():
    network = read('network_manifest.json')
    for key in ('files_sha256', 'transport_audit_inputs_sha256'):
        for name, expected in network[key].items():
            check_hash(name, expected)
    audit = read('audit_manifest.json')
    for key in ('sources_sha256', 'audit_sha256'):
        for name, expected in audit[key].items():
            check_hash(name, expected)
    for item in read('quantitative_manifest.json')['files']:
        check_hash(item['file'], item['sha256'], item['bytes'])
    falsification = read('falsification_manifest.json')
    for key in ('artifacts', 'audited_external_artifacts'):
        for item in falsification[key]:
            check_hash(item['name'], item['sha256'], item.get('bytes'))


GENERATORS = [
    ('network_relative_character.py', ['network_relative_character_results.json']),
    ('packet_transport_subgate_verify.py', ['packet_transport_subgate_results.json']),
    ('proxy_robin_verify.py', ['proxy_robin_results.json']),
    ('root_boundary_q_verify.py', ['root_boundary_q_results.json']),
    ('quantitative_midpoint_bernstein.py', [
        'quantitative_midpoint_bernstein_results.json',
        'quantitative_midpoint_bernstein_full.json.gz']),
]
AUDITS = [
    ('audit_boundary_q_verify.py', ['audit_boundary_q_results.json']),
    ('audit_midpoint_base_verify.py', ['audit_midpoint_base_results.json']),
]


def replay(item):
    script, outputs = item
    before = {name: digest((HERE / name).read_bytes()) for name in outputs}
    process = subprocess.run([sys.executable, str(HERE / script)], cwd=HERE,
                             capture_output=True, text=True)
    assert process.returncode == 0, (script, process.stderr[-4000:])
    after = {name: digest((HERE / name).read_bytes()) for name in outputs}
    assert before == after, (script, 'non-identical replay', before, after)
    return {'script': script, 'exit_code': 0, 'outputs_identical': True,
            'outputs_sha256': after}


def main():
    check_manifests()
    with ThreadPoolExecutor(max_workers=5) as pool:
        generators = list(pool.map(replay, GENERATORS))
    # Audits read producer outputs and must run only after producers finish.
    with ThreadPoolExecutor(max_workers=2) as pool:
        audits = list(pool.map(replay, AUDITS))
    check_manifests()
    quantitative = read('quantitative_midpoint_bernstein_results.json')
    assert quantitative['universal_corner_identity_formal_check'] is True
    for record in quantitative['records']:
        for key in ('sharp_MP2_parameter_certificate_pass',
                    'uniform_MP2_parameter_certificate_pass'):
            assert record[key] is True
        for key in ('H_defects', 'L_defects'):
            assert record[key]['strict_all_supported_bernstein'] is True
    for trace in quantitative['traces']:
        assert trace['certificate']['strict_all_supported_bernstein'] is True
    full = quantitative['full_certificate']
    compressed = (HERE / full['file']).read_bytes()
    payload = gzip.decompress(compressed)
    assert len(compressed) == full['gzip_bytes']
    assert len(payload) == full['uncompressed_bytes']
    assert digest(compressed) == full['gzip_sha256']
    assert digest(payload) == full['uncompressed_sha256']
    json.loads(payload)
    frozen = read('falsification_results.json')
    assert frozen['cases'] == frozen['all_index_strength_certificates'] == 1584
    assert frozen['actual_states'] == 33
    assert frozen['strength_only_failures'] == 0 and not frozen['first_failures']
    record_payload = gzip.decompress((HERE / 'falsification_records.json.gz').read_bytes())
    assert digest(record_payload) == 'ba854ff29fc8e01a8ab55f158887a52dbb2626999d325eb037e95f5cead1cfe3'
    json.loads(record_payload)
    base = read('audit_midpoint_base_results.json')
    boundary = read('audit_boundary_q_results.json')
    assert base['full_relative_Bernstein_coefficients_verified'] == 30348
    assert base['pure_L_H_trace_all_character_coefficients_verified'] == 17607
    assert base['strict_L_H_Bernstein_coefficients_verified'] == 1512
    assert base['strict_trace_Bernstein_coefficients_verified'] == 45
    assert boundary['defects_verified'] == 22
    assert boundary['Bernstein_coefficients_verified'] == 1813
    result = {
        'status': 'PASS_EXACT_REPLAY_AND_FROZEN_HASHES',
        'replays': generators + audits,
        'lane_manifests_verified': 4,
        'archive_payloads_verified': 2,
        'falsification_scan': 'Frozen 1584 cases integrity checked; no new search or replay.',
        'independent_base_counts': {
            'relative_Bernstein': 30348, 'pure_character': 17607,
            'strict_L_H': 1512, 'strict_trace': 45},
        'independent_boundary_counts': {'defects': 22, 'Bernstein': 1813},
        'scope': 'Reproducibility of finite exact certificates and formal identities; universal conclusions additionally require the audited analytic proofs.',
        'remaining_regular_gates': ['BOTH changed-center paired MP_sharp',
                                    'BOTH strict proxy overlap'],
        'full_tree_Local_TP2': 'OPEN',
    }
    (HERE / 'replay_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'replays'}, indent=2))


if __name__ == '__main__':
    main()
