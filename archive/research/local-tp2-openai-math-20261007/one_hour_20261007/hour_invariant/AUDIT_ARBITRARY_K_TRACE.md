# Independent audit of the auxiliary trace theorem at every one-turn center

**Verdict: PASS.** The source `../hour_transport/ARBITRARY_K_TRACE_EXPLORATORY.md` proves the following limited auxiliary statement: if `C` is the canonical center at `L^mR^k`, with integers `m,k>=0`, then

\[
3(x+1)C-x-r\quad\text{and}\quad
(x+1)\{3(x+1)C-x-r\}
\]

are at least **1-strong** folded-cone polynomials for every real `r in [-2,2]`. The proof treats both the `m=0` and `k=0` boundaries. This theorem is separate from the completed `L^mR²L^ell` Local TP2 proof; it is not a new dependency of that result and does not prove Local TP2 for arbitrary `L^mR^kL^ell`.

This is a shared-session internal audit by a separate agent. It is not blind, external, or formal proof verification. All new algebraic lemmas and unbounded-index arguments were checked independently. The finite certificates were independently reconstructed by `audit_arbitrary_k_trace.py`, which imports no author implementation. Its complete result is `arbitrary_k_trace_independent_audit.json`.

## 1. Central-ratio lemma

Let the first coefficients of `H(F)` be `a,b,c,d`. Cone membership of `F` gives `a>=b>=c>=d>=0`. Independent expansion gives

\[
\delta_0(yF)=-a^2+ab+4b^2-3ac-2bc-2c^2+ad+2bd
\le-a^2+ab+4b^2.
\]

If `yF` is also in the cone, this implies `b>0` and

\[
\frac ab\le\frac{1+\sqrt{17}}2<3.
\]

The nonzero constant case fails the `yF` cone premise, so it is correctly excluded. Strict cone membership is unnecessary for this particular inequality; ordinary cone membership with positive interval support suffices.

## 2. Smoothing strength and support endpoints

The two retained Cauchy–Binet terms in `K_(y²)K_F` give

\[
\delta_n(y^2F)\ge4\delta_n(F)
+\det K_F[(2,3),(n,n+1)].
\]

For `n>=2`, the second term is at least `delta_(n-2)(F)`, including the final two output indices. The output coefficient is at most `9f_(n-2)`, so lambda-strength gives the required `lambda/9` bound. At zero, the first term gives `4lambda/9`. At one, the central-ratio bound gives the sharper output bound `13f_1`, and `4lambda/13>=lambda/9`. All support boundaries therefore satisfy the claimed strength.

When applying the lemma to `F=yZ_k`, the central-ratio premise is justified because `y²Z_k` is a cone product of `y²` and `Z_k`. The proof does not assume that multiplication by `y` preserves the cone.

## 3. Fixed-addition lemmas

The reviewer independently expanded all low-index changes for

\[
3h+(a,2),\qquad
3h+(a+4,a+2,2),\qquad 1\le a\le5.
\]

They agree with the source's exact formulas. After subtracting `(3lambda-8)` times the output row, the displayed lower bounds follow from decrease, the supported lower bound `h_j>=lambda`, and, for the second family at index one, `h_0<=2h_1`. Their constant terms are positive on the whole interval; the upper support uses zero extension correctly.

The requirements `deg h>=3` and `deg h>=4` ensure that the lower coefficients used in these bounds are supported. They hold for every application here. The condition `lambda>8/3` makes the resulting strength positive. Thus both fixed additions really give `(3lambda-8)` strength; there is no general addition-closure premise.

## 4. All positive inner indices and the squared mixture weights

The prior one-turn theorem gives the common single-template strength

\[
\lambda_L=3\,2^{2m-3}
\]

and the shifted-trace strength `lambda_t=3*2^(m-1)`, for `m>=1`. The raw and smoothed spectral summands have common strength `lambda_L lambda_t^(k-1)` and the established pairwise compatibility on every ordered minor.

Since `B<=A` and a shifted trace has central coefficient greater than one, every summand lies between `A R_k` and `2A R_k`. Hence it is at least half the average row, both before and after multiplication by the Laurent-nonnegative polynomial `y`. Retaining the **squared** spectral weights, with at most `k` active weights, gives

\[
\Lambda_{m,k}=\frac{\lambda_L\lambda_t^{k-1}}{2k}
\]

as a valid common strength of `Z_k,yZ_k`. The denominator is `2k`, not `k`, and it is correctly retained in the source.

