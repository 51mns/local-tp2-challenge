"""Standard-library exact polynomial arithmetic for packet_gate_verify.py."""
from fractions import Fraction as Q
from math import comb

def trim(p):
 while len(p)>1 and not p[-1]:p.pop()
 return p
def add(*ps):return trim([sum(p[i] if i<len(p) else 0 for p in ps) for i in range(max(map(len,ps)))])
def scale(p,c):return [c*v for v in p]
def mul(*ps):
 o=[1]
 for p in ps:
  z=[0]*(len(o)+len(p)-1)
  for i,a in enumerate(o):
   for j,b in enumerate(p):z[i+j]+=a*b
  o=trim(z)
 return o
def row(p):return [sum(p[i]*comb(i,(i-j)//2) for i in range(j,len(p),2)) for j in range(len(p))]
def at(h,i):return h[abs(i)] if abs(i)<len(h) else 0
def delta(h,j):return at(h,j)**2-at(h,j-1)*at(h,j+1)-at(h,j+1)**2+at(h,j)*at(h,j+2)
y=[1,1];beta=[3,6,3];z=[3,2]
def state(a,e,r):
 X=add([1],mul(y,a));t=add(z,mul(beta,a));k=mul(X,add(scale(X,3),[-2]));g=add(mul(add(t,[-2]),e),k,r);s=add(mul(t,g),scale(r,-1));T=add(t,mul(beta,add(e,g)));c=add(e,g,s);d=mul(e,add(T,[1]));return t,g,s,T,c,d

def advance(a,e,r,sigma):
 _,g,_,_,_,_=state(a,e,r)
 return (add(a,scale(e,sigma)),add(g,scale(e,1-sigma)),add(g,scale(e,sigma)))
