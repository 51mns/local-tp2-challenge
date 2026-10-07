"""Independent replay of every finite fixed-proxy certificate, m=0..409.

Own ordinary-x recurrence and multiplication; packed homogeneous Laurent
substitution; own generic exact-rational Bernstein conversion. No proxy-author
routine is imported. The packing formula is disclosed from the independent
finite_audit_independent.py foundation and checked against a separate direct
Laurent implementation and defining binomial formula here.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import time
import falsification_targeted as t


HERE = Path(__file__).resolve().parent


def mass(a):
    value = 0
    for coef in reversed(a):
        value = value*2+coef
    return value


def packed_product(a, b):
    assert min(a) >= 0 and min(b) >= 0
    total = sum(a)*sum(b)
    bits = max(1, total.bit_length())
    mask = (1 << bits)-1
    left = right = 0
    for coef in reversed(a):
        left = (left << bits)+coef
    for coef in reversed(b):
        right = (right << bits)+coef
    encoded = left*right
    output = []
    for _ in range(len(a)+len(b)-1):
        output.append(encoded & mask)
        encoded >>= bits
    assert not encoded and sum(output) == total
    return output


def packed_row(a):
    """Carries excluded because every Laurent coefficient <= P(2)<radix.

    If D=degP, after k steps the integer is
      sum_(i=0)^k a_(D-i) B^i (B^2+1)^(k-i).
    At k=D it equals B^D P(B+B^-1). Thus its radix digits
    recover the symmetric Laurent row, with no rounding or interpolation.
    """
    assert min(a) >= 0 and a[-1] > 0
    D = len(a)-1
    total = mass(a)
    bits = max(1, total.bit_length())
    mask = (1 << bits)-1
    encoded = a[-1]
    for k in range(1, D+1):
        encoded = (encoded << (2*bits))+encoded+(a[D-k] << (bits*k))
    lower = []
    for _ in range(D):
        lower.append(encoded & mask)
        encoded >>= bits
    half = []
    for _ in range(D+1):
        half.append(encoded & mask)
        encoded >>= bits
    assert not encoded and lower == half[:0:-1]
    assert half[0]+2*sum(half[1:]) == total
    return half


def defining_row(a):
    return [sum(a[j]*comb(j, (j-n)//2) for j in range(n, len(a), 2))
            for n in range(len(a))]


def central_margin(base, slope, base_mass, slope_mass, bound):
    params = [{t.ZERO: F(base[n]), (1, 0, 0): F(slope[n])}
              for n in range(3)]
    mass_params = {t.ZERO: F(base_mass), (1, 0, 0): F(slope_mass)}
    margin = t.padd(t.pdefect(params, 0), t.pscale(mass_params, -bound))
    degrees, coefficients = t.bernstein(margin)
    assert degrees == (2, 0, 0)
    values = [str(coefficients[(i, 0, 0)]) for i in range(3)]
    assert min(map(F, values)) > 0
    return values


def ceil(v):
    return (v.numerator+v.denominator-1)//v.denominator


def main():
    started = time.monotonic()
    maximum = 409
    _, prefixes, _ = t.inner(maximum+2)
    foundation_degrees = []
    for poly in [[1], [0, 1], [2, 0, 1], [1, 2, 1],
                 *[prefixes[i] for i in [0, 1, 2, 7, 20, 96, 200, 409, 411]]]:
        assert packed_row(poly) == defining_row(poly)
        if len(poly) <= 21:
            assert packed_row(poly) == t.row(poly)
        foundation_degrees.append(len(poly)-1)
    for a, b in [([1, 2, 1], prefixes[20]), (prefixes[7], prefixes[9])]:
        assert packed_product(a, b) == t.mul(a, b)

    records = []
    wcount = 0
    whash = hashlib.sha256()
    for m in range(maximum+1):
        c, d = prefixes[m], prefixes[m+2]
        X = t.add([1], t.mul([1, 1], prefixes[m+1]))
        tau = t.sub(t.scale(t.mul([1, 1], X), 3), [0, 1])
        tau2 = t.sub(tau, [2])
        J = t.mul([1, 1], tau2)
        V = t.scale(t.mul(t.mul([1, 2, 1], X), [2, 1]), 3)
        K = t.scale(t.mul(X, [4, 4, 1]), 2)
        j, v, k = [packed_row(a) for a in [J, V, K]]
        assert len(j) == len(k) == m+5 and len(v) == m+6
        w = [t.at(j, n)*t.at(v, n+1)-t.at(j, n+1)*t.at(v, n)
             for n in range(len(j))]
        assert min(w) > 0
        for n, value in enumerate(w):
            whash.update((str(m)+','+str(n)+':'+str(value)+'\n').encode())
        wcount += len(w)
        jmass = mass(J)
        beta = max(F(jmass*k[n], w[n]) for n in range(len(w)))
        if m == 0:
            alpha, gamma, tailstart = F(4, 5), F(2), 5
            lower = F(80**2)*F(4, 5)/6
        elif m == 1:
            alpha, gamma, tailstart = F(5), F(40), 4
            lower = gamma*alpha**(tailstart-1)/(2*tailstart)
        elif m == 2:
            alpha, gamma, tailstart = F(5), F(ceil(4*beta/5)+13), 2
            lower = gamma*alpha**(tailstart-1)/(2*tailstart)
        else:
            alpha, gamma, tailstart = F(4), F(2*ceil(beta)+13), 2
            lower = gamma*alpha**(tailstart-1)/(2*tailstart)
        assert lower > beta > 6
        assert mass(d) < mass(c)*mass(tau2)
        L = t.add(packed_product(c, tau2), d)
        ch, lh, th = [packed_row(a) for a in [c, L, tau2]]
        trace = central_margin(th[:3], [4, 0, 0], mass(tau2), 4, alpha)
        single = central_margin(lh[:3], [4*t.at(ch, n) for n in range(3)],
                                mass(L), 4*mass(c), gamma)
        rem = min(lower*w[n]-jmass*k[n] for n in range(len(w)))
        assert rem > 0
        records.append({'m': m, 'beta': str(beta), 'alpha_trace': str(alpha),
             'gamma_template': str(gamma), 'outer_tail_start': tailstart,
             'minimum_base_minor': str(min(w)), 'base_minor_count': len(w),
             'template_margin_bernstein': single, 'trace_margin_bernstein': trace,
             'outer_tail_central_mass_lower': str(lower),
             'tail_vs_proxy_threshold_residual': str(lower-beta),
             'minimum_fixed_proxy_residual': str(rem)})
        if m % 50 == 0 or m == maximum:
            print(json.dumps({'completed_m': m, 'elapsed_seconds': round(time.monotonic()-started, 3)}), flush=True)

    # Expected complete output is read only after independent recomputation.
    author_file = HERE/'proxy_mass_results.json'
    expected = json.loads(author_file.read_text())
    assert expected['status'] == 'PASS' and expected['inner_interval'] == [0, maximum]
    assert wcount == expected['base_proxy_minors'] == 85895
    assert len(records)*2 == 820
    for actual, reference in zip(records, expected['certificates']):
        assert all(reference[key] == value for key, value in actual.items()), actual['m']
    output = {'status': 'PASS', 'scope': 'every inner index m=0..409, every supported fixed base-proxy minor and both entire-interval central-margin Bernstein arrays',
              'fixed_base_minor_count': wcount, 'central_Bernstein_array_count': len(records)*2,
              'central_Bernstein_coefficient_count': len(records)*6,
              'all_record_fields_match_author': True,
              'base_minor_sha256': whash.hexdigest(),
              'foundation_crosscheck_degrees': foundation_degrees,
              'independence': 'Ordinary-polynomial route, packed homogeneous Horner Laurent transform, own generic Fraction Bernstein. No author-proxy code imports. Packing foundation disclosed from finite_audit_independent.py and independently validated here.',
              'proof_limits': 'Finite numerical hypotheses only; the analytic tail and folded-cone/Jacobi compatibility proof dependencies are separate.',
              'elapsed_seconds': round(time.monotonic()-started, 3),
              'source_script_sha256': hashlib.sha256((HERE/'proxy_mass_cert.py').read_bytes()).hexdigest(),
              'source_results_sha256': hashlib.sha256(author_file.read_bytes()).hexdigest(),
              'disclosed_packing_foundation_sha256': hashlib.sha256((HERE/'finite_audit_independent.py').read_bytes()).hexdigest(),
              'independent_primitives_sha256': hashlib.sha256((HERE/'falsification_targeted.py').read_bytes()).hexdigest(),
              'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'records': records}
    (HERE/'falsification_proxy_full_audit_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k != 'records'}), flush=True)


if __name__ == '__main__':
    main()
