# The multiplier gate from three local center defects

**Status: a new conditional general implication, with exact abstract
obstructions. Full-tree common closure remains OPEN.** This note does not
assume any all-tree center strength theorem. It distinguishes the existing
whole-support 1-strength lemma from the weaker local result below.

Write `h=H(C)`, `v=H(yC)`, and `M=3yC-x+1`. Every row is reflected at
negative indices and zero extended. Let `A_ij` be the ordered minor of the
first two rows of K_h at columns i,j. In particular,

`A_01=delta_0(h)`, `A_12=delta_1(h)`, `A_23=delta_2(h)`.

## 1. Frozen finite center condition

Assume C has positive interval Fourier support of degree at least two,
`K_C` is TP2, and impose only three strength inequalities:

`delta_i(h)>=h_i/2`, `i=0,1,2`.                     (L)

Define the single central quantity

`B0(C)=9delta_0(v)+3v_0+6v_1`.                    (B)

**Theorem.** If (L) holds and `B0(C)>=0`, then `K_M` is TP2 and the two
Fourier rows satisfy

`M-1 <=lr (x+2)M`.

The multiplier has strictly positive defects at indices 0,1,2 and at its
terminal index. No strictness is asserted for the other tail indices.
No whole-support strength or multiplication-by-y cone premise is used.

The older sufficient package `C is 1-strong` and `delta_0(yC)>=0` implies
these hypotheses. The new package is strictly weaker: `C=Croot+2`
satisfies (L) and B, while `delta_0(yC)=-9<0`. Thus this is not a
re-statement of the known `C1strong -> t_C2strong` lemma.

## 2. Exact proof of the only dangerous noncentral defect

Because K_C is TP2, h is decreasing and every A_ij is nonnegative.
Cauchy--Binet with the row of y gives, including the low-degree boundary,

`delta_1(v)=A_01+A_02+A_03+A_13+A_23`.             (1)

The elementary two-row identities are

`h_1 A_02=h_2 delta_0(h)+h_0 delta_1(h)`,

`h_2 A_13=h_3 delta_1(h)+h_1 delta_2(h)`,

`h_1 A_03=h_3 delta_0(h)+h_0 A_13`.               (2)

Here h_1,h_2 are positive, so no unsupported division occurs. Condition
(L) yields

`A_02>=(h_0+h_2)/2`,

`A_13>=(h_1+h_3)/2`,

`A_03>=h_0(1+2h_3/h_1)/2`.

Consequently, putting

`B=3h_0+h_1+2h_2+h_3+2h_0h_3/h_1`,

we have `delta_1(v)>=B/2`. On the other hand,

`2v_1+v_2+v_3=2h_0+3h_1+4h_2+2h_3+h_4`.

The difference `B/2-(2v_1+v_2+v_3)/3` is nonnegative. After multiplying
by `6h_1`, its numerator is exactly

`5(h_0-h_1)h_1+2(h_1-h_2)h_1`
` +6(h_0-h_1)h_3+3h_1h_3+2h_1(h_3-h_4)>=0`.      (3)

Every term uses only monotonicity of h. This proves the useful local
inequality

`3delta_1(yC)>=2v_1+v_2+v_3`.                    (4)

For M, direct expansion gives

`delta_0(M)=9delta_0(v)+6v_0+12v_1+3v_2-1`,

`delta_1(M)=9delta_1(v)-6v_1-3v_2-3v_3+1`,

`delta_2(M)=9delta_2(v)+3v_3`,

`delta_n(M)=9delta_n(v)`, `n>=3`.                 (5)

Equation (4) therefore gives `delta_1(M)>=1`, a strict bound independent
of degree. The formulas remain valid when deg C=2: h_3=h_4=0, while
the first-two-row minors at column 3 retain their terminal h_2 term.
They also cover deg C=3 without a separate omitted index.

## 3. Central, tail, support, and centerbase cases

Multiplication by y is not a cone operation at the central index.
Nevertheless its adjacent kernel minors at every output index n>=1
are the five nonnegative terms

`A_(n-1,n)+A_(n-1,n+1)+A_(n-1,n+2)`
` +A_(n,n+2)+A_(n+1,n+2)`.

Thus K_C TP2 alone implies `delta_n(v)>=0` for n>=1, including its
terminal support. Equations (5) give all multiplier tail defects
nonnegative; index 2 is strict because v_3>0 for deg C>=2.

The support of M is positive. Indeed, the local index-one hypothesis
gives `h_1/2<=delta_1(h)<=2h_1^2`, so `h_1>=1/4` and
`v_1=h_0+h_1+h_2>1/2`; hence `3v_1-1>0`. All other supported M entries
are `3v_n`, except `M_0=3v_0+1`. In particular `v_0>=3/4`, and

`delta_0(M)=B0(C)+3v_0+6v_1+3v_2-1>0`

under (B). The terminal defect is the square of the positive terminal
coefficient. Folded TP2 equivalence now proves K_M TP2.

For the two-row centerbase, put `c=M-1`, `P=x+2`. Direct convolution
gives

`W_0(c,PM)=B0(C)`,

