#!/usr/bin/env python3
"""Exact identity replay; not a finite-state proof of child packet closure."""
from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path

NV=8
ZERO=(0,)*NV


class Poly(dict):
    """Independent sparse Z/Q polynomial ring, copied/adapted from audit lane."""
    def __add__(self,other):
        other=aspoly(other)
        out=dict(self)
        for k,v in other.items():
            out[k]=out.get(k,0)+v
        return Poly({k:v for k,v in out.items() if v})
    __radd__=__add__

    def __neg__(self):
        return Poly({k:-v for k,v in self.items()})

    def __sub__(self,other):
        return self+-aspoly(other)

    def __rsub__(self,other):
        return aspoly(other)+-self

    def __mul__(self,other):
        other=aspoly(other)
        out={}
        for ka,va in self.items():
            for kb,vb in other.items():
                k=tuple(i+j for i,j in zip(ka,kb))
                out[k]=out.get(k,0)+va*vb
        return Poly({k:v for k,v in out.items() if v})
    __rmul__=__mul__

    def __pow__(self,n):
        assert n>=0
        out=aspoly(1)
        for _ in range(n):
            out*=self
        return out

    def __truediv__(self,n):
        return self*Fraction(1,n)

    def scalar(self):
        assert not any(any(k) for k in self)
        return self.get(ZERO,Fraction(0))

    def __gt__(self,other):
        return self.scalar()>aspoly(other).scalar()

    def __lt__(self,other):
        return self.scalar()<aspoly(other).scalar()

    def __str__(self):
        return str(self.scalar()) if all(not any(k) for k in self) else dict.__repr__(self)

    def subs(self,symbol,value):
        index=next(i for i,v in enumerate(next(iter(symbol))) if v)
        out={}
        for key,val in self.items():
            power=key[index]
            key=list(key)
            key[index]=0
            key=tuple(key)
            out[key]=out.get(key,0)+val*Fraction(value)**power
        return Poly({k:v for k,v in out.items() if v})


def aspoly(value):
    if isinstance(value,Poly):
        return value
    return Poly({ZERO:Fraction(value)}) if value else Poly()


def var(i):
    key=list(ZERO)
    key[i]=1
    return Poly({tuple(key):Fraction(1)})


def collapse(value):
    p=aspoly(value)
    return p.scalar() if all(not any(k) for k in p) else p


class UniPoly:
    def __init__(self,p,unused=None):
        self.p=aspoly(p)
        self.is_zero=not self.p

    def degree(self):
        return max((k[0] for k in self.p),default=0)

    def nth(self,n):
        out={}
        for k,v in self.p.items():
            if k[0]==n:
                kk=(0,)+k[1:]
                out[kk]=out.get(kk,0)+v
        return Poly(out)

    def LC(self):
        return self.nth(self.degree())


class ExactRing:
    # Small syntax shim; everything is Python arbitrary-precision Fraction.
    Integer=Fraction
    Rational=Fraction
    Poly=UniPoly
    expand=staticmethod(aspoly)
    degree=staticmethod(lambda p,unused=None: UniPoly(p).degree())
    Symbol=staticmethod(lambda name: var(0 if name=="x" else 1))
    symbols=staticmethod(lambda names: tuple(var(i) for i in
                      range(0 if len(names.split())==8 else 1,
                            (0 if len(names.split())==8 else 1)+len(names.split()))))


S=ExactRing()

x = S.Symbol("x")


def zero(expr):
    assert not aspoly(expr), str(expr)


