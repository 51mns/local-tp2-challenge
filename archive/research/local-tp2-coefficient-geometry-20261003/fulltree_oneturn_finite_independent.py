"""Independent continuum replay in ordinary x and generic parameter monomials.

No source routines, Fourier convolution, or hand-written Bernstein weight arrays
are imported from the primary verifier. Every arithmetic value is a Python int.
NumPy object arrays accelerate exact vector operations only.
"""
import argparse
from fractions import Fraction
from math import comb
import hashlib
import itertools
import json
import time
import numpy as np


def ordinary_add(a,b):
    c=[0]*max(len(a),len(b))
    for j,x in enumerate(a): c[j]+=x
    for j,x in enumerate(b): c[j]+=x
    return c


def ordinary_product(a,b):
    assert min(a)>=0 and min(b)>=0
    # An entirely ordinary-x product. The coefficient sum is an independent
    # carry bound: every output coefficient is at most sum(a)*sum(b).
    bits=(sum(a)*sum(b)).bit_length()
    bits=max(bits,1)
    pa=pb=0
    for x in reversed(a): pa=(pa<<bits)+x
    for x in reversed(b): pb=(pb<<bits)+x
    product=pa*pb
    mask=(1<<bits)-1
    out=[]
    for _ in range(len(a)+len(b)-1):
        out.append(product&mask)
        product >>= bits
    assert product==0
    assert sum(out)==sum(a)*sum(b)
    return out


def ordinary_prefixes(maximum):
    previous=[0]
    current=[1]
    total=[1]
    result=[total]
    for _ in range(maximum):
        following=[0]*(len(current)+1)
        for j,x in enumerate(current):
            following[j]+=3*x
            following[j+1]+=2*x
        for j,x in enumerate(previous): following[j]-=x
        assert min(following)>0
        total=ordinary_add(total,following)
        result.append(total)
        previous,current=current,following
    return result


PARAM_MONOMIALS=[(0,0,0),(1,0,0),(0,1,0),(1,1,0),(0,0,1)]
SQUARE_MONOMIALS=sorted({tuple(x+y for x,y in zip(a,b))
                        for a in PARAM_MONOMIALS for b in PARAM_MONOMIALS})
INDICES=list(itertools.product(range(3),repeat=3))


def scaled_bernstein(index,power):
    coefficient=Fraction(8)
    for k,j in zip(index,power):
        if j>k: return 0
        coefficient*=Fraction(comb(k,j),comb(2,j))
    assert coefficient.denominator==1
    return coefficient.numerator


BERNSTEIN=np.array([[scaled_bernstein(k,p) for k in INDICES]
                    for p in SQUARE_MONOMIALS],dtype=object)
LINEAR=np.array([[scaled_bernstein(k,p) for k in INDICES]
                 for p in PARAM_MONOMIALS],dtype=object)


def ordinary_fourier_matrix(maximum):
    matrix=np.zeros((maximum+1,maximum+1),dtype=object)
    for j in range(maximum+1):
        for q in range(j//2+1): matrix[j-2*q,j]=comb(j,q)
    return matrix


def certify(m,prefix,transform,smooth=False):
    A,B=prefix[m+1],prefix[m-1]
    if smooth:
        A=ordinary_product([1,1],A)
        B=ordinary_product([1,1],B)
    trace=ordinary_product([1,2,1],prefix[m])
    trace=[3*x for x in trace]
    trace[0]+=5
    trace[1]+=2
    At=ordinary_product(A,trace)
    constant=ordinary_add(ordinary_product(At,trace),ordinary_product(B,trace))
    degree=len(constant)-1
    # This is H(x;u,v,w)=constant-4 At*u-4 At*v+16 A*uv-4 B*w,
    # obtained by expanding r=-2+4u, s=-2+4v, c=-2+4w in ordinary x.
    ordinary=np.zeros((degree+1,5),dtype=object)
    for j,(row,scalar) in enumerate([(constant,1),(At,-4),(At,-4),(A,16),(B,-4)]):
        ordinary[:len(row),j]=[scalar*x for x in row]
    half=transform[:degree+1,:degree+1]@ordinary
    base0=sum(B[j]*comb(j,j//2) for j in range(0,len(B),2))
    mu=8*base0
    assert degree==3*m+5+int(smooth)
    assert half[degree,0]==18*8**m
    extended=np.vstack([half,np.zeros((2,5),dtype=object)])
    current=extended[:degree+1]
    previous=np.vstack([half[1],half[:degree]])
    following=extended[1:degree+2]
    second=extended[2:degree+3]
    # Multiply generic parameter polynomials. No polarized-defect shortcut
    # and no certificate-specific weights are used.
    coefficients=np.zeros((degree+1,len(SQUARE_MONOMIALS)),dtype=object)
    for i,p in enumerate(PARAM_MONOMIALS):
        for j,q in enumerate(PARAM_MONOMIALS):
            exponent=tuple(a+b for a,b in zip(p,q))
            column=SQUARE_MONOMIALS.index(exponent)
            coefficients[:,column]+=(current[:,i]*current[:,j]
               -previous[:,i]*following[:,j]-following[:,i]*following[:,j]
               +current[:,i]*second[:,j])
    margins=coefficients@BERNSTEIN-mu*(current@LINEAR)
    minimum=None
    witness=None
    digest=hashlib.sha256()
    negative=zero=0
    for n,row in enumerate(margins):
        for index,raw in zip(INDICES,row):
            value=int(raw)
            digest.update((str(value)+'\n').encode())
            negative+=value<0
            zero+=value==0
            if minimum is None or value<minimum:
                minimum=value
                witness=[n,*index]
    return dict(m=m,degree=degree,margins=(degree+1)*27,negative=negative,
                zero=zero,minimum=str(minimum),witness=witness,sha256=digest.hexdigest())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--min',type=int,default=1)
    parser.add_argument('--max',type=int,default=390)
    parser.add_argument('--smooth',action='store_true')
    parser.add_argument('--output',default='fulltree_oneturn_finite_independent_results.json')
    args=parser.parse_args()
    start=time.monotonic()
    prefix=ordinary_prefixes(args.max+1)
    transform=ordinary_fourier_matrix(3*args.max+5+int(args.smooth))
    results=[]
    for m in range(args.min,args.max+1):
        result=certify(m,prefix,transform,args.smooth)
        results.append(result)
        if m%10==0 or result['negative'] or result['zero'] or m==args.max:
            print(json.dumps({k:result[k] for k in ['m','degree','negative','zero','witness']}),flush=True)
        output=dict(status='PASS' if all(x['negative']==x['zero']==0 for x in results) else 'FAIL',
                    scope=[args.min,m],smooth=args.smooth,method='ordinary x recurrence and products; binomial Fourier transform; generic parameter polynomial multiplication; defining tensor Bernstein transform',
                    arithmetic='Python arbitrary-precision integers and NumPy dtype=object',
                    scaling='8 times Bernstein coefficient of delta_n(H)-8 H(B)_0 H(H)_n; with A,B replaced by yA,yB if smooth',
                    elapsed_seconds=round(time.monotonic()-start,3),cases=results)
        with open(args.output,'w') as f: json.dump(output,f,indent=2)
    assert output['status']=='PASS'


if __name__=='__main__': main()
