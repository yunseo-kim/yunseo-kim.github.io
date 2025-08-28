---
title: ウェブ パフォーマンス指標（Web Vitals）
description: "Web VitalsとLighthouseの計測・評価基準を整理し、LCP・INP・CLS・TBT・FCP・SIの意味と改善ポイントを解説。"
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## ウェブ性能を決定する要素
ウェブ性能最適化で考慮すべき主な要素は、大きくロード性能とレンダリング性能の2つに分類できる。

### HTML のロード性能
- ネットワーク経由でサーバーに最初にページを要求してから、HTML 文書を受信しブラウザがレンダリングを開始するまでの時間
- ページがどれだけ早く表示され始めるかを左右する
- リダイレクトの最小化、HTML 応答のキャッシュ、リソース圧縮、適切なCDN活用などで最適化

### レンダリング性能
- ブラウザがユーザーに見える画面を描画し、かつインタラクティブにするまでに要する時間
- どれだけ滑らかかつ素早く画面が描画されるかを左右する
- 不要なCSSやJSの削除、フォントやサムネイルの遅延読み込みを避ける、重い計算は別のWeb Worker（Web Worker）に分離してメインスレッド占有を最小化、アニメーションの最適化などで最適化

## ウェブ パフォーマンス指標（Web Vitals）
Google の [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) と [Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})を基準に記述する。特段の理由がない限り、どれか1つの指標だけに注力するのではなく全体的な改善を目標にするのがよく、最適化対象ページでどこがボトルネックになっているかを把握することが重要である。また実ユーザーデータの統計がある場合は、上位や平均ではなく第1四分位（Q1）程度の下位値にも注目し、そのケースでも目標基準を満たすか確認・改善するのがよい。

### 主要なウェブ バイタル（Core Web Vitals）
後述するようにウェブ パフォーマンス指標（Web Vitals）には複数あるが、このうち特にユーザー体験に密接に関連し、ラボ環境ではなく実環境で測定可能な次の3指標をGoogleは特に重要視し、これを[主要なウェブ バイタル（Core Web Vitals）](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)と呼ぶ。Google は自社検索エンジンの順位にも対象サイトの主要ウェブ バイタルを反映しているため、サイト運営者にとってもこれらの指標はSEOの観点から注意深く見るべきである。
- [最大コンテンツの描画（Largest Contentful Paint, LCP）](#lcp-largest-contentful-paint): *ロード性能*を反映、2.5秒以内であること
- [次のペイントまでのインタラクション（Interaction to Next Paint, INP）](https://web.dev/articles/inp?hl={{ site.active_lang }}): *応答性*を反映、200ms以下であること
- [累積レイアウトシフト（Cumulative Layout Shift, CLS）](#cls-cumulative-layout-shift): *視覚的安定性*を反映、0.1以下に保つこと

主要ウェブ バイタルは基本的に実環境での測定を想定しているが、INP を除く2つは Chrome DevTools や Lighthouse といったラボ環境でも測定できる。INP は実際のユーザー入力があって初めて測定可能なためラボ環境では測れないが、その場合は [TBT](#tbt-total-blocking-time) が INP と非常に相関が高く近い指標なので参考にでき、[通常はTBTを改善すればINPも改善される](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)。

### Lighthouse 10 の性能スコアの重み
[Lighthouse の性能スコアは各測定項目のスコアの加重平均で算出され、その際の重みは以下の表に従う](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})。

| 測定項目 | 重み |
| --- | --- |
| [最初のコンテンツの描画（First Contentful Paint, FCP）](#fcp-first-contentful-paint) | 10% |
| [スピードインデックス（Speed Index, SI）](#si-speed-index) | 10% |
| [最大コンテンツの描画（Largest Contentful Paint, LCP）](#lcp-largest-contentful-paint) | 25% |
| [合計ブロッキング時間（Total Blocking Time, TBT）](#tbt-total-blocking-time) | 30% |
| [累積レイアウトシフト（Cumulative Layout Shift, CLS）](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- ページ要求後、最初のDOMコンテンツをレンダリングするまでの所要時間を測定
- ページ内の画像、白以外を描画する `<canvas>` 要素、SVG などをDOMコンテンツとみなし、`iframe` 内のコンテンツは考慮しない

> FCP に特に大きく影響する要素の1つはフォントのロード時間であり、その最適化については[関連ポスト](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})を参照するよう[Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})は推奨している。
{: .prompt-tip }

#### Lighthouse の評価基準
[Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})によれば、Lighthouse の評価基準は次の表のとおり。

| 色区分 | モバイル FCP（秒） | デスクトップ FCP（秒） |
| --- | --- | --- |
| 緑（速い） | 0-1.8 | 0-0.9 |
| 橙（中間） | 1.8-3 | 0.9-1.6 |
| 赤（遅い） | 3 超 | 1.6 超 |

### LCP (Largest Contentful Paint)
- ページを初めて開いたときに最初に見える表示領域（viewport）を基準に、その領域内で最も大きく表示される要素（画像、テキストブロック、動画など）をレンダリング完了するまでの所要時間を測定
- 画面上で占める面積が大きいほど、ユーザーに主要コンテンツとして認識される可能性が高い
- LCP が画像の場合、所要時間は4つの下位区間に分けられ、どこでボトルネックが起きているかを把握することが重要
  1. 最初のバイトまでの時間（Time to First Byte, TTFB）: ページロード開始から HTML 応答の最初のバイトを受信するまで
  2. ロード遅延（Load delay）: ブラウザが LCP リソースのロードを開始した時点と TTFB の差
  3. ロード時間（Load time）: LCP リソース自体のロードに要した時間
  4. レンダリング遅延（Render delay）: LCP リソースのロード完了から LCP 要素の完全なレンダリング完了まで

#### Lighthouse の評価基準
[Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})によれば、Lighthouse の評価基準は次の表のとおり。

| 色区分 | モバイル LCP（秒） | デスクトップ LCP（秒） |
| --- | --- | --- |
| 緑（速い） | 0-2.5 | 0-1.2 |
| 橙（中間） | 2.5-4 | 1.2-2.4 |
| 赤（遅い） | 4 超 | 2.4 超 |

### TBT (Total Blocking Time)
- ページがマウスクリック、画面タップ、キーボード入力などのユーザー入力に反応できない合計時間を測定
- FCP と [TTI（インタラクティブになるまでの時間, Time to Interactive）](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }}) の間に実行されたタスクのうち 50ms 以上かかったものを[長いタスク](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})とみなし、各長いタスクの実行時間から 50ms を差し引いた超過分を*ブロッキング部分（blocking portion）*とし、これらの合計を TBT と定義する

> ※ TTI 自体はネットワーク応答の外れ値や長いタスクに過度に敏感で一貫性が低く変動が大きいため、[Lighthouse 10 以降は評価項目から除外された](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)。
{: .prompt-info }

> 一般に長いタスクを引き起こす最も一般的な原因は、不要または非効率な JavaScript のロード・パース・実行である。[コード分割（Code Splitting）](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }})によって各タスクが 50ms 以内に実行できるよう JS ペイロードを削減し、必要に応じてメインスレッドではなく別の Service Worker（Service Worker）に分離してマルチスレッドで実行することを検討するよう、[Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})と[Google の web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }})は推奨している。
{: .prompt-tip }

