#!/usr/bin/env python3
"""Exact finite bridge and scalar tail gates for every L^m R^2 seed.

This certifies the full independent parameter cube r,s,c in [-2,2],
not a sample of parameters.  All arithmetic uses Python integers or Fraction.
The mathematical tail m>=54 is given in all_m_mixed_transport.md.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*ps):
    p = [0] * max(map(len, ps))
    for q in ps:
        for i, v in enumerate(q):
            p[i] += v
    return trim(p)


def scale(p, c):
    return trim([c * v for v in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def half(p):
    return [sum(p[j] * comb(j, (j-n)//2) for j in range(n, len(p), 2))
            for n in range(len(p))]


def trace(p):
    return sub(scale(mul([1, 1], p), 3), [0, 1])


# A row entry is a sparse integer polynomial in u,v,w in [0,1].
ZERO = (0, 0, 0)
ONE_U = (1, 0, 0)
ONE_V = (0, 1, 0)
ONE_W = (0, 0, 1)
UV = (1, 1, 0)


def ssum(*ps):
    out = {}
    for p in ps:
        for e, a in p.items():
            out[e] = out.get(e, 0) + a
    return {e: a for e, a in out.items() if a}


def sscale(p, c):
    return {e: c*a for e, a in p.items() if c*a}


def smul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(i+j for i, j in zip(e, f))
            out[g] = out.get(g, 0) + a*b
    return {e: a for e, a in out.items() if a}


def row_from_components(components):
    d = max(len(h) for h in components.values())
    return [{e: h[n] for e, h in components.items() if n < len(h) and h[n]}
            for n in range(d)]


def row_at(h, n):
    n = abs(n)
    return h[n] if n < len(h) else {}


def defect(h, n):
    a, b, c, d = [row_at(h, j) for j in (n-1, n, n+1, n+2)]
    return ssum(smul(b, b), sscale(smul(a, c), -1),
                sscale(smul(c, c), -1), smul(b, d))


def bernstein_scaled(p, axes):
    """Return 2^len(axes) times all tensor Bernstein coefficients.

    The prescribed degree is two on each active axis.  Direct conversion
    uses 2*C(i,k)/C(2,k) = [2,0,0], [2,1,0], [2,2,2].
    The inverse is also checked for each polynomial.
    """
    weights = ((2, 0, 0), (2, 1, 0), (2, 2, 2))
    assert all(all(0 <= k <= 2 for k in e) for e in p)
    assert all(all(e[j] == 0 for j in range(3) if j not in axes) for e in p)
    indices = list(product(range(3), repeat=len(axes)))
    out = []
    for index in indices:
        out.append(sum(a * _prod(weights[i][e[j]] for i, j in zip(index, axes))
                       for e, a in p.items()))

    # Independent expansion of the Bernstein basis into powers, clearing
    # the same common denominator 2^len(axes).
    recovered = {}
    for index, b in zip(indices, out):
        for exponents in product(*(range(i, 3) for i in index)):
            e = [0, 0, 0]
            v = b
            for i, k, axis in zip(index, exponents, axes):
                e[axis] = k
                v *= comb(2, i) * comb(2-i, k-i) * (-1)**(k-i)
            e = tuple(e)
            recovered[e] = recovered.get(e, 0) + v
    recovered = {e: a for e, a in recovered.items() if a}
    assert recovered == sscale(p, 2**len(axes))
    return out


def _prod(values):
    r = 1
    for v in values:
        r *= v
    return r


def trace_strength(m):
    return 18 if m == 0 else 18*4**m - 18*2**m - 11


def certify(row, strength_numerator, axes, normalized_target):
    digest = hashlib.sha256()
    minima = []
    count = 0
    normalized_certificates = 0
    for n in range(len(row)):
        margin = ssum(sscale(defect(row, n), 128),
                      sscale(row[n], -strength_numerator))
        coefficients = bernstein_scaled(margin, axes)
        assert min(coefficients) > 0, (n, min(coefficients))
        minima.append(min(coefficients))
        # The row entry is largest at u=v=w=0: all factors t-r,
        # t-s,t-c decrease coefficientwise as their parameter increases.
        # The certified strength margin therefore gives this independent
        # lower bound for delta(row)/row_n^2 on the whole cube.
        hmax = row[n][ZERO]
        assert min(coefficients)*normalized_target.denominator >= (
            normalized_target.numerator * 128 * 2**len(axes) * hmax**2), n
        normalized_certificates += 1
        for value in coefficients:
            digest.update(str(value).encode())
            digest.update(b'\n')
        count += len(coefficients)
    return {'degree': len(row)-1,
            'strength': str(Q(strength_numerator, 128)),
            'supported_indices': len(row),
            'positive_tensor_bernstein_coefficients': count,
            'scaled_bernstein_denominator': 128 * 2**len(axes),
            'uniform_normalized_defect_lower_bound': str(normalized_target),
            'normalized_finite_certificates': normalized_certificates,
            'minimum_scaled_bernstein_coefficient': min(minima),
            'minima_by_supported_index': minima,
            'sha256_ordered_scaled_coefficients': digest.hexdigest()}


def main():
    u = [[1], [3, 2]]
    for _ in range(1, 54):
        u.append(sub(mul([3, 2], u[-1]), u[-2]))
    T = []
    p = [0]
    for v in u:
        p = add(p, v)
        T.append(p)
    atT = lambda n: T[n] if n >= 0 else [0]
    records = []
    c0, sigma = Q(1, 400000000), Q(59, 100)
    for m in range(54):
        t0 = trace(add([1], mul([1, 1], T[m])))
        aX = add(mul(T[m+1], add(t0, [1])), atT(m-1))
        X = add([1], mul([1, 1], aX))
        t1 = trace(X)
        assert t1 == sub(mul(t0, trace(add([1], mul([1, 1], T[m+1])))), [3, 4, 1])
        A = sub(mul(t0, aX), u[m])
        B = u[m+1]
        assert all(v > 0 for v in A+B+sub(t1, [2]))
        assert len(A)-1 == 3*m+5
        assert len(t1)-1 == 2*m+5
        R = add(t1, [2])
        AR = mul(A, R)
        single_constant = add(AR, B)
        midpoint_constant = add(mul(AR, R), mul(B, R))
        by0 = half(mul([1, 1], B))[0]
        lam_single_num = 9*8**m*trace_strength(m)
        lam_midpoint_num = max(9*8**m*trace_strength(m)**2, 128*8*by0)
        etaL = c0**5*sigma**(5*m+2)/(65536*(m+3)**4)
        etaH = c0**7*sigma**(7*m+3)/(4194304*(m+3)**6)
        record = {'m': m, 'degree_A': len(A)-1, 'degree_t1': len(t1)-1,
                  'B_halfrow_central': half(B)[0], 'yB_halfrow_central': by0,
                  'cases': {}}
        for smooth in (False, True):
            multiplier = [1, 1] if smooth else [1]
            H = lambda p: half(mul(multiplier, p))
            single = row_from_components({ZERO: H(single_constant),
                                          ONE_U: scale(H(A), -4)})
            midpoint = row_from_components({ZERO: H(midpoint_constant),
                                            ONE_U: scale(H(AR), -4),
                                            ONE_V: scale(H(AR), -4),
                                            UV: scale(H(A), 16),
                                            ONE_W: scale(H(B), -4)})
            label = 'y' if smooth else ''
            record['cases'][label+'L'] = certify(single, lam_single_num, (0,), etaL)
            record['cases'][label+'H'] = certify(midpoint, lam_midpoint_num, (0, 1, 2), etaH)
        records.append(record)
        if m % 10 == 0 or m == 53:
            print(json.dumps({'finite_m_complete': m}), flush=True)

    M = 54
    EH = lambda m: c0**7*sigma**(7*m+3)/(524288*(m+3)**6)
    eps = lambda m: Q(20*(2*m+5)**3*(2*m+7), 27**4*6**(4*m+1))
    ratio = lambda m: 6**4*sigma**7*Q((m+3)**6*(2*m+5)**3*(2*m+7),
                                    (m+4)**6*(2*m+7)**3*(2*m+9))
    assert EH(M) >= 12*eps(M)
    assert EH(M-1) < 12*eps(M-1)
    assert ratio(M) > 27
    assert eps(M) < 1
    # Midpoint strength is >= 8 H(yB)_0 by H(yB)_0 <= 3*7^(m+1).
    # Already at m=2, A_m >= 9*4^m, then the strength lower bound is
    # (729/128)*128^m and its ratio against 24*7^(m+1) is 128/7.
    assert trace_strength(2) >= 9*4**2
    assert Q(729, 128)*128**2 > 24*7**3
    trace_normalized_finite = []
    for m in range(21):
        lhs = Q(trace_strength(m), 25*7**(2*m+3))
        rhs = c0**2*sigma**(2*m+1)/(16*(m+3))
        assert lhs > rhs
        trace_normalized_finite.append({'m': m, 'strict_ratio_floor': lhs//rhs})
    result = {
        'status': 'PASS',
        'statement': 'Uniform single/midpoint folded kernels at all L^m R^2 seeds; all real r,s,c in [-2,2]',
        'finite_range': [0, 53],
        'finite_cases': 4*54,
        'total_positive_tensor_bernstein_coefficients': sum(
            c['positive_tensor_bernstein_coefficients'] for r in records for c in r['cases'].values()),
        'total_normalized_finite_certificates': sum(
            c['normalized_finite_certificates'] for r in records for c in r['cases'].values()),
        'trace_normalized_finite_scalar_certificates': trace_normalized_finite,
        'tail_start': M,
        'tail_gate_EH_over_12epsilon': str(EH(M)/(12*eps(M))),
        'tail_gate_consecutive_ratio_at_start': str(ratio(M)),
        'tail_ratio_lower_bound': 27,
        'tail_ratio_monotonicity': 'Every rational factor (m+a)/(m+a+1) increases; see proof note.',
        'records': records,
    }
    destination = Path(__file__).with_name('uniform_mixed_transport_results.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))


if __name__ == '__main__':
    main()
