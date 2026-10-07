# Strict Local TP2 on every path L^m R^2 L^ell

**Primary status: PROVED_INTERNAL — complete proof assembly with separate mathematical reviews and an independent finite-certificate reconstruction.**

## 1. Statement and scope

For every pair of integers `m,ell >= 0`, the original strict Local TP2
inequalities hold at the canonical Farey state with path `L^m R^2 L^ell`.
The terminal supported comparison is included. The result depends on the
previously proved folded-kernel, normalized-product, pure-left, one-turn,
and Jacobi-resolvent theorems identified below. It is a mathematical proof
with exact finite certificates, not an extrapolation from bounded paths.

This does not assert the theorem on arbitrary paths. In particular, it
does not settle `L^m R^k L^ell` for arbitrary `k>=3`, nor arbitrary further
alternations. No formal proof-assistant verification is claimed.

The root is `(1,2x^2+6x+5,x+2)`. With `y=x+1`, its child mutations are

\[
L=3yAC-x(A+C)-B,\qquad R=3yCB-x(C+B)-A.
\]

At a state with center `C`, let `U,V` be its children ordered by increasing
degree. The original target is

\[
S=U-C,\quad D=V-U,\qquad
F_n=H(S)_nH(D)_{n+1}-H(S)_{n+1}H(D)_n>0
\quad(0\le n\le\deg S),
\tag{1}
\]

where `H(P)_n=[q^n]P(q+q^{-1})`, with reflection at negative indices and
zero extension beyond the degree.

We use the folded-kernel convention and LR order in
`../hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md`. Write

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2},\qquad
\eta(h)=\min_{0\le n\le\deg h}\frac{\delta_n(h)}{h_n^2}.
\]

A strict folded-cone polynomial has a positive, nonincreasing half-row
and positive supported defects. Multiplication of two cone polynomials
preserves TP2. The established normalized product bound is

\[
\eta(FG)\ge
\frac{\eta(F)\eta(G)}{2(\min(\deg F,\deg G)+1)}.
\tag{2}
\]

All coefficient comparisons below are in the Laurent half-row basis
unless explicitly stated otherwise.

## 2. Exact seeds at the second right turn

Set

\[
u_j=U_j(x+3/2),\quad T_j=\sum_{i=0}^j u_i,\quad T_{-1}=0,
\quad g_j=1+yT_j.
\]

At the prefix `L^m R^2`, write the state as `(X,C_0,Y)`, where
`Y=g_m` and `X` is the center at `L^m R`. Define

\[
t_0=3yY-x,\quad
a_X=T_{m+1}(t_0+1)+T_{m-1},\quad X=1+ya_X,
\]
\[
t=3yX-x,\qquad A=t_0a_X-u_m,\qquad B=u_{m+1}.
\tag{3}
\]

These are identities from the original mutation, not definitions of a
different sequence. Equivalently,

\[
A=(C_0-Y)/y,\quad B=(tY-xX-C_0-Y)/y,
\qquad t=t_0t_{m+1}-y(x+3).
\tag{4}
\]

The notation `t_{m+1}=3yg_{m+1}-x` in (4) is an inner pure-left trace.
The new outer trace is `t`. Their distinction matters.

The degrees are

\[
\deg Y=m+1,\quad \deg X=2m+4,\quad
\deg A=3m+5,\quad \deg B=m+1,\quad\deg t=2m+5.
\tag{5}
\]

All these polynomials have positive ordinary coefficients, including
`t-r` for every real `r in [-2,2]`. Moreover `A>=B` coefficientwise:
`a_X>=T_{m+1}>=u_m,u_{m+1}`, and
`A=(t_0-1)a_X+(a_X-u_m)>=a_X>=B`.

Let `v_N=U_N(t/2)`, `v_-1=0`, and `R_N=sum_(j=0)^N v_j`. The subsequent
left run has

