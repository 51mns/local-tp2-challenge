#!/usr/bin/env python3
from __future__ import annotations
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def sub(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)])


def scale(a, c):
    return trim([c * x for x in a])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def eval_poly(a, x):
    out = 0
    for c in reversed(a):
        out = out * x + c
    return out


def divide_x_plus_one(a):
    if len(a) < 2:
        raise ValueError("nonzero constant not divisible by x+1")
    q = [0] * (len(a) - 1)
    q[0] = a[0]
    for k in range(1, len(q)):
        q[k] = a[k] - q[k - 1]
    remainder = a[-1] - q[-1]
    if remainder != 0:
        raise ValueError(f"not divisible by x+1: remainder={remainder}")
    return trim(q)


ONE_PLUS_X = [1, 1]
X = [0, 1]
G0 = [1]
G1 = [2, 1]
G12 = [5, 6, 2]


def mutation_left(A, C, B):
    return sub(sub(scale(mul(mul(ONE_PLUS_X, A), C), 3), mul(X, add(A, C))), B)


def mutation_right(A, C, B):
    return sub(sub(scale(mul(mul(ONE_PLUS_X, C), B), 3), mul(X, add(C, B))), A)


def cubic_residual(A, C, B):
    out = add(add(mul(A, A), mul(C, C)), mul(B, B))
    out = add(out, mul(X, add(add(mul(A, C), mul(C, B)), mul(A, B))))
    out = sub(out, scale(mul(mul(ONE_PLUS_X, mul(A, C)), B), 3))
    return trim(out)


def H(p):
    degree = len(p) - 1
    out = []
    for n in range(degree + 1):
        value = 0
        for j in range(n, degree + 1, 2):
            value += p[j] * comb(j, (j - n) // 2)
        out.append(value)
    return trim(out)


def hget(h, n):
    return h[n] if 0 <= n < len(h) else 0


def f_values(S, D):
    hs, hd = H(S), H(D)
    return [hget(hd, n + 1) * hget(hs, n) - hget(hd, n) * hget(hs, n + 1) for n in range(len(S))]



def children(A, C, B):
    return mutation_left(A, C, B), mutation_right(A, C, B)


def W(hp, hq, i, j):
    return hget(hp, i) * hget(hq, j) - hget(hq, i) * hget(hp, j)
