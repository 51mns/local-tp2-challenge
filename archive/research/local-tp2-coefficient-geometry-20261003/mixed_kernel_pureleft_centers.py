"""Companion exact certificates: every pure-left center belongs to F."""
import json
import mixed_kernel_pureleft_margin as c
p=c.p

if __name__=='__main__':
 result={}
 for name,R in c.residues.items():
  d=max(k[0] for k in R)
  poly=p.scale(p.mul(c.b.y,R),2**d)
  result[name]={'residue_degree':d,'strength':3,'certificates':c.cert_strength(name,poly,3)}
 with open('mixed_kernel_pureleft_centers_certificates.json','w') as out:json.dump(result,out,indent=2)
