# Completion of the arbitrary-inner-index one-turn proof

**Lane status: PROVED_INTERNAL.** This is an internal proof assembly,
with explicit certificate and audit dependencies. It is not a formal
promotion to an externally reproduced or independently published result.

This note completes the previously implicit single-block and smoothed
tail arguments and states the resulting one-turn theorem. It uses the
previously proved folded-kernel, prefix-factorization, and normalized
block results explicitly listed below. The result concerns `L^m R^k`;
it does **not** assert Local TP2 on paths with arbitrarily many turns.

Put `x=q+q^-1`, `y=x+1`,

`T_m=sum_(j=0)^m U_j(x+3/2)`, `P=1+yT_m`,
`t=3yP-x=3y^2T_m+2x+3`, `A=T_(m+1)`, `B=T_(m-1)`.

The Fourier half-row is denoted `H`, and

`delta_n(h)=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2)`.

Negative indices are reflected and entries beyond the support are zero.
The phrase lambda-strong means `delta_n(h)>=lambda h_n` throughout
the positive support. The previously proved strength-product lemma and
all-minor strength theorem are used, not closure under arbitrary sums.

## 1. Additional prefix bounds supplied by exact residue certificates

The eight residue parameter boxes are exactly those in
`mixed_kernel_pureleft_multiplier.md`; removed scaled quartics are
16-strong by `mixed_kernel_sharp_strength.md`. For every residue `R`
of degree `d`, `fulltree_oneturn_remaining.py` certifies on the entire
parameter box that both

`2^d yR` and `2^d y^3R` are `2^(d-1)`-strong.

The certificate consists of every exact rational tensor-Bernstein
coefficient of each supported defect margin. It is saved in
`fulltree_oneturn_remaining_certificates.json`. Its separately listed
`m=1` cases prove the same assertion for the missing small prefix.
Product closure, and `m=d+4r` for the remaining `r` quartics, give

`yT_m` and `y^3T_m` are `2^(m-1)`-strong for every `m>=1`.       (1)

The normalized degree-16 block result from
`fulltree_oneturn_normalized_tail.md` also gives

`eta(yT_m)>=c0 sigma^m`, `c0=1/400000000`, `sigma=59/100`.       (2)

Here `eta(h)=min_n delta_n(h)/h_n^2`. To check the constant, reserve
at most three further quartics in the residue, leaving degree `d<=18`.
The scaled smoothed residue is `2^(d-1)`-strong and has mass at most
`3*2^d*(9/2)^d`. Its normalized defect is therefore at least
`1/[6*(9/2)^d]`. Each further degree-16 normalized block loses at
most a factor 4352 by the normalized product theorem. The exact
inequalities

`4352 sigma^16<1`, `6c0((9/2)sigma)^18<1`

prove (2) because `m=d+16r`. For `m=1` the explicit row
`H(yT_1)=(8,6,2)` has defects `(8,16,4)`, which also proves (2).

## 2. The smoothed shifted trace, at every inner index

For all `m>=1` and `r in [-2,2]`,

`y(t-r)` is `3*2^(m-2)`-strong.                              (3)

The complete degree-two Bernstein certificates for `m=1,2,3` occur
under label `yf` in `fulltree_oneturn_single_finite_results.json`.
For `m>=4`, put `lambda=2^(m-1)>=8`, `h=H(y^3T_m)`, and
`a=3-r in [1,5]`. By (1), `h` is lambda-strong. Its terminal
coefficient is `2^m=2lambda`, so every supported coefficient is
at least `2lambda`. It is nonincreasing. Also `h_0<=2h_1`:
write `h=H(yQ)` with `Q=y^2T_m` and nonnegative half-row `p`;
then `h_0=p_0+2p_1` and `h_1=p_0+p_1+p_2`.

The row `b=H(y(t-r))` is `3h+(a+4,a+2,2,0,...)`. Exact expansion
gives the following changes from `9delta_n(h)`:

```
n=0: (6a+30)h0-(12a+24)h1+(3a+12)h2-a^2+2a+16
n=1: (6a+12)h1-6h0-(3a+24)h2+(3a+6)h3+a^2+2a-8
n=2: 12h2-3(a+2)h3+6h4+4
n=3: -6h4
n>=4: 0.
```

