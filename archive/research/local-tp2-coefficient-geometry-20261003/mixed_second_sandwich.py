"""Exact checks for the identities and canonical shortcut obstruction.

The global induction and the conditional upper-band theorem are proved
algebraically in mixed_second_sandwich.md, not by these finite checks.
"""
import json
from pathlib import Path
import canonical_arithmetic as p


def alpha(poly):
    row = p.H(poly) + [0]
    return [a - b for a, b in zip(row, row[1:])]


def main():
    one, x, y, P = [1], [0, 1], [1, 1], [2, 1]
    A, C, B = p.G0, p.G12, p.G1
    centers = []
    for move in ['L', 'R']:
        centers.append((A, C, B))
        if move == 'L':
            A, C, B = A, p.mutation_left(A, C, B), C
        else:
            A, C, B = C, p.mutation_right(A, C, B), B
    centers.append((A, C, B))
    checks = []
    for A, C, B in centers:
        X, Y = sorted((A, B), key=len)
        U = p.mutation_left(X, C, Y)
        S = p.sub(U, C)
        M = p.add(p.sub(p.scale(p.mul(y, C), 3), x), one)
        R = p.sub(p.add(p.add(p.scale(X, 3), p.scale(Y, 3)), x), one)
        assert p.scale(S, 3) == p.sub(p.mul(p.sub(p.scale(X, 3), one), M), R)
        assert p.scale(S, 3) == p.add(p.mul(p.sub(p.scale(X, 3), [2]), M), p.sub(M, R))
        assert all(v > 0 for v in alpha(p.sub(p.sub(C, A), B)))
        assert all(v > 0 for v in alpha(R))
        assert all(v > 0 for v in alpha(p.sub(M, R)))
        lhs = p.sub(p.sub(U, X), C)
        bracket = p.sub(p.mul(p.sub(p.scale(y, 2), one), C), y)
        rhs = p.add(p.add(bracket, p.sub(C, Y)),
                    p.mul(p.mul(y, p.sub(X, one)), p.sub(p.scale(C, 3), one)))
        assert lhs == rhs
        checks.append({'degree_C': len(C)-1, 'degree_Y': len(Y)-1,
                       'old_cutoff': len(C)+1, 'new_cutoff': len(Y)})
    XM = p.mul(X, M)
    obstruction = p.f_values(U, XM)[0]
    convolved = p.f_values(p.mul(P, U), p.mul(P, XM))[0]
    assert obstruction == -197848930
    assert convolved == -2520809814
    result = {'status': 'PASS', 'scope': 'identity examples and exact obstruction only',
              'identity_examples': checks,
              'path_LR_false_U_to_XM_minor': obstruction,
              'path_LR_false_PU_to_PXM_minor': convolved}
    Path('mixed_second_sandwich_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
