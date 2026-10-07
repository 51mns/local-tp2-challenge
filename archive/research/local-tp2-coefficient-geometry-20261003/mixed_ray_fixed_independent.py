"""Independent direct-Laurent audit of fixed mixed-ray proof tables.

No producer, Fourier-transform helper, or prior polynomial module is imported.
Continuum certificates and canonical finite bases are audited separately.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def plus(*polynomials):
    result = {}
    for poly in polynomials:
        for index, value in poly.items():
            result[index] = result.get(index, 0) + value
    return {index: value for index, value in result.items() if value}


def times(a, b):
    result = {}
    for i, v in a.items():
        for j, w in b.items():
            result[i+j] = result.get(i+j, 0) + v*w
    return {index: value for index, value in result.items() if value}


def scale(a, value):
    return {index: coefficient*value for index, coefficient in a.items()
            if coefficient*value}


def row(poly):
    assert all(poly.get(-n, 0) == value for n, value in poly.items())
    return [poly.get(n, 0) for n in range(max(poly)+1)]


def minors(lower, upper):
    return [lower.get(n, 0)*upper.get(n+1, 0)
            -lower.get(n+1, 0)*upper.get(n, 0)
            for n in range(max(lower)+1)]


def main():
    one = {0: 1}
    x = {-1: 1, 1: 1}
    y = plus(x, one)
    P1 = plus(x, {0: 2})
    P = plus(scale(times(x, x), 2), scale(x, 6), {0: 5})
    t = plus(scale(times(y, P), 3), scale(x, -1))
    w = scale(times(P1, plus(scale(x, 2), {0: 3})), 2)
    q0L = times(y, w)
    q1L = times(y, plus(times(w, t), one))
    q0R = times(y, plus(t, w))
    q1R = times(y, plus(times(t, t), scale(one, -1), times(w, t)))
    C0L = plus(one, q0L)
    C0R = plus(P1, q0R)

    def mutation(a, c, b):
        return plus(scale(times(times(y, a), c), 3),
                    scale(times(x, plus(a, c)), -1), scale(b, -1))

    # Seed identities from the original canonical mutation, not from a table.
    assert mutation(one, P, P1) == C0L
    assert mutation(P1, P, one) == C0R
    assert plus(times(t, C0L), scale(one, -1), scale(times(x, P), -1),
                scale(C0L, -1)) == q1L
    assert plus(times(t, C0R), scale(P1, -1), scale(times(x, P), -1),
                scale(C0R, -1)) == q1R

    B0 = times(P1, P)
    E1L = plus(C0L, scale(P, -1))
    E1R = plus(C0R, scale(P, -1))
    A = plus(t, {0: -2})
    b = times(y, plus(w, one))
    assert b == plus(A, scale(times(x, P), -1))
    B = scale(times(times(y, P), P1), 3)
    K = scale(times(P, times(P1, P1)), 2)
    Ay, By = times(A, y), times(B, y)

    expected_rows = {
        'B0': (B0, [30, 23, 10, 2]),
        'b': (b, [49, 39, 18, 4]),
        'Ay': (Ay, [161, 135, 80, 30, 6]),
        'By': (By, [606, 522, 330, 147, 42, 6]),
        'K': (K, [212, 172, 90, 28, 4]),
    }
    for name, (polynomial, expected) in expected_rows.items():
        assert row(polynomial) == expected, (name, row(polynomial), expected)
    assert sum(Ay.values()) == 663
    assert sum(t.values()) == 223 and sum(w.values()) == 56

    expected_minors = {
        'LR_q0_q1': (q0L, q1L, [32922, 52734, 23880, 3440]),
        'RL_q0_q1': (q0R, q1R, [492854, 857178, 477196, 109472, 10224]),
        'LR_B0_q0': (B0, q0L, [36, 34, 4, 0]),
        'LR_B0_E1': (B0, E1L, [40, 48, 8, 0]),
        'RL_B0_q0': (B0, q0R, [397, 504, 144, 12]),
        'RL_B0_E1': (B0, E1R, [408, 508, 148, 12]),
        'LR_b_q1': (b, q1L, [31996, 57348, 23880, 3440]),
        'RL_b_q0': (b, q0R, [346, 672, 220, 24]),
        'Ay_By': (Ay, By, [2232, 2790, 1860, 378, 36]),
    }
    for name, (lower, upper, expected) in expected_minors.items():
        assert minors(lower, upper) == expected, (name, minors(lower, upper), expected)
        assert min(expected) >= 0
    m = minors(Ay, By)
    residual = [75*a-663*k for a, k in zip(m, row(K))]
    assert residual == [26844, 95214, 79830, 9786, 48]
    assert all(value > 0 for value in residual)

    # Exact algebra of the mixture/root-count scalar lower bounds.
    assert F(40)*F(4, 5)**2/F(2) == F(64, 5)
    assert F(100)*F(4, 5)**2/F(2) == F(32)
    lowerL = lambda k: F(64, 5*k)*90**((k-2)//2)
    lowerR = lambda k: F(32, k)*90**((k-2)//2)
    initial_bounds = {str(k): [str(lowerL(k)), str(lowerR(k))] for k in (4, 5)}
    assert all(lowerL(k) > 75 and lowerR(k) > 75 for k in (4, 5))
    # For all k>=4, the same-parity ratio is 90*k/(k+2)>1:
    # subtracting one leaves (89*k-2)/(k+2), positive on that domain.
    assert 89*4-2 > 0
    # The summand-mass comparison is strictly stronger than the used 1/2.
    assert F(56, 57) > F(1, 2) and F(278, 279) > F(1, 2)

    result = {
        'status': 'PASS',
        'method': 'standalone exact direct Laurent arithmetic',
        'fixed_rows_verified': len(expected_rows),
        'fixed_adjacent_minors_verified': sum(len(v[2]) for v in expected_minors.values()),
        'fixed_minor_tables': {name: values[2] for name, values in expected_minors.items()},
        'strict_remainder_margins': residual,
        'scalar_bounds_at_k4_k5': initial_bounds,
        'all_k_argument': '90*k/(k+2)>1 for k>=4, separately on each parity',
        'scope': 'fixed tables and scalar bound; continuum and canonical bases separately audited',
    }
    Path('mixed_ray_fixed_independent.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