\[
Z_N=AR_N+BR_{N-1},\quad q_N=y(Av_N+Bv_{N-1}),\quad C_N=Y+yZ_N.
\tag{6}
\]

For `N>=1` the endpoint `X` is shorter than `C_(N-1)`. Thus the actual
target in (1) is

\[
S_N=q_{N+1},\quad E_N=C_{N-1}-X,\quad
M_N=3yC_N-x+1,\quad D_N=E_NM_N.
\tag{7}
\]

With `p=x+2`, put

\[
\Pi=Xp,\quad K_0=t_0+1,\quad J=y(t-2),\quad
V=3y^2Xp,\quad K=XpK_0.
\tag{8}
\]

Then

\[
M_N=3y^2Z_N+K_0,\quad \Pi M_N=VZ_N+K,
\quad V=pJ+yp^2,
\tag{9}
\]
\[
q_{N+1}=JZ_N+q_N+y(A+B),\qquad
E_N=E_1+\sum_{j=1}^{N-1}q_j.
\tag{10}
\]

## 3. All-m kernel and initial-order inputs

The new results in `../hour_quantum/UNIFORM_SEED_STRENGTH.md`,
`../hour_transport/all_m_trace_transport.md`, and
`../hour_transport/all_m_mixed_transport.md` establish the following.
Put `c_0=1/400000000`, `sigma=59/100`.

For every `m>=0`, every `r,s,c in [-2,2]`, the single and midpoint
polynomials

\[
L_r=A(t-r)+B,\qquad H_{r,s,c}=A(t-r)(t-s)+B(t-c)
\tag{11}
\]

and their products with `y` are strict cone polynomials. The midpoints
dominate every required reference minor of `B` or `yB` by a factor four.
Consequently the positive Jacobi-resolvent summands for both `Z_N` and
`q_N` are pairwise compatible on every ordered kernel minor. These
claims hold on the full real parameter boxes, not sampled roots.

The usable quantitative bounds, valid at every `m>=0`, are

\[
\eta(t-r)\ge E_t(m):=
\frac{c_0^2\sigma^{2m+1}}{16(m+3)},\qquad
\eta(L_r)\ge E_L(m):=
\frac{c_0^5\sigma^{5m+2}}{65536(m+3)^4}.
\tag{12}
\]

The smoothed trace `J` is `mu_m`-strong, where

\[
\mu_0=18,\quad\mu_1=72,\quad
\mu_m=9\,4^m-21\,2^m-25\quad(m\ge2).
\tag{13}
\]

The initial-order note in `../hour_invariant/ALL_M_INITIAL_COMPARISONS.md`
derives from the previously proved one-turn theorem and its companion
transport the four comparisons

\[
q_0\le_{lr}q_1,\quad y(A+B)\le_{lr}q_1,\quad
\Pi\le_{lr}E_1,\quad \Pi\le_{lr}q_1.
\tag{14}
\]

For clarity, the key reduction uses old right-run increments `p_j`.
Writing `b=yB=g_(m+1)-g_m`, one has
`b<=lr p_1<=lr p_2<=lr p_3` and
`q_0=b+p_1+p_2<=lr p_3<=lr q_1`. Also `b<=lr q_0`, so
`q_0+b<=lr q_0<=lr q_1`. The higher-endpoint companion gives
`Xp<=lr p_2=E_1`, and `p_2<=lr q_1`. The root exceptions in the
companion recurrence use the already proved first-child bases.

Cone closure in (11) and the gap recurrence imply
`q_N<=lr q_(N+1)` by induction. Equations (10) and (14) then give

\[
S_N\le_{lr}JZ_N,\qquad \Pi\le_{lr}E_N.
\tag{15}
\]

It remains to prove that `M_N` is cone and

\[
JZ_N<_{lr}VZ_N+K
\tag{16}
\]

through every supported index. The rest of this note proves these two
obligations for all `m,N`, with a finite bridge followed by an analytic
tail.

