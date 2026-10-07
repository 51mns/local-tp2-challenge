# Strict Local TP2 on two genuinely mixed infinite rays

Using the compatible-kernel theorem in `mixed_ray_kernel_theorem.md`,
this proves the original Local TP2 inequality at every state `LR^k`
and `RL^k`, for every integer `k>=0`. It makes no assertion about
arbitrary mixed words or the full canonical tree.

## Notation and exact canonical identities

Write

`y=x+1`, `P1=x+2`, `P=2x²+6x+5`,
`t=3yP-x=6x³+24x²+32x+15`, `w=2P1(2x+3)`.

Set `u_j=U_j(t/2)`, `v_j=u_j+u_(j-1)`, and
`T_j=sum_{i=0}^j u_i`, with `u_-1=T_-1=0`.
For the two rays define

`Z_k^L=wT_k+T_(k-1)`, `q_k^L=y(wu_k+u_(k-1))`,
`Z_k^R=T_(k+1)+wT_k`, `q_k^R=y(u_(k+1)+wu_k)`.

In the first family the canonical center after `LR^k` is
`C_k=1+yZ_k^L`, with preceding seed `C_-1=1`; in the second it is
`C_k=1+yZ_k^R`, with preceding seed `C_-1=P1`. Direct substitution
of the two seeds into the original mutation gives, in either case,

`C_(k+1)=t C_k-C_(k-1)-xP`, `C_k-C_(k-1)=q_k`.

Equivalently, the gaps have exactly the mixed initial conditions shown
above and obey `q_(k+1)=t q_k-q_(k-1)`. These are exact recurrence
solutions; a pure single Chebyshev gap is not assumed.

For `k>=1` the lower-degree endpoint is the fixed endpoint `P`.
Therefore the actual short-child gap and long-minus-short difference
are

`S_k=q_(k+1)`, `E_k=C_(k-1)-P`,
`M_k=3yC_k-x+1=2P1+3y²Z_k`, `D_k=E_k M_k`.             (1)

The center degrees are `3k+3` and `3k+4`. The child degrees are
`deg C_k+3` and `2 deg C_k-2`, so this ordering is valid for `k>=1`.

As before, write

`M_n(f,g)=H(f)_n H(g)_(n+1)-H(f)_(n+1)H(g)_n`.

Likelihood-ratio order refers to all ordered minors; adjacent minors
suffice here because every relevant row has positive, uninterrupted
support. Folded-cone membership means TP2 of the folded multiplication
kernel. All strict cone assertions below concern supported defects,
not every minor of an infinite banded matrix.

## Mixed-gap time order and the two preliminary comparisons

The compatible-kernel theorem proves that every `q_j` and every `Z_k`
is a cone polynomial with strictly positive supported defects. In
particular the recurrence and cone broadening imply

`M_n(q_j,q_(j+1))=M_n(q_j,t q_j)+M_n(q_(j-1),q_j)>=0`

whenever the preceding comparison is known. The two initial comparisons
`q_0<=lr q_1` have the exact minor lists

- `LR^k`: `(32922,52734,23880,3440)`;
- `RL^k`: `(492854,857178,477196,109472,10224)`.

Thus `q_j<=lr q_(j+1)` for every `j>=0` on both rays.

Let `B0=P1 P`, whose half-row is `(30,23,10,2)`. Direct base
comparisons give

| Family | Minors of `B0,q_0` | Minors of `B0,E_1` |
| --- | --- | --- |
| `LR^k` | `(36,34,4,0)` | `(40,48,8,0)` |
| `RL^k` | `(397,504,144,12)` | `(408,508,148,12)` |

Since `E_k=E_1+sum_{j=1}^{k-1}q_j`, time order and linearity in the
upper row show

`B0<=lr E_k` for every `k>=1`.                          (2)

This summation uses the same fixed lower polynomial `B0` for every
summand.

For the short gap, put `A=t-2` and `b=y(w+1)`. The exact center
recurrence implies

`S_k=A(C_k-1)+q_k+b`.                                   (3)

The half-row of `b` is `(49,39,18,4)`. Its comparison to `q_1` on
the first ray has minors `(31996,57348,23880,3440)`; its comparison
to `q_0` on the second has minors `(346,672,220,24)`.
Together with gap time order, these give
`q_k+b<=lr q_(k+1)=S_k`. Subtracting this narrower row in (3)
therefore yields the valid short-gap sandwich

