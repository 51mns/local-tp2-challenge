# Quantitative common gates: proved reductions and failed sufficient predicates

**Status: conditional general lemmas and exact actual-state obstructions. No
common left/right closure theorem, or full-tree Local TP2 theorem, is proved.**

All paths below use `s/l` for degree-ordered short/long children. Original
`L^j` is `s^j`; original `R^j` is `l s^(j-1)`. Both labels matter when
classifying a failed common predicate.

## 1. Frozen predicates and closure status

Let `lc` mean the ordinary leading coefficient. The frozen leading-scale
candidate is

`A: delta_n(H(C)) >= lc(C) H(C)_n`,

`delta_n(H(yC)) >= lc(C) H(yC)_n/2`.

For the actual incoming gap `G=C-Y=yg`, the separate candidate is

`D: delta_n(H(G)) >= lc(G) H(G)_n/2`;

the stronger nonroot variant uses `lc(G)` instead. These are quantitative
kernel predicates, not the desired outgoing LR comparison.

| Candidate | ROOT | degree-ordered SHORT CHILD | degree-ordered LONG CHILD | IMPLIES TARGET |
|---|---|---|---|---|
| A | proved: rows `(9,6,2)`, `(21,17,8,2)` | missing proof | missing proof | supplies center/trace hypotheses only; separate actual gap and proxy gates remain |
| D | proved: `H(G)=(7,5,2)`, defects `(13,7,4)`; half-leading strength is 1 | missing proof | missing proof | folded G alone is insufficient; use the separate reduction lane's LR/proxy package |
| fixed remainder reserve `1/32`, Section 4 | proved for the center | **false** at actual `L^28` smoothed and `L^29` raw | missing proof | no |
| reference-band scalar gate, Section 2 | proved for `(s,r)` and `(ys,yr)` | **false** at actual `L^6` smoothed, `L^7` raw; also `R^7` smoothed and `R^8` raw | missing proof | proves relative kernel minors when it holds; does not establish the separate target |

The bounded falsification lane reports A and D passing its stated finite
scope. This is not an induction proof. In particular, the full-leading
version of D is already false at the root, since `7<2*5` at index 1.
The original R-ray failures above also occur on degree-ordered short
moves after its first long move. They must not be described as
counterexamples to long-child preservation.

## 2. A valid reference-band all-minor theorem

Let `h` have finite positive interval support and a TP2 folded kernel. Let
`b` be nonnegative of degree `d`, with `b_n<=b_0`, and suppose `deg h>=d`.
Extend h symmetrically and by zero. Define

`L_d(h)=min_(0<=a<=d) {delta_a(h)/h_a,`

`                       (delta_a+delta_(a+1)+delta_(a+2))/(h_a+h_(a+2))}`.

If `h>=alpha b` coefficientwise, `alpha>=2`, and

`alpha L_d(h)>=8b_0`,

then **every ordered folded minor satisfies `det K_h>=4 det K_b`**.

Here the normalized constant ignores remote terminal defects; it is at
least the simpler truncated strength
`min_(0<=n<=d+1) delta_n(h)/h_n` whenever `deg h>=d+1`.

**Proof, including boundaries.** Folded TP2 makes h decreasing and every
defect nonnegative. For an adjacent cell with row/column indices positive,
transpose if needed and put `a=|i-j|`, `b'=i+j>=a+2`. The audited folded
minor formula gives

`M >= Delta_a-Delta_(b'+1) = sum_(k=a)^b' delta_k`.

Its additional cross term is nonnegative. If `h_(b'+1)=0`, the expanded
cross term is `h_a(h_b'+h_(b'+2))>=0`; hence this lower bound also holds
at the support boundary. If `a<=d`, monotonicity of h and nonnegativity
of delta give

`M/(h_a+h_b') >= (delta_a+delta_(a+1)+delta_(a+2))/(h_a+h_(a+2))`

`>=L_d(h)`.

