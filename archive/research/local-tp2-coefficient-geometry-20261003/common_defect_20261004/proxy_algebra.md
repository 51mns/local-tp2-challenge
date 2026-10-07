# A direct SHORT lower-block order and a coupled D advance

Status: the identities below are universal canonical algebra. The SHORT
lower-block LR order is proved for every ordinary smaller endpoint along a
certified history, using a proved retained central flag. It removes one
whole signed cross-order from direct Q<D preservation. The independent
D-advance comparison and the LONG signed residual remain open. No full
BOTH proxy preservation or full-tree Local TP2 is claimed.

## 1. Direct transformation retaining the parent comparison

Use y=x+1, t=3yX-x, T=3yC-x, M=T+1, A=t-2, h=t-1=A+1,
E=ye, G=yg, R=yr, S=ys, Q=S-G and D=EM. Put

    B=T-t=3y(E+G), H=G-AE=y[X(3X-2)+r],
    K=M H+B S.

The canonical SHORT child obeys the exact two-pair update

    Q'=hQ+AG, D'=hD+K.                               (1)

Here G=A E+yX(3X-2)+R and S=tG-R. In particular all negative
subtractions in H cancel before it is evaluated. An equivalent expression
retaining that cancellation is

    K=(t+1)H+3y(E+G)[tG+yX(3X-2)].                  (2)

The current parent strict comparison transports through the common h:

    hQ <_lr hD.                                      (3)

For ordinary endpoints K_h is supplied by the origin shifted-trace gate
at parameter 1. At endpoint 1, h=2(x+2), whose folded kernel is strict.
Strictness in (3) follows from the exact folded Cauchy--Binet argument:
Q has degree at least deg h, and its strictly positive adjacent LR minors
with D are retained at i=max(deg h,min(n,deg Q)). The second minor is a
positive ordinary log-concavity difference of h, or its terminal-central
value 2(lc h)^2. This covers zero, the complete interior, and terminal
support. No cone assertion about D is needed.

## 2. A proved ordinary-endpoint lower-block order

**Theorem.** Assume the parent regular LR link R<=_lr G, K_G folded TP2,
the weak shifted-trace gate K_A, nonnegative ordinary coefficients of A,
and the retained flag delta_0(A)>=1. Then

    AG <=_lr hQ.                                     (4)

The essential identity is the exact full-character formula

    R(AG,hQ)=T_G (T_A-1)D_A
                     +T_A R(R,G)+R(R,AG),             (5)

where D_A=R(1,A). It follows before the character transform from
Q=hG-R and

    R(A,h^2)=(T_A-1)D_A.

Weak K_A makes T_A character nonnegative. The integer central flag
makes T_A-1 character nonnegative: only its central character is reduced.
The ordinary coefficients of A give D_A character nonnegative. Likewise
T_G and R(R,G) are nonnegative by the existing kernel and LR premises.
Finally

    R(G,AG)=T_G D_A >=_char 0,

so R<=_lr G<=_lr AG. Positive dense supports and LR transitivity give
R(R,AG)>=_char0. Every term in (5) is therefore signed from an already
proved premise. This is an all-character statement, not merely an
adjacent-boundary inequality.

The central flag is NOT extracted from the weak MP_sharp trace premise.
It is a separate proved history record. At the initial ordinary endpoint
X=P, A has half-row (10,8,3) and delta_0(A)=2. Every subsequently created
ordinary endpoint is a prior center C. Its trace is the recorded old T;
the proved all-shift central theorem in
`../common_crosscenter_20261004/root_central_trace.md` supplies strict
central defects at creation, independently of a child packet or proxy.
Integer coefficients make that strict value at least one. Retention
keeps the trace and flag fixed. This ROOT/initialization/retention flag
has no additional unresolved transport obligation along certified
histories. The stronger bound185 at newly created centers is available
but unnecessary here.

The endpoint-1 trace A=2x+1 is not weak folded TP2, so (5)'s sign proof
does not cover that endpoint. The omission is essential: at the actual
root, R(AG,hQ) has central character -6. This is an actual obstruction
to extending the lower-block theorem without its hypotheses, not a
failed child Q<D comparison. The first short record has nonnegative
lower-block characters, but that finite check is not a boundary theorem.
No ordinary packet is assigned to endpoint 1.

