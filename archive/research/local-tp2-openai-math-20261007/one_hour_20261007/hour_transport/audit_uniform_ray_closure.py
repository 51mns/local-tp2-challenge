#!/usr/bin/env python3
"""Independent exact all-m finite bridge audit for the new two-turn rays.

Unlike the primary verifier, this reconstructs the seeds directly as
symmetric Laurent half-rows through the inner Chebyshev recurrence.  It
never constructs ordinary-x coefficients, uses no binomial Fourier transform,
and imports no primary verifier.  Quadratic Bernstein coefficients are
recovered from exact endpoint/midpoint values rather than symbolic powers.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json


def trim(h):
    h = list(h)
    while len(h) > 1 and h[-1] == 0:
        h.pop()
    return h


def plus(*rows):
    h = [0] * max(map(len, rows))
    for row in rows:
        for n, a in enumerate(row):
            h[n] += a
    return trim(h)


def times_scalar(h, a):
    return trim([a*v for v in h])


def minus(a, b):
    return plus(a, times_scalar(b, -1))


def convolution(a, b):
    """Product in 1, q^n+q^-n, n>=1 (symmetric Laurent half-rows)."""
    c = [0] * (len(a)+len(b)-1)
    c[0] = a[0]*b[0]
    for i in range(1, len(a)):
        c[i] += a[i]*b[0]
    for j in range(1, len(b)):
        c[j] += a[0]*b[j]
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            v = a[i]*b[j]
            c[i+j] += v
            c[abs(i-j)] += v*(2 if i == j else 1)
    return trim(c)


def at(h, n):
    n = abs(n)
    return h[n] if n < len(h) else 0


def evaluation_one(h):
    return h[0]+2*sum(h[1:])


def defect(h, n):
    a, b, c, d = (at(h, j) for j in (n-1, n, n+1, n+2))
    return b*b-a*c-c*c+b*d


def kernel(h, i, j):
    if i == 0:
        return at(h, j)
    if j == 0:
        return 2*at(h, i)
    return at(h, j-i)+at(h, j+i)


def cell(h, i, n):
    return kernel(h, i, n)*kernel(h, i+1, n+1)-kernel(h, i, n+1)*kernel(h, i+1, n)


def wronskians(p, q):
    return [at(p,n)*at(q,n+1)-at(p,n+1)*at(q,n) for n in range(len(p))]


def bernstein_from_three(values):
    """Twice the quadratic Bernstein coefficients from u=0,1/2,1."""
    left, middle, right = values
    coefficients = [2*left, 4*middle-left-right, 2*right]
    # Invert by evaluation of degree-two Bernstein basis at the same nodes.
    assert coefficients[0] == 2*left
    assert coefficients[-1] == 2*right
    assert coefficients[0]+2*coefficients[1]+coefficients[2] == 8*middle
    return coefficients


def digest(values):
    return sha256(json.dumps(values, separators=(',', ':')).encode()).hexdigest()


def trace(g):
    return minus(times_scalar(convolution(y, g), 3), x)


x, y, P, z = [0, 1], [1, 1], [2, 1], [3, 2]


def main():
    primary_path = Path(__file__).resolve().parent.parent / 'hour_root' / 'uniform_ray_closure_results.json'
    primary = json.loads(primary_path.read_text())
    assert primary['finite_range'] == [0, 76]
    u = [[1], z]
    for _ in range(1, 77):
        u.append(minus(convolution(z, u[-1]), u[-2]))
    T = []
    prefix = [0]
    for h in u:
        prefix = plus(prefix, h)
        T.append(prefix)
    getT = lambda m: T[m] if m >= 0 else [0]
    records = []
    for m in range(77):
        other = plus([1], convolution(y, T[m]))
        t0 = trace(other)
        aX = plus(convolution(T[m+1], plus(t0, [1])), getT(m-1))
        endpoint = plus([1], convolution(y, aX))
        t = trace(endpoint)
        A = minus(convolution(t0, aX), u[m])
        B = u[m+1]
        center = plus(other, convolution(y, A))
        assert len(A)-1 == 3*m+5 and len(B)-1 == m+1
        assert len(t)-1 == 2*m+5
        assert all(v>0 for row in (A, B, endpoint, t) for v in row)
        K0 = plus(t0, [1])
        J = convolution(y, minus(t, [2]))
        V = times_scalar(convolution(convolution(convolution(y,y),endpoint),P),3)
        K = convolution(convolution(endpoint,P),K0)
        assert V == plus(convolution(P,J),convolution(y,convolution(P,P)))
        assert all(defect(K0,n)>0 for n in range(len(K0)))
        w = wronskians(J,V)
        assert min(w)>0
        # Parameter u=0,1/2,1 corresponds to r=2,0,-2, respectively.
        trace_rows = [minus(t,[r]) for r in (2,0,-2)]
        Lrows = [plus(convolution(A,tr),B) for tr in trace_rows]
        Qrows = [convolution(convolution(y,y),L) for L in Lrows]
        Lmass = [evaluation_one(L) for L in Lrows]
        trace_cert = bernstein_from_three([
            defect(tr,0)-2*evaluation_one(tr) for tr in trace_rows])
        assert min(trace_cert)>0
        assert evaluation_one(B)<evaluation_one(A)*(evaluation_one(t)-2)
        proxy = []
        for n in range(len(K)):
            i = min(n,len(J)-1)
            numerator = 2*evaluation_one(J)*K[n]
            alpha = numerator//w[i]+1
            coefficients = bernstein_from_three([
                cell(L,i,n)-alpha*mass for L,mass in zip(Lrows,Lmass)])
            assert min(coefficients)>0,(m,'proxy',n)
            assert alpha*w[i]>numerator
            proxy.append({'n':n,'i':i,'alpha':alpha,'scaled_bernstein':coefficients})
        multiplier = []
        for n in range(len(K0)+1):
            beta = 6*(at(K0,n-1)+3*at(K0,n+1))+1
            coefficients = bernstein_from_three([
                defect(Q,n)-beta*mass for Q,mass in zip(Qrows,Lmass)])
            assert min(coefficients)>0,(m,'multiplier',n)
            multiplier.append({'n':n,'beta':beta,'scaled_bernstein':coefficients})
        q0 = convolution(y,A)
        q1 = convolution(y,plus(convolution(A,t),B))
        beta = convolution(y,plus(A,B))
        E1 = minus(center,endpoint)
        Pi = convolution(P,endpoint)
        orders = {}
        for label,a,b in [('q0_q1',q0,q1),('beta_q1',beta,q1),
                          ('Pi_E1',Pi,E1),('E1_q1',E1,q1)]:
            values = wronskians(a,b)
            assert min(values)>0,(m,label)
            orders[label] = {'minimum':min(values),'count':len(values),'sha256':digest(values)}
        values = trace_cert+[a for r in proxy+multiplier for a in r['scaled_bernstein']]
        record = {'m':m,'degrees':{'A':len(A)-1,'t':len(t)-1,'J':len(J)-1,'K':len(K)-1},
                  'trace_delta0_minus_2mass_scaled_bernstein':trace_cert,
                  'minimum_scaled_bernstein':min(values),'bernstein_count':len(values),
                  'coefficient_sha256':digest(values),
                  'proxy':proxy,'multiplier':multiplier,'initial_orders':orders}
        expected = primary['records'][m]
        assert record == expected, ('primary mismatch',m)
        records.append({k:v for k,v in record.items() if k not in ('proxy','multiplier')})
        if m%10 == 0 or m==76:
            print(json.dumps({'independently_matched_m':m}),flush=True)

    # Independently recompute the exact scalar tail gates from the formulas.
    c0,sigma = Q(1,400000000),Q(59,100)
    def single_eta(m):
        return c0**5*sigma**(5*m+2)/(65536*(m+3)**4)
    def base_eta(m):
        return single_eta(m)*Q(4,49)**m/(6048*(4*m+14))
    def dom(m):
        return Q(27**3*6**(4*m+2),2*(2*m+3)*(2*m+5)**2*(2*m+7))
    def propagation(m):
        return Q(c0**2*sigma**(2*m+1)*27**2*6**(2*m+1),
                 128*(m+3)**2*(2*m+5)*(2*m+7))
    M = 77
    tail = {'E_times_dominance':str(base_eta(M)*dom(M)),
            'normalized_propagation_ratio':str(propagation(M)),
            'dominance':str(dom(M)),
            'consecutive_ratio_Ec':str(base_eta(M+1)*dom(M+1)/(base_eta(M)*dom(M))),
            'consecutive_ratio_propagation':str(propagation(M+1)/propagation(M))}
    assert tail == primary['tail']
    assert base_eta(M)*dom(M)>96
    assert propagation(M)>2 and dom(M)>2
    assert base_eta(M+1)*dom(M+1)/(base_eta(M)*dom(M))>6
    assert propagation(M+1)/propagation(M)>11
    result = {'status':'PASS',
              'independent_method':'Direct symmetric-Laurent Chebyshev recurrence; exact three-value Bernstein reconstruction',
              'finite_range':[0,76],
              'matched_every_primary_record_exactly':True,
              'matched_bernstein_coefficients':sum(r['bernstein_count'] for r in records),
              'matched_initial_order_minors':sum(o['count'] for r in records for o in r['initial_orders'].values()),
              'matched_initial_order_digests':4*len(records),
              'tail_scalar_gates_independently_matched':True,
              'tail_mathematical_argument':'PASS in separate UNIFORM_RAY_INDEPENDENT_AUDIT.md; this script checks scalar arithmetic only.',
              'primary_result_path':'../hour_root/uniform_ray_closure_results.json',
              'records':records}
    output=Path(__file__).with_name('uniform_ray_closure_independent_audit.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':
    main()
