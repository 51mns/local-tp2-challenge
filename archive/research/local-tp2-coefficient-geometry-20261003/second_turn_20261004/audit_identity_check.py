#!/usr/bin/env python3
"""Independent ordinary-x reconstruction. No sibling/parent imports."""
from math import comb
from pathlib import Path
import hashlib
import json


def tr(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def plus(*aa):
    n = max(map(len, aa))
    return tr(sum(a[i] if i < len(a) else 0 for a in aa) for i in range(n))


def times(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai * bj
    return tr(c)


def scalar(a, k):
    return tr(k * v for v in a)


def neg(a):
    return scalar(a, -1)


one, x, y, z = (1,), (0, 1), (1, 1), (3, 2)


def U_sequence(trace, count):
    a = [one]
    if count:
        a.append(trace)
    while len(a) <= count:
        a.append(plus(times(trace, a[-1]), neg(a[-2])))
    return a


def mutation(A, C, B):
    return plus(scalar(times(y, times(A, C)), 3),
                neg(times(x, plus(A, C))), neg(B))


def halfrow(a):
    return tuple(sum(a[j]*comb(j, (j-n)//2)
                     for j in range(n, len(a), 2)) for n in range(len(a)))


def minor_values(S, D):
    s, d = halfrow(S), halfrow(D)
    return tuple(s[n]*(d[n+1] if n+1 < len(d) else 0)
                 -(s[n+1] if n+1 < len(s) else 0)*d[n]
                 for n in range(len(s)))


def main():
    records = []
    inner = U_sequence(z, 14)
    T = [plus(*inner[:j+1]) for j in range(len(inner))]
    left_states = [(one, (5, 6, 2), (2, 1))]
    for _ in range(12):
        A0, C0, B0 = left_states[-1]
        left_states.append((A0, mutation(A0, C0, B0), C0))
    for m in range(13):
        c, a, d = T[m:m+3]
        P, X = plus(one, times(y, c)), plus(one, times(y, a))
        assert left_states[m] == (one, X, P)
        tau = plus(scalar(times(y, X), 3), neg(x))
        C1 = mutation(P, X, one)
        assert C1 == plus(times(tau, P), neg(one), neg(times(x, X)))
        assert plus(C1, neg(P)) == times(y, plus(times(tau, c), d))
        uv = U_sequence(tau, 8)
        R = [plus(*uv[:j+1]) for j in range(len(uv))]
        qm2, qm1, current = one, P, C1
        for ell in range(7):
            Z = plus(times(c, R[ell+1]), times(d, R[ell]))
            gap = times(y, plus(times(c, uv[ell+1]), times(d, uv[ell])))
            assert current == plus(one, times(y, Z))
            assert plus(current, neg(qm1)) == gap
            assert len(current)-1 == (ell+2)*(m+3)-2
            low, high = sorted((X, qm1), key=len)
            U, V = mutation(low, current, high), mutation(high, current, low)
            S, D = plus(U, neg(current)), plus(V, neg(U))
            assert plus(high, neg(low)) != (0,)
            assert D == times(plus(high, neg(low)),
                              plus(scalar(times(y, current), 3), neg(y), (2,)))
            if ell == 0:
                assert low == P and high == X
                assert U != mutation(X, current, qm1)
            else:
                assert low == X and high == qm1
                assert S == times(y, plus(times(c, uv[ell+2]), times(d, uv[ell+1])))
                E = plus(times(c, R[ell]), times(d, R[ell-1]), neg(a))
                assert plus(qm1, neg(X)) == times(y, E)
                M = plus((4, 2), scalar(times(times(y, y), Z), 3))
                assert D == times(y, times(E, M))
            values = minor_values(S, D)
            assert min(values) > 0
            records.append({"m": m, "ell": ell,
                            "short_degree": len(S)-1,
                            "actual_local_tp2_minimum": min(values),
                            "minor_digest": hashlib.sha256(str(values).encode()).hexdigest()})
            qm2, qm1, current = qm1, current, mutation(X, current, qm1)
    out = {"scope": "Exact identity/orientation audit, plus bounded direct Local TP2 evidence only.",
           "independence": "No imports from sibling or parent implementations; ordinary-x recurrence and binomial Laurent conversion.",
           "m_range": [0, 12], "ell_range": [0, 6],
           "identity_cases": len(records), "status": "PASS", "records": records}
    target = Path(__file__).with_name("audit_identity_results.json")
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "records"}))


if __name__ == "__main__":
    main()
