---
title: "Vytvoření a správa blogu na GitHub Pages"
description: "Probereme vlastnosti a rozdíly statických a dynamických webů, vysvětlíme static site generátory (SSG) a ukážeme, jak hostovat Jekyll blog na GitHub Pages."
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Od začátku roku 12021 hostuji blog na GitHub Pages pomocí Jekyllu. Jenže při původním sestavování blogu jsem si instalační postup pořádně nezapsal, takže jsem později při údržbě narazil na určité potíže. Proto jsem se rozhodl stručně sepsat instalaci i způsob údržby.  

(+ aktualizace obsahu 12024.12)

## 1. Generátor statických webů & webhosting
### 1-1. Statická webová stránka vs dynamická webová stránka
#### Statická webová stránka (Static Web Page)
- webová stránka, která uživateli předává data uložená na serveru „tak, jak jsou“
- webový server doručí předem uloženou stránku odpovídající uživatelskému požadavku
- uživatel uvidí stejnou stránku, dokud nezmění data uložená na serveru
- obvykle rychlá odezva, protože stačí odeslat příslušné soubory bez dalších výpočtů
- nízké náklady na zprovoznění, protože se skládá jen z jednoduchých souborů a stačí webový server
- služby jsou omezené, protože se zobrazuje jen uložený obsah
- přidávání, úpravy a mazání dat musí správce provádět ručně
- struktura je pro vyhledávače snadno procházetelná (crawling), a tedy relativně výhodná pro optimalizaci pro vyhledávače (SEO)

#### Dynamická webová stránka (Dynamic Web Page)
- webová stránka, která zpracuje data uložená na serveru skriptem a teprve poté je předá
- webový server interpretuje požadavek uživatele, zpracuje data a doručí takto vygenerovanou stránku
- uživatel uvidí stránku, která se mění podle situace, času, požadavků apod.
- relativně pomalejší odezva, protože je potřeba zpracovávat skripty pro doručení stránky
- vedle webového serveru je potřeba aplikační server, takže při nasazení vznikají dodatečné náklady
- lze poskytovat rozmanité služby díky dynamickému skládání informací
- podle struktury webu může uživatel přidávat, upravovat a mazat data přímo v prohlížeči

### 1-2. Generátor statických webů (SSG, Static Site Generator)
- nástroj, který generuje statické webové stránky na základě raw dat (obvykle textové soubory ve formátu markdown) a předdefinovaných šablon
- automatizuje proces: nemusíte ručně psát jednotlivé HTML stránky; napíšete post v Markdownu, web se sestaví (build) a nasadí
- např.) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- bezplatná hostingová služba statických webů od GitHubu
- na účet lze hostovat 1 osobní „hlavní“ stránku a neomezeně vytvářet a hostovat projektové dokumentační stránky pro jednotlivé repozitáře
- vytvoříte repozitář pojmenovaný ve tvaru `{username}.github.io` podle svého GitHub username a do něj buď přímo pushnete vygenerované HTML, nebo sestavení a nasazení provedete pomocí GitHub Actions
- máte-li vlastní doménu, můžete ji v nastavení připojit a místo výchozí domény `{username}.github.io` používat jinou adresu

## 2. Volba SSG a tématu

### 2-1. Proč jsem zvolil Jekyll
Existuje řada SSG jako Jekyll, Hugo, Gatsby atd., ale rozhodl jsem se pro Jekyll. Kritéria, která jsem zvažoval při výběru, a důvody volby Jekyllu jsou následující.
- Lze minimalizovat zbytečné pokusy-omyly a soustředit se na psaní a provoz blogu?
  - Jekyll je oficiálně podporovaný generátor statických webů na GitHub Pages. Samozřejmě lze na GitHub Pages hostovat i jiné SSG jako Hugo či Gatsby a alternativně použít třeba Netlify nebo úplně jiný hosting, ale u osobního blogu této velikosti není technicky zásadní, jaké SSG je použito, ani rychlost buildu či výkon. Proto jsem usoudil, že je lepší zvolit něco s co nejjednodušší údržbou a s dostatkem referenční dokumentace.
  - Jekyll má navíc oproti konkurentům jako Hugo či Gatsby nejdelší dobu vývoje. Díky tomu je dobře zdokumentovaný a při problémech existuje obrovské množství materiálů, o které se lze opřít.
