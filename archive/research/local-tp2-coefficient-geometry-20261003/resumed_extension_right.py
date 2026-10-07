"""Exact continuum certificates for the all-right Local TP2 proof.

No depth extrapolation is used: the parameters cover every root block.
Run with standard Python; output is exact rational JSON.
"""
from fractions import Fraction as F
import json
import continuation_prefix as p

x, u, v, w = [p.variable(i) for i in range(4)]
y = p.add(x, p.const(1))
P = p.add(x, p.const(2))
t = p.add(p.scale(p.mul(x, x), 3), p.scale(x, 8), p.const(6))
e = p.mul(y, P)
A = p.add(t, p.const(-2))
B = p.scale(p.mul(y, p.mul(P, P)), 3)
Q = p.add(p.mul(t, t), p.scale(p.mul(u, t), 2), p.scale(v, -4))
G = p.add(t, w)


def mass(f):
    return p.add(*[{(0,) + key[1:]: value * 2**key[0]}
                   for key, value in f.items()])


def cert(f):
    degrees, coefficients = p.bernstein(f)
    lower = min(coefficients.values())
    assert lower > 0, lower
    return {
        'degrees': degrees,
        'strict_lower_bound': str(lower),
        'power_coefficients': {','.join(map(str, key[1:])): str(value)
                               for key, value in sorted(f.items())},
        'bernstein_coefficients': {key: str(value)
                                   for key, value in coefficients.items()},
    }


def main():
    answer = {'quartic_growth': cert(p.add(p.defects(Q)[0], p.scale(mass(Q), -4)))}
    for name, R in [('quadratic_in_t', Q), ('linear_in_t', G)]:
        a = p.fourier(p.mul(p.mul(A, e), R))
        b = p.fourier(p.mul(p.mul(B, e), R))
        margins = []
        for n, k_n in enumerate([20, 15, 6, 1]):
            minor = p.add(p.mul(a[n], b[n+1]), p.scale(p.mul(a[n+1], b[n]), -1))
            margins.append(cert(p.add(minor, p.scale(mass(R), -384*k_n))))
        answer[name] = margins
    print(json.dumps(answer, indent=2))


if __name__ == '__main__':
    main()