## 4. Finite bridge: 0 <= m <= 76, every N >= 1

The exact standalone generator `verify_uniform_ray_closure.py`
constructs each prefix from the root by the original ordinary-x
mutations. It does not import another author's implementation or
expected certificate arrays.

For each of the 77 values of `m`, write `j=H(J)`, `k=H(K)`,
`a=H(K_0)`, and `w_n=W_n(J,V)`. Every `w_n` is strictly positive.
For `0<=n<=deg K`, set

\[
i_n=\min(n,\deg J),\qquad
\alpha_n=\left\lfloor\frac{2J(2)k_n}{w_{i_n}}\right\rfloor+1.
\tag{17}
\]

The generator certifies on the entire interval `r in [-2,2]` that

\[
\det K_{L_r}[(i_n,i_n+1),(n,n+1)]>
\alpha_nL_r(2).
\tag{18}
\]

For `0<=n<=deg K_0+1`, set

\[
\beta_n=6(a_{n-1}+3a_{n+1})+1.
\tag{19}
\]

It likewise certifies

\[
\delta_n(y^2L_r)>\beta_nL_r(2),\qquad
\delta_0(t-r)>2(t(2)-r).
\tag{20}
\]

Every margin is a polynomial of degree at most two in `u`, where
`r=2-4u`, `0<=u<=1`. Its three degree-two Bernstein coefficients are
computed exactly; all **38,115** coefficients are strictly positive.
The Bernstein-to-power reverse identity is checked for every margin.
Every coefficient, each threshold (17),(19), and all finite initial-order
checks are saved in `uniform_ray_closure_results.json`.

The general criterion in
`../hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md` now applies with
`rho=1/2` and propagator mass factor `gamma=2`. Its squared positive
residue weights are retained: if there are at most `N` active residues,
`sum lambda_i^2>=1/N`, and `2^(N-1)>=N`. This proves the two remaining
obligations for every `N>=1`, including all terminal indices, at each
of these 77 inner indices. No finite bound on `N` is used.

## 5. A normalized smoothing lemma

Let `F` be a strict cone polynomial of positive degree, with half-row
`f_0<=C f_1`. Then

\[
\eta(y^2F)\ge
\frac{\min(1,4/C^2)}{81}\eta(F).
\tag{21}
\]

Indeed `H(y^2)=(3,2,1)`. Its folded kernel's first two rows have minors
4 on columns `(0,1)` and 1 on columns `(2,3)`; all other ordered
minors are nonnegative. Cauchy--Binet gives

\[
\delta_n(y^2F)\ge4\delta_n(F)
+\det K_F[(2,3),(n,n+1)].
\]

For `n>=2`, the latter term is at least `delta_(n-2)(F)`, while
`H(y^2F)_n<=9f_(n-2)`. This includes `n=deg F+1,deg F+2`.
At `n=0` use `4delta_0(F)` and `H(y^2F)_0<=9f_0`.
At `n=1` use `4delta_1(F)>=4eta(F)f_0^2/C^2` and the same mass
bound `H(y^2F)_1<=9f_0`. These prove (21).

For the present `L_r`, take `C=8`. To verify this without an unproved
smoothing assertion, put `a=H(yX)`. Then `a_0<=2a_1`, and the row
`f=H(t-r)` satisfies

`f_0=3a_0-r<=6a_1+2<=4(3a_1-1)=4f_1`, since `a_1>=1`.

The trace row is nonnegative and nonincreasing. Hence, at every row
index `i`, `K_(t-r)(i,0)<=4K_(t-r)(i,1)`. Multiplying by the
nonnegative row of `A` gives `H(A(t-r))_0<=4H(A(t-r))_1`.
Since `B<=A(t-r)`, addition gives `H(L_r)_0<=8H(L_r)_1`.
Therefore

