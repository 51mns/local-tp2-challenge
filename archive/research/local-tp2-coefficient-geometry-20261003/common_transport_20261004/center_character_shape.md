# Character shape: a proved tail lemma and a false sufficient candidate

Status: one general tail lemma proved; one explicit standalone character
candidate refuted. Neither proves canonical center-F preservation under
both mutations. The canonical strip and Fricke correlations remain
available but have not been converted into preservation of the proposed
character shape.

## 1. An exact character form of the folded defect

Let h have finite positive interval support 0,...,m and let its positive
character row be `alpha_n=h_n-h_(n+1)`. Put `alpha_-1=-alpha_0` and
`alpha_(m+1)=0`. Direct substitution, including reflection at zero, gives

`delta_n(h)=h_n(2alpha_n-alpha_(n-1)-alpha_(n+1))`

`             +alpha_n(alpha_(n-1)-alpha_n)`.                 (1)

At zero this is exactly `h_0(3alpha_0-alpha_1)-2alpha_0^2`.
The cross term in (1) changes sign in the increasing character band;
dropping it cannot justify cone closure.

## 2. Log-concave characters decide the band after their mode

**Lemma.** Suppose the positive character row is log-concave. At every
`1<=n<=m` for which `alpha_(n+1)<=alpha_n`,

`delta_n(h)>=alpha_m(alpha_n-alpha_(n+1))>=0`.                (2)

Thus log-concavity of the actual character row would make the weak
folded-kernel question automatic from its mode onward. It does not
provide leading-coefficient strength, and it does not settle the
increasing character band or zero index.

Proof: for n<m put `A=alpha_n`, `B=alpha_(n+1)`, `q=B/A`.
For `0<q<1`, log-concavity gives `alpha_(n-1)<=A/q` and all subsequent
ratios at most q. Equation (1) decreases as alpha_(n-1) increases because
its coefficient is `A-h_n<=0`. Hence

`delta_n(h)>=A(1-q)/q * [A-(1-q)h_n]`.

The exact telescoping identity

`A-(1-q)h_n=sum_(j=n)^(m-1)(q alpha_j-alpha_(j+1))+q alpha_m`

has nonnegative summands by log-concavity. Its lower bound `q alpha_m`
proves (2). If q=1, log-concavity gives alpha_(n-1)<=A and the exact
defect is `(h_n-A)(A-alpha_(n-1))>=0`, while the right side of (2)
is zero. At n=m, zero extension gives `delta_m=alpha_m^2`, exactly
the claimed terminal bound. No normalization, Fricke division, or
unbounded-index scan is used.

The geometric estimate alone can also give a strict margin when q<1;
its strength relative to h is state dependent. One cannot replace it
with leading strength: for characters `(8,4,2)`, the half-row `(14,6,2)`
has `delta_1=4<2h_1`, despite log-concavity and terminal character 2.

## 3. A natural dimension-normalized candidate is insufficient

Freeze candidate W for a center C as follows:

1. C has positive ordinary and character coefficients;
2. `beta_n=alpha_n/(2n+1)` is nonincreasing and log-concave;
3. `delta_0(C)>=2H(C)_0`.

This is a finite shape predicate independent of the outgoing LR target.
Its status is **ROOT: proved; BOTH: not proved; IMPLIES CENTER F / TARGET:
false as a standalone abstract implication.** It does not include the
actual canonical strip or Fricke relation, and no counterexample to
their combined use is asserted.

The canonical root has characters `(3,4,2)`, normalized row
`(3,4/3,2/5)`, and central defect `27>=2*9`, so ROOT is exact.

The ordinary-positive polynomial

`C=1495+57105x+32805x^2`

has characters `(10000,24300,32805)`, normalized row
`(10000,8100,6561)` and half-row `(67105,57105,32805)`.
The normalized row is a decreasing geometric progression, hence
log-concave. Nevertheless its defects are

`(182498500,-16566525,1076168025)`.

The central 2-strength margin is `182364290>0`, but the index-one
folded minor is negative. Thus even dimension-normalized character
log-concavity and a strong central defect do not solve the increasing
band. This is a standalone polynomial obstruction, not a canonical
state, not a Fricke state, and not a child-preservation failure.

Run `python center_character_reproducer.py` for the exact obstruction
and root checks; it uses only Python integers/Fractions and saves
`center_character_results.json`. No parent implementation is imported.

## 4. Remaining canonical question

The known strip writes `C=(t_X-1)Y+rho`, `0<_B rho<=_B Y`. Its residual
is already known to fail both cone membership and a uniform LR order
at an actual first-level state. Hence treating rho as an independent
positive cone summand remains invalid. Equation (1) shows precisely
which signed character cross term needs correlated control.

An actual log-concavity induction for alpha(C), if proved from ancestry,
strip and Fricke, would supply the weak terminal band through (2).
It has not been proved here. Neither the existing character domination
nor the exact scalar Fricke equation has yet been converted into an
all-index inequality for that induction or for the required central
strength. Center F, actual incoming-gap cones, M cones, and the strict
proxy still need common mutation closure. No all-tree conclusion follows.
