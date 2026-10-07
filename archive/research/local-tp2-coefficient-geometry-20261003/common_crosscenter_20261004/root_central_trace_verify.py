"""Exact formal checks for root_central_trace.md; standard library only."""
from pathlib import Path
import json

N = 7
ZERO = (0,) * N


def const(c):
    return {ZERO: c} if c else {}


def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): 1}


def add(*items):
    out = {}
    for item in items:
        for key, value in item.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def scale(item, scalar):
    return {key: value * scalar for key, value in item.items() if value * scalar}


def mul(*items):
    out = const(1)
    for item in items:
        temp = {}
        for ka, va in out.items():
            for kb, vb in item.items():
                key = tuple(a + b for a, b in zip(ka, kb))
                temp[key] = temp.get(key, 0) + va * vb
        out = {key: value for key, value in temp.items() if value}
    return out


def sub(a, b):
    return add(a, scale(b, -1))


def square(a):
    return mul(a, a)


def defect(a):
    return sub(mul(a[0], add(a[0], a[2])), scale(square(a[1]), 2))


def polar(a, b):
    return add(scale(mul(a[0], b[0]), 2), mul(a[0], b[2]),
               mul(a[2], b[0]), scale(mul(a[1], b[1]), -4))


def main():
    a = [var(i) for i in range(3)]
    b = [var(i) for i in range(3, 6)]
    r = var(6)
    checks = []
    assert defect([add(x, y) for x, y in zip(a, b)]) == add(defect(a), defect(b), polar(a, b))
    checks.append('central polarization')
    lhs = add(mul(a[0], add(b[0], b[2])), mul(b[0], add(a[0], a[2])))
    product = mul(a[0], add(a[0], a[2]), b[0], add(b[0], b[2]))
    assert sub(square(lhs), scale(product, 4)) == square(sub(mul(a[0], b[2]), mul(a[2], b[0])))
    checks.append('AMGM square identity')
    linear = add(scale(a[0], 438), scale(a[1], -600), scale(a[2], 183))
    assert scale(mul(a[0], linear), 61) == add(
        scale(square(sub(scale(a[1], 61), scale(a[0], 50))), 6),
        scale(square(a[0]), 555), scale(defect(a), 11163))
    checks.append('rational central strength SOS')
    root = [const(61), const(50), const(24)]
    assert defect(root) == const(185)
    assert defect([add(z, scale(u, 3)) for z, u in zip(root, a)]) == add(const(185), scale(defect(a), 9), linear)
    checks.append('translated root central defect')
    shifted = [sub(scale(a[0], 3), r), sub(scale(a[1], 3), const(1)), scale(a[2], 3)]
    shift_two = [sub(scale(a[0], 3), const(2)), shifted[1], shifted[2]]
    assert sub(defect(shifted), defect(shift_two)) == mul(
        sub(const(2), r), sub(add(scale(a[0], 6), scale(a[2], 3)), add(r, const(2))))
    checks.append('exact entire shift interval reduction')
    row = [3, 2, 1]
    def h(i):
        return row[abs(i)] if abs(i) < len(row) else 0
    defects = [h(i)**2-h(i-1)*h(i+1)-h(i+1)**2+h(i)*h(i+2) for i in range(len(row))]
    assert defects == [4, 0, 1]
    checks.append('weak y squared factor')
    result = {
        'status': 'PASS_EXACT_FORMAL_IDENTITIES', 'checks': checks,
        'arithmetic': 'Python arbitrary precision integer sparse polynomial ring',
        'y_squared_halfrow': row, 'y_squared_defects': defects,
        'root_trace_shift2_halfrow': [61, 50, 24, 6],
        'root_central_lower_bound': 185,
        'translated_cone_linear_lower_bound': '555/61 times u0',
        'scope': 'Analytic note proves arbitrary BOTH central trace preservation; formal checks alone do not prove packet closure.',
        'full_tree_Local_TP2': 'OPEN',
    }
    Path(__file__).with_name('root_central_trace_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
