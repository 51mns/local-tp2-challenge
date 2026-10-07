# Uniform mass and proxy bounds for every one-turn ray

This note supplies the multiplier and final proxy comparison for every
integer `m>=2`, uniformly over the entire subsequent run `k>=1`.
It uses the separately proved one-turn mixed-kernel closure, including
the nonnegative mixed minors in its positive Jacobi-resolvent expansion.
The already proved `m=1` mixed-ray theorem supplies that initial case.

Put `x=q+q^-1`, `y=x+1`, `P1=x+2`, and

\[
T_m=\sum_{j=0}^mU_j(x+3/2),\quad P=1+yT_m,\quad
t=3yP-x,\quad A=T_{m+1},\quad B=T_{m-1}.
\]

For the outer variable let `v_j=U_j(t/2)`, `R_k=sum_(j=0)^k v_j`, and

\[
Z_k=AR_k+BR_{k-1},\quad
M_k=2P1+3y^2Z_k.
\]

The needed fixed proxy polynomials are

\[
J=y(t-2),\quad V=3y^2PP1,\quad K=2PP1^2.
\]

The conclusions proved below are

\[
M_k\text{ is a strict supported folded-cone polynomial},\qquad
H(JZ_k)<_{\rm lr}H(VZ_k+K). \tag{1}
\]

Together with the unconditional recurrence reduction in
`general_one_turn_reduction.md`, these are precisely the remaining
multiplier and proxy steps for strict Local TP2 at `L^mR^k`.

## 1. A sufficient fixed-boundary criterion

For each fixed `m>=2`, it is enough to have a number `gamma_m>12` such
that, for every `r in [-2,2]`,

\[
\delta_0(t-r)\ge4(t-r)(2),\qquad
\delta_0(A(t-r)+B)\ge\gamma_m[A(t-r)+B](2), \tag{2}
\]

and, writing `j=H(J)`, `v=H(V)`, `k=H(K)`,

\[
w_n:=j_nv_{n+1}-j_{n+1}v_n>0,
\qquad
\gamma_m w_n>2J(2)k_n
\quad(0\le n\le m+3). \tag{3}
\]

The finite interval `2<=m<=390` and the uniform tail `m>=391` are
proved separately below.

## 2. Propagating the central mass bound through every outer index

The compatible Jacobi-resolvent representation of `Z_k` has the form

\[
Z_k=\sum_{i\in I}\lambda_i Z_i,\qquad
Z_i=[A(t-r_i)+B]\prod_{\ell\ne i}(t-r_\ell),
\]

where the `k` values `r_l` are the roots of the outer prefix `R_k` in
its independent variable. The active residues satisfy
`lambda_i>0`, `sum lambda_i=1`, and `|I|<=k`. Each summand has one
template and exactly `k-1` propagator factors. Its supported folded
defects are strict, and any two summands have nonnegative symmetrized
mixed kernel minors, by the separate one-turn kernel theorem.

The central Cauchy--Binet term for a cone product gives
`delta_0(FG)>=delta_0(F)delta_0(G)`. Therefore (2) implies

\[
\delta_0(Z_i)\ge\gamma_m4^{k-1}Z_i(2).
\]

At `x=2` the ratios

\[
\frac{Z_i(2)}{R_k(2)}=A(2)+\frac{B(2)}{t(2)-r_i}
\]

lie strictly between `A(2)` and `2A(2)`, since `B(2)<=A(2)` and
`t(2)-2>1`. Thus every `Z_i(2)>Z_k(2)/2`. Pairwise compatibility,
the squared residue weights, and `4^(k-1)>=k` now give

\[
\begin{aligned}
\delta_0(Z_k)
&\ge\sum_i\lambda_i^2\delta_0(Z_i)\\
&>\frac{\gamma_m4^{k-1}}{2k}Z_k(2)
\ge\frac{\gamma_m}{2}Z_k(2)>6Z_k(2).
\end{aligned} \tag{4}
\]

This includes `k=1`. No outer-index exceptions are introduced.

## 3. The exact multiplier

Write `Q=y^2Z_k` with half-row `h`. The known cone factor `y^2` has
half-row `(3,2,1)` and defects `(4,0,1)`. Product closure, using the
strict supported defects of `Z_k`, gives strict supported defects for
`Q`. In the two terminal positions one retains the last positive
adjacent minor of `K_(y^2)`; at the other positions one can retain its
first positive adjacent minor.

In the opposite commuting order, the central intermediate pair gives

\[
\delta_2(Q)\ge\delta_0(Z_k)\delta_2(y^2)=\delta_0(Z_k).
\]

Since `h_3<=Q(2)=9Z_k(2)`, (4) implies `3delta_2(Q)>2h_3`.
The exact defects of `M_k=3Q+2P1` are

\[
\begin{aligned}
\delta_0(M_k)&=9\delta_0(Q)+24(h_0-h_1)+12h_2+8,\\
\delta_1(M_k)&=9\delta_1(Q)+12(h_1-h_2)+6h_3+4,\\
\delta_2(M_k)&=9\delta_2(Q)-6h_3,\\
\delta_n(M_k)&=9\delta_n(Q)\quad(n\ge3).
\end{aligned}
\]

