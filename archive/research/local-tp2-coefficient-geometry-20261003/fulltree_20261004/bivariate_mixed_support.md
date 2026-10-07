# Mixed bivariate tensors: a support obstruction on the canonical tree

Status: exact all-degree lemmas and an exact canonical obstruction to a
particular enlarged invariant. This does not prove or refute full-tree
Local TP2. The results are lane-local E0--E1; the accompanying executable
is an internal exact check, not an independent reproduction or a novelty
assessment.

Use the ordinary Bezoutian and its two-character image from
`../recovery_fulltree_bivariate_character.md`:

\[
 B(P,Q)=\frac{P(s)Q(z)-Q(s)P(z)}{z-s},\qquad
 R(P,Q)=\Phi B(P,Q),
\]

where \(\Phi(s+z)=UV\), \(\Phi(sz)=U^2+V^2-4\). Define the **doubled
mixed tensor**

\[
 J(P,Q)=\Phi\{P(s)Q(z)+Q(s)P(z)\}.
\]

The doubling avoids rational coefficients. Write
\(h_n=H(P)_n\), \(k_n=H(Q)_n\), with symmetric and zero extensions.

## 1. Exact polarization identity

For arbitrary real polynomials P,Q,

\[
 \boxed{J(P,Q)=R(P,xQ)+R(Q,xP).}                 \tag{1}
\]

Indeed the sum of the two Bezoutian numerators is exactly
\((z-s)(P(s)Q(z)+Q(s)P(z))\). Therefore, at the boundary of the
character array,

\[
\begin{split}
 [\chi_{2n}(U)\chi_0(V)]J(P,Q)
  ={}&2h_nk_n-h_{n-1}k_{n+1}-k_{n-1}h_{n+1}\
    &-2h_{n+1}k_{n+1}+h_nk_{n+2}+k_nh_{n+2}.
\end{split}                                                        \tag{2}
\]

This follows either from (1) and the exact adjacent-minor character
formula, or by expanding the quadratic folded defect of h+k. Denoting
the right side by \(j_n(P,Q)\), the latter gives

\[
 \boxed{\delta_n(H(P+Q))
 =\delta_n(h)+\delta_n(k)+j_n(P,Q).}             \tag{3}
\]

These identities hold at the folded index n=0 as well: the convention
\(h_{-1}=h_1\), \(k_{-1}=k_1\) is essential there.

## 2. A forced negative character coefficient

Suppose \(p=\deg P\), \(\operatorname{lc}(P)>0\),
\(\deg Q\ge p+2\), and \(H(Q)_{p+2}>0\). Then

\[
 \boxed{[\chi_{2p+2}(U)\chi_0(V)]J(P,Q)
 =-\operatorname{lc}(P)H(Q)_{p+2}<0.}           \tag{4}
\]

Proof: set n=p+1 in (2). Every h term vanishes except
\(h_{n-1}=h_p=\operatorname{lc}(P)\). No shape assumption, numerical
approximation, or depth induction is involved. QED.

Consequently, even if individual tensors \(T_P=\Phi(P(s)P(z))\) and
\(T_Q\) are character-nonnegative, and all Bezoutian coefficients of
\(R(P,Q)\) are nonnegative, these facts cannot make J(P,Q)
character-nonnegative when the displayed support condition holds.
This is a support obstruction, so imposing the Fricke equation on a
triple cannot remove it when its actual P,Q obey the same condition.

## 3. Exact canonical example, including Fricke

At the canonical root,

\[
 X=1,\quad Y=x+2,\quad C=2x^2+6x+5,
\]

and direct mutation gives

\[
 S=4x^3+16x^2+20x+8,
\quad D=6x^4+30x^3+56x^2+48x+16.
\]

The root triple satisfies the original Fricke equation exactly. For
P=C and Q=D, their degrees are 2 and 4, so (4) gives

\[
 \boxed{[\chi_6(U)\chi_0(V)]J(C,D)=-2\cdot6=-12.}               \tag{5}
\]

Both individual tensors are character-nonnegative, and R(C,D) is
character-nonnegative, as the exact executable checks from their
original Fourier rows. Thus a proof package requiring **all mixed
tensors between its canonical center and outgoing gaps** to be
character-nonnegative fails on the seed itself. It does not merely
fail on a noncanonical tuple that violates Fricke.

For the actual outgoing S,D pair, the same obstruction appears after
the first left step:

\[
 \deg S=4,\quad\operatorname{lc}(S)=8,
 \quad\deg D=6,\quad\operatorname{lc}(D)=24,
\]

so

\[
 [\chi_{10}(U)\chi_0(V)]J(S,D)=-192.                            \tag{6}
\]

These are exact counterexamples to the enlarged mixed-tensor
invariant. They are not counterexamples to the target R(S,D), whose
required adjacent minors are strictly positive in these examples.

## 4. What the negative coefficient forces in a sum proof

For p=deg P and deg Q>=p+2, (3)--(4) give the exact identities

\[
 \boxed{\delta_{p+1}(H(P+Q))
 =\delta_{p+1}(H(Q))
  -\operatorname{lc}(P)H(Q)_{p+2},}             \tag{7}
\]

\[
 \delta_n(H(P+Q))=\delta_n(H(Q))\quad(n\ge p+2).                \tag{8}
\]

In particular the only new index strictly beyond P's support is
p+1. It is controlled if Q has the quantitative strength
\(\delta_n(H(Q))\ge\mu H(Q)_n\) with
\(\mu\ge\operatorname{lc}(P)\), and its half-row is nonincreasing.
Indeed (7) is then at least

\[
 \mu H(Q)_{p+1}-\operatorname{lc}(P)H(Q)_{p+2}\ge0.
\]

This conditional cancellation lemma reduces a proposed sum argument
to the overlapping support and to establishing actual canonical
quantitative strength. It does not establish either missing property.
For n<=p the mixed term in (2) retains several signs, and support
alone supplies no positivity.

## Remaining obligation

No finite invariant package under both child mutations was closed in
this lane. A successful bivariate proof must retain signed mixed
tensors or combine them with positive self-tensors before taking
character coefficients. The exact Fricke equation is satisfied by
(5)--(6); it does not justify discarding these negative components.
The character positivity of the complete target R(S,D) on arbitrary
canonical paths remains open here.
