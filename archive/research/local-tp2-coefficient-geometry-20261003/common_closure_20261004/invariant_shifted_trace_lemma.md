# A shared sufficient shifted-trace gate

Status: proved from the stated folded-kernel foundations. This does not
prove preservation of its normalized endpoint hypothesis under summing
a+e, and therefore is not a complete common invariant.

Write A_n=H(a)_n, v=H(y^2 a), t_a=3y^2a+2x+3. Assume a has a positive
integer half-row of degree m>=2, is 1-strong, and ya is folded TP2.
Then every t_a-rho, rho in [-2,2], has strictly positive supported
folded defects and a positive interval half-row.

## Tail strength of y^2 a

The parent multiplier-y lemma in `../mixed_kernel_strong_cone.md`
gives delta_n(H(ya))>=H(ya)_n for n>=1. Put u=H(ya); its full kernel
is TP2 by hypothesis. The same five-minor Cauchy--Binet formula for
multiplication by y proves delta_n(v)>=v_n for n>=2, because every
intermediate adjacent defect used there has index at least 1. The
support-boundary formulas are unchanged: at the penultimate output
index use `delta_(deg u-1)(u)+u_(deg u-1)u_(deg u)`, and at the terminal
index use `u_(deg u)^2`; the integer terminal entry is at least 1.

At n=1 the five-minor formula uses W_u(0,1), W_u(0,2), W_u(0,3),
W_u(1,3), W_u(2,3). The first is nonnegative. The increasing first-two
row ratios and delta_j(u)>=u_j for j>=1 give respectively the lower
bounds u_0,u_0,u_1,u_2 for the remaining four minors. Hence

    delta_1(v)>=2u_0+u_1+u_2=v_1+u_0>=v_1.

These ratio bounds remain valid at a zero terminal column by the
direct identity W_u(i,deg u+1)=u_i u_(deg u). No smoothing-central
strength has been assumed.

## Central margin

Let W_a(i,j) be the first-two-row folded minor. The exact
Cauchy--Binet expansion is

    delta_0(v)=4W_a(0,1)+2W_a(0,2)+3W_a(0,3)
                 +4W_a(1,3)+2W_a(2,3).

For i<j within support, telescoping the first-two-row ratios gives

    W_a(i,j)>=A_i+(j-i-1)A_j.

Indeed the last adjacent defect contributes at least A_i, and every
earlier contribution is at least A_j since A is decreasing. At
j=m+1 use W_a(i,m+1)=A_i A_m>=A_i; the displayed bound remains valid
because A_(m+1)=0. Consequently, for m>=2,

    delta_0(v)>=9A_0+4A_1+4A_2+10A_3.

The last term is zero when m=2. Also

    Q:=8v_1-2v_0-v_2=9A_0+22A_1+9A_2+6A_3-A_4.

For the worst central shift rho=2, direct expansion gives

    delta_0(H(t_a-2))=9delta_0(v)-3Q-7
       >=3(18A_0-10A_1+3A_2+24A_3+A_4)-7
       >=24A_0-7>0.

Increasing the constant 3-rho increases this defect, so the bound
covers the full shift interval. For n=1 the worst constant is 5 and
the exact expansion yields

    delta_1(H(t_a-rho))>=9v_1+12v_1-15v_2+6v_3+4>0.

For n=2 it yields `9delta_2(v)-6v_3>=3v_2>0`; for n>=3 it is
`9delta_n(v)>=9v_n>0`. These formulas include the terminal support.

## Small degrees and exact abstract exception

If a is the positive integer constant A, its trace row is
`(9A+3-rho,6A+2,3A)`. At the worst central shift its defect is
`36A^2-27A-7>=2`; its n=1 defect is at least `9A+4`; the terminal
defect is `9A^2`. Thus all constants A>=1 are covered directly.

For degree one write H(a)=(A,B). If a is optimally B-strong, then
A>=2B. If additionally B>=2, the worst central defect is bounded by
`108B^2-120B-7>=185`. Put c0=3-rho in [1,5]; the remaining defects
are exactly

    delta_1=36AB+72B^2+(24-3c0)A+(54-6c0)B+4,
    delta_2=9A^2+18AB-9B^2-6B,
    delta_3=9B^2.

These are positive using A>=2B and B>=2. The actual degree-one
canonical a is T_1=2x+4, with (A,B)=(4,2). To see that there is no
other degree-one case, the root has (a,e,g)=(0,1,z); its short child
has (a,e)=(0,z+1), its long child has (a,e)=(1,z). Only long mutations
change a. Applying a'=a+e at either of those states gives z+1, while
every subsequent changed e has degree at least two because it is g
or e+g. Short moves may retain the already obtained degree-one a.

The lower-degree qualification matters. The abstract polynomial
a=x+2 has half-row (2,1), is optimally 1-strong, and ya has a folded
TP2 kernel. Nevertheless

    t_a-2=3x^3+12x^2+17x+7,
    H(t_a-2)=(31,26,12,3), delta_0=-19.

This is a counterexample to dropping the degree-one leading-coefficient
qualification. It is not an actual canonical normalized endpoint.
No assertion that it admits no abstract Fricke completion is made.

The zero endpoint a=0 also cannot use shifted factors: t_a-2=2x+1
has negative central folded defect. It is the exact pure-boundary
branch of the common spectral-packet candidate.

## Common-state obligations

The proposed normalized endpoint gate is: a=0; or a is a positive
integer constant; or a has degree one, optimal leading strength and
leading coefficient at least 2; or a has degree at least two, integer
1-strength and ya folded TP2. This is explicit and independent of
Local TP2.

| Obligation | Status |
| --- | --- |
| ROOT | Proved through a=0 boundary clause. |
| SHORT | Proved: a is unchanged. |
| LONG | Open: a becomes a+e; arbitrary positive-sum closure cannot prove the strength and smoothing gate. |
| IMPLIES TARGET | Supplies all shifted fixed-X trace kernels for positive a only; gap packet preservation and the final proxy remain separate obligations. |
