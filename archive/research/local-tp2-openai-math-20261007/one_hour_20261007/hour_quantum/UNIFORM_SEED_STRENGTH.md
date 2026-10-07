# Uniform seed strength after the prefix L^m R²

**Status: PROVED_INTERNAL; the new algebra and inherited premises have
received a shared-session independent review, and every finite gate has
been reproduced by a second exact implementation.** This proves
auxiliary seed theorems for **every** initial
left-run length `m>=0`. It supplies a missing structural input toward
all paths `L^mR²L^ell`; it does not by itself prove Local TP2 on that
two-parameter family or on the full tree.

Let

\[
x=q+q^{-1},\quad y=x+1,\quad z=2x+3,
\]

\[
u_m=U_m(z/2),\quad T_m=\sum_{j=0}^m u_j,\quad T_{-1}=0,
\quad g_m=1+yT_m.
\]

In particular `g_0=x+2`; this fixes the indexing. Put

\[
t_m=3yg_m-x,\qquad
a_X=T_{m+1}(t_m+1)+T_{m-1},\qquad X=1+ya_X,
\tag{1}
\]

and define the new two seeds

\[
A_m=t_ma_X-u_m,\qquad B_m=u_{m+1}.
\tag{2}
\]

Write `H(P)_n=[q^n]P(q+q^-1)`, with reflection at negative indices
and zero extension above the support, and

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}.
\]

A row is `lambda`-strong if `delta_n(h)>=lambda h_n` throughout
its positive support. Its normalized defect is

\[
\eta(h)=\min_{0\le n\le\deg P}\frac{\delta_n(h)}{h_n^2}.
\]

Set the previously established constants

\[
c_0=\frac1{400000000},\qquad \sigma=\frac{59}{100}.
\]

## Theorem

For every integer `m>=0`, the canonical seeds in (2) satisfy

\[
\boxed{A_m\text{ and }yA_m\text{ are }
\frac9{32}8^m\text{-strong}.}
\tag{3}
\]

They have dense positive ordinary coefficients. The reference seeds
`B_m` and `yB_m` are in the folded cone with positive supported
defects. In addition,

\[
\boxed{\eta(a_X),\eta(ya_X)
\ge\frac{c_0^2\sigma^{2m+1}}{16(m+3)}}
\tag{4}
\]

and

\[
\boxed{\eta(A_m),\eta(yA_m)
\ge\frac{c_0^3\sigma^{3m+1}}{128(m+3)^2}.}
\tag{5}
\]

All four displayed bounds include their finite initial cases and an
unbounded analytic tail. The proof introduces no unproved global
mutation-preservation premise.

## 1. Exact identification with the original mutations

The canonical state at `L^m` has endpoints `1,g_m` and center
`g_(m+1)`. Let `Y=g_m`. The first and second right centers satisfy

\[
X=t_mg_{m+1}-xY-1,\qquad C_0=t_mX-xY-g_{m+1}.
\tag{6}
\]

The inner prefix recurrence is

\[
T_{m+1}=zT_m-T_{m-1}+1.
\tag{7}
\]

Since `t_m-xY-2=y(1+zT_m)`, equations (6)–(7) give

\[
\frac{X-1}{y}=t_mT_{m+1}+T_{m+1}+T_{m-1}=a_X.
\]

Likewise

\[
\frac{t_m-xY-g_{m+1}-Y}{y}
=1+2yT_m-T_{m+1}=-u_m.
\]

Consequently

\[
\frac{C_0-Y}{y}=t_ma_X-u_m=A_m,
\qquad
\frac{g_{m+1}-Y}{y}=u_{m+1}=B_m.
\tag{8}
\]

These are exactly the seeds for subsequent left iteration from the
state `L^mR²`. Their degrees are

\[
\deg t_m=m+2,\quad\deg a_X=2m+3,\quad
\deg A_m=3m+5,\quad\deg B_m=m+1.
\]

The independent mutation reconstruction in `uniform_seed_strength.py`
confirms (8) for every finite-bridge index. In particular

\[
A_0=167+500x+620x^2+398x^3+132x^4+18x^5,
\]

and `A_1` is the degree-eight seed used in the separately proved
`LR²L^ell` theorem. The identities (6)–(8), rather than the finite
comparison, establish the correspondence for all `m`.

All `u_j` have dense positive ordinary coefficients. One direct
induction uses `u_(j+1)-u_j=(z-2)u_j+(u_j-u_(j-1))>=0`.
Hence `a_X>=T_(m+1)>=u_m` coefficientwise. Every coefficient of
`t_m-1` is positive, including its constant coefficient. Therefore

\[
A_m=(t_m-1)a_X+(a_X-u_m)
\]

