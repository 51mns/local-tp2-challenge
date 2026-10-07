# Independent spectral audit of sparse single-block strictness

**PASS: strict L_0 alone retains every core origin/register consumer
used by the current common predicate.** Optional strict L_-1 retains
the smallest-prefix and short reverse-anchor subgates. The proof recovers strictness of
the complete resolvent sum at every supported index. It does not require
each spectral residue polynomial to be strict at every index.

This replaces one genuinely stronger premise: full-continuum strictness
of L_r and yL_r. It does not prove weak single-block child preservation,
the child trace gate, mixed child preservation, or either proxy. All older
directories are frozen; this independent audit is based on the stated
packet and the already proved canonical register identities.

## 1. Precisely the packet audited

Let d=deg T>=1, p=deg b0>=0, and deg b1<p+d. Retain positive Fourier
interval support and weak folded TP2 of T-r for every r in [-2,2].
Retain the full sharp mixed gate

    J(L_r(T-s),L_s(T-r))>=_char0

and its separately smoothed counterpart, for all r,s in [-2,2].
Require L_r=b0(T-r)+b1 and yL_r to have positive interval support and
weak folded TP2 for every r in the closed parameter interval. The core
packet requires strict supported defects only for L_0,yL_0. The optional
stronger packet also requires strict L_-1,yL_-1.

Write MP_0 for the core packet and MP_01 for the optional stronger packet.
They are the W_0 and W_01 conditions in `audit_packet_weakening.md`.
MP_sharp implies both immediately.
No cone premise is imposed on b0, b1, or their y multiples. Under MP_0,
arbitrary H_rs need only be weak; this proof never silently asserts that
all H_rs are strict merely because the old strict packet supplied that.

## 2. A fixed defect has at most one interior bad parameter

At any fixed base index k, delta_k(L_r) is a real polynomial of degree
at most two in r. The same is true of delta_k(yL_r). Each is nonnegative
on [-2,2] and strictly positive at zero.

If such a polynomial has an interior zero, nonnegativity on both sides
forces even multiplicity. A nonzero polynomial of degree at most two
can therefore have at most one distinct interior zero. The strict value
at zero rules out the identically zero polynomial. Endpoint zeros can
occur at both ends and do not contradict this argument; the spectral
poles used below lie strictly inside the interval.

Consequently, at any supported k, among any two distinct parameters
in (-2,2) at least one base defect is strictly positive. The good parameter
may depend on k. A single parameter good for every index is unnecessary.

## 3. The backwards Cauchy--Binet index is independent of the residue

Let B be a positive-interval weak trace factor of degree d. Its ordinary
Toeplitz differences satisfy

    Delta_j(B)=sum_(ell=j)^d delta_ell(B)>0, 0<=j<=d,

because the terminal term is the positive square of its leading Fourier
coefficient. This requires no strict folded defect of B itself.

Suppose a current weak factor A has degree f>=d. To retain an adjacent
Cauchy--Binet term for output n, choose intermediate columns

    i=max(d,min(n,f)), i+1.

The first minor is delta_i(A). For n>=1, the reflected sum-index terms
of the trace factor vanish since i+n>=d+1. The second minor is exactly
Delta_|i-n|(B)>0, and |i-n|<=d for every output 0<=n<=f+d.
For n=0, i=d and the second minor is exactly 2(lc B)^2>0, including
the folded central-column factor two.

This gives a lower bound even when delta_i(A)=0. If that chosen defect
is positive, the output defect is positive, as all omitted terms are
nonnegative. Iterating backwards through M factors of the same degree d
ends at a base index k0 determined solely by the output n, the common
base degree and M. It does not depend on the numerical roots, their
ordering, or which residue index is omitted from the product.

Thus among two or more distinct spectral residues, Section 2 supplies
at least one with delta_k0(base)>0, and the same backwards index chain
supplies a strictly positive diagonal contribution at the chosen output.
This works independently at every output, including zero and terminal.

## 4. Robin origin theorem retained with its exact scope

For |rho|<=1, the one-end Robin path J_N(rho) has characteristic

    p_N=U_N(T/2)-rho U_(N-1)(T/2)

