# Local TP2 bounded strategy gate

Baseline: `604f4369756ecd6e1896a916e5164a4b1fc6a9e2` on the existing private
`research/local-tp2-coefficient-geometry-20261003` branch.

Primary campaign level: **DRAFT** (lane-local synthesis, no canonical promotion).
Portfolio decision: **HOLD current closure workflow**.
Full-tree Local TP2: **OPEN**, neither proved nor refuted here.

Start with [RESULT_JA.md](RESULT_JA.md), then
[audit_dependency.md](audit_dependency.md). Writer notes keep distinct the
canonical route obstructions, noncanonical sufficient-lemma counterexamples,
elementary parity theorem, and finite packet viability checks.

The absence of a bridge in this bounded campaign is a resource decision,
not a mathematical impossibility theorem. The parity lemma is not claimed
to be new in the mathematical literature. Partial internal results do not
establish external novelty or imply Frobenius uniqueness.

## Exact replay

Environment used: Python 3.12.14, standard library only. From this directory
in a terminal (on the user's Mac, the VS Code integrated terminal is suitable),
each command checks the named finite witnesses and writes its matching JSON:

```bash
python3 short_gate_verify.py
python3 long_gate_verify.py
python3 packet_gate_verify.py
python3 alternative_parity_verify.py
python3 supervisor_witness_verify.py
python3 audit_fresh_verify.py
```

The supervisor and auditor programs import no writer implementation or
generated expected-output file. The packet writer uses its own local helper
`packet_gate_probe.py`; that writer replay is not itself an independent audit.
Analytical universal claims are checked in the audit prose, not inferred from
these finite calculations.

Optional fixed-state viability records are reproduced by
`falsification_verify.py`, `falsification_packet_verify.py`, and
`falsification_continuum_verify.py`. These share the falsification lane's own
arithmetic; the continuum certificates concern only current packets at the
listed states. They are not full P_0 certificates and are not a continuation
justification. No depth expansion is needed to reproduce the decision.

The packet candidate initially used an incorrect trace normalization. The
fixed writer and two independent reconstructions use `T=t+beta(e+g)` and
`R=2x+5+beta(a+e-r)` and compare against the original canonical child mutation.
Preliminary CB-probe passes based on the incorrect normalization are withdrawn.

`checkpoint_manifest.json` records all final file hashes and the baseline.
`replay_results.json` records the supervisor's targeted replay commands,
environment and exit codes. Earlier campaign artifacts are not changed.
