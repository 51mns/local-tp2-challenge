# A finite common-state reduction with exact two-child transport

**Status. ROOT: proved (with an explicit root exception to two LR links). IMPLIES TARGET: proved. LEFT/RIGHT: the four LR companion inequalities close; preservation of two actual folded kernels and one explicit proxy surplus remains open.** This is a common-state reduction, not a common closure theorem, and does not prove another path family.

This note uses the already proved ordinary positivity, degree orientation, dense support, and normalized mutation theorem in `../fulltree_20261004/invariants_normalized_state.md`. It uses the established folded-kernel TP2 transport theorem; it does not use any one-turn or second-turn Local TP2 theorem to prove its companion transport. The direct original-child algebra below was derived independently. The simplification of the proxy to a self defect plus one mixed correction was also independently supplied by the `pair_*` lane.

## 1. Original children and universal ray identities

Put `y=x+1`, `P=x+2`, `z=2x+3`. Orient endpoints `X,Y` by degree and let `C` be the center. Thus

    X=1+ya, Y=X+ye, C=Y+yg,
    t=3yX-x, k=X(3X-2),
    g=(t-2)e+k+r.

Use capital letters for the actual, already smoothed gaps:

    E=Y-X=ye, G=C-Y=yg, R=yr,
    Z=a+e+g=(C-1)/y,
    M=3yC-x+1=2P+3y²Z.

The original children retaining `X` and `Y` are respectively

    U_X=3yXC-x(X+C)-Y,
    U_Y=3yYC-x(Y+C)-X.

The first has lower degree, and the actual target quantities are

    S=U_X-C=tG-R,
    D=U_Y-U_X=EM.                                      (1)

For the first identity, substitute `yr=G-(t-2)E-yk`. It gives
`S=(t-1)G+(t-2)E+yk`; using `G=C-Y`, `E=Y-X`, and
`yk=yX(3X-2)` reduces this to `(t-1)C-xX-Y`, exactly `U_X-C`.
The second identity follows by subtracting the two original children.
No Fricke division or Fourier shape assumption enters (1).

The two degree-ordered children have states `(X,C,U_X)` and
`(Y,C,U_Y)`. These are called **short** and **long** below; do not
identify them with a fixed named Farey L/R edge when degree orientation
has swapped the original endpoint labels.

There is a universal version of the ray sandwich identity:

    J=y(t-2), B=zX-P=y(1+za), T=G+B,
    S=JZ+T.                                            (2)

Indeed
`S-JZ=y[2g-r-(t-2)(a+e)]`
and `g=(t-2)e+k+r` imply
`S-JZ=yg+y[k-(t-2)a]`. The last bracket is `1+za`.
Thus the correction is positive at every canonical state. In particular
(2) replaces a path-specific Chebyshev-prefix identity algebraically;
it does not prove its LR comparison.

The simpler proxy used here retains only `G` in the correction:

    Q=S-G=(t-2)C-xX=JZ+B,
    Π=XP M.                                            (3)

Both `Q` and `Π` have positive ordinary coefficients and dense Fourier
support. A useful further exact identity is

    V=PX+P²C,
    Π=PQ+V.                                            (4)

Consequently the proxy surplus is exactly

    W_n(Q,Π)=δ_n(Q)+W_n(Q,V),                           (5)

where `W_n(f,h)=H(f)_n H(h)_(n+1)-H(f)_(n+1)H(h)_n`.
Here `W_n(Q,PQ)=δ_n(Q)` including `n=0`: at zero the reflected
coefficient formula is `H(PQ)_0=2q_0+2q_1`. This avoids introducing
an unjustified cone-preserving multiplication by `y`.

## 2. A sharp sufficient comparison criterion

All LR orders in this note mean **every ordered half-row minor** is
nonnegative. Adjacent minors suffice because the canonical rows are
positive on one dense initial support interval; beyond support the
remaining required minors are zero or positive. Let `K_f` denote the
folded multiplication kernel from the brief.

