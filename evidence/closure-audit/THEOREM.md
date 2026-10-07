# Closure audit: a canonical obstruction and an automatic channel bound

**Primary status: PROOF_CANDIDATE.** These are explicit counterexamples and
written proofs of scoped structural statements. They do not establish full-tree
Local TP2, do not retract the earlier conditional ray theorems, and do not
constitute external review or a formal proof.

Repository: private `51mns/AIMath`. Baseline:
`0f7bb105a3330ba890528bb60b1f85ef6debcef5`.
Owned path: `research/local-tp2-openai-math-20261007/closure_gate_20261007/`.
The accepted main and every earlier mathematical artifact are unchanged.

## 1. The exact question being tested

The previous campaign proposed making the signed-seed / compound-transport
conditions invariant under both canonical child updates. That is stronger than
showing that one fixed prefix satisfies an all-length extension theorem.
We test this preservation question before enumerating new four- or five-run
examples.

Let `y=x+1`, `p=x+2`, and start from `(1,2x²+6x+5,p)`. The canonical mutation
with retained endpoint X is

    U=3yXC-x(X+C)-Y.

Write `h_F(j)=[q^j]F(q+q^-1)`, reflected at zero and zero outside its degree,
and

    delta_j(F)=h_F(j)^2-h_F(j-1)h_F(j+1)
               -h_F(j+1)^2+h_F(j)h_F(j+2).

For a chosen retained endpoint X at a prefix define

    t=3yX-x, T=tY-xX-C,
    A=(C-Y)/y, B=(T-Y)/y, Q=|B|.

For `r,s∈[-2,2]` the actual midpoint polynomial is

    H_rs=A(t-r)(t-s)+B(t-(r+s)/2).

The previous packages certify mixed-minor compatibility through the sufficient
**max-reference strength condition**, for both `(F,R)=(H_rs,Q)` and
`(F,R)=(yH_rs,yQ)`:

    delta_j(F) >= 8 max_i h_R(i) h_F(j)       for all 0<=j<=deg F.       (G)

This is exactly section 4.1 of `signed_seed_20261007/THEOREM.md` and equation
(4.1) of `compound_transport_20261007/THEOREM.md`. The underlying requirement
is a comparison of kernel minors, not (G) itself. In particular (G) must not
be mistaken for a necessary condition for Local TP2.

## 2. A one-step canonical counterexample to preserving (G)

On the right ray the fixed endpoint is X=p and

    t=3x²+8x+6, A_0=2p, B_0=0.

One forward step changes the signed seeds by

    (A,B) -> (tA+B,-A).

At the prefix R, continuing right, therefore

    A_1=2pt, B_1=-2p, Q_1=2p.

Take distinct spectral parameters `r=-2,s=2`. Then

    H_1=2p[t(t²-4)-t]=2pt(t²-5),
    F_1=yH_1, R_1=2yp.

The polynomial F_1 has degree 8 and leading coefficient 54. The half-row of
R_1 is `(8,6,2)`. At the terminal index, zero extension makes

    delta_8(F_1)=54²=2916,
    8 max h_(R_1) h_(F_1)(8)=8·8·54=3456.

Consequently

    delta_8(F_1)-8 max h_(R_1) h_(F_1)(8) = -540.                    (2.1)

This is an exact negative integer at genuine canonical data, not a negative
Bernstein control coefficient for an otherwise positive polynomial. The
leading coefficient does not depend on r,s, so the same terminal failure
occurs throughout the entire spectral square.

At the preceding root, right continuation passes every qualitative and
quantitative certificate of the compound-transport package. Its author and
Laurent-verifier implementations independently reconstruct the same 716
certificate entries. Replaying the same predicate after the single R step
fails exactly `midpoint_y_strength`; the verifier rejects with margin -540.
Thus the actual sufficient predicate used by that package is not invariant
under even this one forward step. Changing its positive channel weights or
its growth rate cannot repair this particular failure: neither appears in (G).

### What has not failed

The original Local TP2 determinants at the root and at R are positive.
At the displayed terminal index the reference first-row minor is zero,
because the reference has degree 2. The actual required polarized first-row
minor is instead

    2 delta_8(F_1) - ((r-s)²/2) delta_8(R_1) = 5832 > 0.

So (2.1) does not refute mixed-minor compatibility, a previous ray theorem,
or Local TP2. It refutes the proposal to propagate the *unchanged sufficient
predicate* from parent to child. A ray theorem proved at its initial prefix
need not be recertified at every later prefix; its conclusion remains valid.

