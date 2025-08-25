---
title: ウェブ性能指標（Web Vitals）
description: Web Vitals（ウェブ性能指標）と Lighthouse の測定・評価基準を整理。FCP・LCP・TBT・CLS・SI など各指標の意味と改善ポイントをわかりやすく解説します。
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## ウェブ性能を決定する要素
ウェブ性能最適化で考慮すべき要素は、大きく読み込み性能とレンダリング性能の2つに分類できる。

### HTML ロード性能
- ネットワーク経由でサーバーへ最初の Web ページをリクエストしてから、HTML ドキュメントを受け取りブラウザがレンダリングを開始するまでの時間
- ページがどれだけ早く描画され始めるかを決定
- リダイレクトの最小化、HTML 応答のキャッシュ、リソース圧縮、適切な CDN 活用などで最適化

### レンダリング性能
- ブラウザがユーザーの見る画面を描き、かつインタラクション可能にするまでにかかる時間
- どれだけ滑らかかつ速く画面が描かれるかを決定
- 不要な CSS と JS の削減、フォントやサムネイルの不適切な遅延読み込みの回避、重い計算は別の Web Worker に分離してメインスレッドの占有を最小化、アニメーション最適化などで最適化

## ウェブ性能指標（Web Vitals）
Google の [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) と [Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})を基準に記述する。特別な理由がない限り、どれか一つの指標だけに注力するよりも全体的な改善を目標にするのがよい。また、最適化対象の Web ページでどこがボトルネックになっているかを把握することが重要である。実ユーザーデータの統計がある場合は、上位や平均ではなく第1四分位（Q1）程度の下位値に注目し、その場合でも目標基準を満たすかを確認して改善するのがよい。

### 主要ウェブ性能指標（Core Web Vitals）
後述するが、Web Vitals には複数の指標がある。その中でも特にユーザー体験に密接に関係し、ラボではなく実環境で測定できる次の3指標を Google は特に重視しており、これを[主要ウェブ性能指標（Core Web Vitals）](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)と呼ぶ。Google は自社検索エンジンの順位にも対象サイトの Core Web Vitals を反映しているため、サイト運営者にとっても SEO の観点からこれらの指標を重視すべきである。
- [最大コンテンツ描画（Largest Contentful Paint, LCP）](#lcp-最大コンテンツ描画): 読み込み性能を反映、2.5秒以内であること
- [次のペイントまでのインタラクション（Interaction to Next Paint, INP）](https://web.dev/articles/inp?hl={{ site.active_lang }}): 応答性を反映、200ms 以下であること
- [累積レイアウトシフト（Cumulative Layout Shift, CLS）](#cls-累積レイアウトシフト): 視覚的安定性を反映、0.1 以下に維持

Core Web Vitals は基本的に実環境で測定するためのものだが、INP を除く2つは Chrome DevTools や Lighthouse といったラボ環境でも測定できる。INP は実際のユーザー入力が必要なためラボ環境では測れないが、この場合は [TBT](#tbt-合計ブロッキング時間) が INP と非常に高い相関を持つ類似指標として参照でき、[多くの場合 TBT を改善すると INP も改善する](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)。

### Lighthouse 10 の性能スコアの重み付け
[Lighthouse の性能スコアは各測定項目スコアの加重平均で計算され、その際は次の表の重み付けに従う](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})。

| 測定項目 | 重み |
| --- | --- |
| [初回コンテンツフルペイント（First Contentful Paint）](#fcp-初回コンテンツフルペイント) | 10% |
| [スピードインデックス（Speed Index）](#si-スピードインデックス) | 10% |
| [最大コンテンツ描画（Largest Contentful Paint）](#lcp-最大コンテンツ描画) | 25% |
| [合計ブロッキング時間（Total Blocking Time）](#tbt-合計ブロッキング時間) | 30% |
| [累積レイアウトシフト（Cumulative Layout Shift）](#cls-累積レイアウトシフト) | 25% |

### FCP（初回コンテンツフルペイント, First Contentful Paint） {#fcp-初回コンテンツフルペイント}
- ページ要求後、最初の DOM コンテンツをレンダリングするまでの所要時間を測定
- ページ内の画像、白以外の `<canvas>` 要素、SVG などを DOM コンテンツと見なし、`iframe` 内コンテンツは考慮しない

> FCP に特に大きく影響する要因の一つはフォントの読み込み時間であり、これに関する最適化は[関連記事](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})を参照することを[Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})は推奨している。
{: .prompt-tip }

#### Lighthouse の評価基準
[Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})によると、Lighthouse の評価基準は次の表のとおり。

| 色の等級 | モバイル FCP（秒） | デスクトップ FCP（秒） |
| --- | --- | --- |
| 緑（速い） | 0-1.8 | 0-0.9 |
| 橙（中間） | 1.8-3 | 0.9-1.6 |
| 赤（遅い） | 3 超過 | 1.6 超過 |

### LCP（最大コンテンツ描画, Largest Contentful Paint） {#lcp-最大コンテンツ描画}
- Web ページを初めて開いたときに最初に見える表示領域（ビューポート）を基準とし、その領域内で最も大きく表示される要素（画像、テキストブロック、動画など）をレンダリング完了するまでの時間を測定
- 画面上で占める面積が広いほど、ユーザーにとって主要コンテンツだと感じられる可能性が高い
- LCP が画像の場合、所要時間は4つの下位区間に分けられ、どこでボトルネックが発生しているかを把握することが重要
  1. 最初のバイトまでの時間（Time to First Byte, TTFB）: ページロード開始から HTML 応答の最初のバイトを受信するまでの時間
  2. 読み込み遅延（Load delay）: ブラウザが LCP リソースの読み込みを開始した時点と TTTB の差
  3. 読み込み時間（Load time）: LCP リソース自体の読み込みに要した時間
  4. レンダリング遅延（Render delay）: LCP リソースの読み込み完了から LCP 要素のレンダリング完了までの時間

#### Lighthouse の評価基準
[Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})によると、Lighthouse の評価基準は次の表のとおり。

| 色の等級 | モバイル FCP（秒） | デスクトップ FCP（秒） |
| --- | --- | --- |
| 緑（速い） | 0-2.5 | 0-1.2 |
| 橙（中間） | 2.5-4 | 1.2-2.4 |
| 赤（遅い） | 4 超過 | 2.4 超過 |

### TBT（合計ブロッキング時間, Total Blocking Time） {#tbt-合計ブロッキング時間}
- Web ページがマウスクリック、タッチ、キーボード入力などのユーザー入力に反応できない合計時間を測定
- FCP と [TTI（対話可能になるまでの時間, Time to Interactive）](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* の間に実行された作業のうち、50ms 以上実行された作業を[長いタスク](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})とみなし、各長いタスクの実行時間から 50ms を引いた超過分をブロッキング部分（blocking portion）とし、これらの合計を TBT と定義する

> \* TTI 自体はネットワーク応答の外れ値や長いタスクに過度に敏感で一貫性が低く変動性が高いため、[Lighthouse 10 から性能評価項目から除外された](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)。
{: .prompt-info }

> 一般に長いタスクを引き起こす最も一般的な原因は、不要または非効率な JavaScript の読み込み・パース・実行である。[コード分割](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }})により、各チャンクが 50ms 以内に実行できるよう JS ペイロードを減らし、必要に応じてメインスレッドではなく別の service worker に分離してマルチスレッドで実行することを、[Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})や [Google の web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }})は推奨している。
{: .prompt-tip }

