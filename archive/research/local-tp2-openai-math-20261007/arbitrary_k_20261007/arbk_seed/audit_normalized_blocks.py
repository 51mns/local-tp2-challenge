#!/usr/bin/env python3
"""Independent reconstruction of every normalized-block certificate.

No author code is imported.  Canonical data use original ordinary-x
mutations.  Every tensor coefficient is reconstructed by exact quadratic
interpolation on {0,1/2,1} in each parameter, then compared to the author's
full array digest or symmetry-compressed rational coefficient.  This
differs from both author's sparse power algebra and endpoint-pair
histogram formula.
"""
import json
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from ordinary_arithmetic import add,sub,times,multiply,mutation,divide_y,fourier_horner,delta


def tensor_bernstein_twice(values,dim):
    out=list(values);size=len(out)
    assert size==3**dim
    for axis in range(dim):
        stride=3**axis
        for base in range(0,size,3*stride):
            for j in range(stride):
                i=base+j;a,b,c=out[i],out[i+stride],out[i+2*stride]
                out[i],out[i+stride],out[i+2*stride]=2*a,4*b-a-c,2*c
    back=list(out)
    for axis in reversed(range(dim)):
        stride=3**axis
        for base in range(0,size,3*stride):
            for j in range(stride):
                i=base+j;a,b,c=back[i],back[i+stride],back[i+2*stride]
                mid=a+2*b+c
                assert mid%4==0
                back[i],back[i+stride],back[i+2*stride]=a,mid//4,c
    assert back==[2**dim*v for v in values]
    return out


def digits(index,dim):
    out=[]
    for _ in range(dim):out.append(index%3);index//=3
    return out


def power_table(p,N):
    out=[[1]]
    for _ in range(N):out.append(multiply(out[-1],p))
    return out


def full_margin_rows(grid_keys,cache,target,dim):
    keys=list(cache);lookup={key:i for i,key in enumerate(keys)}
    indices=[lookup[key] for key in grid_keys]
    rows=[cache[key] for key in keys]
    degree=len(rows[0])-1
    assert all(len(h)==degree+1 and min(h)>0 for h in rows)
    for n in range(degree+1):
        bykey=[target.denominator*delta(h,n)-target.numerator*h[n]**2 for h in rows]
        values=[bykey[i] for i in indices]
        yield n,tensor_bernstein_twice(values,dim)


def m0_grid(case):
    npairs=case['pairs'];single=case['nonpositive_single']
    dim=2*npairs+int(single);t=[6,8,3]
    factors=[add(add(multiply(t,t),times(t,2*a)),[-4+4*b])
             for b in range(3) for a in range(3)]
    factorpowers=[power_table(p,npairs) for p in factors]
    seed=[4,2] if case['seed_2p'] else [1]
    if case['smooth_y']:seed=multiply(seed,[1,1])
    grid=[];cache={}
    for index in range(3**dim):
        ds=digits(index,dim);hist=[0]*9
        for pair in range(npairs):hist[ds[2*pair]+3*ds[2*pair+1]]+=1
        sing=ds[-1] if single else 0
        key=tuple(hist)+(sing,);grid.append(key)
        if key in cache:continue
        p=seed
        for i,n in enumerate(hist):
            if n:p=multiply(p,factorpowers[i][n])
        if single:p=multiply(p,add(t,[sing]))
        assert min(p)>0
        cache[key]=fourier_horner(p)
    return grid,cache,dim


def audit_m0(saved):
    records=[];total=0
    for case in saved['records']:
        grid,cache,dim=m0_grid(case);target=Q(case['target_eta'])
        checksum=sha256();minima=[];count=0
        for n,values in full_margin_rows(grid,cache,target,dim):
            assert min(values)>=0
            minima.append(min(values));count+=len(values)
            for v in values:checksum.update((str(v)+'\n').encode())
        assert minima==[r['minimum_scaled_margin'] for r in case['records']]
        assert checksum.hexdigest()==case['ordered_margin_sha256']
        assert count==case['bernstein_coefficient_count']
        total+=count
        record={'pairs':case['pairs'],'seed':case['seed_2p'],'smooth':case['smooth_y'],
                'single':case['nonpositive_single'],'tensor_coefficients':count,
                'ordered_margin_sha256':checksum.hexdigest(),'all_minima_and_digest_match':True}
        records.append(record)
        print('m0 block',record['pairs'],record['seed'],record['smooth'],record['single'],'PASS',count,flush=True)
    return {'records':records,'total_tensor_coefficients':total}


