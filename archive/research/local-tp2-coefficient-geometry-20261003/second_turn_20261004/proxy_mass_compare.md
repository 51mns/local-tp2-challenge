# Reversed-pair central mass, multiplier, and final comparison

This proves the mass and final proxy steps for the additional-turn ray,
for every `m>=0` and `N>=2`. It is a **scoped proof with explicit kernel
dependencies**, not a claim that a conditional full-tree premise is proved.
The required reversed-pair cone and Jacobi-compatibility theorem is supplied
separately by the `kernels_*` lane. The unconditional canonical recurrence
and initial LR transport are supplied by `reduction_*`. None of these
results asserts anything about arbitrary canonical-tree paths.

Put `y=x+1`, `P1=x+2`, `T_j=sum_(i=0)^j U_i((2x+3)/2)`, and

\[
X=1+yT_{m+1},\quad \tau=3yX-x,\quad c=T_m,\quad d=T_{m+2},
\]
\[
R_N(\tau)=\sum_{i=0}^NU_i(\tau/2),\qquad
Z_N=cR_N+dR_{N-1},\qquad C_N=1+yZ_N.
\]

The exact multiplier and fixed proxy are

\[
M_N=3yC_N-x+1=2P1+3y^2Z_N,
\]
\[
J=y(\tau-2),\quad V=3y^2XP1,\quad K=2XP1^2,
\qquad XP1M_N=VZ_N+K. \tag{1}
\]

Under the listed proved kernel dependencies the conclusions are

\[
\boxed{\delta_0(Z_N)>6Z_N(2),\quad M_N\text{ has strict supported folded defects},}
\]
\[
\boxed{H(JZ_N)<_{\rm lr}H(VZ_N+K)} \tag{2}
\]

for every `m>=0,N>=2`. The last inequality is strict at each comparison
index `0<=n<=deg(JZ_N)=2m+4+(m+3)N`. This is the middle strict comparison
needed in `S<=lr JZ_N <lr XP1M_N<=lr D`. The state `ell=0`, corresponding
to `N=1`, has the old orientation and is not covered or needed here.

## 1. Exact dependencies and a mass lemma

We use the established folded-kernel product/Cauchy--Binet theory,
central-product inequality `delta_0(FG)>=delta_0(F)delta_0(G)`, the
nonincreasing positive supported rows of strict folded-cone polynomials,
and the old sharp trace and smoothed-trace strengths at inner index
`m+1`. From the reversed-pair kernel theorem we use:

* `tau-r` and `L_r=c(tau-r)+d` are strict supported folded-cone
  polynomials, for all `r in [-2,2]`.
* The compatible resolvent expansion of `Z_N` has active positive
  weights `lambda_i`, `sum lambda_i=1`, at most `N` weights, and
  summands
  `Z_i=L_(r_i) product_(j!=i)(tau-r_j)`, with all roots in `[-2,2]`.
  Pairwise symmetrized kernel minors are nonnegative, so the central
  defect of the sum is at least the sum of its diagonal squared-weight
  defects. Supported defects of `Z_N` are strict.
* In the analytic inner tail `m>=410`, the reversed single template is
  `lambda_L=3*2^(2m-3)`-strong. The finite and analytic proof of this
  strength belongs to `kernels_*`; it is not supplied by a central-mass
  certificate alone.

The prefix identities `R_(2h)=U_h V_h` and
`R_(2h+1)=U_h V_(h+1)` explain the stated expansion directly:
`R_(2h-1)/R_(2h)=U_(h-1)/U_h` and
`R_(2h)/R_(2h+1)=V_h/V_(h+1)`. Their positive Jacobi residues are
active at respectively `h` and `h+1` roots; the other prefix roots have
zero residues. Reintroducing the outside root factors gives each active
summand exactly `N-1` propagators and retains `sum lambda_i=1`.

These are actual single-block and midpoint compatibility inputs, not
closure under arbitrary sums. In particular the smoothing factor `y`
is not assumed to be a folded-cone factor.

The summand masses satisfy `Z_i(2)>Z_N(2)/2`. Indeed, at `x=2`,

\[
\frac{Z_i(2)}{R_N(\tau(2))}=c(2)+\frac{d(2)}{\tau(2)-r_i},
\]

and the ratio lies between `c(2)` and `2c(2)`. To verify the latter
uniformly without assuming a reversed coefficient ordering, write
`a_j=T_j(2)`. Its recurrence is `a_j=7a_(j-1)-a_(j-2)+1`.
Since `a_j>=1`, `a_(m+1)<=7a_m+1` and
`a_(m+2)<=49a_m+8<=57a_m`. Meanwhile `tau(2)-2>=221`.
Thus `d(2)/(tau(2)-2)<c(2)`. (The kernel proof's stronger ordinary
coefficient domination `d<=16y^2c` also suffices.)

