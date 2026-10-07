# Uniform trace transport at every endpoint reached by L^m R

**Status: PROVED_INTERNAL, conditional only on previously proved and audited
prefix-strength theorems explicitly cited below.** This supplies a new
all-m family of positive comparison kernels. It does not, by itself, prove
Local TP2 on all `L^m R^2 L^ell`, because their coupled initial-gap and
midpoint comparisons are separate obligations.

Date: 2026-10-07. Arithmetic and symbolic identities are independently
reconstructed by `verify_trace_transport.py` using Python integers and
`fractions.Fraction`; no numerical root approximations or bounded tree scan
is used to infer the all-m result.

## 1. The theorem

Put

\[
x=q+q^{-1},\quad y=x+1,\quad
T_m=\sum_{j=0}^m U_j(x+3/2),\quad g_m=1+yT_m,
\quad t_P=3yP-x.
\]

Then `g_0=x+2`, `g_1=2x^2+6x+5`. The canonical state at `L^m` has
endpoints 1 and g_m, and center g_(m+1). Define its right child

\[
X_m=3y g_mg_{m+1}-x(g_m+g_{m+1})-1.
\]

Thus X_m is exactly the center at the word `L^m R`; it is the fixed
endpoint appearing in the subsequent `L^m R^2 L^ell` run.

For a polynomial P write h_n=H(P)_n=[q^n]P(q+q^{-1}), with reflection
at negative indices and zeros above its degree. Set

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2}.
\]

A positive finite half-row is called lambda-strong if
`delta_n(h)>=lambda h_n` throughout its support. Its folded multiplication
kernel is then TP2. The existing product theorem says that strengths
multiply under polynomial multiplication.

**Theorem.** For every integer m>=0 and every real r in [-2,2],

\[
t_{X_m}-r\text{ is }A_m\text{-strong},\qquad
y(t_{X_m}-r)\text{ is }B_m\text{-strong},
\tag{1}
\]

where the explicit strictly positive constants are

\[
A_m=\begin{cases}
18,&m=0,\\
18\,4^m-18\,2^m-11,&m\ge1,
\end{cases}
\qquad
B_m=\begin{cases}
18,&m=0,\\
72,&m=1,\\
9\,4^m-21\,2^m-25,&m\ge2.
\end{cases}
\tag{2}
\]

For example A_1=25 and B_2=35. These are certified lower bounds;
optimality is not claimed for the infinite formulas. The three small-m
certificates use the optimal terminal leading-coefficient bounds.

The proof combines a fixed-degree correction identity with growing
strength. The correction degree does not grow with m, which distinguishes
this result from the previously falsified coarse subtraction invariant on
long arbitrary endpoint runs.

## 2. Exact trace factorization

Expanding the definition of t_P and the actual canonical mutation gives

\[
\boxed{t_{X_m}=t_{g_m}t_{g_{m+1}}-y(x+3).}
\tag{3}
\]

Indeed the product minus the new trace is
`x^2+3y+x=x^2+4x+3`. This is an identity for every m, without a
positivity assumption. The verifier also checks (3) against an independently
reconstructed canonical root and first left state used for the exceptional
certificates.

Let F=t_(g_m)t_(g_(m+1)). Subtracting r changes the correction's Fourier
half-row to

\[
H(y(x+3)+r)=(c,4,1),\qquad c=5+r\in[3,7].
\tag{4}
\]

For the smoothed trace, the correction row is

\[
H\bigl(y[y(x+3)+r]\bigr)=(c+8,c+5,5,1).
\tag{5}
\]

These bounded rows are the only subtractions made in the proof.

## 3. General fixed-degree subtraction lemmas

We first record two positive comparison-kernel lemmas independent of the
canonical recurrence.

If h is lambda-strong with lambda>0, then h is nonincreasing and each
supported entry is at least lambda. For completeness, telescoping delta
gives nonnegative log-concavity defects Delta. Symmetry gives h_0>=h_1,
and log-concavity propagates the decrease. At the terminal index d,
`delta_d=h_d^2>=lambda h_d`, hence h_d>=lambda.

### Lemma 3.1: degree-two correction costs at most 15 in strength

Suppose h is L-strong, has positive support 0 through d with d>=3, and
L>15. For any c in [3,7] put

`b=h-(c,4,1,0,...)`.

Then b has positive interval support and is `(L-15)`-strong.

**Proof.** Positivity follows from h_n>=L>15. Direct expansion gives

\[
\begin{aligned}
\delta_0(b)-\delta_0(h)
 &=-(2c+1)h_0-ch_2+16h_1+c^2+c-32,\\
\delta_1(b)-\delta_1(h)
 &=-8h_1+h_0+(c+2)h_2-4h_3+15-c,\\
\delta_2(b)-\delta_2(h)
 &=-2h_2+4h_3-h_4+1,\\
\delta_3(b)-\delta_3(h)&=h_4,\\
\delta_n(b)&=\delta_n(h)\quad(n\ge4).
\end{aligned}
\tag{6}
\]

