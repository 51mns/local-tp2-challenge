# Uniform folded-kernel strength for every pure-left boundary multiplier

**Status:** infinite theorem, proved by exact parameter-box certificates and product closure. This gives the propagator kernel needed for arbitrary fixed pure-left boundaries. It does not by itself prove Local TP2 after the turn.

Put

\[
y=x+1,\quad z=x+\tfrac32,\quad
T_m(z)=\sum_{j=0}^{m}U_j(z),\quad g_m=1+yT_m(z),\quad
 t_Q=3yQ-x.
\]

Here U denotes the Chebyshev polynomial of the second kind. These are the pure-left boundary polynomials: \(g_0=x+2\), and \(g_1=2x^2+6x+5\) is the root center.

Recall that a positive Laurent half-row h is lambda-strong if \(\delta_n(h)\ge\lambda h_n\) at every supported n. The theorem `mixed_kernel_strong_cone.md` proves that strengths multiply under polynomial multiplication.

## Theorem

For every integer \(m\ge1\) and every real \(a\in[-2,2]\), the polynomial

\[
t_{g_m}-a
\]

is **3-strong**. For \(m=0\), the same family is **1/5-strong**.

Consequently, for all \(m\ge1\) and integers \(k\ge0\),

\[
U_k(t_{g_m}/2)
\]

is \(3^k\)-strong. In particular, each of these polynomials has a TP2 folded multiplication kernel, with strictly positive supported defects.

## 1. A stronger prefix-product bound

Write \(P_m=y^2T_m(z)\). We first prove

\[
\delta_n(H(P_m))\ge4H(P_m)[n]\qquad(m\ge2)
\tag{1}
\]

at every supported n.

Use the established factorization

\[
T_m=U_{\lfloor m/2\rfloor}V_{\lceil m/2\rceil},
\qquad V_j=U_j+U_{j-1},
\]

and the exact root grouping in `continuation_bracket.md`. Every removed quartic has the scaled form

\[
Q=16f_{u,v}f_{u',v'},\qquad
f_{u,v}=x^2+(3+u)x+\tfrac54+\tfrac52u+v,
\]

where all four parameters range independently over [0,1]. An exact Bernstein certificate proves Q is 1-strong. In order of supported indices 0 through 4, the lower bounds for \(\delta_n(H(Q))-H(Q)[n]\) are

\[
(19092,22448,16840,4384,240).
\]

After removing such quartics, keep the same eight residue families R from the bracket proof. If d is the degree of R, set \(P_R=2^d y^2R\). The parameterizations used by the verifier are:

\[
\begin{aligned}
z&=x+\tfrac32,&
\ell&=x+\tfrac32+\tfrac12w,\\
f_e&=x^2+3x+2+\tfrac14u,&
f_o&=x^2+3x+\tfrac74+\tfrac12u,\\
I&=(x+1+\tfrac12v)(x+\tfrac32+w),&
f&=f_{u,v},\quad f'=f_{w,z_0},\quad F=f_{v,z_0},
\end{aligned}
\]

with independent unit-interval variables \(u,v,w,z_0,t\). Each row in the following table denotes its own independent parameter box.

| m modulo 8 | Residue R | d | Lower bounds for delta(P_R) minus 4H(P_R) |
|---|---|---:|---|
| 0 | ff' | 4 | 517952, 951280, 769013, 310392, 70944, 7296, 192 |
| 1 | ff'(x+3/2+t/2) | 5 | 16896516, 36601512, 29947837, 14170212, 3931456, 617152, 43584, 896 |
| 2 | z ell | 2 | 492, 1060, 609, 92, 0 |
| 3 | z I | 3 | 14304, 31600, 19904, 6380, 816, 32 |
| 4 | f_e I | 4 | 524224, 1071008, 784128, 304480, 63424, 6176, 192 |
| 5 | f_e ell F | 5 | 20869440, 44005008, 35483776, 16151520, 4310560, 637792, 43584, 896 |
| 6 | z f_o ell F | 6 | 713730628, 1549468996, 1341581617, 685576268, 218781408, 42622272, 4694464, 239872, 3840 |
| 7 | z f_o | 3 | 20488, 39756, 26305, 7896, 1040, 32 |

