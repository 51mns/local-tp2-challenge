#!/usr/bin/env python3
"""Exact targeted counterexamples/domain checks. No broad state/parameter scan."""
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'common_transport_20261004'))
from adversarial_probe import add, at, build, children, defects, H, mul, power, scale, sub, y, y2, P, z


def relative(p, q):
    hp, hq = H(p), H(q)
    degree = max(len(hp), len(hq))
    out = {}
    for k in range(degree):
        for l in range(k + 1, degree):
            value = at(hp, k) * at(hq, l) - at(hp, l) * at(hq, k)
            if value:
                a, b = k + l - 1, l - k - 1
                out[a, b] = value
                if a != b:
                    out[b, a] = value
    return out


def tensor(p):
    return relative(p, mul([0, 1], p))


def cadd(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def cscale(term, scalar):
    return {key: scalar * value for key, value in term.items() if scalar * value}


def mixed(p, q):
    return cadd(tensor(add(p, q)), cscale(tensor(p), -1), cscale(tensor(q), -1))


def cgprod(left, right):
    out = {}
    for (a, b), u in left.items():
        for (c, d), v in right.items():
            for i in range(abs(a - c), a + c + 1, 2):
                for j in range(abs(b - d), b + d + 1, 2):
                    out[i, j] = out.get((i, j), 0) + u * v
    return {key: value for key, value in out.items() if value}


def first_negative(term):
    return next(({'character': list(key), 'value': value} for key, value in sorted(term.items()) if value < 0), None)


def canonical(path):
    state = build([0], [1], [1])
    for letter in path:
        state = dict(children(state))['short' if letter == 's' else 'long']
    return state


def anchored_flux_checks():
    records = []
    for move, state in children(canonical('')):
        trace = sub(state['M'], [1])
        n = state['e']
        c = add(n, state['g'], state['s'])
        zz = add(trace, [1])
        anchor = add(mul(n, zz), c)
        direct_flux = cadd(mixed(anchor, mul(n, zz)), cscale(mixed(mul(anchor, zz), n), -1))
        factored_flux = cgprod(cgprod(cgprod({(2, 0): 1, (0, 0): -3}, {(0, 2): 1, (0, 0): -3}), relative([1], zz)), relative(anchor, n))
        assert direct_flux == factored_flux
        d, f = len(zz) - 1, len(anchor) - 1
        column = f + d + 1
        far = direct_flux.get((column - 1, column - 1), 0)
        assert far == -H(n)[0] * mul(anchor, zz)[-1] < 0
        # Independently replay the anchored whole-certificate identity at three
        # genuinely distinct parameter pairs, in both modes.
        for r, s in ((-2, 2), (-2, 0), (0, 2)):
            alpha, omega = Fraction(r + s, 2), Fraction((r - s) ** 2, 4)
            eta, kappa = alpha + 1, (r + 1) * (s + 1)
            A = cadd(tensor(zz), cscale(mixed(zz, [1]), -eta), {(0, 0): kappa})
            for smooth in (False, True):
                B, N, C = (mul(y, p) for p in (anchor, n, c)) if smooth else (anchor, n, c)
                K = cadd(tensor(B), cscale(tensor(N), kappa), cscale(mixed(B, N), -eta))
                F = cadd(mixed(B, mul(N, zz)), cscale(mixed(mul(B, zz), N), -1))
                hh = add(mul(N, mul(sub(trace, [r]), sub(trace, [s]))), mul(C, sub(trace, [alpha])))
                target = cadd(tensor(hh), cscale(tensor(C), -omega))
                assert target == cadd(cgprod(A, K), cscale(F, omega))
        records.append({'move': move, 'trace_degree': d, 'anchor_degree': f,
                        'central_flux': direct_flux[0, 0],
                        'far_columns': [0, column], 'far_character': [column - 1, column - 1],
                        'n_fourier_zero': H(n)[0], 'lc_anchor_times_z': mul(anchor, zz)[-1],
                        'far_flux': far, 'identity_checks': 6})
    return records


def relaxed_updates():
    beta = scale(y2, 3)
    out = []
    for name, trace, e in (
        ('linear_low_complexity', [20, 10], [1]),
        ('cubic_trace_divisibility', [11, 22, 16, 4], [5, 2]),
    ):
        c, g, v, n = scale(e, 2), [0], e, e
        u = sub(trace, mul(beta, n))
        child_trace = add(trace, mul(beta, v))
        child_c = add(mul(add(u, [1]), v), e)
        child_L0 = add(mul(child_c, child_trace), n)
        assert child_c[-1] < 0 and child_L0[-1] < 0
        record = {'name': name, 'T': trace, 'e': e, 'c': c, 'g': g, 's': v,
                  'u': u, 'short_T': child_trace, 'short_c': child_c,
                  'short_forward_L0_degree': len(child_L0) - 1,
                  'short_forward_L0_leading_coefficient': child_L0[-1]}
        if name.startswith('cubic'):
            B = [Fraction(8, 3), Fraction(4, 3)]
            assert trace == add(z, mul(beta, B))
            record['canonical_B'] = B
            record['implied_a'] = sub(B, e)
            assert min(record['implied_a']) < 0
            assert H(trace) == [43, 34, 16, 4]
            assert defects(H(trace)) == [225, 348, 104, 16]
            assert defects(H(e)) == [17, 4]
            assert defects(H(mul(y, e))) == [1, 27, 4]
        out.append(record)
    return out


def targeted_new_gates():
    out = []
    for path in ('', 's', 'l', 'ss', 'sl', 'ls', 'll'):
        state = canonical(path)
        F = sub(state['E'], mul(state['X'], P))
        short = dict(children(state))['short']
        long = dict(children(state))['long']
        assert sub(short['E'], mul(short['X'], P)) == add(F, state['G'])
        a, e, r = (state[key] for key in ('a', 'e', 'r'))
        long_formula = add(mul([-1, 0, 1], e), [0, 1], mul(y, sub(r, [1])),
                           mul(mul(y, a), [2, 3]), scale(mul(power(y, 3), mul(a, add(a, e))), 3))
        assert sub(long['E'], mul(long['X'], P)) == long_formula
        tensors = {'G_Pi': relative(state['G'], state['Pi']),
                   'S_FM': relative(state['S'], mul(F, state['M'])),
                   'Q_DminusPQ': relative(state['Q'], sub(state['D'], mul(P, state['Q']))),
                   'Q_shortnextQ': relative(state['Q'], short['Q']),
                   'short_proxy_increment': cadd(relative(short['Q'], short['Pi']), cscale(relative(state['Q'], state['Pi']), -1))}
        assert all(first_negative(term) is None for term in tensors.values())
        out.append({'path': path or 'ROOT', 'F_fourier_row': H(F),
                    'negative_characters': {key: first_negative(term) for key, term in tensors.items()},
                    'Q_DminusPQ_minimum_nonzero': min(tensors['Q_DminusPQ'].values())})
    return out


def restricted_advance_checks():
    trace = [Fraction(41, 12), 1]
    previous, current = [0], [1]
    endpoints = [Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1)]
    out = []
    for index in range(1, 5):
        previous, current = current, sub(mul(trace, current), previous)
        for r in endpoints:
            for s in endpoints:
                alpha, omega = (r + s) / 2, (r - s) ** 2 / 4
                hh = sub(mul(current, mul(sub(trace, [r]), sub(trace, [s]))), mul(previous, sub(trace, [alpha])))
                certificate = cadd(tensor(hh), cscale(tensor(previous), -omega))
                assert first_negative(certificate) is None
        out.append({'N': index, 'fixed_pairs': 25, 'negative_characters': 0})
    return out


