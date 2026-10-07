"""Separate direct Laurent / symbolic-parameter reconstruction.
No import of the author implementation or saved expected certificates.
"""
from fractions import Fraction
from math import comb
from itertools import product
from pathlib import Path
import json,sys

# Univariate Laurent arithmetic, negative exponents retained throughout.
def plus(*parts):
 d={}
 for p in parts:
  for k,v in p.items():d[k]=d.get(k,0)+v
 return {k:v for k,v in d.items() if v}
def times(p,q):
 d={}
 for i,a in p.items():
  for j,b in q.items():d[i+j]=d.get(i+j,0)+a*b
 return {k:v for k,v in d.items() if v}
def sc(p,c):return {k:c*v for k,v in p.items() if c*v}
I={0:1};X={-1:1,1:1};Y=plus(I,X);P=plus({0:2},X)
def mutation(a,c,b):return plus(sc(times(times(Y,a),c),3),sc(times(X,plus(a,c)),-1),sc(b,-1))
def make_state(word):
 a,c,b=I,plus({0:5},sc(X,6),sc(times(X,X),2)),P
 for move in word:
  if move=='L':a,c,b=a,mutation(a,c,b),c
  else:a,c,b=c,mutation(b,c,a),b
 return a,c,b
def div_y(poly):
 # Long division in the Laurent ring; divisibility fixes all coefficients.
 f=dict(poly);out={}
 lower=min(poly,default=0)+2
 while f and max(f)>=lower:
  e=max(f)-1;v=f[max(f)];out[e]=out.get(e,0)+v
  f=plus(f,sc({e-1:1,e:1,e+1:1},-v))
 assert not f,('not divisible',f)
 assert all(out.get(-i,0)==v for i,v in out.items())
 return out

def at(poly,n):return poly.get(n,0)
def row(poly):
 d=max(poly,default=0);return tuple(poly.get(j,0) for j in range(d+1))
def reflect(h,j):return h[abs(j)] if abs(j)<len(h) else 0
def defect(h,n):return reflect(h,n)**2-reflect(h,n-1)*reflect(h,n+1)-reflect(h,n+1)**2+reflect(h,n)*reflect(h,n+2)
def detpair(a,b,n):return at(a,n)*at(b,n+1)-at(a,n+1)*at(b,n)

# Polynomials in u,v. r=4u-2 and s=4v-2; expressions expanded symbolically.
def pp_add(*polys):
 out={}
 for poly in polys:
  for k,v in poly.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v}
def pp_scale(poly,s):return {k:s*v for k,v in poly.items() if s*v}
def pp_mul(p,q):
 out={}
 for (i,j),a in p.items():
  for (k,l),b in q.items():out[i+k,j+l]=out.get((i+k,j+l),0)+a*b
 return {k:v for k,v in out.items() if v}
def cc(n):return {(0,0):n} if n else {}
def hp(h,n):return h[abs(n)] if abs(n)<len(h) else {}
def symbolic_defect(h,n):
 a,b,c,d=hp(h,n-1),hp(h,n),hp(h,n+1),hp(h,n+2)
 return pp_add(pp_mul(b,b),pp_scale(pp_mul(a,c),-1),pp_scale(pp_mul(c,c),-1),pp_mul(b,d))
def bs(poly,dim):
 assert all(i<=2 and j<=2 for i,j in poly),(dim,poly)
 indices=product(range(3),repeat=dim)
 out=[]
 for idx in indices:
  ii=idx[0];jj=idx[1] if dim==2 else 0
  out.append(sum(Fraction(val*comb(ii,a)*comb(jj,b),comb(2,a)*comb(2,b)) for (a,b),val in poly.items() if a<=ii and b<=jj))
 return out

def symbolic_row(coeffs):
 # coeffs maps parameter exponents to a full Laurent polynomial.
 d=max(max(v,default=0) for v in coeffs.values())
 return [{k:v.get(n,0) for k,v in coeffs.items() if v.get(n,0)} for n in range(d+1)]
def sk(h,i,j):
 if i==0:return hp(h,j)
 if j==0:return pp_scale(hp(h,i),2)
 return pp_add(hp(h,i-j),hp(h,i+j))
def sd(h,i,j,a,b):return pp_add(pp_mul(sk(h,i,a),sk(h,j,b)),pp_scale(pp_mul(sk(h,i,b),sk(h,j,a)),-1))
def smass(h):return pp_add(h[0],*(pp_scale(a,2) for a in h[1:]))

