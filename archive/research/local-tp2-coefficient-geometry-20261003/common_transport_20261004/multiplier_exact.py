#!/usr/bin/env python3
"""Standalone exact multiplier identities and sharply scoped witnesses."""
from __future__ import annotations
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def at(h,n):
    n=abs(n)
    return h[n] if n<len(h) else 0


def delta(h,n):
    return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)


def smooth(h):
    return [at(h,n)+at(h,n-1)+at(h,n+1) for n in range(len(h)+1)]


def multiplier(h):
    v=smooth(h)
    return [3*v[0]+1,3*v[1]-1]+[3*z for z in v[2:]]


def first_minor(h,i,j):
    second=lambda n:2*at(h,1) if n==0 else at(h,n-1)+at(h,n+1)
    return at(h,i)*second(j)-at(h,j)*second(i)


def H(p):
    return [sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2)) for n in range(len(p))]


def centerbase(h):
    v=smooth(h)
    return 9*delta(v,0)+3*v[0]+6*v[1]


def Froot_residual(C):
    # At root endpoints X=1,Y=x+2, Fricke=(C-Croot)(C-1).
    def mul(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):z[i+j]+=x*y
        return z
    c0=[5,6,2]
    p=[C[i]-(c0[i] if i<len(c0) else 0) for i in range(len(C))]
    q=C.copy();q[0]-=1
    return mul(p,q)


class Poly:
    """Sparse exact ring Q[h0,...,hN]."""
    N=7
    def __init__(self,v=0):
        self.p={tuple([0]*self.N):Fraction(v)} if v else {}
    @classmethod
    def var(cls,i):
        z=cls();m=[0]*cls.N;m[i]=1;z.p[tuple(m)]=Fraction(1);return z
    def __add__(self,b):
        b=b if isinstance(b,Poly) else Poly(b)
        z=Poly();z.p=self.p.copy()
        for m,c in b.p.items():
            z.p[m]=z.p.get(m,Fraction(0))+c
            if not z.p[m]:del z.p[m]
        return z
    __radd__=__add__
    def __neg__(self):
        z=Poly();z.p={m:-c for m,c in self.p.items()};return z
    def __sub__(self,b):return self+(-b if isinstance(b,Poly) else -Poly(b))
    def __rsub__(self,b):return Poly(b)+(-self)
    def __mul__(self,b):
        b=b if isinstance(b,Poly) else Poly(b)
        z=Poly()
        for m,c in self.p.items():
            for n,d in b.p.items():
                k=tuple(i+j for i,j in zip(m,n))
                z.p[k]=z.p.get(k,Fraction(0))+c*d
                if not z.p[k]:del z.p[k]
        return z
    __rmul__=__mul__
    def __pow__(self,n):
        z=Poly(1)
        for _ in range(n):z=z*self
        return z


