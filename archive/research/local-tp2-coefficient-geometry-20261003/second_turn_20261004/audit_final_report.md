# Independent adversarial proof audit: the additional-turn family

**Verdict: PASS for the additional-turn theorem, with the explicitly
inherited audited foundations. The complete independent finite kernel
and proxy replays have passed, including all supported indices and
continuum Bernstein coefficients.**

The target is the original strict canonical Local TP2 inequality at every
`L^m R L^ell`, `m,ell>=0`, through the terminal index `deg S`. It is not
the family `L^m R^k L^ell` for unrestricted `k`, and not the full tree.
The older theorem for every `L^m R^k` remains a dependency.

This audit independently froze the base algebra before reading new
sibling implementations. `audit_frozen_algebra.md` gives that derivation;
`audit_identity_check.py` reconstructs the original scalar mutations,
prefixes and binomial Fourier map without importing any sibling or
parent implementation. Its 91 cases `0<=m<=12`, `0<=ell<=6` pass.
Those finite original Local TP2 checks are implementation evidence only;
the infinite proof is the analytic assembly audited below.

## 1. The exact reversal is real, but positivity alone was already known

Extending the actual fixed-X recurrence to `Q_-2=1`, `Q_-1=P` is
consistent with its original first-right center. The identity

`Q_0-P=y*(tau*c+d)`

follows from `d=z*T_(m+1)-c+1`. Its preceding gap is `yc`.
The homogeneous gap recurrence therefore gives exactly

`Q_ell-Q_(ell-1)=y*(c U_(ell+1)+d U_ell)`,

`Q_ell=1+y*(c R_(ell+1)+d R_ell)`.

Equivalently, beginning at the first gap would give the signed expression
`y*((tau*c+d)U_j-c U_(j-1))`; the Chebyshev recurrence absorbs its
negative term into `c U_(j+1)+d U_j`. This is a substantive family-specific
cancellation. It does not reverse the hypotheses of the earlier theorem
for `(d,c)`: the old coefficient ordering is unavailable.

The earlier raw-positive transfer and normalized quotient routes already
supplied ordinary-coefficient positivity. They left folded-kernel
membership, quantitative mixed compatibility and the final smoothed
comparison open. The new contribution is the proof of those actual
obligations for this restricted reversed pair, not a claim that positive
component kernels or ordinary coefficients imply a kernel for their sum.
No claim about academic novelty or external acceptance is made.

## 2. Orientation and the initial LR package

For `ell>=1`, the lower endpoint is X and

`S=q_(ell+2)`, `D=(Q_(ell-1)-X) M`,

`M=2(x+2)+3y^2 Z_ell`.

The center degree is `(ell+2)(m+3)-2`. The two terms of the gap
formula differ in degree by `m+1`; a preliminary wording saying one
was corrected before finalization. At `ell=0`, P is the lower endpoint.
The new ray continuation is then the long child, so that boundary uses
the existing one-turn theorem.

The all-left ordering applies at indices `j>=1`. Grouping the low
prefix terms as `p0+p1` or `2p0+p1` correctly avoids assuming an order
for `p0` alone. The new correction beta has a fixed-upper-row mixture
comparison, including `m=0`. Using old Local TP2 at `L^mR` gives
`q1<=lr q2`, `beta<=lr q2`, and `X(x+2)<=lr E1` for every m.

The homogeneous recurrence transports time order starting at q1.
Starting at q0 would fail: at m0 its first comparison minor is -36.
The recurrence sign, fixed-row summation, and subtraction of the
narrower row yield exactly

`S<=lr y(tau-2)Z`, `X(x+2)<=lr E`.

No additive folded-cone closure enters this argument.

## 3. The all-minor and kernel tail arguments

`audit_scaled_relative_minors.md` independently proves the scaled
corollary: if h is lambda-strong, `h>=alpha*b`, `b_n<=b0`, and
`lambda*alpha>=8b0`, then every ordered folded minor satisfies
`det K_h>=4 det K_b`. A positive reference minor makes both h diagonal
entries positive, exactly the hypothesis of the inherited all-minor
strength theorem. This is valid at every kernel index, without
enumeration. For midpoint H, `alpha=H(tau)0-2` follows from its
actual `d(tau-u)` summand. The smoothed proof uses reference yd and
independently proved strength of yH.

The reversed correction domination is exact. The elementary prefix
recurrence gives `d<=16y^2c`. With
`a0=H(T_(m+1))0>=6^(m+1)/(2m+3)` and `J=tau-2`,

`J>=3a0*y^2`, `J>=(tau+2)/3`,

so double and single corrections are bounded by respectively

`epsilonH=16(2m+3)/6^(m+1)`, `epsilonL=epsilonH/3`.

All these are Laurent coefficient inequalities; multiplication by y
preserves these inequalities, without any claim that y is a cone factor.

The normalized product degrees, conservative bounds

`EL=c0^2 sigma^(2m+1)/(4(m+2))`,

`EH=c0^3 sigma^(3m+2)/(16(m+2)(m+4))`,

and strength products `3*2^(2m-1)`, `9*2^(3m-1)` are correct.
The perturbation consumes at most half the normalized defect when
`E>=12epsilon`, and the resulting row is at most twice the dominant
one; hence one quarter of strength remains. Exact Fraction arithmetic
checks the m410 gates and both increasing consecutive ratios. The
remaining mass gate `9*2^(3m-3)>=4(7^(m+3)-1)` proves even the unscaled
relative threshold on the entire tail.

