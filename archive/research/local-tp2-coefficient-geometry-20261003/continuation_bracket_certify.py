"""Exact coefficient-margin certificates for the all-left bracket."""
import continuation_prefix as p
from fractions import Fraction as Q
import json

p.DIM = 6
p.ZERO = (0,) * p.DIM
x, u, v, w, z, t = [p.variable(i) for i in range(p.DIM)]
one = p.const(1)
y = p.add(x, one)
y2 = p.mul(y, y)
x2 = p.mul(x, x)
central = p.add(x, p.const(Q(3, 2)))


def general_pair(a, b):
    return p.add(x2, p.mul(p.add(p.const(3), a), x), p.const(Q(5, 4)), p.scale(a, Q(5, 2)), b)


def eval_two(poly):
    out = {}
    for key, value in poly.items():
        new_key = (0,) + key[1:]
        out = p.add(out, {new_key: value * 2**key[0]})
    return out


def certify(name, poly):
    degrees, coefficients = p.bernstein(poly)
    lower = min(coefficients.values())
    assert lower > 0, (name, lower)
    return {
        'degrees': degrees,
        'strict_lower_bound': str(lower),
        'power_coefficients': {','.join(map(str, k[1:])): str(v) for k, v in sorted(poly.items())},
        'bernstein_coefficients': {k: str(v) for k, v in coefficients.items()},
    }


def margin_for_residue(residue):
    degree = max(k[0] for k in residue)
    base = p.mul(y2, residue)
    return degree, p.add(p.scale(p.defects(base)[2], 2**degree), p.scale(eval_two(residue), -6))


def main():
    f = general_pair(u, v)
    g = general_pair(w, z)
    quartic = p.mul(f, g)
    scaled_quartic_margin = p.add(p.scale(p.defects(quartic)[0], 16), p.scale(eval_two(quartic), -1))
    result = {'scaled_quartic_delta0_minus_mass': certify('quartic', scaled_quartic_margin)}
    middle = p.add(x, p.const(Q(3, 2)), p.scale(w, Q(1, 2)))
    # For U_(4j+2), isolate c in [2,9/4]. For U_(4j+3), allow [7/4,9/4].
    u_pair_even = p.add(x2, p.scale(x, 3), p.const(2), p.scale(u, Q(1, 4)))
    u_pair_odd = p.add(x2, p.scale(x, 3), p.const(Q(7, 4)), p.scale(u, Q(1, 2)))
    inner = p.mul(p.add(x, p.const(1), p.scale(v, Q(1, 2))), p.add(x, p.const(Q(3, 2)), w))
    general_independent = general_pair(v, z)
    residues = {
        'n_mod8_0_pull_quartic': quartic,
        'n_mod8_1_pull_quartic': p.mul(quartic, p.add(x, p.const(Q(3, 2)), p.scale(t, Q(1, 2)))),
        'n_mod8_2': p.mul(central, middle),
        'n_mod8_3': p.mul(central, inner),
        'n_mod8_4': p.mul(u_pair_even, inner),
        'n_mod8_5': p.mul(p.mul(u_pair_even, middle), general_independent),
        'n_mod8_6': p.mul(p.mul(p.mul(central, u_pair_odd), middle), general_independent),
        'n_mod8_7': p.mul(central, u_pair_odd),
    }
    for name, residue in residues.items():
        degree, margin = margin_for_residue(residue)
        cert = certify(name, margin)
        cert['residue_degree'] = degree
        result[name] = cert
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
