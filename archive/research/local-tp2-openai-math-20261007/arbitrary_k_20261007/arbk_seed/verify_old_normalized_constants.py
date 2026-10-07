#!/usr/bin/env python3
"""Exact interval certificates for old trace/single normalized defects.

The rows use the inner Laurent recurrence and carry-free convolution.
The parameter r=2-4u, 0<=u<=1, is treated by complete degree-two
Bernstein certificates, not a sample grid.  Three evaluations reconstruct
each degree-two polynomial exactly.  Standard Python only.
"""
import argparse
import json
import sys
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from laurent_arithmetic import get, add, scale, times_y, delta, multiply

sys.set_int_max_str_digits(0)


def bernstein_twice(values):
    a,b,c=values
    out=[2*a,4*b-a-c,2*c]
    # Invert the Bernstein conversion to ordinary power coefficients.
    power=[a,4*b-3*a-c,2*(a+c-2*b)]
    assert out[0]==2*power[0]
    assert out[1]-out[0]==power[1]
    assert out[0]-2*out[1]+out[2]==2*power[2]
    return out


def interval_normalized(rows):
    assert len(rows)==3 and len({len(h) for h in rows})==1
    assert all(v>0 for h in rows for v in h)
    assert all(rows[0][n]+rows[2][n]==2*rows[1][n]
               for n in range(len(rows[0])))
    best_num,best_den,best_at=1,1,None
    checksum=sha256(); count=0
    for n in range(len(rows[0])):
        ds=bernstein_twice([delta(h,n) for h in rows])
        hs=bernstein_twice([h[n]**2 for h in rows])
        assert min(ds)>0 and min(hs)>0,(n,ds,hs)
        for b,(d,h) in enumerate(zip(ds,hs)):
            if d*best_den<best_num*h:
                best_num,best_den,best_at=d,h,[n,b]
            checksum.update((str(d)+'/'+str(h)+'\n').encode())
            count+=1
    bound=Q(best_num,best_den)
    exponent=max(0,best_den.bit_length()-best_num.bit_length())
    while (best_num<<exponent)<best_den:exponent+=1
    assert Q(1,2**exponent)<=bound
    return {'degree':len(rows[0])-1,'coefficient_pairs':count,
            'normalized_lower_bound':str(bound),'attained_bernstein_index':best_at,
            'dyadic_lower_bound':str(Q(1,2**exponent)),
            'ordered_coefficient_pair_sha256':checksum.hexdigest()}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--max-m',type=int,default=69)
    args=parser.parse_args();limit=args.max_m
    u=[[1],[3,2]]
    for m in range(1,limit+1):
        h=[3*get(u[-1],n)+2*get(u[-1],n-1)+2*get(u[-1],n+1)-get(u[-2],n)
           for n in range(m+2)]
        assert min(h)>0;u.append(h)
    pref=[];acc=[0]
    for h in u:acc=add(acc,h);pref.append(acc)
    records=[]
    for m in range(limit+1):
        Y=times_y(pref[m]);Y[0]+=1
        t=scale(times_y(Y),3);t[1]-=1
        a=pref[m+1];b=pref[m-1] if m else [0]
        raw=[];single=[]
        for r in [2,0,-2]:
            f=t.copy();f[0]-=r;raw.append(f)
            single.append(add(multiply(a,f),b))
        trace=interval_normalized(raw)
        L=interval_normalized(single)
        yL=interval_normalized([times_y(h) for h in single])
        e=Q(trace['normalized_lower_bound'])
        ell=min(Q(L['normalized_lower_bound']),Q(yL['normalized_lower_bound']))
        rate=e/(2*(m+3))
        mass=t[0]+2*sum(t[1:])
        # Both central and x=2 mass versions are recorded explicitly.
        central=t[0]-2
        r2s=rate**2*central;r3s2=rate**3*central**2
        r2mass=rate**2*(mass-2);r3mass2=rate**3*(mass-2)**2
        rec={'m':m,'trace':trace,'single':L,'smoothed_single':yL,
             'e_m':str(e),'ell_m':str(ell),'one_factor_rate':str(rate),
             'trace_mass':str(mass),'minimum_shifted_central':str(central),
             'rate_squared_times_central':str(r2s),
             'rate_cubed_times_central_squared':str(r3s2),
             'rate_squared_times_mass_minus_two':str(r2mass),
             'rate_cubed_times_mass_minus_two_squared':str(r3mass2),
             'rate_cubed_times_mass_minus_two':str(rate**3*(mass-2))}
        records.append(rec)
        if m%25==0:
            brief=lambda q:float(q) if q.numerator.bit_length()-q.denominator.bit_length()<990 else 'greater than 2^990'
            print('m',m,'eta_trace',float(e),'eta_single',float(ell),
                  'r2central',brief(r2s),'r3central2',brief(r3s2),flush=True)
            save(records,limit)
    save(records,limit)


def save(records,limit):
    out={'status':'PASS for every fully listed exact real-interval certificate',
         'requested_max_m':limit,'completed_max_m':records[-1]['m'],
         'normalization':'min degree-two Bernstein coefficient ratio delta/h_n^2',
         'total_coefficient_pairs':sum(r[key]['coefficient_pairs'] for r in records
                                       for key in ['trace','single','smoothed_single']),
         'records':records}
    Path(__file__).with_name('old_normalized_constants.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
