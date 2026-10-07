# Exact obstruction to abstract strong-cone mutation closure

**Status:** this is a counterexample to a proposed *sufficient closure theorem*, not a counterexample to canonical Local TP2. It shows that the product-closed cone F from `mixed_kernel_strong_cone.md`, even combined with the proved support invariant, normalization, endpoint orders, and center-gap orders, does not close under an arbitrary application of the mutation formula. The triple below violates the canonical Fricke equation.

Write y=x+1, P=x+2, and h_Q(n)=[q^n]Q(q+q^{-1}). Put

\[
\Delta_n(h)=h_n^2-h_{n-1}h_{n+1},\qquad
\delta_n(h)=\Delta_n(h)-\Delta_{n+1}(h),
\]

with h_{-1}=h_1 and zero extension. The cone F requires a positive integer half-row of degree at least two, \(\delta_n(h_Q)\ge 2h_Q(n)\) at every supported index, and \(\delta_0(h_{yQ})\ge0\).

Consider

\[
A=1,\qquad B=58x^2+128x+71,\qquad
C=29x^3+120x^2+122x+32.
\]

The nonconstant endpoints and center satisfy the proposed cone hypotheses:

| Polynomial | Half-row h | Defect differences delta | Central defect of y times polynomial |
|---|---|---|---|
| B | (187,128,58) | (13047,2174,3364) | 389 |
| C | (272,209,120,29) | (19262,2702,7498,841) | 718 |

Thus B and C belong to F. In particular both folded kernels are TP2; the proved multiplier lemma also gives K_(3yC-x) TP2. The center margin satisfies \(\delta_0(h_C)=19262\ge h_C(0)+h_C(1)=481\).

All ordinary coefficients are positive integers. Each of A,B,C takes the value 1 at x=-1. With \(\alpha_Q(n)=h_Q(n)-h_Q(n+1)\), their B-basis rows are

\[
\alpha_A=(1),\qquad \alpha_B=(59,70,58),\qquad
\alpha_C=(63,89,91,29).
\]

Consequently A and B have constant B-basis coefficients at least 1, C has constant B-basis coefficient at least 3, and \(\alpha_C(1)\ge\alpha_C(0)+2\). Moreover

\[
\alpha_{C-A}=(62,89,91,29),\qquad
\alpha_{C-B}=(4,19,33,29),
\]

so C strictly dominates both endpoints throughout its support. Its degree is greater than the degree of both endpoints and even obeys the canonical degree relation

\[
\deg C=\deg A+\deg B+1=3.
\]

The likelihood-ratio order invariants used in the conditional first-sandwich induction also hold:

\[
h_A\le_{\rm lr}h_B\le_{\rm lr}h_C,\qquad
h_{PA}\le_{\rm lr}h_{C-A},\qquad
h_{PB}\le_{\rm lr}h_{C-B}.
\]

For the three nontrivial comparisons, the consecutive minors (over the union of their supports) are respectively

\[
(4267,3238,1682),\qquad (147,120,0),\qquad
(8445,11298,3480).
\]

All rows have interval support; these nonnegative consecutive minors imply the stated orders. The executable certificate additionally verifies every pair of indices directly.

Nevertheless, mutation using A as the retained endpoint gives

\[
\begin{aligned}
U&=3yAC-x(A+C)-B\\
 &=58x^4+327x^3+546x^2+301x+25,\\
h_U&=(1465,1282,778,327,58).
\end{aligned}
\]

Its central folded minor is

\[
\delta_0(h_U)=1465^2+1465\cdot778-2\cdot1282^2
=-1053<0.
\]

Hence K_U is not TP2, and U does not belong to F. This is not a mere failure of the quantitative strength margin. The already proved support conclusions themselves do remain valid: \(\alpha_U=(183,504,451,269,58)\) is dense positive, \(\alpha_U(1)>\alpha_U(0)+2\), U(-1)=1, and U strictly dominates C and A in the B basis.

The canonical Fricke residual is explicitly nonzero:

\[
\begin{aligned}
&C^2+x(A+B)C-3yABC+A^2+B^2+xAB\\
&\quad=-750-16731x-56058x^2-79307x^3\\
&\qquad\quad-56137x^4-19430x^5-2523x^6.
\end{aligned}
\]

Therefore this triple does not arise in the canonical tree. Any proof of canonical F closure must use additional canonical information, such as the Fricke identity or stronger correlations between a center and its endpoints. The existing F product and multiplier theorems remain valid.

The independent, deterministic integer-arithmetic verifier is `mixed_kernel_closure_obstruction.py`. It checks every assertion above; it performs no search and requires only the existing local exact-polynomial helper.
