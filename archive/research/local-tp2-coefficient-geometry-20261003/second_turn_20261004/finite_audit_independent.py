"""Independent exact Bernstein replay for the reversed additional-turn blocks.

No primary-writer implementation is imported or read.  Disclosed foundation:
ordinary_add, ordinary_product and ordinary_prefixes follow the ordinary-x
route of fulltree_oneturn_finite_independent.py.  Laurent conversion is the
independently proved packed homogeneous Horner transform below.  Defects use
generic parameter-polynomial multiplication, and Bernstein weights are obtained
from their defining binomial formula rather than writer-specific weight tables.

All arithmetic is exact Python integers; NumPy object arrays only batch it.
Expected writer JSON is first opened after every requested case is recomputed.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path
import time

import numpy as np


def ordinary_add(a, b):
    out = [0] * max(len(a), len(b))
    for j, value in enumerate(a):
        out[j] += value
    for j, value in enumerate(b):
        out[j] += value
    return out


def ordinary_product(a, b):
    """Nonnegative ordinary product, with an independently bounded radix."""
    assert min(a) >= 0 and min(b) >= 0
    mass = sum(a) * sum(b)
    bits = max(1, mass.bit_length())
    av = bv = 0
    for value in reversed(a):
        av = (av << bits) + value
    for value in reversed(b):
        bv = (bv << bits) + value
    packed = av * bv
    mask = (1 << bits) - 1
    out = []
    for _ in range(len(a) + len(b) - 1):
        out.append(packed & mask)
        packed >>= bits
    assert packed == 0 and sum(out) == mass
    return out


def ordinary_prefixes(maximum):
    """T_m=sum_(i=0)^m U_i((3+2x)/2), constructed in ordinary x."""
    previous, current, total = [0], [1], [1]
    out = [total]
    for _ in range(maximum):
        following = [0] * (len(current) + 1)
        for j, value in enumerate(current):
            following[j] += 3 * value
            following[j + 1] += 2 * value
        for j, value in enumerate(previous):
            following[j] -= value
        assert min(following) > 0
        total = ordinary_add(total, following)
        out.append(total)
        previous, current = current, following
    return out


def ordinary_half(poly):
    """H_n of P(z+z^-1), by carry-free homogeneous Horner evaluation.

    For degree D and radix B, after k updates acc is
    sum_(i=0)^k p_(D-i) B^i (B^2+1)^(k-i).
    Finally acc=B^D P(B+B^-1).  The nonnegative Laurent coefficients
    sum to P(2), hence each is strictly smaller than B=2^bit_length(P(2)).
    Ordinary radix digits therefore recover the Laurent row without carries.
    """
    assert min(poly) >= 0 and poly[-1] > 0
    degree = len(poly) - 1
    mass = 0
    for value in reversed(poly):
        mass = 2 * mass + value
    bits = max(1, mass.bit_length())
    packed = poly[-1]
    for k in range(1, degree + 1):
        packed = (packed << (2 * bits)) + packed + (poly[degree-k] << (bits*k))
    mask = (1 << bits) - 1
    lower = []
    for _ in range(degree):
        lower.append(packed & mask)
        packed >>= bits
    half = []
    for _ in range(degree + 1):
        half.append(packed & mask)
        packed >>= bits
    assert packed == 0 and lower == half[:0:-1]
    assert half[0] + 2 * sum(half[1:]) == mass
    return half


def defining_half(poly):
    """Slow binomial definition, used only to audit the packed foundation."""
    degree = len(poly) - 1
    half = [0] * (degree + 1)
    for j, value in enumerate(poly):
        for q in range(j // 2 + 1):
            half[j-2*q] += value * comb(j, q)
    return half


def bernstein_weights(powers, indices, dimension, scale):
    """scale times degree-(2,...,2) Bernstein coefficient of a monomial."""
    out = []
    for power in powers:
        row = []
        for index in indices:
            value = Fraction(scale)
            for k, j in zip(index, power):
                if j > k:
                    value = Fraction(0)
                    break
                value *= Fraction(comb(k, j), comb(2, j))
            assert value.denominator == 1
            row.append(value.numerator)
        out.append(row)
    return np.array(out, dtype=object)


def generic_defect(half, powers):
    """Multiply generic parameter polynomials for all four terms of delta."""
    degree = len(half) - 1
    square_powers = sorted({tuple(a+b for a, b in zip(p, q))
                            for p in powers for q in powers})
    columns = {power: j for j, power in enumerate(square_powers)}
    extended = np.vstack([half, np.zeros((2, len(powers)), dtype=object)])
    current = extended[:degree+1]
    previous = np.vstack([half[1], half[:degree]])
    following = extended[1:degree+2]
    second = extended[2:degree+3]
    coeff = np.zeros((degree+1, len(square_powers)), dtype=object)
    for i, p in enumerate(powers):
        for j, q in enumerate(powers):
            exponent = tuple(a+b for a, b in zip(p, q))
            coeff[:, columns[exponent]] += (
                current[:, i]*current[:, j]
                - previous[:, i]*following[:, j]
                - following[:, i]*following[:, j]
                + current[:, i]*second[:, j])
    return coeff, square_powers


def margin_summary(margins, indices):
    minimum = None
    witness = None
    negative = zero = 0
    digest = sha256()
    for n, row in enumerate(margins):
        for index, raw in zip(indices, row):
            value = int(raw)
            digest.update((str(value) + '\n').encode('utf-8'))
            negative += value < 0
            zero += value == 0
            if minimum is None or value < minimum:
                minimum = value
                witness = [n, *index]
    return dict(margins=int(margins.size), negative=negative, zero=zero,
                minimum=str(minimum), witness=witness, sha256=digest.hexdigest())


def generic_half(rows, scalars):
    degree = max(len(row) for row in rows) - 1
    out = np.zeros((degree+1, len(rows)), dtype=object)
    for j, (row, scalar) in enumerate(zip(rows, scalars)):
        out[:len(row), j] = [scalar * value for value in row]
    return out


def certify(m, prefixes, smooth):
    c, d = prefixes[m], prefixes[m+2]
    # t=tau+2=5+2x+3(1+x)^2 T_(m+1); all pieces are ordinary-positive.
    t = ordinary_add([5, 2], [3*v for v in ordinary_product([1, 2, 1], prefixes[m+1])])
    ct = ordinary_product(c, t)
    single = ordinary_add(ct, d)
    midpoint = ordinary_add(ordinary_product(ct, t), ordinary_product(d, t))
    # alpha=H(tau)_0-2=H(t)_0-4, independently evaluated from the binomial definition.
    alpha = sum(t[j]*comb(j, j//2) for j in range(0, len(t), 2)) - 4
    assert alpha > 0
    if smooth:
        c, d, ct, single, midpoint = [ordinary_product([1, 1], p)
                                    for p in [c, d, ct, single, midpoint]]
    ch, dh, cth, lh, hh = [ordinary_half(p) for p in [c, d, ct, single, midpoint]]
    assert len(lh)-1 == 2*m+3+int(smooth)
    assert len(hh)-1 == 3*m+6+int(smooth)
    assert hh[-1] == 36*8**m
    b0 = dh[0]
    cases = []
    powers = [(0,), (1,)]
    indices = list(product(range(3), repeat=1))
    half = generic_half([lh, ch], [1, -4])
    assert all(int(row[0]+row[1]) > 0 for row in half)
    coeff, squared = generic_defect(half, powers)
    numerator = 3*2**max(0, 2*m-3)
    denominator = 2**max(0, 3-2*m)
    margins = denominator * (coeff @ bernstein_weights(squared, indices, 1, 4))
    margins -= numerator * (half @ bernstein_weights(powers, indices, 1, 4))
    result = margin_summary(margins, indices)
    result.update(m=m, smooth=smooth, label='single', degree=len(lh)-1,
                  lambda_numerator=str(numerator), lambda_denominator=str(denominator))
    cases.append(result)
    powers = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1)]
    indices = list(product(range(3), repeat=3))
    half = generic_half([hh, cth, cth, ch, dh], [1, -4, -4, 16, -4])
    assert all(sum(map(int, row)) > 0 for row in half)
    coeff, squared = generic_defect(half, powers)
    margins = alpha * (coeff @ bernstein_weights(squared, indices, 3, 8))
    margins -= 8*b0 * (half @ bernstein_weights(powers, indices, 3, 8))
    result = margin_summary(margins, indices)
    result.update(m=m, smooth=smooth, label='midpoint', degree=len(hh)-1,
                  alpha=str(alpha), b0=str(b0))
    cases.append(result)
    return cases


def foundation_checks(prefixes):
    tested = []
    for poly in [[1], [0, 1], [3, 0, 2], [1, 2, 1],
                 *[prefixes[j] for j in [0, 1, 2, 3, 7, 20, 96, 200, 409, 411]
                   if j < len(prefixes)]]:
        assert ordinary_half(poly) == defining_half(poly)
        tested.append(len(poly)-1)
    return tested


def compare_expected(cases, path):
    expected = json.loads(path.read_text())
    assert expected['status'] == 'PASS'
    rows = expected['cases']
    assert len(rows) == len(cases)
    comparisons = []
    for actual, reference in zip(cases, rows):
        # Writer naming is detected from output metadata only, after recomputation.
        writer_label = reference.get('label', reference.get('kind', reference.get('block')))
        writer_smooth = reference.get('smooth')
        assert actual['m'] == reference['m'] and actual['smooth'] == writer_smooth
        if writer_label is not None:
            assert actual['label'] == writer_label
        assert actual['degree'] == reference['degree']
        assert actual['sha256'] == reference['sha256']
        comparisons.append(dict(m=actual['m'], smooth=actual['smooth'], label=actual['label'],
                                hash_match=True))
    return dict(status='PASS', matched_cases=len(comparisons),
                input_sha256=sha256(path.read_bytes()).hexdigest(), comparisons=comparisons)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', type=int, default=0)
    parser.add_argument('--max', type=int, default=409)
    parser.add_argument('--output', default='finite_audit_independent_results.json')
    parser.add_argument('--expected', type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    prefixes = ordinary_prefixes(args.max+2)
    checks = foundation_checks(prefixes)
    cases = []
    output = dict(status='RUNNING', scope=[args.min, args.max],
        arithmetic='Python arbitrary precision integers; NumPy dtype=object',
        method='ordinary-x recurrence/products; packed homogeneous Laurent substitution; generic parameter multiplication; defining tensor Bernstein weights',
        disclosed_foundation='ordinary-x nonnegative product and prefix recurrence route from parent fulltree_oneturn_finite_independent.py; no primary-writer imports or source access',
        packed_binomial_crosscheck_degrees=checks,
        scaling={'single':'4*denominator Bernstein(delta_n(L)-lambda L_n), lambda=3*2^(2m-3)',
                 'midpoint':'8 Bernstein(alpha delta_n(H)-8 b0 H_n), alpha=H(tau)_0-2; b=d or yd'},
        case_order='m increasing; smooth False then True; single then midpoint',
        cases=cases)
    destination = Path(args.output)
    for m in range(args.min, args.max+1):
        for smooth in [False, True]:
            cases.extend(certify(m, prefixes, smooth))
        output['scope_completed'] = [args.min, m]
        output['elapsed_seconds'] = round(time.monotonic()-started, 3)
        destination.write_text(json.dumps(output, indent=2)+'\n')
        if m % 10 == 0 or m == args.max:
            print(json.dumps(dict(completed_m=m, elapsed_seconds=output['elapsed_seconds'],
                                  negative=sum(r['negative'] for r in cases),
                                  zero=sum(r['zero'] for r in cases))), flush=True)
    output['status'] = 'PASS' if all(r['negative'] == r['zero'] == 0 for r in cases) else 'FAIL'
    output['total_margins'] = sum(r['margins'] for r in cases)
    output['strict_minimum'] = min((r['minimum'] for r in cases), key=int)
    if args.expected:
        output['writer_comparison'] = compare_expected(cases, args.expected)
    output['elapsed_seconds'] = round(time.monotonic()-started, 3)
    destination.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ['cases', 'writer_comparison']}), flush=True)
    assert output['status'] == 'PASS'


if __name__ == '__main__':
    main()
