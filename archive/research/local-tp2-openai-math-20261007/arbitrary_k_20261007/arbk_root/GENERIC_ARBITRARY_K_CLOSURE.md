# Strict Local TP2 on every path L^m R^k L^ell

**Primary status: PROVED_INTERNAL.** The mathematical assembly, finite
certificates, and scalar coverage have separate shared-session internal
audits and independent exact implementations. Full-tree Local TP2 remains
open; this is not a formal or external verification.

**Theorem.** Original strict Local TP2 holds at every canonical state
`L^m R^k L^ell`, for integers `m,k,ell>=0`, including the terminal supported
minor. The previous pinned campaign supplies `k<=2`; the new work proves
`k>=3`. The proof below combines a uniform closure theorem, its analytic
`m>=70` application, 70 fixed-m tails, and 34 finite starting prefixes.
No finite range of path lengths is being extrapolated.

If U,V are the two children ordered by degree and C is their parent
center, the original assertion is

\[
H(U-C)_n H(V-U)_{n+1}-H(U-C)_{n+1}H(V-U)_n>0,
\quad 0\le n\le\deg(U-C).
\]

## 1. Original state and old one-turn representation

The canonical root is `(1,2x^2+6x+5,x+2)`, with `y=x+1`, `p=x+2` and
mutations `L=3yAC-x(A+C)-B`, `R=3yCB-x(C+B)-A`.
Let `H(P)_n=[q^n]P(q+q^-1)`, reflected at negative indices and zero beyond
its degree. The defect and its normalization are

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2},
\qquad \eta(h)=\min_n\delta_n(h)/h_n^2.
\]

All coefficient orders below are Laurent half-row orders, unless an
ordinary coefficient order is stated. We use the previously audited
folded cone/kernel equivalence, multiplicative strength, normalized
product bound

\[
\eta(FG)\ge\eta(F)\eta(G)/[2(\min(\deg F,\deg G)+1)],
\tag{1}
\]

and positive Jacobi-resolvent mixture theorem. Their precise inherited
sources are the preceding `one_hour_20261007` package and its fixed
baseline dependencies, not an assertion that every positive sum is cone.

Put `u_j=U_j(x+3/2)`, `T_j=sum_(i=0)^j u_i`, `T_-1=0`,

\[
Y=1+yT_m,\quad \tau=3yY-x,\quad d=m+2,\quad
R_j=\sum_{i=0}^jU_i(\tau/2),
\quad Z_j=T_{m+1}R_j+T_{m-1}R_{j-1}.
\tag{2}
\]

The old center at `L^mR^j` is exactly `1+yZ_j`. At the new prefix
`L^mR^k`, `k>=2`, define

\[
X=1+yZ_{k-1},\quad C_0=1+yZ_k,\quad
A=Z_k-T_m,\quad B=Z_{k-2}-T_m,\quad t=3yX-x.
\tag{3}
\]

These are the fixed-prefix left-ray seeds from the original mutations.
For example, the inverse center is `C_(k-2)` on the old ray, so
`B=(tY-xX-C_0-Y)/y`.

Writing `a_j=Z_j-T_m` gives a useful exact positive recurrence:

\[
a_{-1}=-T_m,\quad a_0=u_{m+1},\quad
 a_{j+1}=\tau a_j-a_{j-1}+\kappa,
\quad \kappa=Y(3Y-2).
\tag{4}
\]

Its solution is

\[
a_j=u_{m+1}U_j(\tau/2)+T_mU_{j-1}(\tau/2)
       +\kappa R_{j-1}\quad(j\ge0).
\tag{5}
\]

Every factor in this formula has nonnegative ordinary coefficients. The
positive increments in (4) also imply
`a_(j+1)>=(tau-1)a_j` for `j>=0`. In particular `0<=B<=A` and

\[
A\ge(\tau-1)^2B\ge\beta B,
\qquad \beta=(H(\tau)_0-1)^2\ge1.
\tag{6}
\]

A smaller explicitly chosen positive lower bound for beta can always be
used in what follows.

## 2. Two quantitative lemmas used in the new argument

### 2.1 Subtraction with a normalized margin

If a cone row `f` and a nonnegative row `g` satisfy `g<=epsilon f`, then

