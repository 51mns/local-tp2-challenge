#!/usr/bin/env python3
"""Exact internal checks of mixed-tensor identities and canonical obstructions."""
from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tp2_source import H, add, hget, generate_tree, cubic_residual
from recovery_fulltree_bivariate_character import (
    predicted_characters, rotate_symmetric, to_characters,
)


def doubled_mixed(p, q):
    a = predicted_characters(p, [0] + q)
    b = predicted_characters(q, [0] + p)
    return {key: a.get(key, 0) + b.get(key, 0)
            for key in a.keys() | b.keys()
            if a.get(key, 0) + b.get(key, 0)}


def direct_doubled_mixed(p, q):
    out = {}
    for i in range(max(len(p), len(q))):
        for j in range(max(len(p), len(q))):
            v = hget(p, i) * hget(q, j) + hget(q, i) * hget(p, j)
            if v:
                out[i, j] = v
    return to_characters(rotate_symmetric(out))


def defect(row, n):
    f = lambda i: hget(row, abs(i))
    return f(n)**2 - f(n-1)*f(n+1) - f(n+1)**2 + f(n)*f(n+2)


def mixed_boundary(p, q, n):
    h, k = H(p), H(q)
    f, g = lambda i: hget(h, abs(i)), lambda i: hget(k, abs(i))
    return (2*f(n)*g(n) - f(n-1)*g(n+1) - g(n-1)*f(n+1)
            - 2*f(n+1)*g(n+1) + f(n)*g(n+2) + g(n)*f(n+2))


def check():
    # A finite normalization check only. The all-degree arguments are in the note.
    count = 0
    for i in range(6):
        for j in range(6):
            p, q = [0]*i+[1], [0]*j+[1]
            m = doubled_mixed(p, q)
            assert m == direct_doubled_mixed(p, q)
            for n in range(max(i, j)+2):
                cross = mixed_boundary(p, q, n)
                assert m.get((2*n, 0), 0) == cross
                assert defect(H(add(p,q)), n) == defect(H(p), n)+defect(H(q), n)+cross
            count += 1

    examples = []
    recs = {rec['path']: rec for rec in generate_tree(1)}
    root = recs['']
    assert cubic_residual(root['A'], root['C'], root['B']) == [0]
    assert root['C'] == [5, 6, 2]
    assert root['S'] == [8, 20, 16, 4]
    assert root['D'] == [16, 48, 56, 30, 6]
    p, q = root['C'], root['D']
    for f in (p, q):
        assert all(v >= 0 for v in predicted_characters(f, [0]+f).values())
    assert all(v >= 0 for v in predicted_characters(p, q).values())

    for path, names in [('', ('C', 'D')), ('L', ('S', 'D'))]:
        rec = recs[path]
        p, q = (rec[name] for name in names)
        pdegree = len(p)-1
        assert len(q)-1 >= pdegree+2
        assert cubic_residual(rec['A'], rec['C'], rec['B']) == [0]
        expected = -p[-1]*H(q)[pdegree+2]
        cross = doubled_mixed(p, q)
        assert cross[(2*pdegree+2, 0)] == expected < 0
        assert defect(H(add(p,q)), pdegree+1) == defect(H(q), pdegree+1)+expected
        for n in range(pdegree+2, len(q)+2):
            assert defect(H(add(p,q)), n) == defect(H(q), n)
        assert all(v >= 0 for v in predicted_characters(rec['S'],rec['D']).values())
        examples.append({
            'path': path or 'root', 'pair': names,
            'degrees': [len(p)-1,len(q)-1],
            'character_index': [2*pdegree+2,0],
            'doubled_mixed_coefficient': expected,
            'fricke_residual_zero': True,
            'target_R_S_D_nonnegative_in_this_example': True,
        })
    assert examples[0]['doubled_mixed_coefficient'] == -12
    assert examples[1]['doubled_mixed_coefficient'] == -192
    return {
        'status': 'exact_internal_identity_checks_passed; no_fulltree_proof',
        'monomial_pair_checks': count,
        'canonical_obstructions': examples,
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