- Je k dispozici dostatek témat a pluginů?
  - I když používáte SSG místo ručního psaní HTML, vytvářet si vlastní šablony je pracné, zabere to čas a často to ani není nutné. Na webu je mnoho kvalitních veřejně dostupných témat; stačí si vybrat a použít to, které se vám líbí.
  - Navíc primárně používám C nebo Python, takže Ruby u Jekyllu nebo Go u Huga jsem moc neznal; o to víc jsem se chtěl opřít o existující témata a pluginy.
  - U Jekyllu jsem rychle našel téma, které mi bylo sympatické, zatímco u Huga nebo Gatsbyho mi přišlo, že je méně témat vhodných přímo pro osobní blog. Zřejmě se zde projeví i dobrá integrace s GitHub Pages, které vývojáři pro osobní blogy často používají, a také delší doba vývoje.

### 2-2. Volba tématu
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- téma, které jsem používal přibližně 1 rok a 3 měsíce od úplného začátku
- podpora komentářů přes Disqus, Discourse, utterances apod.
- podpora třídění podle kategorií a tagů
- základní podpora Google Analytics
- možnost zvolit předdefinované skiny
- později jsem objevil designově líbivější téma Chirpy a přešel na něj, ale vzhledem k tomu, že je to „inženýrsky“ laděný blog, i když Minimal Mistakes není vyloženě hezké, má poměrně čistý design a dalo se používat bez problémů.

#### Chirpy Jekyll Theme (12022.04 - současnost)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- téma, které používám od migrace v dubnu 12022 až dosud
- podpora vícenásobných kategorií a tagů
- základní podpora zápisu matematiky (LaTeX) přes MathJax
- základní podpora diagramů přes Mermaid
- podpora komentářů přes Disqus, Giscus apod.
- podpora Google Analytics, GoatCounter
- podpora světlého i tmavého režimu
- v době přechodu bylo potřeba u Minimal Mistakes MathJax a Mermaid doplnit vlastní úpravou, protože je téma samo nepodporovalo; u Chirpy jsou tyto funkce integrovány. Samozřejmě i „customizace“ tehdy nebyla nic dramatického, ale je to příjemná drobná výhoda.
- hlavně: vypadá hezky. Minimal Mistakes je čisté, ale má určitou „tuhost“, takže se hodí spíš na oficiální projektovou dokumentaci nebo portfolio než na blog. Chirpy má výhodu v designu, který se neztratí ani ve srovnání s komerčními blogovacími platformami jako Tistory, Medium, velog apod.