For a row-zero cell the ratio is exactly `delta_a/h_a`; column-zero has
both numerator and diagonal doubled. Thus every adjacent cell whose
diagonal displacement is at most d has `M>=L_d(h) K_h(i,j)`.

Take any ordered minor for which the b minor is positive. Its diagonal
entries are positive, so the corresponding h diagonals are positive and
their displacements are at most d. If an h off-diagonal is zero, the
minor is its diagonal product and coefficient domination gives

`det K_h >= alpha^2 K_b(i,k)K_b(j,l)>=4 det K_b`.

Otherwise the entire h rectangle is positive. The usual adjacent
cross-ratio product telescopes. Retaining its bottom-right cell, whose
diagonal displacement is `|j-l|<=d`, proves

`det K_h >= L_d(h) K_h(i,k)`.

Now `K_h(i,k)>=alpha K_b(i,k)` and `K_b(j,l)<=2b_0`. Hence

`det K_h >=8b_0 K_b(i,k)>=4 K_b(i,k)K_b(j,l)>=4 det K_b`.

A nonpositive b minor is covered by TP2 of h. No bound on the kernel
indices is needed. This is a theorem about a sufficient criterion, not
an assertion that the criterion is canonical-mutation invariant.

**Actual obstructions.** At `s^6`, in smoothed mode, exact optimal
constants for this gate are

`alpha=2508664/60121`, `L_d=2332480/329`,

`alpha L_d-8b_0=-3662046568392/19779809<0`.

At `s^7`, raw mode gives

`alpha=1923199/46177`, `L_d=169472/11`,

`alpha L_d-8b_0=-237002865928/507947<0`.

Thus merely removing the terminal-strength bottleneck does not repair
the central-mass loss in the old scalar relative-minor bound. These are
failures of the sufficient predicate, not failures of direct relative
minor domination. The falsification lane's direct minor checks retain
that distinction.

## 3. A strict trace-base lemma for interior endpoint strata

Put `P1=x+2`, `h=H(yX)`,

`A=3yX-P1=t-2`, `L=3yXP1`.

If h has positive interval support of degree at least one and is
lambda-strong with `lambda>4/3`, then the two Fourier rows `(A,L)` have
strict adjacent LR minors throughout the support of A, and consequently
all their ordered LR minors are nonnegative. The exact formulas are

`w_0=9delta_0(h)-6(h_1+h_2)`,

`w_1=9delta_1(h)-3(h_1+2h_2+h_3)`,

`w_n=9delta_n(h)`, `n>=2`.

Indeed `L=P1(A+P1)`, so
`W(A,L)=9W(h,P1h)-3W(P1,P1h)`, and `W(h,P1h)=delta(h)`.
The only nonzero entries of the latter fixed correction are the two
displayed low-index expressions. Since h decreases,

`w_0>=(9lambda-12)h_0>0`,

`w_1>=(9lambda-12)h_1>0`.

All later supported indices are strict, including the terminal one.
Strength also gives every supported h entry at least lambda, so A has
positive interval support and L has exactly one extra terminal entry.
This proves the all-ordered LR extension by ratio transitivity. Zero
extension makes the same formulas valid in degrees one and two.

This lemma is **not universal over all canonical endpoints**:
`X=1` has central base minor -15 and `X=P1` has -6. For the first center
`X=2x^2+6x+5`, the actual row h is `(21,17,8,2)` and the base central
minor is 129. Its strength is `31/21>4/3`. Every later canonical center
has leading coefficient at least 4; hence candidate A, if closed, gives
lambda at least 2 for those endpoints. Existing boundary-ray theorems
may cover `X=1,P1`; this note proves no new ray theorem.

## 4. Exact retained remainder and why a fixed reserve also fails

For the actual canonical center write `F=t_X Y`, `Gcorr=F-C`, with
`f=H(F), g=H(Gcorr), c=f-g`. For either raw or smoothed mode the audited
identity is

`delta_n(c)-lambda c_n=B_n+R_n`,

