"""Exact canonical mutations and independently reconstructed Laurent profiles."""
from math import comb
from fractions import Fraction
from functools import lru_cache

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p)
def add(a,b):
    return trim((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))
def scale(a,c):return trim(c*v for v in a)
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    p=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:p[i+j]+=v*w
    return trim(p)
x=(0,1);y=(1,1);p=(2,1);one=(1,)
root=(one,(5,6,2),p)
def mutate(X,C,Y):return sub(sub(scale(mul(mul(y,X),C),3),mul(x,add(X,C))),Y)
@lru_cache(maxsize=3000)
def state(word):
    if not word:return root
    A,C,B=state(word[:-1])
    if word[-1]=='L':return (A,mutate(A,C,B),C)
    if word[-1]=='R':return (C,mutate(B,C,A),B)
    raise ValueError(word)
@lru_cache(maxsize=12000)
def H(a):
    return tuple(sum(a[j]*comb(j,(j-n)//2) for j in range(n,len(a),2)) for n in range(len(a)))
def coeff(h,i):return h[abs(i)] if abs(i)<len(h) else 0
def delta_row(h):
    return tuple(h[n]**2-coeff(h,n-1)*coeff(h,n+1)-coeff(h,n+1)**2+h[n]*coeff(h,n+2) for n in range(len(h)))
def cone(a):return all(v>0 for v in H(a)) and min(delta_row(H(a)))>=0
def eta(a):
    h=H(a)
    if min(h)<=0:return None
    return min(Fraction(d,v*v) for d,v in zip(delta_row(h),h))
def W(a,b):
    h,g=H(a),H(b)
    return tuple(coeff(h,n)*coeff(g,n+1)-coeff(h,n+1)*coeff(g,n) for n in range(len(h)))
def divide_y(a):
    b=list(a);q=[0]*(len(b)-1)
    for i in range(len(q)-1,-1,-1):q[i]=b[i+1];b[i]-=q[i]
    assert b[0]==0,(a,b[0])
    return trim(q or [0])
def canonical_pair(word):
    A,C,B=state(word)
    children=sorted((mutate(A,C,B),mutate(B,C,A)),key=len)
    U,V=children
    return sub(U,C),sub(V,U)
def raydata(word,direction='L'):
    X,C,Y=state(word)
    if direction=='R':X,Y=Y,X
    t=sub(scale(mul(y,X),3),x)
    T=sub(sub(mul(t,Y),mul(x,X)),C)
    A=divide_y(sub(C,Y));B=divide_y(sub(T,Y))
    J=mul(y,sub(t,(2,)));P=mul(p,X)
    V=scale(mul(mul(y,y),P),3)
    K0=add(sub(scale(mul(y,Y),3),x),one)
    q0=mul(y,A);q1=mul(y,add(mul(A,t),B));beta=mul(y,add(A,B));E1=sub(C,X)
    return dict(X=X,C=C,Y=Y,t=t,A=A,B=B,J=J,P=P,V=V,K0=K0,q0=q0,q1=q1,beta=beta,E1=E1)
if __name__=='__main__':
    s,d=canonical_pair('');print(H(s),H(d),W(s,d))
