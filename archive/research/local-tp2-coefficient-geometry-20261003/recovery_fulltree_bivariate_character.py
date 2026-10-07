#!/usr/bin/env python3
"""Exact SU(2)xSU(2) transform of the Local TP2 Bezoutian.

The general identity is proved in the accompanying note. Small examples
check implementation and normalizations; they are not an all-tree proof.
Only the standard library and original scalar recurrences are used.
"""
from collections import defaultdict
from math import comb
import json
from tp2_source import generate_tree, H, hget, mul


def plus(a,b):
    c=defaultdict(int,a)
    for k,v in b.items():c[k]+=v
    return {k:v for k,v in c.items() if v}


def times(a,b):
    c=defaultdict(int)
    for (i,j),v in a.items():
        for (k,l),w in b.items():c[i+k,j+l]+=v*w
    return {k:v for k,v in c.items() if v}


def scale(a,n):return {k:v*n for k,v in a.items() if v*n}


def power(a,n):
    out={(0,0):1}
    for _ in range(n):out=times(out,a)
    return out


def bezoutian(p,q):
    """[p(s)q(z)-q(s)p(z)]/(z-s), in ordinary s,z coefficients."""
    out=defaultdict(int)
    size=max(len(p),len(q))
    for i in range(size):
        for j in range(i+1,size):
            w=hget(p,i)*hget(q,j)-hget(q,i)*hget(p,j)
            for k in range(j-i):out[i+k,j-1-k]+=w
    return {k:v for k,v in out.items() if v}


def rotate_symmetric(poly):
    """s+z=UV, sz=U^2+V^2-4, by symmetric power-sum recurrence."""
    for (i,j),v in poly.items():assert poly.get((j,i),0)==v
    a={(1,1):1};b={(2,0):1,(0,2):1,(0,0):-4}
    degree=max((abs(i-j) for i,j in poly),default=0)
    sums=[{(0,0):2},a]
    for k in range(2,degree+1):
        sums.append(plus(times(a,sums[-1]),scale(times(b,sums[-2]),-1)))
    bpowers=[power(b,i) for i in range(max((min(i,j) for i,j in poly),default=0)+1)]
    out={}
    for (i,j),v in poly.items():
        if i<j:continue
        term=bpowers[j] if i==j else times(bpowers[j],sums[i-j])
        out=plus(out,scale(term,v))
    return out


def chars_of_power(n):
    return {n-2*k:comb(n,k)-(comb(n,k-1) if k else 0) for k in range(n//2+1)}


def to_characters(poly):
    out=defaultdict(int)
    for (i,j),v in poly.items():
        for a,c in chars_of_power(i).items():
            for b,d in chars_of_power(j).items():out[a,b]+=v*c*d
    return {k:v for k,v in out.items() if v}


def predicted_characters(p,q):
    hp,hq=H(p),H(q);out=defaultdict(int)
    for i in range(max(len(hp),len(hq))):
        for j in range(i+1,max(len(hp),len(hq))):
            w=hget(hp,i)*hget(hq,j)-hget(hq,i)*hget(hp,j)
            a,b=i+j-1,j-i-1
            out[a,b]+=w
            if i:out[b,a]+=w
    return {k:v for k,v in out.items() if v}


def actual_characters(p,q):return to_characters(rotate_symmetric(bezoutian(p,q)))


def verify():
    results={}
    # Exhaust individual monomial pairs through degree 7, including either
    # orientation. The general all-degree result follows from the Laurent
    # identity in the accompanying note, not this finite unit check.
    count=0
    for i in range(8):
        for j in range(8):
            p=[0]*i+[1];q=[0]*j+[1]
            assert actual_characters(p,q)==predicted_characters(p,q)
            count+=1
    results['normalization_checks']=count
    examples=[]
    for rec in generate_tree(1):
        p,q=rec['S'],rec['D'];chars=actual_characters(p,q)
        assert chars==predicted_characters(p,q)
        adjacent=[chars.get((2*n,0),0) for n in range(len(p))]
        assert adjacent==rec['F']
        examples.append({'path':rec['path'],'adjacent_minors':adjacent,
                         'character_terms':len(chars),
                         'negative_character_terms':sum(v<0 for v in chars.values()),
                         'ordinary_bezoutian_negative_terms':sum(v<0 for v in bezoutian(p,q).values())})
    results['canonical_normalization_examples']=examples
    y=[1,1];xy=[0,1,1]
    obstruction=actual_characters(y,xy)
    assert obstruction=={(0,0):-1,(2,0):1,(0,2):1,(1,1):1}
    results['positive_tensor_obstruction']={f'{i},{j}':v for (i,j),v in sorted(obstruction.items())}
    # Divided difference: Q=F, P=1. Character expansion is diagonal H(F)_j.
    f=[-3,2,4,7,1]
    dd=actual_characters([1],f)
    assert dd=={(j-1,j-1):v for j,v in enumerate(H(f)) if j and v}
    results['divided_difference_diagonal_check']=True
    # Independent character-trivial projection via Catalan moments.
    for rec in generate_tree(1):
        rotated=rotate_symmetric(bezoutian(rec['S'],rec['D']))
        projection=defaultdict(int)
        for (i,j),v in rotated.items():
            if j%2==0:projection[i]+=v*comb(j,j//2)//(j//2+1)
        projection_chars=defaultdict(int)
        for i,v in projection.items():
            for k,c in chars_of_power(i).items():projection_chars[k]+=v*c
        assert {k:v for k,v in projection_chars.items() if v}=={2*n:v for n,v in enumerate(rec['F']) if v}
    results['Catalan_projection_check']=True
    # T_F = R_(F,xF); its boundary is exactly the existing folded defect.
    tensor_examples=[[1],[2,1],[1,1],[1,2,1],[3,3,1],[8,20,16,4]]
    for f in tensor_examples:
        ff={(i,j):a*b for i,a in enumerate(f) for j,b in enumerate(f) if a*b}
        tensor=to_characters(rotate_symmetric(ff))
        assert tensor==actual_characters(f,[0]+f)
        h=H(f)
        hs=lambda n:hget(h,abs(n))
        defects=[hs(n)**2-hs(n-1)*hs(n+1)-hs(n+1)**2+hs(n)*hs(n+2)
                 for n in range(len(h))]
        assert defects==[tensor.get((2*n,0),0) for n in range(len(h))]
        assert all(v>=0 for v in tensor.values())==all(v>=0 for v in defects)
    results['folded_cone_tensor_examples']=len(tensor_examples)
    # Product homomorphism checked before character expansion; positivity
    # after expansion follows from the all-degree Clebsch-Gordan identity.
    fp,fq=[2,1],[3,3,1]
    tp=rotate_symmetric({(i,j):a*b for i,a in enumerate(fp) for j,b in enumerate(fp)})
    tq=rotate_symmetric({(i,j):a*b for i,a in enumerate(fq) for j,b in enumerate(fq)})
    fqprod=mul(fp,fq)
    tprod=rotate_symmetric({(i,j):a*b for i,a in enumerate(fqprod) for j,b in enumerate(fqprod)})
    assert tprod==times(tp,tq)
    assert all(v>=0 for v in to_characters(tprod).values())
    results['product_tensor_check']=True
    return results


if __name__=='__main__':print(json.dumps(verify(),indent=2))