def symbolic_checks():
    checks=[]
    for degree in range(2,6):
        h=[Poly.var(i) for i in range(degree+1)]
        v=smooth(h);m=multiplier(h)
        expected=[9*delta(v,0)+6*v[0]+12*v[1]+3*v[2]-1,
                  9*delta(v,1)-6*v[1]-3*v[2]-3*at(v,3)+1,
                  9*delta(v,2)+3*at(v,3)]
        expected += [9*delta(v,n) for n in range(3,len(m))]
        assert all(not (delta(m,n)-expected[n]).p for n in range(len(m)))
        assert not (delta(v,1)-sum(first_minor(h,i,j) for i,j in [(0,1),(0,2),(0,3),(1,3),(2,3)])).p
        a02,a13,a03=(first_minor(h,i,j) for i,j in [(0,2),(1,3),(0,3)])
        assert not (h[1]*a02-h[2]*delta(h,0)-h[0]*delta(h,1)).p
        assert not (h[2]*a13-at(h,3)*delta(h,1)-h[1]*delta(h,2)).p
        assert not (h[1]*a03-at(h,3)*delta(h,0)-h[0]*a13).p
        c=m.copy();c[0]=c[0]-1
        pm=[2*at(m,n)+at(m,n-1)+at(m,n+1) for n in range(len(m)+1)]
        W=lambda i:at(c,i)*at(pm,i+1)-at(c,i+1)*at(pm,i)
        assert not (W(0)-centerbase(h)).p
        assert all(not (W(n)-delta(m,n)).p for n in range(1,len(c)))
        checks.append({'degree':degree,'multiplier_defects':'PASS','tail_CB':'PASS',
                       'three_Pluckers':'PASS','centerbase':'PASS'})
    h0,h1,h2,h3,h4=(Poly.var(i) for i in range(5))
    numerator=(5*h0-3*h1-2*h2-h3-2*h4)*h1+6*h0*h3
    sos=5*(h0-h1)*h1+2*(h1-h2)*h1+6*(h0-h1)*h3+3*h1*h3+2*h1*(h3-h4)
    assert not (numerator-sos).p
    u=[Poly.var(i) for i in range(3)]
    w=[Poly.var(i) for i in range(3,6)]
    mixed=2*u[0]*w[0]+u[0]*w[2]+w[0]*u[2]-4*u[1]*w[1]
    assert not (delta([a+b for a,b in zip(u,w)],0)-delta(u,0)-delta(w,0)-mixed).p
    return {'degree_boundaries':checks,'half_local_strength_surplus_SOS':'PASS',
            'central_polarization_identity':'PASS'}


def example(label,h,ordinary=None):
    v=smooth(h);m=multiplier(h)
    record={'label':label,'H_C':h,'delta_C':[delta(h,n) for n in range(len(h))],
            'H_yC':v,'delta_yC':[delta(v,n) for n in range(len(v))],
            'H_M':m,'delta_M':[delta(m,n) for n in range(len(m))],
            'centerbase_0':centerbase(h),
            'C_cone':all(delta(h,n)>=0 for n in range(len(h))),
            'yC_cone':all(delta(v,n)>=0 for n in range(len(v))),
            'M_cone':all(delta(m,n)>=0 for n in range(len(m))),
            'local_half_margins':[str(delta(h,n)-Fraction(at(h,n),2)) for n in range(3)]}
    if ordinary is not None:
        assert H(ordinary)==h
        record['C_ordinary']=ordinary
        record['root_endpoint_Fricke_residual']=Froot_residual(ordinary)
    return record


def run():
    ex=[example('canonical_root',H([5,6,2]),[5,6,2]),
        example('ordinary_positive_weaker_central_gate',H([7,6,2]),[7,6,2]),
        example('M_cone_does_not_imply_centerbase',H([8,6,2]),[8,6,2]),
        example('C_one_strong_does_not_remove_central_gate',H([9,6,2]),[9,6,2]),
        example('weak_paired_character_positive_row_does_not_imply_M', [22,20,15,8],[-8,-4,15,8]),
        example('relaxed_B0_not_closed_under_identical_positive_sums',H([21,18,6]),[21,18,6])]
    assert ex[0]['centerbase_0']>0 and ex[0]['M_cone']
    assert ex[1]['delta_yC'][0]<0<ex[1]['centerbase_0'] and ex[1]['M_cone']
    assert ex[2]['M_cone'] and ex[2]['centerbase_0']<0
    assert not ex[3]['M_cone'] and all(delta(ex[3]['H_C'],n)>=at(ex[3]['H_C'],n) for n in range(len(ex[3]['H_C'])))
    assert ex[4]['C_cone'] and ex[4]['yC_cone'] and not ex[4]['M_cone']
    assert ex[5]['C_cone'] and ex[5]['centerbase_0']==-180
    assert all(Fraction(s)>=0 for s in ex[5]['local_half_margins'])
    return {'status':'EXACT_GENERAL_IDENTITIES_AND_ABSTRACT_OBSTRUCTIONS_NOT_ALL_TREE_PROOF',
            'imports':'Python standard library only; no parent arithmetic',
            'symbolic':symbolic_checks(),'examples':ex}


if __name__=='__main__':
    result=run()
    out=Path(__file__).with_name('multiplier_exact_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'symbolic':result['symbolic'],
                     'example_labels':[z['label'] for z in result['examples']]},indent=2))
