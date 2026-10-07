"""Independent exact checks of two explicitly scoped bridge obstructions.

No audited implementation, adapter, verifier, or expected output is imported.
The universal parity theorem is audited analytically in audit_fresh.md;
this file reconstructs its root witness and the relaxed LONG witness.
"""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


def add(*ps):
    out = [F(0)] * max(map(len, ps))
    for p in ps:
        for i, a in enumerate(p):
            out[i] += a
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(p, a):
    return [F(a) * b for b in p]


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def power(p, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, p)
    return out


def halfrow(p):
    # x=z+z^-1, one contribution per matching binomial coefficient.
    return [sum((a * comb(k, (k-n)//2)
                 for k, a in enumerate(p) if k >= n and (k-n) % 2 == 0), F(0))
            for n in range(len(p))]


def at(row, n):
    n = abs(n)
    return row[n] if n < len(row) else F(0)


def defects(p):
    h = halfrow(p)
    return [at(h, n)**2 - at(h, n-1)*at(h, n+1)
            - at(h, n+1)**2 + at(h, n)*at(h, n+2)
            for n in range(len(h))]


def orders(p, q):
    hp, hq = halfrow(p), halfrow(q)
    n = max(len(hp), len(hq))
    values = [(i, j, at(hp, i)*at(hq, j)-at(hp, j)*at(hq, i))
              for i in range(n) for j in range(i+1, n)]
    return {"minimum": min(v for _, _, v in values),
            "negative": [v for v in values if v[2] < 0],
            "zero_count": sum(v[2] == 0 for v in values),
            "adjacent": [at(hp, i)*at(hq, i+1)-at(hp, i+1)*at(hq, i)
                         for i in range(len(hp))]}


def divide_y(p):
    out = [F(0)] * (len(p)-1)
    out[0] = p[0]
    for i in range(1, len(out)):
        out[i] = p[i] - out[i-1]
    assert p[-1] == out[-1]
    return out


def parity_split(L, R, n=0):
    f, g = divide_y(L), divide_y(R)
    N = max(len(f), len(g))
    sectors = {"even_even": F(0), "odd_odd": F(0), "mixed": F(0)}
    terms = []
    for a in range(N):
        for b in range(a+1, N):
            source = at_coeff(f, a)*at_coeff(g, b)-at_coeff(f, b)*at_coeff(g, a)
            ka = halfrow([F(0)]*a + [F(1), F(1)])
            kb = halfrow([F(0)]*b + [F(1), F(1)])
            kernel = at(ka, n)*at(kb, n+1)-at(ka, n+1)*at(kb, n)
            sector = "mixed" if a % 2 != b % 2 else ("odd_odd" if a % 2 else "even_even")
            sectors[sector] += source * kernel
            terms.append({"powers": [a, b], "source": source,
                          "kernel": kernel, "contribution": source*kernel})
    hL, hR = halfrow(L), halfrow(R)
    actual = at(hL, n)*at(hR, n+1)-at(hL, n+1)*at(hR, n)
    assert sum(sectors.values()) == actual
    return {"L": L, "R": R, "f": f, "g": g,
            "sectors": sectors, "terms": terms, "target": actual}


def at_coeff(p, n):
    return p[n] if n < len(p) else F(0)


def normalized(a, e, r):
    x, y = [F(0), F(1)], [F(1), F(1)]
    X = add([F(1)], mul(y, a))
    t = add(scale(mul(y, X), 3), scale(x, -1))
    k = mul(X, add(scale(X, 3), [F(-2)]))
    g = add(mul(add(t, [F(-2)]), e), k, r)
    Y = add(X, mul(y, e))
    C = add(Y, mul(y, g))
    T = add(scale(mul(y, C), 3), scale(x, -1))
    return X, Y, C, t, g, T


def packet_witness():
    x, y, beta = [F(0), F(1)], [F(1), F(1)], [F(3), F(6), F(3)]
    a0, e0, r0 = [F(0)], [F(1)], [F(1)]
    _, _, _, _, g0, _ = normalized(a0, e0, r0)
    a, e, r = a0, add(e0, g0), g0
    X, Y, C, t, g, T = normalized(a, e, r)
    fricke = add(power(X, 2), power(Y, 2), power(C, 2),
                 mul(x, add(mul(X, Y), mul(Y, C), mul(C, X))),
                 scale(mul(mul(mul(y, X), Y), C), -3))
    assert all(v == 0 for v in fricke)
    s = add(mul(t, g), scale(r, -1))
    d = mul(e, add(T, [F(1)]))
    trace_long_plus2 = add(T, mul(beta, add(s, d)), [F(2)])
    h = add(a, e, scale(r, -1))
    A = mul(mul(beta, g), add(t, [F(1)]))
    B = mul(mul(beta, e), add(T, [F(1)]))
    R = add([F(5), F(2)], mul(beta, h))
    assert add(A, B, R) == trace_long_plus2
    sources = {"A": A, "B": B, "R": R}
    ds = {key: defects(p) for key, p in sources.items()}
    assert all(v > 0 for row in ds.values() for v in row)
    actual = defects(trace_long_plus2)[6]
    budget = sum(at_coeff(row, 6) for row in ds.values())
    return {"canonical_SHORT_parent": {"a": a, "e": e, "r": r},
            "Fricke_residual": fricke, "sources": sources,
            "halfrows": {key: halfrow(p) for key, p in sources.items()},
            "source_defects": ds, "index": 6,
            "actual_defect": actual, "additive_budget": budget,
            "loss": actual-budget}


def canonical_proxy_witnesses():
    x, y = [F(0), F(1)], [F(1), F(1)]
    _, _, _, _, g0, _ = normalized([F(0)], [F(1)], [F(1)])
    states = {"SHORT": ([F(0)], add([F(1)], g0), g0),
              "LONG": ([F(1)], g0, add([F(1)], g0))}
    out = {}
    for label, (a, e, r) in states.items():
        X, Y, C, t, g, T = normalized(a, e, r)
        E, G, R = mul(y, e), mul(y, g), mul(y, r)
        S = add(mul(t, G), scale(R, -1))
        M = add(T, [F(1)])
        D, Q = mul(E, M), add(S, scale(G, -1))
        if label == "SHORT":
            h = add(scale(mul(y, Y), 3), scale(x, -1), [F(-1)])
            Fgap = add(S, D)
            Qchild = add(mul(h, Fgap), scale(add(E, G), -1))
            GM, high = mul(G, M), scale(mul(mul(y, G), Fgap), 3)
            Dchild = add(GM, high)
            out["long_canonical_split"] = {
                "parent": label, "low_center": orders(Qchild, GM)["adjacent"][0],
                "high_center": orders(Qchild, high)["adjacent"][0],
                "total": orders(Qchild, Dchild),
                "subtraction_center": orders(Dchild, add(E, G))["adjacent"][0]}
        else:
            A, h = add(t, [F(-2)]), add(t, [F(-1)])
            H = add(G, scale(mul(A, E), -1))
            hE, E1 = mul(h, E), add(E, G)
            hD, MH = mul(h, D), mul(M, H)
            BS = scale(mul(mul(y, E1), S), 3)
            K = add(MH, BS)
            out["short_canonical_split"] = {
                "parent": label, "endpoint": orders(hE, E1),
                "low_source": orders(hD, MH),
                "high_center": orders(hD, BS)["adjacent"][0],
                "coupled": orders(hD, K)}
    return out


def main():
    x, y, P = [F(0), F(1)], [F(1), F(1)], [F(2), F(1)]
    X, Y, C = [F(1)], P, [F(5), F(6), F(2)]
    U = add(scale(mul(mul(y, X), C), 3), scale(mul(x, add(X, C)), -1), scale(Y, -1))
    V = add(scale(mul(mul(y, Y), C), 3), scale(mul(x, add(Y, C)), -1), scale(X, -1))
    root = parity_split(add(U, scale(C, -1)), add(V, scale(C, -1)))
    relaxed_parity = parity_split(mul(power(y, 2), [F(5), F(4)]),
                                  mul(mul(power(y, 2), [F(3), F(2)]), [F(9), F(4)]))

    # Freeze the strengthened final LONG model with actual endpoint trace.
    C7 = [F(0), F(-7), F(0), F(14), F(0), F(-7), F(0), F(1)]
    h = mul(y, add(scale(P, 3), [F(-1)]))
    Q, D, B = P, power(P, 4), mul(h, P)
    K = add(mul(h, D), scale(C7, F(1, 100)))
    Fh, hD = mul(h, add(Q, D)), mul(h, D)
    Qchild, Dchild = add(Fh, B), add(hD, K)
    ps = {"Q": Q, "D": D, "h": h, "B": B, "K": K,
          "h_QplusD": Fh, "hD": hD, "Qchild": Qchild, "Dchild": Dchild}
    long = {"polynomials": ps,
            "halfrows": {k: halfrow(p) for k, p in ps.items()},
            "defects": {k: defects(p) for k, p in ps.items()},
            "ordinary_coefficients_positive": {k: all(a > 0 for a in p) for k, p in ps.items()},
            "orders": {"Q_D": orders(Q, D), "B_hQplusD": orders(B, Fh),
                       "hQplusD_hD": orders(Fh, hD), "hD_K": orders(hD, K),
                       "Qchild_Dchild": orders(Qchild, Dchild)}}
    assert all(d > 0 for ds in long["defects"].values() for d in ds)
    assert all(all(a > 0 for a in row) for row in long["halfrows"].values())
    assert all(long["ordinary_coefficients_positive"].values())
    assert all(not o["negative"] for o in long["orders"].values())
    assert all(v > 0 for v in long["orders"]["Q_D"]["adjacent"])
    assert long["orders"]["Qchild_Dchild"]["adjacent"][4:6] == [F(0), F(0)]
    # tau-r=h+c, c=1-r in [-1,3]; reconstructed exact defect quadratics.
    shift_samples = {str(c): defects(add(h, [F(c)])) for c in (-1, 0, 1, 3)}
    long["shifted_trace_samples"] = shift_samples
    # delta_0(c)=c^2+25c+26, increasing on [-1,3];
    # delta_1(c)=22-3c, decreasing; delta_2(c)=9.
    assert shift_samples["-1"] == [F(2), F(25), F(9)]
    assert shift_samples["3"] == [F(110), F(13), F(9)]
    long["shifted_trace_exact_minima"] = [F(2), F(13), F(9)]
    long["central_flag"] = defects(add(h, [F(-1)]))[0]
    output = {"scope": "Analytic audit plus exact standalone witness checks; no canonical promotion",
              "parity_root": root, "parity_relaxed": relaxed_parity, "long_relaxed": long,
              "packet_canonical": packet_witness(),
              "canonical_proxy": canonical_proxy_witnesses()}
    path = Path(__file__).with_name("audit_fresh_results.json")
    path.write_text(json.dumps(output, default=lambda v: str(v), indent=2) + "\n")
    print(json.dumps({"root_target": str(root["target"]), "root_sectors": root["sectors"],
                      "relaxed_parity_target": str(relaxed_parity["target"]),
                      "long_child_adjacent": long["orders"]["Qchild_Dchild"]["adjacent"],
                      "all_long_rows_strict_folded": True,
                      "packet_budget_loss": output["packet_canonical"]["loss"]}, default=str))


if __name__ == "__main__":
    main()
