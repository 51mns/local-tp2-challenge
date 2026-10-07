"""Exact targeted replay for audit_dependency.md; no state or parameter scan."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
NV = 8
ZERO = (0,) * NV


class Poly(dict):
    def __add__(self, other):
        other = aspoly(other)
        out = dict(self)
        for k, v in other.items():
            out[k] = out.get(k, F(0)) + v
        return Poly({k:v for k,v in out.items() if v})
    __radd__ = __add__

    def __neg__(self):
        return Poly({k:-v for k,v in self.items()})

    def __sub__(self, other):
        return self + -aspoly(other)

    def __rsub__(self, other):
        return aspoly(other) + -self

    def __mul__(self, other):
        other = aspoly(other)
        out = {}
        for ka, va in self.items():
            for kb, vb in other.items():
                k = tuple(i+j for i,j in zip(ka,kb))
                out[k] = out.get(k,F(0)) + va*vb
        return Poly({k:v for k,v in out.items() if v})
    __rmul__ = __mul__

    def __pow__(self, n):
        assert n >= 0
        out = aspoly(1)
        for _ in range(n):
            out *= self
        return out

    def __truediv__(self, n):
        return self * (F(1)/F(n))


def aspoly(v):
    if isinstance(v, Poly):
        return v
    return Poly({ZERO:F(v)}) if v else Poly()


def var(i):
    key = list(ZERO)
    key[i] = 1
    return Poly({tuple(key):F(1)})


x,a,e,r = [var(i) for i in range(4)]
y=x+1


def state(av, ev, rv):
    X = 1 + y * av
    t = 3 * y * X - x
    k = X * (3 * X - 2)
    g = (t - 2) * ev + k + rv
    s = t * g - rv
    Y = X + y * ev
    C = Y + y * g
    T = 3 * y * C - x
    d = ev * (T + 1)
    c = ev + g + s
    return dict(X=X, Y=Y, C=C, T=T, t=t, g=g, s=s, d=d, c=c)


def halfrow(poly):
    assert all(not any(key[1:]) for key in poly)
    degree = max(key[0] for key in poly)
    out = [F(0)] * (degree+1)
    for key,value in poly.items():
        power=key[0]
        for j in range(power + 1):
            exponent = power - 2 * j
            if exponent >= 0:
                out[exponent] += value * math.comb(power, j)
    return out


def defects(h):
    def at(i):
        i = abs(i)
        return h[i] if i < len(h) else F(0)
    return [at(n)**2-at(n-1)*at(n+1)-at(n+1)**2+at(n)*at(n+2)
            for n in range(len(h))]


def tensor(poly):
    h=halfrow(poly)
    at=lambda i: h[abs(i)] if abs(i)<len(h) else F(0)
    xh=[2*at(1)]+[at(j-1)+at(j+1) for j in range(1,len(h)+1)]
    out={}
    for k in range(len(h)):
        for l in range(k+1,len(h)+1):
            value=at(k)*xh[l]-at(l)*xh[k]
            if value:
                key=(k+l-1,l-k-1)
                out[key]=value
                out[key[::-1]]=value
    return out


def charsum(*pairs):
    out={}
    for scale,arr in pairs:
        for k,v in arr.items():
            out[k]=out.get(k,F(0))+scale*v
    return {k:v for k,v in out.items() if v}


def mixed(f,g):
    return charsum((1,tensor(f+g)),(-1,tensor(f)),(-1,tensor(g)))


def main():
    z = state(a, e, r)
    center_B=a+e+z['g']
    assert z['c']+e-(1+(2*x+3)*center_B) == (z['T']-2)*a
    long_F=y*z['g']-(x+2)*z['Y']
    positive_F=(x*x-1)*e+x+y*(r-1)+y*a*(2+3*x)+3*y**3*a*(a+e)
    assert long_F == positive_F
    child_checks = []
    beta = 3*y*y
    for sigma in (0, 1):
        n = z['g'] + (1-sigma)*e
        v = z['s'] + sigma*z['d']
        u = z['T'] - beta*n
        h = (1-2*sigma)*e
        cp = (u+1)*v+h
        actual = state(a if sigma == 0 else a+e,
                       e+z['g'] if sigma == 0 else z['g'],
                       z['g'] if sigma == 0 else e+z['g'])
        assert not actual['T']-z['T']-beta*v
        assert not actual['c']-cp
        assert not actual['g']-v
        child_checks.append({'sigma': sigma, 'actual_mutation_tuple': True})

    root = state(aspoly(0), aspoly(1), aspoly(1))
    wh = halfrow(y*root['C'])
    th = halfrow(root['T']-2)
    assert wh == [21, 17, 8, 2]
    assert th == [61, 50, 24, 6]
    assert defects(th)[0] == 185
    assert halfrow(y*y) == [3, 2, 1]
    assert defects([3, 2, 1]) == [4, 0, 1]

    A0,A1,A2,B0,B1,B2 = [var(i) for i in range(6)]
    D = lambda h0,h1,h2: h0*(h0+h2)-2*h1*h1
    cross = 2*A0*B0+A0*B2+A2*B0-4*A1*B1
    assert not D(A0+B0,A1+B1,A2+B2)-D(A0,A1,A2)-D(B0,B1,B2)-cross

    h0,h1,h2,rr,ss = [var(i) for i in range(5)]
    alpha=(rr+ss)/2
    omega=(rr-ss)**2/4
    central=D(h0-alpha,h1,h2)-omega
    expected=D(h0,h1,h2)-(rr+ss)*(h0+h2/2)+rr*ss
    assert not central-expected
    assert not D(h0-rr,h1,h2)-(D(h0,h1,h2)-rr*(2*h0+h2)+rr**2)
    h3=var(5)
    defect1=lambda a0,a1,a2,a3: a1*a1-a0*a2-a2*a2+a1*a3
    assert not defect1(h0-rr,h1,h2,h3)-defect1(h0,h1,h2,h3)-rr*h2
    linear=438*A0-600*A1+183*A2
    assert 61*A0*linear == 6*(61*A1-50*A0)**2+555*A0**2+11163*D(A0,A1,A2)

    root_Q=(root['t']-2)*root['C']-x*root['X']
    qh=halfrow(root_Q)
    dh=halfrow(y*root['d'])
    root_Q_D=[qh[n]*dh[n+1]-(qh[n+1] if n+1<len(qh) else F(0))*dh[n]
              for n in range(len(qh))]
    assert root_Q_D == [126,228,100,24]

    # The optional anchored margin has an exact minimum at t=50/61.
    t = var(0)
    upper_branch=366*t*t-600*t+255
    minimum=F(255)-F(600*600,4*366)
    assert minimum == F(555,61)
    assert not upper_branch-(366*(t-F(50,61))**2+F(555,61))

    # Independent formal proof of the factored mixed gate before Phi.
    Bx,Bz,Nx,Nz,Zx,Zz,theta,phi=[var(i) for i in range(8)]
    eta=(theta+phi)/2
    kappa=theta*phi
    omega=(theta-phi)**2/4
    Hx=Bx*(Zx-eta)-Nx*(eta*Zx-kappa)
    Hz=Bz*(Zz-eta)-Nz*(eta*Zz-kappa)
    base=(Zx*Zz-eta*(Zx+Zz)+kappa)*(Bx*Bz+kappa*Nx*Nz-eta*(Bx*Nz+Nx*Bz))
    flux=(Zz-Zx)*(Bx*Nz-Nx*Bz)
    assert Hx*Hz-omega*(Bx-Nx*Zx)*(Bz-Nz*Zz) == base+omega*flux
    aa,bb,cc,theta=[var(i) for i in range(4)]
    E=lambda th: aa-th*bb+th*th*cc
    coordinate=(theta+1)/4
    assert E(theta) == E(-1)*(1-coordinate)**2+2*(aa-bb-3*cc)*coordinate*(1-coordinate)+E(3)*coordinate**2

    beta_tensor=tensor(3*y*y)
    expected_beta={(0,0):36,(1,1):18,(2,2):27,(3,1):18,(1,3):18,(4,0):9,(0,4):9}
    assert beta_tensor == expected_beta
    flux_witnesses=[]
    for sigma in (0,1):
        child=state(aspoly(sigma),root['g']+1-sigma,root['g']+sigma)
        zz=child['T']+1
        for orientation in ('reverse','forward'):
            eprime=root['g']+1-sigma
            b0,b1=(eprime,child['c']) if orientation=='reverse' else (child['c'],eprime)
            for mode in ('raw','y'):
                p0,p1=(b0,b1) if mode=='raw' else (y*b0,y*b1)
                anchor=p0*zz+p1
                flux=charsum((1,mixed(anchor,p0*zz)),(-1,mixed(anchor*zz,p0)))
                leading=halfrow(anchor*zz)[-1]
                idx=len(halfrow(anchor*zz))-1
                actual=flux[(idx,idx)]
                expected=-halfrow(p0)[0]*leading
                assert actual == expected and actual<0
                flux_witnesses.append({'sigma':sigma,'orientation':orientation,'mode':mode,
                                       'character':[idx,idx],'coefficient':str(actual)})

    # Complete exact raw/y certificates of ONE relaxed spectral witness.
    hv=list(map(F,['4659/1000','4537/1000','4181/1000','3610/1000',
                   '2859/1000','1971/1000','1']))
    cosine=[aspoly(1),x]
    for i in range(2,len(hv)):
        cosine.append(x*cosine[-1]-(2 if i==2 else cosine[-2]))
    relaxed=sum((hv[i]*cosine[i] for i in range(len(hv))),aspoly(0))
    assert halfrow(relaxed)==hv
    relaxed_certificates=[]
    for mode,poly in [('raw',relaxed),('y',y*relaxed),('beta',3*y*y*relaxed)]:
        h=halfrow(poly)
        ds=defects(h)
        ts=tensor(poly)
        assert all(v>0 for v in h+ds) and all(v>=0 for v in ts.values())
        relaxed_certificates.append({'mode':mode,'degree':len(h)-1,
                                     'character_terms':len(ts),'minimum_defect':str(min(ds))})
    relaxed_negative=defects(halfrow((x+4)**2+3*y*y*relaxed))[3]
    assert relaxed_negative==F(-29300421,500000)

    # Exact frozen-source normalization, both endpoint regimes.
    frozen_sources=[]
    for label,X in [('one',aspoly(1)),('P',x+2)]:
        J=y*(3*y*X-x-2)
        L=3*y*y*X*(x+2)
        jh,lh=halfrow(J),halfrow(L)
        ws=[jh[n]*lh[n+1]-(jh[n+1] if n+1<len(jh) else F(0))*lh[n]
            for n in range(len(jh))]
        assert ws==([30,-12,6] if label=='one' else [72,81,45,9])
        frozen_sources.append({'endpoint':label,'adjacent_minors':list(map(int,ws))})

    result = {'status':'PASS targeted exact replay; analytical scope PARTIAL',
              'state_checks':child_checks,
              'root_yC_halfrow':list(map(int,wh)),
              'root_trace_minus_2_halfrow':list(map(int,th)),
              'root_trace_central_defect':185,
              'y_squared_halfrow':[3,2,1], 'y_squared_defects':[4,0,1],
              'central_polarization_identity':True,
              'trace_square_central_identity':True,
              'trace_line_central_identity':True,
              'trace_delta1_shift_identity':True,
              'root_central_strength_SOS_identity':True,
              'root_weaker_comparison_Q_D':list(map(int,root_Q_D)),
              'optional_anchored_margin':'555/61',
              'packet_algebra_factor_formal_identity':True,
              'packet_algebra_copositivity_Bernstein_identity':True,
              'spectral_beta_tensor_exact':True,
              'packet_algebra_flux_fixed_normalizations':flux_witnesses,
              'canonical_anchor_off_Fricke_identity':True,
              'canonical_Fourier_surplus_identity':True,
              'spectral_relaxed_complete_certificates':relaxed_certificates,
              'spectral_relaxed_border_failure':str(relaxed_negative),
              'proxy_frozen_source_normalizations':frozen_sources,
              'continuum_and_all_index_proofs':'analytical note, not finite checks',
              'remaining':['child Tprime+2 trace defects inside the fixed origin anchor band',
                           'reverse raw/y low-prefix copositivity and forward all-r strict singles',
                           'sharp mixed interior character layers raw/y both orientations over full square',
                           'regular-child Qprime<Dprime, or original proxy as optional stronger route'],
              'remaining_closure_types':2,
              'ROOT':'PASS inherited continuous full packet and stronger proxy bases',
              'BOTH':'PARTIAL; algebra/LR/origins and audited subgates PASS, two closure types OPEN',
              'TARGET':'PASS conditional on complete P_D, proved directly; full-tree closure OPEN'}
    note=HERE/'audit_dependency.md'
    result['note_sha256']=hashlib.sha256(note.read_bytes()).hexdigest()
    result['gate_reduction_note_sha256']=hashlib.sha256((HERE/'audit_gate_reduction.md').read_bytes()).hexdigest()
    result['review_note_sha256']=hashlib.sha256((HERE/'audit_review.md').read_bytes()).hexdigest()
    audited_sources=json.loads((HERE/'audit_source_hashes.json').read_text())
    for name,expected_hash in audited_sources.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected_hash, name
    result['frozen_primary_source_files_verified']=len(audited_sources)
    output=HERE/'audit_dependency_results.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