def row(poly):
    p = S.Poly(S.expand(poly), x)
    if p.is_zero:
        return [S.Integer(0)]
    d = p.degree()
    return [collapse(sum(p.nth(i) * comb(i, (i-j)//2)
                         for i in range(j, d+1, 2))) for j in range(d+1)]


def at(a, j):
    j = abs(j)
    return a[j] if j < len(a) else S.Integer(0)


def xrow(a):
    return [2*at(a, 1)] + [at(a, j-1)+at(a, j+1)
                           for j in range(1, len(a)+1)]


def defect(a, j):
    return collapse(at(a,j)**2-at(a,j-1)*at(a,j+1)
                    -at(a,j+1)**2+at(a,j)*at(a,j+2))


def tensor(poly):
    a = row(poly)
    b = xrow(a)
    out = {}
    for k in range(len(a)):
        for l in range(k+1, len(a)+1):
            v = collapse(at(a,k)*at(b,l)-at(a,l)*at(b,k))
            if v:
                ab = (k+l-1, l-k-1)
                out[ab] = v
                out[ab[::-1]] = v
    return out


def lin(*terms):
    out = {}
    for scale, tab in terms:
        for key, val in tab.items():
            out[key] = collapse(out.get(key, 0)+scale*val)
    return {k:v for k,v in out.items() if v}


def mixed(f,g):
    return lin((1,tensor(f+g)),(-1,tensor(f)),(-1,tensor(g)))


def mul(a,b):
    out = {}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            for p in range(abs(i-k),i+k+1,2):
                for q in range(abs(j-l),j+l+1,2):
                    out[p,q] = out.get((p,q),0)+v*w
    return {k:collapse(v) for k,v in out.items() if v}


def same(a,b):
    assert not lin((1,a),(-1,b))


def state(a,e,r):
    y=x+1
    X=1+y*a
    t=3*y*X-x
    k=X*(3*X-2)
    g=(t-2)*e+k+r
    s=t*g-r
    C=X+y*(e+g)
    T=3*y*C-x
    d=e*(T+1)
    c=e+g+s
    F=r*g-(t-2)*e**2-2*k*e-3*a*X**2
    return {key:S.expand(val) for key,val in locals().items()
            if key in ["a","e","r","X","t","k","g","s","C","T","d","c","F"]}


def formal_checks():
    TT,cc,ee,gg,bb,rr=S.symbols("TT cc ee gg bb rr")
    for sigma in (0,1):
        n=gg+(1-sigma)*ee
        v=cc+sigma*TT*ee-n
        h=(1-2*sigma)*ee
        u=TT-bb*n
        Tp=TT+bb*v
        cp=(u+1)*v+h
        B=cc*(TT+1)+ee if sigma==0 else ee*(TT**2+TT-1)+cc*(TT+1)
        zero(n*(Tp-rr)+cp-(B-(rr+1)*n))

    B0,B1,N0,N1,Z0,Z1,th,ph=S.symbols("B0 B1 N0 N1 Z0 Z1 th ph")
    eta=(th+ph)/2
    kap=th*ph
    om=(th-ph)**2/4
    H0=B0*(Z0-eta)-N0*(eta*Z0-kap)
    H1=B1*(Z1-eta)-N1*(eta*Z1-kap)
    seed0=B0-N0*Z0
    seed1=B1-N1*Z1
    A=Z0*Z1-eta*(Z0+Z1)+kap
    K=B0*B1+kap*N0*N1-eta*(B0*N1+N0*B1)
    F=(Z1-Z0)*(B0*N1-N0*B1)
    zero(H0*H1-om*seed0*seed1-(A*K+om*F))
    zero(B0**2-(Z0+1)*N0*B0+(Z0+1)*N0**2
         -(seed0**2+(Z0-1)*N0*seed0+N0**2))

    aa,bbb,ccc,theta=S.symbols("aa bbb ccc theta")
    E=aa-theta*bbb+theta**2*ccc
    t=(theta+1)/4
    zero(E-(E.subs(theta,-1)*(1-t)**2
             +2*(aa-bbb-3*ccc)*t*(1-t)+E.subs(theta,3)*t**2))

    # Independent symbolic trace central normalization, including h_-1=h_1.
    h0,h1,h2,r,s=S.symbols("h0 h1 h2 r s")
    delta=h0**2-2*h1**2+h0*h2
    alpha=(r+s)/2
    omega=(r-s)**2/4
    zero((h0-alpha)**2-2*h1**2+(h0-alpha)*h2-omega
         -(delta-(r+s)*(h0+h2/2)+r*s))

    # Entire tensor trace pair identity over symbolic parameters, not a grid.
    q=S.Rational(7,2)+2*x+x**2
    same(mixed(q-r,q-s),lin((2,tensor(q-alpha)),(-2*omega,tensor(1))))
    return {"both_anchor_identities":2,"mixed_factor_identity":True,
            "strict_copositivity_Bernstein_identity":True,
            "trace_pair_symbolic_tensor":True,"trace_central_identity":True}


def correlated_checks():
    a,e,r=S.symbols("a e r")
    old=state(a,e,r)
    y=x+1
    beta=3*y**2
    Z=a+e+old["g"]
    zero(old["c"]**2+e*(old["T"]*old["c"]+e)
         -old["C"]**2*(1+3*Z)+(old["T"]-2)*old["F"])
    for sigma in (0,1):
        child=state(a+sigma*e,old["g"]+(1-sigma)*e,
                    old["g"]+sigma*e)
        n=old["g"]+(1-sigma)*e
        v=old["s"]+sigma*old["d"]
        u=old["T"]-beta*n
        h=(1-2*sigma)*e
        zero(child["T"]-(old["T"]+beta*v))
        zero(child["c"]-((u+1)*v+h))
        zero(child["F"]-old["F"])
    return {"canonical_child_tuple_off_Fricke":True,
            "Fricke_both_invariance":True,"paired_Cassini_residual":True}


def root_replays():
    old=state(S.Integer(0),S.Integer(1),S.Integer(1))
    out=[]
    for sigma in (0,1):
        name="short" if sigma==0 else "long"
        child=state(sigma,old["g"]+(1-sigma),old["g"]+sigma)
        z=child["T"]+1
        for orient in ("reverse","forward"):
            b0,b1=(child["e"],child["c"]) if orient=="reverse" else (child["c"],child["e"])
            for smoothed in (False,True):
                if smoothed:
                    b0,b1=(x+1)*b0,(x+1)*b1
                B=S.expand(b0*z+b1)
                flux=lin((1,mixed(B,b0*z)),(-1,mixed(B*z,b0)))
                D=S.degree(b0,x)
                dd=S.degree(z,x)
                ff=S.degree(B,x)
                assert ff==D+dd
                ll=ff+dd+1
                coeff=flux.get((ll-1,ll-1),0)
                expected=-row(b0)[0]*S.Poly(B*z,x).LC()
                zero(coeff-expected)
                assert coeff<0
                for r,s in [(S.Integer(-2),S.Integer(2)),(S.Rational(-3,2),S.Rational(5,4))]:
                    th,ph=r+1,s+1
                    eta=(th+ph)/2
                    kap=th*ph
                    om=(th-ph)**2/4
                    H=b0*(child["T"]-r)*(child["T"]-s)+b1*(child["T"]-(r+s)/2)
                    direct=lin((1,tensor(H)),(-om,tensor(b1)))
                    A=lin((1,tensor(z-eta)),(-om,tensor(1)))
                    K=lin((1,tensor(B)),(kap,tensor(b0)),(-eta,mixed(B,b0)))
                    factored=lin((1,mul(A,K)),(om,flux))
                    same(direct,factored)
                    hh=row(H)
                    MM=len(hh)-1
                    lcH=S.Poly(H,x).LC()
                    nb=row(b0)
                    for kk in range(MM+1):
                        character=(kk+MM,MM-kk)
                        zero(flux.get(character,0)+at(nb,kk)*lcH)
                        zero(direct.get(character,0)-hh[kk]*lcH)
                        assert direct.get(character,0)>0
                entry={"child":name,"orientation":orient,"mode":"y" if smoothed else "raw",
                       "degrees":[int(D),int(dd),int(ff)],"far_columns":[0,int(ll)],
                       "flux_far":str(coeff),"flux_central":str(flux.get((0,0),0)),
                       "factor_identity_replays":2,"all_outer_layer_coefficients":True}
                if orient=="reverse":
                    # Exact polynomial theta identity for every asserted upper defect.
                    theta=S.Symbol("theta")
                    lower=int(D)+2
                    top=int(ff)
                    pencil=row(B-theta*b0)
                    base=row(B)
                    for j in range(lower,top+1):
                        zero(defect(pencil,j)-defect(base,j))
                        assert defect(base,j)>0
                    entry["symbolic_upper_tail_defects"]=top-lower+1
                    boundary=int(D)+1
                    zero(defect(pencil,boundary)-defect(base,boundary)
                         -theta*row(b0)[-1]*at(base,boundary+1))
                    entry["extra_boundary_identity_r_ge_minus1"]=True
                out.append(entry)
    return out


def main():
    result={"purpose":"exact algebra and fixed normalization replays, not full closure",
            "arithmetic":"stdlib Fraction sparse polynomial ring; no external dependencies",
            "formal":formal_checks(),"correlations":correlated_checks(),
            "fixed_root_edges":root_replays(),
            "analytical_claims":"See packet_algebra.md; full MP_sharp BOTH closure remains OPEN"}
    path=Path(__file__).with_name("packet_algebra_results.json")
    path.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"formal":result["formal"],"correlations":result["correlations"],
                      "root_edge_orientation_mode_replays":len(result["fixed_root_edges"]),
                      "output":path.name},indent=2))


if __name__=="__main__":
    main()
