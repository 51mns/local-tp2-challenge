# Continuation: matrix-gap identities and the Fourier-network obstruction

**Status: proved algebraic lemmas; Local TP2 remains unproved.** This note continues the exact continuant representation in `external_structure.md`. It adds relations coupling matrix entries, not another list of possible sources. `continuation_network.py` is a self-contained exact-arithmetic verifier.

Write `y=x+1`, `t=3y` and

\[
T=\begin{pmatrix}t&-1\\1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
Q_{r\oplus s}=Q_r^{\mathsf T}TQ_s^{\mathsf T}.
\]

The boundary matrices are

\[
Q_0=\begin{pmatrix}1&0\\-x&1\end{pmatrix},\qquad
Q_1=\begin{pmatrix}x+2&x+1\\1&1\end{pmatrix}.
\]

Thus

\[
Q_{1/2}=\begin{pmatrix}2x^2+6x+5&2x+2\\x+2&1\end{pmatrix}.
\]

For each canonical matrix, `(Q_t)_{11}=G_t`, `det Q_t=1`, and `(Q_t)_{12}-(Q_t)_{21}=x`. In the formulas below matrices are named `A,C,B`, whereas their top-left scalar polynomials are `G_A,G_C,G_B`.

## 1. Constant-trace monodromy: an exact representation

Define

\[
P_t=Q_tJ,\qquad K=-JT=\begin{pmatrix}-1&0\\3y&-1\end{pmatrix}.
\]

Then for every Farey triple,

\[
\boxed{P_rP_{r\oplus s}P_s=K,\quad \det P_t=1,\quad\operatorname{tr}P_t=-x.}
\]

Indeed, for a determinant-one matrix, `J Q^T=Q^{-1}J`; direct substitution into the Q recurrence gives the product identity. Alternatively, the following child rules prove preservation of both determinant and trace from the displayed seed:

\[
\boxed{P_L=P_C P_B P_C^{-1},\qquad P_R=P_C^{-1}P_A P_C.}
\]

They follow by solving `P_A P_L P_C=K=P_A P_C P_B` and `P_C P_R P_B=K`. Hence the antisymmetry identity for Q is preserved everywhere, independently of finite-depth checking.

An associated trace identity is

\[
\operatorname{tr}(P_A P_C)=x-3yG_B,
\]

because `P_A P_C=K P_B^{-1}` and the right-hand trace can be multiplied explicitly. This monodromy representation is consistent with the generalized Markov matrix literature; no novelty claim is made.

## 2. Matrix-gap determinant lemma

**Lemma.** For every ordered Farey triple `C=A^T T B^T`,

\[
\boxed{\det(C-A)=-y(3G_B+x-2),\qquad
\det(C-B)=-y(3G_A+x-2).}
\]

In particular, if `U` is the child obtained with a fixed boundary matrix `P`,

\[
\boxed{\det(Q_U-Q_C)=-y(3G_P+x-2).}
\]

**Proof.** Every difference of Q matrices is symmetric. Since `A^T=A-xJ` and `A^{-1}J=JA^T`, cyclic invariance of trace gives

\[
\begin{aligned}
\operatorname{tr}(CA^{-1})
&=\operatorname{tr}(TB^T)-x\operatorname{tr}(JTB^TA^{-1})\\
&=\operatorname{tr}(TB^T)-x\operatorname{tr}(JA^TTB^T)\\
&=(3yG_B-x)-x\operatorname{tr}(JC)\\
&=3yG_B-x+x^2.
\end{aligned}
\]

Here `tr(JC)=-x`. For determinant-one 2-by-2 matrices, `det(C-A)=2-tr(CA^{-1})`, which proves the first formula. For the other formula, use `C^T=BT^T A`, `C=C^T+xJ` and `tr(JB^{-1})=x` to obtain `tr(CB^{-1})=3yG_A-x+x²`. QED.

All Q matrices specialize at `x=-1` to

\[
Q_* = \begin{pmatrix}1&0\\1&1\end{pmatrix};
\]

this follows from the common boundary value and `Q_*^T T(-1)Q_*^T=Q_*`. Consequently each matrix gap is divisible by y. If

\[
\frac{Q_U-Q_C}{y}=\begin{pmatrix}s&h\\h&v\end{pmatrix},\qquad
F_P=\frac{G_P-1}{y},
\]

then the determinant lemma becomes the polynomial Pell-type relation

