#!/usr/bin/env python3
"""Exact symbolic mutation bookkeeping and Jacobi/counterexample replay."""
from fractions import Fraction as F
from math import comb
import json

NV=4; ZZ=(0,)*NV
def C(n): return {ZZ:n} if n else {}
def V(i):
    z=[0]*NV; z[i]=1
    return {tuple(z):1}
def add(*ps):
    z={}
    for p in ps:
        for k,v in p.items(): z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def sc(p,n): return {k:n*v for k,v in p.items() if n*v}
def sub(p,q): return add(p,sc(q,-1))
def mul(*ps):
    z=C(1)
    for p in ps:
        out={}
        for k,v in z.items():
            for l,w in p.items():
                m=tuple(a+b for a,b in zip(k,l))
                out[m]=out.get(m,0)+v*w
        z={k:v for k,v in out.items() if v}
    return z
def sq(p): return mul(p,p)

x,a,e,r=map(V,range(4)); y=add(x,C(1)); beta=sc(sq(y),3); z=add(sc(x,2),C(3))
def state(a,e,r):
    X=add(C(1),mul(y,a)); t=add(z,mul(beta,a)); k=mul(X,sub(sc(X,3),C(2)))
    g=add(mul(sub(t,C(2)),e),k,r); s=sub(mul(t,g),r)
    M=add(t,C(1),mul(beta,add(e,g))); d=mul(e,M)
    return t,g,s,M,d,sub(M,C(1)),add(e,g,s)
t,g,s,M,d,T,c=state(a,e,r)
center=add(C(1),mul(y,add(a,e,g)))
assert not sub(mul(sub(T,C(2)),add(e,g)),sub(mul(center,sub(sc(center,3),C(2))),add(c,e)))
mutation_checks=[]
for sigma in [0,1]:
    n=add(g,sc(e,1-sigma)); u=add(t,sc(mul(beta,e),sigma))
    v=sub(add(c,sc(mul(T,e),sigma)),n)
    na=add(a,sc(e,sigma)); nr=add(g,sc(e,sigma))
    nt,ng,ns,nM,nd,nT,nc=state(na,n,nr)
    assert not sub(ng,v)
    assert not sub(nT,add(T,mul(beta,v)))
    assert not sub(nc,add(mul(add(u,C(1)),v),sc(e,1-2*sigma)))
    assert not sub(ns,sub(mul(u,v),nr))
    new_endpoint_next=add(mul(T,c),e) if not sigma else add(mul(e,sub(sq(T),C(1))),mul(T,c))
    assert not sub(add(ns,nd),new_endpoint_next)
    mutation_checks.append({'sigma':sigma,'formal_checks':5})

def det(mat):
    if not mat: return C(1)
    out={}
    for j,p in enumerate(mat[0]):
        if p:
            minor=[[v for k,v in enumerate(row) if k!=j] for row in mat[1:]]
            out=add(out,sc(mul(p,det(minor)),(-1)**j))
    return out
tt,rr,ss=V(0),V(1),V(2)
us=[C(1),tt]
for n in range(1,6): us.append(sub(mul(tt,us[-1]),us[-2]))
jacobi_checks=[]
for n in range(1,5):
    mat=[[{} for j in range(n)] for i in range(n)]
    for i in range(n):mat[i][i]=sub(tt,rr) if i==n-1 else tt
    for i in range(n-1):mat[i][i+1]=mat[i+1][i]=C(-1)
    assert not sub(det(mat),sub(us[n],mul(rr,us[n-1])))
    jacobi_checks.append({'type':'Robin','vertices':n})
for n in range(1,5):
    size=n+2; mat=[[{} for j in range(size)] for i in range(size)]
    for i in range(n):mat[i][i]=tt
    mat[n][n]=sub(tt,rr);mat[n+1][n+1]=sub(tt,ss)
    for i in range(n-1):mat[i][i+1]=mat[i+1][i]=C(-1)
    # Rational directed entries are diagonally similar to weights 1/sqrt(2).
    for j in [n,n+1]:mat[n-1][j]=C(-1);mat[j][n-1]=C(F(-1,2))
    A=mul(sub(tt,rr),sub(tt,ss)); mean=sc(add(rr,ss),F(1,2))
    chi=sub(mul(us[n],A),mul(us[n-1],sub(tt,mean)))
    assert not sub(det(mat),chi)
    jacobi_checks.append({'type':'forked path','stem_vertices':n})

def pa(p,q):
    return [(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))]
def pm(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out
def H(p):
    out=[F(0)]*len(p)
    for j,c in enumerate(p):
        for k in range(j//2+1):out[j-2*k]+=c*comb(j,k)
    return out
def at(h,n):
    n=abs(n)
    return h[n] if n<len(h) else F(0)
def defects(h):
    return [at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2) for n in range(len(h))]
def pf(v):return [v.numerator,v.denominator]
tau=[F(41,12),F(1)]; seed=[F(5,2),F(1)]; low=[F(17,12),F(1)]
counter=[]
for u in [-2,2]:
    advanced=pm(seed,pa(pm(tau,pm(low,low)),[-tau[0]+u,-1]))
    raw=defects(H(advanced)); smooth=defects(H(pm([1,1],advanced)))
    counter.append({'r':2,'s':2,'u':u,'raw_defects':[pf(v) for v in raw],'smooth_defects':[pf(v) for v in smooth]})
assert counter[0]['raw_defects'][0]==[-1939833799,11943936]
assert counter[1]['raw_defects'][0]==[6959573561,11943936]
assert all(v[0]>0 for v in counter[1]['raw_defects']+counter[1]['smooth_defects'])
result={'formal_ancestry_check':True,'mutation_checks':mutation_checks,'jacobi_characteristic_replay':jacobi_checks,'counterexample':counter,'scope':'Both-child identities are formal; all-N conclusions use analytic recurrences and exact Schur-pivot induction. Matrix sizes above only validate implementation.'}
print(json.dumps(result,indent=2))
