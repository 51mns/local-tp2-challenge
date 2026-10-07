"""Numerical discovery only; exact witnesses must be checked separately."""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

def add(*ps):
    z=np.zeros(max(map(len,ps)))
    for p in ps:z[:len(p)]+=p
    return z
def mul(*ps):
    z=np.ones(1)
    for p in ps:z=np.convolve(z,p)
    return z
def sub(p,q):return add(p,-np.asarray(q))
y=np.array([1.,1.]);P=np.array([2.,1.]);z=np.array([3.,2.])
def H(p):
    h=np.zeros(len(p))
    for j,c in enumerate(p):
        for n in range(j%2,j+1,2):h[n]+=c*math.comb(j,(j-n)//2)
    while len(h)>1 and h[-1]==0:h=h[:-1]
    return h
def vals(h,n):return h[abs(n)] if abs(n)<len(h) else 0.
def delta(h):
    return np.array([(vals(h,n)**2-vals(h,n-1)*vals(h,n+1)-vals(h,n+1)**2+vals(h,n)*vals(h,n+2))/(vals(h,n)**2+1e-100) for n in range(len(h))])
def W(f,h):
    f,h=H(f),H(h)
    return np.array([(vals(f,n)*vals(h,n+1)-vals(f,n+1)*vals(h,n))/(vals(f,n)*vals(h,n)+1e-100) for n in range(len(f))])
def state(a,e,r):
    X=add([1],mul(y,a));t=add(z,3*mul(y,y,a));k=mul(X,add([1],3*mul(y,a)))
    g=add(mul(sub(t,[2]),e),k,r);s=sub(mul(t,g),r)
    E,G,R=mul(y,e),mul(y,g),mul(y,r);S=mul(y,s)
    Y=add(X,E);C=add(Y,G);M=add(2*P,3*mul(y,y,add(a,e,g)))
    Q=sub(S,G);Pi=mul(X,P,M)
    return dict(a=a,e=e,r=r,g=g,E=E,G=G,R=R,S=S,X=X,Y=Y,C=C,M=M,Q=Q,Pi=Pi)
def constraints(v):
    return np.concatenate([W(v['E'],v['G']),W(v['R'],v['G']),W(mul(v['X'],P),v['E']),W(mul(v['Y'],P),v['G']),delta(H(v['G'])),delta(H(v['M'])),W(v['Q'],v['Pi'])])
def children(v):
    a,e,r,g=(v[k] for k in ('a','e','r','g'))
    return [state(a,add(e,g),g),state(add(a,e),g,add(e,g))]
def gates(v):return np.concatenate([delta(H(v['G'])),delta(H(v['M'])),W(v['Q'],v['Pi'])])
def decode(x,degree,adeg):
    a=np.asarray(x[:adeg+1]);u=np.asarray(x[adeg+1:adeg+degree+2]);e=add(a,u)
    # Last degree+1 coordinates are coefficient fractions.
    r=add(a,e)*x[adeg+degree+2:]
    return state(a,e,r)
def main(degree=3,adeg=0,starts=12,zero_a=False):
    rng=np.random.default_rng(55314+degree+adeg)
    bounds=[(.00001,10.)]*(adeg+1)+[(.00001,10.)]*(degree+1)+[(.00001,1.)]*(degree+1)
    if zero_a:bounds[:adeg+1]=[(0.,0.)]*(adeg+1)
    best=1e100;out=[]
    for k in range(starts):
        x=np.r_[rng.uniform(0,1,adeg+1),np.exp(rng.uniform(-3,2,degree+1)),rng.uniform(.05,.95,degree+1)]
        if zero_a:x[:adeg+1]=0
        pv=decode(x,degree,adeg)
        # Feasibility stage preserves strict proxy up to a small margin.
        res=minimize(lambda q:-min(np.min(constraints(decode(q,degree,adeg))),.001),x,method='SLSQP',bounds=bounds,options={'maxiter':100,'ftol':1e-10})
        if np.min(constraints(decode(res.x,degree,adeg))) < -1e-7:continue
        x=res.x
        childg=[gates(cv) for cv in children(decode(x,degree,adeg))]
        for side in range(2):
            # Minimize the handful of weakest child defect/surplus indices.
            cv=children(decode(x,degree,adeg))[side]
            ng,nm,nq=map(lambda k:len(H(cv[k])),['G','M','Q'])
            targets=list(range(min(6,ng-1)))+list(range(ng,ng+min(6,nm-1)))+list(range(ng+nm,ng+nm+min(6,nq-1)))
            for idx in targets:
                def obj(q):return gates(children(decode(q,degree,adeg))[side])[idx]
                def con(q):return constraints(decode(q,degree,adeg))
                rr=minimize(obj,x,method='SLSQP',bounds=bounds,constraints={'type':'ineq','fun':con},options={'maxiter':180,'ftol':1e-11})
                val=obj(rr.x);feas=np.min(con(rr.x))
                if feas>=-1e-7 and val<best:
                    best=val;record=dict(degree=degree,adeg=adeg,start=k,side=side,index=int(idx),value=float(val),parent_min=float(feas),x=rr.x.tolist())
                    out.append(record);print(json.dumps(record),flush=True)
                if feas>=-1e-8 and val<-.00001:
                    Path(__file__).with_name('gate_optimize_candidate.json').write_text(json.dumps(out,indent=2)+'\n');return
    Path(__file__).with_name(f'gate_optimize_{degree}_{adeg}_results.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=3);ap.add_argument('--adeg',type=int,default=0);ap.add_argument('--starts',type=int,default=12);ap.add_argument('--zero-a',action='store_true')
    q=ap.parse_args();main(q.degree,q.adeg,q.starts,q.zero_a)
