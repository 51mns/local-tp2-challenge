# Family 231 and canonical Local TP2: exact transfer audit

Status: **three proved obstructions and an exact conditional bridge; full Local TP2 remains OPEN.**

Target recurrence: the AIMath canonical recurrence supplied with research head
`a36fbac460073bf757434f122e721dfa254e8e48`.
Audit date: 2026-10-07.

## 1. What the source actually supplies

The relevant openai/math item is Family 231, *The free uniform spanning forest
is a factor of IID*, dated 2026-09-25. Its `strongly-rayleigh.tex` section proves
a dimension-independent response estimate for finite strongly Rayleigh binary
laws, including their positive external-field tilts:

\[
\partial_{h_j}p_i=\operatorname{Cov}(X_i,X_j),\qquad
\sum_j|\partial_{h_j}p_i|\le 2p_i(1-p_i)\le\tfrac12.
\]

The proof uses a stable symmetric homogenization with dummy coordinates,
nonpositive off-diagonal covariances, and a constant total count. The paper
then uses this response bound to construct equivariant IID samplers. It
does **not** state a monotone-likelihood-ratio theorem for Fourier coefficient
rows or for differences between Markov polynomials. Its weighted-tree section
also obtains negative covariances as minus squares of inverse-Laplacian entries.

Sources inspected through the GitHub connector (not inferred from the title):

- [Family 231 overview entry](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/overview.tex).
- [Strongly Rayleigh section](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/strongly-rayleigh.tex), blob `9127a3bc90836f18b875fc8f72a84c8e0228dab5`.
- [Weighted-tree response section](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/response.tex), blob `d2d381022e4cbbf8988aecf11c9ff03945faabd9`.
- [Introduction and precise theorem scope](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/introduction.tex), blob `0f60f590e1f85fdec5bb66a40b615295e48a3073`.

The transfer statements below are independent elementary deductions. They do
not assume the correctness of the source's infinite-process theorem.

## 2. First obstruction: ordinary-count stable lifts are impossible

Let a canonical state be `(A,C,B)`, with

\[
L=3(x+1)AC-x(A+C)-B,\qquad
R=3(x+1)CB-x(C+B)-A.
\]

Let U,V be the children in increasing degree, S=U-C and D=V-U. Write
H(P)_n=[q^n]P(q+q^{-1}).

**Proposition 1 (all words).** Every canonical state has
`A(-1)=C(-1)=B(-1)=1`. In particular S and D are divisible by x+1. For
every nonzero canonical S or D of degree d, the polynomial

\[
Q_P(q)=q^dP(q+q^{-1})
\]

is divisible by `q²+q+1`, and is not real stable.

**Proof.** The initial values 1, x+2 and 2x²+6x+5 all equal 1 at x=-1.
At that value the mutation reads `L=A+C-B` or `R=C+B-A`; an all-one
triple stays all-one. Induction on word length proves the evaluation
identity. The two differences therefore vanish at x=-1. If
P=(x+1)T and deg P=d, then

\[
Q_P(q)=(q^2+q+1)\,q^{d-1}T(q+q^{-1}).
\]

The second factor is a polynomial. The primitive cube root
`(-1+i sqrt(3))/2` lies in the upper half-plane and is a zero of the
first factor. This contradicts real stability. QED.

**Consequence.** These shifted full Fourier rows cannot be the distribution
of the ordinary number of occupied coordinates in a strongly Rayleigh law,
even after adjoining extra coordinates, marginalization, or positive external
fields. Indeed, if g is a stable multiaffine generating polynomial,
the count polynomial g(q,...,q) is univariate stable, hence real-rooted.
Setting uncounted coordinates to 1 is a stability-preserving boundary
specialization. Adding a deterministic count only multiplies by a monomial
and does not remove the nonreal zeros. Likewise, symmetric homogenization
cannot repair this obstruction: setting its dummy coordinates back to 1
would recover the prohibited unstable specialization.

This proposition concerns ordinary counts. A statistic containing positive
and negative signs is **not** covered by its no-go statement; see Section 4.

## 3. Folding first does not repair the root

Define the folded generating polynomial

\[
\widehat P(q)=\sum_{n=0}^{\deg P}H(P)_nq^n.
\]

At the canonical root, direct substitution into the recurrence gives

\[
\begin{aligned}
S&=4(x+1)^2(x+2),\\
D&=2(x+1)(x+2)\bigl(3(x+1)^2+1\bigr),\\
H(S)&=(40,32,16,4),\\
H(D)&=(164,138,80,30,6).
\end{aligned}
\]

**Proposition 2.** The folded root row H(S) is not an ordinary-count
distribution of any strongly Rayleigh law, up to a positive normalizing
constant.

**Proof.** A cubic with positive coefficients `a0,a1,a2,a3` and only
nonpositive real roots necessarily satisfies `a1² >= 3 a0 a2`.
To see this directly, write it as
`a0(1+lambda1 q)(1+lambda2 q)(1+lambda3 q)` with positive lambdas;
the inequality is equivalent to
`(lambda1+lambda2+lambda3)² >= 3(lambda1 lambda2+lambda1 lambda3+lambda2 lambda3)`.
The difference is half the sum of the three squared pairwise differences.
For H(S), however,

\[
32^2-3\cdot40\cdot16=-896<0.
\]

Thus its polynomial is not real-rooted. The count-specialization argument
from Proposition 1 applies. QED.

As an independent exact arithmetic check, its cubic discriminant is -134144.
The original x-polynomial D also fails real-rootedness already at the root,
because `3(x+1)²+1` has roots `-1 +/- i/sqrt(3)`.

The canonical root itself still satisfies Local TP2:

