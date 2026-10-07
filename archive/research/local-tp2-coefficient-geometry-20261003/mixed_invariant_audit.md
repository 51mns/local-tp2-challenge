# Independent audit of the mixed-tree invariant routes

The two new Fourier-row reductions below pass independent mathematical
review. They are conditional reductions, not a proof of Local TP2 on the
full tree. The first-difference route has a genuine abstract obstruction:
its multiplier claim does not follow even from the new strong folded
cone. No canonical counterexample was found or is claimed.

## 1. Exact obstruction to a generic first-difference multiplier lemma

For an integer parameter `lambda>=1`, set

`C_lambda=3 lambda x^2+8 lambda x+5 lambda+1`,

`M_lambda=3(x+1)C_lambda+1-x`.

This is an abstract polynomial family. It is **not** a family of
canonical centers. In particular, the only canonical degree-two center
is the root, whereas this family is different from the root.

The exact half-row and first-difference row of C are

`H(C)=(11 lambda+1,8 lambda,3 lambda)`,

`alpha_C=(3 lambda+1,5 lambda,3 lambda)`.

These are positive integer rows, `C(-1)=1`, `alpha_C(0)>=3`, and
`alpha_C(1)>=alpha_C(0)`. The ordinary coefficients are also dense and
positive. The top-two-row adjacent minors of its first-difference
kernel J are

`tau_C=(8 lambda^2+14 lambda+1,7 lambda^2-3 lambda,9 lambda^2)`.

They are strictly positive for every integer `lambda>=1`; the established
J-kernel criterion therefore gives J_C TP2.

The stronger folded conditions also hold. Its folded defects are

`delta_C=(26 lambda^2+25 lambda+1,22 lambda^2-3 lambda,9 lambda^2)`.

Subtracting twice the half-row gives

`delta_C-2H(C)=(26 lambda^2+3 lambda-1,22 lambda^2-19 lambda,9 lambda^2-6 lambda)`,

which is nonnegative for integer `lambda>=1`. Moreover,

`H((x+1)C)=(27 lambda+1,22 lambda+1,11 lambda,3 lambda)`,

`delta_0(H((x+1)C))=58 lambda^2-23 lambda-1>0`.

Thus C belongs to the proposed product-closed class F in
`mixed_kernel_strong_cone.md`. It also satisfies the weaker central
margin `delta_C(0)>=H(C)[0]+H(C)[1]`, since the difference is
`26 lambda^2+6 lambda`.

Nevertheless,

`H(M)=(81 lambda+4,66 lambda+2,33 lambda,9 lambda)`,

and the J_M top adjacent minors are

`(-9 lambda^2+72 lambda+4,450 lambda^2+102 lambda+4,198 lambda^2-18 lambda,81 lambda^2)`.

The first is negative for every integer `lambda>=9`. At `lambda=9`,

| Quantity | Exact row |
| --- | --- |
| C, ordinary coefficients | `(46,72,27)` |
| H(C) | `(100,72,27)` |
| alpha_C | `(28,45,27)` |
| J_C adjacent top minors | `(775,540,729)` |
| M, ordinary coefficients | `(139,353,297,81)` |
| H(M) | `(733,596,297,81)` |
| alpha_M | `(137,299,216,81)` |
| J_M adjacent top minors | `(-77,37372,15876,6561)` |

Therefore positivity, normalization, J_C TP2, and even membership of C
in F do not imply J_M TP2. A proof of the first-difference multiplier
claim needs additional canonical information. This obstruction does not
refute the Fourier-row conditional first-sandwich theorem or canonical
Local TP2.

All displayed parameter identities are checked in the polynomial ring
`Z[lambda]` by `mixed_invariant_audit.py`; they are not inferred from
interpolation or sampled values.

## 2. Audit of the conditional full-tree first sandwich

The proof in `mixed_first_sandwich.md` passes, with precisely its three
stated global center assumptions: K_C TP2, K_(3yC-x) TP2, and
`delta_C(0)>=H(C)[0]+H(C)[1]`.

The exact child-gap decomposition is

`S_A=(A-1)(3yC-x)+(2yC-x-B)`.

The first summand is nonnegative in the character basis. The second is

`(2yC-C-y+1)+(C-B)`.

The globally proved support invariant makes both displayed terms
character-nonnegative and makes the bracket strictly positive throughout
its support. Thus the proof does not use an invalid subtraction closure.

Writing P=x+2 and h=H(C), the independent determinant check gives

`W_n(PC,3yC)=3delta_C(n)`,

`W_n(PC,2yC-x-B)=2delta_C(n)-W_n(PC,x)-W_n(PC,B)`.

The correction `W_n(PC,x)` is `2(h_0+h_1)` at n=0, is negative at
n=1, and is zero above n=1. This verifies the stated central margin,
including its factor of two. Endpoint order `B<=lr C<=lr PC` makes the
B correction favorable. Broadening by the nonzero nonnegative
multiplier A-1 is legitimate under K_(3yC-x) TP2; A=1 contributes the
zero summand and is omitted.

