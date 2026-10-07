"""Exact degree-two Bernstein proofs for the remaining one-turn single blocks."""
import argparse
import hashlib
import json
from fulltree_oneturn_finite import at, add, times, prefixes


def certificate(base, slope, twice_strength):
    minima = [None]*3
    digest = hashlib.sha256()
    negative = zero = 0
    for n in range(len(base)):
        v = [(at(base, j), at(slope, j)) for j in [n-1, n, n+1, n+2]]
        p, h, b, c = v
        d0 = h[0]**2-p[0]*b[0]-b[0]**2+h[0]*c[0]
        d1 = 2*h[0]*h[1]-p[0]*b[1]-p[1]*b[0]-2*b[0]*b[1]+h[0]*c[1]+h[1]*c[0]
        d2 = h[1]**2-p[1]*b[1]-b[1]**2+h[1]*c[1]
        for a in range(3):
            margin = 4*d0+2*a*d1+2*a*(a-1)*d2-twice_strength*(2*h[0]+a*h[1])
            negative += margin < 0
            zero += margin == 0
            minima[a] = margin if minima[a] is None else min(minima[a], margin)
            digest.update((str(margin)+'\n').encode())
    return dict(degree=len(base)-1, margins=3*len(base), twice_strength=str(twice_strength),
                negative=negative, zero=zero, minima=list(map(str, minima)), sha256=digest.hexdigest())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max', type=int, default=390)
    args=parser.parse_args()
    ts=prefixes(args.max+1)
    results=[]
    for m in range(1,args.max+1):
        A,B=ts[m+1],ts[m-1]
        t=[3*v for v in times([3,2,1],ts[m])]
        t[0]+=5
        t[1]+=2
        L=add(times(A,t),B)
        slope=[-4*v for v in A]
        twice=3*2**(2*m-2)
        for label,base,sl in [('L',L,slope),('yL',times([1,1],L),times([1,1],A))]:
            if label=='yL':
                sl=[-4*v for v in sl]
            r=certificate(base,sl,twice)
            r.update(m=m,label=label)
            results.append(r)
        if m<=3:
            yf=times([1,1],t)
            r=certificate(yf,[-4,-4],3*2**(m-1))
            r.update(m=m,label='yf')
            results.append(r)
    output=dict(status='PASS' if all(r['negative']==r['zero']==0 for r in results) else 'FAIL',
                scaling='4 times Bernstein coefficient of delta_n(H) - (twice_strength/2) H_n',
                cases=results)
    with open('fulltree_oneturn_single_finite_results.json','w') as f:
        json.dump(output,f,indent=2)
    print(json.dumps(dict(status=output['status'], cases=len(results),
                         margins=sum(r['margins'] for r in results),
                         failed=[(r['m'],r['label'],r['negative'],r['zero']) for r in results if r['negative'] or r['zero']]),indent=2))


if __name__=='__main__':
    main()
