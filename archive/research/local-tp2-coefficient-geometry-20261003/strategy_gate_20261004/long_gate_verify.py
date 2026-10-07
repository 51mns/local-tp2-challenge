#!/usr/bin/env python3
"""Exact bounded LONG bridge obstructions; no state-family scan."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]: p.pop()
    return p

def add(*ps):
    q = [0] * max(map(len, ps))
    for p in ps:
        for i, c in enumerate(p): q[i] += c
    return trim(q)

def scale(p, c): return trim([c*a for a in p])
def sub(p, q): return add(p, scale(q, -1))

def mul(*ps):
    q = [1]
    for p in ps:
        z = [0] * (len(q)+len(p)-1)
        for i, a in enumerate(q):
            for j, b in enumerate(p): z[i+j] += a*b
        q = trim(z)
    return q

def H(p):
    return trim([sum(p[j]*comb(j, (j-n)//2)
                     for j in range(n, len(p), 2)) for n in range(len(p))])

def at(h, n): return h[abs(n)] if abs(n) < len(h) else 0
def W(f, g, i, j): return at(f,i)*at(g,j)-at(f,j)*at(g,i)
def defects(p):
    a = H(p)
    return [at(a,n)**2-at(a,n-1)*at(a,n+1)-at(a,n+1)**2
            +at(a,n)*at(a,n+2) for n in range(len(a))]

def relative(*pairs):
    rows = [(H(p),H(q)) for p,q in pairs]
    size = max(max(len(p),len(q)) for p,q in rows)
    vals = {(i,j):sum(W(p,q,i,j) for p,q in rows)
            for i in range(size) for j in range(i+1,size)}
    return vals

def weak(*pairs): return all(v >= 0 for v in relative(*pairs).values())
def cone(p): return weak((p,mul([0,1],p)))
def adjacent(p,q):
    a,b=H(p),H(q)
    return [W(a,b,n,n+1) for n in range(len(a))]

one=[1];x=[0,1];y=[1,1];P=[2,1]

def canonical(a,e,r):
    X=add(one,mul(y,a)); Y=add(X,mul(y,e))
    t=sub(scale(mul(y,X),3),x); A=sub(t,[2])
    k=mul(X,sub(scale(X,3),[2]));g=add(mul(A,e),k,r)
    s=sub(mul(t,g),r); C=add(Y,mul(y,g))
    T=sub(scale(mul(y,C),3),x); M=add(T,one)
    E,G,R,S=[mul(y,f) for f in (e,g,r,s)]
    return dict(a=a,e=e,r=r,X=X,Y=Y,A=A,k=k,g=g,s=s,
                C=C,M=M,E=E,G=G,R=R,S=S,Q=sub(S,G),D=mul(E,M))

def relaxed_chain_obstruction():
    h=mul(y,sub(scale(P,3),one));Q=P;D=mul(P,P,P,P)
    B=mul(h,Q);V=mul(h,D);U=mul(h,add(Q,D))
    C7=[0,-7,0,14,0,-7,0,1]
    K=add(V,scale(C7,Fraction(1,100)))
    qc=add(U,B);dc=add(V,K)
    for p in (h,Q,D,B,U,V,K,qc,dc):
        assert all(c>0 for c in p)
        assert all(c>0 for c in H(p))
    for p in (h,Q,D,B,V,K,qc,dc): assert cone(p)
    assert all(v>0 for v in adjacent(Q,D))
    assert weak((B,U)) and weak((U,V)) and weak((V,K))
    assert len(qc)-1==6 and len(dc)-1==7
    assert adjacent(qc,dc)[4:6]==[0,0]
    # tau=h+1, r in [-2,2]: tau-r=h+c, c in [-1,3].
    # Defects are (c^2+25c+26,22-3c,9); positive on this interval.
    assert defects(add(h,[-1]))==[2,25,9]
    assert defects(add(h,[3]))==[110,13,9]
    assert min(25+2*c for c in (-1,3))>0
    return dict(domain='RELAXED source-chain algebra, not canonical P_0',
                h=h,Q=Q,D=D,B=B,K=K,Q_child=qc,D_child=dc,
                parent_strict_adjacent=adjacent(Q,D),
                B_U_adjacent=adjacent(B,U),U_V_adjacent=adjacent(U,V),
                V_K_adjacent=adjacent(V,K),
                child_adjacent=adjacent(qc,dc),
                trace_shift_defects=['c^2+25c+26','22-3c','9'],
                trace_shift_domain=[-1,3],central_flag=2,
                zero_target_indices=[4,5],
                missing_canonical_premises=['Fricke','normalized ancestry',
                    'origin registers and paired MP_0','B=A_L G-E',
                    'K=M(G-hE)+3yG(S+D)'])

def canonical_low_block_obstruction():
    # Genuine first SHORT parent; its stronger full packet/P_0 certificate
    # is an inherited audited seed, not inferred from finite checks here.
    root=canonical([0],[1],[1])
    st=canonical(root['a'],add(root['e'],root['g']),root['g'])
    h=sub(scale(mul(y,st['Y']),3),add(x,one))
    F=add(st['S'],st['D']);J=add(st['E'],st['G'])
    ql=sub(mul(h,F),J); dl=mul(st['G'],add(st['M'],scale(mul(y,F),3)))
    lo=canonical(add(st['a'],st['e']),st['g'],add(st['e'],st['g']))
    assert ql==lo['Q'] and dl==lo['D']
    fricke=sub(mul(st['r'],st['g']),add(mul(st['A'],st['e'],st['e']),
        scale(mul(st['k'],st['e']),2),scale(mul(st['a'],st['X'],st['X']),3)))
    assert fricke==[0]
    for p,q in ((st['E'],st['G']),(st['R'],st['G']),
                (mul(st['X'],P),st['E']),(mul(st['Y'],P),st['G'])):
        assert weak((p,q))
    assert cone(st['G']) and cone(st['M'])
    assert all(v>0 for v in adjacent(st['Q'],st['D']))
    low=mul(st['G'],st['M']);high=scale(mul(y,st['G'],F),3)
    assert relative((ql,low))[(0,1)] == -1074148800
    assert relative((dl,J))[(0,1)] == -49976016
    assert weak((mul(h,F),dl)) and weak((ql,dl))
    assert weak((ql,high))
    return dict(domain='CANONICAL first SHORT parent',parent_a=st['a'],
                parent_e=st['e'],parent_r=st['r'],Fricke_residual=fricke,
                inherited_full_packet_source='../common_defect_20261004/ROOT_AUDIT.md Sections 1,5',
                central_selector_columns=[0,1],
                central_selector_characters=[0,0],
                complete_low_M_block=-1074148800,
                subtraction_block=-49976016,
                total_child_adjacent=adjacent(ql,dl),
                tested_obstruction='separate nonnegativity of the complete coupled M block')

if __name__=='__main__':
    result=dict(status='PASS exact two bounded bridge obstructions',
                relaxed_chain=relaxed_chain_obstruction(),
                canonical_low_block=canonical_low_block_obstruction(),
                arbitrary_LONG_Q_D='OPEN',full_tree_Local_TP2='OPEN')
    out=HERE/'long_gate_results.json'
    out.write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps(result,indent=2,default=str))
