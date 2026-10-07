#!/usr/bin/env python3
"""Independent direct-Laurent and symbolic-parameter replay of 11 trace seeds.

No author implementation is imported. Original mutations are performed in
the full Laurent q basis, rather than the author's ordinary x basis. The
parameter r remains a symbolic degree-two polynomial through every defect,
rather than reconstructing it from three sampled values. All 813 final
Bernstein coefficients are compared only after their independent generation.
"""
from pathlib import Path
from fractions import Fraction
from math import comb
import json


def clean(p):
    return {i: v for i, v in p.items() if v}


def add(*polys):
    out = {}
    for p in polys:
        for i, a in p.items():
            out[i] = out.get(i, 0) + a
    return clean(out)


def scale(p, c):
    return clean({i: c * a for i, a in p.items()})


def multiply(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i + j] = out.get(i + j, 0) + a * b
    return clean(out)


ONE = {0: 1}
X = {-1: 1, 1: 1}
Y = add(ONE, X)
P = add({0: 2}, X)
ROOT_CENTER = add({0: 5}, scale(X, 6), scale(multiply(X, X), 2))


def child(endpoint, center, opposite):
    return add(
        scale(multiply(multiply(Y, endpoint), center), 3),
        scale(multiply(X, add(endpoint, center)), -1),
        scale(opposite, -1),
    )


def canonical_center(m, k):
    left, center, right = ONE, ROOT_CENTER, P
    for _ in range(m):
        left, center, right = left, child(left, center, right), center
    for _ in range(k):
        left, center, right = center, child(right, center, left), right
    return center


def parameter_defect(row, reference, n):
    # Reuse the sparse polynomial ring with its index now the degree of r.
    def entry(j):
        return clean({0: row.get(j, 0), 1: -reference.get(j, 0)})
    a, b, c, d = [entry(j) for j in (n - 1, n, n + 1, n + 2)]
    defect = add(multiply(b, b), scale(multiply(a, c), -1),
                 scale(multiply(c, c), -1), multiply(b, d))
    return add(defect, scale(b, -1))  # delta_n minus 1 * h_n


def bernstein_twice(poly):
    assert all(j <= 2 for j in poly)
    a, b, c = (poly.get(j, 0) for j in range(3))
    # Substitute r = -2 + 4u in the symbolic power polynomial.
    p0, p1, p2 = a - 2 * b + 4 * c, 4 * b - 16 * c, 16 * c
    values = [2 * p0, 2 * p0 + p1, 2 * (p0 + p1 + p2)]
    # Invert the Bernstein basis, independently checking the whole polynomial.
    assert [values[0], 2 * (values[1] - values[0]),
            values[0] - 2 * values[1] + values[2]] == [2 * p0, 2 * p1, 2 * p2]
    return values


def primitive_certificates():
    trace = add(scale(multiply(X, X), 3), scale(X, 8), {0: 6})
    trace_squared = multiply(trace, trace)
    assert all(trace_squared.get(n, 0) - (4 if n == 0 else 0) > 0 for n in range(5))

    def ring_add(*polys):
        out = {}
        for poly in polys:
            for monomial, value in poly.items():
                out[monomial] = out.get(monomial, 0) + value
        return clean(out)

    def ring_mul(left, right):
        out = {}
        for i, a in left.items():
            for j, b in right.items():
                key = (i[0] + j[0], i[1] + j[1])
                out[key] = out.get(key, 0) + a * b
        return clean(out)

    def entry(n):
        # a=4u, b=-4+8v in trace^2+a trace+b.
        return clean({(0, 0): trace_squared.get(n, 0) - (4 if n == 0 else 0),
                      (1, 0): 4 * trace.get(n, 0),
                      (0, 1): 8 if n == 0 else 0})

    tensor = []
    for n in range(5):
        a, b, c, d = [entry(j) for j in (n - 1, n, n + 1, n + 2)]
        margin = ring_add(ring_mul(b, b), scale(ring_mul(a, c), -1),
                          scale(ring_mul(c, c), -1), ring_mul(b, d), scale(b, -9))
        assert all(max(key) <= 2 for key in margin)
        matrix = []
        for i in range(3):
            row = []
            for j in range(3):
                value = sum(Fraction(coef * comb(i, key[0]) * comb(j, key[1]),
                                     comb(2, key[0]) * comb(2, key[1]))
                            for key, coef in margin.items()
                            if key[0] <= i and key[1] <= j) * 4
                assert value.denominator == 1 and value >= 0
                row.append(int(value))
            matrix.append(row)
        power_v = [[row[0], 2 * (row[1] - row[0]), row[0] - 2 * row[1] + row[2]]
                   for row in matrix]
        restored = [power_v[0],
                    [2 * (power_v[1][j] - power_v[0][j]) for j in range(3)],
                    [power_v[0][j] - 2 * power_v[1][j] + power_v[2][j] for j in range(3)]]
        assert all(restored[i][j] == 4 * margin.get((i, j), 0)
                   for i in range(3) for j in range(3))
        tensor.append(matrix)

    single = []
    for n in range(3):
        poly = parameter_defect(trace, ONE, n)
        a, b, c = (poly.get(j, 0) for j in range(3))
        p0, p1, p2 = a - 2 * b + 4 * c, 2 * b - 8 * c, 4 * c
        coeff = [2 * p0, 2 * p0 + p1, 2 * (p0 + p1 + p2)]
        assert min(coeff) > 0
        assert [coeff[0], 2 * (coeff[1] - coeff[0]), coeff[0] - 2 * coeff[1] + coeff[2]] == [2 * p0, 2 * p1, 2 * p2]
        single.append(coeff)
    return tensor, single


