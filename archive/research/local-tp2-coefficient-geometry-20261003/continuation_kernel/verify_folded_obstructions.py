#!/usr/bin/env python3
"""Exact arithmetic checks for counterexamples and coefficient identities.
This script does not assert a universal canonical Local TP2 theorem.
"""
from itertools import combinations

def auto(a):
    return [sum(u*v for u,v in zip(a,a[n:])) for n in range(len(a))]

def defects(h):
    def get(n):
        return h[abs(n)] if abs(n)<len(h) else 0
    return [get(n)**2-get(n-1)*get(n+1) for n in range(len(h)+1)]

def delta(h):
    d=defects(h)
    return [d[n]-d[n+1] for n in range(len(h))]

def k(h,i,j):
    def get(n):
        return h[n] if n<len(h) else 0
    if i==0:return get(j)
    if j==0:return 2*get(i)
    return get(abs(i-j))+get(i+j)

def minor(h,i,j,r,s):
    return k(h,i,r)*k(h,j,s)-k(h,i,s)*k(h,j,r)

def main():
    a=[6,12,24,34,45,52,60]
    assert all(a[i]**2>=a[i-1]*a[i+1] for i in range(1,len(a)-1))
    h=auto(a)
    assert h==[10241,8166,6100,4032,2334,1032,360]
    assert minor(h,0,1,1,2)==-71232
    print('Positive log-concave autocorrelation counterexample: minor = -71232.')
    strict=[21,41,79,112,151,174,200]
    assert all(strict[i]**2>strict[i-1]*strict[i+1] for i in range(1,len(strict)-1))
    assert minor(auto(strict),0,1,1,2)==-9189654
    print('Strict log-concave autocorrelation counterexample: minor = -9189654.')
    assert delta([3,2,1])==[4,0,1]
    assert delta([7,6,3,1])==[-2,12,2,1]
    print('Multiplication by x+1 fails folded-cone preservation exactly.')
    ht=[12,8,3]
    for a in [-2,-1,0,1,2]:
        ha=ht.copy();ha[0]+=a
        assert delta(ha)==[52+27*a+a*a,19-3*a,9]
        assert all(v>0 for v in delta(ha))
    print('t_(x+2)+a endpoint-margin formulas verified exactly.')
    assert (k(ht,0,0)-1)*0-1*k(ht,1,0)==-16
    print('Natural two-state block TP2 obstruction: minor = -16.')

if __name__=='__main__':main()