#### Lighthouse の評価基準
[Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})によると、Lighthouse の評価基準は次の表のとおり。

| 色の等級 | モバイル FCP（ミリ秒） | デスクトップ FCP（ミリ秒） |
| --- | --- | --- |
| 緑（速い） | 0-200 | 0-150 |
| 橙（中間） | 200-600 | 150-350 |
| 赤（遅い） | 600 超過 | 350 超過 |

### CLS（累積レイアウトシフト, Cumulative Layout Shift） {#cls-累積レイアウトシフト}
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="突然のレイアウト変更の例" autoplay=true loop=true %}
> 動画出典: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~カーソルの動きから深い怒りが伝わってくる~~

- 予期せぬレイアウトの変化は、テキストが突然移動して読んでいた位置を見失わせたり、リンクやボタンを誤クリックさせるなど、さまざまな形でユーザー体験を損なう
- CLS スコアの算定方法の詳細は [Google の web.dev](https://web.dev/articles/cls) に記載されている
- 下の画像のとおり、0.1 以下を目標にするべき

![良い CLS スコアとは？](/assets/img/about-web-vitals/good-cls-values.svg)
> 画像出典: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI（スピードインデックス, Speed Index） {#si-スピードインデックス}
- ページの読み込み中にコンテンツがどれだけ速く視覚的に表示されるかを測定
- Lighthouse はブラウザでのページ読み込み過程を動画として記録し、その動画を分析してフレーム間の進行を計算したうえで、[Speedline Node.js モジュール](https://github.com/paulirish/speedline)を使って SI スコアを算出する

> 先にまとめた [FCP](#fcp-初回コンテンツフルペイント)、[LCP](#lcp-最大コンテンツ描画)、[TBT](#tbt-合計ブロッキング時間) への対策を含め、ページ読み込み速度を改善する施策は SI スコアにも概ね好影響を与える。ページ読み込みの特定の一工程だけを代表するというより、全体の読み込み過程を一定程度反映する指標といえる。
{: .prompt-tip }

#### Lighthouse の評価基準
[Chrome デベロッパー ドキュメント](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})によると、Lighthouse の評価基準は次の表のとおり。

| 色の等級 | モバイル SI（秒） | デスクトップ SI（秒） |
| --- | --- | --- |
| 緑（速い） | 0-3.4 | 0-1.3 |
| 橙（中間） | 3.4-5.8 | 1.3-2.3 |
| 赤（遅い） | 5.8 超過 | 2.3 超過 |
