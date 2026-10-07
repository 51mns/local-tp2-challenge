"""Bounded, exact interval/rectangle certificate for a signed-seed ray criterion."""
from core import *
from itertools import product
from fractions import Fraction as F
import json

def bern2(vals):
    return (vals[0],2*vals[1]-(vals[0]+vals[2])/2,vals[2])
def bern_grid(grid,ndim):
    # Degree at most two per variable, nodes -2, 0, 2. All arithmetic exact.
    g={k:F(v) for k,v in grid.items()}
    for ax in range(ndim):
        new={}
        for rest in product(range(3),repeat=ndim-1):
            keys=[]
            for j in range(3):
                a=list(rest);a.insert(ax,j);keys.append(tuple(a))
            vals=bern2([g[k] for k in keys])
            for k,v in zip(keys,vals):new[k]=v
        g=new
    return g

def K(row,i,j):
    if i==0:return coeff(row,j)
    if j==0:return 2*coeff(row,i)
    return coeff(row,i-j)+coeff(row,i+j)
def minor(row,i,j,a,b):return K(row,i,a)*K(row,j,b)-K(row,i,b)*K(row,j,a)
def mass(a):return sum(c*2**j for j,c in enumerate(a))
def fractional(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):fractional(w) for k,w in v.items()}
    if isinstance(v,(list,tuple)):return [fractional(w) for w in v]
    return v

