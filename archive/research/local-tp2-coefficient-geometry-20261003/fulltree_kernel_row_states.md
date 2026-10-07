# The two selective states in the positive canonical matrix model

This note records exact reductions following `fulltree_kernel_positive_transfer.md`. It does not prove their Fourier-cone closure.

Write the original continuant matrix and its positive congruence as

\[
Q=\begin{pmatrix}G&s+x\\s&d\end{pmatrix},\qquad
\widehat Q=R^{-1}QR^{-\mathsf T},\qquad
R=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

Set \(r=G-s\). Direct multiplication gives the row and column sums

\[
\widehat Q e=\binom r s,\qquad
\widehat Q^{\mathsf T}e=\binom{r-x}{s+x},
\qquad e=\binom11.
\tag{1}
\]

Thus the second row state is the original continued-fraction denominator, and the first is numerator minus denominator. If the canonical continued fraction is \([a_1,a_2,\ldots,a_n]\), then

\[
\frac rs=[a_1-1,a_2,\ldots,a_n].
\]

The determinant-one condition supplies the additional polynomial identity

\[
Gd=s^2+xs+1.
\tag{2}
\]

These are canonical companion polynomials, not arbitrary positive rows.

The positive connector

\[
\widehat T=\begin{pmatrix}3y&3y-1\\3y+1&3y\end{pmatrix}
\]

acts on the column-sum vector particularly simply. With \(t_G=3yG-x\),

\[
\widehat T\binom{r-x}{s+x}
=\binom{t_G-s}{t_G+r}.
\tag{3}
\]

Therefore the exact row-state recurrence at a mediant is

\[
\binom{r_C}{s_C}
=\widehat Q_A^{\mathsf T}
  \binom{t_B-s_B}{t_B+r_B}.
\tag{4}
\]

This identifies the constrained input that a selective two-state closure theorem would have to preserve. It is stronger information than positivity of an arbitrary input vector.

At the initial center the two row states are

\[
r=2x^2+5x+3,\qquad s=x+2,
\]

with half-rows \((7,5,2)\) and \((2,1)\). Both lie in the folded cone, and the adjacent minors for \(H(s)\le_{\rm lr}H(r)\) are \((3,2)\). In contrast, the column state \(r-x\) has half-row \((7,4,2)\) and defect \(\delta_1=-2\), while \(s+x=2x+2\) has central defect \(-4\).

Thus a symmetric assertion treating row and column states alike is false already at the root. Equations (1) and (3) show the exact corrections that must be retained. The row states provide a possible smaller auxiliary family than all matrix entries, but a proof that their folded cones, likelihood-ratio order, or mixed minors close under (4) is still missing.
