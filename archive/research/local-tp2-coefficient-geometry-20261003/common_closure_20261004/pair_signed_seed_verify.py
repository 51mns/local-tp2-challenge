#!/usr/bin/env python3
"""Independent exact Z[x,a,e,r] check of signed endpoint seed identities."""
import json
from pathlib import Path

N = 4
ONE = {(0,)*N: 1}

def add(*ps):
    out = {}
    for p in ps:
        for key, value in p.items():
            out[key] = out.get(key, 0)+value
    return {k:v for k,v in out.items() if v}

def scale(p, n):
    return {k:n*v for k,v in p.items() if n*v}

def sub(p, q):
    return add(p, scale(q, -1))

def mul(*ps):
    out = ONE
    for p in ps:
        tmp = {}
        for k, v in out.items():
            for l, w in p.items():
                key = tuple(ki+li for ki,li in zip(k,l))
                tmp[key] = tmp.get(key, 0)+v*w
        out = {k:v for k,v in tmp.items() if v}
    return out

def var(n):
    k = [0]*N
    k[n] = 1
    return {tuple(k):1}

def const(n):
    return scale(ONE, n)

def run():
    x,a,e,r = map(var, range(N))
    y = add(x, ONE)
    X = add(ONE, mul(y,a))
    Y = add(X,mul(y,e))
    t = add(scale(x,2),const(3),scale(mul(y,y,a),3))
    k = mul(X,sub(scale(X,3),const(2)))
    g = add(mul(sub(t,const(2)),e),k,r)
    s = sub(mul(t,g),r)
    tau = add(t,scale(mul(y,y,e),3))
    c = add(e,g)
    eta = sub(e,r)
    d = mul(e,add(t,ONE,scale(mul(y,y,c),3)))
    q1 = add(s,d)
    F = sub(mul(r,g),add(mul(sub(t,const(2)),e,e),
                        scale(mul(k,e),2),scale(mul(a,X,X),3)))
    checks = {
        'signed_seed_q1': sub(q1,add(mul(tau,c),eta)),
        'short_eta_update': sub(sub(add(e,g),g),e),
        'long_eta_update': add(sub(g,add(e,g)),e),
        'signed_Cassini_residual': add(sub(add(mul(c,c),mul(eta,q1)),
                                                mul(Y,Y,add(ONE,scale(add(a,e),3)))),
                                       mul(sub(tau,const(2)),F)),
        'fixed_X_Cassini_residual': add(sub(sub(mul(g,g),mul(r,s)),
                                            mul(X,X,add(ONE,scale(a,3)))),
                                       mul(sub(t,const(2)),F)),
    }
    assert all(not p for p in checks.values())
    # U_-1=0, U_0=1, U_1=tau, U_N=tau U_(N-1)-U_(N-2).
    us = [{},ONE,tau]
    qs = [scale(eta,-1),c,q1]
    for n in range(2,6):
        us.append(sub(mul(tau,us[-1]),us[-2]))
        formula = add(mul(c,us[n+1]),mul(eta,us[n]))
        recurrence = sub(mul(tau,qs[-1]),qs[-2])
        assert formula == recurrence
        qs.append(formula)
    return dict(status='exact universal polynomial identities passed',
                coefficient_ring='Z[x,a,e,r]', symbolic_checks=list(checks),
                Chebyshev_initial_normalization_checks=list(range(0,6)),
                scope='algebraic audit only; no Fourier positivity assertion')

if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('pair_signed_seed_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
