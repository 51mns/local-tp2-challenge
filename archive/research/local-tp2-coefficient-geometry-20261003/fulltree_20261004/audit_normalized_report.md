# Independent audit of normalized canonical constraints

**PASS for the stated all-depth algebra and coefficient inequalities. Local TP2 remains unproved.**

Audited manuscripts:

- `invariants_normalized_state.md`, Sections 1–4.
- `network_quotient_constraints.md`, Sections 1–5, including the final two-step obstruction.

The accompanying `audit_normalized_symbolic.py` uses a separately implemented sparse multivariate integer polynomial ring and imports no research modules. It checks arbitrary-symbol identities, rather than identifying formulas from finitely many trees or barrier indices. `audit_normalized_results.json` records checks and hashes of the exact audited sources.

## 1. Canonical state and nonlinear identity

The root state `(a,e,r)=(0,1,1)` and both positive updates are correct. Direct substitution into the original scalar mutations establishes the new endpoints and centers, the actual quotients `S/y=s`, `D/y=eM`, and the short/long remainders. The labels short/long are degree-oriented and are not globally fixed Farey L/R letters.

For independent symbols `x,a,e,g`, the original cubic residual is exactly

```
y² [g²-(t-2)e(e+g)-k(g+2e)-3aX²].
```

After substituting `g=(t-2)e+k+r`, its normalized value is

```
F = rg-(t-2)e²-2ke-3aX².
```

Both normalized updates preserve `F` as a polynomial identity. Its value at the root is zero. Consequently the two displayed positive Fricke product identities are valid at every canonical node, not merely at tested nodes. The ancestral endpoint formula and the square-dominance identity, including its off-surface residual `F`, also pass.

The final added normalized Cassini identity also passes independently:

```
g²-rs-X²(1+3a) = -(t-2)F.
```

It therefore gives `g²-rs=X²(1+3a)` on the canonical surface. This is a polynomial product identity, not an assertion about neighboring Fourier coefficients.

## 2. All-depth nonnegativity, support, and bounds

The proofs of `0<=a<=e`, `0<r<=a+e`, and `g>=a+e+r+1` are valid coefficientwise in the ordinary `x` basis. The growth certificate is a polynomial with nonnegative coefficients; it establishes the long-step bound without assuming the conclusion. The short and long upper-remainder transports reduce respectively to `a+e` and `a`.

The dense-support claim also follows inductively. A nonzero dense polynomial here has support exactly the integer interval from zero to its degree. Sums and products of such polynomials retain dense support. The zero root coordinate `a` is handled separately; the other coordinates are nonzero from the root onward. Once `a` becomes nonzero, both updates preserve its dense support. The displayed positive formulas then give dense support for `g,s,d`. This argument establishes ordinary coefficient density only.

The stronger remainder separation

```
g-(t-1)r = (t-2)(a+e-r)+1+(2x+3)a >= 0
```

is correct. Its ray decomposition into `U_j(t/2)` and their consecutive differences follows directly from the Chebyshev recurrence. Neither summand is thereby certified as a folded-TP2 multiplier.

## 3. Sharp scalar bounds and every-index barriers

The induction for `c e<=r<=phi e`, where `c²+c=1` and `phi=1+c`, is correct. It uses `t-2>=1` coefficientwise and the previous lower bound to obtain `g>=(1+c)e`. Both short and long estimates reduce exactly to the defining quadratic equation for `c`. The pure-short constant-term recurrence gives the stated Fibonacci formulas and the lower limiting ratio `c`; one subsequent long step yields the upper limiting ratio `phi`. These constant terms suffice to prove optimality of both universal scalar constants.

The polynomial barrier proof is valid for every `m>=0`. The auditor checks the recurrence with generic formal previous values `p,q`:

```
p'=zq+p,  q'=(z+1)q+p,
q'-p'=q,
zq'(q'-p')-(p')² = zq(q-p)-p².
```

Thus the quadratic identity follows by induction from `p=0,q=1`, without a finite bound on `m`. The short transport identity is likewise checked with arbitrary formal `z,e,r,k,p,q`, and the long expression is manifestly nonnegative. Tree induction assumes all indices simultaneously; the short step uses index `m-1` at the preceding tree depth. There is no circular induction or unchecked infinite tail. The trailing-short expansion is repeated application of this exact transport with fixed `t,k`.

## 4. Conditional LR statements and remaining gap

The selective LR transport statements are valid **as conditional statements**. For the dense nonnegative half rows under discussion, LR comparisons compose, and positive sums preserve comparisons with a fixed upper or lower row. The zero `a` row creates no difficulty. The Christoffel–Darboux expression is the elementary determinant identity

```
W(g',t'g'-r') = W(g',t'g')+W(r',g').
```

If the folded multiplication kernel of `g'` is TP2, it transports the input comparison between the constant polynomial `1` and the nonnegative polynomial `t'`, giving the required broadening term. This is a conditional use of TP2, not a proof that the needed kernel has that property.

The manuscripts correctly leave open preservation of the actual folded kernels, the final outgoing quotient LR comparison, and transport through multiplication by `y=x+1`. None of the new ordinary coefficient inequalities alone establishes these missing quadratic comparisons. The independently bounded falsification probes are separate evidence and are not used in this audit's all-depth conclusions.

The finite numerical counts and random-stress statistics in Section 5 of the invariants manuscript were not rerun for this symbolic audit; they are explicitly labelled finite evidence there.

## 5. Final two-step obstruction addition

The `(r,h)` short-ray update is exactly `N=[[t-1,1],[t-2,1]]`. Independent symbolic multiplication confirms all four entries of its displayed square. Direct binomial Fourier transforms give `(2,2)` for its root lower-right entry `2x+2`, and `(13,12,4)` for the root product `(t-2)(t+2)=4x²+12x+5`. Their central folded defects are exactly `-4` and `-67`.

These negative values refute the specified assertion that all scalar entries or extreme-root pair factors have folded-TP2 multiplication kernels. They are not canonical Local TP2 counterexamples and do not exclude all possible grouped or coupled-network arguments. The updated source hashes are recorded in the accompanying JSON.
