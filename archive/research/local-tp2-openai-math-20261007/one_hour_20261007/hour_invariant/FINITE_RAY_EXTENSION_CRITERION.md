# A finite certificate criterion for extending a canonical prefix along every left ray

**Status: PROVED_INTERNAL, with a shared-session independent mathematical audit PASS in `../hour_quantum/AUDIT_FINITE_RAY_CRITERION.md`.** This is a general sufficient-condition theorem extracted from the independently audited proofs for `R²L^N` and `LR²L^N`. Its proof is given below. It does not assert that its finite conditions hold for every prefix. In particular, it does not establish arbitrary-tree Local TP2 or remove the existing global preservation gap.

The useful reduction is that **no unbounded path length occurs in the hypotheses**. For a fixed canonical prefix, the hypotheses involve fixed polynomials, finitely many coefficient indices, and polynomial inequalities on intervals or a three-dimensional compact box. Complete Bernstein certificates turn these into finitely many exact rational inequalities. The conclusion concerns the original strict Local TP2 minors at every subsequent left-ray state.

The inherited mathematical input is the proved folded-kernel criterion and quantitative all-minor strength theorem in the previous research files `continuation_kernel/folded_kernel_theorem.md` and `mixed_kernel_all_minor_strength.md`. The spectral, mass-propagation, correction, and original-target arguments are restated explicitly here.

## 1. Notation and the inherited folded-kernel facts

Put `y=x+1` and `p=x+2`. For a real polynomial `P`, write

\[
h_P(j)=[q^j]P(q+q^{-1}),\qquad j\ge0,
\]

with `h_P(-j)=h_P(j)` and zero extension above the degree. Its mass is

\[
\mathfrak m(P)=P(2)=h_P(0)+2\sum_{j\ge1}h_P(j).
\]

A positive interval row means `h_P(j)>0` for every integer `0<=j<=deg P`. Define

\[
\delta_j(P)=h_P(j)^2-h_P(j-1)h_P(j+1)-h_P(j+1)^2+h_P(j)h_P(j+2).
\tag{1.1}
\]

The folded multiplication kernel is

\[
K_P(i,j)=
\begin{cases}
h_P(j),&i=0,\\
2h_P(i),&i>0,\ j=0,\\
h_P(|i-j|)+h_P(i+j),&i,j>0.
\end{cases}
\tag{1.2}
\]

It satisfies `H(PQ)=H(P)K_Q` and `K_(PQ)=K_PK_Q`. A polynomial is in the **folded cone** if it has a positive interval row and every supported defect (1.1) is nonnegative. It is **strict** if all those defects are positive. The zero polynomial may be used as a reference `B`, with all of its kernel minors zero.

The established facts used are:

1. The finite defect condition is equivalent to TP2 of the entire infinite kernel. Products preserve the cone, and products of strict factors are strict.
2. For any adjacent row and column pairs with `n>=a>=0`,

   \[
   \det K_P[(a,a+1),(n,n+1)]\ge\delta_{n-a}(P).
   \tag{1.3}
   \]

   In particular every adjacent principal minor is at least `delta_0(P)`. If `P` is strict and `0<=n-a<=deg P`, the selected minor is positive. For `a=0`, (1.3) is an equality. For `a>0`, the interior formula in the folded-kernel proof is bounded below by `Delta_(n-a)-Delta_(n+a+1)>=delta_(n-a)`; the support-boundary formula gives the same inequality.
3. If `B` is in the cone, `H(H)>=H(B)` coefficientwise, and

   \[
   \delta_j(H)\ge8h_B(0)h_H(j)
   \quad(0\le j\le\deg H),
   \tag{1.4}
   \]

   then for every ordered pair of rows and columns,

   \[
   \det K_H[I,J]\ge4\det K_B[I,J].
   \tag{1.5}
   \]

   This is the quantitative all-minor strength corollary, not an inference from finitely many sampled kernel indices. When the reference minor is positive, the all-minor strength bound and `K_B(i,j)<=2h_B(0)` prove (1.5). A nonpositive reference minor needs only TP2 of `K_H`.

