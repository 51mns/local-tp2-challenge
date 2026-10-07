#!/usr/bin/env python3
"""Exact finite bridge and analytic-tail scalar gates for L^m R^2 L^ell.

This file reconstructs canonical prefixes using ordinary-x recurrences.
No author module or expected certificate is imported. All arithmetic is exact.
The mathematical all-m, all-ell argument is in UNIFORM_RAY_CLOSURE.md.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from pathlib import Path
import json


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*ps):
    r = [0] * max(map(len, ps))
    for p in ps:
        for i, a in enumerate(p):
            r[i] += a
    return trim(r)


def sc(p, c):
    return trim([a*c for a in p])


def sub(p, q):
    return add(p, sc(q, -1))


def mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return trim(r)


def half(p):
    return [sum(p[j]*comb(j, (j-n)//2) for j in range(n, len(p), 2))
            for n in range(len(p))]


def mass(p):
    return sum(a*2**i for i, a in enumerate(p))


def at(h, n):
    n = abs(n)
    return h[n] if n < len(h) else 0


def defect(h, n):
    return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)


def mutate(a, c, b, direction):
    left = sub(sub(sc(mul(mul(Y, a), c), 3), mul(XVAR, add(a, c))), b)
    right = sub(sub(sc(mul(mul(Y, c), b), 3), mul(XVAR, add(c, b))), a)
    return (a, left, c) if direction == 'L' else (c, right, b)


def divide_y(p):
    out, prev = [], 0
    for a in p[:-1]:
        prev = a-prev
        out.append(prev)
    assert p[-1] == prev
    return trim(out)


def linear_rows(p0, p1):
    h0, h1 = half(p0), half(p1)
    return [(at(h0,n), at(h1,n)) for n in range(max(len(h0),len(h1)))]


def lat(h,n):
    n=abs(n)
    return h[n] if n < len(h) else (0,0)


def linadd(p,q):
    return (p[0]+q[0],p[1]+q[1])


def linsc(p,c):
    return (p[0]*c,p[1]*c)


def linmul(p,q):
    return [p[0]*q[0],p[0]*q[1]+p[1]*q[0],p[1]*q[1]]


def pdefect(h,n):
    a,b,c,d = [lat(h,j) for j in (n-1,n,n+1,n+2)]
    return add(linmul(b,b),sc(linmul(a,c),-1),sc(linmul(c,c),-1),linmul(b,d))


def kernel(h,i,j):
    if i==0:
        return lat(h,j)
    if j==0:
        return linsc(lat(h,i),2)
    return linadd(lat(h,j-i),lat(h,j+i))


def minor(h,i,n):
    return sub(linmul(kernel(h,i,n),kernel(h,i+1,n+1)),
               linmul(kernel(h,i,n+1),kernel(h,i+1,n)))


def bern2(p):
    a,b,c = (p+[0,0,0])[:3]
    out = [2*a,2*a+b,2*(a+b+c)]
    # Reverse degree-two Bernstein expansion, independently clearing 2.
    assert [out[0],2*(out[1]-out[0]),out[0]-2*out[1]+out[2]] == [2*a,2*b,2*c]
    return out


def lr(p,q):
    a,b=half(p),half(q)
    return [at(a,n)*at(b,n+1)-at(a,n+1)*at(b,n) for n in range(len(a))]


XVAR,Y,P = [0,1],[1,1],[2,1]
ROOT=([1],[5,6,2],P)


def main():
    records=[]
    total=0
    pure=ROOT
    for m in range(77):
        s1=mutate(*pure,'R')
        endpoint,center,other=mutate(*s1,'R')
        t=sub(sc(mul(Y,endpoint),3),XVAR)
        inverse=sub(sub(mul(t,other),mul(XVAR,endpoint)),center)
        A=divide_y(sub(center,other))
        B=divide_y(sub(inverse,other))
        t0=sub(sc(mul(Y,other),3),XVAR)
        K0=add(t0,[1])
        J=mul(Y,sub(t,[2]))
        V=sc(mul(mul(mul(Y,Y),endpoint),P),3)
        K=mul(mul(endpoint,P),K0)
        assert V == add(mul(P,J),mul(Y,mul(P,P)))
        assert len(A)-1 == 3*m+5 and len(B)-1 == m+1
        assert len(t)-1 == 2*m+5
        assert all(a>0 for p in (A,B,sub(t,[2]),K0,J,V,K) for a in p)
        hK0,hK=half(K0),half(K)
        assert all(defect(hK0,n)>0 for n in range(len(hK0)))
        w=lr(J,V)
        assert min(w)>0
        L0=add(mul(A,sub(t,[2])),B)
        L1=sc(A,4)
        hL=linear_rows(L0,L1)
        hQ=linear_rows(mul(mul(Y,Y),L0),mul(mul(Y,Y),L1))
        lm=[mass(L0),mass(L1)]
        ht=linear_rows(sub(t,[2]),[4])
        trace_cert=bern2(sub(pdefect(ht,0),sc([mass(sub(t,[2])),4],2)))
        assert min(trace_cert)>0
        assert mass(B)<mass(A)*(mass(t)-2)
        proxy=[]
        for n in range(len(hK)):
            i=min(n,len(w)-1)
            alpha=(2*mass(J)*hK[n])//w[i]+1
            margin=bern2(sub(minor(hL,i,n),sc(lm,alpha)))
            assert min(margin)>0, ('proxy',m,n,alpha,min(margin))
            assert alpha*w[i] > 2*mass(J)*hK[n]
            proxy.append({'n':n,'i':i,'alpha':alpha,'scaled_bernstein':margin})
        multiplier=[]
        for n in range(len(hK0)+1):
            beta=6*(at(hK0,n-1)+3*at(hK0,n+1))+1
            margin=bern2(sub(pdefect(hQ,n),sc(lm,beta)))
            assert min(margin)>0, ('multiplier',m,n,beta,min(margin))
            multiplier.append({'n':n,'beta':beta,'scaled_bernstein':margin})
        q0=mul(Y,A)
        q1=mul(Y,add(mul(A,t),B))
        beta=mul(Y,add(A,B))
        E1=sub(center,endpoint)
        Pi=mul(P,endpoint)
        orders={}
        for label,p,q in [('q0_q1',q0,q1),('beta_q1',beta,q1),('Pi_E1',Pi,E1),('E1_q1',E1,q1)]:
            minors=lr(p,q)
            assert min(minors)>0, ('initial',m,label)
            orders[label]={'minimum':min(minors),'count':len(minors),'sha256':sha256(json.dumps(minors,separators=(',',':')).encode()).hexdigest()}
        values=trace_cert+[a for r in proxy+multiplier for a in r['scaled_bernstein']]
        total+=len(values)
        record={'m':m,'degrees':{'A':len(A)-1,'t':len(t)-1,'J':len(J)-1,'K':len(K)-1},
                'trace_delta0_minus_2mass_scaled_bernstein':trace_cert,
                'minimum_scaled_bernstein':min(values),'bernstein_count':len(values),
                'coefficient_sha256':sha256(json.dumps(values,separators=(',',':')).encode()).hexdigest(),
                'proxy':proxy,'multiplier':multiplier,'initial_orders':orders}
        records.append(record)
        pure=mutate(*pure,'L')
        if m%10==0 or m==76:
            print(json.dumps({'finite_m_complete':m}),flush=True)

    c0,sigma=Q(1,400000000),Q(59,100)
    def E(m):
        EL=c0**5*sigma**(5*m+2)/(65536*(m+3)**4)
        return EL*Q(4,49)**m/(6048*(4*m+14))
    def dominance(m):
        return Q(27**3*6**(4*m+2),2*(2*m+3)*(2*m+5)**2*(2*m+7))
    def ratio_gate(m):
        return c0**2*sigma**(2*m+1)*Q(27**2*6**(2*m+1),128*(m+3)**2*(2*m+5)*(2*m+7))
    M=77
    assert E(M)*dominance(M)>96
    assert ratio_gate(M)>2 and dominance(M)>2
    assert E(M+1)*dominance(M+1)/(E(M)*dominance(M))>6
    assert ratio_gate(M+1)/ratio_gate(M)>11
    # Both consecutive ratios are products of increasing (m+a)/(m+a+1)
    # factors and a positive fixed exponential ratio; see the proof note.
    result={'status':'PASS','scope':'Finite ray-extension gates for 0<=m<=76; analytic scalar tail m>=77',
            'finite_range':[0,76],'total_strictly_positive_bernstein_coefficients':total,
            'tail_start':M,'tail':{'E_times_dominance':str(E(M)*dominance(M)),
            'normalized_propagation_ratio':str(ratio_gate(M)),
            'dominance':str(dominance(M)),
            'consecutive_ratio_Ec':str(E(M+1)*dominance(M+1)/(E(M)*dominance(M))),
            'consecutive_ratio_propagation':str(ratio_gate(M+1)/ratio_gate(M))},'records':records}
    dest=Path(__file__).with_name('uniform_ray_closure_results.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','finite_range':[0,76],'total_bernstein_coefficients':total,'tail_start':77,'output':str(dest)}))


if __name__=='__main__':
    main()