has dense positive ordinary coefficients, independently of any folded
kernel conclusion. The same holds after multiplying by `y`.

## 2. A subtraction lemma for strong folded rows

**Lemma.** Let `h=H(F)` be lambda-strong and let `p=H(P)` belong to
the folded cone. Assume that `F-P` has positive interval support,
`H(F-P)>=0`, and `lambda>=4p_0`. Then `F-P` is
`(lambda-4p_0)`-strong. More precisely,

\[
\delta_n(F-P)\ge(\lambda-4p_0)h_n+\delta_n(P).
\tag{9}
\]

If `lambda>=8p_0`, then also

\[
\delta_n(F-P)\ge\tfrac12\delta_n(F),\qquad
\eta(F-P)\ge\tfrac12\eta(F).
\tag{10}
\]

**Proof.** Folded cone rows are nonnegative and nonincreasing. The
polarization is

\[
\begin{aligned}
\operatorname{Pol}_n(h,p)
={}&2h_np_n-h_{n-1}p_{n+1}-p_{n-1}h_{n+1}
-2h_{n+1}p_{n+1}\\
&+h_np_{n+2}+p_nh_{n+2}.
\end{aligned}
\]

Discard its three nonpositive terms. Since `p_n,p_(n+2)<=p_0` and
`h_(n+2)<=h_n`, the remaining terms total at most `4p_0h_n`.
This argument also applies at `n=0` with reflection, and at the upper
support boundary with zero extension. Thus

\[
\delta_n(F-P)=\delta_n(F)-\operatorname{Pol}_n(h,p)+\delta_n(P)
\ge\delta_n(F)-4p_0h_n+\delta_n(P).
\]

Because `P` is in the cone, `delta_n(P)>=0`; this proves (9). Also
`H(F-P)<=h`, which converts (9) to the asserted strength. If
`lambda>=8p_0`, then
`4p_0h_n<=delta_n(F)/2`, giving (10). Its normalized assertion uses
`0<H(F-P)_n<=h_n` on the supported range. ∎

The lemma is specific to subtraction of a cone row and does not
assert any general closure under addition or arbitrary mutation.

## 3. Uniform strength from a small analytic tail

The established one-turn theorem `recovery_oneturn_closure.md`,
Sections 3–5, gives, for every `m>=1` and every `r in [-2,2]`,

\[
T_{m+1}(t_m-r)+T_{m-1}
\quad\text{and its product with }y
\quad\text{are }3\,2^{2m-3}\text{-strong}.
\]

Specializing at `r=-1` yields the same strengths for `a_X,ya_X`.
The sharp trace theorem gives `t_m` strength `3·2^(m-1)`.
By the established multiplicative strength theorem, both

\[
F=t_ma_X,\qquad yF=t_m(ya_X)
\]

have strength

\[
\lambda_F=(3\,2^{m-1})(3\,2^{2m-3})
=\frac9{16}8^m.
\tag{11}
\]

The established Chebyshev-ray theorem gives cone membership of
`u_m` for every `m>=0`, and of `yu_m` for every `m>=1`.
At `x=2`, the inner recurrence has multiplier 7; its positivity gives
`u_m(2)<=7^m`. Therefore both references have central half-row entry

\[
p_0\le3\cdot7^m.
\tag{12}
\]

The exact scalar inequality

\[
9\cdot8^{29}>384\cdot7^{29}
\]

and the ratio `8/7>1` imply
`lambda_F>24·7^m>=8p_0` for every `m>=29`. Apply the subtraction
lemma to `(F,u_m)` and `(yF,yu_m)`. It gives

\[
\delta_n(A_m)>\tfrac12\lambda_FH(A_m)_n,
\qquad
\delta_n(yA_m)>\tfrac12\lambda_FH(yA_m)_n.
\]

This proves (3) for all `m>=29`.

For `m=0,...,28`, `uniform_seed_strength.py` constructs the actual
canonical seeds from scratch and verifies every integer margin

\[
32\delta_n(H(P))-9\cdot8^m H(P)_n>0,
\qquad P=A_m,yA_m.
\]

There are **2,813** such supported margins, all positive; the smallest
is `10,206`. The complete half-rows and integer margin lists are in
`uniform_seed_strength_certificates.json`. This finite bridge includes
`m=0`, where the reference `yu_0=y` would not satisfy the subtraction
lemma's cone hypothesis. Thus no invalid use of that reference is
made.

Finally `B_m=u_(m+1)` and `yB_m=yu_(m+1)` have positive supported
defects by the same existing Chebyshev-ray results, for every `m>=0`.

## 4. Sharper normalized defects for a_X and ya_X

