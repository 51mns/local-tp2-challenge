#!/usr/bin/env python3
"""Exact coupled-prefix identities and an initialized ordinary residual obstacle."""
from pathlib import Path
from math import comb
import json

HERE=Path(__file__).resolve().parent
def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]:p.pop()
    return p
def add(*aa):
    z=[0]*max(map(len,aa))
    for a in aa:
        for i,c in enumerate(a):z[i]+=c
    return trim(z)
def scale(a,c):return trim([v*c for v in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(*aa):
    z=[1]
    for a in aa:
        o=[0]*(len(z)+len(a)-1)
        for i,c in enumerate(z):
            for j,d in enumerate(a):o[i+j]+=c*d
        z=trim(o)
    return z
def H(p):return trim([sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2)) for n in range(len(p))])
def hv(h,n):return h[abs(n)] if abs(n)<len(h) else 0
def R(f,g):
    h,k=H(f),H(g);z={}
    for i in range(max(len(h),len(k))):
        for j in range(i+1,max(len(h),len(k))):
            v=hv(h,i)*hv(k,j)-hv(h,j)*hv(k,i)
            if v:
                z[i+j-1,j-i-1]=v
                if i:z[j-i-1,i+j-1]=v
    return z
def tensor(f):return R(f,[0]+f)
def cpadd(*aa):
    z={}
    for a in aa:
        for k,c in a.items():z[k]=z.get(k,0)+c
    return {k:c for k,c in z.items() if c}
def cpmul(a,b):
    z={}
    for (i,j),c in a.items():
        for (k,l),d in b.items():
            for r in range(abs(i-k),i+k+1,2):
                for s in range(abs(j-l),j+l+1,2):z[r,s]=z.get((r,s),0)+c*d
    return {k:c for k,c in z.items() if c}

x,y,P=[0,1],[1,1],[2,1]
def state(a,e,r):
    X=add([1],mul(y,a));t=sub(scale(mul(y,X),3),x)
    k=mul(X,sub(scale(X,3),[2]));g=add(mul(sub(t,[2]),e),k,r)
    s=sub(mul(t,g),r);Y=add(X,mul(y,e));C=add(Y,mul(y,g))
    M=add(sub(scale(mul(y,C),3),x),[1]);T=sub(M,[1]);c=add(e,g,s)
    Q=sub(mul(sub(t,[2]),C),mul(x,X));E=mul(y,e);G=mul(y,g);S=mul(y,s);D=mul(E,M)
    assert sub(mul(r,g),add(mul(sub(t,[2]),e,e),scale(mul(k,e),2),scale(mul(a,X,X),3)))==[0]
    return dict(a=a,e=e,r=r,X=X,Y=Y,C=C,t=t,k=k,g=g,s=s,M=M,T=T,c=c,Q=Q,E=E,G=G,S=S,D=D)
def child(st,long=False):
    return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g'])) if long else state(st['a'],add(st['e'],st['g']),st['g'])
def seq(t,N):
    U=[[1],t]
    for j in range(2,N+1):U.append(sub(mul(t,U[-1]),U[-2]))
    return U[:N+1]
def origin(t,b0,b1,aO,aX,N):
    U=seq(t,N)
    uu=lambda j:U[j] if j>=0 else [0]
    rr=lambda j:add(*U[:j+1]) if j>=0 else [0]
    f=lambda j:add(mul(b0,uu(j)),mul(b1,uu(j-1)))
    Z=lambda j:add(mul(b0,rr(j-1)),mul(b1,rr(j-2)))
    assert sub(Z(N),f(N-1))==Z(N-1)
    assert sub(Z(N+1) if N+1<=len(U) else add(Z(N),f(N)),Z(N))==f(N)
    Hanchor=sub(aO,aX);e=add(Hanchor,Z(N-1));J=mul(y,sub(t,[2]));q0=mul(y,add(b0,b1))
    Q=add(mul(J,Z(N)),q0);M0=add(scale(P,2),scale(mul(y,y,aO),3))
    M=add(M0,scale(mul(y,y,Z(N)),3));E=mul(y,e);D=mul(E,M)
    assert Q==mul(y,sub(f(N),f(N-1)))
    L=scale(mul(y,y,E),3);d0=mul(M0,E)
    lead=cpmul(tensor(Z(N)),R(J,L))
    residual=cpadd(R(mul(J,Z(N)),d0),R(q0,mul(L,Z(N))),R(q0,d0))
    assert cpadd(lead,residual)==R(Q,D)
    Lu=scale(mul(y,y,y,Z(N-1)),3)
    du=add(d0,scale(mul(y,y,y,Hanchor,Z(N)),3))
    ru=cpadd(R(mul(J,Z(N)),du),R(q0,mul(Lu,Z(N))),R(q0,du))
    assert cpadd(cpmul(tensor(Z(N)),R(J,Lu)),ru)==R(Q,D)
    return dict(N=N,Z=Z(N),Zprev=Z(N-1),Hanchor=Hanchor,e=e,Q=Q,E=E,D=D,J=J,L=L,q0=q0,d0=d0,M0=M0,lead=lead,residual=residual,source=R(J,L),unanchored_residual=ru)

