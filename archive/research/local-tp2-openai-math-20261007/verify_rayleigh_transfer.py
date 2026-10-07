#!/usr/bin/env python3
"""Exact, dependency-free certificates for the Family 231 transfer audit.

This verifies finite algebra in the accompanying note. The all-word statement
is proved there by induction at x = -1; no bounded tree scan replaces it.
"""
from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, t):
    return trim([t * v for v in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    p = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            p[i + j] += u * v
    return trim(p)


def power(a, n):
    r = [1]
    for _ in range(n):
        r = mul(r, a)
    return r


def evaluate(p, t):
    r = 0
    for v in reversed(p):
        r = r * t + v
    return r


def H(p):
    return [sum(p[j] * comb(j, (j - n) // 2)
                for j in range(n, len(p), 2)) for n in range(len(p))]


def half_minor(a, b, n):
    get = lambda p, i: p[i] if i < len(p) else 0
    return get(a, n) * get(b, n + 1) - get(a, n + 1) * get(b, n)


def shifted_laurent(p):
    d = len(p) - 1
    row = H(p)
    return [row[abs(k - d)] for k in range(2 * d + 1)]


def remainder(p, divisor):
    p = list(map(Fraction, p))
    divisor = list(map(Fraction, divisor))
    while len(p) >= len(divisor) and p != [0]:
        k = len(p) - len(divisor)
        t = p[-1] / divisor[-1]
        for j, c in enumerate(divisor):
            p[k + j] -= t * c
        p = trim(p)
    return p


def root_pair():
    x, y = [0, 1], [1, 1]
    A, C, B = [1], [5, 6, 2], [2, 1]
    L = sub(sub(scale(mul(mul(y, A), C), 3), mul(x, add(A, C))), B)
    R = sub(sub(scale(mul(mul(y, C), B), 3), mul(x, add(C, B))), A)
    U, V = sorted([L, R], key=len)
    return sub(U, C), sub(V, U)


def main():
    x, y = [0, 1], [1, 1]
    S, D = root_pair()
    assert S == [8, 20, 16, 4]
    assert D == [16, 48, 56, 30, 6]
    assert S == scale(mul(power(y, 2), [2, 1]), 4)
    assert D == scale(mul(mul(y, [2, 1]), add(scale(power(y, 2), 3), [1])), 2)
    hs, hd = H(S), H(D)
    assert hs == [40, 32, 16, 4]
    assert hd == [164, 138, 80, 30, 6]
    F = [half_minor(hs, hd, n) for n in range(len(hs))]
    assert F == [272, 352, 160, 24]
    newton_defect = hs[1] ** 2 - 3 * hs[0] * hs[2]
    assert newton_defect == -896
    a, b, c, d = hs[::-1]
    discriminant = b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d
    assert discriminant == -134144
    for p in (S, D):
        assert evaluate(p, -1) == 0
        assert remainder(shifted_laurent(p), [1, 1, 1]) == [0]

    h1, h2 = H(y), H(power(y, 2))
    h3, h4 = H(power(y, 3)), H(power(y, 4))
    assert h1 == [1, 1] and h2 == [3, 2, 1]
    assert half_minor(h1, h2, 0) == -1
    assert h3 == [7, 6, 3, 1] and h4 == [19, 16, 10, 4, 1]
    counterexample = [half_minor(h3, h4, n) for n in range(len(h3))]
    assert counterexample == [-2, 12, 2, 1]
    signed_probability_minor = Fraction(-2, 3**7)
    absolute_probability_minor = 2 * signed_probability_minor

    # A positive 2-bit law with positive covariance but the same uniform
    # 1/2 response bound: unnormalized generating polynomial 2+z+w+2zw.
    aa, bb, cc, dd = map(Fraction, (2, 1, 1, 2))
    z = aa + bb + cc + dd
    p1, p2 = (bb + dd) / z, (cc + dd) / z
    covariance = dd / z - p1 * p2
    variance = p1 * (1 - p1)
    assert covariance == Fraction(1, 12)
    assert variance + abs(covariance) == Fraction(1, 3)
    assert bb * cc - aa * dd == -3

    report = {
        "scope": "Exact obstruction/bridge audit; full canonical Local TP2 remains OPEN",
        "root": {"S": S, "D": D, "H_S": hs, "H_D": hd,
                 "F": F, "newton_degree3_defect": newton_defect,
                 "folded_cubic_discriminant": discriminant,
                 "shifted_laurent_cyclotomic_factor": [1, 1, 1]},
        "strongly_rayleigh_signed_count_counterexample": {
            "generator": "3^(-m) product_i (1+u_i+v_i); statistic sum_i(U_i-V_i)",
            "m_1_vs_2_central_minor": -1,
            "H_y3": h3, "H_y4": h4, "minors_3_vs_4": counterexample,
            "normalized_signed_central_minor": str(signed_probability_minor),
            "normalized_absolute_central_minor": str(absolute_probability_minor)},
        "response_bound_not_sign_certificate": {
            "generator": "2+z+w+2zw", "rayleigh_difference": -3,
            "covariance_at_unit_fields": str(covariance),
            "absolute_row_sum_at_unit_fields": str(variance + abs(covariance))},
        "all_word_proof": "Induction: A(-1)=C(-1)=B(-1)=1; mutation = A+C-B at x=-1. Thus every gap is divisible by x+1."
    }
    target = Path(__file__).with_name("rayleigh_transfer_results.json")
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