def main():
    pairs = [(0, k) for k in range(1, 4)] + [(1, k) for k in range(1, 6)] + [(2, 1), (2, 2), (3, 1)]
    records = []
    coefficient_count = 0
    for m, k in pairs:
        center = canonical_center(m, k)
        trace = add(scale(multiply(Y, center), 3), scale(X, -1))
        assert all(trace.get(-j, 0) == a for j, a in trace.items())
        record = {'m': m, 'k': k, 'cases': {}}
        for name, smooth in [('raw', False), ('smooth', True)]:
            row = multiply(Y, trace) if smooth else trace
            ref = Y if smooth else ONE
            degree = max(row)
            assert min(row.get(j, 0) - 2 * ref.get(j, 0)
                       for j in range(degree + 1)) > 0
            coefficients = [bernstein_twice(parameter_defect(row, ref, n))
                            for n in range(degree + 1)]
            assert min(value for triple in coefficients for value in triple) > 0
            coefficient_count += 3 * len(coefficients)
            record['cases'][name] = {
                'degree': degree,
                'twice_degree_two_bernstein': coefficients,
                'minimum_scaled_coefficient': min(value for triple in coefficients
                                                   for value in triple),
            }
        records.append(record)
    assert coefficient_count == 813
    tensor, single = primitive_certificates()

    # The expected certificate is only read after every independent value exists.
    author_path = Path(__file__).parent.parent / 'hour_transport' / 'arbitrary_k_trace_exploratory_results.json'
    original = json.loads(author_path.read_text())
    assert tensor == original['m0_primitive_pair_box']['four_times_tensor_bernstein']
    assert single == original['m0_primitive_nonpositive_root']['twice_bernstein']
    indexed = {(record['m'], record['k']): record for record in original['records']}
    for record in records:
        saved = indexed[record['m'], record['k']]
        for name, row in record['cases'].items():
            other = saved['cases'][name]
            assert row['degree'] == other['degree']
            assert row['twice_degree_two_bernstein'] == other['twice_degree_two_bernstein']
            assert row['minimum_scaled_coefficient'] == other['minimum_scaled_coefficient']

    corners = {}
    for m, k, expected in [(1, 6, Fraction(17, 8)), (2, 3, Fraction(4)),
                           (3, 2, Fraction(16)), (4, 1, Fraction(8))]:
        strength = Fraction(2) ** (2 * m - 4) * Fraction(3 * 2 ** (m - 1)) ** (k - 1) / k - 8
        assert strength == expected and strength >= 1
        corners[f'{m},{k}'] = str(strength)
    result = {
        'verdict': 'PASS: all 813 exception coefficients and all 54 primitive coefficients independently generated and matched',
        'scope': 'Auxiliary trace theorem on centers L^m R^k with m>=0,k>=1; no larger Local TP2 assertion',
        'method': 'Original full-Laurent mutation and symbolic-r defect arithmetic',
        'author_implementation_imported': False,
        'positive_bernstein_coefficient_count': coefficient_count,
        'm0_pair_box_bernstein_count': 45,
        'm0_pair_box_four_times_bernstein': tensor,
        'm0_nonpositive_root_bernstein_count': 9,
        'm0_nonpositive_root_twice_bernstein': single,
        'tail_corner_strengths': corners,
        'records': records,
    }
    output = Path(__file__).with_name('arbitrary_k_trace_independent_audit.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'records'}, indent=2))


if __name__ == '__main__':
    main()
