#!/usr/bin/env python3
"""Exact small checks for fulltree_external_bridge.md; no helper imports."""
import json
from pathlib import Path


def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
    return {k: v for k, v in c.items() if v}


def mul(a, b):
    c = {}
    for i, v in a.items():
        for j, w in b.items():
            c[i + j] = c.get(i + j, 0) + v*w
    return {k: v for k, v in c.items() if v}


def scale(a, k):
    return {i: k*v for i, v in a.items() if k*v}


ONE, X = {0: 1}, {-1: 1, 1: 1}
Y = add(ONE, X)


def mutation(a, c, b):
    return add(add(scale(mul(mul(Y, a), c), 3), scale(mul(X, add(a, c)), -1)), scale(b, -1))


def paths(word):
    """Last-tile recurrence for decorated monomer/domino path counts."""
    before, current = {}, ONE
    for alpha, beta in word:
        letter = add(scale(X, alpha), {0: beta})
        before, current = current, add(mul(letter, current), before)
    return current


def autocorrelation(a):
    return [sum(a[k]*a[k+n] for k in range(len(a)-n)) for n in range(len(a))]


def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])


def defects(h):
    get = lambda n: h[abs(n)] if abs(n) < len(h) else 0
    return [get(n)**2-get(n-1)*get(n+1) for n in range(len(h)+1)]


def main():
    b = add(X, {0: 2})
    c = add(add(scale(mul(X, X), 2), scale(X, 6)), {0: 5})
    left, right = mutation(ONE, c, b), mutation(b, c, ONE)
    words = [[(2, 2), (1, 2)], [(2, 2), (0, 1), (1, 1), (2, 2)], [(1, 2), (2, 2), (3, 2), (1, 2)]]
    for word, expected in zip(words, [c, left, right]):
        assert paths(word) == expected
    factor_minor = det3([[4, 5, 2], [2, 4, 5], [0, 2, 4]])
    assert factor_minor == -8
    assert autocorrelation([1, 2, 2]) == [9, 6, 2]
    assert autocorrelation([2, 4, 5, 2]) == [49, 38, 18, 4]
    h = autocorrelation([6, 12, 24, 34, 45, 52, 60])
    delta = defects(h)
    assert delta[1]-delta[2] == -71232
    assert defects([2, 2])[:2] == [0, 4]
    a = [1, 2, 1, 1]
    assert a[2]**2-a[1]*a[3] == -1
    decorated = [[3, 3, 3], [3, 4, 3]]
    decorated_minors = [decorated[0][j]*decorated[1][j+1]-decorated[0][j+1]*decorated[1][j] for j in (0, 1)]
    assert decorated_minors == [3, -3]
    spin_weights = [[9, 6, 4], [6, 6, 6], [4, 6, 9]]
    spin_minors = [spin_weights[i][k]*spin_weights[j][l]-spin_weights[i][l]*spin_weights[j][k]
                   for i in range(3) for j in range(i+1, 3)
                   for k in range(3) for l in range(k+1, 3)]
    assert min(spin_minors) > 0
    spin_row = [sum(spin_weights[i][j] for i in range(3) for j in range(3) if i+j-2 == n) for n in range(3)]
    assert spin_row == [14, 12, 9]
    assert spin_row[1]-spin_row[0] == -2
    spin_delta = defects(spin_row)
    assert all(v >= 0 for v in spin_delta)
    assert spin_delta[1]-spin_delta[2] == -63
    identity_count = 0
    for h in [[9, 6, 2], [49, 38, 18, 4], [213, 176, 98, 34, 6]]:
        get = lambda n: h[abs(n)] if abs(n) < len(h) else 0
        delta = lambda n: get(n)**2-get(n-1)*get(n+1)
        for n in range(len(h)):
            D = det3([[get(n+j-i) for j in range(3)] for i in range(3)])
            assert get(n)*D == delta(n)**2-delta(n-1)*delta(n+1)
            identity_count += 1
    result = {"status": "PASS", "decorated_continuants_checked": 3,
              "spectral_factor_PF3_counterexample": factor_minor,
              "positive_LC_autocorrelation_folded_minor": -71232,
              "seed_letter_folded_minor": -4,
              "multiaffine_diagonal_LC_defect": -1,
              "decorated_connector_adjacent_minors": decorated_minors,
              "ferromagnetic_interaction_min_2minor": min(spin_minors),
              "ferromagnetic_extension_comparison_minor": -2,
              "ferromagnetic_folded_minor": -63,
              "Dodgson_identity_checks": identity_count}
    out = Path(__file__).with_name("fulltree_external_checks.json")
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