## 3. The terminal failure is structural, at every R^n, n>=1

Define monic second-kind polynomials by

    u_-1(z)=0, u_0(z)=1, u_(n+1)(z)=z u_n(z)-u_(n-1)(z).

The exact signed seeds at R^n, with right continuation, are

    A_n=2p u_n(t), B_n=-2p u_(n-1)(t), Q_n=2p u_(n-1)(t).          (3.1)

This follows by induction from the signed update, not from finite sampling.
For any fixed r,s the midpoint has degree `2n+5` and leading coefficient
`18·3^n`; multiplying it by y preserves that leading coefficient. Thus, for
`F_n=yH_rs`,

    deg F_n=2n+6, h_(F_n)(deg F_n)=54·3^(n-1).                    (3.2)

All coefficient comparisons in the following paragraph are ordinary x
coefficient comparisons. Because t-2 is nonnegative, induction gives
`u_j(t)>=u_(j-1)(t)>=0`: the increment is

    u_(j+1)-u_j=(t-2)u_j+(u_j-u_(j-1)).

Consequently

    u_(j+1)=(t-1)u_j+(u_j-u_(j-1)) >= (t-1)u_j,
    u_j(t)>=(t-1)^j>=5^j.

Here the final comparison uses the constant coefficient 5 of t-1, and all
remaining coefficients are nonnegative. Since `h_(2yp)(0)=8`, (3.1) gives

    max h_(yQ_n) >= h_(yQ_n)(0) >= 8·5^(n-1).

At the terminal index,

    delta(F_n)/(max h_(yQ_n) h_(F_n))
       = h_(F_n)(deg F_n)/max h_(yQ_n)
       <= (27/4)(3/5)^(n-1) < 8.                               (3.3)

Therefore (G) fails at **every** R^n, n>=1, for all spectral parameters.
Moreover the right side of (3.3) tends to zero: replacing 8 by *any fixed
positive constant* still cannot yield an all-state, all-support invariant.
This is an infinite-family proof from the exact recurrence and leading term.
It does not require an asymptotic estimate of any Fourier coefficient.

The raw version fails from n=2 onwards. At n=2 its leading coefficient is
162, Q_2 has half-row `(80,62,28,6)`, and its terminal margin is

    162²-8·80·162=-77436.

For larger n use `Q_n >= 5^(n-2)Q_2` and the leading coefficient
`162·3^(n-2)` to obtain the same conclusion.

## 4. Dropping only the terminal indices does not solve the issue

A support-aware estimate could avoid charging a zero reference minor at
j>deg Q. That is a legitimate possibility, but preserving the unchanged
max-reference bound on the remaining band still fails.

For the distinct parameters r=-2,s=2 at R^56, with **raw** H and Q, the first
coefficient index j=0 satisfies

    delta_0(H)/(8 max h_Q · h_H(0))
      = 0.9739282167643731... < 1.

The exact rational and the exact negative integer difference are in the
regenerated witness JSON. Here `deg H=117`, `deg Q=111`: the failure occurs
inside the reference support, not at its edge. Both independent arithmetic
implementations reconstruct the full rows and the same difference. The actual
polarized first-row minor `2delta_0(H)-8delta_0(Q)` is positive, and all 117
required original Local TP2 determinants at R^56 are positive.
The decimal is only for readability; all decisions use exact integers.

### A central-index no-go for every fixed positive constant

There is also a direct analytic reason this happens. Keep r=-2,s=2. As n
increases,

    delta_0(H_n)/(h_(Q_n)(0) h_(H_n)(0)) -> 0.                    (4.1)

In particular, any fixed positive max-reference budget also eventually fails
at j=0, since `max h_Q>=h_Q(0)`. This rules out repairing (G) merely by cutting
its support and decreasing its constant.

Here is a proof of (4.1) that requires no central-limit approximation. Put
`x=2cos(theta)`, theta in [-pi,pi]. Then

    t(theta)=3x²+8x+6 ∈ [2/3,34].

Its unique maximum 34 is at theta=0. For t>2 put

    lambda(t)=(t+sqrt(t²-4))/2,
    lambda_0=lambda(34)=17+12sqrt(2).

The elementary solution of the second-order recurrence is

    u_j(t)=(lambda^(j+1)-lambda^(-j-1))/(lambda-lambda^-1)
          =sum_(a=0)^j lambda^(j-2a).                           (4.2)

