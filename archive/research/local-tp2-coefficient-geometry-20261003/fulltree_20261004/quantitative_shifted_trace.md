# A uniform shifted-trace lemma from smoothed strength

**Status: proved conditional infinite lemma. Its smoothed-strength hypothesis
is not established for every canonical center.**

Let `v` be a positive finite half-row of degree at least one. Suppose it is
`lambda`-strong, with `lambda>=4`:

`delta_n(v)>=lambda v_n` throughout its support.

In particular its folded kernel is TP2, so `v` is nonincreasing, and its
terminal entry is at least `lambda`. Thus every supported `v_n>=lambda`.
For any `r in [-2,2]`, define

`b_0=3v_0-r`, `b_1=3v_1-1`, `b_n=3v_n` for `n>=2`.

Then **b is `(3lambda/2)`-strong**, uniformly over the entire interval of r.
Its support is exactly the positive support of v, since `v_0,v_1>=lambda`.

Put `mu=3lambda/2`. Expansion gives

`delta_0(b)=9delta_0(v)-3r(2v_0+v_2)+12v_1+r^2-2`,
`delta_1(b)=9delta_1(v)-6v_1+3r v_2-3v_3+1`,
`delta_2(b)=9delta_2(v)+3v_3`,
`delta_n(b)=9delta_n(v)` for `n>=3`.

Zero extension covers low degrees without omitted boundary cases. The
zero-index margin `delta_0(b)-mu b_0` decreases with r because its derivative
is `-6v_0-3v_2+2r+mu<=-9lambda/2+4<0`. Its minimum is at r=2, where

`delta_0(b)-mu b_0`
` >=(9lambda/2-12)v_0+12v_1-6v_2+2+3lambda`
` >=(9lambda/2-12)v_0+6v_1+2+3lambda >0`.

The index-one margin is minimized at r=-2, giving

`delta_1(b)-mu b_1`
` >=(9lambda/2-6)v_1-6v_2-3v_3+1+3lambda/2`
` >=(9lambda/2-15)v_1+1+3lambda/2 >0`.

Both last coefficients are positive for lambda>=4. At every remaining
supported index the margin is at least `(9lambda/2)v_n>0`.

For a polynomial P, apply this to `v=H((x+1)P)`. The resulting row is
exactly `H(3(x+1)P-x-r)`. Therefore sufficiently strong *smoothed* kernel
control provides **all shifted trace factors** required by a generic
Jacobi-resolvent run argument, with a uniform quantitative margin.
The shift r is not restricted to actual Jacobi roots.

The subtraction lemma in `quantitative_subtraction.md` is a possible way
to establish the needed smoothed strengths at canonical nodes. Its finite
checks do not yet prove that global premise. This lemma consequently does
not close the arbitrary-turn induction by itself.