## 3. One independent D comparison would complete ordinary SHORT

Combining (3)-(4), the following explicit comparison is sufficient:

    hD <=_lr D', equivalently R(hD,K)>=_char0.          (6)

It concerns the advance of D alone, rather than the target pair Q',D'.
Indeed, (6) says hD<=_lr K because D'=hD+K and R(hD,hD)=0.
Together with (3)-(4) it supplies

    AG<=_lr hQ<_lr hD<=_lr K.

All four terms in the expansion of R(hQ+AG,hD+K) are nonnegative,
and its R(hQ,hD) term is strictly positive on the supported output
indices. Hence Q'<_lr D'. This argument proves a genuine conditional
SHORT theorem from a separate one-component D advance, without assuming
the child's packet or comparison. Condition (6) itself remains open.

The exact coupled source can also be written in fixed-endpoint variables.
Let K0=yX(3X-2), E_0=E, E_1=E+G, E_2=E+G+S. Then

    E_2=tE_1-E_0+K0,
    Q=A E_1+K0, D=E_0[t+1+3yE_1],
    D'=E_1[t+1+3yE_2].                               (7)

Thus (6) is the determinant comparison

    (t-1)E_0[t+1+3yE_1] <=_lr E_1[t+1+3yE_2].        (8)

The positive unanchored prefixes from the frozen origin subsystem are
available, but E_j carries the fixed signed anchor a_O-a_X. Dropping
that anchor or multiplying separately by y would lose a required
correlation. The known sharp packet has not yet been shown to sign (8).

For reference the homogeneous proxy registers give one further exact
cancellation. With Qprev=A E_0+K0 and

    F0=(t+1)A-3yK0=3yX+x^2+x-2,

one has

    Qnext=tQ-Qprev,
    A^2 D=(Qprev-K0)(3yQ+F0).                         (9)

Multiplication by A^2 does not reflect LR, so (9) is retained as a
correlated identity, not used as a deconvolution theorem.

## 4. LONG retains a signed residual

Set tau=3yY-x, A_L=tau-2, h_L=tau-1, F=S+D. Its exact update is

    Q'_L=h_L(Q+D)+(A_L G-E),
    D'_L=h_L D+K_L,
    K_L=M(G-h_L E)+3yG F.                            (10)

The parent comparison directly gives Q+D<=_lr D, with relative tensor
R(Q+D,D)=R(Q,D). Its adjacent minors beyond deg Q are zero, so it
must not be called strict throughout the longer Q+D support. Common
h_L transports this weak order; it does not by itself provide strictness
through the full LONG child support. However K_L has the signed
piece G-h_L E, and (4)'s proof does not apply to A_L G-E. Treating the
larger previous register y(e+g) as a strict cone would be invalid at
its possible index0 seed. A valid LONG analogue requires either a signed
coupled determinant certificate or another cancellation; it is not
supplied by (10) alone.

## 5. Scope

| Obligation | Outcome |
| --- | --- |
| Canonical direct SHORT/LONG identities | PROVED, no Fricke needed for (1),(2),(7),(9),(10) |
| Retained ordinary central trace flag | PROVED ROOT/initialization/retention history subsystem |
| Ordinary SHORT lower-block order AG<=hQ | PROVED from existing LR/kernels and retained flag |
| Parent strict comparison through common SHORT h | PROVED throughout hQ support |
| Parent Q+D<=D through common LONG h_L | PROVED weak order; full LONG strictness not supplied |
| Ordinary SHORT from the independent D-advance gate | PROVED conditional implication |
| Independent D-advance gate and LONG residual signs | OPEN |
| Full BOTH Q<D and new paired packets | OPEN |
| Full-tree strict Local TP2 | OPEN |

The targeted verifier records exact identities and seed source checks.
Passing a few source arrays is not evidence of arbitrary-parent closure.

The SHORT lower-block theorem only consumes the listed LR links, K_G,
weak trace kernels, ordinary coefficients, and the retained central flag.
It therefore also applies to an audited MP_0 predicate augmented by
the retained central flag that supplies those conclusions. The flag is
not silently inferred from core MP_0, and strictness of every parent
L_r is not used here.

Independent analytic review by the proxy-character lane passed the
identity (5), every sign dependency, the retained-flag distinction,
and strict common-h Cauchy--Binet coverage including zero and terminal.
