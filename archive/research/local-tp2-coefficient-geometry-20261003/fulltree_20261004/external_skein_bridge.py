#!/usr/bin/env python3
"""Exact algebra checks for external_skein_bridge.md; standard library only."""
from __future__ import annotations

import json
from math import comb
from pathlib import Path


class Poly:
    names = ("x", "A", "B", "C", "G", "s", "d")
    zero = (0,) * len(names)

    def __init__(self, terms=0):
        if isinstance(terms, int):
            terms = {self.zero: terms}
        self.terms = {k: v for k, v in terms.items() if v}

    @classmethod
    def variable(cls, name):
        exponent = list(cls.zero)
        exponent[cls.names.index(name)] = 1
        return cls({tuple(exponent): 1})

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly(value)

    def __add__(self, other):
        other = self.coerce(other)
        out = self.terms.copy()
        for exponent, coefficient in other.terms.items():
            out[exponent] = out.get(exponent, 0) + coefficient
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                exponent = tuple(i + j for i, j in zip(a, b))
                out[exponent] = out.get(exponent, 0) + ca * cb
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        out = Poly(1)
        for _ in range(exponent):
            out = out * self
        return out

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def univariate(self):
        assert all(all(e == 0 for e in powers[1:]) for powers in self.terms)
        degree = max((powers[0] for powers in self.terms), default=0)
        out = [0] * (degree + 1)
        for powers, coefficient in self.terms.items():
            out[powers[0]] = coefficient
        return out


def H(polynomial):
    coefficients = polynomial.univariate()
    return [sum(coefficients[j] * comb(j, (j - n) // 2)
                for j in range(n, len(coefficients), 2))
            for n in range(len(coefficients))]


def minors(P, Q):
    p, q = H(P), H(Q)
    at = lambda row, n: row[n] if n < len(row) else 0
    return [at(p, n) * at(q, n + 1) - at(p, n + 1) * at(q, n)
            for n in range(len(p))]


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def main():
    x, A, B, C, G, s, d = map(Poly.variable, Poly.names)
    y = x + 1
    kappa = x * (x + 2)
    omega = 2 * x**3 + 3 * x**2 + 4
    trace = lambda value: 3 * y * value - x
    a, b, c = map(trace, (A, B, C))
    original = A**2 + B**2 + C**2 + x * (A*B + A*C + B*C) - 3*y*A*B*C
    transformed = a**2 + b**2 + c**2 - a*b*c + kappa*(a+b+c) + omega-4
    assert transformed == 9*y**2*original
    U = 3*y*A*C - x*(A+C) - B
    assert trace(U) == a*c-b-kappa
    peripheral = (x, x, x, Poly(2))
    p1, p2, p3, p4 = peripheral
    assert p1*p2+p3*p4 == kappa
    assert p1*p3+p2*p4 == kappa
    assert p1*p4+p2*p3 == kappa
    assert p1*p2*p3*p4 + sum(p*p for p in peripheral) == omega

    # P=QJ and its adjugate. For det(Q)=1, adj(P)=P^(-1).
    P = [[-(s+x), G], [-d, s]]
    adjP = [[s, -G], [d, -(s+x)]]
    K = [[Poly(-1), Poly(0)], [3*y, Poly(-1)]]
    product = mmul(K, adjP)
    assert P[0][0] + P[1][1] == -x
    assert product[0][0] + product[1][1] == x-3*y*G

    z = x+2
    bracelet2 = z**2-2
    bracelet3 = z**3-3*z
    assert bracelet2.univariate() == [2, 4, 1]
    assert bracelet3.univariate() == [2, 9, 6, 1]
    assert H(bracelet2) == [4, 4, 1]
    assert H(bracelet3) == [14, 12, 6, 1]
    assert minors(bracelet2, bracelet3) == [-8, 12, 1]

    raw = minors(y, x*y)
    multiplied = minors(y**2, x*y**2)
    assert raw == [-1, 1]
    assert multiplied == [4, 0, 1]

    # Use two otherwise independent formal coordinates as U,V.
    u, v = A, B
    image = (u**2+v**2-4)+u*v+1
    chi_expansion = (u**2-1)+(v**2-1)+u*v-1
    assert image == chi_expansion

    result = {
        "status": "PASS",
        "claims": {
            "universal_fricke_residual_identity": True,
            "universal_affine_mutation_identity": True,
            "four_peripheral_specialization": True,
            "monodromy_trace_formula": True,
            "signed_character_normalization": True,
        },
        "bracelet_counterexample": {
            "P": bracelet2.univariate(), "Q": bracelet3.univariate(),
            "H_P": H(bracelet2), "H_Q": H(bracelet3),
            "adjacent_minors": minors(bracelet2, bracelet3),
        },
        "cancellation_counterexample": {
            "before_multiplication": raw,
            "after_multiplication_by_x_plus_one": multiplied,
        },
        "scope": "Algebraic bridge and shortcut obstructions; no full-tree TP2 claim.",
    }
    output = Path(__file__).with_name("external_skein_bridge_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