Subtract `mu b_n`, where `mu=3lambda/2`. Decrease, the bound on
`h0/h1`, and the interval for `a` yield, respectively,

```
n=0: >=(9lambda/2-24)h0+1-27lambda/2
     >=9lambda^2-123lambda/2+1 >0,
n=1: >=(9lambda/2-21)h1-5-21lambda/2
     >=9lambda^2-105lambda/2-5 >0,
n=2: >=(9lambda/2-9)h2+4-3lambda >0,
n=3: >=(9lambda/2-6)h3 >0,
n>=4: >=(9lambda/2)h_n >0.
```

The two quadratics are increasing on `lambda>=8` and have values
85 and 151 at 8. All displayed coefficients multiplying `h_n` are
positive there. This proves (3), including every support boundary.

## 3. Single blocks and smoothed midpoints for the infinite tail

The unsmoothed normalized-tail theorem has already established, for
`m>=391`, on the entire independent parameter cube `[-2,2]^3`,

`Hrs=A(t-r)(t-s)+B(t-c)` is `8H(B)_0`-strong.             (4)

We now prove the missing assertions

`Lr=A(t-r)+B` and `yLr` are `3*2^(2m-3)`-strong,         (5)
`yHrs` is `8H(yB)_0`-strong.                             (6)

The audited normalized product inequality is

`eta(FG)>=eta(F)eta(G)/[2(min(deg F,deg G)+1)]`.

Combine it with (2), with `eta(T_j)>=c0 sigma^j`, and with the
audited shifted-trace bound `eta(t-r)>=c0 sigma^m/2` for `m>=21`.
Both dominant single products `A(t-r)` and `yA(t-r)` have normalized
defect at least

`EL_m=c0^2 sigma^(2m+1)/[4(m+3)]`.

The dominant smoothed double product `yA(t-r)(t-s)` has normalized
defect at least

`EyH_m=c0^3 sigma^(3m+1)/[16(m+3)^2]`.

All three are folded-cone products. Their respective strengths are
`3*2^(2m-1)`, `3*2^(2m-1)`, and `9*2^(3m-2)`, because both
`A` and `yA` are `2^m`-strong and each trace factor is
`3*2^(m-1)`-strong.

Write `t0=H(t)_0`. The old proof gives `t0>=27*6^m/(2m+5)`.
For each single product its correction satisfies, coefficientwise,

`B <= A(t-r)/(t0-2)`, or `yB <= yA(t-r)/(t0-2)`.

Here `t0>=3`, so `1/(t0-2)<=3/t0<=epsilon_m`; the last
inequality follows from the displayed lower bound for `t0`.

For the double product the old coefficient-domination identity remains
valid after multiplication by the Laurent-nonnegative polynomial `y`.
Thus in all three cases, writing the dominant product as `F` and the
correction as `G`,

`0<=H(G)_n<=epsilon_m H(F)_n`, `epsilon_m=(2m+5)/(9*6^m)<1`.

The audited perturbation bound, valid also at zero and the upper support
boundary, is

`delta_n(F+G)>=delta_n(F)-(4epsilon+2epsilon^2)H(F)_n^2`.

Exact rational arithmetic at 391 gives both `EL_m>=12epsilon_m`
and `EyH_m>=12epsilon_m`. The consecutive ratios of these inequalities
are respectively

`6sigma^2 (m+3)(2m+5)/[(m+4)(2m+7)]`,
`6sigma^3 (m+3)^2(2m+5)/[(m+4)^2(2m+7)]`.

Both exceed one at 391 and increase thereafter, since each nonconstant
factor increases. Hence the inequalities hold for every `m>=391`.
The perturbation costs at most half of `delta_n(F)`. As
`H(F+G)_n<=2H(F)_n`, the sum is at least one quarter as strong as
the dominant product. This proves (5).

For (6), additionally use

`H(yB)_0 <= (yB)(2)=3B(2) <= (7^m-1)/2`,
`9*2^(3m-2) >= 96(7^m-1)/6` for every `m>=391`.

The latter is checked exactly at 391 and propagated by
`8(7^m-1)-(7^(m+1)-1)=7^m-7>=0`. This proves (6).

