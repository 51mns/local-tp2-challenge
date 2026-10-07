# Independent audit: three local center defects imply the multiplier gate

**Verdict: PASS.** `multiplier_local_gate.md` proves the stated general
implication from `K_C TP2`, only `delta_i(C)>=h_i/2` for i=0,1,2, and
`B0(C)>=0`. It supplies K_M and `(M-1)<=lr (x+2)M`; it does not prove
the new center package is preserved at either child.

Audited source SHA-256:
`cca4390068f8b2f7344559b980964eb468a8e541214f3711e63524f28bb96072`.
This is an analytic audit using the frozen folded criterion,
Cauchy--Binet, and elementary two-row minor identities. No finite scan
is used to establish the theorem.

## 1. The only dangerous noncentral index

The five-minor expression for delta_1(yC) is exact. The three displayed
Plucker identities hold for all the stipulated degrees. Since h_1,h_2
are positive, division occurs only inside support. Local half-strength
and monotonicity of h give

`A_02>=(h_0+h_2)/2`, `A_13>=(h_1+h_3)/2`,

`A_03>=h_0(1+2h_3/h_1)/2`.

Adding these and A_01,A_23 gives exactly B/2 from the source. Its
comparison to `(2v_1+v_2+v_3)/3` is the stated exact sum

`5(h_0-h_1)h_1+2(h_1-h_2)h_1+6(h_0-h_1)h_3`

`+3h_1h_3+2h_1(h_3-h_4)`

after multiplication by 6h_1. Every summand is nonnegative because
the parent kernel is TP2. This proves the factor-three lower bound on
delta_1(yC), hence `delta_1(M)>=1` with no remote strength premise.

For deg C=2, h_3=h_4=0. The first-two-row entry of column 3 is h_2,
not zero, and the same Plucker identities retain it. In particular
A_13=h_1 h_2 and A_03=h_0 h_2; the local terminal inequality gives
h_2>=1/2. Thus no low-degree terminal product is lost. Degree three
is likewise covered by zero extension in the same exact formulas.

## 2. Central sign, all tails, and positive support

K_C TP2 gives all ordered first-two-row minors nonnegative. At every
noncentral output index the y convolution has exactly the five
nonnegative terms displayed in the source; therefore
`delta_n(yC)>=0` for n>=1. This is not multiplication-by-y cone
closure at zero.

The local condition also proves `h_1>=1/4`, since
`h_1/2<=delta_1(h)<=2h_1^2`. With deg C>=2, h_2>0, so
`v_1=h_0+h_1+h_2>1/2`. Therefore `M_1=3v_1-1>0`.
This support argument works for real positive coefficients; it does
not rely on an unstated integer premise. Also v_0>=3/4, and

`delta_0(M)=B0(C)+3v_0+6v_1+3v_2-1>0`.

The exact perturbation gives positive delta_2(M) because v_3>0,
nonnegative later defects, and a positive terminal square. Thus all
cases required by the folded-TP2 equivalence are covered.

## 3. Centerbase and scope

`W_0(M-1,(x+2)M)=B0(C)` follows by subtracting the unit row from M
in `W(M,(x+2)M)=delta(M)`. At n>=1 the unit-row correction vanishes,
so the base minor is exactly delta_n(M). The smaller row has positive
initial-interval support; the larger has one extra positive terminal
entry. Adjacent LR signs consequently imply every ordered comparison,
including all support endpoints.

The root package and the root-plus-two strict weakening are correct.
The root-plus-three example has K_M but negative centerbase; the
root-plus-four example is 1-strong but has negative multiplier central
defect. Their nonzero root-endpoint Fricke residuals are classified
correctly. The positive-character weak-pair example with negative
ordinary coefficients is also correctly restricted to that abstract
class. None is an actual canonical target failure.

The new result genuinely reduces the multiplier obligation to one
center cone, three local half-strength inequalities and one central
scalar. Both correlated center mutations must still preserve these
premises. It does not eliminate K_M from the original P_Q without
that extra proved center invariant. The actual gap and strict proxy
remain separate obligations.

## 4. Final central-closure addendum

The final source's two added distinctions are valid. For Croot+2,
delta_0(yC)=-9 and `3v_0+6v_1=183`, so scaling gives exactly
`B0(lambda C)=-81lambda^2+183lambda`. The listed values 102,42,-180
at lambda=1,2,3 are correct. Those three multiples retain the parent
cone and local half-strength, showing the relaxed B0 condition is not
closed under unrestricted positive sums. This remains an abstract
scaling obstruction, not an actual correlated child failure.

For the stronger central condition, the displayed polarization is
also nonnegative under its stated nonnegative-row hypotheses.
Its first three terms equal
`u_0(w_0+w_2)+w_0(u_0+u_2)`; AM--GM and the two central defect
inequalities bound this below by `4u_1w_1`. The argument uses no
division and includes zero central entries. Hence adding C and Fout
preserves delta_0(yC)>=0 conditional on the separate smoothing
condition delta_0(yFout)>=0. Neither K_Fout alone nor arbitrary
full-cone sum closure is asserted. This addendum changes no verdict
or common-preservation status.
