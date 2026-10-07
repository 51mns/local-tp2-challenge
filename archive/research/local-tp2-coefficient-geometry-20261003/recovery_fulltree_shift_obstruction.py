#!/usr/bin/env python3
"""Exact proof certificates for the uniform affine-power obstruction.

Standalone integer arithmetic; no finite scan is used as an all-shift
argument. Each symbolic coefficient is represented as an integer array.
"""
from fractions import Fraction
from math import comb
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0)
                 + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, k):
    return trim([k * x for x in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def child(retained, center, replaced):
    return sub(sub(scale(mul([1, 1], mul(retained, center)), 3),
                   mul([0, 1], add(retained, center))), replaced)


def shift(p, a):
    """Return the coefficient row of p(u-a)."""
    return [sum(p[j] * comb(j, i) * (-a) ** (j - i)
                for j in range(i, len(p))) for i in range(len(p))]


def symbolic_shift_coefficient(p, i):
    """Return [u^i]p(u-a), as a polynomial in the symbol a."""
    return trim([p[j] * comb(j, i) * (-1) ** (j - i)
                 for j in range(i, len(p))])


def main():
    x, y, center = [1], [2, 1], [5, 6, 2]
    short = child(x, center, y)
    long = child(y, center, x)
    S, D = sub(short, center), sub(long, short)
    assert S == [8, 20, 16, 4]
    assert S == scale(mul(mul([1, 1], [1, 1]), [2, 1]), 4)
    assert D == [16, 48, 56, 30, 6]
    root_u2 = symbolic_shift_coefficient(S, 2)
    assert root_u2 == [16, -12]

    # Symbolic a(2a) - (a^2+2) = a^2-2.
    kernel_minor = sub(mul([0, 1], [0, 2]), [2, 0, 1])
    assert kernel_minor == [-2, 0, 1]
    assert Fraction(2) > Fraction(4, 3) ** 2

    root_sy, root_dy = shift(S, 1), shift(D, 1)
    assert root_sy == [0, 0, 4, 4]
    assert root_dy == [0, 2, 2, 6, 6]
    root_y_minor = root_sy[1] * root_dy[2] - root_sy[2] * root_dy[1]
    assert root_y_minor == -8

    # First left state is (1, short, center).
    next_short = child(x, short, center)
    left_S = sub(next_short, short)
    assert left_S == [21, 71, 86, 44, 8]
    assert shift(left_S, 1) == [0, -1, 2, 12, 8]

    return {
        "all_shift_obstruction": "proved by incompatible a >= sqrt(2), a <= 4/3",
        "symbolic_kernel_minor_in_a": kernel_minor,
        "root_u_squared_coefficient_in_a": root_u2,
        "root_y_coefficient_minor_degrees_1_2": root_y_minor,
        "first_left_short_gap_y_coefficients": shift(left_S, 1),
        "full_tree_Local_TP2_proved": False,
        "canonical_Local_TP2_counterexample": False,
        "verification": "PASS"
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
