#!/usr/bin/env python3
"""Exact certificates for the two-run endpoint trace transport theorem.

No third-party packages are required. The all-index input strengths are
the previously audited AIMath prefix theorems, not a finite scan here.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(p, c):
    return trim([c * x for x in p])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    p = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            p[i + j] += u * v
    return trim(p)


def hrow(p):
    return [sum(p[j] * comb(j, (j - n) // 2) for j in range(n, len(p), 2))
            for n in range(len(p))]


def defects(h):
    f = lambda n: h[abs(n)] if abs(n) < len(h) else 0
    return [f(n)**2 - f(n-1)*f(n+1) - f(n+1)**2 + f(n)*f(n+2)
            for n in range(len(h))]


def trace(p):
    return sub(scale(mul([1, 1], p), 3), [0, 1])


def left(A, C, B):
    return sub(sub(scale(mul(mul([1, 1], A), C), 3), mul([0, 1], add(A, C))), B)


def right(A, C, B):
    return sub(sub(scale(mul(mul([1, 1], C), B), 3), mul([0, 1], add(C, B))), A)


def get_prefix(m):
    """Original scalar recurrence at L^m, followed by its right child."""
    A, C, B = [1], [5, 6, 2], [2, 1]
    for _ in range(m):
        A, C, B = A, left(A, C, B), C
    X = right(A, C, B)
    assert A == [1]
    assert trace(X) == sub(mul(trace(B), trace(C)), [3, 4, 1])
    return B, C, X


# Sparse exact symbolic polynomials in h0,...,h6,c.  They verify every
# low-index correction formula with independent direct expansion.
NV = 8


def const(n):
    return {(0,) * NV: Fraction(n)} if n else {}


def var(i):
    key = [0] * NV
    key[i] = 1
    return {tuple(key): Fraction(1)}


def plus(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
    return {k: v for k, v in out.items() if v}


def times(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x + y for x, y in zip(ka, kb))
            out[key] = out.get(key, 0) + va * vb
    return {k: v for k, v in out.items() if v}


def scal(a, c):
    return {k: v * c for k, v in a.items() if v * c}


def minus(a, b):
    return plus(a, scal(b, -1))


def total(*args):
    out = {}
    for a in args:
        out = plus(out, a)
    return out


def symdef(row, n):
    f = lambda k: row[abs(k)] if abs(k) < len(row) else {}
    return total(times(f(n), f(n)), scal(times(f(n-1), f(n+1)), -1),
                 scal(times(f(n+1), f(n+1)), -1), times(f(n), f(n+2)))


def check_symbolic_formulas():
    h = [var(i) for i in range(7)]
    c = var(7)
    corrections = [c, const(4), const(1)]
    row = [minus(v, corrections[i] if i < len(corrections) else {})
           for i, v in enumerate(h)]
    raw = [
        total(scal(times(total(scal(c, 2), const(1)), h[0]), -1),
              scal(times(c, h[2]), -1), scal(h[1], 16), times(c, c), c, const(-32)),
        total(scal(h[1], -8), h[0], times(plus(c, const(2)), h[2]),
              scal(h[3], -4), const(15), scal(c, -1)),
        total(scal(h[2], -2), scal(h[3], 4), scal(h[4], -1), const(1)),
        h[4],
        {},
    ]
    for n, formula in enumerate(raw):
        assert minus(symdef(row, n), symdef(h, n)) == formula, ("raw", n)

    corrections = [plus(c, const(8)), plus(c, const(5)), const(5), const(1)]
    row = [minus(v, corrections[i] if i < len(corrections) else {})
           for i, v in enumerate(h)]
    smooth = [
        total(scal(times(plus(scal(c, 2), const(21)), h[0]), -1),
              scal(times(plus(c, const(8)), h[2]), -1),
              scal(times(plus(c, const(5)), h[1]), 4),
              scal(times(c, c), -1), c, const(54)),
        total(scal(times(plus(scal(c, 2), const(11)), h[1]), -1),
              scal(h[0], 5), times(plus(c, const(18)), h[2]),
              scal(times(plus(c, const(5)), h[3]), -1),
              times(c, c), scal(c, 6), const(-35)),
        total(scal(h[2], -10), h[1], times(plus(c, const(7)), h[3]),
              scal(h[4], -5), const(19), scal(c, -1)),
        total(scal(h[3], -2), scal(h[4], 5), scal(h[5], -1), const(1)),
        h[5],
    ]
    for n, formula in enumerate(smooth):
        assert minus(symdef(row, n), symdef(h, n)) == formula, ("smooth", n)

    # Existing-prefix -> new unshifted-strength improvements, independently
    # verifying the displayed correction formulas as well.
    for label, perturbation, expected in [
        ("t_m", [3, 2], [
            total(scal(h[0], 18), scal(h[2], 9), scal(h[1], -24), const(1)),
            total(scal(h[1], 12), scal(h[2], -9), scal(h[3], 6), const(4)),
            scal(h[3], -6), {}, {}]),
        ("y_t_m", [7, 5, 2], [
            total(scal(h[0], 48), scal(h[1], -60), scal(h[2], 21), const(13)),
            total(scal(h[1], 30), scal(h[0], -6), scal(h[2], -33), scal(h[3], 15), const(7)),
            total(scal(h[2], 12), scal(h[3], -15), scal(h[4], 6), const(4)),
            scal(h[4], -6), {}]),
    ]:
        row = [plus(scal(v, 3), const(perturbation[i] if i < len(perturbation) else 0))
               for i, v in enumerate(h)]
        for n, formula in enumerate(expected):
            assert minus(symdef(row, n), scal(symdef(h, n), 9)) == formula, (label, n)
    return {"raw_subtraction": len(raw), "smoothed_subtraction": len(smooth),
            "unshifted_trace_improvements": 10}


def small_certificate(m, smooth, strength):
    gm, gm1, X = get_prefix(m)
    tr = trace(X)
    rows = {}
    margins = {}
    for r in (-2, 0, 2):
        p = sub(tr, [r])
        if smooth:
            p = mul([1, 1], p)
        h = hrow(p)
        rows[r] = h
        margins[r] = [d - strength*v for d, v in zip(defects(h), h)]
    bernstein = []
    for lo, mid, hi in zip(margins[-2], margins[0], margins[2]):
        # Degree-two Bernstein coefficients after r=4u-2.
        b = [Fraction(lo), 2*Fraction(mid)-Fraction(lo+hi, 2), Fraction(hi)]
        assert all(v >= 0 for v in b)
        bernstein.append([int(v) if v.denominator == 1 else str(v) for v in b])
    assert all(v > 0 for v in rows[-2]) and all(v > 0 for v in rows[2])
    assert all(x == 0 for x in bernstein[-1]), "optimal terminal strength"
    return {"m": m, "smoothed": smooth, "strength": strength,
            "trace_x_coefficients": tr,
            "half_rows_at_r_minus2_and_plus2": [rows[-2], rows[2]],
            "degree_two_bernstein_margins": bernstein}


def main():
    symbolic = check_symbolic_formulas()
    small = [small_certificate(0, False, 18),
             small_certificate(0, True, 18),
             small_certificate(1, True, 72)]
    # Boundary arithmetic for the infinite formula, not a tree scan.
    a = 2
    assert (3*a-2)*(6*a-2)-15 == 25
    a = 4
    assert (3*a-2)*(3*a-5)-35 == 35
    result = {
        "status": "PASS; analytical all-m trace theorem, not all Local TP2",
        "symbolic_identity_checks": symbolic,
        "input_theorems": ["mixed_kernel_sharp_strength.md", "mixed_kernel_strong_cone.md",
                           "recovery_oneturn_closure.md section 1"],
        "uniform_trace_strength": "18 (m=0); 18*4^m - 18*2^m - 11 (m>=1)",
        "uniform_smoothed_trace_strength": "18 (m=0); 72 (m=1); 9*4^m - 21*2^m - 25 (m>=2)",
        "shift_parameter_domain": "all real r in [-2,2]",
        "small_m_certificates": small,
    }
    out = Path(__file__).with_name("trace_transport_results.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "symbolic_identity_checks": symbolic,
                      "small_m_certificates": len(small), "output": str(out)}, indent=2))


if __name__ == "__main__":
    main()
