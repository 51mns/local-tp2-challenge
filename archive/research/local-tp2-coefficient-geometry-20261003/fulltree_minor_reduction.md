# Direct child-pair recurrences and the missing canonical correlation

**Status:** exact all-tree algebra and an abstract obstruction. The
identities below incorporate the actual Fricke equation into the gap
recurrence. They do not yet give a positive recurrence for every Local
TP2 minor. The obstruction is not a canonical counterexample.

Write `H(P)[n]=[q^n]P(q+q^-1)`, y=x+1, and sort the current
endpoints as X,Y with degree(X)<degree(Y). Let C be the center,
U,V its short and long children, and set

`E=Y-X`, `G=C-Y`, `M=3yC-x+1`,

`S=U-C`, `D=V-U=EM`, `Q=S+D=V-C`,

`t_X=3yX-x`, `t_Y=3yY-x`.

All identities are checked exactly as multivariate polynomial
identities by `fulltree_minor_reduction.py`. The symbolic checks do
not enumerate tree depths.

## 1. Both new actual pairs in parent variables

At the child centered at U, the endpoints are X,C. Its actual short
gap and child difference, denoted S_X,D_X, are

`S_X=t_X S-G`,

`D_X=(G+E)(M+3yS)`.

At the child centered at V, the endpoints are Y,C. The corresponding
pair is

`S_Y=t_Y Q-(G+E)`,

`D_Y=G(M+3yQ)`.

Both orientations follow from the established degree separation of
the center from its endpoints. These formulas follow directly by
performing both new mutations, not by selecting an arbitrary pair of
positive polynomials.

The sums simplify further:

`S_X+D_X=(M-1)(S+G)+D`,

`S_Y+D_Y=(M-1)(S+D+G)-E`.

The identities `t_X=M-1-3y(G+E)` and `t_Y=M-1-3yG` give these
forms directly.

For any antisymmetric bilinear coefficient minor W, the first child
therefore has the exact polarization

`W(S_X,D_X)=W(t_X S,(G+E)M)`

` +3W(t_X S,y(G+E)S)-W(G,(G+E)M)`

` -3W(G,y(G+E)S)`.

The second child has the analogous formula

`W(S_Y,D_Y)=W(t_Y Q,GM)+3W(t_Y Q,yGQ)`

` -W(G+E,GM)-3W(G+E,yGQ)`.

These expressions identify the new comparisons that a direct induction
must control. They contain negative terms; positivity of the parent
minor W(S,D) alone does not remove them.

## 2. Fricke becomes an exact Cassini constraint on adjacent gaps

Define the Fricke residual

`R=X^2+Y^2+C^2+x(XY+XC+YC)-3yXYC`.

It vanishes on every canonical state. Define

`K_X=yX^2(3X+x-2)`, `K_Y=yY^2(3Y+x-2)`.

The preceding fixed-X gap is

`q_prev=C-(t_X-1)Y+xX=t_XG-S`.

For a nonroot state, the inverse neighbor is
`T=t_XY-xX-C`, so q_prev=Y-T is the actual preceding
center-endpoint gap. At the root q_prev=y, agreeing with the same
formula.

Before imposing the Fricke equation, direct expansion gives

`G^2-q_prev S-K_X=-(t_X-2)R`.

Thus every canonical state satisfies the Cassini identity

`G^2+S^2-t_XGS=K_X`.

Equivalently, the short-child gap recurrence has the multiplicative
form

`G S_X=S^2-K_X`.

For the other endpoint the symmetric identity is

`(G+E)S_Y=(S+D)^2-K_Y`.

The executable verifies the stronger residual versions

`G S_X-S^2+K_X=(t_X-2)R`,

`(G+E)S_Y-(S+D)^2+K_Y=(t_Y-2)R`.

These exhibit exactly where the canonical equation enters: the
error is an explicit multiple of its residual. They are stronger
correlations than coefficientwise positivity or a generic cone
assumption on the individual gaps.

