---
title: Web Performance Metrics (Web Vitals)
description: A concise guide to Web Vitals and Lighthouse scoring: what LCP, INP, CLS, FCP, TBT, and SI mean, how they’re measured, and practical tips to improve real‑world performance.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## What determines web performance
When optimizing web performance, the factors that determine it can broadly be classified into two categories: loading performance and rendering performance.

### HTML loading performance
- The time from when the server receives the initial page request over the network to when the browser starts rendering the HTML document
- Determines how quickly the page begins to display
- Optimize by minimizing redirects, caching HTML responses, compressing resources, and using an appropriate CDN

### Rendering performance
- The time it takes the browser to paint what the user sees and make it interactive
- Determines how smoothly and quickly the screen is drawn
- Optimize by removing unnecessary CSS and JS, preventing delayed loading of fonts and thumbnails, moving heavy computations to a separate Web Worker to minimize main-thread contention, and optimizing animations

## Web performance metrics (Web Vitals)
This post follows Google’s guidance on [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) and the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Unless you have a specific reason, aim for holistic improvements rather than focusing on a single metric, and identify which parts of the target page are acting as bottlenecks. If you have field user data, look beyond top or average values and pay attention to lower-quartile (Q1) values to ensure you still meet targets under those conditions.

### Core Web Vitals
As we’ll cover shortly, there are many Web Vitals. Among them, Google highlights three metrics that are tightly tied to user experience and can be measured in the field rather than only in lab conditions; these are called the [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Because Google incorporates Core Web Vitals into its search ranking, site owners should pay close attention to these for SEO.
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): reflects loading performance; should be within 2.5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): reflects responsiveness; should be ≤ 200 ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): reflects visual stability; should be ≤ 0.1

Core Web Vitals are fundamentally field metrics, but the two other than INP can also be measured in lab tools like Chrome DevTools or Lighthouse. INP requires real user input, so it cannot be measured in lab conditions; in such cases, [TBT](#tbt-total-blocking-time) is highly correlated with INP and can be used as a proxy, and [improving TBT usually improves INP as well](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

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

#### Lighthouse scoring criteria
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile FCP (s) | Desktop FCP (s) |
| --- | --- | --- |
| Green (fast) | 0–1.8 | 0–0.9 |
| Orange (average) | 1.8–3 | 0.9–1.6 |
| Red (slow) | greater than 3 | greater than 1.6 |

### LCP (Largest Contentful Paint)
- From the initial viewport when the page first opens, measures the time to render the largest element (image, text block, video, etc.) within that viewport
- The larger the area it occupies on screen, the more likely users perceive it as primary content
- If the LCP is an image, the total time can be broken into four sub-intervals; identifying where the bottleneck occurs is important:
  1. Time to First Byte (TTFB): time from the start of page load to receiving the first byte of the HTML response
  2. Load delay: the difference between when the browser starts loading the LCP resource and TTFB
  3. Load time: time to load the LCP resource itself
  4. Render delay: time from completing the LCP resource load to fully rendering the LCP element

#### Lighthouse scoring criteria
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile LCP (s) | Desktop LCP (s) |
| --- | --- | --- |
| Green (fast) | 0–2.5 | 0–1.2 |
| Orange (average) | 2.5–4 | 1.2–2.4 |
| Red (slow) | greater than 4 | greater than 2.4 |

### TBT (Total Blocking Time)
- Measures the total time the page is unable to respond to user inputs such as mouse clicks, taps, or keyboard input
- Between FCP and [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }}), any task that runs for ≥ 50 ms is considered a [long task](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}). For each long task, the time beyond 50 ms is the blocking portion, and TBT is the sum of all blocking portions.

> TTI itself is overly sensitive to network outliers and long tasks, leading to inconsistency and high variance. Accordingly, [Lighthouse removed TTI from scoring starting in v10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> The most common causes of long tasks are unnecessary or inefficient JavaScript loading, parsing, and execution. The [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) and [Google’s web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recommend using [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) to reduce JavaScript payloads so each chunk can execute within 50 ms, and, if needed, moving work off the main thread to a separate service worker to run in multiple threads.
{: .prompt-tip }

#### Lighthouse scoring criteria
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile TBT (ms) | Desktop TBT (ms) |
| --- | --- | --- |
| Green (fast) | 0–200 | 0–150 |
| Orange (average) | 200–600 | 150–350 |
| Red (slow) | greater than 600 | greater than 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="An example of an unexpected layout shift" autoplay=true loop=true %}
> Video source: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~You can feel deep rage in the cursor movement~~

- Unexpected layout shifts hurt UX in many ways, such as making text jump so you lose your reading position or causing misclicks on links or buttons
- The exact scoring method for CLS is described on [Google’s web.dev](https://web.dev/articles/cls)
- As shown below, you should target ≤ 0.1

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Image source: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Measures how quickly content is visually displayed during page load
- Lighthouse records a video of the page loading in the browser, analyzes the frames to calculate visual progress, and uses the [Speedline Node.js module](https://github.com/paulirish/speedline) to compute the SI score

> Any action that improves page load speed—including the measures discussed for [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint), and [TBT](#tbt-total-blocking-time)—will typically improve SI as well. Rather than representing a single step, SI reflects the overall loading process to some extent.
{: .prompt-tip }

#### Lighthouse scoring criteria
According to the [Chrome Developers docs](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), Lighthouse uses the following thresholds:

| Color rating | Mobile SI (s) | Desktop SI (s) |
| --- | --- | --- |
| Green (fast) | 0–3.4 | 0–1.3 |
| Orange (average) | 3.4–5.8 | 1.3–2.3 |
| Red (slow) | greater than 5.8 | greater than 2.3 |
