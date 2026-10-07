# Internal algebra audit of the quantitative lemmas

Scope: `quantitative_subtraction.md` and `quantitative_shifted_trace.md`.
Result: **PASS for their stated conditional universal lemmas.** This is an
internal cross-agent review, not external peer review or a claim that the
canonical all-tree hypotheses have been proved.

## Subtraction lemma

Writing `c=f-g`, direct expansion gives

`delta(c)=delta(f)+delta(g)-2f_n g_n`
` +f_(n-1)g_(n+1)+g_(n-1)f_(n+1)+2f_(n+1)g_(n+1)`
` -f_n g_(n+2)-g_n f_(n+2)`.

Substitution of the note's B and R gives exactly this expression minus
`lambda(f_n-g_n)`. Every R term is nonnegative under the stated
nonnegativity of f,g,c and `f_n>=f_(n+2)`. The latter follows from the
assumed nonincreasing half-row. At n=0 the same polynomial identity
applies after identifying `f_(-1)=f_1` and `g_(-1)=g_1`.

The support-boundary identity is correct: at n=d+1, only the term
`g_d f_(d+2)` survives from the correction. For n>=d+2 there is no
correction. These signs agree with the opposite-sign addition identity
in `bivariate_mixed_support.md`.

The displayed character coefficients of `t_X=3(x+1)X-x` are correct:
the coefficient at zero is `3alpha_1+1`, the coefficient at one is
`3(alpha_0+alpha_1+alpha_2)-1`, and subsequent coefficients are
`3(alpha_(j-1)+alpha_j+alpha_(j+1))`. Thus the note correctly validates
the nonnegative and nonincreasing rows needed for its canonical
application. It does not establish the sufficient margin B>=0.

## Shifted-trace lemma

Assume the stated positive interval support `0,...,d`, with d>=1,
`delta_n(v)>=lambda v_n`, and lambda>=4. The monotonicity used in the
proof follows from the hypotheses alone. Indeed, with
`Delta_n=v_n^2-v_(n-1)v_(n+1)`, telescoping gives

`Delta_n=sum_(j=n)^d delta_j>=0`.

At n=0, `Delta_0=v_0^2-v_1^2>=0` gives `v_0>=v_1`.
For n>=1, these inequalities give logconcavity and hence
nonincreasing positive ratios, so the entire half-row is nonincreasing.
At its terminal index, `delta_d=v_d^2>=lambda v_d` gives
`v_d>=lambda`; therefore every supported entry is at least lambda.

All four displayed perturbation formulas are exact. The independent
symbolic checker expands them from the defect definition and verifies
zero residual coefficients. The formulas apply unchanged at d=1:

`delta_0(b)=(3v_0-r)^2-2(3v_1-1)^2`,
`delta_1(b)=(3v_1-1)^2`,

and every later defect is zero. At d=2, the displayed index-two formula
reduces to the terminal square, since v_3=0.

For `mu=3lambda/2`, the zero-index margin's r derivative is bounded by

`-6v_0-3v_2+2r+mu <= -9lambda/2+4 <0`.

Its minimum is therefore at r=2. The note's resulting bound is valid;
its two leading coefficients are nonnegative because
`9lambda/2-12>=6` and `v_1>=v_2`.
The index-one margin is affine in r with coefficient `3v_2>=0`, so
r=-2 gives its minimum (with equality of all r values when d=1).
The last lower bound has coefficient `9lambda/2-15>=3`, and is
strictly positive. The remaining supported indices have margin at
least `9lambda v_n/2>0`.

Thus lambda>=4 suffices uniformly for every real r in [-2,2], and b is
strictly positive on exactly the original support. The proof does not
need integer entries. No claim that the threshold 4 is sharp is made.

The exclusion d=0 is essential: v=(4) is 4-strong, but the prescribed
perturbation creates `b_1=-1`. The statement correctly excludes this
case. When applying it to `H((x+1)P)`, that row must still satisfy all
the stated positivity, degree, and strength hypotheses.

## Exact checker and conclusion

`bivariate_audit_quantitative.py` uses its own elementary multivariate
polynomial operations; it does not import the implementation being
reviewed. It checks the universal subtraction identity, the folded
zero-index specialization, the three nontrivial shifted identities,
and exact degree-one/two/three boundary examples at rational shifts.
These algebra checks support the displayed proofs; finite examples
are not being used to infer an all-tree result.

Both manuscripts retain the necessary limitation: the required
canonical lower bounds or smoothed strengths remain open. This audit
does not turn their finite diagnostic checks into an all-depth proof.
