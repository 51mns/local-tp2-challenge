# Audit of the scaled relative-minor criterion

**Verdict: valid**, as a corollary of the previously proved all-minor
strength theorem. This lemma does not establish the required strength
of the proposed midpoint blocks.

Let `b` have a finite nonnegative half-row with `b_n<=b_0` for every
index. Let `h` have positive interval support and be `lambda`-strong,
where `lambda>0`. Suppose `h_n>=alpha*b_n` coefficientwise for some
`alpha>0`, and

`lambda*alpha>=8*b_0`.

Then every ordered two-by-two folded minor satisfies

`det K_h >= 4 det K_b`.

If the right-hand minor is nonpositive, folded TP2 of `h` is enough.
If it is positive, its two diagonal entries are positive. Linearity
and entrywise nonnegativity of the folded kernel give
`K_h(i,k)>=alpha*K_b(i,k)>0` and the same assertion for the other
diagonal. The positive-diagonal hypothesis of the all-minor strength
theorem is therefore satisfied. That theorem yields

`det K_h >=lambda*K_h(i,k)>=lambda*alpha*K_b(i,k)`

`>=8*b_0*K_b(i,k)>=4*K_b(i,k)*K_b(j,l)>=4 det K_b`,

because every entry of `K_b` is at most `2*b_0`. This also handles
band boundaries; no selected nonzero diagonal is lost. No kernel-index
cutoff or finite minor enumeration is needed.

## Application to the reversed midpoint

Put `tau0=H(tau)[0]`, `alpha=tau0-2`, and

`M=c*(tau-r)*(tau-s)+d*(tau-u)`, `r,s,u in [-2,2]`.

All shifted factors are Laurent-nonnegative, and `c,d` are
Laurent-nonnegative. Hence

`H(M)>=H(d*(tau-u))>=alpha*H(d)`.

The second inequality follows by separating the Laurent constant
term `tau0-u>=tau0-2` from the nonnegative nonconstant terms.
Multiplication by Laurent-nonnegative `y` preserves this particular
coefficientwise inequality:

`H(yM)>=alpha*H(yd)`.

This does **not** assert that multiplication by `y` preserves folded
TP2. To use the criterion for the smoothed midpoint, `yM` must itself
be independently proved strong. Likewise each reference row must be
bounded by its central entry; the inherited prefix strength theorems
supply this for `d=T_(m+2)` and `yd` for all `m>=0`.

At `m=0`, exact rows are

`H(tau)=(63,50,24,6)`, `H(d)=(20,14,4)`,
`H(yd)=(48,38,18,4)`.

Thus `alpha=61`, and the respective sufficient strength thresholds
are `160/61` and `384/61`. The boundary `c=1` does not invalidate
the relative-minor criterion: `c` is absent from its reference
hypotheses. It remains relevant for the separate diagonal-summand
strictness and zero-outer-index arguments.
