# Independent audit: child supports, degrees, and the one-endpoint trace gate

**Verdict: PASS conditional BOTH gate reduction; full closure PARTIAL.**
Assume a canonical regular parent with the current paired sharp packets
and the two certified actual origin registers. No child packet is used.

## 1. Child packet support and degree clauses are not missing gates

Put `dX=deg X`, `dY=deg Y`, `dC=deg C`. Canonical degree ordering gives
`0<=dX<dY`, `dC=dX+dY+1`. These formulas follow from the positive
leading term of `(t-2)e` in `g`: it has degree `dX+dY`, above both
`deg k=2dX` and `deg r<=deg e=dY-1`. At endpoint `X=1`, the trace's
leading coefficient is 2, so the same degree statement still holds.

Write the exact child data as

`u=T-3y^2 n`, `v=s+sigma d`, `n=g+(1-sigma)e`,
`T'=T+3y^2 v`, `c'=(u+1)v+(1-2sigma)e`, `e'=n`.

Both `g` and `v` are raw positive-interval origin terms. The next term
`s'` of the retained origin has strictly larger degree. The exact
mutation also gives `g'=v` and `c'=n+v+s'`. Thus `e'=g` or `e+g` has
positive interval support, and `c'` has the interval support of its
largest summand `s'`, all summands being Laurent nonnegative. Ordinary
origin raw positivity/strictness follows from the sharp origin theorem;
the endpoint-1 raw `U_N` theorem is imported independently from
`../continuation_independent_audit.md`.

For every `r in [-2,2]`,

`T'-r=2x+3-r+3y^2 Z'`, `Z'=a'+e'+g'`.

Canonical ordinary bounds make `Z'` a nonzero polynomial with
nonnegative coefficients. The leading monomial of `Z'`, after
multiplication by `y^2`, supplies the highest two consecutive ordinary
powers. Their Laurent expansions fill both parity classes at every
index through the degree. The remaining terms are nonnegative.
Therefore shifted trace support is strictly positive throughout its
initial Fourier interval, uniformly in the full continuous parameter
box. This does not assert that the shifted trace is TP2.

Products of positive interval rows have positive interval support.
Consequently both orientations of `L'_r=b0'(T'-r)+b1'`, and their
`y` multiples, have the required supports. Here multiplication by `y`
is used only for nonnegative support, never for cone preservation.

The degrees are

| Mutation | `deg v` | `deg T'` | `deg c'` | `deg e'` |
| --- | --- | --- | --- | --- |
| short | `dX+dC` | `dX+dC+2` | `2dX+dC+1` | `dC-1` |
| long | `dY+dC` | `dY+dC+2` | `2dY+dC+1` | `dC-1` |

In the reversed orientation, the strict degree margin
`deg e'+deg T'-deg c'` equals `dY+1` or `dX+1`, respectively.
In the forward orientation the margin is plainly positive. This
includes every endpoint and rules out leading-degree cancellation.

## 2. The complete shifted trace gate reduces to one endpoint

The exact folded-kernel criterion in
`../continuation_kernel/folded_kernel_theorem.md`, Section 2, states that
a positive Fourier interval row gives `K_f` TP2 if and only if all
supported defects `delta_n(f)>=0`. It proves all ordered minors from
the defect inequalities, including the central-column normalization
and support zeros.

For a fixed half-row `h=H(f)`, reflection at zero gives

`delta_0(f-r)=delta_0(f)-r(2h0+h2)+r^2`,
`delta_1(f-r)=delta_1(f)+r h2`,
`delta_n(f-r)=delta_n(f)` for `n>=2`.

The independent central theorem in `root_central_trace.md` proves
`delta_0(T'-r)>0` for **every** `r in [-2,2]`, from the parent packet
and retained origin. With Section 1 support already proved, the complete
remaining trace gate is therefore exactly

`K_(T'+2) is weak folded TP2`.

Necessity takes `r=-2`. Sufficiency follows because `h2>=0`, so the
`n=1` defect has its minimum at `r=-2`; all `n>=2` defects are unchanged;
the `n=0` family is already strict. The folded-kernel theorem then
supplies every ordered minor for every real parameter. This is a
continuum equivalence, not a two-point test without proof.

## 3. The remaining endpoint trace gate has a finite overlap

Let `f=T+2` have degree `d=dC+1`, and let `b=3y^2v` have degree
`D=deg T'>d`. The retained origin and the weak degree-two cone `y^2`
prove strict supported defects of `b`; the strict degree condition
holds because `deg v>=2` at BOTH children, including endpoint 1.

At every index `n>=d+2`, all four entries of `f` in the defect formula
vanish, so `delta_n(f+b)=delta_n(b)>0` through the terminal `D`.
At the preceding boundary,

`delta_(d+1)(f+b)=delta_(d+1)(b)-lc(f)b_(d+2)`.

Zero extension handles `D=d+1`, where the correction is zero and the
defect is already strict. The central defect is independently proved.
Thus, without introducing redundant obligations, the full child trace
gate is equivalent to the finite overlap inequalities

`delta_n(T'+2)>=0`, `1<=n<=min(d+1,D)`.

Some members of this interval can already be automatic in small degree
gaps; retaining them is a harmless upper bound on the remaining index
set. The statement covers zero, interior, the transition index, and
terminal separately. It does not assume `J(f,b)>=_character 0`.

