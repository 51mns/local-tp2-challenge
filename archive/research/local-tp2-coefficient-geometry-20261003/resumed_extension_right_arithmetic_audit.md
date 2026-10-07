# Independent arithmetic audit of the all-right proof

**PASS.** The standalone verifier `resumed_extension_right_audit.py`
imports no producer or prior arithmetic helper. It constructs polynomials
directly in the Laurent variable `q`, over a rational parameter ring,
using `x=q+q^-1`. Thus it does not reuse the producer's Fourier map.

The verifier independently reconstructs and replays every exported
certificate in `resumed_extension_right_certificates.json`:

- The quartic amplification certificate
  `delta_0(Q)-4Q(2)>=884`.
- All four low-index correction margins for `R=Q`.
- All four low-index correction margins for `R=G`.

For every certificate, the reconstructed Laurent calculation equals its
recorded power-basis polynomial. Independently expanding its complete
Bernstein array recovers that same polynomial exactly, with all
coefficients strictly positive. This replays **9 polynomials and 57
Bernstein coefficients**. Parameter positions are matched explicitly:
`Q=t^2+2ut-4v`, whereas the producer uses `G=t+w`.

| Initial block | Four verified strict correction bounds |
| --- | --- |
| `Q` | `151266414,338478852,290971872,145555380` |
| `G` | `17268,358599,322626,138210` |

The independent calculation also verifies the full adjacent pair
comparison through the terminal index for both blocks, and their
supported cone defects, on the entire parameter boxes. In total this
checks **33 polynomial inequalities and 159 Bernstein coefficients**.
These supplemental certificates are independently produced and reverse
expanded; the proof itself needs only the nine replayed certificates
together with its actual-root factorization.

The verifier additionally checks the displayed rows of `Ae`, `Be`,
and `K`, the mass `(Ae)(2)=384`, the five base pair minors, and the
two initial comparisons used in the first sandwich.

The all-right proof's exact ray identities, child-degree ordering,
both parity factorizations, and Cauchy--Binet propagation were reviewed.
The root-block grouping is valid: opposite roots of each second-kind
factor give `Q`; paired roots of each adjacent-sum factor have magnitudes
`0<=a<=b<=2`, giving `Q=t^2+(b-a)t-ab`; any two middle linear factors
combine as `t(t+b)`. Hence at most one `G` remains. Choosing it first
ensures all subsequent blocks are quartics. No leading scalar is missing
because `U_j(t/2)` is monic in `t`.

No gap was found in the arithmetic or its use in the comparison proof.
The separate right-multiplier lemma remains an explicit dependency;
this audit does not silently replace its proof. The resulting theorem
concerns all-right states, with the root handled separately, and makes
no claim about arbitrary mixed paths.

Run `python resumed_extension_right_audit.py` from the research directory.
The machine-readable result is `resumed_extension_right_audit.json`.
