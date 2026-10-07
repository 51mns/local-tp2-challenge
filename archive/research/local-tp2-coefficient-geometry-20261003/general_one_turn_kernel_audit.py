"""Independent direct-Laurent audit for the first new one-turn kernel family.

This verifier does not import a certificate producer or its arithmetic helpers.
Polynomials in q are constructed directly over a rational parameter ring.
"""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

F = Fraction
PARAMETERS = 3


def padd(*polynomials):
    out = {}
    for p in polynomials:
        for exponent, coefficient in p.items():
            out[exponent] = out.get(exponent, F(0)) + coefficient
    return {e: c for e, c in out.items() if c}


def pscale(p, scalar):
    return {e: c * scalar for e, c in p.items() if c * scalar}


def pmul(p, r):
    terms = {}
    for e, c in p.items():
        for f, d in r.items():
            power = tuple(a + b for a, b in zip(e, f))
            terms[power] = terms.get(power, F(0)) + c * d
    return {e: c for e, c in terms.items() if c}


def pc(value):
    return {(0,) * PARAMETERS: F(value)} if value else {}


def pv(index):
    return {tuple(int(i == index) for i in range(PARAMETERS)): F(1)}


def scalar(p):
    return {0: p} if p else {}


def ladd(*polynomials):
    out = {}
    for p in polynomials:
        for index, coefficient in p.items():
            out[index] = padd(out.get(index, {}), coefficient)
    return {n: c for n, c in out.items() if c}


def lscale(p, multiplier):
    return {n: pscale(c, multiplier) for n, c in p.items() if multiplier}


def lmul(p, r):
    terms = {}
    for i, a in p.items():
        for j, b in r.items():
            terms[i + j] = padd(terms.get(i + j, {}), pmul(a, b))
    return {n: c for n, c in terms.items() if c}


def coeff(p, index):
    return p.get(index, {})


def mass(p):
    return padd(*p.values())


def determinant(p, r, index):
    return padd(pmul(coeff(p, index), coeff(r, index + 1)),
                pscale(pmul(coeff(p, index + 1), coeff(r, index)), -1))


def defect(p, index):
    def delta(j):
        return padd(pmul(coeff(p, j), coeff(p, j)),
                    pscale(pmul(coeff(p, j - 1), coeff(p, j + 1)), -1))
    return padd(delta(index), pscale(delta(index + 1), -1))


def exact_bernstein(p):
    degrees = tuple(max((e[i] for e in p), default=0)
                    for i in range(PARAMETERS))
    coefficients = {}
    for indices in product(*(range(d + 1) for d in degrees)):
        value = F(0)
        for powers, coefficient in p.items():
            if all(k <= j for k, j in zip(powers, indices)):
                contribution = coefficient
                for k, j, d in zip(powers, indices, degrees):
                    contribution *= F(comb(j, k), comb(d, k))
                value += contribution
        coefficients[indices] = value
    # Reverse the complete basis expansion, independently of the forward map.
    reconstructed = {}
    for indices, coefficient in coefficients.items():
        for offsets in product(*(range(d - j + 1)
                                 for j, d in zip(indices, degrees))):
            power = tuple(j + k for j, k in zip(indices, offsets))
            value = coefficient
            for j, k, d in zip(indices, offsets, degrees):
                value *= comb(d, j) * comb(d - j, k) * (-1) ** k
            reconstructed[power] = reconstructed.get(power, F(0)) + value
    reconstructed = {e: c for e, c in reconstructed.items() if c}
    assert reconstructed == p
    return degrees, coefficients


def replay_block(actual, certificate):
    degrees, values = exact_bernstein(actual)
    assert tuple(certificate['parameter_degrees']) == degrees
    recorded = {tuple(map(int, key.split(','))): F(value)
                for key, value in certificate['power_coefficients'].items()}
    assert recorded == actual
    recorded_values = {tuple(map(int, key.split(','))): F(value)
                       for key, value in certificate['bernstein_coefficients'].items()}
    assert recorded_values == values
    minimum = min(values.values())
    assert minimum > 0 and minimum == F(certificate['lower_bound'])
    return len(values)


def folded_entry(polynomial, i, j):
    if i == 0:
        return coeff(polynomial, j)
    if j == 0:
        return pscale(coeff(polynomial, i), 2)
    return padd(coeff(polynomial, abs(i-j)), coeff(polynomial, i+j))


def folded_minor(polynomial, i, j, k, l):
    return padd(pmul(folded_entry(polynomial, i, k), folded_entry(polynomial, j, l)),
                pscale(pmul(folded_entry(polynomial, i, l), folded_entry(polynomial, j, k)), -1))


