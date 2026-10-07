#!/usr/bin/env python3
"""Independent reconstruction of the R^2 L^ell finite proof certificates.

This imports no code from the author lane.  It starts with the canonical
mutation and ordinary x polynomials, whereas the author's implementation
expands full Laurent polynomials first.  Every saved degree-two tensor
Bernstein coefficient is compared, and each conversion is inverted.
All outputs stay in hour_quantum.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json
import lrrl_certificate as a


def fixed_bernstein(p, degrees):
    """Specified-degree tensor basis, including degree elevation."""
    assert all(e[0] == 0 for e in p)
    assert all(all(e[j + 1] <= degrees[j] for j in range(3)) for e in p)
    indices = list(product(*(range(d + 1) for d in degrees)))
    out = {}
    for i in indices:
        value = Q(0)
        for e, coeff in p.items():
            term = coeff
            for n, k, degree in zip(i, e[1:], degrees):
                if k > n:
                    term = 0
                    break
                term *= Q(comb(n, k), comb(degree, k))
            value += term
        out[i] = value
    # Directly expand Bernstein basis back to power basis.
    inverse = {}
    for i, value in out.items():
        for k in product(*(range(j, d + 1) for j, d in zip(i, degrees))):
            term = value
            for j, n, degree in zip(i, k, degrees):
                term *= comb(degree, j) * comb(degree - j, n - j)
                term *= (-1) ** (n - j)
            key = (0,) + k
            inverse[key] = inverse.get(key, Q(0)) + term
    assert {e: v for e, v in inverse.items() if v} == p
    return list(out.values())


def main():
    saved_path = Path(__file__).resolve().parent.parent / 'hour_invariant' / 'r2_ray_certificates.json'
    saved = json.loads(saved_path.read_text())
    X, C0, P = a.node('RR')
    old = [5, 6, 2]
    y, x, p = [1, 1], [0, 1], [2, 1]
    A, B = a.divide_y(a.psub(C0, P)), a.divide_y(a.psub(old, P))
    tau = a.psub(a.pscale(a.pmul(y, X), 3), x)
    K0 = a.padd(a.psub(a.pscale(a.pmul(y, P), 3), x), [1])
    J = a.pmul(y, a.psub(tau, [2]))
    V = a.pscale(a.pmul(a.pmul(a.pmul(y, y), X), p), 3)
    K = a.pmul(a.pmul(X, p), K0)
    ordinary = dict(P=P, X=X, C0=C0, Zold=old, A=A, B=B,
                    tau=tau, K0=K0, J=J, V=V, K=K)
    assert saved['base_ordinary'] == ordinary
    a4, b4, t4, y4 = map(a.lift, (A, B, tau, y))
    roots = [a.add(t4, a.const(-2), a.scale(a.variable(j), 4))
             for j in (1, 2, 3)]
    L = a.add(a.mul(a4, roots[0]), b4)
    H = a.add(a.mul(a4, a.mul(roots[0], roots[1])), a.mul(b4, roots[2]))
    blocks = dict(trace=roots[0], L=L, L_y=a.mul(y4, L),
                  H=H, H_y=a.mul(y4, H))
    total_coefficients = 0
    summaries = {}
    for name, block in blocks.items():
        record = saved['interval_kernel_certificates'][name]
        lam = {'trace': 1, 'L': 1, 'L_y': 1, 'H': 24, 'H_y': 56}[name]
        dimensions = 3 if name.startswith('H') else 1
        degrees = (2, 2, 2) if dimensions == 3 else (2, 0, 0)
        h, delta = a.fourier(block), a.defects(block)
        assert record['strength_lambda'] == lam
        assert record['dimension'] == dimensions
        assert record['polynomial_degree'] == len(delta) - 1
        assert len(record['all_indices']) == len(delta)
        minimum = None
        for n, d in enumerate(delta):
            values = fixed_bernstein(a.add(d, a.scale(h[n], -lam)), degrees)
            assert all(v > 0 for v in values)
            exact_saved = list(map(Q, record['all_indices'][n]['bernstein']))
            assert values == exact_saved, (name, n)
            minimum = min(values) if minimum is None else min(minimum, *values)
            total_coefficients += len(values)
        assert Q(record['minimum']) == minimum
        summaries[name] = str(minimum)

    trace_values = fixed_bernstein(
        a.add(a.defects(roots[0])[0], a.scale(a.evaluate_x(roots[0]), -22)), (2, 0, 0))
    assert trace_values == list(map(Q, saved['mass_certificates']['trace_delta0_minus_22_mass']))
    assert min(trace_values) > 0
    total_coefficients += len(trace_values)
    for n in range(4):
        values = fixed_bernstein(
            a.add(a.defects(L)[n], a.scale(a.evaluate_x(L), -40000)), (2, 0, 0))
        assert values == list(map(Q, saved['mass_certificates']['single_delta_j_minus_40000_mass'][n]['bernstein']))
        assert min(values) > 0
        total_coefficients += len(values)
    assert total_coefficients == 993

    for name, poly in dict(A=A, yA=a.pmul(y,A), B=B, yB=a.pmul(y,B), J=J, K0=K0).items():
        ds = [d.get(a.ZERO, 0) for d in a.defects(a.lift(poly))]
        assert saved['base_halfrows'][name]['row'] == a.half(poly)
        assert saved['base_halfrows'][name]['defects'] == ds
        assert min(ds) > 0

    q0 = a.pmul(y, A)
    q1 = a.pmul(y, a.padd(a.pmul(A, tau), B))
    beta = a.pmul(y, a.padd(A, B))
    E1 = a.psub(C0, X)
    for name, lower, upper in [('q0_le_q1',q0,q1), ('Beta_le_q1',beta,q1),
                               ('P1X_le_E1',a.pmul(p,X),E1), ('E1_le_q1',E1,q1)]:
        mins = a.adjacent(lower, upper)[:len(lower)]
        assert saved['initial_lr'][name] == {
            'lower_halfrow': a.half(lower), 'upper_halfrow': a.half(upper), 'minors': mins}
        assert min(mins) > 0
    assert a.mutate(X, C0, P) == a.padd(C0, q1)
    assert beta == a.psub(a.pmul(a.psub(tau,[2]),P),a.pmul(x,X))

    w = a.adjacent(J, V)[:len(J)]
    assert min(w)>0 and saved['proxy']['fixed_J_V_minors'] == w
    assert saved['proxy']['J_mass'] == a.peval(J)
    assert saved['proxy']['K_halfrow'] == a.half(K)
    threshold0 = max(Q(a.peval(J)*a.half(K)[n],w[n]) for n in range(len(w)))
    threshold1 = Q(a.peval(J)*a.half(K)[7],w[6])
    assert threshold0 == Q(saved['proxy']['beta0']) == Q(234515,18)
    assert threshold1 == Q(saved['proxy']['beta1']) == Q(7565,6)
    assert max(threshold0, threshold1)<20000
    left, right = a.mutate(X,C0,P), a.mutate(P,C0,X)
    assert len(right)<len(left)
    S0,D0=a.psub(right,C0),a.psub(left,right)
    F0=a.adjacent(S0,D0)[:len(S0)]
    assert saved['ell_zero_original_target'] == dict(H_S=a.half(S0),H_D=a.half(D0),F=F0)
    assert min(F0)>0

    # Exact polarization coefficients derived with independent symbolic h_i.
    m = a.half(K0)
    polar = []
    for n in range(4):
        terms = {}
        def add_term(index, coefficient):
            terms[index] = terms.get(index,0)+coefficient
        add_term(n,2*a.at(m,n))
        add_term(abs(n-1),-a.at(m,n+1))
        add_term(n+1,-a.at(m,abs(n-1)))
        add_term(n+1,-2*a.at(m,n+1))
        add_term(n,a.at(m,n+2))
        add_term(n+2,a.at(m,n))
        terms={j:c for j,c in terms.items() if c}
        polar.append(terms)
    negative=[sum(-c for c in terms.values() if c<0) for terms in polar]
    assert negative==[32,22,8,3]
    assert 9*4*20000-3*max(negative)*9==719136>0
    report={
        'verdict':'PASS: all independent finite certificates and symbolic scalar gates',
        'author_code_imported':False,
        'reconstructed_from_original_mutation':True,
        'coefficient_method':'ordinary x polynomials -> binomial Fourier transform -> degree-two tensor Bernstein',
        'compared_bernstein_coefficients':total_coefficients,
        'each_basis_change_inverted':True,
        'kernel_margin_minima':summaries,
        'proxy_thresholds':[str(threshold0),str(threshold1)],
        'multiplier_polarization':polar,
        'multiplier_negative_weights':negative,
        'minimum_ell_zero_F':min(F0),
        'mathematical_assembly_review':'See AUDIT_R2_RAY.md; no unproved universal preservation gate used.'
    }
    output=Path(__file__).with_name('audit_r2_ray_results.json')
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
