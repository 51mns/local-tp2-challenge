#!/usr/bin/env python3
"""Independent ordinary-x polynomial, canonical mutation, and Fourier helpers."""
from pathlib import Path
from hashlib import sha256
import json


def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p


def add(p,q):
    out=[0]*max(len(p),len(q))
    for i,v in enumerate(p):out[i]+=v
    for i,v in enumerate(q):out[i]+=v
    return trim(out)


def sub(p,q):
    return add(p,[-v for v in q])


def times(p,c):
    return trim([c*v for v in p])


def multiply(p,q):
    if min(len(p),len(q))<=24:
        out=[0]*(len(p)+len(q)-1)
        for i,a in enumerate(p):
            for j,b in enumerate(q):out[i+j]+=a*b
        return trim(out)
    n=max(len(p),len(q))//2
    p0,p1=p[:n],p[n:] or [0]
    q0,q1=q[:n],q[n:] or [0]
    low=multiply(p0,q0)
    high=multiply(p1,q1)
    middle=sub(sub(multiply(add(p0,p1),add(q0,q1)),low),high)
    return add(add(low,[0]*n+middle),[0]*(2*n)+high)


def mutation(A,C,B):
    triple=times(multiply(multiply([1,1],A),C),3)
    return sub(sub(triple,[0]+add(A,C)),B)


def divide_y(p):
    q=[p[0]]
    for c in p[1:-1]:q.append(c-q[-1])
    assert p[-1]==q[-1]
    return trim(q)


def fourier_horner(p):
    # Each step is multiplication by q+q^-1 and addition of one constant.
    h=[p[-1]]
    for coefficient in reversed(p[:-1]):
        out=[0]*(len(h)+1)
        out[0]=(2*h[1] if len(h)>1 else 0)+coefficient
        for n in range(1,len(out)):
            out[n]=h[n-1]+(h[n+1] if n+1<len(h) else 0)
        h=out
    return h


def delta(h,n):
    at=lambda j:h[abs(j)] if abs(j)<len(h) else 0
    return at(n)**2-at(n-1)*at(n+1)-at(n+1)**2+at(n)*at(n+2)


def digest(values):
    out=sha256()
    for v in values:out.update((str(v)+'\n').encode())
    return out.hexdigest()


