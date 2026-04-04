---
title: Viashiria vya utendaji wa wavuti (Web Vitals)
description: "Muhtasari wa Web Vitals pamoja na vigezo vya upimaji na tathmini vya Lighthouse, na ufafanuzi wa maana ya kila kiashiria cha utendaji."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Vipengele vinavyoamua utendaji wa wavuti
Wakati wa kuboresha utendaji wa wavuti, vipengele vinavyoamua utendaji huo vinaweza kugawanywa kwa ujumla katika makundi mawili makubwa: utendaji wa upakiaji na utendaji wa uchoraji (rendering).

### Utendaji wa upakiaji wa HTML
- Muda unaopita tangu ukurasa wa wavuti uombwe kwa mara ya kwanza kutoka kwa seva kupitia mtandao, hadi hati ya HTML ipokelewe na kivinjari kianze kuchora ukurasa
- Huamua ni kwa kasi gani ukurasa unaanza kuonekana
- Huboreshwa kwa mbinu kama kupunguza uelekezaji upya (redirects), kuweka akiba ya majibu ya HTML, kubana rasilimali, na kutumia CDN ipasavyo

### Utendaji wa uchoraji (rendering)
- Muda unaochukuliwa na kivinjari kuchora kile mtumiaji anachoona kwenye skrini na kukifanya kiweze kuingiliana
- Huamua ni kwa ulaini na kasi gani skrini huchorwa
- Huboreshwa kwa mbinu kama kuondoa CSS na JS zisizo za lazima, kuzuia ucheleweshaji wa kupakia fonti na vijipicha, kutenganisha hesabu nzito kwenye Web Worker tofauti ili kupunguza umiliki wa main thread, na kuboresha animashen

## Viashiria vya utendaji wa wavuti (Web Vitals)
Maelezo yafuatayo yanategemea [web.dev ya Google](https://web.dev/performance?hl={{ site.active_lang }}) na [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Isipokuwa kama kuna sababu maalum, ni bora kulenga uboreshaji wa jumla badala ya kuzingatia kiashiria kimoja tu cha utendaji, na ni muhimu kutambua ni sehemu gani ya ukurasa wa wavuti unaotaka kuboresha inayosababisha kikwazo cha utendaji. Pia, ikiwa kuna takwimu za data halisi za watumiaji, ni vyema zaidi kuzingatia thamani za sehemu ya chini kama Q1 kuliko thamani za juu au wastani, kisha kuthibitisha na kuboresha iwapo viwango lengwa vinatimizwa hata katika hali hizo.

### Viashiria muhimu vya utendaji wa wavuti (Core Web Vitals)
Tutavijadili baada ya muda mfupi, lakini Web Vitals ina viashiria mbalimbali. Hata hivyo, kati ya hivyo, Google huvitazama viashiria vitatu vifuatavyo kuwa muhimu hasa kwa sababu vina uhusiano wa karibu na uzoefu wa mtumiaji na vinaweza kupimwa katika mazingira halisi, si ya majaribio pekee; hivi ndivyo vinavyoitwa [Viashiria muhimu vya utendaji wa wavuti (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Kwa kuwa Google pia hujumuisha Core Web Vitals za tovuti katika mpangilio wa matokeo ya injini yake ya utafutaji, viashiria hivi pia vinapaswa kuangaliwa kwa makini na waendeshaji wa tovuti kwa mtazamo wa uboreshaji wa injini za utafutaji (SEO).
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): *huakisi utendaji wa upakiaji*, inapaswa kuwa ndani ya sekunde 2.5
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): *huakisi mwitikio*, inapaswa kuwa 200ms au chini
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): *huakisi uthabiti wa mwonekano*, inapaswa kubaki 0.1 au chini

