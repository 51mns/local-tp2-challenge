"""Exact finite checks of the identities in quantum_applicability.md.

The displayed algebra proves the general identity. The computations below
verify coefficient conventions and root numbers; they are not a tree proof.
"""
from collections import defaultdict
from itertools import product


def torus_product(p, q):
    out = defaultdict(int)
    for (a, b), pc in p.items():
        for (c, d), qc in q.items():
            out[a+c, b+d, a*d-b*c] += pc*qc
    return {k: v for k, v in out.items() if v}


def difference(p, q):
    return {k: p.get(k, 0)-q.get(k, 0) for k in p.keys() | q.keys()
            if p.get(k, 0) != q.get(k, 0)}


def check_identity(s, d):
    a = {(i, 1): c for i, c in enumerate(s) if c}
    b = {(i, 1): c for i, c in enumerate(d) if c}
    lhs = difference(torus_product(b, a), torus_product(a, b))
    rhs = defaultdict(int)
    quotient = defaultdict(int)
    size = max(len(s), len(d))
    s = list(s) + [0]*(size-len(s))
    d = list(d) + [0]*(size-len(d))
    for i in range(size):
        for j in range(i+1, size):
            w = s[i]*d[j]-s[j]*d[i]
            rhs[i+j, 2, j-i] += w
            rhs[i+j, 2, i-j] -= w
            for exponent in range(j-i-1, -(j-i), -2):
                quotient[i+j, exponent] += w
    assert lhs == {k: v for k, v in rhs.items() if v}
    for n in range(size-1):
        assert quotient[2*n+1, 0]-quotient[2*n+1, 2] == s[n]*d[n+1]-s[n+1]*d[n]
    return quotient


def main():
    # Signed arrays verify the general algebra, not only positivity cases.
    checks = 0
    for s in product((-1, 0, 1), repeat=3):
        for d in product((-1, 0, 1), repeat=3):
            check_identity(s, d)
            checks += 1
    s = [40, 32, 16, 4]
    d = [164, 138, 80, 30, 6]
    q = check_identity(s, d)
    assert [q[3, e] for e in (-2, 0, 2)] == [544, 896, 544]
    assert s[1]*d[2] == 2560 and s[2]*d[1] == 2208
    assert s[2]*d[3] == 480 and s[3]*d[2] == 320
    assert 32*240-64*64 == 3584
    print({'algebra_cases': checks, 'root_commutator_N3': [544, 896, 544],
           'root_minor_12': q[3, 0]-q[3, 2], 'naive_lorentzian_hessian_det': 3584,
           'status': 'PASS; no full-tree positivity claim'})


if __name__ == '__main__':
    main()
