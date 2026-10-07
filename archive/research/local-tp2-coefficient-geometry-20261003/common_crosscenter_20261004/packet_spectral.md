# Character compensation for common changed-center trace flux

**Status.** This proves two common child-trace subgates and isolates an
exact quantitative border obstruction. It does not prove either complete
changed-center paired `MP_sharp`, full trace TP2, the remaining proxy, or
full-tree Local TP2. All calculations use the actual canonical degree and
leading-coefficient correlations; the counterexample is explicitly relaxed.

The finite character/minor equivalence is the established theorem in
`../common_midpoint_20261004/network_relative_character.md`. Write
`T_f=Phi(f(xi)f(zeta))` and `J(f,g)=T_(f+g)-T_f-T_g`.
For Fourier half-rows `h=H(f)`, the coefficient at
`(i+j-1,j-i-1)` is the rows `(0,1)`, columns `(i,j)` folded minor

    R_f(i,j)=h_i(h_(j-1)+h_(j+1))-h_j(h_(i-1)+h_(i+1)).

Reflection and zero extension are understood. At zero the stated formula
uses `h_-1=h_1`; it therefore has the correct central-column normalization.

## 1. A necessary negative source at both changed centers

Let `f,g` have degrees `d,D`, positive leading coefficients `B,E`, and
`D>=d+2`. At rows `(0,1)`, columns `(d+1,D)`, polarization gives exactly

    J(f,g)[chi_(d+D)(U) chi_(D-d-2)(V)] = -B E.        (1)

Indeed row zero of `f` is zero at both columns; row one of `f` is `B`
at `d+1` and zero at `D`. The only surviving cross product is `-B E`.
This is an actual character coefficient, not a negative power coefficient.
It proves that two individually positive folded-TP2 summands can have a
negative mixed source. An additive network proof that signs every source
separately therefore cannot establish arbitrary changed-center traces.

Apply (1) to the unified exact child trace

    T'=T+beta v,    beta=3y^2,
    v=s                    (short),
    v=s+difference         (long), difference=e(T+1).

Let `d_X=deg X`, `d_Y=deg Y`, `d_C=deg C`. Canonical degree ordering gives

    d_Y>d_X,  d_C=d_X+d_Y+1,  d=deg T=d_C+1,
    deg s=d_X+d_C,  deg(s+difference)=d_Y+d_C.

Thus `deg(beta v)-deg T` is `d_X+1` for short and `d_Y+1` for long.
The negative source (1) occurs on every short edge with `d_X>=1` and
every long edge. The short edges retaining `X=1` have gap one and are
correctly excluded from this particular witness.

The actual first long edge has `d=3,D=5`, selected character `(8,0)`,
and `J(T,beta v)=-108` there. Its child trace nevertheless has coefficient
`6624>0`, because the diagonal `T_(beta v)` contributes `6732`.
At the short edge from the actual first long child, the analogous selected
values are `-972`, `121500`, and `120528`. These are witnesses of the
sourcewise obstruction and compensation, not a state scan or closure proof.

## 2. The negative witness is always compensated in actual regular children

The same degree-separated minor in fact has a common analytical margin.
No positivity premise on `f` is needed for the following lemma.

**Lemma.** Suppose `v` has positive Fourier interval support, weak folded
TP2, degree `m>=d>=1`, and leading coefficient `A>0`. Let `f` have degree
`d` and leading coefficient `B>0`. Then at

    (a,b)=(d+m+2,m-d)

one has

    T_(f+3y^2 v)[a,b] >= 9A^2-3AB.                    (2)

If `m>d`, the stronger bound `27A^2-3AB` holds.

**Proof.** The exact nonnegative tensor of `beta=3y^2` is

| Character index | Coefficient |
| --- | ---: |
| `(0,0)` | 36 |
| `(1,1)` | 18 |
| `(2,2)` | 27 |
| `(3,1)`, `(1,3)` | 18 each |
| `(4,0)`, `(0,4)` | 9 each |

Folded TP2 of `v` implies `T_v>=_char0`. Also its half-row is decreasing:
write `Delta_i=v_i^2-v_(i-1)v_(i+1)`, with reflection at zero.
The telescoping identity `Delta_i=sum_(j=i)^m delta_j(v)>0` includes
the terminal term `delta_m=A^2`. It gives `v_0>v_1` and decreasing successive
ratios, hence `v_i>=A` throughout the support.

