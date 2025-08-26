---
title: Web Performance Metrics (Web Vitals)
description: "Overview of Web Vitals and Lighthouse scoring—what each metric means, how it’s measured, and target thresholds for LCP, INP, CLS, TBT, FCP, and Speed Index to improve performance."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Factors that determine web performance
Broadly, the factors that determine web performance to consider during optimization fall into two categories: loading performance and rendering performance.

### HTML loading performance
- The time from the initial page request over the network to when the browser receives the HTML document and starts rendering
- Determines how quickly the page starts to display
- Optimize by minimizing redirects, caching HTML responses, compressing resources, and using an appropriate CDN

### Rendering performance
- The time it takes the browser to paint what users see and make it interactive
- Determines how smoothly and quickly the screen is drawn
- Optimize by removing unnecessary CSS and JS, avoiding delayed loading of fonts and thumbnails, offloading heavy computations to a separate Web Worker to minimize main-thread occupancy, and optimizing animations

## Web Performance Metrics (Web Vitals)
This post follows Google’s [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) and the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Unless there’s a special reason, aim for overall improvement rather than focusing on a single metric, and identify which part of the target page is the performance bottleneck. If you have real-user data, it’s better to focus on lower-quartile (Q1) values rather than the top or average, and verify that your targets are still met in those cases and improve accordingly.

### Core Web Vitals
As we’ll cover shortly, there are many Web Vitals. Among them, Google highlights three metrics that are tightly tied to user experience and can be measured in the field rather than only in lab conditions; these are called the [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Because Google incorporates Core Web Vitals into its search ranking, site owners should pay close attention to these for SEO.
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): reflects *loading performance*; should be within 2.5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): reflects *responsiveness*; should be ≤ 200 ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): reflects *visual stability*; should be ≤ 0.1

Core Web Vitals are primarily field metrics, but the other two besides INP can also be measured in lab tools like Chrome DevTools or Lighthouse. INP requires actual user input, so it can’t be measured in a lab; in such cases, [TBT](#tbt-total-blocking-time) is highly correlated with INP and serves as a close proxy, and [improving TBT usually improves INP as well](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Performance score weights in Lighthouse 10
[The Lighthouse performance score is a weighted average of metric scores, using the following weights](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Metric | Weight |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Measures the time from page request to the first render of DOM content
- Counts images, non-white `<canvas>` elements, and SVG as DOM content; excludes content inside `iframe`s

> One factor that significantly affects FCP is font loading. For optimization tips, the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recommend this [related post](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Lighthouse scoring thresholds
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile FCP (s) | Desktop FCP (s) |
| --- | --- | --- |
| Green (fast) | 0–1.8 | 0–0.9 |
| Orange (moderate) | 1.8–3 | 0.9–1.6 |
| Red (slow) | > 3 | > 1.6 |

### LCP (Largest Contentful Paint)
- Measures the time it takes to render the largest element (image, text block, video, etc.) within the initial viewport when the page first opens
- The larger the on-screen area it occupies, the more likely users will perceive it as primary content
- If the LCP is an image, you can break the time down into four sub-intervals; identify where the bottleneck occurs:
  1. Time to First Byte (TTFB): time from the start of page load to receipt of the first byte of the HTML response
  2. Load delay: the difference between when the browser starts loading the LCP resource and the TTFB
  3. Load time: the time to load the LCP resource itself
  4. Render delay: the time from finishing the LCP resource load until the LCP element is fully rendered

#### Lighthouse scoring thresholds
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile LCP (s) | Desktop LCP (s) |
| --- | --- | --- |
| Green (fast) | 0–2.5 | 0–1.2 |
| Orange (moderate) | 2.5–4 | 1.2–2.4 |
| Red (slow) | > 4 | > 2.4 |

### TBT (Total Blocking Time)
- Measures the total time the page is unable to respond to user input such as mouse clicks, touches, and key presses
- Among the tasks between FCP and [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, tasks that run for ≥ 50 ms are considered [long tasks](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}). For each long task, the time beyond 50 ms is called the *blocking portion*, and TBT is the sum of all blocking portions.

> \* TTI itself is overly sensitive to outliers in network responses and long tasks, leading to low consistency and high variance, [so it was removed from Lighthouse scoring starting with Lighthouse 10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> The most common causes of long tasks are unnecessary or inefficient JavaScript loading, parsing, and execution. The [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) and [Google’s web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recommend reducing JavaScript payload via [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) so each chunk runs within 50 ms, and, if needed, offloading work from the main thread to a separate Service Worker to run in multiple threads.
{: .prompt-tip }

#### Lighthouse scoring thresholds
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile TBT (ms) | Desktop TBT (ms) |
| --- | --- | --- |
| Green (fast) | 0–200 | 0–150 |
| Orange (moderate) | 200–600 | 150–350 |
| Red (slow) | > 600 | > 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="An example of an unexpected layout shift" autoplay=true loop=true %}
> Video source: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~I sense deep rage in that cursor movement~~

- Unexpected layout shifts degrade UX in many ways, such as suddenly moving text that causes readers to lose their place, or misclicks on links and buttons
- The exact method for calculating the CLS score is described on [Google’s web.dev](https://web.dev/articles/cls)
- As shown in the image below, you should target ≤ 0.1

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Image source: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Measures how quickly content is visually displayed during page load
- Lighthouse records a video of the page loading in the browser, analyzes it to compute frame-by-frame progression, and then uses the [Speedline Node.js module](https://github.com/paulirish/speedline) to compute the SI score

> Any improvement that speeds up page loading—including what we covered for [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint), and [TBT](#tbt-total-blocking-time)—will generally improve the SI score as well. Rather than representing a single stage of loading, SI reflects the overall loading process to some extent.
{: .prompt-tip }

#### Lighthouse scoring thresholds
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile SI (s) | Desktop SI (s) |
| --- | --- | --- |
| Green (fast) | 0–3.4 | 0–1.3 |
| Orange (moderate) | 3.4–5.8 | 1.3–2.3 |
| Red (slow) | > 5.8 | > 2.3 |