For the analytic range `m>=391`, the existing proof in
`recovery_oneturn_closure.md`, Section 3, supplies the following inputs.
Let `G=T_(m+1)(t_m+1)` and `P=T_(m-1)`, or use both polynomials
multiplied by `y`. Their dominant product has

\[
\eta(G)\ge E_m:=\frac{c_0^2\sigma^{2m+1}}{4(m+3)},
\]

and the actual sum satisfies

\[
\delta_n(G+P)\ge\tfrac12\delta_n(G),\qquad
0\le H(P)_n\le\epsilon_m H(G)_n,
\quad\epsilon_m=\frac{2m+5}{9\,6^m}.
\tag{13}
\]

The stronger normalization here uses the actual correction bound,
rather than replacing `1+epsilon_m` by 2. Indeed `epsilon_1=7/54<1/3`
and its consecutive ratio is less than 1, so `epsilon_m<1/3`.
Equation (13) gives

\[
\eta(G+P)
\ge\frac{\eta(G)}{2(1+\epsilon_m)^2}
>\frac14\eta(G)\ge\frac14E_m.
\]

These are precisely the two assertions (4). This improves the
coarser denominator 32 to denominator 16.

For `m=0,...,390`, `uniform_ax_normalized.py` independently constructs
the full symmetric Laurent half-rows by the inner recurrence and exact
positive convolution. It checks every supported integer inequality

\[
400000000^2\,100^{2m+1}\,16(m+3)\,\delta_n(H(P))
>59^{2m+1}H(P)_n^2,
\quad P=a_X,ya_X.
\tag{14}
\]

There are **308,499** positive exact margins. The output
`uniform_ax_normalized_certificates.json` records each case's support,
minimum exact integer margin, minimizing index, actual minimum eta,
and full-row and full-margin SHA-256 digests. The deterministic script
regenerates every comparison. Its convolution algorithm packs positive
coefficients into an integer base exceeding the rigorous maximum
coefficient of the product, so carries cannot occur. Only standard
Python integers are used, with no floating-point arithmetic or external
numeric library.

The finite bridge and (13) prove (4) for every `m>=0`.

### Separate exact reconstruction of the finite bridges

`audit_uniform_seed_finite.py` imports neither generating implementation.
It constructs each actual `L^m` state and its right mutation in the
ordinary `x` basis, using polynomial Karatsuba multiplication, then
computes Fourier half-rows by Horner iteration of multiplication by
`q+q^-1`. This differs in both the canonical construction and coefficient
basis from the primary normalized generator's inner Laurent recurrence
and packed symmetric convolution.

The second implementation reproduces all **308,499** normalized
comparisons, matching every full-half-row and full-margin digest. For
the new seeds it reproduces all **2,813** strength margins and all
**2,813** normalized margins, comparing the complete saved integer lists.
The original canonical seed data and the exact `m=29` scalar gate also
agree. Its result is saved in `audit_uniform_seed_finite_results.json`.
This is a second implementation within the same research session,
not external or formal proof-assistant verification.

## 5. Normalized defects for the actual new seeds

For `m>=29`, the old normalized shifted-trace estimate, valid already
for `m>=21`, is

\[
\eta(t_m)\ge\frac12c_0\sigma^m.
\]

The established normalized product inequality is

\[
\eta(PQ)\ge
\frac{\eta(P)\eta(Q)}{2(\min(\deg P,\deg Q)+1)}.
\]

Here `deg t_m=m+2`, while `deg a_X=2m+3` and `deg(ya_X)=2m+4`.
Combining this product inequality with (4) gives, for both `F=t_ma_X`
and `yF`,

\[
\eta(F),\eta(yF)
\ge\frac{c_0^3\sigma^{3m+1}}{64(m+3)^2}.
\]

The same verified scalar tail gate ensures `lambda_F>=8p_0`, so
the normalized subtraction conclusion (10) loses at most one half.
This proves (5) for every `m>=29`, with denominator **128**.

The finite script `uniform_seed_strength.py` additionally checks (5)
for `m=0,...,28` by integer cross multiplication. Every one of those
2,813 normalized margins is saved in full alongside the strength
margins. Thus (5) holds for all `m>=0`.

## Scope and reusable conclusion

The new subtraction lemma turns already proved one-turn strengths
into a uniform second-turn seed theorem. Both the strength and
normalized-defect bounds grow or decay at explicit exponential rates,
with every finite initial case accounted for. The constants do not
depend on the later run length `ell`.

To obtain all-`m` Local TP2 on `L^mR²L^ell`, one still needs the
corresponding shifted-trace, single-template, midpoint-compatibility,
multiplier, and strict proxy comparison inputs. This note supplies
`A_m,yA_m` and their normalized bounds; it does not identify those
remaining obligations with an already proved full-tree statement.
