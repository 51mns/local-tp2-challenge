#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb
from itertools import product
import json
from pathlib import Path

def clean(p): return {k:v for k,v in p.items() if v}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def sc(p,c): return clean({k:v*c for k,v in p.items()})
def mul(p,q):
 out={}
 for i,a in p.items():
  for j,b in q.items():out[i+j]=out.get(i+j,0)+a*b
 return clean(out)
def power(p,n):
 out={0:1}
 for _ in range(n):out=mul(out,p)
 return out
def divy(p):
 d=max(p); q={};last=0
 for j in range(d):
  last=p.get(j,0)-last
  if last:q[j]=last
 assert p.get(d,0)==last
 return q
def laur(p):
 out={}
 for k,v in p.items():out=add(out,sc(power({1:1,-1:1},k),v))
 return out
def half(p):
 h=laur(p);return [h.get(i,0) for i in range(max(h)+1)]
def get(h,i):return h[abs(i)] if abs(i)<len(h) else 0
def delta(h,i):return get(h,i)**2-get(h,i-1)*get(h,i+1)-get(h,i+1)**2+get(h,i)*get(h,i+2)
def W(p,q,n):
 h,j=half(p),half(q)
 return get(h,n)*get(j,n+1)-get(h,n+1)*get(j,n)
def mass(p):return sum(v*2**i for i,v in p.items())
def stateR(a,c,b):return c,add(sc(mul(mul(y,c),b),3),sc(mul(x,add(c,b)),-1),sc(a,-1)),b

x={1:1};y={0:1,1:1};one={0:1};p1={0:2,1:1}
def step(a,c,b,direction):
 if direction=='L':return a,add(sc(mul(mul(y,a),c),3),sc(mul(x,add(a,c)),-1),sc(b,-1)),c
 return c,add(sc(mul(mul(y,b),c),3),sc(mul(x,add(b,c)),-1),sc(a,-1)),b
