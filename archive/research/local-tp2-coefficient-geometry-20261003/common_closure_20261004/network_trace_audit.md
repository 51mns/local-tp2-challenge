# Independent audit of the shifted-trace lemma

Verdict: the intended degree-at-least-two theorem in `invariant_shifted_trace_lemma.md` is valid from the stated folded-kernel foundations. The separately qualified constant and degree-one cases are also valid. The qualification cannot be removed: a=x+2 is an exact abstract counterexample. The lemma supplies shifted trace kernels; it does not prove preservation under a -> a+e or the common target.

This audit is an analytic proof audit, including all support cases. `network_trace_audit.py` supplies independent formal polynomial coefficient checks, without parent arithmetic imports or scans. Those checks validate algebra, not the inequalities or an infinite induction.

## Central Cauchy--Binet coefficients and strength bound

Let A=(A0,...,Am) be a positive integer initial-interval half-row, m>=2, with delta_n(A)>=A_n. The folded-kernel criterion makes K_a TP2 and A decreasing. For y² the half-row is (3,2,1), with defects (4,0,1), so its kernel is TP2. Its first two columns on rows 0,...,3 are exactly

| intermediate row | column 0 | column 1 |
|---|---:|---:|
| 0 | 3 | 2 |
| 1 | 4 | 4 |
| 2 | 2 | 2 |
| 3 | 0 | 1 |

All later rows vanish in these two columns. The ordered minors are 4,2,3,0,4,2 on pairs 01,02,03,12,13,23. Thus the manuscript's five coefficients 4,2,3,4,2 are exact, with the 12 term absent because it is zero. This retains the central factor-two convention.

Write W(i,j) for the first-two-row minor of K_a. On positive columns i<j<=m, put b_k=K_a(1,k). Since W(k,k+1)=delta_k(A), the exact telescoping identity is

    W(i,j)=A_i A_j sum_(k=i)^(j-1) delta_k(A)/(A_k A_(k+1)).

Every denominator is positive. The last summand is at least A_i; each preceding summand is at least A_j because A_i>=A_(k+1). Therefore

    W(i,j)>=A_i+(j-i-1)A_j.

At j=m+1 one must not use a ratio with A_(m+1)=0. The direct terminal identity instead gives W(i,m+1)=A_i A_m>=A_i, because A_m is a positive integer. The same displayed lower bound then holds with A_(m+1)=0. In particular all terms used in the central expansion are covered when m=2.

Combining the five terms yields exactly

    delta_0(v)>=9A0+4A1+4A2+10A3,  v=H(y²a).

When m=2, A3=0 and the 03,13,23 terms use the direct terminal identity. No terminal strength term is lost.

## Second smoothing and all tail indices

Put u=H(ya), of degree M=m+1>=3. The inherited multiplier-y tail lemma supplies delta_n(u)>=u_n for n>=1. The separate hypothesis that ya is folded TP2 supplies nonnegative first-two-row minors, including delta_0(u)>=0. It does not supply central 1-strength, and none is used here.

For v=H(y²a), the exact five-minor formula at n>=1 is

    delta_n(v)=W_u(n-1,n)+W_u(n-1,n+1)+W_u(n-1,n+2)
                 +W_u(n,n+2)+W_u(n+1,n+2).

For 2<=n<=M-1, all adjacent strong defects needed to lower-bound these terms have index at least 1. The manuscript's inherited proof consequently gives delta_n(v)>=3u_(n-1)+u_n+u_(n+1)>=v_n. At n=M-1, any zero column M+1 is handled by W_u(i,M+1)=u_i u_M>=u_i.

At n=M, the exact expression is delta_(M-1)(u)+u_(M-1)u_M, at least u_(M-1)+u_M=v_M. At n=M+1, the terminal defect is u_M²>=u_M=v_(M+1). Positive integrality supplies the product bounds at both boundaries.

At n=1, the first term W_u(0,1) is merely nonnegative. The other four bounds are W_u(0,2)>=u0, W_u(0,3)>=u0, W_u(1,3)>=u1, and W_u(2,3)>=u2. They follow by the exact three-column minor identity and the strong adjacent defects at indices 1 and 2. Since M>=3, these columns are in support; the terminal direct identity also covers any equivalent boundary argument. Hence

    delta_1(v)>=2u0+u1+u2=v1+u0>=v1.

