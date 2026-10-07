# Additional infinite lemmas for the actual all-left comparison

**Later update:** The original all-left Local TP2 comparison left open at this stage is now proved in `resumed_comparison_all_left.md`, audited in `resumed_audit_all_left.md`. The full tree remains open. The earlier derivations below are retained as proof ingredients.

This note uses the strict folded-kernel product theorem and the B2 certificates already established in `continuation_kernel/folded_kernel_theorem.md` and `continuation_ray.md`. The conclusions below are infinite statements, not finite-depth observations. They still do not prove the full all-left Local TP2 inequality.

Write `y=x+1`, `z=2x+3`, `u_m=U_m(x+3/2)`, `p_m=y u_m`, and `T_k=sum_{j=0}^k u_j`.

## 1. Every unweighted Chebyshev row is strictly in the folded cone

**Theorem.** The Fourier half-row of `u_m` has strictly positive decreasing-log-concavity defects `delta_n` on its entire supported range, for every integer `m>=0`.

**Proof.** Let `f_c=x²+3x+c` and `zeta=x+3/2`. Pairing opposite Chebyshev roots gives

`u_m=2^m zeta^epsilon product_j f_(c_j)`,

where `epsilon` is the parity of m and `c_j=9/4-cos²(j*pi/(m+1))` is in `[5/4,9/4]`. Two arbitrary quadratic factors can be grouped as the already certified strictly folded-TP2 block B2.

If the number of quadratic factors is odd, isolate the one with largest c. For even `m>=2`, this largest parameter is

`9/4-sin²(pi/(2(m+1))) >= 2`,

since the angle is at most `pi/6`. For odd `m>=7`, the largest parameter is

`9/4-sin²(pi/(m+1)) > 2`,

since its angle is at most `pi/8`. A singleton `f_c` with `2<=c<=9/4` is strictly in the cone: its Fourier half-row is `(c+2,3,1)` and its defects are exactly

`(c²+5c-12, 6-c, 1)`,

all positive. The remaining quadratic factors pair into B2 blocks. The optional linear factor `zeta` is also strict, with defects `(1/4,1)`.

The only remaining nontrivial case is `m=3`, where `u_3/8=zeta f_(7/4)`. Its Fourier half-row and defects are respectively

`(93/8,37/4,9/2,1)`,

`(1045/64,89/4,10,1)`.

These are positive. The cases m=0 and m=1 are the constant and the linear factor, respectively; m=5 has an even number of quadratic factors. Strict product closure proves the theorem. QED.

**Corollary (strict consecutive ordering).** For all `m>=0` and `0<=n<=m`,

`H(u_(m+1))_(n+1) H(u_m)_n-H(u_(m+1))_n H(u_m)_(n+1) >= 2*4^n > 0`.

Indeed the same Chebyshev Christoffel–Darboux coefficient identity gives the minor as `2 sum_(j=0)^m delta_(H(u_j))(n)`. Every summand is nonnegative; choose `j=n`, whose terminal defect is the square `4^n` of its leading coefficient `2^n`. There is no exceptional m=0 row.

**Consequence.** Since `y²` has nonnegative defects `(4,0,1)`, every `y² u_m` belongs to the folded cone. In particular each increment of the all-left bracket

`M_k=2+2y+3y²T_(k+1)`

is a cone polynomial:

`M_(k+1)-M_k=3y²u_(k+2)`.

This does **not** prove that M_k is in the cone: closure under addition has not been established and cannot be silently substituted for product closure.

## 2. One actual-ray sandwich premise is proved for every k

**Theorem.** For every k>=0,

`H(x+2) <=_lr H(y T_k)`.

**Proof.** The row `H(x+2)` is `(2,1)`. The rows `H(p_0)=(1,1)` and `H(p_1)=(7,5,2)` are both likelihood-ratio above it: their nonzero adjacent comparison minors are respectively `(1)` and `(3,2)`. The established consecutive-p theorem gives `H(p_j)>=_lr H(p_1)` for all j>=1. Transitivity shows every summand p_j is above x+2. For a fixed lower row, the comparison minors are linear in the upper row; adding all the p_j proves the result, since `yT_k=sum_j p_j`. QED.

This supplies one of the proposed sandwich's actual infinite premises. To finish using that sandwich still requires the appropriate cone property for M_k and

`H(p_(k+2)) <=_lr H((x+2)M_k)`.

Neither is asserted here.

Subsequent progress: `continuation_bracket.md` proves strict cone membership
of every `M_k=B_k`. Its final section also proves that the remaining comparison
need only be non-strict; the strictness of the original conclusion follows
from the strict bracket kernel. That remaining comparison is still open.

## 3. Two exact simplifications for the remaining task

First, with `u_(-1)=0`, Chebyshev addition gives

`T_(2r)=u_r(u_r+u_(r-1))`,

`T_(2r+1)=u_r(u_(r+1)+u_r)`.

The adjacent identity `u_r²+u_(r-1)²-z u_r u_(r-1)=1` then yields

`T_k T_(k+1)=(z+2)V²+(-1)^(k+1)V`,

where `V=u_r²` for `k=2r` and `V=u_r u_(r+1)` for `k=2r+1`.

Second, the identity

`y(x+2)=u_2/4`

simplifies the remaining sandwich polynomial. With `s=k+2`, set `B=(x+2)M_k`. Then

`B=2(x+2)²+(3/4)u_2 sum_(j=0)^(s-1) p_j`,

and `2(x+2)²=p_1+3p_0+2`.

Using `u_2 u_j=u_(j+2)+u_j+u_(j-2)` for j>=2, with the usual boundary exceptions, this represents B as a short weighted sum of p_j rows up to index s+1 plus a constant. The sum contains positive coefficients at indices below s, so the consecutive-p MLR theorem alone does not compare it with p_s. Those lower terms have the unfavorable determinant sign and must be quantitatively controlled.
