#!/usr/bin/env python3
"""Eight-factor normalized trace blocks and distinguished single residues.

Uses permutation symmetry to represent every tensor Bernstein coefficient
by the histogram of its degree-two indices.  All arithmetic is exact.
"""
from fractions import Fraction as Q
from math import comb, factorial
from hashlib import sha256
from pathlib import Path
import json


def trim(h):
    h=list(h)
    while len(h)>1 and h[-1]==0:h.pop()
    return h
def plus(*rows):
    out=[0]*max(map(len,rows))
    for h in rows:
        for i,v in enumerate(h):out[i]+=v
    return trim(out)
def scale(h,c):return trim([c*v for v in h])
def minus(a,b):return plus(a,scale(b,-1))
def conv(a,b):
    c=[0]*(len(a)+len(b)-1);c[0]=a[0]*b[0]
    for i in range(1,len(a)):c[i]+=a[i]*b[0]
    for j in range(1,len(b)):c[j]+=a[0]*b[j]
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            v=a[i]*b[j];c[i+j]+=v;c[abs(i-j)]+=v*(2 if i==j else 1)
    return trim(c)
def at(h,n):
    n=abs(n)
    return h[n] if n<len(h) else 0


def old_data(m):
    u0,u1=[1],[3,2]
    u=[u0,u1]
    for _ in range(1,m+1):u.append(minus(conv([3,2],u[-1]),u[-2]))
    prefix=[];running=[0]
    for h in u:running=plus(running,h);prefix.append(running)
    T=lambda j:prefix[j] if j>=0 else [0]
    t=plus(scale(conv([3,2,1],T(m)),3),[3,2])
    A,B=T(m+1),T(m-1)
    return t,A,B


def powers(h,n):
    out=[[1]]
    for _ in range(n):out.append(conv(out[-1],h))
    return out


def make_rows(t,N,distinguished=None,smooth=False):
    lo,hi=minus(t,[2]),plus(t,[2])
    plo,phi=powers(lo,N),powers(hi,N)
    common=[conv(plo[a],phi[N-a]) for a in range(N+1)]
    if distinguished is None:return [[h] for h in common]
    A,B=distinguished
    Llo,Lhi=plus(conv(A,lo),B),plus(conv(A,hi),B)
    if smooth:Llo,Lhi=conv([1,1],Llo),conv([1,1],Lhi)
    return [[conv(h,Llo),conv(h,Lhi)] for h in common]


def coefficient_list(rows,N,distinguished):
    degree=len(rows[0][0])-1
    values=[]
    for n0 in range(N+1):
        for n1 in range(N-n0+1):
            n2=N-n0-n1
            multiplicity=factorial(N)//(factorial(n0)*factorial(n1)*factorial(n2))
            for index in range(3) if distinguished else (0,):
                pair_signs=([(0,0)] if index==0 else [(0,1),(1,0)] if index==1 else [(1,1)])
                if not distinguished:pair_signs=[(0,0)]
                denominator=2**(n1+int(distinguished and index==1))
                for n in range(degree+1):
                    square=0;delta=0
                    for a in range(n1+1):
                        c=comb(n1,a)
                        for first,second in pair_signs:
                            h=rows[n0+a][first];g=rows[n0+n1-a][second]
                            v=at(h,n)*at(g,n)
                            square+=c*v
                            delta+=c*(v-at(h,n-1)*at(g,n+1)-at(h,n+1)*at(g,n+1)+at(h,n)*at(g,n+2))
                    assert square>0
                    values.append({'histogram':[n0,n1,n2],'distinguished_index':index,
                                   'n':n,'numerator_delta':delta,'numerator_square':square,
                                   'common_denominator':denominator,'multiplicity':multiplicity})
    expected=(degree+1)*3**(N+int(distinguished))
    assert sum(r['multiplicity'] for r in values)==expected
    return degree,values


def best_eta(values):return min(Q(r['numerator_delta'],r['numerator_square']) for r in values)


def certify(values,target):
    digest=sha256();minimum=None;records=[]
    for r in values:
        margin=target.denominator*r['numerator_delta']-target.numerator*r['numerator_square']
        assert margin>=0
        minimum=margin if minimum is None else min(minimum,margin)
        digest.update(str(margin).encode());digest.update(b'\n')
        records.append({k:v for k,v in r.items() if k not in ('numerator_delta','numerator_square')} |
                       {'scaled_margin':margin})
    return {'target_eta':str(target),'best_certified_eta':str(best_eta(values)),
            'histogram_coefficient_count':len(values),
            'full_tensor_coefficient_count':sum(r['multiplicity'] for r in values),
            'minimum_scaled_margin':minimum,'ordered_histogram_margin_sha256':digest.hexdigest(),
            'coefficients':records}


def main():
    records=[]
    for m in range(1,5):
        t,A,B=old_data(m);d=len(t)-1
        degree,block_values=coefficient_list(make_rows(t,8),8,False)
        assert degree==8*d
        block_eta=best_eta(block_values);D=2*(degree+1)
        rate_den=2
        while block_eta*rate_den**8<D:rate_den+=1
        residue_candidates=[]
        for N in range(8):
            for smooth in (False,True):
                rd,values=coefficient_list(make_rows(t,N,(A,B),smooth),N,True)
                residue_candidates.append((N,smooth,rd,values))
        residual_best=min(best_eta(v) for _,_,_,v in residue_candidates)
        residue_den=residual_best.denominator//residual_best.numerator+1
        residue_target=Q(1,residue_den)
        record={'m':m,'trace_degree':d,'block_degree':degree,'product_loss_denominator':D,
                'per_trace_rate':f'1/{rate_den}', 'residual_eta':str(residue_target),
                'block':certify(block_values,Q(D,rate_den**8)),
                'residues':[{'remaining_propagators':N,'smooth':smooth,'degree':rd,
                             **certify(v,residue_target)} for N,smooth,rd,v in residue_candidates]}
        records.append(record)
        print(json.dumps({'m':m,'rate':f'1/{rate_den}','residual_eta':str(residue_target),
                          'actual_block_eta':str(block_eta),
                          'actual_residual_eta':str(residual_best),
                          'block_histograms':len(block_values),
                          'residue_histograms':sum(len(v) for _,_,_,v in residue_candidates)}),flush=True)
    result={'status':'PASS','method':'Full degree-two tensor Bernstein through exact symmetry histograms',
            'scope':'m=1,...,4; eight independent shifted trace factors and 0,...,7-factor distinguished single residues',
            'records':records}
    dest=Path(__file__).with_name('finite_m_normalized_blocks_results.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
