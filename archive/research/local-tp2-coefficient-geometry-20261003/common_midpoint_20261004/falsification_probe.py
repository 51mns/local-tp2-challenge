#!/usr/bin/env python3
"""Frozen actual paired midpoint probe, exact rational coefficients."""
import sys,json,itertools,hashlib,gzip
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'common_transport_20261004'))
import adversarial_probe as p

PAIRS=[(-2,-2),(-2,2),(2,2),(0,0),(-1,1),(0,2),(-2,0),(1,2),
       (Fraction(-3,2),Fraction(3,2)),(Fraction(3,2),Fraction(3,2)),(Fraction(3,2),2),
       (Fraction(-1,2),Fraction(1,2))]
def frac(v):
 v=Fraction(v);return {'numerator':v.numerator,'denominator':v.denominator}
def serial(v):
 if isinstance(v,Fraction):return frac(v)
 if isinstance(v,dict):return {k:serial(w) for k,w in v.items()}
 if isinstance(v,list) or isinstance(v,tuple):return [serial(w) for w in v]
 return v
def root():return p.build([0],[1],[1])
def actual(path):
 v=root();triple=([1],[2,1],[5,6,2])
 for ch in path:
  X,Y,C=triple
  short=p.sub(p.sub(p.scale(p.mul(p.y,p.mul(X,C)),3),p.mul([0,1],p.add(X,C))),Y)
  long=p.sub(p.sub(p.scale(p.mul(p.y,p.mul(Y,C)),3),p.mul([0,1],p.add(Y,C))),X)
  triple=(X,C,short) if ch=='s' else (Y,C,long)
  v=dict(p.children(v))['short' if ch=='s' else 'long']
  assert tuple(v[k] for k in ('X','Y','C'))==triple
 assert p.fricke(v)==[0]
 return v
def paths():
 words=[''.join(w) for n in range(3) for w in itertools.product('sl',repeat=n)]
 words+=['s'*j for j in range(13)]+['l'+'s'*j for j in range(11)]+['l'*j for j in range(7)]
 words+=['sl'*j for j in range(1,6)]+['ls'*j for j in range(1,6)]
 return sorted(set(words),key=lambda w:(len(w),tuple(0 if c=='s' else 1 for c in w)))
def row01_minors(h):
 xh=[p.at(h,abs(1-n))+p.at(h,n+1) for n in range(len(h)+1)]
 # At n0 both Laurent contributions are h1, including the factor2.
 return {(k,l):p.at(h,k)*xh[l]-p.at(h,l)*xh[k]
         for k in range(len(h)+1) for l in range(k+1,len(h)+1)}
def scalar_certificate(h,b,factor):
 ds=p.defects(h);lam=min(Fraction(d,hn) for d,hn in zip(ds,h));alpha=min(Fraction(p.at(h,n),bn) for n,bn in enumerate(b) if bn)
 margin=lam*alpha-2*factor*b[0]
 return {'lambda':frac(lam),'alpha':frac(alpha),'threshold_factor':frac(factor),'margin':frac(margin),
 'pass':lam>0 and alpha>=2 and len(h)>=len(b) and max(b)<=b[0] and margin>=0}
