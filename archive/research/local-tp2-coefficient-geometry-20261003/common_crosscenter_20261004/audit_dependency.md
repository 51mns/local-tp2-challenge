# Independent cross-center dependency and minimality audit

Status: **PARTIAL.** Existing origin/register consequences pass within their
stated scope. Additional child support, degree, and central-trace subgates
are noncircular. Full paired child packets and the proxy overlap remain
OPEN. This audit does not infer any infinite claim from sampled states.

## 1. Exact directed implications

The parent regular predicate comprises canonical ordinary bounds, Fricke
and ancestry, four LR companions, two current paired `MP_sharp` packets,
two certified origin registers, and the strict proxy. The exact initial
root uses its established exceptional clause for the LR links.

| Source | Derived conclusion | Does it use a child packet? |
| --- | --- | --- |
| Smaller parent origin, previous index at least one | Current `K_G` | No |
| Current trace gate at parameter `-1` | Current `K_M` | No |
| Current `K_G,K_M`, LR and strict proxy | Parent target and all four child LR companions | No |
| Parent registers plus current paired packets | Both child register identities/certificates | No |
| Transported smaller child origin plus Robin/boundary theorem | Strict child `K_Q`, raw `Q` kernel, including zero/interior/terminal | No |
| Strict child `K_Q` and exact degree/support identities | Strict proxy tail and terminal | No |
| Parent forward packet; parent reversed Robin `q_2+q_1` | Both reversed child `L'_-1`, raw/y | No |
| Parent trace central cone plus retained-origin strict `v` | All shifted child trace **central defects** | No |
| New paired child packet | Child full trace, single-block and mixed gates; hence new initialization data | This is the open component |

The LR step consumes the **parent** proxy, which is part of the induction
hypothesis. It cannot be invoked to infer the child proxy. The `K_Q`
consequence uses the retained origin, not the new center. No cycle is
present in the preceding proved arrows.

The remaining proxy index interval is exactly

`0 <= n <= min(deg Q' - 1, deg C' + 2)`.

Its zero condition is
`q0^2 - 2 q1^2 + q0 q2 + q0 v1 - q1 v0 > 0`.
The interior conditions retain the signed correction
`delta_n(q) + q_n v_(n+1) - q_(n+1) v_n > 0`.
Strict `K_Q` alone does not imply these comparisons. In particular a
negative correction at `n=deg V<deg Q` is compatible with a positive
proxy, so sourcewise correction nonnegativity is a false simplification.

## 2. Why H and seed cones remain redundant

The audited sharp packet has three analytic gates: shifted-trace cones,
strict supported single blocks in raw/y, and the exact all-ordered mixed
gate. The strict degree hypothesis ensures that every `L_r` has degree
at least the shifted-trace degree. The strict-times-weak product argument
then proves strict `F=L_r(T-s)` and `G=L_s(T-r)`, including column zero
and the terminal defect. Thus `H=(F+G)/2` has positive support and strict
defects from positive diagonal tensors plus the nonnegative mixed tensor.

No raw/y seed cone is needed. In particular `yb0=y` at the reversed root
has central defect `-1`; inserting such a premise would invalidate ROOT.
The exact finite character theorem covers all ordered minors and cannot
be replaced by adjacent checks for the mixed/reference condition.

## 3. Child support and degree are already supplied

Write `dX=deg X`, `dY=deg Y`, `dC=deg C`; canonical degrees give
`dY>dX>=0` and `dC=dX+dY+1`. Let `u` be the retained endpoint trace,
`n=g+(1-sigma)e`, `v=s+sigma d`, and `T'=T+3y^2v`.

The actual retained origins supply raw positive interval support for
`g`, `v`, and the next outgoing term `s'`. Ordinary origin indices are
in the certified range. For endpoint 1, the separately proved raw
`U_N(x+3/2)` theorem applies. The identities `e'=n`, `g'=v`,
`c'=n+v+s'`, with the next outgoing term of strictly largest degree,
therefore supply positive interval support for `e'` and `c'` without
asserting TP2 of their positive sums.

Canonical ordinary positivity gives

`T'-r = 2x+3-r+3y^2 Z'`, `Z'=a'+e'+g' >=_coefficient 0`, `Z'!=0`.

For `r in [-2,2]`, this polynomial has nonnegative ordinary coefficients.
The leading term of `Z'` supplies the top two consecutive ordinary powers
in `y^2Z'`. Their Laurent expansions fill both parities throughout the
degree interval. Thus every shifted child trace has strictly positive
Fourier interval support. Products with the positive-interval seeds and
addition of the other nonnegative seed prove all raw single-block
supports. Multiplication by the Laurent-positive `y` proves their y
supports; this makes no TP2 claim about `y`.