\[
(F(0),F(1),F(2),F(3))=(272,352,160,24).
\]

Hence the obstruction concerns the proposed proof route, not the conjecture.

## 4. Second obstruction: even an explicit signed-count SR model is insufficient

One can evade the first obstruction by assigning q to some coordinates and
q^{-1} to others. But strong Rayleigh dependence and adding an independent
block then do not imply the required folded coefficient order.

**Proposition 3 (explicit stable model).** For each m>=1, let

\[
g_m(u_1,v_1,\ldots,u_m,v_m)
=3^{-m}\prod_{i=1}^m(1+u_i+v_i).
\]

This is a normalized multiaffine real-stable probability generating
polynomial: independently in each block choose `(U_i,V_i)` uniformly from
`(0,0),(1,0),(0,1)`. Nevertheless the distributions of
`T_m=sum_i(U_i-V_i)` are not always likelihood-ratio ordered after folding
to nonnegative n, even when m is increased by one.

**Proof.** Each factor has strictly positive imaginary part whenever both
of its variables are in the upper half-plane. Thus no factor vanishes,
and their product is stable. Under the signed-count substitution,

\[
\mathbb E q^{T_m}=3^{-m}(1+q+q^{-1})^m.
\]

For m=1 and 2, the unnormalized half-rows are `(1,1)` and `(3,2,1)`;
their first minor is -1. For the degrees 3 and 4 matching the canonical
root degrees, the rows are

\[
H((x+1)^3)=(7,6,3,1),\qquad
H((x+1)^4)=(19,16,10,4,1).
\]

The successive minors are `(-2,12,2,1)`, since the central one equals
`7*16-6*19=-2`. Positive probability normalization preserves its sign.
For the distributions of `|T_m|`, multiplying each positive-index column
by 2 also preserves the sign; the normalized central minor is `-4/2187`.
QED.

This is an explicit strongly Rayleigh realization of the earlier scalar
`(x+1)^3,(x+1)^4` counterexample. It rules out the stronger assertion that
negative dependence of a common multiaffine model, signed occupation counts,
and independent block extension together suffice. A canonical construction
would need additional structure controlling the signed statistic and the
particular pair S,D.

## 5. Third obstruction: the response estimate has no sign information by itself

**Proposition 4.** Every law on two binary coordinates, with or without the
strongly Rayleigh property, satisfies

\[
\sum_{j=1}^2|\operatorname{Cov}(X_i,X_j)|
\le 2\operatorname{Var}(X_i)\le\tfrac12.
\]

This remains true after every finite positive external-field tilt.

**Proof.** For a nondegenerate binary X_i,

\[
\operatorname{Cov}(X_i,X_j)
=\operatorname{Var}(X_i)
\bigl(\mathbb E[X_j\mid X_i=1]-\mathbb E[X_j\mid X_i=0]\bigr).
\]

The bracket belongs to [-1,1]; degenerate X_i has a zero row. Add the
diagonal variance. The argument applies to any tilted law as well. QED.

For example the positive generating polynomial `2+z+w+2zw`, normalized by
6, has covariance +1/12 at unit fields, and row absolute sum 1/3. Its
Rayleigh difference is `1*1-2*2=-3`. Thus a dimension-independent response
bound sufficient for the source's sampling argument is not by itself a
certificate for the determinant sign in Local TP2.

## 6. Exact conditional bridge, and why it is presently circular

Let `s_n=H(S)_n` and `d_n=H(D)_n`. For each supported index n define

\[
G_n(z,w)=s_{n+1}+s_nz+d_{n+1}w+d_nzw.
\]

**Proposition 5.** G_n is real stable if and only if

\[
F(n)=s_nd_{n+1}-s_{n+1}d_n\ge0.
\]

When its coefficients define a positive law after normalization, the
two-coordinate covariance under positive fields z,w is exactly

\[
\operatorname{Cov}_{z,w}(Z,W)
=-\frac{zwF(n)}{G_n(z,w)^2}.
\]

**Proof.** For nonnegative a,b,c,d, the nonzero polynomial `a+bz+cw+dzw`
vanishes at
`w=-(a+bz)/(c+dz)`. For Im z>0 this w has imaginary part

\[
\frac{(ad-bc)\operatorname{Im}z}{|c+dz|^2}.
\]

Consequently real stability is equivalent to `bc>=ad` (the trivial
zero-coefficient boundary cases follow directly or by a limit).
Substitute `a=s_{n+1}, b=s_n, c=d_{n+1}, d=d_n`. Differentiating the
finite two-bit partition sum gives the covariance formula. QED.

This is a correct dictionary to the Rayleigh inequality, but verifying
stability of these G_n is exactly the original sign problem. It is not a
proof by invoking the name of a stronger property. To make Family 231's
minus-square route useful, one would have to exhibit a single canonical
stable or weighted-tree model whose actual two-coordinate partition
sections are these G_n, and prove this correspondence through both tree
mutations. No such construction was obtained in this audit.

## 7. Reproduction and result status

`verify_rayleigh_transfer.py` is dependency-free Python with exact integers
and `fractions.Fraction`. It independently rebuilds the canonical root,
checks the factorizations, the cyclotomic divisibility at the root, all
displayed coefficient rows, the Newton violation and discriminant, and the
SR signed-count and response counterexamples. It writes
`rayleigh_transfer_results.json`. The all-word cyclotomic obstruction is
the induction proof in Section 2, not an extrapolation from this verifier.

No claim that Family 231 solves the AIMath conjecture is made. No canonical
counterexample to Local TP2 was found. The completed advance here is a
rigorous elimination of three tempting transfer routes and an exact
criterion specifying what a successful Rayleigh representation must prove.