Suppose throughout the root interval

\[
\delta_0(L_r)>\gamma L_r(2),\qquad
\delta_0(\tau-r)>\alpha(\tau(2)-r).
\]

Product closure and compatibility give

\[
\delta_0(Z_N)>
\frac{\gamma\alpha^{N-1}}{2N}Z_N(2). \tag{3}
\]

If paired factors instead satisfy
`delta_0((tau-r)(tau-s))>kappa(tau(2)-r)(tau(2)-s)`, grouping the
`N-1` propagators in each summand gives the refined bound

\[
\delta_0(Z_N)>
\frac{\gamma\kappa^{\lfloor(N-1)/2\rfloor}
\alpha^{(N-1)\bmod2}}{2N}Z_N(2). \tag{4}
\]

Both formulas follow from `sum lambda_i^2>=1/N` and the strict summand
mass bound. This argument works at low outer indices and introduces no
assumed generic full-tree theorem.

## 2. A fixed finite proxy threshold

Write `j=H(J)`, `v=H(V)`, `k=H(K)`, and

\[
w_n=j_nv_{n+1}-j_{n+1}v_n,\qquad
\beta_m=\max_{0\le n\le m+4}\frac{J(2)k_n}{w_n}. \tag{5}
\]

The exact certificates prove `w_n>0` at every displayed index for
`0<=m<=409`, and `beta_m>6`. For this interval it suffices to prove
`delta_0(Z_N)>beta_m Z_N(2)`. The finite certificate constructs every
inner Chebyshev row directly by the recurrence in the Laurent basis.
Each central interval margin is represented by its complete degree-two
Bernstein coefficients after `r=2-4u`, `0<=u<=1`; all are strictly
positive. This is a continuum certificate, not root sampling.

For `3<=m<=409`, take

\[
\alpha=4,\qquad\gamma=2\lceil\beta_m\rceil+13.
\]

Every template and trace central margin is strictly positive. Since
`4^(N-1)/(2N)>=1` for `N>=2`, (3) gives the needed stronger mass bound.
The following small cases use the extra restriction `N>=2`.

| Inner index | Fixed threshold | Trace bound | Template bound | Outer range from mass propagation |
|---|---:|---:|---:|---|
| `m=0` | `beta=221/3` | `alpha=4/5` | `gamma=2` | Pair bound `kappa=80`, then `N>=5` |
| `m=1` | `beta=1517/6` | `alpha=5` | `gamma=40` | `N>=4` |
| `m=2` | `beta=2600/3` | `alpha=5` | `gamma=707` | Every `N>=2` |

For `m=2`, (3) is at least `5gamma/4=3535/4>2600/3` and increases
with `N`. For `m=1`, its first value at `N=4` is `625>1517/6`, then
it increases since the consecutive ratio is `5N/(N+1)>1`.

For `m=0`, `H(tau)=(63,50,24,6)`. The paired margin

`delta_0((tau-r)(tau-s))-80(tau(2)-r)(tau(2)-s)`

has the complete independent degree-(2,2) tensor-Bernstein array

`(486317,575113,666869,575113,768741,970001,666869,970001,1285693)`.

It is strictly positive on the entire independent square. Formula (4)
reduces to

\[
\delta_0(Z_N)>
\frac{80^{\lfloor(N-1)/2\rfloor}(4/5)^{(N-1)\bmod2}}N Z_N(2).
\]

The two parity bases are `1280` at `N=5` and `2560/3` at `N=6`,
both exceeding `221/3`. Each parity subsequence increases, with
consecutive ratio `80N/(N+2)>1`. Finally, the script constructs and
certifies the five exact finite outer cases `m=0,N=2,3,4` and
`m=1,N=2,3` directly. Every one has
`delta_0(Z_N)-beta_m Z_N(2)>0`. This covers the full outer range.

The complete result file `proxy_mass_results.json` contains all
85,895 positive fixed base minors summarized by their exact per-inner
minimum, 820 whole-interval central margin arrays, one paired-square
array, five exact outer central records, and exact tail scalar gates.
The script is standalone Python integer/Fraction code, without SymPy or
imports of the old parent implementation.

## 3. Analytic inner tail `m>=410`

At the old trace inner index `m+1`, the proved sharp bounds give

\[
\lambda_t=3\,2^m,\qquad
\lambda_J=3\,2^{m-1}.
\]

The reversed single-template strength from the separate kernel theorem
is `lambda_L=3*2^(2m-3)`. Degrees are `deg(tau-r)=m+3`,
`deg L_r=2m+3`. Therefore decrease of their half-rows gives

