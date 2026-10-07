"""Exact identities and small checks for reduction_additional_turn.md.

Only Python's standard library is used. No parent implementation is
imported. Formal checks are unrestricted identities. The m/ell loops
are implementation checks and are not an infinite proof.
"""
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*polys):
    ans = [0] * max(map(len, polys))
    for p in polys:
        for i, a in enumerate(p):
            ans[i] += a
    return trim(ans)


def scale(p, a):
    return trim([a * t for t in p])


def mul(p, q):
    ans = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            ans[i + j] += a * b
    return trim(ans)


def sub(p, q):
    return add(p, scale(q, -1))


def halfrow(p):
    """Direct binomial Fourier map, independent of mutation code."""
    ans = [0] * len(p)
    for degree, a in enumerate(p):
        for left in range(degree // 2 + 1):
            ans[degree - 2 * left] += a * comb(degree, left)
    return ans


def minors(p, q):
    a, b = halfrow(p), halfrow(q)
    width = max(len(a), len(b))
    a += [0] * (width + 1 - len(a))
    b += [0] * (width + 1 - len(b))
    return [a[n] * b[n + 1] - a[n + 1] * b[n]
            for n in range(width)]


def lr(p, q):
    w = minors(p, q)
    assert min(w) >= 0, (halfrow(p), halfrow(q), w)
    return w


# Tiny independent multivariate ring for formal identities. There are
# four formal variables; ordinary-polynomial checks above use lists.
ZERO = (0, 0, 0, 0)


def fc(a):
    return {ZERO: Fraction(a)} if a else {}


def fv(i):
    e = list(ZERO)
    e[i] = 1
    return {tuple(e): Fraction(1)}


def fa(*polys):
    ans = {}
    for p in polys:
        for e, a in p.items():
            ans[e] = ans.get(e, 0) + a
    return {e: a for e, a in ans.items() if a}


def fs(p, a):
    return {e: a * t for e, t in p.items() if a * t}


def fm(*polys):
    ans = fc(1)
    for p in polys:
        nxt = {}
        for e, a in ans.items():
            for f, b in p.items():
                g = tuple(u + v for u, v in zip(e, f))
                nxt[g] = nxt.get(g, 0) + a * b
        ans = {e: a for e, a in nxt.items() if a}
    return ans


def formal_checks():
    x, c, a, center = [fv(i) for i in range(4)]
    y, p1, z = fa(x, fc(1)), fa(x, fc(2)), fa(fs(x, 2), fc(3))
    d = fa(fm(z, a), fc(1), fs(c, -1))
    p, fixed = fa(fc(1), fm(y, c)), fa(fc(1), fm(y, a))
    t, tau = fa(fs(fm(y, p), 3), fs(x, -1)), fa(fs(fm(y, fixed), 3), fs(x, -1))
    q0 = fa(fm(t, fixed), fc(-1), fs(fm(x, p), -1))
    assert q0 == fa(fm(tau, p), fc(-1), fs(fm(x, fixed), -1))
    assert fa(q0, fs(p, -1)) == fm(y, fa(fm(tau, c), d))
    beta = fm(y, fa(c, d))
    assert beta == fa(fm(z, fixed), fs(p1, -1))
    assert beta == fa(tau, fc(-2), fs(fm(x, fixed), -1))
    j = fm(y, fa(tau, fc(-2)))
    v = fs(fm(y, y, fixed, p1), 3)
    assert v == fa(fm(p1, j), fm(y, p1, p1))

    # Generic R_N=tau R_(N-1)-R_(N-2)+1 identity, with two independent
    # symbolic previous prefixes instead of an outer-index enumeration.
    prev, older = c, center
    nxt = fa(fm(tau, prev), fs(older, -1), fc(1))
    assert fa(nxt, fs(fm(tau, prev), -1), older) == fc(1)

    # Universal child difference: the independent symbols are endpoints
    # X,Y and center C. This requires no canonical constraint.
    endpoint_x, endpoint_y = c, a
    short = fa(fs(fm(y, endpoint_x, center), 3),
               fs(fm(x, fa(endpoint_x, center)), -1), fs(endpoint_y, -1))
    long = fa(fs(fm(y, endpoint_y, center), 3),
              fs(fm(x, fa(endpoint_y, center)), -1), fs(endpoint_x, -1))
    assert fa(long, fs(short, -1)) == fm(
        fa(endpoint_y, fs(endpoint_x, -1)),
        fa(fs(fm(y, center), 3), fs(x, -1), fc(1)))
    return 7


ONE, XVAR, Y, P1, Z = [1], [0, 1], [1, 1], [2, 1], [3, 2]


def mutate(endpoint, other, center):
    return sub(sub(scale(mul(mul(Y, endpoint), center), 3),
                   mul(XVAR, add(endpoint, center))), other)


def move(state, letter):
    left, right, center = state
    if letter == "L":
        return left, center, mutate(left, right, center)
    return center, right, mutate(right, left, center)


def canonical(path):
    state = (ONE, P1, [5, 6, 2])
    for letter in path:
        state = move(state, letter)
    return state


def pure_prefixes(count):
    u, prev = ONE, [0]
    total = [0]
    us, ts, gs = [], [], []
    for _ in range(count):
        total = add(total, u)
        us.append(u)
        ts.append(total)
        gs.append(add(ONE, mul(Y, total)))
        prev, u = u, sub(mul(Z, u), prev)
    return us, ts, gs


def outer_arrays(trace, count):
    v, prev, total = ONE, [0], [0]
    vs, rs = [], []
    for _ in range(count):
        total = add(total, v)
        vs.append(v)
        rs.append(total)
        prev, v = v, sub(mul(trace, v), prev)
    return vs, rs


def main():
    formal_count = formal_checks()
    us, ts, gs = pure_prefixes(16)
    ps = [mul(Y, u) for u in us]
    assert minors(add(ps[0], ps[1]), ps[2]) == [16, 32, 8, 0]
    assert minors(add(scale(ps[0], 2), ps[1]), ps[2]) == [8, 48, 8, 0]
    assert halfrow(ps[2]) == [40, 32, 16, 4]
    record = {"formal_identities": formal_count, "initial_cases": [], "canonical_cases": []}

    for m in range(13):
        p, fixed, c, d = gs[m], gs[m + 1], ts[m], ts[m + 2]
        t = sub(scale(mul(Y, p), 3), XVAR)
        tau = sub(scale(mul(Y, fixed), 3), XVAR)
        qcenter = sub(sub(mul(t, fixed), ONE), mul(XVAR, p))
        beta = mul(Y, add(c, d))
        vs, rs = outer_arrays(tau, 7)
        gaps = [mul(Y, add(mul(c, vs[n]), mul(d, vs[n - 1]) if n else [0]))
                for n in range(7)]
        assert gaps[1] == sub(qcenter, p)
        assert beta == sub(mul(Z, fixed), P1)
        h1 = sub(qcenter, fixed)
        h2 = sub(mutate(p, fixed, qcenter), qcenter)
        old_diff = sub(mutate(fixed, p, qcenter), mutate(p, fixed, qcenter))
        assert gaps[2] == add(h2, old_diff)
        assert gaps[1] == add(h1, ps[m + 1])
        pairs = [(beta, ps[m + 2]), (ps[m + 2], h1),
                 (mul(P1, fixed), h1), (h1, h2), (h2, old_diff),
                 (gaps[1], gaps[2]), (beta, gaps[2]), (h1, gaps[2])]
        for lower, upper in pairs:
            lr(lower, upper)
        record["initial_cases"].append({"m": m, "comparisons": len(pairs)})
        if m == 0:
            assert halfrow(gaps[1]) == [211, 175, 98, 34, 6]
            assert minors(gaps[0], gaps[1])[0] == -36
            record["excluded_q0_time_order"] = {"m": 0, "n": 0, "minor": -36}

        if m > 6:
            continue
        for ell in range(5):
            left, right, center = canonical("L" * m + "R" + "L" * ell)
            n = ell + 1
            zell = add(mul(c, rs[n]), mul(d, rs[n - 1]))
            assert center == add(ONE, mul(Y, zell))
            if ell == 0:
                assert center == sub(mul(tau, p), add(ONE, mul(XVAR, fixed)))
            assert len(center) - 1 == (ell + 2) * (m + 3) - 2
            assert left == fixed
            if ell == 0:
                assert right == p
                continue
            assert right == add(ONE, mul(Y, add(mul(c, rs[n - 1]), mul(d, rs[n - 2]))))
            short = mutate(left, right, center)
            long = mutate(right, left, center)
            assert len(short) < len(long)
            s, e = sub(short, center), sub(right, fixed)
            multiplier = add(scale(mul(Y, center), 3), scale(XVAR, -1), ONE)
            childdiff = sub(long, short)
            assert s == gaps[ell + 2]
            assert childdiff == mul(e, multiplier)
            proxy = mul(mul(Y, sub(tau, [2])), zell)
            assert s == add(proxy, gaps[ell + 1], beta)
            lr(mul(P1, fixed), e)
            lr(s, proxy)
            local = minors(s, childdiff)
            assert min(local[:len(s)]) > 0
            record["canonical_cases"].append({"m": m, "ell": ell,
                "degree_short_gap": len(s) - 1, "min_local_minor": min(local[:len(s)])})

    record["scope"] = "Formal identities plus bounded independent implementation checks; no finite-to-infinite inference."
    output = Path(__file__).with_name("reduction_additional_turn_results.json")
    output.write_text(json.dumps(record, indent=2) + "\n")
    print("PASS: 7 formal identities, 13 initial packages, 28 canonical additional-turn cases")
    print("Excluded q0<=lr q1 assertion has exact minor -36 at m=n=0")
    print("Infinite proof uses manuscript recurrences and cited established ray theorems")


if __name__ == "__main__":
    main()
