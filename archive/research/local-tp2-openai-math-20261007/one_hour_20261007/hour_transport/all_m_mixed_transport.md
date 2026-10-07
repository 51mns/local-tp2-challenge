# Uniform mixed comparison kernels at every L^m R² seed

**Status: PROVED_INTERNAL.** This proves a new family of comparison-kernel
theorems for every integer `m>=0`, with complete finite certificates and an
unbounded analytic tail. It supplies single-block and midpoint compatibility
for subsequent left runs of arbitrary length. The last comparison returning
these auxiliary kernels to the original Local TP2 determinant is a separate
obligation; this note does not claim the full canonical-tree conjecture.

The inputs are the proved and audited folded-kernel, multiplicative-strength,
and normalized-product theorems in the original AIMath research directory,
the new trace theorem `all_m_trace_transport.md`, and the new uniform seed
theorem `../hour_quantum/UNIFORM_SEED_STRENGTH.md`.

## 1. Definitions and statement

Write `x=q+q^-1`, `y=x+1`, and

\[
u_m=U_m(x+3/2),\quad T_m=\sum_{j=0}^m u_j,\quad T_{-1}=0,
\quad g_m=1+yT_m,\quad t_m=3yg_m-x.
\]

For the canonical state at `L^mR²`, put

\[
a_X=T_{m+1}(t_m+1)+T_{m-1},\qquad X=1+ya_X,
\]

\[
A=t_ma_X-u_m,\qquad B=u_{m+1},\qquad \tau=3yX-x.
\tag{1}
\]

Here `X` is its fixed left endpoint, while `A` and `B` are exactly the two
gap seeds for the subsequent left run. Their derivation from the original
mutations is in the uniform seed theorem. In particular

\[
\deg A=3m+5,\qquad \deg B=m+1,\qquad \deg\tau=2m+5.
\tag{2}
\]

For a polynomial `P`, denote its Fourier half-row by
`h_n=H(P)_n=[q^n]P(q+q^-1)`, reflecting negative indices and extending by
zero above the support. Let

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2},
\qquad \eta(h)=\min_n\frac{\delta_n(h)}{h_n^2}.
\]

As usual, `lambda`-strong means `delta_n(h)>=lambda h_n` throughout its
positive interval support. Put

\[
\kappa_m=\begin{cases}18,&m=0,\\
18\,4^m-18\,2^m-11,&m\ge1,
\end{cases}
\qquad c_0=\frac1{400000000},\quad\sigma=\frac{59}{100}.
\tag{3}
\]

For any real `r,s,c in [-2,2]` define

\[
L_r=A(\tau-r)+B,
\qquad H_{rsc}=A(\tau-r)(\tau-s)+B(\tau-c).
\tag{4}
\]

**Theorem.** For every integer `m>=0`, uniformly on the entire independent
parameter cube `[-2,2]^3`,

\[
L_r,\ yL_r\quad\hbox{are}\quad
\lambda_L=\frac9{128}8^m\kappa_m\hbox{-strong},
\tag{5}
\]

\[
H_{rsc},\ yH_{rsc}\quad\hbox{are}\quad
\lambda_H=\max\left\{\frac9{128}8^m\kappa_m^2,
8H(yB)_0\right\}\hbox{-strong}.
\tag{6}
\]

All four polynomials have dense positive ordinary coefficients. They also
satisfy the uniform normalized bounds

\[
\boxed{\eta(L_r),\eta(yL_r)\ge
\frac{c_0^5\sigma^{5m+2}}{65536(m+3)^4},}
\tag{7}
\]

\[
\boxed{\eta(H_{rsc}),\eta(yH_{rsc})\ge
\frac{c_0^7\sigma^{7m+3}}{4194304(m+3)^6}.}
\tag{8}
\]

The normalized trace bound used below holds at every initial index as well:

\[
\boxed{\eta(\tau-r)\ge
\frac{c_0^2\sigma^{2m+1}}{16(m+3)}.}
\tag{9}
\]

The constants are deliberately conservative. Their role is to permit
further uniform comparisons without assuming closure under arbitrary sums.

## 2. Normalized trace retention

The exact identity from the trace theorem is

\[
\tau=t_mt_{m+1}-y(x+3).
\tag{10}
\]

Its degree-two subtraction lemma gives, with `h=H(t_mt_(m+1))`,

