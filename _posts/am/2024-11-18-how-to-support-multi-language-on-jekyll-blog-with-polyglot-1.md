---
title: "በPolyglot በመጠቀም በJekyll ብሎግ ውስጥ ብዙ ቋንቋ ድጋፍ እንዴት እንደሚጨምሩ (1) - Polyglot ፕላግን መተግበር & html ሄደር እና sitemap ማስተካከል"
description: "'jekyll-theme-chirpy' ላይ የተመሠረተ Jekyll ብሎግ ላይ Polyglot ፕላግን በመተግበር ብዙ ቋንቋ ድጋፍ እንዴት እንደተገነባ ያብራራል። ይህ የተከታታይ ጽሑፎች የመጀመሪያው ሲሆን Polyglot ፕላግኑን መተግበር እና html ሄደርን ከ sitemap ጋር ማስተካከልን ይሸፍናል።"
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## አጠቃላይ እይታ
በ12024 ዓ.ም. ጁላይ መጀመሪያ ላይ፣ በGithub Pages በኩል የሚስተናገድ ይህ በJekyll የተመሠረተ ብሎግ ላይ [Polyglot](https://github.com/untra/polyglot) ፕላግን በመተግበር ብዙ ቋንቋ ድጋፍ አክዬበታለሁ።
ይህ ተከታታይ ጽሑፎች በChirpy ገጽታ ላይ Polyglot ፕላግን ሲተገበር የተፈጠሩ ችግኞችን እና የመፍትሄ ሂደታቸውን፣ እንዲሁም SEO ን በማሰብ html ሄደር እና sitemap.xml እንዴት እንደሚጻፉ ያጋራል።
ይህ ተከታታይ 3 ጽሑፎችን ያካትታል፣ እያነበቡት ያሉትም ይህ ጽሑፍ የመጀመሪያው ነው።
- ክፍል 1: Polyglot ፕላግን መተግበር & html ሄደር እና sitemap ማስተካከል (ይህ ጽሑፍ)
- ክፍል 2: [የቋንቋ ምርጫ አዝራር መተግበር & የአቀማመጥ ቋንቋ አካባቢያዊ ማድረግ](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
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

## Polyglot ፕላግን መተግበር
Jekyll በመሠረታዊነት ብዙ ቋንቋ ብሎግን አይደግፍም፣ ስለዚህ ከላይ ያሉትን መስፈርቶች የሚያሟላ ብዙ ቋንቋ ብሎግ ለመገንባት የውጭ ፕላግን መጠቀም ያስፈልጋል። ፍለጋ ሳደርግ [Polyglot](https://github.com/untra/polyglot) ለብዙ ቋንቋ ድረ ገጽ ግንባታ ብዙ ጊዜ እንደሚጠቀሙበት አግኝቻለሁ፣ እና ከላይ ያሉትን መስፈርቶች አብዛኛውን ማሟላት ስለሚችል ይህን ፕላግን መርጬዋለሁ።

### ፕላግን መጫን
እኔ Bundler እጠቀማለሁ፣ ስለዚህ ወደ `Gemfile` የሚከተለውን ይዘት አክዬ ነበር።

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

ከዚያ በኋላ በተርሚናል ላይ `bundle update` ካስኬዱ መጫኑ በራሱ ይጠናቀቃል።

Bundler ካልተጠቀሙ ግን፣ በተርሚናል ውስጥ `gem install jekyll-polyglot` ትእዛዝ በመጠቀም gem በቀጥታ ከጫኑ በኋላ `_config.yml`{: .filepath} ውስጥ እንደሚከተለው ፕላግኑን ማከል ይችላሉ።

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### ቅንብር ማዋቀር
በመቀጠል `_config.yml`{: .filepath} ፋይሉን ይክፈቱ እና ከታች ያለውን ይዘት ያክሉ።

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: ለመደገፍ የሚፈልጉት የቋንቋ ዝርዝር
- `default_lang`: ነባሪ fallback ቋንቋ
- `exclude_from_localization`: ከቋንቋ አካባቢያዊ ማድረግ ውጭ የሚሆኑ የስር ፋይል/አቃፊ መንገድ ህብረቁምፊ መደበኛ መግለጫዎች
- `parallel_localization`: በግንባታ ሂደት ውስጥ የብዙ ቋንቋ ሂደትን በትይዩ ለማስኬድ ወይም አለመስኬድን የሚወስን boolean እሴት
- `lang_from_path`: boolean እሴት ነው፣ 'true' ሲሆን በፖስት Markdown ፋይሉ ውስጥ በYAML front matter 'lang' ባህሪ በተናጠል ካልተገለጸም፣ የዚያ የMarkdown ፋይል መንገድ ህብረቁምፊ የቋንቋ ኮድ ካካተተ ይህን በራሱ አውቆ ይጠቀማል

> [የSitemap ፕሮቶኮል ኦፊሴላዊ ሰነድ](https://www.sitemaps.org/protocol.html#location) የሚከተለውን በግልፅ ይገልጻል።
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> ይህን ለማክበር፣ ተመሳሳይ ይዘት ያለው `sitemap.xml`{: .filepath} ፋይል በእያንዳንዱ ቋንቋ እንዳይፈጠር እና በስር ዳይሬክተሪ ውስጥ አንድ ብቻ እንዲኖር፣ 'exclude_from_localization' ዝርዝር ውስጥ ማከል አለብዎት፣ እንዲሁም ከታች እንዳለው የተሳሳተ ምሳሌ እንዳይሆን መከላከል አለብዎት።
>
> የተሳሳተ ምሳሌ(የእያንዳንዱ ፋይል ይዘት በቋንቋ አይለያይም፣ ሁሉም አንድ ናቸው)፦
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (12025.01.14. ዝማኔ) [ከላይ የተገለጸውን ይዘት README ውስጥ በማጠናከር ያስገባሁት Pull Request](https://github.com/untra/polyglot/pull/230) ከተቀበለ በኋላ፣ አሁን [በPolyglot ኦፊሴላዊ ሰነድ](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation) ውስጥም ተመሳሳይ መመሪያ ማየት ይቻላል።
{: .prompt-tip }

> 'parallel_localization' ን 'true' ብለው ከገለጹ የግንባታ ጊዜን በእጅጉ የሚቀንስ ጥቅም አለው፣ ግን በ12024 ዓ.ም. ጁላይ ጊዜ ላይ ለዚህ ብሎግ ይህን ባህሪ እንዳበራሁት ጊዜ በገጹ ቀኝ ያለው ሳይድባር ውስጥ 'Recently Updated' እና 'Trending Tags' ክፍሎች የአገናኝ ርዕሶች በትክክል አልተሰሩም እና ከሌሎች ቋንቋዎች ጋር ተቀላቀሉ። እስካሁን ድረስ በቂ ያልተረጋጋ ይመስላል፣ ስለዚህ በጣቢያዎ ላይ ከመተግበርዎ በፊት በመደበኛነት እንደሚሰራ ፈተና ማድረግ ያስፈልጋል። በተጨማሪም [Windows ተጠቃሚ ከሆኑ ይህ ባህሪ ስለማይደገፍ መሰናከል አለበት](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)።
>
> (12025.09 ዝማኔ) በ12025 ዓ.ም. የበጋ ወቅት ላይ አሁን ያለውን ይህን ብሎግ መሰረት አድርጌ 'parallel_localization' ባህሪን እንደገና ሞክሬው ጊዜ ያለ ችግኝ በመደበኛነት እንደሚሰራ አገኘሁ። ስለዚህ አሁን ይህን ባህሪ አብርቼዋለሁ፣ ለዚህም ምክንያት የግንባታ ጊዜ በእጅጉ ተቀንሷል።
{: .prompt-warning }

በተጨማሪም [በJekyll 4.0 ውስጥ CSS sourcemaps ፍጠራ እንደሚከተለው መሰናከል አለበት](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)።

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### ፖስቶችን ሲጽፉ ማስታወስ ያለባቸው ነገሮች
ብዙ ቋንቋ ፖስቶችን ሲጽፉ መጠንቀቅ ያለባቸው ነገሮች እንደሚከተሉት ናቸው።
- ተገቢ የቋንቋ ኮድ መግለጽ፦ የፋይል መንገድ(ex. `/_posts/ko/example-post.md`{: .filepath}) ወይም በYAML front matter ውስጥ ያለው 'lang' ባህሪ(ex. `lang: ko`) በመጠቀም ተገቢውን ISO የቋንቋ ኮድ መግለጽ አለብዎት። [የChrome አበልጻጊ ሰነድ](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) ውስጥ ያሉትን ምሳሌዎች ይመልከቱ።

> ነገር ግን [የChrome አበልጻጊ ሰነድ](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) የክልል ኮድን እንደ 'pt_BR' ቅርጽ ቢያሳይም፣ በእውነቱ በኋላ html ሄደር ውስጥ hreflang ተለዋጭ ታጎችን ሲጨምሩ በትክክል እንዲሰራ _ ፋንታ - በመጠቀም እንደ 'pt-BR' መጻፍ አለብዎት።
{: .prompt-tip }

- የፋይል መንገድና ስም ተደጋጋሚ ቅጥ ያለው መሆን አለበት።

ተጨማሪ ዝርዝሮች ለማወቅ የGitHub [untra/polyglot ሪፖዚቶሪ README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it) ይመልከቱ።

## html ሄደር እና sitemap ማስተካከል
አሁን ለSEO ሲባል በብሎጉ ውስጥ ባሉ እያንዳንዱ ገጾች html ሄደር ውስጥ Content-Language ሜታ ታግ እና hreflang ተለዋጭ ታጎችን ማስገባት ያስፈልጋል፣ እንዲሁም መደበኛ URL(canonical URL) በተገቢው ሁኔታ መወሰን ያስፈልጋል።

### html ሄደር
በ12024.11. ወቅት ከነበረው የቅርብ ጊዜ ስሪት 1.8.1 ልቀት መሰረት፣ Polyglot በገጽ ሄደር ክፍል ውስጥ {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid ታግ ሲጠራ ከላይ ያሉትን ስራዎች በራሱ የሚያከናውን ባህሪ አለው።
ነገር ግን ይህ ማለት በዚያ ገጽ ላይ 'permalink' ባህሪ ታግ በግልፅ እንደተገለጸ ይገምታል፣ ካልሆነ ግን በመደበኛነት አይሰራም።

ስለዚህ እኔ [የChirpy ገጽታ head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) አውጥቼ ከዚያ በኋላ ከታች እንደሚታየው ይዘቱን በቀጥታ ጨመርኩ።
[የPolyglot ኦፊሴላዊ ብሎግ SEO Recipes ገጽ](https://polyglot.untra.io/seo/) ን አጣቅሼ ሰራሁት፣ ነገር ግን ለእኔ የአጠቃቀም አካባቢ እና መስፈርቶች እንዲስማማ `page.permalink` ፋንታ `page.url` ባህሪ እንዲጠቀም አስተካክዬዋለሁ።

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">
  
  {% if site.default_lang -%}
  <link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />
  {%- endif -%}
  {% for lang in site.languages -%}
    {% if lang == site.default_lang -%}
      {%- continue -%}
    {%- endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {%- endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

(12025.07.29. ተጨማሪ) እንዲሁም Chirpy ገጽታ [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag) ፕላግንን በነባሪነት ውስጥ ያካትታል፣ እና Jekyll SEO Tag በራሱ የሚፈጥራቸው `og:locale`, `og:url` [Open Graph](https://ogp.me/) ሜታዳታ ባህሪዎች እና [መደበኛ URL(canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)(`rel="canonical"` `link` ንጥል) በጣቢያው ነባሪ ቋንቋ(`site.lang`, `site.default_lang`) ላይ የተመሠረቱ ስለሆኑ ተጨማሪ ሂደት እንደሚያስፈልግ አረጋግጫለሁ።  
ስለዚህ {% raw %}`{{ seo_tags }}`{% endraw %} ከመታየቱ በፊት የሚከተለውን ንዑስ ኮድ ጨመርኩ።

{% raw %}
```liquid
(전략)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(중략)...

  {%- capture old_og_locale -%}
    <meta property="og:locale" content="{{site.lang}}" />
  {%- endcapture -%}
  {%- capture new_og_locale -%}
    <meta property="og:locale" content="{{site.active_lang}}" />
    {% for lang in site.languages -%}
      {%- if lang == site.active_lang -%}
        {%- continue -%}
      {%- endif %}
    <meta property="og:locale:alternate" content="{{lang}}" />
    {%- endfor %}
  {%- endcapture -%}
  {% assign seo_tags = seo_tags | replace: old_og_locale, new_og_locale %}
  
  {% unless site.active_lang == site.default_lang -%}
    {%- capture old_canonical_link -%}
      <link rel="canonical" href="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture old_og_url -%}
      <meta property="og:url" content="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_canonical_link -%}
      <link rel="canonical" href="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_og_url -%}
      <meta property="og:url" content="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {% assign seo_tags = seo_tags | replace: old_canonical_link, new_canonical_link %}
    {% assign seo_tags = seo_tags | replace: old_og_url, new_og_url %}
  {%- endunless %}

  {{ seo_tags }}

  ...(후략)
```
{: file='/_includes/head.html'}
{% endraw %}

> [የGoogle አበልጻጊ ሰነድ](https://developers.google.com/search/docs/crawling-indexing/canonicalization) መሠረት፣ አንድ ገጽ ብዙ የቋንቋ ስሪቶች ሲኖሩት ዋና ይዘቱ ተመሳሳይ ቋንቋ ሲሆን ብቻ ነው እንደ ተደጋጋሚ የሚቆጠረው፤ ማለትም ራስጌ፣ ግርጌ እና ሌሎች አስፈላጊ ያልሆኑ ጽሑፎች ብቻ ተተርጉመው ዋናው የአካል ጽሑፍ ተመሳሳይ ከሆነ ብቻ። ስለዚህ እንደዚህ ብሎግ ውስጥ ዋና የአካል ጽሑፍ በብዙ ቋንቋዎች የሚቀርብ ከሆነ፣ የእያንዳንዱ ቋንቋ ስሪቶች ሁሉ ተደጋጋሚ ሳይሆኑ እርስ በርሳቸው ገለልተኛ ገጾች እንደሆኑ ይቆጠራሉ፣ ስለዚህም በቋንቋ መሰረት የተለያዩ canonical URL ዎችን መወሰን አለብዎት።  
> ለምሳሌ አሁን ያለው የዚህ ገጽ የኮሪያኛ ስሪት ከተመለከቱ፣ canonical URL ው ` "{{site.url}}{{page.url}}"` ሳይሆን ` "{{site.url}}/ko{{page.url}}"` ነው።
{: .prompt-tip }

### sitemap
በተለየ ሁኔታ ቴምፕሌት ካልተገለጸ፣ Jekyll በግንባታ ጊዜ በራሱ የሚፈጥረው sitemap ብዙ ቋንቋ ገጾችን በመደበኛነት አይደግፍም፣ ስለዚህ በስር ዳይሬክተሪ ላይ `sitemap.xml`{: .filepath} ፋይል ፍጠሩ እና እንደሚከተለው ይዘት ያስገቡ።

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages -%}

  {% for node in site.pages %}
    {%- comment -%}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{%- endcomment -%}
    {%- comment -%}<!-- Exclude redirects from sitemap -->{%- endcomment -%}
    {%- if node.redirect.to -%}
      {%- continue -%}
    {%- endif -%}
    {%- unless site.exclude_from_localization contains node.path -%}
      {%- comment -%}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{%- endcomment -%}
      {% if node.layout %}
        <url>
          <loc>
            {%- if lang == site.default_lang -%}
              {{ node.url | absolute_url }}
            {%- else -%}
              {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
            {%- endif -%}
          </loc>
          {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {% endif -%}
          {% if site.default_lang -%}
          <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
          {%- endif -%}
          {% for lang in site.languages -%}
            {% if lang == site.default_lang -%}
              {%- continue -%}
            {%- endif %}
          <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
          {%- endfor %}
        </url>
      {% endif %}
    {%- elsif site.default_lang -%}
        <url>
          <loc>{{ node.url | absolute_url }}</loc>
      {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {% endif -%}
        </url>
    {%- endunless -%}
  {% endfor %}

  {%- comment -%}<!-- This loops through all site collections including posts -->{%- endcomment -%}
  {% for collection in site.collections %}
    {% for node in site[collection.label] %}
      <url>
        <loc>
          {%- if lang == site.default_lang -%}
            {{ node.url | absolute_url }}
          {%- else -%}
            {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
          {%- endif -%}
        </loc>
        {% if node.last_modified_at and node.last_modified_at != node.date -%}
        <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- elsif node.date -%}
        <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- endif %}
        {% if site.default_lang -%}
        <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
        {%- endif -%}
        {% for lang in site.languages -%}
          {% if lang == site.default_lang -%}
            {%- continue -%}
          {%- endif %}
        <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
        {%- endfor %}
      </url>
    {% endfor %}
  {% endfor %}

{%- endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## ተጨማሪ ንባብ
በ[ክፍል 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2) ይቀጥላል