## 4. The finite bridge and relative-minor conclusion

For `1<=m<=390`, the two single blocks in (5) have the complete
degree-two interval certificates in `fulltree_oneturn_single_finite.py`
and its result file. There are no untested values of `r` or supported
indices: each margin has exactly three Bernstein coefficients.

For the same finite range, (4) and (6) have complete three-parameter
tensor-Bernstein certificates in `fulltree_oneturn_finite.py`, using
the original and `--smooth` modes. The independent ordinary-x verifier
in `fulltree_oneturn_finite_independent.py` reconstructs the rows and
all Bernstein margins separately. The stored full runs agree in every
per-case SHA-256 digest and minimum, for all 390 indices in both modes.
They contain respectively 6,239,025 and 6,249,555 strictly positive
integer margins. These counts and matches are reproduced by
`recovery_oneturn_checks.py`.

Consequently (4)--(6) hold for all `m>=1`. The relative-minor corollary
of `mixed_kernel_all_minor_strength.md` now gives

`det K_Hrs >= 4 det K_B`,
`det K_(yHrs) >= 4 det K_(yB)`                           (7)

on every ordered pair of rows and columns. Its hypotheses include
coefficientwise domination, immediate here from the positive constant
coefficient of each shifted trace and `A>=B`. The reference rows are
nonnegative and nonincreasing: `B=1` when `m=1`, and `yB=y` then has
row `(1,1)`; for larger `m`, the prefix strength results give decrease.
Thus even the `m=1` smoothed reference, which itself is not in the
folded cone, satisfies the corollary's actual hypotheses.

## 5. Jacobi compatibility, including the low outer indices

For roots `r,s in [-2,2]`, let

`F=A(t-r)(t-s)+B(t-s)`,
`G=A(t-r)(t-s)+B(t-r)`.

Their midpoint is `Hrs` with `c=(r+s)/2`, and `F-G=(r-s)B`.
On any ordered kernel minor,

`mixed(K_F,K_G)=2det K_Hrs-(r-s)^2 det K_B/2`.

The same identity holds after multiplying `F,G,Hrs,B` by `y`.
If the reference minor is nonpositive, the right side is nonnegative
because the midpoint kernel is TP2. If it is positive, (7) and
`(r-s)^2<=16` give the same conclusion. Therefore both unsmoothed
and smoothed pairs are compatible, without requiring the reference
kernel to be TP2.

For `p_N(t)=U_N(t/2)` or `U_N(t/2)+U_(N-1)(t/2)`, the established
Jacobi resolvent is

`p_(N-1)/p_N=sum_i lambda_i/(t-r_i)`,
`lambda_i>0`, `sum_i lambda_i=1`, `r_i in [-2,2]`.

Thus `A p_N+B p_(N-1)` is the weighted sum of

`[A(t-r_i)+B] product_(ell != i)(t-r_ell)`.

Each summand is a strict folded-cone product by (5) and trace strength.
For each pair the common omitted-root product is a cone factor and
the remaining pair is exactly `F,G`. Compatibility is preserved by
common cone multiplication, by Cauchy--Binet. Every minor of the sum
is therefore nonnegative; supported defects are strictly positive
because diagonal terms have positive squared residue weights and all
summands have the same degree.

The same argument, using `yLr` for the diagonal terms and `yF,yG`
for each off-diagonal pair, proves the assertion after multiplication
by `y`. It applies already to `N=1,2`: no common root factor is
needed in the smoothed compatibility step. At `N=0` the result is
`A` or `yA`, already strong by the prefix results.

For `v_j=U_j(t/2)`, `R_k=sum_(j=0)^k v_j`, it follows that

`q_k=y[A v_k+B v_(k-1)]`,
`Z_k=A R_k+B R_(k-1)`

have strict supported folded defects for every `k>=0`. For `Z_k`,
use the exact prefix factorizations from
`general_one_turn_kernel_theorem.md`. Multiplication by their outside
root factors also proves the assertion for `yZ_k`.

## 6. One-turn Local TP2 conclusion and its scope