Smoothing by `y²` and then applying the fixed-addition lemma gives

\[
\kappa_{m,k}=
\frac{2^{2m-4}}k\bigl(3\,2^{m-1}\bigr)^{k-1}-8.
\]

Its first positive-region corner values are exactly `8`, `16`, `4`, and `17/8` at `(m,k)=(4,1),(3,2),(2,3),(1,6)`. For fixed `m`, the pre-subtraction factor increases by `lambda_t*k/(k+1)>=3/2`. It also increases with `m`. Thus these four corners cover all positive integer pairs except the eight stated finite exceptions, and all used strengths are at least one.

## 5. The all-right boundary: spectral pairing

At `m=0`, the exact old all-right formula is

\[
t_*=3x^2+8x+6,\quad Z_k=2(x+2)R_k(t_*),\quad C=1+yZ_k.
\]

The raw and smoothed initial factors have strengths two and one, respectively. The independently verified primitive boxes give nine-strength for `t_*²+a t_*+b` on `[0,4]×[-4,4]`, and one-strength for `t_*-r` when `-2<=r<=0`.

The exact prefix factorization is `R_(2h)=U_h V_h` or `R_(2h+1)=U_h V_(h+1)`, in monic trace notation. The `U` roots pair as opposites. The `V_h` roots are `2cos(2πj/(2h+1))`; pairing `j` with `h+1-j` gives sum

\[
4\cos\frac{\pi(h+1)}{2h+1}
\cos\frac{\pi(2j-h-1)}{2h+1}<0.
\]

The first cosine is negative and the second positive for each genuine pair. A remaining middle `V` root is negative. If there are two unpaired roots from the outside factors, one is zero and the other negative, so these may be paired as well. Thus `R_k` has exactly `floor(k/2)` allowed root pairs and at most one nonpositive singleton.

Every pair has `a=-(r+s) in [0,4]` and `b=rs in [-4,4]`, so the primitive box applies. Multiplicative strength gives `9^floor(k/2)` for both `Z_k,yZ_k`. For `k>=4`, the smoothing and fixed-addition steps give strength at least `9²/3-8=19`. Only `k=1,2,3` need additional finite certificates.

## 6. Independent complete finite reconstruction

The author's implementation uses ordinary `x` polynomials, binomial Fourier conversion, and three exact parameter values to recover quadratic Bernstein coefficients. The audit uses a different route:

1. Reconstruct the root and every required mutation directly as full Laurent polynomials in `q`.
2. Keep the shift parameter symbolic through the defect calculation in a separate polynomial ring.
3. Substitute the interval coordinates algebraically and convert power coefficients to Bernstein coefficients.
4. Check the inverse Bernstein identity and strict signs before reading the author's result arrays.
5. Compare every independently generated coefficient exactly.

The audit reproduces all of the following:

| Finite part | Coefficients | Result |
|---|---:|---|
| Eleven exceptional center pairs, raw and smoothed | 813 | All strictly positive; every array matches |
| Primitive two-parameter paired-root box | 45 | All nonnegative; nine terminal zeros; every array matches |
| Primitive nonpositive singleton interval | 9 | All strictly positive; every array matches |

The total is **867 exact Bernstein coefficients**. The nine zeros are compatible with positive nine-strength: they say that the terminal strength lower bound is attained, not that a supported defect vanishes. Every polynomial has positive interval support over its entire parameter box.

The exact tail corner strengths were also independently recalculated with `Fraction` and matched the values above. These certificates establish whole intervals and a whole rectangle using exact degree bounds; they are not sign checks on a finite grid.

## 7. The pure-left boundary and the final scope

For `k=0`, `C=g_(m+1)`. The inherited pure-left shifted-trace theorem gives strength `3*2^m`. The smoothed theorem in `recovery_oneturn_closure.md`, Section 2, applied at inner index `m+1`, gives strength `3*2^(m-1)>=3/2`. Thus the claimed one-strength bound also holds at all `k=0`, including the canonical root.

The auxiliary statement is therefore established for **all `m,k>=0` and every `r in [-2,2]`**. Its potential use is to supply new fixed-endpoint trace kernels when investigating arbitrary two-turn prefixes. It leaves the new seed compatibility, mixed templates, normalized correction domination, and strict original proxy comparison for arbitrary `k` unresolved. None of those missing assertions is inserted into the already completed `L^mR²L^ell` theorem.