The right sides K_X,K_Y have nonnegative character coefficients,
because

`3X+x-2=3(X-1)+y`

and every endpoint satisfies X>=_B1. This fact does not make the
subtraction in `S^2-K_X` a cone-preserving operation. Nor can one
cancel the factor G from an LR comparison after multiplication without
an additional argument. The Cassini identities are a possible input
to such an argument, not its completion.

## 3. A strong parent-pair package still does not close under summing

There is a useful exact obstruction to a proposed induction through
the long gap S+D. Set

`S=(x+1)(x^2+50x+100)`,

`D=S+2(x+1)(x+2)^3`.

Their ordinary coefficient arrays are

`S=(100,150,51,1)`, `D=(116,190,87,15,2)`.

The relevant rows are

| Polynomial | Half-row | Character row |
| --- | --- | --- |
| S | `(202,153,51,1)` | `(49,102,50,1)` |
| D | `(302,235,95,15,2)` | `(67,140,80,13,2)` |
| D-S | `(100,82,44,14,2)` | `(18,38,30,12,2)` |

All ordinary and character coefficients are positive, all three
polynomials vanish at x=-1, and D strictly dominates S in the
character basis. All three have optimal leading-coefficient strength:

`delta(S)=(4288,10659,2447,1)>=1 H(S)`,

`delta(D)=(9444,21035,5465,31,4)>=2 H(D)`,

`delta(D-S)=(952,1536,680,104,4)>=2 H(D-S)`.

The original adjacent S,D minors are `(1264,2550,670,2)`, all
strictly positive. Even the stronger first-difference comparison holds:
its adjacent minors are `(26,1160,570,2)`, and the verifier checks
every supported ordered pair directly.

Nevertheless,

`H(S+D)=(504,388,146,16,2)`,

`delta(S+D)=(26512,61852,15144,-40,4)`.

Thus the long-gap sum fails folded TP2. Common multiplication of the
entire example by any positive integer preserves positivity,
divisibility, optimal leading strength, both LR comparisons, and the
negative sum defect, giving an infinite family of the same obstruction.

This pair is explicitly **not canonical**. Its short-gap degree is
three; the only canonical state with that degree is the root, whose
actual S,D pair is different. The example does not refute Local TP2
on the tree. It shows that even parent Local TP2, stronger
first-difference order, optimal individual kernel strength, and a
positive cone difference D-S do not justify passing to the long-gap
kernel. The genuine Fricke/Cassini correlations must be used if this
route is pursued.

## 4. Audit of the new canonical strip

The independent proof in `fulltree_structural_strip.md` passes review.
Its strengthened additive separation follows from the exact positive
decomposition

`U-y(A+C)=y(C-2)+y(A-1)(3C-2)+A+(C-B)`.

The established support invariant makes each term nonnegative and
supplies strictness throughout the new support. Every endpoint T
satisfies alpha_T(1)>=alpha_T(0)-1, so `1+xT>=_B0`, including the
exceptional endpoint T=1.

At a nonroot state the larger endpoint Y is the preceding center.
Writing its replaced endpoint as T gives

`C=(t_X-1)Y+rho`,

`rho=[Y-y(X+T)]+X+xT`, `Y-rho=T+xX`.

These prove `0<_B rho<=_B Y`; the degree statement follows from the
preceding canonical degree sum. At the root rho=1 directly. Hence
the strip is a valid global canonical constraint. It is still a linear
coefficient statement, and does not by itself determine the quadratic
folded defects in Sections 1--3.

## Current gap

No positive all-index recurrence for the actual child S,D minors has
yet been obtained. The new exact gap recurrences and residual-controlled
Cassini identities isolate canonical information absent from the
refuted generic induction packages. A proof must convert that
information into signed-cancellation or quantitative control of the
new polarized minors; it cannot rely only on positive-sum closure.
