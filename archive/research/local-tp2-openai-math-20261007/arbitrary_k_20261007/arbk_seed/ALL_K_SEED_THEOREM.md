# Seed kernels and half-defect bounds after every right-run length

**Status: PROVED_INTERNAL; separate mathematical and exact finite
reconstruction audit PASS, subject to the identified prior one-turn
foundation theorems.** The finite gates are exact integer certificates.
The new proof does not assume Local TP2 at any new two-turn state.

Put `y=x+1`,

\[
T_m=\sum_{i=0}^m U_i(x+3/2),\qquad T_{-1}=0,
\quad Y=g_m=1+yT_m,\quad t_0=3yY-x.
\]

Write `a=T_(m+1)`, `b=T_(m-1)`,
`R_j=sum_(i=0)^j U_i(t_0/2)`, `R_-1=0`, and

\[
Z_j=aR_j+bR_{j-1},\qquad C_j=1+yZ_j,
\qquad a_j=Z_j-T_m.
\tag{1}
\]

The established canonical one-turn identities identify `C_j` as the
center at `L^mR^j`. In particular `a_0=u_(m+1)`, where
`u_i=U_i(x+3/2)`.

## 1. Identification of the actual new seeds

At the prefix `L^mR^k`, `k>=2`, the fixed endpoint for the subsequent
left run is `X=C_(k-1)`, its other endpoint is `Y`, and its inverse
center is `C_(k-2)`. Therefore the two new seeds are exactly

\[
\boxed{A=(C_k-Y)/y=a_k,\qquad
B=(C_{k-2}-Y)/y=a_{k-2}.}
\tag{2}
\]

Their degrees are

\[
\deg a_j=(j+1)(m+2)-1,\quad
\deg A=(k+1)(m+2)-1,\quad
\deg B=(k-1)(m+2)-1.
\]

The finite verifier also reconstructs the original canonical root and
each required center by the actual mutation
`3y endpoint*center-x(endpoint+center)-opposite`, in the symmetric
Laurent basis. Thus the finite checks concern these actual seeds.

## 2. Positive coefficient domination

The inhomogeneous prefix recurrence gives

\[
a_j=t_0a_{j-1}-a_{j-2}+D,
\qquad D=(t_0-2)T_m+a+b\ge0\quad(j\ge2).
\tag{3}
\]

All inequalities in this section hold coefficientwise already in the
ordinary `x` basis. The initial difference `a_1-a_0=at_0+b` is positive.
Equation (3) gives

\[
a_j-a_{j-1}=(t_0-2)a_{j-1}
+(a_{j-1}-a_{j-2})+D>0.
\]

The base `a_0=u_(m+1)` is dense positive. Induction proves positivity
and increase of every `a_j`, without using a cone assertion. Moreover

\[
a_j\ge(t_0-1)a_{j-1}\quad(j\ge1).
\tag{4}
\]

For `j>=2` this follows from (3) and increase. For `j=1`, direct
subtraction gives `a_1-(t_0-1)a_0=2a+b+(t_0-2)T_m>=0`.
Consequently

\[
\boxed{A\ge(t_0-1)^2B,\qquad a_j\ge(t_0-1)^j u_{m+1}.}
\tag{5}
\]

In the Laurent basis, with `s_0=H(t_0)_0-1`, this also gives
`A>=s_0^2 B` and `a_j>=s_0^j u_(m+1)`.

## 3. A uniform half-defect theorem

For every integer `m>=0,j>=1`, at every supported index,

\[
\boxed{\delta_n(a_j)\ge\tfrac12\delta_n(Z_j),\qquad
\delta_n(ya_j)\ge\tfrac12\delta_n(yZ_j).}
\tag{6}
\]

Here `delta_n` is the established reflected folded defect. In particular

\[
\eta(a_j)\ge\eta(Z_j)/2,\qquad
\eta(ya_j)\ge\eta(yZ_j)/2.
\tag{7}
\]

The normalization follows because subtraction decreases each positive
row coefficient. Both `a_j,ya_j` have strict folded kernels. At `j=0`
the rows `u_(m+1),yu_(m+1)` have the already proved strict Chebyshev-ray
kernels. Thus both new seeds in (2), with and without multiplication by
`y`, belong to the strict folded cone for every `m>=0,k>=2`.

### 3.1 The region m>=1,j>=2

The previously proved arbitrary-right-run trace note, Section 4, supplies

\[
Z_j,\ yZ_j\text{ are }\Lambda_{m,j}\text{-strong},\qquad
\Lambda_{m,j}=\frac{3\,2^{2m-3}}{2j}
(3\,2^{m-1})^{j-1}.
\tag{8}
\]

This follows from the old positive Jacobi-resolvent expansion, compatible
mixed minors, and squared weights; it holds for every `j>=1`.
The references `T_m,yT_m` are cone rows when `m>=1`, and their central
coefficients are bounded by

\[
p_0\le3T_m(2)\le(7^{m+1}-1)/2.
\]

For a cone reference `P`, the proved subtraction polarization estimate is

\[
\delta_n(F-P)\ge\delta_n(F)-4p_0H(F)_n+\delta_n(P).
\]

Thus (6) holds whenever

\[
\Lambda_{m,j}\ge4(7^{m+1}-1).
\tag{9}
\]

