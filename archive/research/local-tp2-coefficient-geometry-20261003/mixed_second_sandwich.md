# Reducing the mixed-path second sandwich

This note gives an exact reduction and a stronger global positivity
invariant. It does not prove the remaining low-index comparison.

Let the endpoints be `X,Y`, sorted by degree, let `C` be the center,
and put `y=x+1`, `P=x+2`,

`M=3yC-x+1`, `Z=PXM`.

The desired second sandwich is `H(S)<=lr H(Z)`. Throughout, write

`W_n(f,g)=H(f)_n H(g)_(n+1)-H(f)_(n+1) H(g)_n`.

## 1. A stronger global character invariant

In addition to the universal invariant already established in
`resumed_extension_kernel_support.md`, every canonical triple satisfies

`C-A-B >_B 0`

dense throughout `0,...,deg C`. Here the positive character basis is
`B_j=sum_(i=-j)^j q^i`.

At the root the coefficient row is `(1,3,2)`. For the child
`U=3yAC-x(A+C)-B`, direct expansion gives

`U-A-C = [(2y-1)C-y] + (C-B) + y(A-1)(3C-1)`.

The latter two terms are character-nonnegative by the established
invariant. If `c_j=alpha_C(j)`, the bracket has coefficients

- `2c_1-c_0` at index zero;
- `2c_0+c_1+2c_2-1` at index one;
- `2c_(n-1)+c_n+2c_(n+1)` at indices `n>=2`.

They are positive through `deg C+1`, since `c_1>=c_0>=3`.
When `deg A>=1`, the product `y(A-1)(3C-1)` supplies strict positivity
in every remaining index through `deg U`, by exactly the character
product support argument in the earlier invariant proof. The other
mutation is symmetric. Thus the strengthened invariant holds globally.

## 2. The correction can be moved below degree Y

The original identity `S=XM-(X+Y+yC)` can be rewritten as

`3S=(3X-1)M-R`, `R=3X+3Y+x-1`.                      (1)

In particular `deg R=deg Y`, strictly below `deg C`. This removes the
apparently higher-degree correction `yC` from the comparison.

Moreover, `R` and `M-R` are character-positive throughout their supports.
To see the upper bound, let `a_j,b_j,c_j` be the character coefficients
of `X,Y,C`. The stronger invariant gives `a_j+b_j<c_j` throughout
the center support. The remainder coefficients are

`r_0=3a_0+3b_0-2`, `r_1=3a_1+3b_1+1`,

`r_n=3a_n+3b_n` for `n>=2`.

The corresponding multiplier coefficients are

`m_0=3c_1+2`, `m_1=3(c_0+c_1+c_2)-1`,

`m_n=3(c_(n-1)+c_n+c_(n+1))` for `n>=2`.

Using `c_1>=c_0>=3` proves `0<_B R<_B M`. In particular, (1) also has
the entirely positive decomposition

`3S=(3X-2)M+(M-R)`.                                  (2)

This positivity statement alone does not compare likelihood ratios of
the two summands with `Z`.

## 3. The primitive pair needs only one scalar margin

Let `h=H(X)` and let `delta_X(n)` be its folded defect difference.
Direct expansion gives

`W_n(3X-1,3PX)=9delta_X(n)` for `n>=1`,

`W_0(3X-1,3PX)=9delta_X(0)-3(h_0+2h_1+h_2)`.          (3)

Consequently, if `K_X` is TP2, the primitive comparison

`H(3X-1)<=lr H(3PX)`

is equivalent to the one additional scalar inequality

`3delta_X(0)>=h_0+2h_1+h_2`.                          (4)

The quantitative premise already used in `mixed_first_sandwich.md`,
`delta_X(0)>=h_0+h_1`, implies (4), because the Fourier row is decreasing.
Every nonboundary endpoint is a previous canonical center, so this
premise applies there. For the two original endpoints `X=1` and
`X=x+2`, direct evaluation gives the first minor in (3) equal to `6`
in both cases; all remaining required minors are nonnegative.

If `K_M` is TP2, common-factor preservation therefore proves

`H((3X-1)M)<=lr H(3PXM)`.                             (5)

## 4. A shorter unresolved band

Since `3Z=3PXM`, identities (1) and (5) give

`9 W_n(S,Z)=W_n((3X-1)M,3PXM)-W_n(R,3PXM)`.           (6)

For every `n>=deg Y+1`, the second term is zero. Thus under the same
kernel and scalar premises as above, the second sandwich is proved
throughout that entire upper band. The original elementary cutoff was
`deg C+2`; (6) improves it to `deg Y+1`.

The only remaining task is the explicit low-band inequality

`W_n((3X-1)M,3PXM)>=W_n(R,3PXM)`,

for `0<=n<=deg Y`, with `0<_B R<_B M`. No degree bound or parameter
sampling proves this residual family. Neither common-factor TP2 nor
the positive decomposition (2), by itself, controls its sign.

## 5. A shortcut that is invalid even canonically

One could try to prove `S<=lr PU` using an upper-gap estimate, and then
replace `U` by `XM`. The second step is false: at the canonical path
`LR`, the first minor for `H(U)<=lr H(XM)` is

`-197848930`.

Even after multiplying both polynomials by `P`, that first minor is
`-2520809814`. The exact checker `mixed_second_sandwich.py` reconstructs
this example from the original mutation recurrence. This failure concerns
only that shortcut, not the desired second sandwich.
