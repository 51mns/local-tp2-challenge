# Fixed mathematical dependencies and external-method provenance

This is a private E1 research package with primary status PROVED_INTERNAL.
The independent implementations and mathematical audits were performed in
the same shared session. No main/canonical or external reproduction status
is changed by this package.

## Immediately preceding proof snapshot

Repository: `51mns/AIMath`. Commit:
[f1bf528c9064e11f79795a581b6a4bc15f0efbe1](https://github.com/51mns/AIMath/commit/f1bf528c9064e11f79795a581b6a4bc15f0efbe1).

Under `research/local-tp2-openai-math-20261007/one_hour_20261007/`:

- [Finite-ray extension criterion](https://github.com/51mns/AIMath/blob/f1bf528c9064e11f79795a581b6a4bc15f0efbe1/research/local-tp2-openai-math-20261007/one_hour_20261007/hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md).
- [All-m initial comparisons, including the all-k corollary](https://github.com/51mns/AIMath/blob/f1bf528c9064e11f79795a581b6a4bc15f0efbe1/research/local-tp2-openai-math-20261007/one_hour_20261007/hour_invariant/ALL_M_INITIAL_COMPARISONS.md).
- [Arbitrary-k one-turn shifted/smoothed trace theorem](https://github.com/51mns/AIMath/blob/f1bf528c9064e11f79795a581b6a4bc15f0efbe1/research/local-tp2-openai-math-20261007/one_hour_20261007/hour_transport/ARBITRARY_K_TRACE_EXPLORATORY.md).
- [Normalized absorption, smoothing, and completed k=2 theorem](https://github.com/51mns/AIMath/blob/f1bf528c9064e11f79795a581b6a4bc15f0efbe1/research/local-tp2-openai-math-20261007/one_hour_20261007/hour_root/UNIFORM_RAY_CLOSURE.md).

The old filename containing EXPLORATORY is retained as a historical path;
its fixed contents explicitly state the auxiliary PROVED_INTERNAL result
and identify its separate audit. The previous package's complete replay
is recorded in its own manifest and result, not silently rerun by the new
package's local certificate replay.

## Earlier foundation snapshot

Commit [a36fbac460073bf757434f122e721dfa254e8e48](https://github.com/51mns/AIMath/commit/a36fbac460073bf757434f122e721dfa254e8e48),
under `research/local-tp2-coefficient-geometry-20261003/`:

- `continuation_kernel/folded_kernel_theorem.md`: folded-kernel convention,
  cone criterion, supported/ordered minors, and product closure.
- `mixed_kernel_sharp_strength.md`, `mixed_kernel_all_minor_strength.md`:
  quantitative inherited prefix/trace and kernel bounds.
- `fulltree_oneturn_normalized_tail.md`: normalized product inequality and
  normalized prefix/trace bounds, with fixed exact block certificates.
- `recovery_oneturn_closure.md`: completed all-m one-turn theorem,
  smoothed prefix bounds, single/midpoint compatibility, and its dependencies.
- `general_one_turn_kernel_theorem.md`, `general_one_turn_reduction.md`:
  Jacobi-resolvent construction and exact one-turn reductions.
- [Previously completed k=1 theorem](https://github.com/51mns/AIMath/blob/a36fbac460073bf757434f122e721dfa254e8e48/research/local-tp2-coefficient-geometry-20261003/second_turn_20261004/THEOREM.md).

The new theorem treats k>=3; k=0 is pure-left, k=1 uses the cited first
return theorem, k=2 uses the preceding package, and ell=0 uses the old
one-turn theorem. All inherited claims retain their existing internal
verification status and limitations.

## Public source investigation

The original public repository was
[openai/math at adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a).
The pinned investigation is [source_review.md](https://github.com/51mns/AIMath/blob/f1bf528c9064e11f79795a581b6a4bc15f0efbe1/research/local-tp2-openai-math-20261007/source_review.md),
with individual URLs/hashes in its neighboring `sources.json`.

The catalogue and selected full manuscripts were inspected, not every
proof in that public collection. Positive reordering and explicit
cancellation were useful proof-design references. The naive Lorentzian
and strongly-Rayleigh lifts had specific obstructions, recorded in the
initial investigation. The new three-run proof is built from AIMath's
actual folded recurrence, quantitative normalized defects, the actual
midpoint identity, and coefficient domination. No public manuscript is
claimed to contain this Local TP2 theorem, and no novelty or priority
claim is inferred from that investigation.
