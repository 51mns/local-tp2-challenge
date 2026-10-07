# Falsification gate: no canonical obstruction; no continuation proof

## Frozen bridge and exact scope

The frozen SHORT proposal is

    hD <=_lr D'  <=>  R(hD,K) >=_char 0,
    h=t-1, D'=hD+K.

An independent integer-polynomial implementation reconstructs canonical
states directly from (a,e,r)=(0,1,1), with SHORT=(a,e+g,g) and
LONG=(a+e,g,e+g). It imports no previous worker arithmetic. The bounded
records ROOT,S,L,SS,SL,LS,LL,SSS have no negative selector in the frozen
D comparison, and their actual SHORT Q',D' pair has no negative selector.
These finite passes establish neither the proposed bridge nor BOTH closure.
ROOT,S,L inherit their existing audited certificates; deeper complete
parent P_0 membership is not asserted in this lane.

The endpoint-1 records ROOT,S,SS,SSS have delta_0(t-2)=-7, so they must
remain in the separate boundary subsystem. The ordinary records L,LS
have value 2, and SL,LL have value 185. Treating endpoint-1 as ordinary
would silently discard the retained central-flag premise.

## Current MP_0 viability on actual canonical records

The more relevant falsification question was whether the adopted current
paired MP_0 already fails on actual near-root states. The exact records
SS,SL,LS,LL,SSS,SSL,SLL,LSL admit complete CONTINUUM certificates for
both CURRENT packet orientations (T,c,e), (T,e,c), c=e+g+s:

* Every shifted-trace selector is nonnegative on the whole [-2,2].
* Every raw/y single-block selector is nonnegative on that whole interval;
  support entries are positive, and supported defects at zero are strict.
* Every raw/y sharp mixed selector is nonnegative on the whole square
  [-2,2]^2, with F=L_r(T-s), G=L_s(T-r), and J(F,G).

This is a finite-state certificate of the full stated parameter gates,
not sampling evidence. Every trace/single selector is quadratic in r.
Interpolation at -1,0,1 reconstructs its exact coefficients; endpoint
values and the interior vertex, when applicable, give its exact minimum.
Support entries are affine, so endpoints certify positive interval support.
For mixed gates, F and G are bilinear in (r,s); their polarized selector is
biquadratic. A 3x3 exact interpolation reconstructs it. Substituting
r=-2+4u,s=-2+4v and converting to degree-(2,2) Bernstein form gives
nonnegative coefficients for EVERY selector on the whole unit square.
No subdivision was needed in any of these records.

| Record | Trace minimum character on [-2,2] | Both current MP_0 |
| --- | ---: | --- |
| SS | 576 | Certified |
| SL | 5184 | Certified |
| LS | 2916 | Certified |
| LL | 11664 | Certified |
| SSS | 2304 | Certified |
| SSL | 82944 | Certified |
| SLL | 746496 | Certified |
| LSL | 944784 | Certified |

This only certifies CURRENT paired packets. It does not certify all stored
origin packets/registers, LR links, central history flags, and strict proxy
clauses comprising full P_0 at these deeper states. It therefore must not
be used as a fully-premised P_0 counterexample or an induction theorem.

## Decision

No exact canonical obstruction was found to the frozen D advance or to
the actual current MP_0 gates tested here. There is no new proved
arbitrary-parent bridge, fully-premised counterexample, or alternative
closure mechanism in this lane. Do not continue the strategy merely on
the basis of these finite passes. No new relaxed witness was promoted:
previous unrelated-cone failures do not test full P_0 and do not answer
its viability question.

Reproduce from this directory:

    python falsification_verify.py
    python falsification_packet_verify.py
    python falsification_continuum_verify.py

The first two files are bounded diagnostic replays; the third provides
exact continuous-parameter certificates for fixed canonical states only.
All scripts and outputs remain inside strategy_gate_20261004. No earlier
directory or GitHub state was modified.
