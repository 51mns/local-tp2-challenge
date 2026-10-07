#!/usr/bin/env python3
"""Exact identity checks for packet_transport_subgate.md.

These finite symbolic checks validate displayed algebra and normalization.
The all-N Robin cone proof is the analytic argument in the accompanying note.
No finite output is used as an all-state closure claim.
"""
import json
from pathlib import Path
from itertools import permutations


class Poly:
    """Small exact sparse polynomial ring over Z; no external dependency."""
    NV=32
    names={}
    def __init__(self, terms):
        self.terms={k:v for k,v in terms.items() if v}
    @classmethod
    def const(cls,n):
        return cls({(0,)*cls.NV:n})
    @classmethod
    def var(cls,name):
        if name not in cls.names:cls.names[name]=len(cls.names)
        k=[0]*cls.NV;k[cls.names[name]]=1
        return cls({tuple(k):1})
    @classmethod
    def coerce(cls,p):return p if isinstance(p,cls) else cls.const(p)
    def __add__(self,p):
        p=self.coerce(p);out=dict(self.terms)
        for k,v in p.terms.items():out[k]=out.get(k,0)+v
        return Poly(out)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.terms.items()})
    def __sub__(self,p):return self+-self.coerce(p)
    def __rsub__(self,p):return self.coerce(p)+-self
    def __mul__(self,p):
        p=self.coerce(p);out={}
        for k,v in self.terms.items():
            for l,w in p.terms.items():
                z=tuple(a+b for a,b in zip(k,l))
                out[z]=out.get(z,0)+v*w
        return Poly(out)
    __rmul__=__mul__
    def __pow__(self,n):
        out=Poly.const(1)
        for _ in range(n):out=out*self
        return out
    def __bool__(self):return bool(self.terms)


def symbols(names):return tuple(Poly.var(n) for n in names.split())


def determinant(mat):
    out=Poly.const(0);N=len(mat)
    for perm in permutations(range(N)):
        term=Poly.const(1)
        for i,j in enumerate(perm):
            if not mat[i][j]:break
            term=term*mat[i][j]
        else:
            sign=(-1)**sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
            out=out+sign*term
    return out


def check_zero(expr):
    assert not expr, len(expr.terms)


