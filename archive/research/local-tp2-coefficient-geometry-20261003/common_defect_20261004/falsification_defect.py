#!/usr/bin/env python3
"""Exact constructive trace/sign witnesses; no broad tree scan."""
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'common_crosscenter_20261004'))
from falsification_crosscenter import H, add, at, canonical, cadd, defects, first_negative, mixed, mul, power, relative, scale, sub, tensor, y, y2, z
from adversarial_probe import fricke, ordinary


def shift_variable(p, base):
    return [sum(p[j] * comb(j, i) * base ** (j-i) for j in range(i, len(p))) for i in range(len(p))]


def full_family_trace_certificate():
    # Fourier entries of f_K=z+beta*2(x+K)^2, as polynomials in K.
    rows = [[51, 48, 18], [38, 48, 12], [30, 24, 6], [12, 12], [6]]
    endpoints = []
    for r in (-2, 2):
        hh = [sub(rows[0], [r])] + rows[1:] + [[0]]
        qq = [scale(hh[1], 2)] + [add(hh[j-1], hh[j+1] if j+1 < len(hh) else [0]) for j in range(1, 6)]
        certs = []
        for k in range(5):
            for l in range(k+1, 6):
                pp = sub(mul(hh[k], qq[l]), mul(hh[l], qq[k]))
                shifted = shift_variable(pp, 2)
                assert min(shifted) >= 0 and shifted[0] > 0
                certs.append({'columns': [k, l], 'Kminus2_coefficients': shifted})
        endpoints.append({'r': r, 'coefficients': certs})
    # All noncentral coefficients are affine in r. Central derivative is
    # 2r-(2h0+h2)<0 throughout [-2,2], K>=2, so its minimum is r=2.
    assert 4 - (2*(51+48*2+18*4)+(30+24*2+6*4)) < 0
    return {'domain': 'K>=2 and -2<=r<=2', 'endpoint_certificates': endpoints,
            'minimum_character_lower_bound': min(c['Kminus2_coefficients'][0] for e in endpoints for c in e['coefficients'])}


def ordinary_trace_witnesses():
    beta = scale(y2, 3)
    v = scale(power([2, 1], 5), 6)
    mode_records = []
    for smooth in (False, True):
        p = mul(y, v) if smooth else v
        assert min(p) > 0 and min(H(p)) > 0 and min(defects(H(p))) > 0
        assert first_negative(tensor(p)) is None
        mode_records.append({'mode': 'y' if smooth else 'raw', 'minimum_defect': min(defects(H(p))),
                             'minimum_nonzero_character': min(tensor(p).values())})
    out = []
    for K in (35, 64):
        B = scale(power([K, 1], 2), 2)
        f = add(z, mul(beta, B))
        g = mul(beta, v)
        child = add(f, g)
        expected = -26028*K*K + 172080*K + 24574464
        assert defects(H(child))[3] == expected < 0
        assert min(f) > 0 and min(child) > 0
        assert len(f)-1 == 4 and len(v)-1 == 5 and f[-1] == v[-1] == 6
        assert first_negative(tensor(sub(f, [-2]))) is None
        assert first_negative(tensor(sub(f, [2]))) is None
        out.append({'K': K, 'B': B, 'f': f, 'v': v, 'f_row': H(f), 'v_row': H(v),
                    'child_row': H(child), 'failed_index': 3, 'failed_defect': expected,
                    'relaxed_degree_pattern': {'dX': 0, 'dY': 2, 'dC': 3, 'dT': 4, 'dv': 5},
                    'relaxed_lc_pattern': {'lcX': 1, 'lcY': 1, 'lcC': 2, 'lcT': 6, 'lcv': 6},
                    'ordinary_ancestry_necessary_inequality': {'B0': B[0], 'upper_bound_1plus3over2_B1minusB2': 1+Fraction(3,2)*(B[1]-B[2])}})
    # The entire K family fails from K=35 onward, by the exact quadratic.
    assert -26028*34*34+172080*34+24574464 == 336816
    assert -26028*35*35+172080*35+24574464 == -1287036
    assert -52056*35+172080 < 0
    return {'classification': 'ORDINARY INTEGER-POSITIVE RELAXED TRACE/V; NO NORMALIZED FRICKE OR ORIGIN',
            'v_mode_certificates': mode_records, 'witnesses': out,
            'failed_defect_polynomial_in_K': [24574464, 172080, -26028],
            'first_failing_integer_K_in_family_Kge2': 35}


