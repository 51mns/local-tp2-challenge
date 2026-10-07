# Canonical quotient networks: a sharp ratio interval and polynomial barriers

Status: all-depth coefficientwise constraints proved. **These are not a proof
of Local TP2.** They use the positive quotient coordinates developed in the
parallel invariants investigation, and identify additional compatibility of
the actual canonical incoming gaps. The orders below are ordinary polynomial
coefficient orders, not Fourier likelihood-ratio orders.

Let y=x+1 and orient endpoints by degree, X<Y, with center C. Put

    a=(X-1)/y, e=(Y-X)/y, g=(C-Y)/y,
    t=2x+3+3y²a, T=t-2, k=(1+ya)(1+3ya),
    r=g-Te-k.

The normalized root is (a,e,r)=(0,1,1), with g=2x+3. The two
canonical child operations, keeping the smaller endpoint or the larger
endpoint, respectively, are exactly

    short: (a,e,r) -> (a, e+g, g),
    long:  (a,e,r) -> (a+e, g, e+g),
    g=Te+k+r.                                      (1)

On a long step, t,T,k are recomputed at a+e. These equations hold as
polynomial identities before imposing the Fricke relation. In particular,
all a,e,r,g have nonnegative ordinary coefficients; e,r,g are nonzero.
The words short/long name the degree-oriented child choice at each node,
not the fixed Farey L/R letters.

One way to verify (1) is to use the normalized short outgoing gap
s=(t-1)g+(t-2)e+k and multiplier M=t+1+3y²(e+g). Then

    s-(t-2)(e+g)-k=g,
    (s+eM)-(t(a+e)-2)g-k(a+e)=e+g,

where

    k(a+e)-k(a)=4ye+6y²ae+3y²e².

## 1. Sharp universal coefficientwise scalar bounds

Let c=(sqrt(5)-1)/2 and phi=1+c. At every canonical node,

    c e <= r <= phi e                               (2)

coefficientwise over the real numbers. Thus, for example, the completely
rational consequences 3e<=5r and 3r<=5e hold at every depth.

Proof: T has constant coefficient at least 1 and all other coefficients
nonnegative. If r>=ce, then

    g=Te+k+r >= (1+c)e.

For a short step,

    r'-ce'=(1-c)g-ce >= ((1-c)(1+c)-c)e=0,

using c²+c=1. The short upper bound follows from r'=g<=e'=e+g.
For a long step, r'=e+g>=g=e', and

    phi e'-r'=c g-e >= (c(1+c)-1)e=0.

The root has r=e. This proves both bounds simultaneously by induction.

Both constants are optimal among uniform scalar coefficient bounds.
Along the pure short sequence, evaluation at x=0 gives

    e_n=F_(2n+3)-1, r_n=F_(2n+2),

with F_0=0,F_1=1. This follows by setting E=e+1: the constant-term
recurrence is (E,r)->(2E+r,E+r). Consequently r_n/e_n tends to c.
Making one long step after these nodes gives r'/e'=(e+g)/g tending
to phi. A stronger uniform scalar lower or upper coefficient bound
would in particular fail for these constant coefficients.

## 2. Infinite polynomial barriers with positive certificates

Define polynomials in a separate variable z by

    P_0(z)=0, Q_0(z)=1,
    P_m=z Q_(m-1)+P_(m-1),
    Q_m=(z+1)Q_(m-1)+P_(m-1),       m>=1.            (3)

They have nonnegative integer coefficients and

    Q_m-P_m=Q_(m-1),
    z Q_m(Q_m-P_m)-P_m²=z.                          (4)

Equivalently, writing u_j=U_j((z+2)/2), u_(-1)=0,

    P_m=z u_(m-1), Q_m=u_m-u_(m-1).

The second expression alone does not establish ordinary positivity;
the subtraction-free recurrence (3) does.

At every canonical node and for every integer m>=0,

    D_m = Q_m(T)r-P_m(T)e >= 0                     (5)

coefficientwise. This is an infinite family of genuine constraints on
the coupled canonical pair. For example,

    (T+1)r-Te >=0,
    (T²+3T+1)r-(T²+2T)e >=0.

Proof: for m>=1, the short map has the exact identity

    D_m' = D_(m-1)+Q_(m-1)(T) k.                   (6)

