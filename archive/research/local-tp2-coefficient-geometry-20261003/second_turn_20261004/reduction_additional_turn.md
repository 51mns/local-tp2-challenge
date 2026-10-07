# Exact reduction and all initial comparisons for an additional turn

Status: the identities, degree orientation, and initial LR comparisons
below are proved uniformly. The propagation theorem in Section 5 is
conditional on the explicitly stated folded-kernel and proxy inputs.
There is no claim about arbitrary canonical paths.

All source dependencies are read-only files in the parent directory.
The known theorem on every `L^m R^k` is the internally assembled theorem
in `recovery_oneturn_closure.md`, with the foundation and certificate
dependencies stated there. In particular this note uses its mixed-gap
time order, as well as Local TP2 at `L^m R`.

Write `f <=lr g` when the nonnegative dense Fourier half-rows obey

`W_n(f,g)=H(f)_n H(g)_(n+1)-H(f)_(n+1) H(g)_n >=0`.

The supported rows here have no internal zeros, so adjacent comparisons
give the corresponding ordered comparisons and can be composed. A
nonnegative sum of rows below one fixed upper row is below that row;
the analogous fixed-lower-row statement also holds. We use these
linearity statements, not additive closure of the folded cone.

## 1. Canonical formula, including the negative initial boundary

Put

`y=x+1`, `P1=x+2`, `z=2x+3`,
`u_j=U_j(z/2)`, `p_j=yu_j`, `T_j=sum_(i=0)^j u_i`,
`T_-1=0`, `g_j=1+yT_j`.

Fix `m>=0` and write

`P=g_m`, `X=g_(m+1)`, `t=3yP-x`, `tau=3yX-x`,
`c=T_m`, `a=T_(m+1)`, `d=T_(m+2)`.

The prefix recurrence gives

`d=za+1-c`, `z-1=2y`.                                    (1)

At `L^m`, the endpoints are `1,P` and the center is `X`. Its
right-child center is

`Q_0=tX-1-xP`.

The symmetry of this mutation gives also

`Q_0=tau P-1-xX`.                                        (2)

Consequently the extension `Q_-2=1`, `Q_-1=P` has precisely the
fixed-`X` recurrence

`Q_(ell+1)=tau Q_ell-Q_(ell-1)-xX`.                        (3)

For `ell>=0`, these are the actual centers on `L^m R L^ell`.
The value `Q_-2` is an auxiliary boundary value, not an extra path.

Using `t=z+3y^2c`, `tau=z+3y^2a` and (1), direct expansion gives

`(Q_0-P)/y=tau c+d`.                                    (4)

More explicitly both sides reduce to
`1+za+2yc+3y^2ac`. This proves the candidate initial identity
without division or a bounded check in `m`.

Set `v_N=U_N(tau/2)`, `v_-1=0`, and
`R_N=sum_(j=0)^N v_j`, `R_-1=0`. The homogeneous differences in
(3), with initial values `Q_-1-Q_-2=yc` and (4), give

`q_N:=Q_(N-1)-Q_(N-2)=y[c v_N+d v_(N-1)]`, `N>=0`.         (5)

Summing gives the exact additional-turn centers

`Q_ell=1+y Z_ell`,
`Z_ell=c R_(ell+1)+d R_ell`, `ell>=-1`.                    (6)

Here `R_0=1` makes the `ell=-1` case `Q_-1=P`. An equivalent
verification uses `R_N-tau R_(N-1)+R_(N-2)=1` and the exact
correction identity

`beta:=y(c+d)=zX-P1=tau-2-xX`.                            (7)

Thus the positive reversed pair `(c,d)` appears with outer index
`N=ell+1>=1`. Formula (5) at `N=0` is useful algebraically, but no
kernel or LR assertion for that initial row is needed below.

## 2. The degree orientation begins at ell=1

The leading coefficients of `T_m` and `tau` are positive, and their
degrees are respectively `m` and `m+3`. In (5), the degrees of the
two terms after multiplication by `y` are

`m+1+N(m+3)`, `m+3+(N-1)(m+3)`.

The first is larger by `m+1`. Hence

`deg Q_ell=(ell+2)(m+3)-2`, `ell>=-1`.                     (8)