If `m=d`, retain the coefficient `9` of `(4,0)` in `T_beta` and the
terminal coefficient `A^2` of `(2m,0)` in `T_v`. The Clebsch--Gordan
product `chi_4 chi_(2m)` contains `chi_(2m+2)` for every `m>=1`.
This supplies at least `9A^2` at the desired index.

If `m>d`, retain `(2,2)` in `T_beta`. The terminal-strip coefficient
of `T_v` at `(d+m,m-d)`, corresponding to columns `(d,m+1)`, is
`A v_d>=A^2`. The first Clebsch--Gordan product contains the character
of index `d+m+2`; the second contains index `m-d` itself because
`m-d>=1`. This supplies at least `27A^2`.

In both cases `T_(beta v)=T_beta T_v`. Every omitted term is nonnegative.
The desired coefficient of `T_f` is zero, since its column pair is
`(d+1,m+2)`. Equation (1) gives the mixed coefficient `-3AB`.
Adding the three tensors proves (2). QED.

For actual short children with `d_X>=1` and all long children,
the precise leading-coefficient correlations are

    lc(v)=lc(X) lc(T)       (short),
    lc(v)=lc(Y) lc(T)       (long).

They follow from `lc g=lc C`, `lc t=3lc X`, and the degree dominance
of `difference=e(T+1)` on the long side. Canonical positive integral
leading coefficients give `A>=B`. Hence the selected child-trace coefficient
is at least `6A^2>0` at BOTH regular children. Subtracting any scalar
parameter `r` changes only the constant coefficient of `T`; therefore
this conclusion holds for every `T'-r`, in particular the full `[-2,2]` box.

This is a genuine all-state common trace subgate using the origin-certified
cone of `v`. It is not a statement that every character coefficient is
controlled. The negative cross source itself remains negative.

## 3. All adjacent trace defects above the single border are already strict

