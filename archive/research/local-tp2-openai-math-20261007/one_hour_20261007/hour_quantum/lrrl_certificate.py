#!/usr/bin/env python3
"""Exact continuum certificates for strict Local TP2 on LR^2 L^ell.

Run with standard Python 3.  No third-party modules or AIMath imports are used.
The exported JSON contains every power coefficient and every tensor-Bernstein
coefficient used in the proof.  Each Bernstein conversion is independently
inverted before its signs are accepted.  The finite comparisons are exact
integer identities; the all-ell argument is in lrrl_theorem.md.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json


# Ordinary polynomials in x, represented in ascending coefficient order.
def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def padd(*ps):
    out = [0] * max(map(len, ps))
    for p in ps:
        for i, a in enumerate(p):
            out[i] += a
    return trim(out)


def pscale(p, a):
    return trim([a * b for b in p])


def psub(p, q):
    return padd(p, pscale(q, -1))


def pmul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def peval(p, z=2):
    value = 0
    for a in reversed(p):
        value = z * value + a
    return value


def divide_y(p):
    q = [p[0]]
    for a in p[1:-1]:
        q.append(a - q[-1])
    assert p[-1] == q[-1], "Polynomial is not divisible by x+1"
    assert pmul(q, [1, 1]) == trim(p)
    return trim(q)


def mutate(A, C, B):
    return psub(psub(pscale(pmul(pmul([1, 1], A), C), 3),
                     pmul([0, 1], padd(A, C))), B)


def node(path):
    A, C, B = [1], [5, 6, 2], [2, 1]
    for step in path:
        if step == 'L':
            A, C, B = A, mutate(A, C, B), C
        else:
            A, C, B = C, mutate(B, C, A), B
    return A, C, B


def half(p):
    return [sum(p[j] * comb(j, (j - n) // 2)
                for j in range(n, len(p), 2)) for n in range(len(p))]


def at(h, n):
    return h[n] if 0 <= n < len(h) else 0


def adjacent(p, q):
    h, k = half(p), half(q)
    return [at(h, n) * at(k, n + 1) - at(h, n + 1) * at(k, n)
            for n in range(max(len(p), len(q)))]


# Sparse multivariate polynomials in (x,u,v,w).  Parameters u,v,w are in [0,1].
ZERO = (0, 0, 0, 0)


def const(a):
    return {ZERO: Q(a)} if a else {}


def variable(i):
    e = [0] * 4
    e[i] = 1
    return {tuple(e): Q(1)}


def lift(p):
    return {(i, 0, 0, 0): Q(a) for i, a in enumerate(p) if a}


def add(*ps):
    out = {}
    for p in ps:
        for e, a in p.items():
            out[e] = out.get(e, Q(0)) + a
    return {e: a for e, a in out.items() if a}


def scale(p, a):
    return {e: a * b for e, b in p.items() if a * b}


def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(i + j for i, j in zip(e, f))
            out[g] = out.get(g, Q(0)) + a * b
    return {e: a for e, a in out.items() if a}


def fourier(p):
    degree = max(e[0] for e in p)
    h = [{} for _ in range(degree + 3)]
    for e, a in p.items():
        for j in range(e[0] // 2 + 1):
            n = e[0] - 2 * j
            h[n] = add(h[n], {(0,) + e[1:]: a * comb(e[0], j)})
    return h


def defects(p):
    h = fourier(p)
    d = [add(mul(h[n], h[n]),
             scale(mul(h[n - 1] if n else h[1], h[n + 1]), -1))
         for n in range(len(h) - 1)]
    return [add(d[n], scale(d[n + 1], -1)) for n in range(len(d) - 1)]


def kernel(h, i, j):
    if i == 0:
        return at(h, j) or {}
    if j == 0:
        return scale(at(h, i) or {}, 2)
    return add(at(h, abs(i - j)) or {}, at(h, i + j) or {})


def minor(h, i, j, k, l):
    return add(mul(kernel(h, i, k), kernel(h, j, l)),
               scale(mul(kernel(h, i, l), kernel(h, j, k)), -1))


def evaluate_x(p, x=2):
    return add(*({(0,) + e[1:]: a * x ** e[0]} for e, a in p.items()))


def bernstein(p):
    """Convert power basis to full tensor Bernstein basis, then invert."""
    assert all(e[0] == 0 for e in p)
    degrees = tuple(max((e[j] for e in p), default=0) for j in (1, 2, 3))
    indices = list(product(*(range(d + 1) for d in degrees)))
    coefficients = {}
    for i in indices:
        value = Q(0)
        for e, a in p.items():
            if all(k <= j for k, j in zip(e[1:], i)):
                term = a
                for k, j, degree in zip(e[1:], i, degrees):
                    term *= Q(comb(j, k), comb(degree, k))
                value += term
        coefficients[i] = value

    # Inverse uses direct expansion of binom(d,i) u^i (1-u)^(d-i).
    reconstructed = {}
    for i, a in coefficients.items():
        for k in product(*(range(j, d + 1) for j, d in zip(i, degrees))):
            term = a
            for j, exponent, degree in zip(i, k, degrees):
                term *= comb(degree, j) * comb(degree - j, exponent - j)
                term *= (-1) ** (exponent - j)
            e = (0,) + k
            reconstructed[e] = reconstructed.get(e, Q(0)) + term
    reconstructed = {e: a for e, a in reconstructed.items() if a}
    assert reconstructed == p, "Independent inverse Bernstein check failed"
    return degrees, coefficients


def export_certificate(p, strict=True):
    degree, bc = bernstein(p)
    minimum = min(bc.values())
    assert minimum > 0 if strict else minimum >= 0
    return {
        'parameter_degrees': degree,
        'minimum_bernstein_coefficient': str(minimum),
        'power_coefficients': {','.join(map(str, e[1:])): str(a)
                               for e, a in sorted(p.items())},
        'bernstein_coefficients': {','.join(map(str, i)): str(a)
                                  for i, a in sorted(bc.items())},
    }


def ordinary_positivity(p):
    degree = max(e[0] for e in p)
    certs = []
    for n in range(degree + 1):
        coefficient = {(0,) + e[1:]: a for e, a in p.items() if e[0] == n}
        certs.append(export_certificate(coefficient))
    return certs


def main():
    X, C0, Y = node('LRR')
    y = [1, 1]
    t = psub(pscale(pmul(y, X), 3), [0, 1])
    T = psub(psub(pmul(t, Y), pmul([0, 1], X)), C0)
    A, B = divide_y(psub(C0, Y)), divide_y(psub(T, Y))
    assert X == [194, 801, 1408, 1336, 716, 204, 24]
    assert Y == [5, 6, 2] and T == [13, 26, 18, 4]
    q0 = pmul(y, A)
    q1 = pmul(y, padd(pmul(A, t), B))
    C1 = mutate(X, C0, Y)
    assert q1 == psub(C1, C0)
    assert C1 == psub(psub(pmul(t, C0), pmul([0, 1], X)), Y)

    # The one initial state ell=0 is checked exactly, not inferred from a ray.
    left, right = mutate(X, C0, Y), mutate(Y, C0, X)
    assert len(right) < len(left)
    initial_F = adjacent(psub(right, C0), psub(left, right))[:len(right)]
    assert len(initial_F) == 13 and min(initial_F) > 0

    Pi = pmul([2, 1], X)
    f = pmul(y, psub(t, [2]))
    g = pscale(pmul(pmul(y, y), Pi), 3)
    M0 = padd(psub(pscale(pmul(y, Y), 3), [0, 1]), [1])
    K = pmul(Pi, M0)
    comparisons = {
        'q0_q1': adjacent(q0, q1),
        'y_AplusB_q1': adjacent(pmul(y, padd(A, B)), q1),
        'Pi_E1': adjacent(Pi, psub(C0, X)),
        'Pi_q1': adjacent(Pi, q1),
        'f_g': adjacent(f, g),
    }
    lower_degrees = [len(q0)-1, len(pmul(y, padd(A, B)))-1,
                     len(Pi)-1, len(Pi)-1, len(f)-1]
    for (name, row), d in zip(comparisons.items(), lower_degrees):
        assert all(a > 0 for a in row[:d + 1]), name
        assert all(a >= 0 for a in row), name

    a, b, trace, yy = map(lift, (A, B, t, y))
    pars = [add(const(-2), scale(variable(i), 4)) for i in (1, 2, 3)]
    roots = [add(trace, scale(r, -1)) for r in pars]
    L = add(mul(a, roots[0]), b)
    midpoint = add(mul(a, mul(roots[0], roots[1])), mul(b, roots[2]))
    blocks = {
        'A': a, 'B': b, 'yA': mul(yy, a),
        't_minus_r': roots[0], 'y_t_minus_r': mul(yy, roots[0]),
        'L_r': L, 'y_L_r': mul(yy, L),
        'midpoint': midpoint,
        'q2': mul(yy, add(mul(a, add(mul(trace, trace), const(-1))),
                           mul(b, trace))),
    }
    strength = 8 * half(B)[0]
    assert strength == 128
    box_certificates = {}
    box_summary = {}
    for name, p in blocks.items():
        h = fourier(p)
        ds = defects(p)
        margins = [add(d, scale(h[n], -strength if name == 'midpoint' else 0))
                   for n, d in enumerate(ds)]
        certs = [export_certificate(d) for d in margins]
        box_certificates[name] = {
            'degree_x': len(ds) - 1,
            'subtracted_strength': strength if name == 'midpoint' else 0,
            'ordinary_positive_support': ordinary_positivity(p),
            'defects_after_strength': certs,
        }
        box_summary[name] = min(Q(c['minimum_bernstein_coefficient']) for c in certs)

    # H(midpoint) dominates H(B) for every independent parameter triple.
    domination = ordinary_positivity(add(midpoint, scale(b, -1)))

    propagator_mass = evaluate_x(roots[0])
    template_mass = evaluate_x(L)
    template_mass_max = max(bernstein(template_mass)[1].values())
    propagator_mass_max = max(bernstein(propagator_mass)[1].values())
    gamma = min(bernstein(defects(roots[0])[0])[1].values()) // propagator_mass_max
    assert gamma == 435 and gamma >= 2
    propagator_margin = export_certificate(
        add(defects(roots[0])[0], scale(propagator_mass, -gamma)), strict=False)
    A2, B2, t2 = map(peval, (A, B, t))
    assert 0 < B2 < A2 * (t2 - 2)
    assert template_mass_max == 947589874320

    alpha_rows = []
    hL = fourier(L)
    hK = half(K)
    f_mass = peval(f)
    for n in range(len(K)):
        i = min(n, len(f) - 1)
        determinant = minor(hL, i, i + 1, n, n + 1)
        alpha = min(bernstein(determinant)[1].values()) // template_mass_max
        assert alpha > 0
        margin_certificate = export_certificate(
            add(determinant, scale(template_mass, -alpha)), strict=False)
        fixed_minor = comparisons['f_g'][i]
        residual = fixed_minor * alpha - 2 * f_mass * hK[n]
        assert residual > 0
        alpha_rows.append({
            'n': n, 'input_index': i, 'alpha': str(alpha),
            'fixed_minor': fixed_minor, 'strict_proxy_residual': str(residual),
            'template_minor_margin': margin_certificate,
        })

    beta_rows = []
    QL = mul(lift([1, 2, 1]), L)
    h0 = half(M0)
    m_at = lambda j: at(h0, abs(j))
    for n in range(len(M0) + 1):
        delta = defects(QL)[n]
        beta = min(bernstein(delta)[1].values()) // template_mass_max
        assert beta > 0
        margin_certificate = export_certificate(
            add(delta, scale(template_mass, -beta)), strict=False)
        negative_cross_bound = m_at(n - 1) + 3 * m_at(n + 1)
        residual = beta - 6 * negative_cross_bound
        assert residual > 0
        beta_rows.append({
            'n': n, 'beta': str(beta),
            'negative_cross_coefficient': negative_cross_bound,
            'strict_multiplier_residual': str(residual),
            'template_defect_margin': margin_certificate,
        })
    M0_delta = [d.get(ZERO, 0) for d in defects(lift(M0))]
    assert M0_delta == [632, 688, 240, 36]

    output = {
        'statement': 'Strict Local TP2 at every LR^2 L^ell, integer ell >= 0',
        'scope': 'Infinite ell is proved in lrrl_theorem.md; no finite scan extrapolation',
        'data': dict(X=X, Y=Y, C0=C0, T=T, A=A, B=B, t=t,
                     Pi=Pi, f=f, g=g, M0=M0, K=K),
        'initial_F_ell_zero': initial_F,
        'fixed_comparisons': comparisons,
        'box_certificates': box_certificates,
        'midpoint_minus_B_ordinary_positive_support': domination,
        'mass_bounds': {
            'A_at_2': A2, 'B_at_2': B2, 't_at_2': t2,
            'template_mass_max': str(template_mass_max),
            'propagator_mass_max': str(propagator_mass_max),
            'gamma': str(gamma), 'gamma_margin': propagator_margin,
            'f_at_2': f_mass, 'H_K': hK,
        },
        'proxy_certificates': alpha_rows,
        'multiplier_certificates': beta_rows,
        'M0_defects': list(map(str, M0_delta)),
        'summary': {
            'box_minima': {k: str(v) for k, v in box_summary.items()},
            'minimum_proxy_residual': str(min(Q(r['strict_proxy_residual']) for r in alpha_rows)),
            'minimum_multiplier_residual': str(min(Q(r['strict_multiplier_residual']) for r in beta_rows)),
            'all_bernstein_conversions_independently_inverted': True,
        },
    }
    path = Path(__file__).with_name('lrrl_certificates.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output['summary'], indent=2))
    print('PASS: all exact coefficient certificates; wrote', path.name)


if __name__ == '__main__':
    main()
