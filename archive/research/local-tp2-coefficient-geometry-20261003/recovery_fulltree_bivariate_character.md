# The Local TP2 Bezoutian as a two-character polynomial

**Status: proved universal algebraic equivalence, not a full-tree positivity proof.**
The reduction applies to any two real polynomials, and hence every canonical
state without a depth bound. It identifies the desired adjacent minors with
one boundary of a representation-ring coefficient array. A canonical
mutation rule preserving that boundary's positivity has not been proved.

## 1. Definitions and change of variables

For polynomials P,Q let

\[
p_n=[q^n]P(q+q^{-1}),\qquad q_n=[q^n]Q(q+q^{-1}),
\quad W_{ij}=p_iq_j-p_jq_i\quad(0\le i<j).
\]

(The coefficient symbol q_n is unrelated to the formal variable q.) Put

\[
\mathcal B_{P,Q}(s,z)
 =\frac{P(s)Q(z)-Q(s)P(z)}{z-s}.
\]

This is an ordinary symmetric polynomial in s,z. Define a linear change on
symmetric polynomials by the substitutions

\[
s=u/v+v/u,\qquad z=uv+(uv)^{-1},\qquad
U=u+u^{-1},\quad V=v+v^{-1}.
\]

Equivalently, it is the algebra homomorphism determined by

\[
s+z\longmapsto UV,\qquad sz\longmapsto U^2+V^2-4.                 \tag{1}
\]

Write the resulting polynomial as \(\mathcal R_{P,Q}(U,V)\). Let
\(\chi_m(U)=U_m(U/2)\), where \(U_m\) is the second-kind Chebyshev polynomial;
explicitly,

\[
\chi_m(u+u^{-1})=u^m+u^{m-2}+\cdots+u^{-m}.
\]

## 2. Exact character formula

For arbitrary P,Q,

\[
\boxed{\begin{aligned}
\mathcal R_{P,Q}(U,V)
={}&\sum_{j\ge1}W_{0j}\chi_{j-1}(U)\chi_{j-1}(V)\\
&+\sum_{1\le i<j}W_{ij}
 \bigl[\chi_{i+j-1}(U)\chi_{j-i-1}(V)
      +\chi_{j-i-1}(U)\chi_{i+j-1}(V)\bigr].
\end{aligned}}                                                     \tag{2}
\]

All sums are finite. There is no factor of two in the i=0 terms.

**Proof.** Use \(C_0(s)=1\), \(C_i(q+q^{-1})=q^i+q^{-i}\) for i>0.
The Laurent definition gives \(P(s)=\sum_i p_iC_i(s)\), and similarly Q.
The numerator of the Bezoutian therefore equals

\[
\sum_{i<j}W_{ij}[C_i(s)C_j(z)-C_j(s)C_i(z)].
\]

Under the stated substitution,
\(z-s=(u-u^{-1})(v-v^{-1})\). For 0<i<j, put a=i+j and b=j-i.
Direct expansion gives

\[
C_i(s)C_j(z)-C_j(s)C_i(z)
=(u^a-u^{-a})(v^b-v^{-b})
 +(u^b-u^{-b})(v^a-v^{-a}).
\]

Dividing proves the second sum. For i=0 the corresponding identity is

\[
C_j(z)-C_j(s)=(u^j-u^{-j})(v^j-v^{-j}),
\]

which proves the first sum and fixes its normalization. QED.

Each product \(\chi_a(U)\chi_b(V)\) is monic with leading monomial
\(U^aV^b\), so these products form a basis. For a>b with equal parity, the
coefficient in (2) is precisely

\[
W_{(a-b)/2,\,(a+b+2)/2}.
\]

For a=b it is \(W_{0,a+1}\); coefficients with different parities vanish.
Thus nonnegative character coefficients are **equivalent** to all-pairs
Fourier likelihood-ratio order. This is not an additional assumption about
root locations or coefficient shape.

In particular the original Local TP2 minors obey the especially simple
formula

\[
\boxed{W_{n,n+1}
 =[\chi_{2n}(U)\chi_0(V)]\mathcal R_{P,Q}(U,V),\qquad n\ge0.}       \tag{3}
\]

For a canonical state take P=S,Q=D; the outgoing-gap replacement Q=S+D
gives the same Bezoutian and the same character polynomial.

## 3. Exact compression to one variable by Catalan moments

Let \(\Lambda_V\) be the linear functional characterized by
\(\Lambda_V(\chi_0)=1\), \(\Lambda_V(\chi_j)=0\) for j>0. Its ordinary
monomial moments are

\[
\Lambda_V(V^{2r})=\frac1{r+1}\binom{2r}{r},\qquad
\Lambda_V(V^{2r+1})=0.
\]

Indeed the coefficient of \(\chi_{m-2k}\) in \(V^m\) is
\(\binom mk-\binom m{k-1}\); at m=2r,k=r this is the displayed Catalan
number. Applying this functional to (2) gives

\[
\boxed{\Lambda_V\mathcal R_{P,Q}(U,V)
 =\sum_{n\ge0}W_{n,n+1}\chi_{2n}(U).}                             \tag{4}
\]

This extracts all requested adjacent minors without retaining the other
character coefficients. If \(B_n(w+w^{-1})=\sum_{k=-n}^n w^k\), then
\(\chi_{2n}(U)=B_n(U^2-2)\). Consequently Local TP2 is equivalent to
positivity of the B coefficients of a single, explicitly computable
Catalan projection. Positivity of its ordinary monomial coefficients is
not asserted to be equivalent.