def run(word,direction):
 a,c,b=make_state(word)
 if direction=='R':a,b=b,a
 trace=plus(sc(times(Y,a),3),sc(X,-1))
 inverse=plus(times(trace,b),sc(times(X,a),-1),sc(c,-1))
 seed=div_y(plus(c,sc(b,-1)));B=div_y(plus(inverse,sc(b,-1)))
 sign=-1 if all(v<=0 for v in B.values()) else 1
 assert all(sign*v>=0 for v in B.values())
 Q=sc(B,sign)
 assert all(at(seed,i)>=at(Q,i) for i in range(max(max(seed),max(Q,default=0))+1))
 plus_trace=plus(trace,{0:2})
 f=symbolic_row({(0,0):plus_trace,(1,0):{0:-4}})
 Lcoeff={(0,0):plus(times(seed,plus_trace),B),(1,0):sc(seed,-4)}
 L=symbolic_row(Lcoeff)
 Hcoeff={(0,0):plus(times(times(seed,plus_trace),plus_trace),times(B,plus_trace)),(1,0):plus(sc(times(seed,plus_trace),-4),sc(B,-2)),(0,1):plus(sc(times(seed,plus_trace),-4),sc(B,-2)),(1,1):sc(seed,16)}
 HH=symbolic_row(Hcoeff)
 yL=symbolic_row({k:times(Y,v) for k,v in Lcoeff.items()})
 yHH=symbolic_row({k:times(Y,v) for k,v in Hcoeff.items()})
 y2L=symbolic_row({k:times(times(Y,Y),v) for k,v in Lcoeff.items()})
 certificates={}
 for name,h,form in [('trace_delta',f,'delta'),('trace_coeffs',f,'value'),('L_delta',L,'delta'),('yL_delta',yL,'delta'),('L_coeffs',L,'value')]:
  vals=[]
  for n in range(len(h)):vals+=bs(symbolic_defect(h,n) if form=='delta' else h[n],1)
  assert min(vals)>0,(name,min(vals))
  certificates[name]=vals
 tg=bs(pp_add(symbolic_defect(f,0),pp_scale(smass(f),-2)),1)
 assert min(tg)>0
 certificates['trace_gamma2']=tg
 for name,h,ref in [('H',HH,Q),('yH',yHH,times(Y,Q))]:
  refrow=row(ref);mm=max(refrow);strong=[];dom=[];support=[]
  for n in range(len(h)):
   strong+=bs(pp_add(symbolic_defect(h,n),pp_scale(h[n],-8*mm)),2)
   dom+=bs(pp_add(h[n],cc(-reflect(refrow,n))),2)
   support+=bs(h[n],2)
  assert min(strong)>0 and min(dom)>=0 and min(support)>0
  certificates[name+'_strong']=strong;certificates[name+'_domination']=dom;certificates[name+'_positive']=support
 # All fixed initial comparisons, reconstructed without author helper routines.
 q0=times(Y,seed);q1=times(Y,plus(times(trace,seed),B));beta=times(Y,plus(seed,B))
 E1=plus(c,sc(a,-1));PP=times(P,a);J=times(Y,plus(trace,{0:-2}));V=sc(times(times(Y,Y),PP),3)
 M0=plus(sc(times(Y,b),3),sc(X,-1),I);K=times(PP,M0)
 for lo,hi in [(q0,q1),(beta,q1),(PP,E1),(PP,q1)]:
  assert min(detpair(lo,hi,n) for n in range(max(lo)+1))>=0
 w=[detpair(J,V,n) for n in range(max(J)+1)]
 assert min(w)>0
 lm=bs(smass(L),1);alpha=[];betav=[]
 for n in range(max(K)+1):
  j=min(n,max(J));dets=bs(sd(L,j,j+1,n,n+1),1)
  alpha.append(min(d/m for d,m in zip(dets,lm))/2)
 for n in range(max(M0)+2):
  dets=bs(symbolic_defect(y2L,n),1)
  betav.append(min(d/m for d,m in zip(dets,lm))/2)
 assert min(alpha)>0 and min(betav)>0
 z1=sum(plus(times(seed,plus(trace,I)),B).values())
 ma=[Fraction(1,2)*w[min(n,max(J))]*al-sum(J.values())*at(K,n) for n,al in enumerate(alpha)]
 mb=[Fraction(9,2)*bv-27*(at(M0,n-1)+3*at(M0,n+1))-Fraction(max(-defect(row(M0),n),0),z1) for n,bv in enumerate(betav)]
 assert min(ma)>0 and min(mb)>0
 certificates.update(alphas=alpha,betas=betav,proxy_margins=ma,multiplier_margins=mb)
 # Verify the displayed universal sum identity at these inputs.
 ux=div_y(plus(a,sc(I,-1))) if a!=I else {}
 vy=div_y(plus(b,sc(I,-1))) if b!=I else {}
 rhs=plus(I,times(plus(sc(X,2),{0:3}),ux),times(plus(sc(X,2),I),vy),sc(times(times(times(Y,Y),ux),vy),3))
 assert plus(seed,B)==rhs
 A0,C0,B0=make_state(word);left=mutation(A0,C0,B0);right=mutation(B0,C0,A0)
 short,long=sorted([left,right],key=lambda p:max(p));S=plus(short,sc(C0,-1));D=plus(long,sc(short,-1))
 assert min(detpair(S,D,n) for n in range(max(S)+1))>0
 return {'word':word,'direction':direction,'B_sign':sign,'status':'PASS','certificates':{k:[str(v) for v in vv] for k,vv in certificates.items()},'prefix_F':[detpair(S,D,n) for n in range(max(S)+1)],'method':'direct Laurent multiplication; symbolic r=4u-2,s=4v-2; exact monomial-to-Bernstein conversion; no author import'}

if __name__=='__main__':
 w=sys.argv[1] if len(sys.argv)>1 else 'LRL';d=sys.argv[2] if len(sys.argv)>2 else 'R'
 result=run(w,d)
 target=Path(__file__).with_name(f'independent_{w}_{d}.json')
 target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(w,d,result['status'],'coefficients',sum(map(len,result['certificates'].values())))