Write `P<=lr Q` when every ordered two-column minor of the two half-rows is nonnegative. For positive interval rows with `deg P<=deg Q`, it is enough to check the finitely many adjacent determinants

\[
W_j(P,Q)=h_P(j)h_Q(j+1)-h_P(j+1)h_Q(j)
\]

through the smaller degree. Multiplication by a folded-cone polynomial preserves this order by Cauchy–Binet.

## 2. Fixed canonical input and the exact ray identities

Let `(X,C_0,Y)` be the left endpoint, center, and right endpoint after a fixed canonical Farey prefix. Subsequent left moves keep `X` fixed. The canonical root is `(1,2x²+6x+5,x+2)`, and its mutations are

\[
\mu_X=3yXC-x(X+C)-Y,\qquad
\mu_Y=3yYC-x(Y+C)-X.
\tag{2.1}
\]

Define fixed polynomials

\[
t=3yX-x,\quad T=tY-xX-C_0,\quad
A=(C_0-Y)/y,\quad B=(T-Y)/y.
\tag{2.2}
\]

Polynomial divisibility in (2.2) is a finite algebraic prerequisite. Here `T` is the inverse center, not a spectral prefix sum. The condition `B>=0` used below is a real restriction of the criterion: the theorem does not silently replace a negative seed by a positive one.

Let `u_0(z)=1`, `u_1(z)=z`, `u_(j+1)=zu_j-u_(j-1)`, and `u_-1=0`. Put

\[
R_N(z)=\sum_{j=0}^N u_j(z),\qquad R_{-1}=0.
\]

All following `u_j,R_j` are evaluated at `t(x)`. Define

\[
q_N=y(Au_N+Bu_{N-1}),\quad
Z_N=AR_N+BR_{N-1},\quad C_N=Y+yZ_N.
\tag{2.3}
\]

Then, identically,

\[
C_{-1}=Y,\quad C_{-2}=T,\quad
C_{N+1}=tC_N-C_{N-1}-xX,\quad
q_N=C_N-C_{N-1},\quad q_{N+1}=tq_N-q_{N-1}.
\tag{2.4}
\]

The initial previous gap is `q_-1=-yB`, which is why the seed formula has a **plus** sign. Equations (2.3) follow from this homogeneous gap recurrence and summation; they identify the abstract ray with the original mutation.

For the degree bookkeeping, assume the finite identities

\[
\deg X=a,\quad\deg Y=b,\quad
\deg t=a+1=:h,\quad\deg C_0=a+b+1,\quad
\deg A=a+b,\quad\deg B<\deg A+h,
\tag{2.5}
\]

where `a,b>=0`, with positive leading coefficients. These are the usual canonical degrees and can also be checked directly at the supplied prefix. The zero reference `B=0` satisfies the last inequality by convention. The positivity hypotheses below imply

\[
\begin{aligned}
\deg Z_N&=a+b+Nh,\\
\deg C_N&=a+b+1+Nh,\\
\deg C_{N-1}&=b+Nh>a\qquad(N\ge1).
\end{aligned}
\tag{2.6}
\]

Thus, for `N>=1`, `X` is the shorter endpoint, regardless of the endpoint orientation at `N=0`. Subtracting the two actual child formulas gives the original target polynomials

\[
S_N=q_{N+1},\quad E_N=C_{N-1}-X,\quad
M_N=3yC_N-x+1,\quad D_N=E_NM_N.
\tag{2.7}
\]

The fixed proxy data are

\[
\begin{aligned}
P&=pX,&M_0&=3yY-x+1,\\
J&=y(t-2),&V&=3y^2P,&K&=PM_0,\\
\beta&=y(A+B),&E_1&=C_0-X.
\end{aligned}
\tag{2.8}
\]

They satisfy

\[
M_N=M_0+3y^2Z_N,\quad PM_N=VZ_N+K,\quad
V=pJ+yp^2,
\tag{2.9}
\]

and the telescoping identities

\[
S_N=JZ_N+q_N+\beta,\qquad
E_N=E_1+\sum_{j=1}^{N-1}q_j.
\tag{2.10}
\]