def canonical_monotonicity_witness():
    state = canonical('sss')
    assert fricke(state) == [0] and ordinary(state)
    trace, n = sub(state['M'], [1]), state['e']
    c = add(n, state['g'], state['s'])
    B = add(mul(n, add(trace, [1])), c)
    L2 = sub(B, scale(n, 3))
    raw = mixed(L2, n).get((6, 0), 0)
    smooth = mixed(mul(y, L2), mul(y, n)).get((8, 0), 0)
    assert raw == -6386912 and smooth == -17705216
    assert H(n) == [113, 88, 40, 8]
    assert defects(H(L2))[3] == 554312100448
    assert defects(H(n))[3] == 64
    assert mixed(B, n)[6, 0] == -6386528
    return {'classification': 'ACTUAL CANONICAL SSS SIGN-SHORTCUT FAILURE; NOT PACKET-CLOSURE FAILURE',
            'path': 'sss', 'a': state['a'], 'e': n, 'r': state['r'], 'T': trace, 'c': c,
            'B': B, 'L2': L2, 'n_row': H(n), 'L2_row': H(L2),
            'raw_columns': [3, 4], 'raw_character': [6, 0], 'raw_mixed': raw,
            'y_columns': [4, 5], 'y_character': [8, 0], 'y_mixed': smooth,
            'delta3_L2': defects(H(L2))[3], 'delta3_n': defects(H(n))[3],
            'J_B_n_at_index3': mixed(B, n)[6, 0]}


def index1_weaker_witness():
    beta, v = scale(y2, 3), power([2, 1], 16)
    base = add(z, [2], mul(beta, v))
    D, J = defects(H(base))[1], mixed(beta, base)[2, 0]
    A = D // (-J) + 1
    f = add(z, scale(beta, A))
    value = defects(H(add(f, mul(beta, v), [2])))[1]
    assert A == 9450423029 and value == -37216985
    assert min(defects(H(v))) > 0 and min(defects(H(mul(y, v)))) > 0
    assert first_negative(tensor(v)) is None and first_negative(tensor(mul(y, v))) is None
    return {'classification': 'WEAKER INDEX1 CRITERION FAILURE; LC/DEGREE CORRELATIONS NOT MET',
            'A': A, 'v': '(x+2)^16', 'lc_f': f[-1], 'lc_v': v[-1],
            'J_beta_beta_v_index1': mixed(beta, mul(beta, v))[2, 0],
            'base_defect': D, 'linear_A_coefficient': J, 'failed_index1': value}


def main():
    results = {'scope': 'EXACT CONSTRUCTIVE WITNESSES; FULL CANONICAL BOTH CLOSURE OPEN',
               'continuous_family_trace': full_family_trace_certificate(),
               'ordinary_positive_trace': ordinary_trace_witnesses(),
               'canonical_monotonicity': canonical_monotonicity_witness(),
               'weaker_index1': index1_weaker_witness()}
    (HERE / 'falsification_defect_results.json').write_text(json.dumps(results, indent=2, default=str)+'\n')
    print(json.dumps({'ordinary_positive_failed_defects': [w['failed_defect'] for w in results['ordinary_positive_trace']['witnesses']],
                      'full_family_trace_minimum': results['continuous_family_trace']['minimum_character_lower_bound'],
                      'canonical_raw_monotonicity_source': results['canonical_monotonicity']['raw_mixed'],
                      'canonical_y_monotonicity_source': results['canonical_monotonicity']['y_mixed'],
                      'weaker_index1_failed_defect': results['weaker_index1']['failed_index1']}, indent=2))


if __name__ == '__main__':
    main()
