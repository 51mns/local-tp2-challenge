# Independent audit of the L²R^k mass margins and fixed proxy

**Verdict: PASS** for both whole-interval mass certificates and all
fixed proxy rows, minors, and remainder signs in
`general_one_turn_m2.md`.

The verifier `general_one_turn_m2_independent.py` imports none of the
author's arithmetic modules. It independently constructs the inner
Chebyshev recurrence twice: with ordinary integer x-polynomials and
with direct Laurent polynomials after substituting `x=q+q^-1`.
It derives P,a,b,t from those recurrences and verifies that both
representations agree. Thus the fixed coefficient arrays are derived
from the canonical definitions, not merely copied into a row-minor
calculation.

All exact results are saved in
`general_one_turn_m2_independent_results.json`.

## Derived seeds

Using `z=2x+3`, inner `u_0=1,u_1=z`, and
`u_(j+1)=zu_j-u_(j-1)`, the two constructions give

`P=1+y(u_0+u_1+u_2)=13+26x+18x²+4x³`,

`a=u_0+u_1+u_2+u_3=33+64x+40x²+8x³`,

`b=u_0+u_1=4+2x`,

`t=3yP-x=39+116x+132x²+66x³+12x⁴`.

Their required evaluations are independently verified:

`t(2)=1519`, `a(2)=385`, `b(2)=8`.

## The two continuous mass certificates

Put `r=2-4u`, `0<=u<=1`, and `f=t-r`.
The independent Laurent construction extracts the central defect and
evaluates total mass by q=1. It reproduces these exact power polynomials:

`delta_0(f)-4f(2)=3009+3688u+16u²`,

`delta_0(af+b)-800(af+b)(2)`

`=9999933+9224984u+28816u²`.

Their full degree-two Bernstein arrays are respectively

`(3009,4853,6713)`,

`(9999933,14612425,19253733)`.

Every power coefficient, Bernstein coefficient, degree, and lower
bound agrees with `general_one_turn_m2_margin_certificates.json`.
The checked source artifact has SHA-256

`5c810a097a5e76b1dcf01fa5032dfad41656b390e701a7b8d73588dab34069b9`.

Both margins are strictly positive on the entire real interval; no
root sampling or bound on the outer index k occurs in this check.

The manuscript's mass evaluations are also consistent with its
resolvent summands:

`Z_i(2)/T_k(2)=385+8/(1519-r_i)` lies in `(385,386)`.

Consequently the comparison `Z_i(2)>Z_k(2)/2` follows from positive
weights of total one. Keeping the squared weights, the stated bound
`delta_0(Z_k)>400*4^(k-1) Z_k(2)/k` is valid once the separately
audited compatibility theorem is applied. Its lower bound 400 holds
for every k>=1 because `4^(k-1)>=k`, including k=1.

## Fixed proxy arithmetic

To avoid confusing the manuscript's B with its y multiple, write

`F=y(t-2)`, `G=3y²P(x+2)`, `K=2P(x+2)²`.

The independent ordinary and Laurent calculations both give

`H(F)=(1001,867,560,258,78,12)`,

`H(G)=(3750,3306,2250,1155,426,102,12)`,

`H(K)=(1268,1076,650,268,68,8)`.

The six supported adjacent comparison minors are exactly

`(58056,99390,66300,19818,2844,144)`.

They are strictly positive, and `F(2)=4551`.
For the chosen central-defect margin factor 256, direct integer
arithmetic gives

`256 M_n(F,G)-4551 H(K)[n]`

`=(9091668,20546964,14014650,3853740,418596,456)`.

Every entry is positive. In particular, the smallest terminal
remainder is exactly `256*144-4551*8=456`; there is no sign or indexing
error at the last nonzero coefficient of K.

The remainder estimate used with these numbers is valid because F,Z,K
have nonnegative Laurent coefficients:

`M_n(FZ,K)>=-H(FZ)[n+1]H(K)[n]`

`>=-F(2)Z(2)H(K)[n]`.

Since K has degree five, its contribution vanishes for every n>=6.
Thus the six checked remainder margins cover all indices affected by
the added polynomial. The infinite upper-index argument still uses
the strict folded-kernel theorem, not a finite numerical extrapolation.

## Scope

This audit independently verifies the requested continuous mass
certificates and the complete fixed proxy arithmetic. Their role in
the final L²R^k theorem is consistent with the stated positive-residue
and Cauchy-Binet argument. The separate relative-kernel and full
comparison audits provide the remaining structural dependencies.
