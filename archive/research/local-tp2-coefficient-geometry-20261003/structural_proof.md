# Structural route: exact Fricke specialization and left-ray formula

Status: exact algebraic reductions; **not a proof of Local TP2**. Source recurrence is frozen at AIMath commit `c8e61e0e398f540bc8c5de79663398d689f37473`.

## 1. Affine trace coordinates

Write `k=3(x+1)`, `t=x(x+2)`, and `T(P)=kP-x`. For an update

`L=kAC-x(A+C)-B`,

direct expansion gives

`T(L)=T(A)T(C)-T(B)-t`.

Consequently, with `a=T(A), b=T(B), c=T(C)`, either Farey mutation is a Vieta involution for

`I(a,b,c)=a²+b²+c²-abc+t(a+b+c)`.

For example, replacing `b` by `b'=ac-b-t` preserves `I`, because

`I(a,b',c)-I(a,b,c)=(b'-b)(b'+b-ac+t)=0`.

At the initial state,

`a=2x+3`,

`b=3x²+8x+6`,

`c=6x³+24x²+32x+15`,

and direct substitution gives

`I=-x²(2x+3)`.

This proves the identity at every state, without a finite-depth inference.

## 2. Exact four-holed-sphere identification, including signs

The standard SL(2,C) relative character variety of a four-holed sphere with boundary traces `u,v,w,d` has pair traces `X,Y,Z` satisfying

`X²+Y²+Z²+XYZ-(uv+wd)X-(vw+ud)Y-(uw+vd)Z+u²+v²+w²+d²+uvwd-4=0`.

Primary reference: Maloni, Palesi, Tan, *On the character variety of the four-holed sphere*, Groups Geom. Dyn. 9 (2015), 737–782, DOI `10.4171/GGD/326`, equation (2), printed page 741; also section 2.3, printed page 744.

Official PDF: https://ems.press/content/serial-article-files/29746

Set

`s²=x+2`, `u=v=w=s`, `d=(x-1)s=s³-3s`.

Each linear coefficient is

`s²+sd=(x+2)+(x-1)(x+2)=x(x+2)=t`.

The constant is exactly

`3s²+d²+s³d-4`

`=3(x+2)+(x-1)²(x+2)+(x-1)(x+2)²-4`

`=x²(2x+3)`.

Now set **`X=-a, Y=-b, Z=-c`**. Then the Fricke equation is precisely

`a²+b²+c²-abc+t(a+b+c)+x²(2x+3)=0`.

The minus signs are essential. The usual Vieta update of `X` is `t-YZ-X`; under `X=-a`, this becomes the update `a'=bc-a-t` already derived.

Under the Fourier specialization `x=q+q^{-1}`, pass to `r=q^{1/2}` and choose

`s=r+r^{-1}`,

`d=s³-3s=r³+r^{-3}`.

Thus the four boundary trace eigenvalue pairs are algebraically compatible with `r,r,r,r³` and their reciprocals. This is an exact identity over the Laurent extension in `r`; it is not an assertion that one has already constructed positive matrix entries, a Fuchsian representation, a planar network, or a coefficientwise positive skein expression. For each complex specialization, the standard character-variety theorem supplies a character point; a simultaneous Laurent-polynomial matrix realization would be an additional result.

The reduction exposes an established trace/Markoff-map framework. It does not imply Local TP2: positivity of individual trace polynomials or scalar geometric lengths does not give positivity of the determinants of adjacent Fourier coefficients.

## 3. Boundary-gap factorization

Orient the two boundary polynomials by degree as `P` (lower) and `Q` (higher), and write `H=Q-P` and `y=x+1`. Then the lower and higher children are

`U=3yPC-x(P+C)-Q`,

`V=3yQC-x(Q+C)-P`.

Subtracting gives the exact factorizations

`D=V-U=H(3yC-y+2)`,

`S=U-C=y[(3P-1)C-P]-H`.

## 4. Exact formula for every all-left state

Let `g_0=x+2`, `g_1=2x²+6x+5`, and

`g_{n+1}=(2x+3)g_n-g_{n-1}-x`.

The state at path `L^k` is `(1,g_{k+1},g_k)`.

Write `y=x+1`, `z=2x+3=2y+1`; let `U_j` denote the second-kind Chebyshev polynomial evaluated at `z/2`, so `U_0=1`, `U_1=z`, `U_{j+1}=zU_j-U_{j-1}`. Define `T_n=Σ_{j=0}^n U_j`.

Then for every `n>=0`,

`g_n=1+yT_n`.

Proof: the displayed expression has the two required initial values. The elementary identity `T_{n+1}=zT_n-T_{n-1}+1` yields

`1+yT_{n+1}=z(1+yT_n)-(1+yT_{n-1})-x`,

since `z-2-x=y`.

Therefore, at `L^k`,

`S=yU_{k+2}`,

`D=yT_k[2+2y+3y²T_{k+1}]`.

This is an infinite-family reduction with an elementary proof. Local TP2 on this family remains the explicit inequality between the Fourier coefficients of those two expressions.

## 5. A precise obstruction to a tempting closure argument

Let `K(m,n)=H((x+1)U_m(x+3/2))[n]`. Its bivariate generating function is

`Σ_{m>=0}(x+1)U_m(x+3/2)t^m=(x+1)/(1-(2x+3)t+t²)`.

The unrestricted claim that `K` is TP2 in `m,n` is false:

`H((x+1)U_0)=(1,1)`,

`H((x+1)U_1)=(7,5,2)`,

so the minor for `m=0,1` and `n=0,1` is `5*1-7*1=-2`.

An exact Python check found no such failure for consecutive `m=1,...,68`, all supported `n`; this is only diagnostic evidence for the modified `m>=1` statement, which has not been proved. Even that statement would not directly prove the ray claim, because the Chebyshev expansion of `D` includes degrees below `k+2`.

The remaining task is a coefficient inequality, such as a valid positive planar/skein model for the exterior difference, or an independently proved sufficiently strong Fourier-coefficient ordering theorem. Neither scalar trace positivity nor the closed Chebyshev formula closes this gap.
