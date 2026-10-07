# Independent audit of uniform pure-left strength and center closure

**Verdict: PASS** for both `mixed_kernel_pureleft_multiplier.md` and
`mixed_kernel_pureleft_centers.md`. Their claims are infinite canonical
subfamily theorems; neither manuscript asserts closure under arbitrary
mixed mutation.

## Independent exact reconstruction

The verifier `mixed_kernel_pureleft_independent.py` imports no symbolic,
Fourier, or Bernstein utility from the author's implementation. It
substitutes `x=q+q^-1` directly, multiplies Laurent polynomials using
rational coefficients, extracts half-rows, and independently constructs
the power and Bernstein arrays for every strength margin.

All **17 blocks and 109 complete arrays** agree exactly with the two
source artifacts. The verifier also proves positivity and symmetry of
each supported row on its full parameter cube. The sole zero lower
bound is the identically zero terminal margin of the degree-two residue
in the 4-strong certificate. This is legitimate: its row entry is
positive and its defect equals four times that entry.

The checked multiplier-certificate SHA-256 is

`c546e69d5be42ee983a109b806dccdfda5dac1a8b2ec0fbb558b34241af5afbe`.

The center-certificate SHA-256 is

`1395dc5c9bcb8048e5b43fcf9d99b9a11eae6058201f28131246b1eeb8cbec52`.

Every independent lower bound is saved in
`mixed_kernel_pureleft_independent_results.json`.

## Strength product lemma and root grouping

The quantitative adjacent-minor lemma used by the proof is valid. For
interior folded minors, the nonnegative defect sum includes both endpoint
entries `h_a,h_b`, since `b>=a+2`. The boundary cases give the same
estimate, and the first row/column use exactly delta or twice delta.
Cauchy-Binet then retains all intermediate adjacent pairs and recovers
the full product row, proving multiplication of the strengths. No
positive-sum closure is needed.

The eight residue choices agree with the established factorization
`T_m=U_floor(m/2) V_ceil(m/2)`. In particular:

- The central U-root pair has constant in `[2,9/4]` for even U degree,
  and in `[7/4,9/4]` for odd U degree with its central linear factor.
- The V residue rectangles and general-pair domains are precisely those
  already proved in the prefix/root-grouping theorem.
- The cases m modulo 8 equal to zero or one have an available quartic
  when m>=8 or m>=9. The only smaller excluded case is m=1, which is
  separately treated.
- All leading scalars are retained: a quartic has scale 16, a residue
  of degree d has scale `2^d`, and their product is `2^m`.

Thus the verified 4-strong residues multiplied by 1-strong quartics
prove `y^2 T_m` is 4-strong for every m>=2. The companion's 3-strong
residues prove `y T_m` is 3-strong for every m>=2 by the same grouping.
Continuous parameter boxes cover any correlations among the actual
roots, so no independence assumption about those roots is required.

## Shifted multiplier inequalities

The verifier independently checks the low-index defect identities as
formal polynomials in `h_0,...,h_4,c`, for
`b_0=3h_0+c`, `b_1=3h_1+2`, `b_n=3h_n` otherwise.

The manuscript's deductions from 4-strength are sound. At index zero,
the derivative of `delta_0(b)-3b_0` in c is
`3(2h_0+h_2)+2c-3>0`; its lower bound at c=1 is at least 2. At indices
one and two, monotonicity of the positive row justifies respectively
`h_2<=h_1` and `h_3<=h_2`. At every later index the unchanged quadratic
scaling gives the asserted bound. The required entries `h_0,h_2>=1`
hold for the actual integer polynomial `y^2 T_m`, m>=2.

The initial cases were also reconstructed independently over their full
parameter intervals. The minimum Bernstein coefficients of
`delta-(1/5)h` at m=0 are `(0,57/5,42/5)`. At m=1, those of
`delta-3h` are `(2,514,168,18)`. Thus both initial assertions, including
the exact boundary strength 1/5, are verified.

For the propagator conclusion, `U_k(t/2)` is monic in t and factors
without an additional scalar as
`product_j(t-2cos(j*pi/(k+1)))`. Each root parameter is in the certified
interval. Strength multiplication gives `3^k`; at k=0 the constant
polynomial 1 has strength one, as required.

## Center companion

The constant-addition formulas for `g_m=1+yT_m` and the central
formula for `yg_m=y+y^2T_m` were checked independently as polynomial
identities. The manuscript then correctly uses the 3-strong bound and
decreasing row to obtain 2-strength of g_m. Its central y-multiplied
defect is bounded below by `2h_0+h_2-1>0` using 4-strength of
`y^2 T_m`. The remaining center m=1 has exactly the stated row and
defects.

Consequently every pure-left center g_m, m>=1, belongs to the proposed
sufficient center cone F and supplies its three center hypotheses.
This conclusion is confined to the pure-left family and does not
assume that F is preserved by canonical mutation.
