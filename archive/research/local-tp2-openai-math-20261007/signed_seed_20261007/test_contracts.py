"""Contract checks and negative controls, not finite-to-infinite extrapolation."""
import unittest
from itertools import product
from fractions import Fraction
import core as o
import verify_direct as l
from signed_gate import bern_grid

class Contracts(unittest.TestCase):
 def test_two_arithmetics_and_quotients(self):
  for length in range(6):
   for chars in product('LR',repeat=length):
    word=''.join(chars)
    for po,pl in zip(o.state(word),l.make_state(word)):
     self.assertEqual(o.H(po),l.row(pl))
     qq=o.divide_y(o.sub(po,o.one))
     qq2=l.div_y(l.plus(pl,l.sc(l.I,-1)))
     self.assertEqual(o.H(qq),l.row(qq2))
 def test_seed_identity_and_bounds(self):
  for length in range(7):
   for chars in product('LR',repeat=length):
    for dr in 'LR':
     r=o.raydata(''.join(chars),dr);A,B=r['A'],r['B']
     self.assertGreaterEqual(min(o.add(A,B)),0)
     self.assertGreaterEqual(min(o.sub(A,B)),0)
     self.assertTrue(min(B)>=0 or max(B)<=0)
     u=o.divide_y(o.sub(r['X'],o.one));v=o.divide_y(o.sub(r['Y'],o.one))
     rhs=o.add(o.add(o.one,o.mul((3,2),u)),o.add(o.mul((1,2),v),o.scale(o.mul(o.mul(o.y,o.y),o.mul(u,v)),3)))
     self.assertEqual(o.add(A,B),rhs)
 def test_ray_recurrence_and_degree(self):
  for word,dr in [('LRL','R'),('RLR','L')]:
   r=o.raydata(word,dr);A,B=r['A'],r['B'];uprev=(0,);u=(1,);z=(0,);Cprev=r['Y']
   for n in range(7):
    increment=o.mul(o.y,o.add(o.mul(A,u),o.mul(B,uprev)))
    z=o.add(z,o.add(o.mul(A,u),o.mul(B,uprev)))
    C=o.add(r['Y'],o.mul(o.y,z))
    self.assertEqual(C,o.state(word+dr*n)[1])
    self.assertEqual(o.sub(C,Cprev),increment)
    ss,dd=o.canonical_pair(word+dr*n)
    self.assertGreater(min(o.W(ss,dd)),0)
    self.assertEqual(o.coeff(o.H(ss),len(ss)),0)
    if n:
     a,b=len(r['X'])-1,len(r['Y'])-1
     self.assertEqual(len(dd)-len(ss),b+1+(n-1)*(a+1))
    uprev,u=u,o.sub(o.mul(r['t'],u),uprev);Cprev=C
 def test_positive_samples_do_not_certify(self):
  # f(r)=(r-1)^2-1/4 is positive at -2,0,2, but negative at r=1.
  values={ (j,):Fraction((r-1)**2)-Fraction(1,4) for j,r in enumerate((-2,0,2)) }
  self.assertGreater(min(values.values()),0)
  self.assertLess(min(bern_grid(values,1).values()),0)
 def test_wrong_commutation_or_sign_rejected(self):
  r=o.raydata('LRL','R')
  self.assertLess(max(r['B']),0)
  real_next=o.state('LRLR')[1]
  wrong_increment=o.mul(o.y,o.sub(o.mul(r['t'],r['A']),r['B']))
  self.assertNotEqual(o.add(r['C'],wrong_increment),real_next)

if __name__=='__main__':unittest.main(verbosity=2)
