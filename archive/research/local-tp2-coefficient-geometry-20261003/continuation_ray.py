"""Exact certificates for Chebyshev-ray folded-TP building blocks.

All arithmetic uses fractions.Fraction; u,v range over [0,1].
"""
from fractions import Fraction as Q
from math import comb
import json


def add(*polys):
    out = {}
    for p in polys:
        for key, value in p.items():
            out[key] = out.get(key, Q(0)) + value
    return {k: v for k, v in out.items() if v}


def scale(p, scalar):
    return {k: v * scalar for k, v in p.items() if v * scalar}


def mul(p, r):
    out = {}
    for (x, u, v), a in p.items():
        for (xx, uu, vv), b in r.items():
            key = (x + xx, u + uu, v + vv)
            out[key] = out.get(key, Q(0)) + a * b
    return {k: v for k, v in out.items() if v}


one = {(0, 0, 0): Q(1)}
x = {(1, 0, 0): Q(1)}
u = {(0, 1, 0): Q(1)}
v = {(0, 0, 1): Q(1)}
y = add(x, one)
z = add(x, scale(one, Q(3, 2)))
c = add(scale(one, Q(5, 4)), u)
d = add(scale(one, Q(5, 4)), v)
fc = add(mul(x, x), scale(x, 3), c)
fd = add(mul(x, x), scale(x, 3), d)


def fourier(p):
    degree = max(k[0] for k in p)
    result = [{} for _ in range(degree + 3)]
    for (power, a, b), value in p.items():
        for j in range(power // 2 + 1):
            n = power - 2 * j
            result[n] = add(result[n], {(0, a, b): value * comb(power, j)})
    return result


def defects(p):
    h = fourier(p)
    ts = []
    for n in range(len(h) - 1):
        left = h[n - 1] if n else h[1]
        ts.append(add(mul(h[n], h[n]), scale(mul(left, h[n + 1]), -1)))
    return [add(ts[n], scale(ts[n + 1], -1)) for n in range(len(ts) - 1)]


def bernstein(p, elevation=0):
    du = max((k[1] for k in p), default=0) + elevation
    dv = max((k[2] for k in p), default=0) + elevation
    out = []
    for i in range(du + 1):
        row = []
        for j in range(dv + 1):
            total = Q(0)
            for (_, a, b), value in p.items():
                if a <= i and b <= j:
                    total += value * Q(comb(i, a), comb(du, a)) * Q(comb(j, b), comb(dv, b))
            row.append(total)
        out.append(row)
    return out


def main():
    blocks = {
        "B0_y_z": mul(y, z),
        "B1_y_fc": mul(y, fc),
        "B2_fc_fd": mul(fc, fd),
        "B3_y_fc_fd": mul(y, mul(fc, fd)),
        "B4_y_z_fc": mul(mul(y, z), fc),
    }
    all_certificates = {}
    for name, p in blocks.items():
        certs = []
        for n, defect in enumerate(defects(p)):
            bc = bernstein(defect)
            minimum = min(value for row in bc for value in row)
            assert minimum > 0, (name, n, minimum)
            certs.append({
                "n": n,
                "power_coefficients_uv": {f"{a},{b}": str(v) for (_, a, b), v in sorted(defect.items())},
                "bernstein_coefficients": [[str(v) for v in row] for row in bc],
                "strict_lower_bound": str(minimum),
            })
        all_certificates[name] = certs
    print(json.dumps(all_certificates, indent=2))


if __name__ == "__main__":
    main()
