"""Independent mass/proxy replay, using ordinary x coefficients throughout.

No imports from the primary verifiers. Bernstein coefficients are reconstructed
from exact evaluations at 0, 1/2, and 1, rather than their power formulas.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json
import time


def add(a, b, factor=1):
    out = list(a) + [0] * max(0, len(b) - len(a))
    for j, v in enumerate(b):
        out[j] += factor * v
    return out


def small_product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for j, v in enumerate(b):
        for i, u in enumerate(a):
            out[i + j] += u * v
    return out


def positive_product(a, b):
    """Distinct ordinary-basis packing bound; all input coefficients positive."""
    assert min(a) >= 0 and min(b) >= 0
    bits = (sum(a) * sum(b)).bit_length()
    width = (bits + 7) // 8
    aa = int.from_bytes(b''.join(v.to_bytes(width, 'little') for v in a), 'little')
    bb = int.from_bytes(b''.join(v.to_bytes(width, 'little') for v in b), 'little')
    size = len(a) + len(b) - 1
    encoded = (aa * bb).to_bytes(size * width, 'little')
    out = [int.from_bytes(encoded[j * width:(j + 1) * width], 'little')
           for j in range(size)]
    assert sum(out) == sum(a) * sum(b)
    return out


def mass(a):
    return sum(v * (1 << j) for j, v in enumerate(a))


def fourier(a, upto=None):
    if upto is None:
        upto = len(a)
    return [sum(a[j] * comb(j, (j - n) // 2)
                for j in range(n, len(a), 2)) for n in range(upto)]


def delta0(row):
    return row[0] ** 2 - 2 * row[1] ** 2 + row[0] * row[2]


def continuum_coefficients(base, delta, threshold):
    # Three independent polynomial evaluations determine the degree-two margin.
    values = []
    for u in (Fraction(0), Fraction(1, 2), Fraction(1)):
        poly = add(base, [u * v for v in delta])
        values.append(delta0(fourier(poly, 3)) - threshold * mass(poly))
    b0, mid, b2 = values
    return [b0, 2 * mid - (b0 + b2) / 2, b2]


def finite(limit):
    prev, curr = [1], [3, 2]
    prefixes = [[1], [4, 2]]
    for n in range(2, limit + 2):
        nxt = add(small_product(curr, [3, 2]), prev, -1)
        assert len(nxt) == n + 1 and nxt[-1] == 2 ** n and min(nxt) > 0
        prefixes.append(add(prefixes[-1], nxt))
        prev, curr = curr, nxt
    certificates = []
    for m in range(2, limit + 1):
        A, B, T = prefixes[m + 1], prefixes[m - 1], prefixes[m]
        P = add(small_product(T, [1, 1]), [1])
        t = add([3 * v for v in small_product(P, [1, 1])], [0, 1], -1)
        trace_base = add(t, [2], -1)
        J = small_product(trace_base, [1, 1])
        V = [3 * v for v in small_product(P, [2, 5, 4, 1])]
        K = [2 * v for v in small_product(P, [4, 4, 1])]
        j, v, k = fourier(J), fourier(V), fourier(K)
        assert len(j) == len(k) == m + 4 and len(v) == m + 5
        w = [j[n] * v[n + 1] - (j[n + 1] if n + 1 < len(j) else 0) * v[n]
             for n in range(len(j))]
        assert min(w) > 0
        ratios = [Fraction(mass(J) * k[n], w[n]) for n in range(len(j))]
        max_ratio = max(ratios)
        ceiling = -(-max_ratio.numerator // max_ratio.denominator)
        gamma = 2 * ceiling + 13
        Lbase = add(positive_product(A, trace_base), B)
        template = continuum_coefficients(Lbase, [4 * u for u in A], gamma)
        trace = continuum_coefficients(trace_base, [4], 4)
        remainder = min(gamma * w[n] - 2 * mass(J) * k[n] for n in range(len(j)))
        assert gamma > 12 and min(template) > 0 and min(trace) > 0 and remainder > 0
        certificates.append({
            'm': m, 'gamma': str(gamma),
            'minimum_base_minor': str(min(w)),
            'maximum_proxy_ratio': str(max_ratio),
            'maximum_proxy_ratio_index': ratios.index(max_ratio),
            'template_margin_bernstein': list(map(str, template)),
            'trace_margin_bernstein': list(map(str, trace)),
            'minimum_proxy_remainder': str(remainder),
        })
    return certificates


def analytic_gates():
    # These are independent rational checks of starting points of the proven
    # monotone sequences. No bounded numerical scan is used for an infinite claim.
    q = Fraction
    out = {
        'proxy_scalar_at_106': q(8 ** 106, 7 ** 106 * 3072 * (4 * 106 + 7)),
        'proxy_ratio_at_106': q(8 * (4 * 106 + 7), 7 * (4 * 106 + 11)),
        'trace_bound_at_6': q(3 * 2 ** 5, 2 * 6 + 5),
        'gamma_at_391': q(3 * 2 ** (2 * 391 - 3), 4 * 391 + 7),
        'proxy_surplus_at_391': q(3 * 2 ** (2 * 391 - 3) * (3 * 2 ** (391 - 2) - 14),
                                  432 * (4 * 391 + 7) * 7 ** 391),
    }
    assert out['proxy_scalar_at_106'] > 1 and out['proxy_ratio_at_106'] > 1
    assert out['trace_bound_at_6'] >= 4 and out['gamma_at_391'] > 12
    assert out['proxy_surplus_at_391'] > 1
    return {k: str(v) for k, v in out.items()}


def main():
    start = time.monotonic()
    root = Path(__file__).parent
    reproduced = finite(390)
    reference = json.loads((root / 'fulltree_oneturn_mass_proxy_certificates.json').read_text())
    assert reproduced == reference['certificates'], 'A complete certificate record differs'
    digest = hashlib.sha256(json.dumps(reproduced, sort_keys=True).encode()).hexdigest()
    result = {
        'status': 'PASS',
        'scope': 'Conditional multiplier/proxy theorem for m>=2, k>=1; kernel lemmas separate',
        'method': 'Ordinary-coefficient recurrence/products; defining binomial Fourier transform; exact interpolation of Bernstein margins',
        'interval': [2, 390], 'certificate_records': len(reproduced),
        'fixed_proxy_minors': sum(m + 4 for m in range(2, 391)),
        'continuum_arrays': 2 * len(reproduced),
        'all_reference_records_identical': True,
        'certificate_records_sha256': digest,
        'analytic_gates': analytic_gates(),
        'elapsed_seconds': round(time.monotonic() - start, 3),
        'certificates': reproduced,
    }
    (root / 'recovery_mass_proxy_audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('certificates', 'analytic_gates')}, indent=2))


if __name__ == '__main__':
    main()
