"""Exact Bernstein certificates for U_r - U_(r-1) root-pair blocks."""
from fractions import Fraction as Q
from math import comb
from itertools import product
import json

DIM = 6  # x and five independent unit-interval parameters
ZERO = (0,) * DIM


def const(c):
    return {ZERO: Q(c)} if c else {}


def variable(i):
    powers = [0] * DIM
    powers[i] = 1
    return {tuple(powers): Q(1)}


def add(*ps):
    result = {}
    for p in ps:
        for key, value in p.items():
            result[key] = result.get(key, Q(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(p, c):
    return {key: c * value for key, value in p.items() if c * value}


def mul(a, b):
    result = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x + y for x, y in zip(ka, kb))
            result[key] = result.get(key, Q(0)) + va * vb
    return {key: value for key, value in result.items() if value}


def fourier(p):
    h = [{} for _ in range(max(k[0] for k in p) + 3)]
    for key, value in p.items():
        for j in range(key[0] // 2 + 1):
            n = key[0] - 2 * j
            h[n] = add(h[n], {(0,) + key[1:]: value * comb(key[0], j)})
    return h


def defects(p):
    h = fourier(p)
    delta = [add(mul(h[n], h[n]), scale(mul(h[n-1] if n else h[1], h[n+1]), -1)) for n in range(len(h)-1)]
    return [add(delta[n], scale(delta[n+1], -1)) for n in range(len(delta)-1)]


def bernstein(p):
    degrees = tuple(max((key[j] for key in p), default=0) for j in range(1, DIM))
    out = {}
    for indices in product(*(range(d + 1) for d in degrees)):
        total = Q(0)
        for key, value in p.items():
            exponents = key[1:]
            if all(a <= i for a, i in zip(exponents, indices)):
                term = value
                for a, i, degree in zip(exponents, indices, degrees):
                    term *= Q(comb(i, a), comb(degree, a))
                total += term
        out[','.join(map(str, indices))] = total
    return degrees, out


def main():
    x,u,v,w,z,h=[variable(i) for i in range(DIM)]
    x2=mul(x,x)
    f=add(x2,mul(add(const(Q(5,2)),scale(u,Q(1,2))),x),const(Q(5,4)),v)
    g=add(x2,mul(add(const(Q(5,2)),scale(w,Q(1,2))),x),const(Q(5,4)),z)
    middle=add(x,const(Q(5,4)),scale(h,Q(1,4)))
    inner_a=add(x,const(Q(2,3)),scale(u,Q(5,6)))
    inner_b=add(x,const(Q(3,2)),scale(v,Q(1,2)))
    blocks={'two_general_pairs':mul(f,g),'middle_times_pair':mul(middle,f),'middle_times_two_pairs':mul(middle,mul(f,g)),'isolated_inner_pair':mul(inner_a,inner_b)}
    result={}
    for name,p in blocks.items():
        certs=[]
        for n,defect in enumerate(defects(p)):
            degrees,coefficients=bernstein(defect)
            lower=min(coefficients.values())
            assert lower>0,(name,n,str(lower))
            certs.append({'n':n,'degrees':degrees,'strict_lower_bound':str(lower),'power_coefficients':{','.join(map(str,k[1:])):str(v) for k,v in sorted(defect.items())},'bernstein_coefficients':{k:str(v) for k,v in coefficients.items()}})
        result[name]=certs
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
