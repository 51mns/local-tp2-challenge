# The midpoint strength obligation holds above the smaller support

Use the arbitrary-inner-index notation from `mixed_kernel_sharp_strength.md`:

\[
A=T_{m+1},\quad B=T_{m-1},\quad
F=A(t_m-r)(t_m-s),\quad G=B(t_m-c),\quad H=F+G,
\]

where m is any integer at least 1 and r,s,c independently range over [-2,2]. Write f,g,h for their Laurent half-rows and \(b_0=H(B)[0]\). Let

\[
d=\deg G=2m+1,\qquad
\lambda_F=9\cdot2^{3m-2}.
\]

The sharp strength theorem already gives \(\delta_n(f)\ge\lambda_F f_n\), and the elementary mass estimate gives

\[
8b_0\le\tfrac43(7^m-1).
\]

**Claim:** the needed midpoint strength inequality

\[
\delta_n(h)\ge8b_0h_n
\]

holds for every supported index \(n\ge2m+2\), uniformly in all three parameters. The remaining unresolved band is therefore \(0\le n\le2m+1\).

At \(n=d+1\), zero extension of g gives \(h_n=f_n\), \(\delta_n(g)=0\), and the exact mixed defect

\[
\delta_n(f+g)-\delta_n(f)-\delta_n(g)
=-g_df_{d+2}.
\]

The folded-cone row f is decreasing, so

\[
\delta_{d+1}(h)
\ge(\lambda_F-g_d)f_{d+1}.
\]

Leading coefficients are independent of r,s,c. Since B has leading coefficient \(2^{m-1}\) and \(t_m\) has leading coefficient \(3\cdot2^m\),

\[
g_d=3\cdot2^{2m-1},\qquad
\frac{g_d}{\lambda_F}=\frac1{3\cdot2^{m-1}}\le\frac13.
\]

Consequently

\[
\lambda_F-g_d\ge\tfrac23\lambda_F
=\tfrac32 8^m
>\tfrac43(7^m-1)\ge8b_0.
\]

This proves the claim at the first index of the band, including strict surplus.

For every \(n\ge d+2\), the smaller row and all its entries appearing in the defect formula vanish. Thus \(h_n=f_n\) and \(\delta_n(h)=\delta_n(f)\), so the same conclusion follows directly from \(\lambda_F>8b_0\).

This argument explicitly absorbs the negative support-boundary cross term. It does not assume nonnegative mixed defects, and it makes no assertion about the remaining lower band.
