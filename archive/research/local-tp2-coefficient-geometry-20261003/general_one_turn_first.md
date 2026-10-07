# An unconditional uniform first comparison for one-turn rays

Put `y=x+1`, `P=x+2`, `z=2x+3`, and

`u_j=U_j(z/2)`, `p_j=y u_j`, `T_m=sum_(j=0)^m u_j`,

`g_m=1+yT_m=1+sum_(j=0)^m p_j`.

Here T_m denotes the prefix sum, not a first-kind Chebyshev polynomial.

## Theorem

For every integer `m>=0`,

`H(P g_m) <=_lr H(p_(m+1))=H(yu_(m+1))`.

In fact every adjacent minor is strictly positive for
`0<=n<=m+1`. Both polynomials have degree m+2, so the subsequent
adjacent minors are forced to vanish.

This is an unconditional infinite theorem. It uses the already proved
strict ordering of the p_j sequence for j>=1 in `continuation_ray.md`;
no global canonical-kernel closure assumption is needed.

## A positive mixture identity

For every `m>=1`,

`P g_m = (1/2)p_(m+1) + p_m
         + (3/2)sum_(j=1)^(m-1)p_j + z`.                 (1)

The sum is empty when m=1. To derive this, set p_-1=0 and use

`2P p_j=p_(j+1)+p_j+p_(j-1)` for j>=0,

which follows from `p_(j+1)=z p_j-p_(j-1)` and `2P=z+1`.
Sum over j=0,...,m and add 2P. The two boundary terms combine as

`P+p_0=(x+2)+(x+1)=z`,

giving (1). Grouping these boundary terms is essential: p_0 alone is
not below all later p_j in MLR.

An alternative unbounded verification is that the right side of (1)
at m=1 equals Pg_1, while its increment from m-1 to m is

`(p_(m+1)+p_m+p_(m-1))/2=Pp_m=Pg_m-Pg_(m-1)`.

## Every summand has the same upper row

The established ray theorem gives

`H(p_j)<=_lr H(p_(m+1))` for every `1<=j<=m`.

The remaining fixed polynomial is z, whose half-row is `(3,2)`.
Since `H(p_1)=(7,5,2)`, the two nonzero adjacent comparison minors are

`3*5-2*7=1`, `2*2=4`.

Thus `H(z)<=_lr H(p_1)<=_lr H(p_(m+1))`.

All coefficients in (1) are nonnegative, and every summand has the
same fixed upper row p_(m+1). Linearity of the minors in their lower
row therefore proves the claimed comparison. This is a legitimate
mixture-order argument, not an assumption that the folded cone is
closed under addition.

The coefficient of p_m in (1) is one. The already proved strict
comparison between p_m and p_(m+1) consequently supplies strictness at
every `0<=n<=m+1`, as well as the explicit lower bounds

`W_0(Pg_m,p_(m+1))>=24`,

`W_1(Pg_m,p_(m+1))>=2`,

`W_n(Pg_m,p_(m+1))>=2*4^(n-1)` for `2<=n<=m+1`.

## Initial case

For m=0, g_0=P. Directly,

`H(Pg_0)=H(P^2)=(6,4,1)`,

`H(p_1)=(7,5,2)`.

Their adjacent minors are `(2,3,0)`, proving the initial case and its
asserted strictness.

## Canonical meaning

For the one-turn family in which the fixed endpoint is g_m and the
initial endpoint gap is `E=y u_(m+1)`, this proves the required initial
first sandwich

`H((x+2)g_m)<=_lr H(E)`

uniformly for every m. Further evolution along that ray and the final
Local TP2 comparison require their own subsequent arguments.

The accompanying exact verifier `general_one_turn_first.py` checks the
generic symbolic increment identity, the m=1 identity, and all finite
initial rows used above. The proof itself is the unbounded recurrence
and mixture argument.
