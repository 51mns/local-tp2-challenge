# Local TP2: coefficient geometry continuation

## Latest audited result

**Strict original Local TP2 is proved on all five infinite canonical families
`L^k`, `R^k`, `LR^k`, `RL^k`, and `L^2R^k`, for every `k>=0`. The universal tree claim
remains unproved. Positive first-difference support is proved for the entire tree.**

- `ONE_TURN_RESULT_JA.md`: current Japanese result, scope, and remaining work.
- `mixed_kernel_sharp_strength.md`: exponential strength bounds for all pure-left
  prefixes/propagators and relative domination for the dominant one-turn product.
- `mixed_kernel_sharp_strength_independent.py`: independent replay of all 101 arrays.
- `mixed_kernel_cross_tail.md` and `general_one_turn_upper_band_audit.md`: exact
  quantitative absorption of the negative cross term in the supported upper band.
- `general_one_turn_open_gap.md`: explicit remaining conditions for arbitrary inner m;
  solving the midpoint low band alone is not claimed to finish the whole problem.
- `general_one_turn_m2.md`: complete strict original Local TP2 proof for all `L^2R^k`.
- `general_one_turn_kernel_theorem.md`: relative-compatible resolvent kernels,
  with an exact infinite-index reduction to 1,543 representative minors.
- `general_one_turn_kernel_audit.py`: independent reconstruction of 41,661
  relative-minor Bernstein coefficients and all supporting kernel certificates.
- `general_one_turn_m2_full_audit.md` / `.py`: complete mathematical audit and
  independent fixed-row and interval-margin reconstruction.
- `general_one_turn_first.md` and `general_one_turn_reduction.md`: unconditional
  initial comparisons for every inner run length; later propagation is conditional.
- `mixed_kernel_pureleft_multiplier.md` and `mixed_kernel_pureleft_centers.md`:
  uniform infinite strength and sufficient-cone theorems for pure-left boundaries.
- `mixed_kernel_pureleft_independent.py`: independent replay of both packages.
- `MIXED_RESULT_JA.md`: preceding two mixed-ray result and general-tree reductions.
- `mixed_ray_all.md`: complete original Local TP2 proof for both mixed rays.
- `mixed_ray_kernel_theorem.md`: compatible Jacobi-resolvent kernel proof.
- `mixed_ray_full_audit.md`: independent mathematical assembly audit.
- `mixed_ray_kernel_independent.py`: independent direct Laurent reconstruction
  of 105 defect arrays in 17 blocks and four continuum mass-margin arrays.
- `mixed_ray_fixed_independent.py`: independent fixed-table/scalar audit.
- `mixed_ray_bases.py`: dual exact reconstruction of six original bases and
  all 81 required strict minors.
- `mixed_first_sandwich.md`, `mixed_kernel_strong_cone.md`, and
  `mixed_second_sandwich.md`: general lemmas and explicitly conditional routes.
- `mixed_invariant_audit.md`, `mixed_kernel_closure_obstruction.md`: exact
  noncanonical obstructions to overly broad closure claims.
- `RESUMED_RESULT_JA.md`: preceding complete boundary-ray results.
- `resumed_comparison_all_left.md` and `resumed_extension_right.md`: retained
  infinite proofs for the two constant-direction rays.
- `resumed_extension_kernel_support.md`: unconditional all-tree support proof.

Run from this directory with Python 3:

```bash
python3 mixed_kernel_sharp_strength_independent.py
python3 general_one_turn_kernel_audit.py
python3 general_one_turn_m2_full_audit.py
python3 mixed_kernel_pureleft_independent.py
python3 mixed_ray_kernel_independent.py
python3 mixed_ray_fixed_independent.py
python3 mixed_ray_bases.py
```

The original mutation is preserved. No arbitrary positive-sum closure of TP2
kernels is assumed: pairwise mixed-minor compatibility is proved explicitly.
The continuum certificates and unbounded index argument are an infinite proof,
not extrapolation from a finite tree scan. Audits use independently implemented
arithmetic in a shared session; no formal or repository-level
`INDEPENDENTLY_REPRODUCED` promotion is claimed.

Earlier open-gap statements below describe historical research stages and are
superseded by this scope statement. Arbitrary mixed words remain open.

## Earlier continuation record

Primary level: `PROOF_CANDIDATE` for the partial lemmas; the universal Local TP2 claim is still unproved.

Branch: `research/local-tp2-coefficient-geometry-20261003`.
Owned path: this directory only.
Base main: `c8e61e0e398f540bc8c5de79663398d689f37473`.

The user explicitly requested on 2026-10-03 to preserve the preceding partial
results in GitHub and then continue toward a full proof. This is a direct-user
E0/E1 research continuation using coefficient kernels, transfer matrices and
combinatorial structure. It does not extend the closed QW3/far-minor ansatz
families, create a canonical numbered role, reopen an old issue, or promote
`C-LOCAL-TP2` on main.

Progress plan:
1. Preserve the existing partial proof and exact verifier on this branch.
2. Derive and falsification-check canonical interior coefficient inequalities.
3. Fix any successful proof or precise remaining obstruction, with explicit scope.

