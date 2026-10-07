"""Exact scalar checks for the all-m >=391 normalized-defect proof.

No sampled parameter values or finite-m extrapolation are used.
The continuum block certificate is a separate exact dependency.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


def main():
    sigma = Q(59, 100)
    c0 = Q(1, 400000000)
    checks = {}
    checks['block_rate'] = 4352 * sigma**16
    checks['residue_rate'] = 9 * c0 * (Q(9, 2) * sigma)**18
    assert checks['block_rate'] < 1
    assert checks['residue_rate'] < 1
    checks['trace_eta_h2_at_21'] = c0 * (6*sigma)**21 / 43
    checks['trace_ratio_at_21'] = 6*sigma * Q(43, 45)
    assert checks['trace_eta_h2_at_21'] >= 8
    assert checks['trace_ratio_at_21'] > 1
    assert Q(6**21,43) >= 20
    checks['trace_n0_fraction'] = Q(92,169)
    checks['trace_n1_fraction'] = Q(114,169)
    checks['trace_n2_fraction'] = Q(11,12)
    assert all(checks[k] >= Q(1,2) for k in
               ['trace_n0_fraction','trace_n1_fraction','trace_n2_fraction'])
    def eta_f(m):
        return c0**3 * sigma**(3*m+1)/(16*(m+2)*(m+3))
    def epsilon(m):
        return Q(2*m+5,9*6**m)
    checks['absorption_at_391'] = eta_f(391)/(12*epsilon(391))
    checks['absorption_at_390'] = eta_f(390)/(12*epsilon(390))
    checks['absorption_ratio_at_391'] = (6*sigma**3 *
        Q((391+2)*(2*391+5),(391+4)*(2*391+7)))
    assert checks['absorption_at_391'] >= 1
    assert checks['absorption_at_390'] < 1
    assert checks['absorption_ratio_at_391'] > 1
    checks['strength_mass_at_7'] = Q(9*2**19, 32)*Q(6,7**7-1)
    assert checks['strength_mass_at_7'] >= 1
    checks['epsilon_at_1'] = epsilon(1)
    assert checks['epsilon_at_1'] < 1
    # The two small prefixes omitted by the root-factor extraction.
    rows = {'T1':[4,2], 'P1':[20,16,8,2]}
    for name, row in rows.items():
        h=lambda n: row[abs(n)] if abs(n)<len(row) else 0
        etas=[Q(h(n)**2-h(n-1)*h(n+1)-h(n+1)**2+h(n)*h(n+2),h(n)**2)
              for n in range(len(row))]
        checks[name+'_eta'] = min(etas)
        assert min(etas) >= c0*sigma
    block = Path('fulltree_normalized_block_results.json')
    block_data=json.loads(block.read_text())
    assert block_data['status']=='PASS'
    assert block_data['patterns']==12870
    assert block_data['defect_arrays']==218790
    assert block_data['negative_coefficients']==0
    assert block_data['zero_coefficients']==0
    output={
        'status':'PASS',
        'proved_inner_indices':'all integers m >= 391',
        'parameters':'independent r,s,c in [-2,2]',
        'remaining_inner_indices':'1 <= m <= 390',
        'block_result_sha256':hashlib.sha256(block.read_bytes()).hexdigest(),
        'checks':{k:{'exact':str(v),'decimal':float(v)} for k,v in checks.items()},
    }
    Path('fulltree_oneturn_normalized_tail_results.json').write_text(
        json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':'PASS','uniform_threshold':391,
                     'scalar_checks':len(checks)}))


if __name__=='__main__':
    main()
