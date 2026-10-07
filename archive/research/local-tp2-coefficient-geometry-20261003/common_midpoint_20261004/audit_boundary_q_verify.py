#!/usr/bin/env python3
"""Independent direct-Laurent reconstruction of the y W_N certificates.

Imports no certificate-producing arithmetic and performs no depth scan.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items()if v}
def scale(p,c):return {k:v*c for k,v in p.items()if v*c}
def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            k=tuple(x+y for x,y in zip(i,j));out[k]=out.get(k,F(0))+a*b
    return {k:v for k,v in out.items()if v}
def defect(p,n):
    row=lambda i:{k[1:]:v for k,v in p.items()if k[0]==i}
    return add(mul(row(n),row(n)),scale(mul(row(n-1),row(n+1)),-1),
               scale(mul(row(n+1),row(n+1)),-1),mul(row(n),row(n+2)))

def run():
    one={(0,)*6:F(1)};x={(-1,0,0,0,0,0):F(1),(1,0,0,0,0,0):F(1)}
    u,v,w,z,h=[{tuple(1 if j==i else 0 for j in range(6)):F(1)}for i in range(1,6)]
    def pair(a,b):return add(mul(x,x),mul(add(scale(one,F(5,2)),scale(a,F(1,2))),x),scale(one,F(5,4)),b)
    f,g=pair(u,v),pair(w,z);y=add(x,one)
    middle=add(x,scale(one,F(5,4)),scale(h,F(1,4)))
    inner=mul(add(x,scale(one,F(2,3)),scale(u,F(5,6))),add(x,scale(one,F(3,2)),scale(v,F(1,2))))
    blocks={'y_two_general_pairs':mul(y,mul(f,g)),
            'y_middle_times_pair':mul(y,mul(middle,f)),
            'y_middle_times_two_pairs':mul(y,mul(middle,mul(f,g))),
            'y_isolated_inner_pair':mul(y,inner)}
    src=Path(__file__).with_name('root_boundary_q_results.json')
    certs=json.loads(src.read_text())['blocks'];minima={};count=ndefects=0
    for name,p in blocks.items():
        assert len(certs[name])==max(k[0]for k in p)+1
        minima[name]=[]
        for n,cert in enumerate(certs[name]):
            actual=defect(p,n)
            expected={tuple(map(int,k.split(','))):F(v)for k,v in cert['power_coefficients'].items()}
            assert actual==expected,(name,n,'independent Laurent defect')
            degrees=tuple(cert['degrees'])
            bc={tuple(map(int,k.split(','))):F(v)for k,v in cert['bernstein_coefficients'].items()}
            assert set(bc)==set(product(*(range(d+1)for d in degrees)))
            expanded={}
            for indices,value in bc.items():
                for offsets in product(*(range(d-i+1)for d,i in zip(degrees,indices))):
                    coefficient=value
                    for d,i,a in zip(degrees,indices,offsets):coefficient*=comb(d,i)*comb(d-i,a)*(-1)**a
                    key=tuple(i+a for i,a in zip(indices,offsets));expanded[key]=expanded.get(key,F(0))+coefficient
            expanded={k:v for k,v in expanded.items()if v}
            assert expanded==actual,(name,n,'complete Bernstein reconstruction')
            minimum=min(bc.values());assert minimum>0 and minimum==F(cert['strict_lower_bound'])
            minima[name].append(str(minimum));count+=len(bc);ndefects+=1
    exception=scale(mul(y,y),2)
    assert defect(exception,1)=={}
    return {'status':'PASS_INDEPENDENT_EXACT_FULL_CUBE_RECONSTRUCTION',
            'defects_verified':ndefects,'Bernstein_coefficients_verified':count,'exact_minima':minima,
            'N1_strict_exception_verified':True,'source_results_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
            'imports':'Python standard library only; no producer arithmetic',
            'all_N_scope':'Analytic four-congruence root partition plus these exact continuum block certificates.',
            'full_tree_Local_TP2':'OPEN'}
if __name__=='__main__':
    result=run();Path(__file__).with_name('audit_boundary_q_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