It follows immediately by substituting r'=g, e'=e+g, g=Te+k+r and
using (3)-(4). For m=0, D_0'=g>=0. For a long map, with T' recomputed,

    D_m' = Q_m(T')e + (Q_m(T')-P_m(T'))g >=0.       (7)

At the root D_m=Q_m(T)-P_m(T)>=0. Induction on tree depth proves
(5) simultaneously for all m: the inductive hypothesis contains all
indices, so (6) introduces no unproved infinite tail. No division by a
polynomial or cancellation of a positive multiplier is involved.

More explicitly, along ell short moves after an entry node, with m>=ell,

    D_m(final)=D_(m-ell)(entry)
               +k sum_(j=m-ell)^(m-1) Q_j(T).      (8)

At the root, or immediately after a long move, r>=e coefficientwise.
Thus the remaining entry term is visibly positive:

    D_j(entry)=(Q_j-P_j)e+Q_j(r-e).

If m<ell, iterate (6) only m times and finish at D_0=r>=0. This gives
an explicit positive network decomposition for every barrier (5).

## 3. Separation of consecutive incoming gaps

The positive quotient recurrence also preserves

    b=a+e-r >=0.

Indeed b=0 at the root; the short child has b'=a+e, and the long
child has b'=a. Since

    k-Ta=1+(2x+3)a,

we get the exact positive identity

    h:=g-(t-1)r=T b+1+(2x+3)a >=0.                 (9)

In particular (t-1)r<=g coefficientwise. This is stronger information
than the universal scalar interval when comparing the two consecutive
incoming gaps r,g.

Along a fixed-endpoint ray let q_(-1)=r,q_0=g and
q_(j+1)=t q_j-q_(j-1). For j>=0, with u_j=U_j(t/2), u_(-1)=0,

    q_j=g u_j-r u_(j-1)
       =r (u_(j+1)-u_j)+h u_j.                    (10)

This is an exact positive decomposition in the two Chebyshev families
u_j and u_(j+1)-u_j, each of which has nonnegative ordinary coefficients
as a polynomial in T=t-2 (the latter equals Q_(j+1) above). The
identity has no division by t-1. Its Fourier meaning still requires
care: h need not belong to the folded cone. At the first short node,
a=0,b=1, so h=2x+2, whose half-row (2,2) has central defect -4.

## 4. The natural two-step block still has a folded obstruction

The positive pair (r,h), with h as in (9), evolves along the same ray by

    (r,h)^T -> N (r,h)^T,
    N=[[t-1,1],[t-2,1]].

Its exact two-step transfer is

    N²=[[t²-t-1,t],[t(t-2),t-1]].

At the canonical root t=2x+3, the lower-right entry is t-1=2x+2.
Its Fourier half-row is (2,2), and its central folded defect is -4.
Thus this natural two-step block cannot be justified by a claim that
all scalar entries have folded-TP2 multiplication kernels.

Likewise the independent extreme-root pair (t-2)(t+2) is not such a
kernel at the root: it equals 4x²+12x+5, has half-row (13,12,4), and
central defect -67. These are obstructions to the specified entrywise
block arguments, not to all possible grouped or coupled-network proofs,
and not counterexamples to Local TP2.

## 5. Scope for Local TP2

The original actual child pair is

    S=y s, D=y eM,
    s=tg-r,
    M=t+1+3y²(e+g).

Equations (1)-(8) retain canonical ancestry and provide constraints
absent from unrelated positive coefficient triples. Nevertheless they
are linear coefficient comparisons. They do not imply the required
quadratic inequalities

    H(S)_n H(D)_(n+1)-H(S)_(n+1)H(D)_n>0.

In particular one cannot cancel Q_m(T), infer Fourier LR from the scalar
interval (2), or treat each network edge T as a folded-TP2 factor. A
complete proof still needs a signed coefficient cancellation or a
quantitative quadratic estimate using the coupled constraints.

`network_quotient_constraints.py` checks the two child identities directly
against scalar mutation as multivariate identities, the universal barrier
transport algebra, the continuant identities (4), the exact Fibonacci
constant-term formula, and small canonical instances only as implementation
checks. The all-depth and all-m statements follow from the proofs above.