The m modulo 8 cases 0 and 1 pull one available quartic into the residue; this is possible for m at least 8 and 9, respectively. The only smaller missing case is m=1, handled separately below. The allowed root intervals and the availability of these residues are established by the root-pair argument in the bracket proof. In particular, isolating a pair nearest the central angle gives the narrower f_e and f_o intervals.

Every table entry is the minimum of all coefficients in the exact multivariate Bernstein expansion of the indicated margin. All are nonnegative, including the exact terminal zero for residue degree 2. Thus each \(P_R\) is 4-strong on its entire parameter box. Positive ordinary coefficients ensure the required interval support. These are certificates over continuous boxes, not tests at sampled parameters.

The leading factors are preserved: \(2^m=2^d16^{(m-d)/4}\). Therefore

\[
P_m=P_R\prod Q_i.
\]

The strength-product theorem proves (1), because \(4\prod1=4\).

The deterministic rational-arithmetic script `mixed_kernel_pureleft_margin.py` regenerates every coefficient in `mixed_kernel_pureleft_certificates.json`. It reuses the polynomial and Bernstein routines from the already established prefix/bracket certificates.

## 2. Uniform shifted-multiplier bounds

Since

\[
t_{g_m}-a=3P_m+2x+c,\qquad c=3-a\in[1,5],
\]

write h=H(P_m) and b=H(t_(g_m)-a). Then

\[
b_0=3h_0+c,\quad b_1=3h_1+2,\quad b_n=3h_n\ (n\ge2).
\]

Exact expansion gives

\[
\begin{aligned}
\delta_0(b)&=9\delta_0(h)+3c(2h_0+h_2)-24h_1+c^2-8,\\
\delta_1(b)&=9\delta_1(h)+12h_1-3ch_2+6h_3+4,\\
\delta_2(b)&=9\delta_2(h)-6h_3,\\
\delta_n(b)&=9\delta_n(h)\qquad(n\ge3).
\end{aligned}
\tag{2}
\]

For m at least 2, (1) implies h is decreasing. All its supported entries are positive integers, in particular \(h_0,h_2\ge1\).

At index 0, \(\delta_0(b)-3b_0\) is increasing as a function of c on [1,5]. Its lower bound from (1), evaluated at c=1, is

\[
33h_0-24h_1+3h_2-10
\ge9h_0+3h_2-10\ge2.
\]

At index 1, using c at most 5 and \(h_2\le h_1\) gives

\[
\delta_1(b)-3b_1
\ge39h_1-15h_2+6h_3-2
\ge24h_1+6h_3-2>0.
\]

At index 2,

\[
\delta_2(b)-3b_2\ge27h_2-6h_3\ge21h_2>0.
\]

At every remaining supported index, (1) gives

\[
\delta_n(b)-3b_n\ge27h_n>0.
\]

This proves the 3-strong conclusion for m at least 2.

For m=1, \(P_1=2y^2(x+2)\) has half-row \((20,16,8,2)\). Thus

\[
b=(60+c,50,24,6),\quad
\delta(b)=(40+144c+c^2,784-24c,240,36).
\]

Subtracting 3b gives lower bounds \((2,514,168,18)\) on the entire interval c in [1,5], proving the same conclusion.

For m=0, direct calculation yields

\[
b=(12-a,8,3),\quad
\delta(b)=(52-27a+a^2,19+3a,9).
\]

Writing \(s=12-a\in[10,14]\), the first defect divided by its row entry is \(s+3-128/s\), which is increasing and has minimum 1/5. The other two ratios exceed 1/5. This proves the boundary assertion.

## 3. Every Chebyshev propagator

The exact real-root factorization is

\[
U_k(t/2)=\prod_{j=1}^k\left(t-2\cos\frac{j\pi}{k+1}\right).
\]

Each factor at \(t=t_{g_m}\), m at least 1, is 3-strong by the theorem. Strength-product closure therefore yields \(3^k\)-strength. For k=0 the polynomial is 1, whose single supported defect is 1, consistent with the formula.
