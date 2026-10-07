# Exact reduction for an arbitrary initial left run

This note proves the identities and initial likelihood-ratio comparisons
needed for the one-turn family `L^m R^k`, uniformly in `m>=0`. The final
propagation is conditional on folded-cone membership of its mixed gaps;
it does not assume that nested Chebyshev sums are automatically cone
polynomials.

Set `y=x+1`, `P1=x+2`, `z=2x+3`. In the inner variable write

`u_j=U_j(z/2)`, `T_j=sum_{i=0}^j u_i`, `p_j=y u_j`,
`T_-1=u_-1=0`, `g_j=1+yT_j`.

Thus `g_-1=1`, `g_0=P1`, and the center at `L^m` is `g_(m+1)`,
with endpoints `1,g_m`. Let

`P=g_m`, `t=3yP-x`, `a=T_(m+1)`, `b=T_(m-1)`.

In the outer variable write

`v_j=U_j(t/2)`, `R_j=sum_{i=0}^j v_i`, `v_-1=R_-1=0`.

The center after `L^m R^k` and its consecutive gap are exactly

`C_k=1+y[aR_k+bR_(k-1)]`,
`q_k=C_k-C_(k-1)=y[a v_k+b v_(k-1)]`, `C_-1=1`.        (1)

Indeed the fixed-endpoint recurrence is
`C_(k+1)=t C_k-C_(k-1)-xP`. Its gaps satisfy the homogeneous
Chebyshev recurrence, `q_0=ya`, and `q_1-tq_0=yb`. The last identity
follows from `g_(m+1)=z g_m-g_(m-1)-x`, including `m=0` with
`g_-1=1`. This proves (1) for every outer index.

For `k>=1` the lower-degree endpoint is `P`, and hence the actual
short-child gap and child difference are

`S_k=q_(k+1)`, `E_k=C_(k-1)-P`,
`M_k=3yC_k-x+1=2P1+3y²Z_k`, `D_k=E_k M_k`,
where `Z_k=aR_k+bR_(k-1)`.

For `m>=1`, `deg C_k=(k+1)(m+2)`. The fixed endpoint has degree
`m+1`, while `C_(k-1)` has degree `k(m+2)>m+1` for `k>=1`.
The lower child has degree `(k+2)(m+2)`; the other has degree
`(2k+1)(m+2)+1`, so the ordering is strict. The already treated
case `m=0` is the all-right ray.

## Uniform comparisons at the initial state

The established all-left theorem gives strict time order
`p_j<=lr p_(j+1)` for all `j>=1`. It also proves strict Local TP2 at
`L^m`. At that state let `s=p_(m+2)` be the short left gap and `d`
the long-minus-short difference. The first right gap is

`q_1=s+d`, and `s<=lr d`.

Consequently `s<=lr q_1`.

We claim that both `q_0` and the fixed correction

`b0=y(a+b)=y[T_(m+1)+T_(m-1)]`

lie below `s` in likelihood-ratio order. The two finite initial
comparisons needed are

`p_0+p_1<=lr p_2`, with minors `(16,32,8)`,
`2p_0+p_1<=lr p_2`, with minors `(8,48,8)`.

Here the respective lower half-rows are `(8,6,2)` and `(9,7,2)`,
and `H(p_2)=(40,32,16,4)`.

Since `q_0=sum_{j=0}^{m+1}p_j`, group `p_0+p_1`; it and every
remaining term are below the single upper row `p_(m+2)`. For `b0`,
use the same group when `m=0`; when `m=1`, group `2p_0+p_1` and
leave `p_2`; when `m>=2`, group `2(p_0+p_1)` and leave the terms
with indices at least two. Each group is below `p_(m+2)`. Summing
these comparisons is legitimate because the upper row is fixed.
Thus

`q_0<=lr s<=lr q_1`, `b0<=lr s<=lr q_1`                (2)

for every `m>=0`.

The separate elementary identity proved in
`general_one_turn_first.md` gives the other initial comparison

`P1 P<=lr E_1=p_(m+1)`.                               (3)

For reference, when `m>=1` this identity is

`2P1P=p_(m+1)+2z+2p_m+3 sum_{j=1}^{m-1}p_j`.

The row of `z` is `(3,2)`, below that of `p_1=(7,5,2)` with
minors `(1,4)`. Every additional term in this identity lies below
`p_(m+1)` by the known time order, proving (3). The case `m=0`
is the direct comparison `(6,4,1)<=lr(7,5,2)`.

## What mixed-gap cone membership would imply

Suppose now that all `q_j` on the chosen fixed-`m` ray have folded
TP2 multiplication kernels. The exact gap recurrence gives

`M_n(q_j,q_(j+1))=M_n(q_j,t q_j)+M_n(q_(j-1),q_j)`.

Cone broadening makes the first term nonnegative. Starting from (2),
induction proves `q_j<=lr q_(j+1)` for every `j>=0`. It follows that

`E_k=E_1+sum_{j=1}^{k-1}q_j >=lr P1P`                  (4)

because all `q_j`, `j>=1`, lie above `q_1`, hence above
`p_(m+2)>=lr p_(m+1)>=lr P1P`.

Put `A=t-2`. The exact center recurrence also gives

`S_k=A(C_k-1)+q_k+b0`.

Equation (2) and time order show `q_k+b0<=lr S_k=q_(k+1)`;
subtracting that narrower polynomial gives

`S_k<=lr A(C_k-1)=AyZ_k`.                              (5)

If `M_k` is a cone multiplier, (4) gives
`P1P M_k<=lr D_k`. To finish original strict Local TP2 it remains
to prove the strict proxy comparison

`AyZ_k <lr P1P M_k=3y²PP1 Z_k+2PP1²`.

These deductions use only fixed-row summation, cone broadening, and
the exact recurrence. They require an actual cone theorem for the
nested mixed gaps; the statement for all `m` remains conditional
until that hypothesis and the multiplier/proxy bounds are established.

## Nested positive resolvents

There is a useful exact inner structure. With
`V_j=u_j+u_(j-1)`, write

`a=u_n V_l`, `b=u_(n-1)V_(l-1)`,

where `(n,l)=(h,h+1)` for `m=2h`, and `(h+1,h+1)` for `m=2h+1`.
For `m>=1`, both quotients in

`b/a=(u_(n-1)/u_n)(V_(l-1)/V_l)`

have positive Jacobi-resolvent representations. Hence

`b/a=sum_{i,j} lambda_i mu_j /[(z-alpha_i)(z-beta_j)]`,

with positive weights of total one. This reduces the coefficient pair
`(a,b)` to degree-two inner templates after factoring the other roots.
However individual inner factors `z-alpha` need not be cone factors;
broken root groups and compatibility between the inner summands must
be controlled. This identity alone does not prove the required cone
closure for arbitrary `m`.
