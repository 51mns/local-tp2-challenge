"""Exact polynomial-identity certificates in Z[x,u,e,Q], not point sampling.
Only standard-library sparse integer polynomial arithmetic is used.
"""
from __future__ import annotations
from pathlib import Path
import json


class Poly:
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.terms=dict(value.terms)
        elif isinstance(value, int):
            self.terms={(0,0,0,0):value} if value else {}
        elif isinstance(value, dict):
            self.terms={k:v for k,v in value.items() if v}
        else:
            raise TypeError(type(value))
    def __add__(self, other):
        other=Poly(other)
        d=dict(self.terms)
        for k,v in other.terms.items():
            d[k]=d.get(k,0)+v
        return Poly(d)
    __radd__=__add__
    def __neg__(self):
        return Poly({k:-v for k,v in self.terms.items()})
    def __sub__(self, other):
        return self+-Poly(other)
    def __rsub__(self, other):
        return Poly(other)+-self
    def __mul__(self, other):
        other=Poly(other)
        d={}
        for k,v in self.terms.items():
            for l,w in other.terms.items():
                m=tuple(a+b for a,b in zip(k,l))
                d[m]=d.get(m,0)+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self, n):
        if not isinstance(n,int) or n<0:
            raise ValueError(n)
        z=Poly(1)
        for _ in range(n):
            z=z*self
        return z


def variable(i):
    exponents=[0]*4
    exponents[i]=1
    return Poly({tuple(exponents):1})


x,u,e,Q=[variable(i) for i in range(4)]
y=x+1
beta=3*y*y


def data(U,E,V):
    X=1+y*U
    g=2*x+1+beta*U
    t=g+2
    kappa=X*(3*X-2)
    a=V+g*E+kappa
    Y=X+y*E
    C=Y+y*a
    T=Y-y*V
    R=a*V-g*E*E-2*kappa*E-3*U*X*X
    return dict(u=U,e=E,Q=V,X=X,Y=Y,C=C,T=T,g=g,t=t,kappa=kappa,a=a,R=R)


def mutation(X,C,Y):
    return 3*y*X*C-x*(X+C)-Y


def fricke(X,Y,C):
    return X*X+Y*Y+C*C+x*(X*Y+X*C+Y*C)-3*y*X*Y*C


def serial(p):
    return [{'exponents':list(k),'coefficient':v} for k,v in sorted(p.terms.items())]


def main():
    z=data(u,e,Q)
    X,Y,C,T,g,t,k,a,R=(z[n] for n in ('X','Y','C','T','g','t','kappa','a','R'))
    s=data(u,a+e,a)
    l=data(u+e,a,a+e)
    equations={
        'trace':t-(3*y*X-x),
        'inverse':T-(t*Y-x*X-C),
        'I_equals_y_squared_R':fricke(X,Y,C)-y*y*R,
        'R_short_preserved':s['R']-R,
        'R_long_preserved':l['R']-R,
        'short_X':s['X']-X,
        'short_Y':s['Y']-C,
        'short_center':s['C']-mutation(X,C,Y),
        'long_X':l['X']-Y,
        'long_Y':l['Y']-C,
        'long_center':l['C']-mutation(Y,C,X),
        'short_inverse_quotient':s['u']+s['e']-s['Q']-(u+e),
        'long_inverse_quotient':l['u']+l['e']-l['Q']-u,
        'short_endpoint_minus_seed':s['e']-s['Q']-e,
        'long_endpoint_minus_seed':l['e']-l['Q']+e,
        'strong_signed_domination_identity':a-(t-1)*Q-(1+(2*x+3)*u+g*(u+e-Q)),
        'long_endpoint_strong_domination':a+e+(t+beta*e-1)*(e-Q)
            -(1+(2*x+3)*(u+e)+(t+beta*e-2)*(u+e-Q)),
        'seed_norm_with_residual':a*a-t*a*Q+Q*Q-X*X*(1+3*u)+g*R,
        'short_gap':mutation(X,C,Y)-C-y*(t*a-Q),
        'child_difference':mutation(Y,C,X)-mutation(X,C,Y)-y*e*(t+1+beta*(a+e)),
        'short_gap_positive_form':t*a-Q-((g+1)*a+g*e+k),
        'root_fricke':data(Poly(0),Poly(1),Poly(1))['R'],
        'root_center':data(Poly(0),Poly(1),Poly(1))['C']-(2*x*x+6*x+5),
    }
    for name,p in equations.items():
        if p.terms:
            raise AssertionError((name,serial(p)))
    maps={
        'a':a,'short_u':s['u'],'short_e':s['e'],'short_Q':s['Q'],
        'long_u':l['u'],'long_e':l['e'],'long_Q':l['Q'],
        'short_gap_quotient':t*a-Q,
        'child_difference_quotient':e*(t+1+beta*(a+e)),
    }
    assert all(v>=0 for p in maps.values() for v in p.terms.values())
    report={
        'status':'PASS','ring':'Z[x,u,e,Q]',
        'scope':'Exact identities for all substitutions; no evaluation-point sampling and no assertion of full-tree Fourier TP2.',
        'identities':{name:'identically zero' for name in equations},
        'positive_expansions':{name:serial(p) for name,p in maps.items()},
        'fricke_residual':serial(R),
    }
    Path('symbolic_results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','identity_count':len(equations),'positive_maps':len(maps)}))


if __name__=='__main__':
    main()
