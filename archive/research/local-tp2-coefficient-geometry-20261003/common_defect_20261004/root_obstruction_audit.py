"""Independent exact audit of the ordinary-positive trace obstruction."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def plus(a, b):
    return [sum(p[i] if i < len(p) else 0 for p in (a, b))
            for i in range(max(len(a), len(b)))]


def times(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] += u*v
    return out


def power(a, n):
    out = [1]
    for _ in range(n):
        out = times(out, a)
    return out


def row(a):
    return [sum(a[j] * comb(j, (j-i)//2)
                for j in range(i, len(a), 2)) for i in range(len(a))]


def value(h, j):
    return h[abs(j)] if abs(j) < len(h) else 0


def defect(h, j):
    return (value(h, j)**2 - value(h, j-1)*value(h, j+1)
            - value(h, j+1)**2 + value(h, j)*value(h, j+2))


def first_rows_minor(h, k, l):
    xh = lambda j: value(h, j-1)+value(h, j+1)
    return value(h, k)*xh(l)-value(h, l)*xh(k)


def minimum_quadratic(values):
    fm, f0, fp = map(Fraction, values)
    a, b, c = (fm+fp-2*f0)/2, (fp-fm)/2, f0
    candidates = [(Fraction(-2), 4*a-2*b+c),
                  (Fraction(2), 4*a+2*b+c)]
    if a > 0 and -2 <= -b/(2*a) <= 2:
        q = -b/(2*a)
        candidates.append((q, a*q*q+b*q+c))
    q, m = min(candidates, key=lambda p:p[1])
    return {'polynomial': [c, b, a], 'argmin': q, 'minimum': m}


def main():
    y, z, P = [1, 1], [3, 2], [2, 1]
    beta = times([3], power(y, 2))
    B = times([2], power([64, 1], 2))
    f = plus(z, times(beta, B))
    v = times([6], power(P, 5))
    assert all(t > 0 for t in f+v)
    assert len(f) == 5 and f[-1] == v[-1] == 6 and len(v) == 6
    shifted = []
    for r in (-1, 0, 1):
        shifted.append(row(plus(f, [-r])))
    shifted_defects = [minimum_quadratic([defect(h, n) for h in shifted])
                       for n in range(len(f))]
    assert all(d['minimum'] > 0 for d in shifted_defects)
    character_checks = []
    for k in range(len(f)+1):
        for l in range(k+1, len(f)+1):
            m = minimum_quadratic([first_rows_minor(h, k, l)
                                   for h in shifted])
            assert m['minimum'] >= 0
            character_checks.append({'columns': [k, l], **m})
    # Positive support holds on the whole interval since only h0 varies.
    assert row(plus(f, [-2]))[0] > 0
    rows = {'v': row(v), 'yv': row(times(y, v))}
    defects = {name: [defect(h, n) for n in range(len(h))]
               for name, h in rows.items()}
    assert all(t > 0 for a in defects.values() for t in a)
    child = plus(f, times(beta, v))
    bad = defect(row(child), 3)
    assert bad == -71023104
    result = {
        'status': 'PASS_INDEPENDENT_EXACT_OBSTRUCTION_AUDIT',
        'f': f, 'v': v, 'normalized_B': B,
        'f_shift_defect_minima': shifted_defects,
        'f_shift_complete_character_minima': character_checks,
        'v_and_yv_rows': rows, 'v_and_yv_defects': defects,
        'child_failed_index': 3, 'child_failed_defect': bad,
        'scope': 'Ordinary positive integer inputs, full shifted trace cone and strict raw/y added block do not imply updated trace cone. No canonical ancestry, Fricke completion, origin packet, or target counterexample is asserted.',
        'full_tree_Local_TP2': 'OPEN',
    }
    output = Path(__file__).with_name('root_obstruction_audit_results.json')
    output.write_text(json.dumps(result, indent=2, default=str)+'\n')
    print(json.dumps({'status': result['status'], 'failed_defect': bad}))


if __name__ == '__main__':
    main()
