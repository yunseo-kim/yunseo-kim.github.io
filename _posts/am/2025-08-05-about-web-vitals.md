---
title: የድር አፈጻጸም መለኪያዎች (Web Vitals)
description: "የድር አፈጻጸም መለኪያዎች(Web Vitals) እና የLighthouse መለኪያና ግምገማ መስፈርቶችን በማጠቃለል፣ እያንዳንዱ የአፈጻጸም መለኪያ ምን እንደሚያመለክት እንመለከታለን።"
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## የድር አፈጻጸምን የሚወስኑ ነገሮች
የድር አፈጻጸም ማሻሻያን ሲያደርጉ ሊጠበቁ የሚገቡ የድር አፈጻጸምን የሚወስኑ ነገሮች በአጠቃላይ ወደ ሁለት ክፍሎች ሊከፈሉ ይችላሉ፤ የመጫን አፈጻጸም እና የሬንደሪንግ አፈጻጸም።

### የHTML መጫን አፈጻጸም
- በኔትወርክ አማካኝነት ለመጀመሪያ ጊዜ የድር ገጹን ከሰርቨር ከጠየቀ በኋላ፣ የHTML ሰነዱን እስኪቀበል እና አሳሹ ሬንደሪንግ መጀመር እስከሚጀምር ያለውን ጊዜ ይለካል
- ገጹ ምን ያህል ፈጥኖ መታየት እንደሚጀምር ይወስናል
- እንደ redirect መቀነስ፣ የHTML ምላሽ caching፣ የምንጭ መጨመቅ፣ ተገቢ CDN መጠቀም ባሉ መንገዶች ማሻሻል ይቻላል

### የሬንደሪንግ አፈጻጸም
- አሳሹ ተጠቃሚው የሚያየውን ማያ ገጽ ለመሳል እና ከእሱ ጋር እንዲገናኝ ለማድረግ የሚፈጅበት ጊዜ
- ማያ ገጹ ምን ያህል ለስላሳና ፈጣን እንደሚሳል ይወስናል
- አላስፈላጊ CSS እና JS ማስወገድ፣ የፎንትና የthumbnail ዘግይቶ መጫን መከላከል፣ ከባድ ስሌቶችን ወደ ተለየ Web Worker መለየት በማድረግ የmain thread ተይዞታን መቀነስ፣ አኒሜሽን ማሻሻል ወዘተ ባሉ መንገዶች ማሻሻል ይቻላል

## የድር አፈጻጸም መለኪያዎች (Web Vitals)
በGoogle ၏ [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) እና [የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}) ላይ ተመስርቶ ይቀርባል። ልዩ ምክንያት ከሌለ ከአንድ ብቻ የአፈጻጸም መለኪያ ላይ ከማተኮር ይልቅ አጠቃላይ ማሻሻያን መድረስ የተሻለ ነው፣ እና ማሻሻል በሚፈልጉት ድረ ገጽ ውስጥ የትኛው ክፍል የአፈጻጸም መከለያ እንደሆነ ማወቅ አስፈላጊ ነው። እንዲሁም የእውነተኛ ተጠቃሚ ውሂብ ስታቲስቲክስ ካለ፣ ከላይ የሚገኙ ወይም አማካይ እሴቶች ይልቅ Q1 ያሉ ዝቅተኛ እሴቶችን መመልከት እና በእነዚያ ሁኔታዎችም የዒላማ መስፈርት መድረሱን ማረጋገጥ ከዚያም ማሻሻል የተሻለ ነው።

