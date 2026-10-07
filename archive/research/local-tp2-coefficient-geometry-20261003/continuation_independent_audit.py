"""Independent exact audit: direct Laurent multiplication and Bernstein reconstruction.

Does not import continuation_ray.py or its Fourier-transform implementation.
"""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


def plus(*ps):
    out = {}
    for p in ps:
        for exp, coeff in p.items():
            out[exp] = out.get(exp, F(0)) + coeff
    return {exp: coeff for exp, coeff in out.items() if coeff}


def times(a, b):
    out = {}
    for ia, ca in a.items():
        for ib, cb in b.items():
            e = tuple(x + y for x, y in zip(ia, ib))
            out[e] = out.get(e, F(0)) + ca * cb
    return {exp: coeff for exp, coeff in out.items() if coeff}


def scalar(p, a):
    return {exp: a * coeff for exp, coeff in p.items() if a * coeff}


def power(p, n):
    one = {(0,) * len(next(iter(p))): F(1)}
    out = one
    for _ in range(n):
        out = times(out, p)
    return out


def main():
    # Laurent powers q can be negative. Other exponents are u,v.
    one = {(0, 0, 0): F(1)}
    x = {(-1, 0, 0): F(1), (1, 0, 0): F(1)}
    u = {(0, 1, 0): F(1)}
    v = {(0, 0, 1): F(1)}
    y = plus(x, one)
    z = plus(x, scalar(one, F(3, 2)))
    fc = plus(times(x, x), scalar(x, 3), scalar(one, F(5, 4)), u)
    fd = plus(times(x, x), scalar(x, 3), scalar(one, F(5, 4)), v)
    blocks = {
        "B0_y_z": times(y, z),
        "B1_y_fc": times(y, fc),
        "B2_fc_fd": times(fc, fd),
        "B3_y_fc_fd": times(y, times(fc, fd)),
        "B4_y_z_fc": times(y, times(z, fc)),
    }
    certificates = json.loads(Path("continuation_ray_certificates.json").read_text())
    count = 0
    minima = {}
    for name, laurent in blocks.items():
        degree = max(exp[0] for exp in laurent)
        assert len(certificates[name]) == degree + 1
        h = {
            n: {(a, b): val for (qn, a, b), val in laurent.items() if qn == n}
            for n in range(-degree - 2, degree + 3)
        }
        delta = {
            n: plus(times(h[n], h[n]), scalar(times(h[n - 1], h[n + 1]), -1))
            for n in range(0, degree + 2)
        }
        minima[name] = []
        for n, item in enumerate(certificates[name]):
            actual = plus(delta[n], scalar(delta[n + 1], -1))
            recorded = {tuple(map(int, key.split(','))): F(value)
                        for key, value in item['power_coefficients_uv'].items()}
            assert actual == recorded, (name, n, 'power polynomial')
            bc = [[F(value) for value in row] for row in item['bernstein_coefficients']]
            ru, rv = len(bc) - 1, len(bc[0]) - 1
            assert all(len(row) == rv + 1 for row in bc)
            # Reconstruct power coefficients by expanding every Bernstein basis.
            expanded = {}
            for i, row in enumerate(bc):
                for j, coefficient in enumerate(row):
                    for a in range(ru - i + 1):
                        for b in range(rv - j + 1):
                            key = i + a, j + b
                            val = (coefficient * comb(ru, i) * comb(rv, j)
                                   * comb(ru - i, a) * comb(rv - j, b)
                                   * (-1) ** (a + b))
                            expanded[key] = expanded.get(key, F(0)) + val
            expanded = {e: val for e, val in expanded.items() if val}
            assert actual == expanded, (name, n, 'Bernstein reconstruction')
            lower = min(value for row in bc for value in row)
            assert lower > 0 and lower == F(item['strict_lower_bound'])
            minima[name].append(str(lower))
            count += 1

    # New shifted-U building blocks, checked as exact parameter polynomials.
    fc_large = plus(times(x, x), scalar(x, 3), scalar(one, 2), scalar(u, F(1, 4)))
    fc_exception = plus(times(x, x), scalar(x, 3), scalar(one, F(7, 4)))
    new_blocks = {
        'z': (z, [{(0, 0): F(1, 4)}, {(0, 0): F(1)}]),
        'fc_2_plus_u_over_4': (fc_large, [
            {(0, 0): F(2), (1, 0): F(9, 4), (2, 0): F(1, 16)},
            {(0, 0): F(4), (1, 0): F(-1, 4)},
            {(0, 0): F(1)},
        ]),
        'U3_over_8': (times(z, fc_exception), [
            {(0, 0): F(1045, 64)}, {(0, 0): F(89, 4)},
            {(0, 0): F(10)}, {(0, 0): F(1)},
        ]),
    }
    extra_checks = 0
    for name, (laurent, expected) in new_blocks.items():
        degree = max(exp[0] for exp in laurent)
        h = {n: {(a, b): val for (qn, a, b), val in laurent.items() if qn == n}
             for n in range(-degree - 2, degree + 3)}
        defects = {n: plus(times(h[n], h[n]), scalar(times(h[n - 1], h[n + 1]), -1))
                   for n in range(degree + 2)}
        assert len(expected) == degree + 1
        for n, value in enumerate(expected):
            assert plus(defects[n], scalar(defects[n+1], -1)) == value, (name, n)
            extra_checks += 1

    # Additional exact recurrence/CD checks, illustrative only.
    p = [y, times(y, scalar(z, 2))]
    for m in range(1, 12):
        p.append(plus(times(scalar(z, 2), p[-1]), scalar(p[-2], -1)))
    row = lambda poly, n: poly.get((n, 0, 0), F(0))
    defect = lambda poly, n: row(poly, n)**2 - row(poly, n-1)*row(poly, n+1)
    deldiff = lambda poly, n: defect(poly, n) - defect(poly, n+1)
    checked = 0
    for m in range(1, 12):
        for n in range(m + 2):
            lhs = row(p[m+1], n+1)*row(p[m], n)-row(p[m+1], n)*row(p[m], n+1)
            rhs = 2 * sum(deldiff(p[j], n) for j in range(m + 1))
            bound = 24 if n == 0 else 2 if n == 1 else 2 * 4**(n-1)
            assert lhs == rhs and lhs >= bound, (m, n)
            checked += 1
    print(json.dumps({'certificate_defects_verified': count,
                      'shifted_U_block_defects_verified': extra_checks,
                      'independent_cd_checks': checked,
                      'exact_minima': minima}, indent=2))


if __name__ == '__main__':
    main()
