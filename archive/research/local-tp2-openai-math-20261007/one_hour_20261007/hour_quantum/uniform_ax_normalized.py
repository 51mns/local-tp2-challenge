#!/usr/bin/env python3
"""Exact finite normalized-defect bridge for a_X and y a_X, m=0,...,390.

The infinite tail is proved in UNIFORM_SEED_STRENGTH.md.  Symmetric Laurent
rows are generated directly from the inner recurrence.  Positive convolution
uses exact carry-free integer packing (standard Python integer multiplication),
so no external numeric library or floating-point arithmetic is used.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def get(h,n):
    return h[abs(n)] if abs(n)<len(h) else 0


def add(h,k):
    return [get(h,n)+get(k,n) for n in range(max(len(h),len(k)))]


def scale(h,c):
    return [c*v for v in h]


def times_y(h):
    return [get(h,n-1)+get(h,n)+get(h,n+1) for n in range(len(h)+1)]


def delta(h,n):
    return get(h,n)**2-get(h,n-1)*get(h,n+1)-get(h,n+1)**2+get(h,n)*get(h,n+2)


def positive_convolution(a,b):
    """Return ordinary convolution exactly, with a proved no-carry width."""
    assert all(v>=0 for v in a+b) and max(a)>0 and max(b)>0
    bits=max(a).bit_length()+max(b).bit_length()+min(len(a),len(b)).bit_length()
    width=(bits+7)//8
    assert min(len(a),len(b))*max(a)*max(b)<1<<(8*width)
    pack=lambda p:int.from_bytes(b''.join(v.to_bytes(width,'little') for v in p),'little')
    n=len(a)+len(b)-1
    raw=(pack(a)*pack(b)).to_bytes(width*n,'little')
    return [int.from_bytes(raw[i*width:(i+1)*width],'little') for i in range(n)]


def multiply(h,k):
    full_h=list(reversed(h[1:]))+h
    full_k=list(reversed(k[1:]))+k
    out=positive_convolution(full_h,full_k)
    degree=len(h)+len(k)-2
    assert out==list(reversed(out))
    return out[degree:]


def digest(values):
    h=sha256()
    for v in values:h.update((str(v)+'\n').encode())
    return h.hexdigest()


def main():
    umax=391
    u=[[1],[3,2]]
    for m in range(1,umax):
        h=[3*get(u[-1],n)+2*get(u[-1],n-1)+2*get(u[-1],n+1)-get(u[-2],n)
           for n in range(m+2)]
        assert all(v>0 for v in h)
        u.append(h)
    prefix=[]
    accum=[0]
    for h in u:
        accum=add(accum,h)
        prefix.append(accum)
    records=[]
    count=0
    for m in range(391):
        Y=times_y(prefix[m]);Y[0]+=1
        t=scale(times_y(Y),3);t[1]-=1
        tplus=t.copy();tplus[0]+=1
        aX=add(multiply(prefix[m+1],tplus),prefix[m-1] if m else [0])
        assert len(aX)==2*m+4 and all(v>0 for v in aX)
        numerator=59**(2*m+1)
        denominator=400000000**2*100**(2*m+1)*16*(m+3)
        record={'m':m,'normalized_target_numerator':str(numerator),
                'normalized_target_denominator':str(denominator),'rows':{}}
        for name,h in [('aX',aX),('yaX',times_y(aX))]:
            margins=[]
            ds=[]
            best=0
            for n in range(len(h)):
                d=delta(h,n)
                assert d>0
                ds.append(d)
                margin=denominator*d-numerator*h[n]**2
                assert margin>0,(m,name,n)
                margins.append(margin)
                if d*h[best]**2<ds[best]*h[n]**2:best=n
            count+=len(margins)
            minimum=min(margins)
            record['rows'][name]={
                'degree':len(h)-1,'supported_margin_count':len(h),
                'minimum_integer_margin':str(minimum),
                'minimum_margin_index':margins.index(minimum),
                'halfrow_sha256':digest(h),'margin_sha256':digest(margins),
                'minimum_actual_eta_index':best,
                'minimum_actual_eta':str(Fraction(ds[best],h[best]**2)),
            }
        records.append(record)
        if m%50==0:print('m =',m,'exact supported margins checked =',count,flush=True)
    result={
        'statement':'eta(aX), eta((x+1)aX) >= c0^2 sigma^(2m+1)/(16(m+3)) for all m>=0',
        'constants':{'c0':'1/400000000','sigma':'59/100'},
        'finite_range':[0,390],'finite_margin_count':count,
        'finite_records':records,
        'tail_start':391,
        'tail_reason':'Inherited EL_m bound and delta(sum)>=delta(dominant)/2; correction ratio epsilon<1/3 implies eta(sum)>=EL_m/4.',
        'exact_algorithm':'Integer recurrence and carry-free positive Laurent convolution; every supported comparison uses integer crossmultiplication.',
        'status':'Finite exact gates PASS; infinite assembly in UNIFORM_SEED_STRENGTH.md',
    }
    path=Path(__file__).with_name('uniform_ax_normalized_certificates.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','finite_range':[0,390],
                      'supported_margin_count':count,'output':path.name},indent=2))


if __name__=='__main__':
    main()
