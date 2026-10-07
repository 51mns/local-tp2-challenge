# A canonical-root obstruction to the naive Lorentzian lift

Scope: the ordinary homogenization of the folded coefficient polynomial. Other normalizations and larger state spaces are not excluded. Full Local TP2 is unchanged.

Family 114 of `openai/math`, *Approximate counting of common bases of two matroids*, section 3, uses the necessary Lorentzian condition that every quadratic derivative Hessian has at most one positive eigenvalue. Its exact matroid model supplies that condition; it is not a theorem about arbitrary positive arrays. See [the pinned source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/build/main.tex), labels `thm:BH` and `lem:coefficient`.

## Proposition

Let P(x) be a polynomial with only negative real roots. Passing to its nonnegative Fourier half-row after x=q+q^{-1}, and then ordinarily homogenizing that half-row, need not produce a Lorentzian polynomial. This failure already occurs for the canonical root S.

## Proof

The root triple is A=1, C=2x^2+6x+5, B=x+2. Applying the prescribed two child mutations, ordering them by degree, and subtracting gives

\[
S(x)=8+20x+16x^2+4x^3=4(x+1)^2(x+2),
\]

so its roots are -1,-1,-2. Its Fourier half-row is

\[
H(S)=(40,32,16,4).
\]

The ordinary degree-three homogenization is

\[
f(u,v)=40v^3+32uv^2+16u^2v+4u^3.
\]

Differentiation yields

\[
\partial_v f=120v^2+64uv+16u^2,
\qquad
\operatorname{Hess}(\partial_v f)=
\begin{pmatrix}32&64\\64&240\end{pmatrix}.
\]

Its first principal minor is 32 and its determinant is

\[
32\cdot240-64^2=3584>0.
\]

Sylvester's criterion makes this Hessian positive definite, with two positive eigenvalues. It fails the necessary Lorentzian signature condition. QED.

Meanwhile the actual root Local TP2 values are (272,352,160,24), all positive. The proposition invalidates a transfer of the external theorem through this particular transform, not the target inequality. The independent verifier reconstructs the root by Laurent arithmetic and computes the Hessian from the coefficients.
