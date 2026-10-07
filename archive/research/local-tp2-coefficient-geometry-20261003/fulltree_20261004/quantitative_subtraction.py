#!/usr/bin/env python3
"""Exact subtraction identity and explicitly finite canonical diagnostics."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tp2_source import H, add, sub, mul, scale, generate_tree, G0, G12, G1, mutation_right


def at(h, n):
    n = abs(n)
    return h[n] if n < len(h) else 0


def defect(h, n):
    return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)


def bound(f, g, n, lam=0):
    fn,gn,g2=at(f,n),at(g,n),at(g,n+2)
    return defect(f,n)-lam*fn-fn*(3*gn+g2)+gn*(gn+g2+lam)


def residual(f, g, n):
    c=lambda i:at(f,i)-at(g,i)
    return (at(g,n)*(at(f,n)-at(f,n+2))
            +at(g,n-1)*at(f,n+1)
            +c(n-1)*at(g,n+1)
            +at(g,n+1)*(at(f,n+1)+c(n+1)))


def run(depth):
    result={"status":"FINITE_DIAGNOSTIC_NOT_GLOBAL_PROOF","depth":depth,"records":[]}
    for r in generate_tree(depth):
        X,Y=sorted((r['A'],r['B']),key=len)
        t=sub(scale(mul([1,1],X),3),[0,1])
        F=mul(t,Y); G=sub(F,r['C'])
        for smooth in (False,True):
            p,q,c=(mul([1,1],z) for z in (F,G,r['C'])) if smooth else (F,G,r['C'])
            f,g,h=H(p),H(q),H(c)
            assert len(f)==len(h)
            assert all(at(f,n)-at(g,n)==at(h,n) for n in range(len(f)))
            assert all(at(f,n)>=at(f,n+1)>=0 for n in range(len(f)))
            assert min(g)>=0 and min(h)>0
            lam=c[-1]
            margins=[bound(f,g,n,lam) for n in range(len(f))]
            for n in range(len(f)):
                assert defect(h,n)-lam*at(h,n)==margins[n]+residual(f,g,n)
                assert residual(f,g,n)>=0
            d=len(g)-1
            assert defect(h,d+1)==defect(f,d+1)+at(g,d)*at(f,d+2)
            assert all(defect(h,n)==defect(f,n) for n in range(d+2,len(f)))
            bad=[n for n,v in enumerate(margins) if v<0]
            result['records'].append({"path":r['path'],"smooth":smooth,"degree_X":len(X)-1,
                "degree_Y":len(Y)-1,"degree_C":len(c)-1,"strength":lam,
                "negative_bound_indices":bad,"minimum_bound":min(margins),
                "actual_optimal_strength":min(defect(h,n)-lam*h[n] for n in range(len(h)))>=0})
    nonboundary=[r for r in result['records'] if r['degree_X']>0]
    result['nonboundary_records']=len(nonboundary)
    result['all_nonboundary_bounds_nonnegative']=all(not r['negative_bound_indices'] for r in nonboundary)
    result['all_actual_optimal_strength_checks_pass']=all(r['actual_optimal_strength'] for r in result['records'])
    result['failing_bound_paths']=sorted({r['path'] for r in result['records'] if r['negative_bound_indices']})
    A,C,E=G0,G12,G1
    for _ in range(13):
        A,C,E=C,mutation_right(A,C,E),E
    X,Y=sorted((A,E),key=len)
    F=mul(sub(scale(mul([1,1],X),3),[0,1]),Y);G=sub(F,C)
    f,g,h=H(F),H(G),H(C)
    obstruction={"path":"R"*13,"index":0,"lambda":0,
        "bound":bound(f,g,0),"nonnegative_remainder":residual(f,g,0),
        "actual_defect":defect(h,0)}
    assert obstruction['bound']<0<obstruction['actual_defect']
    assert obstruction['bound']+obstruction['nonnegative_remainder']==obstruction['actual_defect']
    result['canonical_obstruction_to_global_sufficient_bound']=obstruction
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--depth',type=int,default=6)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('quantitative_subtraction_results.json'))
    args=ap.parse_args();res=run(args.depth);args.output.write_text(json.dumps(res,indent=2)+'\n')
    print(json.dumps({k:v for k,v in res.items() if k!='records'},indent=2))
