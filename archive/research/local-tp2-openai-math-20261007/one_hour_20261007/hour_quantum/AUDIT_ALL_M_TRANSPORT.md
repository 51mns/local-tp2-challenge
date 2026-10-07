# Independent audit of the uniform trace and mixed-kernel transport

**Verdict: PASS.** The theorems in
`hour_transport/all_m_trace_transport.md` and
`hour_transport/all_m_mixed_transport.md` are valid under their explicitly
cited, previously proved folded-kernel and prefix inputs. The new
subtraction, normalization, coefficient domination, analytic tails,
finite parameter bridges, and relative-minor conclusions were checked.
No circular assumption of a later Local TP2 conclusion was found.

The scope of this verdict is the raw and smoothed trace/single/midpoint
kernel theorems at every `L^mR²` seed and their stated unbounded Jacobi
transport. Returning those kernels to the original `F_n` requires the
separate initial-order and final-comparison arguments; the transport
notes correctly distinguish those obligations.

## 1. Separate exact reconstruction of every finite certificate

`audit_all_m_transport.py` imports no implementation from the author
directory. It reconstructs the actual canonical state `L^m`, its first
right child, and its second right child by the original mutations. Its
ordinary polynomial multiplication uses Karatsuba; Fourier half-rows are
obtained by Horner iteration of multiplication by `q+q^-1`. The parameter
blocks are constructed through generic multiplication in a polynomial
ring, rather than by importing the author's component formulas.

Its Bernstein implementation uses a separate route: after explicitly
checking degree at most two in each active parameter, it reconstructs
the tensor Bernstein coefficients from exact values at `0,1/2,1` on
each axis. The interpolation is exact under the checked degree bound;
the verifier tests the resulting Bernstein coefficients, so it does
not substitute grid sampling for a continuum certificate.

The following comparisons all passed:

| Obligation | Exact values independently reproduced |
|---|---:|
| Raw/smoothed trace exceptional cases | 66 Bernstein coefficients |
| Single/midpoint parameter bridge, `m=0,...,53` | 635,688 positive scaled Bernstein coefficients |
| Normalized single/midpoint bounds on that bridge | 37,368 supported inequalities |
| Normalized trace initial range, `m=0,...,20` | 21 exact scalar comparisons |
| Analytic-tail and reference-strength gates | All displayed exact rational gates |

For every one of the 216 single/midpoint parameter cases, the independent
implementation matched the minimum at **every supported output index**
and the SHA-256 digest of the complete ordered coefficient list. The
trace exception arrays matched entry by entry, including their zero
terminal strength margins. Results are in
`audit_all_m_transport_results.json`.

## 2. Trace identity and finite-degree subtraction

The exact canonical identity

\[
t_{X_m}=t_{g_m}t_{g_{m+1}}-y(x+3)
\]

follows directly by expansion of the original right mutation. Its raw
correction half-row after shifting by `r` is `(c,4,1)`, `c=5+r`, and
its smoothed correction is `(c+8,c+5,5,1)`. Both are correct.

The two subtraction lemmas were checked at every affected index.
For the raw lemma, the loss of 15 in strength follows from the displayed
exact defect changes. In particular, the central change is minimized
at `c=7`, because its derivative is `-2h_0-h_2+2c+1<0` under `L>15`.
The bound becomes `-15h_0+9h_1+24`, as stated. The remaining changes
cost at most 8, 2, and 0 times the corresponding row entries.

For the smoothed lemma, the constants in the exact changes are
`-c²+c+54`, `c²+6c-35`, `19-c`, and 1. Their stated interval
bounds are correct. Decrease of the dominant row gives the losses
35, 20, 10, and 2, with the positive remaining terms covering the
small constant `-8` at index 1. The assumptions `L>35` and positive
supported entries give every required strict positivity condition.

Both lemmas include the reflected central index and the last supported
indices. Entries beyond the support are zero; no missing boundary
correction changes the formulas. The lemmas do not require the
subtracted correction to be in the folded cone.

## 3. Improved unshifted strengths and all-m trace conclusion

The two new unshifted strengths correctly use the previously proved
inputs `y²T_j` of strength `2^j` and `y³T_j` of strength `2^(j-1)`.
The exact additive rows are `(3,2)` and `(7,5,2)`, respectively.
Expanding their defects reproduces the displayed low-index margins.

For the smoothed case, the additional inequality `h_0<=2h_1` follows
from writing `h=H(yQ)` with a nonnegative half-row for `Q=y²T_j`:
`h_0=p_0+2p_1` and `h_1=p_0+p_1+p_2`. This is the correct extra
input for the index-1 estimate. The stated ranges `j>=1` and `j>=2`
ensure all referenced low entries are supported and the strength
constants are positive.

Multiplicative strength and the two subtraction lemmas then give

\[
\kappa_m=18\,4^m-18\,2^m-11\quad(m\ge1),
\]

and

\[
\widetilde\kappa_m=9\,4^m-21\,2^m-25\quad(m\ge2).
\]

Their first values are correctly 25 and 35. The exceptional cases
use strengths 18, 18, and 72. A zero terminal margin in those
certificates does not remove strict supported defects: the positive
strength times the positive terminal coefficient remains positive.

## 4. Normalized trace retention

The raw subtraction lemma also yields the finer estimate

\[
\delta_n(\tau-r)\ge\delta_n(t_mt_{m+1})-15H(t_mt_{m+1})_n.
\]

