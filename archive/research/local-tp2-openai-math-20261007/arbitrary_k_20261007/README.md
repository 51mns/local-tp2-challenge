# Strict Local TP2 for all L^m R^k L^ell

**Primary status: PROVED_INTERNAL.** For every `m,k,ell>=0`, the original
supported Local TP2 minors at the canonical state `L^mR^kL^ell` are
strictly positive, including the terminal minor. This extends the preceding
`k=2` theorem to every middle right-run length. Full canonical-tree Local
TP2 remains open.

Read the [Japanese result](RESULT_JA.md), the [complete theorem and proof](arbk_root/GENERIC_ARBITRARY_K_CLOSURE.md),
and the [exact infinite-parameter coverage](arbk_root/SCALAR_COVERAGE.md).
The [dependency record](DEPENDENCIES.md) fixes every inherited research
snapshot and explains the role of the original `openai/math` investigation.

## Proof structure

The new actual-midpoint identity turns the mixed correction into a
subtraction of relative size `O(s^-2)`. A normalized all-minor theorem
converts coefficient domination into the required compatibility of every
ordered folded-kernel minor. Positive old-ray seed recurrences provide
mass-scale domination of both fixed corrections. Together with normalized
trace blocks this proves every remaining final left-run length.

The full `(m,k)` range is covered by an analytic region `m>=70,k>=3`,
70 separately certified fixed-m tails, and exactly 34 remaining starting
prefixes. The latter receive continuum certificates that themselves
propagate through every final left length. No finite-to-infinite
extrapolation is used.

The package contains independent reconstructions of the new certificates:
original ordinary-x mutations versus Laurent recurrences, exact tensor
interpolation versus symbolic polynomial arithmetic, and full tensor
expansion versus symmetry histograms. All source and output bytes are
fixed by the manifests. The reviews are separate implementations and
mathematical checks in one shared session, not external or blind review.

## Reproduce

From this directory, in a terminal with Python 3.11 or newer:

```bash
python3 reproduce.py
```

Only the Python standard library is required. The command checks the fixed
package, decompresses the large certificates in a temporary directory,
and runs all **12** new author/audit programs in dependency order. Each
regenerated JSON must match the saved exact SHA-256 byte hash. It then
writes `REPLAY_RESULT.json` beside this README. The saved source and
certificates are not modified by the replay.

The inherited foundation packages have their own fixed prior replay
records. This command replays the new proof's certificates and audits;
it does not formally verify the prose proof or silently claim to reprove
all inherited mathematics by running finite programs.

Large JSON certificates are stored as deterministic `.json.gz` files.
`COMPRESSED_CERTIFICATES.json` records both compressed and original byte
hashes. `FILE_MANIFEST.json` fixes all package files except itself and the
final replay/remote verification records, whose roles are explicitly
listed there. Exact parameters and input hashes are recorded by the
individual generators. `RUN_CONTEXT.json` fixes the campaign baseline,
arithmetic, dependency scope, and status limitations.

## Main files

| Purpose | File |
|---|---|
| Original full three-run theorem | `arbk_root/GENERIC_ARBITRARY_K_CLOSURE.md` |
| Infinite m/k partition and scalar gates | `arbk_root/SCALAR_COVERAGE.md` |
| Positive seeds and mass domination | `arbk_audit/ARBITRARY_K_POSITIVE_SEEDS_AND_MASS.md` |
| Normalized all-minor lemma | `arbk_audit/NORMALIZED_ALL_MINOR_AUDIT.md` |
| Actual-midpoint subtraction lemma | `arbk_audit/MIDPOINT_SUBTRACTION_AUDIT.md` |
| Normalized trace blocks | `arbk_mixed/NORMALIZED_BLOCKS.md` |
| Finite mixed templates | `arbk_mixed/FINITE_MIXED_KERNELS.md` |
| Independent closure/scalar audit | `arbk_audit/GENERIC_CLOSURE_AND_SCALAR_AUDIT.md` |
| Independent finite mixed audit | `arbk_root/FINITE_MIXED_INDEPENDENT_AUDIT.md` |
| Independent normalized-block audit | `arbk_seed/AUDIT_NORMALIZED_BLOCKS.md` |
| Auxiliary all-length seed half-defect theorem | `arbk_seed/ALL_K_SEED_THEOREM.md` |

The theorem is lane-local private research. No canonical-main integration,
formal proof-assistant verification, novelty claim, or external
reproduction is asserted.
