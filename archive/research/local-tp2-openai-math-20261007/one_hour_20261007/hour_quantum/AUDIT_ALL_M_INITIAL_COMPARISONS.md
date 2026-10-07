# Independent review of all one-turn-prefix initial comparisons

**Verdict: PASS for the four initial likelihood-ratio comparisons.**

Reviewed `../hour_invariant/ALL_M_INITIAL_COMPARISONS.md`, Sections 1–5,
against the original companion transport and all-right-ray source. This
review checks the algebra and dependency directions; it does not claim the
remaining analytic ray gates for arbitrary inner right-run length.

## 1. The weaker companion premise is sufficient

Write `p=x+2`, `t=3(x+1)X-x`, and `h=H(X)`. The canonical Laurent row has
nonnegative coefficients and `h_0>=1`. Since `H(p)=(2,1)`,

\[
W_0(p,t)=3h_0+6h_2-2\ge1,
\qquad W_1(p,t)=H(t)_2\ge0.
\]

The other adjacent comparisons vanish. Thus `1<=lr p<=lr t` is valid
without a separate folded-kernel premise on `X`. The hypothesized `K_G`
transports it to `G<=lr pG<=lr tG`.

From `S=tG-R` and `R<=lr G<=lr pG`, the determinant identity

\[
W(pG,S)=W(pG,tG)+W(R,pG)\ge0
\]

has the stated sign. The corresponding identity with `G` gives `G<=lr S`.
Both summands of `pC=pY+pG` are below `S`. The stated short-child and
long-child updates then give every new companion link, with the long
child using only the already known parent comparison `S<=lr D`.

In particular, the argument does not require the resulting child's
multiplier, proxy, or target comparison. There is no circular use of the
new two-turn conclusion.

## 2. The old one-turn hypotheses cover the exceptional first step

The root itself must not start the regular four-link induction. The
separate first-level seeds provide the induction bases, exactly as stated.
Every parent on a subsequent path `L^mR^k` is an old one-turn state.
Its original Local TP2 supplies the parent target comparison, while the
old gap-kernel theorem supplies `K_G`.

For `m=0`, the old `resumed_extension_right.md` gives actual consecutive
gaps `2e u_j`, with `e=(x+1)(x+2)`, strict folded kernels for `e` and every
`t-a`, and the recurrence proof of gap time order. Thus the all-right
boundary has the required kernel and order premises; it is not silently
covered by a theorem requiring `m>=1`.

## 3. The general inner-run corollary has the correct directions

For `k>=2`, the identities are

\[
q_0=yB+p_{k-1}+p_k,
\qquad q_1=p_{k+1}+D_{\rm old},
\qquad E_1=p_k.
\]

The row `yB` is the sum of the initial old gap and gaps through `k-2`.
Every such summand lies below both `p_(k-1)` and `p_k`. Consequently
`yB<=lr q_0`, and hence `beta=q_0+yB<=lr q_0`. Every summand of `q_0`
lies below `p_(k+1)`; old Local TP2 gives
`p_(k+1)<=lr D_old`. Therefore

\[
\beta\le_{\rm lr}q_0\le_{\rm lr}p_{k+1}
\le_{\rm lr}q_1.
\]

The transported higher-endpoint companion link gives

\[
pX\le_{\rm lr}E_1=p_k\le_{\rm lr}q_1.
\]

This proves exactly the four initial comparisons for all `m>=0,k>=2`.
It supplies no claim that the new trace or mixed seed templates satisfy
the separate analytic assumptions for `k>=3`; the source document's
scope limitation is correct.

## Sources inspected

- `../hour_invariant/ALL_M_INITIAL_COMPARISONS.md`.
- Existing research `common_closure_20261004/reduction_common.md`.
- Existing research `resumed_extension_right.md` and
  `resumed_audit_right.md`.

This is an independent mathematical review within the shared research
session, not a proof-assistant verification or an external peer review.
