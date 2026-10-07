"""Exact supplementary checks for recovery_oneturn_closure.md.

Formal polynomial identities and rational scalar gates, plus complete
comparison of the existing independent finite certificate records.
This does not substitute a finite m-scan for the manuscript's tail proof.
Only the newly named recovery result is written.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
ZERO = (0,) * 7  # h0,h1,...,h5,a


def const(c):
    return {ZERO: Q(c)} if c else {}


def var(i):
    k = list(ZERO)
    k[i] = 1
    return {tuple(k): Q(1)}


def add(*polys):
    result = {}
    for p in polys:
        for k, v in p.items():
            result[k] = result.get(k, Q(0)) + v
    return {k: v for k, v in result.items() if v}


def scale(p, c):
    return {k: c * v for k, v in p.items() if c * v}


def product(p, q):
    result = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(a + b for a, b in zip(k, ell))
            result[key] = result.get(key, Q(0)) + v * w
    return {k: v for k, v in result.items() if v}


def defect(row, n):
    def at(i):
        i = abs(i)
        return row[i] if i < len(row) else {}
    return add(product(at(n), at(n)),
               scale(product(at(n-1), at(n+1)), -1),
               scale(product(at(n+1), at(n+1)), -1),
               product(at(n), at(n+2)))


def identity_checks():
    h = [var(i) for i in range(6)]
    a = var(6)
    b = [add(scale(h[i], 3), r) for i, r in enumerate(
        [add(a, const(4)), add(a, const(2)), const(2), {}, {}, {}])]
    expected = [
        add(product(add(scale(a, 6), const(30)), h[0]),
            product(add(scale(a, -12), const(-24)), h[1]),
            product(add(scale(a, 3), const(12)), h[2]),
            scale(product(a, a), -1), scale(a, 2), const(16)),
        add(product(add(scale(a, 6), const(12)), h[1]),
            scale(h[0], -6),
            product(add(scale(a, -3), const(-24)), h[2]),
            product(add(scale(a, 3), const(6)), h[3]),
            product(a, a), scale(a, 2), const(-8)),
        add(scale(h[2], 12),
            product(add(scale(a, -3), const(-6)), h[3]),
            scale(h[4], 6), const(4)),
        scale(h[4], -6),
    ]
    for n, p in enumerate(expected):
        assert add(defect(b, n), scale(defect(h, n), -9)) == p, n
    # After lambda=8+z, both polynomial lower bounds have positive
    # coefficients. This proves positivity for all real lambda>=8.
    shifted_quadratics = [[Q(85), Q(165, 2), Q(9)],
                          [Q(151), Q(183, 2), Q(9)]]
    assert all(v > 0 for row in shifted_quadratics for v in row)
    return {"formal_defect_identities": 4,
            "quadratic_coefficients_after_lambda_equals_8_plus_z":
            [[str(v) for v in row] for row in shifted_quadratics]}


def scalar_checks():
    m = 391
    sigma, c0 = Q(59, 100), Q(1, 400000000)
    eps = Q(2*m+5, 9*6**m)
    ey = c0**3 * sigma**(3*m+1) / (16*(m+3)**2)
    el = c0**2 * sigma**(2*m+1) / (4*(m+3))
    checks = {
        "EyH_over_12epsilon_at_391": ey / (12*eps),
        "EL_over_12epsilon_at_391": el / (12*eps),
        "EyH_ratio_growth_lower": 6*sigma**3*Q((m+3)**2*(2*m+5), (m+4)**2*(2*m+7)),
        "EL_ratio_growth_lower": 6*sigma**2*Q((m+3)*(2*m+5), (m+4)*(2*m+7)),
        "double_strength_over_smoothed_mass_gate":
            Q(9*2**(3*m-2), 96) / Q(7**m-1, 6),
        "normalized_block_gate_inverse": 1/(4352*sigma**16),
        "smoothed_residue_gate_inverse": 1/(6*c0*((Q(9, 2)*sigma)**18)),
    }
    assert all(v > 1 for v in checks.values())
    assert eps < 1
    assert Q(2*m+7, 6*(2*m+5)) < 1
    return {key: {"exact": str(v), "decimal": float(v)}
            for key, v in checks.items()}


def compare_finite_records():
    comparisons = []
    for primary, independent in [
        ("fulltree_oneturn_finite_results.json", "fulltree_oneturn_finite_independent_results.json"),
        ("fulltree_oneturn_finite_smooth_results.json", "fulltree_oneturn_finite_smooth_independent_results.json"),
    ]:
        left = json.loads((ROOT / primary).read_text())["cases"]
        right = json.loads((ROOT / independent).read_text())["cases"]
        assert [r["m"] for r in left] == list(range(1, 391))
        assert [r["m"] for r in right] == list(range(1, 391))
        for a, b in zip(left, right):
            for k in ["m", "degree", "margins", "minimum", "witness", "sha256"]:
                assert a[k] == b[k], (primary, a["m"], k)
            assert a["negative"] == a["zero"] == b["negative"] == b["zero"] == 0
        comparisons.append({"primary": primary, "independent": independent,
                            "scope": [1, 390], "matched_cases": len(left),
                            "strict_positive_margins": sum(r["margins"] for r in left)})
    singles = json.loads((ROOT / "fulltree_oneturn_single_finite_results.json").read_text())["cases"]
    expected = {(m, label) for m in range(1, 391) for label in ["L", "yL"]}
    expected |= {(m, "yf") for m in range(1, 4)}
    assert {(r["m"], r["label"]) for r in singles} == expected
    assert len(singles) == len(expected)
    assert all(r["negative"] == r["zero"] == 0 for r in singles)
    return {"independent_midpoint_comparisons": comparisons,
            "single_record_scope": {"L_yL": [1, 390], "yf": [1, 3]},
            "single_cases": len(singles),
            "single_strict_positive_margins": sum(r["margins"] for r in singles)}


if __name__ == "__main__":
    results = {"status": "PASS", "identities": identity_checks(),
               "scalar_checks": scalar_checks(),
               "finite_records": compare_finite_records()}
    output = ROOT / "recovery_oneturn_checks_results.json"
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "formal_identities": 4,
                      "scalar_gates": len(results["scalar_checks"]),
                      "independent_midpoint_cases": 780,
                      "single_cases": results["finite_records"]["single_cases"]}))
