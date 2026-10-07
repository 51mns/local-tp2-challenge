# Quantitative strength controls every folded minor

**Status: proved.** This extends the previously proved adjacent-minor estimate to every ordered minor with positive diagonal entries. The resulting relative bound is sufficient for the general one-turn compatibility argument, but does not yet prove the required strength of its polynomial H.

## All-minor theorem

Let h have finite positive interval support 0 through m and suppose it is lambda-strong, with lambda greater than zero. Then for every \(i<j\) and \(k<l\) for which both \(K_h(i,k)\) and \(K_h(j,l)\) are positive,

\[
\det K_h[\{i,j\},\{k,l\}]
\ge\lambda K_h(i,k).
\tag{1}
\]

The positive-diagonal restriction is necessary: a minor with a zero lower diagonal entry can vanish despite a positive upper diagonal entry.

The established adjacent-minor theorem supplies

\[
\det K_h[\{a,a+1\},\{b,b+1\}]
\ge\lambda K_h(a,b)
\tag{2}
\]

for every adjacent cell. Also \(\delta_m=h_m^2\ge\lambda h_m\), so \(h_m\ge\lambda\). The folded cone implies h is decreasing, hence every positive entry of K_h is at least lambda.

If either off-diagonal entry of the selected minor vanishes, its determinant is its diagonal product. The lower diagonal entry is at least lambda, proving (1).

Otherwise the two off-diagonal entries are positive. The support of K_h is exactly the band \(|a-b|\le m\). Its extreme corner distances show that every cell of the rectangle \([i,j]\times[k,l]\) is positive. Define its adjacent cross-ratios

\[
R_{a,b}=\frac{K_h(a,b)K_h(a+1,b+1)}
 {K_h(a,b+1)K_h(a+1,b)}\ge1.
\]

The product telescopes:

\[
\frac{K_h(i,k)K_h(j,l)}{K_h(i,l)K_h(j,k)}
=\prod_{a=i}^{j-1}\prod_{b=k}^{l-1}R_{a,b}
\ge R_{j-1,l-1}.
\]

Consequently, using (2) at the bottom-right cell,

\[
\begin{aligned}
1-\frac{K_h(i,l)K_h(j,k)}{K_h(i,k)K_h(j,l)}
&\ge 1-R_{j-1,l-1}^{-1}\\
&=\frac{\det K_h[\{j-1,j\},\{l-1,l\}]}
 {K_h(j-1,l-1)K_h(j,l)}\\
&\ge\frac{\lambda}{K_h(j,l)}.
\end{aligned}
\]

Multiplication by the full diagonal product proves (1).

## Relative-minor corollary

Let B have a nonnegative finite half-row b with \(b_n\le b_0\) for every n; a folded-cone B automatically satisfies this. Let H be lambda-strong and assume

\[
H(H)[n]\ge H(B)[n]\quad\hbox{for every }n,
\qquad \lambda\ge8b_0.
\tag{3}
\]

Then every ordered minor satisfies

\[
\det K_H\ge4\det K_B.
\tag{4}
\]

Indeed, a nonpositive B minor is harmless because K_H is TP2. A positive B minor has both diagonal entries positive. Coefficientwise domination makes the corresponding H diagonal entries positive, so (1) applies. Every K_B entry is at most \(2b_0\). Thus

\[
\begin{aligned}
\det K_H
&\ge\lambda K_H(i,k)\\
&\ge8b_0K_B(i,k)\\
&\ge4K_B(i,k)K_B(j,l)\\
&\ge4\det K_B.
\end{aligned}
\]

No upper bound on the kernel indices, bandwidth truncation, or enumeration of minors is involved.

## Exact remaining one-turn obligation

For the arbitrary-inner-index setting, write

\[
A=T_{m+1},\quad B=T_{m-1},\quad
 t=t_{g_m},\quad
H=A(t-r)(t-s)+B(t-c),\qquad r,s,c\in[-2,2].
\]

The actual pure-left trace theorem proves positive ordinary coefficients for every factor \(t-c\), with constant coefficient at least 1. Since all coefficients of A and B are nonnegative, the half-row domination \(H(H)\ge H(B)\) in (3) follows immediately.

It is therefore sufficient to prove the single quantitative family statement

\[
\delta_n(H(H))\ge8H(B)[0]\,H(H)[n]
\]

at every supported n, uniformly in every integer m at least 1 and all three real parameters in [-2,2]. This strength assertion remains unproved here. Individual cone membership of the two summands is insufficient to conclude it; the cross terms in their defects must still be controlled.