`S_k<=lr A y Z_k`.                                     (4)

No summation of comparisons with different lower rows is used.

## A quantitative central-defect bound for both mixed prefixes

We next prove, for either prefix family and every `k>=4`,

`delta_0(Z_k)>75 Z_k(2)`.                              (5)

The four exact continuum certificates in `mixed_ray_margin.py`, with
all power and Bernstein coefficients exported in
`mixed_ray_margin_certificates.json`, are as follows:

| Block | Parameter range | Certified bound | Bernstein lower bound for the difference |
| --- | --- | --- | --- |
| `f=t-a` | `-2<=a<=2` | `delta_0(f)>(4/5)f(2)` | `41/5` |
| `Q=t²+s t-c` | `0<=s<=2`, `0<=c<=4` | `delta_0(Q)>90Q(2)` | `169619` |
| `L_a=w(t-a)+1` | `-2<=a<=2` | `delta_0(L_a)>40L_a(2)` | `5101` |
| `R_a=(t+w)(t-a)-1` | `-2<=a<=2` | `delta_0(R_a)>100R_a(2)` | `1873428` |

All actual factors in this argument are cone factors, by the separate
kernel theorem. A certificate on the larger rectangular parameter box
does not require that every point of that box arise from actual roots.

The roots of `T_k` in the independent variable `t` can be paired into
blocks `Q` of the displayed kind, leaving at most one factor `t+b`,
`0<=b<=1`. Indeed, use

`T_(2h)=u_h v_h`, `T_(2h+1)=u_h v_(h+1)`.

Opposite `u` roots give `(t-a)(t+a)`. The opposite `v` roots give
`(t-a)(t+b)` with `0<=a<=b<=2`; its middle unpaired root, when
present, has magnitude at most one and is nonpositive. Two leftover
linear factors can be combined as `t(t+b)`. Removing any one root
factor from `T_k` consequently leaves at least
`J=floor((k-2)/2)` balanced blocks and at most two unpaired factors.

The positive-residue Jacobi resolvent used in the kernel theorem also
provides an exact representation

`Z_k=sum_{i in I} lambda_i Z_i`,
`lambda_i>0`, `sum_i lambda_i=1`, `|I|<=k`,

where each `Z_i` is `L_(a_i)` or `R_(a_i)` times every root factor
of `T_k` except `t-a_i`. Here is the precise parity identification:

- For `Z^L`, the active denominator is `u_h` when `k=2h`, and
  `v_(h+1)` when `k=2h+1`; the numerator is the preceding member.
- For `Z^R`, it is `v_h` when `k=2h`, and `u_h` when `k=2h+1`.
  The factorization is respectively
  `u_h[(t+w)v_h-v_(h-1)]` or
  `v_(h+1)[(t+w)u_h-u_(h-1)]`.

All these active denominators have positive degree when `k>=4`.
The compatible-kernel theorem gives **nonnegative symmetrized mixed
minors between every pair `Z_i,Z_j`**, not merely separate cone
membership. Thus the quadratic expansion gives

`delta_0(Z_k)>=sum_i lambda_i² delta_0(Z_i)`.            (6)

For cone products, Cauchy--Binet gives
`delta_0(FG)>=delta_0(F)delta_0(G)` by retaining intermediate indices
`(0,1)`. The four certified bounds and the root count therefore imply

`delta_0(Z_i)>40(4/5)² 90^J Z_i(2)` on the first ray,
`delta_0(Z_i)>100(4/5)² 90^J Z_i(2)` on the second.       (7)

The evaluation masses of the summands are uniformly comparable. At
`x=2`, `t=223` and `w=56`, and

`Z_i(2)/T_k(2)=56+1/(223-a_i)` on the first ray,
`Z_i(2)/T_k(2)=279-1/(223-a_i)` on the second.

The first values all lie between 56 and 57, and the second between 278
and 279. In particular each `Z_i(2)>Z_k(2)/2`. Finally
`sum_i lambda_i²>=1/|I|>=1/k`. Equations (6)--(7) prove

