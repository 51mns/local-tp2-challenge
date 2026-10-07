# Mathematical audit of the all-`m`, all-`ell` second-turn theorem

**Verdict: PASS for the complete mathematical assembly**, subject to the explicitly named inherited foundation theorems and exact finite certificates. The reviewed source is `../hour_root/UNIFORM_RAY_CLOSURE.md`. The theorem proves the original strict Local TP2 inequalities on every canonical path `L^mR²L^ell`, for integers `m,ell>=0`. No arbitrary-tree or arbitrary-`k` extension is inferred.

This is a shared-session internal review by a different agent, not blind, external, or formal verification. The reviewer has independently constructed and audited the two fixed initial-index ray proofs, the general finite-ray criterion, the normalized smoothing lemma, and the all-`m` initial-order transport. The scalar tail identities below were also independently reconstructed with exact rational arithmetic; no root-lane implementation or expected result array was imported.

## 1. Canonical anchoring and support

The new seeds `A=t_0 a_X-u_m`, `B=u_(m+1)`, and the new outer trace `t=3yX-x` agree with the original canonical mutations and with the independently audited uniform-seed note. The trace identity `t=t_0 t_(m+1)-y(x+3)` uses an inner pure-left trace in its second factor; it does not confuse that inner trace with the new outer trace.

The recurrence has previous gap `-yB`, hence the plus sign in

\[
q_N=y(AU_N(t/2)+BU_{N-1}(t/2))
\]

is correct. At every `N>=1`, `X` has lower degree than the previous center, so the shorter child is the next left center and

\[
S_N=q_{N+1},\qquad D_N=(C_{N-1}-X)(3yC_N-x+1)
\]

are the actual original target rows. The single `N=0` state has the other endpoint orientation and is correctly supplied by the previous one-turn theorem.

The degree formulas are

\[
\deg S_N=(2m+5)N+5m+11,
\quad\deg D_N=(4m+10)N+4m+8.
\]

Their difference is `(2m+5)N-m-3>=m+2>0`. Thus the final original determinant is a product of two positive entries, including the terminal index.

## 2. The quoted normalized and strength inputs

The reviewer read the source notes `all_m_trace_transport.md` and `all_m_mixed_transport.md` as well as the uniform-seed note. Their constants have the correct relationship to the closure argument:

- The inner trace product normalized bound loses a factor one half under the bounded degree-two subtraction. This gives the new-trace denominator `16(m+3)`.
- The dominant single product has normalized denominator `8192(m+3)^4`. Retention of half its defect and the coefficient bound by twice its dominant row lose a further factor eight, giving the used denominator `65536(m+3)^4`.
- The smoothed trace strengths are `18`, `72`, and `9*4^m-21*2^m-25` in the stated ranges. For `m>=3`, the last is at least `(9/2)*4^m`.
- The raw and smoothed midpoint strengths meet the all-minor factor-four reference bounds. This is the hypothesis needed for pairwise compatibility, rather than an assertion that arbitrary positive sums preserve the cone.

The finite mixed certificates and their normalized refinements are distinct obligations from these algebraic checks; their independent numerical reconstruction is recorded separately when completed.

## 3. Normalized smoothing includes every boundary index

The result

\[
\eta(y^2F)\ge\eta(F)\min\{1,4/C^2\}/81
\]

was independently derived in `NORMALIZED_SMOOTHING_AUDIT.md`. The two retained Cauchy–Binet terms are compatible because all omitted minors are nonnegative. The second term supplies `delta_(n-2)(F)` at `n>=2`, including the two new terminal indices. The central-ratio assumption forces positive degree, so the constant-polynomial exception is excluded.

For the present `L_r`, `H(yX)_0<=2H(yX)_1` follows directly from nonnegative coefficients. The trace's central ratio is therefore at most four. Its cone property supplies decrease, which makes every kernel row obey the same bound. Convolution by `A`, followed by the reference domination `B<=A(t-r)`, gives the required bound eight for `L_r`. Hence `eta(y²L_r)>=E_L/1296` is valid for every relevant parameter.

## 4. The common base normalized bound

The pure-left mass estimate `g_m(2)<=4*7^m` gives

\[
t(2)\le9072\,49^m,\qquad J(2)\le27216\,49^m.
\]

Together with the smoothed strength lower bound, this proves

\[
\eta(J)\ge(4/49)^m/6048.
\]

The product denominator for `J L_r` is exactly `2(deg J+1)=4m+14`. Therefore the common lower bound

\[
E_m=E_L(m)\frac{(4/49)^m}{6048(4m+14)}
\]

is valid for `J L_r`. It is also smaller than `E_L/1296`, so the same `E_m` can safely be used for `y²L_r`.

## 5. Coefficient domination and its constant

All comparisons in this step are in the Laurent half-row basis. In particular `y²>=p` is correct there; it is not an ordinary-`x` coefficient assertion.

Set `b_m=H(t_0)_0`, `d_m=H(T_(m+1))_0`, and `s_m=H(t)_0-2`. The central convolution terms and the positive seed identities give

\[
A\ge(b_m-1)a_X\ge(b_m-1)d_mK_0,
\qquad L_r\ge(b_m-1)d_ms_mK_0.
\]

Since `J>=2y²X` and `y²>=p`, the two base corrections have respective domination factors at least `2(b_m-1)d_ms_m` and `3(b_m-1)d_ms_m`. The common conservative factor uses the smaller one.

The lower bounds

\[
b_m\ge\frac{27\,6^m}{2m+5},\quad
d_m\ge\frac{6^{m+1}}{2m+3},\quad
s_m\ge\tfrac12 b_mb_{m+1},\quad b_m-1\ge b_m/2
\]

