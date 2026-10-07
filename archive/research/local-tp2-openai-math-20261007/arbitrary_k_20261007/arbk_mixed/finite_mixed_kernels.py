#!/usr/bin/env python3
"""Exact continuum certificates for the 34 remaining mixed spectral kernels.

The midpoint parameter is c=(r+s)/2. Each interval is [-2,2].
All arithmetic is integral or Fraction; there are no sampled inequalities.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json


def trim(h):
    h=list(h)
    while len(h)>1 and not h[-1]: h.pop()
    return h
def add_rows(*rows):
    out=[0]*max(map(len,rows))
    for h in rows:
        for i,v in enumerate(h):out[i]+=v
    return trim(out)
def scale(h,c):return trim([c*v for v in h])
def sub(a,b):return add_rows(a,scale(b,-1))
def conv(a,b):
    c=[0]*(len(a)+len(b)-1);c[0]=a[0]*b[0]
    for i in range(1,len(a)):c[i]+=a[i]*b[0]
    for j in range(1,len(b)):c[j]+=a[0]*b[j]
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            v=a[i]*b[j];c[i+j]+=v;c[abs(i-j)]+=v*(2 if i==j else 1)
    return trim(c)


def canonical_data(m,k):
    u=[[1],[3,2]]
    for j in range(1,m+1):u.append(sub(conv([3,2],u[-1]),u[-2]))
    running=[0];T=[]
    for h in u:running=add_rows(running,h);T.append(running)
    alpha,beta=T[m+1],T[m-1] if m else [0]
    oldtrace=add_rows(scale(conv([3,2,1],T[m]),3),[3,2])
    Rminus,Rprev=[0],[1];Rs=[[1]]
    for j in range(1,k+1):
        Rnext=add_rows(sub(conv(oldtrace,Rprev),Rminus),[1])
        Rs.append(Rnext);Rminus,Rprev=Rprev,Rnext
    Z=lambda j:add_rows(conv(alpha,Rs[j]),conv(beta,Rs[j-1] if j else [0]))
    A=sub(Z(k),T[m]);B=sub(Z(k-2),T[m]);X=add_rows([1],conv([1,1],Z(k-1)))
    trace=sub(scale(conv([1,1],X),3),[0,1])
    assert all(v>0 for v in A+B+trace)
    return A,B,trace


def pa(*polys):
    out={}
    for p in polys:
        for e,a in p.items():out[e]=out.get(e,0)+a
    return {e:a for e,a in out.items() if a}
def ps(p,c):return {e:a*c for e,a in p.items() if a*c}
def pm(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(i+j for i,j in zip(e,f));out[g]=out.get(g,0)+a*b
    return {e:a for e,a in out.items() if a}
def bernstein(p,dim):
    """2**dim times every tensor degree-2 Bernstein coefficient."""
    size=3**dim;power=[0]*size
    for e,a in p.items():
        assert all(0<=v<=2 for v in e)
        power[sum(v*3**j for j,v in enumerate(e))]=a
    out=list(power)
    for axis in range(dim):
        stride=3**axis
        for base in range(0,size,3*stride):
            for j in range(stride):
                i=base+j;a,b,c=(out[i+t*stride] for t in range(3))
                out[i],out[i+stride],out[i+2*stride]=2*a,2*a+b,2*(a+b+c)
    recovered=list(out)
    for axis in range(dim):
        stride=3**axis
        for base in range(0,size,3*stride):
            for j in range(stride):
                i=base+j;a,b,c=(recovered[i+t*stride] for t in range(3))
                recovered[i],recovered[i+stride],recovered[i+2*stride]=a,2*(b-a),a-2*b+c
    assert recovered==[2**dim*a for a in power]
    return out


def certificate(A,B,t,kind,smooth):
    T=sub(t,[2]);AT=conv(A,T)
    if kind=='single':
        dim=1;terms={(0,):add_rows(AT,B),(1,):scale(A,4)}
    else:
        dim=2;linear=add_rows(scale(AT,4),scale(B,2))
        terms={(0,0):add_rows(conv(AT,T),conv(B,T)),(1,0):linear,
               (0,1):linear,(1,1):scale(A,16)}
    if smooth:terms={e:conv(h,[1,1]) for e,h in terms.items()};B=conv(B,[1,1])
    zero=(0,)*dim;base=terms[zero];degree=len(base)-1
    assert all(v>0 for v in base)
    dominance=min(Q(base[n],b) for n,b in enumerate(B) if b)
    row=[{e:h[n] for e,h in terms.items() if n<len(h) and h[n]} for n in range(degree+1)]
    at=lambda n:row[abs(n)] if abs(n)<len(row) else {}
    records=[];best=None;minimum=None;relative_min=None;digest=sha256();count=0
    for n,h in enumerate(row):
        square=pm(h,h)
        delta=pa(square,ps(pm(at(n-1),at(n+1)),-1),ps(pm(at(n+1),at(n+1)),-1),pm(h,at(n+2)))
        d=bernstein(delta,dim);s=bernstein(square,dim)
        assert all(a>0 for a in d),('defect',kind,smooth,n,d)
        assert all(a>0 for a in s)
        eta=min(Q(a,b) for a,b in zip(d,s));best=eta if best is None else min(best,eta)
        rec={'n':n,'scaled_defect_bernstein':d,'scaled_square_bernstein':s}
        if kind=='midpoint':
            relative=[dominance.numerator**2*a-16*dominance.denominator**2*b for a,b in zip(d,s)]
            assert all(a>=0 for a in relative),('relative',smooth,n,min(relative))
            rec['scaled_relative_bernstein']=relative
            relative_min=min(relative) if relative_min is None else min(relative_min,min(relative))
        minimum=min(d) if minimum is None else min(minimum,min(d))
        for field in ('scaled_defect_bernstein','scaled_square_bernstein','scaled_relative_bernstein'):
            for v in rec.get(field,[]):digest.update(str(v).encode());digest.update(b'\n')
        records.append(rec);count+=len(d)
    return {'kind':kind,'smooth_y':smooth,'degree':degree,'parameter_dimension':dim,
            'eta_lower_bound':str(best),'dominance_over_reference':str(dominance),
            'minimum_scaled_defect':minimum,'minimum_scaled_relative':relative_min,
            'bernstein_coefficient_count':count,'ordered_margin_sha256':digest.hexdigest(),
            'coefficients':records}


def main():
    pairs=[(m,k) for m,stop in ((0,21),(1,11),(2,6),(3,5),(4,4),(5,5)) for k in range(3,stop)]
    assert len(pairs)==34
    records=[]
    for m,k in pairs:
        A,B,t=canonical_data(m,k)
        certs=[certificate(A,B,t,kind,smooth) for kind in ('single','midpoint') for smooth in (False,True)]
        record={'m':m,'k':k,'A_degree':len(A)-1,'B_degree':len(B)-1,'new_trace_degree':len(t)-1,'certificates':certs}
        records.append(record)
        print(json.dumps({'m':m,'k':k,'status':'PASS','coefficient_count':sum(r['bernstein_coefficient_count'] for r in certs),
                          'minimum_eta':str(min(Q(r['eta_lower_bound']) for r in certs))}),flush=True)
    out={'status':'PASS','scope':'34 finite (m,k) prefixes; all spectral r,s in [-2,2], c=(r+s)/2',
         'method':'Exact symmetric-Laurent recurrence and full tensor degree-two Bernstein with inverse reconstruction',
         'records':records}
    Path(__file__).with_name('finite_mixed_kernels_results.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