In particular, if `d=deg J=a+2` and `e=deg K=a+b+2`, then

\[
\deg V=d+1,\quad e-d=b,
\tag{2.11}
\]

and

\[
\begin{aligned}
\deg S_N&=2a+b+2+Nh=\deg(JZ_N),\\
\deg D_N&=a+2b+2+2Nh,\\
\deg D_N-\deg S_N&=b+1+(N-1)h>0.
\end{aligned}
\tag{2.12}
\]

## 3. The finite hypotheses

All parameter-dependent hypotheses below hold throughout their indicated interval or box. A sufficient exact implementation is a full tensor Bernstein certificate, as described in Section 9.

### Gate A: positivity and raw kernel compatibility

The fixed rows of `A,yA,E_1,M_0,P,J,V,K` have positive interval support. The reference `B` is either zero or has a nonnegative positive-interval row and belongs to the folded cone. The polynomials `A,yA` are strict. For every `r,s,c in [-2,2]`, put

\[
f_r=t-r,\quad L_r=A(t-r)+B,\quad
H_{r,s,c}=A(t-r)(t-s)+B(t-c).
\tag{3.1}
\]

Require positive interval support, independent of the parameters, for `f_r,L_r,yL_r,H_(r,s,c)`, and require:

\[
f_r,\ L_r,\ yL_r\text{ are strict folded-cone polynomials};
\tag{3.2}
\]

\[
H(H_{r,s,c})\ge H(B),\qquad
\delta_j(H_{r,s,c})\ge8h_B(0)h_{H_{r,s,c}}(j)
\tag{3.3}
\]

at every supported `j`, with `H_(r,s,c)` in the folded cone. For `B=0`, require that last cone assertion directly. In the positive reference case it already follows from (3.3).

Dense positive ordinary coefficients on the box are a convenient stronger way to certify the support statements. Nonnegative Laurent coefficients and explicitly checked interval support also suffice; no ordinary-coefficient positivity is used in the kernel arguments themselves.

### Gate B: one of two finite smoothing mechanisms

Because multiplication by `y=x+1` does not preserve the folded cone, **one** of the following mechanisms is required.

**B1: certify the smoothed midpoint.** Require `yB` to be zero or in the cone; require positive interval rows and, for every `r,s,c`,

\[
H(yH_{r,s,c})\ge H(yB),\quad
\delta_j(yH_{r,s,c})\ge8h_{yB}(0)h_{yH_{r,s,c}}(j),
\tag{3.4}
\]

with `yH_(r,s,c)` in the cone. This handles smoothed mixtures uniformly at every size.

**B2: absorb `y` into a common propagator.** Require `y(t-r)` to be strict for every `r in [-2,2]`, and require the one additional fixed polynomial

\[
q_2=y\{A(t^2-1)+Bt\}
\tag{3.5}
\]

to be strict. The already listed `yA,yL_r` handle the smaller cases. A smoothed three-parameter midpoint certificate is unnecessary under B2.

### Gate C: a trace mass rate and finitely many template minor bounds

Set

\[
\tau=t(2)>2,\quad A_*=A(2)>0,\quad B_*=B(2)\ge0.
\]

Choose a rational `gamma>1` such that, for all `r in [-2,2]`,

\[
\delta_0(t-r)\ge\gamma(\tau-r).
\tag{3.6}
\]

Define the fixed constants

\[
\rho=\frac{A_*+B_*/(\tau+2)}{A_*+B_*/(\tau-2)},\quad
N_*=\max\{1,\lceil1/(\gamma-1)\rceil\},
\]

\[
\eta=\frac{\gamma^{N_*-1}}{N_*},\qquad \theta=\rho\eta>0.
\tag{3.7}
\]

Any smaller positive rational lower bound for `rho`, `eta`, or `theta` can be used. In particular, `gamma>=2` implies `eta=1`; if `B_*<=A_*(tau-2)`, then `rho>=1/2` is sufficient.

For every integer `0<=n<=e=deg K`, put `i_n=min(n,d)` and choose `alpha_n>0` such that