\[
\frac{\delta_0(\tau-r)}{\tau(2)-r}
\ge\frac{3\,2^m}{2m+7}\ge4,
\qquad
\frac{\delta_0(L_r)}{L_r(2)}
\ge\gamma_m:=\frac{3\,2^{2m-3}}{4m+7}>12. \tag{6}
\]

The weak signs in (6) are sufficient: the summand mass ratio in the
proof of (3) is strict. In particular `delta_0(Z_N)>gamma_m Z_N(2)`
for `N>=2`.

The old fixed identities remain exact with `X` in place of `P`:

\[
V=P1J+R,\qquad R=yP1^2,\qquad H(R)=(14,11,5,1).
\]

Thus `w_n=delta_n(J)+M_n(J,R)>=(lambda_J-14)j_n>0`.
Moreover `J>=2y^2X` and `K<=4y^2X<=2J` coefficientwise in the
Laurent basis. These follow from `X>=P1`, `y^2>=y`, and
`P1^2<=2y^2`; these coefficient inequalities do not assert that `y`
is a cone factor. The inner mass estimate gives

`J(2)<=108*7^(m+1)=756*7^m`.

The sufficient scalar gate is now

\[
(8/7)^m>10752(4m+7). \tag{7}
\]

It holds by exact rational arithmetic at `410` and propagates because
`8(4m+7)/(7(4m+11))>1` there and thereafter. Also
`lambda_J-14>=lambda_J/2`. Equation (7) consequently gives

\[
\lambda_L(\lambda_J-14)>4(4m+7)J(2),
\qquad \gamma_m w_n>2J(2)k_n. \tag{8}
\]

The trace mass, template gamma, smoothed strength, proxy scalar, and
direct proxy surplus gates are checked exactly in the same standalone
script; their consecutive ratios are greater than one at the tail
start and increase. This is an infinite tail argument, with the full
remaining interval explicitly certified above.

## 4. Exact multiplier and absorption of the correction

Let `Q=y^2Z_N`, with half-row `h`. The known cone factor `y^2` has
half-row `(3,2,1)` and folded defects `(4,0,1)`. Product closure and
the strict supported defects of `Z_N` imply strict supported defects
of `Q`: in `K_Q=K_(y^2)K_(Z_N)`, retain the intermediate pair
`(0,1)` for `n<=deg Z_N`, using `delta_0(y^2)=4`; for the two last
indices retain `(2,3)`, using `delta_2(y^2)=1` and the corresponding
strict adjacent minors of `K_(Z_N)`. In the reverse commuting order, retain the central
intermediate pair to get

\[
\delta_2(Q)\ge\delta_0(Z_N)\delta_2(y^2)=\delta_0(Z_N).
\]

Since `h_3<=Q(2)=9Z_N(2)` and `delta_0(Z_N)>6Z_N(2)`,
`3delta_2(Q)>2h_3`. Direct expansion of (1) yields

\[
\begin{aligned}
\delta_0(M_N)&=9\delta_0(Q)+24(h_0-h_1)+12h_2+8,\\
\delta_1(M_N)&=9\delta_1(Q)+12(h_1-h_2)+6h_3+4,\\
\delta_2(M_N)&=9\delta_2(Q)-6h_3,\\
\delta_n(M_N)&=9\delta_n(Q)\quad(n\ge3).
\end{aligned}
\]

All are strictly positive, proving the multiplier assertion.

For the final comparison, all ordered minors of the two-row fixed
matrix `(H(J),H(V))` are nonnegative because all adjacent fixed
minors are positive. Apply Cauchy--Binet after multiplying by
`K_(Z_N)`. For `0<=n<=m+4`, retain the intermediate pair `(n,n+1)`;
its kernel minor is at least `delta_0(Z_N)`. Hence

\[
M_n(JZ_N,VZ_N)\ge w_n\delta_0(Z_N).
\]

The correction contributes at worst

\[
M_n(JZ_N,K)\ge-J(2)Z_N(2)k_n.
\]

For the finite interval, `delta_0(Z_N)>beta_m Z_N(2)` and (5)
make their sum strict. For the tail, `delta_0(Z_N)>gamma_m Z_N(2)`
and (8) give the same conclusion. For `n>=m+5`, `K` vanishes.
Retain instead the positive fixed base minor at `(m+4,m+5)`; the
associated adjacent kernel minor is strictly positive whenever
`n-(m+4)<=deg Z_N`. This covers every remaining supported comparison
index, including the terminal index. It proves the final assertion (2).

The only comparison inputs still external to this manuscript are the
specified actual reversed kernel theorem and the specified unconditional
canonical LR reduction. No conditional global premise is promoted by
these certificates.