def canonical_old(m):
    prior=[1];Y=[2,1];C=[5,6,2]
    for _ in range(m):prior,Y,C=Y,C,mutation([1],C,Y)
    t=sub(times(multiply([1,1],Y),3),[0,1])
    a=divide_y(sub(C,[1]));b=divide_y(sub(prior,[1])) if m else [0]
    return t,a,b


def finite_grid(t,a,b,N,distinguished,smooth):
    dim=N+int(distinguished)
    f=[sub(t,[2]),t,add(t,[2])]
    powers=[power_table(p,N) for p in f]
    l=[add(multiply(a,p),b) for p in f]
    if smooth:l=[multiply(p,[1,1]) for p in l]
    grid=[];cache={}
    for index in range(3**dim):
        ds=digits(index,dim);hist=tuple(ds[:N].count(j) for j in range(3))
        sing=ds[-1] if distinguished else 0;key=hist+(sing,)
        grid.append(key)
        if key in cache:continue
        p=multiply(multiply(powers[0][hist[0]],powers[1][hist[1]]),powers[2][hist[2]])
        if distinguished:p=multiply(p,l[sing])
        assert min(p)>0
        cache[key]=fourier_horner(p)
    return grid,cache,dim


def audit_finite_case(t,a,b,N,distinguished,smooth,case):
    grid,cache,dim=finite_grid(t,a,b,N,distinguished,smooth)
    expected={tuple(v['histogram'])+(v['distinguished_index'],v['n']):v
              for v in case['coefficients']}
    assert len(expected)==case['histogram_coefficient_count']
    keys=[]
    for index in range(3**dim):
        ds=digits(index,dim)
        hist=tuple(ds[:N].count(j) for j in range(3))
        keys.append(hist+(ds[-1] if distinguished else 0,))
    target=Q(case['target_eta']);count=0;visited=set()
    for n,values in full_margin_rows(grid,cache,target,dim):
        assert min(values)>=0
        for key,value in zip(keys,values):
            exp=expected[key+(n,)]
            assert value*exp['common_denominator']==2**dim*exp['scaled_margin'],(N,distinguished,smooth,n,key)
            visited.add(key+(n,));count+=1
    assert count==case['full_tensor_coefficient_count']
    assert len(visited)==len(expected)
    # Reconstruct the author's compressed ordered digest after full verification.
    checksum=sha256()
    for v in case['coefficients']:checksum.update((str(v['scaled_margin'])+'\n').encode())
    assert checksum.hexdigest()==case['ordered_histogram_margin_sha256']
    return {'propagators':N,'distinguished':distinguished,'smooth':smooth,
            'full_tensor_coefficients':count,'histogram_coefficients':len(expected),
            'all_rational_coefficients_match':True}


def audit_finite(saved):
    records=[];total=0;histtotal=0
    for record in saved['records']:
        m=record['m'];t,a,b=canonical_old(m)
        cases=[audit_finite_case(t,a,b,8,False,False,record['block'])]
        for residue in record['residues']:
            cases.append(audit_finite_case(t,a,b,residue['remaining_propagators'],True,residue['smooth'],residue))
        assert Q(record['block']['target_eta'])/record['product_loss_denominator']==Q(record['per_trace_rate'])**8
        assert record['product_loss_denominator']==2*(8*(len(t)-1)+1)
        total+=sum(c['full_tensor_coefficients'] for c in cases)
        histtotal+=sum(c['histogram_coefficients'] for c in cases)
        records.append({'m':m,'cases':cases,'per_trace_rate':record['per_trace_rate'],'residual_eta':record['residual_eta']})
        print('finite m',m,'PASS; every full tensor coefficient matches',flush=True)
    return {'records':records,'total_full_tensor_coefficients':total,'total_histogram_coefficients':histtotal}


def main():
    here=Path(__file__).resolve().parent;source=here.parent/'arbk_mixed'
    m0=json.loads((source/'m0_normalized_blocks_results.json').read_text())
    finite=json.loads((source/'finite_m_normalized_blocks_results.json').read_text())
    result={'status':'PASS','author_code_imported':False,
            'method':'Original ordinary-x mutations; exact full tensor interpolation and inverse check',
            'm0':audit_m0(m0),'m1_to_4':audit_finite(finite)}
    dest=here/'normalized_blocks_independent_audit.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','m0_coefficients':result['m0']['total_tensor_coefficients'],
                      'm1_to_4_coefficients':result['m1_to_4']['total_full_tensor_coefficients'],
                      'output':dest.name},indent=2),flush=True)


if __name__=='__main__':main()
