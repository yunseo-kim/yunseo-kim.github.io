---
title: 網頁效能指標（Web Vitals）
description: "整理網頁效能指標（Web Vitals）與 Lighthouse 的量測與評分標準，並說明各指標的意義與最佳化方向，助你提升實際使用者體驗與 SEO。"
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## 決定網頁效能的要素
在進行網頁效能最佳化時，影響效能的要素大致可分為「載入效能」與「渲染效能」兩類。

### HTML 載入效能
- 透過網路向伺服器發出初次頁面請求後，接收 HTML 文件並由瀏覽器開始繪製前的時間
- 決定頁面多快開始出現可見內容
- 透過最小化重新導向、快取 HTML 回應、壓縮資源、妥善運用 CDN 等方式最佳化

### 渲染效能
- 瀏覽器把使用者看到的畫面繪製出來並變得可互動所需的時間
- 決定畫面繪製的流暢度與速度
- 移除不必要的 CSS 與 JS、避免延遲載入字型與縮圖、將沉重計算分離到獨立的 Web Worker 以降低主執行緒（main thread）占用、最佳化動畫等方式進行最佳化

## 網頁效能指標（Web Vitals）
以下以 Google 的 [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) 與 [Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})為基準進行說明。除非有特殊理由，不要只聚焦於單一指標，而應以整體改善為目標；找出欲最佳化之頁面中的效能瓶頸所在至關重要。此外，若有實際使用者資料，與其參考前段或平均值，不如關注約略第 1 四分位數（Q1）的低段值，並確認在這些情況下也能達到目標基準再行改善。

### 核心網頁生命力（Core Web Vitals）
稍後會介紹 Web Vitals 中的多個指標；其中與使用者體驗最為密切、且可於真實環境量測的三項指標，Google 特別重視，稱為[核心網頁生命力（Core Web Vitals）](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)。由於 Google 也會在自家搜尋引擎的排名中納入目標網站的核心網頁生命力，對站點經營者而言，這些指標在搜尋引擎最佳化（SEO）上亦須特別留意。
- [最大內容繪製（Largest Contentful Paint, LCP）](#lcp最大內容繪製-largest-contentful-paint)：反映*載入效能*，應在 2.5 秒以內
- [互動到下一次繪製（Interaction to Next Paint, INP）](https://web.dev/articles/inp?hl={{ site.active_lang }})：反映*回應性*，應在 200ms 以內
- [累積版面位移（Cumulative Layout Shift, CLS）](#cls累積版面位移-cumulative-layout-shift)：反映*視覺穩定性*，應維持在 0.1 以下

核心網頁生命力基本上是為真實環境量測而設計，但除了 INP 外，其餘兩者也能在 Chrome 開發人員工具或 Lighthouse 等模擬環境中量測。INP 需要真實使用者輸入才可量測，故無法於模擬環境取得；此時可改參考與 INP 高度相關且類似的指標 [TBT](#tbt總封鎖時間-total-blocking-time)，[通常改善 TBT 也會同時改善 INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)。

### Lighthouse 10 的效能分數權重
[Lighthouse 的效能分數是各量測項目分數的加權平均，權重如下表所示](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})。

| 量測項目 | 權重 |
| --- | --- |
| [首次內容繪製](#fcp首次內容繪製-first-contentful-paint) | 10% |
| [速度指數](#si速度指數-speed-index) | 10% |
| [最大內容繪製](#lcp最大內容繪製-largest-contentful-paint) | 25% |
| [總封鎖時間](#tbt總封鎖時間-total-blocking-time) | 30% |
| [累積版面位移](#cls累積版面位移-cumulative-layout-shift) | 25% |

### FCP（首次內容繪製, First Contentful Paint）
- 量測自頁面請求後，至首次繪製 DOM 內容的時間
- 影像、非白色的 `<canvas>` 元素、SVG 等皆視為 DOM 內容，但不包含 `iframe` 內的內容

> 影響 FCP 的重要因素之一是字型載入時間。關於此處的最佳化，[Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})建議參考[相關文章](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})。
{: .prompt-tip }

#### Lighthouse 評分基準
依[Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})，Lighthouse 的評分基準如下。

| 顏色等級 | 行動版 FCP（秒） | 桌面版 FCP（秒） |
| --- | --- | --- |
| 綠色（快） | 0-1.8 | 0-0.9 |
| 橘色（中等） | 1.8-3 | 0.9-1.6 |
| 紅色（慢） | 大於 3 | 大於 1.6 |

### LCP（最大內容繪製, Largest Contentful Paint）
- 以首次開啟網頁時畫面最先可見的視窗（viewport）為基準，量測該區域內面積最大之元素（圖片、文字區塊、影片等）完成繪製所需時間
- 元素在畫面上佔用面積越大，越可能被使用者視為主要內容
- 若 LCP 是圖片，可將耗時區分為四個子階段，找出瓶頸所在相當重要
  1. 首位元組時間（TTFB, Time to First Byte）：自頁面載入開始至收到 HTML 回應的第一個位元組的時間
  2. 載入延遲（Load delay）：瀏覽器開始載入 LCP 資源的時間與 TTFB 之間的差
  3. 載入時間（Load time）：載入 LCP 資源本身所需的時間
  4. 繪製延遲（Render delay）：自完成載入 LCP 資源至將 LCP 元素完全繪製完成所需的時間

#### Lighthouse 評分基準
依[Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})，Lighthouse 的評分基準如下。

| 顏色等級 | 行動版 LCP（秒） | 桌面版 LCP（秒） |
| --- | --- | --- |
| 綠色（快） | 0-2.5 | 0-1.2 |
| 橘色（中等） | 2.5-4 | 1.2-2.4 |
| 紅色（慢） | 大於 4 | 大於 2.4 |

### TBT（總封鎖時間, Total Blocking Time）
- 量測網頁無法對滑鼠點擊、觸控、鍵盤輸入等使用者輸入做出反應的總時長
- 在 FCP 與 [TTI（互動時間, Time to Interactive）](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* 之間，將執行時間超過 50ms 的作業視為[長任務](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})。每個長任務超過 50ms 的部分稱為*阻塞部分（blocking portion）*，而所有阻塞部分的總和即為 TBT

> \* TTI 本身對於網路回應離群值與長任務過於敏感，導致一致性不足且變異大，因此[自 Lighthouse 10 起已從評分項目中移除](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)。
{: .prompt-info }

> 造成長任務的最常見原因，多半是不必要或低效率的 JavaScript 載入、剖析與執行。[Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})與 [Google 的 web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }})建議運用[程式碼分割（code splitting）](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }})以降低 JavaScript 負載，使每段能在 50ms 內執行；必要時可分離到非主執行緒、或獨立的 Service Worker 以多執行緒方式執行。
{: .prompt-tip }

