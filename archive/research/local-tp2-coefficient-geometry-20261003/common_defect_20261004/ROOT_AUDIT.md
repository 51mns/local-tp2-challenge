# Supervisor audit: strictness can be concentrated in the resolvent sum

Full-tree strict Local TP2 remains **OPEN**. This campaign starts from
private commit `457e1588d0106c9a9262e6a38d9e882e9678990d` and uses six
GPT-6.1 Sol workers, with independent proof and falsification lanes.
All earlier checkpoints remain unchanged.

## 1. The new core predicate is genuinely weaker

For an ordinary origin, retain positive interval supports, the strict seed
degree bound, all weak shifted-trace gates and the complete two-parameter
sharp mixed gates in raw and y modes. Require single blocks L_r and yL_r
to be weak cones on the full interval, with strict supported defects only
at r=0. Call this packet MP_0. The optional MP_01 also requires strictness
at r=-1. Both are implied by the old MP_sharp.

The key new argument is a quadratic zero count, not a finite spectral scan.
Every base defect is nonnegative on [-2,2], is quadratic in r, and is
positive at zero. It therefore has at most one distinct zero in (-2,2).
For a Robin path of length N>=2 there are at least two distinct interior
eigenvalues with positive endpoint weights. At each output index the
backwards Cauchy--Binet choice selects the SAME base index for all residues.
At least one residue is consequently strict at that index; the other
diagonal and mixed contributions are nonnegative. This proves strictness
of the whole sum even if some individual residue defects vanish.

The supervisor independently checked the exact selected CB factor. For
weak factors of degrees f>=d and output n, put i=max(d,min(n,f)). At n>=1
the second minor is Delta_|i-n|>0 because the sum-index terms vanish;
at n=0 it is 2(lc B)^2>0. The telescoping identity
Delta_j=sum_(k=j)^d delta_k makes the first claim strict using the terminal
square, without assuming any missing strict trace defect.

MP_0 retains ordinary q_N for N>=1 and Robin q_N-rho q_(N-1) for N>=2,
|rho|<=1. Every core ordinary Q register has index at least two. The root
endpoint-1 exception remains on its separate audited theorems.

Thus replace both current and stored ordinary packets by MP_0 in the
previous P_D predicate, with the proved central flags in Section 5, to
obtain the adopted P_0. ROOT and the first two children
inherit their stronger certificates. The exact BOTH register transport,
four LR companion updates and direct TARGET sandwich S<=Q<D still hold.
No child packet or future target is assumed in this deduction.

The two remaining closure TYPES are BOTH paired MP_0 and BOTH strict Q<D.
They are not proved in this checkpoint. This is a reduction of the actual
proof burden, not a completed induction and not an estimate of how many
future proofs will be needed.

## 2. Which previous consequences must not be carried over silently

Under MP_0, ordinary prefixes are strict for N>=3. The N=3 prefix uses
L_0 times the weak factor T+1; larger prefixes have at least two active
poles. Prefix N=2 is L_-1 and is only weak under MP_0.

MP_01 retains strict prefix N=2 and the short reverse child block at
parameter -1. The corresponding long block q_2+q_1 remains strict under
MP_0 already. The old complete reverse upper-band proof cannot simply
retain its short strict anchor after dropping this optional clause.

Likewise the earlier quantitative theorem with a uniform strictly positive
minimum of delta_j(L_r) over the whole interval is not retained: that
minimum can be zero. Its algebraic spectral identities are still valid.
Neither optional theorem is needed for the core P_0 target implication.

The generic short update does not automatically certify its new e seed:
its larger-origin index can be one, leaving e'=f_0=b0 with no seed cone
premise. The long update's previous small window has index at least one.
This distinction prevents a circular attempt to certify c by looking two
short moves into the future.

## 3. The complete weak mixed gate remains essential to this method

Pairs of roots from the same N-vertex pure Jacobi path become dense in
[-2,2]^2 as N grows. Each mixed character coefficient is a continuous
polynomial in its two parameters. Requiring it to be nonnegative for all
future path spectra is therefore equivalent to its continuum weak gate.
It is not a weaker replacement with a separate finite proof burden.

