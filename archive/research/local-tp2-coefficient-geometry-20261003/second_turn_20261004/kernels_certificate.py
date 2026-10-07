"""Exact continuum finite bridge for the reversed second-turn pair.

This deliberately reuses only the disclosed parent half-row arithmetic
and inner prefix recurrence. The parameter expansion and strength targets
are reconstructed here. Each defect polynomial has coordinate degrees
at most two; all 27 Bernstein coefficients, not parameter samples, are
certified on the entire independent cube. An integer digest records every
coefficient in fixed lexicographic order.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from fulltree_oneturn_finite import at, add, times, prefixes


INDICES = list(itertools.product(range(3), repeat=3))


def bernstein_weights(a, b, u):
    aa, bb, uu = a*(a-1)//2, b*(b-1)//2, u*(u-1)//2
    table = [[8, 4*(a+b), 2*a*b, 4*u],
             [0, 8*(aa+bb)+4*a*b, 4*(aa*b+bb*a), 2*(a+b)*u],
             [0, 0, 8*aa*bb, a*b*u],
             [0, 0, 0, 8*uu]]
    return [table[i][j] for i in range(4) for j in range(i,4)], table[0]


WEIGHTS = [bernstein_weights(*abc) for abc in INDICES]


def quadratics(rows, n):
    prev, cur, nex, nex2 = [[at(row,j) for row in rows]
                          for j in [n-1,n,n+1,n+2]]
    coefficients = []
    for i in range(len(rows)):
        for j in range(i,len(rows)):
            if i == j:
                value = cur[i]*cur[i]-prev[i]*nex[i]-nex[i]*nex[i]+cur[i]*nex2[i]
            else:
                value = (2*cur[i]*cur[j]-prev[i]*nex[j]-prev[j]*nex[i]
                         -2*nex[i]*nex[j]+cur[i]*nex2[j]+cur[j]*nex2[i])
            coefficients.append(value)
    return coefficients, cur


def single_certificate(base, slope, m):
    # lambda=3*2^(2m-3), including lambda=3/8 at m=0.
    numerator = 3*2**max(0,2*m-3)
    denominator = 2**max(0,3-2*m)
    minimum, witness = None, None
    negative = zero = 0
    digest = hashlib.sha256()
    for n in range(len(base)):
        (d0,d1,d2), cur = quadratics([base,slope],n)
        for a in range(3):
            margin = (denominator*(4*d0+2*a*d1+2*a*(a-1)*d2)
                      -2*numerator*(2*cur[0]+a*cur[1]))
            digest.update((str(margin)+'\n').encode())
            negative += margin < 0
            zero += margin == 0
            if minimum is None or margin < minimum:
                minimum, witness = margin, [n,a]
    return dict(degree=len(base)-1,margins=3*len(base),
                lambda_numerator=str(numerator),lambda_denominator=denominator,
                scale=4*denominator,negative=negative,zero=zero,
                minimum=str(minimum),witness=witness,sha256=digest.hexdigest())


def midpoint_certificate(comps, alpha, d0):
    minimum, witness = None, None
    negative = zero = 0
    digest = hashlib.sha256()
    for n in range(len(comps[0])):
        quad, cur = quadratics(comps,n)
        for abc,(weights,linear) in zip(INDICES,WEIGHTS):
            margin = (alpha*sum(w*q for w,q in zip(weights,quad))
                      -8*d0*sum(w*h for w,h in zip(linear,cur)))
            digest.update((str(margin)+'\n').encode())
            negative += margin < 0
            zero += margin == 0
            if minimum is None or margin < minimum:
                minimum, witness = margin, [n,*abc]
    return dict(degree=len(comps[0])-1,margins=27*len(comps[0]),
                alpha=str(alpha),reference_central=str(d0),scale=8,
                negative=negative,zero=zero,minimum=str(minimum),
                witness=witness,sha256=digest.hexdigest())


def certify_case(m,ts,smooth):
    c,d=ts[m],ts[m+2]
    if smooth:
        c,d=times([1,1],c),times([1,1],d)
    tauplus2=[3*v for v in times([3,2,1],ts[m+1])]
    tauplus2[0]+=5
    tauplus2[1]+=2
    alpha=tauplus2[0]-4
    ct=times(c,tauplus2)
    single=single_certificate(add(ct,d),[-4*v for v in c],m)
    comps=[add(times(ct,tauplus2),times(d,tauplus2)),
           [-4*v for v in ct],[16*v for v in c],[-4*v for v in d]]
    midpoint=midpoint_certificate(comps,alpha,d[0])
    for label,record in [('single',single),('midpoint',midpoint)]:
        record.update(m=m,smooth=smooth,label=label)
    return [single,midpoint]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--min',type=int,default=0)
    parser.add_argument('--max',type=int,default=409)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('kernels_certificate_results.json'))
    args=parser.parse_args()
    start=time.monotonic()
    ts=prefixes(args.max+2)
    results=[]
    for m in range(args.min,args.max+1):
        for smooth in (False,True):
            results.extend(certify_case(m,ts,smooth))
        if m<3 or m%10==0 or m==args.max or any(r['negative'] or r['zero'] for r in results[-4:]):
            print(json.dumps(dict(m=m,failed=[(r['smooth'],r['label'],r['negative'],r['zero'])
                                            for r in results[-4:] if r['negative'] or r['zero']])),flush=True)
        output=dict(status='PASS' if all(r['negative']==r['zero']==0 for r in results) else 'FAIL',
                    scope=[args.min,m],elapsed_seconds=round(time.monotonic()-start,3),
                    targets={'single':'delta(L)-3*2^(2m-3)*L_n, also yL',
                             'midpoint':'alpha*delta(H)-8*reference_central*H_n, also yH; alpha=tau_0-2'},
                    cases=results)
        args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(status=output['status'],cases=len(results),
                         margins=sum(r['margins'] for r in results),
                         elapsed_seconds=output['elapsed_seconds'])),flush=True)


if __name__=='__main__':
    main()