At one canonical state, the following finite criterion suffices:

1. `G <=lr S`;
2. `XP <=lr E`;
3. `K_M` is TP2;
4. `W_n(Q,Π)>0` for `0<=n<deg S` (equivalently the surplus (5)).

Then strict Local TP2 holds. To see this, linearity gives

    W_n(S,Q)=W_n(G,S),

so the first link is exactly `S<=lr Q`; no stronger first-link premise
has been inserted. Folded TP2 transport of item 2 through multiplication
by the actual `M` gives `Π<=lr EM=D`. Thus

    S <=lr Q <lr Π <=lr D.                             (6)

For every `n<deg S`, all four rows have positive entries at both
indices and the strict middle comparison survives transitivity.
The terminal target index is automatically

    W_(deg S)(S,D)=H(S)_(deg S) H(D)_(deg S+1)>0.

In fact if `p=deg X`, `q=deg Y`, and `c=deg C`, then

    deg S=deg Q=p+c+1,
    deg Π=p+c+2,
    deg D=q+c+1 >=p+c+2.

The strict terminal proxy comparison is automatic for the same reason.
Hence it is harmless to state item 4 through `n=deg Q`, as the exact
checker does. This is a noncircular criterion: it compares `Q` to the
fixed endpoint proxy `XP M`; it does not assume the actual `(S,D)`
comparison or any descendant target comparison.

The alternative first-link criterion in (2) is equally exact:
`W_n(S,JZ)=W_n(T,S)`. It yields the older sandwich when paired with
a strict `JZ<lr Π` comparison. Splitting `T=G+B` is invalid at the
root, where `B<=lr S` fails centrally. Also, fixed base minors of
`(J,3y²XP)` are not universally nonnegative: at `a=0`, the index-one
minor is `-12`. We therefore do not promote those fixed base-minor
conditions to a common predicate.

## 3. The finite regular predicate and the completed LR subsystem

On nonroot canonical states, define the proposed regular predicate
`P_Q` by the four row comparisons

    E <=lr G,       R <=lr G,
    XP <=lr E,      YP <=lr G,                          (7)

and the three analytic gates

    K_G is TP2,     K_M is TP2,
    δ_n(Q)+W_n(Q,V)>0 for 0<=n<=deg Q.                  (8)

Only a fixed number of actual polynomial rows occurs. Ordinary
positivity, full support, degree ordering, and the canonical Fricke
constraints remain background requirements; they are not replaced by
positivity of arbitrary mixtures. The canonical root is a separately
specified seed, since its `E<=lr G` and `R<=lr G` comparisons are false.
The common proposed state predicate is `root OR P_Q`.

### Lemma: the four LR links close once the analytic gates close

Assume (7)-(8) at a regular state. Then all four links (7) hold at
**both** children. No child Local TP2 premise is used.

First `1<=lr P<=lr t`. The first comparison follows from the unit
row and positivity. For the second, write `x_i=H(X)_i`. Since
`H(X)_0>=1`, the only possibly nonzero adjacent base minors are

    W_0(P,t)=3x_0+6x_2-2 >=1,
    W_1(P,t)=H(t)_2 >=0.

Indeed `H(t)_0=3x_0+6x_1` and
`H(t)_1=3x_0+3x_1+3x_2-1`. The full ordered comparison follows
from dense support and terminal zeros.

Transport through `K_G` gives

    G <=lr PG <=lr tG.

The old `R<=lr G` consequently implies `R<=lr PG`. By the exact
subtraction identity (1),

    W_n(PG,S)=W_n(PG,tG)+W_n(R,PG)>=0.                 (9)

Likewise
`W_n(G,S)=W_n(G,tG)+W_n(R,G)>=0`, so item 1 of the
sufficient criterion holds. Items 2-4 follow from (7)-(8), and (6)
proves the actual strict target, in particular `S<=lr D`.

The endpoint link is strengthened for free:

    YP <=lr G <=lr S,
    PG <=lr S,
    CP=YP+PG <=lr S.                                  (10)