`W_n(c,PM)=delta_n(M)`, `n>=1`.                   (6)

The row c is also positive: its central entry is `3v_0`, and its index
one is the already positive `3v_1-1`. PM has one extra terminal entry.
All adjacent minors are nonnegative by (B) and (5), so ratio transitivity
proves all ordered LR minors nonnegative. This completes the theorem.

## 4. Scope and closure matrix

The natural proposed center package F_local is `K_C TP2 + (L) + (B)`.

| Obligation | Status |
|---|---|
| ROOT | **Proved**: h=(9,6,2), defects=(27,14,4); v=(21,17,8,2), B0=444 |
| IMPLIES K_M | **Proved** by Sections 2–3 |
| IMPLIES centerbase | **Proved** by (6) |
| SHORT CHILD preserves F_local | **OPEN**; requires actual correlated C+S transport |
| LONG CHILD preserves F_local | **OPEN**; requires actual correlated C+S+D transport |
| IMPLIES strict Local TP2 | **Not alone**; actual gap kernel and strict proxy gates from the regular state package remain |

Therefore this note conditionally eliminates K_M and its centerbase
companion from a strengthened center predicate. It does **not** eliminate
the gate from the original P_Q alone, and it does not prove a common
canonical invariant. Only three center defects and one central scalar
remain to transport, rather than all center strengths and an entire
smoothed cone.

## 5. Exact obstacles to tempting weaker implications

These are abstract center examples, not actual canonical counterexamples.
At root endpoints `(1,x+2)`, `C=Croot+j` has exact Fricke residual
`j(Croot+j-1)`, nonzero for every listed j>0. No impossibility of some
other Fricke completion is claimed.

* `C=Croot+3=2x^2+6x+8` is 4/3-strong and ordinary-positive. Its multiplier
  row `(73,59,24,6)` has defects `(119,1507,186,36)`, so K_M is TP2, but
  `B0(C)=-96`. Thus K_M, ordinary positivity and even center strength do
  not by themselves imply the extra centerbase.
* `C=Croot+4=2x^2+6x+9` is 1-strong and ordinary-positive, but
  `delta_0(M)=-88`. Hence dropping the old central condition while
  retaining whole-support 1-strength is invalid.
* The integer row `h=(22,20,15,8)` has defects `(14,5,1,64)`. Its smoothed
  row `(62,57,43,23,8)` has defects `(12,45,353,121,64)`. Both are in the
  folded cone, yet `H(M)=(187,170,129,69,24)` has `delta_1(M)=-134`.
  Its character differences are `(2,5,7,8)`, all positive, but the
  ordinary polynomial is `8x^3+15x^2-4x-8`; it violates ordinary
  nonnegativity. This rules out weak paired row/character predicates,
  not the stronger canonical ordinary/Fricke/ancestry class.

Small bounded ordinary-positive searches found no counterexample to the
stronger weak-paired implication in their stated ranges, but this is
only exploratory evidence and is not used by the theorem. No all-tree
strength conclusion is inferred.

The relaxed central condition B is not closed under unrestricted positive
sums, even of identical centers. For `C=Croot+2`,

`B0(lambda C)=-81lambda^2+183lambda`.

At lambda=1 it is 102, at lambda=2 it is 42, and at lambda=3 it is -180.
All these positive multiples retain K_C TP2 and the three local half
strength inequalities. This is not a canonical child counterexample:
the actual child has larger degree and correlated added gap. It rules
out treating F_local as a positive-sum cone.

There is a distinct valid central closure fact. For nonnegative rows u,w
with `delta_0(u)>=0` and `delta_0(w)>=0`, their polarized central defect
is

`2u_0w_0+u_0w_2+w_0u_2-4u_1w_1>=0`.

Indeed AM--GM bounds its first three terms below by
`2sqrt(u_0(u_0+u_2)w_0(w_0+w_2))>=4u_1w_1`.
Thus the stronger condition `delta_0(yC)>=0` is preserved under
`C->C+Fout` **if** `delta_0(yFout)>=0`. This is a conditional central
transport lemma only; K_Fout TP2 alone does not supply that smoothing
condition, and the full folded cone is not closed under arbitrary sums.

## 6. Exact reproducer and foundations

`multiplier_exact.py` uses only Python integers, Fractions, and an explicit
sparse rational polynomial ring. It imports no parent arithmetic. It
independently verifies (1), (2), (3), (5), and (6), including formal
degree-two/three/four/five boundary cases, and saves all exact witness
rows, defects, ordinary polynomials and root-endpoint Fricke residuals
in `multiplier_exact_results.json`.

The proof's imported mathematical foundations are the previously audited
folded TP2 equivalence, first-two-row minor identities, the y-tail
Cauchy--Binet formula and LR ratio transitivity. The old whole-support
1-strength trace theorem is recorded in `mixed_kernel_strong_cone.md`
but is not used to prove the new three-local-defect implication.

The independent `common_gate_audit` lane reported PASS for the conditional
theorem, including every support case, the local-strength SOS, and the
exact obstruction classifications. No child-preservation or full-tree
claim was promoted by that review.
