"""Exact Bernstein certificates for mixed-ray folded-kernel blocks."""
from fractions import Fraction as Q
from itertools import product
from math import comb
import json

DIM = 4  # x and three independent parameters in [0,1]
ZERO = (0,) * DIM


def const(v):
    return {ZERO: Q(v)} if v else {}


def variable(i):
    e = [0] * DIM
    e[i] = 1
    return {tuple(e): Q(1)}


def add(*ps):
    out = {}
    for p in ps:
        for e, v in p.items():
            out[e] = out.get(e, Q(0)) + v
    return {e: v for e, v in out.items() if v}


def scale(p, v):
    return {e: v*c for e, c in p.items() if v*c}


def mul(p, q):
    out = {}
    for e, v in p.items():
        for f, w in q.items():
            z = tuple(a+b for a, b in zip(e, f))
            out[z] = out.get(z, Q(0)) + v*w
    return {e: v for e, v in out.items() if v}


def fourier(p):
    h = [{} for _ in range(max(e[0] for e in p)+3)]
    for e, v in p.items():
        for j in range(e[0]//2+1):
            n = e[0]-2*j
            h[n] = add(h[n], {(0,)+e[1:]: v*comb(e[0], j)})
    return h


def defects(p):
    h = fourier(p)
    ds = [add(mul(h[n], h[n]), scale(mul(h[n-1] if n else h[1], h[n+1]), -1))
          for n in range(len(h)-1)]
    return [add(ds[n], scale(ds[n+1], -1)) for n in range(len(ds)-1)]


def bernstein(p):
    ds = tuple(max((e[j] for e in p), default=0) for j in range(1, DIM))
    values = {}
    for indices in product(*(range(d+1) for d in ds)):
        value = Q(0)
        for e, v in p.items():
            powers = e[1:]
            if all(k <= i for k, i in zip(powers, indices)):
                for k, i, degree in zip(powers, indices, ds):
                    v *= Q(comb(i, k), comb(degree, k))
                value += v
        values[','.join(map(str, indices))] = value
    return ds, values


def main():
    x, u, v, z = [variable(i) for i in range(DIM)]
    y = add(x, const(1))
    a, b, c = [add(const(-2), scale(p, 4)) for p in (u, v, z)]
    t = add(scale(mul(mul(x, x), x), 6), scale(mul(x, x), 24), scale(x, 32), const(15))
    w = add(scale(mul(x, x), 4), scale(x, 14), const(12))
    ta, tb = add(t, scale(a, -1)), add(t, scale(b, -1))
    lr_single = add(mul(w, ta), const(1))
    rl_single = add(mul(add(t, w), ta), const(-1))
    lr_pair = add(mul(w, mul(ta, tb)), t, scale(c, -1))
    rl_pair = add(mul(add(t, w), mul(ta, tb)), scale(t, -1), c)
    blocks = {
        'cubic': ta,
        'y_cubic': mul(y, ta),
        'w': w,
        'w_minus_one': add(w, const(-1)),
        'y_w': mul(y, w),
        't_plus_w': add(t, w),
        't_plus_w_plus_one': add(t, w, const(1)),
        'y_t_plus_w': mul(y, add(t, w)),
        'y_t_plus_w_plus_one': mul(y, add(t, w, const(1))),
        'lr_single': lr_single,
        'rl_single': rl_single,
        'y_lr_single': mul(y, lr_single),
        'y_rl_single': mul(y, rl_single),
        'y_lr_degree_two': mul(y, add(mul(w, add(mul(t, t), const(-1))), t)),
        'y_rl_degree_two': mul(y, add(mul(add(t, w), add(mul(t, t), const(-1))), scale(t, -1))),
        'lr_pair_midpoint': lr_pair,
        'rl_pair_midpoint': rl_pair,
    }
    output = {}
    for name, p in blocks.items():
        certs = []
        for n, delta in enumerate(defects(p)):
            # Pair midpoint delta_0 >= 8 supplies all principal minors >= 4.
            offset = 8 if name.endswith('midpoint') and n == 0 else 0
            ds, values = bernstein(add(delta, const(-offset)))
            lower = min(values.values())
            assert lower > 0, (name, n, lower)
            certs.append({
                'n': n,
                'subtracted_margin': offset,
                'parameter_degrees': ds,
                'bernstein_lower_bound': str(lower),
                'power_coefficients': {','.join(map(str, e[1:])): str(v) for e, v in sorted(delta.items())},
                'bernstein_coefficients_after_margin': {k: str(v) for k, v in values.items()},
            })
        output[name] = certs
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
