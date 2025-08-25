---
title: ウェブパフォーマンス指標（Web Vitals）
description: ウェブパフォーマンス指標（Web Vitals）とLighthouseの測定・評価基準をまとめ、各パフォーマンス指標が何を意味するのかを理解する。
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## ウェブパフォーマンスを決定する要素
ウェブパフォーマンス最適化時に考慮すべきウェブパフォーマンスを決定する要素は、大きくローディングパフォーマンス、レンダリングパフォーマンスの2つに分類できる。

### HTMLローディングパフォーマンス
- ネットワークを通じてサーバーに最初にウェブページを要求した後、HTML文書を受け取ってブラウザがレンダリングを開始するまでの時間
- どれだけ早くページが表示され始めるかを決定
- リダイレクトの最小化、HTML応答キャッシング、リソース圧縮、適切なCDN活用などの方法で最適化

### レンダリングパフォーマンス
- ブラウザがユーザーが見る画面を描画し、インタラクション可能にするのにかかる時間
- どれだけスムーズで高速に画面が描画されるかを決定
- 不要なCSSおよびJSの削除、フォントおよびサムネイルの遅延ローディング防止、重い演算は別のWeb Workerに分離してメインスレッドの占有を最小化、アニメーション最適化などの方法で最適化

## ウェブパフォーマンス指標（Web Vitals）
Googleの[web.dev](https://web.dev/performance?hl={{ site.active_lang }})と[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})を基準に記述する。特別な理由がない限り、どれか一つのパフォーマンス指標にのみ集中するよりは全体的な改善を目標とするのが良く、最適化したいウェブページでどの部分がパフォーマンスのボトルネックとなっているかを把握することが重要である。また、実際のユーザーデータ統計がある場合、上位や平均に該当する値よりはQ1程度の下位値に注目して、その場合でも目標基準を達成するかを確認し改善するのが良い。

### 主要ウェブパフォーマンス指標（Core Web Vitals）
後ほど扱うが、ウェブパフォーマンス指標（Web Vitals）には様々なものがある。しかし、その中でも特にユーザーエクスペリエンスに密接に関連し、模擬環境ではなく実際の環境で測定可能な次の3つの指標をGoogleでは特に重要視しており、これを[主要ウェブパフォーマンス指標（Core Web Vitals）](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)と呼ぶ。Googleは自社検索エンジンの検索結果順序にも対象サイトの主要ウェブパフォーマンス指標を反映するため、サイト運営者の立場でもこれらの指標は検索エンジン最適化（SEO）の観点から注意深く見る必要がある。
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): *ローディングパフォーマンス*を反映、2.5秒以内である必要がある
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): *応答性*を反映、200ms以下である必要がある
- [Cummulative Layout Shift (CLS)](#cls-cumulative-layout-shift): *視覚的安定性*を反映、0.1以下に維持する必要がある

主要ウェブパフォーマンス指標は基本的に実際の環境で測定するためのものだが、INPを除く残りの2つはChrome開発者ツールやLighthouseのような模擬環境でも測定できる。INPの場合は実際のユーザー入力が与えられなければ測定不可能なため模擬環境では測定できないが、この場合[TBT](#tbt-total-blocking-time)がINPと非常に相関関係が高く類似したパフォーマンス指標なので代わりに参考でき、[通常はTBTを改善すればINPも一緒に改善される](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)。

### Lighthouse 10のパフォーマンススコア重み
[Lighthouseのパフォーマンススコアは各測定項目スコアの重み付き平均で計算し、この時次の表の重みに従う](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})。

| 測定項目 | 重み |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- ページ要求後、最初のDOMコンテンツをレンダリングするまでの所要時間を測定
- ページ内の画像、白色でない`<canvas>`要素、SVGなどをDOMコンテンツと見なし、`iframe`内のコンテンツは考慮しない

> FCPに特に重要な影響を与える要素の一つはフォントローディング時間で、これに関する最適化は[関連ポスト](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})を参考することを[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})では推奨している。
{: .prompt-tip }

#### Lighthouse評価基準
[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})によると、Lighthouseの評価基準は次の表の通りである。

| 色等級 | モバイルFCP（秒） | デスクトップFCP（秒） |
| --- | --- | --- |
| 緑（高速） | 0-1.8 | 0-0.9 |
| オレンジ（中間） | 1.8-3 | 0.9-1.6 |
| 赤（低速） | 3超過 | 1.6超過 |

