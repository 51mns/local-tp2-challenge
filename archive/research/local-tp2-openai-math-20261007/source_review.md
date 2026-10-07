# External sources and the hypotheses needed for transfer

Source baseline: `openai/math` at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, retrieved 2026-10-07. File paths and Git blob hashes are in [sources.json](sources.json).

## Search scope

The repository [README](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/README.md), [overview](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/overview.tex), and [contents](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/CONTENTS.md) were inspected. The catalogue describes 722 manuscripts in 372 families, at varying verification stages. Catalogue searches included total positivity, TP2, Lorentzian, log-concavity, real-rootedness, Markov polynomials, cluster algebras, Chebyshev, determinantal, stability, and Rayleigh. No direct Local TP2 theorem was located in this scoped search. This is not a full audit of all manuscripts.

## Family 169: positive reordering and an independent identification

*Elementary positivity of chromatic quasisymmetric functions*, September 24, 2026. Read the [introduction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/01-introduction.tex) and the following sections.

| Pinned section | Labels | Hypothesis or mechanism |
|---|---|---|
| [§3 Reordering](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/03-reordering.tex) | `alg:reordering`, `alg:strings` | Admissible elementary quantum units, finite multiplicities, ordered rays with positive alternating pairing; opposite-order factorization has nonnegative multiplicities. |
| [§4 Walls](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/04-walls.tex) | `wall:unit`, `wall:recursion`, `wall:positivity` | Signed pairing controls positivity of jumps; a target-dependent finite recursion transports independently nonnegative incoming coefficients. |
| [§5 Identification](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/build/sections/05-triangle.tex) | `tri:domination`, `tri:monomial` | A positive power bounds support before subtraction; a minimal-height contradiction then identifies the target with a theta section. |

**Our transfer requirement:** identify the Local TP2 minor itself with positive incoming data, without using TP2. The attempted centered-torus lifts either fail monomial positivity or re-express the target. The commutator requires finite quantum-integer positivity, not merely Laurent positivity. The manuscript's infinite Weyl strings are not these finite characters. See [the algebraic attempt](quantum_applicability.md).

## Family 114: Lorentzian coefficient inequalities

*Approximate counting of common bases of two matroids*, September 23, 2026. Read [the full source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/build/main.tex), especially §3, `thm:BH` and `lem:coefficient`.

The manuscript uses a particular Lorentzian matroid-rank polynomial, derivatives, and nonnegative substitutions. Quadratic Hessians have at most one positive eigenvalue. A Schur-complement argument yields inequalities between paired occupancy coefficients, including `4 c_ij c_ji <= z^2` and `c_ij c_jk <= z c_ik`. These statements have a concrete matroid model as a hypothesis.

**Our transfer requirement:** construct such a signature-controlled state model and identify its coefficients with the Fourier quantities. The ordinary homogenization of the actual root H(S) already has a positive-definite derivative Hessian, so that specific lift is ineligible. This says nothing about every possible normalization or larger model. See [the root proof](lorentzian_obstruction.md).

## Family 231: stable laws and response estimates

*The free uniform spanning forest is a factor of IID*, September 25, 2026. Read the [introduction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/introduction.tex), [Strongly Rayleigh section](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/strongly-rayleigh.tex), and [weighted-tree response section](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/build/sections/response.tex).

The response derivative is a covariance. For the stated stable/tree models, the absolute row sum is at most `2p_i(1-p_i) <= 1/2`. Symmetric homogenization and negative covariance representations are available under their hypotheses. The source does not assert a Fourier-folded monotone-likelihood-ratio theorem.

**Our transfer requirement:** a stable model whose actual two-coordinate section equals `G_n=s_(n+1)+s_n z+d_(n+1)w+d_n zw`, with nondegeneracy for strictness. The univariate ordinary-count lift is obstructed on the entire canonical tree by a cyclotomic factor. An explicit stable signed-count model disproves automatic folded TP2. The response magnitude bound by itself does not fix the covariance sign. See [the full proofs](rayleigh_transfer_audit.md).

## Family 180: paired-state cancellation

*Paired states and Hamiltonian cycles in cubic bipartite planar graphs*, September 24, 2026. Read [the full source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/build/paper.tex), especially §5.

The proof pairs cyclic configurations by a weight-preserving sign-reversing involution, regroups by undirected cycles, and obtains a common phase and positive magnitude in the first nonzero Taylor degree. That establishes a nonvanishing conclusion.

**Our transfer requirement:** an involution or injection preserving each requested Fourier index, with positive remaining states for every minor. Positive leading order alone does not prove all indexed coefficients positive. No such canonical correspondence was constructed in this attempt.

## Relationship to prior private research

The fixed private baseline is `a36fbac460073bf757434f122e721dfa254e8e48`. [The prior character reduction](../local-tp2-coefficient-geometry-20261003/recovery_fulltree_bivariate_character.md), [positive transfer model](../local-tp2-coefficient-geometry-20261003/fulltree_kernel_positive_transfer.md), and [direct exchange reduction](../local-tp2-coefficient-geometry-20261003/fulltree_direct_exchange.md) already isolate a relative ordering problem beyond ordinary coefficient positivity. The new quantum dictionary is a different expression of that residual problem, not a new positive closure theorem.

All mathematical deductions made for Local TP2 are stated separately from the external source theorems. This investigation does not certify the cited manuscripts globally and does not promote any private canonical claim.