`R_n=g_n(f_n-f_(n+2))+g_(n-1)f_(n+1)`
`    +c_(n-1)g_(n+1)+g_(n+1)(f_(n+1)+c_(n+1))>=0`.

The frozen attempted reserve was

`delta_n(c)-lc(C)c_n>=R_n/32` (raw),

`delta_n(c)-lc(C)c_n/2>=R_n/32` (smoothed).

It is stronger than A and retains 31/32 of the favorable exact remainder
inside its sufficient bound. It still fails on actual canonical states.
The first failures along the tested pure-short ray are `s^28` smoothed
and `s^29` raw, both at index zero. The falsification lane records full
polynomials/rows and an independent B+R identity cross-check. The
standalone reproducer here independently obtains the same first depths.
No statement about every positive reserve fraction is inferred from
these two finite witnesses.

At the known original `R^13` obstruction, the raw optimal-strength
surplus is

`123114021891610995185594953863037604893`,

while the actual remainder is

`136369427728705566915805938015739962789`.

The coarse bound is negative, but the 1/32 reserve is positive there.
Thus checking only R13 would have missed the longer pure-short failure.
The exact Fricke and Cassini correlations are checked without division
by the reproducer; they do not supply a proof of the needed coefficient
inequality by themselves.

For the actual short gap `S=tG-Rincoming`, the same subtraction lemma
applies whenever its shape hypotheses hold. Since the correction is
shorter, its first out-of-support boundary is favorable:

`delta_(degR+1)(S)=delta_(degR+1)(tG)+H(R)_degR H(tG)_(degR+2)`.

All later defects inherit the dominant product. The missing signed
comparisons are therefore at indices `0,...,degR`, rather than at an
unbounded unsupported tail.

## 5. Direct proxy absorption with actual signed corrections

The exact interior-state proxy is

`Q=S-G=A C-p`, `U=XP1 M=L C-v`,

`p=xX`, `v=(x-1)P1X`.

The row of `(x-1)P1=x^2+x-2` is `(0,1,1)`, so v is Laurent
nonnegative. The two-row pair `(H(x),H((x-1)P1))` has only one nonzero
ordered minor, equal to 1. If `K_X` is TP2, convolution gives
`W_n(p,v)>=0` at every n. Consequently, with `F=AC` and `H=LC`,

`W_n(Q,U)=W_n(F,H)-F_n v_(n+1)+F_(n+1)v_n`
`         -p_n H_(n+1)+p_(n+1)H_n+W_n(p,v)`.

This is an exact correlated identity; three terms are favorable. Let
`d_A=deg A`, assume the strict trace-base lemma, strict supported folded
defects of C, and `K_X` TP2. Define the finite state-dependent threshold

`beta_X=max_(0<=n<=d_A) [A(2)v_(n+1)+p_n L(2)]/w_n`.

Then

`delta_0(C)>beta_X C(2)`

implies the strict proxy `Q<lr U` at every supported comparison index.
For `n<=d_A`, retain the principal intermediate pair `(n,n+1)` in
Cauchy--Binet to obtain `W_n(F,H)>=w_n delta_0(C)`. Also
`F_n<=A(2)C(2)` and `H_(n+1)<=L(2)C(2)`, giving precisely the displayed
threshold. At `n=d_A+1`, p vanishes, v has its last coefficient and
`v_(n+1)=0`; every remaining correction is favorable. After that all
corrections vanish. Retaining the positive terminal fixed minor
`(d_A,d_A+1)` and a strict adjacent kernel minor of C covers all those
indices, including the terminal support of Q. No multiplication-by-y
cone assertion is used.

There is also a simple scalar upper bound. Laurent coefficientwise,
`p=xX<=yX` and

`y^2X-v=(x+3)X>=0`.

Thus `p_n<=h_n` and `v_(n+1)<=h_n+h_(n+1)+h_(n+2)<=3h_n`.
All the base minors satisfy `w_n>=(9lambda-12)h_n`, so

