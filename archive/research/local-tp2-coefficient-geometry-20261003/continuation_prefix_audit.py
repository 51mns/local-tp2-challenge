"""Independent direct-Laurent and Bernstein audit of prefix-cone certificates."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            k = tuple(x+y for x, y in zip(i, j))
            out[k] = out.get(k, F(0)) + a*b
    return {k: v for k, v in out.items() if v}


def main():
    # The first coordinate is a Laurent exponent, so no Fourier binomial formula
    # is imported or reused from the certificate-producing implementation.
    one = {(0, 0, 0, 0, 0): F(1)}
    x = {(-1, 0, 0, 0, 0): F(1), (1, 0, 0, 0, 0): F(1)}
    u = {(0, 1, 0, 0, 0): F(1)}
    v = {(0, 0, 1, 0, 0): F(1)}
    w = {(0, 0, 0, 1, 0): F(1)}
    z = {(0, 0, 0, 0, 1): F(1)}
    f = add(mul(x, x), mul(add(scale(one, 3), u), x),
            scale(one, F(5, 4)), scale(u, F(5, 2)), v)
    g = add(mul(x, x), mul(add(scale(one, 3), w), x),
            scale(one, F(5, 4)), scale(w, F(5, 2)), z)
    middle = add(x, scale(one, F(3, 2)), scale(w, F(1, 2)))
    blocks = {
        'pair_of_general_pairs': mul(f, g),
        'middle_times_general_pair': mul(middle, f),
        'isolated_innermost_pair': mul(add(x, one, scale(u, F(1, 2))),
                                       add(x, scale(one, F(3, 2)), v)),
        'middle_linear': middle,
    }
    certs = json.loads(Path('continuation_prefix_certificates.json').read_text())
    minima = {}
    checked = 0
    coefficients_checked = 0
    for name, p in blocks.items():
        degree = max(k[0] for k in p)
        h = {n: {k[1:]: a for k, a in p.items() if k[0] == n}
             for n in range(-degree-2, degree+3)}
        defects = {n: add(mul(h[n], h[n]), scale(mul(h[n-1], h[n+1]), -1))
                   for n in range(degree+2)}
        assert len(certs[name]) == degree + 1
        minima[name] = []
        for n, cert in enumerate(certs[name]):
            actual = add(defects[n], scale(defects[n+1], -1))
            recorded = {tuple(map(int, k.split(','))): F(v)
                        for k, v in cert['power_coefficients'].items()}
            assert actual == recorded, (name, n, 'Laurent defect')
            degrees = tuple(cert['degrees'])
            bc = {tuple(map(int, k.split(','))): F(v)
                  for k, v in cert['bernstein_coefficients'].items()}
            assert set(bc) == set(product(*(range(d+1) for d in degrees)))
            expanded = {}
            # Expand all tensor Bernstein basis functions into ordinary powers.
            for indices, value in bc.items():
                for offsets in product(*(range(d-i+1) for d, i in zip(degrees, indices))):
                    coefficient = value
                    for d, i, a in zip(degrees, indices, offsets):
                        coefficient *= comb(d, i)*comb(d-i, a)*(-1)**a
                    key = tuple(i+a for i, a in zip(indices, offsets))
                    expanded[key] = expanded.get(key, F(0)) + coefficient
            expanded = {k: v for k, v in expanded.items() if v}
            assert actual == expanded, (name, n, 'Bernstein reconstruction')
            minimum = min(bc.values())
            assert minimum > 0 and minimum == F(cert['strict_lower_bound'])
            minima[name].append(str(minimum))
            checked += 1
            coefficients_checked += len(bc)

    # Exact polynomial identities supplement (but do not replace) the general
    # root-factorization and trigonometric proof in the accompanying audit.
    recurrence_multiplier = add(scale(x, 2), scale(one, 3))
    us = [one, recurrence_multiplier]
    for n in range(1, 16):
        us.append(add(mul(recurrence_multiplier, us[-1]), scale(us[-2], -1)))
    prefix = {}
    for n in range(17):
        prefix = add(prefix, us[n])
        r = n//2
        expected = mul(us[r], add(us[r], us[r-1] if r else {})) if n%2 == 0 else mul(us[r], add(us[r+1], us[r]))
        assert prefix == expected, ('prefix factorization', n)
    print(json.dumps({'defects_verified': checked,
                      'Bernstein_coefficients_verified': coefficients_checked,
                      'supplementary_prefix_identities': 17,
                      'exact_minima': minima}, indent=2))


if __name__ == '__main__':
    main()
