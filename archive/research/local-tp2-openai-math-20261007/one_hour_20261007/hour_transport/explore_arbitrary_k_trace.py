#!/usr/bin/env python3
"""Exact tiny bridge for the exploratory arbitrary-right-length trace lemma.

This is separate from the completed L^m R^2 L^ell proof and is not an
additional dependency of it.  All scalar and interval arithmetic is exact.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def add(*ps):
    p=[0]*max(map(len,ps))
    for q in ps:
        for n,a in enumerate(q):p[n]+=a
    return trim(p)


def scale(p,c):
    return trim([a*c for a in p])


def sub(p,q):
    return add(p,scale(q,-1))


def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)


def half(p):
    return [sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2))
            for n in range(len(p))]


def at(h,n):
    n=abs(n)
    return h[n] if n<len(h) else 0


def delta(h,n):
    return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)


def node(word):
    A,C,B=[1],[5,6,2],[2,1]
    for letter in word:
        if letter=='L':
            M=sub(sub(scale(mul(mul([1,1],A),C),3),mul([0,1],add(A,C))),B)
            A,C,B=A,M,C
        else:
            M=sub(sub(scale(mul(mul([1,1],B),C),3),mul([0,1],add(B,C))),A)
            A,C,B=C,M,B
    return A,C,B


def trace(C):
    return sub(scale(mul([1,1],C),3),[0,1])


# Sparse symbolic polynomial ring in h0,...,h5,a.
NV=7
ZERO=(0,)*NV


def const(c):return {ZERO:c} if c else {}
def var(n):
    e=[0]*NV;e[n]=1
    return {tuple(e):1}
def sp(*ps):
    out={}
    for p in ps:
        for e,a in p.items():out[e]=out.get(e,0)+a
    return {e:a for e,a in out.items() if a}
def ss(p,c):return {e:a*c for e,a in p.items() if a*c}
def sm(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(i+j for i,j in zip(e,f));out[g]=out.get(g,0)+a*b
    return {e:a for e,a in out.items() if a}
def sd(h,n):
    get=lambda j:h[abs(j)] if abs(j)<len(h) else {}
    a,b,c,d=[get(j) for j in (n-1,n,n+1,n+2)]
    return sp(sm(b,b),ss(sm(a,c),-1),ss(sm(c,c),-1),sm(b,d))


def verify_symbolic():
    h=[var(i) for i in range(6)];a=var(6)
    h0,h1,h2,h3,h4,h5=h
    cases=[
        ([a,const(2)], [
            sp(ss(sm(a,h0),6),ss(h1,-24),ss(sm(a,h2),3),sm(a,a),const(-8)),
            sp(ss(h1,12),ss(sm(a,h2),-3),ss(h3,6),const(4)),
            ss(h3,-6),{},
        ]),
        ([sp(a,const(4)),sp(a,const(2)),const(2)], [
            sp(sm(sp(ss(a,6),const(30)),h0),ss(sm(sp(ss(a,12),const(24)),h1),-1),
               sm(sp(ss(a,3),const(12)),h2),ss(sm(a,a),-1),ss(a,2),const(16)),
            sp(sm(sp(ss(a,6),const(12)),h1),ss(h0,-6),
               ss(sm(sp(ss(a,3),const(24)),h2),-1),
               sm(sp(ss(a,3),const(6)),h3),sm(a,a),ss(a,2),const(-8)),
            sp(ss(h2,12),ss(sm(sp(a,const(2)),h3),-3),ss(h4,6),const(4)),
            ss(h4,-6),{},
        ]),
    ]
    count=0
    for correction,expected in cases:
        b=[sp(ss(p,3),correction[n] if n<len(correction) else {}) for n,p in enumerate(h)]
        for n,formula in enumerate(expected):
            assert sp(sd(b,n),ss(sd(h,n),-9))==formula,n
            count+=1
    # Central defect of yF, with reflection included.
    yh=[sp(h0,ss(h1,2)),sp(h0,h1,h2),sp(h1,h2,h3)]
    expected=sp(ss(sm(h0,h0),-1),sm(h0,h1),ss(sm(h1,h1),4),
                ss(sm(h0,h2),-3),ss(sm(h1,h2),-2),ss(sm(h2,h2),-2),
                sm(h0,h3),ss(sm(h1,h3),2))
    assert sd(yh,0)==expected
    return count+1


def main():
    symbolic_count=verify_symbolic()
    exceptional=[(0,k) for k in range(1,4)]+[(1,k) for k in range(1,6)]+[(2,1),(2,2),(3,1)]
    records=[]
    count=0
    for m,k in exceptional:
        C=node('L'*m+'R'*k)[1]
        t=trace(C)
        record={'m':m,'k':k,'center_ordinary':C,'trace_ordinary':t,'cases':{}}
        for smooth in (False,True):
            values=[]
            rows=[]
            for r in (-2,0,2):
                p=sub(t,[r])
                if smooth:p=mul([1,1],p)
                h=half(p)
                assert min(h)>0
                rows.append(h)
                values.append([delta(h,n)-h[n] for n in range(len(h))])
            certs=[]
            for n in range(len(rows[0])):
                left,middle,right=[v[n] for v in values]
                coefficients=[2*left,4*middle-left-right,2*right]
                assert min(coefficients)>0,(m,k,smooth,n)
                # Independently check values of the recovered Bernstein quadratic.
                assert coefficients[0]+2*coefficients[1]+coefficients[2]==8*middle
                certs.append(coefficients)
                count+=3
            record['cases']['smooth' if smooth else 'raw']={
                'degree':len(rows[0])-1,'strength':1,
                'twice_degree_two_bernstein':certs,
                'minimum_scaled_coefficient':min(a for c in certs for a in c)}
        records.append(record)
    strength=lambda m,k:Q(2)**(2*m-4)*Q(3*2**(m-1))**(k-1)/k-8
    corners={(1,6):Q(17,8),(2,3):Q(4),(3,2):Q(16),(4,1):Q(8)}
    for (m,k),bound in corners.items():assert strength(m,k)==bound
    # The m=0 primitive paired-root box: t^2+a*t+b, a in [0,4], b in [-4,4].
    base_trace=[6,8,3]
    box=[]
    for a in (0,2,4):
        row=[]
        for b in (-4,0,4):
            h=half(add(mul(base_trace,base_trace),scale(base_trace,a),[b]))
            assert min(h)>0
            row.append([delta(h,n)-9*h[n] for n in range(len(h))])
        box.append(row)
    paired_certificates=[]
    for n in range(5):
        along_first=[]
        for j in range(3):
            left,middle,right=[box[i][j][n] for i in range(3)]
            along_first.append([2*left,4*middle-left-right,2*right])
        tensor=[]
        for i in range(3):
            left,middle,right=[along_first[j][i] for j in range(3)]
            tensor.append([2*left,4*middle-left-right,2*right])
        assert min(a for row in tensor for a in row)>=0
        # Verify all nine original values by the Bernstein basis evaluations.
        weights=((4,0,0),(1,2,1),(0,0,4))
        for i in range(3):
            for j in range(3):
                rebuilt=sum(tensor[a][b]*weights[i][a]*weights[j][b]
                            for a in range(3) for b in range(3))
                assert rebuilt==64*box[i][j][n]
        paired_certificates.append(tensor)
    negative_single=[]
    for r in (-2,-1,0):
        h=half(sub(base_trace,[r]))
        negative_single.append([delta(h,n)-h[n] for n in range(len(h))])
    single_certificates=[]
    for n in range(3):
        left,middle,right=[row[n] for row in negative_single]
        coefficients=[2*left,4*middle-left-right,2*right]
        assert min(coefficients)>0
        single_certificates.append(coefficients)
    assert all(2*(k//4)>=2 if k%2==0 else (k-1)//2>=2 for k in range(4,8))
    result={'status':'PASS_EXPLORATORY_AUXILIARY_LEMMA',
            'independent_audit':'PASS in ../hour_invariant/audit_arbitrary_k_trace.py and its result JSON',
            'scope':'Shifted and smoothed center trace after L^m R^k, all m>=0,k>=1; k=0 is an inherited pure-left trace theorem; not a Local TP2 extension theorem',
            'exceptional_pairs':[list(p) for p in exceptional],
            'positive_bernstein_coefficient_count':count,
            'total_bernstein_coefficient_count':count+45+9,
            'zero_bernstein_coefficient_count':9,
            'm0_primitive_pair_box':{'strength':9,'parameter_box':[[0,4],[-4,4]],
                                   'scaled_tensor_denominator':4,
                                   'nonnegative_bernstein_count':45,
                                   'four_times_tensor_bernstein':paired_certificates},
            'm0_primitive_nonpositive_root':{'strength':1,'root_interval':[-2,0],
                                           'positive_bernstein_count':9,
                                           'twice_bernstein':single_certificates},
            'symbolic_identity_count':symbolic_count,
            'tail_corner_strengths':{f'{m},{k}':str(v) for (m,k),v in corners.items()},
            'records':records}
    path=Path(__file__).with_name('arbitrary_k_trace_exploratory_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':main()
