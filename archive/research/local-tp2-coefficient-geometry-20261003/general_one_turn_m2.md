# Strict Local TP2 on every state L²R^k

This proves the original strict Local TP2 inequality at `L²R^k` for
every integer `k>=0`. It uses the relative-compatible-kernel theorem
in `general_one_turn_kernel_theorem.md` and the uniform preliminary
comparisons in `general_one_turn_reduction.md`. Arbitrary initial run
length `m` remains outside this theorem.

## Exact fixed-boundary recurrence and preliminary sandwiches

Put `y=x+1`, `P1=x+2`, and

`P=13+26x+18x²+4x³`,
`t=3yP-x=39+116x+132x²+66x³+12x⁴`,
`a=33+64x+40x²+8x³`, `b=4+2x`.

Thus `P=g_2`, and `a,b` are the inner prefix polynomials `T_3,T_1`
defined in the uniform reduction. Write `u_j=U_j(t/2)` and
`T_k=sum_{j=0}^k u_j`, with `u_-1=T_-1=0`. Define

`Z_k=aT_k+bT_(k-1)`, `q_k=y(a u_k+b u_(k-1))`.

The center at `L²R^k` is exactly `C_k=1+yZ_k`, with preceding seed
`C_-1=1`. The original mutations give

`C_(k+1)=t C_k-C_(k-1)-xP`,
`C_k-C_(k-1)=q_k`, `q_(k+1)=t q_k-q_(k-1)`.

For `k>=1`, the actual short gap and child difference are

`S_k=q_(k+1)`, `E_k=C_(k-1)-P`,
`M_k=3yC_k-x+1=2P1+3y²Z_k`, `D_k=E_k M_k`.             (1)

Here `deg C_k=4k+4`, `deg S_k=4k+8`; the other child has degree
`8k+5>4k+8`, confirming the ordering used in (1).

The relative-compatible-kernel theorem proves strict supported folded
defects for every `q_j` and every `Z_k`. Applying the uniform reduction
at `m=2` therefore gives, for every `k>=1`,

`P1 P<=lr E_k`,
`S_k<=lr AyZ_k`, where `A=t-2`.                         (2)

These deductions have no remaining conjectural hypothesis. Briefly,
the established all-left theorem supplies `q_0<=lr q_1` and the fixed
correction comparison `y(a+b)<=lr q_1`. Gap cone membership and the
recurrence then give all gap time orders. Finally the exact identity
`S_k=A(C_k-1)+q_k+y(a+b)` permits subtraction of the narrower row.
The first comparison in (2) follows from the uniform initial endpoint
comparison and the positive sum of subsequent gaps. Full derivations
and their initial rows appear in `general_one_turn_reduction.md`.

We use
`M_n(f,g)=H(f)_n H(g)_(n+1)-H(f)_(n+1)H(g)_n`.
All rows below have positive uninterrupted support, so adjacent minor
inequalities imply the full likelihood-ratio order needed for product
preservation.

## A uniform central-defect margin, with no small-k exceptions

The exact whole-interval certificates in
`general_one_turn_m2_margin.py` prove, for every `r in [-2,2]`,

`delta_0(t-r)>4(t-r)(2)`,
`delta_0(a(t-r)+b)>800[a(t-r)+b](2)`.                   (3)

With `r=2-4u`, their complete degree-two Bernstein coefficient lists
on `0<=u<=1` are respectively

`(3009,4853,6713)`,
`(9999933,14612425,19253733)`.

The power and Bernstein arrays are exported in
`general_one_turn_m2_margin_certificates.json`. These certificates
hold on the entire interval, not just at selected Chebyshev roots.

For every `k>=1`, the Jacobi resolvent and exact prefix factorizations
give

`Z_k=sum_{i in I} lambda_i Z_i`,
`Z_i=[a(t-r_i)+b] product_(l != i)(t-r_l)`,

where `r_l` are all `k` roots of the independent-variable prefix
polynomial `T_k`, `lambda_i>0`, `sum lambda_i=1`, and `|I|<=k`.
For `k=2h` the active denominator is `U_h`, after removing the common
factor `U_h+U_(h-1)`; for `k=2h+1` it is
`U_(h+1)+U_h`, after removing the common factor `U_h`.
Each active denominator has positive degree, including `k=1`.

The relative-compatible-kernel theorem proves nonnegative symmetrized
mixed minors between every pair of these summands. Hence

`delta_0(Z_k)>=sum_i lambda_i² delta_0(Z_i)`.            (4)

