---
title: 網站效能指標 (Web Vitals)
description: 本文整理了網站效能指標 (Web Vitals) 與 Lighthouse 的測量及評分標準，並探討各項效能指標的具體含義。
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## 決定網站效能的要素
在進行網站效能最佳化時，需要考量的決定性要素大致可分為「載入效能」和「渲染效能」兩大類。

### HTML 載入效能
- 從透過網路向伺服器首次請求網頁，到接收 HTML 文件並由瀏覽器開始渲染為止所需的時間。
- 決定了頁面開始顯示的速度。
- 可透過最小化重新導向、快取 HTML 回應、壓縮資源、妥善利用 CDN 等方法進行最佳化。

### 渲染效能
- 瀏覽器繪製使用者所見畫面，並使其具備互動性所需的時間。
- 決定了畫面繪製的流暢度與速度。
- 可透過移除不必要的 CSS 及 JS、防止字型及縮圖延遲載入、將繁重運算分離至獨立的 Web Worker 以最小化主執行緒的佔用、以及動畫最佳化等方法進行改善。

## 網站效能指標 (Web Vitals)
本文將以 Google 的 [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) 和 [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}) 為基準進行闡述。除非有特殊理由，否則建議以全面改善為目標，而非僅專注於單一效能指標。找出欲最佳化的網頁中，是哪個部分造成了效能瓶頸至關重要。此外，若有實際的使用者數據統計，建議關注 Q1（第一四分位數）等較低區間的數值，而非頂尖或平均值，以確認在這些情況下是否仍能達到目標標準並加以改善。

