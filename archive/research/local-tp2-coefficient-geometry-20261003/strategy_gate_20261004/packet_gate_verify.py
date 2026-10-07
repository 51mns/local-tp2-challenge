"""Exact replay of one canonical compensation obstruction; no state scan."""
from packet_gate_probe import add,scale,mul,row,at,delta,advance,state,beta
import json
from pathlib import Path

a,e,r=advance([0],[1],[1],0)
t,g,s,T,c,d=state(a,e,r)
h=add(a,e,scale(r,-1))
A=mul(beta,g,add(t,[1]))
B=mul(beta,e,add(T,[1]))
R=add([5,2],mul(beta,h))
child=add(T,[2],mul(beta,add(s,d)))
assert child==add(A,B,R)
# Independent formula within this lane: original scalar LONG mutation.
# This guard reconstructs the child center before computing its trace.
y=[1,1];x=[0,1]
X=add([1],mul(y,a));Y=add(X,mul(y,e));C=add(Y,mul(y,g))
assert T==add(mul([3],y,C),scale(x,-1))
scalar_child_C=add(mul([3],y,Y,C),scale(mul(x,add(Y,C)),-1),scale(X,-1))
scalar_child_trace=add(mul([3],y,scalar_child_C),scale(x,-1))
assert child==add(scalar_child_trace,[2])
assert T==[39,116,132,66,12]
X=add([1],mul([1,1],a))
k=mul(X,add(scale(X,3),[-2]))
fricke=add(mul(r,g),scale(mul(add(t,[-2]),e,e),-1),scale(mul(k,e),-2),scale(mul(a,X,X),-3))
assert fricke==[0]
HA,HB,HR=row(A),row(B),row(R)
for H in (HA,HB,HR):assert all(delta(H,j)>0 for j in range(len(H)))
j=6
actual=delta(row(child),j)
source_sum=sum(delta(H,j) for H in (HA,HB,HR))
assert actual==227664 and source_sum==229392 and actual-source_sum==-1728
assert len(A)-1==5 and len(B)-1==7
assert -A[-1]*HB[7]==-1728
result={'parent':'first SHORT child S, whose complete P0 is independently established in earlier base certificates','a':a,'e':e,'r':r,'canonical_T':T,'direct_scalar_child_C':scalar_child_C,'direct_scalar_child_trace':scalar_child_trace,'fricke_residual':fricke,'h':h,'sources':{'A':A,'B':B,'R':R},'source_rows':{'A':HA,'B':HB,'R':HR},'source_supported_defects':{name:[delta(H,j) for j in range(len(H))] for name,H in [('A',HA),('B',HB),('R',HR)]},'failed_bridge':'delta_j(T_LONG_child+2) >= delta_j(A)+delta_j(B)+delta_j(R)','index':j,'character':[12,0],'mixed_selector':-1728,'actual_defect':actual,'source_sum':source_sum,'scope':'This canonical witness refutes the proposed additive compensation bridge, not child trace positivity or MP0.'}
Path(__file__).with_name('packet_gate_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
