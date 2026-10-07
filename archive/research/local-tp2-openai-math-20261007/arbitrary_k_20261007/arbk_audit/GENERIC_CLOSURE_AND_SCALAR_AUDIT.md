# Independent audit of arbitrary-k closure, finite bridge, and scalar tails

**Verdict: PASS for the stated sufficient closure theorem and the scalar
partition.** This is a shared-session independent mathematical and exact
arithmetic audit, not a blind, external, or formally verified review.
The old normalized interval/block constants are inputs whose complete
certificates are reviewed separately by the other research lanes.

Reviewed author note: `../arbk_root/GENERIC_ARBITRARY_K_CLOSURE.md`.
This audit does not independently assert those input certificates without
their companion checks, nor promote any external repository status.

## 1. New normalized trace bound, including every boundary coefficient

Suppose `Z,yZ` are cone, have normalized defect at least `e`, and are
`Lambda`-strong, where `Lambda>=189`. The inherited central-ratio lemma
gives `H(Z)_0<3H(Z)_1` and `H(yZ)_0<3H(yZ)_1`: for the latter, its next
smoothing `y²Z` is cone by multiplying Z by the cone polynomial y².
The boundary-aware smoothing estimate therefore gives

\[
\eta(y^2Z),\eta(y^3Z)\ge4e/729,
\qquad y^2Z,y^3Z\text{ have strength at least }21.
\]

For either base row h the trace has the form `b=3h+v`, where
`v=(a,2)` or `(a+4,a+2,2)`, `1<=a<=5`. The previously displayed exact
correction identities imply

\[
\delta_n(b)\ge9\delta_n(h)-84h_n.
\]

For the raw row the worst loss is at most `32h_n`. For the smoothed row:
at n=0 the only negative linear term has coefficient at most 84, and
the constant `-a²+2a+16` is positive on `[1,5]`; at n=1 use
`h_0<=2h_1`, making the loss at most `56h_1`; the n=2,3 losses are at
most `21h_2,6h_3`. At all later indices the correction vanishes.
The central bound `h_0<=2h_1` for the smoothed base follows directly
from `h=H(yF)` with `F=y²Z` nonnegative: `h_0=f_0+2f_1` and
`h_1=f_0+f_1+f_2`.

Ordinary log-concavity gives `delta_n(h)<=h_n²`, so strength at least
21 implies `h_n>=21` throughout its support. Each coefficient of v is at
most h_n. Thus `b_n<=4h_n` and

\[
\delta_n(b)\ge5\delta_n(h),\qquad
\eta(b)\ge\frac5{16}\eta(h)\ge\frac14\eta(h)\ge e/729.
\]

The final supported indices are untouched by v and remain covered.
The old fixed-addition strength lemma gives `Lambda/3-8>=55` as well.
Thus the constant `e/729` and the strength 55 in author §3 are valid.

## 2. Single blocks, midpoint compatibility, and correction absorption

The seed recurrence and mass bounds are proved independently in
`ARBITRARY_K_POSITIVE_SEEDS_AND_MASS.md`. The normalized all-minor and
actual-midpoint subtraction arguments are proved independently in
`NORMALIZED_ALL_MINOR_AUDIT.md` and `MIDPOINT_SUBTRACTION_AUDIT.md`.
They apply simultaneously to raw and smoothed rows using their own
nonnegative references B and yB. A cone assumption on those reference
rows is unnecessary for the relative all-minor comparison.

The single-block positive-addition step is also sound. If `F` is cone,
`0<=G<=epsilon F`, its polarized defect satisfies
`delta(F+G)>=delta(F)-(4epsilon+2epsilon²)f_n²`. With
`eta(F)>=12epsilon`, at least half the original defect remains. Since
`F+G<=(1+epsilon)F` and `epsilon<=1/12`, the normalized margin is at
least `eta(F)/4`. This justifies the `l=f/4` used in the scalar gates.

Only `c=(r+s)/2` enters the actual pairwise spectral compatibility
identity. The condition `g s²>=48` ensures its normalized margin
`g/2`. The coefficient domination `H>=beta s²B` then gives

\[
(g/2)(\beta s^2)^2\ge24\beta^2s^2>16,
\]

so the all-minor reference factor four follows without an additional
scalar gate. The same reasoning applies after smoothing.

For the mass-only bound on beta, the author has now made explicit the
needed inequality `M>=4d-2`. It follows from `M>=27*6^m` and `d=m+2`;
therefore `H(tau)_0-1>=M/[2(2d+1)]`. This supplies the square root of
the proposed beta lower bound with the correct sign.

For correction absorption, both required common products are cone.
The bound `eta(J)>=z` follows from the smoothed shifted trace, and
`H(L)_0<=8H(L)_1` follows from the decreasing shifted trace and
`B<=A(t-r)`. Hence

\[
E=\min\{lz/[2(dk+3)],\ l/1296\}
\]

is valid. The compatible spectral expansion has at most N active
positive weights; keeping their squares loses at most a factor N.
Each term and its convex sum lie within a factor two. With
`R=zs/[2(dk+2)]>=2`, the inherited absorption estimate is

\[
\frac{\eta(F_N)}{\epsilon_N}
\ge\frac{Ec}{8}\frac{R^{N-1}}N>12
\quad(Ec>96).
\]

Thus the multiplier and strict proxy comparison follow for every N.
The original-target chain uses the previously proved four initial
orders for all m,k>=2, not unverified orders at a new child. The final
degrees are consistent: with `a=dk+1`,

