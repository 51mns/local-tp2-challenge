# Independent audit of the adjacent-difference theorem

## Verdict

**PASS, with strictness interpreted on supported defect differences.** For `u_r=U_r(x+3/2)` and `W_r=u_r-u_(r-1)`, every `r≥2` has a TP2 folded kernel and strictly positive defect differences at all supported indices. Consecutive W rows are strictly likelihood-ratio ordered as stated. The kernel itself has forced zero minors outside its finite band, so calling it unqualified “strictly TP2” would be too strong; the source author was asked to clarify that terminology.

No original Local TP2 subfamily is proved by these statements. In particular, this audit does not authorize the rejected substitution of `2(x+1)` for the actual factor `2x+1`.

## Certificate verification

The independent verifier `continuation_difference_audit.py` constructs the blocks directly as Laurent polynomials in q and five parameters, with `x=q+q^-1`. It imports none of the certificate-producing implementations. It computes each defect directly and expands every recorded tensor Bernstein basis back into ordinary powers.

All **18** defect polynomials and **1,453** rational Bernstein coefficients passed exact reconstruction, completeness, positivity, and minimum checks. The lower bounds match the source table exactly. Thus all four block certificates hold throughout their complete closed parameter cubes, not merely at sampled values.

Supplementary exact checks also verified 10 instances of the corrected difference identity and 52 instances of the CD identity and its quantitative bounds. Those checks supplement the unbounded proofs below.

## Roots and parameter bounds

The trigonometric identity

`U_r(cos theta)-U_(r-1)(cos theta)=cos((2r+1)theta/2)/cos(theta/2)`

gives the r distinct roots stated in the note; the apparent additional zero at `theta=pi` is canceled by the denominator and is correctly excluded.

For paired roots, set `epsilon=pi/(2r+1)`, `theta=(2j-1)epsilon`, `e=sin(epsilon/2)`, and `t=sin(theta+epsilon/2)`. Direct multiplication yields exactly

`s=3-2et`,

`c=5/4+t²+e²-3et`.

The lower-half pairing angles satisfy `theta≥epsilon` and `theta+epsilon/2≤pi/2`. Hence `t≥sin(3epsilon/2)`, and the ratio estimate

`t/e≥3-4e²≥(3+sqrt(5))/2`

is valid for every `r≥2`, using the exact value `sin(pi/10)=(sqrt(5)-1)/4`. The last constant is the larger zero of `v²-3v+1`; consequently `c≥5/4`. Also `t²≤1` and `e²-3et≤0`, giving `c≤9/4`.

For `r≥3`, `e≤sin(pi/14)<1/4`. The bound is rigorous from `sin a<a` and `pi<22/7`, since `(22/7)/14<1/4`. Thus `5/2<s≤3`. At `r=2`, the pair has exactly `s=5/2`, `c=5/4`; it is included in the closed certified domain.

For odd `r≥3`, the middle shift is `3/2-e`, strictly between `5/4` and `3/2`. The required middle-factor domain is therefore justified. The excluded index `r=1` would give shift 1 and is not silently included.

For the innermost pair when r is even, the source's angle comparisons are valid. Its lower shift is at least `(5-sqrt(5))/4>2/3`; the latter inequality follows equivalently from `49>45`. Its upper shift lies between `3/2` and 2. Thus this factor lies within the isolated-pair certificate.

## Exhaustive factor grouping

For odd r, if the number of quadratic pairs is odd, the middle factor combines with one pair into a certified cubic; the others form quartics. If the number is even, it is at least two because r≥3 and this case begins at r=5. The middle factor combines with two pairs into the certified quintic, leaving quartics. For even r, all pairs form quartics except possibly one innermost pair, handled by its separate certificate. This includes r=2.

All roots are negative, all resulting factors have positive ordinary coefficients, and the positive leading scalar is `2^r`. The certified blocks therefore have dense positive Fourier support, and strict multiplicative closure applies. Every integer r≥2 is covered.

## Christoffel–Darboux and strict ordering

The recurrence `W_(r+1)=(2x+3)W_r-W_(r-1)` has initial values `W_0=1`, `W_1=2x+2`. Its CD identity still has factor 2: the telescoping proof's initial determinant is `W_1(X)-W_1(Y)=2(X-Y)`. The changed constant in W_1 does not introduce a correction term.

The Fourier extraction gives the stated sum of defect differences. The initial defect rows `(1)`, `(-4,4)`, and `(21,32,16)` are correct. At n=0 the first three contributions sum to 18, giving the bound 36. At n=1 the positive W_1 contribution already gives bound 8. For `2≤n≤r`, choose the W_n terminal defect, exactly `4^n`, to obtain bound `2·4^n`. All other terms have the required nonnegative signs at those indices. Thus strict consecutive ordering follows for every r≥2.

## Correct difference identity and final comparison

The exact recurrence gives

`W_r-W_(r-1)=(2x+1)u_(r-1)`.

For r≥3, comparing W_r with this positive difference gives a determinant exactly equal to the determinant comparing W_(r-1) with W_r, so the claimed strict comparison holds for `0≤n<r`. Both rows have degree r. This is a valid subtraction argument because the difference has positive coefficients, as shown by its explicit factorization.

The factor `2x+1` is not a folded-cone polynomial. Replacing it by `2(x+1)`, or applying an unproved multiplication-preservation statement to it, would invalidate an application to the original problem. The source correctly disclaims that step. Original full Local TP2 remains open in this continuation.
