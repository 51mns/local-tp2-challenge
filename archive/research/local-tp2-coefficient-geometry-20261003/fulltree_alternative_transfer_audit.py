"""Targeted exact audit of positive-transfer identities and block obstructions.

No tree scan is performed. This file uses only Python's standard library.
"""
from math import comb
import json


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*v for v in a])


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i+j] += v*w
    return trim(out)


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def H(a):
    return [sum(a[j]*comb(j, (j-n)//2) for j in range(n, len(a), 2))
            for n in range(len(a))]


def total(a):
    return add(add(a[0][0], a[0][1]), add(a[1][0], a[1][1]))


def main():
    R = [[[1], [1]], [[0], [1]]]
    Ri = [[[1], [-1]], [[0], [1]]]
    T = [[[3, 3], [-1]], [[1], [0]]]
    That = mm(mm(transpose(R), T), R)
    assert That == [[[3, 3], [2, 3]], [[4, 3], [3, 3]]]
    seeds = [
        [[[1], [0]], [[0, -1], [1]]],
        [[[2, 1], [1, 1]], [[1], [1]]],
        [[[5, 6, 2], [2, 2]], [[2, 1], [1]]],
    ]
    hats = [mm(mm(Ri, q), transpose(Ri)) for q in seeds]
    assert hats == [
        [[[2, 1], [-1]], [[-1, -1], [1]]],
        [[[1], [0, 1]], [[0], [1]]],
        [[[2, 3, 2], [1, 2]], [[1, 1], [1]]],
    ]
    boundary_transfer = mm(transpose(hats[0]), That)
    assert boundary_transfer == [[[2, 2], [1, 2]], [[1], [1]]]
    assert mm(boundary_transfer, transpose(hats[1])) == hats[2]
    for q, hat in zip(seeds, hats):
        assert q[0][0] == total(hat)
    squared = mm(That, That)
    central = [[H(squared[i][j])[0] for j in range(2)] for i in range(2)]
    assert central == [[53, 48], [60, 53]]
    det_central = central[0][0]*central[1][1]-central[0][1]*central[1][0]
    assert det_central == -71
    cubed_sum = total(mm(squared, That))
    assert cubed_sum == [408, 1272, 1296, 432]
    h = H(cubed_sum)
    assert h == [3000, 2568, 1296, 432]
    central_defect = h[0]**2+h[0]*h[2]-2*h[1]**2
    assert central_defect == -301248
    print(json.dumps({
        'seed_and_congruence_identities': 'pass',
        'coefficient_zero_matrix_of_That_squared': central,
        'its_state_minor': det_central,
        'e_That_cubed_e_ordinary_coefficients': cubed_sum,
        'e_That_cubed_e_half_row': h,
        'its_central_folded_defect': central_defect,
        'tree_scan_performed': False,
    }, indent=2))


if __name__ == '__main__':
    main()
