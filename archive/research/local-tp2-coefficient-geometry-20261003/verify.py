#!/usr/bin/env python3
"""Exact regression/negative controls. Finite checks are NOT the universal proof.

Run in VS Code's integrated terminal, with this directory open:
    python3 verify.py
Standard library only. Inputs are the frozen recurrence, not source expected data.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import platform
import sys


def clean(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return clean([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def scale(p, c):
    return clean([c * v for v in p])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    p = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            p[i+j] += u*v
    return clean(p)


def power(p, n):
    a = [1]
    for _ in range(n):
        a = mul(a, p)
    return a


def h(p):
    return [sum(p[j] * comb(j, (j-n)//2) for j in range(n, len(p), 2))
            for n in range(len(p))]


def h_laurent(p):
    """Independent Laurent multiplication, without the binomial H formula."""
    acc = defaultdict(int)
    monomial = {0: 1}
    for value in p:
        for n, c in monomial.items():
            acc[n] += value*c
        nxt = defaultdict(int)
        for n, c in monomial.items():
            nxt[n-1] += c
            nxt[n+1] += c
        monomial = nxt
    return [acc[n] for n in range(len(p))]


def get(p, n):
    return p[n] if 0 <= n < len(p) else 0


def f(s, d):
    a, b = h(s), h(d)
    return [a[n]*get(b, n+1)-get(a, n+1)*b[n] for n in range(len(a))]


def child(t, c, z):
    return sub(sub(scale(mul(mul([1, 1], t), c), 3), mul([0, 1], add(t, c))), z)


def positive_difference(t, c, z):
    return add(add(scale(mul(mul([1, 1], sub(t, [1])), c), 3),
                   mul([0, 1], sub(scale(c, 2), t))), sub(scale(c, 2), z))


def mm(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def transpose(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]


def q_child(a, b):
    return mm(mm(transpose(a), [[[3, 3], [-1]], [[1], [0]]]), transpose(b))


def formal_identity_checks():
    """Verify identities over Z[x,T,C,Z], rather than fitted substitutions."""
    def plus(a, b):
        r = defaultdict(int, a)
        for k, v in b.items(): r[k] += v
        return {k:v for k,v in r.items() if v}
    def times(a, b):
        r = defaultdict(int)
        for k,v in a.items():
            for l,w in b.items(): r[tuple(u+t for u,t in zip(k,l))] += v*w
        return {k:v for k,v in r.items() if v}
    def scal(a,k): return {i:k*v for i,v in a.items() if k*v}
    one = {(0,0,0,0):1}
    x,t,c,z = [{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
    y = plus(one,x)
    w = plus(plus(scal(times(times(y,t),c),3),scal(times(x,plus(t,c)),-1)),scal(z,-1))
    rhs = plus(plus(scal(times(times(y,plus(t,scal(one,-1))),c),3),
                    times(x,plus(scal(c,2),scal(t,-1)))),plus(scal(c,2),scal(z,-1)))
    assert plus(plus(w,scal(c,-1)),scal(rhs,-1)) == {}
    wz = plus(plus(scal(times(times(y,z),c),3),scal(times(x,plus(z,c)),-1)),scal(t,-1))
    gap = times(plus(z,scal(t,-1)),plus(plus(scal(times(y,c),3),one),scal(x,-1)))
    assert plus(plus(wz,scal(w,-1)),scal(gap,-1)) == {}
    # Exact affine-trace identity: Fricke residual = [3(x+1)]^2 times
    # the deformed Markov residual, as an identity in four indeterminates.
    lam = scal(y,3)
    aa,bb,cc = [plus(times(lam,p),scal(x,-1)) for p in (t,z,c)]
    tau = times(x,plus(x,scal(one,2)))
    fr = plus(plus(times(aa,aa),times(bb,bb)),times(cc,cc))
    fr = plus(fr,scal(times(times(aa,bb),cc),-1))
    fr = plus(fr,times(tau,plus(plus(aa,bb),cc)))
    fr = plus(fr,times(times(x,x),plus(scal(x,2),scal(one,3))))
    markov = plus(plus(times(t,t),times(z,z)),times(c,c))
    markov = plus(markov,times(x,plus(plus(times(t,z),times(t,c)),times(z,c))))
    markov = plus(markov,scal(times(lam,times(times(t,z),c)),-1))
    assert plus(fr,scal(times(times(lam,lam),markov),-1)) == {}
    return 3


def shape(p):
    hp = h(p)
    # Symmetric Laurent extension makes h[-1]=h[1].
    defects = [hp[n]**2-get(hp, n-1 if n else 1)*get(hp,n+1)
               for n in range(len(hp))] + [0]
    return {'H':hp, 'log_concavity_defects':defects,
            'log_concave':all(v>=0 for v in defects),
            'decreasing_defects':all(a>=b for a,b in zip(defects,defects[1:]))}


def main():
    formal = formal_identity_checks()
    q0 = [[[1],[0]], [[0,-1],[1]]]
    q1 = [[[2,1],[1,1]], [[1],[1]]]
    qc = q_child(q0,q1)
    stack = [('',[1],[5,6,2],[2,1],q0,qc,q1)]
    count = minors = 0
    minimum = terminal = None
    root = None
    while stack:
        path,a,c,b,qa,qc,qb = stack.pop()
        l,r = child(a,c,b),child(b,c,a)
        ql,qr = q_child(qa,qc),q_child(qc,qb)
        assert qc[0][0] == c and ql[0][0] == l and qr[0][0] == r
        for q in (qa,qc,qb,ql,qr):
            assert sub(mul(q[0][0],q[1][1]),mul(q[0][1],q[1][0])) == [1]
            assert sub(q[0][1],q[1][0]) == [0,1]
        for t,z,w in ((a,b,l),(b,a,r)):
            assert sub(w,c) == positive_difference(t,c,z)
            assert all(v>0 for v in sub(w,c))
        u,v = sorted((l,r),key=len)
        x,y = sorted((a,b),key=len)
        s,d = sub(u,c),sub(v,u)
        bracket = sub(add(scale(mul([1,1],c),3),[1]),[0,1])
        assert d == mul(sub(y,x),bracket)
        assert all(v>=2 for v in c)
        assert all(v>=6 for v in bracket) and all(v>=6 for v in d)
        assert s[-1]>=4 and len(d)>len(s)
        assert h(s)==h_laurent(s) and h(d)==h_laurent(d)
        fv = f(s,d)
        assert fv[-1]>=24 and all(v>0 for v in fv)
        count += 1
        minors += len(fv)
        minimum = min(fv+[minimum]) if minimum is not None else min(fv)
        terminal = min(terminal,fv[-1]) if terminal is not None else fv[-1]
        if path=='': root={'S':s,'D':d,'H_S':h(s),'H_D':h(d),'F':fv}
        if len(path)<5:
            stack.append((path+'L',a,l,c,qa,ql,qc))
            stack.append((path+'R',c,r,b,qc,qr,qb))
    controls=[]
    for s,d in ((power([1,1],3),power([1,1],4)),
                ([40,80,50,10],[40,84,58,17,3]),
                ([5,14,13,4],[27,84,95,46,8])):
        ordinary=[get(s,i)*get(d,j)-get(d,i)*get(s,j)
                  for i in range(len(s)) for j in range(i+1,len(d))]
        assert all(v>0 for v in ordinary)
        assert sum(c*(-1)**i for i,c in enumerate(s))==0
        assert sum(c*(-1)**i for i,c in enumerate(d))==0
        assert shape(s)['log_concave'] and shape(d)['log_concave']
        assert f(s,d)[0]<0
        controls.append({'S':s,'D':d,'S_shape':shape(s),'D_shape':shape(d),'F':f(s,d)})
    assert controls[1]['S_shape']['decreasing_defects']
    assert controls[1]['D_shape']['decreasing_defects']
    assert controls[2]['S_shape']['decreasing_defects']
    assert controls[2]['D_shape']['decreasing_defects']
    assert mul(power([1,1],2),[5,4]) == controls[2]['S']
    assert mul(mul(power([1,1],2),[3,2]),[9,4]) == controls[2]['D']
    # Orientation negative control is intentionally incorrect and must be detected.
    assert all(v<0 for v in f(root['S'],scale(root['D'],-1)))
    data={'result':'PASS','arithmetic':'exact Python integers',
          'universal_local_tp2':'NOT_PROVED',
          'scope':'formal identities + bounded depth-5 implementation checks + abstract negative controls',
          'main_sha':'c8e61e0e398f540bc8c5de79663398d689f37473',
          'formal_identities':formal,'depth':5,'nodes':count,'adjacent_minors':minors,
          'minimum_F':minimum,'minimum_terminal_F':terminal,'root':root,
          'abstract_negative_controls_not_canonical_counterexamples':controls,
          'python':sys.version,'platform':platform.platform(),
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))


if __name__=='__main__':
    main()
