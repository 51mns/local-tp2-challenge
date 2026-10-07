"""Independent exact audit of the first-difference convolution theorem.

No symbolic algebra or project polynomial code is imported.
The exhaustive checks are finite evidence, separate from the written proof audit.
"""
from itertools import combinations
from fractions import Fraction
import json
import random


def at(h, n):
    n = abs(n)
    return h[n] if n < len(h) else 0


def matrix_entry(h, i, j):
    return at(h, i-j) - at(h, i+j+1)


def invariants(h):
    m = len(h) - 1
    g = [at(h, n)-at(h, n+1) for n in range(m+1)]
    defects = [at(h, n)**2-at(h, n-1)*at(h, n+1)
               for n in range(m+2)]
    delta = [defects[n]-defects[n+1] for n in range(m+1)]
    return g, defects, delta


def ratio_criterion(h):
    g, _, delta = invariants(h)
    return all(delta[n]*g[n+1] >= delta[n+1]*g[n]
               for n in range(len(h)-1))


def minor(h, i, k, j, l):
    return (matrix_entry(h, i, j)*matrix_entry(h, k, l)
            - matrix_entry(h, i, l)*matrix_entry(h, k, j))


def convolve(h, q):
    p = len(h)-1
    r = len(q)-1
    return [sum(at(h, k)*at(q, n-k) for k in range(-p, p+1))
            for n in range(p+r+1)]


def run():
    rows_checked = 0
    accepted = 0
    minors_checked = 0
    boundary_cases = {"a>m": 0, "b=m": 0, "b>m": 0, "interior": 0}
    accepted_examples = []
    for length in range(1, 7):
        for increasing in combinations(range(1, 13), length):
            h = increasing[::-1]
            rows_checked += 1
            criterion = ratio_criterion(h)
            m = length-1
            g, defects, delta = invariants(h)
            nbound = 2*m+3
            for n in range(m):
                assert minor(h, 0, 1, n, n+1)*h[n+1] == (
                    delta[n]*g[n+1]-delta[n+1]*g[n])
            assert minor(h, 0, 1, m, m+1) == h[m]**2
            adjacent_ok = True
            for i in range(nbound-1):
                for j in range(i, nbound-1):
                    a, b = j-i, i+j+1
                    value = minor(h, i, i+1, j, j+1)
                    adjacent_ok = adjacent_ok and value >= 0
                    if a > m:
                        boundary_cases["a>m"] += 1
                        assert value == 0
                    elif b == m:
                        boundary_cases["b=m"] += 1
                        assert value == defects[a]-h[a]*h[m]
                    elif b > m:
                        boundary_cases["b>m"] += 1
                        assert value == defects[a]
                    else:
                        boundary_cases["interior"] += 1
                        fs = [1-Fraction(h[a]*h[b+1], h[k]*h[k+1])
                              for k in range(a, b+1)]
                        assert sum(g[k]*fs[k-a] for k in range(a, b+1)) == 0
                        assert value == sum(delta[k]*fs[k-a] for k in range(a, b+1))
            assert criterion == adjacent_ok, h
            if criterion:
                accepted += 1
                accepted_examples.append(h)
                entries = [[matrix_entry(h, i, j) for j in range(nbound)]
                           for i in range(nbound)]
                for i, k in combinations(range(nbound), 2):
                    for j, l in combinations(range(nbound), 2):
                        minors_checked += 1
                        assert entries[i][j]*entries[k][l] >= entries[i][l]*entries[k][j], (h, i, k, j, l)

    random.seed(231)
    product_checks = 0
    for _ in range(300):
        h = random.choice(accepted_examples)
        q = random.choice(accepted_examples)
        product = convolve(h, q)
        assert all(product[n] > at(product, n+1) for n in range(len(product)))
        assert ratio_criterion(product)
        for i in range(12):
            for j in range(12):
                product_checks += 1
                lhs = matrix_entry(product, i, j)
                rhs = sum(matrix_entry(h, i, k)*matrix_entry(q, k, j)
                          for k in range(i+len(h)))
                assert lhs == rhs, (h, q, i, j)
    result = {
        "all_integer_rows_with_1_to_12_distinct_entries_length_1_to_6": rows_checked,
        "criterion_accepted_rows": accepted,
        "all_ordered_2_by_2_minors_checked_on_accepted_rows": minors_checked,
        "adjacent_formula_cases": boundary_cases,
        "exact_convolution_matrix_entries_checked": product_checks,
        "random_accepted_factor_pairs": 300,
        "status": "pass",
        "qualification": "Finite checks support the independently audited general proof; no canonical infinite-family claim."
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