For 0<=t<=2 use complex conjugate roots of modulus one; the same finite sum
has absolute value at most j+1. Hence on all of [2/3,34],

    |u_j(t)| <= (j+1) max(1,lambda(t)^j),

with lambda interpreted as 1 on [2/3,2]. On every closed set |theta|>=d>0,
this is bounded by `(j+1)rho_d^j` for a `rho_d<lambda_0`.

The Fourier integral for Q_n has integrand `2p(theta)u_(n-1)(t(theta))`.
On a sufficiently small neighborhood of zero it is positive. Its integral
on a smaller fixed interval is at least `c L^(n-1)` for some L>rho_d:
choose that interval so t>2 and lambda(t)>L, use (4.2) and p(0)=4.
The absolute integral outside |theta|<d is exponentially smaller. Thus the
normalized integral concentrates at theta=0. More explicitly, for any fixed
continuous multiplier phi, splitting at d and then sending d to zero gives

    integral 2p u_(n-1)(t) phi(theta)
      / integral 2p u_(n-1)(t) -> phi(0).                       (4.3)

This argument does not assume the integrand is positive everywhere: possible
oscillations outside the neighborhood are controlled by the absolute
exponential bound.

Now

    H_n=2p[(t²-4)u_n(t)-t u_(n-1)(t)].

Uniformly on a fixed small neighborhood of zero, (4.2) gives
`u_n/u_(n-1)->lambda(t)`. The same exponential bounds control the remaining
part of the H integral. Applying (4.3) with the continuous local multiplier
and with cos(j theta) proves, for each fixed j,

    h_(H_n)(j)/h_(Q_n)(0) -> L_0,
    L_0=(34²-4)lambda_0-34 > 0.                                (4.4)

The rows in question have positive constant coefficients. Indeed
`H_n=2p[u_(n+2)-3u_n]`, and the coefficient bound in section 3 gives
`u_(n+2)>=(t-1)²u_n>=25u_n`. Substituting j=0,1,2 in (4.4), the three terms
of the central defect, normalized by h_Q(0)², have limit

    L_0²-2L_0²+L_0²=0.

The normalized denominator has positive limit L_0, proving (4.1). The same
argument works after multiplying both H and Q by y, whose value at theta=0
is 3; outside the dominant neighborhood its possible sign is again harmless.
This proof establishes the limit; finite witness calculations are not its
justification.

## 5. A useful positive reduction: channel weights are not the remaining bottleneck

The preceding obstruction involves the reference bound, not the positive
channel weights. In fact the channel condition can be supplied uniformly once
the qualitative trace-cone condition has been established.

### 5.1 General column-sum lemma

Let h=(h_0,...,h_D) be positive on its support, reflected and zero-extended,
with all delta_j>=0. Let K_h be the folded multiplication kernel from the
baseline theorem, and take channels `(i,i+1)`, i=0,...,e, with **e>=D**.
Define

    M(i,j)=det K_h[(i,i+1),(j,j+1)].

Then each column satisfies

    sum_(i=0)^e M(i,j) >= Delta_0=h_0²-h_1²,   0<=j<=e.          (5.1)

Proof: for i,j>0, the established folded interior identity and monotonicity
of `(h_(a-1)+h_(a+1))/h_a` give

    M(i,j)>=sum_(r=|i-j|)^(min(i+j,D)) delta_r.

The support-boundary formula gives the same inequality when i+j>=D; if
|i-j|>D the sum is empty. At i=0, M(0,j)=delta_j; at j=0,i>0,
M(i,0)=2delta_i. For fixed j>0 and any r<=D, the choice i=|j-r| lies in
[0,e]. If i=0 the boundary cell contains delta_r; otherwise its displayed
interval contains r. Thus every nonnegative delta_r is counted at least once
in the column sum. For j=0 the assertion follows directly. Finally
`sum_r delta_r=Delta_0`. QED.

This is a lower bound from the true infinite kernel, not a truncation equality.
The bandwidth hypothesis matters: h=(3,2,1), e=0 gives a column sum of 4,
whereas Delta_0=5.

For D>=1, cone membership implies h_0>=h_1>=... and

    mass(h)<=h_0+2D h_1<=(D+1/2)(h_0+h_1).

It follows that

    Delta_0 >= [2(h_0-h_1)/(2D+1)] mass(h).                      (5.2)

### 5.2 A global low-character bound for canonical centers