The sum in (10) is legitimate because both summands are below the same
fixed row `S`. No convexity assertion for the folded cone is used.

The exact actual-gap updates are

| child | X' | Y' | E' | R' | G' |
|---|---|---|---|---|---|
| short | X | C | E+G | G | S |
| long | Y | C | G | E+G | S+D |

For the short child, `E+G<=lr S` follows because both `E` and `G`
are below the fixed row `S`. Also `G<=lr S`. Thus both first links
in (7) hold. Both `XP<=lr E` and `XP<=lr G` hold, so
`XP<=lr E+G`. Finally (10) is exactly `Y'P<=lr G'`.

For the long child, `G<=lr S+D` and `E+G<=lr S+D` follow because
all summands are below the fixed rows `S` and `D`; transitivity uses
`S<=lr D`. Its endpoint comparisons are respectively the old
`YP<=lr G` and `CP<=lr S+D`, the latter following from (10) and
`S<=lr D`. This completes all four child LR links.

More explicitly, for every ordered coefficient-index pair, the eight
transported companion minors are the following fixed finite collection:

| link | short child minor | long child minor |
|---|---|---|
| E' versus G' | W(E,S)+W(G,S) | W(G,S)+W(G,D) |
| R' versus G' | W(G,S) | W(E,S)+W(E,D)+W(G,S)+W(G,D) |
| X'P versus E' | W(XP,E)+W(XP,G) | W(YP,G) |
| Y'P versus G' | W(YP,S)+W(PG,S) | W(CP,S)+W(CP,D) |

All blocks on the right are nonnegative by (7), (9), (10), and the
target comparison already **derived** from the parent predicate. These
are identities for minors, rather than an assertion that arbitrary
positive sums preserve the folded cone.

This isolates the real common-closure obligations: **only** the actual
new `G` kernel, the actual new `M` kernel, and the new proxy surplus
in (8). Their preservation is not proved by this note.

## 4. Exact left/right transport of the remaining gates

All following identities hold as polynomial identities, retaining the
original smoothing factors. Put `F=S+D`, `t_L=t+3yE`, and
`A=t-1`. Here subscript `L` means the long child, not a fixed Farey L.

| coordinate | short child | long child |
|---|---|---|
| a | a | a+e |
| e | e+g | g |
| r | g | e+g |
| t | t | t_L |
| Z | Z+s | Z+s+d |
| B | B | B+zE |
| S | tS-G | t_LF-(E+G) |
| T | S+B | F+B+zE |
| M | M+3yS | M+3yF |
| D | (E+G)(M+3yS) | G(M+3yF) |
| Q | (t-1)S-G | (t_L-1)F-(E+G) |
| Π | Π+3yXP S | Π+PD+3yYP F |
| V | V+P²S | V+PE+P²F |

Here lower-case `s=S/y`, `d=D/y` are exact quotients, so `Z+s`
and `Z+s+d` introduce no Fourier-kernel assumption about division
by `y`.

The proxy also has a form suitable for the self-defect-plus-correction
identity (5):

    Q_short=Q+(t-2)S,
    Q_long=Q+(t-2)F+E(M-1+3yF).                        (11)

The exact ordered-minor closure equations for the proxy are therefore

    W(Q_short,Π_short)
      =W((t-1)S,Π)+W((t-1)S,3yXP S)
       -W(G,Π)-W(G,3yXP S),                           (12)

    W(Q_long,Π_long)
      =W((t_L-1)F,Π+PD)+W((t_L-1)F,3yYP F)
       -W(E+G,Π+PD)-W(E+G,3yYP F).                    (13)

These equations apply to every ordered pair of indices, and hence to
central and terminal adjacent indices. Equivalently substitute (11)
and the displayed `V` updates in (5). Equations (12)-(13) are a finite
collection of companion **mixed-minor surplus** inequalities; replacing
the negative terms separately by uncorrelated upper estimates may lose
the canonical cancellation. No sign has been asserted for the individual
mixed blocks.

