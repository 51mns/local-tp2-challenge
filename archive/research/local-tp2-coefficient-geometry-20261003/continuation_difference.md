# Chebyshev adjacent differences: an infinite folded-cone theorem

**Later update:** The original all-left Local TP2 comparison left open at this stage is now proved in `resumed_comparison_all_left.md`, audited in `resumed_audit_all_left.md`. The full tree remains open. The earlier derivations below are retained as proof ingredients.

Write `u_r=U_r(x+3/2)`, `u_(-1)=0`, `W_r=u_r-u_(r-1)`, and `z=2x+3`. This note uses the independently proved strict multiplicative closure of the folded-TP2 cone. It does **not** assert Local TP2 for any infinite subfamily of the original S,D pairs.

## Theorem

Every `W_r` with `r>=2` has a TP2 folded convolution kernel, with strictly positive folded defects throughout its support. Moreover, for every `r>=2`,

`H(W_r) <_lr H(W_(r+1))`

strictly at all adjacent supported columns `0<=n<=r`. The omitted `W_1=2(x+1)` is not in the cone.

## Exact parameter-box certificates

Let `f=x²+s x+c`, with `5/2<=s<=3` and `5/4<=c<=9/4`. The following blocks have strictly positive folded defects on their entire supported range:

| Block | Parameter domain | Exact lower bounds by Fourier index |
|---|---|---|
| `fg` | f,g independent general quadratics | `5201/256,4845/64,705/16,37/4,1` |
| `(x+a)f` | `5/4<=a<=3/2` | `1213/256,715/64,75/16,1` |
| `(x+a)fg` | `5/4<=a<=3/2` | `1134325/4096,550125/1024,91125/256,7505/64,257/16,1` |
| `(x+a)(x+b)` | `2/3<=a<=3/2`, `3/2<=b<=2` | `2/9,25/36,1` |

The standalone script `continuation_difference.py` forms the exact Fourier rows and defects and expands them in multivariate Bernstein bases over the full unit cube. Every rational Bernstein coefficient is positive. The complete certificates are in `continuation_difference_certificates.json`. These are parameter-domain algebraic certificates, not numerical sampling.

The lower bound `a>=5/4` in the middle-root blocks is material: enlarging it to `a>=1` makes the generic cubic claim false at `a=1,s=5/2,c=9/4`.

## Root bounds

For `r>=1`, the roots of W_r are

`x_j=cos((2j-1)pi/(2r+1))-3/2`, `j=1,...,r`.

Put `epsilon=pi/(2r+1)` and pair indices j and r+1-j. For a paired lower index let `theta=(2j-1)epsilon`, `e=sin(epsilon/2)`, and `t=sin(theta+epsilon/2)`. The two shifted factors are

`x+a`, `a=3/2-cos(theta)`,

`x+b`, `b=3/2+cos(theta+epsilon)`.

Thus their quadratic coefficients satisfy

`s=a+b=3-2et`,

`c=ab=5/4+t²+e²-3et`.

For `r>=3`, `e<=sin(pi/14)<1/4`, where the latter follows from `sin(v)<v` and `pi<22/7`. Hence `5/2<s<=3`. The case r=2 is direct and has `s=5/2`.

The lower-half pairing angles give `t>=sin(3epsilon/2)` and therefore

`t/e>=3-4e²`.

For every `r>=2`, `e<=sin(pi/10)=(sqrt(5)-1)/4`, so

`t/e >= (3+sqrt(5))/2`.

Since this is the larger root of `v²-3v+1`, it follows that `t²+e²-3et>=0`, proving `c>=5/4`. Conversely, `t²<=1` and `e²-3et<=0`, so `c<=9/4`. Every paired quadratic is therefore in the domain of the first three certificates.

If r is odd and at least 3, the unpaired middle root has shift

`a_middle=3/2-sin(epsilon/2)` in `(5/4,3/2)`.

If there is an odd number of quadratic pairs, combine one with this middle factor into the certified cubic and group the remaining pairs into quartics. If there is an even number, combine two with the middle factor into the certified quintic and group the rest into quartics. The latter case starts at r=5, so there are indeed at least two pairs.

If r is even and the number of pairs is even, use quartic blocks. If it is odd, isolate the innermost pair. Write r=2h, h>=1. Its first angle is `(2h-1)pi/(4h+1)>=pi/5`, so

`a>=3/2-cos(pi/5)=(5-sqrt(5))/4>2/3`.

Its second angle is `2h*pi/(4h+1)>=2pi/5>pi/3`; hence `3/2<=b<=2`. The innermost pair fits the final certificate. All remaining pairs group into quartics.

Apart from its positive scalar leading coefficient `2^r`, every W_r with r>=2 is now a product of certified strict blocks. Strict product closure proves the cone theorem.

## Strict consecutive ordering

The sequence W_r satisfies `W_(r+1)=zW_r-W_(r-1)`, with `W_0=1` and `W_1=z-1`. Its Christoffel–Darboux identity has the same coefficient form as for the u_r sequence. Taking Fourier coefficients gives

`H(W_(r+1))_(n+1) H(W_r)_n-H(W_(r+1))_n H(W_r)_(n+1)`

`=2 sum_(j=0)^r delta_(H(W_j))(n)`.

The initial defect rows are

`delta(H(W_0))=(1)`,

`delta(H(W_1))=(-4,4)`,

`H(W_2)=(13,10,4)`,

`delta(H(W_2))=(21,32,16)`.

All later defect rows are strictly positive on support by the theorem. For r>=2 the resulting minor is at least 36 at n=0, at least 8 at n=1, and at least `2*4^n` at `2<=n<=r`, using the terminal defect of W_n. This proves strict consecutive MLR.

## Correct difference identity and applicability limit

For r>=1, the exact difference is

`W_r-W_(r-1)=(z-2)u_(r-1)=(2x+1)u_(r-1)`.

**It is not `2(x+1)u_(r-1)`.** Consequently, for r>=3, subtracting the narrower row H(W_(r-1)) from H(W_r) yields

`H(W_r) <_lr H((2x+1)u_(r-1))`,

with strictly positive adjacent minors for `0<=n<r` (both rows have degree r).

This is a useful comparison, but the factor `2x+1` is itself not in the folded cone. No multiplication by an unproved common kernel is used here. In particular the identity cannot be replaced by the incorrect `2(x+1)` factor to claim an all-even-ray solution of the original Local TP2 problem.