\[
\eta(y^2L_r)\ge E_L(m)/1296.
\tag{22}
\]

## 6. Base normalized bounds and coefficient domination

This section is used only for `m>=77`. Put

\[
s_m=H(t)_0-2,\qquad D_m=2(\deg t+1)=4m+12,
\]
\[
E_m=E_L(m)\frac{(4/49)^m}{6048(4m+14)},
\qquad
c_m=\frac{27^3\,6^{4m+2}}
{2(2m+3)(2m+5)^2(2m+7)}.
\tag{23}
\]

Both possible base polynomials `C L_r`, with `C=J` or `C=y^2`, have
normalized defect at least `E_m`. For `C=y^2`, this follows from
(22). For `C=J`, use (2), (12), and

\[
\eta(J)\ge\frac{\mu_m}{J(2)}
\ge\frac1{6048}(4/49)^m\quad(m\ge3).
\tag{24}
\]

Here the first inequality is strength divided by maximum row entry,
bounded by mass. The elementary pure-left recurrence gives
`g_m(2)<=4*7^m`, whence `t(2)<=9072*49^m` and
`J(2)<=27216*49^m`. Also `mu_m>=(9/2)4^m` for `m>=3`.
The denominator in (2) is `2(deg J+1)=4m+14`.

The same two base polynomials dominate their respective corrections:

\[
JL_r\ge c_mK,\qquad y^2L_r\ge c_mK_0
\quad\text{coefficientwise}.
\tag{25}
\]

Here is a full derivation. Put `b_m=H(t_0)_0` and
`d_m=H(T_(m+1))_0`. Since `a_X>=T_(m+1)(t_0+1)` and `a_X>=u_m`,

\[
A=t_0a_X-u_m\ge(b_m-1)a_X
\ge(b_m-1)d_mK_0,
\]

and multiplication by `t-r` contributes its central coefficient at
least `s_m`. Thus `L_r>=(b_m-1)d_ms_mK_0`.

Also `J=3y^2X-yp>=2y^2X`, because `yX>=p`.
The Laurent comparison `y^2>=p` gives

\[
JL_r\ge2(b_m-1)d_ms_mK,
\quad y^2L_r\ge3(b_m-1)d_ms_mK_0.
\tag{26}
\]

The inherited pure-left central bound is
`b_m>=27*6^m/(2m+5)`. Positivity, decrease, and the inner recurrence
at `x=2` give
`d_m>=6^(m+1)/(2m+3)`.
Finally (4) gives

\[
s_m\ge b_mb_{m+1}-7\ge\tfrac12 b_mb_{m+1},\qquad
b_m-1\ge b_m/2.
\tag{27}
\]

These inequalities hold well before the tail starts; for the first
bound in (27), `b_mb_(m+1)>=14` suffices. Substitution in (26) proves
(25), with exactly the conservative constant in (23).

## 7. Uniform normalized perturbation through every outer length

The established positive Jacobi-resolvent expansion has

\[
Z_N=\sum_{i\in I}\lambda_i Z_i,\quad
Z_i=L_{r_i}\prod_{j\ne i}(t-r_j),\quad
\lambda_i>0,\quad\sum_i\lambda_i=1,\quad |I|\le N.
\tag{28}
\]

Each summand contains exactly `N-1` propagators. Their mixed kernel
minors are nonnegative. This remains true after common multiplication
by either `C=J` or `C=y^2`.

Put `F=CZ_N`, `F_i=CZ_i`, and let `Q` denote the corresponding fixed
correction (`K` if `C=J`, `K_0` if `C=y^2`). At every supported index,

\[
\tfrac12H(F)\le H(F_i)\le2H(F).
\tag{29}
\]

To justify the comparison uniformly in `N`, all summands contain the
same polynomial `A R_N`. Since `B<=A` and every omitted trace factor
has central coefficient at least `s_m>1`,

`A R_N <= Z_i <= (1+1/s_m) A R_N <=2 A R_N`.

