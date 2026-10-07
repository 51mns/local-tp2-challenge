# All four finite-ray initial comparisons hold uniformly after `L^mR²`

**Status: proved from the already established one-turn Local TP2 and one-turn gap kernels, together with the existing exact first-level companion seeds.** This removes all four initial likelihood-ratio gates of `FINITE_RAY_EXTENSION_CRITERION.md` for every `m>=0`. Section 5 proves the same initial-gate result for all prefixes `L^mR^k`, `m>=0,k>=2`. It does not establish the remaining new-trace, template, mass, multiplier, or proxy gates for those arbitrary inner right-run lengths.

No bounded scan of the new parameter `m` is used. The proof extracts the already completed companion transport from `common_closure_20261004/reduction_common.md` and supplies its parent target premise using the proved one-turn theorem.

## 1. A useful weaker hypothesis for the old companion transport

At a degree-ordered canonical state, let endpoints be `X_old,Y_old`, with `deg X_old<deg Y_old`, center `C`, and write

\[
E=Y_{\rm old}-X_{\rm old},\quad G=C-Y_{\rm old},\quad
S=U-C,\quad D=V-U,
\]

where `U,V` are the short and long children. Let `R` be the positive companion gap in the established normalized recursion, so that

\[
S=tG-R,\qquad t=3yX_{\rm old}-x.
\]

Suppose the four companion links hold:

\[
E\le_{\rm lr}G,\quad R\le_{\rm lr}G,\quad
pX_{\rm old}\le_{\rm lr}E,\quad
pY_{\rm old}\le_{\rm lr}G.
\tag{1}
\]

Then the old transport proof needs only the additional assertions

\[
K_G\text{ is TP2},\qquad S\le_{\rm lr}D.
\tag{2}
\]

It does **not** need an independently asserted multiplier or proxy gate if the second condition in (2) is already a theorem. In the original reduction those analytic gates were used to derive `S<=lr D`; all subsequent companion transport uses that conclusion and `K_G` only.

Here is the direct verification. The canonical fixed comparison `1<=lr p<=lr t`, transported through `K_G`, gives

\[
G\le_{\rm lr}pG\le_{\rm lr}tG.
\]

Since `R<=lr G<=lr pG`, the subtraction identity gives

\[
W(pG,S)=W(pG,tG)+W(R,pG)\ge0.
\]

The same argument gives `G<=lr S`. Therefore

\[
pY_{\rm old}\le_{\rm lr}G\le_{\rm lr}S,\qquad
pG\le_{\rm lr}S,
\]

and summing rows below the one fixed upper row yields

\[
pC=pY_{\rm old}+pG\le_{\rm lr}S.
\tag{3}
\]

The exact child updates are

| Child | `E'` | `R'` | `G'` | Lower endpoint | Higher endpoint |
|---|---|---|---|---|---|
| Short | `E+G` | `G` | `S` | `X_old` | `C` |
| Long | `G` | `E+G` | `S+D` | `Y_old` | `C` |

For the short child, (1), `G<=lr S`, and (3) give all four new links immediately. For the long child, use `S<=lr D` from (2): every row already below `S` is also below `S+D`. The endpoint link `pY_old<=lr G` is inherited directly, and `pC<=lr S+D` follows from (3). This proves both-child transport under precisely (1)–(2).

## 2. Why those hypotheses hold along every old one-turn path

The already established one-turn theorem proves the original strict Local TP2 at all states `L^mR^k`, `m,k>=0`. Hence `S<=lr D` in (2) is available on every such parent, without invoking the new two-turn theorem.

Its actual `G` kernels are also already proved. On a pure-left state, `G=y u_(m+1)` is a Chebyshev increment with a strict folded kernel. After a right step, the higher endpoint is the preceding right-ray center, so `G` is exactly the old right-ray gap `q_k`; the one-turn compatible-mixture theorem supplies its strict kernel for every `m,k` in this range. The `m=0` all-right case is part of the proved one-turn family and its base analysis.

At the canonical root two of the four comparisons (1) fail, so regular transport must not be started there. The existing common-reduction result separately verifies all four links at both first-level children. Those two exact seeds are already established; they are not new unverified finite checks. Every later path `L^mR^k` is reached from one of them by parents still in the one-turn family. Inductively applying Section 1 therefore proves (1) at **every nonroot one-turn state**.

As an additional arithmetic audit, `companion_seed_audit.json` records a fresh reconstruction of both original first-level mutations and their Fourier rows by direct binomial expansion. It reproduces all eight seed comparison lists, including their terminal zeros, and the exceptional-root comparison `W(G,S)=(24,16,8)` exactly. This confirms the seed data used here without importing the previous companion implementation.

In particular the companion inequality for the higher endpoint holds uniformly there:

\[
\boxed{pY_{\rm old}\le_{\rm lr}C-Y_{\rm old}.}
\tag{4}
\]

This conclusion can also be transported one further edge out of the one-turn family, because its proof uses only the parent's kernels and Local TP2. It does not assert that the resulting child's new analytic gates are preserved.

## 3. Apply the companion link at the new prefix

Fix `m>=0`. At `L^m`, let the right endpoint be `Y=g_m` and the center be `g_(m+1)`. Denote the first, second, and third right centers by

\[
X=C^{\rm old}_1,\qquad C_0=C^{\rm old}_2,\qquad C^{\rm old}_3.
\]

Set the positive old gaps

