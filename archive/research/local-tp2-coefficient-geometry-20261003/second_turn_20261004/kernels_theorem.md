# Reversed coefficient blocks on the additional-turn ray

**Status: PROVED_INTERNAL, subject to the stated audited foundation
dependencies.** The primary exact finite replay and explicit analytic
tail are complete. Independent replay and audit have their own records.

This proof concerns the folded kernels of the reversed coefficient pair.
It is a dependency for the `L^m R L^ell` reduction, not by itself a proof
of Local TP2. Its finite bridge is recorded in `kernels_certificate.py`
and `kernels_certificate_results.json`; the analytic tail below is an
infinite argument. The independent audit is recorded separately.

Put `x=q+q^-1`, `y=x+1`, `z=2x+3`,

`T_j=sum_(i=0)^j U_i(z/2)`, `T_-1=0`,

`c=T_m`, `d=T_(m+2)`, `tau=3y^2 T_(m+1)+z`, `m>=0`.

For independent `r,s,u in [-2,2]`, write

`L_r=c(tau-r)+d`, `H_(r,s,u)=c(tau-r)(tau-s)+d(tau-u)`.

Write `h_n` for the Laurent half-row of a polynomial and extend it
symmetrically at negative indices and by zero past its degree. The defect
is `delta_n=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2)`.
Strength `lambda` means `delta_n>=lambda*h_n` on every supported index.

## 1. Precise block theorem

For every `m>=0` and the entire indicated independent parameter boxes:

1. `L_r` and `yL_r` are `lambda_L=3*2^(2m-3)`-strong.
2. Put `alpha=h_0(tau)-2>0`. Then

   `alpha*delta_n(H)>=8*h_0(d)*h_n(H)`,

   `alpha*delta_n(yH)>=8*h_0(yd)*h_n(yH)`.

3. For every ordered pair of rows and columns of the infinite folded
   kernels,

   `det K_H>=4 det K_d`, `det K_(yH)>=4 det K_(yd)`.

All the half-rows in 1 and 2 have positive interval support, and their
supported defects are strictly positive. The strength statement in 2 is
deliberately scaled. The unscaled assertion `H is 8*h_0(d)-strong` is
false at small `m`: at `m=0` its terminal coefficient is 36, whereas
`8*h_0(d)=160`. No assumption that reversal preserves an earlier theorem
is made here.

## 2. The scaled all-minor implication

The parent all-minor strength theorem says that a lambda-strong row gives

`det K_H[i,j;k,l]>=lambda*K_H(i,k)`

whenever both diagonal entries are positive. Let a nonnegative reference
row `b` satisfy `b_n<=b_0`, and suppose `H>=alpha*B` coefficientwise and
`lambda*alpha>=8b_0`. A positive reference minor has both diagonal
entries positive, so the corresponding `H` entries are positive. Hence

`det K_H>=lambda*K_H(i,k)>=8b_0*K_B(i,k)`

`>=4*K_B(i,k)*K_B(j,l)>=4 det K_B`.

A nonpositive reference minor is covered by TP2 of `K_H`. This proof has
no finite restriction on kernel indices and does not require `B` itself
to lie in the folded cone.

Here `tau-u` has central coefficient at least `alpha` and all other
Laurent coefficients nonnegative. Therefore `H>=alpha*d` and
`yH>=alpha*yd`. Both reference rows are decreasing: `T_(m+2)` is in the
parent sharp prefix theorem, and `yT_(m+2)` is in the parent smoothed
prefix theorem. In particular `b_n<=b_0` holds in both modes. Taking
`lambda=8b_0/alpha` proves assertion 3 from assertion 2.

## 3. Exact correction domination for the reversed pair

The inner prefix recurrence is

`T_(j+1)=z*T_j-T_(j-1)+1`.

All its ordinary coefficients are nonnegative, and `T_j>=1`.
Consequently

`T_(j+1)<=(z+1)*T_j`,

`d<=(z+1)^2*c=4(x+2)^2*c<=16y^2*c`.

The final inequality follows from
`16y^2-(z+1)^2=12x^2+16x`. These are ordinary-coefficient inequalities,
so they also hold in the Laurent basis.

Let `a_0=h_0(T_(m+1))`, `J=tau-2` and `tau_0=h_0(tau)`.
The elementary inner recurrence also proves `U_j>=U_(j-1)` in ordinary
coefficients: from this at index `j`,
`U_(j+1)-U_j>=(z-2)U_j>=0`. It then gives
`U_(j+1)>=(z-1)U_j=2yU_j`, so `T_j>=2^j y^j`.
The central coefficient of `y^j` is at least the average of its `2j+1`
coefficients (the symmetric trinomial row is unimodal). Therefore

