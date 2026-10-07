#!/usr/bin/env python3
"""Exact Robin/proxy algebra replay; analytical theorem is proxy_robin.md."""
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(*aa):
    a=[0]*max(map(len,aa))
    for b in aa:
        for i,v in enumerate(b):a[i]+=v
    return trim(a)
def neg(a):return [-v for v in a]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return trim([c*v for v in a])
def mul(*aa):
    a=[1]
    for b in aa:
        z=[0]*(len(a)+len(b)-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):z[i+j]+=u*v
        a=trim(z)
    return a
def get(a,n):return a[abs(n)] if abs(n)<len(a) else 0
def H(a):
    row=[0]*len(a)
    for k,c in enumerate(a):
        for j in range(k+1):
            n=k-2*j
            if n>=0:row[n]+=c*comb(k,j)
    return trim(row)
def delta(a,n):
    f=lambda k:get(a,k)
    return f(n)**2-f(n-1)*f(n+1)-f(n+1)**2+f(n)*f(n+2)
def W(a,b,n):return get(a,n)*get(b,n+1)-get(a,n+1)*get(b,n)

x,y,p,z=[0,1],[1,1],[2,1],[3,2]
one,two=[1],[2]

def state(a,e,r):
    X=add(one,mul(y,a));t=sub(scale(mul(y,X),3),x)
    k=mul(X,sub(scale(X,3),two))
    g=add(mul(sub(t,two),e),k,r);s=sub(mul(t,g),r)
    Y=add(X,mul(y,e));C=add(Y,mul(y,g));M=add(sub(scale(mul(y,C),3),x),one)
    Q=sub(mul(sub(t,two),C),mul(x,X));Pi=mul(X,p,M)
    V=add(mul(p,X),mul(p,p,C))
    return dict(a=a,e=e,r=r,X=X,Y=Y,C=C,t=t,k=k,g=g,s=s,M=M,Q=Q,Pi=Pi,V=V)

def child(st,long=False):
    if long:return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g']))
    return state(st['a'],add(st['e'],st['g']),st['g'])

