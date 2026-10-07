"""Independent reconstruction of four strategically relevant finite witnesses.

No worker module, generated expected output, or old implementation is imported.
The analytic degree/parity theorems require separate manuscript review.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def plus(*args):
    ans = [0] * max(map(len, args))
    for a in args:
        for i, v in enumerate(a):
            ans[i] += v
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def neg(a):
    return [-v for v in a]


def times(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            ans[i + j] += u * v
    return ans


def power(a, n):
    ans = [1]
    for _ in range(n):
        ans = times(ans, a)
    return ans


def row(a):
    return [sum(a[j] * comb(j, (j - n) // 2)
                for j in range(n, len(a), 2)) for n in range(len(a))]


def entry(a, i):
    return a[abs(i)] if abs(i) < len(a) else 0


def minors(a, b):
    aa, bb = row(a), row(b)
    return {(i, j): entry(aa, i) * entry(bb, j) - entry(aa, j) * entry(bb, i)
            for i in range(max(len(aa), len(bb)))
            for j in range(i + 1, max(len(aa), len(bb)))}


def defects(a):
    aa = row(a)
    return [entry(aa, n)**2 - entry(aa, n-1)*entry(aa, n+1)
            - entry(aa, n+1)**2 + entry(aa, n)*entry(aa, n+2)
            for n in range(len(aa))]


def main():
    x, y, P = [0, 1], [1, 1], [2, 1]
    # Genuine first-long parent, reconstructed from explicit normalized tuple.
    a, e, r = [1], [3, 2], [4, 2]
    X = plus([1], times(y, a))
    t = plus(times([3], times(y, X)), neg(x))
    A, h = plus(t, [-2]), plus(t, [-1])
    k = times(X, plus(times([3], X), [-2]))
    g = plus(times(A, e), k, r)
    s = plus(times(t, g), neg(r))
    E, G, S = (times(y, z) for z in (e, g, s))
    C = plus(X, E, G)
    T = plus(times([3], times(y, C)), neg(x))
    M = plus(T, [1])
    D, Q = times(E, M), plus(S, neg(G))
    H = plus(G, neg(times(A, E)))
    B = plus(T, neg(t))
    hD, MH, BS = times(h, D), times(M, H), times(B, S)
    K = plus(MH, BS)
    assert plus(times(r, g), neg(plus(times(A, power(e, 2)),
                 times([2], times(k, e)), times([3], times(a, power(X, 2)))))) == [0]
    factor = minors(times(h, E), plus(E, G))
    negative = minors(hD, MH)
    positive = minors(hD, BS)
    total = minors(hD, K)
    assert factor[0, 1] == -387 and factor[3, 4] == -18
    assert negative[0, 1] == -2218228656 and negative[8, 9] == -5832
    assert positive[0, 1] == 345828343416
    assert total[0, 1] == 343610114760 and min(total.values()) >= 0
    assert all(minors(Q, D)[i, i+1] > 0 for i in range(len(Q)))
    short = dict(domain='actual first-long parent',
                 factor_central=factor[0, 1], source_central=negative[0, 1],
                 coupled_central=total[0, 1], bridge_refuted=False)

    # Actual root parity recombination: negative component, positive whole.
    f, d = [8, 12, 4], [24, 44, 28, 6]
    ordinary01 = f[0]*d[1]-f[1]*d[0]
    transform01 = minors(y, times(y, x))[0, 1]
    root_target = minors(times(y, f), times(y, d))[0, 1]
    assert ordinary01 == 64 and transform01 == -1 and root_target == 272
    parity = dict(domain='actual root', source01=ordinary01,
                  kernel01=transform01, contribution=ordinary01*transform01,
                  whole_target_central=root_target, target_refuted=False)

    # Genuine first-short parent, LONG trace: a failed additive budget.
    aa, ee, rr = [0], [4, 2], [3, 2]
    xx = plus([1], times(y, aa))
    tt = plus(times([3], times(y, xx)), neg(x))
    kk0 = times(xx, plus(times([3], xx), [-2]))
    gg = plus(times(plus(tt, [-2]), ee), kk0, rr)
    ss = plus(times(tt, gg), neg(rr))
    cc = plus(xx, times(y, plus(ee, gg)))
    trace = plus(times([3], times(y, cc)), neg(x))
    beta = times([3], power(y, 2))
    source_a = times(beta, times(gg, plus(tt, [1])))
    source_b = times(beta, times(ee, plus(trace, [1])))
    remainder = plus([5, 2], times(beta, plus(aa, ee, neg(rr))))
    full = plus(source_a, source_b, remainder)
    child_trace = plus(trace, times(beta, plus(ss, times(ee, plus(trace, [1])))))
    assert full == plus(child_trace, [2])
    assert all(min(defects(z)) > 0 for z in (source_a, source_b, remainder))
    at6 = lambda z: defects(z)[6] if len(z) > 6 else 0
    actual = at6(full)
    additive = sum(at6(z) for z in (source_a, source_b, remainder))
    assert actual == 227664 and additive == 229392
    assert actual-additive == -1728
    # A trace shift changes only h_0, while delta_6 uses h_5..h_8.
    assert len(remainder)-1 < 5
    packet = dict(domain='actual first-short parent and its LONG child',
                  actual_defect6=actual, proposed_additive_budget=additive,
                  loss=actual-additive, individually_strict_sources=True,
                  shift_independence='delta_6 uses only rows 5 through 8',
                  additive_budget_refuted=True, child_trace_refuted=False)

    # Actual first-short parent: even the full coupled low-M block is negative.
    old_y = plus(xx, times(y, ee))
    long_h = plus(times([3], times(y, old_y)), neg(x), [-1])
    outgoing = times(y, plus(ss, times(ee, plus(trace, [1]))))
    lower_j = times(y, plus(ee, gg))
    canonical_q = plus(times(long_h, outgoing), neg(lower_j))
    canonical_d = times(times(y, gg), plus(child_trace, [1]))
    low_m = times(times(y, gg), plus(trace, [1]))
    assert minors(canonical_q, low_m)[0, 1] == -1074148800
    assert minors(canonical_d, lower_j)[0, 1] == -49976016
    assert all(minors(canonical_q, canonical_d)[i, i+1] > 0
               for i in range(len(canonical_q)))

    # Noncanonical LONG weak-chain counterexample, including all its premises.
    hh, qq, dd = times(y, plus(times([3], P), [-1])), P, power(P, 4)
    bb = times(hh, qq)
    c7 = [0, -7, 0, 14, 0, -7, 0, 1]
    kk = plus(times(hh, dd), times([F(1, 100)], c7))
    chain = [bb, times(hh, plus(qq, dd)), times(hh, dd), kk]
    for u, v in zip(chain, chain[1:]):
        assert min(minors(u, v).values()) >= 0
    for z in (hh, qq, dd, bb, kk):
        assert all(v > 0 for v in z) and all(v > 0 for v in row(z))
        assert min(defects(z)) >= 0
    assert all(minors(qq, dd)[i, i+1] > 0 for i in range(len(qq)))
    qc, dc = plus(chain[1], bb), plus(chain[2], kk)
    assert len(qc) == 7 and len(dc) == 8
    child_w = [minors(qc, dc)[i, i+1] for i in range(len(qc))]
    assert child_w[4] == child_w[5] == 0 and min(child_w) == 0
    long = dict(domain='relaxed noncanonical weak-chain lemma',
                all_stated_chain_and_cone_premises=True,
                child_adjacent_minors=[str(v) for v in child_w],
                canonical_low_M_central=minors(canonical_q, low_m)[0, 1],
                canonical_subtraction_central=minors(canonical_d, lower_j)[0, 1],
                strict_weak_chain_implication_refuted=True,
                canonical_P0_implication_refuted=False)
    output = dict(status='PASS_INDEPENDENT_FINITE_WITNESS_RECONSTRUCTION',
                  short=short, parity=parity, packet=packet, long=long,
                  full_tree_Local_TP2='OPEN',
                  scope='Finite exact witnesses only; no arbitrary-parent closure or novelty assertion.')
    Path(__file__).with_name('supervisor_witness_results.json').write_text(
        json.dumps(output, indent=2) + '\n')
    print(json.dumps(output))


if __name__ == '__main__':
    main()
