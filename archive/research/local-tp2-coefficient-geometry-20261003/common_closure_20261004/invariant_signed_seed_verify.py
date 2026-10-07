#!/usr/bin/env python3
"""Exact, self-contained algebra and counterexample replay; no tree scan."""
from fractions import Fraction
from math import comb
import json

NV = 4
ZERO = (0,) * NV
def C(n): return {ZERO: n} if n else {}
def V(i):
    e = [0] * NV; e[i] = 1
    return {tuple(e): 1}
def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items(): out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}
def sc(p, n): return {k: n*v for k, v in p.items() if n*v}
def sub(p,q): return add(p,sc(q,-1))
def mul(*ps):
    out = C(1)
    for p in ps:
        nxt = {}
        for k,v in out.items():
            for l,w in p.items():
                z = tuple(a+b for a,b in zip(k,l))
                nxt[z] = nxt.get(z,0)+v*w
        out = {k:v for k,v in nxt.items() if v}
    return out
def sq(p): return mul(p,p)

x,a,e,r = map(V,range(NV))
y=add(x,C(1)); y2=sq(y); z=add(sc(x,2),C(3))
X=add(C(1),mul(y,a)); t=add(z,sc(mul(y2,a),3))
k=mul(X,sub(sc(X,3),C(2)))
g=add(mul(sub(t,C(2)),e),k,r)
s=sub(mul(t,g),r)
M=add(t,C(1),sc(mul(y2,add(e,g)),3)); D=mul(e,M)
tau=add(t,sc(mul(y2,e),3)); c=add(e,g); eta=sub(e,r)
Y=add(C(1),mul(y,add(a,e)))
F=sub(mul(r,g),add(mul(sub(t,C(2)),sq(e)),sc(mul(k,e),2),sc(mul(a,sq(X)),3)))
assert not sub(add(s,D),add(mul(tau,c),eta))
assert not add(sub(add(sq(c),mul(eta,add(s,D))),mul(sq(Y),add(C(1),sc(add(a,e),3)))),mul(sub(tau,C(2)),F))
# eta is reset by either mutation, without imposing Fricke.
assert not sub(sub(add(e,g),g),e)
assert not sub(sub(g,add(e,g)),sc(e,-1))
T=sub(M,C(1)); Z=add(a,e,g); center=add(C(1),mul(y,Z))
cA=add(e,g,s); cB=add(g,s,D)
KC=mul(sq(center),add(C(1),sc(Z,3)))
assert not sub(cB,add(cA,mul(T,e)))
assert not add(sub(add(sq(cA),mul(e,add(mul(T,cA),e))),KC),mul(sub(T,C(2)),F))
assert not add(sub(add(sq(cB),sc(mul(e,mul(T,cB)),-1),sq(e)),KC),mul(sub(T,C(2)),F))
beta=sub(sub(e,a),C(1))
deficit=sub(mul(T,e),cA)
positive_decomp=add(sc(mul(y2,sq(e)),3),mul(add(sc(sq(x),3),sc(x,4)),g),e,sc(k,-1),sc(mul(y2,beta,g),3))
assert not sub(deficit,positive_decomp)
assert not sub(sub(g,mul(sub(z,C(2)),add(a,e))),add(sc(mul(y2,a,add(a,e)),3),C(1),mul(z,a),r))

def trim(p):
    while len(p)>1 and not p[-1]: p.pop()
    return p
def pa(p,q):
    v=[0]*max(len(p),len(q))
    for i,c in enumerate(p):v[i]+=c
    for i,c in enumerate(q):v[i]+=c
    return trim(v)
def ps(p,q):return pa(p,[-c for c in q])
def pm(p,q):
    v=[0]*(len(p)+len(q)-1)
    for i,c in enumerate(p):
        for j,d in enumerate(q):v[i+j]+=c*d
    return trim(v)
def H(p):
    v=[0]*len(p)
    for j,c in enumerate(p):
        for k in range(j//2+1):v[j-2*k]+=c*comb(j,k)
    return trim(v)
def at(h,n):
    n=abs(n)
    return h[n] if n<len(h) else 0
def delta(h):return [at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2) for n in range(len(h))]
def gate(h,b):
    dh=delta(h)
    lam=min(Fraction(v,c) for v,c in zip(dh,h) if c)
    alpha=min(Fraction(at(h,n),v) for n,v in enumerate(b) if v)
    return {'lambda':[lam.numerator,lam.denominator], 'alpha':[alpha.numerator,alpha.denominator], 'b0':b[0], 'gate':lam*alpha>=8*b[0]}

us=[[1],[3,2]]
for n in range(1,14):us.append(ps(pm([3,2],us[-1]),us[-2]))
records=[]
for m in range(13):
    records.append({'m':m,'plain':gate(H(us[m+2]),H(us[m])), 'smooth':gate(H(pm([1,1],us[m+2])),H(pm([1,1],us[m])))})
root_packet=ps(pm([3,2],pm([1,2],[1,2])),[5,2])
assert root_packet==[-2,12,20,8]
assert delta(H(root_packet))[0]==-388

# Stronger analytic obstruction: alpha <=49 and lambda <=2^(m+2).
assert 3**6 > Fraction(49,2)*(2*6+1)
assert 3**5 > Fraction(49,6)*(2*5+3)
result={'symbolic_checks':9,'root_X_packet':{'parameters':[2,2,-2],'polynomial':root_packet,'half_row':H(root_packet),'defects':delta(H(root_packet))}, 'coarse_gate_records':records,'analytic_obstruction_plain_from_m':6,'analytic_obstruction_smooth_from_m':5,'scope':'Symbolic identities and analytic scalar gates; bounded records only replay minimal coarse failures.'}
print(json.dumps(result,indent=2))
