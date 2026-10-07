# Exact finite mixed-kernel completion

**Status: author certificates PASS; independent recomputation PASS.**
The independent implementation and mathematical audit are recorded in
`../arbk_root/FINITE_MIXED_INDEPENDENT_AUDIT.md`. This is a same-session
independent audit, not an external review.

The finite complement of the analytic mixed-kernel gates consists of
these 34 canonical prefixes:

| m | k |
|---|---|
| 0 | 3 through 20 |
| 1 | 3 through 10 |
| 2 | 3 through 5 |
| 3 | 3 through 4 |
| 4 | 3 |
| 5 | 3 through 4 |

Use the canonical old prefixes `Z_j` and `T_m` from
`NORMALIZED_BLOCKS.md`. The actual new seeds and fixed trace are

\[
A=Z_k-T_m,\quad B=Z_{k-2}-T_m,
\quad X=1+yZ_{k-1},\quad t=3yX-x.
\]

For `r,s in [-2,2]`, define precisely the required midpoint family

\[
L_r=A(t-r)+B,\qquad
H_{r,s}=A(t-r)(t-s)+B\left(t-\frac{r+s}{2}\right).
\]

The certificate generator `finite_mixed_kernels.py` proves positive
supported folded defects for all four families `L_r,yL_r,H_(r,s),yH_(r,s)`.
It simultaneously proves the normalized dominance inequality required
for midpoint compatibility against `B` and `yB`.

Specifically, let `P` denote either midpoint row and let `Q` be its raw
or smoothed reference. At `r=s=2`, write `P_0` for that polynomial, and
set

\[
c=\min_{0\le n\le\deg Q}\frac{H(P_0)_n}{H(Q)_n}>0.
\]

Every coefficient of the family is minimized at this endpoint: with
`r=2-4u,s=2-4v,T=t-2`, the polynomial is

\[
H_{r,s}=AT^2+BT+(4AT+2B)(u+v)+16Auv.
\]

All listed coefficient rows are nonnegative and the constant row is
dense positive. Hence `P>=cQ` throughout the full square. The exact
certificate proves, at every supported index, the stronger assertion

\[
c^2\delta_n(H(P))-16H(P)_n^2>0.\tag{1}
\]

The generic normalized ordered-minor lemma in
`../arbk_root/GENERIC_ARBITRARY_K_CLOSURE.md`, Section 2.2, now implies
`det K_P>=4 det K_Q` for every ordered kernel minor. Its hypotheses hold
because the new reference seeds are strict cone polynomials by the
independently audited seed theorem. Thus the old midpoint identity gives
the pairwise mixed-kernel nonnegativity used in the spectral expansion.

Each row is affine in `u` for the single family and multiaffine in
`u,v` for the midpoint family. Consequently its defect and squared row
entry have tensor degree at most two. The verifier explicitly constructs
their power coefficients, transforms them into degree-two Bernstein
coefficients on the entire unit interval/square, and exactly inverts the
transform to check reconstruction. It uses the exact rational value of
`c`, clearing its denominator in (1). This is a continuum certificate,
not a sampled spectral test.

The final JSON stores all 136 family records, all 51,804 strictly
positive defect coefficients, and all 42,246 strictly positive
relative coefficients, as well as squared-entry coefficients, exact
normalized lower bounds, exact dominance constants, and ordered digests.
The independent verifier reconstructs the original canonical mutations
in ordinary `x` and recovers the parameter polynomials through exact
interpolation, without importing the author implementation. Every saved
record agrees exactly.

Reproduce the author certificate with

```sh
python arbk_mixed/finite_mixed_kernels.py
```

The result is `finite_mixed_kernels_results.json`. The finite result
joins the separate analytic tail gates; by itself it asserts only the
listed 34 prefix families with arbitrary continuous spectral parameters.
