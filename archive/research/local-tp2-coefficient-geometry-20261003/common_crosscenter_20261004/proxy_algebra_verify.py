#!/usr/bin/env python3
"""Independent exact anchor/proxy identity replay, not a sign scan."""
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a

def add(*aa):
    a=[0]*max(map(len,aa))
    for b in aa:
        for i,v in enumerate(b):a[i]+=v
    return trim(a)

def scale(a,c):return trim([v*c for v in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(*aa):
    a=[1]
    for b in aa:
        z=[0]*(len(a)+len(b)-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):z[i+j]+=u*v
        a=trim(z)
    return a

def deg(a):return -1 if a==[0] else len(a)-1

def H(a):
    h=[0]*len(a)
    for k,c in enumerate(a):
        for n in range(k%2,k+1,2):h[n]+=c*comb(k,(k-n)//2)
    return trim(h)

def at(a,n):return a[abs(n)] if abs(n)<len(a) else 0

def delta(h,n):
    return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)

def W(a,b,n):return at(a,n)*at(b,n+1)-at(a,n+1)*at(b,n)

one=[1];x=[0,1];y=[1,1];P=[2,1];z=[3,2];beta=scale(mul(y,y),3)

def state(a,e,r):
    X=add(one,mul(y,a));Y=add(X,mul(y,e));t=sub(scale(mul(y,X),3),x)
    k=mul(X,sub(scale(X,3),[2]));g=add(mul(sub(t,[2]),e),k,r);s=sub(mul(t,g),r)
    B=add(a,e,g);C=add(one,mul(y,B));T=sub(scale(mul(y,C),3),x);M=add(T,one)
    d=mul(e,M);c=add(e,g,s);Q=sub(mul(sub(t,[2]),C),mul(x,X));Pi=mul(X,P,M)
    return dict(a=a,e=e,r=r,X=X,Y=Y,t=t,k=k,g=g,s=s,B=B,C=C,T=T,M=M,d=d,c=c,Q=Q,Pi=Pi)

def child(st,long=False):
    if long:return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g']))
    return state(st['a'],add(st['e'],st['g']),st['g'])

def U_R(t,n):
    u=[[1]]
    for j in range(1,n+1):u.append(sub(mul(t,u[-1]),u[-2] if j>=2 else [0]))
    r=[];s=[0]
    for v in u:s=add(s,v);r.append(s)
    return u,r

def origin(endpoint_ax,b0,b1,anchor,N):
    endpoint=add(one,mul(y,endpoint_ax));trace=sub(scale(mul(y,endpoint),3),x)
    return dict(ax=endpoint_ax,endpoint=endpoint,t=trace,b0=b0,b1=b1,anchor=anchor,N=N)

def eval_origin(o):
    N=o['N'];u,r=U_R(o['t'],N)
    f=lambda n:add(mul(o['b0'],u[n]),mul(o['b1'],u[n-1]) if n>=1 else [0])
    Z=add(mul(o['b0'],r[N-1]),mul(o['b1'],r[N-2]) if N>=2 else [0])
    return dict(prev=f(N-1),out=f(N),Z=Z,B=add(o['anchor'],Z))

def transport(st,regs,long=False):
    keep=dict(regs[int(long)]);keep['N']+=1
    if long:new=origin(st['B'],st['e'],st['c'],st['a'],2)
    else:new=origin(st['B'],st['c'],st['e'],st['a'],1)
    return [keep,new]

# Formal four-variable ring x,a,e,r: identity c+e-k0_C=(T-2)a.
def ring_anchor_check():
    zero=(0,0,0,0);mo={zero:1}
    def mv(i):return {tuple(int(j==i) for j in range(4)):1}
    def ma(*aa):
        d={}
        for a in aa:
            for k,v in a.items():d[k]=d.get(k,0)+v
        return {k:v for k,v in d.items() if v}
    def ms(a,c):return {k:c*v for k,v in a.items() if c*v}
    def mm(*aa):
        a=mo
        for b in aa:
            d={}
            for k,u in a.items():
                for l,v in b.items():
                    q=tuple(k[i]+l[i] for i in range(4));d[q]=d.get(q,0)+u*v
            a={k:v for k,v in d.items() if v}
        return a
    mx,a,e,r=[mv(i) for i in range(4)];my=ma(mx,mo);mz=ma(ms(mx,2),ms(mo,3))
    X=ma(mo,mm(my,a));t=ma(ms(mm(my,X),3),ms(mx,-1));A=ma(t,ms(mo,-2))
    k=mm(X,ma(ms(X,3),ms(mo,-2)));g=ma(mm(A,e),k,r);s=ma(mm(t,g),ms(r,-1))
    B=ma(a,e,g);T=ma(mz,ms(mm(my,my,B),3));c=ma(e,g,s);k0=ma(mo,mm(mz,B))
    residual=ma(c,e,ms(k0,-1),ms(mm(ma(T,ms(mo,-2)),a),-1))
    assert not residual
    return dict(variables=['x','a','e','r'],residual_terms=0,Fricke_used=False)

def run():
    formal=ring_anchor_check()
    trace=[0,1];u,r=U_R(trace,10)
    for N in range(1,10):
        assert sub(sub(u[N],u[N-1]),one)==mul(sub(trace,[2]),r[N-1])
        if N>=2:assert sub(sub(u[N-1],u[N-2]),one)==mul(sub(trace,[2]),r[N-2])
    for h in range(5):
        assert r[2*h]==mul(u[h],add(u[h],u[h-1] if h else [0]))
        assert r[2*h+1]==mul(u[h],add(u[h+1],u[h]))

    root=state([0],[1],[1]);rootregs=[origin([0],[1],[0],[0],2),origin([1],scale(P,2),[0],[0],1)]
    records=[]
    tests=[('root',root,rootregs)]
    for long in [False,True]:tests.append(('long' if long else 'short',child(root,long),transport(root,rootregs,long)))
    for name,st,regs in tests:
        expected=[(st['g'],st['s']),(add(st['e'],st['g']),add(st['s'],st['d']))]
        rr=[]
        for o,(prev,out) in zip(regs,expected):
            eo=eval_origin(o);assert eo['prev']==prev and eo['out']==out and eo['B']==st['B']
            A=sub(o['t'],[2]);k0=add(one,mul(z,o['ax']))
            assert add(o['b0'],o['b1'])==add(k0,mul(A,o['anchor']))
            assert mul(y,sub(out,prev))==sub(mul(A,st['C']),mul(x,o['endpoint']))
            # Retention recurrence including its fixed initial anchor.
            advanced=dict(o);advanced['N']+=1;assert sub(eval_origin(advanced)['B'],eo['B'])==out
            rr.append(dict(index=o['N'],endpoint_degree=deg(o['endpoint']),anchor=o['anchor'],center_degree=deg(eo['B'])))
        assert sub(add(st['c'],st['e']),add(one,mul(z,st['B'])))==mul(sub(st['T'],[2]),st['a'])
        records.append(dict(state=name,origins=rr))

    # Use root-long's newly initialized C origin and a nonzero fixed anchor.
    # This is an identity replay at formal future indices, not a tree scan.
    parent=tests[2][1]
    o=origin(parent['B'],parent['c'],parent['e'],parent['a'],2)
    band_records=[]
    for N in [2,3]:
        o['N']=N;eo=eval_origin(o);X=o['endpoint'];A=sub(o['t'],[2])
        J=mul(y,A);L=scale(mul(y,y,X,P),3);b=mul(y,add(one,mul(z,o['ax'])));K=scale(mul(X,P,P),2)
        q0=add(mul(J,o['anchor']),b);p0=add(mul(L,o['anchor']),K)
        Q=add(mul(J,eo['Z']),q0);Pi=add(mul(L,eo['Z']),p0)
        C=add(one,mul(y,eo['B']))
        assert Q==sub(mul(A,C),mul(x,X));assert Pi==mul(X,P,add(sub(scale(mul(y,C),3),x),one))
        band=max(deg(q0),deg(p0));qh,ph=H(Q),H(Pi);baseq,basep=H(mul(J,eo['Z'])),H(mul(L,eo['Z']))
        assert all(W(qh,ph,n)==W(baseq,basep,n) for n in range(band+1,len(qh)))
        anchor_degree=deg(o['anchor']);B=H(eo['B']);Z=H(eo['Z']);yB=H(mul(y,eo['B']));yZ=H(mul(y,eo['Z']))
        assert all(delta(B,n)==delta(Z,n) for n in range(anchor_degree+2,len(B)))
        assert all(delta(yB,n)==delta(yZ,n) for n in range(anchor_degree+3,len(yB)))
        h=1 if o['anchor']==[0] else anchor_degree+2
        tracebase=mul(beta,eo['Z']);actualtrace=add(z,mul(beta,eo['B']))
        for shift in [-2,0,2]:
            shifted=sub(actualtrace,[shift]);row,baserow=H(shifted),H(tracebase)
            assert all(delta(row,n)==delta(baserow,n) for n in range(h+2,len(row)))
            yrow,ybase=H(mul(y,shifted)),H(mul(y,tracebase))
            assert all(delta(yrow,n)==delta(ybase,n) for n in range(h+3,len(yrow)))
        band_records.append(dict(N=N,fixed_proxy_band=band,Q_degree=deg(Q),raw_anchor_defect_band=anchor_degree+1,y_anchor_defect_band=anchor_degree+2,raw_shifted_trace_strict_from=h+2,y_shifted_trace_strict_from=h+3))
    assert band_records[0]['fixed_proxy_band']==band_records[1]['fixed_proxy_band']

    sources=[]
    rho=H(mul(y,P,P));assert rho==[14,11,5,1]
    for X in [[1],P]:
        J=mul(y,sub(scale(mul(y,X),3),P));L=scale(mul(y,y,X,P),3);j,l=H(J),H(L)
        ws=[W(j,l,n) for n in range(len(j))]
        assert ws==[delta(j,n)+W(j,rho,n) for n in range(len(j))]
        for n in range(len(j)):
            corr=[11*at(j,0)-14*at(j,1),5*at(j,1)-11*at(j,2),at(j,2)-5*at(j,3),-at(j,4)]
            assert ws[n]==delta(j,n)+(corr[n] if n<4 else 0)
        sources.append(dict(endpoint=X,J_halfrow=j,L_halfrow=l,source_adjacent=ws))
    boundary_base=H(mul(beta,scale(P,2)))
    boundary_defects=[delta(boundary_base,n) for n in range(len(boundary_base))]
    assert boundary_base==[60,48,24,6]
    assert boundary_defects==[432,576,252,36]
    assert sources[0]['source_adjacent']==[30,-12,6]
    assert sources[1]['source_adjacent']==[72,81,45,9]
    return dict(status='PASS exact identities and targeted support/source checks',formal_anchor_cancellation=formal,prefix_identity_indices=list(range(1,10)),prefix_factorizations_h=list(range(5)),BOTH_origin_seed_checks=records,fixed_band_checks=band_records,source_examples=sources,endpoint1_raw_degree1_base=dict(halfrow=boundary_base,defects=boundary_defects),scope={'anchor_identity_BOTH':'PROVED','ordinary_prefix_N_ge_2':'PROVED conditional on existing MP_sharp certificates','fixed_proxy_band':'PROVED conditional on frozen source LR and strict prefix','raw_shifted_center_trace_tail_BOTH':'PROVED conditional on certified ordinary prefixes and existing pure-boundary prefix theorem, uniformly in r,N','ordinary_smoothed_shifted_center_trace_tail':'PROVED conditional on certified ordinary prefix, uniformly in r,N','frozen_source_all_new_origins':'OPEN','anchor_low_band':'OPEN','strict_proxy_BOTH':'OPEN','Local_TP2_full_tree':'OPEN'})

if __name__=='__main__':
    result=run();HERE.joinpath('proxy_algebra_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
