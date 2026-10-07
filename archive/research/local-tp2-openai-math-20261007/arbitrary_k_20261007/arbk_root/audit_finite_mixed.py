#!/usr/bin/env python3
"""Independent reconstruction of the 34 mixed-kernel certificates.

This uses original ordinary-x mutations and exact evaluation/interpolation.
The author uses the old one-turn half-row recurrence and sparse parameter
polynomials. No author code, adapter, or expected array is used to build
these data. Expected JSON is read only after reconstruction for comparison.
"""
from fractions import Fraction
from math import comb
from hashlib import sha256
from pathlib import Path
import json


def plus(a,b):
    c=[0]*max(len(a),len(b))
    for i in range(len(c)):c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(c)>1 and not c[-1]:c.pop()
    return c

def scale(a,c):return [c*v for v in a]
def minus(a,b):return plus(a,scale(b,-1))
def product(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c

def mutation(st,left):
    a,c,b=st
    if left:lower,upper=a,b
    else:lower,upper=b,a
    z=minus(minus(scale(product(product([1,1],lower),c),3),product([0,1],plus(lower,c))),upper)
    return (a,z,c) if left else (c,z,b)

def div_y(p):
    q=[0]*(len(p)-1)
    for j in range(len(q)-1,-1,-1):q[j]=p[j+1]-(q[j+1] if j+1<len(q) else 0)
    assert product([1,1],q)==p
    return q

def row(p):return [sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2)) for n in range(len(p))]
def val(h,n):return h[abs(n)] if abs(n)<len(h) else 0
def defect(h,n):return val(h,n)**2-val(h,n-1)*val(h,n+1)-val(h,n+1)**2+val(h,n)*val(h,n+2)

def bernstein_from_evaluations(values,dim):
    out=list(values)
    # Values are at 0,1/2,1 on each axis. Each transform clears a factor2.
    for axis in range(dim):
        stride=3**axis
        for start in range(0,len(out),3*stride):
            for off in range(stride):
                i=start+off;a,b,c=[out[i+j*stride] for j in range(3)]
                out[i],out[i+stride],out[i+2*stride]=2*a,4*b-a-c,2*c
    # Verify reverse Bernstein evaluation at the same three exact nodes.
    inv=list(out)
    for axis in range(dim):
        stride=3**axis
        for start in range(0,len(inv),3*stride):
            for off in range(stride):
                i=start+off;a,b,c=[inv[i+j*stride] for j in range(3)]
                inv[i],inv[i+stride],inv[i+2*stride]=4*a,a+2*b+c,4*c
    assert inv==[(8**dim)*v for v in values]
    return out

def one_certificate(A,B,t,kind,smooth):
    dim=1 if kind=='single' else 2
    hs=[]
    for v in (range(3) if dim==2 else range(1)):
        for u in range(3):
            r,s=2-2*u,2-2*v
            tr=minus(t,[r])
            if dim==1:P=plus(product(A,tr),B)
            else:P=plus(product(product(A,tr),minus(t,[s])),product(B,minus(t,[(r+s)//2])))
            if smooth:P=product(P,[1,1])
            hs.append(row(P))
    ref=row(product(B,[1,1]) if smooth else B)
    dominance=min(Fraction(hs[0][n],b) for n,b in enumerate(ref) if b)
    assert all(v>0 for h in hs for v in h)
    certs=[];checksum=sha256();minimum=None;relative_min=None;eta=Fraction(1)
    for n in range(len(hs[0])):
        ds=bernstein_from_evaluations([defect(h,n) for h in hs],dim)
        ss=bernstein_from_evaluations([h[n]**2 for h in hs],dim)
        assert min(ds)>0 and min(ss)>0
        record={'n':n,'scaled_defect_bernstein':ds,'scaled_square_bernstein':ss}
        if dim==2:
            rr=[dominance.numerator**2*a-16*dominance.denominator**2*b for a,b in zip(ds,ss)]
            assert min(rr)>0
            record['scaled_relative_bernstein']=rr
            relative_min=min(rr) if relative_min is None else min(relative_min,min(rr))
        eta=min(eta,min(Fraction(a,b) for a,b in zip(ds,ss)))
        minimum=min(ds) if minimum is None else min(minimum,min(ds))
        for field in ['scaled_defect_bernstein','scaled_square_bernstein','scaled_relative_bernstein']:
            for item in record.get(field,[]):checksum.update(str(item).encode());checksum.update(b'\n')
        certs.append(record)
    return {'kind':kind,'smooth_y':smooth,'degree':len(hs[0])-1,'parameter_dimension':dim,
        'eta_lower_bound':str(eta),'dominance_over_reference':str(dominance),
        'minimum_scaled_defect':minimum,'minimum_scaled_relative':relative_min,
        'bernstein_coefficient_count':len(hs[0])*3**dim,
        'ordered_margin_sha256':checksum.hexdigest(),'coefficients':certs}


def main():
    limits={0:21,1:11,2:6,3:5,4:4,5:5}
    pure=([1],[5,6,2],[2,1]);records=[]
    for m,limit in limits.items():
        st=pure
        for k in range(1,limit):
            st=mutation(st,False)
            if k<3:continue
            X,C,Y=st;t=minus(scale(product([1,1],X),3),[0,1])
            inverse=minus(minus(product(t,Y),product([0,1],X)),C)
            A=div_y(minus(C,Y));B=div_y(minus(inverse,Y))
            certificates=[one_certificate(A,B,t,kind,sm) for kind in ['single','midpoint'] for sm in [False,True]]
            records.append({'m':m,'k':k,'A_degree':len(A)-1,'B_degree':len(B)-1,'new_trace_degree':len(t)-1,'certificates':certificates})
        pure=mutation(pure,True)
    assert len(records)==34
    # Expected output is used solely for comparison after every coefficient
    # above was independently reconstructed from the canonical mutations.
    target=Path(__file__).resolve().parent.parent/'arbk_mixed/finite_mixed_kernels_results.json'
    expected=json.loads(target.read_text())
    assert records==expected['records']
    cs=[c for r in records for c in r['certificates']]
    out={'status':'PASS','independence':'Original ordinary-x mutations plus exact 3x3 interpolation; no author code imported',
         'prefix_count':34,'all_record_fields_and_coefficients_match':True,
         'strict_defect_bernstein_coefficients':sum(c['bernstein_coefficient_count'] for c in cs),
         'strict_relative_bernstein_coefficients':sum(c['bernstein_coefficient_count'] for c in cs if c['kind']=='midpoint'),
         'expected_artifact_sha256':sha256(target.read_bytes()).hexdigest(),
         'independent_ordered_digest_list':[c['ordered_margin_sha256'] for c in cs]}
    Path(__file__).with_name('finite_mixed_independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='independent_ordered_digest_list'},indent=2))
if __name__=='__main__':main()