This verifies the modified tail proof without introducing an unjustified central strength premise. All v entries are positive on 0,...,m+2: multiplication by y twice has entrywise nonnegative folded coefficient maps. Moreover v is folded TP2 from K_(y²a)=K_a K_(y²), so v is decreasing. This use of y² is valid; it does not presume TP2 of K_y.

## Every shifted trace defect

Let c=3-rho in [1,5] and h=H(t_a-rho)=3v+(c,2,0,...). Direct expansion gives

    delta_0(h)=9delta_0(v)+6cv0-24v1+3cv2+c²-8,
    delta_1(h)=9delta_1(v)+12v1-3cv2+6v3+4,
    delta_2(h)=9delta_2(v)-6v3,
    delta_n(h)=9delta_n(v), n>=3.

The central expression increases with c, so c=1 is worst. The exact linear identity

    8v1-2v0-v2=9A0+22A1+9A2+6A3-A4

and the audited central lower bound give

    delta_0(h)>=3(18A0-10A1+3A2+24A3+A4)-7
               >=24A0-7>0.

At n=1 the worst c is 5; tail strength and v1>=v2 give delta_1(h)>=21v1-15v2+6v3+4>0. At n=2, tail strength and v2>=v3 give delta_2(h)>=3v2>0. Every n>=3, including the terminal index m+2, has delta_n(h)>=9v_n>0. Zero extension covers the top two indices automatically. The trace half-row remains positive on its full degree interval because c>=1 and v is positive. Thus the strict folded-defect conclusion holds uniformly for the entire real shift interval.

## Degree zero, degree one, and the zero endpoint

For a=A>=1, the trace half-row is (9A+c,6A+2,3A). Its exact defects are

    delta_0=36A²+(21c-48)A+c²-8,
    delta_1=(24-3c)A+4,
    delta_2=9A².

The minima give 36A²-27A-7>=2, 9A+4, and 9A². This is a direct exception proof; ya need not be TP2 in this degree.

For a of degree one, H(a)=(A,B), optimal B-strength gives A²-2B²>=AB, hence A>=2B. With B>=2, the exact central minimum is

    36A²+18AB-72B²-27A-66B-7
      >=108B²-120B-7>=185.

The first inequality holds because the polynomial is increasing in A on A>=2B. The other exact defects are

    delta_1=36AB+72B²+(24-3c)A+(54-6c)B+4,
    delta_2=9A²+18AB-9B²-6B,
    delta_3=9B².

The first is at least 36AB+72B²+9A+24B+4. The second is at least 63B²-6B. Both and the terminal defect are strictly positive. No smoothing-cone assumption is needed for this separate direct case.

The actual canonical degree-one normalized endpoint is a=2x+4. The root has (a,e)=(0,1); its first short and long children have (0,z+1) and (1,z). Their g has degree at least two because g contains (t-2)e and t-2 has degree at least one. Every subsequent changed e is g or e+g and therefore has degree at least two. Only a long move changes a, by a+e. Thus the only way to obtain degree-one a is the second long mutation from either first-level state, producing z+1=2x+4; later short moves can retain it. This justifies the canonical low-degree identification.

For the abstract a=x+2, H(a)=(2,1) is 1-strong and H(ya)=(4,3,1) has defects (2,4,1). Yet H(t_a-2)=(31,26,12,3) has central defect -19. It is noncanonical by the preceding low-degree argument. Noncanonicity alone should not be presented as a separate proof that no abstract (e,r) completion can satisfy Fricke and ordinary bounds; no such no-completion theorem is needed here.

Finally a=0 gives t_a-2=2x+1 with central defect -7. It must remain a separate boundary clause. The manuscript does not claim that this clause supplies the shifted kernels.

## Scope and reproduction

The intended sufficient gate is sound: zero boundary; positive integer constant; qualified degree-one endpoint; or degree>=2 endpoint with 1-strength and ya folded TP2. The short mutation retains a and therefore retains this gate. The long mutation a -> a+e remains open; neither this proof nor product closure yields sum closure. Other packet and strict proxy conditions remain separate.

Run `python network_trace_audit.py` for independent formal coefficient identities and the exact abstract exception. Output is `network_trace_audit_results.json`. All original frozen network files remain unchanged.
