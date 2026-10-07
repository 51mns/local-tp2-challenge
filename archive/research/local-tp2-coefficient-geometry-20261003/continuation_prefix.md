# Chebyshev adjacent sums and prefix sums lie in the folded cone

**Later update:** The original all-left Local TP2 comparison left open at this stage is now proved in `resumed_comparison_all_left.md`, audited in `resumed_audit_all_left.md`. The full tree remains open. The earlier derivations below are retained as proof ingredients.

Throughout, `U_r` abbreviates the standard polynomial `U_r(x+3/2)`, `U_(-1)=0`, and `y=x+1`. The folded cone is the class of dense nonnegative symmetric Laurent rows whose defects `delta(n)=Delta(n)-Delta(n+1)` are nonnegative. We use the proved product-closure theorem, the proved `p_r=yU_r` cone theorem for `r>=1`, and the independently proved unweighted `U_r` cone theorem.

## Theorem

For all integers `r>=0`, `V_r=U_r+U_(r-1)` lies in the folded cone. Consequently every prefix sum `T_n=sum_(j=0)^n U_j` lies in the folded cone. Moreover `yT_n` lies in the folded cone for all `n>=1`.

All nonconstant rows in these statements have strictly positive defects throughout their full support, using the separately proved strict product closure. The later applications require only nonnegative closure.

## Four universal block certificates

Consider a quadratic `f_(s,c)=x²+s*x+c`, with

`3<=s<=4`, `5s/2-25/4<=c<=5s/2-21/4`.

Equivalently, write `s=3+u`, `c=5/4+5u/2+v`, for `u,v in [0,1]`. The following four blocks have strictly positive folded defects at every supported index:

1. A product of two such quadratics, with independent allowed parameters.
2. `(x+a)f_(s,c)`, with `3/2<=a<=2`.
3. `(x+a)(x+b)`, with `1<=a<=3/2`, `3/2<=b<=5/2`.
4. `x+a`, with `3/2<=a<=2`.

These are certified by expansion in the multivariate Bernstein basis on the full unit parameter cube. All exact rational Bernstein coefficients are positive. The standalone standard-library script `continuation_prefix.py` constructs each Fourier row, forms every defect, and calculates the exact coefficients; the complete output is `continuation_prefix_certificates.json`. Positivity on the entire parameter domain follows because Bernstein basis functions are nonnegative and sum to one. This is a finite algebraic certificate for a parameterized family, not finite numerical sampling.

## Root pairing for V_r

For `r>=1`, the trigonometric identity for `U_r+U_(r-1)` gives exactly the roots

`x_j=cos(2j*pi/(2r+1))-3/2`, `j=1,...,r`.

Let `epsilon=pi/(2r+1)`, so the two angles belonging to indices `j` and `r+1-j` sum to `pi+epsilon`. Pair each lower-half index with its partner. The corresponding two linear factors are `(x+a)(x+b)`, with

`1/2<=a<=3/2`, `3/2<=b<=5/2`.

Their sum `s=a+b` is in `[3,4]`: the cosine sum is

`-2*sin(epsilon/2)*sin(theta-epsilon/2)`,

which is nonpositive and has magnitude at most one. Their product `c=ab` satisfies

`c>=5s/2-25/4`,

because `(5/2-a)(5/2-b)>=0`. Also

`c-(5s/2-25/4)<=s²/4-5s/2+25/4=(s-5)²/4<=1`.

Thus every paired quadratic lies in the domain of the first two universal certificates.

When `r` is odd, one unpaired middle root remains. Its shift is

`a=3/2+sin(epsilon/2) in [3/2,2]`.

If the number of quadratic pairs is even, use this linear factor and group the pairs into quartics. If the number of pairs is odd, combine one quadratic with the middle linear factor into a certified cubic and group all remaining pairs into quartics.

When `r` is even and the number of pairs is even, group all pairs into quartics. When `r` is even and the number of pairs is odd, isolate the innermost pair. Write `r=2h`, `h>=1`; its lower angle is `2h*pi/(4h+1)>=pi/3`. Hence its lower shift is at least one. The two shifts are therefore in the rectangle of certificate 3. Group the remaining pairs into quartics.

Apart from its positive scalar leading coefficient `2^r`, `V_r` is now a product of the certified folded-cone blocks. Product closure proves the claim for every `r>=1`; `V_0=1` is immediate.

## Prefix sums

The exact Chebyshev identities are

`T_(2h)=U_h (U_h+U_(h-1))=U_h V_h`,

`T_(2h+1)=U_h (U_(h+1)+U_h)=U_h V_(h+1)`.

They follow from the usual product-to-sum identity for second-kind Chebyshev polynomials. The unweighted `U_h` cone theorem and the preceding `V_r` theorem imply cone membership of every `T_n`.

For `n>=2`, multiply the same factorizations by `y` and use `p_h=yU_h`, where `h=floor(n/2)>=1`. This gives cone membership of `yT_n`. For `n=1`, directly

`yT_1=2(x+1)(x+2)`,

whose Fourier row is `(8,6,2)` and whose defects are `(8,16,4)`. The omitted case `n=0` is genuinely different: `yT_0=x+1` has defect `-1` at index zero.

## Remaining original-ray obstruction

The factor `H_k=yT_k` in the original ray's `D=H_k B_k` is therefore folded-TP for every `k>=1`. The other factor is

`B_k=2+2y+3y²T_(k+1)`.

Its folded-cone membership does not follow from the prefix theorem alone: the folded cone must not be assumed closed under arbitrary positive sums. The separate note `continuation_bracket.md` now proves bracket cone membership using the exact scalar-margin reduction below. The original strict comparison with `S=yU_(k+2)` remains unresolved.

There is, however, an exact reduction of the bracket's cone question to one scalar coefficient margin. Put `P=y²T_(k+1)` and `h_n=H(P)[n]`. The multiplier `y²` has Fourier row `(3,2,1)` and defects `(4,0,1)`, so `P` is in the cone by product closure. As `B_k=3P+2(x+2)`, direct expansion gives

`delta_B(0)=9delta_P(0)+24(h_0-h_1)+12h_2+8`,

`delta_B(1)=9delta_P(1)+12(h_1-h_2)+6h_3+4`,

`delta_B(2)=9delta_P(2)-6h_3`,

`delta_B(n)=9delta_P(n)` for `n>=3`.

The cone implies symmetric unimodality of `h`, so the first two expressions are strictly positive, and the last family is nonnegative. Thus the only additional condition needed for bracket cone membership is exactly

`3delta_(y²T_(k+1))(2) >= 2H(y²T_(k+1))[3]`.

This inequality requires the specific prefix-sum structure. It does not follow for arbitrary integer folded-cone rows: cosine-shaped rows can have constant interior log-concavity defects, giving zero interior defect differences even after this convolution. It is proved strictly for the canonical prefix sums in `continuation_bracket.md`, with independently audited exact certificates. The original strict `D/S` comparison still requires an additional argument.