The two certified orientations also cannot be treated as one mutually
compatible family. If positive interval polynomials have degrees D and
E>=D+2, their mixed selector at columns D+1,D+2 is exactly
-lc(f)H(g)_(D+2)<0. Canonical forward/reverse blocks have this degree gap
for every parameter pair. The witness is a character coefficient and an
actual ordered mixed minor, not a scalar evaluation or an ordinary power
coefficient. This does not contradict either within-orientation packet.

## 4. Independently verified trace obstruction

The falsification lane found ordinary positive integer polynomials

    f=2x+3+3(x+1)^2 * 2(x+64)^2,
    v=6(x+2)^5.

Every f-r, r in [-2,2], has positive interval support and strict folded
defects; v and yv have strict folded defects as well. Nevertheless

    delta_3(f+3y^2 v)=-71023104.

`root_obstruction_audit.py` independently reconstructs these polynomials
without importing worker arithmetic. It verifies the complete finite
character array over the continuous shift interval by exact quadratic
minimization, as well as all supported strict defects and the negative
updated defect. The failed index is unaffected by changing r.

This refutes closure based only on separate trace/addend cones, ordinary
positivity and the displayed trace shape. It is NOT an actual canonical
state: no normalized ancestry, Fricke completion or origin packet is
claimed. It does not refute Local TP2.

## 5. A new SHORT comparison, with an explicit retained history flag

Write A=t-2, h=t-1, H=G-AE, B=T-t and K=MH+BS. The exact SHORT
identities are Q'=hQ+AG and D'=hD+K. The parent strict Q<D transports
strictly through the common weak h kernel at every supported hQ index.
The supervisor checked the same CB index choice as in Section 1, now
retaining a strict adjacent relative minor of Q,D instead of a kernel
defect. It includes the actual child Q' terminal support.

For ordinary endpoints, the full-character identity

    R(AG,hQ)=T_G(T_A-1)R(1,A)+T_A R(R,G)+R(R,AG)

proves AG<=hQ from the existing regular LR links/kernels and the flag
delta_0(A)>=1. This flag must NOT be inferred from weak MP_0 alone.
It can be added as a proved history clause: the initial ordinary endpoint
P gives value 2; newly created endpoints inherit the already proved
strict central trace bound, and retained endpoints keep their trace.
Keep the corresponding current-center flag as well. Its BOTH transport
uses the MP_0 origin theorem above, so it adds no new open preservation
condition. The adopted P_0 includes these flags explicitly; the bare weak
packet by itself does not.

The endpoint-1 boundary is excluded from that sign theorem; its actual
root lower-block comparison has central coefficient -6. Boundary
theorems remain separate.

The one-component comparison hD<=D' (equivalently hD<=K) would now
complete the ordinary SHORT proxy update via

    AG<=hQ<hD<=K.

This final comparison is OPEN. The LONG algebra has a signed residual
and only a weak transported Q+D<=D order; it cannot inherit an unjustified
strict order above deg Q. Thus the entire BOTH Q<D obligation remains.
The independent review is `proxy_character_short_audit.md`.

Here SHORT and LONG distinguish endpoints by degree; they must not be
identified with fixed left/right labels on every drawing of the tree.

## 6. Exact coupled prefixes and actual failures of sourcewise shortcuts

For a smaller-endpoint origin, the actual E row is
y[a_O-a_X+Z_(N-1)], while Q and D also depend on Z_N. Both new-origin
initializations and retention obey these identities. The signed anchor
a_O-a_X cannot be discarded. In the exact split
R(Q,D)=T_ZN R(J,L_N)+Psi_N, Psi_N already has coefficient -2504 at
the genuine first long state, although the whole comparison is strict.
The source/residual split is exact algebra, not a solved positivity gate.

The actual SSS state also refutes the proposed reverse-single low-band
monotonicity sign: a relevant mixed coefficient is -6386912. Its single
block defect remains positive. The preceding SS full packet is not
asserted from a finite computation. These witnesses invalidate the
specified sign shortcuts, not an implication whose complete parent
premises have not been verified.

## 7. Saving and verification scope

The public reference `51mns/AIMath-public/main` was reread at
`6e770f3b3e3f26af5df5308572917559343b68f4`, unchanged. No public or main
write is included. Exact replay validates identities and finite witnesses;
the universal conclusions rest on the analytical proofs and their
independent audits. The final appended Git tree must preserve all 904
prior blobs byte-for-byte and add only this campaign directory.
