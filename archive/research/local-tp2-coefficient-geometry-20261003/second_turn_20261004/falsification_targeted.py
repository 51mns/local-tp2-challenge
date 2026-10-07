"""Independent exact targeted checks for the additional-turn mechanism.

All load-bearing polynomial, Laurent, and Bernstein operations are written
here. Parent scripts are source-provenance dependencies only, not imports.
No floating point and no numerical root approximation are used.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * x for x in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def child(t, c, z):
    # Frozen canonical mutation from verify.py, independently implemented.
    return sub(sub(scale(mul(mul([1, 1], t), c), 3),
                   mul([0, 1], add(t, c))), z)


def state(word):
    a, c, b = [1], [5, 6, 2], [2, 1]
    for turn in word:
        if turn == 'L':
            a, c, b = a, child(a, c, b), c
        else:
            a, c, b = c, child(b, c, a), b
    return a, c, b


def row(a):
    # Direct Laurent substitution via repeated multiplication by z+z^-1.
    # This deliberately avoids the binomial Fourier formula in verify.py.
    out, mono = {}, {0: 1}
    for coef in a:
        for n, x in mono.items():
            out[n] = out.get(n, 0) + coef * x
        nxt = {}
        for n, x in mono.items():
            nxt[n - 1] = nxt.get(n - 1, 0) + x
            nxt[n + 1] = nxt.get(n + 1, 0) + x
        mono = nxt
    assert all(out.get(-n, 0) == v for n, v in out.items())
    return trim([out.get(n, 0) for n in range(len(a))])


def at(a, n):
    return a[abs(n)] if abs(n) < len(a) else 0


def defects(a):
    return [at(a, n)**2 - at(a, n-1)*at(a, n+1)
            - at(a, n+1)**2 + at(a, n)*at(a, n+2)
            for n in range(len(a))]


def lr(a, b):
    a, b = row(a), row(b)
    return [at(a, n)*at(b, n+1)-at(a, n+1)*at(b, n)
            for n in range(len(a))]


def u_prefix(trace, maximum):
    us = [[1]]
    ts = [[1]]
    prev = [0]
    for j in range(1, maximum + 1):
        nxt = sub(mul(trace, us[-1]), prev)
        prev = us[-1]
        us.append(nxt)
        ts.append(add(ts[-1], nxt))
    return us, ts


def inner(maximum):
    us, ts = u_prefix([3, 2], maximum)
    return us, ts, [add([1], mul([1, 1], t)) for t in ts]


ZERO = (0, 0, 0)


def padd(*args):
    out = {}
    for a in args:
        for k, v in a.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def pscale(a, c):
    return {k: v*c for k, v in a.items() if v*c}


def pmul(a, b):
    out = {}
    for k, v in a.items():
        for l, w in b.items():
            e = tuple(x+y for x, y in zip(k, l))
            out[e] = out.get(e, F(0)) + v*w
    return {k: v for k, v in out.items() if v}


def prow(parts):
    rows = {e: row(a) for e, a in parts.items()}
    length = max(len(a) for a in rows.values())
    return [{e: F(at(a, n)) for e, a in rows.items() if at(a, n)}
            for n in range(length)]


def pat(a, n):
    return a[abs(n)] if abs(n) < len(a) else {}


def pdefect(a, n):
    return padd(pmul(pat(a, n), pat(a, n)),
                pscale(pmul(pat(a, n-1), pat(a, n+1)), -1),
                pscale(pmul(pat(a, n+1), pat(a, n+1)), -1),
                pmul(pat(a, n), pat(a, n+2)))


def bernstein(a):
    degrees = tuple(max((e[j] for e in a), default=0) for j in range(3))
    values = {}
    for idx in product(*(range(d+1) for d in degrees)):
        value = F(0)
        for e, coef in a.items():
            if all(k <= j for k, j in zip(e, idx)):
                term = coef
                for k, j, d in zip(e, idx, degrees):
                    term *= F(comb(j, k), comb(d, k))
                value += term
        values[idx] = value
    return degrees, values


def peval(a, parameters):
    return sum(v*parameters[0]**e[0]*parameters[1]**e[1]
               *parameters[2]**e[2] for e, v in a.items())


def certificate(a):
    degrees, coefficients = bernstein(a)
    minimum = min(coefficients.values())
    return {'degrees': list(degrees), 'minimum': str(minimum),
            'minimum_indices': list(min(coefficients, key=coefficients.get)),
            'power': {','.join(map(str, e)): str(v) for e, v in sorted(a.items())},
            'bernstein': {','.join(map(str, e)): str(v)
                          for e, v in sorted(coefficients.items())}}


def blocks(c, d, tau, smooth=False):
    t2 = add(tau, [2])
    single_parts = {ZERO: add(mul(c, t2), d),
                    (1, 0, 0): scale(c, -4)}
    midpoint_parts = {ZERO: add(mul(c, mul(t2, t2)), mul(d, t2)),
                      (1, 0, 0): scale(mul(c, t2), -4),
                      (0, 1, 0): scale(mul(c, t2), -4),
                      (1, 1, 0): scale(c, 16),
                      (0, 0, 1): scale(d, -4)}
    if smooth:
        single_parts = {e: mul([1, 1], a) for e, a in single_parts.items()}
        midpoint_parts = {e: mul([1, 1], a) for e, a in midpoint_parts.items()}
    return prow(single_parts), prow(midpoint_parts)


def kernel(h, i, j):
    if i == 0:
        return pat(h, j)
    if j == 0:
        return pscale(pat(h, i), 2)
    return padd(pat(h, abs(i-j)), pat(h, i+j))


def minor(h, i, j, k, l):
    return padd(pmul(kernel(h, i, k), kernel(h, j, l)),
                pscale(pmul(kernel(h, i, l), kernel(h, j, k)), -1))


def simple_summary(a):
    return {'minimum': str(min(a)), 'minimum_index': a.index(min(a)),
            'checked': len(a), 'nonnegative': min(a) >= 0,
            'strict': min(a) > 0}


def canonical_checks(maxm=8):
    us, ts, gs = inner(maxm+2)
    records = []
    for m in range(maxm+1):
        P, X, c, d = gs[m], gs[m+1], ts[m], ts[m+2]
        tau = sub(scale(mul([1, 1], X), 3), [0, 1])
        oldtau = sub(scale(mul([1, 1], P), 3), [0, 1])
        C1 = child(P, X, [1])
        assert state('L'*m+'R') == (X, C1, P)
        assert sub(C1, P) == mul([1, 1], add(mul(tau, c), d))
        outus, outts = u_prefix(tau, 15)
        for ell in [0, 1, 2, 3, 5, 8, 13]:
            Q = add([1], mul([1, 1], add(mul(c, outts[ell+1]),
                                        mul(d, outts[ell]))))
            prev = P if ell == 0 else add([1], mul([1, 1],
                   add(mul(c, outts[ell]), mul(d, outts[ell-1]))))
            newgap = mul([1, 1], add(mul(c, outus[ell+1]),
                                     mul(d, outus[ell])))
            assert sub(Q, prev) == newgap
            sa, sc, sb = state('L'*m+'R'+'L'*ell)
            assert sc == Q
            assert (sa, sb) == ((X, P) if ell == 0 else (X, prev))
            if ell:
                left, right = child(sa, sc, sb), child(sb, sc, sa)
                short, long = sorted([left, right], key=len)
                S, D = sub(short, sc), sub(long, short)
                assert short == child(X, Q, prev)
                expectedS = mul([1, 1], add(mul(c, outus[ell+2]),
                                            mul(d, outus[ell+1])))
                assert S == expectedS
                Z = add(mul(c, outts[ell+1]), mul(d, outts[ell]))
                J = mul([1, 1], sub(tau, [2]))
                V = scale(mul(mul(mul([1, 1], [1, 1]), X), [2, 1]), 3)
                K = scale(mul(X, mul([2, 1], [2, 1])), 2)
                proxy = add(mul(V, Z), K)
                checks = {
                    'Local_TP2': simple_summary(lr(S, D)),
                    'final_proxy': simple_summary(lr(mul(J, Z), proxy)),
                    'short_upper': simple_summary(lr(S, mul(J, Z))),
                    'proxy_lower': simple_summary(lr(proxy, D)),
                }
                assert all(q['nonnegative'] for q in checks.values()), (m, ell, checks)
                records.append({'m': m, 'ell': ell, 'N': ell+1,
                                'degree_center': len(Q)-1, 'checks': checks})
        oldq1 = sub(C1, X)
        newq1 = sub(C1, P)
        newq2 = mul([1, 1], add(mul(c, outus[2]), mul(d, outus[1])))
        beta = mul([1, 1], add(c, d))
        init = {
            'q1_q2': lr(newq1, newq2),
            'beta_q2': lr(beta, newq2),
            'beta_oldq1': lr(beta, oldq1),
            'P1_X_oldq1': lr(mul([2, 1], X), oldq1),
            'p_mplus2_oldq1': lr(mul([1, 1], us[m+2]), oldq1),
            'beta_p_mplus2': lr(beta, mul([1, 1], us[m+2])),
        }
        records.append({'m': m, 'initial_LR': {
            name: simple_summary(a) for name, a in init.items()}})
    return records


def continuum_checks(maxm=8):
    _, ts, gs = inner(maxm+2)
    output, exact_failures = [], []
    for m in range(maxm+1):
        c, d, X = ts[m], ts[m+2], gs[m+1]
        tau = sub(scale(mul([1, 1], X), 3), [0, 1])
        for smooth in [False, True]:
            L, H = blocks(c, d, tau, smooth)
            baseline = mul([1, 1], d) if smooth else d
            target = 8*row(baseline)[0]
            candidate_lambda = F(3)*F(2)**(2*m-1)
            conservative_lambda = F(3)*F(2)**(2*m-3)
            record = {'m': m, 'smooth': smooth, 'degree_single': len(L)-1,
                      'degree_midpoint': len(H)-1, 'relative_strength_target': str(target)}
            alpha = row(tau)[0]-2
            record['domination_alpha'] = str(alpha)
            for name, h, strength, defect_scale in [
                ('single_candidate_strength', L, candidate_lambda, 1),
                ('single_conservative_strength', L, conservative_lambda, 1),
                ('midpoint_relative_strength', H, target, 1),
                ('midpoint_scaled_relative_strength', H, target, alpha),
                ('midpoint_cone', H, F(0), 1)]:
                arrays = [certificate(padd(pscale(pdefect(h, n), defect_scale),
                                           pscale(h[n], -strength)))
                          for n in range(len(h))]
                record[name] = {
                    'lambda': str(strength), 'defect_scale': str(defect_scale),
                    'all_bernstein_nonnegative':
                    all(F(a['minimum']) >= 0 for a in arrays),
                    'arrays': arrays}
                # A negative Bernstein coefficient is not a counterexample.
                # Only exact cube-corner evaluations below are reported as failures.
                for n in range(len(h)):
                    margin = padd(pscale(pdefect(h, n), defect_scale),
                                  pscale(h[n], -strength))
                    for corner in product([F(0), F(1)], repeat=3):
                        v = peval(margin, corner)
                        if v < 0:
                            exact_failures.append({'m': m, 'smooth': smooth,
                                'condition': name, 'index': n,
                                'unit_parameters': [str(x) for x in corner],
                                'parameters': [str(-2+4*x) for x in corner],
                                'margin': str(v), 'lambda': str(strength),
                                'defect_scale': str(defect_scale),
                                'h_n': str(peval(h[n], corner)),
                                'delta_n': str(peval(pdefect(h, n), corner))})
            output.append(record)
    return output, exact_failures


def fixed_proxy_checks(maxm=8):
    _, ts, gs = inner(maxm+2)
    output = []
    for m in range(maxm+1):
        c, d, X = ts[m], ts[m+2], gs[m+1]
        tau = sub(scale(mul([1, 1], X), 3), [0, 1])
        J = mul([1, 1], sub(tau, [2]))
        V = scale(mul(mul(mul([1, 1], [1, 1]), X), [2, 1]), 3)
        K = scale(mul(X, mul([2, 1], [2, 1])), 2)
        hj, hk, w = row(J), row(K), lr(J, V)
        massJ = sum(hj[1:])*2+hj[0]
        assert min(w) > 0
        ratios = [F(massJ*at(hk, n), w[n]) for n in range(len(hj))]
        top = max(ratios)
        ceil = (top.numerator+top.denominator-1)//top.denominator
        gamma = 2*ceil+13
        L, _ = blocks(c, d, tau)
        massL = {ZERO: F(sum(add(mul(c, add(tau, [2])), d)[i]*2**i
                           for i in range(len(add(mul(c, add(tau, [2])), d))))),
                 (1, 0, 0): F(-4*sum(c[i]*2**i for i in range(len(c))))}
        Lmargin = padd(pdefect(L, 0), pscale(massL, -gamma))
        T = prow({ZERO: add(tau, [2]), (1, 0, 0): [-4]})
        massT = {ZERO: F(sum(add(tau, [2])[i]*2**i
                          for i in range(len(add(tau, [2]))))),
                 (1, 0, 0): F(-4)}
        Tmargin = padd(pdefect(T, 0), pscale(massT, -4))
        lc, tc = certificate(Lmargin), certificate(Tmargin)
        remainders = [gamma*w[n]-2*massJ*at(hk, n) for n in range(len(hj))]
        item = {'m': m, 'gamma': str(gamma), 'max_proxy_ratio': str(top),
                'max_proxy_ratio_index': ratios.index(top),
                'base_proxy': simple_summary(w),
                'proxy_remainder': simple_summary(remainders),
                'single_central_margin': lc, 'trace_central_margin': tc}
        assert min(remainders) > 0
        item['sufficient_criterion_bernstein_pass'] = F(lc['minimum']) > 0 and F(tc['minimum']) > 0
        item['exact_corner_failures'] = []
        for name, margin in [('single_central', Lmargin), ('trace_central', Tmargin)]:
            for u in [F(0), F(1)]:
                value = peval(margin, (u, F(0), F(0)))
                if value < 0:
                    item['exact_corner_failures'].append({'condition': name,
                        'r': str(-2+4*u), 'margin': str(value)})
        output.append(item)
    return output


def relative_checks(maxm=1):
    _, ts, gs = inner(maxm+2)
    output = []
    for m in range(maxm+1):
        c, d, X = ts[m], ts[m+2], gs[m+1]
        tau = sub(scale(mul([1, 1], X), 3), [0, 1])
        for smooth in [False, True]:
            _, h = blocks(c, d, tau, smooth)
            b = prow({ZERO: mul([1, 1], d) if smooth else d})
            dh, db = len(h)-1, len(b)-1
            limit = dh+db+1
            patterns, minimum, minwitness = 0, None, None
            digest = hashlib.sha256()
            for i in range(limit+1):
                for gap in range(1, limit+1):
                    j = i+gap
                    for e in range(-db, db+1):
                        k = i+e
                        if k < 0:
                            continue
                        for f in range(-db, db+1):
                            l = j+f
                            if l <= k:
                                continue
                            mb = minor(b, i, j, k, l).get(ZERO, F(0))
                            if mb <= 0:
                                continue
                            margin = padd(minor(h, i, j, k, l), {ZERO: -4*mb})
                            degrees, values = bernstein(margin)
                            lower = min(values.values())
                            digest.update((str((i, j, k, l))+':'+str(lower)+'\n').encode())
                            patterns += 1
                            if minimum is None or lower < minimum:
                                minimum, minwitness = lower, [i, j, k, l]
                            assert lower >= 0, (m, smooth, [i, j, k, l], lower)
            item = {'m': m, 'smooth': smooth, 'degree_H': dh, 'degree_B': db,
                    'representative_limit': limit,
                    'positive_baseline_minor_patterns': patterns,
                    'minimum_bernstein': str(minimum), 'minimum_pattern': minwitness,
                    'sha256_pattern_bounds': digest.hexdigest()}
            print(json.dumps({'relative_completed': item}), flush=True)
            output.append(item)
    return output


def main():
    canon = canonical_checks()
    Path(HERE/'falsification_canonical_results.json').write_text(
        json.dumps(canon, indent=2)+'\n')
    print('Canonical candidate formulas and finite final comparisons PASS', flush=True)
    continuum, failures = continuum_checks()
    Path(HERE/'falsification_continuum_results.json').write_text(
        json.dumps({'records': continuum, 'exact_corner_failures': failures}, indent=2)+'\n')
    print(json.dumps({'continuum_records': len(continuum),
                      'exact_corner_failures': len(failures),
                      'first_failure': failures[:1]}), flush=True)
    proxy = fixed_proxy_checks()
    Path(HERE/'falsification_fixed_proxy_results.json').write_text(
        json.dumps(proxy, indent=2)+'\n')
    print(json.dumps({'fixed_proxy_small_failures': [
        {'m': a['m'], 'gamma': a['gamma'], 'failures': a['exact_corner_failures']}
        for a in proxy if not a['sufficient_criterion_bernstein_pass']]}), flush=True)
    # Root requested no further relative enumeration once scaled condition passed.
    # The previous completed m=0,1 representative results remain available.
    old_results = json.loads((HERE/'falsification_results.json').read_text())
    relative = old_results['relative']
    sources = ['verify.py', 'general_one_turn_reduction.md',
               'mixed_kernel_all_minor_strength.md', 'fulltree_oneturn_mass_proxy.md',
               'general_one_turn_kernel_cert.py', 'second_turn_20261004/BRIEF.md']
    provenance = {s: hashlib.sha256((BASE/s).read_bytes()).hexdigest() for s in sources}
    Path(HERE/'falsification_results.json').write_text(json.dumps({
        'status': 'PASS with falsified overstrong sufficient premise',
        'arithmetic': 'exact independent integer/Fraction polynomial, direct Laurent, Bernstein',
        'canonical_finite_scope': {'m': [0, 8], 'ell': [0, 1, 2, 3, 5, 8, 13]},
        'continuum_scope': {'m': [0, 8], 'r_s_u': 'entire [-2,2]^3'},
        'relative_minor_scope': {'m': [0, 1], 'r_s_u': 'entire [-2,2]^3'},
        'exact_failures': failures, 'relative': relative,
        'fixed_proxy_scope': {'m': [0, 8], 'r': 'entire [-2,2]'},
        'source_sha256': provenance,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'infinite_family_status': 'NOT_PROVED by these bounded checks'}, indent=2)+'\n')


if __name__ == '__main__':
    main()
