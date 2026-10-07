#!/usr/bin/env python3
"""Exact paired character diagnostics. Bounded evidence, not closure proof."""
from collections import deque
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from tp2_source import add, sub, scale, mul, H, hget, cubic_residual
from tp2_source import mutation_left, mutation_right
from recovery_fulltree_bivariate_character import predicted_characters as R
from recovery_fulltree_bivariate_character import plus, times, scale as bscale
from recovery_fulltree_bivariate_character import bezoutian, rotate_symmetric
from recovery_fulltree_bivariate_character import to_characters

y = [1, 1]
p = [2, 1]
x = [0, 1]
one = [1]


def tensor(f):
    return R(f, [0] + f)


def mixed(f, g):
    return plus(R(f, [0] + g), R(g, [0] + f))


def difference(a, b):
    return plus(a, bscale(b, -1))


def cprod(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            for ii in range(abs(i-k), i+k+1, 2):
                for jj in range(abs(j-l), j+l+1, 2):
                    out[ii, jj] = out.get((ii, jj), 0) + v*w
    return {k: v for k, v in out.items() if v}


def state(raw):
    X, Y = sorted((raw[0], raw[2]), key=len)
    C = raw[1]
    assert cubic_residual(X, C, Y) == [0]
    t = sub(scale(mul(y, X), 3), x)
    c = sub(scale(mul(y, C), 3), x)
    M = add(c, one)
    E, G = sub(Y, X), sub(C, Y)
    b = mul(y, C)
    S = sub(sub(mul(c, X), Y), b)
    Z = sub(sub(mul(c, Y), X), b)
    D = sub(Z, S)
    assert D == mul(E, M)
    Q = sub(S, G)
    U = mul(mul(X, p), M)
    V = add(mul(p, X), mul(mul(p, p), C))
    assert Q == sub(mul(sub(t, [2]), C), mul(x, X))
    assert U == add(mul(p, Q), V)
    return dict(X=X, Y=Y, C=C, t=t, c=c, M=M, E=E, G=G,
                S=S, Z=Z, D=D, Q=Q, U=U, V=V)


def children(st):
    X, Y, C = st['X'], st['Y'], st['C']
    return [('s', (X, add(C, st['S']), C)),
            ('l', (Y, add(C, st['Z']), C))]


def first_negative(poly):
    bad = [(key, value) for key, value in poly.items() if value < 0]
    return min(bad, default=None)


def proxy(st):
    out = R(st['Q'], st['U'])
    assert out == plus(tensor(st['Q']), R(st['Q'], st['V']))
    return out


def frozen_flux(st, sn, side, algebra_check=False):
    Q, U = st['Q'], st['U']
    E, c = st['E'], st['c']
    F = st['S'] if side == 's' else st['Z']
    X = st['X'] if side == 's' else st['Y']
    A = sub(sub(scale(mul(y, X), 3), x), [2])
    L = scale(mul(mul(y, X), p), 3)
    Hh = [0] if side == 's' else mul(E, c)
    K = [0] if side == 's' else mul(mul(p, E), add(c, one))
    AF, LF = mul(A, F), mul(L, F)
    assert sn['Q'] == add(add(Q, AF), Hh)
    assert sn['U'] == add(add(U, LF), K)
    direct = difference(proxy(sn), proxy(st))
    if algebra_check:
        expanded = plus(plus(R(Q, LF), R(AF, U)),
                        cprod(tensor(F), R(A, L)))
        for term in (R(Q, K), R(Hh, U), R(AF, K), R(Hh, LF), R(Hh, K)):
            expanded = plus(expanded, term)
        assert expanded == direct
    return direct


def check_node(st, path, failures, counts, algebra_check=False):
    G, Hh = st['G'], sub(st['C'], st['X'])
    tests = {'T_G': tensor(G), 'T_H': tensor(Hh), 'J_G_H': mixed(G, Hh),
             'T_M': tensor(st['M']), 'proxy': proxy(st)}
    for side, raw in children(st):
        sn = state(raw)
        tests['flux_' + side] = frozen_flux(st, sn, side, algebra_check)
    for name, poly in tests.items():
        counts[name] = counts.get(name, 0) + 1
        neg = first_negative(poly)
        if neg and name not in failures:
            failures[name] = dict(path=path or 'root', character_index=list(neg[0]),
                                  coefficient=neg[1], degrees={k:len(st[k])-1 for k in ('X','Y','C','Q','U')},
                                  exact_state={k:st[k] for k in ('X','Y','C','Q','U')})
    return tests


def symbolic_root_check(st):
    # Universal symmetric-pair identity checked independently in ordinary
    # bivariate coefficients at the root; the note gives its algebraic proof.
    c, X, Y, b, D = (st[k] for k in ('c','X','Y','C','D'))
    b = mul(y, b)
    tc = bezoutian(c, [0]+c)
    tx, ty = bezoutian(X, [0]+X), bezoutian(Y, [0]+Y)
    result = plus(times(plus(tc, {(0,0):-1}), bezoutian(X,Y)),
                  times(difference(tx,ty), bezoutian(one,c)))
    result = difference(result, bezoutian(b,D))
    assert result == bezoutian(st['S'], st['D'])
    assert to_characters(rotate_symmetric(result)) == R(st['S'], st['D'])


def trace_obstructions():
    root = state(([1],[5,6,2],[2,1]))
    long = state(children(root)[1][1])
    out = []
    for label,st,powers in [('root',root,range(3)),('first-long',long,range(1))]:
        A = sub(st['t'],[2])
        L = scale(mul(mul(y,st['X']),p),3)
        for power in powers:
            factor = [1]
            for _ in range(power):
                factor = mul(factor,y)
            aa,ll = mul(factor,A),mul(factor,L)
            chars = R(aa,ll)
            neg = first_negative(chars)
            assert neg
            out.append(dict(state_label=label,X=st['X'],Y=st['Y'],C=st['C'],
                            Fricke_residual_zero=True,common_y_power=power,
                            first_polynomial=aa,second_polynomial=ll,
                            first_negative_character_index=list(neg[0]),
                            coefficient=neg[1],
                            adjacent=[chars.get((2*n,0),0) for n in range(len(aa))],
                            scope='counterexample to termwise transfer-block positivity only'))
    return out


def run(depth=5, raylength=24):
    root_raw = ([1], [5,6,2], [2,1])
    root = state(root_raw)
    symbolic_root_check(root)
    failures, counts = {}, {}
    queue = deque([('', root_raw)])
    nodes = 0
    while queue:
        path, raw = queue.popleft()
        st = state(raw)
        check_node(st, path or 'root', failures, counts, algebra_check=len(path)<2)
        nodes += 1
        if len(path)<depth:
            queue.extend((path+side, child) for side,child in children(st))
    rayrecords = 0
    for namedside in 'LR':
        raw = root_raw
        for n in range(1, raylength+1):
            A,C,B = raw
            raw = (A,mutation_left(A,C,B),C) if namedside=='L' else (C,mutation_right(A,C,B),B)
            check_node(state(raw), namedside+str(n), failures, counts)
            rayrecords += 1
    root_tests = check_node(root, 'root', {}, {}, algebra_check=True)
    return dict(status='bounded exact diagnostic; no common-closure proof',
                binary_depth=depth, binary_nodes=nodes, named_ray_length=raylength,
                named_ray_records=rayrecords, coefficient_scans=counts, failures=failures,
                root_boundary={key:[v.get((2*n,0),0) for n in range(5)] for key,v in root_tests.items()},
                root_proxy_correction_boundary=[R(root['Q'],root['V']).get((2*n,0),0) for n in range(5)],
                root_proxy_self_boundary=[tensor(root['Q']).get((2*n,0),0) for n in range(5)],
                trace_block_obstructions=trace_obstructions())


if __name__ == '__main__':
    result = run(int(sys.argv[1]) if len(sys.argv)>1 else 5,
                 int(sys.argv[2]) if len(sys.argv)>2 else 24)
    HERE.joinpath('pair_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