The leading degrees are

| Child | `deg v` | `deg T'` | `deg c'` | `deg e'` |
| --- | --- | --- | --- | --- |
| short | `dX+dC` | `dX+dC+2` | `2dX+dC+1` | `dC-1` |
| long | `dY+dC` | `dY+dC+2` | `2dY+dC+1` | `dC-1` |

The forward strict degree condition is immediate. For the reversed
orientation, `deg e'+deg T'-deg c'` is `dY+1` (short) or `dX+1` (long),
strictly positive even at endpoint 1. Hence support and degree clauses
need not remain separate unknowns in child packet transport.

## 4. Central trace preservation is a genuine BOTH subgate

For a nonnegative row triple define

`D(a)=a0(a0+a2)-2a1^2=delta_0(a)`.

If `D(a),D(b)>=0`, the polarized cross term satisfies

`2a0b0+a0b2+a2b0-4a1b1 >= 0`.

Indeed the first three terms equal
`a0(b0+b2)+b0(a0+a2)`, at least
`2 sqrt(a0b0(a0+a2)(b0+b2))`, at least `4a1b1`.
This proof also covers zero first coordinates. Therefore
`D(a+b)>=D(a)+D(b)`.

The factor `y^2` has half-row `(3,2,1)` and defects `(4,0,1)`; it is a
weak folded-TP2 polynomial. The retained-origin term `v` is raw strict
and has degree at least two: the short register has index `N_X>=2`;
the long register has `N_Y>=1` at an endpoint trace of degree at least
two. Endpoint-1 raw `U_N` is covered by its established independent
factor proof. The strict-times-weak degree lemma therefore makes
`3y^2v` strict throughout support.

At every real `r in [-2,2]`, the parent shifted trace has nonnegative
row and `delta_0(T-r)>=0`. Since `T'-r=(T-r)+3y^2v`,

`delta_0(T'-r) >= delta_0(T-r)+delta_0(3y^2v) > 0`.

This uses neither a child trace cone nor a child packet or proxy. It
proves one defect at every parameter, not the other defects or all
ordered trace minors. Those distinctions remain explicit.

## 5. Exact continuum reduction for shifted traces

For any polynomial `f` whose `f-2` row has positive interval support,
the full trace cone on `r in [-2,2]` is equivalent to the two endpoint
cones `K_(f-2),K_(f+2)`. In `T_(f-r)`, every noncentral character
coefficient is affine in `r`. Its only quadratic coefficient is

`delta_0(f)-r(2h0+h2)+r^2`.

Since `h0>2,h2>=0`, its derivative is negative throughout the interval;
its minimum is the `r=2` value. Endpoint cone nonnegativity therefore
signs every coefficient for the full continuum. The equivalence uses
complete finite tensors, not merely endpoint adjacent defects.

Furthermore the trace gate implies pairwise compatibility for the whole
parameter square:

`J(f-r,f-s)/2 = T_(f-(r+s)/2) - (r-s)^2 T_1/4 >=_character 0`.

Every noncentral coefficient is affine in the midpoint and is signed by
the endpoints. The central coefficient is
`delta_0(f)-(r+s)(h0+h2/2)+rs`; it decreases in each coordinate and is
minimized at `r=s=2`. This is the packet-algebra lane's valid universal
lemma. It does not sign the cross-center tensor `J(T-r,3y^2v)`.

## 6. Scope ledger

| Obligation | Verdict |
| --- | --- |
| ROOT and both first-child full packets on continuous square, raw/y, all ordered minors | PASS by existing independently audited certificates |
| Algebra, four LR companions and two origin registers at BOTH children | PASS conditional on the regular parent package |
| Strict child `K_Q`, proxy tail/terminal, reversed `L'_-1` | PASS conditional BOTH consequences |
| Child packet supports/degrees, all shifted central trace defects | PASS additional conditional BOTH subgates |
| Full child trace beyond central; all-r strict singles; both mixed tensors | OPEN |
| Proxy overlap on regular edges | OPEN |
| TARGET implication from a complete regular predicate, and exact initial root | PASS; full-tree closure remains OPEN |

The final sharper reduction is recorded in `audit_gate_reduction.md`:
the trace family reduces to one endpoint and the actual fixed-origin
anchor band; reversed single upper bands and the mixed outer character
layer are supplied; and the valid alternative `P_D` predicate uses
`Q<D` in place of the old stronger proxy. Under that alternative the
only two remaining closure types are the new paired packet and the
new strict comparison `Q'<D'`. The original proxy route remains valid
but is no longer a mandatory extra gate.

The targeted verifier records exact algebra, root data, central-polarization
identities, and trace parameter formulas. Those checks replay the displayed
lemmas and are not substituted for their continuum or infinite-index proofs.