`a_0>=6^(m+1)/(2m+3)`.

Also `J>=3a_0*y^2`. Since `T_(m+1)>=T_1` and
`h_0(3y^2 T_1+z)=63`, the trace has `tau_0>=63`, so
`J>=(tau+2)/3`; this follows by separating the nonnegative Laurent
remainder from the central coefficient. For independent parameters,

`(tau-r)(tau-s)>=J^2>=a_0*y^2*(tau+2)`.

Thus, writing `F=c(tau-r)(tau-s)`, `G=d(tau-u)`,

`0<=G<=epsilon_H F`, `epsilon_H=16(2m+3)/6^(m+1)`.

Likewise, for `F_L=c(tau-r)`, `G_L=d`,

`0<=G_L<=epsilon_L F_L`, `epsilon_L=epsilon_H/3`.

All these Laurent coefficient inequalities remain valid after
multiplication by `y`, which has nonnegative Laurent coefficients.

## 4. The uniform analytic tail, m>=410

Use the audited constants `sigma=59/100`, `c0=1/400000000`.
The parent normalized-prefix proofs give, for every `m>=1`,

`eta(c)>=c0*sigma^m`, `eta(yc)>=c0*sigma^m`.

The shifted-trace proof at inner index `m+1` gives, for `m>=20`,

`eta(tau-r)>=c0*sigma^(m+1)/2`.

The normalized product theorem is

`eta(AB)>=eta(A)eta(B)/(2(min(deg A,deg B)+1))`.

Since `deg(c)=m`, `deg(yc)=m+1`, and `deg(tau)=m+3`, both single
dominant products have normalized defect at least

`E_L=c0^2*sigma^(2m+1)/(4(m+2))`,

and both double dominant products have normalized defect at least

`E_H=c0^3*sigma^(3m+2)/(16(m+2)(m+4))`.

The sharp strength-product theorem gives their respective strengths

`Lambda_L=3*2^(2m-1)`, `Lambda_H=9*2^(3m-1)`.

For a folded-cone row `f` and a correction `0<=g<=epsilon*f`, the audited
boundary-aware perturbation estimate is

`delta_n(f+g)>=delta_n(f)-(4epsilon+2epsilon^2)f_n^2`.

It holds at index 0 and at the terminal support index. Exact rational
arithmetic in `kernels_checks.py` proves at `m=410` that

`epsilon_H<1`, `E_H>=12epsilon_H`, `E_L>=12epsilon_L`.

The consecutive ratios of `E_H/epsilon_H` and `E_L/epsilon_L` are

`6sigma^3*(m+2)(m+4)(2m+3)/[(m+3)(m+5)(2m+5)]`,

`6sigma^2*(m+2)(2m+3)/[(m+3)(2m+5)]`.

Every nonconstant factor is increasing in `m`; both ratios exceed 1 at
410. Thus all three gates hold for every `m>=410`. The perturbation loses
at most half the original defect, while `f+g<=2f`. Hence each sum
retains at least one quarter of its dominant strength. This proves
assertion 1 on the tail and gives midpoint strength

`lambda_H=9*2^(3m-3)`.

The elementary mass estimate `T_j(2)<=(7^(j+1)-1)/6` gives

`8*h_0(yd)<=4(7^(m+3)-1)`.

At 410 the exact inequality

`9*2^(3m-3)>=4(7^(m+3)-1)`

holds. It propagates because the left side multiplies by8, whereas
`8(7^(m+3)-1)-(7^(m+4)-1)=7^(m+3)-7>=0`. The smoothed reference bound
also covers the unsmoothed one. Since `alpha>=1`, assertion 2 follows
on the entire infinite tail.

## 5. The exact finite bridge, 0<=m<=409

The finite bridge uses every supported Fourier index and every
tensor-Bernstein coefficient on the whole parameter box. It has four
records per inner index: single and midpoint, each unsmoothed and
smoothed. All 1,640 records pass, with 14,766,150 strictly positive exact
integer margins. `kernels_certificate_results.json` records the minimum, exact
scaling, coefficient count and SHA-256 digest of each record.

Substitute `r=-2+4a`, `s=-2+4b`, `u=-2+4v`. The midpoint has parameter
power expansion

`H=H0+(a+b)H1+ab H2+v H3`,

`H0=c(tau+2)^2+d(tau+2)`, `H1=-4c(tau+2)`,
`H2=16c`, `H3=-4d`.

The defect has coordinate degrees at most2. The generator proves that
all 27 degree-(2,2,2) Bernstein coefficients of
`alpha*delta_n(H)-8*h_0(d)*h_n(H)` are strictly positive at every
supported index. In smoothed mode it replaces `c,d` by `yc,yd`, leaving
`tau` and `alpha` unchanged. Single defects use the three exact
degree-two interval Bernstein coefficients of
`delta_n(L)-3*2^(2m-3)*h_n(L)`; the rational small-index strengths are
stored with their exact numerator and denominator.