The midpoint polarization and factor 4 control all mixed ordered minors.
Jacobi resolvents and common omitted-root factors consequently prove
the actual sums, including y times each sum. N1 and N2 require no
nonconstant common factor and are covered by the independently smoothed
single/midpoint blocks. The prefix parity factorizations cover ZN and
yZN for every N>=1. At m0,N0, c=1 is itself strict on its support;
yc=y has central defect -1. That sole smoothed exception is explicitly
excluded and unused by the new target.

## 4. Central mass and all outer indices

The prefix quotient has an active Jacobi resolvent obtained from
`R_(2h)=U_h V_h` and `R_(2h+1)=U_h V_(h+1)`. Canceled outside roots
are restored as ordinary propagator factors. Every summand thus has
one L template and exactly N-1 shifted traces; active positive weights
sum to one and their count is at most N.

The reversed coefficient mass ratio remains bounded by two: the prefix
recurrence gives `d(2)<=57c(2)`, while `tau(2)-2>=221`. Thus each
summand mass exceeds half the mixture mass. Pairwise compatibility and
`sum weights^2>=1/N` give the stated central mass bound.

At m0, pairing the N-1 propagators with kappa80 and leftover alpha4/5
is valid on the entire independent root square. Both parity bases are
checked: N5 gives1280, N6 gives2560/3, each greater than beta221/3.
Each parity grows by `80N/(N+2)>1`. At m1, gamma40/alpha5 begins at
N4 with625>1517/6. At m2, gamma707/alpha5 begins at N2 with
3535/4>2600/3. The five lower outer cases are directly certified and
independently reconstructed in `falsification_proxy_audit_results.json`.

For m>=410, the trace degree and template degree give denominators
`2m+7`, `4m+7`. The smoothed J strength is `3*2^(m-1)` and
`J(2)<=756*7^m`. These yield the exact sufficient scalar gate
`(8/7)^m>10752(4m+7)`, valid at410 and propagated by its displayed
increasing ratio. The correction signs and factors of two in the final
proxy inequalities are conservative and correct.

## 5. Multiplier, terminal support, and final logical chain

The cone y^2 has supported defects `(4,0,1)`. In the product
`K_(y^2) K_Z`, intermediate pair `(0,1)` proves strictness through
deg Z; `(2,3)` proves the last two supported indices. In the commuting
order `K_Z K_(y^2)`, intermediate `(0,1)` proves `delta2(y^2Z)>=delta0Z`.
The four explicit perturbation formulas for `M=3y^2Z+2(x+2)` then
give strict multiplier defects from `delta0Z>6Z(2)`.

Fixed proxy minors have the correct sign. At low output indices,
retaining `(n,n+1)` gives at least `w_n delta0Z`; the additive remainder
costs at most `J(2)Z(2)K_n`. At higher indices the remainder is zero.
The retained fixed pair `(m+4,m+5)` has a strictly positive corresponding
kernel minor through `n=deg(JZ)`. Thus the terminal index is covered.

The final chain is

`S<=lr JZ <lr X(x+2)M<=lr EM=D`.

S and JZ have the same degree `2m+4+N(m+3)`, and all rows have dense
positive initial support. Interior strictness follows from consecutive
ratios; terminal strictness follows directly from `H(S)[deg S]>0` and
`H(D)[deg S+1]>0`. The complete new finite inputs have passed, so this
proves the target. The old theorem supplies ell0.

## 6. Reproducibility and precise audit limits

The inherited mathematical foundations are the folded-kernel criterion,
product/strength closure, all-minor theorem, audited normalized prefix
and trace bounds, Jacobi resolvents, and the existing one-turn theorem.
This report audits their new applications; it does not independently
reprove all parent residue and normalized-block certificates.

The complete new kernel bridge contains all 1,640 records on m0..409,
every supported index, all three single Bernstein coefficients and all
27 independent midpoint tensor coefficients in both modes. The primary
file records 14,766,150 strictly positive integer margins. Its independent
ordinary-x reconstruction agrees in every per-case digest and positive
minimum. Complete coverage is checked by `audit_completion_checks.py`;
that script imports no mathematical
implementation and also verifies exact scalar gates and bookkeeping.

The proxy generator certifies all 85,895 fixed minors and 820 central
interval arrays on m0..409. Its entire finite implementation and analytic
inference were inspected. `falsification_proxy_full_audit.py` separately
reconstructs every fixed minor and all 2,460 central Bernstein coefficients
in the ordinary-x basis; all author record fields match. Its packed
Laurent substitution is disclosed as shared with the independent kernel
auditor and independently checked against the defining binomial transform.
The paired-square array and all five small outer rows were separately
reconstructed in `falsification_proxy_audit_results.json`. The full proxy
audit's source script and primary result hashes are recorded there and
checked by `audit_completion_checks.py`. Exact algebra, template degree
bounds and finite continuum certificates are distinct from bounded
falsification scans.

No GitHub writes, public campaign-state changes, external theorem
promotion, or full-tree claim are part of this audit.

The final Japanese summary `RESULT_JA.md` was checked against the proof:
its path family, terminal index, certificate counts, inherited theorem
scope, and remaining `k>1` obligation agree. The internal status is not
described as external review or proof-assistant formalization.