\[
\delta_n(f-g)\ge\delta_n(f)-(4\epsilon+2\epsilon^2)f_n^2.
\tag{7}
\]

For the mixed polarization, its positive terms are
`2f_ng_n+f_ng_(n+2)+g_nf_(n+2)<=4epsilon f_n^2` by decrease. The two
negative terms of `delta(g)` are bounded by
`-epsilon^2[f_(n-1)f_(n+1)+f_(n+1)^2]>=-2epsilon^2 f_n^2` by
log-concavity and decrease. Reflection handles `n=0`; zero extension
handles terminal indices. If `f-g` has positive interval support and
`eta(f)>=12epsilon`, then `epsilon<=1/12`, and

\[
\eta(f-g)\ge\eta(f)/2.
\tag{8}
\]

The support assumption will follow from the original positive formulas.

### 2.2 A normalized bound for every ordered kernel minor

For a strict cone polynomial `F` with `eta(F)>=e`, every ordered minor
with positive diagonal entries satisfies

\[
\det K_F[\{i,j\},\{a,b\}]
\ge\frac e4K_F(i,a)K_F(j,b).
\tag{9}
\]

The established normalized adjacent-minor formula bounds an adjacent
minor below by `e/2` times its upper-left entry squared. Its lower-right
entry is at most twice its upper-left entry: in the interior their
indices are `|i-a|` and `i+a`, with only the latter increasing by two;
the first-row/column cases follow from the displayed folded-kernel
formula. Thus every adjacent determinant has at least an `e/4`
fraction of its diagonal product. For a larger rectangle with positive
off-diagonal entries, the band support makes the entire rectangle
positive; multiplying its adjacent cross-ratios telescopes to the full
cross-ratio, which retains that fraction. If an off-diagonal entry is
zero, the assertion follows directly, since `e<=1`.

Consequently, for any nonnegative reference polynomial `B`,

\[
F\ge cB,\qquad e c^2\ge16
\quad\Longrightarrow\quad
\det K_F\ge4\det K_B
\tag{10}
\]

on every ordered minor. No cone or decrease hypothesis on B is needed.
The reference nonnegativity is essential. Separate mathematical audits
of (7)--(10) are in `../arbk_audit`.

## 3. Recovering the new seeds and normalized traces

Assume old quantitative bounds, valid for `j>=1`,

\[
\eta(Z_j),\eta(yZ_j)\ge e_j,
\quad Z_j,yZ_j\text{ are }\Lambda_j\text{-strong}.
\tag{11}
\]

For `m>=1`, both `T_m` and `yT_m` are cone. Let
`P_m=max(H(T_m)_0,H(yT_m)_0)`. If `Lambda_k>=8P_m`, the established
subtraction-strength estimate gives
`delta(A)>=delta(Z_k)/2`, and the same for the smoothed rows.
Because `A<=Z_k`, this proves

\[
\eta(A),\eta(yA)\ge a:=e_k/2.
\tag{12}
\]

At `m=0`, the subtractions are `1` and `y`. The latter has its single
negative defect `delta_0(y)=-1`. The same polarization estimate loses
at most `4h_n+1<=5h_n`; hence `Lambda_k>=10` suffices for (12).
Positivity of A and yA was already supplied by (5).

If `Lambda_(k-1)>=189`, then uniformly for `r in [-2,2]`,

\[
\eta(t-r),\eta(y(t-r))\ge z:=e_{k-1}/729,
\quad y(t-r)\text{ has strength at least }55.
\tag{13}
\]

Here are the constants and boundary checks. The preceding campaign
proved that cone membership of both F and yF implies `h_0<3h_1`, and
that

`eta(y^2F)>=4eta(F)/729`, `strength(y^2F)>=strength(F)/9`.

Apply this first to `Z_(k-1)` and then to `yZ_(k-1)`; their subsequent
`y^2` multiples are cone by product closure. The two exact traces are

`3y^2Z_(k-1)+(2x+3-r)` and `3y^3Z_(k-1)+y(2x+3-r)`.

For a base row h of strength at least 21, their fixed additions have
`delta(b)>=9delta(h)-84h_n>=5delta(h)` at every index, and
`b_n<=4h_n`. This follows from the exact low-index correction identities
in the prior arbitrary-k trace lemma: raw loss is at most 32h_n;
smoothed loss is at most 84h_n, using `h_0<=2h_1` for the smoothed base.
Thus their normalized margin is at least `eta(h)/4`, proving (13).
The same previous strength lemma gives `Lambda_(k-1)/3-8>=55`.
All bases here have degree at least three; the finite exceptional
prefixes are dealt with directly by the certificates below.