### 核心網站生命週期指標 (Core Web Vitals)
稍後將會提到，網站效能指標 (Web Vitals) 有很多種。然而，其中有三項指標與使用者體驗密切相關，且可在真實環境中測量，Google 特別重視這三項指標，並稱之為 [核心網站生命週期指標 (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)。Google 會將目標網站的核心網站生命週期指標納入其搜尋引擎的搜尋結果排名中，因此從網站營運者的角度來看，這些指標在搜尋引擎最佳化 (SEO) 方面也需密切關注。
- [最大內容繪製 (LCP, Largest Contentful Paint)](#lcp-最大內容繪製)：反映*載入效能*，應在 2.5 秒內。
- [下次繪製互動性 (INP, Interaction to Next Paint)](https://web.dev/articles/inp?hl={{ site.active_lang }})：反映*回應速度*，應低於 200 毫秒。
- [累計版面配置位移 (CLS, Cumulative Layout Shift)](#cls-累計版面配置位移)：反映*視覺穩定性*，應維持在 0.1 以下。

核心網站生命週期指標基本上是為了在真實環境中測量而設計的，但除了 INP 之外的兩項指標，也可以在 Chrome 開發者工具或 Lighthouse 等模擬環境中進行測量。至於 INP，由於需要實際的使用者輸入才能測量，因此無法在模擬環境中進行。不過，在這種情況下，可以參考 [TBT](#tbt-總封鎖時間)，因為它與 INP 有高度相關性且是個相似的效能指標，而且[通常改善 TBT 也會一併改善 INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)。

### Lighthouse 10 的效能分數權重
[Lighthouse 的效能分數是透過各項指標分數的加權平均計算得出，並遵循下表的權重](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})。

| 指標 | 權重 |
| --- | --- |
| [首次內容繪製](#fcp-首次內容繪製) | 10% |
| [速度指標](#si-速度指標) | 10% |
| [最大內容繪製](#lcp-最大內容繪製) | 25% |
| [總封鎖時間](#tbt-總封鎖時間) | 30% |
| [累計版面配置位移](#cls-累計版面配置位移) | 25% |

### FCP (首次內容繪製)
- 測量從發出頁面請求到渲染第一個 DOM 內容所需的時間。
- 頁面中的圖片、非白色的 `<canvas>` 元素、SVG 等被視為 DOM 內容，但不考慮 `iframe` 內的內容。

> [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) 建議，對 FCP 有重要影響的因素之一是字型載入時間，關於這方面的最佳化，可以參考[相關的文章](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})。
{: .prompt-tip }

#### Lighthouse 評分標準
根據 [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})，Lighthouse 的評分標準如下表所示。

| 顏色等級 | 行動版 FCP (秒) | 桌面版 FCP (秒) |
| --- | --- | --- |
| 綠色 (快) | 0-1.8 | 0-0.9 |
| 橘色 (中) | 1.8-3 | 0.9-1.6 |
| 紅色 (慢) | 超過 3 | 超過 1.6 |

### LCP (最大內容繪製)
- 以首次開啟網頁時最先映入眼簾的可視區域 (viewport) 為基準，測量渲染該區域內顯示的最大元素（如圖片、文字區塊、影片等）所需的時間。
- 元素在畫面上所佔的面積越大，使用者越有可能將其視為主要內容。
- 當 LCP 元素是圖片時，其所需時間可分為四個子階段，找出其中造成瓶頸的部分至關重要：
  1. Time to first byte (TTFB)：從頁面開始載入到接收到 HTML 文件回應的第一個位元組為止的時間。
  2. 載入延遲 (Load delay)：瀏覽器開始載入 LCP 資源的時間點與 TTFB 之間的時間差。
  3. 載入時間 (Load time)：載入 LCP 資源本身所需的時間。
  4. 渲染延遲 (Render delay)：從 LCP 資源載入完成到 LCP 元素完全渲染完成為止的時間。

#### Lighthouse 評分標準
根據 [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})，Lighthouse 的評分標準如下表所示。

| 顏色等級 | 行動版 LCP (秒) | 桌面版 LCP (秒) |
| --- | --- | --- |
| 綠色 (快) | 0-2.5 | 0-1.2 |
| 橘色 (中) | 2.5-4 | 1.2-2.4 |
| 紅色 (慢) | 超過 4 | 超過 2.4 |

### TBT (總封鎖時間)
- 測量網頁無法回應滑鼠點擊、螢幕觸控、鍵盤輸入等使用者互動的總時間。
- 在 FCP 與 [TTI (可互動時間, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})* 之間，執行時間超過 50 毫秒的任務被視為[長任務 (long tasks)](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})。將這些長任務各自的執行時間減去 50 毫秒後所得的超額部分稱為*封鎖部分 (blocking portion)*，而所有封鎖部分的總和即定義為 TBT。

> \* TTI 本身對網路回應的異常值和長任務過於敏感，導致其一致性低且變動性高，因此[從 Lighthouse 10 開始，已將其從效能評分項目中移除](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)。
{: .prompt-info }

> [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) 和 [Google 的 web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) 建議，導致長任務最常見的原因通常是不必要或低效率的 JavaScript 載入、解析和執行。應考慮透過[程式碼分割 (code splitting)](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) 來減少 JavaScript 的負載大小，使其能在 50 毫秒內執行完畢；如有必要，也可將其分離到獨立的 Service Worker 中，以多執行緒方式執行，而非在主執行緒上。
{: .prompt-tip }

#### Lighthouse 評分標準
根據 [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})，Lighthouse 的評分標準如下表所示。

| 顏色等級 | 行動版 TBT (毫秒) | 桌面版 TBT (毫秒) |
| --- | --- | --- |
| 綠色 (快) | 0-200 | 0-150 |
| 橘色 (中) | 200-600 | 150-350 |
| 紅色 (慢) | 超過 600 | 超過 350 |

### CLS (累計版面配置位移)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="突發版面配置位移的範例" autoplay=true loop=true %}
> 影片來源：[Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~從游標的移動中可以感受到深深的憤怒~~

- 非預期的版面配置位移會導致文字突然移動，讓使用者錯失閱讀位置，或是誤點擊連結或按鈕，從多方面損害使用者體驗。
- 計算 CLS 分數的具體方式已詳述於 [Google 的 web.dev](https://web.dev/articles/cls)。
- 如下圖所示，目標應是將 CLS 維持在 0.1 以下。

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> 圖片來源：[Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (速度指標)
- 測量頁面載入過程中，內容以多快的速度在視覺上呈現。
- Lighthouse 會錄下瀏覽器載入頁面的過程影片，並分析該影片以計算影格之間的進度，然後使用 [Speedline Node.js 模組](https://github.com/paulirish/speedline) 來計算 SI 分數。

> 除了先前在整理 [FCP](#fcp-首次內容繪製)、[LCP](#lcp-最大內容繪製) 和 [TBT](#tbt-總封鎖時間) 時提到的方法外，任何能改善頁面載入速度的措施，都會對 SI 分數產生正面影響。可以說，SI 並非只代表載入過程中的某個單一環節，而是在一定程度上反映了整體載入過程的效能指標。
{: .prompt-tip }

#### Lighthouse 評分標準
根據 [Chrome 開發者文件](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})，Lighthouse 的評分標準如下表所示。

| 顏色等級 | 行動版 SI (秒) | 桌面版 SI (秒) |
| --- | --- | --- |
| 綠色 (快) | 0-3.4 | 0-1.3 |
| 橘色 (中) | 3.4-5.8 | 1.3-2.3 |
| 紅色 (慢) | 超過 5.8 | 超過 2.3 |