\[
\deg S_N=a(N+2)+d-1,\quad
\deg D_N=2aN+a+2d-1,
\quad\deg D_N-\deg S_N=a(N-1)+d>0.
\]

The inherited strict support argument therefore covers the terminal
target minor. N=0 is supplied by the already proved one-turn theorem.

## 3. Independent finite bridge

`audit_finite_ray_bridge.py` reconstructs the 34 original canonical
prefixes using direct symmetric Laurent multiplication and mutation.
It solves division by y from outer coefficients and checks the product
back exactly. No author implementation or expected JSON is imported.

For each prefix it independently produces the three degree-two
Bernstein coefficients of:

* `delta_0(t-r)-2(t(2)-r)`;
* `det K_(L_r)[(i,i+1),(n,n+1)]-alpha_n L_r(2)`, where
  `i=min(n,deg J)` and `alpha_n=floor(2J(2)K_n/W_i(J,V))+1`;
* `delta_n(y²L_r)-beta_n L_r(2)`, where
  `beta_n=6(K0_(n-1)+3K0_(n+1))+1`.

Every Bernstein conversion is independently expanded back into the
original power polynomial. All **3,282** coefficients are strictly
positive. Only after completing those checks were author results read:
every coefficient, threshold, index, and shared degree agrees exactly.
Full independently generated values are in
`finite_ray_bridge_independent_results.json`.

The covered prefixes are `m=0,k=3..20`; `m=1,k=3..10`;
`m=2,k=3..5`; `m=3,k=3..4`; `m=4,k=3`; and `m=5,k=3..4`.
Their missing infinite ray length is handled by the earlier proved
finite-ray criterion and separately certified compatible kernels.

## 4. Exact scalar reconstruction and monotone infinite tails

`audit_scalar_closure.py` uses exact rational arithmetic and independent
scalar assembly. For finite m it uses the certified old constants as
inputs; m=1..4 block constants are separately written as the exact
fractions stated in the theorem. Its independent full-Laurent recurrence
also regenerates the finite seed-strength thresholds.

Every one of the eight gates and every consecutive k ratio for all
70 fixed m values agrees exactly with the author output. The analytic
corner `(m,k)=(70,3)`, its eight consecutive m ratios, and its eight
all-k ratio lower bounds also agree exactly. All required inequalities
are strict, except the intentional constant-in-k beta ratio equal to
one. Full values are in `scalar_closure_independent_results.json`.

For completeness, the infinite monotonicity does not follow from those
finite checks alone. Here is its algebraic justification. For the
spectral normalized form `e_j=E r^(j-1)/(4j)`, ignore positive factors
constant in k and write `D=2(dk+2)`, `D_J=2(dk+3)`, `b=2dk-3`.
The eight gate expressions have the following k-dependence:

| Gate | Dependence up to a positive k-independent factor |
|---|---|
| Single | `r^(2k-3) M^k / [k(k-1)D b]` |
| Midpoint | `r^(3k-5) M^(2k) / [k(k-1)²D²b²]` |
| Proxy | `r^(3k-5) M^(2k) / [k(k-1)²D D_J b²]` |
| Multiplier | `r^(2k-3) M^(2k) / [k(k-1)D b²]` |
| Propagator | `r^(k-2) M^k / [(k-1)D b]` |
| Correction domination | `M^(2k)/b²` |
| Trace center | `M^k/b` |
| Seed ratio | constant |

Every consecutive ratio is a positive constant times products of
`(ak+b)/(a(k+1)+b)` with nonnegative powers. Those fractions increase
on the positive domain. The m=0 direct estimate `e_j=E r^j` removes
the k and k-1 factors, preserving that monotonicity. Thus each checked
fixed-m threshold covers its whole tail. Strength thresholds also
persist: for m>=1 the strength ratio is
`(3*2^(m-1))*j/(j+1)>1`, and for m=0 the paired-block strength is
nondecreasing.

For all `k>=3,d>=2`, use

\[
\frac{k}{k+1}\ge\frac34,\quad
\frac{k-1}{k}\ge\frac23,\quad
\frac{D_k}{D_{k+1}},\frac{D_{J,k}}{D_{J,k+1}}\ge\frac34,
\quad\frac{b_k}{b_{k+1}}\ge\frac23.
\]

This gives the respective consecutive-k lower bounds

\[
r^2M/4,\quad r^3M^2/12,\quad r^3M^2/12,
\quad r^2M^2/6,\quad rM/3,
\quad4M^2/9,\quad2M/3,\quad1.
\]

The scalar verifier computes precisely these quantities. For the
analytic m-tail, `r²M>=16`, `0<r<1`, and `M>=27` ensure all seven
nonconstant bounds exceed one. The quantity `r²M` itself increases
with m since its consecutive ratio is
`6sigma²((m+3)/(m+4))²>1` at m=70 and thereafter.

At k=3, every consecutive m ratio of each gate is likewise a positive
constant times increasing positive affine fractions: E and r have
denominator m+3, while D,D_J,b and 2d+1 are positive affine functions
of m. Exact positivity of the corner and its consecutive ratios
therefore covers all `m>=70,k=3`, and the k bounds extend to every
`k>=3`. The auxiliary old single-block absorption gate has consecutive
m ratio `6sigma² (m+3)/(m+4) (2m+5)/(2m+7)>1`; it too is checked
at m=70. Finally the trace-strength corner increases by a factor 8
per m, and the seed-strength corner by 16 while its required bound
increases by less than 8. No finite scan is being extrapolated.
