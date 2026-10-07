# Independent frozen algebra — second turn

Frozen before reading any new sibling manuscript or implementation. This
derivation uses only the brief, the canonical first-right formula, and the
prefix recurrence documented in `structural_proof.md`.

Put `y=x+1`, `z=2y+1`, `a=T_(m+1)`, `c=T_m`, `d=T_(m+2)`.
The prefix recurrence is `d=z*a-c+1`. Set

`P=1+y*c`, `X=1+y*a`, `tau=3yX-x=z+3y^2*a`.

The first-right center is

`C1=(3yP-x)X-1-xP=tau*P-1-xX`.

Thus the ray recurrence extends consistently to `Q_-2=1`,
`Q_-1=P`, `Q_0=C1`. In particular, its preceding gap is `y*c`.
Directly expanding gives

`C1-P-y(tau*c+d)=zX-P-y-y*d`

`=z(1+y*a)-(1+y*c)-y-y*(z*a-c+1)=0`.

For `Delta_ell=Q_ell-Q_(ell-1)` subtraction of the two consecutive
inhomogeneous recurrences gives

`Delta_(ell+1)=tau*Delta_ell-Delta_(ell-1)`.

Its initial values are `Delta_-1=y*c`, `Delta_0=y*(tau*c+d)`.
The second-kind recurrence therefore proves, for every `ell>=-1`,

`Delta_ell=y*(c*U_(ell+1)(tau/2)+d*U_ell(tau/2))`,

with `U_-1=0`. Summing from `Q_-2=1` gives, for `ell>=-1`,

`Q_ell=1+y*(c*R_(ell+1)(tau)+d*R_ell(tau))`,

where `R_-1=0`. No positivity or kernel assumption enters these
identities. At `m=0`, `c=1`, `a=2x+4`, `d=4x^2+14x+12`;
the identities include this boundary without a singular division.

## What changes, and what does not

At inner index `n=m+1`, the previously proved first-turn construction
has coefficient pair `(A,B)=(T_(n+1),T_(n-1))=(d,c)`.
The present outer bracket uses `(c,d)`, the reverse pair, and is shifted
by one outer index. This is a real exact cancellation of the formerly
negative initial coefficient. It is not a reparameterization which
automatically meets the old theorem's hypotheses: its dominant prefix
is the smaller one. The old block statements `A>=B` and correction
domination consequently cannot be imported by swapping names alone.

The result proved here is an exact algebraic reduction, not folded
kernel membership, relative minor strength, proxy comparison, or Local
TP2. Positive ordinary coefficients of the new brackets do not settle
any of those obligations.