## 4. Single blocks, actual midpoints, and spectral compatibility

Set `D=2(dk+2)=2(deg t+1)` and suppose `s<=H(t)_0-2`, `s>=1`.
For `r in [-2,2]`, put `L_r=A(t-r)+B`. The product part is cone and
has normalized margin at least

\[
f:=az/D.
\]

From (6), `B<=A(t-r)/(beta s)`. The positive-addition normalized
perturbation lemma therefore proves, simultaneously raw and smoothed,

\[
\eta(L_r),\eta(yL_r)\ge l:=f/4
\quad\hbox{if}\quad f\beta s\ge12.
\tag{14}
\]

The perturbation size is at most `1/12`; the factor four includes the
change in row normalization.

For the midpoint actually used by pairwise compatibility, let
`c=(r+v)/2`, `h=(r-v)/2`. Then

\[
H_{r,v}=A(t-r)(t-v)+B(t-c)
       =(t-c)L_c-h^2A.
\tag{15}
\]

The dominant product, raw or smoothed, is cone with margin at least

\[
g:=lz/D,
\]

and the subtracted term is bounded by `4/s^2` times that product.
Its positivity is also clear from the left side of (15). By (7)--(8),

\[
\eta(H_{r,v}),\eta(yH_{r,v})\ge g/2
\quad\hbox{if}\quad gs^2\ge48.
\tag{16}
\]

Moreover `H_(r,v)>=beta s^2 B` and likewise after smoothing. Equations
(9)--(10) give the required all-minor factor four: indeed
`(g/2)(beta s^2)^2>=24 beta^2 s^2>=24>16`.
Only the actual midpoint is required; an independent third parameter
cube is an unnecessary stronger assertion.

The previously proved midpoint identity for the two spectral summands
now implies nonnegative mixed determinants on every ordered minor.
The Jacobi-resolvent expansions of the new outer Chebyshev sequence
and its prefix sums are therefore pairwise compatible, raw and
smoothed, without invoking arbitrary positive-sum closure.

## 5. Domination of the two fixed corrections

Put

\[
K_0=\tau+1,\quad J=y(t-2),\quad V=3y^2Xp,
\quad K=XpK_0,
\quad M=\tau(2)-2=5+27T_m(2),\quad b=2dk-3.
\]

The independent positive-recurrence derivation in
`../arbk_audit/ARBITRARY_K_POSITIVE_SEEDS_AND_MASS.md` proves

\[
\alpha=\frac{T_m(2)M^{k-1}}b,\quad
A\ge\alpha K_0,\quad H(t)_0-2\ge9\alpha,
\tag{17}
\]

\[
JL_r\ge cK,\quad y^2L_r\ge cK_0,
\qquad c=18\alpha^2.
\tag{18}
\]

Briefly, `kappa=T_m K_0+1+2xT_m>=T_m K_0` and (5) give
`a_j>=T_m K_0 R_(j-1)`. The relevant old products are cone; their
central coefficient is at least their mass divided by the number of
supported Laurent coefficients. Their masses are at least the indicated
powers of M because all spectral factors have roots in [-2,2].
This gives (17). The elementary identities `J>=2y^2X`, `y^2>=p` and
`H(y^2)_0=3` give (18). In particular we may use the simpler lower bounds

\[
s=\frac9{32}\frac{M^k}{2dk-3},\qquad
c=\frac9{512}\frac{M^{2k}}{(2dk-3)^2},\qquad
\beta=\frac{M^2}{4(2d+1)^2},
\tag{19}
\]

where `T_m(2)>=M/32`, `H(tau)_0>=(M+2)/(2d+1)`, and
`M>=4d-2` supply the last central-minus-one comparison.
These constants use mass growth in k, not a central-coefficient power
that would lose that growth.

## 6. Absorb corrections for every final left-run length

The new outer ray is

\[
\mathcal Z_N=A\mathcal R_N+B\mathcal R_{N-1},\quad
q_N=y[A U_N(t/2)+B U_{N-1}(t/2)],\quad
C_N=Y+y\mathcal Z_N,
\]