def run(word,direction):
    r=raydata(word,direction); A,B,t=r['A'],r['B'],r['t'];
    if all(v<=0 for v in H(B)):Q=scale(B,-1);sgn=-1
    elif all(v>=0 for v in H(B)):Q=B;sgn=1
    else:return {'word':word,'direction':direction,'fail':'mixed_sign_B'}
    data={'word':word,'direction':direction,'B_sign':sgn,'degrees':{k:len(v)-1 for k,v in r.items()},'fixed_polynomials':r,'gates':{},'certificates':{}}
    errors=[]
    def gate(name,cond,extra=None):
        data['gates'][name]={'passed':bool(cond),'extra':extra}
        if not cond:errors.append(name)
    a,b=len(r['X'])-1,len(r['Y'])-1
    gate('degree_prerequisites',len(r['C'])-1==a+b+1 and len(t)-1==a+1 and len(A)-1==a+b and len(B)-1<len(A)-1+a+1)
    gate('positive_leading',all(r[k][-1]>0 for k in ('X','Y','C','t','A')))
    gate('X_nonconstant',len(r['X'])>1)
    gate('B_abs_le_A',all(coeff(H(Q),i)<=coeff(H(A),i) for i in range(max(len(A),len(Q)))))
    for name in ('A','E1','K0','P','J','V','beta'):
        gate('positive_'+name,min(H(r[name]))>0)
    gate('yA_strict',min(delta_row(H(mul(y,A))))>0)
    gate('A_strict',min(delta_row(H(A)))>0)
    gate('Q_nonnegative',min(H(Q))>=0)
    gate('yQ_nonnegative',min(H(mul(y,Q)))>=0)
    for name,a,b in [('q0_q1',r['q0'],r['q1']),('beta_q1',r['beta'],r['q1']),('P_E1',r['P'],r['E1']),('P_q1',r['P'],r['q1'])]:
        gate(name,min(W(a,b))>=0,list(W(a,b)))
    wk=W(r['J'],r['V']);gate('J_V',min(wk)>0,wk)
    tau=mass(t)
    gate('tau_six',tau>=6,tau)
    # interval trace and template conditions
    rr=(-2,0,2); fs=[sub(t,(s,)) for s in rr];Ls=[add(mul(A,f),B) for f in fs]
    def intarray(label,values,strict=True):
        cert=[]
        for n in range(len(values[0])):
            b=bern_grid({(i,):values[i][n] for i in range(3)},1)
            cert.extend(b.values())
        data['certificates'][label]=cert
        gate(label,min(cert)>0 if strict else min(cert)>=0,{'min':min(cert),'count':len(cert)})
        return cert
    intarray('trace_delta',[delta_row(H(f)) for f in fs])
    intarray('trace_gamma2',[(delta_row(H(f))[0]-2*mass(f),) for f in fs])
    intarray('L_delta',[delta_row(H(f)) for f in Ls])
    intarray('yL_delta',[delta_row(H(mul(y,f))) for f in Ls])
    intarray('trace_coeffs',[H(f) for f in fs])
    intarray('L_coeffs',[H(f) for f in Ls])
    # actual midpoint, dimension two instead of three
    HH={}; yHH={}
    for i,s in enumerate(rr):
        for j,v in enumerate(rr):
            hh=add(mul(mul(A,sub(t,(s,))),sub(t,(v,))),mul(B,sub(t,(F(s+v,2),))))
            HH[(i,j)]=H(hh);yHH[(i,j)]=H(mul(y,hh))
    for label,table,ref in [('H',HH,Q),('yH',yHH,mul(y,Q))]:
        refh=H(ref);maxref=max(refh);cert=[];dom=[];supp=[]
        for n in range(len(next(iter(table.values())))):
            cert+=list(bern_grid({ij:delta_row(h)[n]-8*maxref*h[n] for ij,h in table.items()},2).values())
            dom+=list(bern_grid({ij:h[n]-coeff(refh,n) for ij,h in table.items()},2).values())
            supp+=list(bern_grid({ij:h[n] for ij,h in table.items()},2).values())
        data['certificates'][label+'_strong']=cert
        data['certificates'][label+'_domination']=dom
        data['certificates'][label+'_positive']=supp
        gate(label+'_strong',min(cert)>0,{'min':min(cert),'count':len(cert)})
        gate(label+'_domination',min(dom)>=0,{'min':min(dom)})
        gate(label+'_positive',min(supp)>0,{'min':min(supp)})
    # finite templates for mass domination; choose rational constants from full Bernstein array
    de=len(r['J'])-1; Kr=mul(r['P'],r['K0']);e=len(Kr)-1;m=len(r['K0'])-1
    lm=bern_grid({(i,):mass(f) for i,f in enumerate(Ls)},1)
    alphas=[];betas=[]
    for n in range(e+1):
        i0=min(n,de)
        dets=bern_grid({(i,):minor(H(f),i0,i0+1,n,n+1) for i,f in enumerate(Ls)},1)
        alpha=min(dets[k]/lm[k] for k in lm)/2
        alphas.append(alpha)
        gate('alpha_'+str(n),alpha>0,alpha)
    for n in range(m+2):
        dd=bern_grid({(i,):delta_row(H(mul(mul(y,y),f)))[n] for i,f in enumerate(Ls)},1)
        beta=min(dd[k]/lm[k] for k in lm)/2
        betas.append(beta);gate('beta_'+str(n),beta>0,beta)
    hK=H(Kr);hM=H(r['K0']);dM=delta_row(hM)
    md=[];rd=[];z1=mass(add(mul(A,add(t,one)),B))
    for n,aa in enumerate(alphas):
        md.append(F(1,2)*wk[min(n,de)]*aa-mass(r['J'])*coeff(hK,n))
    for n,bb in enumerate(betas):
        nu=coeff(hM,n-1)+3*coeff(hM,n+1)
        dl=dM[n] if n<len(dM) else 0
        rd.append(F(9,2)*bb-27*nu-F(max(-dl,0),z1))
    gate('proxy_correction',min(md)>0,{'min':min(md)})
    gate('multiplier_correction',min(rd)>0,{'min':min(rd)})
    data['certificates'].update(alphas=alphas,betas=betas,proxy_margins=md,multiplier_margins=rd)
    ss,dd=canonical_pair(word);gate('prefix_target',min(W(ss,dd))>0,min(W(ss,dd)))
    data['status']='PASS' if not errors else 'FAIL';data['failed_gates']=errors
    return fractional(data)

if __name__=='__main__':
    import sys
    w=sys.argv[1] if len(sys.argv)>1 else 'LRL';dr=sys.argv[2] if len(sys.argv)>2 else 'R'
    a=run(w,dr)
    fname=f'certificate_{w or "root"}_{dr}.json'
    with open(fname,'w') as f:json.dump(a,f,indent=2,sort_keys=True);f.write('\n')
    print(w,dr,a['status'],a['failed_gates'])
