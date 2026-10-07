"""Independent sparse-integer symbolic audit, with no imported research code.

Verifies arbitrary-symbol identities, including inductive certificates for
all-depth normalized recurrence and all-index polynomial barriers.
"""
from pathlib import Path
import hashlib
import json
from math import comb

N = 8

class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.c = value.c.copy()
        elif isinstance(value, dict):
            self.c = {m:c for m,c in value.items() if c}
        else:
            self.c = {(0,)*N: value} if value else {}

    def __add__(self, other):
        out = self.c.copy()
        for m,c in P(other).c.items():
            out[m] = out.get(m,0)+c
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m:-c for m,c in self.c.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) + (-self)

    def __mul__(self, other):
        out = {}
        for m,c in self.c.items():
            for n,d in P(other).c.items():
                k = tuple(a+b for a,b in zip(m,n))
                out[k] = out.get(k,0)+c*d
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, k):
        out = P(1)
        for _ in range(k):
            out = out*self
        return out

    def __eq__(self, other):
        return self.c == P(other).c

    def nonnegative(self):
        return all(c>=0 for c in self.c.values())

    @classmethod
    def var(cls, i):
        k=[0]*N; k[i]=1
        return cls({tuple(k):1})


def main():
    results={}
    def check(name, left, right=0):
        assert left==right, name
        results[name]='PASS'

    x,a,e,g,r,z,p,q=[P.var(i) for i in range(N)]
    y=x+1
    X=1+y*a
    Y=X+y*e
    C=Y+y*g
    t=3*y*X-x
    T=t-2
    k=X*(3*X-2)
    check('t_normalization', t, 2*x+3+3*y*y*a)
    check('k_normalization', k, (1+y*a)*(1+3*y*a))
    U=3*y*X*C-x*(X+C)-Y
    V=3*y*Y*C-x*(Y+C)-X
    s=(t-1)*g+(t-2)*e+k
    M=t+1+3*y*y*(e+g)
    check('actual_S_formula', U-C, y*s)
    check('actual_D_formula', V-U, y*e*M)
    check('short_r_identity', U-C-y*(T*(e+g)+k), y*g)
    ty=3*y*Y-x
    ky=Y*(3*Y-2)
    check('long_r_identity', V-C-y*((ty-2)*g+ky), y*(e+g))
    check('k_increment', ky-k, 4*y*e+6*y*y*a*e+3*y*y*e*e)
    fr=g*g-T*e*(e+g)-k*(g+2*e)-3*a*X*X
    cubic=X*X+Y*Y+C*C+x*(X*Y+X*C+Y*C)-3*y*X*Y*C
    check('Fricke_original_residual', cubic, y*y*fr)

    # Coefficientwise cone certificate for the long operation:
    # g-(a+e) = 2xe+3y^2ae + [k-a]+r, with k-a >= 1.
    G=T*e+k+r
    cone=2*x*e+3*y*y*a*e+1+(4*x+3)*a+3*y*y*a*a+r
    check('long_gap_bound_certificate', G-a-e, cone)
    assert cone.nonnegative()
    results['long_gap_bound_certificate_nonnegative']='PASS'
    check('short_upper_r_transport', a+(e+G)-G, a+e)
    check('long_upper_r_transport', (a+e)+G-(e+G), a)

    def normalized(A,E,R):
        XX=1+y*A
        TT=2*x+1+3*y*y*A
        KK=XX*(3*XX-2)
        GG=TT*E+KK+R
        FF=R*GG-TT*E*E-2*KK*E-3*A*XX*XX
        return GG,FF

    GG,FF=normalized(a,e,r)
    check('Fricke_remainder_form', GG, G)
    check('Fricke_short_invariance', normalized(a,e+G,G)[1], FF)
    check('Fricke_long_invariance', normalized(a+e,G,e+G)[1], FF)
    check('Fricke_root_vanishing', normalized(P(0),P(1),P(1))[1], 0)
    check('square_dominance_off_surface',
          e*e-(2*x+1)*a*(a+e)-e-2*a-(a+e-r)*(G+a+e), FF)
    check('Cassini_off_surface', G*G-r*(t*G-r)-X*X*(1+3*a), -T*FF)
    check('ray_h_positive_identity', G-(t-1)*r, T*(a+e-r)+1+(2*x+3)*a)
    # Previous replaced endpoint, directly from the scalar mutation identity.
    Cprev=Y+y*G
    replaced=t*Y-x*X-Cprev
    check('ancestral_endpoint_remainder', replaced, 1+y*(a+e-r))

    # Generic induction steps in z,p,q: no finite-m interpolation is used.
    pp=z*q+p
    qq=(z+1)*q+p
    check('barrier_QminusP_inductive_step', qq-pp, q)
    J=lambda A,B:z*B*(B-A)-A*A
    check('barrier_quadratic_invariant_step', J(pp,qq), J(p,q))
    gg=z*e+g+r  # Here formal g independently denotes the nonnegative k.
    check('barrier_short_transport_all_m', qq*gg-pp*(e+gg), q*r-p*e+q*g)
    check('barrier_long_transport_all_m', qq*(e+g)-pp*g, qq*e+q*g)
    check('barrier_quadratic_invariant_base', J(P(0),P(1)), z)
    assert pp.nonnegative() and qq.nonnegative()
    results['barrier_positive_recurrence']='PASS'

    # Sharp scalar proof reduces exactly to c^2+c-1=0. q denotes c.
    check('golden_lower_margin', (1-q)*(1+q)-q, -(q*q+q-1))
    check('golden_upper_margin', q*(1+q)-1, q*q+q-1)

    # Positive two-coordinate ray transfer, and its narrow folded obstruction.
    ray_g=(z-1)*r+g  # Here z is formal t and g independently denotes h.
    ray_s=z*ray_g-r
    check('ray_r_update', ray_g, (z-1)*r+g)
    check('ray_h_update', ray_s-(z-1)*ray_g, (z-2)*r+g)
    mat=[[z-1,P(1)],[z-2,P(1)]]
    mat2=[[sum((mat[i][j]*mat[j][k] for j in range(2)),P(0)) for k in range(2)] for i in range(2)]
    expected=[[z*z-z-1,z],[z*(z-2),z-1]]
    for i in range(2):
        for j in range(2):
            check(f'ray_two_step_entry_{i}{j}',mat2[i][j],expected[i][j])

    def transform(coeffs):
        return [sum(coeffs[j]*comb(j,(j-n)//2) for j in range(n,len(coeffs),2)) for n in range(len(coeffs))]

    for name, coeffs, expected_row, defect in [
        ('root_lower_right',[2,2],[2,2],-4),
        ('root_extreme_pair',[5,12,4],[13,12,4],-67),
    ]:
        row=transform(coeffs)
        assert row==expected_row
        results[name+'_Fourier_row']='PASS'
        h0,h1=row[:2]
        h2=row[2] if len(row)>2 else 0
        assert h0*h0-2*h1*h1+h0*h2==defect
        results[name+'_central_defect']='PASS'

    here=Path(__file__).resolve().parent
    targets=[Path(__file__).resolve(),here/'network_quotient_constraints.md',here/'network_quotient_constraints.py']
    for name in ['invariants_normalized_state.md','invariants_normalized_verify.py']:
        if (here/name).exists(): targets.append(here/name)
    payload={'status':'PASS','scope':'All-symbol identities and induction certificates; not a proof of Local TP2.',
             'independent_implementation':'Sparse multivariate polynomials over integers; no imported research modules.',
             'checks':results,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in targets}}
    (here/'audit_normalized_results.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))

if __name__=='__main__':
    main()
