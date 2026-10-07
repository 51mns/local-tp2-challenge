# 任意経路への拡張：今回の確定結果と残る証明義務

**全木の厳密Local TP2は未証明。今回の検討でも、最後の帰納閉包は得られなかった。**

既存の全整数 `m,k>=0` に対する `L^m R^k` の証明は維持される。今回、任意の左右切替にも成立する正の再帰と係数不等式を新たに証明したが、Local TP2の証明済み経路を任意経路へ広げたとは主張しない。

既存の結論を対称性だけで全 `R^m L^k` へ広げてもいない。未解決範囲を「二回以上の方向転換だけ」と限定しない。

基準コミットは `bdc6f58529f39d809e5389456379b9492d4ba12b`。既存の証明は親フォルダの `GENERAL_ONE_TURN_RESULT_JA.md` と `recovery_oneturn_closure.md` にある。このフォルダは追加研究の記録であり、過去の証明を置き換えない。

## 1. 任意の枝で証明できたこと

`y=x+1` とし、次数順の端点を `X,Y`、中心を `C` とする。次の正規化を使う。

```
a=(X-1)/y,  e=(Y-X)/y,  g=(C-Y)/y,
t=2x+3+3y²a,  k=(1+ya)(1+3ya),
g=(t-2)e+k+r.
```

根は `(a,e,r)=(0,1,1)`。次数の小さい子・大きい子への更新は、それぞれ

```
(a,e,r) -> (a,e+g,g),
(a,e,r) -> (a+e,g,e+g).
```

これは引き算のない正確な再帰であり、全深さで次の**通常のx係数ごとの不等式**を与える。

```
0<=a<=e,  0<r<=a+e,  g>=a+e+r+1.
```

Frickeの関係とCassiniの関係も、次の形で保持される。

```
rg=(t-2)e²+2ke+3a(1+ya)²,
e²-(2x+1)a(a+e)-e-2a=(a+e-r)(g+a+e)>=0,
g²-rs=(1+ya)²(1+3a),  s=tg-r.
```

さらに、黄金比による最良の一様係数比較

```
((sqrt(5)-1)/2)e <= r <= ((sqrt(5)+1)/2)e
```

と、全整数 `m>=0` にわたる多項式不等式 `Q_m(t-2)r-P_m(t-2)e>=0` を証明した。後者は有限個の計算からの外挿ではなく、全mを同時に保持する深さに関する帰納法による。

証明本体は [invariants_normalized_state.md](invariants_normalized_state.md) と [network_quotient_constraints.md](network_quotient_constraints.md)。別実装による記号計算と論理監査は [audit_normalized_report.md](audit_normalized_report.md)。

## 2. 成立する補題と、成立しなかった十分条件

| 対象 | 確定した内容 |
|---|---|
| 減算の局所欠損 | `delta(f-g)-lambda(f-g)=B+R`、仮定の下で `R>=0` となる正確な恒等式 |
| 一様シフト | `H(yP)` が `lambda`-strong、`lambda>=4` 等の仮定を満たすなら、全 `u in [-2,2]` で `H(3yP-x-u)` は `3lambda/2`-strong |
| 粗い下界 `B>=0` | **一般には偽**。実際の正準経路 `R^13` の中央で負となる |
| 混合二変数項の一律非負性 | **一般には偽**。実際の正準状態でも負のcharacter係数が現れる |
| 自然な2段行列の成分別TP2 | **成立しない**。根で中央欠損が負の成分が残る |
| skeinの既存正値性定理 | 正確な代数対応は確認したが、必要なFourier小行列式の正値性は導けない |

`R^13` では、粗い下界 `B_0` は負でも、捨てていた正の項 `R_0` を戻した実際の欠損は正である。したがって、これは**Local TP2そのものへの反例ではない**。

これらの証明・反証は `quantitative_subtraction.md`、`quantitative_shifted_trace.md`、`bivariate_mixed_support.md`、`external_skein_bridge.md` に記録した。量的補題の独立監査は [bivariate_audit_quantitative.md](bivariate_audit_quantitative.md)。

## 3. 残る証明義務

元の目標は、`S=ys`、`D=yd`、`d=e(t+1+3y²(e+g))` に対して

```
H(S)_n H(D)_(n+1)-H(S)_(n+1)H(D)_n > 0,
0<=n<=deg S,
H(P)_n=[q^n]P(q+q^-1)
```

を任意経路で示すこと。

今回の係数比較からこの二次不等式を導く証明は得られていない。調べた帰納方針では、実際の正規化多項式の折り畳み核がTP2に保たれること、最後の商のLR比較、そして `y=x+1` の乗算による中央添字の移送が未解決である。これらの一部を仮定した条件付きの伝播は証明したが、その仮定の全木での成立は証明していない。

## 4. 有限検査の正確な範囲

47本の選択した経路で、35,315個のLocal TP2小行列式を厳密整数演算で検査し、全て正だった。最大の `deg D` は4,347。通常多項式による元の再帰との照合は深さ4までの31状態で実施した。詳細と全経路は [falsification_report.md](falsification_report.md) と `falsification_results.json` にある。

別の正規化状態の検査は深さ7まで255状態。量的下界は深さ7では良好だったが、より長い経路 `R^13` で破れた。この事実自体が、有限検査と全深さの証明を分ける必要性を示している。有限検査で反例がないことを全体証明として扱わない。

## 5. 検証と研究状態

状態は、個々の一般補題について研究ブランチ内の **PROVED_INTERNAL**、全木のLocal TP2について **OPEN**。同じ研究セッション内の別担当による監査であり、外部査読・形式証明器での検証・mainでの正式受理を主張しない。既存の文献に対する新規性も主張しない。

`MANIFEST.json` に入力コミット、ファイルのハッシュ、実行コマンドを記録した。実行結果は `VERIFICATION.json`。再実行する場合は、VS Codeのターミナル（Mac/Linux、bashまたはzsh）で親の研究フォルダを開き、例えば次を実行する。

```bash
python3 fulltree_20261004/invariants_normalized_verify.py
python3 fulltree_20261004/network_quotient_constraints.py
python3 fulltree_20261004/audit_normalized_symbolic.py
python3 fulltree_20261004/bivariate_audit_quantitative.py
```

順に、正規化恒等式、多項式障壁、独立の記号監査、量的補題の別実装検証を実行する。これらは一般記号恒等式を確認する検証であり、未証明の全木Local TP2を認定するコマンドではない。