\[
\delta_n\bigl(H(\tau-r)\bigr)\ge\delta_n(h)-15h_n.
\tag{11}
\]

Indeed the displayed low-index corrections in that lemma are bounded below
by `-15h_n`, and all higher corrections are nonnegative. The product has
strength `(3·2^m-2)(6·2^m-2)>=40` for `m>=1`. Hence (11) retains at least
half of its defect. Subtraction also decreases every positive half-row
entry, so it retains at least half of its normalized defect.

For `m>=21`, the previously audited shifted-trace theorem in
`fulltree_oneturn_normalized_tail.md`, Section 3, gives

\[
\eta(t_m)\ge c_0\sigma^m/2,\qquad
\eta(t_{m+1})\ge c_0\sigma^{m+1}/2.
\]

The normalized product theorem is

\[
\eta(FG)\ge
\frac{\eta(F)\eta(G)}{2(\min(\deg F,\deg G)+1)}.
\tag{12}
\]

Since `deg t_m=m+2`, its application followed by half-retention proves (9)
for `m>=21`.

There is a short exact scalar bridge for `0<=m<=20`. The recurrence at
`x=2` gives `u_j(2)<=7^j`, and therefore

\[
t_j(2)=27T_j(2)+7\le5\,7^{j+1}.
\]

From (10), `(tau-r)(2)<=25·7^(2m+3)`. The trace theorem supplies strength
`kappa_m`, so decrease of its half-row implies

\[
\eta(\tau-r)\ge\frac{\kappa_m}{25\,7^{2m+3}}.
\tag{13}
\]

The verifier checks the 21 exact rational inequalities comparing (13) with
(9). Every one is strict; even at `m=20` the ratio exceeds 53,009.
This completes (9) for all `m` and all real `r` in the interval.

## 3. Dominant-product margins

The new uniform seed theorem gives

\[
A,yA\ \hbox{are}\ \frac9{32}8^m\hbox{-strong},
\qquad
\eta(A),\eta(yA)\ge
\frac{c_0^3\sigma^{3m+1}}{128(m+3)^2}
\tag{14}
\]

for every `m>=0`. The new trace theorem gives `kappa_m` strength of every
factor `tau-r`. By multiplicative strength, the dominant single and double
products

\[
F_L=A(\tau-r),\quad yF_L,
\qquad F_H=A(\tau-r)(\tau-s),\quad yF_H
\]

have respective strengths

\[
\mu_L=\frac9{32}8^m\kappa_m,
\qquad\mu_H=\frac9{32}8^m\kappa_m^2.
\tag{15}
\]

Each normalized-product denominator is at most
`2(deg tau+1)=4(m+3)`. Combining (9), (12), and (14) yields

\[
\eta(F_L),\eta(yF_L)\ge E_L(m):=
\frac{c_0^5\sigma^{5m+2}}{8192(m+3)^4},
\tag{16}
\]

\[
\eta(F_H),\eta(yF_H)\ge E_H(m):=
\frac{c_0^7\sigma^{7m+3}}{524288(m+3)^6}.
\tag{17}
\]

The bound `E_L>=E_H` is immediate from their ratio.

## 4. The correction is much smaller at this second-turn seed

Write `rho_m=H(t_m)_0` and `theta_m=H(tau)_0`. The inner Chebyshev
recurrence gives `u_m<=u_(m+1)=B` in ordinary coefficients. Also

\[
a_X\ge t_m B.
\]

Consequently, using the central convolution term,

\[
H(A)=H(t_ma_X-u_m)
\ge H(t_m^2B-B)
\ge(\rho_m^2-1)H(B)
\tag{18}
\]

coefficientwise. All inequalities remain true after multiplication by `y`.
Every shifted trace has central coefficient at least `theta_m-2`. In
addition `theta_m>=3`, so for every `s,c in [-2,2]`,

\[
0\le H(\tau-c)\le5H(\tau-s)
\tag{19}
\]

coefficientwise: only the central entry changes with the shift, and
`(theta_m+2)/(theta_m-2)<=5`. Therefore the corrections `G=B` and
`G=B(tau-c)`, respectively, obey

\[
0\le H(G)_n\le
\frac5{(\rho_m^2-1)(\theta_m-2)}H(F)_n
\tag{20}
\]

for the corresponding dominant product `F`; the same is true for `yG,yF`.

