#!/usr/bin/env python3
"""Exact reference-band tests and retained-remainder witnesses.

Standalone integer/Fraction arithmetic.  The finite tests are diagnostics,
not an all-tree or all-minor proof; the latter lemma is proved in the note.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, k):
    return trim([k * v for v in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    z = [0] * (len(p) + len(q) - 1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            z[i+j] += v*w
    return trim(z)


def H(p):
    return trim([sum(p[j] * comb(j, (j-n)//2)
                     for j in range(n, len(p), 2)) for n in range(len(p))])


def at(h, n):
    n = abs(n)
    return h[n] if n < len(h) else 0


def delta(h, n):
    return (at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2
            +at(h,n)*at(h,n+2))


def K(h, i, j):
    if i == 0:
        return at(h,j)
    if j == 0:
        return 2*at(h,i)
    return at(h,i-j)+at(h,i+j)


def minor(h, i, j, k, l):
    return K(h,i,k)*K(h,j,l)-K(h,i,l)*K(h,j,k)


def W(h, g, n):
    return at(h,n)*at(g,n+1)-at(h,n+1)*at(g,n)


def check_proxy_identities(z):
    P1 = [2,1]
    X,C = z['X'],z['C']
    A = sub(scale(mul(Y,X),3),P1)
    L = scale(mul(mul(Y,X),P1),3)
    p = mul([0,1],X)
    v = mul(mul([-1,1],P1),X)
    Q = sub(mul(A,C),p)
    U = mul(mul(X,P1),z['M'])
    assert Q == sub(mul(Y,z['s']),mul(Y,z['g']))
    assert U == sub(mul(L,C),v)
    assert U == add(mul(P1,Q),add(mul(P1,X),mul(mul(P1,P1),C)))
    h,a,l = H(mul(Y,X)),H(A),H(L)
    for n in range(len(a)):
        correction = (6*(at(h,1)+at(h,2)) if n==0 else
                      3*(at(h,1)+2*at(h,2)+at(h,3)) if n==1 else 0)
        assert W(a,l,n) == 9*delta(h,n)-correction
    q = H(Q)
    pq = H(mul(P1,Q))
    assert all(W(q,pq,n)==delta(q,n) for n in range(len(q)))
    return True


def band_constant(h, d):
    assert all(v > 0 for v in h) and 0 <= d < len(h)
    vals = []
    for a in range(d+1):
        vals.append((Fraction(delta(h,a), at(h,a)), 'edge', a))
        vals.append((Fraction(sum(delta(h,k) for k in range(a,a+3)),
                              at(h,a)+at(h,a+2)), 'interior', a))
    return min(vals)


def relative_record(h, b):
    d = len(b)-1
    assert len(h) >= len(b)
    alpha, ai = min((Fraction(h[n], b[n]), n) for n in range(len(b)))
    lam, kind, li = band_constant(h, d)
    global_lam, gi = min((Fraction(delta(h,n),v),n) for n,v in enumerate(h))
    rec = {'reference_degree':d, 'degree':len(h)-1,
           'alpha':str(alpha), 'alpha_index':ai,
           'band_constant':str(lam), 'band_kind':kind, 'band_index':li,
           'global_strength':str(global_lam), 'global_strength_index':gi,
           'band_surplus':str(lam*alpha-8*b[0]),
           'global_surplus':str(global_lam*alpha-8*b[0]),
           'gate':alpha>=2 and lam*alpha>=8*b[0],
           'cone':all(delta(h,n)>=0 for n in range(len(h)))}
    return rec


Y = [1,1]
Y2 = mul(Y,Y)


def state(a=(0,), e=(1,), r=(1,)):
    a,e,r = list(a),list(e),list(r)
    X = add([1],mul(Y,a))
    t = add([3,2],scale(mul(Y2,a),3))
    k = mul(X,add([1],scale(mul(Y,a),3)))
    g = add(add(mul(sub(t,[2]),e),k),r)
    s = sub(mul(t,g),r)
    M = add(add(t,[1]),scale(mul(Y2,add(e,g)),3))
    d = mul(e,M)
    Z = add(add(a,e),g)
    C = add([1],mul(Y,Z))
    YY = add(X,mul(Y,e))
    # Both exact same-variable correlations are checked at every state.
    assert mul(r,g) == add(add(mul(sub(t,[2]),mul(e,e)),
                                  scale(mul(k,e),2)),scale(mul(a,mul(X,X)),3))
    assert sub(mul(g,g),mul(r,s)) == mul(mul(X,X),add([1],scale(a,3)))
    return dict(a=a,e=e,r=r,g=g,s=s,d=d,t=t,X=X,Y=YY,C=C,Z=Z,M=M)


def child(z, side):
    a,e,r,g = (z[k] for k in ['a','e','r','g'])
    zz = state(a,add(e,g),g) if side == 's' else state(add(a,e),g,add(e,g))
    expected_g = z['s'] if side == 's' else add(z['s'],z['d'])
    assert zz['g'] == expected_g
    assert zz['Z'] == add(z['Z'], expected_g)
    return zz


def follow(word):
    z = state()
    for side in word:
        z = child(z,side)
    return z


def remainder(f, g, n):
    c = lambda i:at(f,i)-at(g,i)
    return (at(g,n)*(at(f,n)-at(f,n+2))+at(g,n-1)*at(f,n+1)
            +c(n-1)*at(g,n+1)
            +at(g,n+1)*(at(f,n+1)+c(n+1)))


def bound(f,g,n,lam):
    fn,gn,g2 = at(f,n),at(g,n),at(g,n+2)
    return delta(f,n)-lam*fn-fn*(3*gn+g2)+gn*(gn+g2+lam)


def subtraction_record(z, smooth=False, center=True):
    if center:
        F = mul(z['t'],z['Y'])
        C = z['C']
    else:
        F = mul(z['t'],mul(Y,z['g']))
        C = mul(Y,z['s'])
    G = sub(F,C)
    if smooth:
        F,G,C = (mul(Y,p) for p in (F,G,C))
    f,g,c = H(F),H(G),H(C)
    lam = Fraction(C[-1],2) if smooth or not center else Fraction(C[-1])
    minima = []
    for n in range(len(c)):
        R = remainder(f,g,n)
        B = bound(f,g,n,lam)
        surplus = delta(c,n)-lam*c[n]
        assert surplus == B+R
        assert R >= 0
        if R:
            minima.append((Fraction(surplus,R),n,surplus,R,B))
    frac,n,surplus,R,B = min(minima)
    return {'smooth':smooth, 'center':center, 'strength':str(lam),
            'min_surplus_over_remainder':str(frac), 'index':n,
            'surplus':str(surplus), 'remainder':R, 'coarse_bound':str(B),
            'reserve_1_32_margin':str(surplus-Fraction(R,32)),
            'reserve_1_32_pass':frac>=Fraction(1,32)}


def run(depth):
    records = []
    stack = [('',state())]
    while stack:
        word,z = stack.pop()
        check_proxy_identities(z)
        raw = relative_record(H(z['s']),H(z['r']))
        smooth = relative_record(H(mul(Y,z['s'])),H(mul(Y,z['r'])))
        records.append({'path':word,'raw':raw,'smoothed':smooth})
        if len(word)<depth:
            stack.extend((word+side,child(z,side)) for side in ['l','s'])
    targeted = []
    for word in ['s'*j for j in range(3,41)]+['l'+'s'*12]:
        z = follow(word)
        check_proxy_identities(z)
        targeted.append({'path':word,
                         'raw':relative_record(H(z['s']),H(z['r'])),
                         'smoothed':relative_record(H(mul(Y,z['s'])),H(mul(Y,z['r']))),
                         'center_reserve_raw':subtraction_record(z),
                         'center_reserve_smoothed':subtraction_record(z,True),
                         'gap_short_reserve':subtraction_record(z,False,False)})
    witnesses=[]
    for original,word,mode,kind in [('L6','s'*6,True,'band'),
                                    ('L7','s'*7,False,'band'),
                                    ('R7','l'+'s'*6,True,'band'),
                                    ('R8','l'+'s'*7,False,'band'),
                                    ('L28','s'*28,True,'reserve'),
                                    ('L29','s'*29,False,'reserve')]:
        z=follow(word)
        check_proxy_identities(z)
        h,b=[H(mul(Y,z[k])) if mode else H(z[k]) for k in ['s','r']]
        record=relative_record(h,b) if kind=='band' else subtraction_record(z,mode)
        assert not (record['gate'] if kind=='band' else record['reserve_1_32_pass'])
        witnesses.append({'original_path':original,'ordered_path':word,
                          'kind':kind,'smoothed':mode,'state_polynomials':z,
                          'h':h,'b':b,'record':record})
    z=follow('l'+'s'*12)
    F=mul(z['t'],z['Y'])
    f,g,c=H(F),H(sub(F,z['C'])),H(z['C'])
    old={'original_path':'R13','index':0,'lambda':0,
         'coarse_bound':bound(f,g,0,0),'positive_remainder':remainder(f,g,0),
         'actual_defect':delta(c,0)}
    assert old['coarse_bound']<0<old['actual_defect']
    assert old['coarse_bound']+old['positive_remainder']==old['actual_defect']
    return {'status':'EXACT_BOUNDED_DIAGNOSTIC_NOT_GLOBAL_PROOF',
            'orientation':'s/l are degree-ordered short/long; original R13 is l+s12',
            'depth':depth,'records':records,'targeted':targeted,'frozen_witnesses':witnesses,
            'known_R13_zero_strength_obstruction':old,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--depth',type=int,default=5)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('quantitative_bandwidth_results.json'))
    args=ap.parse_args()
    result=run(args.depth)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    failures=[(r['path'],m) for r in result['targeted'] for m in ['raw','smoothed'] if not r[m]['gate']]
    brief={'status':result['status'],'states':len(result['records']),
           'tree_band_gate_failure_count':sum(not r[m]['gate'] for r in result['records'] for m in ['raw','smoothed']),
           'targeted_band_gate_failure_count':len(failures),
           'first_targeted_failures':failures[:3],
           'first_raw_reserve_failure':next((r['path'] for r in result['targeted'] if not r['center_reserve_raw']['reserve_1_32_pass']),None),
           'first_smoothed_reserve_failure':next((r['path'] for r in result['targeted'] if not r['center_reserve_smoothed']['reserve_1_32_pass']),None)}
    print(json.dumps(brief,indent=2))
