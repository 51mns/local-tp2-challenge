# Research map — starting points, not mandatory instructions

Start from [PROBLEM.md](PROBLEM.md). Existing representations are optional; none is a known full-tree proof.

## Direct two-gap comparison

Let the outgoing child-minus-parent gaps in degree order be Lgap=U-C and Rgap=V-C. Since S=Lgap and D=Rgap-Lgap,

`H(S)_i H(D)_j-H(S)_j H(D)_i = H(Lgap)_i H(Rgap)_j-H(Lgap)_j H(Rgap)_i`.

The subtraction in D cancels exactly in the determinant. The positive canonical networks and factorized Fricke exchanges may therefore help with a weight-preserving injection or cancellation on paired paths. Ordinary positivity of networks by itself is insufficient.

[Direct exchange/network note](archive/research/local-tp2-coefficient-geometry-20261003/fulltree_direct_exchange.md)

## Keep the canonical coupling

For degree-oriented endpoints X,Y and centre C, the preserved relation is

`X²+Y²+C²+x(XY+XC+YC)-3(x+1)XYC=0`.

The latest source gives subtraction-free updates in nonnegative quotient coordinates while keeping this residual. Removing the coupling admits noncanonical negative minors. A generic statement for arbitrary positive polynomials may be false even when the canonical claim is true.

[Exact Fricke coordinates](archive/research/local-tp2-openai-math-20261007/fricke_closure_20261007/THEOREM.md)

## Diagnose long runs followed by a turn

The finite search's tightest reported family was RL^5 R^k L. Explaining its central margin by an exact identity or a rigorous asymptotic estimate with error bounds would be informative. Do not assume it crosses zero, or that all other indices are easier, from the observed samples.

## Audit the finite-to-infinite steps

The three-run package combines finite certificates and infinite-tail inequalities. Independently check its dependencies, parameter coverage, signs, squared mixture weights, and terminal strictness. A reproducible bug or a clearly isolated proof gap is a useful contribution.

## Stop repeating known dead ends

Avoid merely increasing enumeration depth, adding another conditional inequality, or replacing a failed fixed constant by another fixed constant in the same disproved margin scheme. A new canonical counterexample, a repaired general proof step, or a genuinely new coupling mechanism is more useful than a larger PASS count.