The first right side is decreasing in c, because its derivative is
`-2h_0-h_2+2c+1<0`. At c=7, use h_2<=h_1. At the other indices use
the same decrease to obtain

\[
\begin{aligned}
\delta_0(b)&\ge(L-15)h_0+9h_1+24,\\
\delta_1(b)&\ge(L-8)h_1+h_0+h_2+8,\\
\delta_2(b)&\ge(L-2)h_2+3h_3+1,\\
\delta_3(b)&\ge Lh_3+h_4,\\
\delta_n(b)&\ge Lh_n\quad(n\ge4).
\end{aligned}
\tag{7}
\]

Each bound is at least `(L-15)b_n`; missing entries are zero, so the
same formulas cover every support boundary. QED.

### Lemma 3.2: smoothed degree-three correction costs at most 35

Suppose h is L-strong with positive support 0 through d, d>=4, and L>35.
For c in [3,7] put

`b=h-(c+8,c+5,5,1,0,...)`.

Then b has positive interval support and is `(L-35)`-strong.

**Proof.** All subtracted entries are at most 15, so positivity is
immediate. The independently checked correction identities are

\[
\begin{aligned}
\delta_0(b)-\delta_0(h)
 &=-(2c+21)h_0-(c+8)h_2+4(c+5)h_1-c^2+c+54,\\
\delta_1(b)-\delta_1(h)
 &=-(2c+11)h_1+5h_0+(c+18)h_2-(c+5)h_3+c^2+6c-35,\\
\delta_2(b)-\delta_2(h)
 &=-10h_2+h_1+(c+7)h_3-5h_4+19-c,\\
\delta_3(b)-\delta_3(h)&=-2h_3+5h_4-h_5+1,\\
\delta_4(b)-\delta_4(h)&=h_5,\\
\delta_n(b)&=\delta_n(h)\quad(n\ge5).
\end{aligned}
\tag{8}
\]

Decrease of h and 3<=c<=7 give

\[
\begin{aligned}
\delta_0(b)&\ge(L-35)h_0+21h_1+12,\\
\delta_1(b)&\ge(L-20)h_1+13h_2-8,\\
\delta_2(b)&\ge(L-10)h_2+h_1+5h_3+12,\\
\delta_3(b)&\ge(L-2)h_3+4h_4+1,\\
\delta_n(b)&\ge Lh_n\quad(n\ge4).
\end{aligned}
\tag{9}
\]

For the first line, use `-c^2+c+54>=12` and absorb `-(c+8)h_2`
into `4(c+5)h_1`. For the second, use h_0>=h_1, h_2>=h_3,
and `c^2+6c-35>=-8`. Since every supported h_n exceeds 35, all
five bounds dominate `(L-35)b_n`. QED.

These lemmas are forward positivity results with stated hypotheses. No
inverse of a smoothing operation, coefficient convolution, or TP2 kernel
is used.

## 4. Stronger unshifted pure-left trace bounds

The existing, audited inputs are

\[
y^2T_j\text{ is }2^j\text{-strong}\quad(j\ge1),
\tag{10}
\]

from `mixed_kernel_sharp_strength.md` and its independent audit, and

\[
y^3T_j\text{ is }2^{j-1}\text{-strong}\quad(j\ge1),
\tag{11}
\]

from `recovery_oneturn_closure.md`, Section 1, with its exact residue
certificates and audit. Both families have positive ordinary coefficients.

**Lemma 4.1.** For j>=1,

\[
t_{g_j}\text{ is }(3\,2^j-2)\text{-strong}.
\tag{12}
\]

**Proof.** Put a=2^j and h=H(y^2T_j). Then
`H(t_(g_j))=3h+(3,2,0,...)`. Write mu=3a-2. The exact margins after
using (10) are bounded below as follows:

\[
\begin{array}{c|l}
n&\delta_n(H(t_{g_j}))-\mu H(t_{g_j})_n\\\hline
0&24(h_0-h_1)+9(h_2-a)+7\\
1&18h_1-9h_2+6h_3+8-6a\\
2&6(h_2-h_3)\\
n\ge3&6h_n.
\end{array}
\tag{13}
\]

These are nonnegative: h decreases and each supported entry is at least a.
Its degree is j+2>=3, so h_2,h_3 are supported in the relevant low-index
arguments. At n=1 one may lower-bound the row by `9h_1+8`. QED.

**Lemma 4.2.** For j>=2,

\[
yt_{g_j}\text{ is }(3\,2^{j-1}-5)\text{-strong}.
\tag{14}
\]

