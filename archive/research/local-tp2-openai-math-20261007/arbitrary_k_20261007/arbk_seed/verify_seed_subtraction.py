#!/usr/bin/env python3
"""Finite gates for the all-m, all-j half-defect seed theorem.

Each canonical center is reconstructed by the original symmetric Laurent
mutation.  All arithmetic is integer or Fraction; no sampled roots occur.
"""
import json
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from laurent_arithmetic import get, add, scale, times_y, delta, multiply, digest


def trim(h):
    while len(h)>1 and h[-1]==0:h.pop()
    return h


def sub(h,g):return trim([get(h,n)-get(g,n) for n in range(max(len(h),len(g)))])


def times_x(h):return [get(h,n-1)+get(h,n+1) for n in range(len(h)+1)]


def mutate(A,C,B):return sub(sub(scale(times_y(multiply(A,C)),3),times_x(add(A,C))),B)


def divide_y(h):
    d=len(h)-1;q=[0]*d
    for n in range(d-1,-1,-1):q[n]=h[n+1]-get(q,n+1)-get(q,n+2)
    assert times_y(q)==h
    return q


def certificate(m,j,Z,a):
    output={'m':m,'j':j,'rows':{}}
    assert len(Z)==len(a) and all(v>0 for v in Z+a)
    for name,F,G in [('raw',Z,a),('smoothed',times_y(Z),times_y(a))]:
        margins=[2*delta(G,n)-delta(F,n) for n in range(len(F))]
        assert min(margins)>0,(m,j,name,margins.index(min(margins)))
        output['rows'][name]={'degree':len(F)-1,'half_defect_integer_margins':margins,
                             'seed_halfrow':G,'old_prefix_halfrow':F,
                             'seed_halfrow_sha256':digest(G),
                             'minimum_margin':min(margins),
                             'minimum_margin_index':margins.index(min(margins))}
    return output


def main():
    exceptional={(m,1) for m in range(70)}|{(m,2) for m in range(1,40)}
    exceptional|={(1,j) for j in range(3,8)}|{(2,j) for j in range(3,6)}
    exceptional|={(3,j) for j in range(3,5)}|{(m,3) for m in range(4,7)}
    # The m=0,j>=2 boundary has a separate uniform analytic proof.
    records=[];Y,C=[2,1],[9,6,2]
    for m in range(70):
        T=divide_y(sub(Y,[1]));aold=divide_y(sub(C,[1]))
        prev,current=[1],C
        needed=max(j for mm,j in exceptional if mm==m)
        for j in range(1,needed+1):
            prev,current=current,mutate(Y,current,prev)
            Z=divide_y(sub(current,[1]));a=divide_y(sub(current,Y))
            assert a==sub(Z,T)
            assert len(a)-1==(j+1)*(m+2)-1
            if (m,j) in exceptional:records.append(certificate(m,j,Z,a))
        Y,C=C,mutate([1],C,Y)
    assert len(records)==len(exceptional)
    # Exact corners covering every other m>=1,j>=2.
    corners=[(40,2),(7,3),(4,4),(3,5),(2,6),(1,8)]
    gates=[]
    for m,j in corners:
        lam=Q(3*4**m,8)*Q(3*2**m,2)**(j-1)/(2*j)
        rhs=4*(7**(m+1)-1)
        assert lam>rhs
        gates.append({'m':m,'j':j,'Z_strength':str(lam),'eight_reference_bound':str(rhs)})
    c=Q(1,400000000);s=Q(59,100);m=70
    E=c*c*s**(2*m+1)/(16*(m+3));eps=Q(2*m+5,27*6**m)
    assert E>8*eps
    ratio=6*s*s*Q((m+3)*(2*m+5),(m+4)*(2*m+7))
    assert ratio>1
    old_E=c*c*s**(2*m+1)/(4*(m+3));old_eps=Q(2*m+5,9*6**m)
    assert old_E>12*old_eps
    result={'status':'PASS: complete finite gates for the half-defect seed theorem',
            'finite_pair_count':len(records),'finite_defect_margin_count':sum(len(row['half_defect_integer_margins'])
                    for record in records for row in record['rows'].values()),
            'finite_pairs':records,'analytic_strength_corners':gates,
            'j1_tail_start':70,'j1_tail_eta_over_eight_epsilon':str(E/(8*eps)),
            'normalized_single_tail_start':70,'single_eta_over_twelve_epsilon':str(old_E/(12*old_eps)),
            'both_tail_consecutive_ratio_at_70':str(ratio)}
    target=Path(__file__).with_name('seed_subtraction_certificates.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['finite_pairs','analytic_strength_corners']},indent=2))


if __name__=='__main__':main()