a,c,b=one,{0:5,1:6,2:2},p1
for direction in 'LRR':a,c,b=step(a,c,b,direction)
X,Y,C0=a,b,c
tau=add(sc(mul(y,X),3),sc(x,-1))
T=add(mul(tau,Y),sc(mul(x,X),-1),sc(C0,-1))
A=divy(add(C0,sc(Y,-1)));B=divy(add(T,sc(Y,-1)))
M0=add(sc(mul(y,Y),3),sc(x,-1),one)
Pi=mul(X,p1);f=mul(y,add(tau,{0:-2}));g=sc(mul(power(y,2),Pi),3);K=mul(Pi,M0)
# Parametric polynomials: (Laurent exponent, parameter-degree tuple).
def lift(p,n):return {(k,(0,)*n):v for k,v in laur(p).items()}
def padd(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def psc(p,c):return clean({k:v*c for k,v in p.items()})
def pmul(p,q):
 out={}
 for (i,a),c in p.items():
  for (j,b),d in q.items():
   key=(i+j,tuple(x+y for x,y in zip(a,b)));out[key]=out.get(key,0)+c*d
 return clean(out)
def shifted(n,var):
 out=lift(add(tau,{0:-2}),n);key=[0]*n;key[var]=1;out[0,tuple(key)]=4;return out
def prow(p,j):return {a:v for (i,a),v in p.items() if i==abs(j)}
def rmul(p,q):
 out={}
 for a,c in p.items():
  for b,d in q.items():
   key=tuple(x+y for x,y in zip(a,b));out[key]=out.get(key,0)+c*d
 return clean(out)
def radd(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return clean(out)
def rsc(p,c):return clean({k:v*c for k,v in p.items()})
def pdelta(p,j):
 a,b,c,d=(prow(p,i) for i in [j,j-1,j+1,j+2])
 return radd(rmul(a,a),rsc(rmul(b,c),-1),rsc(rmul(c,c),-1),rmul(a,d))
def pmass(p):
 out={}
 for (i,a),v in p.items():out[a]=out.get(a,0)+v
 return clean(out)
def bern(p,degs):
 out=[]
 for idx in product(*(range(d+1) for d in degs)):
  s=F(0)
  for a,c in p.items():
   if all(a[k]<=idx[k] for k in range(len(degs))):
    f=F(c)
    for k in range(len(degs)):f*=F(comb(idx[k],a[k]),comb(degs[k],a[k]))
    s+=f
  out.append(s)
 return out

def penc(a):return [str(z) for z in a]
def pkentry(p,i,j):
 if i==0:return prow(p,j)
 if j==0:return rsc(prow(p,i),2)
 return radd(prow(p,abs(i-j)),prow(p,i+j))
def pkminor(p,a,n):
 return radd(rmul(pkentry(p,a,n),pkentry(p,a+1,n+1)),rsc(rmul(pkentry(p,a,n+1),pkentry(p,a+1,n)),-1))
result={'audit':'shared-session independent implementation; no author implementation or expected JSON imported', 'base':{name:[v.get(j,0) for j in range(max(v)+1)] for name,v in [('X',X),('Y',Y),('C0',C0),('T',T),('A',A),('B',B),('t',tau),('M0',M0),('f',f),('g',g),('K',K)]},'kernel_checks':{},'template_minor_mass':[],'smoothed_template_mass':[]}
for name,p in [('A',A),('B',B),('yA',mul(y,A)),('q2',mul(y,add(mul(A,add(power(tau,2),{0:-1})),mul(B,tau))))]:
 h=half(p);ds=[delta(h,j) for j in range(len(h))];assert min(ds)>0
 result['kernel_checks'][name]={'minimum':min(ds),'all_defects':ds}
for kind,n in [('t',1),('L',1),('H',3)]:
 if kind=='t':poly=shifted(1,0)
 if kind=='L':poly=padd(pmul(lift(A,1),shifted(1,0)),lift(B,1))
 if kind=='H':poly=padd(pmul(pmul(lift(A,3),shifted(3,0)),shifted(3,1)),pmul(lift(B,3),shifted(3,2)))
 for smooth in ([0] if kind=='H' else [0,1]):
  pp=pmul(poly,lift(y,n)) if smooth else poly
  lam=128 if kind=='H' else 0
  deg=max(k for k,a in pp)
  arrays=[bern(radd(pdelta(pp,j),rsc(prow(pp,j),-lam)),[2]*n) for j in range(deg+1)]
  assert min(z for a in arrays for z in a)>0
  result['kernel_checks'][kind+('_y' if smooth else '')]={'degree':deg,'strength':lam,'minimum':str(min(z for a in arrays for z in a)),'all_bernstein_arrays':[penc(a) for a in arrays]}
L=padd(pmul(lift(A,1),shifted(1,0)),lift(B,1))
trace=shifted(1,0)
trace_arr=bern(radd(pdelta(trace,0),rsc(pmass(trace),-435)),[2]);assert min(trace_arr)>=0
result['trace_mass']={'bernstein':penc(trace_arr),'A2':mass(A),'B2':mass(B),'t2':mass(tau),'mass_upper_L':mass(A)*(mass(tau)+2)+mass(B)}
assert mass(B)<mass(A)*(mass(tau)-2)
alphas=[169642463,2064106360,2831195954,2384116463,1904306391,1741592332,1716888939,1715350492,1715324201,1545681738,1129953741]
betas=[9257671245,23253961033,27139331618,22199966965,13865402773]
yyL=pmul(L,lift(power(y,2),1))
m0=half(M0)
for n,beta in enumerate(betas):
 arr=bern(radd(pdelta(yyL,n),rsc(pmass(L),-beta)),[2]);assert min(arr)>=0
 surplus=beta-6*(get(m0,n-1)+3*get(m0,n+1));assert surplus>0
 result['smoothed_template_mass'].append({'n':n,'beta':beta,'bernstein':penc(arr),'multiplier_surplus':surplus})
w=[W(f,g,n) for n in range(max(f)+1)];assert min(w)>0
kh=half(K)
for n,alpha in enumerate(alphas):
 i=min(n,max(f));arr=bern(radd(pkminor(L,i,n),rsc(pmass(L),-alpha)),[2]);assert min(arr)>=0
 surplus=w[i]*alpha-2*mass(f)*get(kh,n);assert surplus>0
 result['template_minor_mass'].append({'n':n,'row':i,'alpha':alpha,'bernstein':penc(arr),'proxy_surplus':surplus})
result['fixed_proxy']={'w':w,'f2':mass(f),'K_halfrow':kh,'degrees':[max(f),max(g),max(K)]}
q0=mul(y,A);q1=mul(y,add(mul(A,tau),B));betaPoly=mul(y,add(A,B));E=add(C0,sc(X,-1))
result['initial_lr']={}
for name,p,q in [('q0q1',q0,q1),('betaq1',betaPoly,q1),('PiE',Pi,E),('Piq1',Pi,q1)]:
 ds=[W(p,q,n) for n in range(max(p)+1)];assert min(ds)>0;result['initial_lr'][name]=ds
assert betaPoly==add(mul(add(tau,{0:-2}),Y),sc(mul(x,X),-1))
C1=step(X,C0,Y,'L')[1]
assert add(C1,sc(C0,-1))==q1
origL=step(X,C0,Y,'L')[1];origR=step(X,C0,Y,'R')[1]
assert max(origR)==12 and max(origL)==16
S0=add(origR,sc(C0,-1));D0=add(origL,sc(origR,-1));F0=[W(S0,D0,n) for n in range(max(S0)+1)];assert min(F0)>0
result['ell_zero']={'short_degree':max(origR),'long_degree':max(origL),'F':F0,'minimum':min(F0)}
result['verdict']='PASS finite continuum certificates; analytical assembly reviewed separately in LRR_AUDIT.md'
path=Path(__file__).with_name('lrr_independent_results.json');path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'verdict':result['verdict'],'kernel_minima':{k:v['minimum'] for k,v in result['kernel_checks'].items()},'trace_mass_bernstein':penc(trace_arr),'smoothed_surpluses':[r['multiplier_surplus'] for r in result['smoothed_template_mass']], 'proxy_surpluses':[r['proxy_surplus'] for r in result['template_minor_mass']], 'ell_zero_min':min(F0),'output':str(path)},indent=2))