The simultaneous induction is valid. It maintains endpoint order and
both comparisons `PA<=lr C-A`, `PB<=lr C-B`. At a child, the new gap
above the previous center is handled by the child-gap lemma; the
retained-endpoint gap is a sum of two rows above one fixed lower row.
Root minors and finite support were checked explicitly. The degree
orientation then gives `PX<=lr Y-X` at every nonroot node, with the
root verified directly.

This proves the implication without a depth bound. It does not prove
the three center hypotheses, the corresponding first-difference order,
or the second sandwich for Local TP2.

## 3. Audit of quantitative folded-cone closure

All six sections of `mixed_kernel_strong_cone.md` pass independent
mathematical review.

For a lambda-strong row, the quantitative bound on every adjacent
folded-kernel minor follows from the interior minor formula and summing
`delta_k>=lambda h_k`. The diagonal case uses the symmetric h_-1
convention; the top row and first column have the stated factors one
and two. When the reflected index leaves the support, the direct
boundary formula retains the required bound. Thus no missing band-edge
case is hidden in the product argument.

Cauchy--Binet may retain all intermediate adjacent pairs because every
other term is nonnegative. The resulting sum is exactly H(PQ), so the
product strength is the product of the two strengths.

For multiplication by y, the five retained minors are the exact
Cauchy--Binet expansion at every n>=1. The bounds in the interior, at
n=m-1, and the separate formulas at n=m,m+1 are valid. Integrality is
used at the endpoint and must remain in the statement. The n=1
strengthening to `delta_1(H(yP))>=(5/3)H(yP)[1]` is valid for degree
at least two.

The four low-index expansions for `3yP-x` are exact. They prove
2-strength from integer 1-strength plus the single central condition
`delta_0(H(yP))>=0`. Strong folded defects imply strictly decreasing h
by log-concavity and the positive central defect, so the required
positive first differences of H(yP) follow as well.

The product closure of F and the weak saturation observation using y^2
are valid. The root belongs to F. The proof expressly leaves canonical
mutation preservation of F open; the product lemma cannot eliminate
the subtractions in a mutation. Establishing this invariant would
discharge the center assumptions of Section 2, but would still leave
the second Local TP2 comparison unresolved.

## 4. Declared finite stress check

The accompanying verifier checks exactly 130 distinct mixed paths:

- `LR^k` and `RL^k`, `1<=k<=30`;
- `LLR^k` and `RRL^k`, `1<=k<=20`;
- `LRL^k` and `RLR^k`, `1<=k<=12`;
- `(LR)^k` and `(RL)^k`, `2<=k<=4`.

All recurrence arithmetic and comparisons use exact integers. The
largest polynomial degree examined is 232. No violation was found of
positive first differences, J_C/J_M TP2, `alpha_(PX)<=lr alpha_E`,
`alpha_S<=lr alpha_(PXM)`, or the direct `alpha_S<=lr alpha_D`.

The smallest relative positive J_C, J_M, and second-sandwich margins
occur at index zero of `RLRLRLRL`, approximately `4.50e-5`, `4.43e-5`,
and `1.77e-5`, respectively. Exact numerators are retained in
`mixed_invariant_audit_results.json`. The first sandwich has a support
equality at LR, index three. These checks supply bounded evidence only;
they neither establish an infinite invariant nor repair the abstract
multiplier obstruction in Section 1.

## 5. Independent replay of the abstract mutation obstruction

The later construction in `mixed_kernel_closure_obstruction.md` also
passes independent review and exact recomputation using
`tp2_source.py`, separate from its author's arithmetic helper. The
triple is

`A=1`, `B=58x^2+128x+71`,

`C=29x^3+120x^2+122x+32`.

B and C belong to F; their central defects after multiplication by y
are respectively 389 and 718. Normalization at x=-1, dense character
positivity, both center-gap dominance conditions, endpoint order, and
every ordered minor in both center-gap LR comparisons check exactly.

The retained-A mutation has ordinary coefficients
`(25,301,546,327,58)` and central folded defect `-1053`. Thus these
abstract conditions do not guarantee even weak folded TP2 after a
mutation. Its Fricke residual has ordinary coefficients
`(-750,-16731,-56058,-79307,-56137,-19430,-2523)`, so the triple is
not canonical. The negative result concerns the proposed sufficient
closure assumptions; it does not refute canonical F preservation or
canonical Local TP2.

## Verdict

The conditional full-tree first-sandwich induction and quantitative
folded-cone lemmas are valid. Canonical preservation of the required
center cone and the full second sandwich remain open. The stronger
first-difference multiplier route cannot be deduced from the currently
proposed abstract cone assumptions alone.
