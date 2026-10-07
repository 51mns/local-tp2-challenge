"""Exact strength certificates for the all-left prefix multipliers."""
import continuation_bracket_certify as b
import continuation_prefix as p
from fractions import Fraction as Q
import json

x,u,v,w,z,t = b.x,b.u,b.v,b.w,b.z,b.t
f=b.general_pair(u,v);g=b.general_pair(w,z)
quartic=p.mul(f,g)
middle=p.add(x,p.const(Q(3,2)),p.scale(w,Q(1,2)))
u_pair_even=p.add(b.x2,p.scale(x,3),p.const(2),p.scale(u,Q(1,4)))
u_pair_odd=p.add(b.x2,p.scale(x,3),p.const(Q(7,4)),p.scale(u,Q(1,2)))
inner=p.mul(p.add(x,p.const(1),p.scale(v,Q(1,2))),p.add(x,p.const(Q(3,2)),w))
general_independent=b.general_pair(v,z)
residues={
 'n_mod8_0_pull_quartic':quartic,
 'n_mod8_1_pull_quartic':p.mul(quartic,p.add(x,p.const(Q(3,2)),p.scale(t,Q(1,2)))),
 'n_mod8_2':p.mul(b.central,middle),
 'n_mod8_3':p.mul(b.central,inner),
 'n_mod8_4':p.mul(u_pair_even,inner),
 'n_mod8_5':p.mul(p.mul(u_pair_even,middle),general_independent),
 'n_mod8_6':p.mul(p.mul(p.mul(b.central,u_pair_odd),middle),general_independent),
 'n_mod8_7':p.mul(b.central,u_pair_odd),
}

def cert_strength(name,poly,lam):
 h=p.fourier(poly);ds=p.defects(poly);result=[]
 for n,d in enumerate(ds):
  margin=p.add(d,p.scale(h[n],-lam))
  degrees,coeffs=p.bernstein(margin)
  lower=min(coeffs.values())
  print(name,n,'lower',lower,flush=True)
  assert lower>=0,(name,n,lower)
  result.append({'index':n,'degrees':degrees,'lower_bound':str(lower),'power_coefficients':{','.join(map(str,k[1:])):str(v) for k,v in sorted(margin.items())},'bernstein_coefficients':{k:str(v) for k,v in coeffs.items()}})
 return result

if __name__=='__main__':
 result={'scaled_quartic_one_strong':cert_strength('quartic',p.scale(quartic,16),1)}
 for name,R in residues.items():
  degree=max(k[0] for k in R)
  poly=p.scale(p.mul(b.y2,R),2**degree)
  result[name]={'residue_degree':degree,'strength':4,'certificates':cert_strength(name,poly,4)}
 with open('mixed_kernel_pureleft_certificates.json','w') as out:json.dump(result,out,indent=2)
