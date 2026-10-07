# Independent audit of the Robin and BOTH-child subgates

**Verdict: PASS within the stated conditional scope.** The general
`|rho|<=1` Robin theorem, its contiguous-window corollary, the reversed
child single block at parameter `-1`, and the retained-origin strict
`K_Q` consequence are proved. The full changed-center paired midpoint
packet and the overlap part of the strict proxy are still **OPEN**.

This is an independent algebraic and analytic proof review, not an
inference from the authors' finite recurrence replays. No additional
path search or parameter scan was performed. The universal character
equivalence in `network_relative_character.md` is used as the exact
all-ordered-minor bridge; it has two independent proof audits.

## Reviewed versions and scope

| Source | SHA256 |
| --- | --- |
| `packet_transport_subgate.md` | `1a20e673d2941e67da3310c321e19e4ae22f73aa18fe481410b9e7a790e3f9fb` |
| `proxy_robin.md` | `933501e6dad682c7276b9a91892fa5fecf4c9d56759d4353a118301f39ca05b2` |

The previously certified endpoint-1 theorem in `root_boundary_q.md`
(SHA256 `c34c71c4c7a7f36a54ffb8e9d1eaf6190c82628e5f5fdc0197273d9e6acf9a8a`)
is imported for the exceptional origin. Its continuum Bernstein
certificate and complete congruence partition already have an independent
boundary audit; this note does not replace that audit. The separate root
new-center packet certificates are not needed in the Robin proof and are
outside this audit's root-certificate scope.

## 1. The strict product boundary argument is complete

For a weak folded-TP2 half-row `a_0,...,a_h` of positive interval support,
define

`Delta_0=a_0^2-a_1^2`,

`Delta_j=a_j^2-a_(j-1)a_(j+1)` for `j>=1`.

Zero extension and reflection give, including at zero,

`delta_j=Delta_j-Delta_(j+1)`,

`Delta_j=sum_(k=j)^h delta_k>0` for `0<=j<=h`,

because `delta_h=a_h^2>0`. Thus weak folded TP2 supplies a strictly
positive pure Toeplitz adjacent minor at every difference up to `h`;
no strictness of the weak factor has been assumed.

Let the first factor be strict of degree `f>=h>=1`. For output defect
index `1<=n<=f+h`, retain in Cauchy--Binet the intermediate pair

`i,i+1`, where `i=max(h,min(n,f))`.

Then `h<=i<=f`, `i+n>h`, and `|i-n|<=h`. The first minor is its strict
defect `delta_i>0`. All four reflected sum-index entries in the second
minor vanish. The remaining determinant is exactly `Delta_|i-n|>0`.
For output index zero, take `i=h`; the second minor is `2a_h^2>0`,
including the folded column-zero normalization. All other CB terms are
nonnegative. This proves strictness at zero, every interior index, and
the terminal index. Positive interval support of the product follows
from convolution of the two positive intervals.

The degree condition in `MP2_exact` gives
`deg L_r=deg b0+d>=d`. Every subsequent shifted trace factor has degree
`d`. Thus the comparison `f>=h` holds at each step; the `y` version has
one additional degree. No arbitrary multiplication-by-`y` assertion is
used. If multiplying two strict factors of unequal degrees, their order
can be chosen so the larger degree is the first factor.

## 2. Robin mixture: support, simplicity, residues, and mixed signs

Use the normalized recurrence
`U_-1=0,U_0=1,U_j(T)=T U_(j-1)(T)-U_(j-2)(T)`.
For the path with terminal diagonal `rho`,

`p_N=U_N-rho U_(N-1)`

is its characteristic polynomial, and deleting the first vertex leaves
`p_(N-1)`. Gershgorin bounds its spectrum by `[-2,2]` for `|rho|<=1`.
The nonzero path edges show that a first-coordinate-zero eigenvector
must vanish; each eigenspace is at most one-dimensional, hence the
spectrum is simple. The first-coordinate spectral weights are strictly
positive and sum to one. At `N=1`, `p_0=1` and the formula is exactly
`1/(T-rho)`; there is no missing empty-matrix convention.

Consequently the polynomial identity is

`q_N-rho q_(N-1)=sum_i w_i L_(lambda_i) prod_(j!=i)(T-lambda_j)`.

Every summand has degree `deg b0+Nd`, positive interval support, and
strict defects by Section 1. The strict degree premise prevents leading
term cancellation, even when `b1` is signed. For a distinct pair of
summands, cancelling their common factors leaves exactly

`L_(lambda_i)(T-lambda_j)`, `L_(lambda_j)(T-lambda_i)`.

The parent `MP2_exact` mixed character gate signs this pair. Reintroducing
the common factors multiplies the mixed tensor by nonnegative character
tensors. Thus all off-diagonal quadratic terms are nonnegative. The
positive diagonal terms are strict at every supported index, since all
summands have the same support degree. This proves the raw conclusion.
The proof for the smoothed conclusion uses the separately assumed
`yL` and `J(yF,yG)`, with the same common factors. No seed cone, `K_y`
cone, `N=0` conclusion, or enlarged spectral radius is hidden here.

The older uniform reference-4 packet implies this sharp mixed gate:
where a reference character coefficient is nonnegative use the
reference-4 lower bound and `omega<=4`; where it is negative use the
weak midpoint cone. This does not require the reference tensor itself
to be nonnegative.

## 3. Contiguous windows and both actual child identities

The two exact window formulas hold for the general recurrence sequence:

