# Independent audit of the finite reversed-coefficient certificates

This audit covers every integer `m=0,...,409`, both original and `y`-smoothed
single and midpoint blocks.  It is a continuum certificate on the whole
parameter interval/cube, not evaluation on a sampled grid.  The exhaustive
run and primary-writer comparison are recorded in
`finite_audit_independent_results.json`; the source is
`finite_audit_independent.py`.  **Verdict: PASS**, with every complete
case hash and numerical metadata matching the primary writer.

## Objects and independent construction

Set `y=1+x`, `c=T_m`, `d=T_(m+2)`,
`tau=3y(1+yT_(m+1))-x`, and `t=tau+2`.  The audit constructs `T_j` in
ordinary powers of `x` by the Chebyshev recurrence

`U_0=1`, `U_(-1)=0`, `U_(j+1)=(3+2x)U_j-U_(j-1)`, `T_j=sum_(i=0)^j U_i`.

Consequently `t=5+2x+3(1+x)^2 T_(m+1)`.  It constructs the following
ordinary-positive pieces by exact ordinary polynomial multiplication:

`c`, `d`, `ct`, `ct+d`, `ct^2+dt`.

For the smoothed cases, it multiplies each ordinary piece by `1+x` **before**
converting to Laurent coefficients.  Thus this replay does not depend on the
primary writer's Laurent recurrence, Fourier convolution, polarized defect,
or specialized Bernstein weight tables.

The disclosed foundation is the ordinary polynomial recurrence/product route
used in the parent `fulltree_oneturn_finite_independent.py`; no new primary
writer implementation is imported or read.  The expected writer JSON is
opened only after this audit's requested cases have been recomputed.

## Exact ordinary-to-Laurent transformation

Let `P(x)=sum_(j=0)^D p_j x^j` with nonnegative integer coefficients and
`p_D>0`.  Put `M=P(2)>0` and `B=2^bit_length(M)`, so `B>M`.  Start
`acc=p_D` and, for `k=1,...,D`, replace

`acc <- (B^2+1)acc + p_(D-k) B^k`.

Induction gives

`acc=sum_(i=0)^k p_(D-i) B^i(B^2+1)^(k-i)`

after step `k`.  At the final step this is exactly
`B^D P(B+B^(-1))`.  The Laurent polynomial `P(z+z^(-1))` has nonnegative
integer coefficients summing to `P(2)=M`; every coefficient is therefore
strictly below `B`.  Its coefficients are consequently the ordinary radix
`B` digits of `acc`, with no carries.  Digit `D+n` is the half-row entry
`H(P)_n`.  The implementation uses only integer shifts/additions for this
Horner calculation, then verifies Laurent symmetry and the total mass.

The implementation additionally crosschecks this transform against the
independent binomial definition

`H(P)_n = sum_(j>=n, j-n even) p_j binom(j,(j-n)/2)`

for monomials and other small polynomials, and for prefix degrees
`0,1,2,3,7,20,96,200,409,411`.  These checks supplement the preceding exact
proof; they are not substituted for it.

The ordinary product similarly uses a carry-free integer radix greater than
`P(1)Q(1)`, which bounds every ordinary coefficient of `PQ`.  Product degree,
nonnegativity, and total mass are checked.

## Parameter polynomials and margins

Write `r=-2+4a`, `s=-2+4b`, `u=-2+4e`, where each parameter lies in `[0,1]`.
The single and midpoint power-basis polynomials are reconstructed as

`L=ct+d-4ca`,

`H=ct^2+dt-4ct(a+b)+16cab-4de`.

Their `y`-smoothed versions use the ordinary pieces already multiplied by
`y`.  For each Fourier index from zero through the full degree, the audit
uses generic parameter polynomial multiplication to form

`delta_n(h)=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2)`.

The convention is `h_(-1)=h_1`, and all entries beyond the degree are zero.
No defect simplification special to these blocks is used.  The single
degrees are `2m+3` and `2m+4`; the midpoint degrees are `3m+6` and `3m+7`.
The midpoint leading coefficient is independently checked to be
`36*8^m` in both cases.  At every larger index both margin polynomials
are identically zero by the support convention, so there are no omitted
nontrivial Fourier indices.

The single strength is `lambda=3*2^(2m-3)`, represented as positive integer
numerator `N` and denominator `D`.  Its certificate entries are

`4D times each degree-2 Bernstein coefficient of delta_n(L)-lambda L_n`.

The midpoint certificate entries are

`8 times each tensor degree-(2,2,2) Bernstein coefficient of
 alpha delta_n(H)-8 b0 H_n`,

where `alpha=H(tau)_0-2`, and `b0=H(d)_0` or `H(yd)_0` respectively.
The value of `alpha` is separately computed directly from the binomial
central-coefficient formula for `t`, rather than extracted from any writer
certificate.

## Exact Bernstein convention and continuum implication

