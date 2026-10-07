#!/usr/bin/env python3
"""Exact actual first-short Cassini projection; no additional tree scans.
Independent Clebsch--Gordan construction; no proxy curvature code imported.
"""
import importlib.util,json
from pathlib import Path
helper=Path(__file__).resolve().parent.parent/'common_closure_20261004'/'network_exterior_reproducer.py'
spec=importlib.util.spec_from_file_location('frozen_network_laurent',helper)
l=importlib.util.module_from_spec(spec);spec.loader.exec_module(l)

def ca(a,b):
 z=dict(a)
 for i,v in b.items():z[i]=z.get(i,0)+v
 return {i:v for i,v in z.items() if v}
def cs(a,k):return {i:v*k for i,v in a.items() if v*k}
def cm(a,b):
 z={}
 for (i,j),v in a.items():
  for (k,m),w in b.items():
   for n in range(abs(i-k),i+k+1,2):
    for p in range(abs(j-m),j+m+1,2):z[n,p]=z.get((n,p),0)+v*w
 return {i:v for i,v in z.items() if v}
def divided(p):return {(j-1,j-1):v for j,v in enumerate(l.half(p)) if j and v}
def curv(r,g,s):return ca(cm(divided(g),divided(g)),cs(cm(divided(r),divided(s)),-1))
def rawchildren(X,Y,C):
 U=l.sub(l.sub(l.scale(l.mul(l.Y,l.mul(X,C)),3),l.mul(l.X,l.add(X,C))),Y)
 V=l.sub(l.sub(l.scale(l.mul(l.Y,l.mul(Y,C)),3),l.mul(l.X,l.add(Y,C))),X)
 assert max(U)<max(V)
 return U,V
def base(X,Y,C):
 U,V=rawchildren(X,Y,C);E=l.sub(Y,X);G=l.sub(C,Y);t=l.sub(l.scale(l.mul(l.Y,X),3),l.X)
 S=l.sub(U,C);D=l.sub(V,U);R=l.sub(l.mul(t,G),S);M=l.add(l.sub(l.scale(l.mul(l.Y,C),3),l.X),l.O);Q=l.sub(S,G)
 Pi=l.mul(l.mul(X,l.ordinary([2,1])),M)
 return dict(X=X,Y=Y,C=C,E=E,G=G,R=R,t=t,S=S,D=D,F=l.add(S,D),M=M,Q=Q,Pi=Pi)
def ordered(p,q):
 a,b=l.half(p),l.half(q);N=max(len(a),len(b));z={}
 for i in range(N):
  for j in range(i+1,N):
   v=l.get(a,i)*l.get(b,j)-l.get(a,j)*l.get(b,i)
   if not v:continue
   z[i+j-1,j-i-1]=z.get((i+j-1,j-i-1),0)+v
   if i:z[j-i-1,i+j-1]=z.get((j-i-1,i+j-1),0)+v
 return {i:v for i,v in z.items() if v}
def adjacent(p,q):
 a,b=l.half(p),l.half(q)
 return [l.wedge(a,b,n) for n in range(len(a))]
def jsonchars(a):return {str(i)+','+str(j):v for (i,j),v in sorted(a.items())}
def run():
 P=l.ordinary([2,1]);root=base(l.O,P,l.ordinary([5,6,2]));child=base(root['X'],root['C'],l.add(root['C'],root['S']))
 R,G,S,E,F=map(child.get,['R','G','S','E','F'])
 kx=curv(R,G,S);ky=curv(l.sub(R,E),l.add(G,E),F)
 assert all(v>=0 for v in kx.values()) and all(v>=0 for v in ky.values())
 # Independently verify every regular current-state gate.
 for a,b in [(E,G),(R,G),(l.mul(child['X'],P),E),(l.mul(child['Y'],P),G)]:assert all(v>=0 for v in ordered(a,b).values())
 assert all(v>=0 for v in l.defects(l.half(G))) and all(v>=0 for v in l.defects(l.half(child['M'])))
 assert all(v>0 for v in adjacent(child['Q'],child['Pi']))
 K=l.sub(l.mul(G,G),l.mul(R,S));hk=l.half(K);assert hk==[3,2,1]
 L={(2,2):1,(2,0):-3,(0,2):-3,(0,0):9}
 correction=cs(cm(L,kx),-1)
 N=max(len(l.half(G)),max((i//2 for i,j in correction if j==0),default=0)+1)
 b=[kx.get((2*n,0),0) for n in range(N+1)]
 c=[kx.get((2*n,2),0) for n in range(N+1)]
 a=[c[n]-3*b[n] for n in range(N+1)]
 closed=[3*a[0]-a[1]]+[2*a[n]-a[n-1]-a[n+1] for n in range(1,N)]
 actual=[correction.get((2*n,0),0) for n in range(N)]
 assert closed==actual==[-245,43,-44,48]
 mixed=[l.defects(l.half(l.add(R,S)))[n]- (l.defects(l.half(R))[n] if n<len(l.half(R)) else 0)- (l.defects(l.half(S))[n] if n<len(l.half(S)) else 0) for n in range(N)]
 sigma=[2*hk[0]+hk[2],-hk[2]]+[0]*(N-2)
 delta=l.defects(l.half(G));assert delta==[192,256,112,16]
 assert [mixed[n]+sigma[n]+actual[n] for n in range(N)]==[2*v for v in delta]
 assert kx==ca(curv(root['R'],root['G'],root['S']),cm(divided(root['t']),ordered(root['G'],root['S'])))
 out=dict(scope='Exact actual first-short witness only, not gap or target failure.',actual_state='first degree-ordered short child',regular_P_Q_verified=True,both_curvatures_nonnegative=True,kappa_X=jsonchars(kx),kappa_Y_terms=len(ky),kappa_X_boundary0=b,kappa_X_boundary2=c,a_boundary=c and a,signed_Cassini_correction=actual,mixed_J_R_S_boundary=mixed,Sigma_K_boundary=sigma,twice_gap_defects=[2*v for v in delta],negative_correction_indices=[n for n,v in enumerate(actual) if v<0],imports=[str(helper)+' (sparse Laurent arithmetic only)'])
 Path(__file__).with_name('gap_curvature_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
