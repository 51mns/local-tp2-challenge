#!/usr/bin/env python3
"""Exact scalar coverage of every integer m,k beyond a fixed finite bridge.

The real-parameter normalized inputs are complete Bernstein certificates
in the sibling seed/mixed directories. This script uses only Fraction and
integer arithmetic. Monotone-ratio proofs are in SCALAR_COVERAGE.md.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json,sys
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parent.parent
C0=Q(1,400000000);SIGMA=Q(59,100)
THRESHOLDS={0:21,1:11,2:6,3:5,4:4,5:5}

def pure_values(m):
    prev,u,total=0,1,1
    for j in range(1,m+1):prev,u=u,7*u-prev;total+=u
    return total

def lambda_z(m,j):
    if m==0:return Q(9)**(j//2)
    return Q(3)*Q(2)**(2*m-3)*(Q(3)*Q(2)**(m-1))**(j-1)/(2*j)

def p0_bound(m):
    # Coarse common bound for H(T_m)_0 and H(yT_m)_0.
    return Q(7**(m+1),2)

def finite_p0(m):
    get=lambda h,n:h[abs(n)] if abs(n)<len(h) else 0
    prev,u=[0],[1];T=[1]
    for j in range(1,m+1):
        nxt=[3*get(u,n)+2*get(u,n-1)+2*get(u,n+1)-get(prev,n) for n in range(j+1)]
        prev,u=u,nxt
        T=[get(T,n)+get(u,n) for n in range(j+1)]
    return T[0]+2*get(T,1)

def gates(m,k,ez,analytic=False):
    d=m+2;D=2*(d*k+2);DJ=2*(d*k+3);width=2*d*k-3
    if analytic:
        M=27*6**m
        s=Q(9,32)*M**k/width
        c=Q(9,512)*M**(2*k)/width**2
        beta=Q(M**2,4*(2*d+1)**2)
    else:
        T=pure_values(m);M=5+27*T
        alpha=Q(T*M**(k-1),width)
        s=9*alpha;c=18*alpha**2
        beta=(Q(M+2,2*d+1)-1)**2
    a=ez(k)/2;z=ez(k-1)/729
    f=a*z/D;l=f/4;g=l*z/D
    out={'single_perturbation':f*beta*s/12,
         'midpoint_subtraction':g*s*s/48,
         'proxy_absorption':l*z*c/(DJ*96),
         'multiplier_absorption':l*c/(1296*96),
         'outer_propagator_growth':z*s/(D*2),
         'correction_coefficient_domination':c/2,
         'trace_central_bound':s,
         'seed_ratio_bound':beta}
    return out

def strs(d):return {k:str(v) for k,v in d.items()}
def digest(path):return sha256(path.read_bytes()).hexdigest()

def main():
    oldpath=BASE/'arbk_seed/old_normalized_constants.json'
    blockpath=BASE/'arbk_mixed/finite_m_normalized_blocks_results.json'
    old=json.loads(oldpath.read_text());blocks=json.loads(blockpath.read_text())
    assert old['completed_max_m']==69
    old={r['m']:r for r in old['records']}
    blocks={r['m']:r for r in blocks['records']}
    recs=[]
    for m in range(70):
        if m==0:
            E,rate=Q(1,256),Q(1,3)
            ez=lambda j:E*rate**j
            source='paired-root blocks; no spectral-weight loss'
        elif m in range(1,5):
            E,rate=Q(blocks[m]['residual_eta']),Q(blocks[m]['per_trace_rate'])
            ez=lambda j:E*rate**(j-1)/(4*j)
            source='eight-trace normalized blocks and all 0..7-factor residues'
        else:
            E,rate=Q(old[m]['ell_m']),Q(old[m]['one_factor_rate'])
            ez=lambda j:E*rate**(j-1)/(4*j)
            source='one-factor normalized interval certificates'
        k=THRESHOLDS.get(m,3)
        now=gates(m,k,ez);nxt=gates(m,k+1,ez)
        assert min(now.values())>1,(m,k,now)
        ratios={key:nxt[key]/v for key,v in now.items()}
        assert all(v>1 for key,v in ratios.items() if key!='seed_ratio_bound'),(m,k,ratios)
        trace=lambda_z(m,k-1)
        seed=lambda_z(m,k)
        assert trace>=189,(m,k,'trace strength',trace)
        seed_required=Q(10) if m==0 else 8*finite_p0(m)
        assert seed>=seed_required,(m,k,'seed subtraction',seed,seed_required)
        recs.append({'m':m,'all_k_from':k,'old_normalized_source':source,
                     'old_normalized_prefactor':str(E),'old_normalized_rate':str(rate),
                     'gates':strs(now),'consecutive_k_ratios':strs(ratios),
                     'trace_input_strength':str(trace),'seed_input_strength':str(seed),
                     'seed_required_strength':str(seed_required)})
    m=70;k=3
    def analytic_e(mm):
        E=C0**2*SIGMA**(2*mm+1)/(16*(mm+3))
        r=C0*SIGMA**mm/(4*(mm+3))
        return E,r,lambda j:E*r**(j-1)/(4*j)
    E,r,ez=analytic_e(m)
    now=gates(m,k,ez,True)
    assert min(now.values())>1
    En,rn,ezn=analytic_e(m+1)
    nxt=gates(m+1,k,ezn,True)
    ratios={key:nxt[key]/v for key,v in now.items()}
    assert min(ratios.values())>1
    M=27*6**m
    rate_gate=r*r*M
    assert rate_gate>=16
    rate_m_ratio=6*SIGMA**2*Q(m+3,m+4)**2
    assert rate_m_ratio>1
    # Lower bounds for every k>=3, every d=m+2>=2.
    k_ratio_lower={'single_perturbation':rate_gate/4,
        'midpoint_subtraction':r**3*M**2/12,
        'proxy_absorption':r**3*M**2/12,
        'multiplier_absorption':r**2*M**2/6,
        'outer_propagator_growth':r*M/3,
        'correction_coefficient_domination':Q(4,9)*M**2,
        'trace_central_bound':Q(2,3)*M,
        'seed_ratio_bound':Q(1)}
    assert all(v>1 for key,v in k_ratio_lower.items() if key!='seed_ratio_bound')
    assert lambda_z(m,2)>=189
    assert lambda_z(m,3)>=8*p0_bound(m)
    # The old single-only analytic normalized gate.
    dominant=C0**2*SIGMA**(2*m+1)/(4*(m+3))
    epsilon=Q(2*m+5,9*6**m)
    assert dominant>=12*epsilon and epsilon<Q(1,3)
    old_single_ratio=6*SIGMA**2*Q(m+3,m+4)*Q(2*m+5,2*m+7)
    assert old_single_ratio>1
    finite_pairs=[[mm,kk] for mm,limit in THRESHOLDS.items() for kk in range(3,limit)]
    assert len(finite_pairs)==34
    out={'status':'PASS','scope':'All m>=0,k>=3 partitioned into 34 finite prefixes and rigorously monotone infinite tails',
         'fixed_m_records':recs,
         'analytic_m_tail':{'all_m_from':m,'all_k_from':k,'gates_at_corner':strs(now),
             'consecutive_m_ratios_at_k3':strs(ratios),
             'rate_squared_times_mass_lower_bound':str(rate_gate),
             'rate_gate_consecutive_m_ratio':str(rate_m_ratio),
             'all_k_ratio_lower_bounds_at_m70':strs(k_ratio_lower),
             'trace_strength_at_corner':str(lambda_z(m,2)),
             'seed_strength_at_corner':str(lambda_z(m,3)),
             'seed_subtraction_required':str(8*p0_bound(m)),
             'old_single_dominant_eta':str(dominant),'old_single_correction_epsilon':str(epsilon),
             'old_single_gate_ratio':str(dominant/(12*epsilon)),
             'old_single_consecutive_m_ratio':str(old_single_ratio)},
         'finite_pairs':finite_pairs,'input_sha256':{'old_normalized_constants.json':digest(oldpath),
             'finite_m_normalized_blocks_results.json':digest(blockpath)},
         'monotonicity':'Every k ratio is a positive constant times products ((ak+b)/(a(k+1)+b))^p, a,p>=0, with ak+b>0; m-tail ratios at k=3 have the identical form in m. Constant beta is excluded from strict k-ratio requirement.'}
    Path(__file__).with_name('scalar_closure_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','fixed_m_thresholds':{r['m']:r['all_k_from'] for r in recs},'analytic_m_tail_from':70,'finite_prefixes':34}))
if __name__=='__main__':main()
