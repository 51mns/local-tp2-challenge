# A positive matrix model for the entire canonical tree

**Status: proved globally.** A fixed congruence turns the continuant connector into a positive polynomial matrix and gives positive transfer recurrences for both endpoint gaps at every canonical node. This is an entrywise positivity theorem. It does not establish Fourier TP2; the precise elementary-block obstruction is stated below.

Use the exact continuant matrices from `continuation_network.md`:

\[
Q_C=Q_A^{\mathsf T}TQ_B^{\mathsf T},\qquad
T=\begin{pmatrix}3y&-1\\1&0\end{pmatrix},\qquad y=x+1,
\]

with \(Q_{11}=G\), determinant one, and \(Q_{12}-Q_{21}=x\).

## 1. Fixed positive congruence

Set

\[
R=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\widehat Q=R^{-1}QR^{-\mathsf T},\qquad
\widehat T=R^{\mathsf T}TR
=\begin{pmatrix}3y&3y-1\\3y+1&3y\end{pmatrix}.
\]

Every entry of \(\widehat T\) has nonnegative ordinary x coefficients. Congruence, rather than similarity, is essential here. The mediant recursion becomes

\[
\widehat Q_C=\widehat Q_A^{\mathsf T}\widehat T\widehat Q_B^{\mathsf T}.
\tag{1}
\]

Indeed all intermediate R and inverse-R factors cancel. The boundary and initial center matrices are

\[
\widehat Q_0=
\begin{pmatrix}x+2&-1\\-y&1\end{pmatrix},\qquad
\widehat Q_1=
\begin{pmatrix}1&x\\0&1\end{pmatrix},
\]

\[
\widehat Q_{1/2}=
\begin{pmatrix}2x^2+3x+2&2x+1\\x+1&1\end{pmatrix}.
\]

The exceptional signed boundary occurs only as the left endpoint. Its full left transfer is nevertheless positive:

\[
\widehat Q_0^{\mathsf T}\widehat T
=\begin{pmatrix}2y&2y-1\\1&1\end{pmatrix}.
\tag{2}
\]

Equations (1) and (2), together with the two positive seed matrices, give an induction under both canonical child operations: **every nonzero-boundary canonical matrix \(\widehat Q\) has nonnegative integer ordinary coefficients in every entry.** The determinant and antisymmetry identities are preserved by this determinant-one congruence.

If \(e=(1,1)^{\mathsf T}\), the original scalar polynomial is particularly simple:

\[
G=e^{\mathsf T}\widehat Q e.
\tag{3}
\]

Thus it is the sum of all four entries of the positive matrix, rather than a selected entry of a signed connector product.

## 2. Both endpoint gaps have positive matrix transfers

For each state put

\[
E_A=\widehat Q_C-\widehat Q_A,\qquad
E_B=\widehat Q_C-\widehat Q_B.
\]

These matrices are symmetric because their antisymmetric parts cancel. The exact gap identities become

\[
\widehat Q_L-\widehat Q_C
=\widehat Q_A^{\mathsf T}\widehat T E_B,
\tag{4}
\]

\[
\widehat Q_R-\widehat Q_C
=E_A\widehat T\widehat Q_B^{\mathsf T}.
\tag{5}
\]

At the initial center,

\[
E_A=y\begin{pmatrix}2x&2\\2&0\end{pmatrix},\qquad
E_B=y\begin{pmatrix}2x+1&1\\1&0\end{pmatrix}.
\]

Both have nonnegative ordinary coefficients. The transfer in (4) is positive for an interior endpoint by Section 1, and for endpoint 0 by (2). The transfer in (5) is positive because its right endpoint is never 0.

After a left step, the two new center-minus-endpoint matrices are the matrix in (4) and its sum with E_A. After a right step, they are the matrix in (5) and its sum with E_B. Induction therefore proves **entrywise ordinary-coefficient positivity of both endpoint gap matrices at every canonical state**.

In particular the shorter-child difference has the exact positive form

\[
S=e^{\mathsf T}(\widehat Q_U-\widehat Q_C)e,
\]

with the appropriate one of (4) and (5). This gives a global positive two-state transfer representation for S, including arbitrary switches between left and right moves.

Every matrix identity and seed is reproduced by the deterministic verifier `fulltree_kernel_positive_transfer.py`. Its role is to check the displayed algebra; the all-depth conclusion follows from the induction, not from a depth scan.

## 3. Why elementary folded-TP2 block closure still cannot work

The connector's diagonal entry is \(3y\). Its Laurent half-row is \((3,3)\), whose central folded defect is

\[
3^2-2\cdot3^2=-9.
\]

Hence the coefficientwise positive connector does not have a TP2 folded kernel in each entry. A block-kernel TP2 theorem that includes these scalar entry submatrices cannot apply directly.

This defect cannot be removed merely by choosing a different constant real congruence. For any real vector \(v=(a,b)^{\mathsf T}\),

\[
v^{\mathsf T}Tv=3ya^2.
\]

Thus every diagonal entry of \(S^{\mathsf T}TS\), for a constant real invertible matrix S, is a nonnegative scalar multiple of y, and at least one is a positive multiple. Its central folded minor is strictly negative. Therefore **no constant real congruence can make all connector entries folded-TP2**.

The positive model remains potentially useful for a selective path-switching argument involving the actual e-to-e gap sums, or a closure theorem for constrained products of connector blocks. Positivity of the two-state paths alone does not prove their adjacent Fourier likelihood-ratio comparison. No global folded-cone or Local TP2 conclusion is asserted here.
