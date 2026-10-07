# Independent algebra audit: normalized smoothing by `(x+1)²`

**Verdict: PASS, with the nonincreasing trace-row premise stated explicitly for the central-ratio corollary.** This is a shared-session mathematical review of the root lane's proposed lemma, not a blind, external, or formal proof audit. No author implementation or expected result arrays were imported.

Let `F` have a strict folded kernel and a positive interval half-row `f_0,...,f_d`. Write

\[
\eta(F)=\min_{0\le j\le d}\frac{\delta_j(F)}{f_j^2},
\qquad f_0\le C f_1.
\]

The latter condition forces `d>=1`; it rules out the constant-polynomial case, for which multiplying by `y²` would give a zero supported defect. A finite folded-cone row is nonnegative and nonincreasing.

The half-row of `y²=(x+1)²` is `(3,2,1)`, and its defects are `(4,0,1)`. In the Cauchy–Binet expansion of the output defect in `K_(y²)K_F`, simultaneously retaining intermediate pairs `(0,1)` and `(2,3)` gives

\[
\delta_n(y^2F)\ge4\delta_n(F)
+\det K_F[(2,3),(n,n+1)].
\tag{1}
\]

All omitted terms are nonnegative. For `n>=2`, the second minor is at least `delta_(n-2)(F)` by the folded adjacent-minor formula. This remains valid at `n=d+1,d+2`, where the first term may vanish but the second is strictly positive.

If `h=H(y²F)`, its coefficient formula is

\[
h_n=3f_n+2f_{n-1}+2f_{n+1}+f_{n-2}+f_{n+2},
\]

with reflection and zero extension. Hence

\[
h_0\le9f_0,\quad h_1\le9f_0,\quad
h_n\le9f_{n-2}\quad(n\ge2).
\]

At `n=0`, (1) gives normalized defect at least `4eta(F)/81`. At `n=1`, it gives

\[
\frac{\delta_1(y^2F)}{h_1^2}
\ge\frac{4\eta(F)f_1^2}{81f_0^2}
\ge\frac{4\eta(F)}{81C^2}.
\]

At every `n>=2` through the full output support, the second retained term gives at least `eta(F)/81`. Therefore

\[
\boxed{
\eta(y^2F)\ge\frac{\min\{1,4/C^2\}}{81}\eta(F).
}
\tag{2}
\]

In particular `C=8` gives `eta(y²F)>=eta(F)/1296`. The proof includes the last two supported output indices and the reflection at zero.

## Central-ratio propagation used to obtain `C=8`

Let a nonnegative symmetric trace row `t_i` be nonincreasing and satisfy `t_0<=4t_1`. For every input index `i`,

\[
K_t(i,0)\le4K_t(i,1).
\]

For `i=0` this is the stated hypothesis. For `i=1`, the left/right ratio is `2t_1/(t_0+t_2)<=2`; for `i>=2`, it is `2t_i/(t_(i-1)+t_(i+1))<=2`, with zero cases interpreted directly. Thus multiplication by any polynomial with a nonnegative half-row preserves the central ratio bound `h_0<=4h_1`.

If `D=A(t-r)` is such a product and `0<=H(B)<=H(D)`, then `L=D+B` satisfies

\[
h_L(0)\le2h_D(0)\le8h_D(1)\le8h_L(1).
\]

The nonincreasing trace-row premise is essential to this particular short argument and follows whenever the shifted trace has a folded-cone kernel. The single inequality `t_0<=4t_1` alone would not control all the other kernel-row ratios.
