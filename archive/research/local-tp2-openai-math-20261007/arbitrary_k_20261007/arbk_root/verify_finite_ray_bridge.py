#!/usr/bin/env python3
"""Exact finite-ray bridge for L^m R^k L^ell at 34 specified prefixes.

This file reconstructs canonical prefixes using ordinary-x recurrences.
No author module or expected certificate is imported. All arithmetic is exact.
The unbounded parameter proof is in GENERIC_ARBITRARY_K_CLOSURE.md.
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
    upper={0:21,1:11,2:6,3:5,4:4,5:5}
    records=[];total=0
    pure=ROOT
    for m in range(6):
        state=pure
        for k in range(1,upper[m]):
            state=mutate(*state,'R')
            if k<3:continue
            endpoint,center,other=state
            t=sub(sc(mul(Y,endpoint),3),XVAR)
            inverse=sub(sub(mul(t,other),mul(XVAR,endpoint)),center)
            A=divide_y(sub(center,other))
            B=divide_y(sub(inverse,other))
            K0=add(sub(sc(mul(Y,other),3),XVAR),[1])
            J=mul(Y,sub(t,[2]))
            V=sc(mul(mul(mul(Y,Y),endpoint),P),3)
            K=mul(mul(endpoint,P),K0)
            assert V==add(mul(P,J),mul(Y,mul(P,P)))
            d=m+2;degree=d*k+1
            assert len(t)-1==degree and len(A)-1==degree+d-2
            assert len(B)-1==degree-d-2
            assert all(a>0 for p in (A,B,sub(t,[2]),K0,J,V,K) for a in p)
            hK0,hK=half(K0),half(K)
            assert all(defect(hK0,n)>0 for n in range(len(hK0)))
            w=lr(J,V);assert min(w)>0
            L0=add(mul(A,sub(t,[2])),B);L1=sc(A,4)
            hL=linear_rows(L0,L1)
            hQ=linear_rows(mul(mul(Y,Y),L0),mul(mul(Y,Y),L1))
            lm=[mass(L0),mass(L1)]
            ht=linear_rows(sub(t,[2]),[4])
            trace_cert=bern2(sub(pdefect(ht,0),sc([mass(sub(t,[2])),4],2)))
            assert min(trace_cert)>0,(m,k,'trace')
            assert mass(B)<mass(A)*(mass(t)-2)
            proxy=[];multiplier=[]
            for n in range(len(hK)):
                i=min(n,len(w)-1)
                alpha=(2*mass(J)*hK[n])//w[i]+1
                margin=bern2(sub(minor(hL,i,n),sc(lm,alpha)))
                assert min(margin)>0,(m,k,'proxy',n,min(margin))
                assert alpha*w[i]>2*mass(J)*hK[n]
                proxy.append({'n':n,'i':i,'alpha':alpha,'scaled_bernstein':margin})
            for n in range(len(hK0)+1):
                beta=6*(at(hK0,n-1)+3*at(hK0,n+1))+1
                margin=bern2(sub(pdefect(hQ,n),sc(lm,beta)))
                assert min(margin)>0,(m,k,'multiplier',n,min(margin))
                multiplier.append({'n':n,'beta':beta,'scaled_bernstein':margin})
            values=trace_cert+[v for rr in proxy+multiplier for v in rr['scaled_bernstein']]
            total+=len(values)
            rec={'m':m,'k':k,'degrees':{'A':len(A)-1,'B':len(B)-1,'t':len(t)-1,'J':len(J)-1,'K':len(K)-1},
                 'trace_delta0_minus_2mass_scaled_bernstein':trace_cert,
                 'minimum_scaled_bernstein':min(values),'bernstein_count':len(values),
                 'coefficient_sha256':sha256(json.dumps(values,separators=(',',':')).encode()).hexdigest(),
                 'proxy':proxy,'multiplier':multiplier,
                 'prefix_polynomial_sha256':sha256(json.dumps([endpoint,center,other],separators=(',',':')).encode()).hexdigest()}
            records.append(rec)
        pure=mutate(*pure,'L')
    assert len(records)==34
    out={'status':'PASS','scope':'Finite-ray criterion for 34 exact (m,k) prefixes, every final left length ell>=1',
         'prefix_count':len(records),'total_strict_bernstein_coefficients':total,
         'thresholds':upper,'records':records,
         'initial_orders':'Inherited all-m/all-k companion theorem; no redundant finite enumeration is used as its proof.'}
    Path(__file__).with_name('finite_ray_bridge_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