The remaining multiplier and proxy steps are proved in
`fulltree_oneturn_mass_proxy.md`. Its only formerly unstated strength
inputs are precisely (3) and (5), now supplied. Its finite bridge
contains every `2<=m<=390`; its analytic tail uses the now-proved
`lambda_L=3*2^(2m-3)` and `lambda_J=3*2^(m-2)`. The Jacobi
compatibility and strictness required there have just been proved.

For each `m>=2,k>=1`, combine that result with the unconditional
recurrence and initial comparisons in `general_one_turn_reduction.md`:

`S_k <=lr y(t-2)Z_k <lr P(x+2)M_k <=lr D_k`.

All rows have the positive supported intervals needed for transitivity;
the middle comparison is strict at every index through `deg S_k`.
Hence the original strict Local TP2 inequality holds at every such
`L^mR^k`. The prior `m=1` mixed-ray theorem, all-right theorem
(`m=0`), and all-left theorem (`k=0`) cover the boundary cases.

**Result:** strict Local TP2 holds at `L^m R^k` for all integers
`m,k>=0`, subject to the explicitly cited audited foundation lemmas
and exact finite certificates. This strengthens the previously proved
fixed-`m` rays to an arbitrary initial left run. It does not handle
general paths such as `L^m R^k L^ell`, and is not a proof of the
full canonical-tree conjecture.

## 7. Reproducible dependency map

All filenames below are relative to the recovered research directory.
The source files preceding this recovery are read-only dependencies.

| Obligation | Proof and generator | Independent review or replay |
|---|---|---|
| Folded-kernel criterion and product closure | `continuation_kernel/folded_kernel_theorem.md` | Established foundation of the earlier ray results |
| Strength multiplication and arbitrary ordered minors | `mixed_kernel_strong_cone.md`, `mixed_kernel_all_minor_strength.md` | Earlier strength audits; direct arguments cited in Sections 1 and 4 |
| Exact eight-case inner root grouping | `continuation_bracket.md`, `mixed_kernel_pureleft_multiplier.md` | Earlier prefix and bracket audits |
| Sharp trace/prefix strengths | `mixed_kernel_sharp_strength.md`, `mixed_kernel_sharp_strength.py` | `mixed_kernel_sharp_strength_independent.md` and its generator/results |
| Degree-16 normalized block | `fulltree_normalized_block.cpp`, `fulltree_normalized_block_results.json` | `fulltree_normalized_block_independent_audit.md`, independent generator/results |
| Normalized product and unsmoothed tail | `fulltree_oneturn_normalized_tail.md` and `.py` | `fulltree_oneturn_normalized_tail_audit.md` |
| Additional y/y^3 residue strengths and small single blocks | `fulltree_oneturn_remaining.py`, `fulltree_oneturn_single_finite.py` and both result artifacts | `recovery_single_audit.py`, `recovery_single_audit.json` |
| Complete finite midpoint and smoothed midpoint interval | `fulltree_oneturn_finite.py`, both original/smoothed result artifacts | `fulltree_oneturn_finite_independent.py`, both independent result artifacts; `recovery_finite_audit.md` |
| Central mass, multiplier, and fixed proxy | `fulltree_oneturn_mass_proxy.md`, its certificate and tail generators/results | `recovery_mass_proxy_audit.py`, `.json`, `.md` |
| Exact canonical reduction and boundary rays | `general_one_turn_reduction.md`, `general_one_turn_first.md`, prior all-left/all-right and first mixed-ray results | Earlier ray and reduction audits |
| Newly explicit analytic assembly | This manuscript, `recovery_oneturn_checks.py` | New recovery audits record their own scope; no blanket external reproduction claim |

From a Linux bash terminal in this directory,
`python3 recovery_oneturn_checks.py` checks the four formal polynomial
identities, the seven exact rational tail gates, and the complete
primary/independent midpoint-record match. It also verifies the precise
scope of the stored single-block records. It writes only
`recovery_oneturn_checks_results.json`.

`python3 recovery_single_audit.py` and
`python3 recovery_mass_proxy_audit.py` independently reconstruct the
corresponding finite obligations. Their authored descriptions identify
what is recomputed and what remains a cited mathematical dependency.
The existing finite midpoint generators can be replayed with their
documented `--output` option into new filenames; the ordinary-basis
independent generator requires NumPy for exact object-array operations.
