#!/usr/bin/env python3
"""Independent exact universal companion identities; bounded probes are not proofs."""
from math import comb
import json
from pathlib import Path

def norm(p):
 p=list(p)
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def add(*ps):
 out=[0]*max(map(len,ps))
 for p in ps:
  for i,v in enumerate(p):out[i]+=v
 return norm(out)

def scale(p,c):return norm([c*v for v in p])
def sub(p,q):return add(p,scale(q,-1))
def mul(*ps):
 out=[1]
 for p in ps:
  tmp=[0]*(len(out)+len(p)-1)
  for i,a in enumerate(out):
   for j,b in enumerate(p):tmp[i+j]+=a*b
  out=norm(tmp)
 return out

def divy(p):
 out=[0]*(len(p)-1)
 rem=list(p)
 for i in range(len(p)-2,-1,-1):out[i]=rem[i+1];rem[i]-=out[i]
 assert rem[0]==0
 return norm(out)

def H(p):
 out=[0]*len(p)
 for j,a in enumerate(p):
  for k in range(j//2+1):out[j-2*k]+=a*comb(j,k)
 return out

def hv(h,n):return h[abs(n)] if abs(n)<len(h) else 0

def W(p,q):
 h,b=H(p),H(q)
 return [hv(h,n)*hv(b,n+1)-hv(h,n+1)*hv(b,n) for n in range(max(len(h),len(b)))]

def defects(p):
 h=H(p)
 return [hv(h,n)**2-hv(h,n-1)*hv(h,n+1)-hv(h,n+1)**2+hv(h,n)*hv(h,n+2) for n in range(len(h))]

y=[1,1];P1=[2,1];z=[3,2];one=[1]

def rawchildren(X,Y,C):
 U=sub(sub(scale(mul(y,X,C),3),mul([0,1],add(X,C))),Y)
 V=sub(sub(scale(mul(y,Y,C),3),mul([0,1],add(Y,C))),X)
 assert len(U)<len(V)
 return (X,C,U),(Y,C,V)

def build(raw):
 X,Y,C=raw
 a=divy(sub(X,one)) if X!=one else [0]
 e=divy(sub(Y,X));g=divy(sub(C,Y))
 t=sub(scale(mul(y,X),3),[0,1]);k=mul(X,sub(scale(X,3),[2]))
 r=sub(sub(g,mul(sub(t,[2]),e)),k)
 R=mul(y,r);E=sub(Y,X);G=sub(C,Y)
 S=sub(mul(t,G),R);M=add(scale(mul(y,C),3),[1,-1]);D=mul(E,M)
 Z=add(a,e,g);J=mul(y,sub(t,[2]));B=sub(mul(z,X),P1);T=add(G,B)
 Q=sub(S,G);U=mul(X,P1,M);V=add(mul(P1,X),mul(P1,P1,C))
 assert Q==sub(mul(sub(t,[2]),C),mul([0,1],X))
 assert U==add(mul(P1,Q),V)
 wqu,wqv,dq=W(Q,U),W(Q,V),defects(Q)
 assert wqu==[hv(dq,n)+hv(wqv,n) for n in range(len(wqu))]
 assert sub(S,mul(J,Z))==T
 assert T==mul(y,add(mul(sub(t,[2]),sub(e,a)),scale(k,2),r))
 assert B==mul(y,add(one,mul(z,a)))
 assert M==add(scale(P1,2),scale(mul(y,y,Z),3))
 assert mul(r,g)==add(mul(sub(t,[2]),e,e),scale(mul(k,e),2),scale(mul(a,X,X),3))
 return dict(X=X,Y=Y,C=C,a=a,e=e,g=g,r=r,t=t,k=k,R=R,E=E,G=G,S=S,M=M,D=D,Z=Z,J=J,B=B,T=T,Q=Q,U=U,V=V)

def check_transport(st,raw):
 for name,child in zip(('short','long'),rawchildren(*raw)):
  sn=build(child);A=st['t'];S=st['S'];D=st['D'];G=st['G'];E=st['E'];B=st['B'];M=st['M'];U=st['U'];X=st['X'];Y=st['Y']
  if name=='short':
   assert sn['E']==add(E,G) and sn['G']==S and sn['R']==G
   assert sn['t']==A and sn['B']==B and sn['S']==sub(mul(A,S),G)
   assert sn['M']==add(M,scale(mul(y,S),3))
   assert sn['Q']==sub(mul(sub(A,one),S),G)
   assert sn['U']==add(U,scale(mul(y,X,P1,S),3))
   assert sn['Q']==add(st['Q'],mul(sub(A,[2]),S))
   assert sn['V']==add(st['V'],mul(P1,P1,S))
  else:
   tp=add(A,scale(mul(y,E),3));F=add(S,D)
   assert sn['E']==G and sn['G']==F and sn['R']==add(E,G)
   assert sn['t']==tp and sn['B']==add(B,mul(z,E))
   assert sn['S']==sub(mul(tp,F),add(E,G))
   assert sn['M']==add(M,scale(mul(y,F),3))
   assert sn['Q']==sub(mul(sub(tp,one),F),add(E,G))
   assert sn['U']==add(U,mul(P1,D),scale(mul(y,Y,P1,F),3))
   assert sn['Q']==add(st['Q'],mul(sub(A,[2]),F),mul(E,add(sub(M,one),scale(mul(y,F),3))))
   assert sn['V']==add(st['V'],mul(P1,E),mul(P1,P1,F))
  assert sn['Z']==add(st['Z'],divy(sn['G']))

def run(depth=5):
 stack=[('',([1],[2,1],[5,6,2]))];fail={};count=0;root=None
 pairs=[('T','S'),('Q','U'),('G','S'),('R','G'),('E','G')]
 while stack:
  path,raw=stack.pop();st=build(raw);check_transport(st,raw);count+=1
  tests={f'lr_{u}_{v}':W(st[u],st[v]) for u,v in pairs}
  tests['lr_XP1_E']=W(mul(st['X'],P1),st['E'])
  tests['lr_YP1_G']=W(mul(st['Y'],P1),st['G'])
  tests['lr_CP1_S']=W(mul(st['C'],P1),st['S'])
  tests['proxy_JZ_U']=W(mul(st['J'],st['Z']),st['U'])
  tests.update({f'cone_{u}':defects(st[u]) for u in ('G','M','Z')})
  if not path:root={key:val for key,val in tests.items()}
  for key in ('lr_Q_U','proxy_JZ_U'):
   if min(tests[key][:len(st['Q'])])<=0:
    v=min(tests[key][:len(st['Q'])]);fail.setdefault('strict_'+key,dict(path=path,index=tests[key].index(v),value=v))
  for key,val in tests.items():
   if min(val)<0:fail.setdefault(key,dict(path=path,index=val.index(min(val)),value=min(val)))
  if len(path)<depth:
   for name,child in reversed(list(zip(('s','l'),rawchildren(*raw)))):stack.append((path+name,child))
 return dict(scope='Bounded exact tests only; no closure theorem',nodes=count,depth=depth,fails=fail,root=root)

if __name__=='__main__':
 import sys
 result=run(int(sys.argv[1]) if len(sys.argv)>1 else 5)
 dest=Path(__file__).with_name('reduction_common_results.json');dest.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
