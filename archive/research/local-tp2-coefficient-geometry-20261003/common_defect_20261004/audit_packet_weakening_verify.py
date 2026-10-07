#!/usr/bin/env python3
"""Small independent exact algebra audit; no scans or worker imports.

The all-parameter strictness recovery is analytic in the companion note.
This verifier covers its universal quadratic identity, the telescoping
Toeplitz difference, and integer ROOT flags. Three separate worker/root
verifiers already replay the full weaker paired witness.
"""
from fractions import Fraction
from pathlib import Path
import json

NV = 9
ZERO = (0,) * NV


class Poly:
    def __init__(self, terms=None):
        self.terms = {m: Fraction(c) for m, c in (terms or {}).items() if c}

    @staticmethod
    def var(i):
        m = list(ZERO)
        m[i] = 1
        return Poly({tuple(m): 1})

    @staticmethod
    def cast(other):
        return other if isinstance(other, Poly) else Poly({ZERO: other})

    def __add__(self, other):
        terms = dict(self.terms)
        for m, c in self.cast(other).terms.items():
            terms[m] = terms.get(m, 0) + c
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        terms = {}
        for m, c in self.terms.items():
            for n, d in self.cast(other).terms.items():
                k = tuple(a + b for a, b in zip(m, n))
                terms[k] = terms.get(k, 0) + c * d
        return Poly(terms)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Poly.cast(1)
        for _ in range(n):
            out = out * self
        return out

    def __eq__(self, other):
        return self.terms == self.cast(other).terms


def defect(row):
    # Entries h_(j-1),h_j,h_(j+1),h_(j+2), including reflection at j=0.
    a, b, c, d = row
    return b * b - a * c - c * c + b * d


def mixed(a, b):
    return (2*a[1]*b[1] - a[0]*b[2] - b[0]*a[2]
            - 2*a[2]*b[2] + a[1]*b[3] + b[1]*a[3])


def main():
    a = [Poly.var(i) for i in range(4)]
    b = [Poly.var(i+4) for i in range(4)]
    r = Poly.var(8)
    pencil = [u-r*v for u, v in zip(a, b)]
    value = defect(pencil)
    assert value == defect(a) - r*mixed(a, b) + r*r*defect(b)
    assert max(m[8] for m in value.terms) == 2
    constant = {m: c for m, c in value.terms.items() if not m[8]}
    assert Poly(constant) == defect(a)

    # Delta_j - Delta_(j+1) is the folded adjacent defect identically.
    assert defect(a) == (a[1]**2-a[0]*a[2])-(a[2]**2-a[1]*a[3])

    def numeric_defect0(h):
        return h[0]**2-2*h[1]**2+h[0]*h[2]

    flags = {
        "root_current_T_minus_2": {
            "row": [61, 50, 24, 6], "delta0": 185},
        "root_ordinary_P_t_minus_2": {
            "row": [10, 8, 3], "delta0": 2},
    }
    for record in flags.values():
        assert numeric_defect0(record["row"]) == record["delta0"]
        assert record["delta0"] >= 1
    out = {
        "status": "PASS",
        "exact_engine": "independent sparse Fraction polynomial arithmetic",
        "universal_checks": {
            "quadratic_defect_pencil_identity": True,
            "parameter_degree_at_most_two": True,
            "constant_coefficient_is_strict_anchor_defect": True,
            "delta_equals_consecutive_Delta_difference": True,
        },
        "root_central_flags": flags,
        "scope": "symbolic identities and ROOT flags; arbitrary-degree spectral/CB and continuum proof are analytic in audit_packet_weakening.md",
        "remaining": ["BOTH new paired W_0 packets", "BOTH strict Q_child<D_child"],
        "full_tree_strict_local_tp2": "OPEN",
    }
    target = Path(__file__).with_name("audit_packet_weakening_results.json")
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"status": out["status"], "results": target.name}, sort_keys=True))


if __name__ == "__main__":
    main()