#### Lighthouse の評価基準
[Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})によれば、Lighthouse の評価基準は次の表のとおり。

| 色区分 | モバイル TBT（ミリ秒） | デスクトップ TBT（ミリ秒） |
| --- | --- | --- |
| 緑（速い） | 0-200 | 0-150 |
| 橙（中間） | 200-600 | 150-350 |
| 赤（遅い） | 600 超 | 350 超 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="予期しないレイアウト変更の例" autoplay=true loop=true %}
> 動画出典: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~カーソルの動きから深い怒りを感じる~~

- 予期しないレイアウト変更は、テキストが突然移動して読んでいた箇所を見失ったり、リンクやボタンを誤ってクリックしてしまうなど、様々な形でユーザー体験を損なう
- CLS スコアの算出方法の詳細は[Google の web.dev](https://web.dev/articles/cls)に記載されている
- 下図のとおり、0.1 以下を目標にする

![良いCLSスコアとは？](https://web.dev/static/articles/cls/image/good-cls-values.svg){: width="640" height="480" }
> 画像出典: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- ページのロード中にコンテンツがどれだけ早く視覚的に表示されるかを測定
- Lighthouse はブラウザでのページロード過程を動画として記録し、その動画を分析してフレーム間の進捗を算出し、[Speedline Node.js モジュール](https://github.com/paulirish/speedline)を用いて SI スコアを算出する

> 先にまとめた [FCP](#fcp-first-contentful-paint)、[LCP](#lcp-largest-contentful-paint)、[TBT](#tbt-total-blocking-time) など、ページロードを速くする施策は概ね SI スコアにも好影響を与える。ページロードのどれか一過程のみを代表するというより、全体のロード過程を一定程度反映する指標といえる。
{: .prompt-tip }

#### Lighthouse の評価基準
[Chrome 開発者向けドキュメント](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})によれば、Lighthouse の評価基準は次の表のとおり。

| 色区分 | モバイル SI（秒） | デスクトップ SI（秒） |
| --- | --- | --- |
| 緑（速い） | 0-3.4 | 0-1.3 |
| 橙（中間） | 3.4-5.8 | 1.3-2.3 |
| 赤（遅い） | 5.8 超 | 2.3 超 |
