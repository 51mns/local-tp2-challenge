"""Exact fixed-outer-boundary relative kernel certificates.

This uses the standalone polynomial/Bernstein arithmetic already audited in
mixed_ray_kernel_cert.py. It proves a continuum statement at m=2, not a scan
of finitely many outer recurrence indices.
"""
import json
from fractions import Fraction as Q
import mixed_ray_kernel_cert as p


def kernel(h, i, j):
    def get(n):
        return h[n] if n < len(h) else {}
    if i == 0:
        return get(j)
    if j == 0:
        return p.scale(get(i), 2)
    return p.add(get(abs(i-j)), get(i+j))


def minor(h, i, j, k, l):
    return p.add(p.mul(kernel(h, i, k), kernel(h, j, l)),
                 p.scale(p.mul(kernel(h, i, l), kernel(h, j, k)), -1))


def certificate(poly, *, strict=True):
    ds, values = p.bernstein(poly)
    lower = min(values.values())
    assert lower > 0 if strict else lower >= 0, (lower, poly)
    return {
        'parameter_degrees': ds,
        'lower_bound': str(lower),
        'power_coefficients': {','.join(map(str, e[1:])): str(v)
                               for e, v in sorted(poly.items())},
        'bernstein_coefficients': {k: str(v) for k, v in values.items()},
    }


def main():
    m = 2
    x, r0, s0, c0 = [p.variable(i) for i in range(p.DIM)]
    y = p.add(x, p.const(1))
    z = p.add(p.scale(x, 2), p.const(3))
    inner_u = [p.const(1), z]
    for j in range(2, m+2):
        inner_u.append(p.add(p.mul(z, inner_u[-1]), p.scale(inner_u[-2], -1)))
    inner_T = [p.add(*inner_u[:j+1]) for j in range(m+2)]
    A, B = inner_T[m+1], inner_T[m-1]
    P = p.add(p.const(1), p.mul(y, inner_T[m]))
    t = p.add(p.scale(p.mul(y, P), 3), p.scale(x, -1))
    r, s, c = [p.add(p.const(-2), p.scale(v, 4)) for v in (r0, s0, c0)]
    tr, ts = p.add(t, p.scale(r, -1)), p.add(t, p.scale(s, -1))
    single = p.add(p.mul(A, tr), B)
    midpoint = p.add(p.mul(A, p.mul(tr, ts)), p.mul(B, p.add(t, p.scale(c, -1))))
    q2 = p.mul(y, p.add(p.mul(A, p.add(p.mul(t, t), p.const(-1))), p.mul(B, t)))
    blocks = {
        'inner_A': A,
        'inner_B': B,
        'cubic_or_higher_root': tr,
        'y_root': p.mul(y, tr),
        'single': single,
        'y_single': p.mul(y, single),
        'y_A': p.mul(y, A),
        'y_degree_two': q2,
        'midpoint': midpoint,
    }
    result = {'m': m, 'blocks': {}}
    for name, block in blocks.items():
        result['blocks'][name] = [certificate(d) for d in p.defects(block)]
        for h in p.fourier(block)[:-2]:
            certificate(h)

    h, hb = p.fourier(midpoint), p.fourier(B)
    degree_h, degree_b = len(h)-3, len(hb)-3
    limit = degree_h+degree_b+1
    patterns = []
    min_bound = None
    min_pattern = None
    for i in range(limit+1):
        for gap in range(1, limit+1):
            j = i+gap
            for e in range(-degree_b, degree_b+1):
                k = i+e
                if k < 0:
                    continue
                for f in range(-degree_b, degree_b+1):
                    l = j+f
                    if l <= k:
                        continue
                    mb = minor(hb, i, j, k, l)
                    assert all(v == 0 or e == p.ZERO for e, v in mb.items())
                    value_b = mb.get(p.ZERO, Q(0))
                    assert value_b >= 0
                    if not value_b:
                        continue
                    difference = p.add(minor(h, i, j, k, l), p.const(-4*value_b))
                    degrees, coeffs = p.bernstein(difference)
                    lower = min(coeffs.values())
                    assert lower > 0, (i, j, k, l, lower)
                    pattern = [i, j, k, l]
                    patterns.append({'indices': pattern,
                                     'minor_B': str(value_b),
                                     'lower_bound': str(lower),
                                     'parameter_degrees': degrees})
                    if min_bound is None or lower < min_bound:
                        min_bound, min_pattern = lower, pattern
    result['relative_minor_certificate'] = {
        'degree_midpoint': degree_h,
        'degree_B': degree_b,
        'representative_first_row_limit': limit,
        'representative_row_gap_limit': limit,
        'positive_B_minor_patterns': len(patterns),
        'uniform_minimum_bernstein_bound': str(min_bound),
        'minimum_pattern': min_pattern,
        'patterns': patterns,
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
