#!/usr/bin/env python3
"""Normalized continuum certificates for paired m=0 trace blocks.

All parameters are independent.  Arithmetic is integral except when the
best certified normalized constant is reported as an exact Fraction.
"""
from fractions import Fraction as Q
from itertools import product
from hashlib import sha256
from pathlib import Path
import argparse
import json


def trim(h):
    h=list(h)
    while len(h)>1 and h[-1]==0:h.pop()
    return h
def plus(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([c*v for v in a])
def conv(a,b):
    c=[0]*(len(a)+len(b)-1);c[0]=a[0]*b[0]
    for i in range(1,len(a)):c[i]+=a[i]*b[0]
    for j in range(1,len(b)):c[j]+=a[0]*b[j]
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            v=a[i]*b[j];c[i+j]+=v;c[abs(i-j)]+=v*(2 if i==j else 1)
    return trim(c)


def add(*polys):
    out={}
    for p in polys:
        for e,a in p.items():out[e]=out.get(e,0)+a
    return {e:a for e,a in out.items() if a}
def sc(p,c):return {e:a*c for e,a in p.items() if a*c}
def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(i+j for i,j in zip(e,f));out[g]=out.get(g,0)+a*b
    return {e:a for e,a in out.items() if a}


def bernstein(p,dim):
    """Return 2^dim times every degree-two tensor Bernstein coefficient."""
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


def row_product(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(i+j for i,j in zip(e,f));h=conv(a,b)
            out[g]=plus(out.get(g,[0]),h)
    return out


def build(npairs,seed=False,smooth=False,single=False):
    dim=2*npairs+int(single);zero=(0,)*dim
    # H(t_*)=(12,8,3), t_*=3x^2+8x+6.
    t=[12,8,3]
    base=[4,2] if seed else [1]
    if smooth:base=conv([1,1],base)
    result={zero:base}
    for pair in range(npairs):
        e=list(zero);e[2*pair]=1
        f=list(zero);f[2*pair+1]=1
        p0=plus(conv(t,t),[-4])
        factor={zero:p0,tuple(e):scale(t,4),tuple(f):[8]}
        result=row_product(result,factor)
    if single:
        e=list(zero);e[-1]=1
        result=row_product(result,{zero:t,tuple(e):[2]})
    degree=max(len(h) for h in result.values())-1
    row=[{e:h[n] for e,h in result.items() if n<len(h) and h[n]}
         for n in range(degree+1)]
    # All input coefficients in this parameterization are nonnegative;
    # the constant half-row is strictly positive throughout support.
    assert all(row[n].get(zero,0)>0 for n in range(degree+1))
    return row,dim


def certificate(npairs,seed=False,smooth=False,single=False,target=Q(1,128),full=False):
    row,dim=build(npairs,seed,smooth,single)
    at=lambda n:row[abs(n)] if abs(n)<len(row) else {}
    best=None;arg=None;count=0;minimum=None;digest=sha256();records=[]
    for n,h in enumerate(row):
        square=mul(h,h)
        defect=add(square,sc(mul(at(n-1),at(n+1)),-1),sc(mul(at(n+1),at(n+1)),-1),mul(h,at(n+2)))
        d=bernstein(defect,dim);s=bernstein(square,dim)
        margins=[]
        for j,(a,b) in enumerate(zip(d,s)):
            assert b>0
            v=Q(a,b)
            if best is None or v<best:best,arg=v,(n,j)
            margin=target.denominator*a-target.numerator*b
            margins.append(margin)
            minimum=margin if minimum is None else min(minimum,margin)
            digest.update(str(margin).encode());digest.update(b'\n')
        count+=len(margins)
        record={'n':n,'minimum_scaled_margin':min(margins)}
        if full:record['scaled_tensor_bernstein']=margins
        records.append(record)
    return {'pairs':npairs,'seed_2p':seed,'smooth_y':smooth,'nonpositive_single':single,
            'degree':len(row)-1,'parameter_dimension':dim,'target_eta':str(target),
            'best_tensor_certified_eta':str(best),'best_eta_location':arg,
            'best_eta_floor_reciprocal':best.denominator//best.numerator if best>0 else None,
            'certified':minimum>=0,'bernstein_coefficient_count':count,
            'minimum_scaled_margin':minimum,'ordered_margin_sha256':digest.hexdigest(),
            'records':records}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--residues',action='store_true');ap.add_argument('--full',action='store_true')
    args=ap.parse_args();records=[]
    for p in (1,2,3,4):
        rec=certificate(p,target=Q(1,128),full=args.full);records.append(rec)
        assert rec['certified'], ('block',p)
        print(json.dumps({k:v for k,v in rec.items() if k!='records'}),flush=True)
    if args.residues:
        for p,s,y in product(range(4),(False,True),(False,True)):
            rec=certificate(p,seed=True,smooth=y,single=s,target=Q(1,256),full=args.full)
            assert rec['certified'], ('residue',p,s,y)
            records.append(rec)
            print(json.dumps({k:v for k,v in rec.items() if k!='records'}),flush=True)
    result={'records':records,'method':'Exact symmetric-Laurent convolution; full tensor Bernstein with integer inverse reconstruction'}
    dest=Path(__file__).with_name('m0_normalized_blocks_results.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
