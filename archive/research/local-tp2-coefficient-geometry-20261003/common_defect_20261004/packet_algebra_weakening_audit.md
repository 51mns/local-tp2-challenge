# Independent algebra/consumer review of the weak-single packet

**PASS, conditional origin theorem and sufficient-predicate weakening.**
This independently reviews `audit_packet_weakening.md`, including its core
W_0, optional W_01, actual consumer map and abstract strict-separation
example. It does not prove child weak-single or mixed preservation.

## 1. The strictness argument is noncircular and index-complete

For a fixed supported defect, E_j(r)=delta_j(L_r) is a nonnegative
polynomial of degree at most two on [-2,2]. Strictness of L_0 makes it
nonzero. An interior zero must have even multiplicity, so there is at
most one. The identical argument uses the independent y-mode E_j.

In a Robin N>=2 resolvent, all N poles are distinct and strictly inside
(-2,2), with positive endpoint residues. For a selected output defect,
the backwards CB rule i=max(d,min(n,f)) selects a base index depending
only on the common degrees and the number of factors. It is independent
of the omitted pole and the values/order of the remaining poles. Thus
at least one of the distinct poles has a positive selected base defect.
Every retained CB multiplier is strictly positive: for central output
it is 2(lc B)^2; otherwise it is the Toeplitz difference
Delta_|i-n|(B), whose telescoping expression contains the positive
terminal folded defect. All omitted terms are nonnegative.

That residue has a strictly positive diagonal contribution at the chosen
output. The unchanged sharp mixed gate makes all off-diagonal residue
contributions nonnegative after common trace factors are restored.
This proves strictness separately at every output, including both
boundaries. No globally strict residue is required, and the good pole
may vary with the output index. The y proof begins with yL, rather than
assuming y is a cone multiplier.

## 2. Actual core consumers require only W_0

I checked the register index restrictions against the exact mutation
identities in the frozen `common_transport_20261004/packet_transport.md`.

| Consumer | Required statement | W_0 coverage |
| --- | --- | --- |
| Smaller previous gap g | q_(N_X-1), N_X>=2 | q_1=L_0; q_N strict for N>=2 |
| Both outgoing register gaps | q_N, N>=1 | Same |
| Short new larger origin | q_1=L_0; q_0 is an identity | Strict at zero is sufficient; no seed cone |
| Long new larger origin | q_2, previous q_1=L_0 | Multi-pole argument and zero anchor |
| Ordinary current/child Q | y(q_N-q_(N-1)), retained N>=2 | Robin rho=1 at N>=2 |
| Equal-weight windows starting at index>=1 | Ordinary q or rho=-1 block | Even windows have N>=2; odd windows use strict q_N |
| Child central trace argument | Actual outgoing v is strict, deg v>=2 | Uses q_N as above, not a prefix seed |
| Endpoint-1 exception | Frozen independent pure U/prefix/Robin theorem | Unchanged |

The current trace gate still supplies M=T+1. The strict Q and the
assumed direct Q<D comparison still give the existing target and LR
consumer implications. No N=1 Robin theorem at arbitrary rho is needed.

Two prior optional subgates genuinely use L_-1: the short reverse child
anchor and prefix Z_2. Core W_0 cannot claim them strict. W_01 retains
both. Prefix Z_3 has the single active pole zero and is strict under
W_0; larger prefixes have at least two interior active poles and follow
from the same selected-index argument. Prefix Z_1=b0 remains excluded.
The source note makes all these distinctions explicitly.

A full-interval uniform positive minimum eta_j is NOT retained by the
weak packet. Any quantitative estimate using such a minimum must be
reproved or omitted. The source's consumer ledger correctly excludes
that older optional quantitative premise.

## 3. Independent verification of genuine paired strict separation

For T=10x+1+5sqrt(17), e=1,c=2, put B=1+5sqrt(17)-q for q in [-4,2].
The rational bounds 4<sqrt(17)<21/5 give 19<B<26. Exactly,

    H(T-q)=(B,10),
    H(y(T-q))=(B+20,B+10,10),
    delta_0(y(T-q))=-B^2+10B+400.

The positive zero is B=5+5sqrt(17), attained exactly at q=-4. The other
raw/smoothed defects are positive on the stated interval. Consequently
the paired singles are weak throughout [-2,2], strict at r=0,-1, and
the reversed yL_-2 has a zero central defect. Thus MP_sharp fails.

For either orientation, H=gamma(T-q1)(T-q2), gamma=2 or1. Writing the
seed ratio eta=b1/b0 in {1/2,2}, its roots are

    q1,q2=alpha-eta/2 +- sqrt(eta^2/4+omega).

With |alpha|<=2 and omega<=(2-|alpha|)^2, the elementary inequality
sqrt(eta^2/4+t^2)<=eta/2+t gives -4<=q1,q2<=2. This covers the complete
parameter square. The two factors and the separately smoothed first
factor are weak cones; products therefore certify H and yH.

The raw central H defect has a CB contribution 20000gamma^2. For
A=10x+B1,B=10x+B2, both Bi>19, a direct calculation gives

    Sel_(0,2) T_(yAB)
       =[B1B2+10(B1+B2)+300]B1B2+100H(yAB)_0
       >375801,

while the CB term for selector (1,2) is

    delta_1(yA) Delta_0(B)
       >(361+190-200)(361-100)=91611.

The only positive characters of T_y are those two selectors, each one;
T_1 has only its central positive character. The largest uniform-4
reference in either orientation is 16 times these unit references.
These explicit bounds dominate it, and cone positivity covers the
remaining zero/negative reference coefficients. Hence the full sharp
mixed gate holds raw/y, even the stronger uniform-4 bound. This proves
paired W_01 without paired MP_sharp, on the full continuous square.
The example is abstract and noncanonical; it does not disprove a target.

`packet_algebra_verify.py` now independently checks the displayed raw/y
defect formulas, exact quadratic-field boundary zero, selector-(0,2)
identity, CB constants, and the roots' elementary square bound. It uses
standard-library exact polynomial/Fraction arithmetic only.

## 4. Scope

The weakening is a valid common-origin and sufficient-predicate advance.
Core W_0 retains the actual target/register consumers; optional W_01
retains the earlier -1 anchor and prefix-N=2 subgates. ROOT and first
children initialize both through the existing stronger certificates.
BOTH weak-single, shifted-trace, full mixed and strict-zero-anchor
preservation are still unproved, as is BOTH strict Q<D. No assertion of
complete child packet or full-tree Local TP2 closure follows here.
