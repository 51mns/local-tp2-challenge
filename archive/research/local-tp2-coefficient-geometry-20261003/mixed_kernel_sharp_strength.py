"""Exact leading-scale strength bounds on the pure-left residue boxes."""
import json
from fractions import Fraction as Q
import mixed_kernel_pureleft_margin as c
p=c.p

if __name__=='__main__':
 result={'quartic':{'strength':16,'certificates':c.cert_strength('quartic16',p.scale(c.quartic,16),16)},'residues':{}}
 for name,R in c.residues.items():
  d=max(k[0] for k in R);leading=2**d
  result['residues'][name]={'degree':d,
   'y2_prefix':{'strength':leading,'certificates':c.cert_strength(name+'_y2',p.scale(p.mul(c.b.y2,R),leading),leading)},
   'prefix':{'strength':Q(leading,2).numerator,'certificates':c.cert_strength(name+'_prefix',p.scale(R,leading),Q(leading,2))}}
 with open('mixed_kernel_sharp_strength_certificates.json','w') as out:json.dump(result,out,indent=2)
