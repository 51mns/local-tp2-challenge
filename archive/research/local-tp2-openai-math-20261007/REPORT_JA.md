# openai/math を用いた Local TP2 の証明試行

2026-10-07。対象：private `51mns/AIMath`。

## 結論

**任意の正準 word に対する Local TP2 の証明は得られなかった。今回、既存の正例の証明範囲を広げる結果も得られていない。**

公開原稿から最も参考になるのは、Family 169 の「対象を正の初期データから作られるものに厳密に同定し、その後で係数正性を運ぶ」という構成である。実際に量子交換子へ移してみると、元の小行列式を回収する恒等式までは導けた。しかし、必要な有限 character の係数正性は既存の SU(2) Bezoutian で残っていた問題と同じであり、解決には至らない。

Family 114 の Lorentzian 多項式、Family 231 の Strongly Rayleigh 分布についても、具体的な生成多項式を作って適用条件を確認した。単純な候補は正準 root で条件に反するか、全木共通の非実零点によって成立しない。この記録には、それらの限定した障害の証明、元の目標との正確な対応、Python による整数・有理数検算を収録する。

以下の反例はすべて**提案した移植方法に対する反例**である。正準 Local TP2 の反例ではない。限定した補題と恒等式をこの研究記録内の `PROOF_CANDIDATE` とし、全体の主張を昇格させない。新規性も未評価。

## 1. 調査した範囲と既存の証明状況

