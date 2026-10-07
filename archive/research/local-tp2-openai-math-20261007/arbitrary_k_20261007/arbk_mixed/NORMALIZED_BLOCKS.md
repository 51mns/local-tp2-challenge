# Uniform normalized trace blocks for the finite-m boundary

Status: PROVED_INTERNAL. Exact author certificates and the independent
mathematical and implementation audit all PASS; see
`../arbk_seed/AUDIT_NORMALIZED_BLOCKS.md`. The audit was carried out
independently in the same research session and is not an external review.
This note supplies old one-turn normalized constants, not a standalone
proof of arbitrary-word Local TP2.

Write `h_n=H(F)_n`, extend by reflection and by zero outside the support,
and set

\[
\delta_n(h)=h_n^2-h_{n-1}h_{n+1}-h_{n+1}^2+h_nh_{n+2},
\qquad \eta(F)=\min_{0\le n\le\deg F}\delta_n(h)/h_n^2.
\]

We use the established folded-cone product inequality

\[
\eta(FG)\ge
\frac{\eta(F)\eta(G)}{2(\min(\deg F,\deg G)+1)}.\tag{1}
\]

All rows used below have positive coefficients throughout their support.
Consequently the positive normalized margins also establish the cone
assumption needed in (1).

## 1. Old one-turn notation

Put `y=x+1`, `u_j=U_j(x+3/2)`, `T_j=sum_(i=0)^j u_i`, and `T_-1=0`.
For the fixed old left index `m`, let

\[
\tau=3y^2T_m+2x+3,\quad
\alpha=T_{m+1},\quad\beta=T_{m-1},\quad
R_j(t)=\sum_{i=0}^jU_i(t/2),
\quad Z_j=\alpha R_j(\tau)+\beta R_{j-1}(\tau).
\]

The established one-turn Jacobi-resolvent expansion, as recorded in
`../../one_hour_20261007/hour_transport/ARBITRARY_K_TRACE_EXPLORATORY.md`, Section 4, writes
`Z_j=sum_i omega_i F_i`, with at most `j` positive weights summing to one,

\[
F_i=[\alpha(\tau-r_i)+\beta]
       \prod_{a\ne i}(\tau-r_a),\qquad r_a\in[-2,2].\tag{2}
\]

The summands have nonnegative pairwise mixed folded minors, also after
multiplication by `y`, and satisfy `F_i>=Z_j/2` coefficientwise. Thus,
if every raw and smoothed summand has normalized margin at least `e`,
retaining the squared weights gives

\[
\eta(Z_j),\eta(yZ_j)\ge e/(4j).\tag{3}
\]

Indeed the diagonal terms contribute at least
`e sum_i omega_i^2 H(F_i)_n^2 >= e H(Z_j)_n^2/(4j)`.

## 2. The m=0 paired blocks

Here `tau=t_*=3x^2+8x+6`, `alpha=2(x+2)`, and `beta=0`, so
`Z_j=2(x+2)R_j(t_*)`. Section 7 of the cited trace note proves that the
`j` roots of `R_j` can be divided into `floor(j/2)` pairs with nonpositive
sum, together with at most one nonpositive unpaired root. Every pair
therefore gives

\[
P(a,b)=t_*^2+a t_*+b,
\quad a\in[0,4],\quad b\in[-4,4],\tag{4}
\]

and an unpaired root gives `t_*-r`, `r in [-2,0]`.

The exact full tensor certificates in `m0_normalized_blocks.py` prove:

* A product of four independent factors (4) has `eta>=1/128`.
* Each residue `2(x+2)` times zero through three independent factors
  (4), with or without one independent factor `t_*-r`, has `eta>=1/256`,
  both raw and multiplied by `y`.

The first block has degree 16. Every listed residue has degree at most
16. Joining one further block therefore loses at most `2(16+1)=34`
in (1). There are exactly `floor(j/8)` complete blocks, giving

\[
\boxed{\eta(Z_j),\eta(yZ_j)
 \ge \frac1{256}\,4352^{-\lfloor j/8\rfloor}
 \ge \frac1{256\,3^j},\qquad j\ge0.}\tag{5}
\]

