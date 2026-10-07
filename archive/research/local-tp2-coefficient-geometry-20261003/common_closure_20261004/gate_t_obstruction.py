#!/usr/bin/env python3
"""Exact auxiliary off-Fricke obstruction; not a failure of P_Q closure.

Imports the current campaign's independent arithmetic foundation only.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from falsification_probe import (add,sub,scale,mul,build,children,H,defects,
                                 minors,y,y2,P1)

def gates(v):
    X,Y=(v[k] for k in ('X','Y'))
    E,G,R,S=(mul(y,v[k]) for k in ('e','g','r','s'))
    M=add(scale(P1,2),scale(mul(y2,add(v['a'],v['e'],v['g'])),3))
    Q=sub(S,G);Pi=mul(mul(X,P1),M)
    rows={'E':E,'G':G,'R':R,'S':S,'M':M,'Q':Q,'Pi':Pi}
    tests={
        'E_G':minors(H(E),H(G)),
        'R_G':minors(H(R),H(G)),
        'XP_E':minors(H(mul(X,P1)),H(E)),
        'YP_G':minors(H(mul(Y,P1)),H(G)),
        'G_fold':defects(H(G)),
        'M_fold':defects(H(M)),
        'proxy':minors(H(Q),H(Pi))[:len(Q)],
    }
    assert all(min(H(p))>0 for p in rows.values())
    assert all(min(ds)>=0 for key,ds in tests.items() if key!='proxy')
    assert min(tests['proxy'])>0
    a,e,r,g=(v[k] for k in ('a','e','r','g'))
    bounds={'a_positive':min(a),'e_minus_a':min(sub(e,a)),
            'a_plus_e_minus_r':min(sub(add(a,e),r)),
            'g_minus_lower_bound':min(sub(g,add(a,e,r,[1])))}
    assert all(val>=0 for val in bounds.values()) and min(r)>0
    assert len(v['X'])<len(v['Y'])<len(v['C'])
    return {'bounds':bounds,'rows':{k:H(p) for k,p in rows.items()},'tests':tests}

def main():
    a=[0,0,1];e=[1,5,11,10,5,1];r=scale(add(a,e),F(1,2))
    v=build(a,e,r)
    parent=gates(v);ch={side:gates(w) for side,w in children(v)}
    dt=defects(H(v['t']))
    assert dt==[334,-110,114,-18,9]
    assert defects(H(v['X']))==[-6,8,-3,1]
    assert defects(H(mul(y,v['X'])))==[28,-7,12,-2,1]
    residual=sub(mul(r,v['g']),add(mul(sub(v['t'],[2]),mul(e,e)),
                  scale(mul(v['k'],e),2),scale(mul(a,mul(v['X'],v['X'])),3)))
    assert residual!=[0]
    result={'classification':'Auxiliary generic implication is false: ordinary bounds + P_Q do not imply K_t TP2. Not a canonical state and not a P_Q child failure.',
            'a':a,'e':e,'r':r,'t':v['t'],'H_t':H(v['t']),
            'delta_t':dt,'Fricke_residual':residual,'parent':parent,'children':ch,
            'X':v['X'],'H_X':H(v['X']),'delta_X':defects(H(v['X'])),
            'H_yX':H(mul(y,v['X'])),'delta_yX':defects(H(mul(y,v['X']))),
            'imports':['falsification_probe.py exact polynomial/Fraction arithmetic'],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('gate_t_obstruction_results.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps({k:result[k] for k in ['classification','a','e','r','t','H_t','delta_t','Fricke_residual']},indent=2,default=str))
if __name__=='__main__':main()