The established central-mass estimate in
`fulltree_oneturn_normalized_tail.md`, Section 4, is

\[
\rho_m\ge\alpha_m:=\frac{27\,6^m}{2m+5}.
\tag{21}
\]

Equation (10) gives `theta_m>=rho_m rho_(m+1)-5`. For `m>=1`,
`alpha_m^2>=2` and `alpha_m alpha_(m+1)>=14`, hence

\[
(\rho_m^2-1)(\theta_m-2)
\ge\frac14\alpha_m^3\alpha_{m+1}.
\]

Thus a single bound applicable to all four corrections is

\[
\boxed{\epsilon_m=
\frac{20(2m+5)^3(2m+7)}{27^4\,6^{4m+1}},
\qquad 0\le H(G)\le\epsilon_m H(F).}
\tag{22}
\]

This denominator contains the square of the old trace mass and the mass
of the new trace. That extra decay is what makes a short finite bridge
possible here.

## 5. Exact analytic tail starting at m=54

For a folded-cone dominant product `F` and a nonnegative correction
`G<=epsilon F` coefficientwise, the audited perturbation inequality is

\[
\delta_n(F+G)\ge\delta_n(F)
-(4\epsilon+2\epsilon^2)H(F)_n^2.
\tag{23}
\]

It follows directly by expanding the defect, dropping positive terms, and
using decrease and log-concavity of `H(F)`. The argument includes the
reflected index zero and the upper support boundary.

The verifier uses exact rational arithmetic to establish

\[
E_H(54)>12\epsilon_{54},\qquad \epsilon_{54}<1.
\tag{24}
\]

The consecutive ratio of `E_H(m)/epsilon_m` is

\[
6^4\sigma^7
\left(\frac{m+3}{m+4}\right)^6
\left(\frac{2m+5}{2m+7}\right)^3
\frac{2m+7}{2m+9}.
\tag{25}
\]

Every nonconstant factor increases with `m`, and the ratio exceeds 27 at
54. Hence (24) propagates to all `m>=54`. Also `epsilon_m` decreases on
that range. Since `E_L>=E_H`, equation (23) retains at least half of every
dominant defect. As `H(F+G)<=2H(F)`, the sum retains at least one quarter
of its strength and one eighth of its normalized defect. This proves
(5), (7), (8), and the first component of (6) throughout the infinite tail.

For the second component of (6),

\[
8H(yB)_0\le24\,7^{m+1}.
\]

For every `m>=2`, `kappa_m>=9·4^m`. Therefore

\[
\frac9{128}8^m\kappa_m^2
\ge\frac{729}{128}128^m>24\,7^{m+1}.
\tag{26}
\]

The last inequality holds already at 2 and propagates by the ratio `128/7`.
Thus the tail supplies the relative-minor strength needed in (6).

## 6. Complete finite bridge on continuous parameter boxes

`verify_uniform_mixed_transport.py` reconstructs `u_m,T_m,t_m,a_X,A,B,tau`
in the ordinary `x` basis for every integer `0<=m<=53`. It verifies the
trace identity (10) independently in that basis. It then sets

\[
r=-2+4u,\quad s=-2+4v,\quad c=-2+4w,
\qquad (u,v,w)\in[0,1]^3.
\]

Every supported row entry of `L` is affine in `u`. Every row entry of `H`
has monomials among `1,u,v,uv,w`. Accordingly every defect margin

\[
\delta_n(H(P))-\lambda H(P)_n
\]

has degree at most two on each active parameter axis. The verifier computes
all three univariate or all 27 tensor Bernstein coefficients, clearing the
denominator `128·2^number_of_axes`. Every coefficient is strictly positive.
For every margin it independently expands those Bernstein coefficients
back into the power basis and requires exact equality before accepting
their signs.

There are **216 full parameter cases and 635,688 strictly positive integer
Bernstein coefficients**. These certify the entire intervals/cubes, not
just a parameter grid. The strength used for `H,yH` is the maximum in (6),
including the small `m=0` case where its relative-minor term is larger.

The same certificates supply the finite part of (7)–(8). For a supported
index `n`, let `b_min>0` be the minimum scaled Bernstein coefficient of the
strength margin. Every entry `H(P)_n` decreases as each of `r,s,c` increases,
so its maximum on the cube is its value `h_max` at all parameters `-2`.
Consequently

