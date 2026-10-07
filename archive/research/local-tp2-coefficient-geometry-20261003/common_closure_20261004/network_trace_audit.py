#!/usr/bin/env python3
"""Formal coefficient identity checks for invariant_shifted_trace_lemma.md.
No scans, no parent arithmetic imports. Inequality proof is in the audit note.
"""
import json
from pathlib import Path

def const(n):return {():n} if n else {}
def var(i):return {(i,):1}
def add(*ps):
 out={}
 for p in ps:
  for mon,v in p.items():out[mon]=out.get(mon,0)+v
 return {mon:v for mon,v in out.items() if v}
def scale(p,k):return {mon:v*k for mon,v in p.items() if v*k}
def neg(p):return scale(p,-1)
def sub(p,q):return add(p,neg(q))
def mul(*ps):
 out=const(1)
 for p in ps:
  nxt={}
  for mon,a in out.items():
   for non,b in p.items():
    z=tuple(sorted(mon+non));nxt[z]=nxt.get(z,0)+a*b
  out={mon:v for mon,v in nxt.items() if v}
 return out

def defect(h,n):
 get=lambda i:h[abs(i)] if abs(i)<len(h) else {}
 return add(mul(get(n),get(n)),neg(mul(get(n-1),get(n+1))),neg(mul(get(n+1),get(n+1))),mul(get(n),get(n+2)))
def ysmooth(h):
 get=lambda i:h[abs(i)] if abs(i)<len(h) else {}
 return [add(get(0),scale(get(1),2))]+[add(get(n-1),get(n),get(n+1)) for n in range(1,len(h)+1)]
def firsttwo_w(h,i,j):
 get=lambda n:h[abs(n)] if abs(n)<len(h) else {}
 row1=lambda n:scale(get(1),2) if n==0 else add(get(n-1),get(n+1))
 return sub(mul(get(i),row1(j)),mul(get(j),row1(i)))
def trace(h,c):
 v=ysmooth(ysmooth(h));z=[scale(p,3) for p in v];z[0]=add(z[0],c);z[1]=add(z[1],const(2));return v,z

def run():
 h=[var(i) for i in range(7)];c=var(7);v,z=trace(h,c);checks={}
 expected=add(scale(firsttwo_w(h,0,1),4),scale(firsttwo_w(h,0,2),2),scale(firsttwo_w(h,0,3),3),scale(firsttwo_w(h,1,3),4),scale(firsttwo_w(h,2,3),2))
 assert defect(v,0)==expected;checks['central_CB_coefficients_4_2_3_4_2']=True
 Q=add(scale(v[1],8),scale(v[0],-2),neg(v[2]))
 assert Q==add(scale(h[0],9),scale(h[1],22),scale(h[2],9),scale(h[3],6),neg(h[4]));checks['central_Q_linear_form']=True
 assert defect(z,0)==add(scale(defect(v,0),9),scale(mul(c,v[0]),6),scale(v[1],-24),scale(mul(c,v[2]),3),mul(c,c),const(-8));checks['trace_delta0_perturbation']=True
 assert defect(z,1)==add(scale(defect(v,1),9),scale(v[1],12),scale(mul(c,v[2]),-3),scale(v[3],6),const(4));checks['trace_delta1_perturbation']=True
 assert defect(z,2)==add(scale(defect(v,2),9),scale(v[3],-6));checks['trace_delta2_perturbation']=True
 for n in range(3,len(z)):
  assert defect(z,n)==scale(defect(v,n),9)
 checks['trace_delta_ge3_perturbation_including_terminal']=True
 for n in [1,2,3]:
  u=ysmooth(h);five=add(firsttwo_w(u,n-1,n),firsttwo_w(u,n-1,n+1),firsttwo_w(u,n-1,n+2),firsttwo_w(u,n,n+2),firsttwo_w(u,n+1,n+2))
  assert defect(v,n)==five
 checks['second_y_five_minor_identity_n1_n2_n3']=True
 A,B=h[0],h[1];vd,zd=trace([A,B],c)
 assert defect(zd,0)==add(scale(mul(A,A),36),scale(mul(A,B),18),scale(mul(B,B),-72),mul(add(scale(c,21),const(-48)),A),mul(add(scale(c,30),const(-96)),B),mul(c,c),const(-8))
 assert defect(zd,1)==add(scale(mul(A,B),36),scale(mul(B,B),72),mul(add(const(24),scale(c,-3)),A),mul(add(const(54),scale(c,-6)),B),const(4))
 assert defect(zd,2)==add(scale(mul(A,A),9),scale(mul(A,B),18),scale(mul(B,B),-9),scale(B,-6))
 assert defect(zd,3)==scale(mul(B,B),9)
 checks['all_degree1_defect_formulas']=True
 vc,zc=trace([A],c)
 assert defect(zc,0)==add(scale(mul(A,A),36),mul(add(scale(c,21),const(-48)),A),mul(c,c),const(-8))
 assert defect(zc,1)==add(mul(add(const(24),scale(c,-3)),A),const(4))
 assert defect(zc,2)==scale(mul(A,A),9)
 checks['all_degree0_defect_formulas']=True
 # Exact abstract degree-one exception: a=x+2 and rho=2.
 def plain_delta(h):
  get=lambda n:h[abs(n)] if abs(n)<len(h) else 0
  return [get(n)**2-get(n-1)*get(n+1)-get(n+1)**2+get(n)*get(n+2) for n in range(len(h))]
 exception=dict(a_halfrow=[2,1],a_defects=plain_delta([2,1]),ya_halfrow=[4,3,1],ya_defects=plain_delta([4,3,1]),trace_minus2_halfrow=[31,26,12,3],trace_minus2_defects=plain_delta([31,26,12,3]))
 assert exception['trace_minus2_defects'][0]==-19
 out=dict(scope='Formal coefficient identities only; infinite inequalities have an analytic audit, not scan inference.',checks=checks,abstract_exception=exception,imports=[])
 Path(__file__).with_name('network_trace_audit_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
