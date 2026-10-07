#!/usr/bin/env python3
"""Exact formal identities for gap_shifted_trace.md; no root scans.
Uses frozen network lane's symbolic arithmetic only, not a trace theorem.
"""
from fractions import Fraction as F
import importlib.util,json
from pathlib import Path
helper=Path(__file__).resolve().parent.parent/'common_closure_20261004'/'network_trace_audit.py'
spec=importlib.util.spec_from_file_location('frozen_network_symbolic_arithmetic',helper)
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

h=[p.var(i) for i in range(7)];c=p.const(F(1,2));v,z=p.trace(h,c)
LB=p.add(p.scale(h[0],9),p.scale(h[1],4),p.scale(h[2],4),p.scale(h[3],10))
central=p.add(p.scale(LB,9),p.scale(v[0],3),p.scale(v[1],-24),p.scale(v[2],F(3,2)),p.const(F(-31,4)))
expected=p.add(p.scale(h[0],F(87,2)),p.scale(h[1],-45),p.scale(h[2],F(-3,2)),p.scale(h[3],69),p.scale(h[4],F(3,2)),p.const(F(-31,4)))
assert central==expected
b=p.var(8);u=p.add(p.scale(p.mul(b,b),2),p.const(-1))
assert p.add(u,p.mul(u,u),p.neg(p.mul(b,b)))==p.add(p.scale(p.mul(b,b,b,b),4),p.scale(p.mul(b,b),-3))
# Direct exact lower-degree worst constants.
A,B=h[0],h[1];_,zd=p.trace([A,B],c)
expected_d0=p.add(p.scale(p.mul(A,A),36),p.scale(p.mul(A,B),18),p.scale(p.mul(B,B),-72),p.scale(A,F(-75,2)),p.scale(B,-81),p.const(F(-31,4)))
assert p.defect(zd,0)==expected_d0
_,a1=p.trace([p.const(1)],c);_,a2=p.trace([p.const(2)],c)
assert p.defect(a1,0)==p.const(F(-37,4));assert p.defect(a2,0)==p.const(F(245,4))
_,linear2=p.trace([p.const(4),p.const(2)],c)
assert p.defect(linear2,0)==p.const(F(449,4))
# Seed-advance identity from exact formal polynomials; mathematical induction
# and spectral bounds are in the note, not inferred from these examples.
t=p.var(9);rho=p.var(10);seedc=p.var(11);seedd=p.var(12)
U=[p.const(1),t]
for n in range(1,7):U.append(p.sub(p.mul(t,U[-1]),U[-2]))
getU=lambda n:{} if n==-1 else U[n]
P=lambda n:p.const(1) if n==0 else p.sub(U[n],p.mul(rho,getU(n-1)))
ck,dk=seedc,seedd
for k in range(6):
 lhs=p.add(p.mul(ck,p.sub(t,rho)),dk)
 rhs=p.add(p.mul(seedc,P(k+1)),p.mul(seedd,P(k)))
 assert lhs==rhs
 ck,dk=p.add(p.mul(t,ck),dk),p.neg(ck)
result=dict(scope='Formal algebra validation only; all inequalities and Robin bounds are analytic.',formal_checks=dict(central_5over2_coefficients=True,cubic_folded_relation=True,degree1_central_formula=True,low_degree_minima=True,seed_advance_identity=True),exact_square_gaps=dict(central=473**2-3*270**2,positive_coefficient_numerator=4*42**2-3*45**2),excluded_constant_a1_central='-37/4',constant_a2_central='245/4',linear_A4_B2_central='449/4',shared_arithmetic=str(helper),no_scans=True)
Path(__file__).with_name('gap_trace_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
