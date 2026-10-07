"""Ordinary-polynomial construction from the positive three-variable dynamics.

No original canonical mutation is used in the tree construction. All arithmetic
is integral or Fraction. The bounded tree is regression evidence, not a proof.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p or [0])


def add(*ps):
    out = [0] * max(map(len, ps))
    for p in ps:
        for i, v in enumerate(p):
            out[i] += v
    return trim(out)


def scale(p, c):
    return trim(c * v for v in p)


def sub(p, r):
    return add(p, scale(r, -1))


def mul(*ps):
    out = (1,)
    for p in ps:
        result = [0] * (len(out) + len(p) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(p):
                result[i+j] += a*b
        out = trim(result)
    return out


ONE, x, y = (1,), (0, 1), (1, 1)
BETA = scale(mul(y, y), 3)


def data(u, e, Q):
    X = add(ONE, mul(y, u))
    g = add((1, 2), mul(BETA, u))
    t = add(g, (2,))
    kappa = add(ONE, scale(mul(y, u), 4), mul(BETA, u, u))
    a = add(Q, mul(g, e), kappa)
    Y = add(X, mul(y, e))
    C = add(Y, mul(y, a))
    T = sub(Y, mul(y, Q))
    short_increment = sub(mul(t, a), Q)
    S = mul(y, short_increment)
    D = mul(y, e, add(t, ONE, mul(BETA, add(a, e))))
    R = sub(mul(a, Q), add(mul(g, e, e), scale(mul(kappa, e), 2),
                           scale(mul(u, X, X), 3)))
    return dict(u=u, e=e, Q=Q, a=a, X=X, Y=Y, C=C, T=T, S=S, D=D,
                g=g, t=t, kappa=kappa, R=R)


def step(state, direction):
    u, e, Q = state
    a = data(*state)['a']
    if direction == 's':
        return u, add(a, e), a
    if direction == 'l':
        return add(u, e), a, add(a, e)
    raise ValueError(direction)


def half(p):
    return [sum(p[j] * comb(j, (j-n)//2) for j in range(n, len(p), 2))
            for n in range(len(p))]


def hget(h, n):
    n = abs(n)
    return h[n] if n < len(h) else 0


def defects(h):
    return [hget(h, n)**2 - hget(h, n-1)*hget(h, n+1)
            - hget(h, n+1)**2 + hget(h, n)*hget(h, n+2)
            for n in range(len(h))]


def eta(h):
    if not h or min(h) <= 0:
        raise ValueError('positive interval row required')
    return min(Fraction(d, a*a) for d, a in zip(defects(h), h))


def compact_digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def record(word, state):
    z = data(*state)
    assert z['R'] == (0,)
    assert min(sub(add(z['u'], z['e']), z['Q'])) >= 0
    assert min(sub(z['a'], mul(sub(z['t'], ONE), z['Q']))) >= 0
    for name in ('u', 'e', 'Q', 'a', 'X', 'Y', 'C', 'T', 'S', 'D'):
        assert min(z[name]) >= 0
    rows = {name: half(z[name]) for name in ('u', 'e', 'Q', 'a', 'X', 'Y', 'C', 'T', 'S', 'D')}
    hs, hd = rows['S'], rows['D']
    minors = [hget(hs, n)*hget(hd, n+1)-hget(hs, n+1)*hget(hd, n)
              for n in range(len(hs))]
    assert min(minors) > 0
    correction_bounds=[]
    for name,A,B,tr in (
        ('short',z['a'],scale(z['Q'],-1),z['t']),
        ('long',add(z['a'],z['e']),sub(z['e'],z['Q']),add(z['t'],mul(BETA,z['e']))),
    ):
        assert all(v>=0 for v in B) or all(v<=0 for v in B)
        assert min(add(A,mul(sub(tr,ONE),B)))>=0
        if min(B)<0:
            Qabs=scale(B,-1)
            nu=half(tr)[0]
            denominator=(nu-1)*(nu-2)
            margin=half(sub(mul(A,sub(tr,(2,))),scale(Qabs,denominator)))
            assert min(margin)>=0
            correction_bounds.append(dict(direction=name,nu=str(nu),
                                          epsilon=str(Fraction(1,denominator)),
                                          margin_sha256=compact_digest(margin)))
    return dict(word=word, rows_sha256=compact_digest(rows),
                negative_seed_bounds=correction_bounds,
                degrees={n: len(z[n])-1 for n in ('X','Y','C','S','D')},
                minor_count=len(minors), minimum_minor=str(min(minors)))


def counterexamples():
    P, Q = (3,44,30,3), (2,1)
    PQ = mul(P,Q)
    ps = {'P': P, 'Q': Q, 'PQ': PQ, 'yP': mul(y,P), 'yQ': mul(y,Q)}
    rows = {n: half(v) for n,v in ps.items()}
    ds = {n: defects(v) for n,v in rows.items()}
    assert all(min(v)>0 for v in ds.values())
    ep, eq, epq = (eta(rows[n]) for n in ('P','Q','PQ'))
    before = min(9*ep, eq)
    after = 16*epq
    assert after < before
    # This second input deliberately omits the canonical Fricke constraint.
    fake = data((0,), (23,1), (1,1))
    assert fake['R'] != (0,)
    assert min(sub(fake['a'], mul(sub(fake['t'],ONE), fake['Q']))) >= 0
    hs, hd = half(fake['S']), half(fake['D'])
    f0 = hs[0]*hd[1]-hs[1]*hd[0]
    assert f0 < 0
    return {
        'degree_normalized_margin': {
            'ordinary': {n:list(v) for n,v in ps.items()}, 'half_rows':rows, 'defects':ds,
            'eta': {'P':str(ep),'Q':str(eq),'PQ':str(epq)},
            'before_min':str(before),'after':str(after),'after_over_before':str(after/before),
            'after_minus_before':str(after-before),
            'scope':'Counterexample to the proposed degree-squared minimum-margin rule, not to the existing product theorem or canonical Local TP2.'},
        'off_fricke': {
            'ordinary': {n:list(fake[n]) for n in ('u','e','Q','a','X','Y','C','T','S','D','R')},
            'H_S':hs,'H_D':hd,'F0':f0,
            'scope':'Noncanonical input; Fricke constraint fails and the seed is not folded-cone. Not a counterexample to any full prior extension criterion.'}
    }


def main():
    current = [('', ((0,), ONE, ONE))]
    records=[]
    for depth in range(8):
        following=[]
        for word, state in current:
            records.append(record(word, state))
            if depth<7:
                following.extend((word+d,step(state,d)) for d in ('s','l'))
        current=following
    output={
        'status':'PASS', 'scope':'Formal identities are checked separately; bounded tree regression does not prove full-tree TP2.',
        'depth':7,'state_count':len(records),
        'checked_supported_minors':sum(r['minor_count'] for r in records),
        'records':records,'counterexamples':counterexamples()
    }
    Path('author_results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:output[k] for k in ('status','depth','state_count','checked_supported_minors')}))


if __name__=='__main__':
    main()
