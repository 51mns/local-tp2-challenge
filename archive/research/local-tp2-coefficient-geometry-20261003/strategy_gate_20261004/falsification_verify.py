#!/usr/bin/env python3
"""Independent exact bounded adversarial replay. No imports from earlier arithmetic."""
from math import comb
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def trim(p):
 p=list(p)
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def add(*ps):
 q=[0]*max(map(len,ps))
 for p in ps:
  for i,v in enumerate(p):q[i]+=v
 return trim(q)
def scale(p,k):return trim([k*v for v in p])
def sub(p,q):return add(p,scale(q,-1))
def mul(*ps):
 q=[1]
 for p in ps:
  z=[0]*(len(q)+len(p)-1)
  for i,u in enumerate(q):
   for j,v in enumerate(p):z[i+j]+=u*v
  q=trim(z)
 return q

def fourier(p):
 q=[0]*len(p)
 for k,v in enumerate(p):
  for n in range(k%2,k+1,2):q[n]+=v*comb(k,(k-n)//2)
 return trim(q)
def at(p,n):return p[abs(n)] if abs(n)<len(p) else 0
def defect(p,n):return at(p,n)**2-at(p,n-1)*at(p,n+1)-at(p,n+1)**2+at(p,n)*at(p,n+2)
def relative(p,q):
 a,b=fourier(p),fourier(q)
 return {(k,l):at(a,k)*at(b,l)-at(a,l)*at(b,k) for l in range(1,max(len(a),len(b))) for k in range(l)}
def rel_summary(p,q):
 arr=relative(p,q);nn=[(k,l,v) for (k,l),v in arr.items() if v<0];nonzero=[v for v in arr.values() if v]
 return {'selector_count':len(arr),'minimum_nonzero':min(nonzero) if nonzero else None,'first_negative':{'columns':nn[0][:2],'character':[sum(nn[0][:2])-1,nn[0][1]-nn[0][0]-1],'value':nn[0][2]} if nn else None}
XVAR=[0,1];YVAR=[1,1]
def state(a,e,r):
 X=add([1],mul(YVAR,a));Y=add(X,mul(YVAR,e));t=sub(scale(mul(YVAR,X),3),XVAR);A=sub(t,[2]);h=sub(t,[1]);k=mul(X,sub(scale(X,3),[2]))
 g=add(mul(A,e),k,r);s=sub(mul(t,g),r);C=add(Y,mul(YVAR,g));T=sub(scale(mul(YVAR,C),3),XVAR);M=add(T,[1]);E,G,R,S=[mul(YVAR,v) for v in (e,g,r,s)];Q=sub(S,G);D=mul(E,M);H=sub(G,mul(A,E));B=sub(T,t);K=add(mul(M,H),mul(B,S))
 return dict(a=a,e=e,r=r,X=X,Y=Y,t=t,A=A,h=h,k=k,g=g,s=s,C=C,T=T,M=M,E=E,G=G,R=R,S=S,Q=Q,D=D,H=H,B=B,K=K)
def short(st):return state(st['a'],add(st['e'],st['g']),st['g'])
def long(st):return state(add(st['a'],st['e']),st['g'],add(st['e'],st['g']))
def canonical(path):
 st=state([0],[1],[1])
 for c in path:st=(short if c=='S' else long)(st)
 return st

def fricke(st):return sub(mul(st['r'],st['g']),add(mul(st['A'],st['e'],st['e']),scale(mul(st['k'],st['e']),2),scale(mul(st['a'],st['X'],st['X']),3)))
def run():
 out=[]
 # Seven low-degree states select both retention/new-origin choices plus
 # fixed-endpoint iterate SSS. This is a bounded diagnostic, not broad scan.
 for path in ('','S','L','SS','SL','LS','LL','SSS'):
  st=canonical(path);ch=short(st)
  assert fricke(st)==[0]
  assert ch['D']==add(mul(st['h'],st['D']),st['K'])
  assert ch['Q']==add(mul(st['h'],st['Q']),mul(st['A'],st['G']))
  assert all(min(st[k])>=0 for k in ('a','e','r','g','s'))
  d=rel_summary(mul(st['h'],st['D']),ch['D']);q=rel_summary(ch['Q'],ch['D'])
  out.append({'path':path or 'ROOT','parent_degree_Q':len(st['Q'])-1,'child_degree_Q':len(ch['Q'])-1,'canonical_Fr icke_residual'.replace(' ',''):fricke(st),'central_A':defect(fourier(st['A']),0),'D_advance':d,'actual_short_Q_D':q,'complete_parent_P0_certificate':path in ('','S','L'),'P0_status':'ROOT/first-level inherited stronger certificates' if path in ('','S','L') else 'not asserted; continuum packets not certified by this replay'})
 return {'scope':'Independent exact arithmetic; proposed hD<=Dprime only; finite passing examples do not prove closure','records':out}
if __name__=='__main__':
 result=run();(HERE/'falsification_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
