# A genuine BOTH-child single-block subgate and the remaining midpoint flux

**Status.** The reversed child single block at parameter `r=-1` is strictly
folded TP2, in both the raw and `y` modes, for BOTH exact mutations of every
regular state carrying the old paired midpoint packets. This is a proved
analytic mutation subgate. It does not prove the other single blocks, the
new trace gate, or either full new-center packet. The root child full packets
are established separately by the quantitative lane's parameter certificates.

All older directories are read-only. The calculation below preserves the
canonical trace/seed correlations; it does not replace them by arbitrary
positive triples.

## 1. The minimal midpoint hypothesis used here

Write `Phi` for the established symmetric two-variable rotation followed by
the SU(2) x SU(2) character expansion, and put

`T_f = Phi(f(xi) f(zeta))`,

`J(f,g) = Phi(f(xi) g(zeta) + g(xi) f(zeta))`.

Character nonnegativity is denoted `>=_char 0`. For a trace `T` of degree
`d>=1` and seeds `(b0,b1)`, assume the strict degree condition

`deg b1 < deg b0 + d`.

The following midpoint hypothesis, denoted `MP2_exact(T,b0,b1)`, suffices:

* Every `T-r`, `-2<=r<=2`, has positive Laurent interval support and a weak
  folded-TP2 kernel.
* Every `L_r=b0(T-r)+b1` and `yL_r` has positive Laurent interval support and
  strictly positive supported folded defects.
* For every `r,s` in that interval, with
  `F=L_r(T-s)`, `G=L_s(T-r)`, both `J(F,G)` and `J(yF,yG)` are character
  nonnegative.

This last condition is exactly the all-mixed-minor condition. If
`alpha=(r+s)/2`, `omega=(r-s)^2/4`, and

`H=b0[(T-alpha)^2-omega]+b1(T-alpha)`,

then `F=H+(r-s)b1/2`, `G=H-(r-s)b1/2`, and

`J(F,G)=2(T_H-omega T_b1)`.

The same equality holds after multiplying both arguments by `y`. Thus this
is the sharp relative certificate, not the older uniform reference `4T_b1`.
The prior packet, which includes weak TP2 of `H` and the uniform all-minor
bound against `4|b1|`, implies this exact condition coefficient by coefficient:
use the uniform bound where the reference coefficient is nonnegative, and
the TP2 of `H` where it is negative. No cone assumption on `b0`, `yb0`,
`b1`, or `yb1` is used.

## 2. Robin run theorem, with no radius enlargement

Set `U_-1=0`, `U_0=1`, `U_j(T)=T U_(j-1)(T)-U_(j-2)(T)`, and

`q_N=b0 U_N(T)+b1 U_(N-1)(T)`.

**Theorem.** Under `MP2_exact(T,b0,b1)`, for every `N>=1` and every real
`rho` with `|rho|<=1`, both

`q_N-rho q_(N-1)` and `y(q_N-rho q_(N-1))`

have positive Laurent interval support and strictly positive supported
folded defects.

**Proof.** Let `A_N(rho)` be the real symmetric path matrix on `N` vertices,
with off-diagonal entries `1`, zero diagonal except terminal diagonal `rho`.
Its characteristic polynomial is

`p_N(T)=U_N(T)-rho U_(N-1)(T)`.

Deleting its first vertex gives the same Robin path on `N-1` vertices, so
the corresponding characteristic polynomial is `p_(N-1)`. All eigenvalues
`lambda_i` lie in `[-2,2]`: each Gershgorin radius plus the absolute diagonal
entry is at most `2`, since the terminal row has `1+|rho|<=2`. For `N>=2`
the nonzero successive off-diagonal entries imply simple eigenvalues and
nonzero first coordinates of every eigenvector. The first-coordinate
resolvent therefore has the exact partial-fraction expansion

`p_(N-1)(T)/p_N(T) = sum_i w_i/(T-lambda_i)`,

where `w_i>0` and `sum_i w_i=1`. For `N=1` this is the single identity
`1/(T-rho)`. Consequently

`q_N-rho q_(N-1) = sum_i w_i L_(lambda_i) prod_(j!=i)(T-lambda_j)`.

Call the summands without their weights `P_i`. Each has the same degree
`deg b0+Nd`, has positive Laurent interval support, and is strict folded TP2.
Indeed, `L_(lambda_i)` is strict, while every shifted factor is weak TP2;
at each multiplication the current strict degree is at least the degree of
the weak factor. Here is the complete strict-product argument. Write those
degrees as `f>=h>=1`, and the weak half-row as `a_j`. Its weak defects give
`Delta_j=sum_(k=j)^h delta_k>0` for `0<=j<=h`, because the terminal defect
is `delta_h=a_h^2>0`. For an output defect index `1<=n<=f+h`, retain the
Cauchy--Binet intermediate adjacent columns `i,i+1`, where
`i=max(h,min(n,f))`. The first minor is the strictly positive defect of
the first factor at index `i`. In the second minor, all reflected sum-index
entries vanish because `i+n>h`; it is the pure Toeplitz minor
`Delta_|i-n|>0`, with `|i-n|<=h`. For output index `n=0`, choose `i=h`;
the second minor is `2a_h^2>0`. This proves strictness through the entire
support, including its endpoints, and applies successively to every
degree-`d` shifted factor.

For distinct `i,j`, remove their common shifted factors. The remaining
pair is exactly

`L_(lambda_i)(T-lambda_j)`, `L_(lambda_j)(T-lambda_i)`.

