#!/usr/bin/env python3
"""Exact direct-proxy identity checks and targeted source replay."""
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(*aa):
    a=[0]*max(map(len,aa))
    for b in aa:
        for i,v in enumerate(b):a[i]+=v
    return trim(a)

def scale(a,c):return trim([c*v for v in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(*aa):
    a=[1]
    for b in aa:
        z=[0]*(len(a)+len(b)-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):z[i+j]+=u*v
        a=trim(z)
    return a

def H(a):
    h=[0]*len(a)
    for k,c in enumerate(a):
        for n in range(k%2,k+1,2):h[n]+=c*comb(k,(k-n)//2)
    return trim(h)

def at(a,n):return a[abs(n)] if abs(n)<len(a) else 0

def delta(a,n):return at(a,n)**2-at(a,n-1)*at(a,n+1)-at(a,n+1)**2+at(a,n)*at(a,n+2)
def W(a,b,n):return at(a,n)*at(b,n+1)-at(a,n+1)*at(b,n)

one=[1];x=[0,1];y=[1,1];P=[2,1]

def state(a,e,r):
    X=add(one,mul(y,a));Y=add(X,mul(y,e));t=sub(scale(mul(y,X),3),x)
    A=sub(t,[2]);k=mul(X,sub(scale(X,3),[2]));g=add(mul(A,e),k,r);s=sub(mul(t,g),r)
    C=add(Y,mul(y,g));T=sub(scale(mul(y,C),3),x);M=add(T,one)
    E,G,R,S=[mul(y,f) for f in [e,g,r,s]];Q=sub(S,G);D=mul(E,M)
    return dict(a=a,e=e,r=r,X=X,Y=Y,t=t,A=A,k=k,g=g,s=s,C=C,T=T,M=M,E=E,G=G,R=R,S=S,Q=Q,D=D)

def child(st,long=False):
    if long:return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g']))
    return state(st['a'],add(st['e'],st['g']),st['g'])

class Ring:
    def __init__(self,n):self.n=n;self.one={(0,)*n:1}
    def v(self,i):return {tuple(int(j==i) for j in range(self.n)):1}
    def add(self,*aa):
        d={}
        for a in aa:
            for k,v in a.items():d[k]=d.get(k,0)+v
        return {k:v for k,v in d.items() if v}
    def scale(self,a,c):return {k:c*v for k,v in a.items() if c*v}
    def sub(self,a,b):return self.add(a,self.scale(b,-1))
    def mul(self,*aa):
        a=self.one
        for b in aa:
            d={}
            for k,u in a.items():
                for l,v in b.items():
                    q=tuple(k[i]+l[i] for i in range(self.n));d[q]=d.get(q,0)+u*v
            a={k:v for k,v in d.items() if v}
        return a


def formal_checks():
    R=Ring(4);ma,ms,mm=R.add,R.scale,R.mul;mo=R.one
    mx,a,e,r=[R.v(i) for i in range(4)];my=ma(mx,mo);p=ma(mx,ms(mo,2))
    X=ma(mo,mm(my,a));Y=ma(X,mm(my,e));t=ma(ms(mm(my,X),3),ms(mx,-1));A=ma(t,ms(mo,-2));h=ma(A,mo)
    k=mm(X,ma(ms(X,3),ms(mo,-2)));g=ma(mm(A,e),k,r);s=ma(mm(t,g),ms(r,-1))
    C=ma(Y,mm(my,g));T=ma(ms(mm(my,C),3),ms(mx,-1));M=ma(T,mo)
    E,G,rr,S=[mm(my,f) for f in [e,g,r,s]];Q=ma(S,ms(G,-1));D=mm(E,M)
    B=ma(T,ms(t,-1));hh=ma(G,ms(mm(A,E),-1));K=ma(mm(M,hh),mm(B,S))
    Qs=ma(mm(h,Q),mm(A,G));Ds=ma(mm(h,D),K)
    # Direct short child from retained t and new C+S.
    Cs=ma(C,S);Ts=ma(ms(mm(my,Cs),3),ms(mx,-1));Ms=ma(Ts,mo)
    directQs=ma(mm(A,Cs),ms(mm(mx,X),-1));directDs=mm(ma(E,G),Ms)
    assert Qs==directQs and Ds==directDs
    K0=mm(my,k)
    assert hh==ma(K0,rr)
    assert K==ma(mm(ma(t,mo),hh),mm(B,ma(mm(t,G),K0)))
    E1=ma(E,G);E2=ma(E1,S)
    assert E2==ma(mm(t,E1),ms(E,-1),K0)
    assert Q==ma(mm(A,E1),K0)
    Qprev=ma(mm(A,E),K0);F0=ma(mm(ma(t,mo),A),ms(mm(my,K0),-3))
    assert F0==ma(ms(mm(my,X),3),mm(mx,mx),mx,ms(mo,-2))
    assert mm(A,A,D)==mm(ma(Qprev,ms(K0,-1)),ma(ms(mm(my,Q),3),F0))
    tau=ma(ms(mm(my,Y),3),ms(mx,-1));Al=ma(tau,ms(mo,-2));hl=ma(Al,mo);F=ma(S,D)
    Kl=ma(mm(M,ma(G,ms(mm(hl,E),-1))),ms(mm(my,G,F),3))
    Ql=ma(mm(hl,ma(Q,D)),mm(Al,G),ms(E,-1));Dl=ma(mm(hl,D),Kl)
    Cl=ma(C,F);Ml=ma(ms(mm(my,Cl),3),ms(mx,-1),mo)
    assert Ql==ma(mm(Al,Cl),ms(mm(mx,Y),-1));assert Dl==mm(G,Ml)

    # Universal two-variable numerator identity (5), arbitrary A,G,R.
    R=Ring(6);ma,ms,mm=R.add,R.scale,R.mul;mo=R.one
    ai,aj,gi,gj,ri,rj=[R.v(i) for i in range(6)];hi,hj=ma(ai,mo),ma(aj,mo)
    qi,qj=ma(mm(hi,gi),ms(ri,-1)),ma(mm(hj,gj),ms(rj,-1))
    lhs=ma(mm(ai,gi,hj,qj),ms(mm(hi,qi,aj,gj),-1))
    rhs=ma(mm(gi,gj,ma(mm(ai,aj),ms(mo,-1)),ma(aj,ms(ai,-1))),
           mm(ai,aj,ma(mm(ri,gj),ms(mm(gi,rj),-1))),
           ma(mm(ri,aj,gj),ms(mm(ai,gi,rj),-1)))
    assert lhs==rhs
    return dict(canonical_ring_variables=['x','a','e','r'],canonical_identity_residuals=0,Fricke_used_for_identities=False,two_variable_lowerblock_ring=['A_i','A_j','G_i','G_j','R_i','R_j'],lowerblock_numerator_residual=0)


def relative_summary(*pairs):
    # Sum R(f,g) coefficient selectors: all k<l give the full finite
    # character array modulo its symmetric duplicates.
    rows=[(H(f),H(g)) for f,g in pairs];size=max(max(len(a),len(b)) for a,b in rows)
    vals=[];neg=[]
    for k in range(size):
        for l in range(k+1,size):
            v=sum(at(a,k)*at(b,l)-at(a,l)*at(b,k) for a,b in rows)
            vals.append(v)
            if v<0:neg.append(dict(columns=[k,l],characters=[k+l-1,l-k-1],value=v))
    nonzero=[v for v in vals if v]
    return dict(negative=neg,min_nonzero=min(nonzero) if nonzero else None,nonzero_coefficients=len(nonzero),checked_selectors=len(vals))


def run():
    formal=formal_checks();root=state([0],[1],[1]);records=[]
    for name,st in [('root',root),('first_short',child(root)),('first_long',child(root,True))]:
        A=st['A'];h=add(A,one);B=sub(st['T'],st['t']);hh=sub(st['G'],mul(A,st['E']));K=add(mul(st['M'],hh),mul(B,st['S']))
        sh=child(st);lo=child(st,True)
        assert sh['Q']==add(mul(h,st['Q']),mul(A,st['G']))
        assert sh['D']==add(mul(h,st['D']),K)
        tau=sub(scale(mul(y,st['Y']),3),x);Al=sub(tau,[2]);hl=add(Al,one);F=add(st['S'],st['D']);Kl=add(mul(st['M'],sub(st['G'],mul(hl,st['E']))),scale(mul(y,st['G'],F),3))
        assert lo['Q']==sub(add(mul(hl,add(st['Q'],st['D'])),mul(Al,st['G'])),st['E'])
        assert lo['D']==add(mul(hl,st['D']),Kl)
        # Canonical Fricke and the equivalent fixed-endpoint conic.
        fricke=sub(mul(st['r'],st['g']),add(mul(A,st['e'],st['e']),scale(mul(st['k'],st['e']),2),scale(mul(st['a'],st['X'],st['X']),3)))
        assert fricke==[0]
        e1=add(st['E'],st['G']);K0=mul(y,st['k']);L0=scale(mul(y,st['X'],st['X'],sub(st['X'],one)),3)
        conic=sub(add(mul(e1,e1),mul(st['E'],st['E'])),add(mul(st['t'],st['E'],e1),mul(K0,add(st['E'],e1)),L0));assert conic==[0]
        summary=dict(state=name,central_flag_delta_A=delta(H(A),0),parent_Q_D_adjacent=[W(H(st['Q']),H(st['D']),n) for n in range(len(st['Q']))],lowerblock=relative_summary((mul(A,st['G']),mul(h,st['Q']))),D_advance=relative_summary((mul(h,st['D']),sh['D'])),residual_pair=relative_summary((mul(A,st['G']),K)),mixed_pair=relative_summary((mul(h,st['Q']),K),(mul(A,st['G']),mul(h,st['D']))))
        if name=='root':assert summary['lowerblock']['negative']==[dict(columns=[0,1],characters=[0,0],value=-6)]
        else:assert not summary['lowerblock']['negative']
        assert not summary['D_advance']['negative'];assert not summary['residual_pair']['negative'];assert not summary['mixed_pair']['negative']
        records.append(summary)
    assert records[2]['central_flag_delta_A']==2
    return dict(status='PASS exact universal identities and targeted finite source replays',formal_checks=formal,targeted_sources=records,scope={'ordinary_SHORT_lowerblock':'PROVED conditional on weak trace/cone/LR premises plus proved retained central history flag','common_SHORT_parent_comparison':'PROVED strict','SHORT_from_D_advance':'PROVED conditional implication','D_advance_arbitrary_origin':'OPEN','LONG_residual':'OPEN','BOTH_Q_D':'OPEN','full_tree_Local_TP2':'OPEN'})

if __name__=='__main__':
    data=run();HERE.joinpath('proxy_algebra_results.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
