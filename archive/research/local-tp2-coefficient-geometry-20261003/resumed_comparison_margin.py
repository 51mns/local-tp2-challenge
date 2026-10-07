"""Exact residue certificates for an actual all-left Local TP2 subfamily.

This verifies pair minors and quantitative low-mode margins; it is not
a finite-depth conjecture check. All parameters range over whole cubes.
"""
import continuation_bracket_certify as b
from fractions import Fraction as F
import json

p = b.p
x, u, v, w, z, t = b.x, b.u, b.v, b.w, b.z, b.t
f = b.general_pair(u, v)
g = b.general_pair(w, z)
quartic = p.mul(f, g)
middle = p.add(x, p.const(F(3, 2)), p.scale(w, F(1, 2)))
even = p.add(b.x2, p.scale(x, 3), p.const(2), p.scale(u, F(1, 4)))
odd = p.add(b.x2, p.scale(x, 3), p.const(F(7, 4)), p.scale(u, F(1, 2)))
inner = p.mul(p.add(x, p.const(1), p.scale(v, F(1, 2))), p.add(x, p.const(F(3, 2)), w))
independent = b.general_pair(v, z)
residues = {
    0: quartic,
    1: p.mul(quartic, p.add(x, p.const(F(3, 2)), p.scale(t, F(1, 2)))),
    2: p.mul(b.central, middle),
    3: p.mul(b.central, inner),
    4: p.mul(even, inner),
    5: p.mul(p.mul(even, middle), independent),
    6: p.mul(p.mul(p.mul(b.central, odd), middle), independent),
    7: p.mul(b.central, odd),
}
A = p.add(p.const(1), p.scale(x, 2))
U2 = p.add(p.const(8), p.scale(x, 12), p.scale(b.x2, 4))
thresholds = [F(80), F(160, 3), F(40, 3)]


def certificate(name, poly):
    degrees, coefficients = p.bernstein(poly)
    lower = min(coefficients.values())
    assert lower > 0, (name, lower)
    return {
        'degrees': degrees,
        'strict_lower_bound': str(lower),
        'power_coefficients': {','.join(map(str, k[1:])): str(v) for k, v in sorted(poly.items())},
        'bernstein_coefficients': {k: str(v) for k, v in coefficients.items()},
    }


def main():
    result = {}
    for residue_class, R in residues.items():
        d = max(key[0] for key in R)
        e = p.mul(b.y, R)
        lower = p.fourier(p.mul(A, e))
        upper = p.fourier(p.mul(U2, e))
        determinants = []
        pair_certificates = []
        for n in range(d + 3):
            minor = p.add(p.mul(lower[n], upper[n+1]), p.scale(p.mul(lower[n+1], upper[n]), -1))
            determinants.append(minor)
            pair_certificates.append(certificate(f'pair_{residue_class}_{n}', minor))
        boost = 4 if residue_class in (2, 3) else 1
        margin_certificates = []
        mass = b.eval_two(e)
        for n, threshold in enumerate(thresholds):
            # Actual residue e0=2^d*e. Dividing the desired margin by 2^d
            # gives boost*2^d*minor(e) - threshold*mass(e).
            margin = p.add(p.scale(determinants[n], boost * 2**d), p.scale(mass, -threshold))
            margin_certificates.append(certificate(f'margin_{residue_class}_{n}', margin))
        result[str(residue_class)] = {
            'monic_residue_degree': d,
            'required_quartic_boost': boost,
            'pair_certificates': pair_certificates,
            'margin_certificates': margin_certificates,
        }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
