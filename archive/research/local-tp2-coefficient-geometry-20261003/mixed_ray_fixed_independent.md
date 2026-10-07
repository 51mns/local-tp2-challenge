# Independent audit of the mixed-ray fixed tables and scalar bound

**PASS.** The standalone verifier `mixed_ray_fixed_independent.py`
constructs all polynomials directly as symmetric Laurent polynomials
in `q`. It imports no producer, Fourier-map helper, or earlier
polynomial module.

It verifies all five displayed rows `B0,b,Ay,By,K` in
`mixed_ray_all.md`, the masses `t(2)=223`, `w(2)=56`, `(Ay)(2)=663`,
and all **38 fixed adjacent minors** in the nine comparison tables:
the two initial gap-time comparisons, four endpoint comparisons,
two comparisons with `b`, and the five minors of `Ay,By`.
The five final correction margins are exactly

`(26844,95214,79830,9786,48)`.

The two seed centers and their next gaps were reconstructed from the
original canonical mutation, independently of the tables. The fixed
identity `b=(t-2)-xP=y(w+1)` was also verified; it is the constant
needed in the short-gap recurrence identity.

The scalar estimate for all `k>=4` was checked algebraically:

`40*(4/5)^2/2=64/5`, `100*(4/5)^2/2=32`.

The respective lower bounds for the two families are `288,720` at
`k=4`, and `1152/5,576` at `k=5`, all greater than `75`.
Advancing `k` by two multiplies either bound by
`90k/(k+2)>1`; hence these two bases prove the bound for every
`k>=4`, without a finite cutoff. The summand-mass ratios used in this
estimate are safely bounded below by `56/57` and `278/279`, each
greater than `1/2`.

No arithmetic discrepancy was found. The positive resolvent weights,
compatible-kernel theorem, and continuum margin certificates remain
the separate explicit proof dependencies. Their existing independent
audits and the already audited 81 original finite-base minors were
not duplicated here.

The machine-readable result is `mixed_ray_fixed_independent.json`.