def run():
    x, a, e, r = symbols('x a e r')
    y=x+1; beta=3*y*y; X=1+y*a
    t=2*x+3+beta*a
    g=(t-2)*e+X*(3*X-2)+r
    s=t*g-r
    C=1+y*(a+e+g); T=3*y*C-x
    d=e*(T+1); c=e+g+s; cB=c+T*e
    checks=[]
    alpha, omega, r0=symbols('alpha omega r0')
    for sigma in (0,1):
        n=g+(1-sigma)*e; v=s+sigma*d
        u=T-beta*n; h=(1-2*sigma)*e; p=n+v
        check_zero(p-c-sigma*T*e)
        new_a=a+sigma*e
        new_e=n
        new_r=g if sigma==0 else e+g
        new_X=1+y*new_a
        new_t=2*x+3+beta*new_a
        new_g=(new_t-2)*new_e+new_X*(3*new_X-2)+new_r
        new_s=new_t*new_g-new_r
        new_C=1+y*(new_a+new_e+new_g)
        new_T=3*y*new_C-x
        new_c=new_e+new_g+new_s
        f=(u+1)*v+h
        check_zero(new_T-(u+beta*p))
        check_zero(new_c-f)
        check_zero(n*(new_T-r0)+f-((T-r0)*n+(T+1)*v+h))
        check_zero(n*(new_T-r0)+f-(p*(T-r0)+h+(r0+1)*v))
        check_zero(n*(new_T+1)+f-((T+1)*c+e if sigma==0 else (T+1)*cB-e))
        checks.append({'sigma':sigma,'normalized_transport_identities':6})

    # Reverse midpoint identity checked independently in the correlated
    # abstract ring T,beta,n,v,h, with p=n+v and u=T-beta*n.
    tv,bv,nv,vv,hv=symbols('tv bv nv vv hv')
    pv=nv+vv;uv=tv-bv*nv;fv=(uv+1)*vv+hv;tp=tv+bv*vv
    baseL=pv*(tv-alpha)+hv
    baseH=pv*((tv-alpha)**2-omega)+hv*(tv-alpha)
    reverseH=nv*((tp-alpha)**2-omega)+fv*(tp-alpha)
    residual=((alpha+1)*(tv-alpha)+omega)*vv+bv*vv*baseL+bv*(alpha+1)*vv*vv
    check_zero(reverseH-baseH-residual)

    # The tensor/character equality is verified BEFORE the linear rotation.
    H0x,H0z,A1x,A1z,zx,zz,bx,bz,ex,ez=symbols('H0x H0z A1x A1z zx zz bx bz ex ez')
    Hx=H0x+zx*A1x+zx**2*bx
    Hz=H0z+zz*A1z+zz**2*bz
    rhs=(H0x*H0z-omega*ex*ez
         +H0x*zz*A1z+zx*A1x*H0z
         +H0x*zz**2*bz+zx**2*bx*H0z
         +zx*zz*A1x*A1z
         +zx*A1x*zz**2*bz+zx**2*bx*zz*A1z
         +zx**2*zz**2*bx*bz)
    check_zero(Hx*Hz-omega*ex*ez-rhs)

    q, rho, b0, b1=symbols('q rho b0 b1')
    U=[Poly.const(1),q]
    for j in range(2,9): U.append(q*U[-1]-U[-2])
    robin_checks=[]
    for N in range(1,8):
        mat=[[Poly.const(0) for _ in range(N)] for _ in range(N)]
        for j in range(N-1):mat[j][j+1]=mat[j+1][j]=Poly.const(1)
        mat[N-1][N-1]=rho
        charmat=[[((q if i==j else 0)-mat[i][j]) for j in range(N)] for i in range(N)]
        pn=U[N]-rho*U[N-1]
        check_zero(determinant(charmat)-pn)
        prev=Poly.const(1) if N==1 else U[N-1]-rho*U[N-2]
        minor=Poly.const(1) if N==1 else determinant([row[1:] for row in charmat[1:]])
        check_zero(minor-prev)
        qN=b0*U[N]+b1*U[N-1]
        qprev=b0*U[N-1]+(b1*U[N-2] if N>=2 else 0)
        check_zero(qN-rho*qprev-(b0*pn+b1*prev))
        robin_checks.append(N)
    check_zero((T+1)*cB-e-(e*(T*T+T-1)+c*(T+1)))

    # Verify window identities for abstract solutions with q_-1=-b1.
    # The general identities follow from the recurrence, not this finite check.
    seq=[b0,b0*q+b1]
    for j in range(2,12):seq.append(q*seq[-1]-seq[-2])
    window_checks=0
    for m in range(1,4):
        for ell in range(1,8):
            k=ell//2
            if ell%2:
                factor=U[k]+(U[k-1] if k else 0)
                rhs=factor*seq[m+k]
            else:
                rhs=U[k-1]*(seq[m+k]+seq[m+k-1])
            check_zero(sum(seq[m:m+ell])-rhs)
            window_checks+=1
    return {'status':'exact symbolic checks PASS',
            'both_mutations':checks,
            'tensor_flux_identity':True,
            'reverse_midpoint_flux_identity':True,
            'long_robin_minus_one_identity':True,
            'robin_characteristic_normalizations':robin_checks,
            'window_normalizations':window_checks,
            'scope':'analytic Robin theorem proves BOTH reverse L_-1 subgate; full regular MP2 transport OPEN'}


if __name__=='__main__':
    result=run()
    path=Path(__file__).with_name('packet_transport_subgate_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
