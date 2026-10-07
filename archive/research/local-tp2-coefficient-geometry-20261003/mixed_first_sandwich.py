"""Exact identities/base cases for mixed_first_sandwich.md.

The unbounded conditional proof is in the accompanying note. This script
checks its symbolic mutation identity and finite initial data only; it
does not assert the unproved global center hypotheses.
"""
from continuation_prefix import add, const, defects, fourier, mul, scale, variable


def minors(a, b):
    n = max(len(a), len(b))
    a = a + [0] * (n + 1 - len(a))
    b = b + [0] * (n + 1 - len(b))
    return [a[j] * b[j+1] - a[j+1] * b[j] for j in range(n)]


def main():
    x, A, B, C = [variable(j) for j in range(4)]
    y = add(x, const(1))
    tC = add(scale(mul(y, C), 3), scale(x, -1))
    gap = add(scale(mul(mul(y, A), C), 3),
              scale(mul(x, add(A, C)), -1), scale(B, -1), scale(C, -1))
    decomposition = add(mul(add(A, const(-1)), tC),
                        scale(mul(y, C), 2), scale(x, -1), scale(B, -1))
    assert gap == decomposition

    P = add(x, const(2))
    assert defects(P) == [const(2), const(1)]
    assert minors([2, 1], [8, 6, 2]) == [4, 2, 0]
    assert minors([6, 4, 1], [7, 5, 2]) == [2, 3, 0]
    assert all(n >= 0 for n in minors([1], [9, 6, 2]))
    assert all(n >= 0 for n in minors([2, 1], [9, 6, 2]))
    assert minors([2, 1], [1, 1]) == [1, 0]
    print("PASS: exact mutation decomposition, fixed kernel, and root invariants")
    print("Global kernel and scalar hypotheses remain conditional.")


if __name__ == "__main__":
    main()
