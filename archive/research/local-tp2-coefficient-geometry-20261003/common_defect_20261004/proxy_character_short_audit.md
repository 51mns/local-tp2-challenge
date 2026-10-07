# Independent review of the ordinary SHORT lower-block theorem

**PASS, with the retained central flag explicit.** I independently read
`proxy_algebra.md` and checked its full-character identity, signs,
strict common-product boundary argument, and conditional SHORT
implication. This audit does not prove its D-advance premise.

Write A=t-2, h=A+1 and Q=hG-R. Before Phi,

    R(AG,hQ)=R(AG,h²G-hR)
             =T_G R(A,h²)+T_A R(R,G)+R(R,AG).

Also R(A,h²)=R(A,A²+2A+1)=(T_A-1)D_A. Thus equation (5) in
the reviewed note is exact, including the sign of both R terms.

The sign theorem consumes all of its stated premises. Weak K_A
supplies T_A>=character0. The retained delta_0(A)>=1 subtracts only
the central coefficient, so T_A-1>=character0. Ordinary positivity of
A supplies D_A>=character0. The other terms use K_G, R<=lrG, and
G<=lrAG from R(G,AG)=T_G D_A. Actual positive interval supports
justify LR transitivity R<=G<=AG and hence R(R,AG)>=character0.
No child target, K_D, or child-center packet is used here.

The central flag has a valid history initialization/retention proof:
the initial ordinary endpoint P has A half-row (10,8,3) and central
defect 2; every new ordinary endpoint is an old center whose trace
central strictness was proved by the old all-shift central subsystem.
Its integer strict value is at least one, and retention does not change
the trace. This is an **additional retained history component** when
working with a weaker core MP_0 predicate. Core weak trace positivity
alone does not imply T_A-1>=character0. Any statement about MP_0
must therefore explicitly include this flag or another proof of it.
The endpoint-1 A=2x+1 fails weak folded TP2 and is correctly excluded.

For strict hQ<hD, I independently checked the retained folded
Cauchy--Binet term. Put d=deg h and f=deg Q>=d, and for output
index n select i=max(d,min(n,f)). The parent relative adjacent minor
at i,i+1 is strict, including i=f by the separate terminal support.
For n>=1, the chosen second minor of K_h is the positive ordinary
log-concavity difference Delta_|i-n|. Weak folded TP2 plus positive
interval support gives Delta_j=sum_(k=j)^d delta_k>0. At n=0 the
second minor is exactly 2(lc h)². The index has |i-n|<=d for every
0<=n<=f+d. Hence strictness covers zero, all supported interior
indices, and terminal, without a cone assumption on D.

The actual SHORT child has deg Q'=deg(hQ): AG is strictly shorter.
Also deg(hD)>deg(hQ). Consequently this strict diagonal contribution
covers the **whole actual child Q' support**, not only the old Q band.

Finally K is a positive actual row. Its equation (2),

    K=(t+1)H+3y(E+G)[tG+yX(3X-2)],

has ordinary nonnegative summands with positive dense support because
H=y[X(3X-2)+r]. Thus hD<=lrD' is equivalent to hD<=lrK:
the relative tensors agree since D'=hD+K. Under that independent
premise the chain

    AG<=hQ<hD<=K

signs all four terms in R(hQ+AG,hD+K). The strict R(hQ,hD) term
covers every supported child index, proving the conditional ordinary
SHORT comparison Q'<D'. The D-advance sign remains **OPEN**.

The LONG caveat is also correct: R(Q+D,D)=R(Q,D) vanishes above
the old Q support. Common multiplication transports weak order there;
it does not supply full LONG strictness. Its signed residual is not
covered by this SHORT theorem.

This review uses exact algebra and the previously proved all-index
folded identities, not a finite state scan. The separate
`proxy_character_verify.py` replays the coupled-prefix algebra and
its actual signed-residual obstruction; it is not presented as an
independent proof of D-advance positivity. Full BOTH proxy preservation
and full-tree strict Local TP2 remain **OPEN**.
