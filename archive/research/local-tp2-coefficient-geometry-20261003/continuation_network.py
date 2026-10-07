#!/usr/bin/env python3
"""Exact integer-polynomial checks for continuation_network.md.

No package or companion-script dependencies.
Finite checks validate examples and implementation; infinite identities have
algebraic proofs in the companion note.
"""
from __future__ import annotations
import json
from math import comb

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,k):return trim([k*z for z in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return trim(out)
def H(p):
    return trim([sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2)) for n in range(len(p))])
def mutation_left(a,c,b):
    return sub(sub(mul([3,3],mul(a,c)),mul([0,1],add(a,c))),b)
def mutation_right(a,c,b):
    return sub(sub(mul([3,3],mul(c,b)),mul([0,1],add(c,b))),a)

def mt(a): return [list(x) for x in zip(*a)]
def mm(a,b):
    return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def ms(a,b): return [[sub(a[i][j],b[i][j]) for j in range(2)] for i in range(2)]
def det(a): return sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
def trace(a): return add(a[0][0],a[1][1])
def inv(a):
    assert det(a)==[1]
    return [[a[1][1],scale(a[0][1],-1)],[scale(a[1][0],-1),a[0][0]]]
def divy(p):
    assert len(p)>1
    q=[p[0]]
    for c in p[1:-1]: q.append(c-q[-1])
    assert p[-1]==q[-1]
    while len(q)>1 and q[-1]==0:q.pop()
    return q

def pair_minors(p,q):
    a,b=H(p),H(q)
    get=lambda v,i:v[i] if i<len(v) else 0
    return [get(a,i)*get(b,i+1)-get(a,i+1)*get(b,i) for i in range(max(len(a),len(b))-1)]

T=[[[3,3],[-1]],[[1],[0]]]
J=[[[0],[1]],[[-1],[0]]]
K=[[[-1],[0]],[[3,3],[-1]]]
A0=[[[1],[0]],[[0,-1],[1]]]
B0=[[[2,1],[1,1]],[[1],[1]]]
def medi(a,b):return mm(mm(mt(a),T),mt(b))

def check(max_depth=6):
    count=0;max_deg=0;naive_obstructions={}
    stack=[(A0,medi(A0,B0),B0,'')]
    while stack:
        a,c,b,path=stack.pop();count+=1;max_deg=max(max_deg,len(c[0][0])-1)
        l,r=medi(a,c),medi(c,b)
        for Q in (a,c,b,l,r):
            assert det(Q)==[1]
            assert sub(Q[0][1],Q[1][0])==[0,1]
        assert l[0][0]==mutation_left(a[0][0],c[0][0],b[0][0])
        assert r[0][0]==mutation_right(a[0][0],c[0][0],b[0][0])
        pa,pc,pb=[mm(Q,J) for Q in (a,c,b)]
        assert mm(mm(pa,pc),pb)==K
        assert mm(l,J)==mm(mm(pc,pb),inv(pc))
        assert mm(r,J)==mm(mm(inv(pc),pa),pc)
        for Q in (pa,pc,pb):assert trace(Q)==[0,-1]
        for e,p in [(ms(c,a),b[0][0]),(ms(c,b),a[0][0]),(ms(l,c),a[0][0]),(ms(r,c),b[0][0])]:
            assert e==mt(e)
            rhs=scale(mul([1,1],add(scale(p,3),[-2,1])),-1)
            assert det(e)==rhs
        # Fixed-boundary, consecutive left and right symmetric gap transfers.
        assert ms(l,c)==mm(mm(mt(a),T),ms(c,b))
        assert ms(r,c)==mm(ms(c,a),mm(T,mt(b)))
        if path=='':
            s=ms(l,c);d=ms(r,l)
            naive_obstructions={
                'C12_to_C11':pair_minors(c[0][1],c[0][0]),
                'S22_to_S12':pair_minors(s[1][1],s[0][1]),
                'D22_to_D12':pair_minors(d[1][1],d[0][1]),
            }
            assert naive_obstructions=={'C12_to_C11':[-6,4],'S22_to_S12':[-2,2],'D22_to_D12':[162,-54,36]}
        if len(path)<max_depth:
            stack.extend([(a,l,c,path+'L'),(c,r,b,path+'R')])
    return {'nodes':count,'max_depth':max_depth,'max_G_degree':max_deg,'identities_pass':True,'naive_fourier_TP2_obstructions':naive_obstructions,'full_Local_TP2_proved':False}

if __name__=='__main__':print(json.dumps(check(),indent=2))
