"""Exact finite-channel and mixed-mass certificates (standard library only).
The all-length implication is the proof in THEOREM.md, not the regression scan.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from math import comb
import hashlib, json


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return tuple(p or [0])
def add(a,b):
    return trim((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                for i in range(max(len(a),len(b))))
def scale(a,c): return trim(c*x for x in a)
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return trim(z)
x=(0,1); y=(1,1); p=(2,1); one=(1,)
def mutate(X,C,Y): return sub(sub(scale(mul(mul(y,X),C),3),mul(x,add(X,C))),Y)
def state(word):
    a,c,b=one,(5,6,2),p
    for ch in word:
        if ch=='L': a,c,b=a,mutate(a,c,b),c
        elif ch=='R': a,c,b=c,mutate(b,c,a),b
        else: raise ValueError('word must use only L/R')
    return a,c,b
def div_y(a):
    z=list(a); q=[0]*(len(z)-1)
    for j in range(len(q)-1,-1,-1): q[j]=z[j+1]; z[j]-=q[j]
    if z[0]: raise ValueError('division by x+1 is not exact')
    return trim(q)
def H(a): return tuple(sum(a[j]*comb(j,(j-i)//2) for j in range(i,len(a),2)) for i in range(len(a)))
def at(h,i): return h[abs(i)] if abs(i)<len(h) else 0
def delta(h): return tuple(v*v-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+v*at(h,n+2) for n,v in enumerate(h))
def Wrow(a,b,n): return at(a,n)*at(b,n+1)-at(a,n+1)*at(b,n)
def W(a,b,n): return Wrow(H(a),H(b),n)
def K(h,i,j):
    if i==0:return at(h,j)
    if j==0:return 2*at(h,i)
    return at(h,i-j)+at(h,i+j)
def minor(h,i,j): return K(h,i,j)*K(h,i+1,j+1)-K(h,i,j+1)*K(h,i+1,j)
def mass(a): return sum(c*2**i for i,c in enumerate(a))
def ray(word,direction):
    X,C,Y=state(word)
    if direction=='R':X,Y=Y,X
    elif direction!='L':raise ValueError(direction)
    t=sub(scale(mul(y,X),3),x)
    T=sub(sub(mul(t,Y),mul(x,X)),C)
    A=div_y(sub(C,Y));B=div_y(sub(T,Y))
    P=mul(p,X);J=mul(y,sub(t,(2,)));V=scale(mul(mul(y,y),P),3)
    M0=add(sub(scale(mul(y,Y),3),x),one)
    return dict(X=X,C=C,Y=Y,t=t,A=A,B=B,P=P,J=J,V=V,M0=M0,K=mul(P,M0),
                q0=mul(y,A),q1=mul(y,add(mul(t,A),B)),beta=mul(y,add(A,B)),E1=sub(C,X))

def bern(grid,dim):
    g={k:F(v) for k,v in grid.items()}
    for axis in range(dim):
        out={}
        for rest in product(range(3),repeat=dim-1):
            keys=[]
            for j in range(3):
                a=list(rest);a.insert(axis,j);keys.append(tuple(a))
            v=[g[k] for k in keys]
            b=(v[0],2*v[1]-(v[0]+v[2])/2,v[2])
            for k,c in zip(keys,b):out[k]=c
        g=out
    return [g[k] for k in product(range(3),repeat=dim)]

def build(word,direction):
    r=ray(word,direction); A,B,t=r['A'],r['B'],r['t']; nodes=(-2,0,2)
    if all(c>=0 for c in B):Q=B
    elif all(c<=0 for c in B):Q=scale(B,-1)
    else:raise ValueError('B must have uniform sign')
    e=len(r['K'])-1;gamma=F(2);channels=e+1;y2=mul(y,y)
    arrays={};fail=[]
    def put(name,values,strict=True):
        vals=list(map(F,values));arrays[name]=vals
        if not vals or (min(vals)<=0 if strict else min(vals)<0):fail.append(name)
    fixed={}
    # All qualitative premises, including support and seed sign, are explicit.
    for name in ['X','Y','C','A','P','J','V','M0','K','q0','q1','beta','E1']:
        put('support_'+name,H(r[name]))
    put('abs_B_le_A',H(sub(A,Q)),strict=False)
    put('Q_nonnegative',H(Q),strict=False)
    put('A_delta',delta(H(A)));put('yA_delta',delta(H(mul(y,A))))
    for aa,bb in [('q0','q1'),('beta','q1'),('P','E1'),('P','q1')]:
        put('initial_'+aa+'_'+bb,[W(r[aa],r[bb],n) for n in range(len(r[aa]))],False)
    put('proxy_J_V',[W(r['J'],r['V'],n) for n in range(len(r['J']))])
    a,b=len(r['X'])-1,len(r['Y'])-1
    assert a>=1 and len(r['C'])-1==a+b+1 and len(t)-1==a+1
    assert len(A)-1==a+b and len(B)-1<len(A)-1+a+1
    assert mass(t)>=6
    fs=[sub(t,(v,)) for v in nodes];Ls=[add(mul(A,f),B) for f in fs]
    # One-parameter Bernstein arrays, channel-major.
    for name,tab in [('f_support',[H(f) for f in fs]),('f_delta',[delta(H(f)) for f in fs]),
                     ('L_support',[H(l) for l in Ls]),('L_delta',[delta(H(l)) for l in Ls]),
                     ('yL_support',[H(mul(y,l)) for l in Ls]),('yL_delta',[delta(H(mul(y,l))) for l in Ls])]:
        put(name,[c for n in range(len(tab[0])) for c in bern({(i,):tab[i][n] for i in range(3)},1)])
    for j in range(channels):
        put('channel_'+str(j),bern({(k,):sum(minor(H(f),i,j) for i in range(channels))-gamma*mass(f)
                                      for k,f in enumerate(fs)},1),False)
    Lmass=bern({(i,):mass(l) for i,l in enumerate(Ls)},1)
    put('L_mass',Lmass)
    proxy_diag=[];multi_diag=[]
    for n in range(channels):
        proxy_diag += bern({(i,):W(mul(r['J'],l),mul(r['V'],l),n) for i,l in enumerate(Ls)},1)
        multi_diag += bern({(i,):delta(H(mul(y2,l)))[n] for i,l in enumerate(Ls)},1)
    put('proxy_diagonal',proxy_diag);put('multiplier_diagonal',multi_diag)
    proxy_ratios=[v/Lmass[j%3] for j,v in enumerate(proxy_diag)]
    multi_ratios=[v/Lmass[j%3] for j,v in enumerate(multi_diag)]
    ef={};hh={}
    for i,rr in enumerate(nodes):
        for j,ss in enumerate(nodes):
            frr=sub(t,(rr,));fss=sub(t,(ss,))
            E=mul(add(mul(A,frr),B),fss)
            G=mul(add(mul(A,fss),B),frr)
            ef[i,j]=(E,G)
            hh[i,j]=scale(add(E,G),F(1,2))
    for label,smooth in [('midpoint',one),('midpoint_y',y)]:
        rows={ij:H(mul(smooth,z)) for ij,z in hh.items()}
        qh=H(mul(smooth,Q));bound=8*max(qh)
        size=len(next(iter(rows.values())))
        put(label+'_strength',[c for n in range(size) for c in bern({ij:delta(h)[n]-bound*h[n] for ij,h in rows.items()},2)])
        put(label+'_domination',[c for n in range(size) for c in bern({ij:at(h,n)-at(qh,n) for ij,h in rows.items()},2)],False)
        put(label+'_support',[c for n in range(size) for c in bern({ij:h[n] for ij,h in rows.items()},2)])
    combined_mass=bern({ij:gamma*(mass(E)+mass(G)) for ij,(E,G) in ef.items()},2)
    put('mixed_mass',combined_mass)
    px=[];mx=[]
    for n in range(channels):
        px+=bern({ij:W(mul(r['J'],E),mul(r['V'],G),n)+W(mul(r['J'],G),mul(r['V'],E),n)
                  for ij,(E,G) in ef.items()},2)
        mx+=bern({ij:delta(H(mul(y2,add(E,G))))[n]-delta(H(mul(y2,E)))[n]-delta(H(mul(y2,G)))[n]
                  for ij,(E,G) in ef.items()},2)
    put('proxy_mixed',px);put('multiplier_mixed',mx)
    proxy_ratios += [v/combined_mass[j%9] for j,v in enumerate(px)]
    multi_ratios += [v/combined_mass[j%9] for j,v in enumerate(mx)]
    cp=min(proxy_ratios);cm=min(multi_ratios)
    if cp<=0 or cm<=0:raise ValueError('positive mixed normalized templates required')
    put('proxy_normalized_margin',[v-cp*Lmass[j%3] for j,v in enumerate(proxy_diag)],False)
    put('multiplier_normalized_margin',[v-cm*Lmass[j%3] for j,v in enumerate(multi_diag)],False)
    put('proxy_mixed_normalized_margin',[v-cp*combined_mass[j%9] for j,v in enumerate(px)],False)
    put('multiplier_mixed_normalized_margin',[v-cm*combined_mass[j%9] for j,v in enumerate(mx)],False)
    hp=H(r['K']);hm=H(r['M0']);dm=delta(hm)
    z1=mass(add(mul(A,add(t,one)),B));m=len(r['M0'])-1
    proxy_budget=mass(r['J'])*max(hp)
    mult_budget=max(27*(at(hm,n-1)+3*at(hm,n+1))+F(max(-at(dm,n),0),z1) for n in range(m+2))
    N0=1
    while not (cp*gamma**(N0-1)>proxy_budget and 9*cm*gamma**(N0-1)>mult_budget):
        N0+=1
        if N0>100:raise ValueError('transient budget exceeded')
    put('final_proxy_budget',[cp*gamma**(N0-1)-proxy_budget])
    put('final_multiplier_budget',[9*cm*gamma**(N0-1)-mult_budget])
    for N in range(N0):
        X,C,Y=state(word+direction*N)
        U,V=sorted((mutate(X,C,Y),mutate(Y,C,X)),key=len)
        S,D=sub(U,C),sub(V,U)
        put('transient_target_'+str(N),[W(S,D,n) for n in range(len(S))])
    fixed=dict(word=word,direction=direction,channels=channels,gamma=str(gamma),c_proxy=str(cp),
               c_multiplier=str(cm),tail_starts=N0,proxy_budget=str(proxy_budget),multiplier_budget=str(mult_budget),
               qualitative_scope='Signed ray criterion hypotheses; no arbitrary-turn closure assumed')
    encoded={name:[str(v) for v in values] for name,values in arrays.items()}
    digest=hashlib.sha256(json.dumps(encoded,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    summary=dict(fixed,status='PASS' if not fail else 'FAIL',failed_arrays=fail,
                 coefficient_count=sum(map(len,arrays.values())),all_array_sha256=digest,
                 extrema={name:{'count':len(vals),'min':str(min(vals))} for name,vals in arrays.items()})
    return dict(summary=summary,arrays=encoded)

if __name__=='__main__':
    from pathlib import Path
    out=Path(__file__).resolve().parent/'generated';out.mkdir(exist_ok=True)
    for word,direction in [('', 'R'),('LRL','R')]:
        result=build(word,direction)
        (out/f'author_{word or "root"}_{direction}.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result['summary'].items() if k!='extrema'},sort_keys=True))
        assert result['summary']['status']=='PASS'
