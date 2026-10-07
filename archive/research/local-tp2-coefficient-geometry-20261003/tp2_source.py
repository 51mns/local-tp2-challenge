#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
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


def mediant(a: Fraction, b: Fraction):
    return Fraction(a.numerator + b.numerator, a.denominator + b.denominator)


def frac_string(f: Fraction):
    return f"{f.numerator}/{f.denominator}"


@dataclass(frozen=True)
class Node:
    r: Fraction
    t: Fraction
    s: Fraction
    A: tuple[int, ...]
    C: tuple[int, ...]
    B: tuple[int, ...]
    path: str
    depth: int


def record(node: Node):
    A, C, B = list(node.A), list(node.C), list(node.B)
    L = mutation_left(A, C, B)
    R = mutation_right(A, C, B)
    if len(L) == len(R):
        raise AssertionError(f"degree tie at {node.path!r}")
    if len(L) < len(R):
        U, V, u_side = L, R, "L"
    else:
        U, V, u_side = R, L, "R"
    S = sub(U, C)
    D = sub(V, U)
    if cubic_residual(A, C, B) != [0]:
        raise AssertionError(f"cubic residual nonzero at {node.path!r}")
    if eval_poly(S, -1) != 0 or eval_poly(D, -1) != 0:
        raise AssertionError(f"x+1 divisibility failed at {node.path!r}")
    P, Q = divide_x_plus_one(S), divide_x_plus_one(D)
    class_name = "root" if node.depth == 0 else ("last-L" if node.path.endswith("L") else "last-R")
    fv = f_values(S, D)
    return {
        "r": frac_string(node.r), "t": frac_string(node.t), "s": frac_string(node.s),
        "path": node.path, "depth": node.depth, "class": class_name, "u_side": u_side,
        "A": A, "C": C, "B": B, "L": L, "R": R, "U": U, "V": V,
        "S": S, "D": D, "H_S": H(S), "H_D": H(D),
        "P": P, "Q": Q, "H_P": H(P), "H_Q": H(Q),
        "F": fv, "degS": len(S) - 1, "degD": len(D) - 1,
        "cubic_zero": True,
    }


def generate_tree(max_depth=6):
    root = Node(Fraction(0, 1), Fraction(1, 2), Fraction(1, 1), tuple(G0), tuple(G12), tuple(G1), "", 0)
    stack = [root]
    out = []
    while stack:
        node = stack.pop()
        rec = record(node)
        out.append(rec)
        if node.depth < max_depth:
            L, R = rec["L"], rec["R"]
            tl, tr = mediant(node.r, node.t), mediant(node.t, node.s)
            stack.append(Node(node.t, tr, node.s, tuple(node.C), tuple(R), tuple(node.B), node.path + "R", node.depth + 1))
            stack.append(Node(node.r, tl, node.t, tuple(node.A), tuple(L), tuple(node.C), node.path + "L", node.depth + 1))
    return out


def W(hp, hq, i, j):
    return hget(hp, i) * hget(hq, j) - hget(hq, i) * hget(hp, j)


def qw_value(rec, n):
    hp, hq = rec["H_P"], rec["H_Q"]
    if n == 0:
        return -W(hp, hq, 0, 1) + W(hp, hq, 0, 2) + 2 * W(hp, hq, 1, 2)
    pairs = [(n - 1, n), (n - 1, n + 1), (n - 1, n + 2), (n, n + 2), (n + 1, n + 2)]
    return sum(W(hp, hq, i, j) for i, j in pairs)