\[
\eta_n(P)\ge
\frac{b_{\min}}{128\,2^{\#\mathrm{axes}}h_{\max}^2}.
\tag{27}
\]

The verifier checks (27) against (7) or (8) at every supported index,
giving **37,368 additional exact normalized certificates**. Ordinary
coefficient positivity follows directly from the positive seeds and the
positive factors `tau-r`.

The result file `uniform_mixed_transport_results.json` records per-case
strengths, supported degrees, minima at every supported index, ordered
coefficient SHA-256 digests, all exact scalar gates, and counts. The script
regenerates every coefficient; it depends only on the Python standard
library. No input from a bounded tree scan is used to infer an infinite
claim.

## 7. Jacobi compatibility and arbitrary outer length

Let

\[
F=A(\tau-r)(\tau-s)+B(\tau-s),\qquad
G=A(\tau-r)(\tau-s)+B(\tau-r).
\]

Their midpoint is `H_(r,s,(r+s)/2)`, and `F-G=(r-s)B`. Since (6) gives
strength at least `8H(B)_0`, the established all-minor relative-strength
theorem yields

\[
\det K_H\ge4\det K_B.
\]

Its coefficient domination hypothesis follows from positive coefficients
of every shifted trace; the reference row `B` is decreasing by the
Chebyshev-ray theorem. The same proof with `yH,yB` uses the stronger
`8H(yB)_0` already built into (6). For every ordered kernel minor,

\[
\operatorname{mixed}(K_F,K_G)
=2\det K_H-\frac{(r-s)^2}{2}\det K_B\ge0.
\tag{28}
\]

If the reference minor is negative the assertion is immediate; otherwise
use `(r-s)^2<=16`. Thus the unsmoothed and smoothed pairs are compatible.

For `p_N(t)=U_N(t/2)` or `U_N(t/2)+U_(N-1)(t/2)`, the established Jacobi
resolvent is

\[
\frac{p_{N-1}(t)}{p_N(t)}
=\sum_i\frac{\lambda_i}{t-r_i},\qquad
\lambda_i>0,\quad\sum_i\lambda_i=1,\quad r_i\in[-2,2].
\]

It expresses `A p_N(tau)+B p_(N-1)(tau)` as the weighted sum of

\[
[A(\tau-r_i)+B]\prod_{j\ne i}(\tau-r_j).
\]

Every summand is a strong folded-cone product by (5), and every pair is
compatible by (28) followed by common-factor Cauchy–Binet. Every supported
defect of the sum is strictly positive because the diagonal terms carry
positive squared residue weights. The smoothed statement uses `yL` and
the smoothed compatibility already proved; it does not assert that `y`
alone belongs to the cone. At `N=0`, use the uniform seed theorem for
`A,yA`.

It follows, for every `m,N>=0`, that

\[
M_N=A\,U_N(\tau/2)+B\,U_{N-1}(\tau/2)
\quad\hbox{and}\quad yM_N
\]

have strictly positive supported folded defects. The existing exact prefix
factorizations in `general_one_turn_kernel_theorem.md` similarly give the
same statement for

\[
Z_N=A\sum_{j=0}^N U_j(\tau/2)
 +B\sum_{j=0}^{N-1}U_j(\tau/2)
\quad\hbox{and}\quad yZ_N.
\]

This is the new all-initial-index mixed-kernel closure. It is a forward
comparison theorem in the original Fourier half-row convention, without
factorial renormalization or inversion of a smoothing kernel.

## 8. Reproduction and scope

Run from the parent of `hour_transport`:

```bash
python hour_transport/verify_uniform_mixed_transport.py
```

The exact input proofs are the original `mixed_kernel_strong_cone.md`,
`mixed_kernel_all_minor_strength.md`, `fulltree_oneturn_normalized_tail.md`,
`recovery_oneturn_closure.md`, and the two new trace/seed notes cited at the
start. The finite verifier reconstructs its own ordinary polynomials and
does not import code from those dependencies.

What is proved here is every single/midpoint kernel and its compatibility
for all `L^mR²` initial seeds and arbitrary following length. Returning that
closure to the original `F_n(S,D)>0` still requires the initial comparison
and proxy/multiplier argument appropriate to the new seeds. Those final
steps are not silently assumed by this theorem.
