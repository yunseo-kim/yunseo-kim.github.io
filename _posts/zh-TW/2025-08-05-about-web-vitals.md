---
title: 網站效能指標（Web Vitals）
description: 整理網站效能指標（Web Vitals）與 Lighthouse 的量測與評分基準，說明各指標的意義與優化方向，聚焦載入效能、回應性與視覺穩定度，助攻 SEO 與實務調校。
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## 決定網站效能的要素
在進行網站效能最佳化時，決定效能的要素大致可分為兩類：載入效能與渲染效能。

### HTML 載入效能
- 透過網路向伺服器發出首次頁面請求開始，到收到 HTML 文件並讓瀏覽器開始渲染為止所需的時間
- 決定頁面能多快開始顯示
- 可透過最小化重新導向、快取 HTML 回應、資源壓縮、妥善運用 CDN 等方式最佳化

### 渲染效能
- 瀏覽器將使用者可見畫面繪出並可互動所需的時間
- 決定畫面繪製的流暢與速度
- 移除不必要的 CSS 與 JS、避免對字型與縮圖進行延遲載入、將重運算分離到獨立的 Web Worker 以最小化主執行緒佔用、優化動畫等方式進行最佳化

## 網站效能指標（Web Vitals）
以下以 Google 的 [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) 與 [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})為準。除非有特殊理由，與其僅關注單一指標，應以整體改善為目標，並辨識頁面上的效能瓶頸所在。若有真實使用者資料，與其盯著前段或平均值，更建議關注第 1 四分位數（Q1）等較差的情況，確認在這些情境下也能達成目標並持續改善。

### 核心網站指標（Core Web Vitals）
稍後會介紹 Web Vitals 的多個指標；其中 Google 特別重視下列三項，因為它們和使用者體驗高度相關，且可在真實環境量測，因此稱為[核心網站指標（Core Web Vitals）](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)。Google 也會在自家搜尋結果排名中反映網站的核心網站指標，站長在搜尋引擎最佳化（SEO）層面亦應重視。
- [最大內容繪製（Large Contentful Paint, LCP）](#lcp-largest-contentful-paint): 反映「載入效能」，應在 2.5 秒內
- [Interaction to Next Paint（INP）](https://web.dev/articles/inp?hl={{ site.active_lang }}): 反映「回應性」，應在 200ms 以下
- [累積版面位移（Cumulative Layout Shift, CLS）](#cls-cumulative-layout-shift): 反映「視覺穩定性」，應維持在 0.1 以下

核心網站指標基本上用於真實環境量測；其中除 INP 外，其餘皆可在 Chrome 開發者工具或 Lighthouse 等實驗室環境量測。INP 需要實際的使用者輸入才能量測，因此在實驗室中無法測得；此時可參考與 INP 高度相關且性質相近的 [TBT](#tbt-total-blocking-time)，[通常改善 TBT 也會同步改善 INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)。

### Lighthouse 10 的效能分數權重
[Lighthouse 的效能分數為各量測項目分數的加權平均，權重如下表所示](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})。

| 量測項目 | 權重 |
| --- | --- |
| [首次內容繪製（First Contentful Paint）](#fcp-first-contentful-paint) | 10% |
| [速度指數（Speed Index）](#si-speed-index) | 10% |
| [最大內容繪製（Largest Contentful Paint）](#lcp-largest-contentful-paint) | 25% |
| [總阻塞時間（Total Blocking Time）](#tbt-total-blocking-time) | 30% |
| [累積版面位移（Cumulative Layout Shift）](#cls-cumulative-layout-shift) | 25% |

### FCP（首次內容繪製, First Contentful Paint）
- 量測自頁面請求後，直到第一個 DOM 內容被繪製出來的時間
- 圖片、非白色的 `<canvas>` 元素、SVG 等都視為 DOM 內容，但不含 `iframe` 內的內容

> 影響 FCP 的關鍵因素之一是字型載入時間。關於字型最佳化，[Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})建議參考[相關文章](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})。
{: .prompt-tip }

#### Lighthouse 評分基準
依據[Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})，Lighthouse 的評分門檻如下。

| 顏色等級 | 行動裝置 FCP（秒） | 桌面 FCP（秒） |
| --- | --- | --- |
| 綠色（快） | 0-1.8 | 0-0.9 |
| 橘色（中） | 1.8-3 | 0.9-1.6 |
| 紅色（慢） | 大於 3 | 大於 1.6 |

### LCP（最大內容繪製, Largest Contentful Paint）
- 以初次開啟頁面時可見的顯示區域（viewport）為準，量測該區域內最大元素（圖片、文字區塊、影片等）被繪製完成所需的時間
- 在畫面上佔比越大的元素，越可能被使用者視為主要內容
- 若 LCP 為圖片，時間可拆為四段，辨識瓶頸所在非常重要：
  1. 首位元組時間（Time to First Byte, TTFB）：自頁面載入開始至收到 HTML 回應的第一個位元組為止的時間
  2. 載入延遲（Load delay）：瀏覽器開始載入 LCP 資源的時間點與 TTFB 之間的差值
  3. 載入時間（Load time）：載入 LCP 資源本身所需的時間
  4. 繪製延遲（Render delay）：完成載入 LCP 資源至將 LCP 元素完全繪製完成之間的時間

#### Lighthouse 評分基準
依據[Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})，Lighthouse 的評分門檻如下。

| 顏色等級 | 行動裝置 LCP（秒） | 桌面 LCP（秒） |
| --- | --- | --- |
| 綠色（快） | 0-2.5 | 0-1.2 |
| 橘色（中） | 2.5-4 | 1.2-2.4 |
| 紅色（慢） | 大於 4 | 大於 2.4 |

### TBT（總阻塞時間, Total Blocking Time）
- 量測網頁對滑鼠點擊、觸控、鍵盤輸入等使用者操作無法回應的總時間
- 在 FCP 與 [TTI（互動就緒時間, Time to Interactive）](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* 之間，將執行時間超過 50ms 的任務視為[長任務（Long Tasks）](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})；各長任務中超過 50ms 的部分稱為「阻塞區段」，所有阻塞區段的總和即為 TBT

> \* TTI 本身對網路異常與長任務過於敏感，導致一致性不佳且變異高，因此[自 Lighthouse 10 起已從評分項目中移除](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)。
{: .prompt-info }

> 造成長任務的最常見原因通常是不必要或低效率的 JavaScript 載入、解析與執行。[Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})與 [Google 的 web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }})建議透過[程式碼分割（Code Splitting）](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }})降低 JS 負載，使各片段能在 50ms 內完成；必要時也可移至非主執行緒（例如 Service Worker）以多執行緒方式運行。
{: .prompt-tip }

