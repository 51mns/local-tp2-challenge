# Independent audit of the normalized midpoint tail

**Verdict: PASS**, with the small scalar-induction wording correction
described in Section 7. The argument proves its stated midpoint
conclusion for every integer `m>=391` and every independent
`r,s,c in [-2,2]`. It does not cover `1<=m<=390`, or prove Local TP2
on the full canonical tree by itself.

The audited manuscript and scalar verifier are
`fulltree_oneturn_normalized_tail.md` and `.py`. This review reconstructs
the mathematical inequalities independently. The eight-quadratic
certificate is an independently audited dependency, recorded in
`fulltree_normalized_block_independent_audit.md`; it is not inferred from
the status flag of the author's output file.

## 1. The normalized product constant is valid

Let `eta(h)=min_n delta_n(h)/h_n^2` over the positive support.
For an interior adjacent minor of `K_h`, put `a=|i-j|` and `b=i+j`.
Since `i,j>=1`, one has `b>=a+2`. Expanding the four entries gives

`det = Delta_a-Delta_(b+1)`
`    +h_a(h_b+h_(b+2))-(h_(a-1)+h_(a+1))h_(b+1)`.

The final cross term is nonnegative. Where its denominator is positive,
this follows from monotonicity of
`tau_j=(h_(j-1)+h_(j+1))/h_j`, because

`tau_(j+1)-tau_j=delta_j/(h_j h_(j+1))>=0`.

At or beyond the end of support the un-divided expression is
nonnegative directly. The first part is `sum_(l=a)^b delta_l`, so
retaining its two distinct endpoint terms proves

`det >= eta(h)(h_a^2+h_b^2) >= eta(h)(h_a+h_b)^2/2`.

At row zero the minor equals `delta_j`; at column zero it equals
`2delta_i`. At `(0,0)` it equals `delta_0`. Thus the uniform lower
bound `eta(h) K_h(i,j)^2/2` is valid on every boundary as well.

In Cauchy--Binet for `K_P K_Q`, rows `(0,1)` and columns `(n,n+1)`,
retain intermediate pairs `(k,k+1)`, `0<=k<=deg P`. Their first
minors are `delta_k(P)`. All other terms are nonnegative because both
kernels are TP2. Also

`sum_(k=0)^(deg P) H(P)[k] K_Q(k,n)=H(PQ)[n]`.

Cauchy--Schwarz with exactly `deg P+1` summands therefore gives

`eta(PQ)>=eta(P)eta(Q)/(2(deg P+1))`.

Interchanging the factors proves the claimed minimum-degree version.
There is no missing zero-index multiplicity and no sum-closure
assumption.

## 2. Prefix residues and their normalization

The established eight-case factorization writes a prefix as a residue
of degree at most six times scaled quartics. Reserving zero through
three additional quartics leaves a residue of degree `d<=18`; all
remaining factors can be grouped into degree-16 blocks. Consequently
`m=d+16k` exactly.

The previously audited sharp-strength certificates, followed by product
closure, give strength `2^(d-1)` for the scaled prefix residue and
`2^d` after multiplying it by `y^2`. Their masses are at most
`2^d(9/2)^d` and `9*2^d(9/2)^d`, respectively. Indeed every displayed
linear factor has shift at most `5/2`, while every quadratic in the
common box has value at two at most `67/4<(9/2)^2`; the narrower
exceptional factors satisfy the same bounds.

For a lambda-strong positive polynomial, `eta>=lambda/P(2)`.
This gives the two residue bounds in the manuscript. The scalars
`2^d` and `16` have been retained in the strength calculation;
normalized eta itself is unchanged by a positive scalar.

Each degree-16 block has eta greater than `1/128` by the independent
continuum certificate. Multiplying one such block costs at most
`2*(16+1)=34`. Thus each costs at most a factor `4352` in the
normalized estimate. Independent exact arithmetic verifies

`4352*(59/100)^16 = 0.938255400755965... < 1`,

`9*(1/400000000)*((9/2)*(59/100))^18`
`    = 0.966816326399549... < 1`.

Since `(9/2)*(59/100)>1` and `d<=18`, these inequalities give
`eta(T_m), eta(y^2T_m)>=c0*sigma^m`. The separately checked `m=1`
rows have eta `1/2` and `3/25`, so no residue exception is omitted.

## 3. Ordinary coefficient domination and shifted traces

Every monic factor used in the actual prefix factorization dominates
the same-degree power of `y=x+1` in ordinary coefficients: all retained
linear shifts are at least one, and every paired quadratic has
linear coefficient at least three and constant coefficient at least
`5/4`. The isolated narrower factors obey the same bounds. Hence

`T_m >= 2^m y^m`

in ordinary coefficients, and therefore also after the nonnegative
Laurent substitution.

The coefficients of `(q^-1+1+q)^m` are symmetric and unimodal, as
follows directly by induction under convolution with `(1,1,1)`.
Their central coefficient is consequently at least their average
`3^m/(2m+1)`. Retaining only the product of the `q^2` coefficient
of `y^2` and the central coefficient of `y^m` proves the manuscript's
lower bound on `h_2`. Applying the same average bound to `y^(m+2)`
proves the later lower bound on `t_0`.

