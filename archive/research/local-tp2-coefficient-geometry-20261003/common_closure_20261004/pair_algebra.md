# Paired exterior transport and the exact proxy cancellation gate

Status: universal algebra proved; root calculations exact; BOTH-child
positivity and global common closure remain OPEN. The diagnostics below
are bounded evidence. No new path-family theorem is claimed.

## 1. Definitions and a symmetric outgoing-pair identity

Use degree-oriented endpoints X,Y and center C, y=x+1, p=x+2,
t=3yX-x, c=3yC-x=M-1, E=Y-X, G=C-Y. For any two
polynomials write

    R(F,H)=Phi((F(s)H(z)-H(s)F(z))/(z-s)),
    T_F=Phi(F(s)F(z)), D_F=R(1,F),
    J(F,H)=Phi(F(s)H(z)+H(s)F(z)).

Phi is the symmetric-polynomial homomorphism s+z -> UV,
sz -> U²+V²-4. Character coefficients are taken in
chi_i(U)chi_j(V). Shared foundations are the exact character formula
and folded-cone equivalence in `../recovery_fulltree_bivariate_character.md`.
In particular [chi_(2n)(U)chi_0(V)]R(F,H)=W_n(F,H).
No ordinary coefficient statement is substituted for character positivity.

Put b=yC. The two outgoing gaps are exactly

    S=cX-Y-b, Z=cY-X-b, D=Z-S=(c+1)E.

The complete signed target bundle is

    R(S,D)=R(S,Z)
          =(T_c-1)R(X,Y)+(T_X-T_Y)D_c-R(b,D).             (1)

Proof: set A=cX-Y and B=cY-X. Bilinearity gives
R(A-b,B-b)=R(A,B)+R(b,A-B)=R(A,B)-R(b,D).
The four terms of R(cX-Y,cY-X) are respectively
T_c R(X,Y), T_X D_c, -T_Y D_c, and -R(X,Y).
This proves (1) for all polynomials, before imposing Fricke.

Both child targets have precisely the same bundle. At the short child
replace (X,Y,C) by (X,C,C+S); at the long child replace it by
(Y,C,C+Z). Thus c becomes c+3yS or c+3yZ and b becomes
b+yS or b+yZ. Formula (1) retains the canonical pairing; its separate
signed terms are not asserted to be nonnegative.

## 2. A smaller proxy pair, with all elementary shifts cancelled

The common-reduction proxy is Q=S-G and U=XpM. Direct algebra gives

    Q=(t-2)C-xX=3yXC-pC-xX,
    V=pX+p²C,
    U=pQ+V.                                                (2)

Indeed pQ+pX+p²C=3ypXC+p(1-x)X=XpM.
Since R(Q,pQ)=T_Q (p has divided difference one),

    Psi:=R(Q,U)=T_Q+R(Q,V).                                (3)

At every folded index, including n=0 by reflection, this is

    W_n(Q,U)=delta_n(H(Q))+W_n(Q,V).                       (4)

The canonical correction V is one correlated polynomial; (3) does not
require its mixed contribution to have either sign. At the root,

    H(Q)=(33,27,14,4), H(U)=(228,188,104,36,6),
    delta(Q)=(93,179,72,16),
    W(Q,V)=(-45,-3,16,8), W(Q,U)=(48,176,88,24).

This proves strict root proxy LR on its full support. Positivity of all
ordered root minors follows by transitivity of the four adjacent ratios
and the positive terminal row. It proves character positivity of Psi.

## 3. BOTH-child paired transport

For the short child set

    A=t-2, L=3yXp, F=S.

The exact pair updates are

    Q'=Q+AF, V'=V+p²F, U'=U+LF.                           (5)

The Q formula follows from Q'=(t-2)(C+S)-xX. Equation (2)
then gives U'=U+p(A+p)F=U+LF.
Bilinearity and common-product transport R(AF,LF)=T_F R(A,L)
give the exact exterior forcing

    Psi'_short=Psi+Delta_short,
    Delta_short=R(Q,LF)+R(AF,U)+T_F R(A,L).                (6)

For the long child put tau=3yY-x=t+3yE, A=tau-2,
L=3yYp, F=Z=S+D, H=Ec and K=pE(c+1)=pD. Then

    Q'=Q+AF+H, V'=V+p²F+pE, U'=U+LF+K.                  (7)

