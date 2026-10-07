# Independent audit of the strict relaxed border obstruction

**PASS**, independently replayed using the falsification lane's Fourier
and finite-character routines rather than the spectral verifier. This
audits `packet_spectral.md` Section 4; it does not extend its scope.

For the displayed rational v, its Fourier row is exactly
(4659,4537,4181,3610,2859,1971,1000)/1000. Both v and yv have
positive interval support, strictly positive supported defects, and
nonnegative **complete** finite character arrays.

| Mode | Minimum supported defect | Minimum nonzero character |
| --- | ---: | ---: |
| Raw | 2899/1,000,000 | 2899/1,000,000 |
| y | 1491/200,000 | 1491/200,000 |

The full continuous shifted-trace box for f=(x+4)^2 has the independently
derived six lower bounds (144,112,16,43,8,1); its central coefficient
is decreasing on [-2,2], and the others are affine or constant. Thus
this is a full-box certificate, not a finite parameter sample.

At the border n=3, the exact arithmetic is

    delta3(beta v)=8,079,579/500,000,
    (beta v)_4=1869/25,
    delta3(f+beta v)=-29,300,421/500,000.

The entire beta v defect list is strictly positive, and lc f=lc v=1.
Consequently strict raw/y cones, leading-coefficient dominance, and the
parent shifted-trace gate do not imply the larger-gap trace border
margin. Additional quantitative origin/ancestry information is needed.

The witness has negative ordinary power coefficients. It is neither an
MP_sharp-origin counterexample nor a canonical/Fricke state; it cannot
refute the desired actual BOTH-child transport. The exact replay is
`falsification_spectral_audit.py`, with saved result JSON of the same
prefix. No state search was performed.

Audited source SHA-256 values at freeze:

| Source | SHA-256 |
| --- | --- |
| `packet_spectral.md` | `b56254f419556bd88435bca6def12079d345aba226203ade91e7e8faae1adb8e` |
| `packet_spectral_verify.py` | `996d5a78eab2657bb3d82b87a269b0e8d3d2adb79eddc71ab9f0515bcb9ae7f5` |
| `packet_spectral_results.json` | `f1bde6c1d75c0362205b308200c098299c4caf91b4f0c89243a4c6dbb556f51c` |
