"""Independent Laurent reconstruction for the y V_r helper certificates."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}


def scale(p,c):return {k:v*c for k,v in p.items() if v*c}


def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            k=tuple(x+y for x,y in zip(i,j))
            out[k]=out.get(k,F(0))+a*b
    return {k:v for k,v in out.items() if v}


def main():
    one={(0,)*6:F(1)}
    x={(-1,0,0,0,0,0):F(1),(1,0,0,0,0,0):F(1)}
    u,v,w,z,h=[{tuple(1 if j==i else 0 for j in range(6)):F(1)} for i in range(1,6)]
    y=add(x,one)
    def pair(a,b):return add(mul(x,x),mul(add(scale(one,3),a),x),scale(one,F(5,4)),scale(a,F(5,2)),b)
    f,g=pair(u,v),pair(w,z)
    middle=add(x,scale(one,F(3,2)),scale(h,F(1,2)))
    inner=mul(add(x,one,scale(u,F(1,2))),add(x,scale(one,F(3,2)),v))
    blocks={'y_times_two_pairs':mul(y,mul(f,g)),
            'y_times_middle':mul(y,middle),
            'y_times_inner_pair':mul(y,inner),
            'y_times_middle_pair':mul(y,mul(middle,f))}
    certificates=json.loads(Path('resumed_external_yV_certificates.json').read_text())
    count=defects=0;minima={}
    for name,p in blocks.items():
        degree=max(k[0] for k in p)
        assert len(certificates[name])==degree+1
        row=lambda n:{k[1:]:v for k,v in p.items() if k[0]==n}
        defect=lambda n:add(mul(row(n),row(n)),scale(mul(row(n-1),row(n+1)),-1))
        minima[name]=[]
        for n,cert in enumerate(certificates[name]):
            actual=add(defect(n),scale(defect(n+1),-1))
            recorded={tuple(map(int,k.split(','))):F(v) for k,v in cert['power_coefficients'].items()}
            assert actual==recorded,(name,n,'Laurent defect')
            degrees=tuple(cert['degrees'])
            bc={tuple(map(int,k.split(','))):F(v) for k,v in cert['bernstein_coefficients'].items()}
            assert set(bc)==set(product(*(range(d+1) for d in degrees)))
            expansion={}
            for indices,value in bc.items():
                for offsets in product(*(range(d-i+1) for d,i in zip(degrees,indices))):
                    coeff=value
                    for d,i,a in zip(degrees,indices,offsets):coeff*=comb(d,i)*comb(d-i,a)*(-1)**a
                    k=tuple(i+a for i,a in zip(indices,offsets))
                    expansion[k]=expansion.get(k,F(0))+coeff
            expansion={k:v for k,v in expansion.items() if v}
            assert expansion==actual,(name,n,'Bernstein reconstruction')
            minimum=min(bc.values())
            assert minimum>0 and minimum==F(cert['strict_lower_bound'])
            count+=len(bc);defects+=1;minima[name].append(str(minimum))
    print(json.dumps({'defects_verified':defects,'Bernstein_coefficients_verified':count,'exact_minima':minima},indent=2))


if __name__=='__main__':main()
