#!/usr/bin/env python3
"""Independent bounded exact predicate probe. No earlier research imports."""
from __future__ import annotations
import argparse, hashlib, json
from collections import deque
from fractions import Fraction
from math import comb
from pathlib import Path

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def add(*args):
    r=[0]*max(map(len,args))
    for a in args:
        for i,v in enumerate(a): r[i]+=v
    return trim(r)
def scale(a,c): return trim([c*v for v in a])
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): r[i+j]+=u*v
    return trim(r)
def divy(a):
    if a==[0]: return [0]
    q=[0]*(len(a)-1)
    q[-1]=a[-1]
    for i in range(len(q)-2,-1,-1): q[i]=a[i+1]-q[i+1]
    assert a[0]==q[0]
    return trim(q)
y=[1,1]; y2=[1,2,1]; P1=[2,1]; z=[3,2]
def build(a,e,r):
    X=add([1],mul(y,a)); t=add(z,scale(mul(y2,a),3))
    k=mul(X,add([1],scale(mul(y,a),3)))
    g=add(mul(sub(t,[2]),e),k,r)
    s=sub(mul(t,g),r)
    d=mul(e,add(t,[1],scale(mul(y2,add(e,g)),3)))
    Y=add(X,mul(y,e)); C=add(Y,mul(y,g))
    return dict(a=a,e=e,r=r,g=g,s=s,d=d,X=X,Y=Y,C=C,t=t,k=k)
def children(v):
    a,e,r,g=(v[n] for n in ('a','e','r','g'))
    return [('s',build(a,add(e,g),g)),('l',build(add(a,e),g,add(e,g)))]
def scalar_children(X,Y,C):
    U=sub(sub(scale(mul(y,mul(X,C)),3),mul([0,1],add(X,C))),Y)
    V=sub(sub(scale(mul(y,mul(Y,C)),3),mul([0,1],add(Y,C))),X)
    assert len(U)<len(V)
    return [('s',(X,C,U)),('l',(Y,C,V))]
