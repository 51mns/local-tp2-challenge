# Independent audit of the normalized signed endpoint seed

Verdict: the displayed seed, BOTH-child sign update, and Cassini identity
are exact. They do not establish folded-cone or LR positivity.

Keep the normalized state (a,e,r), g=(t-2)e+k+r,
X=1+ya, Y=1+y(a+e), t=3yX-x and k=X(3X-2).
Set

    eta=e-r, c=e+g, tau=3yY-x=t+3y²e,
    q1=s+d=tau c+eta,
    F=rg-(t-2)e²-2ke-3aX².

The q1 equality follows by substituting s=tg-r and
d=e(t+1+3y²(e+g)). Its error polynomial is identically zero.

The normalized SHORT update has e'=e+g,r'=g and hence eta'=e.
The LONG update has e'=g,r'=e+g and hence eta'=-e.
Since the old canonical e is dense and positive, nonroot eta is positive
or negative coefficientwise according to the last degree-oriented move.
At the root eta=0. This sign cannot be erased in a positive-mixture proof.

The stronger off-Fricke Cassini identity is

    c²+eta q1-Y²(1+3(a+e))=-(tau-2)F.                    (1)

One proof uses the universal fixed-X residual
g²-rs-X²(1+3a)=-(t-2)F and exchanges endpoints. Under this
purely algebraic exchange the new coordinates are
a_new=a+e, e_new=-e, g_new=e+g=c, r_new=r-e=-eta,
t_new=tau, and s_new=q1. The residual F is unchanged because
it equals the symmetric original Fricke residual divided by y².
Substitution gives (1). The independent sparse Z[x,a,e,r]
verifier also checks every coefficient of (1) directly without using
that exchange proof or enumerating canonical states.

On canonical states F=0, proving the claimed positive Cassini right side

    c²+eta q1=Y²(1+3(a+e)).

For fixed Y define u_N=U_N(tau/2), with u_-1=0,u_0=1.
Then the exact homogeneous gap run has

    q_-1=-eta, q_0=c,
    q_N=c u_N+eta u_(N-1), N>=0.

This follows from u_(N+1)=tau u_N-u_(N-1), which gives
q_(N+1)=tau q_N-q_(N-1). At N=0 the initial q1 is
tau c+eta, fixing the sign and the Chebyshev normalization. The
all-degree conclusion is this recurrence induction. Finite symbolic
checks through N=5 merely reproduce its initial normalization.

At the root c=2(x+2)=2Y and eta=0; the Cassini right side is
4Y², so its seed is exact. Neither pointwise Cassini nor positive
ordinary coefficients permits dropping the signed eta term after the
two-character transform. A common Fourier closure mechanism remains OPEN.

Artifacts: `pair_signed_seed_verify.py`, `pair_signed_seed_results.json`.
They use independent exact integer sparse-polynomial arithmetic only.
