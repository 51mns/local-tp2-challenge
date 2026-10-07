# A uniform 5/2 shifted-trace cone and the Robin propagators

Status: the sufficient shifted-trace theorem and all-depth pure propagator conclusion below are proved algebraically, conditional only on the inherited folded-kernel foundations. They do not prove child gap-kernel closure for P_Q. They remove a fixed-trace factor obstruction without assuming positivity of unrelated mixtures.

## 1. Precise sufficient endpoint gate

Let y=x+1, a have a positive integer Fourier half-row A on 0,...,m, and

    t_a=3y²a+2x+3.

Each of the following alternatives suffices to make every t_a-rho, |rho|<=5/2, have a positive initial-interval half-row and strictly positive supported folded defects:

1. m>=2, a is 1-strong, and ya is folded TP2;
2. m=1, H(a)=(A,B), a is optimally B-strong, and B>=2;
3. m=0, a is an integer constant A>=2.

The zero endpoint is excluded. The constant a=1 is also excluded for this enlarged shift range, although it is covered by the earlier [-2,2] lemma. No extra condition has been silently appended to the m>=2 alternative.

The relevant common-center trace in the paired packet is T=3yC-x=t_Z with Z=(C-1)/y. At the canonical root, Z=2x+4 meets alternative 2. Preserving the sufficient Z gate under Z -> Z+s or Z+s+d remains open.

## 2. A cubic consequence of the first two folded defects

For m>=2, the inherited folded criterion gives A0>=A1>=...>=Am>0. Put

    b=A1/A0, u=A2/A0, w=A3/A0,

with A3=0 if m=2. Nonnegativity of the first two folded defects gives

    u>=2b²-1,
    bw>=u+u²-b².

When b>=sqrt(3)/2, the lower bound for u is at least 1/2. The function u+u² is increasing there, hence

    w>=4b³-3b.                                      (1)

This uses no extrapolation from coefficients or finite experiments. When b<sqrt(3)/2, the elementary bound w>=0 suffices.

The positive integer 1-strong hypotheses also force A0>=3. If A0=1 then A1=A2=1 and delta0=0<1. If A0=2 and A1=2, then delta0<=4-8+4=0<2. If A0=2 and A1=1, then A2=1 and A3<=1, so delta1<=1-2-1+1=-1<1. These exhaust A0<3.

## 3. Central shift 5/2

Let v=H(y²a). The audited five-minor Cauchy--Binet bound is

    delta0(v)>=9A0+4A1+4A2+10A3.                    (2)

It follows from the first-two-row minor coefficients 4,2,3,4,2 and
W(i,j)>=A_i+(j-i-1)A_j. The terminal column m+1 is evaluated directly as W(i,m+1)=A_i A_m, so (2) includes m=2. The exact coefficients of v needed here are

    v0=3A0+4A1+2A2,
    v1=2A0+4A1+2A2+A3,
    v2=A0+2A1+3A2+2A3+A4.

Write c=3-rho in [1/2,11/2], and h=H(t_a-rho)=3v+(c,2,0,...). Direct expansion gives

    delta0(h)=9delta0(v)+6cv0-24v1+3cv2+c²-8.

Its derivative in c is 6v0+3v2+2c>0, so c=1/2 is worst. Substituting (2) gives

    delta0(h)>=(87/2)A0-45A1-(3/2)A2
                    +69A3+(3/2)A4-31/4
               >=42A0-45A1+69A3-31/4.               (3)

Here A2<=A0 and A4>=0. For b<=sqrt(3)/2, the last coefficient expression in (3) is at least

    (42-45sqrt(3)/2)A0-31/4.

For b>=sqrt(3)/2, apply (1). The normalized expression becomes

    42-252b+276b³.

Its derivative is 828b²-252>=369>0 on this interval. Its minimum is again 42-45sqrt(3)/2. Since this positive coefficient multiplies A0>=3,

    delta0(h)>=(473-270sqrt(3))/4>0.                 (4)

The last strict inequality is exact: 473²-3*270²=5029>0. This proves the enlarged central shift range; it is not a decimal margin estimate.

## 4. Tail, positive support, and terminal indices

The inherited multiplier-y tail lemma and the assumed full cone of ya give

    delta_n(v)>=v_n  for all n>=1.

The modified second-y proof at n=1 uses only nonnegative delta0(H(ya)), not its 1-strength; the four other first-two-row minor bounds use tail strength. For n>=2 all strong adjacent defects lie at indices >=1. Direct penultimate and terminal formulas handle the last two indices. These details are audited independently in `../common_closure_20261004/network_trace_audit.md`.

Also v is folded TP2 from K_(y²a)=K_a K_(y²), with H(y²)=(3,2,1), so v is decreasing. This invokes y² product closure, not a nonexistent y cone. All v entries are positive on 0,...,m+2 by the positive coefficient map.

The exact remaining trace perturbations are

    delta1(h)=9delta1(v)+12v1-3cv2+6v3+4,
    delta2(h)=9delta2(v)-6v3,
    delta_n(h)=9delta_n(v), n>=3.

For c<=11/2 and v1>=v2,

    delta1(h)>=(9/2)v1+6v3+4>0.