`sum_(j=m)^(m+2k) q_j=(U_k+U_(k-1))q_(m+k)`,

`sum_(j=m)^(m+2k-1) q_j=U_(k-1)(q_(m+k)+q_(m+k-1))`.

For the odd formula, sum the paired identities
`q_(N+h)+q_(N-h)=C_h(T)q_N` and use
`1+sum_(h=1)^k C_h=U_k+U_(k-1)`.
For the even formula, the paired term at distance `j` from the
half-integer center is
`q_(N+j)+q_(N-1-j)=(U_j-U_(j-1))(q_N+q_(N-1))`.
Summing `j=0,...,k-1` telescopes to `U_(k-1)`.
The odd prefactor is `p_k` at `rho=-1`; the
even prefactor is a pure-path polynomial. Their roots lie in `[-2,2]`,
so they can be multiplied as shifted factors using Section 1. The
initial strict factor is a Robin run with `N=m+k>=1`, at `rho=0` or
`rho=-1`. Odd `k=0` has prefactor `U_0+U_-1=1`; even `k>=1` causes no
negative index. These identities prove strict raw and smoothed windows,
without proving compatibility with an external initial anchor.

For the exact child tuple in the reviewed note, substitute
`T'=T+beta v`, `c'=(T-beta n+1)v+h`, `e'=n`. Direct cancellation gives

`n(T'-r0)+c'=p(T-r0)+h+(r0+1)v`, `p=n+v`.

The two cases at `r0=-1` are therefore

| Child | Exact reversed single block | Strictness source |
| --- | --- | --- |
| short | `(T+1)c+e` | parent forward `L_-1` |
| long | `(T+1)(c+Te)-e=e(T^2+T-1)+c(T+1)` | reversed-origin `q_2+q_1`, Robin `N=2,rho=-1` |

The potentially large `beta n v` terms cancel before the sign argument.
Both raw and `y` blocks are consequently strict under the old paired
packets. This is a genuine BOTH-child subgate; it does not consume the
new child's packet, trace cone, or proxy.

## 4. Strict K_Q from retained origins and the exact residual overlap

The proxy note specializes Robin to `rho=1`. Its two quadratic-form
identities are exact, including `N=1`, and show the spectrum is strictly
inside `(-2,2)`. It is otherwise precisely Section 2. For an ordinary
certified origin, both `f_N-f_(N-1)` and its `y` multiple are strict for
every `N>=1`.

The actual smaller register has `g=f_(N_X-1)`, `s=f_(N_X)` and
`Q=y(s-g)`. At the short child it retains the X origin with index
`N_X+1>=3`; at the long child it retains the Y origin with index
`N_Y+1>=2`. The Y origin is ordinary. An endpoint-1 origin occurs only
in the retained short register, where the imported boundary theorem
applies for all indices at least two. Thus BOTH actual child `K_Q`
gates follow noncircularly, including root edges.

The identity `Pi=PQ+V` gives exactly

`W_n(Q,Pi)=delta_n(Q)+q_n v_(n+1)-q_(n+1)v_n`,

including reflected `q_-1=q_1` at zero. With `d_C>d_X` the leading-degree
calculation is

`deg Q=d_X+d_C+1`, `deg Pi=deg Q+1`, `deg V=d_C+2`.

For `X=1`, the terminal proxy is `6(lc C)^2`; for `d_X>=1` it is
`(3 lc X lc C)^2`. These are positive. Where `n>deg V`, the correction
vanishes and the strict `K_Q` theorem suffices. Hence the precise
remaining overlap is

`0<=n<=min(deg Q-1,deg C+2)`.

Neither strict `delta(Q)` nor origin midpoint compatibility signs this
correction. In particular the correction at `n=deg V<deg Q` is negative,
`-q_(deg V+1)lc V`, so it cannot simply be discarded.

The ancillary fixed-endpoint identities also check directly:

`A Pi=3yXP Q+XP[A+Px]`,

`A+Px=3yX+P(x-1)=3yX+x^2+x-2`,

`R(A,3yXP)=T_A+R(A,P^2)`.

The last identity uses `3yXP=PA+P^2`. Since the Fourier half-row of
`P^2` is `(6,4,1)`, its adjacent correction coefficients are exactly
`4a_0-6a_1`, `a_1-4a_2`, `-a_3`, and then zero. The shifted gate
`K_(A+4)` yields `delta_1(A)-4a_2>=0`; the zero and second source
indices remain uncontrolled. This deduction cannot establish the
strict proxy or a sourcewise nonnegative transfer.

## 5. Open flux remains open

The reverse midpoint identity in the packet note follows by substituting
the exact child tuple and cancelling its `beta^2 n v^2` terms:

`H'_reverse=H_base+[(alpha+1)(T-alpha)+omega]v`

`             +beta v L_base+beta(alpha+1)v^2`.

Its factor `alpha+1` has both signs on the required parameter domain.
The general six-term sharp tensor expansion is also an exact quadratic
polarization of `H'=H0+zeta0 A1+zeta0^2 b0'`; it gives an obligation,
not a positivity proof. Neither the all-window theorem nor the single
parameter BOTH subgate supplies the missing cross-center mixed terms.

The reviewed notes correctly preserve the final distinction: common
Robin, single-block, and retained-origin `K_Q` subgates are proved;
new-center paired `MP2_exact` transport and regular-edge strict proxy
overlap remain unresolved. Full-tree Fourier Local TP2 is not claimed.