Use the already proved character basis
`B_j(q)=sum_(i=-j)^j q^i`, with coefficients alpha_G(j)=h_G(j)-h_G(j+1).
The baseline `resumed_extension_kernel_support.md` establishes, on the entire
canonical tree, dense positive character coefficients, center dominance over
both endpoints, and `alpha_C(1)>=alpha_C(0)>=3`.

The following quantitative sharpening follows from that proof:

    alpha_C(0)>=deg C+1, alpha_C(1)>=deg C+1                     (5.3)

for every canonical center. At the root the constant character coefficient
is 3 and degree is 2. For a mutation write `R=3XC-X-C`, so
`U=yR+X+C-Y`. The character-positive factorization

    R=(2C-1)+(X-1)(3C-1)>=_B2C-1

gives alpha_R(1)>=2alpha_C(1). Therefore

    alpha_U(0)>=2alpha_C(1)+alpha_X(0)+alpha_C(0)-alpha_Y(0)
                >=2alpha_C(0)+1.

If deg C=c, the new degree is deg X+c+1<=2c, since deg X<c. This proves
(5.3) by induction; the previously established inequality alpha_U(1)>=alpha_U(0)
provides the second half. This sharpening uses no unproved folded-cone claim.

### 5.3 Uniform trace-channel condition

Let X be any nonconstant canonical polynomial, let a=deg X, and set
`f_r=3yX-x-r`, r in [-2,2]. **Assume f_r is in the folded cone**, as is
already a qualitative premise of the ray methods. Use e>=deg f_r+1 channels
and the common row of weights w=(1,...,1). Then

    w M_(f_r) >= 2 mass(f_r) w.                                 (5.4)

For a>=2, X was a center and (5.3) applies. Its shifted trace has degree
D=a+1 and constant character coefficient

    h_f(0)-h_f(1)=3alpha_X(1)+1-r>=3a+2.

Equations (5.1)--(5.2) give a multiplier at least
`2(3a+2)/(2a+3)>2`, proving (5.4).

The only nonconstant boundary exception is X=p, whose half-row is
`(z,8,3)`, z=12-r in [10,14]. For all e>=3 its column sums have just five
forms, omitting the middle range when it is empty:

    j=0:       z²-3z,
    j=1:       z²-3z+64,
    2<=j<=e-2: z²-6z+82,
    j=e-1:     z²-6z+73,
    j=e:       z²-3z+9.

Each exceeds `2(z+22)=2mass(f_r)` on [10,14]. Exact quadratic Bernstein
coefficients of these five margins are included in the verification.
For X=1 the shifted trace need not be cone; that boundary is excluded.

Thus searching for node-specific channel weights is unnecessary in this
setting. Establishing the qualitative trace cone is still an open global
obligation, and (5.4) does not replace it. Nor does it repair the failed
reference-strength premise in sections 2--4.

## 6. Reproduction and review scope

`author.py` evaluates ordinary integer x polynomials and uses the binomial
coefficient transform. `verifier.py` constructs the full symmetric Laurent
polynomials directly and uses a different polarization calculation. They
import neither each other's algorithms nor expected outputs. Their complete
results, including all original target minors at the three displayed states,
match byte for byte after deterministic serialization.

`reproduce.py` also replays the pinned previous author/verifier at the root,
then requires rejection after one right step. The old files are used unchanged;
their Git blob hashes are checked. A direct expected rejection is evidence for
the obstruction, not a test failure being hidden as a successful proof.
The general column bound has finite regression tests and negative controls for
too few channels and reversed row/column orientation. Its infinite scope rests
on section 5's proof. The infinitely many failures in sections 3 and 4 likewise
rest on their written arguments.

All new results remain lane-local PROOF_CANDIDATE. Different arithmetic
implementations by the same model are not a fresh mathematical reviewer,
external peer review, or formal verification. No novelty or full-tree result
is claimed.

## 7. Decision

**HOLD the unchanged max-reference-strength preservation route.** It is
refuted on canonical data and cannot be repaired merely by a smaller fixed
constant, a support cutoff, more channel weights, or a larger finite scan.

The conditional extension results remain useful at prefixes satisfying their
hypotheses, and the transport lemmas remain valid. A genuinely different
continuation would need a reference-sensitive comparison retaining both
kernels' shapes, or a direct recurrence for the original two-gap determinant.
Neither is supplied as a completed all-tree proof here. No further sufficient
condition is introduced just to keep the previous preservation campaign running.