The same holds for their convex average and after multiplication by
`C`. No comparison whose constant grows with `N` is being used.

By (2), (12), (23), (25), and nonnegative convolution,

\[
\eta(F_i)\ge E_m(E_t(m)/D_m)^{N-1},\qquad
F_i\ge c_ms_m^{N-1}Q.
\tag{30}
\]

Cauchy--Binet compatibility, the squared weights in (28), and (29)
therefore imply

\[
\eta(F)\ge\frac{E_m}{4N}(E_t(m)/D_m)^{N-1},\qquad
H(Q)\le\varepsilon_NH(F),\quad
\varepsilon_N=\frac{2}{c_ms_m^{N-1}}.
\tag{31}
\]

In particular, if

\[
E_mc_m>96,\qquad
\mathcal R_m:=E_t(m)s_m/D_m\ge2,\qquad c_m\ge2,
\tag{32}
\]

then `epsilon_N<=1` and

\[
\frac{\eta(F)}{\varepsilon_N}
\ge\frac{E_mc_m}{8}\frac{\mathcal R_m^{N-1}}N>12
\quad\text{for every }N\ge1.
\tag{33}
\]

The elementary inequality `2^(N-1)>=N` handles all `N`, including
`N=1`. In particular no infinite sequence of additional certificates
is hidden in (33).

The scalar gates (32) hold for all `m>=77`. An explicit lower bound for
the second one, from (12),(27), is

\[
\mathcal R_m\ge
\frac{c_0^2\sigma^{2m+1}27^2\,6^{2m+1}}
{128(m+3)^2(2m+5)(2m+7)}.
\tag{34}
\]

At `m=77`, the exact rational values in the result JSON give
`E_m c_m>165` and the right side of (34) greater than 2.
The consecutive ratio of `E_m c_m` is

\[
6^4\sigma^5\frac4{49}
\left(\frac{m+3}{m+4}\right)^4
\frac{2m+7}{2m+9}
\frac{2m+3}{2m+5}
\left(\frac{2m+5}{2m+7}\right)^2
\frac{2m+7}{2m+9}.
\tag{35}
\]

Every variable factor is increasing, and their product is greater
than 6 at 77. The consecutive ratio in (34) is

\[
36\sigma^2
\left(\frac{m+3}{m+4}\right)^2
\frac{2m+5}{2m+7}\frac{2m+7}{2m+9}>11
\quad(m\ge77).
\tag{36}
\]

This product is likewise increasing. The constant `c_m` is increasing
on the tail by its displayed formula. These are exact rational
inequalities in the generator, so (32) holds on the whole infinite
tail.

## 8. Absorbing the multiplier and proxy corrections

First take `C=y^2`, `F=y^2Z_N`, `Q=K_0`. The established normalized
perturbation inequality for a nonincreasing, log-concave base half-row
(in particular the present strict folded-cone row) says that
`0<=H(G)<=epsilon H(F)` implies

\[
\delta_n(F+G)\ge\delta_n(F)
-(4\varepsilon+2\varepsilon^2)H(F)_n^2.
\tag{37}
\]

Use `G=K_0/3`; the more conservative `epsilon_N` from (31) is valid.
Since `epsilon_N<=1` and `eta(F)>12epsilon_N`, the right side of
(37) is strictly positive throughout the support. Therefore
`M_N=3(F+K_0/3)` is strict cone.

For the proxy, take `C=J`, `F=JZ_N`, `Q=K`. The exact remainder in
(9) is `R=yp^2`, with half-row `(14,11,5,1)`. Thus

\[
W_n\bigl(J,V-\tfrac12pJ\bigr)
=\tfrac12\delta_n(J)+W_n(J,R)
\ge(\mu_m/2-14)H(J)_n\ge0.
\tag{38}
\]