where `mathcal R_N=sum_(j=0)^N U_j(t/2)`. Do not confuse this with the
old Z_j in (2). For N>=1,

\[
S_N=q_{N+1},\quad E_N=C_{N-1}-X,\quad
M_N=3y^2\mathcal Z_N+K_0,\quad D_N=E_NM_N.
\]

All four initial LR comparisons already hold for every m,k>=2 by the
previous campaign's old-ray companion argument. The compatible new
kernels from Section 4 propagate them to

\[
S_N\le_{lr}J\mathcal Z_N,\qquad Xp\le_{lr}E_N.
\tag{20}
\]

The preceding normalized absorption theorem applies with

\[
D_J=2(dk+3),\qquad
E=\min\{lz/D_J,\ l/1296\}.
\tag{21}
\]

The first quantity is the product margin for JL_r. For the second,
`H(L_r)_0<=8H(L_r)_1` follows by multiplication with the decreasing
trace kernel and B<=A(t-r); the earlier boundary-aware y² smoothing
lemma gives `eta(y²L_r)>=l/1296`.

The scalar conditions needed are exactly

\[
Ec>96,\qquad zs/D\ge2,\qquad c\ge2.
\tag{22}
\]

For completeness, the positive spectral expansion has at most N active
weights summing to one and terms L_r times N-1 shifted trace factors.
Every term lies between half and twice their convex sum, coefficientwise,
because B<=A and each omitted trace factor has central coefficient at
least s>1. Nonnegative mixed minors, squared weights and (1) imply, for
F=J mathcal Z_N or y²mathcal Z_N and its respective correction Q,

\[
\eta(F)\ge\frac E{4N}(z/D)^{N-1},\qquad
Q\le\frac2{cs^{N-1}}F.
\]

By (22), their quotient exceeds 12, using `2^(N-1)>=N`. This proves
that `M_N` is cone by the positive perturbation estimate. Since J has
strength at least 55, the identity `V=pJ+yp²`, `H(yp²)=(14,11,5,1)`
gives `W(J,V-pJ/2)>=0` through every supported index. Transport of all
ordered LR minors therefore retains

`W(J mathcal Z_N,V mathcal Z_N)>=delta(J mathcal Z_N)/2`.

The correction K is smaller than the available normalized margin, so
`J mathcal Z_N <_lr V mathcal Z_N+K` strictly. Together with (20) and
multiplication by the cone kernel of M_N this yields the original
strict comparison `S_N<_lr D_N`.

For a=dk+1, the exact degrees are

`deg S_N=a(N+2)+d-1`, `deg D_N=2aN+a+2d-1`.

Their difference is `a(N-1)+d>=d>0`. The proof therefore includes the
last supported comparison, not only an interior band. N=0 is the
already proved old one-turn state; the endpoint orientation above is
not applied to it.

## 7. Coverage of the two infinite indices

For m>=70, the existing single-only normalized tail, verified separately
in `../arbk_seed`, supplies

\[
E_m=\frac{c_0^2\sigma^{2m+1}}{16(m+3)},\quad
r_m=\frac{c_0\sigma^m}{4(m+3)},\quad
e_j=\frac{E_m r_m^{j-1}}{4j},\quad
c_0=1/400000000,\quad\sigma=59/100.
\tag{23}
\]

Use M>=27·6^m and the conservative constants (19). The exact verifier
checks all scalar gates at (m,k)=(70,3). It also checks the consecutive
m ratios at k=3, and `r_m²M>=16`. Every ratio in m is an increasing
product of positive linear fractions. For k>=3 the single-perturbation
ratio is at least r_m²M/4; all other required ratios have still larger
exponential factors and the displayed finite products of linear
fractions. This rigorously covers every m>=70,k>=3.

For each fixed m=0,...,69, finite exact real-interval certificates
provide stronger constants in (11). At m=0, a paired spectral block
argument gives `e_j=1/(256·3^j)` for all j. For m=1,...,4, small
trace-block certificates improve the exponential rate; the remaining
fixed m use the one-factor interval constants directly. A single
threshold K_m is fixed only after all scalar and strength gates,
and every required consecutive k ratio, are strictly verified.
Because all such ratios are products of increasing linear fractions,
the check at K_m covers every k>=K_m. The bounded remaining prefixes
3<=k<K_m receive exact finite-ray and midpoint certificates.