`beta_X <= (3A(2)+L(2))/(9lambda-12)`

`       = (63X(2)-12)/(9lambda-12)`.

This gives a completely explicit state-dependent mass premise. It is
not implied by the leading-scale predicate A, and its mutation transport
remains an additional obligation.

This is a completed general sufficient reduction for interior strata.
**The remaining common-closure obligations are candidate A, the actual
short/long gap cones, and this mass gate at each child.** No canonical
coefficient bound for beta_X or its child transport is claimed.

## 6. The long-child support boundary has an inexpensive conditional bound

At every nonroot canonical state, `lc(Y)>=2lc(X)`. Indeed the larger
endpoint at either child is its parent's center, whose leading
coefficient is `(2 if X=1 else 3lc(X))*lc(Y)` and is at least twice
either retained endpoint's leading coefficient. Root is the sole
endpoint pair with leading coefficients `(1,1)`.

Since

`lc(S)=(2 if X=1 else3lc(X))*lc(C)`,

`lc(D)=3lc(Y)lc(C)`,

we have `lc(D)/2>=lc(S)` at every nonroot state. If D is
`lc(D)/2`-strong, it is strictly decreasing. With `d_S=deg S`, the
exact mixed support boundary is

`delta_(d_S+1)(S+D)=delta_(d_S+1)(D)-lc(S)H(D)_(d_S+2)>0`.

The last inequality follows from the leading-coefficient inequality and
strict decrease (zero extension includes a terminal D index). For
`n>=d_S+2`, the sum inherits D's defects exactly. Thus only
`0,...,d_S` and the explicit root base need further correction control
to prove the long-child cone under this conditional strength premise.

If the goal is instead half-leading strength of the sum, assume D is
full-leading strong. Subtracting `lc(D)H(S+D)/2` gives the same positive
boundary argument and a nonnegative tail margin. This does not decide
the low indices.

## 7. Verification and dependencies

`quantitative_bandwidth.py` is standalone Python integer/Fraction code;
it imports **no parent arithmetic**. It reconstructs the normalized
state, verifies both child identities, the exact Fricke and Cassini
relations, all trace-base formulas, both proxy polynomial identities,
and the subtraction remainder identity at every supported index in its
stated finite scope. The saved result is explicitly a diagnostic: 63
states through depth 5 and targeted `s^3,...,s^40` plus original R13.
Its six frozen witness records save the complete normalized polynomial
state and relevant Fourier rows for `L^6,L^7,R^7,R^8,L^28,L^29`.

The infinite lemmas use the audited folded-kernel equivalence, adjacent
minor formula, Cauchy--Binet convolution, and cross-ratio telescoping
from `mixed_kernel_strong_cone.md` and
`mixed_kernel_all_minor_strength.md`. The subtraction identity is from
`fulltree_20261004/quantitative_subtraction.md`; its algebra was separately
audited there. No same-path strength or central-mass estimate is imported
as an arbitrary-tree premise.

For the canonical reference pair `(s,r)` the coefficient-domination
hypothesis itself is unconditional: `r<=a+e` and
`g>=a+e+r+1` imply `g>=2r+1`, while `t>=3` gives
`s=tg-r>=5r+3` in ordinary coefficients. Hence `H(s)>=5H(r)` and
`H(ys)>=5H(yr)`. The failed reference-band gate concerns its quantitative
defect threshold, not this positive coefficient domination.

The independent `common_gate_audit` lane reviewed Sections 2, 3, 5, and 6,
including the beta upper bound, and reported PASS for these **conditional
general lemmas**. Its review also confirms a compatibility limitation:
the reduction lane's basic P_Q package does not by itself imply K_X TP2
or the trace-base strength hypothesis on arbitrary abstract states. Those
are explicit additional premises here. A proved ancestral all-center
strength induction could supply them on the canonical interior strata;
that induction remains open. The review does not promote the false
scalar applications or establish a common mutation invariant.
