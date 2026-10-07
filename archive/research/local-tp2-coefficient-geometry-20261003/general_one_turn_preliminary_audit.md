# Independent audit of uniform one-turn preliminary comparisons

**Verdict: PASS.** The initial endpoint comparison, initial gap time
order, and initial correction comparison below hold for every integer
m>=0. They are unconditional consequences of the proved all-left
theorem and the smoothed Chebyshev time order. The remaining nested
kernel assertions are not silently assumed.

Set `y=x+1`, `P1=x+2`, `z=2x+3`, and write

`u_j=U_j(z/2)`, `p_j=y u_j`, `T_j=sum_(i=0)^j u_i`,

`g_j=1+yT_j`, `g_-1=1`, `T_-1=0`.

The canonical state L^m has endpoints 1,g_m and center g_(m+1).
Its short left-child gap is `s=p_(m+2)`. Let D be its original
long-minus-short child difference. The already proved all-left theorem
gives `s<lr D` at every required adjacent index.

## 1. Initial endpoint comparison

The identity in `general_one_turn_first.md` is exact for m>=1:

`P1 g_m=(1/2)p_(m+1)+p_m+(3/2)sum_(j=1)^(m-1)p_j+z`.

It follows by summing `2P1 p_j=p_(j+1)+p_j+p_(j-1)` and grouping
the boundary terms as `P1+p_0=z`. In particular, the inadmissible
standalone comparison from p_0 to later p_j is not used.

The fixed row H(z)=(3,2) is below H(p_1)=(7,5,2), with adjacent
minors (1,4). All the other summands are below the same upper row
p_(m+1) by the proved p_j time order for j>=1. Linearity in the
lower row therefore proves

`P1 g_m<=lr p_(m+1)`.

The coefficient-one p_m term supplies strictness through index m+1.
At m=0, the rows are H(P1^2)=(6,4,1) and H(p_1)=(7,5,2), with
minors (2,3,0). The first-comparison manuscript and its stated strict
range are correct.

## 2. Exact initial gaps and correction

For the tail L^mR^k, fix P=g_m and put `t=3yP-x`. Take
`C_-1=1`, `C_0=g_(m+1)`, and define q_k=C_k-C_(k-1).
Then

`q_0=yT_(m+1)`,

`q_1=s+D`,

because the first right child is the long child at L^m. The correction
in the recentered recurrence is

`b=(t-2)-xP=z g_m-P1=y(T_(m+1)+T_(m-1))`.

These identities are valid at m=0 with T_-1=0. They distinguish the
initial center-minus-one gap q_0 from the endpoint gap
`E_1=g_(m+1)-g_m=p_(m+1)`.

## 3. Both q_0 and b lie below s

The fixed comparison rows are

`H(p_0+p_1)=(8,6,2)`,

`H(2p_0+p_1)=(9,7,2)`,

`H(p_2)=(40,32,16,4)`.

The first two rows compared to the third have adjacent minors
(16,32,8) and (8,48,8), respectively. Thus both are below p_2.

For q_0, group its first two terms:

`q_0=(p_0+p_1)+sum_(j=2)^(m+1)p_j`.

Every nonzero summand is below the same upper row s=p_(m+2).
The sum is empty when m=0. This proves `q_0<=lr s` uniformly.

At m=0, b=q_0. At m=1,

`b=(2p_0+p_1)+p_2`.

For m>=2,

`b=(2p_0+p_1)+p_1+2sum_(j=2)^(m-1)p_j+p_m+p_(m+1)`.

Again all summands lie below the one fixed row s, proving `b<=lr s`.
The exceptional p_0 is always grouped inside a verified fixed row.
For m>=1, the p_(m+1) term supplies strictness throughout the support
of q_0 and b; m=0 is covered by the displayed finite row comparison.

Since `s<=lr D`, addition puts q_1=s+D between s and D:

`s<=lr q_1<=lr D`.

Consequently the desired uniform initial comparisons are

`q_0<=lr q_1`, `b<=lr q_1`.

The direction of the sum comparison is material: D is above q_1,
not below it. The argument uses only fixed-upper-row mixtures and
does not require arbitrary positive-sum closure of the folded cone.

## 4. What follows once the tail increment kernels are proved

If every q_j on a given tail has a folded-TP2 multiplication kernel,
then broadening and

`q_(j+1)=tq_j-q_(j-1)`

propagate the initial gap order to `q_j<=lr q_(j+1)` for all j.
For k>=1 the fixed endpoint P is the lower-degree endpoint, giving

`S_k=q_(k+1)`,

`E_k=E_1+sum_(j=1)^(k-1)q_j`.

The first comparison above gives `P1P<=lr E_1=p_(m+1)`. Time order
of the original p_j sequence gives

`P1P<=lr p_(m+1)<=lr s<=lr q_1`.

Thus the conditional tail q_j order implies `P1P<=lr E_k` for every
k>=1 by summing upper rows above one fixed lower row. It is not
necessary to compare P1P directly to q_0.

The exact recentered identity is

`S_k=(t-2)(C_k-1)+q_k+b`.

Once q_j time order is available, both q_k and b lie below S_k.
Subtracting this narrower residual gives

`S_k<=lr (t-2)(C_k-1)`.

These two deductions require only the stated increment-kernel theorem,
in addition to the unconditional initial comparisons proved above.

## 5. Precise remaining uniform nested-kernel issue

The outer recurrence has coefficients `A=T_(m+1)` and `B=T_(m-1)`,
using the inner prefix sequence defined above. If `U_j^out=U_j(t/2)` and
`T_k^out=sum_(j=0)^k U_j^out`, then

`q_j=y(A U_j^out+B U_(j-1)^out)`,

`C_k-1=yZ_k`, `Z_k=A T_k^out+B T_(k-1)^out`.

The scalar-coefficient mixed-ray proof does not automatically extend
to these m-dependent polynomial coefficients. Its resolvent summands
have templates `A(t-a)+B`. Two summands after removing common root
factors differ by `(a-b)B`, which is generally nonconstant. For their
midpoint

`H=A(t-a)(t-b)+B(t-(a+b)/2)`,

the exact mixed-minor formula is

`mixed(K_F,K_G)=2det(K_H)-(a-b)^2 det(K_B)/2`.

Accordingly, a sufficient replacement is a relative bound
`det(K_H)>=4det(K_B)` for every ordered row/column pair, together
with the required cone memberships, uniformly in the parameters and
in m. The old principal-minor bound for a constant difference does
not suffice here. The separate fixed-m=2 relative certificate must
not be promoted to an all-m result.

After increment/prefix kernels are supplied, the multiplier perturbation
and the strict final proxy comparison still require their quantitative
margins. The unconditional preliminary lemmas in this note remove the
initial-order obligations; they do not discharge those remaining
uniform nested-kernel and margin obligations or prove all one-turn
Local TP2 by themselves.

The additional inner factorization in `general_one_turn_reduction.md`
also checks exactly. With V_j=u_j+u_(j-1), A=u_n V_l and
B=u_(n-1)V_(l-1), for (n,l)=(h,h+1) at m=2h and (h+1,h+1) at
m=2h+1. For m>=1 both quotient factors have positive Jacobi
residues. This does not by itself solve the inner compatibility
problem: a linear factor z-alpha has central folded defect
`(3-alpha)^2-8`, which can be negative for alpha in [-2,2]. Thus
removing inner roots cannot be justified by treating every remaining
linear factor as a cone multiplier. The source correctly leaves this
issue open.
