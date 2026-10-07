# Status and evidence levels

**The universal assertion is OPEN in this project.** No external validation, novelty, success probability or percentage-complete claim is made.

## Historical partial proofs — offered for audit

The archive preserves the original status labels and frozen arithmetic outputs. An internal `PASS` can mean that code agreed or a stated conditional lemma was checked. It is not necessarily a proof of the universal target.

| Result | Record to examine | What is not claimed |
|---|---|---|
| All L^m R^k L^j, m,k,j >= 0 | [Three-run report](archive/research/local-tp2-openai-math-20261007/arbitrary_k_20261007/RESULT_JA.md), [assembly](archive/research/local-tp2-openai-math-20261007/arbitrary_k_20261007/arbk_root/GENERIC_ARBITRARY_K_CLOSURE.md), and its dependency/replay files | Not all alternating words; not externally peer-reviewed or formally verified |
| LRL R^N and RLR L^N | [Signed-seed manuscript](archive/research/local-tp2-openai-math-20261007/signed_seed_20261007/THEOREM.md) | Proof candidates, not all four-run words |
| Positive all-tree matrix/character models | [Matrix model](archive/research/local-tp2-coefficient-geometry-20261003/fulltree_kernel_positive_transfer.md), [character support](archive/research/local-tp2-coefficient-geometry-20261003/resumed_extension_kernel_support.md) | Entrywise/character positivity is not Fourier TP2 |
| Finite-channel and mixed-mass transport | [Compound transport](archive/research/local-tp2-openai-math-20261007/compound_transport_20261007/THEOREM.md) | Conditional transport; canonical preservation under arbitrary turns remains unproved |
| Positive degree-oriented Fricke coordinates | [Fricke manuscript](archive/research/local-tp2-openai-math-20261007/fricke_closure_20261007/THEOREM.md) | Algebraic preservation, not preservation of the desired minors |

Publishing these records does **not** upgrade their evidential status. A solver is welcome to bypass or refute them. A complete validation of the three-run proof requires its inherited mathematical lemmas, interval certificates, strictness and coverage arguments, not merely a successful smoke test.

## Historical direct counterexample search

The supplied report from 2026-10-07 records 16,677 distinct states and 10,176,120 supported minors, all strictly positive:

- Exhaustive through depth 13: 16,383 states, 9,565,936 minors.
- Additional targeted states: 278 states, 539,318 minors.
- Additional stress states: 16 states, 70,866 minors.

Selected word length reached 1,024; maximum degree of D was 8,202. Only depth 13 was exhaustive. Different methods by the **same model** cross-checked 518 states / 51,126 complete minors and one additional central comparison. The whole ten-million-minor search was not independently repeated by another researcher.

At RL^5 R^160 L, n=0, the smallest reported relative margin was about 2.120514229740311e-7. All observed relative minima were central. Neither is a theorem about other paths or asymptotics. A small positive margin is not a probability of an imminent counterexample.

The compact source report is in [evidence](evidence/README.md). Distinguish the historical run from the smaller publication-time tests in `evidence/PUBLICATION_CHECKS.json`.

## The important negative result

A uniform sufficient condition of the form

`delta_n(F) >= C * max_i H(Q)_i * H(F)_n`

is not preserved on the whole canonical tree. At the first right state, a tested instance with C=8 has `2916 - 3456 = -540`. The target Local TP2 minors there remain positive. The source argument also rules out repairing this particular family merely by choosing a smaller fixed positive C. See [FAILED_ROUTES.md](FAILED_ROUTES.md).

This does not invalidate a conditional extension theorem at inputs that satisfy its hypotheses. It prevents silently assuming those hypotheses at every subsequent state.