I independently expanded the three changed defects for
`b=(3h_0+a,3h_1+2,3h_2,...)`. They are exactly

`delta_0(b)=9delta_0(h)+3a(2h_0+h_2)-24h_1+a^2-8`,

`delta_1(b)=9delta_1(h)+12h_1-3a h_2+6h_3+4`,

`delta_2(b)=9delta_2(h)-6h_3`.

All subsequent defects are multiplied by nine. For `a in [1,5]`,
`eta*h_2>=8`, and the decreasing row `h`, the manuscript's lower
bounds `23eta h_0^2/4`, `57eta h_1^2/8`, and `33eta h_2^2/4`
are valid. Dividing by the upper bounds on `b_n^2` gives the stated
fractions `92/169`, `114/169`, and `11/12`, each above one half.

Independent exact arithmetic gives `eta*h_2>=19.658...` already at
`m=21`, with a subsequent lower-bound ratio above one. Thus
`eta(t-r)>=c0*sigma^m/2` throughout the required range. Two applications
of Section 1 give exactly

`E_m=c0^3*sigma^(3m+1)/(16(m+2)(m+3))`

as a lower bound on `eta(F)`.

## 4. Coefficient domination of the entire correction

With `t=t_0+R`, the symmetric Laurent polynomial `R` has nonnegative
coefficients and zero central coefficient. For

`kappa=(t_0-2)^2/(t_0+2)`,

direct expansion gives

`(t-2)^2-kappa(t+2)=[2(t_0-2)-kappa]R+R^2`.

The omitted constant is exactly zero and the displayed scalar is
nonnegative. Since all shifted trace factors are nonnegative and
`A>=B` coefficientwise, this proves `F>=kappa G` on the whole
independent parameter cube. For `t_0>=6`, the inequality
`kappa>=t_0/3` is equivalent to `2(t_0-1)(t_0-6)>=0`.

Together with `t_0>=27*6^m/(2m+5)`, this yields the precise
coefficientwise estimate `0<=g_n<=epsilon_m f_n`, where
`epsilon_m=(2m+5)/(9*6^m)<1`.

## 5. Mixed-defect absorption includes every boundary

Expanding the defect of `f+g`, its negative mixed terms are

`-f_(n-1)g_(n+1)-g_(n-1)f_(n+1)-2f_(n+1)g_(n+1)`.

Their magnitude is at most
`2epsilon(f_(n-1)f_(n+1)+f_(n+1)^2)<=4epsilon f_n^2`.
The two negative terms in `delta(g)` cost at most another
`2epsilon^2 f_n^2`. These estimates use only symmetric log-concavity
and decrease of the folded-cone row `f`, together with coefficientwise
domination. They hold at `n=0` with `f_-1=f_1`, and at the terminal
indices with zero extension. In particular the previously identified
negative cross term just above the support of G is included.

No cone membership of G is required. Thus the perturbation inequality
used by the author is valid without an unproved compatibility premise.

## 6. Exact asymptotic threshold

An independent Fraction calculation, without importing the author's
verifier, gives

`E_391/(12epsilon_391)=1.038241466080245... > 1`.

The ratio at consecutive indices is exactly

`6sigma^3*(m+2)(2m+5)/((m+4)(2m+7))`.

Each of its two nonconstant fractions increases with m; the ratio is
already `1.222926818867016...` at 391. Hence the inequality holds for
all larger m by a valid infinite induction. Since epsilon is below
one, the perturbation costs at most `6epsilon f_n^2`, at most half
the lower bound `E_m f_n^2` on the original defect. Therefore

`delta_n(H)>=delta_n(F)/2>=lambda_F f_n/2>=lambda_F h_n/4`.

## 7. Conversion to the required strength and scope

The previously proved dominant-product strength is
`lambda_F=9*2^(3m-2)`. Also `b_0<=(7^m-1)/6`.
The needed scalar comparison `lambda_F>=32(7^m-1)/6` holds at
`m=7`; its ratio there is exactly `147456/137257>1`.

For its induction step use

`8(7^m-1)-(7^(m+1)-1)=7^m-7>=0`.

The manuscript originally summarized this as a ratio `8/7`; that is
not the exact ratio when the minus ones are retained. The displayed
induction proves the asserted bound and is the requested wording fix.
It causes no change to any threshold or conclusion.

Thus `delta_n(H)>=8b_0 H(H)[n]` at every supported index for all
`m>=391`. The trace factors and A have positive ordinary coefficients,
with `A>=B`, so `H>=F>=B` coefficientwise. The audited all-minor
strength theorem then gives `det K_H>=4 det K_B` for every ordered
row and column pair, including pairs outside finite support.

This establishes the large-m midpoint compatibility obligation on its
entire independent parameter cube. The finite continuum interval
`1<=m<=390` and the other obligations needed for the general one-turn
or arbitrary-tree theorem are separate; none is supplied by this audit.
