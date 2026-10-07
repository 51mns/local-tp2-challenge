# Common transport campaign after 51af29c

Full-tree strict Local TP2 is OPEN. The user's criterion is one explicit
state predicate with ROOT, BOTH CHILDREN, and IMPLIES TARGET proofs.
Do not count new path families or larger finite scans as a closure proof.

Read-only foundations: ../common_closure_20261004/ and earlier parent files.
Private base commit: 51af29c7b849a7c05dcf0c2374355b71bc8744eb.
Public reference last rechecked: 6e770f3b3e3f26af5df5308572917559343b68f4.
Write only assigned prefixes in this NEW directory. Do not edit frozen work.
Use exact integers / Fractions / symbolic identities. Label discovery-only
floating evidence and distinguish off-Fricke states from actual states.

## Exact setup

y=x+1, z=2x+3, P=x+2.
X=1+ya, Y=X+ye, C=Y+yg,
t=z+3y²a, k=X(3X-2), g=(t-2)e+k+r,
s=tg-r, M=3yC-x+1, d=eM.
Short: (a,e,r)->(a,e+g,g).
Long: (a,e,r)->(a+e,g,e+g).
Root: (0,1,1). Short/long refer to degree ordering, not fixed Farey labels.
Fricke F=rg-(t-2)e²-2ke-3aX²=0.
Known ordinary inequalities include a>=0, e>=a+1, r>=1, r<=a+e,
g>=a+e+r+1, e>=(z-2)a. The global character multiplicative strip and
the previous endpoint ancestry must not be replaced by arbitrary rows.

Actual rows E=ye,G=yg,R=yr,S=ys,D=yd.
Q=S-G=(t-2)C-xX, Pi=XP M=PQ+V, V=PX+P²C.
For H(A)_n=[q^n]A(q+q^-1), reflect negative n and zero extend.
delta_n(h)=h_n²-h_(n-1)h_(n+1)-h_(n+1)²+h_nh_(n+2).
K_h(0,j)=h_j; K_h(i,0)=2h_i for i>0;
K_h(i,j)=h_|i-j|+h_i+j for i,j>0.
Folded TP2 equivalence and product closure are proved in parent files.
W_n(A,B)=H(A)_n H(B)_(n+1)-H(A)_(n+1) H(B)_n.

Regular P_Q: E<=lrG, R<=lrG, XP<=lrE, YP<=lrG,
K_G TP2, K_M TP2, W_n(Q,Pi)>0 on Q support.
Parent P_Q implies strict target W_n(S,D)>0 and ALL FOUR LR links at
BOTH children. Root target and both first-level full predicates proved.
Only K_G, K_M, strict proxy child preservation are OPEN.

Short G'=S, M'=M+3yS, Q'=Q+(t-2)S, Pi'=Pi+3yXP S.
Long Fout=S+D, tl=t+3yE, G'=Fout, M'=M+3yFout,
Q'=Q+(t-2)Fout+E(M-1+3yFout), Pi'=Pi+PD+3yYP Fout.
Retain correlated signed blocks; arbitrary positive sums do NOT preserve
folded TP2. Multiplication by y is NOT generally cone-preserving.

## Most recent common paired candidate

T=3yC-x=M-1, Z=a+e+g, cA=e+g+s, cB=g+s+d=cA+Te.
Global ordinary 0<=cA<=Te<=cB<=2Te is proved.
cA²+e(TcA+e)=cB²-e(TcB-e)=C²(1+3Z) on Fricke;
off-Fricke residual is exactly -(T-2)F.
qN_A=cA U_N(T/2)+e U_(N-1)(T/2),
qN_B=cA U_N(T/2)+e U_(N+1)(T/2).
Positive Packet(T,cA,e) and reversed Packet(T,e,cA) have proved ROOT,
correct strict degree condition deg d0<deg c+deg T, and conditional
N>=1 run-kernel implication. Their mutation preservation is OPEN.
q0_A is e'+g', NOT short child's g'=s. Full-tree path coverage is separate.
Full definitions and precise parameter boxes: previous invariant_spectral_packet.md.

## Failed routes already established

Coarse strength*domination relative-minor gates fail at canonical s³/s⁴
and on infinite pure-short tails. Refined reference-band gates fail s⁶/s⁷.
A uniform retained subtraction reserve 1/32 fails s²⁸/s²⁹.
Ordinary or character coefficient domination does not imply folded TP2.
Sourcewise nonnegative exterior transfer fails at an actual root edge.
P_Q plus ordinary bounds does NOT generically imply K_X or K_t TP2:
an exact OFF-FRICKE auxiliary witness is in prior gate_audit.md.
It is NOT a P_Q child-closure counterexample. No actual target failure known.

## Standard for this round

Aim for an actual elimination of a remaining child gate, or a new explicit
common predicate with a proved additional closure obligation, or an exact
counterexample that decisively rules out a stated implication. Do not
silently strengthen hypotheses or assert Fricke completion is impossible.
State precise support/central/terminal cases and expose each unproved gate.
Each lane must deliver a concise theorem/obstacle note and exact reproducer
if computational evidence is used. Independent audits come before promotion.
