---
title: "Jak na vícejazyčnou podporu v Jekyll blogu pomocí Polyglot (2) – implementace tlačítka pro výběr jazyka & lokalizace rozvržení"
description: "Popisuji, jak jsem na Jekyll blogu na bázi 'jekyll-theme-chirpy' zavedl vícejazyčnost pomocí Polyglot. 2. díl: výběr jazyka a lokalizace rozvržení."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Přehled
Začátkem července 12024 jsem na tento blog (hostovaný přes GitHub Pages a postavený na Jekyllu) nasadil plugin [Polyglot](https://github.com/untra/polyglot) a doplnil tak podporu více jazyků.  
V této sérii sdílím bugy, které se objevily při aplikaci Polyglot na téma Chirpy, jejich řešení a také způsob psaní HTML hlavičky a `sitemap.xml`{: .filepath} s ohledem na SEO.  
Série se skládá ze 3 článků a tento, který právě čtete, je její druhý díl.

- 1. díl: [Nasazení pluginu Polyglot & úprava HTML hlavičky a sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- 2. díl: Implementace tlačítka pro výběr jazyka & lokalizace rozvržení (tento článek)
- 3. díl: [Troubleshooting: selhání buildu tématu Chirpy a chyby ve vyhledávání](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Původně byla série ve 2 dílech, ale jak jsem ji později v několika krocích doplňoval, výrazně narostl rozsah, a proto jsem ji přepracoval na 3 díly.
{: .prompt-info }

## Požadavky
- [x] Výstup buildu (webové stránky) musí být možné poskytovat rozlišeně podle jazyka pomocí cest (např. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Aby se minimalizoval dodatečný čas a práce spojené s vícejazyčností, nesmí být nutné u každého zdrojového Markdown souboru ručně nastavovat ve YAML front matter tagy `lang` a `permalink`. Při buildu se musí jazyk automaticky rozpoznat podle lokální cesty, kde soubor leží (např. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}).
- [x] Hlavička každé stránky na webu musí splňovat Google SEO doporučení pro vícejazyčné vyhledávání: správný meta tag `Content-Language`, alternátní tagy `hreflang` a canonical odkaz.
- [x] Odkazy na všechny jazykové verze stránek musí být bez vynechání uvedeny v `sitemap.xml`{: .filepath}; samotný `sitemap.xml`{: .filepath} musí existovat bez duplicit pouze jednou v kořenové cestě.
- [x] Všechny funkce, které poskytuje [téma Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy), musí fungovat korektně i na stránkách jednotlivých jazyků; pokud ne, musí se upravit tak, aby fungovaly.
  - [x] Správná funkce „Recently Updated“, „Trending Tags“
  - [x] Žádné chyby v procesu buildu přes GitHub Actions
  - [x] Správná funkce vyhledávání příspěvků vpravo nahoře

## Než začnete
Tento článek navazuje na [1. díl](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), takže pokud jste jej ještě nečetli, doporučuji nejdřív začít předchozím článkem.

## Přidání tlačítka pro výběr jazyka do postranního panelu
> (Aktualizace 12025.02.05.) Vylepšil jsem tlačítko výběru jazyka na formát rozbalovacího seznamu.
{: .prompt-info }

Vytvořil jsem soubor `_includes/lang-selector.html`{: .filepath} a vložil do něj následující obsah.

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

Dále jsem vytvořil soubor `assets/css/lang-selector.css`{: .filepath} a vložil do něj následující.

```css
/**
 * Styl výběru jazyka
 * 
 * Definuje styl rozbalovacího výběru jazyka v postranním panelu.
 * Podporuje dark mode tématu a je optimalizovaný i pro mobilní prostředí.
 */

/* Kontejner výběru jazyka */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Kontejner dropdownu */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Prvek select */
.lang-select {
    /* Základní styl */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Fonty a barvy */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Tvar a interakce */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Přidání ikony šipky */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Styl emoji vlajek */
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

/* Stav hover */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Stav focus */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Ošetření prohlížeče Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Ošetření prohlížeče IE */
.lang-select::-ms-expand {
    display: none;
}

/* Ošetření pro dark mode */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optimalizace pro mobilní prostředí */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Větší dotyková oblast */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Širší výběrová oblast na mobilu */
    }
}
```
{: file='assets/css/lang-selector.css'}

Poté jsem do části [Chirpy tématu `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) hned před blok s třídou `sidebar-bottom` přidal následující tři řádky s třídou `lang-selector-wrapper`, aby se obsah `_includes/lang-selector.html`{: .filepath} načítal při buildu stránky.

{% raw %}
```liquid
  (vynecháno)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(vynecháno)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (12025.07.31. přidání funkce) Lokalizace jazyka rozvržení
Dříve jsem lokalizaci aplikoval jen na obsah (např. titulky a text článku) a jazyk rozvržení (např. názvy tabů v levém sidebaru, horní/spodní část webu nebo pravý panel) jsem nechával napevno v angličtině, která je výchozím jazykem webu. Osobně mi to přišlo dostačující, takže jsem necítil velkou potřebu se tím dál zabývat.  
Nedávno jsem ale při práci na [výše zmíněném patchi pro Open Graph metadata a standardní URL (canonical URL)](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-hlavicka) zjistil, že lokalizace jazyka rozvržení je možná velmi snadno a vyžaduje jen drobné úpravy. Pokud by to znamenalo velké a otravné zásahy do kódu, asi bych to neřešil, ale protože šlo o [jednoduchou úpravu na méně než 10 minut](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), rovnou jsem ji přidal.

### Přidání locales
I když Chirpy téma samo o sobě neumí současně poskytovat více jazykových verzí téže stránky a přepínat mezi nimi podle volby uživatele, [rozsah jazyků, které Chirpy podporuje pro UI, je už v základu poměrně široký](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). Stačí tedy selektivně stáhnout a doplnit potřebné locale soubory a případně jen vhodně upravit názvy souborů. Názvy locale souborů musí odpovídat položkám v seznamu `languages`, který jste definovali v `_config.yml`{: .filepath} v kroku [konfigurace](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#konfigurace).

> Ve skutečnosti (jak ještě zmíním níže) soubory v adresáři `_data`{: .filepath} ani nemusíte přidávat ručně, protože jsou základně poskytované přes [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy).
>
> V mém případě ale bylo obtížné použít locale soubory z Chirpy beze změn a bylo potřeba několik úprav:
> - Formát názvů locale souborů, které Chirpy poskytuje, obsahuje regionální kód (např. `ko-KR`, `ja-JP`), což neodpovídá formátu, který na tomto webu používám (`ko`, `ja` atd.).
> - Text licenčního upozornění je potřeba změnit: místo výchozího [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) použít [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), který používá tento blog.
> - U [korejského](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) a [japonského](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) locale mi jako rodilému mluvčímu přišlo několik výrazů nepřirozených, případně se pro tento blog nehodily, takže jsem je upravil.
> - Jak popisuji níže, z různých důvodů nemám rád letopočet „našeho letopočtu“ (AD/CE) a na tomto blogu jsem jako formát data zavedl [holocenní kalendář](https://en.wikipedia.org/wiki/Holocene_calendar), takže bylo potřeba upravit locale i kvůli tomu.
>   - V základu je silně nábožensky zabarvený a západocentrický.
>     - Neříkám, že Ježíš nebyl velká duchovní osobnost, a respektuji i pohled daného náboženství; kdyby šlo o interní používání v rámci víry (podobně jako buddhistické letopočty), nebyl by to problém. Problém je v tom, že jde o globálně používaný standard. Proč by měl být z pohledu nenáboženských lidí, vyznavačů jiných náboženství i neevropských kultur „rok 1“ zrovna rokem narození Ježíše, když existuje mnoho dalších významných postav (Konfucius, Buddha, Sókratés atd.)?
>     - Navíc ani není jisté, zda je „rok 1“ skutečně rokem Ježíšova narození; konsenzus je spíš takový, že se narodil o několik let dříve.
>   - Jde o letopočet vymyšlený před zavedením konceptu „0“, takže po roce 1 př. n. l. (-1) následuje rovnou rok 1 n. l. (1), což dělá výpočty roků neintuitivní.
>   - „Zabalí“ 10 000 let mezi přechodem do neolitu/zemědělské společnosti a Ježíšovým narozením do „před naším letopočtem“; i když vezmete jen období po vynálezu písma, jde o 3000–4000 let historie. To vede ke kognitivnímu zkreslení ve světových dějinách, zejména v dějinách starověku.
>
> Proto jsem zde locale soubory přidal přímo do `_data/locales`{: .filepath} a upravil je podle potřeby.  
> Pokud se vás to netýká a chcete používat locale soubory Chirpy beze změn, tento krok můžete přeskočit.
{: .prompt-tip }

### Integrace s Polyglot
Teď stačí lehce upravit jen následující dva soubory, aby integrace s Polyglot probíhala hladce.

> Pokud jste při zakládání repozitáře neforkovali přímo repozitář tématu, ale použili jste [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended), je možné, že tyto soubory ve vašem repozitáři vůbec nejsou. Je to proto, že jsou standardně poskytované přes [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy). V takovém případě si nejdřív stáhněte originální soubory z repozitáře [Chirpy tématu](https://github.com/cotes2020/jekyll-theme-chirpy) a uložte je do stejné cesty ve vašem repozitáři, a pak teprve provádějte úpravy. Při buildu Jekyll upřednostní soubory se stejným názvem ve vašem repozitáři před soubory poskytovanými přes [externí gem (jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy).
{: .prompt-tip }

#### '\_includes/lang.html'
Do prostřední části souboru [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) jsem přidal následující dva řádky, aby se v případě, že ve YAML front matter stránky není explicitně uvedená proměnná `lang`, upřednostnila [Polyglot proměnná `site.active_lang`](https://github.com/untra/polyglot?tab=readme-ov-file#features) před výchozím jazykem webu z `_config.yml`{: .filepath} (`site.lang`) nebo angličtinou (`'en'`).  
Tento soubor se volá při buildu ze všech stránek webu používajících téma Chirpy (z [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) kvůli deklaraci proměnné `lang`, která se následně používá pro lokalizaci jazyka rozvržení.

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

Priorita při deklaraci proměnné `lang`:
- Před úpravou:
  1. `page.lang` (pokud je definováno ve YAML front matter dané stránky)
  2. `site.lang` (pokud je definováno v `_config.yml`{: .filepath})
  3. `'en'`
- Po úpravě:
  1. `page.lang` (pokud je definováno ve YAML front matter dané stránky)
  2. **`site.active_lang`** (pokud je nasazen Polyglot)
  3. `site.lang` (pokud je definováno v `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
Podobně jsem upravil obsah souboru [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html), aby se atribut `lang` na kořenovém prvku HTML dokumentu (tag `<html>`) nastavoval korektně.

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

Priorita při nastavování atributu `lang` na tagu `<html>`:
- Před úpravou:
  1. `page.lang` (pokud je definováno ve YAML front matter dané stránky)
  2. `site.alt_lang` (pokud je definováno v `_config.yml`{: .filepath})
  3. `site.lang` (pokud je definováno v `_config.yml`{: .filepath})
  4. `unknown` (prázdný řetězec, `lang=""`)
- Po úpravě:
  1. `page.lang` (pokud je definováno ve YAML front matter dané stránky)
  2. **`site.active_lang`** (pokud je nasazen Polyglot)
  3. `site.alt_lang` (pokud je definováno v `_config.yml`{: .filepath})
  4. `site.lang` (pokud je definováno v `_config.yml`{: .filepath})
  5. `unknown` (prázdný řetězec, `lang=""`)

> Nechat jazyk webové stránky (`lang`) jako `unknown` se nedoporučuje; ideálně jej vždy nastavte na vhodnou hodnotu. Jak je vidět, jako fallback se používá hodnota `lang` v `_config.yml`{: .filepath}, takže bez ohledu na to, zda Polyglot používáte, je dobré mít tuto hodnotu správně nastavenou (v běžném případě už nastavená být bude). Pokud jste nasadili Polyglot nebo podobný i18n plugin, obvykle dává smysl nastavit ji na stejnou hodnotu jako [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#konfigurace).
{: .prompt-tip }

## Další čtení
Pokračování v [Dílu 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
