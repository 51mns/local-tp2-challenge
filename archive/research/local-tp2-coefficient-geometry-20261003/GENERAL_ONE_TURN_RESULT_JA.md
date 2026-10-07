# Local TP2：任意の初期左連続長 L^m R^k の証明

**結果：すべての整数 m,k≥0 について、経路 L^m R^k 上の厳密Local TP2を証明した。**

LとRは正準木の左右の移動を表す。従来の固定された初期左連続長m=1,2から、任意のmへ拡張した。任意のR^mL^kまで対称性だけで拡張したとは主張しない。

**木全体のLocal TP2は未証明。** L^mR^kL^ℓなど、さらに向きを切り替える一般経路は今回の結論に含まれない。

状態：**PROVED_INTERNAL**（研究ブランチ内）。同一研究セッション内の別担当による数学的監査・別実装での検証を実施した。外部研究者の査読、形式証明器での検証、mainでの正式受理、文献上の新規性を主張しない。

## 元の不等式

次数の小さい子をU、大きい子をV、親をCとし、S=U−C、D=V−Uと置く。
H(P)_n=[q^n]P(q+q⁻¹)に対して、

H(S)_n H(D)_(n+1) − H(S)_(n+1) H(D)_n > 0

が、L^mR^k上の全状態で、0≤n≤deg Sのすべてについて成立する。

## 今回閉じた部分

1. m=1..390の中点核とその平滑化を、独立パラメーター立方体[-2,2]³全域で厳密Bernstein検証。780件・12,488,580個の係数が厳密正で、主実装と別実装の全結果・ハッシュが一致。
2. m≥391は正規化した欠損の下界と摂動評価による解析的証明。有限例からの外挿ではない。
3. 単一核・平滑化核の783ケースと925,524個の係数、8種類の剰余因子の連続領域証明書を独立再計算した。
4. Jacobi表示の混合小行列式を制御して、外側の全段数kへ伝播。小さい段数・支持末端を含む。
5. 中央欠損の質量評価と最終比較を接続。有限側389件の記録を別実装で完全再構成し、無限側の解析も監査した。

証明本体は [recovery_oneturn_closure.md](recovery_oneturn_closure.md)。依存する従来補題と証明書の対応表も同文書の末尾にある。

## 完了した監査

- [recovery_oneturn_closure_audit.md](recovery_oneturn_closure_audit.md)：新しい解析・論理接続全体。
- [recovery_finite_audit.md](recovery_finite_audit.md)：通常・平滑化の中点核、全有限範囲と連続パラメーター。
- [recovery_single_audit.md](recovery_single_audit.md)：単一核・剰余因子・平滑化したtraceの評価。
- [recovery_mass_proxy_audit.md](recovery_mass_proxy_audit.md)：質量下界、乗数、最後の厳密比較。

これらは全てPASS。未完了として記載されていた旧資料は途中段階の履歴であり、この証明本体と最終監査が今回のL^mR^kの状態を示す。

## 再実行

実行場所は、VS Codeのターミナル（Mac/Linux、bashまたはzsh）でこの研究フォルダを開いた場所。

```bash
python3 recovery_oneturn_checks.py
python3 recovery_single_audit.py
python3 recovery_mass_proxy_audit.py
```

順に、恒等式・解析的閾値・保存結果の一致、単一核と因子の独立再計算、質量と最終比較の独立再計算を行う。
中点核の全再計算用コマンドと依存環境はRECOVERY_MANIFEST.jsonに記録した。独立中点核の再計算にはNumPyが必要。

## 次の再開地点

今回の一方向の固定境界を離れ、L^mR^kL^ℓや任意の左右切替で必要な同時不等式を保つ構造が未解決。
全木の恒等式はfulltree_direct_exchange.md、fulltree_minor_reduction.md等。
recovery_fulltree_bivariate_character.mdは二変数表示の恒等式・部分的な構造を記録する。recovery_fulltree_shift_obstruction.mdは単一の平行移動した冪基底による安易な証明方針を排除するもので、Local TP2の反例ではない。

次回はこの証明済み範囲をやり直さず、全木の未解決条件から再開できる。