Their mixed character polynomial is nonnegative by `MP2_exact`. Multiplying
back the common factors multiplies it by their character tensors, which
are nonnegative by folded product closure. Hence all `J(P_i,P_j)` are
nonnegative. Expanding

`T_(sum_i w_i P_i)=sum_i w_i^2 T_Pi + sum_(i<j) w_i w_j J(P_i,P_j)`

proves the cone assertion, with strictly positive supported defects supplied
by the diagonal terms. The identical argument uses `yL_(lambda_i)` and
`J(yF,yG)` for the `y` mode. The seeds themselves are never asserted to be
cones. There is no claim for `N=0`. QED.

For later use, every contiguous equal-weight window
`sum_(j=m)^(m+ell-1) q_j`, `m>=1`, `ell>=1`, is strict in both modes.
For `ell=2k+1` it equals `(U_k+U_(k-1))q_(m+k)`; for `ell=2k` it equals
`U_(k-1)(q_(m+k)+q_(m+k-1))`. The first prefactor is a Robin path
polynomial with terminal diagonal `-1`, the second a pure path polynomial.
Their roots lie in `[-2,2]`; apply the theorem with `rho=0` or `rho=-1`
and multiply the shifted factors one at a time. This window corollary does
not give compatibility with an additional initial anchor and is not a
closure theorem for endpoint differences.

## 3. Exact BOTH-child tuple and the beta cancellation

Use the canonical normalized variables

`y=x+1`, `beta=3y^2`, `t=2x+3+beta a`,

`g=(t-2)e+(1+ya)(3(1+ya)-2)+r`, `s=tg-r`,

`C=1+y(a+e+g)`, `T=3yC-x`, `d=e(T+1)`,

`c=e+g+s`, `cB=c+Te`.

For `sigma=0` (short) or `sigma=1` (long), put

`n=g+(1-sigma)e`, `v=s+sigma d`,

`u=T-beta n`, `h=(1-2sigma)e`, `p=n+v=c+sigma Te`.

The exact child paired tuple is

`T'=u+beta p=T+beta v`, `c'=(u+1)v+h`, `e'=n`.

Its reversed single block at arbitrary parameter `r0` satisfies the exact
cancellation

`L'_(r0),reverse=n(T'-r0)+c'`

`                 =(T-r0)n+(T+1)v+h`

`                 =p(T-r0)+h+(r0+1)v`.

In particular, the potentially large term `beta n v` cancels before any
positivity inference. At `r0=-1`:

* Short: `L'_-1,reverse=(T+1)c+e=L_-1(T,c,e)`.
* Long: `L'_-1,reverse=(T+1)cB-e`
  `=e(T^2+T-1)+c(T+1)=q_2+q_1`, where the parent reversed origin has
  `(b0,b1)=(e,c)`.

The first expression is directly strict by the parent forward packet.
The second is the Robin theorem with `N=2,rho=-1` for the parent reversed
packet. Therefore BOTH children preserve this actual single-block gate in
both raw and `y` modes. No Fricke relaxation, fixed-trace radius `5/2`,
or finite testing is used. The original paired MP2 and its exact midpoint
replacement both supply the required parent hypotheses.

## 4. Exact sharp flux for the still-open changed center

The cancellation does not sign every reversed single block. For the short
child the last line is `L_(r0)(T,c,e)+(r0+1)s`; its cross compatibility with
the retained-origin term is not an axiom of the parent packet. For the long
child the base pair is `(cB,-e)`, a signed advance of `(e,c)`, and is not the
parent positive pair. A generic fixed-trace advance would enlarge the
Robin spectral interval when `|r0|>1`.

The full reverse midpoint block has the exact additional identity

`H'_reverse = H_base + [(alpha+1)(T-alpha)+omega]v`

`             + beta v L_base + beta(alpha+1)v^2`,

where `L_base=p(T-alpha)+h` and
`H_base=p[(T-alpha)^2-omega]+h(T-alpha)`.
Here `p=c,h=e` in the short case, and `p=cB,h=-e` in the long case.
The signed coefficient `alpha+1` cannot be discarded on the parameter
domain. This identity identifies the cross-center term precisely; it does
not assert a negative actual minor.

For either orientation of the new pair, write its seeds as `(b0',b1')`,
set `zeta0=beta p`, and define

`H0=b0'[(u-alpha)^2-omega]+b1'(u-alpha)`,

`A1=2b0'(u-alpha)+b1'`.

Then `H'=H0+zeta0 A1+zeta0^2 b0'`, and its exact mixed certificate is

`B'=T_H0-omega T_b1' + J(H0,zeta0 A1)`

`   + J(H0,zeta0^2 b0') + T_zeta0 T_A1`

`   + J(zeta0 A1,zeta0^2 b0') + T_zeta0^2 T_b0'`.

The parameter domain is
`|alpha|<=2`, `0<=omega<=(2-|alpha|)^2`. The `y` mode uses the same formula
after replacing each seed by its product with `y`. Thus the remaining sharp
all-mixed-minor obligation is exactly `B'>=_char0` throughout this domain
for BOTH tuples and BOTH orientations. Parent packets certify neither the
base pair `(b0',b1')` at trace `u` nor these cross-center `J` terms. Paired
Cassini and origin ancestry remain available correlations, but no argument
here converts this signed flux into nonnegative parent certificates.

This document proves one common analytic mutation subgate and gives the
exact residual certificate. The global new-center packet transport and the
regular-edge strict proxy remain OPEN.
