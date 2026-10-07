#!/usr/bin/env python3
"""Exact canonical witness for two invalid SHORT D-advance factorizations.
No scans, floating arithmetic, external packages, or child packet assumptions.
"""
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(*aa):
    z=[0]*max(map(len,aa))
    for a in aa:
        for i,v in enumerate(a): z[i]+=v
    return trim(z)

def scale(a,k): return trim([k*v for v in a])
def sub(a,b): return add(a,scale(b,-1))
def mul(*aa):
    z=[1]
    for a in aa:
        q=[0]*(len(z)+len(a)-1)
        for i,u in enumerate(z):
            for j,v in enumerate(a): q[i+j]+=u*v
        z=trim(q)
    return z

def row(a):
    z=[0]*len(a)
    for k,c in enumerate(a):
        for n in range(k%2,k+1,2): z[n]+=c*comb(k,(k-n)//2)
    return trim(z)

def val(a,n): return a[n] if n<len(a) else 0

def selectors(*pairs):
    rows=[(row(a),row(b)) for a,b in pairs]
    n=max(max(len(a),len(b)) for a,b in rows)
    return {(k,l):sum(val(a,k)*val(b,l)-val(a,l)*val(b,k)
                      for a,b in rows) for k in range(n) for l in range(k+1,n)}

def brief(s):
    nz=[v for v in s.values() if v]
    neg=[dict(columns=list(k),characters=[sum(k)-1,k[1]-k[0]-1],value=v)
         for k,v in s.items() if v<0]
    return dict(checked=len(s),negative_count=len(neg),negative=neg,
                minimum_nonzero=min(nz) if nz else None)

one=[1];x=[0,1];y=[1,1]

def state(a,e,r):
    X=add(one,mul(y,a));Y=add(X,mul(y,e))
    t=sub(scale(mul(y,X),3),x);A=sub(t,[2]);h=add(A,one)
    k=mul(X,sub(scale(X,3),[2]));g=add(mul(A,e),k,r);s=sub(mul(t,g),r)
    C=add(Y,mul(y,g));T=sub(scale(mul(y,C),3),x);M=add(T,one)
    E,G,R,S=[mul(y,z) for z in (e,g,r,s)]
    Q=sub(S,G);D=mul(E,M)
    return locals()

def child(st,long=False):
    if long: return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g']))
    return state(st['a'],add(st['e'],st['g']),st['g'])

def run():
    root=state([0],[1],[1]);st=child(root,True);sh=child(st)
    a,e,r,X,t,A,h,k,g,s,E,G,R,S,T,M,Q,D=[st[z] for z in
       ('a','e','r','X','t','A','h','k','g','s','E','G','R','S','T','M','Q','D')]
    assert a==[1] and e==[3,2] and r==[4,2] and X==[2,1]
    assert sub(mul(r,g),add(mul(A,e,e),scale(mul(k,e),2),scale(mul(a,X,X),3)))==[0]
    # Frozen actual smaller origin P: b0=2P, b1=0, a_O=0, a_X=1, N=2.
    b0=scale(X,2);b1=[0];Z1=b0;Z2=mul(b0,add(t,one))
    assert e==sub(Z1,one)
    assert g==mul(b0,t)
    assert s==mul(b0,sub(mul(t,t),one))
    assert add(a,e,g)==Z2
    H=add(mul(y,k),R);B=sub(T,t);E1=add(E,G)
    assert H==sub(G,mul(A,E)) and E1==add(mul(h,E),H)
    K=add(mul(M,H),mul(B,S));F=mul(h,D)
    assert sh['D']==add(F,K)
    assert sh['Q']==add(mul(h,Q),mul(A,G))
    # Exact conic in fixed-endpoint variables, with the true signed anchor.
    K0=mul(y,k);L0=scale(mul(y,X,X,sub(X,one)),3)
    assert add(mul(E1,E1),mul(E,E))==add(mul(t,E,E1),mul(K0,add(E,E1)),L0)
    factor=selectors((mul(h,E),E1));low=selectors((F,mul(M,H)))
    growth=selectors((F,mul(B,S)));coupled=selectors((F,K))
    assert factor[(0,1)]==-387 and factor[(3,4)]==-18
    assert low[(0,1)]==-2218228656 and low[(8,9)]==-5832
    assert growth[(0,1)]==345828343416
    assert coupled[(0,1)]==343610114760
    assert all(v>=0 for v in coupled.values())
    assert all(coupled.get(q,0)==low.get(q,0)+growth.get(q,0)
               for q in set(coupled)|set(low)|set(growth))
    # Full canonical current companions and strict supported parent Q<D.
    companions={label:brief(selectors((f,z))) for label,f,z in
        [('E_G',E,G),('R_G',R,G),('XP_E',mul(X,[2,1]),E),
         ('YP_G',mul(st['Y'],[2,1]),G)]}
    assert all(v['negative_count']==0 for v in companions.values())
    qd=selectors((Q,D));assert all(qd[(n,n+1)]>0 for n in range(len(Q)))
    return dict(status='PASS exact canonical obstruction to factorwise/sourcewise proofs',
       state='first LONG child of root; ordinary SHORT proposed at this parent',
       origin=dict(endpoint='P=x+2',trace=t,b0=b0,b1=b1,a_O=0,a_X=1,N=2),
       Fricke_residual=0,origin_anchor_residual=0,SHORT_identity_residual=0,
       parent_companions=companions,
       hE_E1=brief(factor),hD_MH=brief(low),hD_BS=brief(growth),hD_K=brief(coupled),
       decisive_coefficients=dict(factor_central=-387,factor_terminal=-18,
           lower_source_central=-2218228656,lower_source_terminal=-5832,
           growth_source_central=345828343416,coupled_central=343610114760),
       scope=dict(proposed_D_advance='OPEN; witness is not a counterexample',
         endpoint_trace_factorization='FALSE on actual fully certified parent',
         separately_nonnegative_MH_source='FALSE on actual fully certified parent',
         arbitrary_parent_SHORT='OPEN',full_tree_Local_TP2='OPEN'))

if __name__=='__main__':
    result=run();HERE.joinpath('short_gate_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','origin','decisive_coefficients','scope')},indent=2))
