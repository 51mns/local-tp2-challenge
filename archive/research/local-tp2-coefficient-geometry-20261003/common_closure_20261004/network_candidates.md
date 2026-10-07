# Frozen selective-row candidates

These candidates are frozen before the probe in `network_probe.py`. All statements concern the actual canonical determinant-one matrices, not arbitrary positive polynomial matrices.

For an interior canonical matrix Q write G=Q11, s=Q21, r=G-s, d=Q22, t=3(x+1)G-x. Candidate Prow requires the folded kernels of r and s to be TP2 and H(s)<=lr H(r). Candidate Pconnector additionally requires folded TP2 of u=t-s and v=t+r, and H(v)<=lr H(u). Root here means the initial center matrix; signed/exceptional endpoint 0 and endpoint 1 must be carried separately.

ROOT / LEFT / RIGHT / IMPLIES TARGET statuses will be filled after exact tests. Cone membership uses all supported folded defects including central and terminal indices. Adjacent likelihood-ratio minors use the full narrower support.

No claim that either predicate implies the target has been made. The motivation is the exact selective recurrence (rC,sC)^T=QhatA^T(uB,vB)^T. In particular this retains det Q=1 and the column boundary corrections.

## Status after the frozen probe

Prow: ROOT proved by exact defects (s:2,1; r:13,7,4) and LR minors (3,2). LEFT / RIGHT unproved, with a bounded exact pass over all 127 centers through depth 6. IMPLIES TARGET unproved.

Pconnector: ROOT proved by exact defects (u:383,655,246,36; v:670,859,310,36) and v-to-u minors (75,46,12). LEFT / RIGHT unproved, with the same bounded pass. IMPLIES TARGET unproved.

A separate transfer-strengthening Pext requiring all polarized source coefficients to be nonnegative is rigorously obstructed in `network_exterior_transfer.md`. It was isolated by algebraic derivation rather than a broad numerical search. The actual root right child has an active negative coefficient -8 times input weight 3^2. This does not falsify Prow, Pconnector, or the target.
