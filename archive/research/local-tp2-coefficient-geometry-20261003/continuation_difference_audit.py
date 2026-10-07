"""Independent direct-Laurent audit of the adjacent-difference certificates."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def add(*ps):
    out = {}
    for p in ps:
        for k,v in p.items():
            out[k] = out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}


def scale(p,c):
    return {k:v*c for k,v in p.items() if v*c}


def mul(p,q):
    out = {}
    for i,a in p.items():
        for j,b in q.items():
            k = tuple(x+y for x,y in zip(i,j))
            out[k] = out.get(k,F(0))+a*b
    return {k:v for k,v in out.items() if v}


def delta(p,n):
    row = lambda i:{k[1:]:v for k,v in p.items() if k[0]==i}
    d0 = add(mul(row(n),row(n)),scale(mul(row(n-1),row(n+1)),-1))
    d1 = add(mul(row(n+1),row(n+1)),scale(mul(row(n),row(n+2)),-1))
    return add(d0,scale(d1,-1))


def main():
    one = {(0,)*6:F(1)}
    x = {(-1,0,0,0,0,0):F(1),(1,0,0,0,0,0):F(1)}
    u,v,w,z,h = [{tuple(1 if j==i else 0 for j in range(6)):F(1)} for i in range(1,6)]
    def pair(a,b):
        return add(mul(x,x),mul(add(scale(one,F(5,2)),scale(a,F(1,2))),x),scale(one,F(5,4)),b)
    f,g = pair(u,v),pair(w,z)
    middle = add(x,scale(one,F(5,4)),scale(h,F(1,4)))
    blocks = {
        'two_general_pairs':mul(f,g),
        'middle_times_pair':mul(middle,f),
        'middle_times_two_pairs':mul(middle,mul(f,g)),
        'isolated_inner_pair':mul(add(x,scale(one,F(2,3)),scale(u,F(5,6))),
                                  add(x,scale(one,F(3,2)),scale(v,F(1,2)))),
    }
    certs = json.loads(Path('continuation_difference_certificates.json').read_text())
    minima = {}
    count = defect_count = 0
    for name,p in blocks.items():
        degree = max(k[0] for k in p)
        assert len(certs[name])==degree+1
        minima[name]=[]
        for n,cert in enumerate(certs[name]):
            actual = delta(p,n)
            expected = {tuple(map(int,k.split(','))):F(v) for k,v in cert['power_coefficients'].items()}
            assert actual==expected,(name,n,'direct Laurent defect')
            degrees=tuple(cert['degrees'])
            bc={tuple(map(int,k.split(','))):F(v) for k,v in cert['bernstein_coefficients'].items()}
            assert set(bc)==set(product(*(range(d+1) for d in degrees)))
            expanded={}
            for indices,value in bc.items():
                for offsets in product(*(range(d-i+1) for d,i in zip(degrees,indices))):
                    coefficient=value
                    for d,i,a in zip(degrees,indices,offsets):
                        coefficient*=comb(d,i)*comb(d-i,a)*(-1)**a
                    key=tuple(i+a for i,a in zip(indices,offsets))
                    expanded[key]=expanded.get(key,F(0))+coefficient
            expanded={k:v for k,v in expanded.items() if v}
            assert expanded==actual,(name,n,'Bernstein reconstruction')
            minimum=min(bc.values())
            assert minimum>0 and minimum==F(cert['strict_lower_bound'])
            minima[name].append(str(minimum))
            count+=len(bc)
            defect_count+=1

    # Supplementary exact checks of the recurrence, corrected difference, and CD.
    zz=add(scale(x,2),scale(one,3))
    us=[one,zz]
    for n in range(1,10):
        us.append(add(mul(zz,us[-1]),scale(us[-2],-1)))
    ws=[one]+[add(us[n],scale(us[n-1],-1)) for n in range(1,len(us))]
    row=lambda p,n:p.get((n,0,0,0,0,0),F(0))
    checked=0
    for r in range(1,11):
        assert add(ws[r],scale(ws[r-1],-1))==mul(add(scale(x,2),one),us[r-1])
    for r in range(2,10):
        for n in range(r+1):
            lhs=row(ws[r+1],n+1)*row(ws[r],n)-row(ws[r+1],n)*row(ws[r],n+1)
            rhs=2*sum(delta(ws[j],n).get((0,)*5,F(0)) for j in range(r+1))
            bound=36 if n==0 else 8 if n==1 else 2*4**n
            assert lhs==rhs and lhs>=bound,(r,n)
            checked+=1
    print(json.dumps({'defects_verified':defect_count,
                      'Bernstein_coefficients_verified':count,
                      'supplementary_correct_difference_checks':10,
                      'supplementary_CD_checks':checked,
                      'exact_minima':minima},indent=2))


if __name__=='__main__':
    main()