For n=2, delta2(h)>=3v2>0. For every n>=3, including the terminal m+2, delta_n(h)>=9v_n>0. Reflection at zero and zero extension at the upper support are retained. The entire trace half-row is positive because c>=1/2 and v is positive.

## 5. Direct lower-degree alternatives and genuine exception

For a=A>=2, the exact defects of (9A+c,6A+2,3A) are

    delta0=36A²+(21c-48)A+c²-8,
    delta1=(24-3c)A+4,
    delta2=9A².

The central minimum at c=1/2 is increasing for A>=2, and at A=2 is 245/4. The first defect is at least (15/2)A+4; the terminal defect is positive. Thus alternative 3 holds without a smoothing hypothesis.

For degree one, optimal B-strength means A²-2B²>=AB, equivalently A>=2B. The exact central minimum at c=1/2 is

    36A²+18AB-72B²-(75/2)A-81B-31/4
       >=108B²-156B-31/4>=449/4.

The first inequality uses monotonicity in A on A>=2B,B>=2, and the second monotonicity in B>=2. The remaining exact defects are

    delta1=36AB+72B²+(24-3c)A+(54-6c)B+4,
    delta2=9A²+18AB-9B²-6B,
    delta3=9B².

The two c-dependent coefficients stay positive for c<=11/2, and delta2>=63B²-6B>0. This proves alternative 2 directly, without assuming ya folded TP2.

The omitted constant a=1 really fails: at rho=5/2 the trace half-row is (19/2,8,3), with delta0=-37/4. At a=0, even rho=2 has negative central defect. These are endpoint exceptions, not target counterexamples.

## 6. Robin spectral interval and all-depth pure propagators

Let U_n(t/2) be the Chebyshev continuant, U_-1=0,U_0=1,U_1=t,U_(n+1)=tU_n-U_(n-1), and define

    P_(n,rho)(t)=U_n(t/2)-rho U_(n-1)(t/2), n>=1,
    P_(0,rho)=1.

It is the characteristic polynomial of the n-by-n real symmetric path matrix with first diagonal rho, all other diagonals zero, and off-diagonals one. Thus all roots are real.

For |rho|<=1, the absolute row sums are at most two, so every root lies in [-2,2]. For 1<rho<=2, take positive weights w_i=rho^(-(i-1)). For n>=2 the weighted absolute row sums equal rho+1/rho at the first and interior rows, and are at most this number at the terminal row; for n=1 the only row is also bounded by that number. Similarity by diag(w_i) leaves the eigenvalues unchanged; its infinity norm therefore bounds every root in absolute value by rho+1/rho<=5/2. For negative rho, alternating diagonal signs transform the matrix to the negative of the corresponding positive-rho matrix. Hence all roots lie in [-5/2,5/2] uniformly in n and |rho|<=2.

This interval is sharp for all-depth uniform coverage. At rho=2, the same geometric vector has Rayleigh quotient

    5/2 - (1/2)*4^(-(n-1))/sum_(j=0)^(n-1)4^(-j),

which tends to 5/2. The largest eigenvalue is bounded above by 5/2, so it tends to that endpoint. No smaller closed interval covers all n.

It follows from the sufficient trace gate that every P_(n,rho)(t_a) is a folded-TP2 polynomial with positive interval half-row, uniformly for every n>=0 and rho in [-2,2]. Each factor t_a-lambda is a strict positive-support cone factor, so products also have strict supported defects for n>=1 by Cauchy--Binet. This is an infinite propagator theorem, not a bounded root scan.

## 7. Exact consequence for a fixed-trace seed advance

For a seed (c,d0), advancing it k>=1 times by (c,d0)->(tau*c+d0,-c) gives

    c_k=c U_k+d0 U_(k-1),
    d_k=-c U_(k-1)-d0 U_(k-2).

Its actual shifted single block is exactly

    c_k(tau-rho)+d_k
       =c P_(k+1,rho)(tau)+d0 P_(k,rho)(tau).         (5)

Thus the pure propagators in every advanced single block are now cone factors when tau satisfies Section 1. For d0=0 and cone seeds c,yc, all these advanced single blocks and their y multiples are cone products, with strictness if a seed or propagator is strict. For signed or nonzero d0, (5) remains a correlated two-term sum; its mixed compatibility has not been proved. The three-parameter H blocks and direct relative-minor gates also remain open.

This removes the quadratic-root trace-factor obstruction identified in the previous packet note, including its repeated-advance version. It does not claim preservation of the whole packet or actual S/Fout kernel gates. The main sufficient trace gate is a current-state condition independent of the target; ROOT is proved for the common-C trace, SHORT/LONG preservation of its Z hypotheses is open, and the result supplies pure factors only.

No computational evidence is needed for these theorems. `gap_trace_reproducer.py` validates the displayed identities by exact formal polynomial arithmetic, and saves `gap_trace_results.json`. It imports only the frozen network lane's independent symbolic arithmetic; it does not import a shifted-trace theorem or use scans. The proof uses inherited folded-defect equivalence, positive-interval product closure, the audited y-tail lemma, and elementary symmetric-matrix spectral theory.