At `ell>=1` the endpoints have degrees

`deg X=m+2`, `deg Q_(ell-1)=(ell+1)(m+3)-2>m+2`.

The child retaining `X` has degree `(ell+3)(m+3)-2`; the child
retaining `Q_(ell-1)` has degree `(2ell+3)(m+3)-3`. Their degree
difference is `ell(m+3)-1>0`. Thus the former really is the short
child, and its original short gap and child difference are

`S_ell=q_(ell+2)`,
`E_ell=Q_(ell-1)-X`,
`M_ell=3yQ_ell-x+1=2P1+3y^2 Z_ell`,
`D_ell=E_ell M_ell`.                                     (9)

The last equality is the universal mutation identity: for endpoints
`X,Y` and center `C`, subtracting the child retaining `X` from the
child retaining `Y` gives `(Y-X)(3yC-x+1)`.

At `ell=0`, the endpoints are `X,P`, and `P` is the lower-degree
endpoint. Continuing this new fixed-`X` ray is the long child there.
That state uses the existing one-turn theorem, not (9).

## 3. All initial LR comparisons are inherited, uniformly in m

For clarity denote the already studied fixed-`P` one-turn gaps by

`h_k=y[T_(m+1) U_k(t/2)+T_(m-1) U_(k-1)(t/2)]`.

Then `h_1=Q_0-X`, while the new first gap is

`q_1=h_1+p_(m+1)`.                                      (10)

The earlier reduction and completed kernel theorem establish

`p_(m+2)<=lr h_1<=lr h_2`.                               (11)

The all-left gap theorem establishes
`p_(m+1)<=lr p_(m+2)` because `m+1>=1`. The unconditional first
sandwich theorem, applied at inner index `m+1`, gives

`P1 X<=lr p_(m+2)<=lr E_1=h_1`.                          (12)

It remains to control the new correction `beta`. Its all-inner-index
expansion is

`beta=sum_(j=0)^m p_j+sum_(j=0)^(m+2) p_j`.

The two exact initial comparisons from
`general_one_turn_reduction.md` are

`p_0+p_1<=lr p_2`, with nonzero minors `(16,32,8)`,
`2p_0+p_1<=lr p_2`, with nonzero minors `(8,48,8)`.

For `m=0`, write `beta=(2p_0+p_1)+p_2`. Both summands are below
the fixed row `p_2`. For `m>=1`, group `2(p_0+p_1)`; all remaining
summands have indices between 2 and `m+2`, with nonnegative integer
multiplicities. Every group is below the same row `p_(m+2)`, by
the all-left time order and its transitivity. Thus

`beta<=lr p_(m+2)<=lr h_1`.                              (13)

At the known state `L^m R`, let `s=h_2` be its short outgoing
right gap and let `d_old` be its long-minus-short difference. Known
Local TP2 says `s<=lr d_old` (indeed strictly on its required support).
Its left outgoing gap is exactly the new gap

`q_2=s+d_old`.                                          (14)

By (10)--(11), both summands of `q_1` are below `s`; hence
`q_1<=lr s`. Fixed-upper-row and fixed-lower-row summation, (13),
and (14) now prove the full initial package

`q_1<=lr q_2`, `beta<=lr q_2`, `E_1<=lr q_2`,
`P1X<=lr E_1`.                                          (15)

Every inequality is uniform over `m>=0`. It needs no new finite
bridge and no cone assertion for `q_0`. In fact, at `m=0`,

`H(q_0)=(1,1)`, `H(q_1)=(211,175,98,34,6)`,
`W_0(q_0,q_1)=-36`.

So starting the new time-order induction at `q_0` would be wrong.
Starting at `q_1<=lr q_2` is sufficient for every `ell>=1`.

## 4. Recurrence transport needs only the actual new kernels

Suppose that each `q_N`, `N>=1`, has a nonnegative folded-TP2
multiplication kernel. The homogeneous recurrence in (5) gives

`W_n(q_N,q_(N+1))=W_n(q_N,tau q_N)+W_n(q_(N-1),q_N)`.

The first term is nonnegative by cone broadening: the unit row
concentrated at index zero is below the nonnegative row of `tau`, and
multiplication by the folded-TP2 kernel of `q_N` preserves the order.
Starting at (15), induction for `N>=2` proves

