# Common-predicate falsification and exact obstructions

The main new result is a set of **actual reachable counterexamples to
uniform scalar strength/remainder premises**, while the more direct
ordered-minor and proxy predicates remain unrefuted in explicit bounded
scopes. No all-tree closure theorem or Local TP2 theorem is claimed.

All paths below use `s` = degree-short and `l` = degree-long. The old
original `R^13` state is `ls^12`; its known bound/remainder/defect were
crosschecked, not presented as a new discovery. Earlier directories were
read only. New code uses only Python integer/Fraction arithmetic and
standard-library binomial transforms, importing no earlier research code.
The normalized recurrence and original scalar recurrence are rebuilt
independently. All 127 states through depth six were crosschecked, with
Fricke and Cassini identities also checked. The candidates and revisions
were written before their corresponding scans in `falsification_frozen.md`.

## Actual scalar-gate obstructions

For h,b, write lambda=min(delta_n(h)/h_n),
alpha=min(h_n/b_n) over supported b, and d=deg b. The exact optimal
scalar premise lambda*alpha>=8b0 fails despite positive folded defects.

| Predicate | First failed state in the stated complete scope | Exact scalar margin |
|---|---|---|
| h=s,b=r | ssss | -1108168/559 |
| h=ys,b=yr | sss | -163080/241 |
| local lambda=min over 0..d+1, h=s,b=r | s^5 | -7471/189 |
| same, smoothed | s^5 | -606463920/13547 |
| refined L_d, h=s,b=r | s^7 | -237002865928/507947 |
| refined L_d, smoothed | s^6 | -3662046568392/19779809 |

Here L_d is the minimum, for 0<=a<=d, of delta_a/h_a and
(delta_a+delta_(a+1)+delta_(a+2))/(h_a+h_(a+2)). The refined gate also
requires alpha>=2. All the witnesses have alpha>2, so the scalar strength
product itself is the failed condition. The first two witnesses are
minimal over every state through depth six, breadth-first s before l;
the four local-band witnesses are first along the complete pure-short
ray tested through s^60. They do not refute the direct ordered-minor
domination conclusion of the sufficient criterion.

At ssss the exact ordinary polynomials, ascending in x, are

    s=[377,1908,3804,3840,2080,576,64]
    r=[55,180,204,96,16]

and the Fourier rows are

    H(s)=[21745,19188,13084,6720,2464,576,64]
    H(r)=[559,468,268,96,16].

The optimal strength is 64, attained at the terminal index 6, and the
optimal coefficient ratio is 21745/559, attained centrally. Therefore
64*(21745/559)-8*559=-1108168/559. This explains why a full-support
strength theorem can be too coarse for a shorter reference.

At sss the smoothed rows are

    H(ys)=[9424,8336,5728,2984,1120,272,32]
    H(yr)=[241,203,118,44,8].

The optimal strength is 32 and alpha=9424/241. Full polynomials and
all local-band exact witnesses are in the result JSON files.

## Retaining a fixed fraction of the subtraction remainder also fails

Let F=tY, G=F-C and let R_n be the nonnegative exact remainder from
`../fulltree_20261004/quantitative_subtraction.md`. The new candidate
required delta_n(C)-lc(C)H(C)_n>=R_n/32, and, separately, used all
y-smoothed rows with strength lc(C)/2. Every remainder identity B+R
was checked against direct defects, including central reflection and
terminal support.

The first failure along the pure-short ray is smoothed s^28 at n=0:

    surplus=7798251685477764920177070656071551168465698795
    R=260543956178452608264272690610284132206253857862
    surplus-R/32=-5499951121582065409303214807997247407675748211/16.

The raw version first fails at s^29, n=0:

    surplus=41170685539015663466901862174390080461649457394
    R=1365246649941448208212869155015303176748322501609
    surplus-R/32=-47784712692946977272009565434820601975539865001/32.

Every preceding ray state passed the respective predicate at every
index. Thus the combined raw/smoothed candidate has a concrete short
closure failure from s^27 to s^28. The surplus itself stays positive;
these examples do not refute the underlying strength assertion.
The analogous actual short-gap decomposition S=tG-R, G=yg,R=yr,
with strength lc(S)/2 and retained fraction 1/32, also first fails
at s^28,n=0, with margin

    -22679955985200024987820827788504892142457773823/16.

The full polynomials and Fourier rows are saved in
`falsification_targeted_results.json` and `falsification_extra_results.json`.
The complete tree through depth six had no retained-fraction failure;
that bounded observation was not extrapolated.

## The direct relative-minor gate survives the tests that falsify its scalar proxies

At 44 actual states (all depth<=4, s^5..s^12, ls^4..ls^8), both
det K_s>=4 det K_r and det K_(ys)>=4 det K_(yr) passed **3,109,051**
ordered 2x2 comparisons. Each test used rows and columns
0..deg(h)+2 inclusive, with exact reflection and zero beyond support.
This is a bounded kernel-index scope, not a claim about every ordered
minor of the infinite folded kernel.

