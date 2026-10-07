"""Exact continuum certificates for H=A(t-r)(t-s)+B(t-c).

All integer arithmetic. The 27 tensor Bernstein coefficients at each
Fourier index cover the entire independent parameter cube [-2,2]^3.
Kronecker multiplication packs nonnegative coefficients with a proved
carry-free base. No parameter or Fourier-index sampling is used.
"""
import argparse
import hashlib
import itertools
import json
import time


def at(a, n):
    n = abs(n)
    return a[n] if n < len(a) else 0


def add(a, b):
    return [at(a, n) + at(b, n) for n in range(max(len(a), len(b)))]


def times(a, b):
    aa, bb = a[:0:-1] + a, b[:0:-1] + b
    bound = min(len(aa), len(bb)) * max(aa) * max(bb)
    width = max(1, (bound.bit_length() + 7) // 8)
    assert (1 << (8 * width)) > bound
    pa = int.from_bytes(b''.join(x.to_bytes(width, 'little') for x in aa), 'little')
    pb = int.from_bytes(b''.join(x.to_bytes(width, 'little') for x in bb), 'little')
    size = len(aa) + len(bb) - 1
    raw = (pa * pb).to_bytes(size * width, 'little')
    centre = len(a) + len(b) - 2
    return [int.from_bytes(raw[n*width:(n+1)*width], 'little')
            for n in range(centre, size)]


def prefixes(maximum):
    prev, u, total = [0], [1], [1]
    out = [total]
    for _ in range(maximum):
        new = [3*at(u, n) + 2*at(u, n-1) + 2*at(u, n+1) - at(prev, n)
               for n in range(len(u)+1)]
        assert min(new) > 0
        total = add(total, new)
        out.append(total)
        prev, u = u, new
    return out


def weights(a, b, c):
    ca, cb, cc = a*(a-1)//2, b*(b-1)//2, c*(c-1)//2
    matrix = [[8, 4*(a+b), 2*a*b, 4*c],
              [0, 8*(ca+cb)+4*a*b, 4*(ca*b+cb*a), 2*(a+b)*c],
              [0, 0, 8*ca*cb, a*b*c],
              [0, 0, 0, 8*cc]]
    return [matrix[i][j] for i in range(4) for j in range(i, 4)], matrix[0]


INDICES = list(itertools.product(range(3), repeat=3))
WEIGHTS = [weights(*abc) for abc in INDICES]


def certify(m, ts, smooth=False):
    A, B = ts[m+1], ts[m-1]
    if smooth:
        A, B = times([1, 1], A), times([1, 1], B)
    p = times([3, 2, 1], ts[m])  # y^2 has half-row (3,2,1)
    t = [3*x for x in p]
    t[0] += 5  # t+2 = 3 y^2 T_m + 2x + 5
    t[1] += 2
    atrow = times(A, t)
    base = add(times(atrow, t), times(B, t))
    comps = [base, [-4*x for x in atrow], [16*x for x in A], [-4*x for x in B]]
    mu = 8*B[0]
    minimum = None
    witness = None
    digest = hashlib.sha256()
    negative = zero = 0
    for n in range(len(base)):
        v = [[at(row, j) for row in comps] for j in [n-1, n, n+1, n+2]]
        prev, cur, nex, nex2 = v
        quad = []
        for i in range(4):
            for j in range(i, 4):
                if i == j:
                    q = cur[i]*cur[i] - prev[i]*nex[i] - nex[i]*nex[i] + cur[i]*nex2[i]
                else:
                    q = (2*cur[i]*cur[j] - prev[i]*nex[j] - prev[j]*nex[i]
                         - 2*nex[i]*nex[j] + cur[i]*nex2[j] + cur[j]*nex2[i])
                quad.append(q)
        for abc, (w, linear) in zip(INDICES, WEIGHTS):
            margin = sum(x*y for x, y in zip(w, quad)) - mu*sum(x*y for x, y in zip(linear, cur))
            digest.update((str(margin)+'\n').encode())
            negative += margin < 0
            zero += margin == 0
            if minimum is None or margin < minimum:
                minimum, witness = margin, [n, *abc]
    return dict(m=m, degree=len(base)-1, margins=27*len(base), negative=negative,
                zero=zero, minimum=str(minimum), witness=witness, sha256=digest.hexdigest())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', type=int, default=1)
    parser.add_argument('--max', type=int, default=390)
    parser.add_argument('--output', default='fulltree_oneturn_finite_results.json')
    parser.add_argument('--smooth', action='store_true', help='replace A and B by yA and yB')
    args = parser.parse_args()
    start = time.monotonic()
    ts = prefixes(args.max+1)
    results = []
    for m in range(args.min, args.max+1):
        result = certify(m, ts, args.smooth)
        results.append(result)
        if result['negative'] or result['zero'] or m % 10 == 0 or m == args.max:
            print(json.dumps({k: result[k] for k in ['m', 'degree', 'negative', 'zero', 'witness']}), flush=True)
        with open(args.output, 'w') as f:
            json.dump(dict(status='PASS' if all(x['negative']==x['zero']==0 for x in results) else 'FAIL',
                           scope=[args.min, m], smooth=args.smooth,
                           scaling='8 times Bernstein coefficient of delta_n(H)-8 H(B)_0 H(H)_n; with A,B replaced by yA,yB if smooth',
                           elapsed_seconds=round(time.monotonic()-start, 3), cases=results), f, indent=2)


if __name__ == '__main__':
    main()
