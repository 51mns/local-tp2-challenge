# A direct two-gap and factorized-exchange formulation

This is an exact full-tree reformulation of the original target. It avoids requiring either child's individual folded kernel to be TP2. It does not yet prove the required coefficient ordering.

Let the endpoints be degree-oriented as `X,Y`, let the center be `C`, and write `y=x+1`. The children are

`U=3yXC-x(X+C)-Y`,

`V=3yYC-x(Y+C)-X`.

Set the two outgoing gaps

`L=U-C`, `R=V-C`.

The original quantities are `S=L` and `D=R-L`. For every pair of Fourier indices `i<j`, bilinearity gives the exact identity

`H(S)_i H(D)_j-H(S)_j H(D)_i`

`=H(L)_i H(R)_j-H(L)_j H(R)_i`.

Thus Local TP2 is precisely a comparison of the two outgoing gap distributions. The subtraction in `D` disappears from the determinant. This is a potentially more direct object for a paired-network argument than separate cone statements about `S`, `D`, or a common multiplier.

## Factorized exchange relations

The global Fricke equation in the original coordinates is

`I=X²+Y²+C²+x(XY+XC+YC)-3yXYC=0`.

Direct substitution of the mutations gives

`UY-(X²+C²+xXC)=-I`,

`VX-(Y²+C²+xYC)=-I`.

Consequently the following identities hold at every canonical node:

`UY=X²+C²+xXC`,

`VX=Y²+C²+xYC`.

After `x=q+q^(-1)`, they factor exactly as

`UY=(C+qX)(C+q^(-1)X)`,

`VX=(C+qY)(C+q^(-1)Y)`.

The corresponding gap identities have positive right sides:

`YL=X²+C(C-Y)+xXC`,

`XR=Y²+C(C-X)+xYC`.

Here `C-X` and `C-Y` have already been proved coefficientwise positive globally. Thus the two gaps admit coupled positive product identities sharing the same center. These identities are stronger than unrelated positivity or shape assumptions on two abstract polynomials.

One must not cancel `X` or `Y` from a Fourier likelihood-ratio comparison without a separate argument: coefficient convolution does not generally reflect likelihood-ratio order. The factorized exchanges identify the precise coupling that a direct argument needs to exploit; they do not themselves justify such cancellation.

## The exact coupled positive networks

Use the globally positive congruence model from `fulltree_kernel_positive_transfer.md`, and let `e=(1,1)^T`. For the Farey-oriented endpoints define

`E_A=Qhat_C-Qhat_A`, `E_B=Qhat_C-Qhat_B`.

The two outgoing gap scalars are exactly

`L_F=e^T Qhat_A^T That E_B e`,

`R_F=e^T E_A That Qhat_B^T e`.

When endpoint degree order reverses Farey left-right order, interchange these two expressions before naming the short and long gaps. Every scalar summand in these constrained networks has nonnegative ordinary coefficients, by the proved global induction. Substituting `x=q+q^(-1)` decorates each occurrence of `x` by one of two signed unit steps.

This gives a concrete finite probability model: take the disjoint union of the two weighted gap networks, retain the branch label, and record the absolute total signed displacement. At height `n>0`, each branch has twice its half-row coefficient; at height zero it has its central coefficient. These common height-dependent factors cancel in branch odds. The desired Local TP2 statement is therefore exactly that the odds of the long branch increase strictly with absolute displacement.

A valid direct proof could now provide a weight-preserving switch for a pair of paths with reversed branch/height order. It must use the paired canonical boundary data `E_A,E_B,Qhat_A,Qhat_B` or the factorized exchanges above. Generic positivity of connector products is insufficient, as the independently checked transfer obstructions show.

## What remains

The direct missing statement is the two-network path-switching inequality, equivalently the monotone branch-odds property. This formulation does not assume the stronger individual-kernel conditions used in the completed ray arguments. No generic matrix TP2 theorem or coefficientwise cancellation has been used to declare that missing statement proved.
