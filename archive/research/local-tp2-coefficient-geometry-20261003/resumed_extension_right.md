# Strict Local TP2 on the entire all-right ray

Using the established folded-kernel theorem and the separately proved
right-multiplier lemma in `resumed_extension_right_multiplier.md`, this
proves the original inequality at every state `R^k`.
It does not assert the theorem for mixed paths.

Write `y=x+1`, `P=x+2`, `t=3x²+8x+6`, `e=yP`, and
`u_j=U_j(t/2)`, with `u_-1=0`, `u_0=1`, `u_1=t`.
Put `T_j=sum_{i=0}^j u_i`. For symmetric Laurent coefficient rows use

`M_n(f,g)=H(f)_n H(g)_(n+1)-H(f)_(n+1) H(g)_n`.

Thus `f <=lr g` means that every supported ordered 2-by-2 minor is
nonnegative. Adjacent minors suffice for the positive, uninterrupted
supports appearing below. All cone assertions mean that the folded
multiplication kernel is TP2; strictness refers to its supported defects.

## Exact ray identities

Let `C_k` be the center at `R^k`. The fixed boundary is `P`, and

`C_-1=1`, `C_0=1+2e`,
`C_(k+1)=t C_k-C_(k-1)-xP`.

Subtracting consecutive recurrences, and checking the first two gaps,
gives

`C_k=1+2e T_k`, `C_(k+1)-C_k=2e u_(k+1)`.

For `k>=1` the lower-degree endpoint is `P`, the other endpoint is
`C_(k-1)`, and the lower-degree child is `C_(k+1)`. Their degrees are
`2k+4` and `4k+3`, respectively. Consequently the actual short gap and
child difference are

`S_k=2e u_(k+1)`,
`E_k=C_(k-1)-P=y(2P T_(k-1)-1)`,
`M_k=3y C_k-x+1=2P(1+3y²T_k)`,
`D_k=E_k M_k`.

The root `k=0` has the opposite endpoint ordering and is handled directly
at the end.

## Cone factors and the first sandwich

Every factor `t-a`, `-2<=a<=2`, is a strict cone factor. Indeed, writing
`c=6-a` in `[4,8]`, its half-row is `(c+6,8,3)`, and its three defect
differences are

`c²+15c-74`, `37-3c`, `9`,

all positive. Also `e` has half-row `(4,3,1)` and defects `(2,4,1)`.
All roots in the variable `t` of `u_j`, `u_j+u_(j-1)`,
`u_j-u_(j-1)`, and twice the first-kind Chebyshev polynomial lie in
`[-2,2]`. Thus all these polynomials, and their products with `e`, are
cone multipliers. The factorizations

`T_(2h)=u_h(u_h+u_(h-1))`,
`T_(2h+1)=u_h(u_(h+1)+u_h)`

also show that every `T_j` is a cone multiplier.

Put `p_j=e u_j`. The recurrence and cone broadening give

`M_n(p_j,p_(j+1))=M_n(p_j,t p_j)+M_n(p_(j-1),p_j)>=0`.

The base `p_0<=lr p_1` follows directly by broadening the cone polynomial
`e` with the nonnegative symmetric multiplier `t`. Hence the `p_j`
increase in likelihood-ratio order. Now

`E_k=E_1+2 sum_{j=1}^{k-1}p_j`,
`H(P²)=(6,4,1)`, `H(E_1)=(7,5,2)`,
`H(p_0)=H(e)=(4,3,1)`.

The adjacent minors comparing `P²` to `E_1` are `(2,3,0)`; those
comparing `P²` to `p_0` are `(2,1,0)`. Transitivity and linearity
of each pair minor therefore prove

`P² <=lr E_k` for every `k>=1`.

By the right-multiplier lemma, `M_k` is a strict cone multiplier. Thus,
with the proxy `Z_k=P² M_k`,

`Z_k <=lr D_k`.                                            (1)

## A Chebyshev sandwich valid for both parities

Put `A=t-2`, and abbreviate `V_r=u_r+u_(r-1)` and
`W_r=u_r-u_(r-1)`. All `W_r` are cone polynomials here, including
`W_0=1` and `W_1=t-1`. The base `W_0<=lr W_1` is immediate from their positive coefficients.
The same recurrence argument just used then shows
`W_(r-1)<=lr W_r`. Since

`W_r-W_(r-1)=(t-2)u_(r-1)`,

subtracting the narrower polynomial gives
`W_r<=lr A u_(r-1)`. Multiplication by the cone polynomial `e V_r`
and the identities `u_(2r)=V_r W_r`, `T_(2r-1)=u_(r-1)V_r` yield

`e u_(2r) <=lr A e T_(2r-1)` for `r>=1`.

For odd indices let `c_r=2 T_r^(first)(t/2)`, so `c_0=2`, `c_1=t`.
Every `c_r` is a cone polynomial; the base `c_0<=lr c_1` is immediate,
and the recurrence again gives `c_r<=lr c_(r+1)`. The identities