\[
b_0=g_{m+1}-Y,\quad
p_1=X-g_{m+1},\quad
p_2=C_0-X,\quad
p_3=C^{\rm old}_3-C_0.
\tag{5}
\]

The first new left-ray gap and reference correction are

\[
q_0=C_0-Y=b_0+p_1+p_2,\quad
\beta=y(A+B)=q_0+b_0,\quad E_1=C_0-X=p_2.
\tag{6}
\]

At the old state `L^mR²`, its lower endpoint is `Y` and its higher endpoint is `X`. Thus (4) is exactly

\[
\boxed{pX\le_{\rm lr}p_2=E_1.}
\tag{7}
\]

This is the endpoint initial gate that was formerly verified separately for `m=0,1`.

## 4. The other three comparisons follow from old time order and old Local TP2

Pure-left gap order and the old target at `L^m` give `b_0<=lr p_1`. Equivalently, the pure-left actual gap `G=b_0` lies below its short child gap `S`, and the proved old target `S<=lr D` implies `S<=lr S+D=p_1`. The pure-left gap comparison includes `m=0`; it is also the explicitly established root comparison `G<=lr S`.

Old right-ray time order gives

\[
b_0\le_{\rm lr}p_1\le_{\rm lr}p_2\le_{\rm lr}p_3.
\tag{8}
\]

At the old prefix `L^mR²`, its short child is the next right child, so `S_old=p_3`. Its long child is the first **new** left child. Consequently

\[
q_1=p_3+D_{\rm old}.
\]

The proved one-turn Local TP2 at this prefix gives `p_3<=lr D_old`, hence

\[
p_3\le_{\rm lr}q_1.
\tag{9}
\]

All three summands of `q_0` in (6) lie below the same fixed upper row `p_3`. By bilinearity,

\[
q_0\le_{\rm lr}p_3\le_{\rm lr}q_1.
\tag{10}
\]

Also (8) puts `b_0` below each summand of `q_0`, so `b_0<=lr q_0`. Therefore `beta=q_0+b_0<=lr q_0`, which, with (10), proves `beta<=lr q_1`. This is a likelihood-ratio statement; it does not assert a coefficientwise inequality between `q_0+b_0` and `q_0`.

Finally (7)–(9) give the stronger endpoint comparison

\[
pX\le_{\rm lr}E_1=p_2\le_{\rm lr}q_1.
\tag{11}
\]

Combining (7), (10), (11), and the beta comparison establishes all four initial gates, for every `m>=0`:

\[
\boxed{
q_0\le_{\rm lr}q_1,\quad
\beta\le_{\rm lr}q_1,\quad
pX\le_{\rm lr}E_1,\quad
pX\le_{\rm lr}q_1.
}
\]

All support and degree orderings follow from the already proved canonical dense positivity and the displayed original gap identities. This completes the uniform initial-comparison result while leaving the new analytic ray-extension gates explicitly separate.

## 5. Stronger corollary: the four initial links hold for every `L^mR^k`, `k>=2`

The initial-comparison argument is not specific to the number two. Fix any `m>=0` and `k>=2`. Keep `Y=g_m`, write `C_j` for the old right-run centers, with `C_0=g_(m+1)`, and set

\[
b_0=C_0-Y,\qquad p_j=C_j-C_{j-1}\quad(j\ge1).
\]

The new prefix is `(X,C_k,Y)` with fixed left endpoint `X=C_(k-1)`. Its inverse center is `C_(k-2)`. Therefore its new quantities are exactly

\[
\begin{aligned}
q_0&=C_k-Y=b_0+\sum_{j=1}^k p_j,\\
yB&=C_{k-2}-Y=b_0+\sum_{j=1}^{k-2}p_j,\\
\beta&=q_0+yB,\qquad E_1=p_k.
\end{aligned}
\tag{12}
\]

An empty sum in (12) is zero, so this includes `k=2`. The already proved comparisons are

\[
b_0\le_{\rm lr}p_1\le_{\rm lr}p_2\le_{\rm lr}\cdots.
\]

All summands of `q_0` are below `p_(k+1)`, hence `q_0<=lr p_(k+1)`. At the old one-turn state `L^mR^k`, its next right child is the short child, so its actual short gap is `S_old=p_(k+1)`. Its long child is the first new left child; therefore `q_1=S_old+D_old`. The old Local TP2 theorem gives

\[
q_0\le_{\rm lr}p_{k+1}\le_{\rm lr}q_1.
\tag{13}
\]

Every summand of `yB` is below both `p_(k-1)` and `p_k`. As `q_0=yB+p_(k-1)+p_k`, bilinearity gives `yB<=lr q_0`. Consequently `beta=q_0+yB<=lr q_0<=lr q_1`.

Finally the higher-endpoint companion (4), now at `L^mR^k`, is

\[
pX\le_{\rm lr}C_k-X=p_k=E_1.
\]

Old time order and (13) put `E_1` below `q_1`. We have therefore established the same four initial gates for **every `m>=0,k>=2`**, with the stronger chain `pX<=lr E_1<=lr q_1`.

This corollary does not assert that the new seeds `A=(C_k-Y)/y`, `B=(C_(k-2)-Y)/y`, the new trace `3yC_(k-1)-x`, or their mixed templates have the required folded-cone and quantitative mass properties. Those analytic gates remain the genuine obligations for extending the final Local TP2 theorem from the proved `k=2` family to arbitrary `k>=3`.