All are strictly positive, proving the first assertion of (1).

## 4. Absorbing the exact proxy remainder

Both `J` and `K` have degree `m+3`; `V` has degree `m+4`. Positive
adjacent minors in (3) give every ordered minor of their two-row
coefficient matrix a nonnegative sign. Apply Cauchy--Binet after
multiplying these rows by `K_(Z_k)`. For `0<=n<=m+3`, retain the
intermediate pair `(n,n+1)`. Every adjacent principal minor of the
folded cone kernel `K_(Z_k)` is at least `delta_0(Z_k)`, so

\[
M_n(JZ_k,VZ_k)\ge w_n\delta_0(Z_k)
>\tfrac12\gamma_mw_nZ_k(2).
\]

The possible negative contribution of `K` is bounded by

\[
M_n(JZ_k,K)\ge-J(2)Z_k(2)k_n.
\]

Condition (3) therefore gives strict positivity after adding `K`.
For `n>=m+4` the correction vanishes. Retain the intermediate pair
`(m+3,m+4)` instead. Its base minor is positive, and the corresponding
adjacent kernel minor of `Z_k` is strictly positive whenever
`n-(m+3)<=deg Z_k`. This covers every remaining supported comparison
index, including the terminal one. The second assertion of (1)
follows.

## 5. Exact finite bridge, `2<=m<=390`

The standalone exact-integer/rational generator
`fulltree_oneturn_mass_proxy_cert.py` constructs the inner Chebyshev
rows directly by recurrence. For each of these 389 indices it computes
every base minor `w_n` and sets

\[
\gamma_m=2\left\lceil\max_{0\le n\le m+3}
\frac{J(2)k_n}{w_n}\right\rceil+13.
\]

All 77,800 base minors are positive. This choice has `gamma_m>12`
and the strict second inequality of (3). For each `m`, the script
then verifies the three exact degree-two Bernstein coefficients for
each of the two margins in (2), with `r=2-4u`, `0<=u<=1`.
Every one of these 778 continuum margin arrays is strictly positive.
The exact arrays, constants, and minimum fixed-proxy residuals are
saved in `fulltree_oneturn_mass_proxy_certificates.json`.

These are exhaustive proofs of the explicitly bounded interval and
the full parameter interval; no sampling or extrapolation is used.

## 6. Analytic tail, `m>=391`

The quantitative single-block and smoothed-propagator theorem supplies
the conservative strengths

\[
L_r=A(t-r)+B\text{ is }\lambda_L\text{-strong},\quad
\lambda_L=3\,2^{2m-3},
\]
\[
J=y(t-2)\text{ is }\lambda_J\text{-strong},\quad
\lambda_J=3\,2^{m-2}.
\tag{5}
\]

The sharp trace theorem supplies `lambda_t=3*2^(m-1)` strength for
`t-r`. A nonincreasing half-row of degree `d` has central entry at
least its mass divided by `2d+1`. Consequently

\[
\frac{\delta_0(t-r)}{(t-r)(2)}
\ge\frac{3\,2^{m-1}}{2m+5}\ge4,
\]
\[
\frac{\delta_0(L_r)}{L_r(2)}
\ge\frac{\lambda_L}{4m+7}=: \gamma_m>12.
\tag{6}
\]

It remains to prove (3) without any growing-degree fixed-row scan.
The identity

\[
V=P1\,J+R,\qquad R=yP1^2,
\qquad H(R)=(14,11,5,1)
\]

is exact. Also `M_n(J,xJ)=delta_n(J)`, so decrease of the row of `J`
gives

\[
w_n=\delta_n(J)+M_n(J,R)
\ge(\lambda_J-14)j_n>0. \tag{7}
\]

Put `Q=y^2P`. Since `P>=P1`, `y^2>=y`, and `P1^2<=2y^2`
coefficientwise in the Laurent basis, one has

\[
J=3Q-yP1\ge2Q,\qquad K=2PP1^2\le4Q\le2J. \tag{8}
\]

The inner recurrence at `x=2` gives
`T_m(2)<=(7^(m+1)-1)/6`, whence `P(2)<=4*7^m` and
`J(2)<=108*7^m`. For `m>=6`, `lambda_J-14>=lambda_J/2`.
Thus the sufficient scalar inequality

\[
\left(\frac87\right)^m>3072(4m+7) \tag{9}
\]

implies

\[
\lambda_L(\lambda_J-14)>4(4m+7)J(2).
\]

Using (6)--(8), this proves
`gamma_m w_n>4J(2)j_n>=2J(2)k_n`, exactly (3).
Inequality (9) holds already at 106 and propagates because its
left-to-right ratio is multiplied by
`8(4m+7)/[7(4m+11)]>1` for `m>=6`. The exact scalar checks are in
`fulltree_oneturn_mass_proxy_tail.py` and its result artifact.

The finite bridge and this analytic tail discharge (2)--(3) for
every `m>=2`. The proof is uniform in `k` throughout.