`delta_0(Z_k)/Z_k(2) > [64/(5k)] 90^floor((k-2)/2)`

on the first ray, and the stronger bound
`[32/k] 90^floor((k-2)/2)` on the second. The first bound is already
greater than 75 at `k=4,5`, and increases along each parity class.
This proves (5) for every `k>=4`, with the squared residue weights
fully accounted for.

## The multiplier is a cone polynomial

Put `Q=y²Z_k`, with half-row `h`. The known cone factor `y²` has
defects `(4,0,1)`. Since `Z_k` has strictly positive supported defects,
Cauchy--Binet proves the same strict supported property for `Q`.
For indices up to `deg Z_k`, retain `(0,1)` in `K_(y²)K_(Z_k)`;
at the last two indices retain `(2,3)`. The relevant kernel minors
are strictly positive in their supports.

For the one defect requiring a quantitative perturbation bound, use
the opposite order of the commuting product and retain `(0,1)`:

`delta_2(Q)>=delta_0(Z_k) delta_2(y²)=delta_0(Z_k)`.

Also `h_3<=Q(2)=9Z_k(2)`. By (5),
`3delta_2(Q)>225Z_k(2)>2h_3`.

Direct expansion of `M_k=3Q+2P1` gives

`delta_0(M_k)=9delta_0(Q)+24(h_0-h_1)+12h_2+8`,
`delta_1(M_k)=9delta_1(Q)+12(h_1-h_2)+6h_3+4`,
`delta_2(M_k)=9delta_2(Q)-6h_3`,
`delta_n(M_k)=9delta_n(Q)` for `n>=3`.

Cone rows are nonincreasing, so every displayed expression is strictly
positive. Hence `M_k` is a cone multiplier for all `k>=4`. Applying
it to (2) proves

`P1 P M_k<=lr D_k`.                                    (8)

## Strict comparison with the proxy

Define `B=3yPP1`, `K=2PP1²`. The proxy has the exact form

`P1 P M_k=B y Z_k+K`.

The fixed rows are

`H(Ay)=(161,135,80,30,6)`,
`H(By)=(606,522,330,147,42,6)`,
`H(K)=(212,172,90,28,4)`, `(Ay)(2)=663`.

The five adjacent minors comparing `Ay` to `By` are

`m=(2232,2790,1860,378,36)`,

all positive. Cauchy--Binet, retaining input indices `(n,n+1)`, and
the folded-kernel adjacent-principal-minor bound give

`M_n(AyZ_k,ByZ_k)>=m_n delta_0(Z_k)>75m_n Z_k(2)`

for `0<=n<=4`. The exact residual margins are

`75m_n-663H(K)_n=(26844,95214,79830,9786,48)>0`.

Since
`M_n(AyZ_k,K)>=-663H(K)_n Z_k(2)`, all five low-index minors remain
strict after adding `K`. For `n>=5`, the remainder contributes zero.
Every supported adjacent pair minor of `AyZ_k,ByZ_k` is strict: retain the
base index `i=min(n,4)` in Cauchy--Binet and use the strictly positive
supported adjacent kernel minor of `Z_k`, since
`0<=n-i<=deg Z_k`. Therefore

`AyZ_k <lr ByZ_k+K=P1 P M_k`                            (9)

strictly at every adjacent index through `deg(AyZ_k)=deg S_k`.

Combining (4), (9), and (8) proves the original strict Local TP2
inequality for both rays at every `k>=4`. All intermediate rows have
positive uninterrupted support covering `S_k`; the strictness therefore
survives both weak comparisons, including the terminal index.

## Remaining initial states

The cases `k=0` belong to the already proved single-letter rays.
For `k=1,2,3`, `mixed_ray_bases.py` evaluates the original mutations
in two independent ways: ordinary `x`-polynomial arithmetic and direct
symmetric Laurent arithmetic. It checks the complete `S,D,H(S),H(D)`
rows and all required minors, with exact integers. The six states have
short-gap degrees `9,12,15` and `10,13,16`; all 81 required minors
are strictly positive. Full arrays are in `mixed_ray_bases.json`.

These six exact initial checks complete the two infinite theorems;
the unbounded tail follows from the proved parameter and residue
bounds above, not from numerical extrapolation.
