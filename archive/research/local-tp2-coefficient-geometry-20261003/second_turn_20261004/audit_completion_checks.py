#!/usr/bin/env python3
"""Independent assembly/bookkeeping audit; no mathematical-code imports."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE/name).read_text())


def main():
    primary = read('kernels_certificate_results.json')
    independent = read('finite_audit_independent_results.json')
    proxy = read('proxy_mass_results.json')
    small = read('falsification_proxy_audit_results.json')
    full_proxy = read('falsification_proxy_full_audit_results.json')
    identities = read('audit_identity_results.json')
    assert primary['status'] == independent['status'] == 'PASS'
    assert primary['scope'] == independent['scope_completed'] == [0, 409]
    expected = {(m, s, k) for m in range(410) for s in (False, True)
                for k in ('single', 'midpoint')}
    pmap = {(r['m'], r['smooth'], r['label']): r for r in primary['cases']}
    imap = {(r['m'], r['smooth'], r['label']): r for r in independent['cases']}
    assert set(pmap) == set(imap) == expected
    assert len(primary['cases']) == len(independent['cases']) == len(expected)
    for key in expected:
        p, i = pmap[key], imap[key]
        m, smooth, label = key
        degree = (2*m+3 if label == 'single' else 3*m+6)+int(smooth)
        count = (3 if label == 'single' else 27)*(degree+1)
        assert p['degree'] == i['degree'] == degree
        assert p['margins'] == i['margins'] == count
        assert p['negative'] == i['negative'] == p['zero'] == i['zero'] == 0
        assert int(p['minimum']) == int(i['minimum']) > 0
        assert p['sha256'] == i['sha256']
        if label == 'single':
            assert F(int(p['lambda_numerator']), int(p['lambda_denominator'])) == 3*F(2)**(2*m-3)
        else:
            assert p['alpha'] == i['alpha']
            assert p['reference_central'] == i['b0']
    assert proxy['status'] == small['status'] == identities['status'] == 'PASS'
    assert proxy['inner_interval'] == [0, 409]
    assert [r['m'] for r in proxy['certificates']] == list(range(410))
    for r in proxy['certificates']:
        assert F(r['beta']) > 6
        assert r['base_minor_count'] == r['m']+5
        assert int(r['minimum_base_minor']) > 0
        assert all(F(v) > 0 for v in r['template_margin_bernstein'])
        assert all(F(v) > 0 for v in r['trace_margin_bernstein'])
        assert F(r['tail_vs_proxy_threshold_residual']) > 0
        assert F(r['minimum_fixed_proxy_residual']) > 0
    assert sum(r['base_minor_count'] for r in proxy['certificates']) == 85895
    assert sum(len(r['small_outer_certificates']) for r in proxy['certificates']) == 5
    for a in small['records']:
        b = proxy['certificates'][a['m']]
        for key in ('beta', 'alpha_trace', 'gamma_template',
                    'template_margin_bernstein', 'trace_margin_bernstein',
                    'paired_trace_80_margin_bernstein', 'small_outer_certificates'):
            assert a[key] == b[key]
    assert full_proxy['status'] == 'PASS' and full_proxy['all_record_fields_match_author']
    assert full_proxy['fixed_base_minor_count'] == 85895
    assert full_proxy['central_Bernstein_array_count'] == 820
    assert full_proxy['central_Bernstein_coefficient_count'] == 2460
    assert [r['m'] for r in full_proxy['records']] == list(range(410))
    for a in full_proxy['records']:
        b = proxy['certificates'][a['m']]
        assert all(a[key] == b[key] for key in a)
    assert full_proxy['source_results_sha256'] == sha256((HERE/'proxy_mass_results.json').read_bytes()).hexdigest()
    assert full_proxy['source_script_sha256'] == sha256((HERE/'proxy_mass_cert.py').read_bytes()).hexdigest()
    assert full_proxy['audit_script_sha256'] == sha256((HERE/'falsification_proxy_full_audit.py').read_bytes()).hexdigest()
    assert full_proxy['disclosed_packing_foundation_sha256'] == sha256((HERE/'finite_audit_independent.py').read_bytes()).hexdigest()
    m = 410
    sigma, c0 = F(59, 100), F(1, 400000000)
    epsilonH = F(16*(2*m+3), 6**(m+1))
    epsilonL = epsilonH/3
    EH = c0**3*sigma**(3*m+2)/(16*(m+2)*(m+4))
    EL = c0**2*sigma**(2*m+1)/(4*(m+2))
    gates = {
        'kernel_epsilonH_below_one': epsilonH < 1,
        'kernel_EH_ge_12epsilonH': EH >= 12*epsilonH,
        'kernel_EL_ge_12epsilonL': EL >= 12*epsilonL,
        'kernel_double_ratio_increasing_from_start':
            6*sigma**3*F((m+2)*(m+4)*(2*m+3), (m+3)*(m+5)*(2*m+5)) > 1,
        'kernel_single_ratio_increasing_from_start':
            6*sigma**2*F((m+2)*(2*m+3), (m+3)*(2*m+5)) > 1,
        'kernel_strength_ge_8_smoothed_reference_mass':
            9*2**(3*m-3) >= 4*(7**(m+3)-1),
        'proxy_trace_mass_ge_4': F(3*2**m, 2*m+7) >= 4,
        'proxy_gamma_above_12': F(3*2**(2*m-3), 4*m+7) > 12,
        'proxy_scalar_at_start': F(8, 7)**m > 10752*(4*m+7),
        'proxy_scalar_propagates': F(8*(4*m+7), 7*(4*m+11)) > 1,
        'proxy_smoothed_J_strength_ge_28': 3*2**(m-1) >= 28,
        'm0_outer_parity_N5': F(80**2, 5) > F(221, 3),
        'm0_outer_parity_N6': F(80**2, 6)*F(4, 5) > F(221, 3),
        'm1_outer_start_N4': F(40*5**3, 8) > F(1517, 6),
        'm2_outer_start_N2': F(707*5, 4) > F(2600, 3),
    }
    assert all(gates.values())
    sources = ['reduction_additional_turn.md', 'kernels_theorem.md',
               'proxy_mass_compare.md', 'THEOREM.md', 'RESULT_JA.md',
               'audit_final_report.md', 'audit_frozen_algebra.md',
               'audit_scaled_relative_minors.md', 'audit_identity_check.py',
               'audit_identity_results.json', 'audit_completion_checks.py',
               'kernels_certificate_results.json', 'finite_audit_independent_results.json',
               'proxy_mass_results.json', 'falsification_proxy_audit_results.json',
               'falsification_proxy_full_audit_results.json', 'falsification_proxy_full_audit.py']
    output = {
        'status': 'PASS', 'scope': 'Analytic proof assembly, explicit inherited foundations, exact finite certificate coverage, and separately identified independent replays.',
        'kernel_inner_interval': [0, 409], 'kernel_records': len(expected),
        'kernel_margins_independently_matched': sum(r['margins'] for r in pmap.values()),
        'proxy_inner_interval': [0, 409], 'proxy_fixed_base_minors': 85895,
        'proxy_central_interval_arrays': 820, 'proxy_small_outer_records_independently_matched': 5,
        'proxy_independent_central_replay_scope': [0, 409],
        'proxy_central_coefficients_independently_matched': 2460,
        'actual_identity_cases': identities['identity_cases'],
        'tail_start': m, 'exact_scalar_gates': gates,
        'fingerprints': {name: sha256((HERE/name).read_bytes()).hexdigest() for name in sources},
    }
    (HERE/'audit_completion_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k != 'fingerprints'}, indent=2))


if __name__ == '__main__':
    main()