in standard second-kind notation. For N>=2, its spectrum is simple,
all first-coordinate residues are positive, and every eigenvalue is
strictly inside (-2,2). The strict spectral bound follows from

    2||u||^2-u^T J_N(rho)u
      =u_1^2+(1-rho)u_N^2+sum_(i<N)(u_i-u_(i+1))^2,

and its plus analogue with 1+rho and squared sums. A zero quadratic
form would force u_1=0 and then every coordinate zero. Nonzero unit
off-diagonals give simple eigenvalues and nonzero first components.

The usual positive resolvent decomposition is therefore

    q_N-rho q_(N-1)=sum_i w_i L_(lambda_i)
                              prod_(j!=i)(T-lambda_j).

Every residue polynomial is a weak cone with positive support of the
same fixed degree p+Nd. There are at least two distinct interior poles
when N>=2. Section 3 makes at least one residue's diagonal defect positive
at every output index. The sharp mixed gate supplies nonnegative mixed
tensors after restoring the common factors. Positive weights then make
the total defect strictly positive at every supported index.

Repeat the argument from yL, not by multiplying a proved cone by y.
The smoothed degree is p+Nd+1 and all index comparisons remain valid.
Thus MP_0 proves raw/y strictness for N>=2 and |rho|<=1.

At N=1 the only block is L_rho. MP_0 proves strictness at rho=0,
precisely L_0. MP_01 additionally handles rho=-1, precisely L_-1.
Neither packet claims
N=1 strictness at arbitrary rho in [-1,1]. That stronger conclusion
is no longer needed by the actual register subsystem.

## 5. Prefixes and every actual consumer

For R_m=sum_(j=0)^m U_j(T/2), m=N-1, the ordinary anchored prefix is
Z_N=b0 R_m+b1 R_(m-1). Its active endpoint-resolvent poles are:

| Prefix degree m | Ratio R_(m-1)/R_m after cancellation | Active poles |
| --- | --- | --- |
| 1 | 1/(T+1) | -1 |
| 2 | 1/T | 0; common factor T+1 |
| 2h>=4 | U_(h-1)/U_h | h>=2 distinct interior poles |
| 2h+1>=3 | (U_h+U_(h-1))/(U_(h+1)+U_h) | h+1>=2 distinct interior poles |

The even factorization R_(2h)=U_h(U_h+U_(h-1)) and the odd
factorization R_(2h+1)=U_h(U_(h+1)+U_h) identify pure paths and
terminal-minus-one Robin paths. All canceled common factors have roots
in [-2,2]. The positive pole count is at least two for m>=3.

For m=1, optional strict L_-1 handles the sole residue under MP_01.
For m=2, strict L_0
times the common weak factor T+1 handles it. For m>=3, Section 3 uses
the total m-1 weak factors per residue, including the common factors,
and the same base index for every active pole. It recovers strictness
in raw/y at every supported index. Thus MP_0 proves ordinary prefixes
for N>=3; MP_01 also proves N=2. N=1 is still excluded: Z_1=b0.

I checked the actual consumers against the existing register identities:

| Consumer | Packet fact used |
| --- | --- |
| Smaller previous term g=q_(N_X-1), N_X>=2 | q_1=L_0 or N>=2 ordinary origin theorem |
| Outgoing smaller/larger origins | q_N strict for N>=1; q_1=L_0 |
| Both child Q=y(q_N-q_(N-1)) | Retained indices N>=2, rho=1 |
| Reverse child block at parameter -1, short | Optional MP_01 parent forward L_-1; not strict under MP_0 alone |
| Reverse child block at parameter -1, long | q_2+q_1, N=2,rho=-1 |
| Every equal-weight window with starting index >=1 | Core q_N at rho=0, or rho=-1 with N>=2 |
| Ordinary anchored prefixes Z_N, N>=3 | Core Section 5, single pole 0, then multiple poles |
| Ordinary anchored prefix Z_2 | Optional MP_01 single pole -1 |
| Trace central/tail deductions using outgoing v | Retained raw strict origins plus canonical degree >=2 |

