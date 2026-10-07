#!/usr/bin/env python3
"""Exact original Local TP2 bases for LR^k and RL^k, k=1,2,3.

The original recurrence is evaluated independently in ordinary x polynomials
and symmetric Laurent q polynomials.  No research arithmetic helper is imported.
"""
from math import comb
from pathlib import Path
import json


def xa(a, b, sign=1):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += sign * v
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def xm(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return c


def child_x(a, c, b):
    product = [3*v for v in xm(xm([1, 1], a), c)]
    return xa(xa(product, xm([0, 1], xa(a, c)), -1), b, -1)


def half_x(p):
    return [sum(p[j]*comb(j, (j-n)//2) for j in range(n, len(p), 2))
            for n in range(len(p))]


def qa(a, b, sign=1):
    c = dict(a)
    for i, v in b.items():
        c[i] = c.get(i, 0) + sign*v
    return {i: v for i, v in c.items() if v}


def qm(a, b):
    c = {}
    for i, v in a.items():
        for j, w in b.items():
            c[i+j] = c.get(i+j, 0) + v*w
    return {i: v for i, v in c.items() if v}


def child_q(a, c, b):
    # Written directly in q, independent of the ordinary-polynomial code.
    y = {-1: 1, 0: 1, 1: 1}
    x = {-1: 1, 1: 1}
    acy = qm(a, qm(c, y))
    return qa(qa({i: 3*v for i, v in acy.items()},
                 qm(x, qa(a, c)), -1), b, -1)


def half_q(p):
    assert p and all(p.get(-i, 0) == v for i, v in p.items())
    return [p.get(i, 0) for i in range(max(p)+1)]


def at(row, n):
    return row[n] if n < len(row) else 0


def evaluate(path):
    ax, cx, bx = [1], [5, 6, 2], [2, 1]
    aq, cq, bq = {0: 1}, {-2: 2, -1: 6, 0: 9, 1: 6, 2: 2}, {-1: 1, 0: 2, 1: 1}
    for move in path:
        if move == 'L':
            ax, cx, bx = ax, child_x(ax, cx, bx), cx
            aq, cq, bq = aq, child_q(aq, cq, bq), cq
        else:
            ax, cx, bx = cx, child_x(bx, cx, ax), bx
            aq, cq, bq = cq, child_q(bq, cq, aq), bq
    lx, rx = child_x(ax, cx, bx), child_x(bx, cx, ax)
    lq, rq = child_q(aq, cq, bq), child_q(bq, cq, aq)
    assert len(lx) != len(rx) and max(lq) != max(rq)
    ux, vx = sorted([lx, rx], key=len)
    uq, vq = sorted([lq, rq], key=lambda p: max(p))
    sx, dx = xa(ux, cx, -1), xa(vx, ux, -1)
    sq, dq = qa(uq, cq, -1), qa(vq, uq, -1)
    hs, hd = half_x(sx), half_x(dx)
    qs, qd = half_q(sq), half_q(dq)
    assert hs == qs and hd == qd, path
    assert all(v > 0 for v in hs+hd), path
    fs = [hs[n]*at(hd, n+1)-at(hs, n+1)*hd[n] for n in range(len(hs))]
    fq = [sq.get(n, 0)*dq.get(n+1, 0)-sq.get(n+1, 0)*dq.get(n, 0)
          for n in range(max(sq)+1)]
    assert fs == fq and all(v > 0 for v in fs), path
    assert len(dx) > len(sx), path
    return {'path': path, 'degree_S': len(sx)-1, 'degree_D': len(dx)-1,
            'S': sx, 'D': dx, 'H_S': hs, 'H_D': hd, 'F': fs}


def main():
    records = [evaluate(first + repeat*k)
               for first, repeat in [('L', 'R'), ('R', 'L')]
               for k in (1, 2, 3)]
    result = {'status': 'PASS', 'scope': 'Six exact original base states only',
              'methods': ['ordinary x recurrence with binomial Fourier transform',
                          'independent direct Laurent q recurrence'],
              'states': len(records), 'strict_minors': sum(len(r['F']) for r in records),
              'records': records}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))


if __name__ == '__main__':
    main()
