#!/usr/bin/env python3
"""Independent exact scalar audit; no writer implementation is imported.

Certified old normalized constants are mathematical inputs, not expected
outputs. The writer results are read only after all independent checks pass.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sys
sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent.parent


def scalar(m, k, e, mass_lower=None):
    d = m+2
    if mass_lower is None:
        prev, cur = 0, 1
        total = 1
        for j in range(m):
            prev, cur = cur, 7*cur-prev
            total += cur
        M = 5+27*total
        alpha = Q(total*M**(k-1), 2*d*k-3)
        s, c = 9*alpha, 18*alpha*alpha
        beta = (Q(M+2, 2*d+1)-1)**2
    else:
        M = mass_lower
        s = Q(9*M**k, 32*(2*d*k-3))
        c = Q(9*M**(2*k), 512*(2*d*k-3)**2)
        beta = Q(M*M, 4*(2*d+1)**2)
    D, DJ = 2*(d*k+2), 2*(d*k+3)
    z = e(k-1)/729
    single = e(k)*z/(8*D)  # The l margin after addition and normalization.
    midpoint_dominant = single*z/D
    return {
        'single_perturbation': single*beta*s/3,
        'midpoint_subtraction': midpoint_dominant*s*s/48,
        'proxy_absorption': single*z*c/(96*DJ),
        'multiplier_absorption': single*c/(96*1296),
        'outer_propagator_growth': z*s/(2*D),
        'correction_coefficient_domination': c/2,
        'trace_central_bound': s,
        'seed_ratio_bound': beta,
    }


def strengths(m, j):
    if m == 0:
        return Q(9)**(j//2)
    return Q(3)*Q(2)**(2*m-3)*(Q(3)*Q(2)**(m-1))**(j-1)/(2*j)


def p0_exact(m):
    # Separate full-Laurent recurrence for the smoothed prefix central term.
    z = {-1:2, 0:3, 1:2}
    prev, cur, total = {}, {0:1}, {0:1}
    for _ in range(m):
        nxt = {}
        for i, a in z.items():
            for j, b in cur.items():
                nxt[i+j] = nxt.get(i+j, 0)+a*b
        for i, a in prev.items():
            nxt[i] = nxt.get(i,0)-a
        prev, cur = cur, {i:a for i,a in nxt.items() if a}
        for i,a in cur.items():
            total[i] = total.get(i,0)+a
    return total.get(-1,0)+total[0]+total.get(1,0)


def encoded(d):
    return {k:str(v) for k,v in d.items()}


def main():
    old = json.loads((BASE/'arbk_seed/old_normalized_constants.json').read_text())
    old = {r['m']:r for r in old['records']}
    thresholds = {0:21,1:11,2:6,3:5,4:4,5:5}
    small_blocks = {1:(Q(1,301),Q(1,4)),2:(Q(1,513),Q(1,4)),
                    3:(Q(1,785),Q(1,4)),4:(Q(1,1114),Q(1,5))}
    records = []
    for m in range(70):
        if m == 0:
            E, r = Q(1,256), Q(1,3)
            e = lambda j: E*r**j
        else:
            E, r = small_blocks[m] if m in small_blocks else (Q(old[m]['ell_m']),Q(old[m]['one_factor_rate']))
            e = lambda j: E*r**(j-1)/(4*j)
        k = thresholds.get(m,3)
        gates, next_gates = scalar(m,k,e), scalar(m,k+1,e)
        assert min(gates.values()) > 1
        ratios = {name:next_gates[name]/value for name,value in gates.items()}
        assert all(v>1 for name,v in ratios.items() if name!='seed_ratio_bound')
        assert ratios['seed_ratio_bound'] == 1
        seed_required = 10 if m == 0 else 8*p0_exact(m)
        assert strengths(m,k) >= seed_required
        assert strengths(m,k-1) >= 189
        records.append({'m':m,'k':k,'gates':encoded(gates),'ratios':encoded(ratios),
                        'seed_required':str(seed_required)})
    c0, sigma = Q(1,400000000), Q(59,100)
    def analytic_input(m):
        E = c0*c0*sigma**(2*m+1)/(16*(m+3))
        r = c0*sigma**m/(4*(m+3))
        return r, lambda j:E*r**(j-1)/(4*j)
    r, e = analytic_input(70)
    _, e_next = analytic_input(71)
    M = 27*6**70
    corner = scalar(70,3,e,M)
    after = scalar(71,3,e_next,6*M)
    assert min(corner.values()) > 1
    m_ratios = {name:after[name]/v for name,v in corner.items()}
    assert min(m_ratios.values()) > 1
    k_lower = {
        'single_perturbation':r*r*M/4,
        'midpoint_subtraction':r**3*M*M/12,
        'proxy_absorption':r**3*M*M/12,
        'multiplier_absorption':r*r*M*M/6,
        'outer_propagator_growth':r*M/3,
        'correction_coefficient_domination':Q(4,9)*M*M,
        'trace_central_bound':Q(2,3)*M,
        'seed_ratio_bound':Q(1),
    }
    assert all(v>1 for name,v in k_lower.items() if name!='seed_ratio_bound')
    assert r*r*M >= 16
    assert 6*sigma*sigma*Q(73,74)**2 > 1
    assert strengths(70,2) >= 189
    assert strengths(70,3) >= 4*7**71
    old_dominant = c0*c0*sigma**141/(4*73)
    old_eps = Q(145,9*6**70)
    assert old_dominant >= 12*old_eps
    old_ratio = 6*sigma*sigma*Q(73,74)*Q(145,147)
    assert old_ratio > 1
    # Only now compare independently computed scalars with writer output.
    writer = json.loads((BASE/'arbk_root/scalar_closure_results.json').read_text())
    for ours,theirs in zip(records,writer['fixed_m_records']):
        assert ours['m']==theirs['m'] and ours['k']==theirs['all_k_from']
        assert ours['gates']==theirs['gates']
        assert ours['ratios']==theirs['consecutive_k_ratios']
        assert Q(ours['seed_required'])==Q(theirs['seed_required_strength'])
    tail = writer['analytic_m_tail']
    assert encoded(corner)==tail['gates_at_corner']
    assert encoded(m_ratios)==tail['consecutive_m_ratios_at_k3']
    assert encoded(k_lower)==tail['all_k_ratio_lower_bounds_at_m70']
    result = {'status':'PASS shared-session independent exact scalar audit',
              'writer_implementation_imported':False,
              'all_70_fixed_m_gate_vectors_and_ratios_match':True,
              'analytic_corner_and_ratio_vectors_match':True,
              'fixed_m_records':records,
              'analytic_corner':encoded(corner),'analytic_m_ratios':encoded(m_ratios),
              'analytic_all_k_ratio_lower_bounds':encoded(k_lower),
              'old_single_gate_ratio':str(old_dominant/(12*old_eps)),
              'old_single_m_ratio':str(old_ratio)}
    output = Path(__file__).with_name('scalar_closure_independent_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if not isinstance(v,(dict,list))}))


if __name__ == '__main__':
    main()
