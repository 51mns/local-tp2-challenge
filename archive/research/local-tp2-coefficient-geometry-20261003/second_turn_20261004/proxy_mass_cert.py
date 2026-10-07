"""Exact second-turn central mass and final fixed-proxy certificates.

Standalone integer/Fraction implementation; no parent polynomial imports.
Certifies finite inner range 0..409, small outer exceptions and all parameter
intervals by Bernstein coefficients. Cone/product and Jacobi compatibility
are mathematical dependencies supplied by the separate kernel theorem.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import argparse
import hashlib
import json


def at(a, n):
    n = abs(n)
    return a[n] if n < len(a) else 0


def add(a, b, scale_b=1):
    return [at(a, n) + scale_b * at(b, n)
            for n in range(max(len(a), len(b)))]


def scale(a, s):
    return [s * v for v in a]


def multiply(a, b):
    return [sum(a[abs(j)] * at(b, n-j)
                for j in range(1-len(a), len(a)))
            for n in range(len(a)+len(b)-1)]


def times_small(a, b):
    assert len(b) <= 3
    return [sum(b[abs(j)] * at(a, n-j)
                for j in range(1-len(b), len(b)))
            for n in range(len(a)+len(b)-1)]


def low_product(a, b, n):
    return sum(a[abs(j)] * at(b, n-j)
               for j in range(1-len(a), len(a)))


def mass(a):
    return a[0] + 2*sum(a[1:])


def delta0(a):
    return at(a, 0)**2 - 2*at(a, 1)**2 + at(a, 0)*at(a, 2)


def central_bern(row, slope, row_mass, slope_mass, bound):
    a, b, c = row
    d, e, f = slope
    power = [a*a-2*b*b+a*c-bound*row_mass,
             2*a*d-4*b*e+a*f+d*c-bound*slope_mass,
             d*d-2*e*e+d*f]
    return [Q(power[0]), Q(2*power[0]+power[1], 2), Q(sum(power))]


def ceilq(v):
    return (v.numerator+v.denominator-1)//v.denominator


def sparse_add(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0)+s*v
    return r


def sparse_multiply(a, b):
    r = {}
    for i, v in a.items():
        for j, w in b.items():
            k = (i[0]+j[0], i[1]+j[1])
            r[k] = r.get(k, 0)+v*w
    return r


def paired_trace_bern(t, bound):
    # Independent r=2-4u,s=2-4v, 0<=u,v<=1.
    h = add(t, [2], -1)
    f = [low_product(h, h, n) for n in range(3)]
    rows = [{(0, 0): f[n], (1, 0): 4*at(h, n),
             (0, 1): 4*at(h, n), (1, 1): 16 if n == 0 else 0}
            for n in range(3)]
    delta = sparse_add(sparse_add(sparse_multiply(rows[0], rows[0]),
                                  sparse_multiply(rows[1], rows[1]), -2),
                       sparse_multiply(rows[0], rows[2]))
    mh = mass(h)
    mass_power = {(0, 0): mh*mh, (1, 0): 4*mh,
                  (0, 1): 4*mh, (1, 1): 16}
    margin = sparse_add(delta, mass_power, -bound)
    return [sum(Q(v)*Q(comb(i, a), comb(2, a))*Q(comb(j, b), comb(2, b))
                for (a, b), v in margin.items() if a <= i and b <= j)
            for i in range(3) for j in range(3)]


def exact_outer(c, d, t, targets, beta):
    u_prev, u = [], [1]
    r_prev, r = [], [1]
    records = []
    for N in range(1, max(targets)+1):
        u_next = add(multiply(t, u), u_prev, -1)
        u_prev, u = u, u_next
        r_prev, r = r, add(r, u)
        if N in targets:
            Z = add(multiply(c, r), multiply(d, r_prev))
            z_mass, central = mass(Z), delta0(Z)
            residual = central-beta*z_mass
            assert residual > 0, (N, 'small outer central margin')
            records.append({'N': N, 'degree_Z': len(Z)-1,
                            'delta0_Z': str(central), 'mass_Z': str(z_mass),
                            'central_to_mass': str(Q(central, z_mass)),
                            'proxy_mass_residual': str(residual),
                            'row_sha256': hashlib.sha256(
                                json.dumps(Z, separators=(',', ':')).encode()).hexdigest()})
    return records


def tail_gates():
    m = 410
    sigma = Q(59, 100)
    checks = {
        'trace_mass_at_410': Q(3*2**m, 2*m+7),
        'trace_mass_consecutive_ratio': Q(2*(2*m+7), 2*m+9),
        'template_gamma_at_410': Q(3*2**(2*m-3), 4*m+7),
        'template_gamma_consecutive_ratio': Q(4*(4*m+7), 4*m+11),
        'J_strength_at_410': Q(3*2**(m-1)),
        'proxy_scalar_at_410': Q(8, 7)**m/Q(10752*(4*m+7)),
        'proxy_scalar_consecutive_ratio': Q(8*(4*m+7), 7*(4*m+11)),
        'proxy_surplus_at_410': Q(3*2**(2*m-3)*(3*2**(m-1)-14),
                                    4*(4*m+7)*756*7**m),
    }
    assert checks['trace_mass_at_410'] >= 4
    assert checks['template_gamma_at_410'] > 12
    assert checks['J_strength_at_410'] >= 28
    assert all(checks[k] > 1 for k in (
        'trace_mass_consecutive_ratio', 'template_gamma_consecutive_ratio',
        'proxy_scalar_at_410', 'proxy_scalar_consecutive_ratio',
        'proxy_surplus_at_410'))
    return {k: str(v) for k, v in checks.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=409)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('proxy_mass_results.json'))
    args = parser.parse_args()
    assert args.limit >= 3
    y, p1, z = [1, 1], [2, 1], [3, 2]
    y2, p1sq = times_small(y, y), times_small(p1, p1)
    u = [[1], z]
    prefixes = [[1], add([1], z)]
    for j in range(2, args.limit+3):
        uj = add(times_small(u[-1], z), u[-2], -1)
        assert uj[-1] == 2**j and min(uj) > 0
        u.append(uj)
        prefixes.append(add(prefixes[-1], uj))
    certificates = []
    base_minor_count = 0
    for m in range(args.limit+1):
        c, d = prefixes[m], prefixes[m+2]
        X = add(times_small(prefixes[m+1], y), [1])
        t = add(scale(times_small(X, y), 3), [0, 1], -1)
        J = times_small(add(t, [2], -1), y)
        V = scale(times_small(times_small(X, y2), p1), 3)
        K = scale(times_small(X, p1sq), 2)
        assert len(J) == len(K) == m+5 and len(V) == m+6
        assert mass(d) < mass(c)*(mass(t)-2)
        jmass = mass(J)
        w = [at(J, n)*at(V, n+1)-at(J, n+1)*at(V, n)
             for n in range(len(J))]
        assert min(w) > 0, (m, 'base proxy minor')
        beta = max(Q(jmass*K[n], w[n]) for n in range(len(J)))
        assert beta > 6
        base_minor_count += len(w)
        if m == 0:
            alpha, gamma, tail_outer = Q(4, 5), Q(2), 5
        elif m == 1:
            alpha, gamma, tail_outer = Q(5), Q(40), 4
        elif m == 2:
            alpha, gamma, tail_outer = Q(5), Q(ceilq(4*beta/5)+13), 2
        else:
            alpha, gamma, tail_outer = Q(4), Q(2*ceilq(beta)+13), 2
        Lrow = [low_product(c, t, n)+at(d, n)-2*at(c, n) for n in range(3)]
        Lslope = [4*at(c, n) for n in range(3)]
        Lmass = mass(c)*(mass(t)-2)+mass(d)
        Lbern = central_bern(Lrow, Lslope, Lmass, 4*mass(c), gamma)
        tbern = central_bern([t[0]-2, t[1], t[2]], [4, 0, 0],
                             mass(t)-2, 4, alpha)
        assert min(Lbern) > 0, (m, 'template central margin')
        assert min(tbern) > 0, (m, 'trace central margin')
        if m == 0:
            paired = paired_trace_bern(t, 80)
            assert min(paired) > 0
            # Minimum over both parity classes N>=5 occurs at N=6.
            odd_base = Q(80**2, 5)
            even_base = Q(80**2)*Q(4, 5)/6
            tail_lower = min(odd_base, even_base)
            assert odd_base > beta and even_base > beta
            assert Q(80*5, 7) > 1 and Q(80*6, 8) > 1
        else:
            tail_lower = gamma*alpha**(tail_outer-1)/(2*tail_outer)
            assert tail_lower > beta
            assert alpha*tail_outer/(tail_outer+1) > 1
            paired = None
        records = exact_outer(c, d, t, range(2, tail_outer), beta) if tail_outer > 2 else []
        certificates.append({
            'm': m, 'beta': str(beta), 'alpha_trace': str(alpha),
            'gamma_template': str(gamma), 'outer_tail_start': tail_outer,
            'minimum_base_minor': str(min(w)),
            'base_minor_count': len(w),
            'template_margin_bernstein': [str(v) for v in Lbern],
            'trace_margin_bernstein': [str(v) for v in tbern],
            'paired_trace_80_margin_bernstein': [str(v) for v in paired] if paired else None,
            'outer_tail_central_mass_lower': str(tail_lower),
            'tail_vs_proxy_threshold_residual': str(tail_lower-beta),
            'minimum_fixed_proxy_residual': str(min(tail_lower*w[n]-jmass*K[n]
                                                   for n in range(len(w)))),
            'small_outer_certificates': records,
        })
    result = {
        'status': 'PASS', 'inner_interval': [0, args.limit], 'outer_scope': 'every N>=2',
        'parameter_scope': 'all r in [-2,2]; m0 paired trace all independent r,s in [-2,2]',
        'base_proxy_minors': base_minor_count,
        'small_outer_count': sum(len(r['small_outer_certificates']) for r in certificates),
        'analytic_tail_start': 410, 'analytic_tail_checks': tail_gates(),
        'scope': 'Exact numerical hypotheses of conditional mass/multiplier/proxy theorem. Folded cones, Jacobi compatibility, product closure and reversed-template analytic strength are separate proof dependencies.',
        'certificates': certificates,
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'inner_interval',
                                            'base_proxy_minors', 'small_outer_count')}))


if __name__ == '__main__':
    main()
