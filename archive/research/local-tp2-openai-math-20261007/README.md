# Local TP2: arbitrary middle right-run length, 2026-10-07

**Latest result: original strict Local TP2 is PROVED_INTERNAL on every
`L^m R^k L^ell`, for integers `m,k,ell>=0`, including terminal supported
minors. Full canonical-tree Local TP2 remains OPEN.**

The latest continuation removes the fixed `k=2` restriction. An actual
midpoint subtraction identity, normalized all-minor bounds, and mass-scale
coefficient domination combine with exact continuum certificates and
monotone infinite tails. Read the [Japanese result](arbitrary_k_20261007/RESULT_JA.md),
[complete theorem](arbitrary_k_20261007/arbk_root/GENERIC_ARBITRARY_K_CLOSURE.md),
and [12-program reproduction](arbitrary_k_20261007/README.md).
Independent implementations agree on the finite coefficients and all scalar
coverage gates; the reviews are internal to this shared research session.

The earlier stages below are retained as dated research history.

---

## Previous continuation: k=2, 2026-10-07

**Previous result: strict Local TP2 is PROVED_INTERNAL on every `L^m R^2 L^ell`, for integers `m,ell>=0`. Full canonical-tree Local TP2 remains OPEN.**

The user requested approximately one more hour of research after the initial investigation. The continuation generalized two new fixed-prefix rays into this two-parameter infinite family. Read the [Japanese result](one_hour_20261007/RESULT_JA.md), [complete proof](one_hour_20261007/hour_root/UNIFORM_RAY_CLOSURE.md), and [reproduction instructions](one_hour_20261007/README.md). The result includes separate implementations of the finite certificates and separate mathematical reviews, with the inherited foundation lemmas explicitly cited.

The earlier report below is preserved as the history of the first investigation, before the continuation. Its statement that no new family was obtained applies to that completed initial stage.

---

## Initial investigation, before the continuation

# Local TP2: OpenAI/math transfer attempt, 2026-10-07

**Full-tree Local TP2 remains OPEN. No new infinite family of positive canonical minors was established in this campaign.**

Primary level: `PROOF_CANDIDATE`, scoped to the elementary transfer obstructions and identities in this directory. These are lane-local research results, not promotion of `C-LOCAL-TP2`.

Read [REPORT_JA.md](REPORT_JA.md) for the Japanese outcome and actual proof attempts. Read [source_review.md](source_review.md) for the inspected external hypotheses, [quantum_applicability.md](quantum_applicability.md) for the quantum route, and [rayleigh_transfer_audit.md](rayleigh_transfer_audit.md) for the stable-polynomial route. [lorentzian_obstruction.md](lorentzian_obstruction.md) isolates the root Hessian obstruction.

## Fixed scope

- User request: examine `openai/math`, find methods relevant to private AIMath Local TP2, and attempt a proof using them.
- Private accepted main: `c8e61e0e398f540bc8c5de79663398d689f37473`.
- Private latest research baseline: `a36fbac460073bf757434f122e721dfa254e8e48`.
- External source: `openai/math` at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
- New branch and owned path: `research/local-tp2-openai-math-20261007`.
- Stage: direct-user E0/E1 bounded external-method transfer; no new numbered worker or canonical intake.
- Stop condition: test concrete external-theorem lifts and their hypotheses; stop a lift at a proved obstruction or a circular premise. Do not substitute a larger finite tree scan for the missing preservation theorem.

The old incremental closure workflow remains on HOLD. This campaign tested an explicitly requested external proof direction. The existing branch results are prior internal research, not accepted mathematical claims on main. No public export or main integration is proposed.

## Outcome

Family 169 supplies the most relevant proof design: identify the object in a positive incoming basis before transporting coefficients. A genuine quantum-commutator dictionary was derived, but it recovers the existing character-positivity problem rather than solving it. Two naive lifts either have a negative root coefficient or re-encode the original inequality.

Families 114 and 231 do not apply to the naive half-row/stable-count lifts. The canonical root is already not Lorentzian under ordinary half-row homogenization. Every canonical difference has a cyclotomic obstruction to an ordinary-count strongly Rayleigh lift. An explicit stable signed-count model shows that allowing signed statistics does not by itself imply folded likelihood-ratio order.

The proofs and finite witnesses are useful applicability boundaries. They are **not counterexamples to canonical Local TP2**. Their novelty is not assessed.

## Reproduction

On a Mac, run in the **VS Code integrated terminal**, from this directory:

```bash
python3 reproduce.py
```

The command runs the author verifiers and a separate implementation, records their exit codes and outputs, and checks the saved file hashes. Only the Python standard library is required. The independent implementation imports no author implementation or generated expected-output file. The review is shared-session and is not represented as a blind audit, external peer review, a Lean verification, or canonical `INDEPENDENTLY_REPRODUCED` status.

The all-word cyclotomic result rests on its written induction, and the commutator identity on its written algebra. Finite replay checks their conventions and witnesses; it is not an infinite-tree proof.
