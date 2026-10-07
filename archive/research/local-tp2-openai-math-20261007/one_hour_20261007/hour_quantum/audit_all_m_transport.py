#!/usr/bin/env python3
"""Independent exact certificate audit of the all-m trace/mixed transport.

No code from hour_transport is imported.  Canonical mutations use ordinary
x polynomials with Karatsuba multiplication and Fourier Horner iteration.
Parameter blocks are assembled by generic polynomial-ring multiplication.
Degree-two Bernstein coefficients are reconstructed from exact values at
0,1/2,1 on each active axis, rather than the author's power-basis formula.
The degree bound is checked, so this is exact polynomial reconstruction,
not a finite-grid positivity test.
"""
from fractions import Fraction as Q
from itertools import product
from hashlib import sha256
from pathlib import Path
import json
import audit_uniform_seed_finite as xpoly


ZERO=(0,0,0)


def radd(*ps):
    out={}
    for p in ps:
        for e,v in p.items():out[e]=out.get(e,0)+v
    return {e:v for e,v in out.items() if v}


def rscale(p,c):
    return {e:c*v for e,v in p.items() if c*v}


def rmul(p,q):
    out={}
    for e,v in p.items():
        for f,w in q.items():
            k=tuple(a+b for a,b in zip(e,f))
            out[k]=out.get(k,0)+v*w
    return {e:v for e,v in out.items() if v}


def lift(p):return {ZERO:p}


def padd(*ps):
    out={}
    for p in ps:
        for e,v in p.items():out[e]=xpoly.add(out.get(e,[0]),v)
    return {e:v for e,v in out.items() if v!=[0]}


def pmul(p,q):
    out={}
    for e,v in p.items():
        for f,w in q.items():
            k=tuple(a+b for a,b in zip(e,f))
            out[k]=xpoly.add(out.get(k,[0]),xpoly.multiply(v,w))
    return {e:v for e,v in out.items() if v!=[0]}


def fourier(p):
    components={e:xpoly.fourier_horner(v) for e,v in p.items()}
    degree=max(len(h) for h in components.values())-1
    return [{e:h[n] for e,h in components.items() if n<len(h) and h[n]}
            for n in range(degree+1)]


def at(h,n):return h[abs(n)] if abs(n)<len(h) else {}


def defect(h,n):
    return radd(rmul(at(h,n),at(h,n)),rscale(rmul(at(h,n-1),at(h,n+1)),-1),
                rscale(rmul(at(h,n+1),at(h,n+1)),-1),rmul(at(h,n),at(h,n+2)))


