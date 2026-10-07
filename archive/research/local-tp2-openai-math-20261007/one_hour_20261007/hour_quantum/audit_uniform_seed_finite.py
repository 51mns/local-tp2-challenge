#!/usr/bin/env python3
"""Separate exact reconstruction of both uniform-seed finite bridges.

No author implementation is imported.  The constructor uses original
canonical mutations in the ordinary x basis; multiplication is polynomial
Karatsuba.  Fourier half-rows are obtained by Horner's rule for x=q+q^-1.
This differs from the primary normalized bridge's inner Laurent recurrence
and packed symmetric convolution.  Every saved full-margin digest is checked.
"""
from pathlib import Path
from hashlib import sha256
import json


def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p


def add(p,q):
    out=[0]*max(len(p),len(q))
    for i,v in enumerate(p):out[i]+=v
    for i,v in enumerate(q):out[i]+=v
    return trim(out)


def sub(p,q):
    return add(p,[-v for v in q])


def times(p,c):
    return trim([c*v for v in p])


def multiply(p,q):
    if min(len(p),len(q))<=24:
        out=[0]*(len(p)+len(q)-1)
        for i,a in enumerate(p):
            for j,b in enumerate(q):out[i+j]+=a*b
        return trim(out)
    n=max(len(p),len(q))//2
    p0,p1=p[:n],p[n:] or [0]
    q0,q1=q[:n],q[n:] or [0]
    low=multiply(p0,q0)
    high=multiply(p1,q1)
    middle=sub(sub(multiply(add(p0,p1),add(q0,q1)),low),high)
    return add(add(low,[0]*n+middle),[0]*(2*n)+high)


def mutation(A,C,B):
    triple=times(multiply(multiply([1,1],A),C),3)
    return sub(sub(triple,[0]+add(A,C)),B)


def divide_y(p):
    q=[p[0]]
    for c in p[1:-1]:q.append(c-q[-1])
    assert p[-1]==q[-1]
    return trim(q)


def fourier_horner(p):
    # Each step is multiplication by q+q^-1 and addition of one constant.
    h=[p[-1]]
    for coefficient in reversed(p[:-1]):
        out=[0]*(len(h)+1)
        out[0]=(2*h[1] if len(h)>1 else 0)+coefficient
        for n in range(1,len(out)):
            out[n]=h[n-1]+(h[n+1] if n+1<len(h) else 0)
        h=out
    return h


def delta(h,n):
    at=lambda j:h[abs(j)] if abs(j)<len(h) else 0
    return at(n)**2-at(n-1)*at(n+1)-at(n+1)**2+at(n)*at(n+2)


def digest(values):
    out=sha256()
    for v in values:out.update((str(v)+'\n').encode())
    return out.hexdigest()


def main():
    here=Path(__file__).parent
    normalized=json.loads((here/'uniform_ax_normalized_certificates.json').read_text())
    strength=json.loads((here/'uniform_seed_strength_certificates.json').read_text())
    assert normalized['finite_range']==[0,390]
    assert strength['finite_range']==[0,28]
    Y,C=[2,1],[5,6,2]
    norm_count=seed_count=0
    summary_records=[]
    for m in range(391):
        # This is the original right mutation at the original L^m state.
        X=mutation(Y,C,[1])
        aX=divide_y(sub(X,[1]))
        y_aX=multiply([1,1],aX)
        num=59**(2*m+1)
        den=400000000**2*100**(2*m+1)*16*(m+3)
        record=normalized['finite_records'][m]
        assert record['m']==m
        assert (record['normalized_target_numerator'],record['normalized_target_denominator'])==(str(num),str(den))
        for name,p in [('aX',aX),('yaX',y_aX)]:
            h=fourier_horner(p)
            assert min(h)>0
            margins=[den*delta(h,n)-num*h[n]**2 for n in range(len(h))]
            assert min(margins)>0
            saved=record['rows'][name]
            assert len(h)-1==saved['degree']
            assert len(h)==saved['supported_margin_count']
            assert str(min(margins))==saved['minimum_integer_margin']
            assert margins.index(min(margins))==saved['minimum_margin_index']
            assert digest(h)==saved['halfrow_sha256'],(m,name,'halfrow')
            assert digest(margins)==saved['margin_sha256'],(m,name,'margins')
            norm_count+=len(margins)
        if m<=28:
            center2=mutation(Y,X,C)
            A=divide_y(sub(center2,Y))
            B=divide_y(sub(C,Y))
            srecord=strength['finite_records'][m]
            assert srecord['m']==m and srecord['A_ordinary']==A and srecord['B_ordinary']==B
            assert srecord['X_ordinary']==X and srecord['aX_ordinary']==aX
            for name,p in [('A',A),('yA',multiply([1,1],A))]:
                h=fourier_horner(p)
                margins=[32*delta(h,n)-9*8**m*h[n] for n in range(len(h))]
                assert min(margins)>0
                saved=srecord['rows'][name]
                assert saved['halfrow']==h
                assert saved['integer_scaled_margins_32delta_minus_9times8powm_h']==margins
                nnum=59**(3*m+1)
                nden=400000000**3*100**(3*m+1)*128*(m+3)**2
                norm=[nden*delta(h,n)-nnum*h[n]**2 for n in range(len(h))]
                assert min(norm)>0 and saved['normalized_integer_margins']==norm
                seed_count+=len(h)
        summary_records.append({'m':m,'normalized_row_and_margin_digests_match':True})
        # Move to the next actual L-state by the original left mutation.
        Y,C=C,mutation([1],C,Y)
        assert all(v>0 for v in Y+C)
        if m%50==0:print('Independent ordinary/Horner replay m =',m,flush=True)
    assert norm_count==308499 and seed_count==2813
    assert 9*8**29>384*7**29
    output={'verdict':'PASS: separate exact finite reconstruction matches every saved coefficient/margin digest',
            'author_code_imported':False,
            'construction':'Original canonical mutations in ordinary x, polynomial Karatsuba, Fourier Horner rule',
            'normalized_aX_range':[0,390],
            'normalized_aX_margin_count':norm_count,
            'seed_strength_and_normalized_range':[0,28],
            'seed_strength_margin_count':seed_count,
            'seed_normalized_margin_count':seed_count,
            'tail_scalar_gate_checked':True,
            'all_cases':summary_records}
    target=here/'audit_uniform_seed_finite_results.json'
    target.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='all_cases'},indent=2))


if __name__=='__main__':
    main()