外部資料は `openai/math` の commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a` に固定した。README、全体の `overview.tex` と `CONTENTS.md` を読み、total positivity、Lorentzian、Rayleigh、実根性、量子交換、cluster、determinant などを横断検索した。そのうえで次の四系統の本文を調べた。全722原稿を個別に査読したわけではない。

| 原稿 | 注目した手法 | 今回の適用結果 |
|---|---|---|
| Family 169, *Elementary positivity of chromatic quasisymmetric functions* | 正の量子再順序化、wall の係数再帰、theta section との同定 | 小行列式との恒等式は構成できたが、正の初期データの同定が未解決 |
| Family 114, *Approximate counting of common bases of two matroids* | Lorentzian 二次微分の Hessian から係数積を比較 | 半行の通常斉次化は root で必要条件に反する |
| Family 231, *The free uniform spanning forest is a factor of IID* | Strongly Rayleigh、外場応答、木モデルの負の共分散 | そのままの総個数分布表現は全木で不可能。符号付き統計量にも追加条件が必要 |
| Family 180, *Paired states and Hamiltonian cycles in cubic bipartite planar graphs* | 対状態上の符号反転 involution と先頭項の正性 | 各 Fourier 添字に対応する重み保存写像は未構成 |

原稿の節・命題・固定URLは [source_review.md](source_review.md)、Git blob SHA は [sources.json](sources.json) に記録した。原稿集合の検証段階は一様ではなく、掲載だけで転用の前提や結論が保証されるわけではない。

private 側は accepted main `c8e61e0e398f540bc8c5de79663398d689f37473` と、最新の研究 commit `a36fbac460073bf757434f122e721dfa254e8e48` を区別した。後者の既存研究には、次の内部証明がある。

- 全ての \(L^mR^k\)、\(m,k\ge0\)：[GENERAL_ONE_TURN_RESULT_JA.md](../local-tp2-coefficient-geometry-20261003/GENERAL_ONE_TURN_RESULT_JA.md)。
- 全ての \(L^mRL^\ell\)、\(m,\ell\ge0\)：[second_turn_20261004/RESULT_JA.md](../local-tp2-coefficient-geometry-20261003/second_turn_20261004/RESULT_JA.md)。

これらは既存の `PROVED_INTERNAL` 記録であり、今回の成果ではない。一般の \(L^mR^kL^\ell\)（\(k>1,\ell>0\)）や任意 word への閉包は未証明。表面上古い README の族数だけを最新状況として扱わず、上記の成果本文を基準とした。

## 2. 固定した Local TP2 の定義

根を

\[
(A,C,B)=(1,\,2x^2+6x+5,\,x+2)
\]

とする。二つの変異は

\[
L=3(x+1)AC-x(A+C)-B,
\qquad
R=3(x+1)CB-x(C+B)-A.
\]

次の状態は左が \((A,L,C)\)、右が \((C,R,B)\)。二つの子を次数順に \(U,V\) と置き、

\[
S=U-C,\qquad D=V-U
\]

とする。多項式 \(P\) の半行を

\[
H(P)_n=[q^n]P(q+q^{-1})
\]

で定義し、次数外は0とする。目標は

\[
F_n=s_nd_{n+1}-s_{n+1}d_n>0,
\quad s_n=H(S)_n,\quad d_n=H(D)_n,
\quad 0\le n\le\deg S.
\]

端点 \(n=\deg S\) も含む。比に割り算して次数外を処理しない。

根の再帰を独立に再構成すると

\[
S=4(x+1)^2(x+2),\qquad
D=2(x+1)(x+2)\bigl(3(x+1)^2+1\bigr),
\]

\[
s=(40,32,16,4),\qquad d=(164,138,80,30,6),
\]

\[
(F_0,F_1,F_2,F_3)=(272,352,160,24).
\]

既存の全木の通常係数正性は、この Fourier 小行列式の正性とは別の主張である。

## 3. 量子交換の手法を当てはめる

Family 169 の方法を使うなら、\(S,D\) それぞれの正性では足りず、差 \(s_id_j-s_jd_i\) 自体を正の構成に対応させる必要がある。量子変数を Fourier 変数 \(q\) と区別して \(v\) とし、

\[
X_{(a,b)}X_{(c,d)}=v^{ad-bc}X_{(a+c,b+d)}
\]

という centered quantum torus で実際に試した。

### 3.1 軸上へ配置する候補

\(S_A=\sum s_iX_{(i,0)}\)、\(S_B=\sum s_iX_{(0,i)}\) とし、\(D\) も同様に定義する。

順番を反転する \(Q=S_AD_B-S_BD_A\) は

\[
[X_{(i,j)}]Q=s_id_jv^{ij}-s_jd_iv^{-ij}.
\]

根の \((i,j)=(1,2)\) では

\[
2560v^2-2208v^{-2}
\]

となる。\(v=1\) で元の正値352に戻るが、量子 Laurent 係数には負の項がある。第二積に固定の \(v^\kappa\) を掛ける修正も、\((1,2)\) は \(\kappa=4\)、\((2,3)\) は \(\kappa=12\) を要求するため同時にはできない。

一方、同じ積順序にした \(Q'=S_AD_B-D_AS_B\) は

\[
[X_{(i,j)}]Q'=v^{ij}W_{ij},\qquad W_{ij}=s_id_j-s_jd_i.
\]

上三角部分 \(i<j\) では目標の言い換えになる。しかし、その係数が正の wall 構成から生まれることを別に示さなければ循環である。また反対側の係数は逆符号で、根の \((1,0)\) は \(-272\)。多項式全体の係数正性を主張することはできない。

### 3.2 真の交換子から得た恒等式

次に

\[
A_v=\sum_i s_iX_{(i,1)},\qquad B_v=\sum_i d_iX_{(i,1)}
\]

とすると、任意の有限係数列について

\[
\boxed{\frac{B_vA_v-A_vB_v}{v-v^{-1}}
=\sum_{i<j}W_{ij}[j-i]_vX_{(i+j,2)}}
\]

が成り立つ。\([r]_v=(v^r-v^{-r})/(v-v^{-1})\)。証明は \(i<j\) と \(j<i\) の二項をまとめるだけで、対角項は消える。係数の正性はこの恒等式の仮定ではない。

右辺の \(X_{(N,2)}\) の係数を \(C_N(v)\) と置く。奇数長の量子整数 \([2r+1]_v\) は定数項を1個持ち、\(v^2\) の項を持つのは \(r\ge1\) のときだけなので、

\[
\boxed{F_n=[v^0]C_{2n+1}(v)-[v^2]C_{2n+1}(v)}.
\]

根では

\[
C_3(v)=544v^2+896+544v^{-2},\qquad F_1=896-544=352.
\]

ここまでは正確な代数的対応である。残るのは中央係数が外側より厳密に大きいこと。単なる Laurent 係数非負性では、例えば \(v^2+v^{-2}\) が反例になる。有限量子整数の非負の重複度を独立に得るか、中央差そのものの正の再帰が必要である。

さらに \(\Omega((i,1),(j,1))=i-j\) で、\(S,D\) の支持が重なるため、二つの和の間の pairing は正負両方を持つ。Family 169 の正しい ray 順序の仮定も、そのまま満たす二つのまとまりにはならない。原稿中の無限 Weyl string を、ここで必要な有限 SU(2) character と同一視することもできない。

この対応は既存 [recovery_fulltree_bivariate_character.md](../local-tp2-coefficient-geometry-20261003/recovery_fulltree_bivariate_character.md) の問題を量子交換子で表したもので、正例族を増やす定理ではない。詳細：[quantum_applicability.md](quantum_applicability.md)。

## 4. Lorentzian 多項式による直接証明を試す

Family 114 の二次 Hessian の符号条件を使うため、根の半行を通常通り斉次化すると

\[
f(u,v)=40v^3+32uv^2+16u^2v+4u^3.
\]

ところが

\[
\operatorname{Hess}(\partial_vf)=
\begin{pmatrix}32&64\\64&240\end{pmatrix},\qquad
\det=3584>0.
\]

先頭主座小行列式も32で正なので正定値である。正の固有値が二つあり、Lorentzian 多項式に必要な「二次微分の Hessian の正の固有値は高々一つ」という条件を満たさない。

元の \(S=4(x+1)^2(x+2)\) は実負根しか持たない。それでも \(q+q^{-1}\) 変換後の半行を通常斉次化すると条件が壊れる。したがって、元の実根性からこの外部定理を適用する証明は成立しない。階乗正規化や別の多変数モデルまで否定する結果ではない。詳細：[lorentzian_obstruction.md](lorentzian_obstruction.md)。

## 5. Strongly Rayleigh による証明を試す

### 5.1 全 word で成り立つ障害

これは有限走査ではなく帰納法で証明できる。

根では \(A(-1)=C(-1)=B(-1)=1\)。親でこれが成り立つと、\(x=-1\) で変異の積の項は消え、

\[
L(-1)=A(-1)+C(-1)-B(-1)=1
\]

となり、右も同じ。よって全ての正準状態で三多項式の値は1で、差 \(S,D\) は必ず \(x+1\) で割れる。

非零 \(P=S,D\)、\(d=\deg P\)、\(P=(x+1)T\) とすると

\[
\boxed{q^dP(q+q^{-1})=(q^2+q+1)q^{d-1}T(q+q^{-1})}.
\]

右辺は通常の多項式で、必ず非実根 \(e^{2\pi i/3}\) を持つ。

Strongly Rayleigh 分布の実安定な生成多項式 \(g(z_1,\dots,z_N)\) から、総選択数の生成多項式を作ると \(g(q,\dots,q)\) になる。上半平面の \(q\) に代入しても零にならないため、実係数なら根は全て実数でなければならない。上の非実根と矛盾する。

従って、**全 Fourier 行を、そのまま Strongly Rayleigh 分布の総選択数として表す方法は、全正準 word で不可能**。正の定数による確率正規化や決定的な整数シフトでも非実根は消えない。別の符号付き統計量や補助状態全般の不可能性を意味しない。

半行のみにしても根で Newton の必要条件

\[
32^2\ge3\cdot40\cdot16
\]

に反し、差は \(-896\)。なお実際の絶対値分布では正の添字の重みを2倍する。こちらは \((40,64,32,8)\) で、別の添字の Newton 条件に反する。二つを混同しない。

### 5.2 符号付き統計量なら自動的に解決するか

\[
g_m=3^{-m}\prod_{i=1}^{m}(1+u_i+v_i)
\]

は多重アフィンかつ実安定で、明示的な Strongly Rayleigh 分布である。各因子の虚部が上半平面で正であることから直接分かる。

符号付き和 \(T_m=\sum(U_i-V_i)\) の生成関数は \(3^{-m}(1+q+q^{-1})^m\)。\(m=3,4\) の非正規化半行は

\[
(7,6,3,1),\qquad(19,16,10,4,1),
\]

中央 minor は \(7\cdot16-6\cdot19=-2\) となる。絶対値の確率分布へ直しても \(-4/2187<0\)。従って Strongly Rayleigh 性に、独立な同種 block の追加を組み合わせても、符号付き和の折り畳み TP2 は自動的に出ない。これは正準 \(S,D\) の例ではない。

### 5.3 元の目標と同値な二変数モデル

非負係数の多重アフィン多項式

\[
G_n(z,w)=s_{n+1}+s_nz+d_{n+1}w+d_nzw
\]

を考えると、

\[
G_n\text{ が実安定}\quad\Longleftrightarrow\quad F_n\ge0.
\]

正の外場 \(z,w\) では

\[
\operatorname{Cov}(Z,W)=-\frac{zwF_n}{G_n(z,w)^2}.
\]

つまり負の共分散として目標を表すことはできる。ただし \(G_n\) の実安定性を直接仮定すれば元の不等式を仮定している。成功には、左右の変異を保つ共通の安定／木モデルを先に構成し、その二座標の重みがこの四係数に一致すると証明する必要がある。また非正共分散だけでは厳密な \(F_n>0\) は出ないので、等号を除く根拠も必要。この構成は得られなかった。詳細：[rayleigh_transfer_audit.md](rayleigh_transfer_audit.md)。

## 6. 何が未解決か

参考にする優先度は Family 169 の構成を最上位とする。ただし次の具体物がない段階で「外部の正性定理から従う」としてはいけない。

1. 正準状態と左右変異から、\(S,D\) の二つのコピーに関する正の状態空間を作る。
2. 重みが元の \(W_{ij}\) または \(F_n\) と一致することを、未証明の TP2 を使わずに示す。
3. 有限 character の重複度、各添字の相殺後の残り、または中央係数差の正の再帰を得る。
4. 根から全ての左右変異に対する保存と、端点を含む厳密な正値性を証明する。

Family 180 の対状態の involution は2〜3の設計例にはなるが、その先頭 Taylor 項の非零性を各 Fourier 添字の正性へ読み替えることはできない。現時点ではこの対応写像も構成できていない。

この調査では、欠けた構成の代わりに木を深く走査したり、既存の無限族を新規成果として再計上したりはしていない。

## 7. 再現と監査

著者実装は整数・有理数で根、Hessian、Newton 条件、量子積、明示的 Strongly Rayleigh の反例を計算する。量子恒等式は符号付き短列729組でも検算したが、一般性の根拠は上記の代数証明にある。

独立担当は著者コードや expected JSON を import せず、根を Laurent 多項式の直接畳み込みで再構成した。これは同一セッション内の独立実装・数学監査であり、blind review、外部査読、Lean 証明、canonical な独立再現状態への昇格ではない。監査本文：[AUDIT_JA.md](AUDIT_JA.md)。

**Mac の VS Code 内蔵ターミナルで、この研究フォルダを開いてから実行する：**

```bash
python3 reproduce.py
```

標準 Python だけで3本の検証スクリプトを実行し、終了コード・出力・固定ファイルの SHA-256 を確認する。実行結果は `replay_results.json` と `replay_logs/` に保存される。計算結果の JSON は再生成される。参照元の固定 commit と blob SHA は `sources.json` に収録した。

今回の保存先は新しい研究ブランチ `research/local-tp2-openai-math-20261007`。全 Local TP2 の証明状況は **OPEN** のままである。
