#!/usr/bin/env python3
"""Shared-session independent arithmetic audit; no author code/data imports.
All fixtures reconstructed from the frozen root mutation, not expected JSON.
"""
from itertools import product
from math import comb
from fractions import Fraction
from collections import Counter
import json
from pathlib import Path

# A univariate Laurent ring, with unrestricted integer exponents.
def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,0)+v
    return clean(out)
def scale(p,c): return clean({k:c*v for k,v in p.items()})
def mul(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items(): out[a+b]=out.get(a+b,0)+c*d
    return clean(out)
def power(p,n):
    out={0:1}
    for _ in range(n): out=mul(out,p)
    return out
def at(p,z): return sum(Fraction(v)*Fraction(z)**k for k,v in p.items())
def vector(p,lo,hi): return [p.get(k,0) for k in range(lo,hi+1)]
def shift(p,k): return {a+k:v for a,v in p.items()}
def divide(p,d):
    q={}; r=dict(p)
    while r and max(r)>=max(d):
        exponent=max(r)-max(d)
        coefficient=Fraction(r[max(r)],d[max(d)])
        q[exponent]=q.get(exponent,0)+coefficient
        r=add(r,scale(shift(d,exponent),-coefficient))
    return clean(q),clean(r)
def mutation(t,c,z,x):
    return add(scale(mul(mul(add(x,{0:1}),t),c),3),scale(mul(x,add(t,c)),-1),scale(z,-1))
def root_pair(x):
    xx={0:1}; yy=add(x,{0:2}); cc=add(scale(power(x,2),2),scale(x,6),{0:5})
    uu=mutation(xx,cc,yy,x); vv=mutation(yy,cc,xx,x)
    return {'X':xx,'Y':yy,'C':cc,'U':uu,'V':vv,'S':add(uu,scale(cc,-1)),'D':add(vv,scale(uu,-1))}
def homogeneous_hessian_after_derivative(h,diff_variable):
    degree=len(h)-1
    p={(n,degree-n):v for n,v in enumerate(h)}
    def diff(p,var):
        out={}
        for k,v in p.items():
            if k[var]:
                nxt=list(k);nxt[var]-=1
                out[tuple(nxt)]=v*k[var]
        return out
    f=diff(p,diff_variable)
    matrix=[]
    for i in range(2):
        row=[]
        for j in range(2):
            value=diff(diff(f,i),j)
            assert all(k==(0,0) for k in value)
            row.append(value.get((0,0),0))
        matrix.append(row)
    return f,matrix

def newton(row):
    degree=len(row)-1
    output=[]
    for k in range(1,degree):
        left=Fraction(row[k],comb(degree,k))**2
        right=Fraction(row[k-1],comb(degree,k-1))*Fraction(row[k+1],comb(degree,k+1))
        output.append({'index':k,'left':str(left),'right':str(right),'difference':str(left-right),'passes':left>=right})
    return output

ordinary=root_pair({1:1})
laurent=root_pair({1:1,-1:1})
for name,p in laurent.items():
    assert all(p.get(-k,0)==v for k,v in p.items())
    # Directly substitute into the separately reconstructed ordinary polynomial.
    from_ordinary={}
    for k,v in ordinary[name].items(): from_ordinary=add(from_ordinary,scale(power({1:1,-1:1},k),v))
    assert p==from_ordinary
hs=vector(laurent['S'],0,max(laurent['S']))
hd=vector(laurent['D'],0,max(laurent['D']))
f=[laurent['S'].get(n,0)*laurent['D'].get(n+1,0)-laurent['S'].get(n+1,0)*laurent['D'].get(n,0) for n in range(len(hs))]
assert all(v>0 for v in f)

partial,hessian=homogeneous_hessian_after_derivative(hs,1)
determinant=hessian[0][0]*hessian[1][1]-hessian[0][1]*hessian[1][0]
assert hessian[0][0]>0 and determinant>0

# Verify the all-tree evaluation proof as a symbolic substitution in the three
# input values at x=-1. If all three values equal 1, mutation outputs 1.
one={0:1}
root_evals={name:str(at(p,-1)) for name,p in ordinary.items()}
assert all(at(ordinary[name],-1)==1 for name in ['X','Y','C','U','V'])
assert mutation(one,one,one,{0:-1})==one
phi={2:1,1:1,0:1}
cyclotomic={}
for name in ['S','D']:
    p=ordinary[name]
    quotient,remainder=divide(p,{1:1,0:1})
    assert not remainder
    degree=max(p)
    shifted=shift(laurent[name],degree)
    quotient_q,remainder_q=divide(shifted,phi)
    assert not remainder_q
    # q^d P(q+q^-1) = Phi_3(q) q^(d-1) R(q+q^-1).
    r_laurent={}
    for k,v in quotient.items(): r_laurent=add(r_laurent,scale(power({1:1,-1:1},k),v))
    assert shifted==mul(phi,shift(r_laurent,degree-1))
    cyclotomic[name]={'ordinary_quotient':vector(quotient,0,max(quotient)), 'shifted_degree':max(shifted), 'phi3_quotient':vector(quotient_q,0,max(quotient_q)), 'remainder':[]}

abs_hs=[value if n==0 else 2*value for n,value in enumerate(hs)]
assert any(not case['passes'] for case in newton(hs))
assert any(not case['passes'] for case in newton(abs_hs))

# Enumerate every configuration of independent mutually exclusive choices
# (empty, u_i, v_i); no Laurent/binomial coefficient formula used here.
counts={}
for m in [3,4]:
    signed=Counter()
    folded=Counter()
    selected_count=Counter()
    for choices in product([0,1,-1],repeat=m):
        value=sum(choices)
        signed[value]+=1
        folded[abs(value)]+=1
        selected_count[sum(c!=0 for c in choices)]+=1
    assert sum(signed.values())==3**m
    assert all(signed[n]==signed[-n] for n in range(m+1))
    counts[m]={'signed_halfrow':[signed[n] for n in range(m+1)], 'absolute_counts':[folded[n] for n in range(m+1)], 'cardinality_counts':[selected_count[n] for n in range(m+1)],'total':sum(signed.values())}
a=counts[3]['signed_halfrow'];b=counts[4]['signed_halfrow']
ah=counts[3]['absolute_counts'];bh=counts[4]['absolute_counts']
half_minor=a[0]*b[1]-a[1]*b[0]
abs_minor=ah[0]*bh[1]-ah[1]*bh[0]
assert half_minor<0 and abs_minor<0

# Centered quantum torus: key (first lattice coordinate, second, v exponent).
def torus_add(a,b,multiplier=1):
    out=dict(a)
    for key,value in b.items(): out[key]=out.get(key,0)+multiplier*value
    return clean(out)
def torus_mul(a,b):
    out={}
    for (i,j,r),c in a.items():
        for (k,l,s),d in b.items():
            key=(i+k,j+l,r+s+i*l-j*k)
            out[key]=out.get(key,0)+c*d
    return clean(out)
def axis(p,which):
    return {(n,0,0) if which==1 else (0,n,0):c for n,c in p.items()}
def coord(p,n,m): return {r:v for (i,j,r),v in p.items() if (i,j)==(n,m)}
p1=axis(laurent['S'],1);p2=axis(laurent['S'],2)
q1=axis(laurent['D'],1);q2=axis(laurent['D'],2)
naive=torus_add(torus_mul(p1,q2),torus_mul(p2,q1),-1)
ordered=torus_add(torus_mul(p1,q2),torus_mul(q1,p2),-1)
opposite_sector=coord(ordered,1,0)
assert opposite_sector.get(0,0)<0
quantum=[]
for n,m in [(0,1),(1,2),(2,3)]:
    w=laurent['S'][n]*laurent['D'][m]-laurent['D'][n]*laurent['S'][m]
    assert coord(ordered,n,m)=={n*m:w}
    assert sum(coord(naive,n,m).values())==w
    if n*m: assert any(c<0 for c in coord(naive,n,m).values())
    quantum.append({'coordinates':[n,m],'naive_laurent_v':coord(naive,n,m),'ordered_laurent_v':coord(ordered,n,m),'classical_minor':w,'necessary_monomial_correction_kappa':2*n*m})
assert quantum[1]['necessary_monomial_correction_kappa']!=quantum[2]['necessary_monomial_correction_kappa']

result={
 'audit_type':'Shared-session independent mathematical and arithmetic audit; not blind; no writer implementation or expected JSON imported',
 'canonical_root':{'ordinary':{name:vector(p,0,max(p)) for name,p in ordinary.items()},'H_S':hs,'H_D':hd,'F':f},
 'ordinary_homogenization':{'partial_v_terms':{str(k):v for k,v in partial.items()},'hessian':hessian,'determinant':determinant,'positive_definite':True,'scope':'ordinary homogeneous polynomial from H(S); not every possible lift or normalization'},
 'root_at_minus_one':root_evals,
 'cyclotomic_divisibility':cyclotomic,
 'newton_halfrow':newton(hs),
 'newton_absolute_fold':newton(abs_hs),
 'stable_signed_counterexample':{'counts':counts,'halfrow_minor':half_minor,'absolute_minor':abs_minor,'normalized_absolute_minor':str(Fraction(abs_minor,counts[3]['total']*counts[4]['total']))},
 'quantum_torus':quantum,
 'ordered_quantum_opposite_sector_1_0':opposite_sector,
 'full_tree_Local_TP2':'OPEN; none of these obstructions is a canonical target counterexample',
 'repository_status':'No canonical promotion; no existing file changed'
}
text=json.dumps(result,ensure_ascii=False,indent=2,default=lambda x:str(x))+'\n'
Path(__file__).with_name('independent_results.json').write_text(text)
print(text)
