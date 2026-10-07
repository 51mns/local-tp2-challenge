# Independent audit of the fixed-inner-index one-turn kernel theorem

**PASS.** This audit concerns `general_one_turn_kernel_theorem.md` at
the fixed inner index `m=2`, for every outer index `k>=0`. No gap was
found in the arithmetic certificates, the reduction of infinitely many
kernel minors, or the subsequent compatibility and resolvent argument.
The conclusion is folded-cone membership of `q_k,Z_k,yZ_k` on `L²R^k`;
it does not itself prove Local TP2 or a theorem for every inner index.

## Independent exact arithmetic

The standalone `general_one_turn_kernel_audit.py` imports no producer
or its helpers. It constructs the polynomials directly in the Laurent
variable `q`, with coefficients in a rational ring of three independent
parameters, using `x=q+q^-1`. Its results are saved in
`general_one_turn_kernel_audit.json`.

The replay verifies:

- All **64 exported defect polynomials and 204 Bernstein coefficients**
  for the nine block families, including the exceptional small increments.
- Strict positivity of the supported half-rows, through **108** additional
  parameter Bernstein coefficients.
- The exact set of **1,543** representative positive `K_B` minors.
- Every corresponding polynomial `det K_H-4det K_B`, reconstructing
  **41,661** Bernstein coefficients and checking them all positive.

Each exported power polynomial is compared to an independently computed
Laurent defect. Bernstein conversion is also reversed into the power
basis, so the certificates are exact identities on their entire cubes.
The relative-pattern records export bounds rather than complete arrays;
the audit reconstructs the full arrays itself and checks every recorded
degree and minimum. The common minimum is exactly

`327364154597925`, at rows `(0,1)` and columns `(0,1)`.

## Why the finite index set is complete

Here `H(B)=(4,2)`, so `K_B` is nonnegative with bandwidth one and is
TP2. The degree of the midpoint polynomial `H` is eleven. For an
ordered two-by-two minor with rows `i<j` and columns `k<l`, positivity
of the `B` determinant implies its diagonal product is positive.
Therefore necessarily

`k=i+e`, `l=j+f`, `e,f in {-1,0,1}`.

This implication uses only nonnegativity of kernel entries and does
not assume a positivity pattern from the generator.

Let `d=j-i`. If `i>13`, subtract `i-13` from every index. All resulting
indices are positive, and the smallest possible Hankel index is
`2*13-1=25>11`. Before and after the shift both kernels therefore
use only their Toeplitz terms. Every row-column difference is unchanged,
so both determinants are exactly unchanged.

If `d>13`, replace `d` by thirteen while keeping `i,e,f` fixed. Each
off-diagonal distance is then at least `13-1=12>11`, so both
off-diagonal entries vanish in both kernels. The lower diagonal
indices are positive, with sum at least twenty-five; its entry is
the Toeplitz coefficient indexed by `|f|`, independently of `d`.
The upper diagonal entry does not change. Hence both determinants are
again exactly preserved. This remains valid when the upper row or
column index is zero: only the unchanged upper diagonal entry then
uses the special folded boundary convention.

Both operations preserve ordered columns: after the gap replacement,
`l-k=13+f-e>=11`. They also preserve nonnegative indices. Applying
them successively puts every positive `B` minor in the enumerated
range `0<=i<=13`, `1<=d<=13`. The audit independently regenerates
that complete range, removes invalid column pairs, and confirms the
set of positive `B` patterns exactly matches all 1,543 exported entries.

If a `B` minor is zero, the desired relative inequality follows from
the separately certified TP2 of `K_H`. Negative `B` minors do not
occur. These observations exhaust all infinite-kernel ordered minors.

## Compatibility and all outer indices

For the two reduced summands `F,G`, their midpoint is
`H_(r,s,(r+s)/2)` and their difference is `(r-s)B`. Direct polarization
of a two-by-two determinant gives

`mixed(K_F,K_G)=2det K_H-((r-s)^2/2)det K_B`.

The interval bound `|r-s|<=4` and the proved relative bound make this
nonnegative. Multiplication by a common cone factor preserves these
mixed minors by coefficient extraction from Cauchy--Binet. Thus the
proof controls the off-diagonal terms in the resolvent mixture; it
does not incorrectly infer positive-sum closure from individual cone
membership.

The earlier Jacobi-resolvent result supplies simple roots in `[-2,2]`,
positive residues with sum one, and monic denominator polynomials
for both outer sequences. No leading constant is missing in the
factored summands. Every summand in a given mixture has the same
degree. Its strict supported defects, together with nonnegative
mixed minors, therefore give strict supported defects of the mixture.

For `q_k` with `k>=3`, two distinct summands have exactly `k-2>=1`
common omitted-root factors. The extra factor `y` can consequently
be absorbed into one certified `y(t-r)` factor. The small cases
`k=0,1,2` are independently certified as `yA`, `yL_0`, and
`y[A(t²-1)+Bt]`; no unsupported multiplication by `y` is used.

The even and odd prefix factorizations are algebraically correct.
For `yZ_k`, the outside factor is nonconstant at every `k>=2`, allowing
the same absorption. The two remaining cases are exactly `yA` and
`yL_(-1)`, both within the exported certificates. This completes the
unbounded outer-index argument with all boundary cases covered.

## Review of the subsequent original-comparison theorem

The assembled `general_one_turn_m2.md` was reviewed separately after
the kernel audit. Its claim is precisely original strict Local TP2 at
every `L²R^k`, `k>=0`; it does not claim arbitrary initial run lengths.
The logical assembly and support accounting pass review, using the
separately supplied interval-margin certificates and fixed numerical
tables without duplicating their arithmetic replay.

For `k>=1`, the degrees are

`deg S=4k+8`, `deg proxy=4k+9`, `deg D=8k+5`.

Thus the proxy has exactly one further coefficient beyond `S`, and
`D` covers that coefficient even at `k=1`. The terminal determinant
is consequently positive; no division by a zero tail coefficient is
needed. The state `k=0` is the previously proved all-left state `L²`.

Each resolvent summand has one template factor and exactly `k-1`
root factors. The certified mass ratios `800` and `4` therefore give
`800*4^(k-1)` for each summand. The proof correctly keeps squared
residue weights and uses `sum lambda_i^2>=1/k`. The mass comparison
is justified by `385<Z_i(2)/T_k(2)<386`. This yields

`delta_0(Z_k)>[400*4^(k-1)/k]Z_k(2)>=400Z_k(2)`

already at `k=1`, since `4^(k-1)>=k` for every positive integer `k`.
The subsequent proxy argument only needs the weaker constant `256`,
so there is no missing small-index threshold. Its last correction
margin is strictly positive (`456`), including the highest index
where the correction polynomial is nonzero.

The uniform preliminary comparison used here is no longer conditional
at `m=2`: its sole gap-kernel premise has been discharged by the kernel
theorem audited above. Its mixture sums all use a fixed comparison
row. The multiplier and proxy strictness arguments use the same valid
Cauchy--Binet support selection as in the earlier mixed-ray theorem.
No remaining logical scope or support gap was found in this assembly.