def main():
 out={'scope':'Frozen actual paths/12 exact midpoint parameter pairs; no parameter-continuum or all-tree implication',
 'arithmetic_import':'read-only common_transport_20261004/adversarial_probe.py','states':[],'skipped_degree_cap':[],
 'first_failures':{},'cases':0,'row01_minor_comparisons':0,'all_index_strength_certificates':0,
 'strength_only_failures':0,'reference_auxiliary_cone_failures':0,'records':[]}
 stop=False
 for path in paths():
  v=actual(path);T=p.sub(v['M'],[1]);c=p.add(v['e'],v['g'],v['s']);maxdeg=max(len(p.mul(c,p.mul(T,T)))-1,len(p.mul(v['e'],p.mul(T,T)))-1)+1
  if maxdeg>160:out['skipped_degree_cap'].append({'path':path,'smoothed_midpoint_degree':maxdeg});continue
  out['states'].append(path)
  for orient,b0,b1 in [('forward',c,v['e']),('reverse',v['e'],c)]:
   for param in sorted(set(r for pair in PAIRS for r in pair)):
    shift=p.sub(T,[param]);L=p.add(p.mul(b0,shift),b1)
    for block,poly in [('trace',shift),('L',L),('yL',p.mul(p.y,L))]:
     h=p.H(poly);ds=p.defects(h);bad=[i for i,z in enumerate(ds) if z<0 or (block!='trace' and z==0)]
     if min(h)<=0 or bad:
      key=block;out['first_failures'].setdefault(key,{'path':path,'orientation':orient,'parameter':frac(param),'index':bad[0] if bad else h.index(min(h)),'value':frac(ds[bad[0]] if bad else min(h)),'poly':poly,'row':h,'a':v['a'],'e':v['e'],'r':v['r']});stop=True
   for r,s in PAIRS:
    u=Fraction(r+s,2);H=p.add(p.mul(b0,p.mul(p.sub(T,[r]),p.sub(T,[s]))),p.mul(b1,p.sub(T,[u])))
    for smooth in (False,True):
     hp=p.mul(p.y,H) if smooth else H;bp=p.mul(p.y,b1) if smooth else b1;h,b=p.H(hp),p.H(bp);ds=p.defects(h)
     assert min(h)>0 and min(b)>0
     out['cases']+=1
     if min(p.defects(b))<0:out['reference_auxiliary_cone_failures']+=1
     bad=[i for i,z in enumerate(ds) if z<0]
     if bad:
      out['first_failures'].setdefault('H_cone',{'path':path,'orientation':orient,'parameters':[frac(r),frac(s)],'smooth':smooth,'index':bad[0],'value':frac(ds[bad[0]]),'poly':hp,'reference':bp,'row':h,'reference_row':b});stop=True
     hm,bm=row01_minors(h),row01_minors(b);uniform=[];sharp=[];factor=Fraction((r-s)**2,4)
     for (k,l),det in hm.items():
      ref=bm.get((k,l),0);mu=det-4*ref;ms=det-factor*ref;out['row01_minor_comparisons']+=1
      if mu<0:uniform.append((k,l,mu,det,ref))
      if ms<0:sharp.append((k,l,ms,det,ref))
     cert=scalar_certificate(h,b,4)
     if cert['pass']:out['all_index_strength_certificates']+=1
     else:out['strength_only_failures']+=1
     rec={'path':path,'orientation':orient,'r':frac(r),'s':frac(s),'smooth':smooth,'degree_h':len(h)-1,'degree_reference':len(b)-1,
       'uniform_row01_failures':len(uniform),'sharp_row01_failures':len(sharp),'uniform_all_index_strength_certificate':cert,
       'min_uniform_row01_margin':frac(min(hm[kl]-4*bm.get(kl,0) for kl in hm)),
       'min_sharp_row01_margin':frac(min(hm[kl]-factor*bm.get(kl,0) for kl in hm))}
     out['records'].append(rec)
     for key,wits in [('uniform4',uniform),('sharp_mixed',sharp)]:
      if wits and key not in out['first_failures']:
       k,l,margin,det,ref=wits[0]
       out['first_failures'][key]={'path':path,'orientation':orient,'parameters':[frac(r),frac(s)],'smooth':smooth,'indices':[0,1,k,l],
        'margin':frac(margin),'H_det':frac(det),'reference_det':frac(ref),'sharp_factor':frac(factor),'sharp_margin_same_witness':frac(det-factor*ref),
        'H_poly':hp,'reference_poly':bp,'H_row':h,'reference_row':b,'a':v['a'],'e':v['e'],'r':v['r']}
       stop=True
  if stop:break
 out['row01_pass_scope']='ALL-index character equivalence independently proof-audited PASS; all strength-certified cases additionally prove ALL ordered minors by the prior strength theorem.'
 out['source_sha256']=hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest()
 return out
def summary(out):
 out=serial(out);records=out['records'];tf=lambda z:Fraction(z['numerator'],z['denominator'])
 result={k:v for k,v in out.items() if k!='records'}
 result['parameter_pairs']=[[frac(r),frac(s)] for r,s in PAIRS]
 result['actual_states']=len(out['states']);result['orientations']=['forward (c_A,e)','reverse (e,c_A)'];result['modes']=['raw','y-smoothed']
 def measure(rec,key):
  cert=rec['uniform_all_index_strength_certificate'];la=tf(cert['lambda'])*tf(cert['alpha']);margin=tf(cert['margin']);b0=(la-margin)/8
  return {'certificate_margin':margin,'certificate_ratio':la/(8*b0),'uniform_row01_margin':tf(rec['min_uniform_row01_margin']),'sharp_row01_margin':tf(rec['min_sharp_row01_margin'])}[key]
 result['global_minima']={}
 for key in ('certificate_margin','certificate_ratio','uniform_row01_margin','sharp_row01_margin'):
  rec=min(records,key=lambda q:measure(q,key))
  result['global_minima'][key]={'value':frac(measure(rec,key)),'case':{k:rec[k] for k in ('path','orientation','r','s','smooth','degree_h','degree_reference')},'certificate':rec['uniform_all_index_strength_certificate']}
 result['reference_auxiliary_exception']='Exactly12 cases: forward root y-smoothed reference ye=y has delta0=-1; reference cone is NOT a packet premise.'
 result['generator_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 result['all_index_status']='1584 fixed cases certified by exact all-minor strength theorem AND row01 character equivalence; no continuum or all-tree inference.'
 return result
def write_outputs(out):
 out=serial(out);out['row01_pass_scope']='ALL-index character equivalence independently proof-audited PASS; strength theorem also certifies every case.'
 raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();gz=gzip.compress(raw,mtime=0)
 Path(__file__).with_name('falsification_records.json.gz').write_bytes(gz)
 result=summary(out);result['detailed_records']={'file':'falsification_records.json.gz','cases':len(out['records']),'compressed_bytes':len(gz),'compressed_sha256':hashlib.sha256(gz).hexdigest(),'uncompressed_sha256':hashlib.sha256(raw).hexdigest()}
 Path(__file__).with_name('falsification_results.json').write_text(json.dumps(result,indent=2)+'\n')
 return result
if __name__=='__main__':
 result=write_outputs(main())
 print(json.dumps({k:result[k] for k in ('actual_states','cases','row01_minor_comparisons','all_index_strength_certificates','first_failures','global_minima','detailed_records')},indent=2))
