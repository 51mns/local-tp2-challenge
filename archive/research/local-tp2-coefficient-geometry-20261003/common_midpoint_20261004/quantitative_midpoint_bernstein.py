#!/usr/bin/env python3
"""Exact finite-base MP2 Bernstein certificates; no all-tree inference."""
from __future__ import annotations
import json
import gzip
import hashlib
from fractions import Fraction
from math import comb
from pathlib import Path


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def add(p,q):return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def scale(p,k):return trim([v*k for v in p])
def sub(p,q):return add(p,scale(q,-1))
def mul(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):z[i+j]+=v*w
    return trim(z)
def H(p):return [sum(p[j]*comb(j,(j-n)//2) for j in range(n,len(p),2)) for n in range(len(p))]
def at(h,n):
    n=abs(n);return h[n] if n<len(h) else 0
def delta(h,n):return at(h,n)**2-at(h,n-1)*at(h,n+1)-at(h,n+1)**2+at(h,n)*at(h,n+2)
def aradd(*qs):
    z={}
    for q in qs:
        for k,v in q.items():z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def arscale(q,n):return {k:v*n for k,v in q.items() if v*n}
def tensor(p):
    h=H(p);xh=H([0]+p);z={}
    for i in range(len(xh)):
        for j in range(i+1,len(xh)):
            v=at(h,i)*at(xh,j)-at(h,j)*at(xh,i)
            if v:
                a,b=i+j-1,j-i-1
                z[a,b]=z.get((a,b),0)+v
                if i:z[b,a]=z.get((b,a),0)+v
    return {k:v for k,v in z.items() if v}
def mixed(p,q):return aradd(tensor(add(p,q)),arscale(tensor(p),-1),arscale(tensor(q),-1))

Y=[1,1];Y2=mul(Y,Y)
def state(a=[0],e=[1],r=[1]):
    X=add([1],mul(Y,a));t=add([3,2],scale(mul(Y2,a),3))
    k=mul(X,add([1],scale(mul(Y,a),3)))
    g=add(add(mul(sub(t,[2]),e),k),r);s=sub(mul(t,g),r)
    M=add(add(t,[1]),scale(mul(Y2,add(e,g)),3));d=mul(e,M)
    C=add([1],mul(Y,add(add(a,e),g)))
    T=sub(scale(mul(Y,C),3),[0,1]);cA=add(add(e,g),s)
    assert mul(r,g)==add(add(mul(sub(t,[2]),mul(e,e)),scale(mul(k,e),2)),scale(mul(a,mul(X,X)),3))
    return dict(a=a,e=e,r=r,g=g,s=s,d=d,C=C,T=T,cA=cA)
def child(z,side):
    return state(z['a'],add(z['e'],z['g']),z['g']) if side=='s' else state(add(z['a'],z['e']),z['g'],add(z['e'],z['g']))


def power_arrays(T,b0,b1,smooth=False,sharp=True):
    p=sub(T,[2]);L=add(mul(b0,p),b1);U=mul(p,L)
    A=add(mul(b0,p),scale(b1,Fraction(1,2)));B=b0
    if smooth:U,A,B,b1=(mul(Y,z) for z in [U,A,B,b1])
    DU,DA,DB,DE=map(tensor,[U,A,B,b1])
    MAU,MUB,MAB=mixed(U,A),mixed(U,B),mixed(A,B)
    c={(0,0):DU,(1,0):MAU,(0,1):MAU,
       (2,0):aradd(DA,arscale(DE,Fraction(-1,4))) if sharp else DA,
       (0,2):aradd(DA,arscale(DE,Fraction(-1,4))) if sharp else DA,
       (1,1):aradd(MUB,arscale(DA,2),arscale(DE,Fraction(1,2))) if sharp else aradd(MUB,arscale(DA,2)),
       (2,1):MAB,(1,2):MAB,(2,2):DB}
    return c,len(U)-1


def bernstein_arrays(c):
    out={}
    for k in range(3):
        for l in range(3):
            terms=[]
            for (i,j),arr in c.items():
                if i<=k and j<=l:
                    w=Fraction(comb(k,i),comb(2,i))*Fraction(comb(l,j),comb(2,j))*4**(i+j)
                    terms.append(arscale(arr,w))
            out[k,l]=aradd(*terms)
    return out


def formal_corner_identity():
    # Work in a free seven-dimensional symbol space; no state rows
    # or positivity assumptions enter this universal identity check.
    def quad(v):
        a,b,c=v
        return {k:n for k,n in {'TU':a*a,'TA':b*b,'TB':c*c,
                'JUA':a*b,'JUB':a*c,'JAB':b*c}.items() if n}
    def polar(v,w):
        return aradd(quad(tuple(a+b for a,b in zip(v,w))),
                     arscale(quad(v),-1),arscale(quad(w),-1))
    U,V,W=(1,0,0),(1,4,0),(1,8,16);E={'TE':1}
    powers={(0,0):{'TU':1},(1,0):{'JUA':1},(0,1):{'JUA':1},
            (2,0):{'TA':1,'TE':Fraction(-1,4)},
            (0,2):{'TA':1,'TE':Fraction(-1,4)},
            (1,1):{'JUB':1,'TA':2,'TE':Fraction(1,2)},
            (2,1):{'JAB':1},(1,2):{'JAB':1},(2,2):{'TB':1}}
    corners={(0,0):quad(U),(1,0):arscale(polar(U,V),Fraction(1,2)),
             (0,1):arscale(polar(U,V),Fraction(1,2)),
             (2,0):aradd(quad(V),arscale(E,-4)),
             (0,2):aradd(quad(V),arscale(E,-4)),
             (1,1):aradd(arscale(polar(U,W),Fraction(1,4)),
                         arscale(quad(V),Fraction(1,2)),arscale(E,2)),
             (2,1):arscale(polar(V,W),Fraction(1,2)),
             (1,2):arscale(polar(V,W),Fraction(1,2)),(2,2):quad(W)}
    assert bernstein_arrays(powers)==corners
    return True


def summary_arrays(arrays,keys):
    vals=[(arr.get(k,Fraction(0)),param,k) for param,arr in arrays.items() for k in keys]
    bad=[v for v in vals if v[0]<0]
    nz=[v for v in vals if v[0]]
    return {'coefficients':len(vals),'negative_coefficients':len(bad),
            'first_negative':encode_min(min(bad)) if bad else None,
            'minimum_nonzero':encode_min(min(nz)) if nz else None,
            'all_nonnegative':not bad,
            'zeros':sum(v[0]==0 for v in vals)}
def encode_min(z):return {'value':str(z[0]),'parameter_bernstein_index':z[1],'character_index':z[2]}


def line_certificate(T,b0=None,b1=None,smooth=False):
    # r=2-4u; trace or L_r gives row P0+u P1.
    P0=sub(T,[2]) if b0 is None else add(mul(b0,sub(T,[2])),b1)
    P1=[4] if b0 is None else scale(b0,4)
    if smooth:P0,P1=(mul(Y,p) for p in [P0,P1])
    a,b=H(P0),H(P1);D0,DB=tensor(P0),tensor(P1);M=mixed(P0,P1)
    c0=D0;c1=aradd(D0,arscale(M,Fraction(1,2)));c2=aradd(D0,M,DB)
    arrays={(0,0):c0,(1,0):c1,(2,0):c2}
    keys=[(2*n,0) for n in range(len(a))]
    rec=summary_arrays(arrays,keys)
    all_keys=sorted(set().union(*(arr.keys() for arr in arrays.values())))
    rec['all_character_bernstein']=summary_arrays(arrays,all_keys)
    rec['complete_all_character_bernstein']=[[k,l,[[a,b,str(v)] for (a,b),v in sorted(arr.items())]] for (k,l),arr in arrays.items()]
    rec['strict_all_supported_bernstein']=all(arr.get(k,0)>0 for arr in arrays.values() for k in keys)
    rec['degree']=len(P0)-1
    rec['complete_supported_defect_bernstein']=[[k,[str(arr.get(index,0)) for index in keys]] for (k,l),arr in arrays.items()]
    return rec


def record(z,label,b0,b1,orientation,smooth):
    p=sub(z['T'],[2]);L2=add(mul(b0,p),b1);H22=mul(p,L2)
    # alpha=2-r,beta=2-s are nonnegative.  These positive dense
    # corner polynomials determine the support throughout the box.
    assert all(v>0 for v in p)
    assert all(v>0 for v in b0) and all(v>0 for v in b1)
    assert len(b1)-1 < len(b0)-1 + len(z['T'])-1
    assert all(v>0 for v in L2) and all(v>0 for v in H22)
    sb0,sb1=(mul(Y,b0),mul(Y,b1)) if smooth else (b0,b1)
    assert len(sb1)-1 < len(sb0)-1 + len(z['T'])-1
    cornerL,cornerH=(mul(Y,L2),mul(Y,H22)) if smooth else (L2,H22)
    assert all(v>0 for v in cornerL) and all(v>0 for v in cornerH)
    support={'trace_T_minus_2_positive_dense':True,
             'trace_T_minus_2_constant':p[0],
             'seeds_positive_dense':True,
             'strict_seed_degree':{'degree_b0':len(sb0)-1,'degree_b1':len(sb1)-1,'degree_T':len(z['T'])-1},
             'degree_L':len(cornerL)-1,'degree_H':len(cornerH)-1,
             'corner_L2_positive_dense':True,'corner_H22_positive_dense':True,
             'corner_L2_ordinary_coefficients':cornerL,'corner_H22_ordinary_coefficients':cornerH,
             'box_support_argument':'nonnegative alpha,beta expansion plus strictly positive dense corner'}
    powers,D=power_arrays(z['T'],b0,b1,smooth,True)
    sharp=bernstein_arrays(powers)
    keys=sorted(set().union(*(p.keys() for p in sharp.values())))
    direct=summary_arrays(sharp,keys)
    hpower,_=power_arrays(z['T'],b0,b1,smooth,False)
    uniform_power=dict(hpower)
    reference=mul(Y,b1) if smooth else b1
    uniform_power[0,0]=aradd(uniform_power[0,0],arscale(tensor(reference),-4))
    uniform=bernstein_arrays(uniform_power)
    uniform_keys=sorted(set().union(*(p.keys() for p in uniform.values())))
    uniform_summary=summary_arrays(uniform,uniform_keys)
    hber=bernstein_arrays(hpower)
    hkeys=sorted(set().union(*(p.keys() for p in hber.values())))
    hall=summary_arrays(hber,hkeys)
    hdef=summary_arrays(hber,[(2*n,0) for n in range(D+1)])
    hdef['strict_all_supported_bernstein']=all(p.get((2*n,0),0)>0 for p in hber.values() for n in range(D+1))
    hdef['complete_supported_defect_bernstein']=[[k,l,[str(p.get((2*n,0),0)) for n in range(D+1)]] for (k,l),p in hber.items()]
    line=line_certificate(z['T'],b0,b1,smooth)
    return {'state':label,'orientation':orientation,'smoothed':smooth,'degree_H':D,
            'trace_T':z['T'],'seed_b0':b0,'seed_b1':b1,'support':support,
            'sharp_relative_all_characters':direct,'H_all_characters':hall,'H_defects':hdef,'L_defects':line,
            'uniform4_relative_all_characters':uniform_summary,
            'sharp_MP2_parameter_certificate_pass':direct['all_nonnegative'] and hall['all_nonnegative'] and hdef['strict_all_supported_bernstein'] and line['strict_all_supported_bernstein'] and line['all_character_bernstein']['all_nonnegative'],
            'uniform_MP2_parameter_certificate_pass':uniform_summary['all_nonnegative'] and hall['all_nonnegative'] and hdef['strict_all_supported_bernstein'] and line['strict_all_supported_bernstein'] and line['all_character_bernstein']['all_nonnegative'],
            'complete_sharp_bernstein_arrays':[[k,l,[[a,b,str(v)] for (a,b),v in sorted(p.items())]] for (k,l),p in sharp.items()],
            'complete_uniform4_bernstein_arrays':[[k,l,[[a,b,str(v)] for (a,b),v in sorted(p.items())]] for (k,l),p in uniform.items()],
            'complete_H_bernstein_arrays':[[k,l,[[a,b,str(v)] for (a,b),v in sorted(p.items())]] for (k,l),p in hber.items()],
            'negative_power_coefficients':[[i,j,a,b,str(v)] for (i,j),p in powers.items() for (a,b),v in sorted(p.items()) if v<0]}


def run():
    root=state();states=[('root',root),('first-short',child(root,'s')),('first-long',child(root,'l'))]
    records=[];traces=[]
    for label,z in states:
        trace_certificate=line_certificate(z['T'])
        assert trace_certificate['strict_all_supported_bernstein'] and trace_certificate['all_character_bernstein']['all_nonnegative']
        traces.append({'state':label,'trace':z['T'],'certificate':trace_certificate})
        for orientation,b0,b1 in [('forward',z['cA'],z['e']),('reverse',z['e'],z['cA'])]:
            for smooth in [False,True]:records.append(record(z,label,b0,b1,orientation,smooth))
    return {'status':'EXACT_FINITE_PARAMETER_CERTIFICATES_NOT_COMMON_CLOSURE',
            'universal_corner_identity_formal_check':formal_corner_identity(),
            'all_minor_implication':'conditional on independently audited network all-minor/character equivalence',
            'canonical_states':[dict(state=label,**z) for label,z in states],
            'traces':traces,'records':records,
            'imports':'standard Python only; no parent arithmetic'}


def concise(value):
    if isinstance(value,list):return [concise(v) for v in value]
    if not isinstance(value,dict):return value
    out={}
    for key,item in value.items():
        if key.startswith('complete_'):continue
        if key=='negative_power_coefficients':
            out['negative_power_coefficient_count']=len(item)
            out['first_negative_power_coefficient']=item[0] if item else None
        else:out[key]=concise(item)
    return out


if __name__=='__main__':
    result=run();path=Path(__file__).with_name('quantitative_midpoint_bernstein_results.json')
    full=(json.dumps(result,indent=2)+'\n').encode()
    compressed=gzip.compress(full,mtime=0)
    archive=path.with_name('quantitative_midpoint_bernstein_full.json.gz')
    archive.write_bytes(compressed)
    short=concise(result)
    short['full_certificate']={'file':archive.name,
          'uncompressed_bytes':len(full),'gzip_bytes':len(compressed),
          'uncompressed_sha256':hashlib.sha256(full).hexdigest(),
          'gzip_sha256':hashlib.sha256(compressed).hexdigest(),
          'compression':'gzip.compress(full_json_utf8,mtime=0)'}
    path.write_text(json.dumps(short,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'trace_pass':[(z['state'],z['certificate']['strict_all_supported_bernstein']) for z in result['traces']],
        'records':[{'state':z['state'],'orientation':z['orientation'],'smooth':z['smoothed'],'sharp_pass':z['sharp_MP2_parameter_certificate_pass'],'uniform4_pass':z['uniform_MP2_parameter_certificate_pass'],
                    'sharp_negative_coefficients':z['sharp_relative_all_characters']['negative_coefficients'],
                    'H_strict':z['H_defects']['strict_all_supported_bernstein'],'L_strict':z['L_defects']['strict_all_supported_bernstein']} for z in result['records']]},indent=2))