`q_N<=lr q_(N+1)` for every `N>=1`.                       (16)

The endpoint gap is exactly

`E_ell=E_1+sum_(N=2)^ell q_N`.

Equations (12), (15), and (16), using one fixed lower row, give

`P1X<=lr E_ell`, `ell>=1`.                               (17)

Put `A=tau-2`. Equations (3) and (7) also give

`S_ell=A(Q_ell-1)+q_(ell+1)+beta`
`     =Ay Z_ell+q_(ell+1)+beta`.                           (18)

Both summands of `q_(ell+1)+beta` lie below the fixed row
`S_ell=q_(ell+2)`, by (15)--(16). Subtracting this narrower row from
`S_ell` therefore yields

`S_ell<=lr Ay Z_ell`.                                    (19)

All rows in this subtraction are nonnegative: `A` has nonnegative
ordinary coefficients and the outer Chebyshev/prefix factors evaluated
at `tau` have nonnegative coefficients. For example their real roots
are in `[-2,2]`, while every `tau-r` has positive constant term and
nonnegative higher ordinary coefficients.

## 5. Exact remaining hypotheses and the final chain

The reduction is complete if, for all fixed `m>=0` and `ell>=1`,
the following new statements are established:

1. The actual reversed mixed gaps `q_N`, `N>=1`, have folded-TP2
   multiplication kernels.
2. `M_ell=2P1+3y^2 Z_ell` has a folded-TP2 multiplication kernel.
3. The proxy comparison is strict on each index
   `0<=n<=d_S`, where `d_S=(ell+3)(m+3)-2`:

   `H(y(tau-2)Z_ell)<lr H(3y^2XP1 Z_ell+2XP1^2)`.

The row on the right in the third item is exactly `H(XP1 M_ell)`.
Thus (17),
multiplier preservation, and (19) give

`S_ell<=lr y(tau-2)Z_ell <lr XP1 M_ell<=lr D_ell`.

Here `deg(y(tau-2)Z_ell)=deg S_ell=d_S`,
`deg(XP1 M_ell)=d_S+1`, and
`deg D_ell=(2ell+3)(m+3)-3>d_S+1`. Every row has positive entries
at all indices from zero to its degree: this follows from the positive
ordinary coefficient formulas above, or the established positivity of
the old initial gap followed by sums of the positive new gaps. For
`0<=n<d_S`, division by these positive entries composes the three
ratio comparisons, retaining the strict middle inequality. At `n=d_S`,
the actual target minor is directly `H(S_ell)_(d_S) H(D_ell)_(d_S+1)>0`.
Thus strictness holds at every required supported index, including
the terminal one. All subsequent target minors vanish because the
short row is zero there.

**Assembly theorem.** Assuming items 1--3 over their stated entire
parameter ranges, original strict canonical Local TP2 holds at
`L^m R L^ell` for every integer `m,ell>=0`, relative only to the
established one-turn and folded-kernel foundation theorems cited here.
The proof for `ell>=1` is the preceding chain, with `m=0` included
by the same initial comparisons and the same hypothesized kernels and
proxy bound. The proof for `ell=0` is the existing one-turn theorem.
No value `q_0`, cone-addition assertion, or other orientation is used
in this assembly.

In particular the new fixed proxy polynomials are

`J=y(tau-2)`, `V=3y^2XP1`, `K=2XP1^2`,
`deg J=deg K=m+4`, `deg V=m+5`,
`V=P1 J+yP1^2`.

No assertion that ordinary positivity implies folded-kernel membership
is used here. Sections 1--3 are unconditional algebra and inherited
LR comparisons; Section 4 and the final theorem retain their stated
kernel/proxy hypotheses until those are independently proved.

## 6. Exact checker and proof scope

`reduction_additional_turn.py` uses only Python integers and
`fractions.Fraction`; it imports no parent polynomial implementation.
It checks the load-bearing identities in generic formal variables,
the two fixed initial minors, and bounded instances constructed from
the original left/right scalar mutations. The bounded checks validate
implementation and orientation; the unbounded conclusions above use
the displayed recurrences and the cited established infinite theorems.
The checker does not promote its bounded Local TP2 checks to a theorem.
