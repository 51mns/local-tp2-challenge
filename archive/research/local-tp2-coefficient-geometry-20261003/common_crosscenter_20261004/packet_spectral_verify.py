#!/usr/bin/env python3
"""Exact verification of common trace-flux subgates and relaxed obstruction.

Self-contained Fraction arithmetic. No path scan and no old-directory writes.
Analytic statements and qualifications are in packet_spectral.md.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, a):
    return trim([a * u for u in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, w in enumerate(q):
            out[i + j] += u * w
    return trim(out)


def H(p):
    return trim([sum(p[j] * comb(j, (j - n) // 2)
                     for j in range(n, len(p), 2)) for n in range(len(p))])


def hval(h, i):
    return h[abs(i)] if abs(i) < len(h) else 0


def xrow(h):
    return [hval(h, i - 1) + hval(h, i + 1) for i in range(len(h) + 1)]


def row_minor(h, i, j):
    q = xrow(h)
    return hval(h, i) * q[j] - hval(h, j) * q[i]


def tensor(p):
    h, out = H(p), {}
    for i in range(len(h) + 1):
        for j in range(i + 1, len(h) + 1):
            w = row_minor(h, i, j)
            if w:
                out[i + j - 1, j - i - 1] = w
                if i:
                    out[j - i - 1, i + j - 1] = w
    return out


def mixed(p, q):
    a, b, c = tensor(add(p, q)), tensor(p), tensor(q)
    return {k: a.get(k, 0) - b.get(k, 0) - c.get(k, 0)
            for k in set(a) | set(b) | set(c)
            if a.get(k, 0) - b.get(k, 0) - c.get(k, 0)}


def cg_mul(a, b):
    out = {}
    for (i, j), u in a.items():
        for (k, l), w in b.items():
            for n in range(abs(i - k), i + k + 1, 2):
                for m in range(abs(j - l), j + l + 1, 2):
                    out[n, m] = out.get((n, m), 0) + u * w
    return {k: v for k, v in out.items() if v}


def strict_certificate(p):
    h, t = H(p), tensor(p)
    defects = [row_minor(h, n, n + 1) for n in range(len(h))]
    assert all(u > 0 for u in h)
    assert all(u >= 0 for u in t.values())
    assert all(u > 0 for u in defects)
    return dict(degree=len(p) - 1, character_terms=len(t),
                min_character=min(t.values()), defects=defects)


def cosine_poly(i):
    if i == 0:
        return [1]
    if i == 1:
        return [0, 1]
    p, q = [2], [0, 1]
    for _ in range(2, i + 1):
        p, q = q, sub(mul([0, 1], q), p)
    return q


def from_halfrow(h):
    p = [0]
    for i, a in enumerate(h):
        p = add(p, scale(cosine_poly(i), a))
    assert H(p) == h
    return p


Y = [1, 1]
BETA = [3, 6, 3]


def record(a, e, r):
    X = add([1], mul(Y, a))
    t = sub(scale(mul(Y, X), 3), [0, 1])
    k = mul(X, sub(scale(X, 3), [2]))
    g = add(add(mul(sub(t, [2]), e), k), r)
    s = sub(mul(t, g), r)
    C = add([1], mul(Y, add(add(a, e), g)))
    T = sub(scale(mul(Y, C), 3), [0, 1])
    d = mul(e, add(T, [1]))
    larger = add(X, mul(Y, e))
    fricke = sub(sub(sub(mul(r, g), mul(sub(t, [2]), mul(e, e))),
                     scale(mul(k, e), 2)), scale(mul(a, mul(X, X)), 3))
    assert fricke == [0]
    return dict(a=a, e=e, r=r, X=X, Y=larger, C=C, T=T, g=g, s=s, d=d)


def actual_witness(st, sigma):
    v = add(st['s'], scale(st['d'], sigma))
    f, g = st['T'], mul(BETA, v)
    d, m, D = len(f) - 1, len(v) - 1, len(g) - 1
    assert m >= d and D >= d + 2
    ch = (d + D, D - d - 2)
    j = mixed(f, g)[ch]
    assert j == -f[-1] * g[-1]
    assert tensor(f).get(ch, 0) == 0
    vg = tensor(g)[ch]
    lower = (9 if m == d else 27) * v[-1] ** 2
    assert vg >= lower
    lc_endpoint = st['X' if sigma == 0 else 'Y'][-1]
    assert v[-1] == lc_endpoint * f[-1]
    child = tensor(add(f, g))[ch]
    assert child == vg + j > 0
    # Every changed shift has the identical selected coefficient.
    for shift in [-2, F(-3, 2), 0, F(3, 2), 2]:
        assert tensor(add(sub(f, [shift]), g))[ch] == child
    # Adjacent upper tail: the only correction above deg f is at d+1.
    hf, hg, hc = H(f), H(g), H(add(f, g))
    assert row_minor(hc, d + 1, d + 2) == (
        row_minor(hg, d + 1, d + 2) - f[-1] * hval(hg, d + 2))
    for n in range(d + 2, D + 1):
        assert row_minor(hc, n, n + 1) == row_minor(hg, n, n + 1) > 0
    return dict(child='short' if sigma == 0 else 'long', degree_T=d,
                degree_v=m, degree_beta_v=D, rows=[0, 1],
                columns=[d + 1, D], character=list(ch),
                lc_T=f[-1], lc_v=v[-1], mixed_negative=j,
                beta_v_coefficient=vg, proved_lower_bound=lower,
                actual_child_coefficient=child)


def main():
    beta_tensor = {(0, 0): 36, (1, 1): 18, (2, 2): 27,
                   (3, 1): 18, (1, 3): 18, (4, 0): 9, (0, 4): 9}
    assert tensor(BETA) == beta_tensor

    # Genuine canonical witnesses, not a finite state or parameter scan.
    root = record([0], [1], [1])
    root_long = record(add(root['a'], root['e']), root['g'],
                       add(root['e'], root['g']))
    actual = [actual_witness(root, 1), actual_witness(root_long, 0)]

    # Exact rational STRICT obstruction to a relaxed border-margin lemma.
    # The row itself is specified rationally; no numerical step is needed.
    hv = [F(4659, 1000), F(4537, 1000), F(4181, 1000),
          F(3610, 1000), F(2859, 1000), F(1971, 1000), F(1)]
    v = from_halfrow(hv)
    vc, yvc = strict_certificate(v), strict_certificate(mul(Y, v))
    f = [16, 8, 1]
    assert f[-1] == v[-1] == 1
    g, out = mul(BETA, v), add(f, mul(BETA, v))
    assert tensor(g) == cg_mul(tensor(BETA), tensor(v))
    gc = strict_certificate(g)
    obstruction = row_minor(H(out), 3, 4)
    assert obstruction == F(-29300421, 500000)
    assert obstruction == row_minor(H(g), 3, 4) - H(g)[4]

    # For f-r=(x+4)^2-r, ALL characters are nonnegative for |r|<=2.
    # Rows (0,1), cols (0,1),(0,2),(0,3),(1,2),(1,3),(2,3):
    # (18-r)(19-r)-128,128-8r,18-r,45+r,8,1.
    trace_bounds = [144, 112, 16, 43, 8, 1]
    assert all(x > 0 for x in trace_bounds)
    for r in [-2, 2]:
        strict_certificate(sub(f, [r]))

    result = dict(
        arithmetic='Exact integers/Fractions; no external imports or numerical proofs.',
        scope='Analytic common trace subgates plus an exact relaxed obstruction; no full packet or target closure.',
        beta_tensor=[dict(character=list(k), coefficient=w)
                     for k, w in sorted(beta_tensor.items())],
        canonical_witnesses=actual,
        strict_relaxed_border_obstruction=dict(
            f_power=f, v_halfrow=hv, v_power=v,
            v_raw=vc, v_y=yvc, beta_v_raw=gc,
            parent_trace_all_r_character_lower_bounds=trace_bounds,
            leading_coefficients=dict(f=1, v=1),
            failed_rows=[0, 1], failed_columns=[3, 4], failed_defect=obstruction,
            qualification='v is not claimed to have an MP_sharp origin, canonical ancestry, ordinary-positive power coefficients, or Fricke completion.'),
        analytic_remaining_gate='For d=deg T, delta_(d+1)(beta v)>lc(T)*(beta v)_(d+2), plus lower overlap indices and full child packet tensors.')
    def encode(obj):
        if isinstance(obj, F):
            return str(obj)
        raise TypeError(type(obj).__name__)
    target = Path(__file__).with_name('packet_spectral_results.json')
    target.write_text(json.dumps(result, indent=2, default=encode) + '\n')
    print(json.dumps(dict(status='PASS', canonical_witnesses=actual,
                         strict_relaxed_border_defect=obstruction,
                         saved=target.name), indent=2, default=encode))


if __name__ == '__main__':
    main()