def main():
    one = scalar(pc(1))
    x = {-1: pc(1), 1: pc(1)}
    y, z = ladd(x, one), ladd(lscale(x, 2), scalar(pc(3)))
    inner_u = [one, z]
    for j in (2, 3):
        inner_u.append(ladd(lmul(z, inner_u[-1]), lscale(inner_u[-2], -1)))
    inner_T = [ladd(*inner_u[:j+1]) for j in range(4)]
    A, B = inner_T[3], inner_T[1]
    P = ladd(one, lmul(y, inner_T[2]))
    t = ladd(lscale(lmul(y, P), 3), lscale(x, -1))
    tr = ladd(t, scalar(padd(pc(2), pscale(pv(0), -4))))
    ts = ladd(t, scalar(padd(pc(2), pscale(pv(1), -4))))
    tc = ladd(t, scalar(padd(pc(2), pscale(pv(2), -4))))
    single = ladd(lmul(A, tr), B)
    midpoint = ladd(lmul(A, lmul(tr, ts)), lmul(B, tc))
    q2 = lmul(y, ladd(lmul(A, ladd(lmul(t, t), scalar(pc(-1)))), lmul(B, t)))
    blocks = {
        'inner_A': A, 'inner_B': B, 'cubic_or_higher_root': tr,
        'y_root': lmul(y, tr), 'single': single,
        'y_single': lmul(y, single), 'y_A': lmul(y, A),
        'y_degree_two': q2, 'midpoint': midpoint,
    }
    exported = json.loads(Path('general_one_turn_kernel_certificates.json').read_text())
    assert exported['m'] == 2 and set(exported['blocks']) == set(blocks)
    block_polynomials = block_coefficients = positive_row_coefficients = 0
    for name, poly in blocks.items():
        assert all(coeff(poly, -n) == coefficient for n, coefficient in poly.items())
        degree = max(poly)
        assert len(exported['blocks'][name]) == degree+1
        for n, certificate in enumerate(exported['blocks'][name]):
            block_coefficients += replay_block(defect(poly, n), certificate)
            block_polynomials += 1
        for n in range(degree+1):
            _, values = exact_bernstein(coeff(poly, n))
            assert min(values.values()) > 0
            positive_row_coefficients += len(values)

    assert [coeff(B, n) for n in range(2)] == [pc(4), pc(2)]
    assert max(midpoint) == 11 and max(B) == 1
    relative = exported['relative_minor_certificate']
    assert relative['degree_midpoint'] == 11 and relative['degree_B'] == 1
    assert relative['representative_first_row_limit'] == 13
    assert relative['representative_row_gap_limit'] == 13
    records = {tuple(record['indices']): record for record in relative['patterns']}
    assert len(records) == len(relative['patterns'])
    expected_patterns = set()
    minimum = None
    minimizing_pattern = None
    relative_coefficients = 0
    for i in range(14):
        for gap in range(1, 14):
            j = i+gap
            for e in (-1, 0, 1):
                k = i+e
                if k < 0:
                    continue
                for f in (-1, 0, 1):
                    l = j+f
                    if l <= k:
                        continue
                    minor_B = folded_minor(B, i, j, k, l)
                    assert all(exponent == (0, 0, 0) for exponent in minor_B)
                    value = minor_B.get((0, 0, 0), F(0))
                    assert value >= 0
                    if value == 0:
                        continue
                    pattern = (i, j, k, l)
                    expected_patterns.add(pattern)
                    record = records[pattern]
                    assert F(record['minor_B']) == value
                    margin = padd(folded_minor(midpoint, i, j, k, l), pc(-4*value))
                    degrees, values = exact_bernstein(margin)
                    lower = min(values.values())
                    assert lower > 0 and F(record['lower_bound']) == lower
                    assert tuple(record['parameter_degrees']) == degrees
                    relative_coefficients += len(values)
                    if minimum is None or lower < minimum:
                        minimum, minimizing_pattern = lower, pattern
    assert set(records) == expected_patterns
    assert len(records) == relative['positive_B_minor_patterns'] == 1543
    assert minimum == F(relative['uniform_minimum_bernstein_bound'])
    assert list(minimizing_pattern) == relative['minimum_pattern']

    report = {
        'status': 'PASS',
        'method': 'independent direct Laurent coefficient ring; no producer imports',
        'block_defect_polynomials_replayed': block_polynomials,
        'block_Bernstein_coefficients_replayed': block_coefficients,
        'positive_row_Bernstein_coefficients_checked': positive_row_coefficients,
        'relative_minor_patterns_reconstructed': len(records),
        'relative_minor_Bernstein_coefficients_reconstructed': relative_coefficients,
        'relative_minor_uniform_minimum': str(minimum),
        'minimum_pattern': minimizing_pattern,
        'completeness': 'infinite-index reduction is proved in general_one_turn_kernel_audit.md',
    }
    Path('general_one_turn_kernel_audit.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