Here `mu_m>=28` throughout the tail. Both rows in (38) are positive
on their supported intervals. Consequently all their ordered minors
are nonnegative. Common multiplication by the cone kernel of `Z_N`
gives the stronger gap estimate

\[
W_n(JZ_N,VZ_N)\ge\tfrac12\delta_n(JZ_N).
\tag{39}
\]

The correction obeys, by decrease and (31),

\[
W_n(F,K)\ge-H(F)_{n+1}H(K)_n
\ge-\varepsilon_NH(F)_n^2.
\]

Combining (33),(39) yields (16) strictly at every index through
`deg F`, including those above the degree of `K` and the terminal
index. This proves the two remaining obligations for all `m>=77`.

## 9. Return to the original target, including boundary cases

For every `m>=0,N>=1`, Sections 4 or 8 give strict (16) and a cone
multiplier `M_N`. Hence (15), LR preservation under this multiplier,
and transitivity yield

\[
H(S_N)\le_{lr}H(JZ_N)
<_{lr}H(\Pi M_N)\le_{lr}H(E_NM_N)=H(D_N).
\tag{40}
\]

The middle comparison is strict through `deg S_N=deg(JZ_N)`.
Every row used has a positive supported interval. Thus (40) proves
the original inequalities (1), with no lost terminal comparison.
The degrees are explicitly

\[
\deg S_N=(2m+5)N+5m+11,\quad
\deg D_N=(4m+10)N+4m+8,
\]

whose difference is `(2m+5)N-m-3>=m+2>0` for `N>=1`.

The case `ell=N=0` has the opposite endpoint orientation; it is
already included in the previously proved one-turn theorem
`L^m R^k` with `k=2`. We do not extend (7) incorrectly to this case.
All `m=0` and `m=1` cases are included in the finite bridge and agree
with the separately audited `R^2L^ell` and `LR^2L^ell` theorems.

Therefore, subject to the explicitly cited prior foundation theorems
and the audited new certificates, strict Local TP2 holds on all
`L^m R^2 L^ell`, for integers `m,ell>=0`.

## 10. Dependency and reproducibility record

New proof dependencies in this campaign:

| Obligation | Proof | Exact generator / independent review |
|---|---|---|
| Uniform second-turn seeds and normalized bounds | `../hour_quantum/UNIFORM_SEED_STRENGTH.md` | `uniform_seed_strength.py`, `uniform_ax_normalized.py`, `audit_uniform_seed_finite.py` in that directory |
| Uniform trace and smoothed trace | `../hour_transport/all_m_trace_transport.md` | `verify_trace_transport.py` |
| Uniform single/midpoint compatibility | `../hour_transport/all_m_mixed_transport.md` | `verify_uniform_mixed_transport.py` |
| All-m initial LR comparisons | `../hour_invariant/ALL_M_INITIAL_COMPARISONS.md` | Structural transport from prior one-turn theorem |
| Finite ray-extension criterion | `../hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md` | Independent criterion audit in `../hour_quantum/AUDIT_FINITE_RAY_CRITERION.md` |
| Finite bridge and analytic scalar gates | This note | `verify_uniform_ray_closure.py`, `uniform_ray_closure_results.json` |

The prior repository at commit
`a36fbac460073bf757434f122e721dfa254e8e48` supplies:
`continuation_kernel/folded_kernel_theorem.md`,
`mixed_kernel_strong_cone.md`, `mixed_kernel_all_minor_strength.md`,
`fulltree_oneturn_normalized_tail.md`, `mixed_kernel_sharp_strength.md`,
`recovery_oneturn_closure.md`, `general_one_turn_reduction.md`,
`general_one_turn_kernel_theorem.md`, and
`common_closure_20261004/reduction_common.md` under
`research/local-tp2-coefficient-geometry-20261003/`.

The new independent reviews are shared-session internal audits. They
are distinct implementations and separate mathematical checks, but
they are not external replication, blind review, or formal verification.