For `m>=1`, the product strength is at least 40, so this retains
at least one half of each defect. The correction row is nonnegative,
and the resulting row is positive; therefore the half-retention
passes to normalized defects as well.

For `m>=21`, applying the inherited normalized trace bounds to both
factors, then the product denominator `2(m+3)`, and then the factor
one half gives precisely

\[
\eta(\tau-r)\ge\frac{c_0^2\sigma^{2m+1}}{16(m+3)}.
\]

The finite scalar bridge is valid. Indeed `t_j(2)<=5·7^(j+1)` implies
`(tau-r)(2)<=25·7^(2m+3)`, because the subtracted mass is at least
13. Strength gives `eta>=kappa_m/H_0>=kappa_m/mass`. All 21 scalar
comparisons to the target were independently reproduced.

## 5. Dominant single and midpoint constants

The uniform seed theorem supplies strengths `(9/32)8^m` and
normalized lower bound
`c_0³ sigma^(3m+1)/(128(m+3)²)` for both `A,yA`.
Each new trace factor contributes strength `kappa_m` and normalized
lower bound from Section 4. Every normalized product denominator is
at most `4(m+3)`, including `m=0`.

The resulting denominators are correctly

\[
128\cdot16\cdot4=8192,
\qquad 8192\cdot16\cdot4=524288,
\]

with powers `(m+3)^4` and `(m+3)^6`, and exponents `5m+2` and
`7m+3`. Thus both normalized dominant-product estimates are correctly
scaled, and the single bound is at least the midpoint bound.

## 6. Coefficient domination of the corrections

The inequalities `u_m<=B=u_(m+1)` and `a_X>=t_mB` are valid in the
ordinary coefficient basis. Multiplication by nonnegative Laurent
polynomials preserves coefficientwise order. The two central
convolution terms therefore give

\[
H(A)\ge(\rho_m^2-1)H(B),\qquad\rho_m=H(t_m)_0.
\]

The same statement survives multiplication by `y`. Shifting `tau`
changes only its central half-row entry, so
`H(tau-c)<=5H(tau-s)` follows from `theta_m>=3`. This factor five
correctly covers the independent midpoint correction parameter.

Combining the above inequalities gives

\[
H(G)\le
\frac5{(\rho_m^2-1)(\theta_m-2)}H(F)
\]

for both single and midpoint corrections, raw or smoothed. The
inherited bound `rho_m>=27·6^m/(2m+5)` and the exact trace identity
give the stated quarter-product denominator and hence

\[
\epsilon_m=
\frac{20(2m+5)^3(2m+7)}{27^4\,6^{4m+1}}.
\]

The extra `6^(-4m)` decay is justified by actual coefficient
domination, not inferred from total mass alone. That distinction is
essential for the subsequent perturbation inequality.

## 7. Analytic tail and finite normalized parameter bounds

Expanding `delta(F+G)`, dropping positive terms, and using
`0<=G<=epsilon F`, decrease, and log-concavity of `H(F)` gives

\[
\delta_n(F+G)\ge\delta_n(F)
-(4\epsilon+2\epsilon^2)H(F)_n^2.
\]

The estimate is valid at index zero and the upper support boundary.
`E_H>=12epsilon` and `epsilon<1` therefore retain half the dominant
defect. The bound `H(F+G)<=2H(F)` then gives precisely one quarter
of the strength and one eighth of the normalized defect. These are
the theorem's constants `9/128`, 65,536, and 4,194,304.

The exact starting inequality at `m=54`, its failure at 53 for this
particular bound, and the consecutive ratio greater than 27 were
independently reproduced. Every nonconstant factor in that ratio
increases with `m`; `epsilon_m` decreases. The tail therefore has
no unverified finite gap.

On the finite bridge, each row entry is nonincreasing in every
shift parameter because its derivative is a nonpositive product of
positive factors. Its maximum is consequently the all-minus-two
parameter value. The strength-margin Bernstein minimum divided by
`128·2^dimension·h_max²` is a valid normalized-defect bound. All
37,368 such inequalities were independently checked.

## 8. Relative strength and unbounded compatible mixtures

For `m>=2`, `kappa_m>=9·4^m`. Therefore the dominant midpoint
strength after the quarter loss exceeds
`(729/128)128^m`, which already exceeds `24·7^(m+1)` at `m=2`
and grows relative to it by `128/7`. Since
`8H(yB)_0<=24·7^(m+1)`, the stated reference-strength requirement
follows throughout the tail. The finite bridge uses the exact maximum
in the theorem and includes `m=0,1`.

Coefficientwise domination of `B` and `yB` is valid: the factors
`tau-r` have positive ordinary coefficients and constant coefficient
at least one. One direct all-m identity is
`tau-r=3y²a_X+(2x+3-r)`, whose terms are nonnegative on the parameter
interval. Both reference rows are decreasing by the established
Chebyshev-ray theorem. Hence the all-minor relative-strength theorem
applies with the exact required constants.

The polarized determinant identity and `|r-s|<=4` give nonnegative
mixed minors. Common-factor Cauchy–Binet preserves that property.
The Jacobi resolvent then yields positive mixtures with positive
squared-residue diagonal contributions at every supported defect.
The smoothed version uses the separately proved `yL,yH` data, and
the degree-zero case uses the uniform seed theorem. There is no
assumption that `y` itself is in the folded cone and no missing small
outer-index exception.

These checks establish the full stated transport dependencies for
every initial index and every spectral run length. The independent
audit is internal to this research session; it is not an external
publication or formal proof-assistant verification.

