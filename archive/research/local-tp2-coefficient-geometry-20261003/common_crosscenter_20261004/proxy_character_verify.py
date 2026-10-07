#!/usr/bin/env python3
"""Exact Robin diagonal bound and weaker-target algebra; no tree-closure claim."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
from itertools import permutations

HERE=Path(__file__).resolve().parent

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
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
def H(a):return trim([sum(a[j]*comb(j,(j-n)//2) for j in range(n,len(a),2)) for n in range(len(a))])
def hv(a,n):return a[abs(n)] if abs(n)<len(a) else 0
def delta(h,n):return hv(h,n)**2-hv(h,n-1)*hv(h,n+1)-hv(h,n+1)**2+hv(h,n)*hv(h,n+2)
def W(h,k,n):return hv(h,n)*hv(k,n+1)-hv(h,n+1)*hv(k,n)
def R(f,g):
    h,k=H(f),H(g);z={}
    for i in range(max(len(h),len(k))):
        for j in range(i+1,max(len(h),len(k))):
            w=hv(h,i)*hv(k,j)-hv(h,j)*hv(k,i)
            if w:
                z[i+j-1,j-i-1]=w
                if i:z[j-i-1,i+j-1]=w
    return z
def cpadd(*aa):
    z={}
    for a in aa:
        for k,v in a.items():z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}

x,y,P=[0,1],[1,1],[2,1]
def state(a,e,r):
    X=add([1],mul(y,a));t=sub(scale(mul(y,X),3),x)
    k=mul(X,sub(scale(X,3),[2]));g=add(mul(sub(t,[2]),e),k,r)
    s=sub(mul(t,g),r);Y=add(X,mul(y,e));C=add(Y,mul(y,g))
    M=add(sub(scale(mul(y,C),3),x),[1])
    Q=sub(mul(sub(t,[2]),C),mul(x,X));Pi=mul(X,P,M)
    V=add(mul(P,X),mul(P,P,C));E=mul(y,e);G=mul(y,g);S=mul(y,s);D=mul(E,M)
    fricke=sub(mul(r,g),add(mul(sub(t,[2]),e,e),scale(mul(k,e),2),scale(mul(a,X,X),3)))
    assert fricke==[0]
    return dict(a=a,e=e,r=r,X=X,Y=Y,C=C,t=t,k=k,g=g,s=s,M=M,Q=Q,Pi=Pi,V=V,E=E,G=G,S=S,D=D)
def child(st,long=False):
    return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g'])) if long else state(st['a'],add(st['e'],st['g']),st['g'])

def min_quadratic(a,b,c):
    candidates=[(F(-2),4*a-2*b+c),(F(2),4*a+2*b+c)]
    if a>0:
        u=-b/(2*a)
        if -2<=u<=2:candidates.append((u,c-b*b/(4*a)))
    return min(candidates,key=lambda z:z[1])
def base_minima(t,b0,b1):
    rows=[H(mul(y,add(mul(b0,sub(t,[r])),b1))) for r in [-1,0,1]]
    out=[]
    for n in range(len(rows[1])):
        dm,dz,dp=[F(delta(h,n)) for h in rows]
        a=(dm+dp-2*dz)/2;b=(dp-dm)/2
        u,m=min_quadratic(a,b,dz)
        assert m>0
        out.append(dict(index=n,a=a,b=b,c=dz,minimizer=u,minimum=m))
    return out
def trace_minima(t):
    h=H(t);d=len(h)-1
    mu=[(h[0]-2)**2-hv(h,1)**2]
    if d>=1:mu.append(hv(h,1)**2-(h[0]+2)*hv(h,2))
    for j in range(2,d+1):mu.append(h[j]**2-hv(h,j-1)*hv(h,j+1))
    assert all(v>0 for v in mu)
    return mu
def cb_bound(t,b0,b1,N):
    """Uniform bound obtained by one exact CB term at each product."""
    eta=[z['minimum'] for z in base_minima(t,b0,b1)];mu=trace_minima(t)
    d=len(t)-1;f0=len(b0)-1+d+1;fN=f0+(N-1)*d
    out=[]
    for n in range(fN+1):
        idx=n;prod=F(1)
        for stage in range(N-1,0,-1):
            prior_degree=f0+(stage-1)*d
            prev=max(d,min(idx,prior_degree))
            prod*=2*t[-1]**2 if idx==0 else mu[abs(prev-idx)]
            idx=prev
        out.append(F(3,2*N+1)*eta[idx]*prod)
    return out

def symbolic_checks():
    def mc(v,n):return {(0,)*n:v} if v else {}
    def mv(i,n):return {tuple(int(j==i) for j in range(n)):1}
    def ma(*aa):return cpadd(*aa)
    def ms(a,v):return {k:c*v for k,c in a.items() if c*v}
    def mm(*aa):
        z=mc(1,len(next(iter(aa[0]))))
        for a in aa:
            out={}
            for i,c in z.items():
                for j,d in a.items():
                    k=tuple(u+v for u,v in zip(i,j));out[k]=out.get(k,0)+c*d
            z={k:c for k,c in out.items() if c}
        return z
    xx,aa,ee,rr,XX,CC=[mv(i,6) for i in range(6)]
    one=mc(1,6);yy=ma(xx,one);pp=ma(xx,mc(2,6));xend=ma(one,mm(yy,aa))
    t=ma(ms(mm(yy,xend),3),ms(xx,-1));k=mm(xend,ma(ms(xend,3),mc(-2,6)))
    g=ma(mm(ma(t,mc(-2,6)),ee),k,rr)
    long_F=ma(mm(yy,g),ms(mm(pp,ma(xend,mm(yy,ee))),-1))
    positive=ma(mm(ma(mm(xx,xx),mc(-1,6)),ee),xx,mm(yy,ma(rr,mc(-1,6))),
                mm(yy,aa,ma(mc(2,6),ms(xx,3))),ms(mm(yy,yy,yy,aa,ma(aa,ee)),3))
    assert not ma(long_F,ms(positive,-1))
    Q=ma(mm(ma(ms(mm(yy,XX),3),ms(pp,-1)),CC),ms(mm(xx,XX),-1))
    V=ma(mm(pp,XX),mm(pp,pp,CC))
    QV=ma(ms(mm(pp,ma(mm(xx,CC),ms(yy,-1))),2),mm(yy,ma(XX,ms(pp,-1)),ma(ms(CC,3),mc(-2,6))))
    assert not ma(Q,ms(V,-1),ms(QV,-1))

    def det_poly(M):
        N=len(M);out=[0]
        for perm in permutations(range(N)):
            sign=(-1)**sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
            out=add(out,scale(mul(*[M[i][perm[i]] for i in range(N)]),sign))
        return out
    def adj_poly(M):
        N=len(M)
        return [[scale(det_poly([[M[r][c] for c in range(N) if c!=i] for r in range(N) if r!=j]),(-1)**(i+j)) for j in range(N)] for i in range(N)]
    def biprod(pa,pb):
        return {(i,j):u*v for i,u in enumerate(pa) for j,v in enumerate(pb) if u*v}
    p=[[1],[-1,1]]
    for n in range(2,5):p.append(sub(mul([0,1],p[-1]),p[-2]))
    checks=[]
    for N in range(1,5):
        J=[[0]*N for _ in range(N)]
        for i in range(N-1):J[i][i+1]=J[i+1][i]=1
        J[N-1][N-1]=1
        M=[[[(-J[i][j]),int(i==j)] for j in range(N)] for i in range(N)]
        adj=adj_poly(M)
        Wgt=[[(4 if i==j else 0)-sum(J[i][k]*J[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
        h=[3] if N==1 else sub(scale(p[N-1],4),mul([0,1],p[N-2]))
        assert add(*[scale(adj[k][0],Wgt[0][k]) for k in range(N)])==h
        K={}
        for i in range(max(len(h),len(p[N]))):
            for j in range(i+1,max(len(h),len(p[N]))):
                c=hv(h,i)*hv(p[N],j)-hv(p[N],i)*hv(h,j)
                for k in range(j-i):K[i+k,j-1-k]=K.get((i+k,j-1-k),0)+c
        K={k:c for k,c in K.items() if c}
        matrix_kernel=cpadd(*[{ij:c*Wgt[k][l] for ij,c in biprod(adj[0][k],adj[l][0]).items()} for k in range(N) for l in range(N)])
        assert matrix_kernel==K
        assert Wgt[0][0]==3
        checks.append(dict(N=N,p_N=p[N],h_N=h,weighted_one_resolvent=True,weighted_two_resolvent=True))
    return dict(long_F_expansion=True,interior_Q_minus_V_expansion=True,robin_diagonal_kernel_checks=checks)

def run():
    syms=symbolic_checks()
    root=state([0],[1],[1]);long=child(root,True)
    sts=[('root',root),('short',child(root)),('long',long),('long,long',child(long,True))]
    records=[]
    for name,st in sts:
        Q,Pi,V,E,G,S,D,M=[st[k] for k in ['Q','Pi','V','E','G','S','D','M']]
        Fsur=sub(E,mul(st['X'],P));B=sub(D,mul(P,Q))
        assert B==add(V,mul(Fsur,M))
        assert R(S,D)==cpadd(R(Q,Pi),R(G,Pi),R(S,mul(Fsur,M)))
        assert R(Q,D)==cpadd(R(Q,mul(P,Q)),R(Q,B))
        q,pi,d=H(Q),H(Pi),H(D)
        original=[W(q,pi,n) for n in range(len(q))]
        weaker=[W(q,d,n) for n in range(len(q))]
        assert all(z>0 for z in original+weaker)
        fs=H(Fsur)
        if name!='root':assert all(z>=0 for z in fs)
        qv=H(sub(Q,V))
        if st['X']!=[1]:assert all(z>=0 for z in qv)
        rb=R(Q,B)
        A=sub(st['t'],[2]);baseB=add(mul(P,P),scale(mul(y,Fsur),3));basechars=R(A,baseB)
        if name=='short':assert basechars[(0,0)]==-65
        records.append(dict(state=name,fricke=True,F_halfrow=fs,Q_minus_V_halfrow=qv,
                            original_proxy=original,weaker_Q_D_proxy=weaker,
                            B_source_char_nonnegative=all(z>=0 for z in rb.values()),
                            B_source_boundary=[rb.get((2*n,0),0) for n in range(len(q))],
                            factored_source_A=A,factored_source_B=baseB,
                            factored_source_boundary=[basechars.get((2*n,0),0) for n in range(len(A))]))

    # The actual first-long smaller origin is (t,2P,0), N=2.
    t=long['t'];b0=scale(P,2);b1=[0];N=2
    p2=sub(sub(mul(t,t),t),[1]);Q=mul(y,b0,p2)
    assert Q==long['Q']
    bounds=cb_bound(t,b0,b1,N);q,v=H(Q),H(long['V'])
    correction=[W(q,v,n) for n in range(len(q))]
    defects=[delta(q,n) for n in range(len(q))]
    assert all(bounds[n]<=defects[n] for n in range(len(q)))
    surplus=[bounds[n]+correction[n] for n in range(len(q))]
    assert surplus[0]==F(-737848,5)
    exact_diagonal=[F(3,5)*z for z in defects]
    # In this zero-b1 example every residue summand is Q itself.
    exact_diagonal_surplus=[exact_diagonal[n]+correction[n] for n in range(len(q))]
    assert all(z>0 for z in exact_diagonal_surplus)
    return dict(status='exact identities and targeted finite checks PASS',
                scope='Universal algebra checked; canonical states only identify seeds/obstacles, not arbitrary BOTH closure.',
                symbolic=syms,targeted_states=records,
                coarse_quantitative_gate_obstacle=dict(state='first-long',origin_t=t,b0=b0,b1=b1,N=N,
                    eta=base_minima(t,b0,b1),mu=trace_minima(t),uniform_lower_bound=bounds,
                    adverse_correction=[-z for z in correction],gate_surplus=surplus,
                    actual_deltaQ=defects,actual_proxy=[defects[n]+correction[n] for n in range(len(q))],
                    exact_diagonal_bound=exact_diagonal,exact_diagonal_surplus=exact_diagonal_surplus,
                    meaning='Coarse CB lower bound is valid but insufficient. Full diagonal retention avoids this loss in this seed only.'),
                unresolved=['arbitrary canonical BOTH original strict proxy','arbitrary BOTH weaker Q<D gate',
                    'general R(Q,D-PQ)>=character0','quantitative retained mixed margin dominating W(Q,V)',
                    'new-center paired MP_sharp BOTH transport','full-tree strict Local TP2'])

def enc(v):
    if isinstance(v,F):return str(v)
    raise TypeError(type(v).__name__)
if __name__=='__main__':
    result=run()
    HERE.joinpath('proxy_character_results.json').write_text(json.dumps(result,indent=2,default=enc)+'\n')
    print(json.dumps(dict(status=result['status'],symbolic=result['symbolic'],
        first_long_coarse_central_surplus=result['coarse_quantitative_gate_obstacle']['gate_surplus'][0],
        exact_diagonal_seed_surplus_min=min(result['coarse_quantitative_gate_obstacle']['exact_diagonal_surplus']),
        unresolved=result['unresolved']),indent=2,default=enc))
