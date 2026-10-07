# Exact determinant transport along a canonical run

This note gives a direct bivariate identity for the desired coefficient determinants. It is not a proof of their positivity under arbitrary switches.

Fix a canonical endpoint `X`, and put `t=3(x+1)X-x`. Consecutive center differences along the fixed-endpoint run satisfy

`q_(k+1)=t q_k-q_(k-1)`.

Use the globally positive Robin initial data from the run reduction:

`q_(-1)=A-B`, `q_0=A`,

so `q_k=A(u_k-u_(k-1))+B u_(k-1)`, where `u_k=U_k(t/2)`.

For two independent polynomial arguments `s,z`, define

`Omega_k(s,z)=q_k(s)q_(k+1)(z)-q_(k+1)(s)q_k(z)`.

A direct use of the recurrence, with no kernel assumption, gives

`Omega_k=Omega_(k-1)+(t(z)-t(s))q_k(s)q_k(z)`.

Consequently

`Omega_k(s,z)=A(s)B(z)-B(s)A(z)`

`             +(t(z)-t(s)) sum_(j=0)^k q_j(s)q_j(z)`.                 (1)

This is the exact Christoffel-Darboux transport for the two successive gap polynomials. The initial term retains the coupled canonical data `A,B`; they are not replaced by unrelated positive summands.

## Fourier extraction

Substitute `s=p+p^(-1)` and `z=q+q^(-1)` in (1). Write

`W_n(F,G)=H(F)_n H(G)_(n+1)-H(F)_(n+1)H(G)_n`.

Extracting the coefficient of `p^n q^(n+1)` gives the finite exact identity

`W_n(q_k,q_(k+1))=W_n(A,B)+sum_(j=0)^k W_n(q_j,t q_j)`.             (2)

Thus one need not separately prove that every summand is nonnegative. A direct run proof could instead control the aggregate in (2), using the canonical Cassini relation

`B^2-(t-2)A(A-B)=(x+1)X^2(3X+x-2)`.

The current argument does not supply that aggregate estimate. Cassini is a same-variable quadratic identity; passing from it to the bivariate determinants in (1) requires an additional argument.

If `t=x`, the forcing term has a particularly exact interpretation. For `h=H(F)`, extended by zero, and `h_(-1)=h_1`,

`W_n(F,xF)=delta_n(h)`

at every `n>=0`, including the folded boundary `n=0`. Hence individual folded-cone membership is one sufficient way to make the forcing nonnegative, but (2) exposes the weaker aggregate statement that would suffice along a run.

## Correct affine trace coordinates

For the entire tree, set `a=3yA-x`, `b=3yB-x`, `c=3yC-x`, and `kappa=x(x+2)`. The mutation and invariant are

`u=ac-b-kappa`,

`a^2+b^2+c^2-abc+kappa(a+b+c)=-x^2(2x+3)`.

The affine correction cannot be omitted. The scaled outgoing gaps are

`l=(a-1)c-b-kappa`, `r=(b-1)c-a-kappa`.

Under a left mutation, the next gap on the same run nevertheless satisfies the clean identity

`l_next=a l+b-c`,

because the affine corrections cancel. Differences of consecutive centers therefore obey the homogeneous recurrence used in (1).

The remaining full-tree problem is to transport the determinant comparison when the fixed endpoint changes. Equations (1)-(2) describe exact run transport; they do not assert that ordinary positivity, the Cassini identity, or positive resolvent residues alone justify switch closure.