\[
\boxed{h^2-sv=1+3F_P.}
\]

This is additional coupling between the desired scalar quotient `s=(U-C)/y` and endpoint continuants. It does not itself assert coefficient positivity or Fourier MLR.

## 3. Linear transfer of symmetric gaps

Let `E=C-B`. The next left child is `L=A^T T C^T`, so

\[
L-C=A^TT(C^T-B^T)=A^TT E.
\]

Likewise, with `E=C-A`,

\[
R-C=E T B^T.
\]

Therefore along any fixed-boundary ray the consecutive gap matrices evolve by a fixed determinant-one transfer matrix. On a left ray, set `M=A^T T`; then

\[
E_{n+1}=ME_n,\quad\operatorname{tr}M=3yG_A-x,\quad\det M=1.
\]

Cayley–Hamilton proves for every entry, including the top-left gap polynomial,

\[
E_{n+2}=(3yG_A-x)E_{n+1}-E_n.
\]

The matrix-gap determinant is preserved along that ray. The right-ray version is right multiplication by `TB^T`. Thus arbitrary fixed-boundary rays have an exact two-dimensional transfer description; the constant term in the original affine scalar mutation has disappeared.

## 4. What the Laurent specialization makes simpler—and what it does not

At `x=q+q^{-1}`, every `P_C` has eigenvalues `-q,-q^{-1}`, regardless of the degree of `G_C`. Over the rational-function field in q, set

\[
\Pi_q=\frac{P_C+q^{-1}I}{q^{-1}-q},\qquad
\Pi_{q^{-1}}=\frac{P_C+qI}{q-q^{-1}}.
\]

These are complementary rank-one projectors. Writing `+` for q and `-` for `q^{-1}`, the right mutation is exactly

\[
P_R=\Pi_+P_A\Pi_++\Pi_-P_A\Pi_-
+q^{-2}\Pi_+P_A\Pi_-+q^2\Pi_-P_A\Pi_+.
\]

For the left mutation, replace `P_A` by `P_B` and interchange `q²` with `q^{-2}` in the cross terms. This reduces mutation to two degree shifts after a local eigenbasis change. The apparent denominators cancel in the final Laurent-polynomial matrices.

**The unresolved point is sign.** These projectors have signed entries and denominators `q-q^{-1}`. They are not established positive path matrices, so this formula does not permit a Lindström–Gessel–Viennot coefficient argument on its own.

## 5. Exact obstruction to the most immediate enlarged TP2 invariant

It is tempting to claim that the coefficient half-rows of all entries of Q or of its symmetric gaps are likelihood-ratio ordered. That proposed stronger invariant is already false at the canonical root.

For root matrices, put `S_mat=Q_L-Q_C` and `D_mat=Q_R-Q_L`. Their scalar top-left entries are precisely the requested S and D. The following are exact adjacent Fourier minors, with the first named entry as the narrower row:

| Proposed entry ordering | Adjacent minors |
|---|---|
| `Q_C[1,2] → Q_C[1,1]` | `[-6,4]` |
| `S_mat[2,2] → S_mat[1,2]` | `[-2,2]` |
| `D_mat[2,2] → D_mat[1,2]` | `[162,-54,36]` |

For example, `S_mat[2,2]=x+1` and `S_mat[1,2]=2x²+5x+3`; their Fourier half-rows are `[1,1]` and `[7,5,2]`, and the central minor is `1·5-1·7=-2`.

Thus ordinary positivity of continuant entries, the determinant-one property, and a blanket Fourier-TP2 claim for matrix entries cannot close the proof. A successful use of these lemmas must preserve a more selective relation involving the actual S,D pair or give a signed cancellation whose remaining terms are demonstrably positive.

## 6. Verification and precise scope

The self-contained Python verifier checked all 127 canonical nodes through depth 6 (maximum G degree 54) using integers only. At every node it compared the top-left matrix children against independent scalar mutation formulas and checked the product, conjugation, antisymmetry, gap-determinant, and gap-transfer identities. It also reproduces the explicit false-invariant minors above.

The infinite identities in §§1–4 follow from the displayed algebra; finite verification is not their proof. The missing result remains

\[
H(D)_{n+1}H(S)_n-H(D)_nH(S)_{n+1}>0
\]

through the required support for the canonical short/long children. No positive network or coefficient injection proving this inequality was obtained in this continuation.
