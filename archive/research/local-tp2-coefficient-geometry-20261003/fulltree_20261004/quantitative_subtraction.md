# A local subtraction bound for canonical mutation

**Status: the general identity and inequalities below are proved. The coarse canonical
lower-margin condition fails at `R^13`; cancellation in the exact remainder
is indispensable.
This is not a proof of Local TP2 or of global canonical folded-cone closure.**

Write `H(P)_n=[q^n]P(q+q^-1)` and extend every finite half-row symmetrically,
then by zero. Put

`delta_n(h)=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2)`.

## 1. Subtraction lemma, with a nonnegative exact remainder

Let `f,g` be nonnegative finite symmetric rows, assume `f_n` is nonincreasing
for `n>=0`, and suppose `c=f-g>=0` entrywise. For any real `lambda`, define

`B_n=delta_n(f)-lambda f_n-f_n(3g_n+g_(n+2))`
`    +g_n(g_n+g_(n+2)+lambda)`.

Then the following is an exact identity at every `n>=0`, including zero:

`delta_n(c)-lambda c_n=B_n+R_n`,

where

`R_n=g_n(f_n-f_(n+2))+g_(n-1)f_(n+1)`
`    +c_(n-1)g_(n+1)+g_(n+1)(f_(n+1)+c_(n+1))`.

Every term of `R_n` is nonnegative. This identity follows by substituting
`c=f-g` into the four terms defining `delta`; the symmetry convention
`g_(-1)=g_1`, `c_(-1)=c_1` supplies the zero-index case without an exception.

Consequently, `B_n>=0` throughout the support is a sufficient condition for
`lambda`-strength of `c`. A simpler, stronger sufficient condition when
`lambda>=0` is

`delta_n(f)>=lambda f_n+f_n(3g_n+g_(n+2))`.

The sharper `B_n` retains the useful positive quadratic correction. There
is no arbitrary positive-sum or subtraction closure assertion here.

If `d=deg g`, the boundary specializes to

`delta_(d+1)(c)=delta_(d+1)(f)+g_d f_(d+2)`,

and `delta_n(c)=delta_n(f)` for `n>=d+2`. In particular subtraction of a
shorter row has a *favorable* first out-of-support boundary term. This
contrasts with adding a short correction, whose boundary term has the
opposite sign. These formulas do not decide the low indices `0,...,d`.

## 2. Application to the exact canonical mutation

Sort a canonical node's endpoints by degree as `X,Y`, and let `C` be its
center. Write `t_X=3(x+1)X-x`. At every nonroot node the inverse neighbor
`T` gives

`F=t_X Y`, `G=xX+T`, `C=F-G`.

At the root the same decomposition holds with `F=(2x+3)(x+2)` and
`G=x+1`. Thus the lemma applies with `f=H(F)`, `g=H(G)`, `c=H(C)`.
These nonnegativity and decrease hypotheses are **unconditional**:

- Canonical `X,Y,C,T` have nonnegative Fourier rows by the
  previously proved support theorem. Multiplication by x is Laurent
  nonnegative, so `g>=0` and `c>=0`.
- Canonical endpoint `X` has nonnegative character coefficients
  `alpha_j=H(X)_j-H(X)_(j+1)`, with `alpha_0>=1`.
- In the character basis `B_j=sum_(i=-j)^j q^i`, the row of `t_X` is
  `3alpha_1+1` at zero, `3(alpha_0+alpha_1+alpha_2)-1` at one, and
  `3(alpha_(j-1)+alpha_j+alpha_(j+1))` at `j>=2`. These are nonnegative.
- The positive character product rule makes `F=t_XY` character-positive,
  so `f` is nonincreasing. Multiplication by `y=x+1=B_1` preserves
  character nonnegativity. The same reasoning therefore applies to
  `yC=yF-yG` as well.

These observations validate the subtraction lemma's hypotheses throughout
the tree without assuming its desired folded-cone conclusion.

If the explicit margins `B_n` are nonnegative for `lambda=lc(C)`, they
prove the optimal leading-coefficient strength of `C`: no greater strength
is possible, since its terminal defect divided by its terminal entry is
exactly `lc(C)`. For `yC`, only nonnegative defects are needed by the
existing center-cone reduction; setting `lambda=0` gives that obligation.

At a genuine switch, `deg T<deg X` and
`deg Y=deg X+deg T+1`. Thus `deg G=deg X+1`, while
`deg F=2deg X+deg T+2`. At a long fixed-endpoint run `deg T` can instead
be large; the lemma makes no unjustified bounded-degree assumption there.

## 3. Precisely bounded diagnostics

`quantitative_subtraction.py` reconstructs the canonical tree through a
specified depth from `tp2_source.py` using integers only. It independently
checks the exact remainder identity against the original defect formula
at every index. It checks the support-boundary identities as well.

The saved `--depth 7` run contains 494 unsmoothed/smoothed records with
`deg X>0`. For all those records, every `B_n` is nonnegative even with
`lambda=lc(C)` in both modes. The only paths with negative sufficient
bounds are the root and the pure-left boundary `L^j`, `1<=j<=7`.
Those negative bounds do not refute the actual cone property. For the
smoothed root the stronger *optimal-strength* assertion is actually
false: `H(yC)=(21,17,8,2)`, its central defect is 31, below `2*21`;
its defects are nevertheless nonnegative as already proved.

The number 494 is the number of finite diagnostic records, not a finite
certificate covering arbitrary depth. A targeted fixed-endpoint check in the same executable shows that the
condition is actually **false** on the canonical node `R^13`, already
with `lambda=0` and `n=0`:

`B_0=-13255405836475262089110874899224563418`,
`R_0=136369427728705566915805938015739962789`,
`delta_0(C)=123114021892230304826695063116515399371>0`.

The positive exact remainder more than compensates for the negative bound.
This is a counterexample to the proposed sufficient-margin invariant,
not to the actual canonical cone or Local TP2. It explains why the finite
depth-seven observation cannot be generalized.

## 4. Why a uniform coarse perturbation estimate is inadequate

Along a fixed-endpoint run, the ratio of the correction to the dominant
product can remain at a scale set by the fixed endpoint while the degree
increases without bound. A generic normalized-defect estimate that loses
with that degree therefore cannot establish closure uniformly merely
from `0<=G<=epsilon F`. The exact local remainder avoids discarding every
favorable term, but it still requires a proved lower bound on `B_n` or
some of the retained `R_n` terms.

The remaining useful target is an inequality that uses the canonical
Fricke/Cassini relations to retain enough of the exact `R_n` cancellation
and control `B_n+R_n`. The coarse `B_n>=0` target is refuted by the
canonical example above. The manuscript does not claim such
a proof and does not claim that center-cone closure alone would finish
the separate final Local TP2 comparison.