Read `REPORT.md` for the Japanese summary and `partial_audit.md` for the
all-depth proof of dense coefficient positivity and the sharp terminal bound
`F(deg S)>=24`. `kernel_proof.md` proves a general shifted-power kernel lemma
but also records why it does not directly apply to the canonical polynomials.
The other notes provide exact structural bridges, not a completed TP2 proof.

Validation (VS Code integrated terminal, from this directory):

```bash
python3 verify.py
```

This standard-library script uses exact integers and writes `results.json`.
It checks formal identities, implementation conventions and abstract negative
controls. Its depth-5 corpus is not an infinite proof.

The supporting partial audit was produced in the same research session with
the author's proposed argument visible. No blind independent review or
canonical `INDEPENDENTLY_REPRODUCED` status is claimed.

Main integration is not proposed by this exploratory preservation commit.
Repository-wide promotion validation is therefore not claimed. No hosted CI
is requested for this E0/E1 branch under `docs/CI_BUDGET_POLICY.md`.

Publication novelty: `NOT_ASSESSED`.

## Continued proof work after the initial preservation commit

The first preservation commit is `a63ae1eb1019d2ad6c0a59ba22761703fa10e3fd`.
The subsequent continuation establishes an infinite theorem for the
Chebyshev differences along the all-left ray. With
`p_m=(x+1)U_m(x+3/2)` and `a_m(n)=[q^n]p_m(q+q^-1)`, it proves

`a_m(n)a_(m+1)(n+1)-a_m(n+1)a_(m+1)(n)>0`

for every `m>=1` and `0<=n<=m+1`. This is a mathematical proof using
factorization, exact parameter-box certificates and Christoffel–Darboux;
it is not extrapolated from a depth scan.

- `continuation_kernel/folded_kernel_theorem.md`: necessary and sufficient
  criterion for folded convolution TP2, multiplicative closure, exact
  counterexamples and conditional reductions.
- `continuation_ray.md`: the infinite theorem and its precise relation to
  the remaining all-left Local TP2 comparison.
- `continuation_ray_external.md`: the strict folded-kernel theorem for
  every unweighted shifted `U_m`, and one proved actual-ray sandwich.
- `CONTINUATION_JA.md`: Japanese summary of the new results and open gap.
- `continuation_ray_certificates.json`: all exact rational Bernstein
  certificates over the continuous parameter boxes.
- `continuation_independent_audit.md`: shared-session mathematical audit;
  the accompanying script independently reconstructs Laurent coefficients
  and inverts the Bernstein transformation.
- `continuation_network.md`: matrix-gap determinant and monodromy identities,
  with a self-contained verifier and explicit failures of stronger guesses.

The original Local TP2 comparison `H(S)<_lr H(D)` remains unproved, even on
the entire all-left ray. The consecutive `p_m` theorem does not imply that
comparison automatically. No canonical claim status is changed.

Additional validation commands (VS Code integrated terminal, this directory):

```bash
python3 continuation_ray.py
python3 continuation_independent_audit.py
python3 continuation_network.py
python3 continuation_kernel/verify_folded_obstructions.py
```

The first script regenerates the certificate JSON on standard output; the
second independently verifies the saved certificates. The other scripts
check the exact structural identities and counterexamples. Recorded output
is included beside the scripts. None requires third-party packages or CI.

## Further completed prefix and bracket theorems

`continuation_prefix.md` proves folded TP2 for every adjacent sum
`U_r+U_(r-1)`, every prefix sum `T_n`, and every `(x+1)T_n` with `n>=1`.
Its audit reconstructs 14 defect polynomials and 376 Bernstein coefficients.

`continuation_bracket.md` proves **strict** folded TP2 for the actual
all-left multiplier `B_k=2+2y+3y^2 T_(k+1)` for every `k>=0`, `y=x+1`.
The proof combines quantitative Cauchy–Binet with eight residue classes of
root factorizations. Its independent implementation verifies 9 margin
polynomials and 609 Bernstein coefficients.

Together with the proved first sandwich, this leaves the explicit sufficient
comparison `H(p_(k+2))<=_lr H((x+2)B_k)` for the full all-left target.
That last comparison, and a proof over the entire canonical tree, remain open.
Having both actual factors in the folded cone does not prove their desired
comparison with `S`.

Additional validation, again from this directory:

```bash
python3 continuation_prefix_audit.py
python3 continuation_bracket_audit.py
```

The matching `*_audit.md` files explain the root bounds, residue cases,
support boundaries and strictness checks; `*_results.json` records stdout.

`continuation_difference.md` supplies a further companion theorem for
`W_r=U_r-U_(r-1)`, `r>=2`, with strict supported defects and strict consecutive
MLR. Its audit verifies 18 defect polynomials and 1453 Bernstein coefficients:

```bash
python3 continuation_difference_audit.py
```

The exact difference is `(2x+1)U_(r-1)`. Replacing this by `2(x+1)U_(r-1)`
would be an algebraic error and does not supply an even-ray Local TP2 proof.
This failed shortcut is explicitly recorded; no original-ray solution is claimed.
