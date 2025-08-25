---
title: Web Performance Metrics (Web Vitals)
description: An overview of Web Vitals and Lighthouse scoring criteria. Learn what each performance metric means and how to interpret them.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Factors That Determine Web Performance
When optimizing web performance, the determining factors can be broadly categorized into two types: loading performance and rendering performance.

### HTML Loading Performance
- The time from the initial request for a webpage over the network to when the browser receives the HTML document and begins rendering.
- Determines how quickly the page starts to display.
- Can be optimized by minimizing redirects, caching HTML responses, compressing resources, and using a CDN effectively.

### Rendering Performance
- The time it takes for the browser to draw the user's screen and make it interactive.
- Determines how smoothly and quickly the screen is drawn.
- Can be optimized by removing unnecessary CSS and JS, preventing font and thumbnail loading delays, offloading heavy computations to a separate Web Worker to minimize main thread occupation, and optimizing animations.

## Web Vitals
This post is based on Google's [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) and the [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Unless there's a specific reason, it's better to aim for overall improvement rather than focusing on a single performance metric. It's crucial to identify which parts of the webpage you're optimizing are causing performance bottlenecks. Furthermore, if you have real user data, it's better to focus on the 75th percentile rather than the top performers or the average. Check if even these cases meet the target criteria and make improvements accordingly.

### Core Web Vitals
As we will discuss shortly, there are several Web Vitals. However, Google considers the following three metrics, which are closely related to user experience and measurable in the field (real-world environments) rather than just in the lab (simulated environments), to be particularly important. These are called the [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Since Google incorporates a site's Core Web Vitals into its search engine ranking algorithm, site owners must pay close attention to these metrics for Search Engine Optimization (SEO) purposes.
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): Measures *loading performance*. Should be 2.5 seconds or less.
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): Measures *responsiveness*. Should be 200 milliseconds or less.
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): Measures *visual stability*. Should be maintained at 0.1 or less.

Core Web Vitals are primarily intended for measurement in the field, but the other two, excluding INP, can also be measured in lab environments like Chrome DevTools or Lighthouse. INP requires real user input to be measured and thus cannot be measured in a lab environment. However, in such cases, [Total Blocking Time (TBT)](#tbt-total-blocking-time) can be used as a proxy, as it is a highly correlated and similar performance metric. [Improving TBT usually leads to improvements in INP as well](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Lighthouse 10 Performance Score Weighting
[The Lighthouse performance score is a weighted average of the individual metric scores. It uses the weightings in the following table](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Metric | Weight |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Measures the time from when the page starts loading to when the first piece of DOM content is rendered on the screen.
- DOM content includes images, non-white `<canvas>` elements, and SVGs. Content inside `iframes` is not included.

> One of the key factors affecting FCP is font loading time. The [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recommends referring to [this related post](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) for optimization.
{: .prompt-tip }

#### Lighthouse Scoring
According to the [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), the Lighthouse scoring is as follows:

| Color Grade | Mobile FCP (seconds) | Desktop FCP (seconds) |
| --- | --- | --- |
| Green (Fast) | 0-1.8 | 0-0.9 |
| Orange (Moderate) | 1.8-3 | 0.9-1.6 |
| Red (Slow) | Over 3 | Over 1.6 |

### LCP (Largest Contentful Paint)
- Measures the time it takes to render the largest element (e.g., image, text block, video) visible within the viewport, from when the user first navigates to the page.
- The larger the area an element occupies on the screen, the more likely it is perceived as the main content by the user.
- When the LCP element is an image, the time can be broken down into four sub-parts. It's important to identify which of these is causing a bottleneck:
  1. Time to first byte (TTFB): The time from the start of the page load until the first byte of the HTML document response is received.
  2. Load delay: The difference between TTFB and when the browser starts loading the LCP resource.
  3. Load time: The time it took to load the LCP resource itself.
  4. Render delay: The time from when the LCP resource finished loading until the LCP element is fully rendered.

#### Lighthouse Scoring
According to the [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), the Lighthouse scoring is as follows:

| Color Grade | Mobile LCP (seconds) | Desktop LCP (seconds) |
| --- | --- | --- |
| Green (Fast) | 0-2.5 | 0-1.2 |
| Orange (Moderate) | 2.5-4 | 1.2-2.4 |
| Red (Slow) | Over 4 | Over 2.4 |

### TBT (Total Blocking Time)
- Measures the total amount of time that a page is blocked from responding to user input, such as mouse clicks, screen taps, or keyboard presses.
- It is the sum of the *blocking portion* of all [long tasks](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) between First Contentful Paint (FCP) and [Time to Interactive (TTI)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})*. A long task is any task that runs for more than 50ms. The blocking portion is the excess time beyond 50ms.

> \* TTI itself is overly sensitive to network response outliers and long tasks, leading to low consistency and high variability. Consequently, [it was removed from the performance scoring in Lighthouse 10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> The most common cause of long tasks is unnecessary or inefficient JavaScript loading, parsing, and execution. Both the [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) and [Google's web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recommend reducing JavaScript payload size through [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) so that each part can execute within 50ms. If necessary, consider offloading tasks from the main thread to a separate service worker for multithreaded execution.
{: .prompt-tip }

#### Lighthouse Scoring
According to the [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), the Lighthouse scoring is as follows:

| Color Grade | Mobile TBT (milliseconds) | Desktop TBT (milliseconds) |
| --- | --- | --- |
| Green (Fast) | 0-200 | 0-150 |
| Orange (Moderate) | 200-600 | 150-350 |
| Red (Slow) | Over 600 | Over 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Example of a sudden layout shift" autoplay=true loop=true %}
> Video source: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~You can feel the deep rage in the cursor movement~~

- Unexpected layout shifts can harm the user experience in various ways, such as causing users to lose their place while reading when text suddenly moves, or making them click on the wrong link or button.
- The specific method for calculating the CLS score is described on [Google's web.dev](https://web.dev/articles/cls).
- As you can see in the image below, you should aim for a score of 0.1 or less.

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Image source: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Measures how quickly content is visually displayed during page load.
- Lighthouse records a video of the page loading in the browser, analyzes it to calculate the progress between frames, and then uses the [Speedline Node.js module](https://github.com/paulirish/speedline) to calculate the SI score.

> Any measure that improves page loading speed, including those mentioned earlier for [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint), and [TBT](#tbt-total-blocking-time), will also positively affect the SI score. It can be seen as a performance metric that reflects the overall loading process to some extent, rather than representing just one specific part of it.
{: .prompt-tip }

#### Lighthouse Scoring
According to the [Chrome Developers documentation](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), the Lighthouse scoring is as follows:

| Color Grade | Mobile SI (seconds) | Desktop SI (seconds) |
| --- | --- | --- |
| Green (Fast) | 0-3.4 | 0-1.3 |
| Orange (Moderate) | 3.4-5.8 | 1.3-2.3 |
| Red (Slow) | Over 5.8 | Over 2.3 |
