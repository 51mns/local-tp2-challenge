# Independent algebra review of the uniform new-seed bounds

**Verdict: PASS for the new algebraic lemmas and the analytic tail assembly.** The reviewed source is `../hour_quantum/UNIFORM_SEED_STRENGTH.md`. This shared-session review imports no author implementation or expected arrays. It checks the new subtraction lemma, the `m>=29` scalar tail, and the normalized constants `16 -> 64 -> 128`, including their inherited premises in the old `recovery_oneturn_closure.md`, Section 3. It does not claim an independent rerun of the author's 308,499 normalized finite-bridge margins.

## Subtraction lemma

For a lambda-strong row `h` and a folded-cone row `p`, both are nonincreasing. The polarization is

\[
\operatorname{Pol}_n(h,p)=2h_np_n-h_{n-1}p_{n+1}-p_{n-1}h_{n+1}
-2h_{n+1}p_{n+1}+h_np_{n+2}+p_nh_{n+2}.
\]

Dropping its three nonpositive terms and using `p_j<=p_0`, `h_(n+2)<=h_n` gives `Pol_n<=4p_0h_n`. This is valid at `n=0` with reflection and at the terminal support indices. Consequently

\[
\delta_n(F-P)\ge\delta_n(F)-4p_0h_n+\delta_n(P).
\]

For `lambda>=4p_0`, positive interval support of `F-P` gives the stated `(lambda-4p_0)` strength. For `lambda>=8p_0`, the middle loss is at most half of `delta_n(F)`. Since `0<H(F-P)_n<=h_n`, the normalized defect loses at most the same factor one half. No addition-closure assumption is involved.

## Uniform strength tail

The inherited strengths multiply to

\[
\lambda_F=(3\,2^{m-1})(3\,2^{2m-3})=\frac9{16}8^m.
\]

Both reference central coefficients are bounded by `3*7^m`, using the inner Chebyshev recurrence evaluated at `x=2`, with multiplier `7`. The exact condition needed for the half-defect subtraction is therefore

\[
9\,8^m\ge384\,7^m.
\]

It is strict at `m=29`, and its left/right ratio increases by the factor `8/7`, so the complete analytic tail is justified. The exception `yu_0=y`, which is not in the folded cone, lies inside the stated exact finite bridge and is not used in the tail argument.

## Normalized constants

The old one-turn proof gives dominant-product normalized defect

\[
E_m=\frac{c_0^2\sigma^{2m+1}}{4(m+3)},
\]

at the required analytic indices, correction size `epsilon_m=(2m+5)/(9*6^m)`, and preservation of at least half the dominant defect. Its coefficient domination applies equally after multiplication by `y`. Since `epsilon_m<1/3` for `m>=1`,

\[
\eta(G+P)\ge\frac{\eta(G)}{2(1+\epsilon_m)^2}
>\frac14\eta(G).
\]

Thus the denominator `16` in the new `a_X,ya_X` bound is valid. The existing normalized trace bound contributes a factor `1/2`, and the normalized product theorem contributes `1/[2(m+3)]`. Their combination gives denominator `64(m+3)²` for `t_m a_X` and `t_m ya_X`. The verified subtraction lemma contributes one more factor `1/2`, giving denominator `128(m+3)²` for `A_m,yA_m`.

The finite ranges stated in the source close exactly the remaining indices: `m=0,...,390` for the improved `a_X` normalization, and `m=0,...,28` for the actual seeds. The need to verify those finite bridges independently remains distinct from this algebra review.

## Separate implementation review

After this algebra review, the seed author supplied `../hour_quantum/audit_uniform_seed_finite.py`, a second implementation using original ordinary-`x` mutations, polynomial Karatsuba multiplication, and Fourier Horner evaluation. The reviewer read its full source and found that its canonical anchoring, synthetic division by `y`, reflected Fourier transformation, all-support loops, and integer cross-multiplication thresholds match the mathematical statement. It imports no primary seed implementation. Its recorded replay checks all 308,499 normalized `a_X,ya_X` margins and all 2,813 strength plus 2,813 normalized actual-seed margins. That replay is a separately implemented reconstruction by the author; this review does not recast it as an independent execution by the present reviewer.
