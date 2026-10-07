#!/usr/bin/env python3
"""Self-contained exact Laurent audit of the selective exterior obstruction.
No parent arithmetic is imported. Finite checks are examples, not all-tree proofs.
"""
import json
from pathlib import Path

def add(a,b):
 z=dict(a)
 for i,v in b.items():z[i]=z.get(i,0)+v
 return {i:v for i,v in z.items() if v}
def neg(a):return {i:-v for i,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z={}
 for i,u in a.items():
  for j,v in b.items():z[i+j]=z.get(i+j,0)+u*v
 return {i:v for i,v in z.items() if v}
def scale(a,k):return {i:k*v for i,v in a.items() if k*v}
O={0:1};Z={};X={-1:1,1:1};Y=add(O,X)
def ordinary(cs):
 z={};power=O
 for c in cs:z=add(z,scale(power,c));power=mul(power,X)
 return z

def mm(a,b):return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def mt(a):return [list(z) for z in zip(*a)]
def det(a):return sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
T=[[scale(Y,3),neg(O)],[O,Z]]
A0=[[O,Z],[neg(X),O]]
B0=[[ordinary([2,1]),Y],[O,O]]
def medi(a,b):return mm(mm(mt(a),T),mt(b))
def half(a):
 assert all(a.get(i,0)==a.get(-i,0) for i in a)
 return [a.get(i,0) for i in range(max(a,default=0)+1)]
def get(h,i):return h[abs(i)] if abs(i)<len(h) else 0
def kernel(h,i,j):
 if i==0:return get(h,j)
 if j==0:return 2*get(h,i)
 return get(h,i-j)+get(h,i+j)
def wedge(h,k,n):return get(h,n)*get(k,n+1)-get(h,n+1)*get(k,n)
def defects(h):return [get(h,n)**2-get(h,n-1)*get(h,n+1)-get(h,n+1)**2+get(h,n)*get(h,n+2) for n in range(len(h))]
def state(Q):
 G,s,d=Q[0][0],Q[1][0],Q[1][1];r=sub(G,s);t=sub(scale(mul(Y,G),3),X)
 return G,s,r,d,sub(t,s),add(t,r)
def audit_pair(A,B,path):
 C=medi(A,B)
 GA,sA,rA,dA,_,_=state(A);GB,_,_,_,UB,_=state(B)
 a,b,c,d=sub(rA,X),sub(sA,dA),add(sA,X),dA
 N=[[a,b],[c,d]]
 assert det(A)==det(B)==det(C)==det(N)==O
 assert C[0][1]==add(C[1][0],X)
 rC=add(mul(a,UB),mul(b,GB));sC=add(mul(c,UB),mul(d,GB))
 assert rC==sub(C[0][0],C[1][0]) and sC==C[1][0]
 ha,hb,hc,hd=map(half,[a,b,c,d]);u,g=half(UB),half(GB)
 output_s,output_r=half(sC),half(rC);all_terms=[];category={}
 def source(kind,i,j,coef,weight):
  all_terms.append(dict(kind=kind,i=i,j=j,coefficient=coef,weight=weight,contribution=coef*weight))
  category[kind]=category.get(kind,0)+coef*weight
 def polar(h,k,i,j,n):
  z=kernel(h,i,n)*kernel(k,j,n+1)-kernel(h,i,n+1)*kernel(k,j,n)
  if i!=j:z+=kernel(h,j,n)*kernel(k,i,n+1)-kernel(h,j,n+1)*kernel(k,i,n)
  return z
 for i in range(len(u)):
  for j in range(i,len(u)):source('UU',i,j,polar(hc,ha,i,j,0),u[i]*u[j])
 for i in range(len(g)):
  for j in range(i,len(g)):source('GG',i,j,polar(hd,hb,i,j,0),g[i]*g[j])
 for i in range(len(u)):
  for j in range(len(g)):
   coef=kernel(hc,i,0)*kernel(hb,j,1)-kernel(hc,i,1)*kernel(hb,j,0)+kernel(hd,j,0)*kernel(ha,i,1)-kernel(hd,j,1)*kernel(ha,i,0)
   source('UG',i,j,coef,u[i]*g[j])
 assert sum(z['contribution'] for z in all_terms)==wedge(output_s,output_r,0)
 m=len(hc)-1;tail_i=m+1
 tail_coef=polar(hc,ha,tail_i,tail_i,0)
 assert tail_coef==-2*hc[m]*ha[tail_i]
 return dict(actual_child=path,N_halfrows=dict(a=ha,b=hb,c=hc,d=hd),input_halfrows=dict(U=u,G=g),output_halfrows=dict(s=output_s,r=output_r),output_adjacent_minors=[wedge(output_s,output_r,n) for n in range(len(output_r)-1)],central_category_sums=category,central_source_terms=all_terms,tail_diagonal_obstruction=dict(i=tail_i,coefficient=tail_coef,input_mass=get(u,tail_i),contribution=tail_coef*get(u,tail_i)**2),all_canonical_det_one_and_skew_verified=True)

def run():
 root=medi(A0,B0)
 root_state=state(root)
 root_rows={k:half(v) for k,v in zip(['G','s','r','d','u','v'],root_state)}
 root_cones={k:defects(root_rows[k]) for k in ['s','r','u','v']}
 root_pairs={a+'_lr_'+b:[wedge(root_rows[a],root_rows[b],n) for n in range(max(len(root_rows[a]),len(root_rows[b]))-1)] for a,b in [('s','r'),('v','u')]}
 result=dict(root_rows=root_rows,root_folded_defects=root_cones,root_adjacent_minors=root_pairs,right_child=audit_pair(root,B0,'R'),scope='exact actual-canonical obstruction; no all-tree Local TP2 claim',imports='none; direct sparse Laurent arithmetic')
 assert result['right_child']['tail_diagonal_obstruction']==dict(i=2,coefficient=-8,input_mass=3,contribution=-72)
 assert result['right_child']['central_category_sums']==dict(UU=180,GG=2,UG=89)
 assert result['right_child']['output_adjacent_minors'][0]==271
 target=Path(__file__).with_name('network_exterior_results.json');target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':run()
