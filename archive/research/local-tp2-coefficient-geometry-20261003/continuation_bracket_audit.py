"""Independent exact audit of all-left bracket margin certificates.

Uses direct Laurent multiplication and expands Bernstein polynomials back into
powers. It does not import the certificate-producing scripts.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            k = tuple(x+y for x, y in zip(i, j))
            out[k] = out.get(k, F(0)) + a*b
    return {k: v for k, v in out.items() if v}


def halfrow(p, n):
    return {k[1:]: v for k, v in p.items() if k[0] == n}


def delta(p, n):
    h = lambda i: halfrow(p, i)
    first = add(mul(h(n), h(n)), scale(mul(h(n-1), h(n+1)), -1))
    second = add(mul(h(n+1), h(n+1)), scale(mul(h(n), h(n+2)), -1))
    return add(first, scale(second, -1))


def mass(p):
    # q=1 is exactly x=2. All Laurent coefficients contribute once.
    out = {}
    for k, v in p.items():
        out[k[1:]] = out.get(k[1:], F(0)) + v
    return {k: v for k, v in out.items() if v}


def main():
    one = {(0,)*6: F(1)}
    x = {(-1,0,0,0,0,0): F(1), (1,0,0,0,0,0): F(1)}
    params = [{tuple(1 if j == i else 0 for j in range(6)): F(1)} for i in range(1,6)]
    u, v, w, z, t = params
    y = add(x, one)
    y2 = mul(y, y)
    def pair(a, b):
        return add(mul(x,x),mul(add(scale(one,3),a),x),scale(one,F(5,4)),scale(a,F(5,2)),b)
    quartic = mul(pair(u,v),pair(w,z))
    middle = add(x,scale(one,F(3,2)),scale(w,F(1,2)))
    central = add(x,scale(one,F(3,2)))
    even = add(mul(x,x),scale(x,3),scale(one,2),scale(u,F(1,4)))
    odd = add(mul(x,x),scale(x,3),scale(one,F(7,4)),scale(u,F(1,2)))
    inner = mul(add(x,one,scale(v,F(1,2))),add(x,scale(one,F(3,2)),w))
    otherpair = pair(v,z)
    residues = {
        'n_mod8_0_pull_quartic': quartic,
        'n_mod8_1_pull_quartic': mul(quartic,add(x,scale(one,F(3,2)),scale(t,F(1,2)))),
        'n_mod8_2': mul(central,middle),
        'n_mod8_3': mul(central,inner),
        'n_mod8_4': mul(even,inner),
        'n_mod8_5': mul(mul(even,middle),otherpair),
        'n_mod8_6': mul(mul(mul(central,odd),middle),otherpair),
        'n_mod8_7': mul(central,odd),
    }
    margins = {'scaled_quartic_delta0_minus_mass': add(scale(delta(quartic,0),16),scale(mass(quartic),-1))}
    for name, residue in residues.items():
        degree = max(k[0] for k in residue)
        margins[name] = add(scale(delta(mul(y2,residue),2),2**degree),scale(mass(residue),-6))
    recorded = json.loads(Path('continuation_bracket_certificates.json').read_text())
    minima = {}
    count = 0
    for name, actual in margins.items():
        cert = recorded[name]
        expected = {tuple(map(int,k.split(','))):F(v) for k,v in cert['power_coefficients'].items()}
        assert actual == expected, (name,'direct Laurent margin')
        if name in residues:
            assert cert['residue_degree'] == max(k[0] for k in residues[name])
        degrees = tuple(cert['degrees'])
        bc = {tuple(map(int,k.split(','))):F(v) for k,v in cert['bernstein_coefficients'].items()}
        assert set(bc) == set(product(*(range(d+1) for d in degrees)))
        expanded = {}
        for indices,value in bc.items():
            for offsets in product(*(range(d-i+1) for d,i in zip(degrees,indices))):
                coefficient = value
                for d,i,a in zip(degrees,indices,offsets):
                    coefficient *= comb(d,i)*comb(d-i,a)*(-1)**a
                key = tuple(i+a for i,a in zip(indices,offsets))
                expanded[key] = expanded.get(key,F(0)) + coefficient
        expanded = {k:v for k,v in expanded.items() if v}
        assert actual == expanded, (name,'Bernstein reconstruction')
        minimum = min(bc.values())
        assert minimum>0 and minimum==F(cert['strict_lower_bound'])
        minima[name] = str(minimum)
        count += len(bc)

    # The separately handled n=1 bracket, with prefix T_1=2(x+2).
    prefix1 = scale(add(x,scale(one,2)),2)
    bracket1 = add(scale(mul(y2,prefix1),3),scale(y,2),scale(one,2))
    b1 = [delta(bracket1,n)[(0,)*5] for n in range(4)]
    assert b1 == [632,688,240,36]
    print(json.dumps({'margin_polynomials_verified':len(margins),
                      'Bernstein_coefficients_verified':count,
                      'n1_bracket_defects':list(map(str,b1)),
                      'exact_minima':minima},indent=2))


if __name__ == '__main__':
    main()