The exact corner checks `(m,j)=(40,2),(7,3),(4,4),(3,5),(2,6),(1,8)`
prove (9) on their upper-right regions. For fixed `m`, the strength's
consecutive ratio is `(3*2^(m-1))*j/(j+1)>1`. For fixed `j>=2`, its
consecutive ratio in `m` is `2^(j+1)>=8`, whereas
`(7^(m+2)-1)/(7^(m+1)-1)<8`. These comparisons justify every unbounded
region. The uncovered pairs are exactly `m=1,...,39,j=2`, and 13 pairs
with `j>=3` recorded by the verifier.

### 3.2 The case j=1

Here `Z_1=a_X=a(t_0+1)+b`. The completed previous campaign proves,
for all `m>=0`,

\[
\eta(Z_1),\eta(yZ_1)\ge
E_m=\frac{c_0^2\sigma^{2m+1}}{16(m+3)},
\quad c_0=1/400000000,\quad\sigma=59/100.
\]

Since `T_m<=a` and `H(t_0)_0>=27*6^m/(2m+5)`, the subtracted row
satisfies `0<=P<=epsilon_m F`, in both raw and smoothed cases, with

\[
\epsilon_m=(2m+5)/(27\,6^m).
\]

The favorable terms of the subtraction polarization are at most
`4epsilon_m H(F)_n^2`. For `m>=1` the reference is cone. Therefore
`E_m>=8epsilon_m` proves (6). The exact check at `m=70` is strict;
the consecutive ratio is

\[
6\sigma^2\frac{(m+3)(2m+5)}{(m+4)(2m+7)}>1\quad(m\ge70).
\]

Every variable factor increases. This proves the whole infinite tail;
the remaining `m=0,...,69,j=1` are checked exactly.

### 3.3 The all-right boundary m=0

Here `T_0=1`, and the already audited paired-root argument gives
`Z_j,yZ_j` strength `lambda=9^floor(j/2)`. For `j>=2`, `lambda>=9`.
The reference `1` is cone, but `y` is not: its only negative defect is
`delta_0(y)=-1`. The same polarization estimate, which only requires the
reference row to be decreasing, gives in either case

\[
\delta_n(F-P)\ge\delta_n(F)-4H(F)_n-1.
\]

Every supported coefficient of a lambda-strong row is at least lambda.
Hence `(lambda/2-4)H(F)_n-1>=9/2-1>0`. This proves (6), without
incorrectly assuming that `y` belongs to the cone. The remaining pair
`m=0,j=1` is among the finite cases above.

### 3.4 Exact finite completion

`verify_seed_subtraction.py` reconstructs exactly **122** canonical pairs
and checks all **16,048** integer margins

\[
2\delta_n(a_j)-\delta_n(Z_j)>0,
\qquad2\delta_n(ya_j)-\delta_n(yZ_j)>0.
\]

Every half-row and every margin is saved in
`seed_subtraction_certificates.json`. These bounded certificates close
precisely the complement of the proved infinite regions; no extrapolation
from finite paths is used.

The separate implementation `../arbk_mixed/audit_seed_bounds.py`
reconstructs all 122 pairs in the ordinary `x` basis and converts to
Laurent coefficients by direct binomial expansion. It imports no
generating implementation and matches every one of the 16,048 margins
and both old/new half-rows. Its mathematical review and precise audit
scope are recorded in `../arbk_mixed/SEED_BOUNDS_INDEPENDENT_AUDIT.md`.

## 4. Uniform strengths and use with improved normalized blocks

Equation (6) implies the following immediately usable strengths:

\[
a_j,ya_j\text{ are }\Lambda_{m,j}/2\text{-strong}
\quad(m\ge1,j\ge1),
\]

\[
a_j,ya_j\text{ are }9^{\lfloor j/2\rfloor}/2\text{-strong}
\quad(m=0,j\ge1).
\]

The second assertion at `j=1` uses the old explicit seed and the
nonpositive-root primitive, which give strength at least one for
`Z_1,yZ_1`.

More importantly, (7) transfers **any** improved normalized bound for
the old mixtures to the actual new seeds, at a fixed loss of two.
There is no restriction on how many propagators are grouped into a
normalized block. In particular, if every shifted old trace has
normalized defect at least `e_m`, and both old single templates have
normalized defect at least `ell_m`, the positive resolvent argument gives

\[
\eta(a_j),\eta(ya_j)\ge
\frac{\ell_m}{8j}
\left(\frac{e_m}{2(m+3)}\right)^{j-1},\qquad j\ge1.
\tag{10}
\]

This estimate retains the squared weights and the factor-two comparison
of each summand with their average. Sharper block estimates can replace
its one-factor product rate without repeating any seed subtraction proof.

## Dependencies and scope

- Prior research `recovery_oneturn_closure.md`: old single strengths,
  compatible resolvent kernels, prefix positivity and normalized bounds.
- Completed campaign `hour_quantum/UNIFORM_SEED_STRENGTH.md`: the
  subtraction lemma and all-m normalized bounds for `a_X,ya_X`.
- Completed campaign `hour_transport/ARBITRARY_K_TRACE_EXPLORATORY.md`,
  Sections 4 and 7: (8) and the all-right paired-root strength.
- `OLD_SINGLE_NORMALIZED_BOUND.md`: explicit usable old trace/single
  normalized constants on the full real parameter intervals.

This theorem supplies the new seed cone, quantitative subtraction, and
coefficient-domination inputs. It does not by itself prove the required
new mixed-template compatibility, multiplier, or strict proxy inequality
at arbitrary `L^mR^kL^ell`.
