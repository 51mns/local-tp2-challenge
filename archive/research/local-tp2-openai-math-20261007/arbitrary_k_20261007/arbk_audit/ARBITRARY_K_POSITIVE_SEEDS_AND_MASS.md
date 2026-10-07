# Positive seed recurrence and mass-scale correction domination

**Status: PROVED_INTERNAL.** These algebraic and coefficient inequalities
hold for every `m>=0,k>=2`. They are new sufficient estimates for arbitrary
right-run length, not a proof of the subsequent Local TP2 ray on their own.
The only cone facts used below concern the already proved one-turn
polynomials; no cone property of the new seed is assumed.

All inequalities between polynomials mean coefficientwise inequalities
after `x=q+q^-1`, unless explicitly described as ordinary-coefficient
inequalities. Every ordinary-coefficient inequality with nonnegative
difference also implies the displayed Laurent inequality.

## 1. Canonical notation and a positive recurrence

Put `y=x+1`, `p=x+2`, `z=2x+3`,

\[
u_j=U_j(z/2),\quad T_m=\sum_{j=0}^m u_j,\quad T_{-1}=0,
\quad Y=1+yT_m,\quad \tau=3yY-x=z+3y^2T_m.
\]

For the old right run from `L^m`, let `C_j` be its center after `j` right
moves, with `C_-1=1,C_0=1+yT_(m+1)`. The original mutation gives

\[
C_{j+1}=\tau C_j-C_{j-1}-xY.
\]

Define `a_j=(C_j-Y)/y` and `kappa=Y(3Y-2)`. Direct substitution gives

\[
\boxed{a_{j+1}=\tau a_j-a_{j-1}+\kappa,\qquad
a_{-1}=-T_m,\quad a_0=u_{m+1}.}\tag{1}
\]

Let `v_j=U_j(tau/2)`, `R_j=sum_(i=0)^j v_i`, with `v_-1=R_-1=0`.
Solving (1) yields the exact formula

\[
\boxed{a_j=u_{m+1}v_j+T_m v_{j-1}+\kappa R_{j-1}
\quad(j\ge0).}\tag{2}
\]

Each summand has nonnegative ordinary coefficients. For `v_j` and `R_j`,
this follows also from their real-root factorizations: each factor is
`tau-r` with `r in [-2,2]`, and `tau-2` has nonnegative ordinary
coefficients. Thus `a_j>=0` and `a_j>=kappa R_(j-1)` for `j>=1`.

The initial difference is `a_0-a_-1=T_(m+1)>0`, and (1) implies

\[
a_{j+1}-a_j=(\tau-2)a_j+(a_j-a_{j-1})+\kappa\ge0.
\]

In particular `a_(j+1)>=(tau-1)a_j+kappa`. At the new prefix `L^mR^k`,

\[
X=C_{k-1},\quad A=a_k,\quad B=a_{k-2},\quad t=3yX-x.
\]

The seeds are therefore nonnegative and satisfy

\[
\boxed{A\ge(\tau-1)^2B,\qquad
A\ge(\tau^2-\tau-1)B+(\tau+1)\kappa.}\tag{3}
\]

For the second inequality use
`a_k=(tau²-1)a_(k-2)-tau a_(k-3)+(tau+1)kappa` and
`a_(k-3)<=a_(k-2)`. For `k=2`, this last inequality is also valid because
`a_-1=-T_m<=a_0`. The polynomial `tau²-tau-1` itself has nonnegative
ordinary coefficients. If `b=H(tau)_0`, (3) in particular gives
`H(A)>=(b²-b-1)H(B)`.

## 2. Extracting the fixed correction exactly

Set

\[
K_0=3yY-x+1=\tau+1,\quad K=XpK_0,\quad J=y(t-2),
\quad L_r=A(t-r)+B.
\]

The following identity is exact in ordinary polynomials:

\[
\boxed{\kappa=T_mK_0+1+2xT_m.}\tag{4}
\]

To verify it, write `Y=1+yT_m`, so
`kappa=1+4yT_m+3y²T_m²` and
`T_mK0=(z+1)T_m+3y²T_m²`; their difference is `1+2xT_m`.
Thus `kappa>=T_mK0`, with no subtraction or cone closure required.

## 3. Central coefficients retain an exponential fraction of mass

Let

\[
M=\tau(2)-2=5+27T_m(2)\ge32,\qquad d=\deg\tau=m+2,
\qquad D=2dk-3,
\qquad\alpha=\frac{T_m(2)M^{k-1}}{D}.\tag{5}
\]

The inherited one-turn folded-cone results imply that `T_m`, each
`tau-r` for `r in [-2,2]`, and hence `R_j(tau)` and `K0` are in the cone.
At `m=0`, the shifted factor is directly checked from
`tau=3x²+8x+6`; this boundary is also included in the existing auxiliary
trace theorem. Products of these factors are in the cone. For a degree-e
cone polynomial `P`, its decreasing half-row gives

\[
H(P)_0\ge\frac{P(2)}{2e+1}.
\]

The `j` spectral roots of the monic polynomial `R_j` lie in `[-2,2]`, so
`R_j(tau)(2)>=M^j`. Now `deg(T_mR_(k-1))=dk-2`, so its central
coefficient is at least `alpha`. From (2) and (4),

\[
\boxed{A\ge T_mR_{k-1}K_0\ge\alpha K_0.}\tag{6}
\]

Similarly `a_(k-1)>=T_mR_(k-2)K0`, whose degree is again `dk-2` and
whose mass is at least `T_m(2)M^(k-2)(M+3)`. Its central coefficient
is therefore at least `alpha`. Because

\[
t=\tau+3y^2a_{k-1},\qquad H(y^2)_0=3,
\]

we obtain

\[
\boxed{s:=H(t)_0-2\ge9\alpha.}\tag{7}
\]

Only the positive *lower-bound product* was assumed to be in the cone in
this step. No assertion that `a_(k-1)` is in the cone is needed.

## 4. The two corrections share a mass-squared domination factor

For every `r in [-2,2]`, the constant Laurent coefficient of `t-r` is at
least `s`; all its other coefficients are nonnegative. Hence

\[
L_r\ge sA\ge\alpha sK_0.
\]

Since `X>=Y>=p` in ordinary coefficients, `yX>=p`, and therefore

\[
J=3y^2X-yp\ge2y^2X.
\]

In the Laurent coefficient order `y²>=p` and `y²>=3`, as their half-rows
are respectively `(3,2,1)`, `(2,1)`, and `(3)`. Consequently

\[
\boxed{JL_r\ge2\alpha sK,\qquad
y^2L_r\ge3\alpha sK_0.}\tag{8}
\]

A common lower bound is

\[
\boxed{c=18\alpha^2\quad\text{in both inequalities}.}\tag{9}
\]

Finally `T_m(2)=(M-5)/27>=M/32` for `M>=32`. Thus the entirely explicit
weaker bound

\[
\boxed{c\ge\frac{9M^{2k}}{512(2dk-3)^2}}\tag{10}
\]

holds uniformly in both indices. Its exponential scale uses the full
old-trace evaluation mass, with only a quadratic degree loss. This is
stronger in the right-run parameter than an estimate based solely on the
old trace's central coefficient. Absorption into normalized defects still
requires the independent quantitative seed and trace inequalities.

The frequently used weaker mass bound `M>=27*6^m` is elementary:
`u_j(2)=7u_(j-1)(2)-u_(j-2)(2)` and these values increase, so
`u_j(2)>=6u_(j-1)(2)>=6^j`; then `T_m(2)>=u_m(2)`.