The larger register with index one uses f_0=b0 only as an identity;
it never requires a seed cone. For an even window beginning at index
m>=1, its Robin core has index m+k>=2 because k>=1. Thus the
discarded N=1,rho=-1 case is not used by those windows.
The endpoint-1 exception remains on its separate audited U/prefix/Robin
theorems. It is not assigned an ordinary MP_0 or MP_01 origin.
New paired origins are still initialized by the parent's actual current
MP_0 packets and the same BOTH algebra. No child packet is used circularly.

## 6. Exact dependencies and status

The ROOT and first-child full MP_sharp certificates initialize MP_0
and MP_01. Replacing the current paired MP_sharp clauses by paired MP_0
retains the core certified origin conclusions, the existing register
transport, the central and parent-degree upper-tail trace subgates,
and strict child Q. The direct Q<D
target and its four LR companion updates are therefore unchanged.

The remaining BOTH obligations are genuinely weaker: child trace gates,
full-continuum weak raw/y single blocks, strict single blocks only at
0, unchanged full sharp mixed gates, and the strict Q<D gate.
If MP_01 is adopted to retain the optional N=2 prefix and short reverse
-1 subgates, both raw/y strict anchors at -1 remain required. The
forward/reversed -1 facts must not be conflated: the known reverse -1
theorem supplies only that orientation. For core MP_0 it is an optional
deduction, not a required child anchor.

This is a logical/common-origin advance. It does not prove any remaining
child trace sign or complete BOTH preservation. Section 7 independently
audits the source lane's complete paired MP_01 example proving strict
separation from MP_sharp.

## 7. Independent full-square check of the weaker paired witness

Read `audit_packet_weakening.md` Section 6. Its trace is
T=10x+1+5sqrt(17), and its paired seeds are (2,1),(1,2).
Every midpoint H is gamma(T-q1)(T-q2), with gamma=2 or 1 and
q1,q2 in [-4,2]. This follows directly by solving the quadratic with
midpoint alpha and omega<= (2-|alpha|)^2; for either positive seed
ratio a<=2, its roots lie between -2-a and 2.

Put B_i=1+5sqrt(17)-q_i. Then 19<B_i<=5+5sqrt(17)<26.
Both T-q_i and y(T-q_i) are weak cones; the raw factors are strict.
At q=-4, y(T-q) has zero central defect. The reverse single at r=-2
is exactly this boundary case, while both 0 and -1 anchors are strict.

The raw midpoint central defect is at least 20000 gamma^2 by the
degree-one CB term (first terminal defect 100, central second minor 200).
For the smoothed midpoint, use K_[y(T-q1)]K_[T-q2]. At output
columns (1,2), intermediate columns (1,2) give a lower bound

    (B_1^2+10B_1-200)(B_2^2-100)gamma^2
       >351*261 gamma^2=91611 gamma^2.

At output columns (0,2), retain three disjoint CB terms, with intermediate
columns (0,2), (1,2), (0,3). Their lower bounds are respectively

    B_1(B_1+10) B_2^2 >198911,
    (B_1^2+10B_1-200)20B_2 >133380,
    10(B_1+20)10B_2 >74100,

each scaled by gamma^2. Their sum exceeds 406391 gamma^2, stronger
than the source's printed 375801 bound. All omitted terms are nonnegative.

The only positive character selectors of T_y are (0,2),(1,2);
the raw constant-seed reference has only the central selector. These
bounds exceed even the maximal uniform-4 references 16T_y or 16T_1.
Where a reference is zero or negative, the weak H/yH cone already gives
the relative inequality. Thus the source's full continuous mixed bounds
hold in both orientations and modes. Its paired MP_01 example is valid
and fails full MP_sharp precisely through the nonstrict boundary single.
It is not a canonical ancestry example, and is not a counterexample to
the target.

`packet_spectral_sparse_verify.py` checks prefix factorizations and
active-pole counts at the smallest cases, plus backwards CB index chains
at central, low, overlap, penultimate and terminal outputs. Its arithmetic
is exact Python integer/Fraction arithmetic. These finite algebra/index
checks are recorded in `packet_spectral_sparse_results.json`; Sections
2-5 supply the arbitrary-degree and all-index proof.
