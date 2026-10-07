# Failed approaches and exact controls

**These are counterexamples to proposed proof shortcuts, not canonical counterexamples to Local TP2.** Do not discard a whole mathematical field because one particular lift fails.

## 1. A uniform maximum-coefficient margin is not an invariant

The sufficient condition `delta_n(F) >= 8 max(H(Q)) H(F)_n` fails already after the first right move in its smoothed midpoint application. At the terminal coefficient in that calculation, the left side is `54²=2916`, the requested right side `8*8*54=3456`, leaving `-540`.

Along a right ray the relevant endpoint coefficient grows like `54*3^(n-1)`, while the reference maximum is at least `8*5^(n-1)`. This explains why reducing a fixed positive constant cannot repair the whole family. A source note also treats central failure (including an exact R^56 instance). The full note is in [evidence/closure-audit/THEOREM.md](evidence/closure-audit/THEOREM.md).

Only this particular bound is ruled out. Conditional kernel theorems are not retracted and the target minors at the displayed failure states are positive.

## 2. Nonnegative second seed B is not invariant

Along a fixed-boundary ray the exact update is `(A,B) -> (tA+B,-A)`. Requiring B>=0 at every step therefore fails. The later signed-seed manuscript retains B inside each spectral summand and proves canonical `|B|<=A`; this does not automatically establish all kernel or initial-order premises.

## 3. Positive coefficients do not give folded TP2

For h_n=H(P)_n, the relevant folded defect is

`delta_n = h_n² - h_(n-1)h_(n+1) - h_(n+1)² + h_n h_(n+2)`.

For `(x+1)^3` and `(x+1)^4`, half-rows are `[7,6,3,1]` and `[19,16,10,4,1]`; the first pair minor is `7*16 - 6*19 = -2`. These polynomials do **not** form a canonical S,D pair. The example rejects overly general positivity/independent-block arguments, not the challenge.

## 4. A naive stable or Lorentzian lift is too strong

At the canonical root, H(S)=[40,32,16,4]. Its ordinary cubic homogenization has a derivative Hessian `[[32,64],[64,240]]`, with determinant 3584>0 and two positive eigenvalues. That particular lift fails the Lorentzian signature test.

Every canonical polynomial G satisfies G(-1)=1 by the original recurrence, so canonical differences S,D are divisible by x+1. Their shifted full Laurent polynomials therefore have a factor q²+q+1. This rules out representing those exact polynomials as ordinary total-count generating functions of a real-stable law; it does not rule out every auxiliary or signed-statistic model.

[Detailed transfer audit](archive/research/local-tp2-openai-math-20261007/rayleigh_transfer_audit.md) · [Lorentzian calculation](archive/research/local-tp2-openai-math-20261007/lorentzian_obstruction.md)

## 5. Quantum re-encoding is not a positivity proof

The commutator representation recovers each target minor as a central coefficient difference. Nonnegative Laurent coefficients alone do not force that difference to be positive: v²+v^(-2) is an elementary counterexample to that inference. An independent positive-basis identification or a new inequality is still needed.

[Quantum applicability boundary](archive/research/local-tp2-openai-math-20261007/quantum_applicability.md)

## 6. Do not erase the signed central term after dividing by x+1

Writing S=(x+1)s, D=(x+1)d and W_ij=H(s)_i H(d)_j-H(s)_j H(d)_i gives

`F_0 = -W_01 + W_02 + 2W_12`.

Thus even a quotient-level ordering needs additional work at the centre. The challenge concerns S,D themselves.

## General cautions

Positive sums need mixed-term control; a finite kernel truncation is a lower-bound device, not generally an equality; spectra/parameters must be covered on their whole intervals; noncanonical witnesses must not be presented as refutations of this target.
