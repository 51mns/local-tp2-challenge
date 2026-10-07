"""Independent small-case proxy audit, ordinary polynomials -> direct Laurent.

The source implementation proxy_mass_cert.py uses Laurent convolution. This
audit imports only this agent's own previously independent ordinary-polynomial,
direct-Laurent, and tensor-Bernstein primitives; no author routines are imported.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import falsification_targeted as t


HERE = Path(__file__).resolve().parent


def mass(a):
    return sum(v*2**i for i, v in enumerate(a))


def central_margin(parts, bound):
    h = t.prow(parts)
    mass_parts = {e: F(mass(a)) for e, a in parts.items() if mass(a)}
    return t.padd(t.pdefect(h, 0), t.pscale(mass_parts, -bound))


def fixed_degree_coefficients(a, degrees):
    # Degree elevation to the advertised (2,2) or (2,0) certificate array.
    from itertools import product
    from math import comb
    values = []
    for indices in product(*(range(d+1) for d in degrees)):
        value = F(0)
        for e, coef in a.items():
            if all(k <= i for k, i in zip(e, indices)):
                term = coef
                for k, i, d in zip(e, indices, degrees):
                    term *= F(comb(i, k), comb(d, k))
                value += term
        values.append(str(value))
    return values


def main():
    author_file = HERE/'proxy_mass_results.json'
    author = json.loads(author_file.read_text())
    assert author['status'] == 'PASS'
    _, prefixes, gs = t.inner(5)
    results = []
    for m, alpha, gamma, tail_start, directNs in [
        (0, F(4, 5), F(2), 5, [2, 3, 4]),
        (1, F(5), F(40), 4, [2, 3]),
        (2, F(5), F(707), 2, [])]:
        c, d, X = prefixes[m], prefixes[m+2], gs[m+1]
        tau = t.sub(t.scale(t.mul([1, 1], X), 3), [0, 1])
        tau2 = t.sub(tau, [2])
        J = t.mul([1, 1], tau2)
        V = t.scale(t.mul(t.mul(t.mul([1, 1], [1, 1]), X), [2, 1]), 3)
        K = t.scale(t.mul(X, t.mul([2, 1], [2, 1])), 2)
        w, hK = t.lr(J, V), t.row(K)
        assert min(w) > 0
        ratios = [F(mass(J)*t.at(hK, n), w[n]) for n in range(len(w))]
        beta = max(ratios)
        expected_beta = [F(221, 3), F(1517, 6), F(2600, 3)][m]
        assert beta == expected_beta
        assert mass(d) < mass(c)*mass(tau2)

        trace_parts = {t.ZERO: tau2, (1, 0, 0): [4]}
        Lparts = {t.ZERO: t.add(t.mul(c, tau2), d),
                  (1, 0, 0): t.scale(c, 4)}
        Tmargin = central_margin(trace_parts, alpha)
        Lmargin = central_margin(Lparts, gamma)
        Tcoeff = fixed_degree_coefficients(Tmargin, (2, 0, 0))
        Lcoeff = fixed_degree_coefficients(Lmargin, (2, 0, 0))
        assert min(map(F, Tcoeff)) > 0 and min(map(F, Lcoeff)) > 0

        paired = None
        if m == 0:
            pairparts = {t.ZERO: t.mul(tau2, tau2),
                         (1, 0, 0): t.scale(tau2, 4),
                         (0, 1, 0): t.scale(tau2, 4),
                         (1, 1, 0): [16]}
            Pmargin = central_margin(pairparts, F(80))
            paired = fixed_degree_coefficients(Pmargin, (2, 2, 0))
            assert paired == list(map(str, [486317, 575113, 666869,
                575113, 768741, 970001, 666869, 970001, 1285693]))
            assert min(map(F, paired)) > 0
            odd5 = F(80**2, 5)
            even6 = F(80**2)*F(4, 5)/6
            assert odd5 > even6 > beta > 6
            assert F(80*5, 7) > 1
            tail_lower = even6
        else:
            tail_lower = gamma*alpha**(tail_start-1)/(2*tail_start)
            assert tail_lower > beta > 6
            assert alpha*tail_start/(tail_start+1) > 1

        direct = []
        _, Rs = t.u_prefix(tau, max(directNs, default=0))
        for N in directNs:
            Z = t.add(t.mul(c, Rs[N]), t.mul(d, Rs[N-1]))
            hz = t.row(Z)
            zdelta, zmass = t.defects(hz)[0], mass(Z)
            residual = F(zdelta)-beta*zmass
            assert residual > 0
            # Compare full row hash plus numerical quantities to the author output.
            item = {'N': N, 'degree_Z': len(Z)-1, 'delta0_Z': str(zdelta),
                    'mass_Z': str(zmass), 'central_to_mass': str(F(zdelta, zmass)),
                    'proxy_mass_residual': str(residual),
                    'row_sha256': hashlib.sha256(
                        json.dumps(hz, separators=(',', ':')).encode()).hexdigest()}
            author_direct = next(a for a in author['certificates'][m]['small_outer_certificates']
                                 if a['N'] == N)
            assert item == author_direct, (m, N, item, author_direct)
            direct.append(item)

        proxy_residuals = [tail_lower*w[n]-mass(J)*t.at(hK, n)
                           for n in range(len(w))]
        assert min(proxy_residuals) > 0
        a = author['certificates'][m]
        compare = {'beta': str(beta), 'alpha_trace': str(alpha),
                   'gamma_template': str(gamma), 'outer_tail_start': tail_start,
                   'minimum_base_minor': str(min(w)), 'base_minor_count': len(w),
                   'template_margin_bernstein': Lcoeff,
                   'trace_margin_bernstein': Tcoeff,
                   'paired_trace_80_margin_bernstein': paired,
                   'outer_tail_central_mass_lower': str(tail_lower),
                   'tail_vs_proxy_threshold_residual': str(tail_lower-beta),
                   'minimum_fixed_proxy_residual': str(min(proxy_residuals)),
                   'small_outer_certificates': direct}
        assert all(a[k] == v for k, v in compare.items()), (m, compare, a)
        results.append({'m': m, 'all_author_arrays_and_small_outer_rows_match': True,
                        **compare})

    output = {'status': 'PASS', 'scope': 'm=0,1,2 full continuum margins and m0N2,3,4/m1N2,3 direct outer rows',
              'independence': 'Own ordinary-polynomial recurrences, direct Laurent expansion and Bernstein primitives, versus author Laurent convolution; no author code imported',
              'proof_limits': 'Checks numerical hypotheses and row identities only; infinite-m, folded-cone and Jacobi-mixture compatibility proof dependencies remain separate',
              'source_script_sha256': hashlib.sha256((HERE/'proxy_mass_cert.py').read_bytes()).hexdigest(),
              'source_results_sha256': hashlib.sha256(author_file.read_bytes()).hexdigest(),
              'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'independent_primitives_sha256': hashlib.sha256((HERE/'falsification_targeted.py').read_bytes()).hexdigest(),
              'records': results}
    (HERE/'falsification_proxy_audit_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
