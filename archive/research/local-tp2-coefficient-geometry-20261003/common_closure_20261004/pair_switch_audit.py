#!/usr/bin/env python3
"""Independent exact audit of paired fixed-C switch and coefficient bounds."""
import json
from pathlib import Path
from pair_signed_seed_verify import ONE, add, sub, mul, scale, var, const


def root_row(poly):
    # x remains formal; a=0,e=r=1. Coefficients remain exact integers.
    out = [0]*(max((key[0] for key in poly),default=0)+1)
    for (ix,ia,ie,ir),value in poly.items():
        if ia == 0:
            out[ix] += value
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out


def run():
    x,a,e,r = map(var,range(4))
    y,z = add(x,ONE),add(scale(x,2),const(3))
    X = add(ONE,mul(y,a))
    t = add(z,scale(mul(y,y,a),3))
    k = mul(X,sub(scale(X,3),const(2)))
    g = add(mul(sub(t,const(2)),e),k,r)
    s = sub(mul(t,g),r)
    Z = add(a,e,g)
    C = add(ONE,mul(y,Z))
    T = sub(scale(mul(y,C),3),x)
    M = add(T,ONE)
    d = mul(e,M)
    cA,cB = add(e,g,s),add(g,s,d)
    F = sub(mul(r,g),add(mul(sub(t,const(2)),e,e),
                        scale(mul(k,e),2),scale(mul(a,X,X),3)))
    KC = mul(C,C,add(ONE,scale(Z,3)))
    b = sub(sub(e,a),ONE)
    w = sub(e,mul(sub(z,const(2)),a))
    bound = sub(mul(T,e),cA)
    decomposition = add(scale(mul(y,y,e,e),3),
                        mul(add(scale(mul(x,x),3),scale(x,4)),g),
                        sub(e,k),scale(mul(y,y,b,g),3))
    checks = {
        'trace_T': sub(T,add(t,scale(mul(y,y,add(e,g)),3))),
        'switch_seed': sub(cB,add(cA,mul(T,e))),
        'short_Cassini_residual': add(sub(add(mul(cA,cA),mul(e,add(mul(T,cA),e))),KC),
                                       mul(sub(T,const(2)),F)),
        'long_Cassini_residual': add(sub(sub(mul(cB,cB),mul(e,sub(mul(T,cB),e))),KC),
                                      mul(sub(T,const(2)),F)),
        'b_short_update': sub(sub(sub(add(e,g),a),ONE),add(b,g)),
        'b_long_growth': sub(sub(sub(sub(g,a),e),ONE),
                             add(r,scale(mul(x,e),2),scale(mul(y,y,a,add(a,e)),3),
                                 mul(sub(scale(y,4),ONE),a))),
        'g_minus_k': sub(sub(g,k),add(mul(sub(t,const(2)),e),r)),
        'strong_e_short_update': sub(sub(add(e,g),mul(sub(z,const(2)),a)),add(w,g)),
        'strong_e_long_update': sub(sub(g,mul(sub(z,const(2)),add(a,e))),
                                  add(scale(mul(y,y,a,add(a,e)),3),ONE,mul(z,a),r)),
        'Te_minus_cA': sub(bound,decomposition),
    }
    assert all(not value for value in checks.values())
    root = {key:root_row(value) for key,value in
            [('C',C),('T',T),('e',e),('cA',cA),('cB',cB),('Te_minus_cA',bound)]}
    assert root == {'C':[5,6,2],'T':[15,32,24,6],'e':[1],
                    'cA':[12,14,4],'cB':[27,46,28,6],'Te_minus_cA':[3,18,20,6]}
    # Independent universal Chebyshev normalization in formal T,cA,e.
    tt,ca,ee = var(0),var(1),var(2)
    us = [{},ONE,tt]
    for n in range(2,7):
        us.append(sub(mul(tt,us[-1]),us[-2]))
    qa = [scale(ee,-1),ca]
    cb = add(ca,mul(tt,ee))
    qb = [ee,cb]
    for n in range(0,6):
        if n>=1:
            qa.append(sub(mul(tt,qa[-1]),qa[-2]))
            qb.append(sub(mul(tt,qb[-1]),qb[-2]))
        assert qa[n+1] == add(mul(ca,us[n+1]),mul(ee,us[n]))
        assert qb[n+1] == add(mul(ca,us[n+1]),mul(ee,us[n+2]))
    return dict(status='exact paired-switch algebra and coefficient lemma audited',
                coefficient_ring='Z[x,a,e,r]',symbolic_checks=list(checks),
                root=root,Chebyshev_checks=list(range(6)),
                packet_degree_condition='deg(d0)<deg(c)+deg(T), N>=1',
                forward_root_mapping='recovery_oneturn_closure.md, m=1',
                reversed_root_mapping='second_turn_20261004/kernels_theorem.md, m=0',
                common_packet_closure='OPEN',full_P_Q_connection='OPEN',
                full_tree_Local_TP2='OPEN')


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('pair_switch_audit_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