`c_(r+1)-c_r=(t-2)V_r`,
`u_(2r+1)=u_r c_(r+1)`, `T_(2r)=u_r V_r`

give the odd-index comparison after multiplication by `e u_r`.
Taking the index to be `k+1` proves, for all `k>=1`,

`S_k=2e u_(k+1) <=lr 2 A e T_k`.                         (2)

## Root blocks for the quantitative comparison

Every `T_k`, `k>=1`, is a product of blocks

`Q=t²+s t-c`, `0<=s<=2`, `0<=c<=4`,

and at most one block `G=t+b`, `0<=b<=1`.
To see this, use the displayed `u,V` factorization of `T_k`. Pair the
opposite roots of each `u` factor, leaving `t` when its degree is odd.
For `V_r`, its roots are `2cos(2j*pi/(2r+1))`, `1<=j<=r`.
Pair the outer positive root `a` with the opposite negative root `-b`.
Their magnitudes satisfy `0<=a<=b<=2`, giving
`(t-a)(t+b)=t²+(b-a)t-ab`. If `r` is odd, the middle root is
`-2sin(pi/(4r+2))`, whose magnitude is at most one, leaving `G`.
If both the `u` and `V` factors leave a linear block, combine `t(t+b)`
into a block `Q`. Each actual `Q` remains a product of two strict cone
factors `t-a`; a rectangle parameter certificate need not assert this
factor property at unattained parameter values.

For every such `Q`, the exact Bernstein certificate in
`resumed_extension_right.py` proves

`delta_0(Q)-4 Q(2)>=884>0`.                              (3)

Here `delta` denotes the folded defect difference. The substitution is
`s=2u,c=4v` with `u,v` in `[0,1]`.

Put `B=3yP²` and `K=P³`. Their relevant values are

`H(Ae)=(94,79,46,17,3)`,
`H(Be)=(396,339,210,90,24,3)`,
`H(K)=(20,15,6,1)`, `(Ae)(2)=384`.

The adjacent pair minors of `Ae,Be` are
`(582,996,570,138,9)`, all strictly positive. For each of the two
possible initial blocks `R=Q` or `R=G`, the same exact certificate
proves, for `0<=n<=3`,

`M_n(AeR,BeR)>384 H(K)_n R(2)`.                         (4)

The Bernstein lower bounds for (4), in order `n=0,1,2,3`, are

| Initial block | Exact strict lower bounds |
| --- | --- |
| `Q` | `151266414, 338478852, 290971872, 145555380` |
| `G` | `17268, 358599, 322626, 138210` |

These are certificates on entire parameter boxes, not samples of roots
or ray depths. The script exports every rational power and Bernstein
coefficient for independent reconstruction.

Choose the initial block `G` if present, and otherwise choose one `Q`.
All remaining blocks are `Q`. Under multiplication by such a block,
Cauchy--Binet, retaining the intermediate adjacent columns `(n,n+1)`,
gives

`M_n(fQ,gQ)>=M_n(f,g) det K_Q[{n,n+1},{n,n+1}]`.

All discarded terms are nonnegative. The principal kernel minor is
at least `delta_0(Q)` (equality for `n=0`); this is the established
principal-minor bound for folded TP2 kernels. By (3) the pair minor
grows by more than `4Q(2)`, whereas the mass on the right of (4)
grows only by `Q(2)`. Therefore (4) holds with `R=T_k` for every
`k>=1`.

All pair minors `M_n(AeT_k,BeT_k)` are strictly positive throughout
the lower support. For completeness, start from the five strict
minors of `Ae,Be`. For output `n`, retain input adjacent index
`i=min(n,4)` in Cauchy--Binet for multiplication by `T_k`.
The corresponding adjacent kernel minor is positive because
`0<=n-i<=deg(T_k)` and `T_k` has strictly positive supported defects.

The remainder `K` can now be included. For `0<=n<=3`, nonnegative
coefficients and evaluation at `q=1` imply

`M_n(AeT_k,K)>=-H(K)_n H(AeT_k)_(n+1)`
`                  >=-384 H(K)_n T_k(2)`.

This is strictly smaller in magnitude than (4). For `n>=4`, the
remainder contributes zero. Consequently

`AeT_k <lr BeT_k+K`                                    (5)

strictly at every adjacent minor up to `deg(AeT_k)=2k+4`.

## Original strict inequality

The proxy is exactly `Z_k=2(BeT_k+K)`. Combining (2), (5), and (1)
gives

`S_k <=lr 2AeT_k <lr Z_k <=lr D_k`.

All rows have positive uninterrupted supports, and the intermediate
rows cover the support of `S_k`. Thus every required adjacent minor
is strict, including the terminal index `deg S_k=2k+4`.

At `k=0`, direct evaluation of the original two-child recurrence gives
the four minors `(272,352,160,24)`, also positive. Therefore the
original Local TP2 statement holds at every all-right state `R^k`,
for every integer `k>=0`.
