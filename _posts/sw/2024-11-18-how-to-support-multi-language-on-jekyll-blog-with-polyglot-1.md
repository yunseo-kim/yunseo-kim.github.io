---
title: "Jinsi ya kusaidia lugha nyingi katika blogu ya Jekyll kwa kutumia Polyglot (1) - Kutumia plagin ya Polyglot & kurekebisha HTML header na sitemap"
description: "Makala hii inaeleza mchakato wa kutekeleza usaidizi wa lugha nyingi kwa kutumia plagin ya Polyglot kwenye blogu ya Jekyll inayotegemea 'jekyll-theme-chirpy'. Kama sehemu ya kwanza ya mfululizo huu, inaangazia matumizi ya plagin ya Polyglot na marekebisho ya HTML header pamoja na sitemap."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Muhtasari
Mwanzoni mwa Julai 12024, niliongeza utekelezaji wa usaidizi wa lugha nyingi kwenye blogu hii inayotegemea Jekyll na inayohostiwa kupitia Github Pages kwa kutumia plagin ya [Polyglot](https://github.com/untra/polyglot).
Mfululizo huu unashiriki hitilafu zilizotokea wakati wa kutumia plagin ya Polyglot kwenye mandhari ya Chirpy, namna zilivyotatuliwa, na jinsi ya kuandika html header pamoja na sitemap.xml kwa kuzingatia SEO.
Mfululizo huu una makala 3, na unayosoma sasa ni makala ya kwanza katika mfululizo huu.
- Sehemu ya 1: Kutumia plagin ya Polyglot & kurekebisha html header na sitemap (makala hii)
- Sehemu ya 2: [Kutengeneza kitufe cha kuchagua lugha & kufanya ulughaishaji wa mpangilio](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- Sehemu ya 3: [Utatuzi wa hitilafu za build failure za mandhari ya Chirpy na makosa ya kipengele cha utafutaji](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Hapo awali niliupanga kama mfululizo wa sehemu 2 kwa jumla, lakini baadaye maudhui yalipanuliwa mara kadhaa, kiasi kwamba urefu wa maandishi uliongezeka sana na hivyo nikaunda upya kuwa sehemu 3.
{: .prompt-info }

## Mahitaji
- [x] Matokeo ya build (ukurasa wa wavuti) lazima yaweze kutolewa kwa kutenganishwa kwa njia za lugha tofauti (mf. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Ili kupunguza kadiri iwezekanavyo muda na juhudi za ziada zinazohitajika kwa usaidizi wa lugha nyingi, faili ya asili ya markdown isiwe lazima ipewe lebo za 'lang' na 'permalink' moja kwa moja kwenye YAML front matter; badala yake, wakati wa build lugha lazima itambulike kiotomatiki kulingana na njia ya ndani ya faili hiyo (mf. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}).
- [x] Sehemu ya header ya kila ukurasa katika tovuti lazima itimize miongozo ya Google SEO kwa utafutaji wa lugha nyingi, ikijumuisha meta tag sahihi ya Content-Language, hreflang alternate tag, na canonical link.
- [x] Lazima iwezekane kutoa viungo vya kila toleo la lugha ya ukurasa bila kukosa lolote kupitia `sitemap.xml`{: .filepath}, na `sitemap.xml`{: .filepath} yenyewe lazima iwepo mara moja tu kwenye root path bila kurudiwa.
- [x] Vipengele vyote vinavyotolewa na [mandhari ya Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) lazima vifanye kazi ipasavyo katika kurasa za kila lugha, na kama sivyo lazima virekebishwe ili vifanye kazi vizuri.
  - [x] Vipengele vya 'Recently Updated' na 'Trending Tags' vifanye kazi kawaida
  - [x] Kusiwe na hitilafu katika mchakato wa build unaotumia GitHub Actions
  - [x] Kipengele cha kutafuta machapisho kilicho juu kulia mwa blogu kifanye kazi kawaida

## Kutumia plagin ya Polyglot
Jekyll haitoi usaidizi wa lugha nyingi kwa msingi, hivyo ili kutekeleza blogu ya lugha nyingi inayotimiza mahitaji yaliyo hapo juu, ni lazima kutumia plagin ya nje. Nilipotafuta, niligundua kuwa [Polyglot](https://github.com/untra/polyglot) hutumika sana kwa ajili ya kutengeneza tovuti za lugha nyingi, na inaweza kutimiza sehemu kubwa ya mahitaji hayo, hivyo nikaichagua.

### Kusakinisha plagin
Kwa kuwa ninatumia Bundler, niliongeza yaliyomo yafuatayo kwenye `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Baada ya hapo, ukikimbiza `bundle update` kwenye terminal, usakinishaji hukamilika kiotomatiki.

Ikiwa hutumii Bundler, unaweza pia kusakinisha gem moja kwa moja kwa amri ya `gem install jekyll-polyglot` kwenye terminal, kisha kuongeza plagin kwenye `_config.yml`{: .filepath} kama ifuatavyo.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Kuweka usanidi
Hatua inayofuata ni kufungua faili ya `_config.yml`{: .filepath} na kuongeza maudhui yafuatayo.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: Orodha ya lugha unazotaka kusaidia
- `default_lang`: Lugha ya msingi ya fallback
- `exclude_from_localization`: Hufafanua regular expression ya mfuatano wa njia ya faili/folda ya root itakayoondolewa kwenye ulughaishaji
- `parallel_localization`: Boolean inayobainisha kama usindikaji wa lugha nyingi uendeshwe kwa sambamba wakati wa build
- `lang_from_path`: Thamani ya boolean; ikiwekwa kuwa 'true', hata kama sifa ya 'lang' haijaainishwa tofauti katika YAML front matter ya faili ya post markdown, ikiwa mfuatano wa njia ya faili hiyo ya markdown una msimbo wa lugha, basi utatambuliwa na kutumika kiotomatiki

> [Hati rasmi ya Sitemap Protocol](https://www.sitemaps.org/protocol.html#location) inaeleza yafuatayo.
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Ili kutii hili, ni lazima faili ya `sitemap.xml`{: .filepath} yenye maudhui yale yale isitengenezwe kwa kila lugha, bali iwepo mara moja tu kwenye root directory. Kwa hiyo, unapaswa kuiongeza kwenye orodha ya 'exclude_from_localization' ili kuepuka hali kama mfano mbaya ulio hapa chini.
>
> Mfano mbaya (maudhui ya kila faili hayana tofauti kwa lugha na yote ni sawa):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Sasisho la 12025.01.14.) Kwa kuwa [Pull Request niliyowasilisha ili kuongeza maelezo hayo kwenye README](https://github.com/untra/polyglot/pull/230) ilikubaliwa, sasa unaweza pia kuona maelekezo hayo hayo kwenye [nyaraka rasmi za Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Ukiweka 'parallel_localization' kuwa 'true', kuna faida ya kupunguza sana muda wa build, lakini kufikia Julai 12024, nilipowasha kipengele hiki kwenye blogu hii, kulikuwa na hitilafu ambapo vichwa vya viungo katika sehemu za 'Recently Updated' na 'Trending Tags' kwenye sidebar ya kulia ya ukurasa havikuchakatwa vizuri na vilichanganyika na lugha nyingine. Inaonekana bado haijatulia kabisa, hivyo ikiwa unataka kuitumia kwenye tovuti yako, ni muhimu kwanza kupima kama inafanya kazi ipasavyo. Zaidi ya hayo, [kipengele hiki pia hakitumiki ukiwa unatumia Windows, hivyo kinapaswa kuzimwa](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
>
> (Sasisho la 12025.09) Nilipojaribu tena kipengele cha 'parallel_localization' katika kiangazi cha 12025 kwa kutumia blogu hii kama msingi, kilifanya kazi vizuri bila matatizo. Kwa hiyo kwa sasa nimekiwasha, na kwa msaada wake muda wa build umepunguzwa sana.
{: .prompt-warning }

Pia, [katika Jekyll 4.0 lazima uzime utengenezaji wa CSS sourcemaps kama ifuatavyo](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Mambo ya kuzingatia unapoandika post
Mambo ya kuzingatia unapoandika post za lugha nyingi ni haya yafuatayo.
- Kuweka msimbo sahihi wa lugha: Lazima ueleze msimbo sahihi wa ISO wa lugha kwa kutumia njia ya faili (mf. `/_posts/ko/example-post.md`{: .filepath}) au sifa ya 'lang' katika YAML front matter (mf. `lang: ko`). Tazama mifano katika [nyaraka za Chrome Developer](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Hata hivyo, ingawa [nyaraka za Chrome Developer](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) huandika msimbo wa eneo katika muundo kama 'pt_BR', kwa vitendo lazima utumie '-' badala ya '_' kama 'pt-BR' ili ifanye kazi vizuri baadaye unapoongeza hreflang alternate tag kwenye html header.
{: .prompt-tip }

- Njia ya faili na jina la faili lazima viwe thabiti.

Kwa maelezo zaidi, tafadhali rejelea README ya GitHub ya [hazina ya untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Kurekebisha html header na sitemap
Sasa, kwa ajili ya SEO, unahitaji kuingiza meta tag ya Content-Language na hreflang alternate tag kwenye html header ya kila ukurasa wa blogu, na pia kuweka vizuri standard URL (canonical URL).

### html header
Kufikia 12024.11, kwa kuzingatia toleo jipya zaidi la 1.8.1, Polyglot ina kipengele kinachofanya kazi hii kiotomatiki unapoitisha Liquid tag ya {% raw %}`{% I18n_Headers %}`{% endraw %} katika sehemu ya header ya ukurasa.
Hata hivyo, hilo linadhania kuwa tag ya sifa ya 'permalink' imeainishwa wazi kwa ukurasa huo, na ikiwa sivyo halifanyi kazi ipasavyo.

Kwa hiyo nilichukua [head.html ya mandhari ya Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html), kisha nikaongeza mwenyewe maudhui kama yafuatayo.
Nilifanya kazi hii kwa kurejelea [ukurasa wa SEO Recipes wa blogu rasmi ya Polyglot](https://polyglot.untra.io/seo/), lakini nikaunda marekebisho ili kutumia sifa ya `page.url` badala ya `page.permalink` kulingana na mazingira yangu ya matumizi na mahitaji yangu.

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

(Iliongezwa 12025.07.29.) Aidha, mandhari ya Chirpy huja ikiwa tayari imejumuisha plagin ya [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag), na nilibaini kuwa sifa za metadata za [Open Graph](https://ogp.me/) za `og:locale` na `og:url`, pamoja na [standard URL (canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (`rel="canonical"` kipengele cha `link`) vinavyozalishwa kiotomatiki na Jekyll SEO Tag hutegemea lugha msingi ya tovuti (`site.lang`, `site.default_lang`), hivyo usindikaji wa ziada ulihitajika.  
Kwa hiyo niliongeza msimbo ufuatao kabla ya {% raw %}`{{ seo_tags }}`{% endraw %}.

{% raw %}
```liquid
(imeachwa)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(imeachwa)...

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

  ...(imeachwa baadaye)
```
{: file='/_includes/head.html'}
{% endraw %}

> Kulingana na [nyaraka za Google Developer](https://developers.google.com/search/docs/crawling-indexing/canonicalization), ukurasa wenye matoleo ya lugha nyingi huzingatiwa kuwa rudufu tu ikiwa lugha ya maudhui makuu ni ile ile, yaani ni kichwa, footer, na maandishi mengine yasiyo muhimu pekee ndiyo yametafsiriwa huku mwili wa maandishi ukiwa ule ule. Kwa hiyo, katika hali kama blogu hii ambapo maandishi ya mwili hutolewa katika lugha nyingi, matoleo ya kila lugha huzingatiwa kuwa kurasa huru zisizo rudufu, hivyo ni lazima uweke standard URL tofauti kwa kila lugha.  
> Kwa mfano, kwa toleo la Kikorea la ukurasa huu wa sasa, standard URL si "{{site.url}}{{page.url}}" bali ni "{{site.url}}/ko{{page.url}}".
{: .prompt-tip }

### sitemap
Iwapo hutaainisha templeti tofauti, sitemap inayozalishwa kiotomatiki na Jekyll wakati wa build haitoi usaidizi sahihi kwa kurasa za lugha nyingi. Hivyo, tengeneza faili ya `sitemap.xml`{: .filepath} kwenye root directory, kisha andika maudhui yafuatayo.

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

## Usomaji Zaidi
Inaendelea katika [Sehemu ya 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