## 3. Vytvoření GitHub repozitáře, build a nasazení
Popis je založen na tématu Chirpy Jekyll Theme, které aktuálně (12024.06) používám, a předpokládá se, že Git je již nainstalovaný.  
Viz [oficiální instalační průvodce Jekyll](https://jekyllrb.com/docs/installation/) a [oficiální stránka Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalace Ruby & Jekyll
Podle [oficiálního instalačního průvodce Jekyll](https://jekyllrb.com/docs/installation/) nainstalujte Ruby a Jekyll dle svého operačního systému.

### 3-2. Vytvoření GitHub repozitáře
[Oficiální stránka Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) představuje dvě metody:
1. načíst klíčové soubory jako gem `jekyll-theme-chirpy` a zbytek zdrojů vzít ze šablony [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - výhoda: jak bude popsáno níže, snadno se aplikují upgrady verzí
  - nevýhoda: při rozsáhlé customizaci to může být naopak nepohodlné
2. fork repozitáře [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) jako repozitáře svého blogu
  - výhoda: všechny soubory spravujete přímo v repozitáři, takže je pohodlné upravovat kód a přidávat funkce, které téma nepodporuje
  - nevýhoda: pro aplikaci upgradu je nutné mergnout [nejnovější upstream tagy původního repozitáře](https://github.com/cotes2020/jekyll-theme-chirpy/tags) a podle situace může dojít ke konfliktům mezi vámi upraveným kódem a novou verzí. V takovém případě je třeba konflikty vyřešit ručně.

Zvolil jsem metodu 1. U Chirpy je základní kvalita vysoká, takže z pohledu většiny uživatelů není mnoho co upravovat. Navíc se i v roce 12024 vyvíjí velmi aktivně a průběžně se vylepšují funkce, takže pokud neplánujete opravdu zásadní „přestavbu“, výhody držení kroku s upstreamem obvykle převáží výhody přímé customizace. I oficiální průvodce Chirpy doporučuje metodu 1 většině uživatelů.

### 3-3. Klíčová nastavení
Potřebná nastavení proveďte v souboru `_config.yml`{: .filepath} v kořenovém adresáři a v souborech `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Komentáře jsou dobře napsané a volby jsou intuitivní, takže se to dá nastavit bez větších potíží. Z externích kroků bývá potřeba hlavně registrace ověřovacího kódu pro napojení na Google Search Console a propojení nástrojů pro webmastery jako Google Analytics nebo GoatCounter; ani to ale obvykle není složité a není to hlavní téma tohoto článku, proto podrobnosti vynechávám.

### 3-4. Lokální build
Není to povinné, ale když píšete nový post nebo něco upravujete na webu, můžete si chtít předem ověřit, zda se vše zobrazí správně. V takovém případě otevřete terminál v kořenovém adresáři lokálního repozitáře a spusťte:
```console
$ bundle exec jekyll s
```
Po chvíli se web lokálně sestaví a výsledek si můžete prohlédnout na <http://127.0.0.1:4000>.

### 3-5. Nasazení
Existují dvě metody.
1. využití GitHub Actions (pokud hostujete na GitHub Pages)
  - pokud používáte GitHub Free Plan, repozitář musí zůstat public
  - na webu GitHubu vyberte v repozitáři záložku *Settings*, v levé navigaci klikněte na *Code and automation > Pages* a v sekci **Source** zvolte možnost **GitHub Actions**
  - po dokončení nastavení se při každém pushi nového commitu automaticky spustí workflow *Build and Deploy*
2. build a nasazení ručně (pokud používáte jiný hosting nebo self-hosting)
  - spusťte následující příkaz a web si sestavte sami
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - nahrajte výsledek buildu z adresáře `_site` na server

## 4. Psaní postů
V tématu Chirpy je [průvodce psaním postu](https://chirpy.cotes.page/posts/write-a-new-post/) dobře zdokumentovaný, včetně voleb a možností. Kromě toho, co popisuji v tomto článku, nabízí i různé další funkce; pokud je budete potřebovat, podívejte se do oficiální dokumentace. Základní syntaxi GitHub Flavored Markdown jsem navíc už dříve shrnul v [samostatném článku](/posts/github-markdown-syntax-summary/). Zde shrnu hlavní body, které je dobré mít na paměti při každém publikování.

### Vytvoření markdown souboru
- formát názvu: `YYYY-MM-DD-TITLE.md`{: .filepath}
- umístění: adresář `_posts`{: .filepath}

### Psaní Front Matter
Na začátku markdown souboru je potřeba správně zapsat Front Matter.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: název postu
- **description**: shrnutí. Pokud ho nenapíšete, automaticky se použije část začátku textu, ale kvůli SEO se doporučuje description meta tag napsat ručně a vhodně. Přiměřená délka je zhruba 135–160 znaků v latince, resp. 80–110 znaků v korejštině.
- **date**: přesné datum a čas napsání postu a timezone (lze vynechat; při vynechání se automaticky použije datum vytvoření souboru nebo datum poslední úpravy)
- **categories**: kategorizace postu
- **tags**: tagy aplikované na post
- **image**: vložení náhledového obrázku v horní části postu
  - **path**: cesta k souboru obrázku
  - **alt**: alternativní text (lze vynechat)
- **toc**: zapnutí/vypnutí obsahu (TOC) v pravém sidebaru; výchozí je `true`
- **comments**: použijte, pokud chcete explicitně určit, zda jsou u konkrétního postu povoleny komentáře, nezávisle na globálním nastavení webu
- **math**: aktivace vestavěného zobrazování matematiky přes [MathJax](https://www.mathjax.org/); kvůli výkonu je ve výchozím stavu vypnuto (`false`)
- **mermaid**: aktivace vestavěného zobrazování diagramů přes [Mermaid](https://github.com/mermaid-js/mermaid); ve výchozím stavu vypnuto (`false`)

## 5. Upgrade

Dále předpokládám, že jste v [3-2](#3-2-vytvoření-github-repozitáře) zvolili metodu 1. Pokud jste zvolili metodu 2, jak bylo zmíněno výše, musíte nejnovější upstream tagy mergovat ručně.

1. Upravte `Gemfile`{: .filepath} a nastavte novou verzi gemu `jekyll-theme-chirpy`.
2. U major upgradu se mohly změnit i klíčové soubory a konfigurační volby, které nejsou součástí gemu `jekyll-theme-chirpy`. V takovém případě zkontrolujte změny přes níže uvedené GitHub API a aplikujte je ručně.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
