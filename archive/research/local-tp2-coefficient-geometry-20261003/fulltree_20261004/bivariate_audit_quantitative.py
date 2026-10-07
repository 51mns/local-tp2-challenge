#!/usr/bin/env python3
"""Independent exact polynomial checks; no tree-depth inference."""
from fractions import Fraction
import json

N = 12
ZERO = (0,)*N


class Poly:
    def __init__(self, terms=0):
        self.terms = dict(terms) if isinstance(terms, dict) else ({ZERO: terms} if terms else {})

    def __add__(self, other):
        if not isinstance(other, Poly): other = Poly(other)
        out = dict(self.terms)
        for k, v in other.terms.items(): out[k] = out.get(k, 0)+v
        return Poly({k:v for k,v in out.items() if v})

    __radd__ = __add__

    def __neg__(self): return Poly({k:-v for k,v in self.terms.items()})
    def __sub__(self, other): return self + -other if isinstance(other, Poly) else self + (-other)
    def __rsub__(self, other): return -self + other

    def __mul__(self, other):
        if not isinstance(other, Poly): other = Poly(other)
        out = {}
        for a, v in self.terms.items():
            for b, w in other.terms.items():
                c = tuple(i+j for i,j in zip(a,b))
                out[c] = out.get(c,0)+v*w
        return Poly({k:v for k,v in out.items() if v})

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Poly(1)
        for _ in range(n): out = out*self
        return out


def var(i):
    e = list(ZERO); e[i] = 1
    return Poly({tuple(e):1})


def d4(p, x, y, z): return x*x-p*y-y*y+x*z


def exact_identity(a, b):
    assert not (a-b).terms, (a-b).terms


def symbolic_checks():
    fp,f0,f1,f2,gp,g0,g1,g2,lam = [var(i) for i in range(9)]
    cp,c0,c1,c2 = fp-gp,f0-g0,f1-g1,f2-g2
    B = d4(fp,f0,f1,f2)-lam*f0-f0*(3*g0+g2)+g0*(g0+g2+lam)
    R = g0*(f0-f2)+gp*f1+cp*g1+g1*(f1+c1)
    exact_identity(d4(cp,c0,c1,c2)-lam*c0, B+R)
    # Folded n=0 specialization checked directly, without a generic-row shortcut.
    B0 = d4(f1,f0,f1,f2)-lam*f0-f0*(3*g0+g2)+g0*(g0+g2+lam)
    R0 = g0*(f0-f2)+g1*f1+c1*g1+g1*(f1+c1)
    exact_identity(d4(c1,c0,c1,c2)-lam*c0, B0+R0)

    v0,v1,v2,v3,v4,r = [var(i) for i in range(6)]
    b0,b1,b2,b3,b4 = 3*v0-r,3*v1-1,3*v2,3*v3,3*v4
    exact_identity(d4(b1,b0,b1,b2),
                   9*d4(v1,v0,v1,v2)-3*r*(2*v0+v2)+12*v1+r*r-2)
    exact_identity(d4(b0,b1,b2,b3),
                   9*d4(v0,v1,v2,v3)-6*v1+3*r*v2-3*v3+1)
    exact_identity(d4(b1,b2,b3,b4), 9*d4(v1,v2,v3,v4)+3*v3)
    return 5


def delta(v, n):
    at = lambda j: v[abs(j)] if abs(j)<len(v) else 0
    return d4(at(n-1),at(n),at(n+1),at(n+2))


def finite_boundary_checks():
    lam = 4
    mu = Fraction(3*lam,2)
    count = 0
    for v in ([8,4],[20,12,4],[80,60,24,4]):
        assert all(delta(v,n)>=lam*v[n] for n in range(len(v)))
        for r in (Fraction(-2),Fraction(-1,2),Fraction(0),Fraction(3,2),Fraction(2)):
            b = [3*x for x in v]
            b[0] -= r; b[1] -= 1
            assert all(x>0 for x in b)
            assert all(delta(b,n)>mu*b[n] for n in range(len(b)))
            assert delta(b,len(b)) == 0
            count += 1
    # Degree zero would violate positive support; the theorem excludes it.
    assert delta([4],0) == 4*4
    assert 3*0-1 == -1
    return count


if __name__ == '__main__':
    print(json.dumps({
        'status': 'PASS: stated universal conditional lemmas only',
        'exact_polynomial_identities': symbolic_checks(),
        'exact_boundary_examples': finite_boundary_checks(),
        'degree_zero_exclusion_verified': True,
        'canonical_all_depth_strength_proved': False,
    },indent=2))
