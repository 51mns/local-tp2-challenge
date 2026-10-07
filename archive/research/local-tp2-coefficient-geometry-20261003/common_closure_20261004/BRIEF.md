# Common left/right closure campaign

The user has explicitly changed the success criterion: do not accumulate more special path families as the main goal. Find a state predicate P with (1) a proved root, (2) closure under BOTH children, and (3) strict Local TP2 as a consequence. A rigorous obstruction to a proposed common predicate also counts as useful evidence, not as a solution. GPT-6.1 Sol parallel proof/search/audit is authorized. Root integrates and saves; subagents do not write GitHub or edit earlier work.

Base private commit: d8ac2ae474512f6562d975129d4f5d0da0c2da4c, research/local-tp2-coefficient-geometry-20261003. Public reference already read at 6e770f3b3e3f26af5df5308572917559343b68f4. Parent directory is read-only. Write only assigned-prefix files in this directory. Exact Python integer/Fraction computations; no finite-to-infinite inference, no unsupported claims of new results. Report shared foundations/imports.

## Canonical target and normalized exact state

Root endpoints 1,x+2; center 2x^2+6x+5; y=x+1. Original children are 3yAC-x(A+C)-B and 3yBC-x(B+C)-A. Order endpoints X,Y and children by degree. Define a=(X-1)/y, e=(Y-X)/y, g=(C-Y)/y, t=2x+3+3y^2a, k=(1+ya)(1+3ya), g=(t-2)e+k+r. Root (a,e,r)=(0,1,1). The short-child / long-child mutations are

    (a,e,r) -> (a,e+g,g),
    (a,e,r) -> (a+e,g,e+g).

These give every binary path; distinguish these degree-ordered children from original named L/R if necessary. Proved ordinary coefficient bounds: 0<=a<=e, 0<r<=a+e, g>=a+e+r+1. Proved identities:

    r g=(t-2)e^2+2k e+3a(1+ya)^2,
    e^2-(2x+1)a(a+e)-e-2a=(a+e-r)(g+a+e),
    g^2-r s=(1+ya)^2(1+3a), s=tg-r.

Actual gaps: S=y s and D=y d, d=e(t+1+3y^2(e+g)). H(P)_n=[q^n]P(q+q^-1). Goal H(S)_n H(D)_(n+1)-H(S)_(n+1)H(D)_n>0 for all 0<=n<=deg S, including terminal support.

Folded defect delta_n(h)=h_n^2-h_(n-1)h_(n+1)-h_(n+1)^2+h_n h_(n+2), reflection h_-n=h_n and zero past degree. Kernel K_h(0,j)=h_j, K_h(i,0)=2h_i for i>0, K_h(i,j)=h_|i-j|+h_i+j for i,j>0. The prior folded-cone / TP2 / strength-product theorems are available but state exactly where used. Multiplication by y is NOT a cone-preserving operation in general.

## Existing outcomes and obstacles

All L^m R^k and all L^m R L^ell have internal proofs, in ../GENERAL_ONE_TURN_RESULT_JA.md and ../second_turn_20261004/THEOREM.md. Do not prove a third path family unless it directly supplies a common closure mechanism.

../fulltree_20261004/RESULT_JA.md and invariants_normalized_state.md give the positive all-tree recurrence above. Ordinary positivity is already proved; it does not imply Fourier TP2. network_quotient_constraints.md gives golden-ratio and all-order coefficient barriers. These are insufficient so far.

The rough quantitative subtraction lower bound B>=0 fails on actual canonical R^13; the positive remainder restores the actual defect. See quantitative_subtraction.md and falsification_report.md there. Mixed two-variable character summands also have actual negative examples; arbitrary positive mixtures are not cone-closed. Do not discard correlations from Fricke/Cassini identities.

../fulltree_kernel_row_states.md and fulltree_kernel_positive_transfer.md give positive canonical matrix representations and selective row companions. Entrywise/row-column-symmetric cone assertions fail already at root. Raw-gap LGV determinant is negative at root. ../recovery_fulltree_shift_obstruction.md rules out EVERY fixed real shifted-power basis as a blanket TP2 transport solution. Quotient/QW3 claims must avoid circular restatement of the target.

Potential newly available mechanism: ../second_turn_20261004/audit_scaled_relative_minors.md. If h is lambda-strong, h>=alpha b coefficientwise, b_n<=b0, and lambda alpha>=8b0, all ordered folded minors of h dominate 4 times b. This repaired the reversed mixed blocks. Can a state-dependent analogue close under BOTH mutations? The midpoint mixed compatibility identity is exact; see second_turn kernel theorem.

## Deliverable requirements

State each candidate as an explicit predicate, with separate ROOT / LEFT / RIGHT / IMPLIES TARGET statuses. Distinguish actual canonical counterexamples, counterexamples to an overly broad abstract class, and merely missing proof. Freeze a proposed statement before computation when possible. A numerical pass is bounded evidence only. Save exact minimal counterexamples and a reproducer. For promising theorems, provide complete reasoning, including small/central/terminal indices and smoothing; submit for another lane's audit. Communicate substantive findings early to root and relevant peers. Do not spend the whole task on deep brute-force scans.
