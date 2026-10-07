"""Check the saved exact certificates and their complete comparison.

This is a fast artifact check, not a new proof or a replay of all margins.
Full generator/replay commands are recorded in MANIFEST.json.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text())


def check():
    primary = read('kernels_certificate_results.json')
    independent = read('finite_audit_independent_results.json')
    assert primary['status'] == independent['status'] == 'PASS'
    assert primary['scope'] == independent['scope'] == [0, 409]
    expected = {(m, smooth, label) for m in range(410)
                for smooth in (False, True) for label in ('single', 'midpoint')}

    def index(records):
        result = {}
        for r in records:
            key = (r['m'], r['smooth'], r['label'])
            assert key not in result
            assert r['negative'] == r['zero'] == 0
            assert Fraction(r['minimum']) > 0
            result[key] = r
        assert set(result) == expected
        return result

    a, b = index(primary['cases']), index(independent['cases'])
    for key in sorted(expected):
        for field in ('degree', 'margins', 'minimum', 'witness', 'sha256'):
            assert a[key][field] == b[key][field], (key, field)
    margins = sum(r['margins'] for r in a.values())
    assert margins == 14766150

    proxy = read('proxy_mass_results.json')
    assert proxy['status'] == 'PASS'
    assert proxy['inner_interval'] == [0, 409]
    assert proxy['analytic_tail_start'] == 410
    assert [r['m'] for r in proxy['certificates']] == list(range(410))
    fixed_count = small_count = 0
    for r in proxy['certificates']:
        assert Fraction(r['minimum_base_minor']) > 0
        assert Fraction(r['beta']) > 6
        assert Fraction(r['tail_vs_proxy_threshold_residual']) > 0
        assert Fraction(r['minimum_fixed_proxy_residual']) > 0
        for label in ('template_margin_bernstein', 'trace_margin_bernstein'):
            assert len(r[label]) == 3
            assert all(Fraction(x) > 0 for x in r[label])
        if r['paired_trace_80_margin_bernstein'] is not None:
            assert len(r['paired_trace_80_margin_bernstein']) == 9
            assert all(Fraction(x) > 0 for x in r['paired_trace_80_margin_bernstein'])
        for record in r['small_outer_certificates']:
            assert Fraction(record['proxy_mass_residual']) > 0
        fixed_count += r['base_minor_count']
        small_count += len(r['small_outer_certificates'])
    assert fixed_count == 85895
    assert small_count == 5

    full_proxy = read('falsification_proxy_full_audit_results.json')
    assert full_proxy['status'] == 'PASS'
    assert full_proxy['all_record_fields_match_author'] is True
    assert full_proxy['fixed_base_minor_count'] == fixed_count
    assert full_proxy['central_Bernstein_array_count'] == 820
    assert full_proxy['central_Bernstein_coefficient_count'] == 2460
    assert [r['m'] for r in full_proxy['records']] == list(range(410))
    for actual, replay in zip(proxy['certificates'], full_proxy['records']):
        for field, value in replay.items():
            assert actual[field] == value, (replay['m'], field)
    for field, name in (
            ('source_script_sha256', 'proxy_mass_cert.py'),
            ('source_results_sha256', 'proxy_mass_results.json'),
            ('audit_script_sha256', 'falsification_proxy_full_audit.py'),
            ('independent_primitives_sha256', 'falsification_targeted.py'),
            ('disclosed_packing_foundation_sha256', 'finite_audit_independent.py')):
        assert full_proxy[field] == hashlib.sha256((HERE/name).read_bytes()).hexdigest(), name

    manifest = HERE / 'MANIFEST.json'
    checked_hashes = 0
    if manifest.exists():
        for record in read('MANIFEST.json')['files']:
            data = (HERE / record['path']).read_bytes()
            assert hashlib.sha256(data).hexdigest() == record['sha256'], record['path']
            checked_hashes += 1

    return {
        'status': 'PASS',
        'scope': 'Saved full-range certificates and hash comparison; not a replacement for the mathematical proofs.',
        'matched_kernel_cases': len(expected),
        'matched_exact_positive_Bernstein_margins': margins,
        'positive_fixed_proxy_minors': fixed_count,
        'independently_matched_proxy_Bernstein_arrays': 820,
        'exact_small_outer_cases': small_count,
        'manifest_file_hashes_checked': checked_hashes,
        'arbitrary_path_Local_TP2_proved': False,
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
