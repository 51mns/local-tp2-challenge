#!/usr/bin/env python3
"""Exact finite character certificate for ALL ordered folded relative minors.
Self-contained integer/Fraction arithmetic. General proof is in the note;
finite identity checks below only validate normalization/implementation.
"""
from math import comb
from fractions import Fraction
import json
from pathlib import Path

def trim(p):
 p=list(p)
 while len(p)>1 and not p[-1]:p.pop()
 return p

def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(p,c):return trim([v*c for v in p])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):z[i+j]+=u*v
 return trim(z)
def H(p):return trim([sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2)) for n in range(len(p))])
def hv(h,n):return h[abs(n)] if abs(n)<len(h) else 0
def xrow(h):return trim([hv(h,n-1)+hv(h,n+1) for n in range(len(h)+1)])
def cp_add(a,b):
 z=dict(a)
 for k,v in b.items():z[k]=z.get(k,0)+v
 return {k:v for k,v in z.items() if v}
def cp_scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def cp_mul(a,b):
 z={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():
   for n in range(abs(i-k),i+k+1,2):
    for m in range(abs(j-l),j+l+1,2):z[n,m]=z.get((n,m),0)+v*w
 return {k:v for k,v in z.items() if v}
def R_rows(h,q):
 z={};N=max(len(h),len(q))
 for i in range(N):
  for j in range(i+1,N):
   w=hv(h,i)*hv(q,j)-hv(h,j)*hv(q,i)
   if not w:continue
   k=(i+j-1,j-i-1);z[k]=z.get(k,0)+w
   if i:
    k=(j-i-1,i+j-1);z[k]=z.get(k,0)+w
 return {k:v for k,v in z.items() if v}
def tensor_from_halfrow(h):return R_rows(h,xrow(h))
def tensor(f):return tensor_from_halfrow(H(f))
def mixed_tensor(f,g):return cp_add(cp_add(tensor(add(f,g)),cp_scale(tensor(f),-1)),cp_scale(tensor(g),-1))
def kernel(h,i,j):
 if i==0:return hv(h,j)
 if j==0:return 2*hv(h,i)
 return hv(h,i-j)+hv(h,i+j)
def minor(h,i,j,k,l):return kernel(h,i,k)*kernel(h,j,l)-kernel(h,i,l)*kernel(h,j,k)
def cosine_character(i,j):
 assert 0<=i<j
 if i==0:return {(j-1,j-1):1}
 return {(i+j-1,j-i-1):1,(j-i-1,i+j-1):1}
def selected_minor(characters,i,j,k,l):return cp_mul(characters,cosine_character(i,j)).get((k+l-1,l-k-1),0)
def relative_characters(f,b,gamma):return cp_add(tensor(f),cp_scale(tensor(b),-gamma))
def relative_certificate(f,b,gamma):
 arr=relative_characters(f,b,gamma)
 neg=next((((a,c),v) for (a,c),v in sorted(arr.items()) if v<0 and a>=c),None)
 if neg is None:return dict(all_ordered_minors_certified=True,character_terms=len(arr),negative_witness=None)
 (a,c),v=neg
 assert (a-c)%2==0
 k,l=(a-c)//2,(a+c+2)//2
 direct=minor(H(f),0,1,k,l)-gamma*minor(H(b),0,1,k,l)
 assert direct==v
 return dict(all_ordered_minors_certified=False,character_terms=len(arr),negative_witness=dict(character=[a,c],rows=[0,1],columns=[k,l],value=v))
def midpoint_blocks(T,b0,b1,r,s):
 r,s=Fraction(r),Fraction(s)
 tr,ts=sub(T,[r]),sub(T,[s]);u=(r+s)/2;delta=(r-s)/2
 Lr=add(mul(b0,tr),b1);Ls=add(mul(b0,ts),b1)
 F,G=mul(Lr,ts),mul(Ls,tr)
 HH=add(mul(mul(b0,tr),ts),mul(b1,sub(T,[u])))
 assert F==add(HH,scale(b1,delta)) and G==sub(HH,scale(b1,delta))
 return HH,F,G,delta

def run():
 examples=[([1,1],[0],Fraction(4)),([4,4,1],[1,1],Fraction(4)),([2,-1,3],[1,2],Fraction(3,2)),([3,1,2,1],[2,0,1],Fraction(-2))]
 rows=[(0,1),(0,3),(1,2),(2,4)];cols=[(0,1),(0,4),(1,3),(2,5),(4,7)]
 exact_relative=exact_mixed=0
 for f,b,gamma in examples:
  hh,bb=H(f),H(b);char=relative_characters(f,b,gamma);mix=mixed_tensor(f,b)
  for i,j in rows:
   for k,l in cols:
    assert selected_minor(char,i,j,k,l)==minor(hh,i,j,k,l)-gamma*minor(bb,i,j,k,l);exact_relative+=1
    direct=minor(H(add(f,b)),i,j,k,l)-minor(hh,i,j,k,l)-minor(bb,i,j,k,l)
    assert selected_minor(mix,i,j,k,l)==direct;exact_mixed+=1
 # Actual paired root tuple; this validates midpoint normalization, not a
 # continuum packet proof. The root theorem remains an inherited proof.
 T=[15,32,24,6];c=[12,14,4];e=[1];midpoint_checks=[]
 for b0,b1 in [(c,e),(e,c)]:
  r,s=Fraction(-2),Fraction(1)
  HH,F,G,delta=midpoint_blocks(T,b0,b1,r,s)
  sharp=relative_characters(HH,b1,delta*delta)
  assert mixed_tensor(F,G)==cp_scale(sharp,2)
  ys=[1,1]
  assert mixed_tensor(mul(ys,F),mul(ys,G))==cp_scale(relative_characters(mul(ys,HH),mul(ys,b1),delta*delta),2)
  midpoint_checks.append(dict(raw=relative_certificate(HH,b1,delta*delta),smoothed=relative_certificate(mul(ys,HH),mul(ys,b1),delta*delta)))
 result=dict(scope='Finite identity/implementation checks only; the all-index theorem is algebraic.',direct_relative_minor_identity_checks=exact_relative,direct_mixed_minor_identity_checks=exact_mixed,examples=[relative_certificate(*z) for z in examples],paired_root_midpoint_normalizations=midpoint_checks,imports=[],arithmetic='exact integers and Fractions')
 def enc(v):
  if isinstance(v,Fraction):return str(v)
  raise TypeError(type(v).__name__)
 Path(__file__).with_name('network_relative_character_results.json').write_text(json.dumps(result,indent=2,default=enc)+'\n')
 print(json.dumps(result,indent=2,default=enc))
if __name__=='__main__':run()
