# Bounded exact Local TP2 falsification probes

No counterexample was found in 47 selected mixed paths, covering 35,315 canonical minors. All margins were strictly positive. This is bounded numerical evidence using exact integers, **not a proof for arbitrary paths**.

The test uses symmetric Laurent half rows directly with the original mutation equation and computes all supported Local TP2 minors for each selected path. All 31 states through depth 4 were independently matched against `tp2_source.py`'s ordinary-polynomial recurrence and binomial Fourier transform, including every S/D row and canonical minor. Laurent multiplication uses the existing carry-free integer Kronecker convolution in `fulltree_oneturn_finite.py`.

The selected paths include repeated alternation, repeated two-letter runs, and two-switch paths L^a R^b L^c / R^a L^b R^c with long and asymmetric runs. Maximum D degree was 4347. All 47 normalized minima occurred at n = 0.

Normalization: F_n / (H(D)_(n+1) H(S)_n). The minimum occurred for R L^80 R, n = 0, with deg(S) = 728 and deg(D) = 731; its decimal approximation is 0.0000047293284467523402524. The exact reduced numerator and denominator are stored in `falsification_results.json`, together with every tested path, source SHA-256 hashes, and the aggregate SHA-256 of exact minors.

Run from the containing research directory:

```sh
python fulltree_20261004/falsification_probe.py
```

Original recurrence crosscheck: 31 nodes. Probe elapsed time: 236.369 seconds. No external uploads were performed by this probe.