def exact_json(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    beta = scale(y2, 3)
    assert defects(H(beta)) == [36, 0, 9]
    assert defects(H(y))[0] == -1
    assert defects(H(mul(y, beta)))[0] == -18
    results = {
        'scope': 'EXACT TARGETED GATES; NO FULL CLOSURE CLAIM',
        'anchored_flux': anchored_flux_checks(),
        'relaxed_paired_packet_counterexamples': relaxed_updates(),
        'new_canonical_gate_checks': targeted_new_gates(),
        'restricted_fixed_trace_advance': restricted_advance_checks(),
        'multiplier_rows': {'y': H(y), 'beta': H(beta), 'y_beta': H(mul(y, beta))},
        'multiplier_defects': {'y': defects(H(y)), 'beta': defects(H(beta)), 'y_beta': defects(H(mul(y, beta)))},
    }
    path = HERE / 'falsification_crosscenter_results.json'
    path.write_text(json.dumps(results, indent=2, default=exact_json) + '\n')
    print(json.dumps({'anchored_flux': results['anchored_flux'],
                      'relaxed_packet_failures': [{'name': r['name'], 'short_c': r['short_c'], 'L0_lc': r['short_forward_L0_leading_coefficient']} for r in results['relaxed_paired_packet_counterexamples']],
                      'canonical_new_gate_states': len(results['new_canonical_gate_checks']),
                      'restricted_advance_fixed_cases': 100}, indent=2))


if __name__ == '__main__':
    main()