#### Lighthouse 評分基準
依據[Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})，Lighthouse 的評分門檻如下。

| 顏色等級 | 行動裝置 TBT（毫秒） | 桌面 TBT（毫秒） |
| --- | --- | --- |
| 綠色（快） | 0-200 | 0-150 |
| 橘色（中） | 200-600 | 150-350 |
| 紅色（慢） | 大於 600 | 大於 350 |

### CLS（累積版面位移, Cumulative Layout Shift）
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="突發版面變動的範例" autoplay=true loop=true %}
> 影片出處： [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~從游標的移動能感受到深沉的憤怒~~

- 出乎意料的版面變動會讓文字突然移動、讀者錯失原本閱讀位置，或誤點連結與按鈕，種種情況都會傷害使用者體驗
- CLS 分數的具體計算方式請見 [Google 的 web.dev](https://web.dev/articles/cls)
- 如下圖所示，建議目標為不超過 0.1

![什麼是良好的 CLS 分數？](/assets/img/about-web-vitals/good-cls-values.svg)
> 圖片來源： [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI（速度指數, Speed Index）
- 量測在頁面載入過程中，內容被視覺化地呈現有多快
- Lighthouse 會錄下瀏覽器載入頁面的過程，分析影格間的進度，並使用 [Speedline Node.js 模組](https://github.com/paulirish/speedline)計算 SI 分數

> 包含前文提到的 [FCP](#fcp-first-contentful-paint)、[LCP](#lcp-largest-contentful-paint)、[TBT](#tbt-total-blocking-time) 等改善措施在內，只要能加速頁面載入，通常也會對 SI 有正向影響。可將 SI 視為「較全面反映整體載入過程」的指標，而非僅代表其中某個單一步驟。
{: .prompt-tip }

#### Lighthouse 評分基準
依據[Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})，Lighthouse 的評分門檻如下。

| 顏色等級 | 行動裝置 SI（秒） | 桌面 SI（秒） |
| --- | --- | --- |
| 綠色（快） | 0-3.4 | 0-1.3 |
| 橘色（中） | 3.4-5.8 | 1.3-2.3 |
| 紅色（慢） | 大於 5.8 | 大於 2.3 |
