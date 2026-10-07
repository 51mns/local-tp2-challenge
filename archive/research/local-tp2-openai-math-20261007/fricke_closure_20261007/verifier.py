"""Separate direct Laurent reconstruction from the original canonical mutations.

Does not import author.py, symbolic.py, or generated expected data. This is a
separate implementation by the same model, not an external independent review.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json


def clean(p):
    return {k:v for k,v in p.items() if v}


def plus(*ps):
    z={}
    for p in ps:
        for k,v in p.items():
            z[k]=z.get(k,0)+v
    return clean(z)


def scale(p,c):
    return clean({k:c*v for k,v in p.items()})


def minus(a,b):
    return plus(a,scale(b,-1))


def times(*ps):
    out={0:1}
    for p in ps:
        z={}
        for i,a in out.items():
            for j,b in p.items():
                z[i+j]=z.get(i+j,0)+a*b
        out=clean(z)
    return out


ONE={0:1}
x={-1:1,1:1}
y={-1:1,0:1,1:1}


def eval_ordinary(coefficients):
    out={}
    for value in reversed(coefficients):
        out=plus(times(out,x),{0:value})
    return out


def quot_y(p):
    """Exact symmetric Laurent division, cancelling the extreme pair at once."""
    result={}
    remainder=clean(dict(p))
    while remainder:
        degree=max(remainder)
        if degree<1:
            raise ArithmeticError('nonzero remainder after division by x+1')
        top=remainder[degree]
        exponent=degree-1
        term={0:top} if exponent==0 else {-exponent:top,exponent:top}
        result=plus(result,term)
        remainder=minus(remainder,times(y,term))
        if any(remainder.get(-k,0)!=v for k,v in remainder.items()):
            raise ArithmeticError('asymmetric remainder')
    return result


def mutation(X,C,Y):
    return minus(minus(scale(times(y,X,C),3),times(x,plus(X,C))),Y)


def node(word):
    X,Y,C=ONE,eval_ordinary((2,1)),eval_ordinary((5,6,2))
    for d in word:
        if d=='s':
            X,Y,C=X,C,mutation(X,C,Y)
        elif d=='l':
            X,Y,C=Y,C,mutation(Y,C,X)
        else:
            raise ValueError(d)
    assert max(X)<max(Y)<max(C)
    return X,Y,C


def half(p):
    return [p.get(i,0) for i in range(max(p,default=0)+1)]


def get(h,n):
    return h[abs(n)] if abs(n)<len(h) else 0


def deltas(h):
    Delta=[get(h,n)**2-get(h,n-1)*get(h,n+1) for n in range(len(h)+1)]
    return [Delta[i]-Delta[i+1] for i in range(len(h))]


def eta(h):
    return min(Fraction(d,h[i]**2) for i,d in enumerate(deltas(h)))


def ordinary(p):
    """Invert x=q+q^-1 by leading-degree elimination, for small witnesses."""
    remainder=dict(p)
    out=[0]*(max(p,default=0)+1)
    while remainder:
        degree=max(remainder)
        c=remainder[degree]
        out[degree]=c
        base=eval_ordinary([0]*degree+[1])
        remainder=minus(remainder,scale(base,c))
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def record(word):
    X,Y,C=node(word)
    t=minus(scale(times(y,X),3),x)
    T=minus(minus(times(t,Y),times(x,X)),C)
    u=quot_y(minus(X,ONE))
    e=quot_y(minus(Y,X))
    Q=quot_y(minus(Y,T))
    a=quot_y(minus(C,Y))
    g=minus(t,{0:2})
    k=times(X,minus(scale(X,3),{0:2}))
    R=minus(times(a,Q),plus(times(g,e,e),scale(times(k,e),2),scale(times(u,X,X),3)))
    assert not R
    assert not minus(a,plus(Q,times(g,e),k))
    assert all(v>=0 for v in minus(plus(u,e),Q).values())
    assert all(v>=0 for v in minus(a,times(minus(t,ONE),Q)).values())
    U,V=mutation(X,C,Y),mutation(Y,C,X)
    S,D=minus(U,C),minus(V,U)
    polys=dict(u=u,e=e,Q=Q,a=a,X=X,Y=Y,C=C,T=T,S=S,D=D)
    assert all(v>=0 for p in polys.values() for v in p.values())
    rows={n:half(p) for n,p in polys.items()}
    hs,hd=rows['S'],rows['D']
    minors=[get(hs,n)*get(hd,n+1)-get(hs,n+1)*get(hd,n) for n in range(len(hs))]
    assert min(minors)>0
    correction_bounds=[]
    for name,fixed,other in (('short',X,Y),('long',Y,X)):
        tr=minus(scale(times(y,fixed),3),x)
        inverse=minus(minus(times(tr,other),times(x,fixed)),C)
        A=quot_y(minus(C,other))
        B=quot_y(minus(inverse,other))
        assert all(v>=0 for v in B.values()) or all(v<=0 for v in B.values())
        if any(v<0 for v in B.values()):
            nu=tr.get(0,0)
            denominator=(nu-1)*(nu-2)
            margin=half(plus(times(A,minus(tr,{0:2})),scale(B,denominator)))
            assert min(margin)>=0
            correction_bounds.append(dict(direction=name,nu=str(nu),
                                          epsilon=str(Fraction(1,denominator)),
                                          margin_sha256=digest(margin)))
    return dict(word=word,rows_sha256=digest(rows),
                negative_seed_bounds=correction_bounds,
                degrees={n:max(polys[n]) for n in ('X','Y','C','S','D')},
                minor_count=len(minors),minimum_minor=str(min(minors)))


def counterexamples():
    P,Q=eval_ordinary((3,44,30,3)),eval_ordinary((2,1))
    ps={'P':P,'Q':Q,'PQ':times(P,Q),'yP':times(y,P),'yQ':times(y,Q)}
    rows={n:half(p) for n,p in ps.items()}
    ds={n:deltas(h) for n,h in rows.items()}
    assert all(min(d)>0 for d in ds.values())
    ep,eq,epq=(eta(rows[n]) for n in ('P','Q','PQ'))
    before=min(9*ep,eq)
    after=16*epq
    assert after<before
    # Build an explicit noncanonical triple without the new positive dynamics.
    X,Y,C=ONE,eval_ordinary((24,24,1)),eval_ordinary((49,97,51,2))
    t=minus(scale(times(y,X),3),x)
    T=minus(minus(times(t,Y),times(x,X)),C)
    u,e,Qseed=quot_y(minus(X,ONE)),quot_y(minus(Y,X)),quot_y(minus(Y,T))
    a=quot_y(minus(C,Y))
    I=minus(plus(times(X,X),times(Y,Y),times(C,C),
                 times(x,plus(times(X,Y),times(X,C),times(Y,C)))),scale(times(y,X,Y,C),3))
    R=quot_y(quot_y(I))
    U,V=mutation(X,C,Y),mutation(Y,C,X)
    S,D=minus(U,C),minus(V,U)
    hs,hd=half(S),half(D)
    f0=hs[0]*hd[1]-hs[1]*hd[0]
    assert f0<0 and R
    polys=dict(u=u,e=e,Q=Qseed,a=a,X=X,Y=Y,C=C,T=T,S=S,D=D,R=R)
    return {
        'degree_normalized_margin': {
            'ordinary':{n:ordinary(p) for n,p in ps.items()},'half_rows':rows,'defects':ds,
            'eta':{'P':str(ep),'Q':str(eq),'PQ':str(epq)},
            'before_min':str(before),'after':str(after),'after_over_before':str(after/before),
            'after_minus_before':str(after-before),
            'scope':'Counterexample to the proposed degree-squared minimum-margin rule, not to the existing product theorem or canonical Local TP2.'},
        'off_fricke': {
            'ordinary':{n:ordinary(p) for n,p in polys.items()},'H_S':hs,'H_D':hd,'F0':f0,
            'scope':'Noncanonical input; Fricke constraint fails and the seed is not folded-cone. Not a counterexample to any full prior extension criterion.'}
    }


def main():
    records=[]
    for depth in range(8):
        for word in product('sl',repeat=depth):
            records.append(record(''.join(word)))
    output={
        'status':'PASS','scope':'Formal identities are checked separately; bounded tree regression does not prove full-tree TP2.',
        'depth':7,'state_count':len(records),
        'checked_supported_minors':sum(r['minor_count'] for r in records),
        'records':records,'counterexamples':counterexamples()
    }
    Path('verifier_results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:output[k] for k in ('status','depth','state_count','checked_supported_minors')}))


if __name__=='__main__':
    main()
