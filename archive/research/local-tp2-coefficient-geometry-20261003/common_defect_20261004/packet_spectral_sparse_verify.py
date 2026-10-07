#!/usr/bin/env python3
"""Exact targeted algebra/index checks for packet_spectral_sparse_audit.md.

These are implementation checks, not substitutes for the analytic all-index
proof. No canonical state scan, no external dependencies, no old-folder writes.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c * v for v in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def cb_chain(d, base_degree, N, n):
    assert base_degree >= d >= 1
    assert 0 <= n <= base_degree + (N - 1) * d
    out, current = [], n
    for stage in range(N - 1, 0, -1):
        prior_degree = base_degree + (stage - 1) * d
        previous = max(d, min(current, prior_degree))
        assert 0 <= previous <= prior_degree
        assert abs(previous - current) <= d
        out.append(dict(output=current, previous=previous,
                        prior_degree=prior_degree,
                        factor='central 2 lc^2' if current == 0
                        else 'Delta_' + str(abs(previous - current))))
        current = previous
    assert 0 <= current <= base_degree
    return dict(d=d, base_degree=base_degree, N=N, output=n,
                chain=out, selected_base_index=current)


def main():
    U = [[1], [0, 1]]
    for _ in range(2, 7):
        U.append(sub(mul([0, 1], U[-1]), U[-2]))
    R, accum = [], [0]
    for p in U:
        accum = add(accum, p)
        R.append(accum)
    checks = []
    for m in [1, 2, 3, 4, 5, 6]:
        if m % 2:
            h = (m - 1) // 2
            prior = U[h - 1] if h else [0]
            assert R[m] == mul(U[h], add(U[h + 1], U[h]))
            assert mul(R[m - 1], add(U[h + 1], U[h])) == (
                mul(R[m], add(U[h], prior)))
            poles = h + 1
        else:
            h = m // 2
            assert R[m] == mul(U[h], add(U[h], U[h - 1]))
            assert mul(R[m - 1], U[h]) == mul(R[m], U[h - 1])
            poles = h
        checks.append(dict(m=m, active_poles=poles,
                           strict_anchor=(-1 if m == 1 else 0) if poles == 1 else None,
                           multiple_distinct_poles=poles >= 2,
                           core_MP0_strict=m >= 2, optional_MP01_strict=True))

    # Raw and smoothed degrees; zero, low, interior, boundary, terminal.
    chains = [cb_chain(2, 2, 4, n) for n in [0, 1, 4, 7, 8]]
    chains += [cb_chain(2, 3, 4, n) for n in [0, 1, 4, 8, 9]]
    chains += [cb_chain(3, 5, 2, n) for n in [0, 1, 5, 7, 8]]
    # An admissible bad-base quadratic vanishes at exactly one interior pole.
    samples = [(-1, [1, -2, 1]), (-1, [F(1, 4), -1, 1])]
    zeros = []
    for other_pole, q in samples:
        def ev(r):
            return sum(a * r ** i for i, a in enumerate(q))
        assert ev(0) > 0 and ev(other_pole) > 0
        zero = F(1) if q == [1, -2, 1] else F(1, 2)
        if other_pole == zero:
            other_pole = -1
        assert ev(zero) == 0 and ev(other_pole) > 0
        zeros.append(dict(quadratic=q, unique_interior_zero=zero,
                          other_pole=other_pole, other_value=ev(other_pole)))
    result = dict(status='PASS', arithmetic='Exact Python integers/Fractions',
                  scope='Targeted prefix identities and degree-only CB index checks; arbitrary-state proof in audit note.',
                  prefix_checks=checks, cb_index_chains=chains,
                  zero_polynomial_examples=zeros,
                  paired_witness_CB_bounds=dict(raw_central=20000,
                      smoothed_12=351*261,
                      smoothed_02_terms=[551*361,351*380,390*190],
                      smoothed_02_total=551*361+351*380+390*190),
                  excluded_claim='N=1 arbitrary rho strictness; full child trace/single/mixed/proxy preservation.')
    def enc(v):
        if isinstance(v, F):
            return str(v)
        raise TypeError(type(v).__name__)
    path = Path(__file__).with_name('packet_spectral_sparse_results.json')
    path.write_text(json.dumps(result, indent=2, default=enc) + '\n')
    print(json.dumps(dict(status='PASS', prefix_checks=len(checks),
                         cb_index_checks=len(chains), saved=path.name), indent=2))


if __name__ == '__main__':
    main()
