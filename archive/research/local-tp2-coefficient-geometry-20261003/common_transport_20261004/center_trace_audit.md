# Independent audit: the enlarged shifted-trace interval

**Verdict: PASS.** The sufficient `|rho|<=5/2` shifted-trace theorem,
the uniform Robin spectral interval, and the pure-propagator product
conclusion in `gap_shifted_trace.md` are valid conditional general
lemmas. They do not prove the sufficient normalized-center gate is
preserved, or that signed/nonzero advanced seed mixtures are cone
polynomials.

Audited source SHA-256:
`dc8530d2f4ae7dcb2e9c08503794fdba08eacb166f72f2381b000d3b6d8260f9`.
This audit uses the frozen folded criterion and positive-support product
theorems; the second-smoothing tail proof was independently rechecked
from `../common_closure_20261004/network_trace_audit.md`.

## 1. Central five-minor bound and the m=2 boundary

For `v=H(y^2 a)`, the relevant two columns of K_(y^2), on rows 0,...,3,
are `(3,2)`, `(4,4)`, `(2,2)`, `(0,1)`. All later rows vanish.
Their minors on pairs 01,02,03,12,13,23 are respectively
`4,2,3,0,4,2`. Thus the asserted five-minor coefficients retain the
central factor-two convention exactly.

For positive columns i<j<=m, the first-two-row minor of K_a satisfies

`W(i,j)=A_i A_j sum_(k=i)^(j-1) delta_k/(A_k A_(k+1))`.

Using `delta_k>=A_k` and monotonicity of A, its last summand supplies
A_i and each preceding one supplies at least A_j. This proves
`W(i,j)>=A_i+(j-i-1)A_j`. At j=m+1 the exact identity is instead
`W(i,m+1)=A_i A_m>=A_i`; integrality supplies A_m>=1.
This covers all three terminal-column terms when m=2. Consequently

`delta_0(v)>=9A_0+4A_1+4A_2+10A_3`

holds with A_3=0 in that smallest degree. No positive-denominator
argument is applied to a zero terminal column.

## 2. Cubic central estimate and the entire shift interval

Normalize `b=A_1/A_0`, `u=A_2/A_0`, `w=A_3/A_0`. The first two
nonnegative folded defects give

`u>=2b^2-1`, `bw>=u+u^2-b^2`.

If b>=sqrt(3)/2, then u>=1/2 and u+u^2 is increasing there, yielding
`w>=4b^3-3b`. Division by b is valid in this range. If b is smaller,
w>=0 is sufficient. Folded TP2 gives b<=1 and A_2<=A_0.

With `c=3-rho in [1/2,11/2]`, direct expansion gives

`delta_0(h)=9delta_0(v)+6cv_0-24v_1+3cv_2+c^2-8`.

The derivative in c is positive, so its worst case is c=1/2. Substituting
the five-minor bound gives exactly

`(87/2)A_0-45A_1-(3/2)A_2+69A_3+(3/2)A_4-31/4`.

After discarding only favorable terms, the normalized lower bound is
`42-45b` for b<=sqrt(3)/2 and `42-252b+276b^3` otherwise. The latter
has derivative at least 369 on the remaining interval. Both attain
their common lower bound at sqrt(3)/2.

The positive integer 1-strong row with m>=2 has A_0>=3, as the source's
explicit A_0=1,2 case split shows. Hence the final bound is
`(473-270sqrt(3))/4>0`; its positivity follows exactly from
`473^2-3*270^2=5029`. No decimal estimate is required.

## 3. Noncentral defects and both terminal indices

The first smoothing has 1-strength at indices >=1. Its separate cone
premise supplies nonnegative delta_0 only. In the second-smoothing
formula at n=1, the first minor is merely nonnegative and the remaining
four give `2u_0+u_1+u_2>=v_1`. Thus central strength of ya is not used.
At n>=2 all adjacent strength premises have indices >=1. The
penultimate and terminal direct formulas give respectively
`delta_(M-1)(u)+u_(M-1)u_M>=v_M` and `u_M^2>=v_(M+1)`.

The exact trace perturbations therefore yield

`delta_1(h)>=(9/2)v_1+6v_3+4>0`,

`delta_2(h)>=3v_2>0`, and `delta_n(h)>=9v_n>0` for n>=3.

The last expression includes degree m+2. All support remains positive
because c>=1/2. The separate use of K_(y^2) product closure is valid;
no assertion that K_y is TP2 is made.

## 4. Lower degrees, Robin factors, and exact scope

For a constant A>=2, the central minimum at A=2,c=1/2 is 245/4.
For degree one, optimal B-strength is exactly A>=2B; with B>=2,
the central minimum at A=2B=4 is 449/4. Both monotonicity steps and
the remaining displayed defects are valid throughout c<=11/2.
The excluded a=1 really has central defect -37/4 at rho=5/2.

The Robin polynomial is the characteristic polynomial of the stated
real symmetric tridiagonal matrix. For 1<rho<=2, the positive weights
rho^(-(i-1)) give weighted row sums at most rho+1/rho<=5/2, including
n=1 and the terminal row. The sign conjugation for negative rho is
correct. At rho=2 the displayed geometric-vector Rayleigh quotient
is exact, even for n=1, and proves sharpness of the uniform interval.
Each monic factor after substitution is therefore a strict shifted-trace
cone factor; inherited strict product closure proves all-depth pure
propagators.

The seed advance identity is correct with the standard convention
`U_-1=0`, needed when k=1. For d0=0 it gives cone products with the
specified seed premises. For d0 nonzero or signed, it is a correlated
sum and the proof does not assert cone closure of that sum.

The theorem genuinely removes the fixed-trace factor obstruction. Its
ROOT application to Z=2x+4 is valid. Preservation of the Z hypotheses
under Z+s and Z+s+d remains OPEN; the actual incoming-gap, multiplier,
and proxy gates remain separate. No full-tree claim is promoted by this
audit. The proof is analytical; no bounded scan is used to justify it.
