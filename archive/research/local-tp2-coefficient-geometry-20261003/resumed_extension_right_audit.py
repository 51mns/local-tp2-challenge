"""Independent Laurent-ring audit for the all-right comparison certificates.

This verifier does not import a certificate producer or its arithmetic helpers.
Polynomials in q are constructed directly over a rational parameter ring.
"""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json

F = Fraction
PARAMETERS = 2


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


def replay_export(actual, certificate, parameter_positions):
    """Expand the producer's complete Bernstein array in its own coordinates."""
    degrees = tuple(certificate['degrees'])
    embedded = {}
    for powers, coefficient in actual.items():
        exponent = [0] * len(degrees)
        for power, position in zip(powers, parameter_positions):
            if position is None:
                assert power == 0
            else:
                exponent[position] = power
        embedded[tuple(exponent)] = coefficient
    recorded = {tuple(map(int, key.split(','))): F(value)
                for key, value in certificate['power_coefficients'].items()}
    assert embedded == recorded
    coefficients = {tuple(map(int, key.split(','))): F(value)
                    for key, value in certificate['bernstein_coefficients'].items()}
    assert set(coefficients) == set(product(*(range(d + 1) for d in degrees)))
    expanded = {}
    for indices, coefficient in coefficients.items():
        for offsets in product(*(range(d - j + 1)
                                 for j, d in zip(indices, degrees))):
            power = tuple(j + k for j, k in zip(indices, offsets))
            value = coefficient
            for j, k, d in zip(indices, offsets, degrees):
                value *= comb(d, j) * comb(d - j, k) * (-1) ** k
            expanded[power] = expanded.get(power, F(0)) + value
    expanded = {e: c for e, c in expanded.items() if c}
    assert expanded == embedded
    minimum = min(coefficients.values())
    assert minimum > 0 and minimum == F(certificate['strict_lower_bound'])
    return len(coefficients)


def main():
    one = scalar(pc(1))
    x = {-1: pc(1), 1: pc(1)}
    y = ladd(x, one)
    P = ladd(x, scalar(pc(2)))
    t = ladd(lscale(lmul(x, x), 3), lscale(x, 8), scalar(pc(6)))
    A = ladd(t, scalar(pc(-2)))
    B = lscale(lmul(y, lmul(P, P)), 3)
    e = lmul(y, P)
    K = lmul(P, lmul(P, P))
    assert [coeff(K, n) for n in range(4)] == [pc(v) for v in (20, 15, 6, 1)]
    assert mass(lmul(A, e)) == pc(384)
    Ae, Be = lmul(A, e), lmul(B, e)
    assert [coeff(Ae, n) for n in range(5)] == [pc(v) for v in (94, 79, 46, 17, 3)]
    assert [coeff(Be, n) for n in range(6)] == [pc(v) for v in (396, 339, 210, 90, 24, 3)]
    assert [determinant(Ae, Be, n) for n in range(5)] == [pc(v) for v in (582, 996, 570, 138, 9)]
    E1 = ladd(lscale(e, 2), lscale(y, -1))
    P2 = lmul(P, P)
    assert [determinant(P2, E1, n) for n in range(3)] == [pc(v) for v in (2, 3, 0)]
    assert [determinant(P2, e, n) for n in range(3)] == [pc(v) for v in (2, 1, 0)]

    Q = ladd(lmul(t, t), lmul(scalar(pscale(pv(0), 2)), t),
             scalar(pscale(pv(1), -4)))
    G = ladd(t, scalar(pv(0)))

    targets = {}
    for name, root in [('Q', Q), ('G', G)]:
        for n in range(max(root) + 1):
            targets[f'{name}_defect_{n}'] = defect(root, n)
        if name == 'Q':
            targets['Q_amplification'] = padd(defect(Q, 0), pscale(mass(Q), -4))
        lower, upper = lmul(A, lmul(e, root)), lmul(B, lmul(e, root))
        for n in range(max(lower) + 1):
            minor = determinant(lower, upper, n)
            targets[f'{name}_pair_{n}'] = minor
            if n <= 3:
                targets[f'{name}_margin_{n}'] = padd(
                    minor, pscale(pmul(coeff(K, n), mass(root)), -384))

    results = {}
    count = 0
    for name, polynomial in targets.items():
        degrees, coefficients = exact_bernstein(polynomial)
        lower = min(coefficients.values())
        assert lower > 0, (name, lower)
        count += len(coefficients)
        results[name] = {'degrees': degrees, 'strict_lower_bound': str(lower),
                         'Bernstein_coefficient_count': len(coefficients)}
    assert results['Q_amplification']['strict_lower_bound'] == '884'

    exported = json.loads(Path('resumed_extension_right_certificates.json').read_text())
    assert set(exported) == {'quartic_growth', 'quadratic_in_t', 'linear_in_t'}
    replay_count = replay_export(targets['Q_amplification'],
                                 exported['quartic_growth'], (0, 1))
    replay_polynomials = 1
    for family, name, positions in [('quadratic_in_t', 'Q', (0, 1)),
                                    ('linear_in_t', 'G', (2, None))]:
        assert len(exported[family]) == 4
        for n, certificate in enumerate(exported[family]):
            replay_count += replay_export(targets[f'{name}_margin_{n}'],
                                          certificate, positions)
            replay_polynomials += 1
    report = {'status': 'PASS', 'method': 'independent direct Laurent ring',
              'polynomials_verified': len(results),
              'Bernstein_coefficients_verified': count,
              'producer_polynomials_replayed': replay_polynomials,
              'producer_Bernstein_coefficients_replayed': replay_count,
              'certificates': results}
    Path('resumed_extension_right_audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
