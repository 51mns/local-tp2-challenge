# Frozen paired-algebra candidates (before computation)

This lane uses exact canonical states only. The following proposed auxiliary
predicate is frozen before its diagnostic scan. It is not asserted to imply
the target or to be closed.

For degree-oriented endpoints X,Y and center C, put G=C-Y and H=C-X.
Let T_F=Phi(F(s)F(z)) and J(F,K)=Phi(F(s)K(z)+K(s)F(z)).

**P_in:** T_G, T_H, and J(G,H) have nonnegative SU(2) x SU(2)
character coefficients. G and H are the two actual incoming gaps. Their
degrees agree; this avoids, but does not by itself resolve, the proved
mixed-support obstruction for gaps of different degrees.

The intended use is to retain the close, correlated incoming pair rather
than demand positivity of J(S,S+D), which can fail by the degree-support
lemma. ROOT, SHORT, LONG, and IMPLIES TARGET obligations remain separate.
The scan will check every coefficient through an explicit finite depth
and save the first exact obstruction, if any.

The algebraic identities under investigation, fixed before diagnostics,
are the symmetric-pair formula with c=3(x+1)C-x and b=(x+1)C:

    S=cX-Y-b, Q=cY-X-b, D=Q-S=(c+1)(Y-X),
    R(S,Q)=(T_c-1)R(X,Y)+(T_X-T_Y)D_c-R(b,D),

where D_c=R(1,c). This is a complete signed combination. No positive
claim will be made by splitting its displayed terms.

All source directories above this directory are read-only for this lane.
Shared imports: tp2_source.py and recovery_fulltree_bivariate_character.py.

## Proxy transfer candidate, frozen before computation

Adopt the common-reduction proxy with p=x+2, Q=S-G, U=XpM.
Define V=pX+p²C. Algebra gives U=pQ+V exactly, so the complete proxy
character polynomial is Psi=T_Q+R(Q,V).

For a short child put A=t-2, L=3yXp and F=S. Its pair has
Q'=Q+AF, U'=U+LF. Freeze the proposed **proxy flux inequality**

    Delta_short=R(Q,LF)+R(AF,U)+T_F R(A,L) >=char 0.

This is stronger than child proxy positivity because
Psi'=Psi+Delta_short. No individual summand is claimed nonnegative.
In particular, at X=1 the small block R(A,L) already has a negative
central coefficient. For the long child use A=t_Y-2, L=3yYp,
F=S+D, c=M-1, H=Ec and K=pE(c+1). Its pair is

    Q'=Q+AF+H, U'=U+LF+K.

Freeze its complete flux as

    Delta_long=R(Q,LF)+R(AF,U)+T_F R(A,L)
              +R(Q,K)+R(H,U)+R(AF,K)+R(H,LF)+R(H,K).

The intended test is full character positivity, not solely adjacent
boundary positivity. The formulas combine the paired updates before
extracting coefficients; they do not assume independent positive
parameters or treat the negative small-block coefficient as fatal.
