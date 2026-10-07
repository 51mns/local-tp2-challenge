# Independent audit of the all-index character certificate

**Verdict: PASS.** This is a proof audit of
`network_relative_character.md`, not a finite-minor extrapolation.
The theorem concerns determinants; packet support, nonnegative entries,
strict single blocks and trace gates must still be supplied separately.

## Row normalization and selector

Let C0=1 and C_i(q+q^-1)=q^i+q^-i for i>0. Multiplication gives exactly
row i of K_f. In particular H(C_i f)_0=2h_i, while row0 is h itself.
C1=x, so row1 is H(xf), with (xh)_0=2h1. At columns k<l its determinant
is W_(k,l)(h,xh). The character selector at k=0 is chi_(l-1)(U)
chi_(l-1)(V), with **no extra factor2**. The factor2 is already in row1.

Elementary independent checks are R(1,x)=1; R(1,C2)=UV=chi1(U)chi1(V);
and R(C1,C2)=Phi(ξζ+2)=chi2(U)+chi2(V). These match their coordinate
unit Fourier rows and verify the central/offcentral conventions.

## All character coefficients and arbitrary kernel indices

T_f=Phi(f(ξ)f(ζ))=R(f,xf). Its expansion is symmetric under U,V exchange
and has equal parity in the two character indices: Phi(ξ+ζ)=UV and
Phi(ξζ)=U²+V²-4 already have these properties. Character basis parity
preserves them. For every potentially nonzero coefficient with a>=b,

    k=(a-b)/2, l=(a+b+2)/2

are integers with 0<=k<l. The opposite ordering a<b is the symmetric
duplicate; unequal parity vanishes. Thus rows(0,1) and all columns really
select every coefficient of T_f-gamma T_b.

For arbitrary rows i<j, the multiplier R(C_i,C_j) has one positive
character when i=0 and two positive characters otherwise. The Bezoutian
product identity gives

    det K_f[{i,j},{k,l}]
      =Sel_(k,l)[T_f R(C_i,C_j)].

Clebsch--Gordan character multiplication has nonnegative integer
coefficients. Therefore character positivity of the relative tensor
implies every ordered relative minor at every kernel index. Conversely
the rows(0,1) conditions give the entire relative tensor. This proves
the claimed equivalence without assuming cone membership of the
reference row or any finite kernel cutoff.

If deg f=D and deg b<=D, all nonzero rows(0,1) comparisons have column
indices at most D+1: h ends at D and xh at D+1. Larger pairs give zero.
Consequently the actual search's complete row(0,1) arrays also have an
ALL-index interpretation under this theorem. Independently, each tested
fixed case has an all-index strength certificate, so the search does not
depend solely on adopting this new reduction.

## Mixed and sharp midpoint statement

For F=H+delta*b1,G=H-delta*b1, direct polarization yields

    J(F,G)=2(T_H-delta²*T_b1), delta=(r-s)/2.

The preceding all-index equivalence therefore makes the exact mixed
gate identical to character positivity of this tensor. The coefficient
is (r-s)²/4, not uniform4. The independent y version replaces H,b1 by
yH,yb1 throughout. No preservation of the cone by y is used.

The sign statement for a signed seed means a GLOBAL sign, as in the
permitted one-sign packet seeds: T_(-b1)=T_b1. It must not be read as
replacing an arbitrary mixed-sign polynomial by its coefficientwise
absolute value. Actual paired seeds in this round are positive.

Finally T_(pf)-gamma T_(pb)=T_p(T_f-gamma T_b) is a valid common-product
transport when p is a cone polynomial. The reference must also be
multiplied by p. This does not supply a changed-reference packet bound
or new-center closure.

The finite-character-to-all-index theorem is sound and can support the
quantitative lane's exact tensor/Bernstein parameter certificates. It
does not prove that those parameter arrays are nonnegative, nor that
the remaining packet or proxy components preserve both children.

## Audited final version

Final note SHA256:
`0ed6f97744bb78e810438285c6cd7e1520197940b6e5c57881c9692f29fa617d`.
The final clarification says `|b1|=+b1` or `-b1` for one-sign seeds,
which matches this audit's scope. The implementation was also updated to
cast midpoint parameters to exact `Fraction`; final code SHA256:
`2ebde5fb0daa501c716072689b58509d769c4a6b4fe7f55d90aae331f236e72d`.