## 4. Relation to run transport and the precise remaining obstruction

Define \(\mathcal T_F\) to be the image under (1) of F(s)F(z), and
\(\mathcal D_t\) the image of \((t(z)-t(s))/(z-s)\). Formula (2) with P=1
shows

\[
\mathcal D_t(U,V)=\sum_{j\ge1}H(t)_j\chi_{j-1}(U)\chi_{j-1}(V).    \tag{5}
\]

In particular it is character-nonnegative whenever the noncentral Fourier
coefficients of t are nonnegative. The transformed version of the exact
canonical run identity in `fulltree_direct_cauchy_darboux.md` is

\[
\mathcal R_{q_k,q_{k+1}}
 =\mathcal R_{A,B}+\mathcal D_t\sum_{j=0}^k\mathcal T_{q_j}.        \tag{6}
\]

Products of nonnegative character polynomials remain nonnegative, because

\[
\chi_a\chi_b=\sum_{r=0}^{\min(a,b)}\chi_{a+b-2r}.
\]

Thus (6) gives a rigorous sufficient closure criterion, but proving its
right-hand side nonnegative for the actual canonical data remains the
substantive missing step. It is enough to control the boundary in (3);
positivity of every character coefficient would be stronger than necessary
for a direct induction.

There is an exact obstruction to inferring this condition from ordinary
positive networks. For F=x+1,

\[
F(s)F(z)=sz+s+z+1\mapsto U^2+V^2+UV-3
\]

and therefore

\[
\boxed{\mathcal T_{x+1}
 =\chi_2(U)+\chi_2(V)+\chi_1(U)\chi_1(V)-1.}                     \tag{7}
\]

The trivial-character coefficient is -1 although every ordinary
coefficient of F(s)F(z) is positive. Equivalently, with P=x+1 and
Q=x(x+1), their adjacent central Fourier minor is -1. Consequently the
positive connector/network representation cannot establish (3) merely
by replacing its positive scalar factors by character-positive tensors.
The actual coupled canonical data, or cancellation after summing complete
networks, are essential. Equation (7) is an abstract obstruction, not a
counterexample on the canonical tree.

## 5. Corollary: the existing folded cone in the character ring

For every polynomial F there is an exact identity

\[
\boxed{\mathcal T_F=\mathcal R_{F,xF}},                            \tag{8}
\]

because the defining Bezoutian for F,xF is F(s)F(z). Write h=H(F),
extended symmetrically by \(h_{-n}=h_n\) and by zero beyond its degree.
Then \(H(xF)_n=h_{n-1}+h_{n+1}\), and (3) gives

\[
[\chi_{2n}(U)\chi_0(V)]\mathcal T_F
 =h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}
 =\delta_n(h).                                                   \tag{9}
\]

Suppose h is strictly positive on the finite interval 0 through d and
zero above d. For 0 through d define
\(r_n=H(xF)_n/h_n\). For n<d, the condition
\(\delta_n(h)\ge0\) is exactly \(r_{n+1}\ge r_n\). Thus nonnegative
adjacent defects imply all-pairs order within this interval by
transitivity. If i<=d<j, the minor is \(h_iH(xF)_j\ge0\); if d<i<j,
it is zero. Conversely all-pairs order includes the adjacent minors.
Applying (2) therefore proves

\[
\boxed{\mathcal T_F\text{ has nonnegative character coefficients}
\quad\Longleftrightarrow\quad
\delta_n(H(F))\ge0\text{ for all }n\ge0.}                         \tag{10}
\]

This identifies the previously used folded cone with a character-positive
tensor condition; it is a connection to the existing cone, not a new
canonical-tree theorem.

Finally, the change of variables (1) is an algebra homomorphism, so

\[
\mathcal T_{PQ}=\mathcal T_P\mathcal T_Q.                         \tag{11}
\]

The nonnegative Clebsch-Gordan product rule in Section 4 proves product
closure immediately. In detail, if H(P),H(Q) are strictly positive on
finite initial intervals and both defect rows are nonnegative, (10)
makes both factors on the right of (11) character-positive. Their
product is character-positive, and (9) yields all nonnegative defects
of PQ. The Laurent convolution for PQ also remains strictly positive
through its full support: for any 0<=n<=deg(P)+deg(Q), there exist
0<=i<=deg(P), 0<=j<=deg(Q) with i+j=n, giving a positive summand.
This recovers the existing folded-cone product closure by a different
proof.

## 6. Verifier and scope

`recovery_fulltree_bivariate_character.py` uses exact integer arithmetic
and two independent constructions:

1. Construct the ordinary s,z Bezoutian from P,Q, rewrite its symmetric
   monomials using power sums, apply (1), then convert ordinary U,V powers
   to the character basis.
2. Compute Fourier rows by the original binomial definition and construct
   the right side of (2) directly from all minors.

These agree on every ordered monomial pair through degree seven and on
the canonical root and its two children. The independent Catalan
projection also agrees with the original adjacent minors. These finite
checks verify normalization and implementation; the all-degree theorem
is the algebraic proof above.

At the canonical root the projected character coefficients are
(272,352,160,24), recovering the original four Local TP2 minors.
The verifier also checks the signed obstruction (7) exactly.

No all-tree Local TP2 conclusion, nor a preserved cone under arbitrary
left/right switches, is claimed here.