give exactly

\[
c_m=\frac{27^3\,6^{4m+2}}
{2(2m+3)(2m+5)^2(2m+7)}.
\]

Thus `JL_r>=c_mK` and `y²L_r>=c_mK_0` are valid with no missing scalar factor. The bound for `s_m` accounts for both the trace correction's central coefficient five and the additional shift two. The resulting subtraction is seven, as required.

## 6. Mixture normalization and the infinite outer run

Each active Jacobi summand has exactly `N-1` propagators, and at most `N` positive residues occur. Their weights sum to one. Removing an active root gives

\[
Z_i=A R_N+B R_N/(t-r_i).
\]

Because `B<=A` and `H(t-r_i)_0>=s_m>1`, every summand and their mean lie between `A R_N` and `2A R_N`, coefficientwise. Common multiplication by `J` or `y²` preserves these inequalities. Thus the factor-two row comparison is uniform in `N`.

Pairwise mixed-minor compatibility makes every off-diagonal contribution to a defect nonnegative. Retaining the diagonal terms gives the exact loss

\[
\eta(F)\ge\frac{E_m}{4N}
\left(\frac{E_t(m)}{D_m}\right)^{N-1}.
\]

The factor `1/N` comes from `sum lambda_i²>=1/N`, and the factor `1/4` comes from the squared half-row comparison. Neither has been omitted.

The fixed correction satisfies `Q<=F/(c_ms_m^(N-1))` directly by averaging the individual domination inequalities. The author's weaker bound with

\[
\epsilon_N=2/(c_ms_m^{N-1})
\]

is therefore valid. It yields the stated lower bound for `eta(F)/epsilon_N`. The two conditions `E_m c_m>96` and `E_t(m)s_m/D_m>=2` imply `eta(F)>12epsilon_N` for every `N>=1`, because `2^(N-1)>=N`. The proof includes `N=1` and contains no untested run lengths.

## 7. Independent exact scalar-tail check

`uniform_tail_scalar_audit.json` records a separate reconstruction with Python `Fraction`. The constants and consecutive ratios were derived directly from their displayed formulas. At `m=77`, their approximate values, provided only for readability, are

| Quantity | Approximate value | Exact verified inequality |
|---|---:|---|
| `E_m c_m` | `165.6041915` | `>165>96` |
| Lower bound for `E_t(m)s_m/D_m` | `2.707074548e60` | `>2` |
| Consecutive ratio of `E_m c_m` | `6.7619259645` | `>6` |
| Consecutive ratio of the propagation lower bound | `11.9241101770` | `>11` |

Each consecutive-ratio formula matches exact division of the independently constructed quantities. Its variable factors are increasing, so the inequalities propagate to every `m>=77`. The bridge `0<=m<=76` and the analytic range `m>=77` meet without a gap.

## 8. The multiplier and the full ordered proxy comparison

The normalized perturbation inequality used for the multiplier is valid because the dominant `F` has a nonincreasing log-concave row, as supplied by its strict folded kernel. Its negative terms are bounded by `(4epsilon+2epsilon²)F_n²`, with reflection at zero and zero extension at the top. Together with `epsilon<=1` and `eta(F)>12epsilon`, this leaves positive defects. The correction is supported inside the dominant row by the proved coefficient domination, so it does not create an untreated support extension.

For the proxy, `R=yp²` has half-row `(14,11,5,1)`. Thus

\[
W_n(J,V-\tfrac12pJ)
\ge(\mu_m/2-14)H(J)_n\ge0.
\]

The second row is `pJ/2+R`, so it is positive and has support degree one larger than `J`. Adjacent inequalities therefore imply the **full ordered** likelihood-ratio order. Multiplication through `K_(Z_N)` gives

\[
W_n(JZ_N,VZ_N)\ge\tfrac12 W_n(JZ_N,pJZ_N)
=\tfrac12\delta_n(JZ_N).
\]

This explicitly justifies the Cauchy–Binet step at all input pairs; it is not an invalid propagation of adjacent numerical bounds alone. The fixed correction costs at most `epsilon_N F_n²`, which is strictly smaller than the retained half defect. The comparison is therefore strict throughout the support, including indices beyond the correction and the terminal index.

## 9. Initial comparisons and original conclusion

`ALL_M_INITIAL_COMPARISONS.md` derives the four initial LR links from the previously proved one-turn Local TP2, its actual gap kernels, and the existing first-child companion seeds. This avoids assuming any new two-turn target. The exact gap recurrence then gives the weak left side of the sandwich, and the now-proved actual multiplier kernel gives its weak right side.

Consequently

\[
S_N\le_{\rm lr}JZ_N<_{\rm lr}XpM_N\le_{\rm lr}D_N
\]

proves the original strict minors on the interior support. At the last index the original determinant is directly `H(S_N)_d H(D_N)_(d+1)>0`. The prior one-turn theorem supplies `ell=0` with its own correct endpoint orientation.

## Editorial corrections reported to the author

Two local wording fixes were requested; neither changes the mathematics:

1. Replace the initial-order filename `UNIFORM_INITIAL_ORDERS.md` by the actual `ALL_M_INITIAL_COMPARISONS.md`.
2. State the dominant row's nonincreasing/log-concave, or folded-cone, hypothesis explicitly when quoting the normalized perturbation inequality. That inequality is not an assertion about arbitrary nonnegative half-rows.

Both corrections were confirmed in the author's current source after the review. No unresolved mathematical amendment remains in this audit.

The final conclusion remains a proved two-parameter family under the cited foundations and verified finite bridges. It does not prove arbitrary `L^mR^kL^ell` with `k>=3` or arbitrary-tree Local TP2.
