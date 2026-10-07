#!/usr/bin/env python3
"""Exact curvature transport identities and root/first-child character seeds."""
from pathlib import Path
from collections import defaultdict
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from tp2_source import add, sub, mul, scale, H, generate_tree
from recovery_fulltree_bivariate_character import predicted_characters as R


def plus(*ps):
    out=defaultdict(int)
    for p in ps:
        for key,value in p.items():out[key]+=value
    return {k:v for k,v in out.items() if v}

def bscale(p,n):return {k:n*v for k,v in p.items() if n*v}
def minus(p,q):return plus(p,bscale(q,-1))

def cprod(p,q):
    out=defaultdict(int)
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            for a in range(abs(i-k),i+k+1,2):
                for b in range(abs(j-l),j+l+1,2):out[a,b]+=v*w
    return {k:v for k,v in out.items() if v}

def dd(p):return R([1],p)
def kap(r,g,s):return minus(cprod(dd(g),dd(g)),cprod(dd(r),dd(s)))

def spadd(*ps):return plus(*ps)
def spmul(*ps):
    size=len(next(iter(ps[0]),(0,)*6))
    out={(0,)*size:1}
    for p in ps:
        tmp=defaultdict(int)
        for k,v in out.items():
            for l,w in p.items():tmp[tuple(a+b for a,b in zip(k,l))]+=v*w
        out={k:v for k,v in tmp.items() if v}
    return out
def spvar(i,size=6):
    k=[0]*size;k[i]=1
    return {tuple(k):1}
def spconst(n,size=6):return {(0,)*size:n} if n else {}


def symbolic_checks():
    rs,rz,gs,gz,ts,tz=map(spvar,range(6))
    ss,sz=minus(spmul(ts,gs),rs),minus(spmul(tz,gz),rz)
    us,uz=minus(spmul(ts,ss),gs),minus(spmul(tz,sz),gz)
    dr,dg,ds,du,dt=map(lambda q:minus(q[1],q[0]),[(rs,rz),(gs,gz),(ss,sz),(us,uz),(ts,tz)])
    raw_new=minus(spmul(ds,ds),spmul(dg,du))
    raw_old=minus(spmul(dg,dg),spmul(dr,ds))
    forcing=spmul(dt,minus(spmul(gs,sz),spmul(ss,gz)))
    checks={'fixed_trace_curvature':minus(minus(raw_new,raw_old),forcing)}
    aa,az,es,ez,ts,tz=map(spvar,range(6))
    bs,bz=spadd(aa,spmul(ts,es)),spadd(az,spmul(tz,ez))
    qa,qaz=spadd(spmul(ts,aa),es),spadd(spmul(tz,az),ez)
    qb,qbz=minus(spmul(ts,bs),es),minus(spmul(tz,bz),ez)
    da,db,de,dt=map(lambda q:minus(q[1],q[0]),[(aa,az),(bs,bz),(es,ez),(ts,tz)])
    ka=spadd(spmul(da,da),spmul(de,minus(qaz,qa)))
    kb=minus(spmul(db,db),spmul(de,minus(qbz,qb)))
    forcing=spmul(dt,spadd(minus(spmul(es,az),spmul(aa,ez)),
                             minus(spmul(es,bz),spmul(bs,ez))))
    checks['sibling_curvature']=minus(minus(kb,ka),forcing)
    xx,X,Y,C=[spvar(i,4) for i in range(4)]
    one,two=spconst(1,4),spconst(2,4)
    yy,pp=spadd(xx,one),spadd(xx,two)
    I=minus(spadd(spmul(X,X),spmul(Y,Y),spmul(C,C),
                        spmul(xx,spadd(spmul(X,Y),spmul(X,C),spmul(Y,C)))),
            bscale(spmul(yy,X,Y,C),3))
    q=minus(spmul(minus(minus(bscale(spmul(yy,X),3),xx),two),C),spmul(xx,X))
    GG=minus(C,Y)
    checks['Fricke_proxy_exchange']=spadd(minus(spmul(Y,q),
                          spadd(spmul(GG,GG),spmul(X,X),spmul(xx,X,C))),I)
    assert all(not v for v in checks.values())
    return list(checks)


def state(rec):
    X,Y=sorted([rec['A'],rec['B']],key=len)
    C=rec['C'];E=sub(Y,X);G=sub(C,Y)
    t=sub(scale(mul([1,1],X),3),[0,1]);tl=sub(scale(mul([1,1],Y),3),[0,1])
    T=sub(scale(mul([1,1],C),3),[0,1])
    S,D=rec['S'],rec['D'];F=add(S,D);RR=sub(mul(t,G),S)
    A,B=add(add(E,G),S),add(G,F)
    assert B==add(A,mul(T,E))
    assert F==sub(mul(tl,add(G,E)),sub(RR,E))
    return dict(X=X,Y=Y,C=C,E=E,G=G,R=RR,S=S,D=D,F=F,t=t,tl=tl,T=T,A=A,B=B,
                kX=kap(RR,G,S),kY=kap(sub(RR,E),add(G,E),F))


def encode(poly):return [[i,j,v] for (i,j),v in sorted(poly.items())]


def run():
    names=symbolic_checks()
    records=generate_tree(1)
    states={rec['path']:state(rec) for rec in records}
    root,s,l=states[''],states['L'],states['R']
    assert s['kX']==plus(root['kX'],cprod(dd(root['t']),R(root['G'],root['S'])))
    assert l['kX']==plus(root['kY'],cprod(dd(root['tl']),R(add(root['G'],root['E']),root['F'])))
    A,B,E,T=(root[k] for k in ('A','B','E','T'))
    ka=plus(cprod(dd(A),dd(A)),cprod(dd(E),dd(add(mul(T,A),E))))
    kb=minus(cprod(dd(B),dd(B)),cprod(dd(E),dd(sub(mul(T,B),E))))
    assert s['kY']==ka and l['kY']==kb
    assert minus(kb,ka)==cprod(dd(T),plus(R(E,A),R(E,B)))
    seed={}
    for label,st in [('root',root),('first-short',s),('first-long',l)]:
        seed[label]={}
        for key in ('kX','kY'):
            poly=st[key]
            if label!='root':assert all(v>=0 for v in poly.values())
            seed[label][key]=dict(negative_terms=encode({k:v for k,v in poly.items() if v<0}),
                                 central_coefficient=poly.get((0,0),0),
                                 characters=encode(poly))
    assert root['kX']=={(0,0):-3,(1,1):4,(2,0):4,(0,2):4}
    root_LR={key:encode(R(a,b)) for key,a,b in
             [('G_S',root['G'],root['S']),('H_F',add(root['G'],root['E']),root['F'])]}
    assert all(v>=0 for rows in root_LR.values() for i,j,v in rows)
    return dict(status='universal identities and exact first-level seeds passed',
                symbolic_checks=names,seeds=seed,root_edge_LR=root_LR,
                conditional_BOTH_child_curvature_closure='PROVED assuming parent P_Q and nonnegative parent curvature pair',
                proxy_or_child_cone_consequence='OPEN',full_tree_Local_TP2='OPEN')


if __name__=='__main__':
    result=run()
    HERE.joinpath('proxy_curvature_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('seeds','root_edge_LR')},indent=2))
    print(json.dumps({key:{name:value['central_coefficient'] for name,value in val.items()}
                      for key,val in result['seeds'].items()},indent=2))
