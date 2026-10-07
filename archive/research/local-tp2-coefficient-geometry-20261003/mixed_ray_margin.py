"""Four exact continuum margin certificates for mixed-ray Local TP2."""
from fractions import Fraction as F
import json
import continuation_prefix as p

x, u, v = [p.variable(i) for i in range(3)]
y = p.add(x, p.const(1))
P1 = p.add(x, p.const(2))
P = p.add(p.scale(p.mul(x, x), 2), p.scale(x, 6), p.const(5))
t = p.add(p.scale(p.mul(y, P), 3), p.scale(x, -1))
w = p.scale(p.mul(P1, p.add(p.scale(x, 2), p.const(3))), 2)
f = p.add(t, p.const(-2), p.scale(u, 4))
Q = p.add(p.mul(t, t), p.scale(p.mul(u, t), 2), p.scale(v, -4))


def mass(poly):
    return p.add(*[{(0,) + key[1:]: value * 2**key[0]}
                   for key, value in poly.items()])


def cert(poly):
    degrees, coefficients = p.bernstein(poly)
    lower = min(coefficients.values())
    assert lower > 0
    return {
        'degrees': degrees,
        'strict_lower_bound': str(lower),
        'power_coefficients': {','.join(map(str, key[1:])): str(value)
                               for key, value in sorted(poly.items())},
        'bernstein_coefficients': {key: str(value)
                                   for key, value in coefficients.items()},
    }


def main():
    blocks = [
        ('single_root', f, F(4, 5)),
        ('balanced_pair', Q, F(90)),
        ('left_right_resolvent', p.add(p.mul(w, f), p.const(1)), F(40)),
        ('right_left_resolvent', p.add(p.mul(p.add(t, w), f), p.const(-1)), F(100)),
    ]
    result = {}
    for name, block, factor in blocks:
        margin = p.add(p.defects(block)[0], p.scale(mass(block), -factor))
        result[name] = {'mass_factor': str(factor), 'certificate': cert(margin)}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