**Proof.** Put a=2^(j-1)>=2 and h=H(y^3T_j). Then
`H(yt_(g_j))=3h+(7,5,2,0,...)`. In addition to decrease and h_n>=a,
we have h_0<=2h_1: write y^3T_j=yQ with Q=y^2T_j and its nonnegative
Fourier row p; then h_0=p_0+2p_1 and h_1=p_0+p_1+p_2.

For mu=3a-5, expansion and (11) give the margins

\[
\begin{array}{c|l}
n&\delta_n(H(yt_{g_j}))-\mu H(yt_{g_j})_n\\\hline
0&\ge63h_0-60h_1+21(h_2-a)+48\\
1&\ge45h_1-6h_0-33h_2+15(h_3-a)+32\\
2&\ge27h_2-15h_3+6h_4+14-6a\\
3&\ge15h_3-6h_4\\
n\ge4&\ge15h_n.
\end{array}
\tag{15}
\]

At n=1 use h_0<=2h_1 to leave `33(h_1-h_2)+15(h_3-a)+32`.
At the other indices decrease suffices. Every bound is nonnegative and
mu>0. QED.

Both improvements use unshifted t_(g_j), which is why they can be stronger
than the previously stated lower bound uniform over all shifted traces.

## 5. Proof of the all-m theorem

For m>=1 put a=2^m. By (12) and multiplicative strength,

\[
F=t_{g_m}t_{g_{m+1}}
\text{ is }(3a-2)(6a-2)\text{-strong}.
\]

This constant is at least 40. Apply Lemma 3.1 to (3)-(4). The resulting
strength is

\[
(3a-2)(6a-2)-15=18a^2-18a-11=A_m>0.
\]

For m>=2, apply (12) to t_(g_m), and (14) to the next index m+1:

\[
yF=t_{g_m}\,[yt_{g_{m+1}}]
\text{ is }(3a-2)(3a-5)\text{-strong}.
\]

This constant is at least 70. Lemma 3.2 applied to (3) and (5) gives

\[
(3a-2)(3a-5)-35=9a^2-21a-25=B_m>0.
\]

The remaining cases are m=0 for the raw trace and m=0,1 for the smoothed
trace. The verifier reconstructs X_m through the original scalar
mutations. For every supported coefficient it forms the degree-two
polynomial in r

`delta_n(H(P_r))-kappa H(P_r)_n`,

using kappa=18,18,72 respectively. After r=4u-2, **every degree-two
Bernstein coefficient is nonnegative**. This certifies the entire interval
[-2,2], not just its endpoints. All half-row entries are positive on that
interval. The full 66 rational/integer Bernstein coefficients are in
`trace_transport_results.json`; the terminal margins are exactly zero.
This proves (1) in every case. QED.

## 6. Positive comparison kernels now available without a degree bound

The standard exact real-root factorization

\[
U_k(t/2)=\prod_{j=1}^k\left(t-2\cos\frac{j\pi}{k+1}\right)
\]

and (1) give, for every m>=0 and k>=0,

\[
U_k(t_{X_m}/2)\text{ is }A_m^k\text{-strong}.
\tag{16}
\]

For k>=1, smoothing a single root factor gives

\[
yU_k(t_{X_m}/2)\text{ is }B_mA_m^{k-1}\text{-strong}.
\tag{17}
\]

The k=0 smoothed object is y itself and is deliberately excluded.

The analogous statements hold for `sum_(j=0)^k U_j(t_(X_m)/2)`:
its factorization into U and `U+U_previous` has degree k and all roots
in [-2,2]. Thus its strengths are A_m^k and, after one y factor and
with k>=1, B_m A_m^(k-1).

Consequently **every one of these canonical multiplication operators
preserves Fourier-half-row likelihood-ratio order**: if an input pair
P,Q has nonnegative ordered Fourier minors, multiplying both by one of
these polynomials preserves those minors by Cauchy-Binet. Their positive
strengths also give the previously proved quantitative all-minor bounds.
This is a genuine forward comparison theorem. It does not infer the input
pair's order from its smoothed output.

## 7. Scope of the advance

This proves the complete shifted-trace and smoothed-trace kernel component
uniformly for **all** fixed endpoints X_m reached at L^mR, and for arbitrary
subsequent Chebyshev run length. It avoids repeating one separate trace
certificate for each fixed m.

For the full `L^m R^2 L^ell` Local TP2 theorem, the initial-gap single and
mixed blocks and the final mass/proxy comparisons still need to be
verified uniformly in m. This note does not assume those statements or a
future child's target. In particular, (16)-(17) alone are not a proof of
the full pair comparison `H(S)<=_lr H(D)`.

`verify_trace_transport.py` checks 20 low-index symbolic identities and
the three complete small-m continuum certificates. The infinite range
uses the proofs in Sections 3-5 and the already audited all-index input
theorems, not deeper sampling.