\[
\det K_{L_r}[(i_n,i_n+1),(n,n+1)]
\ge\alpha_n L_r(2)\qquad(-2\le r\le2).
\tag{3.8}
\]

Let `m_j=h_(M_0)(j)`, symmetrically extended, and let `m=deg M_0=b+1`. For every `0<=n<=m+1`, choose `beta_n>0` such that

\[
\delta_n(y^2L_r)\ge\beta_n L_r(2)\qquad(-2\le r\le2).
\tag{3.9}
\]

These bounds concern finitely many minors of the fixed-degree template `L_r`, never minors at unbounded run lengths.

### Gate D: the finite correction inequalities

Compute all the fixed adjacent proxy minors

\[
w_j=W_j(J,V)>0\qquad(0\le j\le d).
\tag{3.10}
\]

For `0<=n<=e`, require

\[
\boxed{\theta\,w_{i_n}\alpha_n>J(2)h_K(n).}
\tag{3.11}
\]

The endpoint multiplier need not have a folded-cone base term `M_0`. To allow its finite negative defects, define

\[
Z_1(2)=A_*(\tau+1)+B_*,\quad
\nu_n=m_{n-1}+3m_{n+1}.
\]

For `0<=n<=m+1`, require

\[
\boxed{
9\theta\beta_n>
27\nu_n+
\frac{\max\{-\delta_n(M_0),0\}}{Z_1(2)}.
}
\tag{3.12}
\]

If `M_0` is in the folded cone, the last term vanishes. In the simpler choice `theta=1/2`, (3.12) then becomes `beta_n>6nu_n`, exactly the form used in the `LR²L^N` proof.

### Gate E: four initial likelihood-ratio comparisons

Require the finite comparisons

\[
q_0\le_{\rm lr}q_1,\quad
\beta\le_{\rm lr}q_1,\quad
P\le_{\rm lr}E_1,\quad
P\le_{\rm lr}q_1.
\tag{3.13}
\]

For the fourth condition, the stronger pair `P<=lr E_1<=lr q_1` is also sufficient. All rows involved must have positive interval support and the indicated support ordering. Hence checking every adjacent minor through the smaller degree is a finite exact test.

No Local TP2 assertion at a later ray state is included in these hypotheses.

## 4. The extension theorem

**Theorem.** Suppose the fixed input is a canonical prefix, the algebraic and degree prerequisites (2.2), (2.5) hold, and finite Gates A–E are certified, with either B1 or B2. Then, for every integer `N>=1`, at the original canonical state obtained by appending `L^N`,

\[
\boxed{
h_{S_N}(n)h_{D_N}(n+1)-h_{S_N}(n+1)h_{D_N}(n)>0
\quad(0\le n\le\deg S_N).
}
\tag{4.1}
\]

If the single prefix state `N=0` also has all its original Local TP2 minors positive, checked directly with its actual degree ordering or supplied by an already proved family, the conclusion holds for every `N>=0`.

### 4.1 Why the kernel hypotheses cover every spectral size

For two roots `r,s`, define

\[
F=A(t-r)(t-s)+B(t-s),\quad
G=A(t-r)(t-s)+B(t-r).
\]

Their midpoint is `H_(r,s,(r+s)/2)` and `F-G=(r-s)B`. On any ordered two rows and columns, the coefficient of `ab` in `det(aK_F+bK_G)` is exactly

\[
2\det K_{H_{r,s,(r+s)/2}}
-\frac{(r-s)^2}{2}\det K_B\ge0.
\tag{4.2}
\]

The inequality follows from (1.5) and `|r-s|<=4`. Common cone multiplication preserves nonnegative mixed-minor coefficients: apply Cauchy–Binet and take the coefficient of `ab`. Thus the argument uses a proved compatibility condition, not closure under arbitrary addition.

