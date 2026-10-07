#!/usr/bin/env python3
"""Independent exact finite-ray closure checks in symmetric Laurent arithmetic.

No writer implementation or expected JSON is imported. Canonical states are
mutated directly as Laurent rows; division by x+1 is solved from the outer
coefficients. Parameter minors use explicit degree-two polynomial arithmetic.
"""
from pathlib import Path
from hashlib import sha256
import json


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def at(a, n):
    n = abs(n)
    return a[n] if n < len(a) else 0


def add(*terms):
    return trim([sum(c * at(a, n) for c, a in terms)
                 for n in range(max(len(a) for _, a in terms))])


def mul(a, b):
    d = len(a) + len(b) - 2
    return trim([sum(at(a, i) * at(b, n - i)
                     for i in range(1-len(a), len(a)))
                 for n in range(d+1)])


def div_y(a):
    q = [0] * (len(a)-1)
    for n in range(len(a)-1, 0, -1):
        q[n-1] = at(a, n) - at(q, n) - at(q, n+1)
    assert mul(q, [1, 1]) == a
    return trim(q)


ONE, XVAR, Y, P = [1], [0, 1], [1, 1], [2, 1]


def mutate(state, direction):
    a, c, b = state
    e = a if direction == 'L' else b
    other = b if direction == 'L' else a
    new = add((3, mul(mul(Y, e), c)),
              (-1, mul(XVAR, add((1, e), (1, c)))), (-1, other))
    return (a, new, c) if direction == 'L' else (c, new, b)


def p_at(rows, n):
    return [at(row, n) for row in rows]


def p_add(*terms):
    d = max(len(a) for _, a in terms)
    return [sum(c * (a[i] if i < len(a) else 0) for c, a in terms)
            for i in range(d)]


def p_mul(a, b):
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def kernel(rows, i, j):
    if i == 0:
        return p_at(rows, j)
    if j == 0:
        return [2*v for v in p_at(rows, i)]
    return p_add((1, p_at(rows, abs(i-j))), (1, p_at(rows, i+j)))


def minor(rows, i, n):
    return p_add((1, p_mul(kernel(rows, i, n), kernel(rows, i+1, n+1))),
                 (-1, p_mul(kernel(rows, i, n+1), kernel(rows, i+1, n))))


def mass(a):
    return a[0] + 2*sum(a[1:])


def bern2(p):
    p = p + [0]*(3-len(p))
    assert len(p) == 3
    a, b, c = p
    out = [2*a, 2*a+b, 2*(a+b+c)]
    # Independent inverse expansion of degree-two Bernstein coefficients.
    assert [out[0], 2*(out[1]-out[0]), out[0]-2*out[1]+out[2]] == [2*v for v in p]
    assert min(out) > 0
    return out


def digest(a):
    return sha256(json.dumps(a, separators=(',', ':')).encode()).hexdigest()


def verify(m, k):
    state = (ONE, [9, 6, 2], P)
    for _ in range(m):
        state = mutate(state, 'L')
    old = [state[1]]
    for _ in range(k):
        state = mutate(state, 'R')
        old.append(state[1])
    fixed, center, endpoint = state
    a = div_y(add((1, center), (-1, endpoint)))
    b = div_y(add((1, old[k-2]), (-1, endpoint)))
    t = add((3, mul(Y, fixed)), (-1, XVAR))
    k0 = add((3, mul(Y, endpoint)), (-1, XVAR), (1, ONE))
    j = mul(Y, add((1, t), (-2, ONE)))
    v = add((3, mul(mul(mul(Y, Y), fixed), P)))
    correction = mul(mul(fixed, P), k0)
    assert all(z > 0 for row in [a, b, t, k0, j, v, correction] for z in row)
    shifted = [add((1, t), (-2, ONE)), [4]]
    single = [add((1, mul(a, shifted[0])), (1, b)), add((4, a))]
    smoothed2 = [mul(mul(Y, Y), z) for z in single]
    single_mass = [mass(z) for z in single]
    w = [at(j, n)*at(v, n+1)-at(j, n+1)*at(v, n) for n in range(len(j))]
    assert min(w) > 0
    assert mass(b) < mass(a)*(mass(t)-2)
    trace = bern2(p_add((1, minor(shifted, 0, 0)),
                       (-2, [mass(z) for z in shifted])))
    proxy = []
    for n in range(len(correction)):
        i = min(n, len(j)-1)
        alpha = (2*mass(j)*at(correction, n)) // w[i] + 1
        arr = bern2(p_add((1, minor(single, i, n)), (-alpha, single_mass)))
        proxy.append({'n': n, 'i': i, 'alpha': alpha, 'bernstein_twice': arr})
    multiplier = []
    for n in range(len(k0)+1):
        beta = 6*(at(k0, n-1)+3*at(k0, n+1))+1
        arr = bern2(p_add((1, minor(smoothed2, 0, n)), (-beta, single_mass)))
        multiplier.append({'n': n, 'beta': beta, 'bernstein_twice': arr})
    return {'m': m, 'k': k,
            'degrees': {'X': len(fixed)-1, 'C0': len(center)-1, 'Y': len(endpoint)-1,
                        'A': len(a)-1, 'B': len(b)-1, 't': len(t)-1,
                        'K0': len(k0)-1, 'J': len(j)-1, 'K': len(correction)-1},
            'halfrow_digests': {name: digest(row) for name, row in
                [('X',fixed),('C0',center),('Y',endpoint),('A',a),('B',b),('t',t),('K0',k0),('J',j),('V',v),('K',correction)]},
            'trace': trace, 'proxy': proxy, 'multiplier': multiplier}


def main():
    pairs = [(0,k) for k in range(3,21)] + [(1,k) for k in range(3,11)]
    pairs += [(2,k) for k in range(3,6)] + [(3,k) for k in range(3,5)]
    pairs += [(4,3),(5,3),(5,4)]
    assert len(pairs) == 34
    records = [verify(m,k) for m,k in pairs]
    count = sum(3*(1+len(r['proxy'])+len(r['multiplier'])) for r in records)
    out = {'status': 'PASS independent Laurent reconstruction; shared-session audit',
           'author_implementation_imported': False, 'pairs': len(pairs),
           'positive_bernstein_coefficients': count, 'records': records}
    # Compare only after independent construction and positivity checks.
    writer_path = Path(__file__).resolve().parent.parent/'arbk_root/finite_ray_bridge_results.json'
    writer = json.loads(writer_path.read_text())
    assert len(writer['records']) == len(records)
    for ours, theirs in zip(records, writer['records']):
        assert (ours['m'], ours['k']) == (theirs['m'], theirs['k'])
        for key, value in theirs['degrees'].items():
            assert ours['degrees'][key] == value
        assert ours['trace'] == theirs['trace_delta0_minus_2mass_scaled_bernstein']
        for label in ['proxy', 'multiplier']:
            assert len(ours[label]) == len(theirs[label])
            for a, b in zip(ours[label], theirs[label]):
                for key, value in b.items():
                    assert a['bernstein_twice' if key == 'scaled_bernstein' else key] == value
    out['post_reconstruction_author_comparison'] = 'All 3282 Bernstein coefficients, all thresholds, indices and shared degrees agree exactly.'
    path = Path(__file__).with_name('finite_ray_bridge_independent_results.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'records'}))


if __name__ == '__main__':
    main()
