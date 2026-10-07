# Audited upper-tail defects for the general one-turn midpoint

**Status: proved partial result.** The perturbation by G preserves the
required quantitative defect bound on the upper part of the support.
This does not establish the remaining low-index defects, full midpoint
cone membership, or all-index relative kernel compatibility.

Use the inner definitions

`y=x+1`, `z=2x+3`, `u_j=U_j(z/2)`,

`T_j=sum_(i=0)^j u_i`, `g_m=1+yT_m`,

and fix m>=1. Put

`A=T_(m+1)`, `B=T_(m-1)`, `t=3yg_m-x`,

`F=A(t-r)(t-s)`, `G=B(t-c)`, `H=F+G`,

where r,s,c belong to [-2,2]. In particular the result applies to the
actual midpoint c=(r+s)/2, but it does not require that restriction.
Write f_n=H(F)[n], g_n=H(G)[n], h_n=f_n+g_n, and

`b0=H(B)[0]`, `mu=8b0`.

To avoid confusion, g_n in the coefficient calculations below denotes
the half-row of G; the inner center polynomial is denoted g_m only
inside the displayed definition of t.

The established sharp-strength theorem supplies

`delta_n(F)>=lambda f_n`,

`lambda=9*2^(3m-2)=(9/4)*8^m`.

It also makes f a positive decreasing row. The degrees and leading
coefficients are exactly

`N=degree(F)=3m+5`, `d=degree(G)=2m+1`,

`f_N=18*8^m`, `g_d=3*2^(2m-1)`.

For m>=2 the next coefficient satisfies

`g_(d-1)=(3m+3/2)g_d`.

The exceptional case m=1 has ratio `g_(d-1)/g_d=4`, since B=T_0=1.
The general upper bound with 3m+3/2 is still valid there.

## 1. A uniform upper bound for the target strength

At x=2 the inner recurrence variable is z=7. Its positive Chebyshev
values satisfy `u_j(2)<=7^j`. Therefore

`b0<=B(2)<=sum_(j=0)^(m-1)7^j=(7^m-1)/6`,

and hence

`mu<= (4/3)(7^m-1) < (4/3)7^m`.

In particular `lambda>mu`, and the terminal coefficient obeys
`f_N>mu`. Since f is decreasing, `f_n>=f_N>mu` throughout its
support. This last bound is useful when the G contribution to h_n is
nonzero.

## 2. Exact perturbation identities at the two support boundaries

Expanding the quadratic folded defect gives

`delta_n(H)=delta_n(F)+delta_n(G)`

` +2f_n g_n-f_(n-1)g_(n+1)-g_(n-1)f_(n+1)`

` -2f_(n+1)g_(n+1)+f_n g_(n+2)+g_n f_(n+2)`.

At n=d+1, all terms of G except g_d vanish, so

`delta_(d+1)(H)=delta_(d+1)(F)-g_d f_(d+2)`.

This is the exact negative mixed defect. Its existence rules out a
proof based on unqualified nonnegative mixed defects. It is nevertheless
absorbed by the known strength of F.

At n=d the exact expression is

`delta_d(H)=delta_d(F)+g_d^2+2f_d g_d`

` -g_(d-1)f_(d+1)+g_d f_(d+2)`.

The positive term 2f_d g_d must be retained when proving a bound in
terms of h_d=f_d+g_d. A bound only in terms of f_d would not by itself
establish the required strength for H.

## 3. Required strength from index d+1 onward, for every m>=1

Because f_(d+2)<=f_(d+1),

`delta_(d+1)(H)>=(lambda-g_d)f_(d+1)`.

The exact ratio `g_d/lambda=1/[3*2^(m-1)]` is at most one third.
Consequently

`lambda-g_d >= (2/3)lambda=(3/2)8^m > mu`.

At this index g_(d+1)=0, so h_(d+1)=f_(d+1). Thus

`delta_(d+1)(H)>mu h_(d+1)`.

For n>=d+2 all perturbation terms vanish and h_n=f_n. The sharp
strength of F gives the same strict inequality through n=N.
Therefore, for every m>=1,

`delta_n(H)>8b0 H(H)[n]`, for `2m+2<=n<=3m+5`.

This independently confirms the upper-tail statement in
`mixed_kernel_cross_tail.md`.

## 4. One additional index for m>=4

For m>=2,

`g_(d-1)/lambda=(m+1/2)/2^(m-1)`.

This ratio decreases with m. For m>=4 it is at most 9/16, so

`lambda-g_(d-1)>=(7/16)lambda=(63/64)8^m`.

At m=4 this lower bound is 4032, greater than `(4/3)7^4`; the
ratio to `(4/3)7^m` increases by 8/7 at every subsequent m.
It follows that `lambda-g_(d-1)>mu` for every m>=4.

Using f_(d+1)<=f_d in the exact expansion at n=d gives

`delta_d(H)>=(lambda-g_(d-1))f_d+2f_d g_d+g_d^2`.

The first term exceeds mu f_d. Also f_d>=f_N>mu, so the positive
cross term satisfies `2f_d g_d>mu g_d`. Therefore

`delta_d(H)>mu(f_d+g_d)=mu h_d`.

Together with Section 3, this proves for every m>=4 the stronger
index range

`delta_n(H)>8b0 H(H)[n]`, for `2m+1<=n<=3m+5`.

For m=3 the simpler estimate gives
`lambda-g_(d-1)=1152-1008=144>0`, hence delta_d(H)>0. The
quantitative extension stated and used here starts at m=4; no missing
low-m case is silently included in that assertion.

## 5. Exact scope of the remaining obstacle

The proved strength concerns defects at the displayed upper indices.
It cannot be promoted to a global strong-cone statement without the
remaining lower defects. In particular this note does not establish
K_H TP2 or the required relative inequality for every pair of rows
and columns.

For m>=4 the unproved defect range has been reduced to
`0<=n<=2m`. For m=3, the boundary n=2m+1 is strictly positive, but
its required quantitative strength is not part of the statement above.
The low-index addition problem and the other uniform one-turn block
and proxy obligations remain open. No full-tree or all-m Local TP2
conclusion is claimed.