For the two kernel gates, let `D_n(f,h)` denote the polarization
`δ_n(f+h)-δ_n(f)-δ_n(h)`. Explicitly, with reflected/zero-extended
half-rows `f_i,h_i`,

    D_n(f,h)=2f_nh_n-f_(n-1)h_(n+1)-h_(n-1)f_(n+1)
             -2f_(n+1)h_(n+1)+f_nh_(n+2)+h_nf_(n+2).

The exact finite defect blocks needing closure are

    δ_n(G_short)=δ_n(tG)+δ_n(R)-D_n(tG,R),
    δ_n(G_long)=δ_n(S)+δ_n(D)+D_n(S,D),                (14)

    δ_n(M_child)=δ_n(M)+9δ_n(yG_child)
                    +3D_n(M,yG_child).               (15)

The reflection convention is retained at `n=0`; zero extension is
retained at the top two indices. In particular (15) does not presume
that `y` preserves the cone. Nor can the polarization in (14) be
replaced by an arbitrary positive-mixture assumption. The previously
recorded canonical mixed-defect counterexamples remain relevant.

Equations (12)-(15), or their equivalent relative-minor versions, are
explicit remaining common transport obligations. They do not ask for
all descendants to satisfy Local TP2, and the completed LR proof shows
which other comparison hypotheses no longer need separate work.

## 5. Exact root and first-level seeds

At the root `(a,e,r)=(0,1,1)`, the actual half-rows are

    E=R: (1,1), G: (7,5,2), S: (40,32,16,4),
    D: (164,138,80,30,6),
    Q: (33,27,14,4), Π: (228,188,104,36,6),
    M: (64,50,24,6).

The root kernel defects are `δ(G)=(13,7,4)` and
`δ(M)=(632,688,240,36)`. The three sufficient-criterion comparisons
are

    W(G,S)=(24,16,8),
    W(XP,E)=(1),
    W(Q,Π)=(48,176,88,24).

Thus the criterion proves root Local TP2, whose direct minors are
`(272,352,160,24)`. The two rejected root LR links both have
`W_0(E,G)=W_0(R,G)=-2`; this is an exact root obstruction, not a
missing proof. Also `W(YP,G)=(2,3)` and `W(CP,S)=(40,48,8)`.

Both children satisfy the entire regular predicate. The four LR-link
minor lists, omitting zeros beyond the shorter support, are

| link | short root child | long root child |
|---|---|---|
| E'<=G' | (16,32,8) | (170,140,68) |
| R'<=G' | (24,16,8) | (136,236,68) |
| X'P<=E' | (4,2) | (2,3) |
| Y'P<=G' | (40,48,8) | (408,508,148,12) |

Their actual folded defects and strict proxy minors are

    short: δ(G')=(192,256,112,16),
      δ(M')=(11864,19240,9480,2052,144),
      W(Q',Π')=(2004,5772,3448,1008,96);

    long: δ(G')=(3400,5880,2856,544,36),
      δ(M')=(180320,315160,188820,53568,6624,324),
      W(Q',Π')=(1221944,2423832,1730408,638012,121452,10764,324).

These finite seed checks establish `root -> P_Q` for both children
exactly. They do not establish regular-state closure of (8).

## 6. Reproducer and current scope

`reduction_common.py` is standalone Python integer arithmetic. It
imports no parent implementation, builds both original scalar children,
divides the exact normalized coordinates by `y`, checks the universal
identities and both-child transport, and tests the candidate rows.
`reduction_common_results.json` records its bounded depth-five run:
63 states, with no candidate failure except the two displayed root LR
links. This scan is implementation validation and bounded evidence only.

The predicate is frozen before any broader scan as (7)-(8), together
with the explicit root seed. The LR closure and target implication
above are complete. The kernel and proxy preservation gates remain
**unproved**, and therefore no all-tree claim follows from this note.
