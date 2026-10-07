# The central shifted-trace gate is preserved at BOTH children

**Status: proved common regular-state subgate, not full packet closure.**
Assume the existing parent sharp packets and certified origin registers.
Then, for either exact mutation and EVERY r in [-2,2], the child shifted
trace T'-r has a positive Fourier interval row and a strictly positive
central folded defect. No child packet or child proxy is assumed.
Noncentral trace defects, full child single blocks, and mixed packets
remain separate obligations.

## 1. The central cone is closed under addition

For a nonnegative Fourier triple a=(a0,a1,a2), put

    D(a)=a0(a0+a2)-2a1².

Its polarization is

    B(a,b)=2a0b0+a0b2+a2b0-4a1b1.

If D(a),D(b)>=0, then

    2a0b0+a0b2+a2b0
      >=2 sqrt[a0(a0+a2)b0(b0+b2)] >=4a1b1.

The first inequality follows from
`[a0(b0+b2)+b0(a0+a2)]²-4a0(a0+a2)b0(b0+b2)
 =(a0b2-a2b0)²`.
Hence B(a,b)>=0 and D(a+b)>=D(a)+D(b). This includes zero
coordinates, requires no division, and does not assert addition closure
of the full folded TP2 cone.

## 2. The retained origins supply the added block

The exact child center obeys

    C'=C+y v, T'=T+beta v, beta=3y²,
    v=s (short), v=s+d (long).

For the ordinary origins these v are certified q_N with N>=1, so they
have positive Fourier interval support and strict supported folded
defects by the sharp origin theorem. In the short case N_X>=2 and
deg v>=2. In the long case the larger endpoint is nonconstant, its trace
has degree at least two, and N_Y>=1; hence deg v>=2 there too.

The endpoint-1 smaller origin has v=U_N((2x+3)/2), N>=2. Its RAW strict
folded TP2 property is the all-N shifted-U theorem in
`../continuation_independent_audit.md`, not an inference from the new
child packet or from multiplying a smoothed polynomial by y.

The half-row of y² is (3,2,1), with defects (4,0,1), so it is a weak
folded cone factor of degree two. The previously audited strict-times-
weak product lemma applies because deg v>=2. It follows that beta v
has positive interval support and strictly positive supported defects.

## 3. Both-child theorem

For each r in [-2,2], the parent packet supplies the positive interval
row of A=T-r and D(A)>=0. The added polynomial B=beta v is independent
of r and has D(B)>0. Section 1 therefore gives

    delta_0(T'-r) >= delta_0(T-r)+delta_0(beta v)>0.

The sum of the two positive interval rows is positive on their union,
which is the full initial interval through deg T'. This proves the
stated continuum and BOTH-child gate from the EXISTING common predicate.

This central argument must not be applied to other ordered minors.
Indeed the spectral lane gives actual degree-separated negative mixed
sources at noncentral column pairs; those do not contradict this theorem.

## 4. An optional quantitative history invariant

There is also a stronger central statement along any certified mutation
history. It is useful for future estimates, but is not needed in Section 3.
Write w=H(yC), w*=H(yCroot)=(21,17,8,2), and u=w-w*.
Initially u=0. Each update adds H(y²v), a nonnegative interval row in the
central cone. Section 1 proves inductively that u is nonnegative and
D(u)>=0, provided each step has the certified origins used in Section 2.
This is an explicit ROOT/BOTH auxiliary invariant, not a statement that
one arbitrary parent packet implies the translated condition.

At shift r=2 the child/current trace triple is
`(61,50,24)+3(u0,u1,u2)`, so

    delta_0(T-2)=185+9D(u)+L(u),
    L(u)=438u0-600u1+183u2.

The exact rational identity

    61u0 L(u)=6(61u1-50u0)²+555u0²+11163D(u)

gives L(u)>=(555/61)u0 when u0>0. If u0=0, the central cone forces
u1=0 and L(u)=183u2>=0. Thus delta_0(T-2)>=185.
For any r<=2 the exact difference is

    delta_0(T-r)-delta_0(T-2)
      =(2-r)[6w0+3w2-(r+2)] >=0,

since w0>=21 and w2>=8. Hence the uniform bound 185 holds on the
entire shift interval along these certified histories. It does not by
itself certify arbitrary histories: the other regular packet gates are
still needed to continue the origin certificates.

## 5. Scope and replay

ROOT trace central strictness was already included in the previous full
base certificates. The new result is arbitrary-parent BOTH preservation
of this component, plus the optional quantitative history invariant.
TARGET does not follow from central trace positivity alone.
Full-tree strict Local TP2 remains OPEN.

`root_central_trace_verify.py` checks the displayed polynomial identities,
the y² defects, and the root constants using exact symbolic/rational Python.
Its finite identities validate the algebra; Sections 1–4 carry the universal
parameter and ancestry arguments.