### LCP (Largest Contentful Paint)
- ウェブページを最初に開いた時、最初に画面に見える表示領域（viewport）を基準に、該当領域内で最も大きく表示される要素（画像、テキストブロック、動画など）をレンダリングするまでの所要時間を測定
- 画面上で占める面積が広いほどユーザーの立場で主要コンテンツとして体感する可能性が高いだろう
- LCPが画像の場合、所要時間を4つの下位区間に分けることができ、この中でボトルネックが発生する部分がどこかを把握することが重要
  1. Time to first byte (TTFB): ページロード開始時点からHTML文書応答の最初のバイトを受信した時点までの時間
  2. ロード遅延（Load delay）: ブラウザがLCPリソースのロードを開始した時点とTTTBの間の差
  3. ロード時間（Load time）: LCPリソース自体をロードするのにかかった時間
  4. レンダリング遅延（Render delay）: LCPリソースロードを完了した時点からLCP要素を完全にレンダリング完了するまでの時間

#### Lighthouse評価基準
[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})によると、Lighthouseの評価基準は次の表の通りである。

| 色等級 | モバイルFCP（秒） | デスクトップFCP（秒） |
| --- | --- | --- |
| 緑（高速） | 0-2.5 | 0-1.2 |
| オレンジ（中間） | 2.5-4 | 1.2-2.4 |
| 赤（低速） | 4超過 | 2.4超過 |

### TBT (Total Blocking Time)
- ウェブページがマウスクリック、画面タッチ、キーボード入力のようなユーザー入力に反応できない総時間を測定
- FCPと[TTI（インタラクション開始時点、Time to Interactive）](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*の間のタスクのうち50ms以上実行されたタスクを[長いタスク](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})と見なし、このような長いタスクそれぞれにかかった時間から50msを引いた超過分を*ブロッキング部分（blocking portion）*と呼び、すべてのブロッキング部分の合計をTBTと定義

> \* TTI自体はネットワーク応答異常値と長いタスクに過度に敏感で一貫性が低く高い変動性を持ち、これにより[Lighthouse 10からはパフォーマンス評価項目から除外された](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)。
{: .prompt-info }

> 一般的に長いタスクを引き起こす最も一般的な原因は不要または非効率的なJavaScriptのローディング、パースおよび実行であり、[コード分割](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }})を通じてそれぞれが50ms以内に実行可能になるようJavaScriptペイロードサイズを減らし、必要であればメインスレッドではなく別のサービスワーカーに分離してマルチスレッドで実行することを検討するよう[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})と[Googleのweb.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }})は推奨している。
{: .prompt-tip }

#### Lighthouse評価基準
[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})によると、Lighthouseの評価基準は次の表の通りである。

| 色等級 | モバイルFCP（ミリ秒） | デスクトップFCP（ミリ秒） |
| --- | --- | --- |
| 緑（高速） | 0-200 | 0-150 |
| オレンジ（中間） | 200-600 | 150-350 |
| 赤（低速） | 600超過 | 350超過 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="突然のレイアウト変更の例" autoplay=true loop=true %}
> 動画出典: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~カーソルの動きから深い怒りが感じられる~~

- 予期しないレイアウト変更はテキストが突然移動して読んでいた位置を見失ったり、リンクやボタンを間違ってクリックさせるなど様々な方式でユーザーエクスペリエンスを阻害する
- CLSスコアを算定する具体的な方式は[Googleのweb.dev](https://web.dev/articles/cls)に記述されている
- 下の画像で確認できるように、0.1以下を目標にする必要がある

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> 画像出典: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- ページをロードする間にコンテンツがどれだけ早く視覚的に表示されるかを測定
- Lighthouseはブラウザでページをロードする過程を動画で録画し、該当動画を分析してフレーム間の進行を計算した後、[Speedline Node.jsモジュール](https://github.com/paulirish/speedline)を使用してSIスコアを算定

> 先ほど[FCP](#fcp-first-contentful-paint)、[LCP](#lcp-largest-contentful-paint)、[TBT](#tbt-total-blocking-time)についてまとめる際に言及したことを含め、ページローディング速度を改善する措置であれば何でもSIスコアにも肯定的に作用する。ページローディングのどれか一つの過程だけを代表するよりは全体のローディング過程を一定レベル反映するパフォーマンス指標と見ることができる。
{: .prompt-tip }

#### Lighthouse評価基準
[Chrome開発者文書](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})によると、Lighthouseの評価基準は次の表の通りである。

| 色等級 | モバイルSI（秒） | デスクトップSI（秒） |
| --- | --- | --- |
| 緑（高速） | 0-3.4 | 0-1.3 |
| オレンジ（中間） | 3.4-5.8 | 1.3-2.3 |
| 赤（低速） | 5.8超過 | 2.3超過 |