#### Lighthouse 評分基準
依[Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})，Lighthouse 的評分基準如下。

| 顏色等級 | 行動版 TBT（毫秒） | 桌面版 TBT（毫秒） |
| --- | --- | --- |
| 綠色（快） | 0-200 | 0-150 |
| 橘色（中等） | 200-600 | 150-350 |
| 紅色（慢） | 大於 600 | 大於 350 |

### CLS（累積版面位移, Cumulative Layout Shift）
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="突發版面變動的範例" autoplay=true loop=true %}
> 影片來源：[Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~從游標的動作中感受到滿滿的憤怒~~

- 出乎意料的版面變動會讓文字突然移位、造成閱讀斷點，或誤點連結與按鈕等，多種方式傷害使用者體驗
- CLS 分數的具體計算方式已記載於 [Google 的 web.dev](https://web.dev/articles/cls)
- 如下圖所示，應以 0.1 以下為目標

![何謂良好的 CLS 分數？](/assets/img/about-web-vitals/good-cls-values.svg)
> 圖片來源：[Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI（速度指數, Speed Index）
- 量測在頁面載入過程中，內容被視覺化呈現的速度
- Lighthouse 會錄下瀏覽器載入頁面的過程影片，分析各影格的進度，並使用 [Speedline Node.js 模組](https://github.com/paulirish/speedline)計算 SI 分數

> 先前整理[ FCP](#fcp首次內容繪製-first-contentful-paint)、[LCP](#lcp最大內容繪製-largest-contentful-paint)、[TBT](#tbt總封鎖時間-total-blocking-time)時提到的作法在內，只要能提升頁面載入速度，通常也會正向影響 SI 分數。此指標較偏向反映整體載入過程，而非代表載入中的某個單一步驟。
{: .prompt-tip }

#### Lighthouse 評分基準
依[Chrome 開發人員文件](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})，Lighthouse 的評分基準如下。

| 顏色等級 | 行動版 SI（秒） | 桌面版 SI（秒） |
| --- | --- | --- |
| 綠色（快） | 0-3.4 | 0-1.3 |
| 橘色（中等） | 3.4-5.8 | 1.3-2.3 |
| 紅色（慢） | 大於 5.8 | 大於 2.3 |