Core Web Vitals kimsingi zimekusudiwa kupimwa katika mazingira halisi, lakini isipokuwa INP, viwili vilivyosalia vinaweza pia kupimwa katika mazingira ya majaribio kama Chrome DevTools au Lighthouse. Kwa INP, lazima kuwe na ingizo halisi la mtumiaji ndipo iweze kupimwa, hivyo haiwezi kupimwa katika mazingira ya majaribio; hata hivyo, katika hali kama hizo [TBT](#tbt-total-blocking-time) ni kiashiria cha utendaji chenye uhusiano mkubwa na kinachofanana sana na INP, hivyo kinaweza kutumika kama mbadala, na [kwa kawaida ukiboresha TBT, INP pia huboreka pamoja nayo](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Uzito wa alama ya utendaji katika Lighthouse 10
[Alama ya utendaji ya Lighthouse huhesabiwa kama wastani wenye uzito wa alama za kila kipimo, na katika kufanya hivyo hutumia uzito uliopo kwenye jedwali lifuatalo](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Kipimo | Uzito |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Hupima muda unaochukuliwa tangu ukurasa uombwe hadi maudhui ya kwanza ya DOM yachorwe
- Picha ndani ya ukurasa, kipengele cha `<canvas>` kisicho cheupe, SVG, n.k. huhesabiwa kama maudhui ya DOM, lakini maudhui ndani ya `iframe` hayazingatiwi

> Moja ya vipengele vinavyoathiri FCP kwa umuhimu wa pekee ni muda wa kupakia fonti; kuhusu uboreshaji wake, [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) zinapendekeza kurejelea [chapisho husika](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Vigezo vya tathmini vya Lighthouse
Kulingana na [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), vigezo vya tathmini vya Lighthouse ni kama ilivyo kwenye jedwali lifuatalo.

| Daraja la rangi | FCP ya simu (sekunde) | FCP ya desktop (sekunde) |
| --- | --- | --- |
| Kijani (haraka) | 0-1.8 | 0-0.9 |
| Machungwa (wastani) | 1.8-3 | 0.9-1.6 |
| Nyekundu (polepole) | zaidi ya 3 | zaidi ya 1.6 |

### LCP (Largest Contentful Paint)
- Hupima muda unaochukuliwa kuchora kipengele kinachoonekana kwa ukubwa zaidi ndani ya eneo la mwonekano (viewport) linaloonekana kwanza unapofungua ukurasa wa wavuti, kama vile picha, blokki ya maandishi, au video
- Kadiri eneo linalochukuliwa kwenye skrini linavyokuwa kubwa, ndivyo uwezekano unavyoongezeka kwamba mtumiaji atakihisi kama maudhui muhimu
- Ikiwa LCP ni picha, muda huo unaweza kugawanywa katika sehemu ndogo 4, na ni muhimu kutambua ni sehemu gani hasa yenye kikwazo
  1. Time to first byte (TTFB): muda tangu kuanza kwa upakiaji wa ukurasa hadi kupokelewa kwa byte ya kwanza ya majibu ya hati ya HTML
  2. Ucheleweshaji wa upakiaji (Load delay): tofauti kati ya TTFB na wakati kivinjari kilipoanza kupakia rasilimali ya LCP
  3. Muda wa upakiaji (Load time): muda uliochukuliwa kupakia rasilimali yenyewe ya LCP
  4. Ucheleweshaji wa uchoraji (Render delay): muda tangu upakiaji wa rasilimali ya LCP ukamilike hadi kipengele cha LCP kichorwe kikamilifu

#### Vigezo vya tathmini vya Lighthouse
Kulingana na [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), vigezo vya tathmini vya Lighthouse ni kama ilivyo kwenye jedwali lifuatalo.

| Daraja la rangi | LCP ya simu (sekunde) | LCP ya desktop (sekunde) |
| --- | --- | --- |
| Kijani (haraka) | 0-2.5 | 0-1.2 |
| Machungwa (wastani) | 2.5-4 | 1.2-2.4 |
| Nyekundu (polepole) | zaidi ya 4 | zaidi ya 2.4 |

### TBT (Total Blocking Time)
- Hupima jumla ya muda ambao ukurasa wa wavuti hauwezi kujibu ingizo la mtumiaji kama kubofya kwa kipanya, mguso wa skrini, au uingizaji wa kibodi
- Miongoni mwa kazi zinazofanyika kati ya FCP na [TTI (wakati wa kuanza kuingiliana, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, kazi zinazochukua zaidi ya 50ms huzingatiwa kuwa [kazi ndefu](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}); kwa kila kazi ndefu, sehemu ya muda inayozidi 50ms huitwa *sehemu ya kuzuia (blocking portion)*, na jumla ya sehemu zote za kuzuia hufafanuliwa kama TBT

> \* TTI yenyewe ni nyeti kupita kiasi kwa thamani za ajabu za majibu ya mtandao na kwa kazi ndefu, hivyo ina uthabiti mdogo na mabadiliko makubwa; kwa sababu hiyo, [kuanzia Lighthouse 10 imeondolewa kwenye vipengele vya tathmini ya utendaji](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Kwa ujumla, sababu ya kawaida zaidi ya kuzua kazi ndefu ni kupakia, kuchanganua, na kutekeleza JavaScript isiyo ya lazima au isiyofaa; [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) na [web.dev ya Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) zinapendekeza kupunguza ukubwa wa payload ya JavaScript kupitia [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) ili kila sehemu iweze kutekelezwa ndani ya 50ms, na ikihitajika kuzingatia kuitenganisha kwenye service worker tofauti badala ya main thread ili itekelezwe kwa multithread.
{: .prompt-tip }

#### Vigezo vya tathmini vya Lighthouse
Kulingana na [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), vigezo vya tathmini vya Lighthouse ni kama ilivyo kwenye jedwali lifuatalo.

| Daraja la rangi | TBT ya simu (milisekunde) | TBT ya desktop (milisekunde) |
| --- | --- | --- |
| Kijani (haraka) | 0-200 | 0-150 |
| Machungwa (wastani) | 200-600 | 150-350 |
| Nyekundu (polepole) | zaidi ya 600 | zaidi ya 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Mfano wa mabadiliko ya ghafla ya mpangilio" autoplay=true loop=true %}
> Chanzo cha video: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Hasira nzito inahisiwa kwenye mwendo wa kishale~~

- Mabadiliko ya mpangilio yasiyotarajiwa huharibu uzoefu wa mtumiaji kwa njia mbalimbali, kama kusababisha maandishi kuhama ghafla na kumfanya mtumiaji apoteze sehemu aliyokuwa akisoma, au kubofya kiungo au kitufe kisicho sahihi
- Mbinu mahususi ya kukokotoa alama ya CLS imeelezwa katika [web.dev ya Google](https://web.dev/articles/cls)
- Kama inavyoonekana kwenye picha hapa chini, lengo linapaswa kuwa 0.1 au chini

![What is a good CLS score?](https://web.dev/static/articles/cls/image/good-cls-values.svg){: width="640" height="480" }
> Chanzo cha picha: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Hupima jinsi maudhui yanavyoanza kuonekana kwa haraka kwenye mwonekano wakati ukurasa unapakia
- Lighthouse hurekodi video ya mchakato wa kupakia ukurasa kwenye kivinjari, huchanganua video hiyo kukokotoa maendeleo kati ya fremu, kisha hutumia [moduli ya Node.js ya Speedline](https://github.com/paulirish/speedline) kukokotoa alama ya SI

> Pamoja na yale yaliyotajwa awali wakati wa kufupisha [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint), na [TBT](#tbt-total-blocking-time), hatua yoyote inayoboresha kasi ya upakiaji wa ukurasa pia huathiri kwa njia chanya alama ya SI. Badala ya kuwakilisha hatua moja tu ya upakiaji wa ukurasa, inaweza kuonekana kama kiashiria cha utendaji kinachoakisi kwa kiwango fulani mchakato mzima wa upakiaji.
{: .prompt-tip }

#### Vigezo vya tathmini vya Lighthouse
Kulingana na [nyaraka za wasanidi wa Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), vigezo vya tathmini vya Lighthouse ni kama ilivyo kwenye jedwali lifuatalo.

| Daraja la rangi | SI ya simu (sekunde) | SI ya desktop (sekunde) |
| --- | --- | --- |
| Kijani (haraka) | 0-3.4 | 0-1.3 |
| Machungwa (wastani) | 3.4-5.8 | 1.3-2.3 |
| Nyekundu (polepole) | zaidi ya 5.8 | zaidi ya 2.3 |