The monic families `u_N(z)` and `v_N(z)=u_N(z)+u_(N-1)(z)` are characteristic polynomials of finite path Jacobi matrices. For `u_N`, the diagonal is zero; for `v_N`, one endpoint diagonal is `-1`. Unit off-diagonal entries give spectra in `[-2,2]`; the tridiagonal recurrence gives simple eigenvalues and nonzero endpoint eigenvectors. Consequently their previous/next ratios are endpoint resolvents

\[
\frac{p_{N-1}(z)}{p_N(z)}=
\sum_i\frac{\lambda_i}{z-r_i},\quad
r_i\in[-2,2],\quad\lambda_i>0,\quad\sum_i\lambda_i=1.
\tag{4.3}
\]

This writes `Ap_N(t)+Bp_(N-1)(t)` as a positive mixture of `L_(r_i)` times all the other shifted factors. Each diagonal summand is a strict cone product, and pairs reduce to (4.2) after removing their common factors. All summands have the same degree and positive supported defects. Their positive squared-weight diagonal contributions therefore make the mixture strict.

For the prefixes, the exact identities are

\[
R_{2h}=u_hv_h,\qquad R_{2h+1}=u_hv_{h+1},
\]

\[
Z_{2h}=v_h(Au_h+Bu_{h-1}),\quad
Z_{2h+1}=u_h(Av_{h+1}+Bv_h).
\tag{4.4}
\]

Thus the active denominator has degree at most `N`; the outside factor restores a total of `N` spectral roots. For `N>=1` we have

\[
Z_N=\sum_{i\in I_N}\lambda_i Z_i,\qquad
Z_i=L_{r_i}\prod_{j\ne i}(t-r_j),
\tag{4.5}
\]

where each product has **exactly `N-1` propagators**, the active set satisfies `1<=|I_N|<=N`, and its positive weights sum to one. Roots from a canceled outside factor are not assigned spurious positive residues. At `N=1`, the single root is `-1` and `Z_1=L_(-1)`, so the formula includes the first required run length.

Equation (4.2) proves all-minor compatibility of the raw summands and strictness of every `Z_N`. The same argument proves raw strictness of the increment factor `Au_N+Bu_(N-1)`.

Under B1, the smoothed analogue of (4.2) follows from (3.4), so every `q_N` and `yZ_N` is strict. Under B2, two increment summands have a common root factor when `N>=3`; absorb `y` into one such factor and use the certified `y(t-r)`. Their diagonal terms use `yL_r`. The missing cases `N=0,1,2` are exactly `yA`, `yL_0`, and (3.5). For `yZ_N`, the outside factor in (4.4) contains a root factor for `N>=2`; the cases `N=0,1` use `yA,yL_(-1)`. This proves the needed `q_N` kernels without assuming `y` itself is in the cone.

Finally `y²` has half-row `(3,2,1)` and defects `(4,0,1)`, so it belongs to the cone. Every `Q_N=y²Z_N`, `N>=1`, is strict. Indeed, in `K_(y²)K_(Z_N)`, retain intermediate pair `(0,1)` for `n<=deg Z_N`, giving `delta_n(Q_N)>=4delta_n(Z_N)>0`. At the last two indices retain `(2,3)`; its first minor is `delta_2(y²)=1`, and (1.3) makes the second minor positive. Here `deg Z_N>=1` by (2.5)–(2.6). The extra statement that `yZ_N` is strict is useful but is not needed as a separate premise in the final proxy chain.

### 4.2 The unbounded mass estimate and the squared residues

Evaluate (4.5) at `x=2`. Every active summand satisfies

\[
\frac{Z_i(2)}{R_N(\tau)}
=A_*+\frac{B_*}{\tau-r_i}.
\]

The minimum and maximum possible values are exactly the numerator and denominator defining `rho` in (3.7). Comparing a summand with the weighted average proves

\[
Z_i(2)\ge\rho Z_N(2),\qquad
\sum_i\lambda_i^2\ge\frac1{|I_N|}\ge\frac1N.
\tag{4.6}
\]

Consider any one of the template minors in (3.8). In each product `Z_i`, retain the same intermediate column pair `(n,n+1)` after the template and after each propagator. Every principal propagator minor is at least `delta_0(t-r)` by (1.3). Cauchy–Binet and (3.6), (3.8) give

