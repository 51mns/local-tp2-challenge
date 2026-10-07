#!/usr/bin/env python3
"""Unbounded symbolic polynomial identities for the normalized state."""
import json
from pathlib import Path
class P:
 def __init__(self,d=0):self.d={k:v for k,v in d.items() if v} if isinstance(d,dict) else ({(0,0,0,0):d} if d else {})
 def __add__(self,b):
  b=b if isinstance(b,P) else P(b);r=self.d.copy()
  for k,v in b.d.items():r[k]=r.get(k,0)+v
  return P(r)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,b):return self+-as_p(b)
 def __rsub__(self,b):return as_p(b)+-self
 def __mul__(self,b):
  b=as_p(b);r={}
  for k,v in self.d.items():
   for l,w in b.d.items():
    m=tuple(i+j for i,j in zip(k,l));r[m]=r.get(m,0)+v*w
  return P(r)
 __rmul__=__mul__
 def __pow__(self,n):
  r=P(1)
  for _ in range(n):r=r*self
  return r
 def __eq__(self,b):return self.d==as_p(b).d
 def nonnegative(self):return all(v>=0 for v in self.d.values())
def as_p(p):return p if isinstance(p,P) else P(p)
def var(n):return P({tuple(int(i==n) for i in range(4)):1})
x,a,e,r=[var(i) for i in range(4)];y=x+1

def state(a,e,r):
 X=1+y*a;t=2*x+3+3*y*y*a;k=X*(3*X-2)
 g=(t-2)*e+k+r;s=t*g-r;M=t+1+3*y*y*(e+g);d=e*M
 F=r*g-(t-2)*e*e-2*k*e-3*a*X*X
 return X,t,k,g,s,M,d,F
X,t,k,g,s,M,d,F=state(a,e,r)
checks={}
def check(name,p,q=0):
 assert p==q,name;checks[name]='PASS'
Y=X+y*e;C=Y+y*g
I=X*X+Y*Y+C*C+x*(X*Y+X*C+Y*C)-3*y*X*Y*C
check('fricke_residual',I,y*y*F)
U=3*y*X*C-x*(X+C)-Y;V=3*y*Y*C-x*(Y+C)-X
check('short_gap',U-C,y*s);check('long_difference',V-U,y*d)
short=state(a,e+g,g);long=state(a+e,g,e+g)
check('short_next_g',short[3],s);check('long_next_g',long[3],s+d)
check('short_preserves_fricke',short[-1],F);check('long_preserves_fricke',long[-1],F)
check('short_remainder_bound',a+(e+g)-g,a+e)
check('long_remainder_bound',(a+e)+g-(e+g),a)
positive=2*x*e+3*y*y*a*e+(4*y-1)*a+3*y*y*a*a
check('growth_positive_decomposition',g-a-e-r-1,positive)
assert positive.nonnegative();checks['growth_decomposition_coefficients']='NONNEGATIVE'
check('cassini_residual',g*g-r*s-X*X*(1+3*a),-(t-2)*F)
check('square_dominance_residual',e*e-(2*x+1)*a*(a+e)-e-2*a-(a+e-r)*(g+a+e),F)
root=state(P(0),P(1),P(1));check('root_g',root[3],2*x+3)
check('root_s',root[4],4*(x+1)*(x+2))
check('root_d',root[6],2*(x+2)*(1+3*(x+1)**2))
result={'scope':'symbolic identities over Z[x,a,e,r], not finite-state interpolation','checks':checks,'fricke_monomials':len(F.d),'all_pass':True}
print(json.dumps(result,indent=2))