def H(a):
    h=[0]*len(a)
    for power,c in enumerate(a):
        for n in range(power%2,power+1,2):
            h[n]+=c*comb(power,(power-n)//2)
    return trim(h)
def get(h,n):
    n=abs(n)
    return h[n] if n<len(h) else 0
def defects(h):
    return [get(h,n)**2-get(h,n-1)*get(h,n+1)-get(h,n+1)**2+get(h,n)*get(h,n+2) for n in range(len(h))]
def minors(h,v):
    return [get(h,n)*get(v,n+1)-get(h,n+1)*get(v,n) for n in range(max(len(h),len(v)))]
def frac(f): return {'numerator':f.numerator,'denominator':f.denominator}
def relative(h,b):
    if min(h)<=0 or min(b)<0: return None
    ds=defects(h)
    lam=min(Fraction(d,c) for d,c in zip(ds,h))
    alpha=min(Fraction(get(h,n),c) for n,c in enumerate(b) if c)
    return {'lambda':frac(lam),'alpha':frac(alpha),'b0':b[0],
            'margin':frac(lam*alpha-8*b[0]),
            'lambda_index':next(i for i,(d,c) in enumerate(zip(ds,h)) if Fraction(d,c)==lam),
            'alpha_index':next(i for i,c in enumerate(b) if c and Fraction(get(h,i),c)==alpha),
            'pass':lam>0 and max(b)<=b[0] and lam*alpha>=8*b[0]}
def quadratic_min(c0,c1,c2,lo=-2,hi=2):
    pts=[Fraction(lo),Fraction(hi)]
    if c2>0:
        vertex=Fraction(-c1,2*c2)
        if lo<=vertex<=hi: pts.append(vertex)
    return min(((c0+c1*u+c2*u*u,u) for u in pts),key=lambda z:z[0])
def shifted_strength(p,lam):
    h=H(p); ds=defects(h); out=[]
    # h0 -> h0-u. Only delta0 and delta1 change.
    for n,(d,c) in enumerate(zip(ds,h)):
        c0=Fraction(d)-lam*c
        c1=(-2*h[0]-get(h,2)+lam) if n==0 else (get(h,2) if n==1 else 0)
        c2=1 if n==0 else 0
        val,u=quadratic_min(c0,c1,c2)
        out.append((val,u,n))
    return min(out,key=lambda z:z[0])

def main(depth=6):
    result={'scope':{'tree_depth':depth,'order':'breadth-first s before l','imports':'Python standard library only'},
            'first_failures':{},'state_counts':{},'relative_samples':{},'quantitative_minima':{},'canonical_crosschecks':0}
    first=result['first_failures']; stats={}; globalmin={}
    def check(key,vals,path,v,poly=None,details=None,strict=False):
        stats[key]=stats.get(key,0)+len(vals)
        indices=[n for n,q in enumerate(vals) if q<0 or (strict and q==0)]
        if indices and key not in first:
            n=indices[0]
            first[key]={'path':path,'index':n,'value':str(vals[n]),'a':v['a'],'e':v['e'],'r':v['r']}
            if poly is not None: first[key]['polynomial']=poly; first[key]['row']=H(poly)
            if details: first[key].update(details)
    q=deque([('',build([0],[1],[1]),([1],[2,1],[5,6,2]))])
    while q:
        path,v,scalar=q.popleft()
        X,Y,C=scalar
        assert all(v[n]==p for n,p in zip(('X','Y','C'),scalar))
        assert v['a']==divy(sub(X,[1])) and v['e']==divy(sub(Y,X)) and v['g']==divy(sub(C,Y))
        assert mul(v['r'],v['g'])==add(mul(sub(v['t'],[2]),mul(v['e'],v['e'])),scale(mul(v['k'],v['e']),2),scale(mul(v['a'],mul(X,X)),3))
        assert mul(v['g'],v['g'])==add(mul(v['r'],v['s']),mul(mul(X,X),add([1],scale(v['a'],3))))
        result['canonical_crosschecks']+=1
        for name in ('a','e','r','g','s','d'):
            for sm in (False,True):
                p=mul(y,v[name]) if sm else v[name]
                check(('y' if sm else '')+'fold_'+name,defects(H(p)),path,v,p)
        check('lr_e_r',minors(H(v['e']),H(v['r'])),path,v,details={'p':v['e'],'q':v['r'],'rows':[H(v['e']),H(v['r'])]})
        check('lr_r_e',minors(H(v['r']),H(v['e'])),path,v,details={'p':v['r'],'q':v['e'],'rows':[H(v['r']),H(v['e'])]})
        for hn,bn in [('g','e'),('s','r')]:
            for sm in (False,True):
                hp=mul(y,v[hn]) if sm else v[hn]; bp=mul(y,v[bn]) if sm else v[bn]
                rr=relative(H(hp),H(bp)); key=('y' if sm else '')+'relative_'+hn+'_'+bn
                stats[key]=stats.get(key,0)+1
                if not rr['pass'] and key not in first:
                    first[key]={'path':path,'h':hp,'b':bp,'rows':[H(hp),H(bp)],**rr}
                if len(path)<=1: result['relative_samples'][path+':'+key]=rr
        lc=C[-1]
        for sm,lam in [(False,Fraction(lc)),(True,Fraction(lc,2))]:
            p=mul(y,C) if sm else C; h=H(p)
            vals=[Fraction(d)-lam*c for d,c in zip(defects(h),h)]
            key='A_yC' if sm else 'A_C'; check(key,vals,path,v,p,details={'strength':frac(lam)})
            m=min(vals); ni=vals.index(m)
            if key not in globalmin or m<globalmin[key][0]: globalmin[key]=(m,path,ni)
        trace=sub(scale(mul(y,C),3),[0,1]); bm,u,ni=shifted_strength(trace,Fraction(3*lc,4))
        key='B_trace'; stats[key]=stats.get(key,0)+len(trace)
        if bm<0 and key not in first: first[key]={'path':path,'index':ni,'margin':frac(bm),'shift':frac(u),'trace_polynomial':trace,'strength':frac(Fraction(3*lc,4))}
        if key not in globalmin or bm<globalmin[key][0]:globalmin[key]=(bm,path,ni)
        if True:
            Z=add(v['a'],v['e'],v['g']); J=mul(y,sub(v['t'],[2])); M=add(scale(P1,2),scale(mul(y2,Z),3))
            b=add(mul(sub(v['t'],[2]),sub(v['e'],v['a'])),scale(v['k'],2),v['r'])
            S=mul(y,v['s']); yp=mul(y,b); ye=mul(y,v['e']); XP=mul(X,P1); JZ=mul(J,Z); XPM=mul(XP,M)
            assert add(JZ,yp)==S
            for key,p,w,strict in [('T1_yb_S',yp,S,False),('T2_XP1_ye',XP,ye,False),('T3_JZ_XP1M',JZ,XPM,True)]:
                vals=minors(H(p),H(w))
                if strict: vals=vals[:len(p)]
                check(key,vals,path,v,details={'p':p,'q':w,'rows':[H(p),H(w)]},strict=strict)
            check('T4_M_fold',defects(H(M)),path,v,M)
            check('T4_Z_fold',defects(H(Z)),path,v,Z)
            Q=sub(S,mul(y,v['g'])); XPm=mul(XP,M)
            check('T5_Q_XP1M',minors(H(Q),H(XPm))[:len(Q)],path,v,details={'p':Q,'q':XPm,'rows':[H(Q),H(XPm)]},strict=True)
            check('T6_yG_fold',defects(H(mul(y,v['g']))),path,v,mul(y,v['g']))
            check('T6_yR_yG',minors(H(mul(y,v['r'])),H(mul(y,v['g']))),path,v,details={'p':mul(y,v['r']),'q':mul(y,v['g'])})
        if len(path)<depth:
            for (label,nv),(clabel,ns) in zip(children(v),scalar_children(*scalar)):
                assert label==clabel
                q.append((path+label,nv,ns))
    result['state_counts']=stats
    result['quantitative_minima']={k:{'margin':frac(v[0]),'path':v[1],'index':v[2]} for k,v in globalmin.items()}
    result['statement']='Bounded exact evidence. No finite-to-infinite inference. First failures are minimal by stated breadth-first scope.'
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--depth',type=int,default=6); ap.add_argument('--output',type=Path)
    args=ap.parse_args(); result=main(args.depth)
    data=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(data)
    print(json.dumps({'nodes':result['canonical_crosschecks'],'first_failures':{k:{z:v[z] for z in ('path','index','value','margin','shift') if z in v} for k,v in result['first_failures'].items()},'quantitative_minima':result['quantitative_minima']},indent=2))