\[
\det K_{Z_i}[(i_n,i_n+1),(n,n+1)]
\ge\alpha_n\gamma^{N-1} Z_i(2).
\]

Every off-diagonal mixed contribution in the positive mixture is nonnegative by (4.2). Retaining the squared-weight diagonal terms and applying (4.6) yields

\[
\det K_{Z_N}[(i_n,i_n+1),(n,n+1)]
\ge\rho\alpha_n\frac{\gamma^{N-1}}N Z_N(2).
\tag{4.7}
\]

The ratio between successive values of `gamma^(N-1)/N` is `gamma N/(N+1)`. It is at least one exactly when `N>=1/(gamma-1)`. Therefore its global minimum over all positive integers is the finite value `eta` in (3.7), including the possible two-index tie. In particular (4.7) gives

\[
\boxed{\det K_{Z_N}[(i_n,i_n+1),(n,n+1)]
\ge\theta\alpha_n Z_N(2).}
\tag{4.8}
\]

The same proof starts with `y²L_r` and its defect minor. Common multiplication by the cone factor `y²` preserves mixed compatibility, so it proves

\[
\boxed{\delta_n(y^2Z_N)\ge\theta\beta_n Z_N(2).}
\tag{4.9}
\]

This is the point at which omitting the squares of the spectral weights would give an invalid stronger estimate. Equations (4.6)–(4.9) retain that loss explicitly and compensate for it through the trace rate.

### 4.3 The actual multiplier, including a non-cone fixed correction

Write `h_j=h_(y²Z_N)(j)` and `m_j=h_(M_0)(j)`. Expanding the quadratic defect gives

\[
\begin{aligned}
\delta_n(M_N)={}&9\delta_n(y^2Z_N)+\delta_n(M_0)\\
&+3\{2h_nm_n-h_{n-1}m_{n+1}-m_{n-1}h_{n+1}
-2h_{n+1}m_{n+1}+h_nm_{n+2}+m_nh_{n+2}\}.
\end{aligned}
\tag{4.10}
\]

All rows in the cross term are nonnegative, and each `h_j<=9Z_N(2)`. Thus

\[
\delta_n(M_N)\ge
(9\theta\beta_n-27\nu_n)Z_N(2)+\delta_n(M_0)
\tag{4.11}
\]

for the finitely many indices `0<=n<=m+1`. For `tau>2`, the positive Chebyshev values and their prefix sums imply `Z_N(2)>=Z_1(2)` for `N>=1`. If `delta_n(M_0)<0`, (3.12) makes the right side of (4.11) strictly positive already at that minimum mass; if the defect is nonnegative, strict positivity is immediate. This proves the claim without requiring `M_0` itself to lie in the folded cone.

For `n>=m+2`, the entire correction, including its polarization and base defect, vanishes. Therefore `delta_n(M_N)=9delta_n(y²Z_N)>0` throughout the remaining support. Consequently the **actual** multiplier `M_N` has a strict folded kernel for every `N>=1`.

### 4.4 Initial order propagates to the weak sides of the sandwich

The nonnegative row of `t` gives `1<=lr t`. Multiplication through the strict kernel of `q_N` gives `q_N<=lr tq_N`. At any ordered two columns, the exact gap recurrence implies

\[
W(q_N,q_{N+1})=W(q_N,tq_N)+W(q_{N-1},q_N).
\tag{4.12}
\]

Starting from `q_0<=lr q_1`, induction proves the entire time order. The fourth condition in (3.13) and this order put `P` below every `q_j`, `j>=1`. The endpoint identity (2.10), together with `P<=lr E_1`, then gives

\[
P\le_{\rm lr}E_N.
\tag{4.13}
\]

Also `q_N<=lr q_(N+1)` and `beta<=lr q_1<=lr q_(N+1)`. Applying bilinearity to the first identity in (2.10) therefore gives

\[
S_N\le_{\rm lr}JZ_N.
\tag{4.14}
\]

Only sums of rows below one fixed upper row, or above one fixed lower row, are used. There is no assertion that arbitrary sums preserve the folded cone.

