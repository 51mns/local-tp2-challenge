# Independent audit of the arbitrary-right-run seed bounds

**Verdict: PASS, within the explicitly cited prior one-turn foundations.**
This is an independent mathematical review and a separately implemented
exact recomputation in the same research session, not an external review.

The reviewed sources are `../arbk_seed/ALL_K_SEED_THEOREM.md` and
`../arbk_seed/OLD_SINGLE_NORMALIZED_BOUND.md`.

The canonical identifications, degrees, and inhomogeneous recurrence for
`a_j=Z_j-T_m` are correct. Both the `j=1` base and the recurrence imply
`a_j> a_(j-1)>0` and `a_j>=(t_0-1)a_(j-1)` coefficientwise. Iterating
twice gives the advertised new-seed comparison `A>=(t_0-1)^2B`.

For `m>=1`, the subtraction polarization retains half the old defect
once the old strength exceeds eight times the reference central
coefficient. The bound `p_0<=(7^(m+1)-1)/2` and all six stated corners
give precisely the advertised unbounded regions. Their consecutive
ratios in `m` and `j` preserve the inequality. The finite complement is
exactly 122 pairs after adding the `j=1,m<70` cases.

At `j=1`, the reference domination `P<=epsilon_m F` follows from the
central old-trace contribution. The all-m inherited normalized bound
for `Z_1,yZ_1` gives the half-defect inequality from `E_m>=8epsilon_m`.
The exact anchor at `m=70` and its increasing consecutive ratio are
correct. The related old-single positive-addition calculation uses
`D_m>12epsilon_m`; half of the dominant defect and the row growth
`1+epsilon_m<4/3` give the stated normalized bound with denominator
`16(m+3)`.

The special `m=0` subtraction correctly avoids treating `y` as a cone
polynomial. Its only negative defect is `-1` at index zero. With
`lambda=9^floor(j/2)>=9`, the remaining estimate
`(lambda/2-4)h_n-1>0` holds because every supported entry of a
lambda-strong cone row is at least lambda. This proves the entire
`m=0,j>=2` region. The residual `j=1` is an explicit finite certificate.

The independent program `audit_seed_bounds.py` imports no author code.
It constructs the inner Chebyshev polynomials in ordinary `x`, builds
the exact prefix representation, and converts to the Laurent half-row
by the binomial identity for `(q+q^-1)^d`. For normalized interval
certificates it obtains the middle Bernstein coefficient by endpoint
polarization, independently of the author's three-point interpolation.
It verifies:

* all 122 finite seed pairs and all 16,048 half-defect margins;
* every saved old-prefix row, new-seed row, and seed-row digest;
* all 38,745 old-trace/single/smoothed-single coefficient pairs for
  `m=0,...,69`, including their normalized bounds, minimizing indices,
  and ordered digests;
* all six infinite-region scalar corners and both exact `m=70` gates.

Every regenerated value agrees exactly. The machine-readable record is
`seed_bounds_independent_audit.json`. Reproduce with

```sh
python arbk_mixed/audit_seed_bounds.py
```

This audit verifies the auxiliary seed and old-normalization inputs. It
does not replace the separate proof of new mixed compatibility, endpoint
order, or correction domination for the full three-run Local TP2 claim.