The tensor weights and scalar tail gates are separately checked by
`kernels_checks.py`. Positivity of every Bernstein coefficient proves
the entire continuum assertions1 and2; it is not a scan of outer
indices or parameter samples. A separate ordinary-x implementation is
used for the independent reconstruction; its audit files state the
completed scope and any matching per-case digests.

## 6. Jacobi compatibility and all outer indices

For `r,s in [-2,2]`, put

`F=c(tau-r)(tau-s)+d(tau-s)`,

`G=c(tau-r)(tau-s)+d(tau-r)`.

Their midpoint is `H_(r,s,(r+s)/2)` and their difference is `(r-s)d`.
For every ordered kernel minor, polarization gives

`mixed(K_F,K_G)=2 det K_H-(r-s)^2 det K_d/2`.

The corresponding smoothed identity replaces `F,G,H,d` by `yF,yG,yH,yd`.
If the reference minor is nonpositive the mixed minor is nonnegative
because `K_H` is TP2. If it is positive, assertion 3 and `(r-s)^2<=16`
give the same conclusion. Thus the two families are compatible.
Multiplication by a common folded-cone factor preserves compatibility
by Cauchy--Binet; no arbitrary-positive-sum closure is invoked.

Let `p_N` be either `U_N(tau/2)` or
`V_N=U_N(tau/2)+U_(N-1)(tau/2)`. For every `N>=1` the audited Jacobi
resolvent has roots `r_i in [-2,2]`, residues `w_i>0`, and `sum w_i=1`:

`p_(N-1)/p_N=sum_i w_i/(tau-r_i)`.

It follows that `c p_N+d p_(N-1)` is the positive weighted sum of

`[c(tau-r_i)+d]*product_(j!=i)(tau-r_j)`.

Each diagonal term is a strict folded-cone product by assertion 1 and
the old shifted-trace theorem. Each pair of distinct terms has a common
omitted-root product, leaving exactly the compatible pair `F,G`.
Expanding its minors proves TP2 of the sum. All summands have the same
degree and positive interval support, so every supported defect is
strictly positive from its positive diagonal contributions. Multiplying
the sum by `y` uses `yL_r` for diagonal terms and `yF,yG` for the mixed
terms; this works already at `N=1,2` when the common factor is constant.

Put `R_N=sum_(i=0)^N U_i(tau/2)` and `R_-1=0`, and
`Z_N=c R_N+d R_(N-1)`. The exact identities

`R_(2h)=U_h V_h`, `R_(2h+1)=U_h V_(h+1)`

give

`Z_(2h)=V_h[c U_h+d U_(h-1)]`,

`Z_(2h+1)=U_h[c V_(h+1)+d V_h]`.

For every `N>=1` the bracket index is at least1. The bracket and its
`y` multiple are covered by the preceding resolvent argument, and the
outside factor is a product of shifted traces (or 1). Therefore `Z_N`
and `yZ_N` have strictly positive supported folded defects for all
`m>=0,N>=1`.

At `N=0`, the unsmoothed polynomial is `c`, which is strict for every
`m>=0` (including `c=1` at `m=0`). The smoothed polynomial `yc` is strict
when `m>=1`; at `m=0` it equals `y`, whose central defect is -1.
This is the only stated outer-index exception. The additional-turn
formulas require `N=ell+1>=1`, so they never use that exceptional case.

## 7. Provenance and scope

The parent sources are read-only dependencies:

- `mixed_kernel_sharp_strength.md`: prefix and trace strengths.
- `recovery_oneturn_closure.md`: smoothed-prefix normalized bound.
- `fulltree_oneturn_normalized_tail.md`: normalized-product theorem,
  shifted-trace normalized bound, perturbation estimate and coefficient
  mass bounds.
- `mixed_kernel_all_minor_strength.md`: arbitrary ordered-minor strength.
- `general_one_turn_kernel_theorem.md` and its cited Jacobi foundation:
  resolvents, prefix identities and common-factor compatibility.

The only parent arithmetic imported by `kernels_certificate.py` is
`at`, `add`, `times`, and `prefixes` from `fulltree_oneturn_finite.py`.
The new target, parameter weights, certificate construction, tail gates
and theorem assembly are explicit here. Source fingerprints are recorded
in `kernels_provenance.json`. `audit_scaled_relative_minors.md` separately
checks the quantitative all-minor implication. Independent mathematical and finite
certificate audits state their own scope; no external publication or
formal promotion is claimed.
