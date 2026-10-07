# Exact external models for AIMath Local TP2

Status: exact representation bridges identified; **these do not prove Local TP2**. No GitHub changes were made.

## 1. Continued fractions for the same deformation

Bittmann–Jouteur–Kantarcı Oğuz–Molander–Yıldırım, *A Mirror deformation of Markov Numbers*, arXiv:2602.14802v1, §3.1, Definition 3.1, identify the deformed squared Markov polynomial with a continued-fraction numerator. Set their `q+q^{-1}=x`. This gives exactly AIMath's `G_0=1`, `G_1=x+2`, `G_{1/2}=2x²+6x+5` and mutation `G'=3(1+x)BC-x(B+C)-A`.

For the Farey parents `r<s`, write `w_r=(a_1,...,a_l)`, `w_s=(b_1,...,b_n)`, and `t=r⊕s`. Their rules become

- `w_{1/2}=(2x+2,x+2)`;
- if `r=0`, `w_t=(2x+2,1,b_n-1,b_{n-1},...,b_1)`;
- if `s=1`, `w_t=(a_l,...,a_1,3x+2,x+2)`;
- otherwise `w_t=(a_l,...,a_1,3x+2,1,b_n-1,b_{n-1},...,b_1)`.

Then `G_t(x)=K(w_t)`, the ordinary continuant. This is an exact subtraction-free representation since endpoint constants are at least 2. It establishes coefficient positivity, not ratios between differences.

**Textual cautions:** Lemma 3.2 says endpoint constants are “greater than 2”, whereas the seed has constants equal to 2. Its proof also prints an extra middle `x` in the seed. Definition 3.1's two-entry seed is the consistent one and directly gives AIMath's seed.

Source: https://arxiv.org/html/2602.14802v1

## 2. Derived two-by-two recursion (independent algebra)

Let

\[
E(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix},\quad
Q_t=E(a_1)\cdots E(a_n),\quad
T=\begin{pmatrix}3x+3&-1\\1&0\end{pmatrix}.
\]

The top-left entry of `Q_t` is `G_t`. All interior words have even length, so `det Q_t=1`. The simple identity

\[
E(1)E(b-1)=J E(b),\qquad J=\begin{pmatrix}1&0\\1&-1\end{pmatrix},
\quad E(3x+2)J=T
\]

turns the exact word recursion into

\[
\boxed{Q_{r\oplus s}=Q_r^{\mathsf T}TQ_s^{\mathsf T}.}
\]

It includes both boundaries when we define

\[
Q_0=\begin{pmatrix}1&0\\-x&1\end{pmatrix},\qquad
Q_1=\begin{pmatrix}x+2&x+1\\1&1\end{pmatrix}.
\]

Indeed `Q_0^T T=[[2x+3,-1],[1,0]]`, and

\[
Q_{1/2}=Q_0^{\mathsf T}TQ_1^{\mathsf T}
=\begin{pmatrix}2x^2+6x+5&2x+2\\x+2&1\end{pmatrix}.
\]

This seed multiplication was independently checked with exact Python integer-polynomial arithmetic. The full recursion follows algebraically from the cited word rules, not from finite numerical agreement. It supplies extra endpoint continuants that are absent from the scalar mutation. Its negative entries mean ordinary entrywise matrix positivity cannot simply be invoked.

## 3. Exact weighted-poset model and possible difference route

Banaian–Gyoda, *Cluster algebraic interpretation of generalized Markov numbers and their matrixizations*, arXiv:2507.06900v3 (6 September 2026), Corollary 8.33, represent the same generalized cluster variables by weighted ideals of fence posets. Specialize cluster variables to 1 and `k_1=k_2=k_3=x`. In Definition 7.1 every crossed segment gives a two-element chain: its lower element has weight `x`, upper element `1/x`. Consequently an ideal contributes `x^m`, where `m` counts partially occupied pairs. The Laurent substitution further decorates each such pair independently by `q` or `q^{-1}`.

This formal-variable specialization is justified from identities for all positive integer `k`: the fixed poset construction is unchanged while `k>0`, and clearing denominators gives polynomial identities.

Lemma 8.27 describes Farey concatenation using reversed parent posets and a fixed connector. Proposition 8.12 gives a weight-preserving skein decomposition

\[
W(P)=W(P_{34})+Z_RZ_t W(P_{56}).
\]

These offer a concrete route to positive combinatorial models for differences. **Still missing:** specific embeddings/resolutions identifying AIMath's `S=U-C` and `D=V-U`, followed by a weight-preserving injection or TP2 theorem proving their coefficient-ratio comparison. No such injection was established here.

Source: https://arxiv.org/pdf/2507.06900

## 4. Matrix source and applicability limits

Gyoda–Maruyama–Sato, *SL(2,Z)-matrixizations of generalized Markov numbers*, arXiv:2407.08203v3, Theorem 1.3 and §7, also applies to this exact model. Its Cohn triples obey

\[
(P,Q,R)\mapsto(P,PQ-\Sigma,Q),\quad(Q,QR-\Sigma,R),\qquad
\Sigma=\begin{pmatrix}x&0\\3x^2+3x&x\end{pmatrix},
\]

with generalized Markov entries in position `(1,2)` and `tr P=3(1+x)P_{12}-x`. This is another valid algebraic bridge, but its subtraction again prevents automatic coefficientwise total positivity.

Source: https://arxiv.org/pdf/2407.08203

Ordinary fence rank-polynomial results cannot be directly imported: the statistic here counts partially occupied pairs and then signed decorations, rather than ideal cardinality. Moreover, general fence rank polynomials need not be log-concave, as discussed in Kantarcı Oğuz–Ravichandran, *Rank Polynomials of Fence Posets are Unimodal*, arXiv:2112.00518. Unimodality alone is weaker than the strict MLR/TP2 target.

Source: https://arxiv.org/abs/2112.00518