This is an analytic partition of all integer parameters, not an
inference that finite cases imply infinite cases. The complete parameter list and exact ratio proof are in
`SCALAR_COVERAGE.md`, and the exact values are in
`scalar_closure_results.json`. Separate reconstruction agrees with all
70 fixed-m gate vectors and all analytic-tail corner/ratio vectors.


## 8. The finite bridge and completed theorem

The thresholds are K_0=21, K_1=11, K_2=6, K_3=5, K_4=4, K_5=5,
and K_m=3 for each m=6,...,69. Hence the unhandled prefixes are exactly
m=0,k=3..20; m=1,k=3..10; m=2,k=3..5; m=3,k=3..4;
m=4,k=3; and m=5,k=3..4, totaling 34.

For each of these, `verify_finite_ray_bridge.py` reconstructs the original
canonical mutations and checks the full real interval r in [-2,2] using
three exact degree-two Bernstein coefficients per margin. These are the
finite-ray extension gates of the previous campaign: the required
low-band kernel minors versus their explicit mass thresholds, the
multiplier defect margins, and the trace central-defect/mass bound.
All **3,282** coefficients are strictly positive. The independent
Laurent reconstruction `../arbk_audit/audit_finite_ray_bridge.py` agrees
with every coefficient, threshold, and index.

The separate `../arbk_mixed/finite_mixed_kernels.py` certifies the raw
and smoothed single and actual midpoint templates for the same 34
prefixes. It checks every supported defect on the full interval/square,
not sampled roots. All **51,804** defect Bernstein coefficients and
all **42,246** midpoint relative-margin coefficients are strictly
positive. The latter certify `c_dom² delta(H)-16 H_n²>0` where
`H>=c_dom B` coefficientwise; (10) supplies the all-minor comparison
consumed by the finite-ray criterion. No uniform-strength condition
stronger than that criterion requires is being imposed.

`audit_finite_mixed.py` independently reconstructs the original states
by ordinary-x mutations and uses exact tensor interpolation. All 136
individual template records, including every coefficient and normalized
bound, agree exactly. The finite-ray criterion therefore proves every
final length ell>=1 at all 34 prefixes.

The remaining normalized inputs have their own independent reconstructions:
223,484 tensor coefficients for the m=0 paired blocks and residues;
4,021,860 full tensor coefficients represented by 102,060 histogram
coefficients for m=1,...,4; and 38,745 old interval coefficient pairs
for m=0,...,69. The old single-only m>=70 bound is proved analytically.
None of these computations imposes a finite upper bound on any of the
three word exponents.

All m>=0,k>=3 have now been covered, with every final ell>=1. For ell=0,
use the old one-turn theorem. For k=0, use the pure-left theorem; for
k=1, use the inherited first-return theorem; and for k=2, use the
preceding uniform two-parameter theorem. This completes the stated
original strict Local TP2 theorem on all L^m R^k L^ell.

## 9. Dependencies and status boundary

The immediately preceding research snapshot is
`f1bf528c9064e11f79795a581b6a4bc15f0efbe1`, on the same private branch.
Its `one_hour_20261007` package supplies the finite-ray criterion, the
all-m/all-k initial comparisons, normalized smoothing, the arbitrary-k
one-turn trace theorem, and the k=2 result. The earlier foundation
snapshot is `a36fbac460073bf757434f122e721dfa254e8e48`, under
`research/local-tp2-coefficient-geometry-20261003/`, particularly:

- `continuation_kernel/folded_kernel_theorem.md`;
- `mixed_kernel_sharp_strength.md`, `mixed_kernel_all_minor_strength.md`;
- `fulltree_oneturn_normalized_tail.md`, `recovery_oneturn_closure.md`;
- `general_one_turn_kernel_theorem.md`, `general_one_turn_reduction.md`;
- the fixed-prefix first-return and common-closure theorems cited by the
  preceding k=2 proof.

Exact dependency links are recorded at the package root. The new proof
is an internally audited mathematical proof with exact finite
certificates and these inherited lemmas. It does not establish arbitrary
canonical-word Local TP2, external novelty, Lean verification, external
replication, or canonical-main acceptance.