For cone products, Cauchy--Binet gives
`delta_0(FG)>=delta_0(F)delta_0(G)`. Every summand has one template
factor and exactly `k-1` propagator factors. Applying (3) gives

`delta_0(Z_i)>800*4^(k-1) Z_i(2)`.                    (5)

At `x=2`, `t=1519`, `a=385`, and `b=8`, so

`Z_i(2)/T_k(2)=385+8/(1519-r_i)`.

All these numbers lie strictly between 385 and 386. Thus every
`Z_i(2)>Z_k(2)/2`. The squared weights satisfy
`sum lambda_i²>=1/|I|>=1/k`. Combining (4)--(5) proves

`delta_0(Z_k)>[400*4^(k-1)/k] Z_k(2)>=400Z_k(2)`        (6)

for every `k>=1`. The final inequality follows from `4^(k-1)>=k`.
The proof explicitly accounts for squared residue weights and applies
already at `k=1`; no finite-depth extrapolation is involved.

## The exact multiplier is a cone polynomial

Set `Q=y²Z_k`, with half-row `h`. The cone factor `y²` has defects
`(4,0,1)`. Since `Z_k` has strict supported defects, Cauchy--Binet
proves strict supported defects for `Q`: retain `(0,1)` in
`K_(y²)K_(Z_k)` up to index `deg Z_k`, and `(2,3)` at the last two
indices. The corresponding supported adjacent kernel minors are
positive.

Using the commuting product in the opposite order, retaining `(0,1)`
gives

`delta_2(Q)>=delta_0(Z_k) delta_2(y²)=delta_0(Z_k)`.

Also `h_3<=Q(2)=9Z_k(2)`. Equation (6) therefore implies
`3delta_2(Q)>2h_3`. Direct expansion of `M_k=3Q+2P1` yields

`delta_0(M_k)=9delta_0(Q)+24(h_0-h_1)+12h_2+8`,
`delta_1(M_k)=9delta_1(Q)+12(h_1-h_2)+6h_3+4`,
`delta_2(M_k)=9delta_2(Q)-6h_3`,
`delta_n(M_k)=9delta_n(Q)` for `n>=3`.

Cone rows are nonincreasing, so all these expressions are positive.
Thus `M_k` is a cone multiplier for every `k>=1`. The first comparison
of (2) gives

`P1 P M_k<=lr D_k`.                                    (7)

## Strict comparison to the proxy

Put `B=3yPP1` and `K=2PP1²`. The proxy is exactly

`P1 P M_k=ByZ_k+K`.

The fixed half-rows are

`H(Ay)=(1001,867,560,258,78,12)`,
`H(By)=(3750,3306,2250,1155,426,102,12)`,
`H(K)=(1268,1076,650,268,68,8)`, `(Ay)(2)=4551`.

The six adjacent minors of `Ay,By` are

`m=(58056,99390,66300,19818,2844,144)`.

They are all positive. For `0<=n<=5`, Cauchy--Binet retaining
intermediate indices `(n,n+1)`, together with the adjacent-principal
folded-kernel bound, gives

`M_n(AyZ_k,ByZ_k)>=m_n delta_0(Z_k)>256m_n Z_k(2)`.

The final strict inequality uses (6). The exact residual margins are

`256m_n-4551H(K)_n`
`=(9091668,20546964,14014650,3853740,418596,456)>0`.

Since `M_n(AyZ_k,K)>=-4551H(K)_n Z_k(2)`, these six inequalities
remain strict after adding `K`. At `n>=6`, `K` contributes zero.
All remaining supported adjacent pair minors are strict: retain the
base index `i=min(n,5)` in Cauchy--Binet, and use the strict supported
adjacent kernel minor of `Z_k`, since `0<=n-i<=deg Z_k`.
Consequently

`AyZ_k <lr ByZ_k+K=P1 P M_k`                           (8)

at every adjacent index through `deg(AyZ_k)=deg S_k=4k+8`.

Combining (2), (8), and (7) gives

`S_k<=lr AyZ_k <lr P1 P M_k<=lr D_k`.

The positive supports of the intermediate rows cover that of `S_k`;
strictness therefore survives both weak comparisons, including the
terminal index. This is exactly the original Local TP2 inequality at
`L²R^k` for every `k>=1`. The remaining state `k=0`, namely `L²`,
is covered by the previously proved all-left theorem. The result holds
for every integer `k>=0`.