The last inequality follows from `4352=128*34<3^8`. No summand or
`1/j` loss occurs at `m=0`, since `beta=0` gives one pure product.

The implementation additionally checks the one-, two-, and three-pair
blocks at `eta=1/128`; these checks are redundant inputs. All parameter
boxes in (4) are independent. They are larger than the actual correlated
root-pair domain, so the certificate covers every spectral factorization.
The code maps `a=4u`, `b=-4+8v`, and `-r=2w`, and transforms each defect
and square into tensor Bernstein degree two on the unit cube. It checks
the transform by exact inversion. The JSON records every supported
index's minimum and an ordered digest; `--residues --full` additionally
records every tensor coefficient.

## 3. Eight independent factors for m=1,...,4

For `d=deg(tau)=m+2`, let `G=prod_(i=1)^8(tau-r_i)` with eight
independent `r_i in [-2,2]`. The exact certificates establish

\[
\eta(G)\ge D\rho_m^8,\quad D=2(8d+1),\tag{6}
\]

and certify every distinguished residue

\[
[\alpha(\tau-r_0)+\beta]\prod_{i=1}^N(\tau-r_i),
\qquad 0\le N\le7,\tag{7}
\]

raw and multiplied by `y`, with margin at least `E_m`:

| m | rho_m | E_m | D |
|---|---|---|---|
| 1 | 1/4 | 1/301 | 50 |
| 2 | 1/4 | 1/513 | 66 |
| 3 | 1/4 | 1/785 | 82 |
| 4 | 1/5 | 1/1114 | 98 |

Group the `j-1` propagators in (2) into blocks of eight and a residue
(7). Since the minimum degree in every block attachment is at most
`8d`, equations (1), (6), and (7) show

\[
\eta(F_i),\eta(yF_i)
\ge E_m\rho_m^{8\lfloor(j-1)/8\rfloor}
\ge E_m\rho_m^{j-1}.
\]

Applying (3) yields the all-length bounds

\[
\boxed{\eta(Z_j),\eta(yZ_j)
\ge\frac{E_m\rho_m^{j-1}}{4j},
\quad m=1,2,3,4,\quad j\ge1.}\tag{8}
\]

## 4. Exact symmetry compression of the full parameter boxes

`finite_m_normalized_blocks.py` certifies every full tensor coefficient;
permutation symmetry merely avoids storing the same number repeatedly.
Let `f_-=tau-2`, `f_+=tau+2`. Parametrize each factor as
`(1-u_i)f_-+u_i f_+`. For `N` identical factors, a degree-two tensor
Bernstein index has a histogram `(n0,n1,n2)`, with sum `N`.
Put `h_a=H(f_-^a f_+^(N-a))`. The tensor Bernstein coefficient of
the product of row entries with indices `n,b` is exactly

\[
2^{-n_1}\sum_{a=0}^{n_1}\binom{n_1}{a}
h_{n_0+a,n}\,h_{n_0+n_1-a,b}.\tag{9}
\]

To see this, each index zero forces both factors to use `f_-`, each
index two forces both to use `f_+`, and each index one averages the two
opposite assignments. Grouping the latter assignments by their count
gives (9). The defect is the signed sum of its four indicated products.
For the distinguished residue, the extra Bernstein index similarly
selects `(L_-,L_-)`, averages `(L_-,L_+),(L_+,L_-)`, or selects
`(L_+,L_+)`, where `L_±=alpha f_±+beta`.

The orbit multiplicity is `N!/(n0!n1!n2!)`. The implementation checks that
the sum of stored multiplicities equals `(degree+1)*3^N`, or
`(degree+1)*3^(N+1)` with a distinguished factor. Every stored coefficient
of `delta-e h^2` is strictly positive. The JSON contains all histogram
coefficients, exact denominators, multiplicities, and ordered digests.
Thus (6)--(8) are continuum proofs and do not rely on parameter sampling.

## 5. Reproduction

Run with Python's standard library:

```sh
python m0_normalized_blocks.py --residues
python finite_m_normalized_blocks.py
```

The corresponding result files are `m0_normalized_blocks_results.json`
and `finite_m_normalized_blocks_results.json`. The latter final proof
scope is precisely `m=1,...,4`; no higher-m blocks are needed.
