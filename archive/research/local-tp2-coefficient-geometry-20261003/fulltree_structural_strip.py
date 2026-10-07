"""Exact algebra checks for fulltree_structural_strip.md; no depth scan.

The all-tree statement is proved by induction in the manuscript. This
script checks the polynomial identities symbolically and the two stated
finite examples; it does not infer any infinite assertion from examples.
"""
from collections import defaultdict
from math import comb


def add(*ps):
    r = defaultdict(int)
    for p in ps:
        for m, c in p.items():
            r[m] += c
    return {m: c for m, c in r.items() if c}


def scale(p, c):
    return {m: c*v for m, v in p.items() if c*v}


def mul(*ps):
    r = {(0,)*5: 1}
    for p in ps:
        out = defaultdict(int)
        for a, v in r.items():
            for b, w in p.items():
                out[tuple(x+y for x, y in zip(a, b))] += v*w
        r = {m: c for m, c in out.items() if c}
    return r


def var(i):
    a = [0]*5
    a[i] = 1
    return {tuple(a): 1}


one = {(0,)*5: 1}
x, A, C, B, T = map(var, range(5))
y = add(x, one)
U = add(scale(mul(y, A, C), 3), scale(mul(x, add(A, C)), -1), scale(B, -1))
lhs = add(U, scale(mul(y, add(A, C)), -1))
rhs = add(mul(y, add(C, scale(one, -2))),
          mul(y, add(A, scale(one, -1)), add(scale(C, 3), scale(one, -2))),
          A, C, scale(B, -1))
assert lhs == rhs

# Here A=X and B=Y; T is the endpoint removed in the preceding step.
t = add(scale(mul(y, A), 3), scale(x, -1))
new_center = add(mul(t, B), scale(mul(x, A), -1), scale(T, -1))
rho = add(new_center, scale(mul(add(t, scale(one, -1)), B), -1))
assert rho == add(B, scale(T, -1), scale(mul(x, A), -1))
assert rho == add(B, scale(mul(y, add(A, T)), -1), A, mul(x, T))
assert add(B, scale(rho, -1)) == add(T, mul(x, A))


def H(p):
    out = [0]*len(p)
    for d, c in enumerate(p):
        for j in range(d//2+1):
            n = d-2*j
            out[n] += c*comb(d, j)
    return out


def defects(h):
    def at(j):
        j = abs(j)
        return h[j] if j < len(h) else 0
    return [at(n)**2-at(n-1)*at(n+1)-at(n+1)**2+at(n)*at(n+2)
            for n in range(len(h))]


assert H([2, 2, 1]) == [4, 2, 1]
assert [4-2, 2-1, 1] == [2, 1, 1]
assert H([3, 4, 2]) == [7, 4, 2]
assert defects([7, 4, 2]) == [31, -2, 4]
assert [7*6-4*9, 4*2-2*6] == [6, -4]
assert 29-2*58 == -87
print('PASS: exact symbolic strip identities and canonical residual obstruction.')