Put `d=deg T`, `g=beta v`, and `f=T-r`. For all `n>=d+2`, every relevant
Fourier coefficient of `f` is zero, including `f_(n-1)`, so

    delta_n(T'-r)=delta_n(g),       n>=d+2.            (3)

The positive weak cone of `beta` has degree two. For an ordinary origin,
`v` is strict in the raw mode and has degree at least two. The established
strict-times-weak degree lemma therefore makes `g=beta v` strict on its
whole support. Thus every supported index in (3) is strictly positive.
The exceptional retained `X=1` origins use the already proved strict raw
pure-boundary `U_N((2x+3)/2)` result in standard second-kind Chebyshev
notation; the same multiplication argument applies.

At the one border `n=d+1` the exact formula is instead

    delta_(d+1)(T'-r)
      =delta_(d+1)(beta v)-lc(T) (beta v)_(d+2).        (4)

It is independent of `r`. When `m=deg v=d`, the selected coefficient of
Section 2 is exactly this border defect, so (2) proves it strict. Therefore
the border is handled for all children with degree gap two, including
short `d_X=1` and long `d_Y=1`. For larger gaps, the selected nonadjacent
minor of Section 2 does not replace (4).

For the gap-one short edges retaining `X=1`, `m=d-1` and `deg(beta v)=d+1`.
The coefficient `(beta v)_(d+2)` in (4) is zero, so this border is just
the strict terminal defect. It adds no open obligation.

Together with the independent central proof, equations (3)-(4) reduce
the remaining trace defect work to the low overlap indices `1<=n<=d`
and the single border margin (4) when `deg v>d`. No child packet is used
to prove this upper-tail reduction.

## 4. A strict relaxed obstruction to a universal border-margin lemma

Neither strict folded TP2 of `v` and `yv`, nor `lc(v)>=lc(T)`, nor the
parent's full shifted-trace gate alone supplies the margin in (4).
Here is an exact rational counterexample to that proposed relaxed lemma.
Take

    f=(x+4)^2,
    H(v)=(4659,4537,4181,3610,2859,1971,1000)/1000.

The associated power polynomial is

    v=3/200+(1781/500)x+(349/200)x^2-(1249/200)x^3
                    -(3141/1000)x^4+(1971/1000)x^5+x^6.

Both `v` and `yv` have positive Fourier interval support and strictly
positive supported folded defects; their entire finite character arrays
are nonnegative, so every ordered folded minor is nonnegative.
Their raw defects are exactly

    (8411/500000,2899/1000000,2357/100000,401/20000,
                       3273/100000,25841/1000000,1).

Both leading coefficients are `lc f=lc v=1`. For every `|r|<=2`, `f-r`
also has a strict folded-TP2 trace kernel and positive interval support:
its six independent character coefficients are

    (18-r)(19-r)-128, 128-8r, 18-r, 45+r, 8, 1,

bounded below by `(144,112,16,43,8,1)`. Yet

    delta_3(f+3y^2 v)=-29300421/500000<0.

This is the border `d+1=3`. The common multiple `3y^2 v` itself is strict;
its positive defect is smaller than the exact correction in (4).

This counterexample **is not** an `MP_sharp` origin counterexample or a
Fricke-completed canonical state. Its power coefficients are not all
positive, and no ordinary ancestry condition is claimed. It proves only
that the common cone/leading-coefficient information used in Section 2
cannot be extended to a universal border margin. A complete child-trace
proof must use additional quantitative information from the actual
origin packet and/or canonical correlations.

The weak model motivating this exact strict example is also instructive.
For `theta=pi/(2m+2)`, the row `v_i=cos(i theta)` has
`(xv)_i=2cos(theta)v_i` for `0<=i<=m`; hence every interior tensor
coefficient vanishes, while the terminal strip is positive. Multiplication
by `y` or `y^2` only changes this recurrence near the top boundary.
Thus a long interior stretch has zero defects even after `y^2` smoothing.
The rational row above perturbs that situation to strict positive defects
without creating the needed border margin. This explanation is not used
as a numerical proof: the saved example is verified wholly rationally.

## 5. Spectral boundary scope and remaining dependencies

Two-end Robin boundaries do not enlarge the universal radius-two spectral
method. For an `N>=2` path with endpoint diagonal values `eta,rho`,

    2||u||^2-u^T J u
      =(1-eta)u_1^2+(1-rho)u_N^2+sum_(i<N)(u_i-u_(i+1))^2.

The analogous plus identity has `(1+eta),(1+rho)` and squared sums.
Thus `|eta|,|rho|<=1` keeps every eigenvalue in `[-2,2]` and permits the
same positive endpoint-resolvent proof as the established one-end theorem.
At both upper potentials equal one, the constant eigenvector gives the
allowed endpoint eigenvalue two. The spectrum need not be strictly inside.

If a fixed endpoint potential is greater than one, an upper eigenvalue
eventually exceeds two as the stem length grows: using a trial geometric
vector with ratio `1/rho`, its limiting Rayleigh quotient is
`rho+1/rho>2`. A potential below minus one gives the lower analogue.
Already the two-vertex one-end potential two has eigenvalues
`1+-sqrt(2)`, the upper value outside the packet box. An endpoint
resolvent with a genuine pole there cannot be represented by a positive
measure supported on `[-2,2]`; partial fractions are unique. Two-end
Robin reparameterization alone therefore does not repair the unsupported
full `r=2` fixed-trace seed advance. This is a limitation of that spectral
representation, not a counterexample to a canonical child packet.

| Scope | Established here | Still needed |
| --- | --- | --- |
| ROOT | Exact first long/then short witness computations and canonical normalization replay | Root full packet remains the inherited independent certificate |
| BOTH | Strict degree-separated upper-column trace minor; all adjacent trace indices `n>=deg T+2`; border when `deg v<=deg T` | Remaining low trace overlap, larger-gap border, all child `L_r` gates and mixed packets |
| TARGET | No new target implication; all deductions preserve the existing origin/register hypotheses | Regular-edge strict proxy and full new-center paired packet preservation |

`packet_spectral_verify.py` is self-contained exact Fraction arithmetic.
It checks the beta character tensor, both actual compensation witnesses,
the all-shift identity at their selected minors, the upper-tail algebra,
and the complete finite raw/y character certificates of the strict
relaxed counterexample. `packet_spectral_results.json` records the output.
Finite computations are witnesses and algebra checks; the arbitrary-parent
statements in Sections 1-3 are proved analytically above.
