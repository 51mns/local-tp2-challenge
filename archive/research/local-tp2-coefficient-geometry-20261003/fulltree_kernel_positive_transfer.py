"""Exact identities for a globally positive congruence model.
No finite-depth search is used: preservation is the manuscript induction.
"""
import continuation_network as p
z=[0];o=[1]
R=[[o,o],[z,o]]
Ri=[[o,[-1]],[z,o]]
def hat(Q):return p.mm(p.mm(Ri,Q),p.mt(Ri))
That=p.mm(p.mm(p.mt(R),p.T),R)
Q0,Q1=p.A0,p.B0
Qc=p.medi(Q0,Q1)
H0,H1,Hc=hat(Q0),hat(Q1),hat(Qc)
assert That==[[[3,3],[2,3]],[[4,3],[3,3]]]
assert H0==[[[2,1],[-1]],[[-1,-1],[1]]]
assert H1==[[[1],[0,1]],[[0],[1]]]
assert Hc==[[[2,3,2],[1,2]],[[1,1],[1]]]
M0=p.mm(p.mt(H0),That)
assert M0==[[[2,2],[1,2]],[[1],[1]]]
assert p.mm(p.mm(p.mt(H0),That),p.mt(H1))==Hc
Eca,Ecb=p.ms(Hc,H0),p.ms(Hc,H1)
assert Eca==[[[0,2,2],[2,2]],[[2,2],[0]]]
assert Ecb==[[[1,3,2],[1,1]],[[1,1],[0]]]
for name,Q in [('That',That),('H1',H1),('Hc',Hc),('M0',M0),('Eca',Eca),('Ecb',Ecb)]:
 assert all(min(entry)>=0 for row in Q for entry in row)
 print(name,Q)
# Congruence recovers original top-left scalar as the sum of four entries.
for Q in [Q0,Q1,Qc]:
 HH=hat(Q)
 assert p.add(p.add(HH[0][0],HH[0][1]),p.add(HH[1][0],HH[1][1]))==Q[0][0]
print('PASS: exact identities and induction seeds.')