### ዋና የድር አፈጻጸም መለኪያዎች (Core Web Vitals)
ቆይቶ እናየዋለን ቢሆንም በድር አፈጻጸም መለኪያዎች(Web Vitals) ውስጥ ብዙ አይነቶች አሉ። ግን ከእነዚህ መካከል በተለይ ከተጠቃሚ ልምድ ጋር በጣም ቅርብ ግንኙነት ያላቸው እና በሙከራ አካባቢ ሳይሆን በእውነተኛ አካባቢ ሊለኩ የሚችሉትን የሚከተሉትን 3 መለኪያዎች Google በተለይ አስፈላጊ ብሎ ይቆጥራቸዋል፣ እነዚህንም [ዋና የድር አፈጻጸም መለኪያዎች(Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals) ብሎ ይጠራቸዋል። Google በራሱ የፍለጋ ሞተር የፍለጋ ውጤት ቅደም ተከተል ውስጥም የተመረጠው ድረ ገጽ ዋና የድር አፈጻጸም መለኪያዎችን ስለሚያካትት፣ ከጣቢያ አስተዳዳሪ እይታ አንጻርም እነዚህ መለኪያዎች በፍለጋ ሞተር ማሻሻያ(SEO) አንጻር በጥንቃቄ ሊታዩ ይገባል።
- [Largest Contentful Paint (LCP)](#lcp-ትልቁ-የይዘት-ስዕል-largest-contentful-paint): *የመጫን አፈጻጸም*ን ያንጸባርቃል፣ በ2.5 ሰከንድ ውስጥ መሆን አለበት
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): *ምላሽ ሰጪነት*ን ያንጸባርቃል፣ 200ms ወይም ከዚያ በታች መሆን አለበት
- [Cummulative Layout Shift (CLS)](#cls-ድምር-የአቀማመጥ-መንቀሳቀስ-cumulative-layout-shift): *እይታዊ መረጋጋት*ን ያንጸባርቃል፣ ከ0.1 በታች መጠበቅ አለበት

ዋና የድር አፈጻጸም መለኪያዎች በመሠረቱ በእውነተኛ አካባቢ ለመለካት የተዘጋጁ ቢሆኑም፣ INP ን ካልተቀረ ሌሎቹ ሁለቱ በChrome የገንቢ መሣሪያዎች ወይም Lighthouse ያሉ የሙከራ አካባቢዎች ውስጥም ሊለኩ ይችላሉ። INP ግን እውነተኛ የተጠቃሚ ግብዓት ሲሰጥ ብቻ ሊለካ ስለሚችል በሙከራ አካባቢ ሊለካ አይችልም፤ በእንዲህ ሁኔታ [TBT](#tbt-ጠቅላላ-የማገጃ-ጊዜ-total-blocking-time) ከINP ጋር በጣም ከፍተኛ የተዛማጅነት እና ተመሳሳይ የአፈጻጸም መለኪያ ስለሆነ በምትኩ መጠቀም ይቻላል፣ እና [በብዙ ጊዜ TBT ሲሻሻል INP ደግሞ አብሮ ይሻሻላል](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals)።

### የLighthouse 10 የአፈጻጸም ነጥብ ክብደቶች
[Lighthouse የአፈጻጸም ነጥብ በእያንዳንዱ የመለኪያ ንጥል ነጥብ የተመዘነ አማካይ በመሆን ይሰላል፣ እና በዚህ ጊዜ የሚከተለውን ሰንጠረዥ ክብደት ይከተላል](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})።

| የመለኪያ ንጥል | ክብደት |
| --- | --- |
| [First Contentful Paint](#fcp-የመጀመሪያ-ይዘታዊ-ስዕል-first-contentful-paint) | 10% |
| [Speed Index](#si-የፍጥነት-መረጃ-ጠቋሚ-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-ትልቁ-የይዘት-ስዕል-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-ጠቅላላ-የማገጃ-ጊዜ-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-ድምር-የአቀማመጥ-መንቀሳቀስ-cumulative-layout-shift) | 25% |

### FCP (የመጀመሪያ ይዘታዊ ስዕል, First Contentful Paint)
- ገጹ ከተጠየቀ በኋላ የመጀመሪያው DOM ይዘት እስኪሬንደር ድረስ የሚፈጅውን ጊዜ ይለካል
- በገጹ ውስጥ ያሉ ምስሎች፣ ነጭ ያልሆነ `<canvas>` ኤለመንት፣ SVG ወዘተን እንደ DOM ይዘት ይቆጥራል፣ ነገር ግን በ`iframe` ውስጥ ያለ ይዘትን አያካትትም

> FCP ላይ በተለይ አስፈላጊ ተጽእኖ ከሚያሳድሩ ነገሮች አንዱ የፎንት መጫን ጊዜ ሲሆን፣ ስለዚህ የማሻሻያ መንገዶች [ተዛማጅ ፖስት](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) ላይ እንዲመለከቱ [የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) ይመክራሉ።
{: .prompt-tip }

#### የLighthouse ግምገማ መስፈርት
[የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) መሰረት፣ የLighthouse ግምገማ መስፈርት የሚከተለው ሰንጠረዥ ነው።

| የቀለም ደረጃ | ሞባይል FCP (ሰከንድ) | ዴስክቶፕ FCP (ሰከንድ) |
| --- | --- | --- |
| አረንጓዴ (ፈጣን) | 0-1.8 | 0-0.9 |
| ብርቱካናማ (መካከለኛ) | 1.8-3 | 0.9-1.6 |
| ቀይ (ዝግ) | ከ3 በላይ | ከ1.6 በላይ |

### LCP (ትልቁ የይዘት ስዕል, Largest Contentful Paint)
- ድረ ገጹን ለመጀመሪያ ጊዜ ሲከፍቱት፣ በመጀመሪያ በማያ ገጹ ላይ የሚታየውን የማሳያ ክልል(viewport) መሠረት በማድረግ፣ በዚያ ክልል ውስጥ በጣም ትልቅ ተደርጎ የሚታየውን ኤለመንት(ምስል፣ የጽሑፍ ብሎክ፣ ቪዲዮ ወዘተ) ለመሬንደር የሚፈጅውን ጊዜ ይለካል
- በማያ ገጹ ላይ የሚይዘው ስፋት በጣም ሰፊ ከሆነ ከተጠቃሚ አንጻር እንደ ዋና ይዘት የሚሰማው እድል ከፍ ይላል
- LCP ምስል ከሆነ፣ የተወሰነው ጊዜ ወደ 4 ንዑስ ክፍሎች ሊከፈል ይችላል፣ ከእነዚህም ውስጥ መከለያ የሚፈጠረው የት እንደሆነ መረዳት አስፈላጊ ነው
  1. Time to first byte (TTFB): ገጽ መጫን ከጀመረበት ጊዜ ጀምሮ የHTML ሰነድ ምላሽ የመጀመሪያው ባይት እስኪደርስ ድረስ ያለው ጊዜ
  2. የመጫን መዘግየት(Load delay): አሳሹ የLCP ምንጩን መጫን ጀመረበት ጊዜ እና TTFB መካከል ያለው ልዩነት
  3. የመጫን ጊዜ(Load time): የLCP ምንጩን ራሱን ለመጫን የፈጀው ጊዜ
  4. የሬንደሪንግ መዘግየት(Render delay): የLCP ምንጩ መጫኑ ከተጠናቀቀበት ጊዜ ጀምሮ የLCP ኤለመንቱ ሙሉ በሙሉ እስኪሬንደር ድረስ ያለው ጊዜ

#### የLighthouse ግምገማ መስፈርት
[የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}) መሰረት፣ የLighthouse ግምገማ መስፈርት የሚከተለው ሰንጠረዥ ነው።

| የቀለም ደረጃ | ሞባይል LCP (ሰከንድ) | ዴስክቶፕ LCP (ሰከንድ) |
| --- | --- | --- |
| አረንጓዴ (ፈጣን) | 0-2.5 | 0-1.2 |
| ብርቱካናማ (መካከለኛ) | 2.5-4 | 1.2-2.4 |
| ቀይ (ዝግ) | ከ4 በላይ | ከ2.4 በላይ |

### TBT (ጠቅላላ የማገጃ ጊዜ, Total Blocking Time)
- ድረ ገጹ እንደ የአይጥ ጠቅታ፣ የማያ ገጽ ንክኪ፣ የቁልፍ ሰሌዳ ግቤት ያሉ የተጠቃሚ ግብዓቶችን መልስ ለመስጠት ያልቻለበትን ጠቅላላ ጊዜ ይለካል
- በFCP እና [TTI(የመስተጋብር መጀመሪያ ጊዜ, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* መካከል ካሉ ስራዎች ውስጥ 50ms ወይም ከዚያ በላይ የተካሄዱ ስራዎችን [ረጅም ስራዎች](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) ብሎ ይቆጥራል፣ እና እነዚህ ረጅም ስራዎች እያንዳንዳቸው የፈጀው ጊዜ ውስጥ 50ms በመቀነስ የሚቀረውን ተጨማሪ ክፍል *የማገጃ ክፍል(blocking portion)* ብሎ ይጠራል፣ የሁሉንም የማገጃ ክፍሎች ድምርንም TBT ብሎ ይገልጻል

> \* TTI ራሱ በኔትወርክ ምላሽ ውጪ እሴቶች እና በረጅም ስራዎች ላይ እጅግ ስሜታዊ ስለሆነ፣ ተመሳሳይነቱ ዝቅተኛ እና መለዋወጡ ከፍተኛ ነው፤ በዚህ ምክንያት [ከLighthouse 10 ጀምሮ ከአፈጻጸም ግምገማ ንጥሎች ተወግዷል](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes)።
{: .prompt-info }

> በአጠቃላይ ረጅም ስራዎችን የሚያስከትለው በጣም የተለመደ ምክንያት አላስፈላጊ ወይም ውጤታማ ያልሆነ JavaScript መጫን፣ መተንተን እና ማስኬድ ነው፤ [ኮድ መከፋፈል](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) በመጠቀም የJavaScript payload መጠንን በመቀነስ እያንዳንዱ በ50ms ውስጥ እንዲፈጸም ማድረግ፣ አስፈላጊ ከሆነም ከmain thread ውጪ ወደ ተለየ service worker በመለየት በmultithread እንዲሰራ ማድረግ እንዲያስቡ [የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) እና [Google ၏ web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) ይመክራሉ።
{: .prompt-tip }

#### የLighthouse ግምገማ መስፈርት
[የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) መሰረት፣ የLighthouse ግምገማ መስፈርት የሚከተለው ሰንጠረዥ ነው።

| የቀለም ደረጃ | ሞባይል TBT (ሚሊሰከንድ) | ዴስክቶፕ TBT (ሚሊሰከንድ) |
| --- | --- | --- |
| አረንጓዴ (ፈጣን) | 0-200 | 0-150 |
| ብርቱካናማ (መካከለኛ) | 200-600 | 150-350 |
| ቀይ (ዝግ) | ከ600 በላይ | ከ350 በላይ |

### CLS (ድምር የአቀማመጥ መንቀሳቀስ, Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="ድንገተኛ የአቀማመጥ ለውጥ ምሳሌ" autoplay=true loop=true %}
> የቪዲዮ ምንጭ: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~በcursor እንቅስቃሴው ውስጥ ጥልቅ ቁጣ ይሰማል~~

- ያልተጠበቀ የአቀማመጥ ለውጥ ጽሑፉ በድንገት እንዲንቀሳቀስ በማድረግ እያነበቡ የነበሩበትን ቦታ እንዲያጡ ወይም ሊንክ ወይም አዝራር በስህተት እንዲጫኑ እና በሌሎችም ብዙ መንገዶች የተጠቃሚ ልምድን ያበላሻል
- የCLS ነጥብ የሚሰላበት ዝርዝር መንገድ በ[Google ၏ web.dev](https://web.dev/articles/cls) ላይ ተገልጿል
- ከታች ባለው ምስል እንደሚታየው፣ 0.1 ወይም ከዚያ በታች መድረስ ዒላማ መሆን አለበት

![What is a good CLS score?](https://web.dev/static/articles/cls/image/good-cls-values.svg){: width="640" height="480" }
> የምስል ምንጭ: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (የፍጥነት መረጃ ጠቋሚ, Speed Index)
- ገጹ እየተጫነ ሳለ ይዘቱ በእይታ ምን ያህል ፈጥኖ እንደሚታይ ይለካል
- Lighthouse በአሳሹ ውስጥ ገጹ የሚጫነበትን ሂደት እንደ ቪዲዮ ይቀርጻል፣ ያንንም ቪዲዮ በመተንተን በframe መካከል ያለውን እድገት ከሰላ በኋላ [Speedline Node.js module](https://github.com/paulirish/speedline) በመጠቀም የSI ነጥብን ይሰላል

> ከዚህ በፊት [FCP](#fcp-የመጀመሪያ-ይዘታዊ-ስዕል-first-contentful-paint)፣ [LCP](#lcp-ትልቁ-የይዘት-ስዕል-largest-contentful-paint)፣ [TBT](#tbt-ጠቅላላ-የማገጃ-ጊዜ-total-blocking-time) ላይ ሲዘረዝሩ የተጠቀሱትን ጨምሮ፣ የገጽ መጫን ፍጥነትን ለማሻሻል የሚወሰድ ማንኛውም እርምጃ በSI ነጥብ ላይም አዎንታዊ ተጽእኖ ይኖረዋል። ከገጽ መጫን ሂደት ውስጥ አንድ የተወሰነ ክፍልን ብቻ ከመወከል ይልቅ፣ አጠቃላይ የመጫን ሂደቱን በተወሰነ ደረጃ የሚያንጸባርቅ የአፈጻጸም መለኪያ ነው ማለት ይቻላል።
{: .prompt-tip }

#### የLighthouse ግምገማ መስፈርት
[የChrome የገንቢ ሰነዶች](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}) መሰረት፣ የLighthouse ግምገማ መስፈርት የሚከተለው ሰንጠረዥ ነው።

| የቀለም ደረጃ | ሞባይል SI (ሰከንድ) | ዴስክቶፕ SI (ሰከንድ) |
| --- | --- | --- |
| አረንጓዴ (ፈጣን) | 0-3.4 | 0-1.3 |
| ብርቱካናማ (መካከለኛ) | 3.4-5.8 | 1.3-2.3 |
| ቀይ (ዝግ) | ከ5.8 በላይ | ከ2.3 በላይ |
