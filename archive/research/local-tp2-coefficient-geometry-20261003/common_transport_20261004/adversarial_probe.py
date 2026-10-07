#!/usr/bin/env python3
"""Standalone exact targeted P_Q closure probe; standard library only."""
import itertools,json,hashlib
from fractions import Fraction
from math import comb
from pathlib import Path

def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(*ps):
 r=[0]*max(map(len,ps))
 for p in ps:
  for i,v in enumerate(p):r[i]+=v
 return trim(r)
def scale(p,c):return trim([c*v for v in p])
def sub(p,q):return add(p,scale(q,-1))
def mul(p,q):
 r=[0]*(len(p)+len(q)-1)
 for i,u in enumerate(p):
  for j,v in enumerate(q):r[i+j]+=u*v
 return trim(r)
def power(p,n):
 r=[1]
 for _ in range(n):r=mul(r,p)
 return r
y=[1,1];y2=[1,2,1];P=[2,1];z=[3,2]
def build(a,e,r):
 X=add([1],mul(y,a));t=add(z,scale(mul(y2,a),3));k=mul(X,sub(scale(X,3),[2]));g=add(mul(sub(t,[2]),e),k,r)
 s=sub(mul(t,g),r);Y=add(X,mul(y,e));C=add(Y,mul(y,g));M=sub(add(scale(mul(y,C),3),[1]),[0,1]);d=mul(e,M)
 E,G,R,S,D=[mul(y,w) for w in (e,g,r,s,d)];Q=sub(S,G);Pi=mul(mul(X,P),M)
 return dict(a=a,e=e,r=r,g=g,s=s,d=d,X=X,Y=Y,C=C,t=t,k=k,M=M,E=E,G=G,R=R,S=S,D=D,Q=Q,Pi=Pi)
def children(v):
 a,e,r,g=[v[k] for k in ('a','e','r','g')]
 return [('short',build(a,add(e,g),g)),('long',build(add(a,e),g,add(e,g)))]
def H(p):
 h=[0]*len(p)
 for m,c in enumerate(p):
  for n in range(m%2,m+1,2):h[n]+=c*comb(m,(m-n)//2)
 return trim(h)
def at(h,n):return h[abs(n)] if abs(n)<len(h) else 0
def defects(h):return [at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2) for n in range(len(h))]
def minors(h,v):return [at(h,n)*at(v,n+1)-at(h,n+1)*at(v,n) for n in range(max(len(h),len(v)))]
def chars(p):
 h=H(p);return [v-at(h,n+1) for n,v in enumerate(h)]
def ordinary(v):
 a,e,r,g=[v[k] for k in ('a','e','r','g')]
 return all(min(p)>=0 for p in [a,sub(e,add(a,[1])),sub(r,[1]),sub(add(a,e),r),sub(e,mul([1,2],a)),sub(g,add(a,e,r,[1]))])
def gates(v):
 fail={};summ={}
 for key,p,q,strict in [('E_G',v['E'],v['G'],False),('R_G',v['R'],v['G'],False),('XP_E',mul(v['X'],P),v['E'],False),('YP_G',mul(v['Y'],P),v['G'],False),('proxy',v['Q'],v['Pi'],True)]:
  hp,hq=H(p),H(q);ds=minors(hp,hq);ds=ds[:len(hp)] if strict else ds
  ix=[i for i,u in enumerate(ds) if u<0 or(strict and u==0)];summ[key]=min(ds)
  if ix:fail[key]={'index':ix[0],'value':ds[ix[0]],'p':p,'q':q,'rows':[hp,hq]}
 for key in ('G','M'):
  h=H(v[key]);ds=defects(h);ix=[i for i,u in enumerate(ds) if u<0];summ[key]=min(ds)
  if min(h)<=0 or ix:fail[key]={'index':ix[0] if ix else h.index(min(h)),'value':ds[ix[0]] if ix else min(h),'p':v[key],'row':h,'defects':ds}
 return fail,summ
def fricke(v):
 a,e,r,g,X,t,k=[v[k] for k in ('a','e','r','g','X','t','k')]
 return sub(mul(r,g),add(mul(sub(t,[2]),mul(e,e)),scale(mul(k,e),2),scale(mul(a,mul(X,X)),3)))