### 4.5 The finite proxy correction controls every output index

For `0<=n<=e`, expand the two-row product `(H(J),H(V))K_(Z_N)` by Cauchy–Binet and retain the intermediate pair `(i_n,i_n+1)`. Gate (3.10) gives nonnegative omitted terms and a positive selected fixed minor. By (4.8),

\[
W_n(JZ_N,VZ_N)\ge\theta w_{i_n}\alpha_n Z_N(2).
\tag{4.15}
\]

Since the rows are nonnegative,

\[
W_n(JZ_N,K)
\ge-h_{JZ_N}(n+1)h_K(n)
\ge-J(2)Z_N(2)h_K(n).
\tag{4.16}
\]

The strict finite inequality (3.11) absorbs this correction. Hence

\[
W_n(JZ_N,VZ_N+K)>0\qquad(0\le n\le e).
\tag{4.17}
\]

For `n>e`, both correction entries vanish. Since `e>=d`, retain the fixed pair `(d,d+1)`. Its minor is `w_d>0`, and the remaining kernel minor is positive by (1.3) whenever

\[
0\le n-d\le\deg Z_N.
\]

That condition holds through `n=deg(JZ_N)=d+deg Z_N`, including the terminal index. We have proved the strict supported adjacent comparison

\[
JZ_N<_{\rm lr}VZ_N+K=PM_N.
\tag{4.18}
\]

The indices `d+1,...,e` are explicitly present in Gate C; discarding them would leave an actual gap whenever the old endpoint has positive degree `b`.

### 4.6 Return to the original strict target

Multiplying (4.13) by the now-proved TP2 kernel of `M_N` gives `PM_N<=lr E_NM_N=D_N`. Together with (4.14), (4.18),

\[
S_N\le_{\rm lr}JZ_N<_{\rm lr}PM_N\le_{\rm lr}D_N.
\tag{4.19}
\]

On the interior support of `S_N`, every relevant row entry is positive, so likelihood-ratio transitivity retains the strict middle comparison. At its final index, `h_(S_N)(deg S_N+1)=0` while `h_(D_N)(deg S_N+1)>0` by (2.12). Thus the terminal original determinant is the product of two positive entries. This proves (4.1) at every required index and completes the theorem.

## 5. A smaller optional form of the mass gate

Direct nonprincipal template certification is not always necessary. By (1.3), if

\[
\delta_j(L_r)\ge c_jL_r(2),
\]

then (3.8) holds with `alpha_n=c_(max(0,n-d))`. Thus the proxy uses only the **finite low band `j=0,...,b`**, because `e-d=b=deg Y`.

Furthermore `delta_j(y²L_r)>=4delta_j(L_r)` for `j<=deg L_r`, by retaining `(0,1)` in `K_(y²)K_(L_r)`. Therefore any available low-band constants give `beta_j=4c_j` on their supported range. Direct certification of `y²L_r` can provide substantially larger constants and also handles indices beyond the raw template support.

This explains the two successful proof styles: one uses a common lower bound for a few raw defects; the other certifies the required nonprincipal minors and smoothed defects directly. They are instances of the same propagation theorem.

## 6. How the two newly proved families instantiate the criterion

| Item | Prefix `R²` | Prefix `LR²` |
|---|---:|---:|
| `(a,b)=(deg X,deg Y)` | `(4,1)` | `(6,2)` |
| `(deg A,deg t,deg B)` | `(5,5,1)` | `(8,7,2)` |
| `(d,e,m)` | `(6,7,2)` | `(8,10,3)` |
| Smoothing mechanism actually certified | B1: separate `yH` strength | B2: `y(t-r)` and one fixed `q_2` |
| Raw midpoint strength `8h_B(0)` | `24` | `128` |
| Smoothed midpoint strength used | `56` | unnecessary |
| Certified trace rate `gamma` | `22` | `435` |
| Sufficient uniform choice of `theta` | `1/2` | `1/2` |
| Proxy mass input | raw `delta_0,delta_1` of `L_r` | eleven nonprincipal minors of `L_r` |
| Multiplier mass input | raw `delta_0,...,delta_3`, then multiply bound by `4` | five defects of `y²L_r` directly |
| Initial endpoint-to-gap comparison | stronger `P<=lr E_1<=lr q_1` | direct `P<=lr E_1` and `P<=lr q_1` |
| Prefix state `N=0` | separate exact original minors | separate exact original minors |