At the smoothed sss scalar counterexample, the smallest margin among
positive reference minors in this scope is 404352 at rows(0,1),cols(4,5):
det K_h=404608, det K_b=64. At raw ssss it is 2025472 at the same
indices: det K_h=2026496, det K_b=256. Hence those scalar failures
are not actual counterexamples to the tested determinant gate.

## Other exact first obstructions

No fixed MLR orientation between e and r can hold at both root children:
at the short child e=2x+4,r=2x+3 gives W0(r,e)=-2, while at the long
child e=2x+3,r=2x+4 gives W0(e,r)=-2. These are smallest actual
depth-one counterexamples and use W(p,q)=p0*q1-p1*q0 consistently.

A predicate requiring folded membership of every smoothed normalized
coordinate already fails at the root: ye=yr=y has row(1,1) and
delta0=-1. The first long child has a=1, so ya=y fails there as well.
The unsmoothed individual-coordinate fold tests had no failure through
depth six. The actual smoothed g,s,d also had no failure in that scope.
The auxiliary sufficient scalar premise for (g,e) fails at the root:
lambda=1/3,alpha=3,margin=-7; its smoothed version has margin -1.
The suggested R=yr<=lr G=yg companion fails at the root, W0=-2;
it must be exempted or replaced in any proposed root predicate.

## Unrefuted candidates and separate obligations

The exact root of the quantitative center candidate is checked directly:
H(C)=(9,6,2), defects=(27,14,4), strength 2 surplus=(9,2,0);
H(yC)=(21,17,8,2), defects=(31,91,26,4), strength 1 surplus=(10,74,18,2).
The whole shifted trace interval -2<=u<=2 was minimized as an exact
quadratic at every index, rather than sampled at endpoints. The root
minimum surplus for strength 3lc(C)/4 is 27 at the terminal index.

| Candidate | ROOT | SHORT | LONG | IMPLIES TARGET |
|---|---|---|---|---|
| Center lc(C), smoothed half-lc(C), shifted-trace strength | exact root check | bounded passes; no closure proof | bounded passes; no closure proof | not established |
| Actual G=yg half-lc strength, full-lc for nonroot | half-lc root checked; full-lc excluded | bounded passes; no closure proof | bounded passes; no closure proof | not established |
| Actual outgoing D and long gap half-lc strengths | bounded root check | bounded passes; no closure proof | bounded passes; no closure proof | not established |
| Reduction T1/T2/T3, M/Z folds and Q=S-G strict proxy | exact root checks | bounded passes; no closure proof | bounded passes; no closure proof | companion implication belongs to reduction lane |
| Uniform retained fraction 1/32, both center modes | exact root check | FALSE on actual s27->s28 | not proved | no common predicate obtained |
| Full/global scalar relative gate, both modes | exact root check | FALSE on actual s2->s3 | not proved | sufficient relative lemma only |
| Refined local-band scalar relative gate, both modes | exact root check | FALSE on actual s5->s6 | not proved | proposed relative implication requires its own audit |
| Spectral corner packet | X-boundary exception required | bounded corners only | bounded corners only | no target implication established here |

The center/shifted-trace strength scope is exactly the 127 states through
depth six. The reduction gates were checked at every depth-six state and 182
focused fixed-endpoint/switch/alternating states of center degree<=400.
The actual-gap strength scope contains 170 states: all depth<=6 plus
s^j,j<=35 and ls^j,j<=20. The spectral packet corners use 40 actual
states (all depth<=4, ls^j,j<=8, lls^j,j<=6), with positive interval
support explicitly checked; all shifted trace/L/yL/H/yH corner defects
passed. A further fixed-X=P1 midpoint (2,2,-2) test passed H and yH
at all 81 states ls^j,j=0..80, maximum unsmoothed midpoint degree 167.
Corner tests do not establish the continuous parameter packet; no
relative-midpoint determinant gate or switch closure was inferred.

## Abstract-class test and reproduction

The integer abstract scan omitted Fricke but kept every ordinary bound
and every regular surrogate gate E<=G,R<=G,XP1<=E,YP1<=G, folded G/M,
strict Q<XP1M. Of 4185 small constant-a/linear-e,r states, 1049 passed
the entire parent surrogate and both complete child surrogates.
No abstract obstruction was found. A second frozen rational quadratic
grid tested 1944 states, of which 64 met all parent gates and passed both
complete child surrogate predicates. Its finite success gives no proof
of generic closure. Exact parameter
domains are in `falsification_frozen.md` and the reproducer.

Run from this directory:

    python falsification_probe.py --depth 6 --output falsification_results.json
    python falsification_targeted.py
    python falsification_relative.py
    python falsification_extra.py
    python falsification_packet_ray.py
    python falsification_abstract.py

Only assigned-prefix files were written. No GitHub or external upload
was used by this lane. The primary outcome is exact common-predicate
obstruction evidence; the bounded passes identify gates still requiring
root/short/long/implication proofs rather than supplying those proofs.
