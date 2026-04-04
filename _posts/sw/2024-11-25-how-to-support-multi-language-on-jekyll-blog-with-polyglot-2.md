---
title: "Jinsi ya kusaidia lugha nyingi katika blogu ya Jekyll kwa kutumia Polyglot (2) - Kutengeneza kitufe cha kuchagua lugha & kufanya ulughaishaji wa mpangilio"
description: "Makala hii inaeleza mchakato wa kutekeleza usaidizi wa lugha nyingi kwa kutumia plagin ya Polyglot kwenye blogu ya Jekyll inayotegemea 'jekyll-theme-chirpy'. Kama sehemu ya pili ya mfululizo huu, inaangazia kutengeneza kitufe cha kuchagua lugha na kufanya ulughaishaji wa mpangilio."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Muhtasari
Mwanzoni mwa Julai 12024, niliongeza utekelezaji wa usaidizi wa lugha nyingi kwenye blogu hii inayotegemea Jekyll na inayohostiwa kupitia Github Pages kwa kutumia plagin ya [Polyglot](https://github.com/untra/polyglot).
Mfululizo huu unashiriki hitilafu zilizotokea wakati wa kutumia plagin ya Polyglot kwenye mandhari ya Chirpy, namna zilivyotatuliwa, na jinsi ya kuandika html header pamoja na sitemap.xml kwa kuzingatia SEO.
Mfululizo huu una makala 3, na unayosoma sasa ni makala ya pili katika mfululizo huu.
- Sehemu ya 1: [Kutumia plagin ya Polyglot & kurekebisha html header na sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Sehemu ya 2: Kutengeneza kitufe cha kuchagua lugha & kufanya ulughaishaji wa mpangilio (makala hii)
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

## Kabla ya kuanza
Kwa kuwa makala hii inaendelea kutoka [Sehemu ya 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), kama bado hujaisoma, ninapendekeza uanze na makala iliyotangulia.

## Kuongeza kitufe cha kuchagua lugha kwenye sidebar
> (Sasisho la 12025.02.05.) Niliboresha kitufe cha kuchagua lugha kuwa katika muundo wa orodha ya kushuka.
{: .prompt-info }

Niliunda faili ya `_includes/lang-selector.html`{: .filepath} na kuandika yaliyomo yafuatayo.

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

Pia niliunda faili ya `assets/css/lang-selector.css`{: .filepath} na kuandika yaliyomo yafuatayo.

```css
/**
 * Mitindo ya kichagua lugha
 * 
 * Hufafanua mitindo ya dropdown ya kuchagua lugha iliyopo kwenye sidebar.
 * Inaunga mkono dark mode ya mandhari na pia imeboreshwa kwa mazingira ya simu.
 */

/* Kontena ya kichagua lugha */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Kontena ya dropdown */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Kipengele cha ingizo la uchaguzi */
.lang-select {
    /* Mitindo ya msingi */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Fonti na rangi */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Muonekano na mwingiliano */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Kuongeza ikoni ya mshale */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Mitindo ya emoji za bendera */
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

/* Hali ya hover */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Hali ya focus */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Usaidizi kwa kivinjari cha Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Usaidizi kwa kivinjari cha IE */
.lang-select::-ms-expand {
    display: none;
}

/* Usaidizi wa dark mode */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Uboreshaji kwa mazingira ya simu */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Eneo kubwa zaidi la mguso */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Eneo pana zaidi la uchaguzi kwenye simu */
    }
}
```
{: file='assets/css/lang-selector.css'}

Kisha, katika [faili ya `_includes/sidebar.html`{: .filepath} ya mandhari ya Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), niliongeza mistari mitatu ya `lang-selector-wrapper` kama ifuatavyo mara moja kabla ya darasa la `sidebar-bottom`, ili Jekyll iweze kupakia yaliyomo ya `_includes/lang-selector.html`{: .filepath} niliyoandika hapo juu wakati wa build ya ukurasa.

{% raw %}
```liquid
  (imeachwa)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(imeachwa baadaye)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (Kipengele kimeongezwa 12025.07.31.) Ulughaishaji wa mpangilio
Hapo awali, nilitumia ulughaishaji tu kwenye maudhui ya mwili kama kichwa cha ukurasa na maandishi ya makala, huku lugha ya mpangilio kama majina ya tab kwenye sidebar ya kushoto, pamoja na sehemu za juu/chini za tovuti na paneli ya kulia, ikiwa imewekwa kwa Kiingereza kama thamani chaguo-msingi ya tovuti. Binafsi niliona hata hivyo ilikuwa ya kutosha, kwa hiyo sikuona sana haja ya kufanya kazi ya ziada. Hata hivyo, hivi karibuni nilipokuwa nikifanya kazi ya [patch iliyotajwa hapo juu ya sifa za metadata za Open Graph na standard URL(canonical URL)](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-header), niligundua kuwa ulughaishaji wa mpangilio unaweza kufanywa kwa urahisi sana kwa marekebisho machache tu. Kama ingehitaji mabadiliko makubwa na ya kuudhi ya msimbo, huenda nisingefanya, lakini kwa kuwa [ilikuwa kazi rahisi isiyochukua hata dakika 10](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), niliamua kuiongeza pia.

### Kuongeza locale
Ingawa Chirpy haina kipengele cha kutoa matoleo ya lugha nyingi kwa kila ukurasa wa tovuti kwa wakati mmoja na kuruhusu kubadilisha kati ya matoleo hayo kulingana na chaguo la mtumiaji, [wigo wa lugha unaoungwa mkono na mandhari ya Chirpy wenyewe ulikuwa tayari mpana kabisa](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). Kwa hiyo unachohitaji kufanya ni kupakua kwa kuchagua faili za locale zinazotolewa na mandhari ya Chirpy, kuziongeza, na ikihitajika, kurekebisha majina ya faili ipasavyo. Majina ya faili za locale lazima yafanane na vipengee ndani ya orodha ya `languages` iliyofafanuliwa kwenye faili ya `_config.yml`{: .filepath} katika hatua ya awali ya [kuweka usanidi](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#kuweka-usanidi).

> Kwa kweli, kama nitakavyotaja tena mara moja hapa chini, faili ndani ya saraka ya `_data`{: .filepath} tayari hutolewa kwa msingi kupitia [gem ya jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy), hata kama huziongezi moja kwa moja.
>
> Hata hivyo, kwa upande wangu, haikuwa rahisi kutumia locale zinazotolewa na mandhari ya Chirpy kama zilivyo kwa sababu zifuatazo, hivyo nilihitaji kufanya marekebisho fulani tofauti.
> - Muundo wa majina ya faili za locale zinazotolewa na mandhari ya Chirpy kwa chaguo-msingi hujumuisha msimbo wa eneo kama `ko-KR`, `ja-JP`, jambo ambalo halilingani na muundo unaotumika kwenye tovuti hii kwa sasa (`ko`, `ja`, n.k.)
> - Nilihitaji kurekebisha maandishi ya taarifa ya leseni ili yaendane na [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) ya blogu hii badala ya [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ya chaguo-msingi
> - Locale za [Kikorea](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) au [Kijapani](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml), nilipoziangalia kama Mkorea, zilionekana kidogo si za asili au hazikufaa kabisa kwa blogu hii, hivyo kuna sehemu nilizorekebisha binafsi
> - Kama nilivyoeleza hapa chini, sipendi sana mfumo wa miaka wa enzi ya kawaida (Common Era) kwa sababu mbalimbali, na kwa kuwa kwenye blogu hii tu nimetumia [kalenda ya Holocene](https://en.wikipedia.org/wiki/Holocene_calendar) kama mfumo wa kuandika tarehe, nilihitaji kurekebisha locale ili ziendane nao
>   - Kimsingi una mwelekeo mkubwa wa kidini wa dini fulani na pia upendeleo wa ulimwengu wa Magharibi
>     - Simkanushi Yesu kuwa alikuwa mtakatifu mkuu, na kwa kuwa ninaheshimu pia mtazamo wa dini hiyo, kama wangesema kuwa kama mfumo wa miaka wa Kibudha, mfumo wa miaka wa enzi ya kawaida utumike ndani ya dini hiyo tu, kusingekuwa na tatizo lolote. Lakini tatizo ni kwamba sivyo ilivyo. Kulikuwa na watakatifu wengine wengi kama Confucius, Buddha, Socrates, na wengineo wengi; basi kwa nini, kutoka mtazamo wa wasio na dini, waumini wa dini nyingine, au tamaduni zisizo za Ulaya, mwaka wa mwanzo wa mfumo wa miaka unaotumiwa na dunia nzima unapaswa kuwa mwaka wa kuzaliwa kwa Yesu?
>     - Na hata ukiuliza kama huo "mwaka wa mwanzo" ni mwaka halisi wa kuzaliwa kwa Yesu, jibu ni kwamba hata huo si mwaka sahihi; maoni yanayokubalika zaidi ni kwamba alizaliwa miaka kadhaa kabla ya hapo
>   - Kwa kuwa ni mfumo wa miaka uliobuniwa kabla dhana ya '0' haijaibuka, hesabu ya miaka si ya moja kwa moja, kwa sababu mwaka wa 1 KK(-1) hufuatiwa moja kwa moja na mwaka wa 1 BK(1)
>   - Miaka 10000 ya historia kati ya kuingia kwa binadamu katika enzi ya Neolithic na jamii za kilimo hadi kabla ya kuzaliwa kwa Yesu, na hata ukihesabu tu tangu uvumbuzi wa maandishi, miaka 3000-4000 ya historia, yote huwekwa chini ya lebo moja ya "kabla ya Kristo"; hili husababisha upotoshaji wa kiutambuzi katika historia ya dunia, hasa historia ya kale
> 
> Kwa hiyo, hapa niliongeza moja kwa moja faili za locale ndani ya saraka ya `_data/locales`{: .filepath}, kisha nikazirekebisha kwa kiasi kinachofaa na kuzitumia.  
> Kwa hiyo, kama hali hii haikuhusu na unataka tu kutumia locale zinazotolewa na mandhari ya Chirpy kama zilivyo bila marekebisho, unaweza kuruka hatua hii.
{: .prompt-tip }

### Kuunganisha na Polyglot
Sasa, ukirekebisha kidogo faili mbili zifuatazo tu, unaweza kuziunganisha kwa ulaini na Polyglot.

> Kama ulitumia [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) wakati wa kuunda repozitori mwanzoni badala ya kufork moja kwa moja repozitori ya mandhari, inawezekana faili husika hazipo kwenye repozitori ya tovuti yako. Hii ni kwa sababu hata bila kuziongeza mwenyewe, faili hizo hutolewa kwa msingi kupitia [gem ya jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy). Katika hali hiyo, unachopaswa kufanya ni kupakua kwanza faili asili husika kutoka [repozitori ya mandhari ya Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy), kisha uziweke katika eneo lile lile ndani ya repozitori yako ndipo ufanye kazi. Jekyll inapojenga tovuti, ikiwa tayari kuna faili yenye jina lile lile ndani ya repozitori, itaitumia kwa kipaumbele juu ya faili inayotolewa na [gem ya nje(jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy).
{: .prompt-tip }

#### '\_includes/lang.html'
Kama ifuatavyo, niliongeza mistari miwili ya msimbo katikati ya faili ya [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html), ili pale ambapo kigeuzi cha `lang` hakijafafanuliwa wazi kwenye YAML front matter ya ukurasa, [kigeuzi cha `site.active_lang` cha Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features) kitambuliwe kwa kipaumbele juu ya lugha chaguo-msingi ya tovuti iliyofafanuliwa kwenye `_config.yml`{: .filepath} (`site.lang`) au Kiingereza(`'en'`). Faili hii huitwa kwa pamoja wakati wa build ya kurasa zote katika tovuti inayotumia mandhari ya Chirpy ([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) kwa ajili ya kutangaza kigeuzi cha `lang`, na ulughaishaji wa mpangilio hufanywa kwa kutumia kigeuzi cha `lang` kinachotangazwa hapa.

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

Kipaumbele wakati wa kutangaza kigeuzi cha `lang`:
- Kabla ya marekebisho:
  1. `page.lang`(ikiwa imefafanuliwa ndani ya YAML front matter ya ukurasa binafsi)
  2. `site.lang`(ikiwa imefafanuliwa kwenye `_config.yml`{: .filepath})
  3. `'en'`
- Baada ya marekebisho:
  1. `page.lang`(ikiwa imefafanuliwa ndani ya YAML front matter ya ukurasa binafsi)
  2. **`site.active_lang`**(ikiwa Polyglot inatumika)
  3. `site.lang`(ikiwa imefafanuliwa kwenye `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
Vivyo hivyo, nilirekebisha yaliyomo ya faili ya [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) ili sifa ya `lang` iwekwe kwa usahihi kwenye tag ya `<html>`, ambayo ni kipengele cha juu kabisa cha hati ya HTML.

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

Kipaumbele wakati wa kutaja sifa ya `lang` ya tag ya `<html>`:
- Kabla ya marekebisho:
  1. `page.lang`(ikiwa imefafanuliwa ndani ya YAML front matter ya ukurasa binafsi)
  2. `site.alt_lang`(ikiwa imefafanuliwa kwenye `_config.yml`{: .filepath})
  3. `site.lang`(ikiwa imefafanuliwa kwenye `_config.yml`{: .filepath})
  4. `unknown`(mfuatano tupu, `lang=""`)
- Baada ya marekebisho:
  1. `page.lang`(ikiwa imefafanuliwa ndani ya YAML front matter ya ukurasa binafsi)
  2. **`site.active_lang`**(ikiwa Polyglot inatumika)
  3. `site.alt_lang`(ikiwa imefafanuliwa kwenye `_config.yml`{: .filepath})
  4. `site.lang`(ikiwa imefafanuliwa kwenye `_config.yml`{: .filepath})
  5. `unknown`(mfuatano tupu, `lang=""`)

> Haipendekezwi kuacha lugha ya ukurasa wa wavuti (sifa ya `lang`) bila kutajwa na kuiweka kama `unknown`; inapowezekana, inapaswa kuwekwa kwa thamani sahihi. Kama unavyoona, thamani ya sifa ya `lang` ndani ya `_config.yml`{: .filepath} hutumika kama fallback, kwa hiyo iwe unatumia Polyglot au hutumii, ni bora kuhakikisha thamani hii imefafanuliwa ipasavyo, na katika hali ya kawaida kwa kawaida huwa tayari imefafanuliwa. Kama unatumia Polyglot au plagin inayofanana ya i18n kama ilivyojadiliwa katika makala hii, kwa kawaida ni salama kuiweka iwe na thamani sawa na [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#kuweka-usanidi).
{: .prompt-tip }

## Usomaji Zaidi
Inaendelea katika [Sehemu ya 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
