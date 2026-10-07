#!/usr/bin/env python3
"""Independent ordinary-x audit of seed half-defects and old constants.

No author verifier is imported. Inner Chebyshev polynomials are built in
ordinary x and converted using binomial coefficients. Normalized interval
coefficients use endpoint polarization, not three-point interpolation.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json

def trim(h):
    while len(h)>1 and not h[-1]:h.pop()
    return h
def plus(*rows):
    h=[0]*max(map(len,rows))
    for r in rows:
        for n,v in enumerate(r):h[n]+=v
    return trim(h)
def sc(h,c):return trim([c*v for v in h])
def sub(a,b):return plus(a,sc(b,-1))
def mul(a,b):
    h=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):h[i+j]+=v*w
    return trim(h)
def H(a):
    h=[0]*len(a)
    for j,c in enumerate(a):
        for n in range(j%2,j+1,2):h[n]+=c*comb(j,(j-n)//2)
    return h
def at(h,n):return h[abs(n)] if abs(n)<len(h) else 0
def delta(h,n):return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)
def polar(a,b,n):
    return (2*at(a,n)*at(b,n)-at(a,n-1)*at(b,n+1)-at(b,n-1)*at(a,n+1)
            -2*at(a,n+1)*at(b,n+1)+at(a,n)*at(b,n+2)+at(b,n)*at(a,n+2))
def digest(seq):return sha256(''.join(str(v)+'\n' for v in seq).encode()).hexdigest()

def tables(limit):
    u=[[1],[3,2]]
    for _ in range(1,limit+1):u.append(sub(mul([3,2],u[-1]),u[-2]))
    acc=[0];T=[]
    for h in u:acc=plus(acc,h);T.append(acc)
    return T

def old_data(m,T):
    a,b=T[m+1],T[m-1] if m else [0]
    t=plus(sc(mul([1,2,1],T[m]),3),[3,2])
    return a,b,t

def main():
    root=Path(__file__).resolve().parent.parent
    seed=json.loads((root/'arbk_seed/seed_subtraction_certificates.json').read_text())
    old=json.loads((root/'arbk_seed/old_normalized_constants.json').read_text())
    T=tables(69);count=0;seed_digest=sha256()
    for rec in seed['finite_pairs']:
        m,j=rec['m'],rec['j'];a,b,t=old_data(m,T)
        rs=[[0],[1]]
        for _ in range(j):rs.append(plus(sub(mul(t,rs[-1]),rs[-2]),[1]))
        Z=plus(mul(a,rs[j+1]),mul(b,rs[j]));A=sub(Z,T[m])
        for name,smooth in [('raw',False),('smoothed',True)]:
            z=H(mul([1,1],Z) if smooth else Z);aa=H(mul([1,1],A) if smooth else A)
            wanted=rec['rows'][name]
            assert z==wanted['old_prefix_halfrow'] and aa==wanted['seed_halfrow']
            margins=[2*delta(aa,n)-delta(z,n) for n in range(len(z))]
            assert margins==wanted['half_defect_integer_margins'] and min(margins)>0
            assert digest(aa)==wanted['seed_halfrow_sha256']
            for v in margins:seed_digest.update((str(v)+'\n').encode())
            count+=len(margins)
    assert count==seed['finite_defect_margin_count']==16048
    interval_count=0;interval_digest=sha256()
    for rec in old['records']:
        m=rec['m'];a,b,t=old_data(m,T);lo=sub(t,[2]);hi=plus(t,[2])
        cases=[('trace',lo,hi),('single',plus(mul(a,lo),b),plus(mul(a,hi),b))]
        cases.append(('smoothed_single',mul([1,1],cases[1][1]),mul([1,1],cases[1][2])))
        for name,f,g in cases:
            h,k=H(f),H(g);best=Q(1);where=None;checksum=sha256();num=0
            for n in range(len(h)):
                ds=[2*delta(h,n),polar(h,k,n),2*delta(k,n)]
                hs=[2*h[n]**2,2*h[n]*k[n],2*k[n]**2]
                assert min(ds)>0 and min(hs)>0
                for idx,(d,s) in enumerate(zip(ds,hs)):
                    ratio=Q(d,s)
                    if ratio<best:best,where=ratio,[n,idx]
                    line=(str(d)+'/'+str(s)+'\n').encode();checksum.update(line);interval_digest.update(line);num+=1
            wanted=rec[name]
            assert wanted['normalized_lower_bound']==str(best)
            assert wanted['attained_bernstein_index']==where
            assert wanted['ordered_coefficient_pair_sha256']==checksum.hexdigest()
            assert wanted['coefficient_pairs']==num
            interval_count+=num
    assert interval_count==old['total_coefficient_pairs']
    # Independently recompute all infinite-tail scalar anchors.
    c=Q(1,400000000);s=Q(59,100);m=70
    E=c*c*s**141/(16*73);eps=Q(145,27*6**70)
    assert E>8*eps and str(E/(8*eps))==seed['j1_tail_eta_over_eight_epsilon']
    D=4*E;eps2=3*eps
    assert D>12*eps2 and str(D/(12*eps2))==seed['single_eta_over_twelve_epsilon']
    for rec in seed['analytic_strength_corners']:
        m,j=rec['m'],rec['j'];lam=Q(3*2**(2*m),8)*Q(3*2**m,2)**(j-1)/(2*j)
        assert lam==Q(rec['Z_strength']) and lam>4*(7**(m+1)-1)
    out={'status':'PASS','independent_method':'ordinary-x inner Chebyshev recurrence; binomial Laurent conversion; endpoint polarization',
         'seed_pairs':len(seed['finite_pairs']),'seed_margin_count':count,'seed_margin_sha256':seed_digest.hexdigest(),
         'old_m_range':[0,69],'old_interval_coefficient_pairs':interval_count,'old_interval_coefficient_pair_sha256':interval_digest.hexdigest(),
         'all_recorded_rows_margins_bounds_and_digests_match':True,'infinite_tail_scalar_anchors_match':True}
    Path(__file__).with_name('seed_bounds_independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