def extras(v):
 X,Y,C,t=[v[k] for k in ('X','Y','C','t')];rho=sub(C,mul(sub(t,[1]),Y));corr=sub(mul(t,Y),C)
 T=add([1],mul(y,sub(add(v['a'],v['e']),v['r'])))
 xc,yc,cc=[chars(p) for p in (X,Y,C)]
 return {'strict_endpoint_degrees':len(X)<len(Y)<len(C),
 'golden_rational_sufficient':min(sub(scale(v['r'],5),scale(v['e'],3)))>=0 and min(sub(scale(v['e'],5),scale(v['r'],3)))>=0,
 'dense_character_XYCEGR':all(min(chars(v[k]))>0 for k in ('X','Y','C','E','G','R')),
 'character_strip':min(chars(rho))>0 and min(chars(corr))>=0,
 'character_additive_separation':min(chars(sub(C,mul(y,add(X,Y)))))>0,
 'endpoint_character_inequalities':at(xc,1)>=xc[0]-1 and at(yc,1)>=yc[0]-1 and at(cc,1)>=cc[0],
 'inverse_endpoint':T,'inverse_degree_pattern':len(T)<len(X) and len(Y)-1==(len(X)-1)+(len(T)-1)+1,
 'fricke_zero':fricke(v)==[0]}
def candidates():
 for m,L,h in itertools.product(range(7),(1,4,16),(0,1,4,16,64)):
  spike=[0]*m+[h];a=scale(add(power(y,m),spike),4*L)
  # Exact inherited normalized state: only long move, not actual if off-Fricke.
  ancestor=build([0],a,a);v=dict(children(ancestor))['long']
  yield {'family':'inherited','m':m,'L':L,'h':h},v,ancestor
  for N,B,nrho in itertools.product(range(m+1,m+6),(1,4,16),(1,2,3,4)):
   e=add(mul([1,2],a),[1],scale(power(y,N),B));r=add(e,[u*nrho//4 for u in a])
   assert all(u%4==0 for u in a)
   yield {'family':'perturbed','m':m,'L':L,'h':h,'N':N,'B':B,'rho_num':nrho,'rho_den':4},build(a,e,r),None
def main():
 out={'status':'BOUNDED_EXACT_TARGETED_PROBE_NOT_CLOSURE_PROOF','tested':0,'parent_passes':0,'counts':{},'strong_parent_counts':{},'first_failure':None,'accepted_examples':[]}
 for params,v,ancestor in candidates():
  out['tested']+=1;assert ordinary(v);fail,summ=gates(v)
  family=params['family'];out['counts'].setdefault(family,{'tested':0,'parent_passes':0,'both_children_pass':0});fc=out['counts'][family];fc['tested']+=1
  if fail:continue
  fc['parent_passes']+=1;out['parent_passes']+=1;ex=extras(v);res=fricke(v)
  # Classification prevents labelling positive Fricke states as merely abstract.
  assert res!=[0], 'A positive Fricke state is actual by the descent theorem.'
  afail,asumm=gates(ancestor) if ancestor else (None,None)
  if ancestor:assert ordinary(ancestor)
  for k,b in ex.items():
   if isinstance(b,bool) and b:out['strong_parent_counts'][k]=out['strong_parent_counts'].get(k,0)+1
  if ancestor and not afail:out['strong_parent_counts']['ancestor_PQ']=out['strong_parent_counts'].get('ancestor_PQ',0)+1
  for label,nv in children(v):
   assert ordinary(nv);nf,ns=gates(nv)
   if nf:
    out['first_failure']={'classification':'OFF-FRICKE abstract full-parent P_Q child failure','parameters':params,'parent':{k:v[k] for k in ('a','e','r','X','Y','C')},'parent_gate_minima':summ,'extra_constraints':ex,'Fricke_residual':res,'move':label,'child_state':{k:nv[k] for k in ('a','e','r')},'child_failed_gates':nf,'ancestor':{k:ancestor[k] for k in ('a','e','r')} if ancestor else None,'ancestor_gate_failures':afail}
    return out
  fc['both_children_pass']+=1
  if len(out['accepted_examples'])<3:out['accepted_examples'].append({'parameters':params,'extras':ex,'parent_minima':summ})
 return out
if __name__=='__main__':
 out=main();p=Path(__file__).with_name('adversarial_results.json');p.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('tested','parent_passes','counts','strong_parent_counts','first_failure')},indent=2))
