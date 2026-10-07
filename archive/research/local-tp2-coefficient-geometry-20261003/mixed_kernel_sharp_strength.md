# Leading-scale strength bounds on the pure-left ray

**Status: proved.** These sharpen the earlier uniform constants. They also prove relative minor domination for the dominant product in the arbitrary-inner-index one-turn problem. The addition of its second summand remains unresolved.

Use the notation and exact eight residue boxes of `mixed_kernel_pureleft_multiplier.md`:

\[
y=x+1,\quad z=x+\tfrac32,\quad T_m=\sum_{j=0}^mU_j(z),\quad
g_m=1+yT_m,\quad P_m=y^2T_m,\quad t_m=3yg_m-x.
\]

The strength-product theorem is from `mixed_kernel_strong_cone.md`.

## Theorem

For every integer m at least 1,

\[
P_m\text{ is }2^m\text{-strong},\qquad
T_m\text{ is }2^{m-1}\text{-strong}.
\tag{1}
\]

For every real a in [-2,2],

\[
t_m-a\text{ is }3\cdot2^{m-1}\text{-strong}.
\tag{2}
\]

The constant in the first assertion of (1) is optimal: the terminal half-row entry of P_m is \(2^m\), so no greater strength is possible.

## 1. Exact normalized block certificates

The same scaled quartic \(Q=16ff'\) used previously is **16-strong**, rather than merely 1-strong. Its exact Bernstein lower bounds for \(\delta_n(Q)-16H(Q)[n]\) are

\[
(10977,16328,13120,2944,0).
\]

For every residue R of degree d in the established eight-case factorization, exact Bernstein coefficients give both

\[
2^dy^2R\text{ is }2^d\text{-strong},\qquad
2^dR\text{ is }2^{d-1}\text{-strong}.
\tag{3}
\]

For the first family every terminal margin is identically zero and every preceding Bernstein coefficient is strictly positive. For the second family every margin has strictly positive Bernstein coefficients. The smallest coefficients across all indices and parameters in each second-family case are:

| m modulo 8 | Residue degree d | Minimum prefix margin |
|---|---:|---:|
| 0 | 4 | 128 |
| 1 | 5 | 512 |
| 2 | 2 | 8 |
| 3 | 3 | 32 |
| 4 | 4 | 128 |
| 5 | 5 | 512 |
| 6 | 6 | 2048 |
| 7 | 3 | 32 |

The full power and Bernstein coefficient arrays for both families are in `mixed_kernel_sharp_strength_certificates.json`. The deterministic exact-rational generator is `mixed_kernel_sharp_strength.py`. It imports the already fixed residue parameterizations, so this is a reweighting of the proved continuous-box certificates, not a new restriction on parameter values.

If the factorization has k removed quartics, its degrees satisfy \(m=d+4k\). Strength-product closure gives

\[
2^d16^k=2^m
\]

for P_m, and \(2^{d-1}16^k=2^{m-1}\) for T_m. This covers every m at least 2, using the same available-quartic argument for residue classes 0 and 1. For m=1 the explicit rows are

\[
H(P_1)=(20,16,8,2),\quad \delta(P_1)=(48,64,28,4),
\]

and \(H(T_1)=(4,2)\), \(\delta(T_1)=(8,4)\). They verify (1) directly.

## 2. Propagation to the shifted trace

For m at least 2 put \(\lambda=2^m\ge4\), \(\mu=3\lambda/2\), \(h=H(P_m)\), and \(b=H(t_m-a)\). Write \(c=3-a\in[1,5]\), so

\[
b_0=3h_0+c,\quad b_1=3h_1+2,\quad b_n=3h_n\ (n\ge2).
\]

The exact defect identities are those already proved in the uniform multiplier theorem:

\[
\begin{aligned}
\delta_0(b)&=9\delta_0(h)+3c(2h_0+h_2)-24h_1+c^2-8,\\
\delta_1(b)&=9\delta_1(h)+12h_1-3ch_2+6h_3+4,\\
\delta_2(b)&=9\delta_2(h)-6h_3,\\
\delta_n(b)&=9\delta_n(h)\quad(n\ge3).
\end{aligned}
\]

The row h is strictly decreasing and has integer entries. Its terminal entry is exactly lambda; its degree is m+2, so \(h_2\ge\lambda+1\).

At index 0, \(\delta_0(b)-\mu b_0\) is increasing in c on [1,5]. Indeed its c derivative is \(6h_0+3h_2+2c-\mu>0\). At c=1 its lower bound is

\[
\begin{aligned}
\delta_0(b)-\mu b_0
&\ge(\tfrac92\lambda-18)h_0+3h_2-7-\tfrac32\lambda\\
&\ge\tfrac32\lambda-4\ge2.
\end{aligned}
\]

Here the first term is nonnegative because lambda is at least 4, and \(h_2\ge\lambda+1\) supplies the second line.

At index 1,

\[
\delta_1(b)-\mu b_1
\ge(\tfrac92\lambda-3)h_1+6h_3+4-3\lambda>0.
\]

The last inequality follows already from \(h_1\ge1\) and lambda at least 4. At index 2,

\[
\delta_2(b)-\mu b_2\ge(\tfrac92\lambda-6)h_2>0.
\]

At every higher supported index, the margin is at least \(\tfrac92\lambda h_n>0\). This proves (2) for m at least 2. For m=1, the earlier explicit proof gives 3-strength, exactly \(3\cdot2^{m-1}\).

## 3. The dominant product already has every required relative minor

For any integer m at least 1 and independent r,s in [-2,2], set

\[
A=T_{m+1},\quad B=T_{m-1},\quad
F=A(t_m-r)(t_m-s),\quad b_0=H(B)[0].
\]

By (1), (2), and strength-product closure,

\[
F\text{ is }\lambda_F\text{-strong},\qquad
\lambda_F=2^m(3\cdot2^{m-1})^2
=9\cdot2^{3m-2}.
\tag{4}
\]

This strength is sufficient at every m. To see this without any asymptotic argument, evaluate the inner Chebyshev recurrence at x=2. Its multiplier is 7. Positivity and

\[
U_{j+1}(7/2)=7U_j(7/2)-U_{j-1}(7/2)
\]

give \(U_j(7/2)\le7^j\). Therefore

\[
8b_0\le8B(2)\le\frac43(7^m-1)
<\frac94 8^m=\lambda_F.
\tag{5}
\]

The ordinary coefficients of A dominate those of B because A is a longer sum of positive-coefficient Chebyshev polynomials. Each \(t_m-r\) has positive ordinary coefficients and constant coefficient at least 1. Hence \(H(F)\ge H(B)\) coefficientwise.

The all-minor theorem in `mixed_kernel_all_minor_strength.md` now proves, for **every** ordered row pair and column pair of the infinite kernels,

\[
\det K_F\ge4\det K_B.
\tag{6}
\]

No finite kernel truncation is used.

## Remaining obstruction

The actual midpoint in the all-m compatibility argument is

\[
H=F+B(t_m-c),\qquad c\in[-2,2].
\]

Equation (6) applies to its dominant product F. It does not automatically pass to H, because determinant cross terms created by addition may be negative. No arbitrary positive-sum closure is assumed. A quantitative bound on those cross terms remains necessary. In fact nonnegative pairwise compatibility of these two summands is impossible: put d=deg G=2m+1, where G=B(t_m-c), while deg F=3m+5. The mixed defect at index d+1 is exactly −H(G)[d]H(F)[d+2]<0. This negative support-boundary term does not refute strength of F+G; it shows why the dominant diagonal defects must absorb, rather than eliminate, the cross correction.