def run():
    # Universal polynomial identities: independent x,X,C are represented
    # by multivariate monomials; no Fricke assumption is needed here.
    def mvar(i):return {tuple(int(j==i) for j in range(3)):1}
    def madd(*aa):
        d={}
        for a in aa:
            for k,v in a.items():d[k]=d.get(k,0)+v
        return {k:v for k,v in d.items() if v}
    def ms(a,c):return {k:v*c for k,v in a.items() if v*c}
    def mm(*aa):
        a={(0,0,0):1}
        for b in aa:
            d={}
            for k,u in a.items():
                for l,v in b.items():
                    q=tuple(k[i]+l[i] for i in range(3));d[q]=d.get(q,0)+u*v
            a={k:v for k,v in d.items() if v}
        return a
    mx,mX,mC=[mvar(i) for i in range(3)];mo={(0,0,0):1}
    my,mp=madd(mx,mo),madd(mx,ms(mo,2))
    mt=madd(ms(mm(my,mX),3),ms(mx,-1));mA=madd(mt,ms(mo,-2))
    mM=madd(ms(mm(my,mC),3),ms(mx,-1),mo)
    mQ=madd(mm(mA,mC),ms(mm(mx,mX),-1));mPi=mm(mX,mp,mM)
    mV=madd(mm(mp,mX),mm(mp,mp,mC))
    e1=madd(mPi,ms(mm(mp,mQ),-1),ms(mV,-1))
    e2=madd(mm(mA,mPi),ms(mm(my,mX,mp,mQ),-3),
            ms(mm(mX,mp,madd(mA,mm(mp,mx))),-1))
    e3=madd(mA,mm(mp,mx),ms(madd(ms(mm(my,mX),3),mm(mp,madd(mx,ms(mo,-1)))),-1))
    assert not e1 and not e2 and not e3

    # Monic continuants in an independent trace variable.
    trace=[0,1];U=[[1],trace]
    for n in range(2,9):U.append(sub(mul(trace,U[-1]),U[-2]))
    robin=[[1]]+[sub(U[n],U[n-1]) for n in range(1,9)]
    assert robin[1]==[-1,1]
    for n in range(2,9):assert robin[n]==sub(mul(trace,robin[n-1]),robin[n-2])
    b0,b1=[3,2],[5,1]
    fs=[add(mul(b0,U[n]),mul(b1,U[n-1]) if n else [0]) for n in range(9)]
    for n in range(1,9):assert sub(fs[n],fs[n-1])==add(mul(b0,robin[n]),mul(b1,robin[n-1]))

    root=state([0],[1],[1]);short=child(root);long=child(root,True)
    ll=child(long,True)
    states=[root,short,long,ll]
    records=[]
    for name,st in zip(['root','short','long','long,long'],states):
        X,C,t,Q,Pi,V=[st[k] for k in ['X','C','t','Q','Pi','V']]
        assert Q==mul(y,sub(st['s'],st['g']))
        assert Pi==add(mul(p,Q),V)
        assert mul(sub(t,two),Pi)==add(scale(mul(y,X,p,Q),3),mul(X,p,add(sub(t,two),mul(p,x))))
        qr,pr,vr=H(Q),H(Pi),H(V)
        proxy=[W(qr,pr,n) for n in range(len(qr))]
        defects=[delta(qr,n) for n in range(len(qr))]
        correction=[W(qr,vr,n) for n in range(len(qr))]
        assert proxy==[a+b for a,b in zip(defects,correction)]
        dX,dC,dQ,dPi,dV=[len(a)-1 for a in [X,C,Q,Pi,V]]
        assert (dQ,dPi,dV)==(dX+dC+1,dX+dC+2,dC+2)
        assert all(correction[n]==0 for n in range(dV+1,dQ+1))
        terminal=6*C[-1]**2 if dX==0 else (3*X[-1]*C[-1])**2
        assert proxy[-1]==terminal
        records.append(dict(state=name,degrees=dict(X=dX,C=dC,Q=dQ,Pi=dPi,V=dV),
                            Q_halfrow=qr,V_halfrow=vr,deltaQ=defects,
                            correction=correction,proxy=proxy,terminal=terminal))
    assert records[-1]['correction'][9]==-7776
    assert all(v>0 for v in records[-1]['proxy'])

    # Exact adjacent trace-block formulas at actual endpoint traces.
    blocks=[]
    for X in [[1],p,root['C']]:
        A=sub(scale(mul(y,X),3),p);L=scale(mul(y,X,p),3)
        ah,lh=H(A),H(L)
        ws=[W(ah,lh,n) for n in range(len(ah))]
        formulas=[]
        for n in range(len(ah)):
            v=delta(ah,n)
            if n==0:v+=4*get(ah,0)-6*get(ah,1)
            elif n==1:v+=get(ah,1)-4*get(ah,2)
            elif n==2:v-=get(ah,3)
            formulas.append(v)
        assert ws==formulas
        if len(ah)>1:assert delta(H(add(A,[4])),1)==delta(ah,1)-4*get(ah,2)
        blocks.append(dict(X=X,A_halfrow=ah,adjacent_trace_block=ws))
    assert blocks[1]['adjacent_trace_block'][0]==-6
    return dict(status='exact identities and finite sanity checks PASS',
                analytical_theorem='strict K_Q from retained MP2_exact origin (older MP_2 suffices); see proxy_robin.md',
                universal_symbolic_checks=['Pi=P Q+V','A Pi=3yXP Q+XP(A+Px)','A+Px=3yX+P(x-1)'],
                robin_continuant_checks=list(range(1,9)),actual_state_support_checks=records,
                trace_source_checks=blocks,
                scope={'strict_K_Q_BOTH':'PROVED conditional on certified registers and audited boundary theorem',
                       'proxy_outside_overlap_and_terminal':'PROVED conditional consequence',
                       'proxy_overlap':'OPEN','strict_proxy_BOTH':'OPEN','full_tree_Local_TP2':'OPEN'})

if __name__=='__main__':
    data=run()
    HERE.joinpath('proxy_robin_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