def interpolation_bernstein(p,dimensions):
    """2^d times degree-two tensor Bernstein coefficients, from grid values."""
    axes=tuple(range(dimensions))
    assert all(all(e[j]<=2 for j in axes) and all(e[j]==0 for j in range(dimensions,3)) for e in p)
    grid=list(product(range(3),repeat=dimensions))
    # grid coordinate t means t/2. Clearing 4^d makes every value integral.
    values={}
    for point in grid:
        value=0
        for e,c in p.items():
            term=c
            for axis,t in zip(axes,point):term*=2**(2-e[axis])*t**e[axis]
            value+=term
        values[point]=value
    # At each axis: (2b0,2b1,2b2)=(2f0,4fmid-f0-f1,2f1).
    for axis in axes:
        transformed={}
        for point in grid:
            points=[]
            for j in range(3):
                index=list(point);index[axis]=j
                points.append(values[tuple(index)])
            transformed[point]=(2*points[0],4*points[1]-points[0]-points[2],2*points[2])[point[axis]]
        values=transformed
    denominator=4**dimensions
    assert all(v%denominator==0 for v in values.values())
    return [values[point]//denominator for point in grid]


def trace(p):return xpoly.sub(xpoly.times(xpoly.multiply([1,1],p),3),[0,1])


def param_trace(p,axis):
    e=[0,0,0];e[axis]=1
    return {ZERO:xpoly.add(p,[2]),tuple(e):[-4]}


def kappa(m):return 18 if m==0 else 18*4**m-18*2**m-11


def main():
    here=Path(__file__).resolve().parent
    transport=here.parent/'hour_transport'
    saved_trace=json.loads((transport/'trace_transport_results.json').read_text())
    saved_mixed=json.loads((transport/'uniform_mixed_transport_results.json').read_text())
    # Original L^m states: left endpoint 1, center C, right endpoint Y.
    Y,C=[2,1],[5,6,2]
    checked=normalized_checked=small_checked=0
    records=[]
    c0,sigma=Q(1,400000000),Q(59,100)
    for m in range(54):
        X=xpoly.mutation(Y,C,[1])
        center2=xpoly.mutation(Y,X,C)
        A=xpoly.divide_y(xpoly.sub(center2,Y))
        B=xpoly.divide_y(xpoly.sub(C,Y))
        tau=trace(X)
        assert tau==xpoly.sub(xpoly.multiply(trace(Y),trace(C)),[3,4,1])
        assert len(A)-1==3*m+5 and len(tau)-1==2*m+5
        roots=[param_trace(tau,j) for j in range(3)]
        L=padd(pmul(lift(A),roots[0]),lift(B))
        H=padd(pmul(lift(A),pmul(roots[0],roots[1])),pmul(lift(B),roots[2]))
        blocks={'L':L,'H':H,'yL':pmul(lift([1,1]),L),'yH':pmul(lift([1,1]),H)}
        b0=xpoly.fourier_horner(B)[0]
        yb0=xpoly.fourier_horner(xpoly.multiply([1,1],B))[0]
        source=saved_mixed['records'][m]
        assert source['m']==m and source['B_halfrow_central']==b0 and source['yB_halfrow_central']==yb0
        case_record={}
        for label,block in blocks.items():
            dimensions=3 if label.endswith('H') else 1
            lam_num=max(9*8**m*kappa(m)**2,128*8*yb0) if dimensions==3 else 9*8**m*kappa(m)
            target=(c0**7*sigma**(7*m+3)/(4194304*(m+3)**6) if dimensions==3 else
                    c0**5*sigma**(5*m+2)/(65536*(m+3)**4))
            row=fourier(block)
            expected=source['cases'][label]
            assert expected['degree']==len(row)-1
            assert Q(expected['strength'])==Q(lam_num,128)
            assert Q(expected['uniform_normalized_defect_lower_bound'])==target
            checksum=sha256()
            minima=[]
            for n in range(len(row)):
                margin=radd(rscale(defect(row,n),128),rscale(row[n],-lam_num))
                coefficients=interpolation_bernstein(margin,dimensions)
                assert min(coefficients)>0,(m,label,n)
                minima.append(min(coefficients))
                for value in coefficients:checksum.update((str(value)+'\n').encode())
                hmax=row[n][ZERO]
                assert min(coefficients)*target.denominator>=target.numerator*128*2**dimensions*hmax**2
                checked+=len(coefficients)
                normalized_checked+=1
            assert minima==expected['minima_by_supported_index'],(m,label,'minima')
            assert checksum.hexdigest()==expected['sha256_ordered_scaled_coefficients'],(m,label,'digest')
            case_record[label]={'degree':len(row)-1,'all_scaled_coefficient_digests_match':True}
        records.append({'m':m,'cases':case_record})

        if m in (0,1):
            for source_small in saved_trace['small_m_certificates']:
                if source_small['m']!=m:continue
                smooth=source_small['smoothed']
                block=pmul(lift([1,1]),roots[0]) if smooth else roots[0]
                row=fourier(block)
                strength=source_small['strength']
                assert source_small['trace_x_coefficients']==tau
                all_actual=[]
                for n in range(len(row)):
                    coefficients=interpolation_bernstein(radd(defect(row,n),rscale(row[n],-strength)),1)
                    actual=[Q(v,2) for v in coefficients]
                    assert min(actual)>=0
                    assert actual==list(map(Q,source_small['degree_two_bernstein_margins'][n]))
                    all_actual.append(actual)
                    small_checked+=3
                assert all(v==0 for v in all_actual[-1])
        Y,C=C,xpoly.mutation([1],C,Y)
        if m%10==0 or m==53:print('Independent parameter reconstruction m =',m,flush=True)

    assert checked==635688 and normalized_checked==37368 and small_checked==66
    EH=lambda m:c0**7*sigma**(7*m+3)/(524288*(m+3)**6)
    epsilon=lambda m:Q(20*(2*m+5)**3*(2*m+7),27**4*6**(4*m+1))
    ratio=lambda m:6**4*sigma**7*Q((m+3)**6*(2*m+5)**3*(2*m+7),(m+4)**6*(2*m+7)**3*(2*m+9))
    assert EH(54)>12*epsilon(54) and EH(53)<12*epsilon(53)
    assert epsilon(54)<1 and ratio(54)>27
    assert EH(54)/(12*epsilon(54))==Q(saved_mixed['tail_gate_EH_over_12epsilon'])
    assert ratio(54)==Q(saved_mixed['tail_gate_consecutive_ratio_at_start'])
    for m in range(21):
        lhs=Q(kappa(m),25*7**(2*m+3))
        rhs=c0**2*sigma**(2*m+1)/(16*(m+3))
        assert lhs>rhs
        assert lhs//rhs==saved_mixed['trace_normalized_finite_scalar_certificates'][m]['strict_ratio_floor']
    assert kappa(2)>=9*4**2 and Q(729,128)*128**2>24*7**3
    result={
        'verdict':'PASS: separate exact full coefficient reconstruction and scalar tail gates',
        'author_code_imported':False,
        'method':'Original mutations / ordinary x Karatsuba / Fourier Horner / generic parameter ring / exact degree-two interpolation to Bernstein',
        'raw_smoothed_trace_bernstein_coefficients':small_checked,
        'all_m_mixed_finite_range':[0,53],
        'all_m_mixed_bernstein_coefficients':checked,
        'normalized_finite_comparisons':normalized_checked,
        'normalized_trace_scalar_comparisons':21,
        'tail_start':54,'tail_and_reference_strength_gates_match':True,
        'records':records,
    }
    (here/'audit_all_m_transport_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':
    main()
