# One-hour continuation: all L^m R² L^ell

**Primary status: PROVED_INTERNAL**, scoped to strict original Local TP2 on
every `L^m R^2 L^ell`, with `m,ell>=0`, and conditional on the explicitly
cited proved foundation lemmas. Full canonical-tree Local TP2 remains open.

- [Japanese result and explanation](RESULT_JA.md)
- [Complete proof](hour_root/UNIFORM_RAY_CLOSURE.md)
- [Mathematical audit](hour_invariant/AUDIT_UNIFORM_RAY.md)
- [Independent finite reconstruction and second mathematical audit](hour_transport/UNIFORM_RAY_INDEPENDENT_AUDIT.md)
- [Finite criterion for a fixed prefix](hour_invariant/FINITE_RAY_EXTENSION_CRITERION.md)

The initial fixed-prefix breakthroughs are retained as supporting records:
[R²L^ell](hour_invariant/THEOREM_R2_RAY.md) and
[LR²L^ell](hour_quantum/lrrl_theorem.md).

## Additional result for the next generalization

For every one-turn center `C=C_(L^m R^k)`, `m,k>=0`, both
`3(x+1)C-x-r` and `(x+1)[3(x+1)C-x-r]` are at least 1-strong for
every real `r in [-2,2]`. See the [separate trace theorem](hour_transport/ARBITRARY_K_TRACE_EXPLORATORY.md)
and [independent audit](hour_invariant/AUDIT_ARBITRARY_K_TRACE.md).
All 867 finite Bernstein coefficients were independently reconstructed.
This is a separate auxiliary result, not an added dependency of the main
theorem and not a proof of Local TP2 for arbitrary `L^m R^k L^ell`.

Large JSON certificates are preserved losslessly as deterministic `.json.gz`
files. Their compressed and uncompressed hashes are recorded in
`COMPRESSED_CERTIFICATES.json`. They are reproducible exact certificates,
not finite-path samples supporting an extrapolation.

## Reproduction

In the **VS Code integrated terminal**, from this directory, run:

```bash
python3 reproduce.py
```

The Python-standard-library runner checks file integrity, unpacks certificates
into a temporary copy, runs the author and separate implementations, and
compares the regenerated certificate hashes. The analytic proof and its
mathematical reviews must also be read to assess the unbounded theorem.

All independent implementations and reviews here are shared-session internal
checks. They are not external peer review, blind replication, Lean verification,
or a promotion to the canonical `INDEPENDENTLY_REPRODUCED` state.
