#!/usr/bin/env python3
"""Exact full-cube Bernstein certificates for y(U_N-U_(N-1)), N>=2.

The all-N root-pair partition is analytical, from continuation_difference.md.
This program certifies the four bounded-degree residue families, not a scan.
"""
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'continuation_difference.py'
spec = importlib.util.spec_from_file_location('boundary_arithmetic', SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def run():
    Q=m.Q
    x,u,v,w,z,h=[m.variable(i) for i in range(m.DIM)]
    a,mul,c,sc=m.add,m.mul,m.const,m.scale
    x2=mul(x,x); y=a(x,c(1))
    f=a(x2,mul(a(c(Q(5,2)),sc(u,Q(1,2))),x),c(Q(5,4)),v)
    g=a(x2,mul(a(c(Q(5,2)),sc(w,Q(1,2))),x),c(Q(5,4)),z)
    middle=a(x,c(Q(5,4)),sc(h,Q(1,4)))
    inner_a=a(x,c(Q(2,3)),sc(u,Q(5,6)))
    inner_b=a(x,c(Q(3,2)),sc(v,Q(1,2)))
    blocks={
        'y_two_general_pairs':mul(y,mul(f,g)),
        'y_middle_times_pair':mul(y,mul(middle,f)),
        'y_middle_times_two_pairs':mul(y,mul(middle,mul(f,g))),
        'y_isolated_inner_pair':mul(y,mul(inner_a,inner_b)),
    }
    result={}
    for name,p in blocks.items():
        certs=[]
        for n,defect in enumerate(m.defects(p)):
            degrees,coefficients=m.bernstein(defect)
            lower=min(coefficients.values())
            assert lower>0,(name,n,str(lower))
            certs.append(dict(
                n=n, degrees=degrees, strict_lower_bound=str(lower),
                power_coefficients={','.join(map(str,k[1:])):str(v) for k,v in sorted(defect.items())},
                bernstein_coefficients={k:str(v) for k,v in coefficients.items()},
            ))
        result[name]=certs
    return dict(
        status='PASS_EXACT_FULL_PARAMETER_CUBES',
        arithmetic_source='continuation_difference.py',
        arithmetic_source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        blocks=result,
        analytical_scope='Together with the existing all-N root-pair partition and strict product closure, proves strict folded TP2 of y W_N for every N>=2.',
        excluded_N_1='y W_1=2y^2 has delta_1=0; no strict claim.',
        full_tree_Local_TP2='OPEN',
    )

if __name__=='__main__':
    result=run()
    HERE.joinpath('root_boundary_q_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({name:[r['strict_lower_bound'] for r in rows]
                      for name,rows in result['blocks'].items()},indent=2))