For `R²`, one can take `alpha_n=40000` for all eight correction indices and `beta_n=160000` for all four multiplier indices. Then `theta alpha_n=20000` and `theta beta_n=80000`. Its two exact proxy thresholds are `234515/18` and `7565/6`, both below `20000`; the multiplier inequalities have a large positive margin.

For `LR²`, the eleven `alpha_n` and five `beta_n` are explicitly listed in `../hour_quantum/lrrl_theorem.md`, with every scalar residual positive. Both families have `M_0` in the cone, so neither needs the negative-base-defect extension in (3.12).

The family proofs have mutually independent exact implementations and shared-session mathematical audits. Those audits verify their concrete hypotheses and target connection; they are not blind, external, or formal proof verification of this general theorem.

## 7. What is and is not reduced

For any supplied fixed prefix meeting the positive-seed and degree prerequisites, Gates A–E are a finite, reviewable sufficient certificate for all subsequent run lengths. A failed gate means this particular proof mechanism has not certified that prefix. It does not imply that the original Local TP2 statement is false there.

The remaining all-prefix problem is to prove these finite gates uniformly as the prefix changes, or to find a different uniform invariant that implies the same conclusion. The present theorem does not assume that arbitrary turns preserve seed compatibility, low-band mass margins, initial likelihood-ratio order, or the fixed `J,V` comparison.

No positive finite scan in `N` appears in the proof. The unbounded step is the Jacobi resolvent, the compatible mixed-minor argument, the exact squared-weight estimate, and the trace-rate minimum in (3.7).

## 8. Verification status and independent-review focus

The canonical formulas, residue support count, nonprincipal minor propagation, correction support, and terminal target connection are the common structure already audited in both concrete families. The additional generalizations introduced here are the exact mass ratio `rho`, the finite minimum `eta` for any `gamma>1`, and the allowance for finitely many negative defects of `M_0` in (3.12). They are proved in Sections 4.2–4.3 and should be checked explicitly when reviewing this theorem.

The criterion is deliberately sufficient. It is not claimed to be necessary, optimal, or a characterization of all positive canonical rays.

## 9. Exact finite certificate format

Every polynomial in the hypotheses has degree depending only on the fixed prefix. The half-row coefficients follow by finite binomial expansion of `x=q+q^-1`. Substitute `r=-2+4u`, and similarly for `s,c`.

- Defects of `t-r`, `L_r`, `yL_r`, `y(t-r)`, and `y²L_r` have parameter degree at most two.
- Every selected nonprincipal template minor in (3.8) also has degree at most two in its one parameter.
- Each raw or smoothed midpoint defect has degree at most two **in each** of the three independent parameters. Thus a degree-two tensor Bernstein array has 27 entries per output index.
- Coefficientwise domination and interval-support statements are finite polynomial inequalities as well. Their actual degree bounds can be used directly; degree elevation or a finite subdivision is allowed if a coarser Bernstein representation does not certify a true inequality.
- The trace mass, template mass, and strength subtractions do not increase these degree bounds. Gates D and E are rational or integer inequalities on fixed rows.

If `p(u)=sum_j a_j u^j` has degree at most `D`, its degree-`D` Bernstein coefficients are

\[
b_k=\sum_{j\le k}a_j\frac{\binom{k}{j}}{\binom{D}{j}}.
\]

Use the tensor product of this formula in several variables. Nonnegative coefficients certify a nonnegative polynomial over the closed box; strictly positive coefficients certify strict positivity there. A complete certificate records every supported output index and every coefficient, including zeros and boundary indices. Re-expanding the Bernstein basis to the original power polynomial checks the conversion independently. This is a finite continuum proof, distinct from evaluations on a finite grid.