Define `B_(k,2)(a)=binom(2,k)a^k(1-a)^(2-k)`.  For `j=0,1,2`,

`a^j=sum_(k=j)^2 [binom(k,j)/binom(2,j)] B_(k,2)(a)`.

Indeed `binom(2,k)binom(k,j)/binom(2,j)=binom(2-j,k-j)`, so the sum is
`a^j(a+(1-a))^(2-j)=a^j`.  Multiplying this identity across the three
independent coordinates proves the tensor coefficient convention used by
the audit:

`beta_k=sum_(p<=k) power_coefficient_p product_i
 binom(k_i,p_i)/binom(2,p_i)`.

All weights are computed from this defining rational formula.  For the
single case, multiplying by `4D` clears denominators.  For the midpoint,
multiplying by `8` clears all tensor denominators.  Both scales are strictly
positive and preserve signs.  Since the Bernstein basis entries are
nonnegative and sum to one everywhere on `[0,1]` or `[0,1]^3`, strict
positivity of every Bernstein coefficient proves strict positivity of
the margin polynomial over the entire continuum.

The supported rows themselves are positive: `tau-2` is Laurent-positive
through its full degree, while `c,d` are Laurent-nonnegative, so the
factor forms prove positivity on the complete parameter boxes.  The audit
also checks the half-row entry at `r=2` or `r=s=u=2`, where it is smallest,
at every supported index.  Thus the single certificates establish the stated uniform strength,
and the midpoint certificates establish the scaled relative inequality
at every supported index.

## Hash convention and scope

Cases are ordered by increasing `m`, then original before smoothed, then
single before midpoint.  Inside a case, Fourier indices increase from
zero through the degree; Bernstein indices are lexicographic in
`product(range(3),repeat=dimension)`.  Each exact signed integer margin is
encoded as its decimal representation followed by one newline in UTF-8.
The SHA-256 digest commits to this complete sequence, rather than merely
to minima, selected vertices, or samples.

This audit only supplies the finite continuum certificates and their
primary-writer comparison.  The analytic tail, all-minor transfer, factor
coverage, ray algebra, orientation, and final Local TP2 conclusion remain
separate obligations.

## Final exhaustive result

All **1,640 cases** and **14,766,150 integer Bernstein margins** passed,
with no negative or zero supported margin.  The independent minimum over
all recorded margins is **1080**.  The four constituent scopes are:

| Block | Cases | Margins | Smallest integer margin | Witness `(m,n; Bernstein index)` |
|---|---:|---:|---:|---|
| Single `L` | 410 | 507,990 | 1080 | `(0,3;0)` |
| Smoothed single `yL` | 410 | 509,220 | 1080 | `(0,4;0)` |
| Midpoint `H` | 410 | 6,868,935 | 586368 | `(0,6;0,0,0)` |
| Smoothed midpoint `yH` | 410 | 6,880,005 | 521856 | `(0,7;0,0,0)` |

Every one of the primary writer's **1,640 case SHA-256 digests** matched.
The finalizer also compared case ordering, degree, margin count, negative
and zero counts, exact minimum, first minimizing witness, single strength
numerator/denominator and scale, and midpoint `alpha`, reference central
entry and scale.  All matched.  The primary output file SHA-256 is

`217229b56cd5f11029f3eebd8c2df6d2e0955a7e12689f172281fe68750e5725`.

The source SHA-256 of the arithmetic replay is

`c42ec27796f49b73ab0061db710597ed1348cc9d616df223c3c6bc594d515245`.

The exact run was split during execution to reduce wall time.  The initial
process checkpoint reached `m=355`; its cases `0..349` were retained in
`finite_audit_prefix_results.json`, and its completed overlap `350..355`
was discarded.  A parallel independent process recomputed and retained
`350..409` in `finite_audit_tail_results.json`.  The retained segments are
disjoint and cover the full range exactly; the finalizer verifies the
complete ordered list before opening the primary expected output.  The
prefix checkpoint elapsed time was `474.859` seconds and the tail run
elapsed time was `370.441` seconds; the processes overlapped.

The designated final artifact is `finite_audit_independent_results.json`.
The two segment JSON files preserve the execution checkpoints and checksums,
and `finite_audit_finalize.py` preserves the merge and comparison procedure.
From `second_turn_20261004`, the simplest complete rerun is:

```bash
python finite_audit_independent.py --min 0 --max 409 --output finite_audit_independent_results.json --expected kernels_certificate_results.json
```

To reproduce the segment merge and every metadata comparison, run the
following first two commands concurrently if desired, then run the finalizer:

```bash
python finite_audit_independent.py --min 0 --max 349 --output finite_audit_prefix_results.json
python finite_audit_independent.py --min 350 --max 409 --output finite_audit_tail_results.json
python finite_audit_finalize.py
```

The finalizer's mathematical inputs are the two independently computed
segments.  The original execution history recorded in it describes this
audit session; reruns may have different elapsed times.