To verify the first update, write
Q'=(tau-2)(C+F)-xY and use
(tau-t)C-x(Y-X)=E(3yC-x)=Ec. Equations (2) and (7)
give the last update because pH+pE=K. Its full exterior forcing is

    Psi'_long=Psi+Delta_long,
    Delta_long=R(Q,LF)+R(AF,U)+T_F R(A,L)
               +R(Q,K)+R(H,U)+R(AF,K)+R(H,LF)+R(H,K).     (8)

All expressions in (6) and (8) refer to one actual canonical parent.
No independent parameters or additional path family have been introduced.

The exact remaining proposed inequality is Delta_short,Delta_long >=char0.
Together with root proxy positivity it would propagate the proxy gate.
It is stronger than merely nonnegative adjacent proxy increments.
Neither (6) nor (8) is a proof of that inequality. In particular, the
current regular LR assumptions and actual child cones have not been
shown in this lane to dominate all their signed cross terms.

## 4. The genuine small-block obstruction, and its compact form

For either endpoint X in a same-endpoint transfer,

    A=3yX-p, L=3yXp,
    R(A,L)=3(3T_(yX)-T_p D_(yX)).                         (9)

Proof: L=pA+p², so R(A,L)=T_A+R(A,p²).
Expand T_A=9T_(yX)-3J(yX,p)+T_p and
R(A,p²)=3R(yX,p²)-R(p,p²), with R(p,p²)=T_p.
Finally J(F,p)-R(F,p²)=T_p D_F: its ordinary two-variable
numerator is p(s)p(z)(F(z)-F(s)). This proves (9).

The canonical endpoint X=1 gives adjacent coefficients (-15,6) for
R(A,L); X=p, occurring at the first actual long child, gives (-6,21,9).
Thus termwise positivity in the quadratic F contribution of (6)/(8)
fails on genuine canonical states. These are not target counterexamples.
For X=1, even multiplying both members by y gives (30,-12,6),
and multiplying both by y² gives (-54,60,-3,6). A blanket repair by
one or two common y factors is also false at the actual boundary endpoint.

For h=H(yX), (9) has the sharper adjacent formulas

    W_0(A,L)=9delta_0(h)-6(h_1+h_2),
    W_1(A,L)=9delta_1(h)-3(h_1+2h_2+h_3),
    W_n(A,L)=9delta_n(h)  (n>=2).                         (10)

This follows because T_p=chi_2(U)+chi_2(V)+2chi_1(U)chi_1(V)+2,
while D_(yX)=sum_(j>=1)h_j chi_(j-1)(U)chi_(j-1)(V).
Only j=1,2,3 can contribute to the trivial V character.
The quantitative lane independently checked (10). If h is
nonincreasing and lambda-strong with lambda>4/3, (10) proves strict
supported trace-block LR. This is a genuine single-endpoint sufficient
condition, not a target restatement. It still does not control the
remaining signed mixed terms of (6)/(8).

## 5. Frozen predicates and exact finite evidence

The earlier frozen auxiliary predicate P_in requires character
nonnegativity of T_G,T_(C-X),J(G,C-X). Incoming gaps have the same
degree, unlike the previously refuted unequal-support mixed package.
At the root its two defect rows are (13,7,4) and (8,16,4);
the doubled mixed boundary is (22,22,8). Its complete character
array is

    (0,0):22, (0,2):22, (0,4):8, (1,1):38, (1,3):22,
    (2,0):22, (2,2):30, (3,1):22, (4,0):8.

All coefficients are positive. The executable independently reproduces it.

| Candidate | ROOT | SHORT closure | LONG closure | Implies target |
| --- | --- | --- | --- | --- |
| P_in | exact pass | OPEN | OPEN | OPEN |
| root proxy plus BOTH nonnegative fluxes | exact root proxy | sign of (6) OPEN | sign of (8) OPEN | supplies proxy gate only |
| endpoint bound (9)>=char0 | fails at X=1,p; conditional (10) proved | not closed | not closed | supplies one transfer block only |

`pair_probe.py 5 24` checks 63 canonical states through binary depth 5
and 48 records on the already existing named L/R rays through length 24.
All characters of P_in, T_M, Psi and both complete fluxes were
nonnegative in these 111 records. The root and first-child exterior
expansions were also reproduced by Clebsch-Gordan products, independently
of subtracting the complete child and parent proxy arrays. The universal
proofs of (1)-(9) are the algebra above, not this bounded scan.

Reproducer and data: `pair_probe.py`, `pair_results.json`.
The shared imports are `../tp2_source.py` and
`../recovery_fulltree_bivariate_character.py`; earlier files were not edited.
There is no claim of full-tree Local TP2 or of a closed common predicate.
