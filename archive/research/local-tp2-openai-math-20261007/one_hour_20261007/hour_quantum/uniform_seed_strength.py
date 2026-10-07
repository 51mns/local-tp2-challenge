#!/usr/bin/env python3
"""Finite bridge and exact identities for the all-m L^m R^2 seed theorem.

Standard library only.  The infinite tail m>=29 is proved symbolically in
UNIFORM_SEED_STRENGTH.md, using established one-turn strengths and the new
subtraction lemma.  This script checks all remaining m=0,...,28 and exports
every supported coefficient and scaled defect margin.
"""
from math import comb
from fractions import Fraction
from pathlib import Path
import json


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def add(*ps):
    n=max(map(len,ps))
    out=[0]*n
    for p in ps:
        for i,v in enumerate(p):
            out[i]+=v
    return trim(out)


def scale(p,c):
    return trim([c*v for v in p])


def sub(p,q):
    return add(p,scale(q,-1))


def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return trim(out)


def hrow(p):
    return [sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2))
            for n in range(len(p))]


def get(h,n):
    return h[abs(n)] if abs(n)<len(h) else 0


def delta(h,n):
    return get(h,n)**2-get(h,n-1)*get(h,n+1)-get(h,n+1)**2+get(h,n)*get(h,n+2)


def mutate(A,C,B):
    return sub(sub(scale(mul(mul([1,1],A),C),3),mul([0,1],add(A,C))),B)


def canonical(path):
    A,C,B=[1],[5,6,2],[2,1]
    for step in path:
        if step=='L': A,C,B=A,mutate(A,C,B),C
        else: A,C,B=C,mutate(B,C,A),B
    return A,C,B


def divy(p):
    q=[p[0]]
    for v in p[1:-1]:q.append(v-q[-1])
    assert p[-1]==q[-1]
    assert mul(q,[1,1])==p
    return q


def value2(p):
    return sum(v*2**i for i,v in enumerate(p))


def main():
    # u_m=U_m((2x+3)/2), T_m=sum_{j=0}^m u_j; T_-1=0.
    umax=29
    u=[[1],[3,2]]
    for _ in range(1,umax):u.append(sub(mul([3,2],u[-1]),u[-2]))
    prefix=[]
    accum=[0]
    for p in u:
        accum=add(accum,p)
        prefix.append(accum)
    atT=lambda m:prefix[m] if m>=0 else [0]
    records=[]
    margin_count=0
    for m in range(29):
        y=[1,1]
        Y=add([1],mul(y,atT(m)))
        t=sub(scale(mul(y,Y),3),[0,1])
        aX=add(mul(atT(m+1),add(t,[1])),atT(m-1))
        X=add([1],mul(y,aX))
        A=sub(mul(t,aX),u[m])
        B=u[m+1]
        originalX,originalC,originalY=canonical('L'*m+'RR')
        assert (X,Y)==(originalX,originalY)
        assert A==divy(sub(originalC,Y))
        originalold=canonical('L'*m)[1]
        assert B==divy(sub(originalold,Y))
        assert A==sub(mul(add(t,[1]),add(mul(atT(m+1),t),atT(m-1))),atT(m))
        assert len(A)-1==3*m+5
        assert all(v>0 for v in A)
        assert all(v>=0 for v in sub(aX,u[m]))
        assert value2(u[m])<=7**m
        record={'m':m,'A_ordinary':A,'B_ordinary':B,'X_ordinary':X,
                'tY_ordinary':t,'aX_ordinary':aX,'rows':{}}
        for name,p in [('A',A),('yA',mul(y,A))]:
            h=hrow(p)
            margins=[32*delta(h,n)-9*8**m*h[n] for n in range(len(h))]
            assert min(margins)>0,(m,name)
            assert all(v>0 for v in h)
            norm_num=59**(3*m+1)
            norm_den=400000000**3*100**(3*m+1)*128*(m+3)**2
            norm_margins=[norm_den*delta(h,n)-norm_num*h[n]**2 for n in range(len(h))]
            assert min(norm_margins)>0,(m,name,'normalized')
            margin_count+=len(margins)
            record['rows'][name]={
                'degree':len(h)-1,'halfrow':h,
                'integer_scaled_margins_32delta_minus_9times8powm_h':margins,
                'minimum_scaled_margin':min(margins),
                'normalized_target_numerator':str(norm_num),
                'normalized_target_denominator':str(norm_den),
                'normalized_integer_margins':norm_margins,
                'minimum_exact_strength':str(min(Fraction(delta(h,n),h[n]) for n in range(len(h))))}
        records.append(record)

    # Exact scalar tail gate.  Its consecutive ratio is 8/7 > 1.
    tail_lhs=9*8**29
    tail_rhs=384*7**29
    assert tail_lhs>tail_rhs
    assert 9*8**28<384*7**28
    result={
        'statement':'A_m and (x+1)A_m are (9/32)*8^m-strong for every integer m>=0',
        'normalized_statement':'eta(A_m),eta((x+1)A_m) >= c0^3 sigma^(3m+1)/(128(m+3)^2) for every m>=0',
        'status':'Complete mathematical proof in UNIFORM_SEED_STRENGTH.md; independent audit pending',
        'finite_range':[0,28],
        'finite_scaled_margin_count':margin_count,
        'finite_records':records,
        'tail_start':29,
        'tail_scalar_gate':{'left_9times8pow29':tail_lhs,'right_384times7pow29':tail_rhs,
                            'strict_surplus':tail_lhs-tail_rhs,'propagation_ratio':'8/7'},
        'scope':'Canonical seeds for all L^m R^2 L^ell rays; not by itself all-m Local TP2',
    }
    path=Path(__file__).with_name('uniform_seed_strength_certificates.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    summary={'status':'PASS','finite_range':[0,28],'scaled_margin_count':margin_count,
             'smallest_scaled_margin':min(rec['rows'][name]['minimum_scaled_margin']
                 for rec in records for name in ['A','yA']),
             'tail_start':29,'tail_gate_strict':True,
             'm0_A':records[0]['A_ordinary'],'m1_A':records[1]['A_ordinary']}
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
