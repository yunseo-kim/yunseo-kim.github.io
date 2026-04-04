---
title: "በPolyglot በመጠቀም በJekyll ብሎግ ውስጥ ብዙ ቋንቋ ድጋፍ እንዴት እንደሚጨምሩ (2) - የቋንቋ ምርጫ አዝራር መተግበር & የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግ"
description: "'jekyll-theme-chirpy' ላይ የተመሠረተ Jekyll ብሎግ ላይ Polyglot ፕላግን በመተግበር ብዙ ቋንቋ ድጋፍ እንዴት እንደተገነባ ያብራራል። ይህ የተከታታይ ጽሑፎች ሁለተኛው ጽሑፍ ሲሆን የቋንቋ ምርጫ አዝራር መተግበርና የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግን ይሸፍናል።"
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## አጠቃላይ እይታ
በ12024 ዓ.ም. ጁላይ መጀመሪያ ላይ፣ በGithub Pages በኩል የሚስተናገድ ይህ በJekyll የተመሠረተ ብሎግ ላይ [Polyglot](https://github.com/untra/polyglot) ፕላግን በመተግበር ብዙ ቋንቋ ድጋፍ አክዬበታለሁ።
ይህ ተከታታይ ጽሑፎች በChirpy ገጽታ ላይ Polyglot ፕላግን ሲተገበር የተፈጠሩ ችግኞችን እና የመፍትሄ ሂደታቸውን፣ እንዲሁም SEO ን በማሰብ html ሄደር እና sitemap.xml እንዴት እንደሚጻፉ ያጋራል።
ይህ ተከታታይ 3 ጽሑፎችን ያካትታል፣ እያነበቡት ያሉትም ይህ ጽሑፍ ሁለተኛው ነው።
- ክፍል 1: [Polyglot ፕላግን መተግበር & html ሄደር እና sitemap ማስተካከል](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- ክፍል 2: የቋንቋ ምርጫ አዝራር መተግበር & የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግ (ይህ ጽሑፍ)
- ክፍል 3: [የChirpy ገጽታ ግንባታ መሳካት አለመቻል እና የፍለጋ ባህሪ ስህተት መላ መፈለግ](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> በመጀመሪያ በአጠቃላይ 2 ክፍሎች ብቻ እንዲሆን አድርጌ ነበር፣ ነገር ግን ከዚያ በኋላ በበርካታ ዙሮች ይዘቱን እየጨመርኩ ስሄድ መጠኑ እጅግ ስለጨመረ ወደ 3 ክፍሎች እንዲሆን አሻሽዬዋለሁ።
{: .prompt-info }

## መስፈርቶች
- [x] የገነባው ውጤት(ድረ ገጽ) በቋንቋ ልዩ መንገዶች(ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}) ተለይቶ መቅረብ አለበት።
- [x] ለብዙ ቋንቋ ድጋፍ ተጨማሪ የሚፈልገውን ጊዜና ጉልበት እስከሚቻል ድረስ ለመቀነስ፣ በተጻፈው የመጀመሪያ የMarkdown ፋይል YAML front matter ውስጥ 'lang' እና 'permalink' ታጎችን በእያንዳንዱ ፋይል ላይ በተናጠል ማስገባት ሳያስፈልግ፣ በግንባታ ጊዜ ፋይሉ ያለበትን አካባቢያዊ መንገድ(ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) መሰረት በማድረግ ቋንቋውን በራሱ መለየት መቻል አለበት።
- [x] በጣቢያው ውስጥ ያሉ እያንዳንዱ ገጽ ሄደር ክፍሎች ተገቢ Content-Language ሜታ ታግ፣ hreflang ተለዋጭ ታጎች እና canonical አገናኝ በመያዝ ለብዙ ቋንቋ ፍለጋ የGoogle SEO መመሪያዎችን ማሟላት አለባቸው።
- [x] በጣቢያው ውስጥ ያሉ የእያንዳንዱ ቋንቋ ስሪት ገጽ አገናኞች ምንም ሳይቀሩ በ`sitemap.xml`{: .filepath} መቅረብ አለባቸው፣ እና `sitemap.xml`{: .filepath} ራሱ በስር መንገድ ላይ ብቻ አንድ መኖር አለበት።
- [x] በ[Chirpy ገጽታ](https://github.com/cotes2020/jekyll-theme-chirpy) የሚሰጡ ሁሉም ባህሪዎች በእያንዳንዱ ቋንቋ ገጽ ላይ በመደበኛነት መስራት አለባቸው፣ ካልሆነም እንዲሰሩ ማስተካከል አለበት።
  - [x] 'Recently Updated', 'Trending Tags' ባህሪዎች በመደበኛነት መስራት
  - [x] GitHub Actions በመጠቀም በሚካሄደው የግንባታ ሂደት ውስጥ ስህተት እንዳይፈጠር
  - [x] በብሎጉ በላይ ቀኝ ጠርዝ ያለው የፖስት ፍለጋ ባህሪ በመደበኛነት መስራት

## ከመጀመርዎ በፊት
ይህ ጽሑፍ ከ[ክፍል 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1) የሚቀጥል ስለሆነ፣ እስካሁን ካላነበቡት በመጀመሪያ ያለፈውን ጽሑፍ እንዲያነቡ እመክራለሁ።

## በጎን አሞሌ ውስጥ የቋንቋ ምርጫ አዝራር መጨመር
> (12025.02.05. ዝማኔ) የቋንቋ ምርጫ አዝራሩ ወደ dropdown ዝርዝር ቅርጽ ተሻሽሏል።
{: .prompt-info }

`_includes/lang-selector.html`{: .filepath} ፋይል ፈጥሬ እንደሚከተለው ይዘት ጻፍሁበት።

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Select Language">
    {%- for lang in site.languages -%}
        <option value="{% if lang == site.default_lang %}{{ page.url }}{% else %}/{{ lang }}{{ page.url }}{% endif %}"
                {% if lang == site.active_lang %}selected{% endif %}>
            {% case lang %}
            {% when 'ko' %}🇰🇷 한국어
            {% when 'en' %}🇺🇸 English
            {% when 'ja' %}🇯🇵 日本語
            {% when 'zh-TW' %}🇹🇼 正體中文
            {% when 'es' %}🇪🇸 Español
            {% when 'pt-BR' %}🇧🇷 Português
            {% when 'fr' %}🇫🇷 Français
            {% when 'de' %}🇩🇪 Deutsch
            {% else %}{{ lang }}
            {% endcase %}
        </option>
    {%- endfor -%}
    </select>
</div>

<script>
function changeLang(url) {
    window.location.href = url;
}
</script>
```
{: file='\_includes/lang-selector.html'}
{% endraw %}

እንዲሁም `assets/css/lang-selector.css`{: .filepath} ፋይል ፈጥሬ እንደሚከተለው ይዘት ጻፍሁበት።

```css
/**
 * የቋንቋ ምርጫ አስመራጭ ስታይል
 * 
 * በጎን አሞሌ ውስጥ የሚገኘውን የቋንቋ ምርጫ dropdown ስታይል ይገልጻል።
 * የገጽታውን ጨለማ ሁነታ ይደግፋል፣ እና በሞባይል አካባቢም የተመቻቸ ነው።
 */

/* የቋንቋ ምርጫ አስመራጭ ኮንቴይነር */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* dropdown ኮንቴይነር */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* የምርጫ ግቤት አካል */
.lang-select {
    /* መሠረታዊ ስታይል */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* ፎንት እና ቀለም */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* ቅርጽ እና መስተጋብር */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* የቀስት አዶ መጨመር */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* የሰንደቅ ኢሞጂ ስታይል */
.lang-select option {
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
    padding: 0.35rem;
    font-size: 1rem;
}

.lang-flag {
    display: inline-block;
    margin-right: 0.5rem;
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
}

/* hover ሁኔታ */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* focus ሁኔታ */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefox አሳሽ ተኳኋኝነት */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE አሳሽ ተኳኋኝነት */
.lang-select::-ms-expand {
    display: none;
}

/* ጨለማ ሁነታ ተኳኋኝነት */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* ለሞባይል አካባቢ ማመቻቸት */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* የበለጠ ትልቅ የንክኪ ቦታ */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* በሞባይል ላይ የበለጠ ሰፊ የምርጫ ቦታ */
    }
}
```
{: file='assets/css/lang-selector.css'}

ከዚያ በኋላ፣ [በChirpy ገጽታ ውስጥ ያለው `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) ፋይል ውስጥ `sidebar-bottom` ክፍል በቀጥታ ከመታየቱ በፊት `lang-selector-wrapper` ክፍል ያላቸውን ሦስት መስመሮች እንደሚከተለው አክዬ ነበር፣ ይህም ከዚያ በፊት የጻፍኩትን `_includes/lang-selector.html`{: .filepath} ይዘት Jekyll ገጹን ሲገነባ እንዲጭነው አድርጎታል።

{% raw %}
```liquid
  (전략)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(후략)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (12025.07.31. ባህሪ ተጨምሯል) የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግ
ከዚህ በፊት ቋንቋ አካባቢያዊ ማድረግን በገጽ ርዕስ እና ይዘት ያሉ ዋና የጽሑፍ ክፍሎች ላይ ብቻ እተገብር ነበር፣ በግራ ጎን አሞሌ ያሉ የትሮች ስሞች ወይም የድረ ገጹ ላይኛ እና ታችኛ ክፍሎች እንዲሁም የቀኝ ፓነል ያሉ የአቀማመጥ ቋንቋዎች ግን የጣቢያው ነባሪ እሴት የሆነው እንግሊዝኛ ብቻ እንዲታይ ተደርጓል። በግል አስተያየቴ ያ መጠን በቂ ነበር፣ ስለዚህ ተጨማሪ ስራ ለመስራት አስፈላጊነት እጅግ አልተሰማኝም። ነገር ግን በቅርቡ [ከላይ የተጠቀሱትን Open Graph ሜታዳታ ባህሪዎች እና canonical URL ፓች](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-ሄደር) በማዘጋጀት ሂደት ውስጥ የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግ በጥቂት ማስተካከያ ብቻ በጣም ቀላል መሆኑን አግኝቻለሁ። ትልቅና አስቸጋሪ የኮድ ማሻሻያ ስራ ቢያስፈልግ ኖሮ እንጂ፣ [ከ10 ደቂቃ እንኳን ያልበለጠ ቀላል ስራ](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb) ስለነበር በአጋጣሚ ይህንም ጨምሬ ተግባራዊ አደረግሁ።

### ሎካል መጨመር
በጣቢያው ውስጥ ለእያንዳንዱ ገጽ ብዙ ቋንቋ ስሪቶችን በአንድ ጊዜ ማቅረብና በተጠቃሚ ምርጫ መሠረት በመካከላቸው መቀያየር ባይኖርም፣ [የChirpy ገጽታ የሚደግፈው የቋንቋ ስፋት ከመጀመሪያውም በጣም ሰፊ ነው](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales)። ስለዚህ ከChirpy ገጽታ የሚሰጡት የሎካል ፋይሎች ውስጥ የሚፈልጉትን ብቻ መርጠው አውርደው ማከል ይችላሉ፣ አስፈላጊ ከሆነም የፋይሉን ስም ብቻ እንዲመጣጠን መቀየር ይችላሉ። የሎካል ፋይል ስሞች ቀደም ሲል [የቅንብር ማዋቀር](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#ቅንብር-ማዋቀር) ደረጃ ላይ `_config.yml`{: .filepath} ፋይል ውስጥ ከተገለጹት `languages` ዝርዝር እቃዎች ጋር መስማማት አለባቸው።

> በእርግጥ በቀጥታ ከዚህ በኋላም እንደምጠቅሰው፣ `_data`{: .filepath} ማውጫ ውስጥ ያሉ ፋይሎች በቀጥታ ሳይጨመሩም [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy) በኩል በነባሪነት ይሰጣሉ።
>
> ግን በእኔ ሁኔታ፣ በሚከተሉት ምክንያቶች Chirpy ገጽታ የሚያቀርበውን ሎካል በቀጥታ መጠቀም አስቸጋሪ ነበር፣ ስለዚህ ጥቂት ማሻሻያዎች ማድረግ አስፈልጎኛል።
> - Chirpy ገጽታ በነባሪነት የሚሰጣቸው የሎካል ፋይሎች ስም ቅርጽ `ko-KR`, `ja-JP` ወዘተ እንደሚሆን የክልል ኮድ ያካትታል፣ ይህም በአሁኑ ጣቢያ ላይ ከምጠቀምበት ቅርጽ(`ko`, `ja` ወዘተ) ጋር አይጣጣምም
> - የፈቃድ ማስታወቂያውን ከነባሪው [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ይልቅ ከዚህ ብሎግ የ[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) ፈቃድ ጋር እንዲስማማ ማስተካከል አስፈልጎኛል
> - [ኮሪያኛ](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) ወይም [ጃፓንኛ](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) ሎካል ፋይሎች እኔ ኮሪያዊ ሰው ስለሆንሁ በማየቴ ትንሽ የማይተፋፈሱ ወይም ለዚህ ብሎግ የማይስማሙ ክፍሎች ነበሩ፣ ስለዚህ በግል ያሻሻልኳቸው ክፍሎች አሉ
> - ከታች እንደገለጽኩት በብዙ ምክንያቶች የክርስቲያን ዘመን ቁጥር ስርዓትን አልወድም፣ እና ቢያንስ በዚህ ብሎግ ላይ የቀን ማሳያ ቅርጽ እንደ [የሆሎሲን ዘመን ቆጠራ](https://en.wikipedia.org/wiki/Holocene_calendar) ስለምጠቀም ሎካሉንም ከዚያ ጋር እንዲስማማ ማስተካከል አስፈልጓል
>   - በመሠረቱ የተወሰነ ሃይማኖት በጣም ጠንካራ የሃይማኖት ቀለም ያለው ሲሆን ወደ ምዕራባዊ ዓለም ያዘነበለ ነው
>     - ኢየሱስ ታላቅ ቅዱስ ሰው እንደሆነ አልክድም፣ እና የዚያን ሃይማኖት አቋምም አከብራለሁ፤ ስለዚህ እንደ ቡድሂስት ቆጠራ ሁሉ የክርስቲያን ቆጠራም በዚያ ሃይማኖት ውስጥ ብቻ ቢጠቀሙበት ምንም ችግር አልነበረም፣ ግን ችግሩ ይህ ብቻ አለመሆኑ ነው። ኮንፊውስ፣ ሻክያሙኒ፣ ሶክራቴስ ወዘተ ሌሎችም ብዙ ታላላቅ ሰዎች ነበሩ፤ እንግዲህ ለሃይማኖት ያልተገኙ ሰዎች፣ ለሌሎች ሃይማኖቶች ተከታዮች እና ከአውሮፓ ውጭ ያሉ ባህላዊ ክልሎች አንጻር ዓለም ሁሉ የሚጠቀምበት የዓመት ቆጠራ ለምን የግድ ከኢየሱስ ልደት ጀምሮ መሆን አለበት?
>     - እንዲሁም ያ ‘መጀመሪያ ዓመት’ በእርግጥ ኢየሱስ የተወለደበት ዓመት ነውን ብንል፣ በእውነቱ ያም አይደለም፣ ከዚያ ጥቂት ዓመታት በፊት እንደተወለደ መቆጠሩ አጠቃላይ የተቀባ ነው
>   - የ‘0’ ጽንሰ-ሐሳብ ከመኖሩ በፊት የተነደፈ የዓመት ቆጠራ ስርዓት ስለሆነ፣ ከክ.ዓ. 1(-1) በኋላ ቀጥታ ክ.ዓ. 1(1) ይመጣል የሚለው አመት ስሌትን በቀጥታ ለማስተዋል አስቸጋሪ ያደርገዋል
>   - ከሰው ልጅ የኒዮሊቲክ ዘመን እና ወደ ግብርና ማህበረሰብ ከገባበት ጊዜ ጀምሮ እስከ ኢየሱስ ልደት ድረስ ያለው 10000 ዓመታት፣ ወይም ቢያንስ ከጽሑፍ ፈጠራ በኋላ ያለው 3000-4000 ዓመታት ታሪክ ‘ከልደት በፊት’ በሚለው አንድ ስም ይጠቃለላል፣ ይህም በዓለም ታሪክ በተለይም በጥንታዊ ታሪክ ላይ የአስተዋል ማዛባት ይፈጥራል
> 
> ስለዚህ እዚህ ውስጥ `_data/locales`{: .filepath} ማውጫ ውስጥ የሎካል ፋይሎችን በቀጥታ ጨምሬ በአግባቡ አሻሽዬ ተግባራዊ አደረግኋቸው።  
> ስለዚህ ይህ አይመለከትዎትም እና Chirpy ገጽታ በነባሪ የሚሰጡትን ሎካሎች ምንም ማሻሻያ ሳይደረግባቸው ማግበር ከፈለጉ፣ ይህን ደረጃ መዝለል ይችላሉ።
{: .prompt-tip }

### ከPolyglot ጋር ማዋሃድ
አሁን ከሚከተሉት ሁለት ፋይሎች ላይ ትንሽ ማስተካከያ ብቻ በማድረግ Polyglot ጋር ለስላሳ የሆነ ውህደት ማድረግ ይቻላል።

> መጀመሪያ ሪፖዚቶሪውን ሲፈጥሩ የገጽታውን ሪፖዚቶሪ በቀጥታ fork ሳታደርጉ [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) ከተጠቀሙ ተዛማጅ ፋይሎቹ በራስዎ የጣቢያ ሪፖዚቶሪ ውስጥ ላይኖሩ ይችላሉ። ምክንያቱም በቀጥታ ሳይጨመሩም [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy) በኩል በነባሪነት የሚሰጡ ፋይሎች ስለሆኑ ነው። በዚህ ሁኔታ [ከChirpy ገጽታ ሪፖዚቶሪ](https://github.com/cotes2020/jekyll-theme-chirpy) ተዛማጅ የሆነውን ዋና ፋይል በመጀመሪያ አውርደው በራስዎ ሪፖዚቶሪ ውስጥ በተመሳሳይ ቦታ ላይ ካስቀመጡት በኋላ ስራውን መጀመር ይችላሉ። Jekyll ጣቢያውን ሲገነባ በሪፖዚቶሪው ውስጥ ተመሳሳይ ስም ያለው ፋይል ካለ [በውጭ gem(jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy) ከሚሰጠው ፋይል በፊት ይተገበራል።
{: .prompt-tip }

#### '\_includes/lang.html'
ከታች እንደሚታየው [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) ፋይል መካከል ሁለት የኮድ መስመሮችን ጨምሬ ነበር፣ ይህም የገጹ YAML front matter ውስጥ `lang` ተለዋዋጭ በተለየ ሁኔታ ካልተገለጸ በ `_config.yml`{: .filepath} ውስጥ ከተገለጸው የጣቢያ ነባሪ ቋንቋ(`site.lang`) ወይም እንግሊዝኛ(`'en'`) በፊት [የPolyglot `site.active_lang` ተለዋዋጭ](https://github.com/untra/polyglot?tab=readme-ov-file#features) እንዲቀድም ያደርጋል። ይህ ፋይል Chirpy ገጽታ የሚጠቀምባቸው ሁሉም ገጾች([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) ላይ በግንባታ ጊዜ `lang` ተለዋዋጭን ለማስተዋወቅ በጋራ የሚጠራ ፋይል ሲሆን፣ እዚህ የሚገለጸውን `lang` ተለዋዋጭ በመጠቀም የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግ ይከናወናል።

{% raw %}
```diff
@@ -1,10 +1,12 @@
 {% comment %}
   Detect appearance language and return it through variable "lang"
 {% endcomment %}
 {% if site.data.locales[page.lang] %}
   {% assign lang = page.lang %}
+{% elsif site.data.locales[site.active_lang] %}
+  {% assign lang = site.active_lang %}
 {% elsif site.data.locales[site.lang] %}
   {% assign lang = site.lang %}
 {% else %}
   {% assign lang = 'en' %}
 {% endif %}
```
{: file='\_includes/lang.html'}
{% endraw %}

`lang` ተለዋዋጭ ሲገለጽ የቅድሚያ ቅደም ተከተል:
- ከማሻሻያው በፊት:
  1. `page.lang`(በእያንዳንዱ ገጽ YAML front matter ውስጥ ከተገለጸ)
  2. `site.lang`(`_config.yml`{: .filepath} ውስጥ ከተገለጸ)
  3. `'en'`
- ከማሻሻያው በኋላ:
  1. `page.lang`(በእያንዳንዱ ገጽ YAML front matter ውስጥ ከተገለጸ)
  2. **`site.active_lang`**(Polyglot ተግባራዊ ሲሆን)
  3. `site.lang`(`_config.yml`{: .filepath} ውስጥ ከተገለጸ)
  4. `'en'`

#### '\_layouts/default.html'
በተመሳሳይም [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) ፋይል ይዘትን አሻሽዬ ነበር፣ ይህም HTML ሰነዱ ከፍተኛ ደረጃ አካል በሆነው `<html>` ታግ ላይ `lang` ባህሪ በትክክል እንዲመደብ ያደርጋል።

{% raw %}
```diff
@@ -1,19 +1,19 @@
 ---
 layout: compress
 ---
 
 <!doctype html>
 
 {% include origin-type.html %}
 
 {% include lang.html %}
 
 {% if site.theme_mode %}
   {% capture prefer_mode %}data-mode="{{ site.theme_mode }}"{% endcapture %}
 {% endif %}
 
 <!-- `site.alt_lang` can specify a language different from the UI -->
-<html lang="{{ page.lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
+<html lang="{{ page.lang | default: site.active_lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
   {% include head.html %}
```
{: file='\_layouts/default.html'}
{% endraw %}

`<html>` ታግ ላይ `lang` ባህሪ ሲመደብ የቅድሚያ ቅደም ተከተል:
- ከማሻሻያው በፊት:
  1. `page.lang`(በእያንዳንዱ ገጽ YAML front matter ውስጥ ከተገለጸ)
  2. `site.alt_lang`(`_config.yml`{: .filepath} ውስጥ ከተገለጸ)
  3. `site.lang`(`_config.yml`{: .filepath} ውስጥ ከተገለጸ)
  4. `unknown`(ባዶ ሕብረቁምፊ፣ `lang=""`)
- ከማሻሻያው በኋላ:
  1. `page.lang`(በእያንዳንዱ ገጽ YAML front matter ውስጥ ከተገለጸ)
  2. **`site.active_lang`**(Polyglot ተግባራዊ ሲሆን)
  3. `site.alt_lang`(`_config.yml`{: .filepath} ውስጥ ከተገለጸ)
  4. `site.lang`(`_config.yml`{: .filepath} ውስጥ ከተገለጸ)
  5. `unknown`(ባዶ ሕብረቁምፊ፣ `lang=""`)

> የድር ገጹን ቋንቋ(`lang` ባህሪ) ሳይገልጹ `unknown` እንዲሆን መተው አይመከርም፣ ስለዚህ ከተቻለ ተገቢ እሴት መመደብ ይኖርበታል። እንደሚታየው `_config.yml`{: .filepath} ውስጥ ያለው የ`lang` ባህሪ እሴት fallback ሆኖ ይጠቀማል፣ ስለዚህ Polyglot ቢጠቀሙም ባትጠቀሙም ይህን እሴት በአግባቡ መግለጽ ጥሩ ነው፣ እና በመደበኛ ሁኔታ አስቀድሞ የተገለጸ ሊሆን ይገባል። እንደ ዚህ ጽሑፍ ውስጥ እንደሚመለከተው Polyglot ወይም ከእሱ ጋር ተመሳሳይ የi18n ፕላግን ከተጠቀሙ ደግሞ [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#ቅንብር-ማዋቀር) ጋር ተመሳሳይ እሴት መመደብ የተለመደ እና አስተማማኝ ምርጫ ይሆናል።
{: .prompt-tip }

## ተጨማሪ ንባብ
በ[ክፍል 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3) ይቀጥላል