## 3a. The actual origin anchor gives a stronger fixed trace band

The proxy-algebra lane proves the exact retained-origin identity

`(C'-1)/y=a_O+Z_N`,
`Z_N=b0 R_(N-1)+b1 R_(N-2)`, `R_j=sum_(i=0)^j U_i`.

Its initialization is `c+e-[1+z(a+e+g)]=(T-2)a`, so both new origins
share anchor `a_O=a`. Retention increments both the center quotient and
`Z_N` by the same actual outgoing origin term. The two root anchors are
zero. This is exact canonical ancestry algebra, not a cone assumption
on the anchor. For an ordinary smaller origin, `N>=2` and trace degree
at least two give `deg Z_N>=2`. The prefix resolvent proof supplies
strict raw `Z_N`, so `beta Z_N` is strict by the degree-controlled
product lemma.

Consequently

`T'=beta Z_N+(z+beta a_O)`, `z=2x+3`,
`h=1` if `a_O=0`, and otherwise `h=deg a_O+2`.

For every real parameter, all supported defects at `n>=h+2` equal
those of `beta Z_N` and are strict. Combining this with the central
theorem and the one-endpoint equivalence reduces the trace work to

`delta_n(T'+2)>=0`, `1<=n<=min(deg T',h+1)`.

Unlike the parent-degree band, this anchor band is fixed when the origin
is retained and its integer index advances. It is a valid stronger
conditional BOTH reduction. At endpoint 1, `a_O=0` and
`Z_N=R_(N-1)(2x+3)`. The imported strict raw prefix theorem in
`../continuation_prefix.md` covers `N>=3` by the same degree lemma.
The remaining `N=2` block is directly
`beta R_1=6y^2P`, with half-row `(60,48,24,6)` and defects
`(432,576,252,36)`. Thus the raw fixed trace band also includes the
retained endpoint-1 exception. The ordinary smoothed counterpart is
proved separately in the proxy-algebra note; smoothed traces are not
a requirement of the current sharp packet.

## 4. What this does not reduce

The single blocks still require strict defects over their full `r` box,
in BOTH raw and y modes. The child paired mixed gate still requires
the exact full-character tensors for all `(r,s)` and both orientations.
The all-ordered mixed/reference inequalities do **not** inherit the
single-polynomial defect criterion, so adjacent mixed checks cannot
replace their all-column character arrays.

The complete remaining new-packet problem is therefore: the one
endpoint trace anchor overlap; all-parameter strict raw/y singles; and
the two orientations of the sharp mixed tensor in raw/y. The regular-edge
comparison gate remains separate. ROOT and both first-child full
packets remain certified by the preceding campaign's exact continuum
certificates; TARGET is conditional on completing the regular predicate.

The packet-algebra lane further certifies reversed singles on the raw
upper band `j>=deg e'+2` and y upper band `j>=deg e'+3`, throughout
the parameter interval. The preceding boundary index is strict for
`r>=-1`. Its remaining low prefixes have an exact strict 2x2
copositivity criterion. Forward singles remain unsupplied. For each
mixed tensor with midpoint polynomial of degree `M`, its entire outer
character layer `a+b=2M` is already strictly positive: the terminal
column selector is `H(H)_k lc H`, and the lower-degree reference is
zero. Only the interior character layers remain unknown. Neither
deduction turns finite samples into a continuum proof.

## 5. Audit of the weaker strict comparison gate

The proposed replacement `Q <_lr D`, strict at every interior supported
Q index, is a valid weaker sufficient gate. Under the four old LR links
and `K_G`, the existing proof in
`../common_closure_20261004/reduction_common.md`, Section 3, derives
`G<=_lr S` and hence `S<=_lr Q`. The new chain

`S <=_lr Q <_lr D`

proves the target directly. Both endpoint supports are positive;
`deg D=deg Y+deg C+1>deg Q=deg X+deg C+1`, so the terminal strict
comparison is automatic. The same proof of all four child LR links
uses only the now-derived `S<=_lr D`, the old four links and `K_G`.
It does not require a separately assumed child target or proxy.

The old gate `Q<_lr Pi` implies this new one through `Pi<=_lr D`,
which is proved by transporting `XP<=_lr E` through `K_M`. The
converse is not asserted. A predicate with the weaker gate must invoke
the direct target/LR argument; it cannot claim implication of the old
`P_Q` proxy predicate. At the exact root,
`W_n(Q,D)=(126,228,100,24)`, all positive.

Neither the old proxy overlap nor the weaker `Q<D` transport has been
proved at arbitrary regular children. Adopting this logical reduction
does not establish full-tree Local TP2.

For the alternative predicate `P_D`, keep all canonical/LR/current
paired packet/origin-register components and replace only the strict
proxy by `Q<D`. ROOT and both first regular children are certified by
the existing stronger proxy and full packet bases. Under `P_D`, all
algebra/LR/register BOTH arrows and the new partial packet subgates
remain proved. TARGET follows directly from `S<=Q<D`. The exact two
remaining **closure types** are: (i) both new current-center paired
`MP_sharp` packets; and (ii) strict `Q'<D'` at both regular children.
The original proxy is an optional stronger sufficient route, not an
additional third requirement in `P_D`.