def run():
    root=state([0],[1],[1]);short=child(root);long=child(root,True)
    B=add(root['a'],root['e'],root['g'])
    cases=[('root-Y first retained',long,origin(long['t'],scale(P,2),[0],[0],[1],2)),
           ('forward C-origin first retained',child(short,True),origin(root['T'],root['c'],root['e'],root['a'],B,2)),
           ('reverse C-origin first retained',child(long,True),origin(root['T'],root['e'],root['c'],root['a'],B,3))]
    records=[]
    for name,st,o in cases:
        assert o['Q']==st['Q'] and o['E']==st['E'] and o['D']==st['D']
        assert st['C']==add([1],mul(y,add([0] if name.startswith('root-Y') else root['a'],o['Z'])))
        chars=R(st['Q'],st['D']);boundary=[chars.get((2*n,0),0) for n in range(len(st['Q']))]
        assert all(v>0 for v in boundary)
        records.append(dict(name=name,N=o['N'],normalized_Fricke=True,Hanchor=o['Hanchor'],
            Z_N=o['Z'],Z_previous=o['Zprev'],actual_e=o['e'],
            exact_Q_E_D_match=True,source_character_nonnegative=all(v>=0 for v in o['source'].values()),
            source_boundary=[o['source'].get((2*n,0),0) for n in range(len(o['J']))],
            lead_boundary=[o['lead'].get((2*n,0),0) for n in range(len(st['Q']))],
            residual_boundary=[o['residual'].get((2*n,0),0) for n in range(len(st['Q']))],
            actual_Q_D_boundary=boundary,
            unanchored_residual_central=o['unanchored_residual'].get((0,0),0),
            residual_negative_characters=[[list(k),v] for k,v in sorted(o['residual'].items()) if v<0]))
    first=records[0]
    assert first['source_boundary']==[129,195,90,18]
    assert first['residual_boundary']==[11688,24412,4804,-2504,0,0,0]
    assert first['lead_boundary'][3]==1311780 and first['actual_Q_D_boundary'][3]==1309276
    assert first['unanchored_residual_central']==-52128
    assert [[6,0],-2504] in first['residual_negative_characters']
    # Exact algebra replay at formal trace values, independent of actual states.
    identities=[]
    for N in range(2,7):
        o=origin([0,1],[3,2],[5,1],[7],[11],N)
        identities.append(dict(N=N,exact_prefix_difference=True,exact_full_tensor_split=True))
    return dict(status='exact coupled-prefix and initialized residual checks PASS',
        arithmetic='Python integers only; no external dependency',
        scope='Finite identities validate formulas. All-N algebra is proved in proxy_character.md; no source or proxy closure inferred from samples.',
        first_use_switch_cases=records,formal_trace_identity_replays=identities,
        obstruction='Nonnegative full source plus strict prefix kernel does not permit separately nonnegative residual; actual first-long residual n=3 is -2504.',
        unresolved=['quantitative domination of signed prefix residual for arbitrary origin and BOTH switch rules',
                    'initialized arbitrary BOTH source preservation','arbitrary BOTH strict Q<D','full-tree strict Local TP2'])
if __name__=='__main__':
    result=run();HERE.joinpath('proxy_character_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],first_long_source=result['first_use_switch_cases'][0]['source_boundary'],
        first_long_signed_residual=result['first_use_switch_cases'][0]['residual_boundary'],unresolved=result['unresolved']),indent=2))
