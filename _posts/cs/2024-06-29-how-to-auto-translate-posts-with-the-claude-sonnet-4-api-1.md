---
title: "Jak automaticky překládat příspěvky pomocí Claude Sonnet 4 API (1) – návrh promptu"
description: "Popisuji návrh promptu pro vícejazyčný překlad souborů v Markdownu a automatizaci v Pythonu s klíči Anthropic/Gemini API. 1. díl série je o designu promptu."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1/
---

## Úvod
Po zavedení Anthropic Claude 3.5 Sonnet API pro vícejazyčný překlad blogových příspěvků v červnu 12024 jsem přes řadu vylepšení promptů a automatizačních skriptů a přes upgrady verzí modelů provozoval tento překladový systém po téměř rok k plné spokojenosti. V této sérii proto chci popsat, proč jsem při zavádění zvolil model Claude Sonnet a proč jsem následně doplnil i Gemini 2.5 Pro, jak jsem navrhoval prompty a jak jsem přes Python skripty realizoval napojení na API a automatizaci.  
Série se skládá ze 2 článků a tento článek je prvním dílem.
- Díl 1: Představení modelů Claude Sonnet/Gemini 2.5 a důvody volby, prompt engineering (tento článek)
- Díl 2: [Napsání a nasazení Python automatizačního skriptu využívajícího API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## O Claude Sonnet
Modely řady Claude se podle velikosti nabízejí ve variantách Haiku, Sonnet a Opus.  
![Rozlišení tierů modelu Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> Zdroj obrázku: [oficiální web Anthropic Claude API](https://www.anthropic.com/api)

> (Doplněno 12025.05.29.)  
> Jde o snímek pořízený před rokem, takže ceny za token jsou uvedeny podle staré verze Claude 3, nicméně dělení podle velikosti na Haiku, Sonnet a Opus je stále platné. Ke konci května 12025 je cenová politika jednotlivých modelů od Anthropic následující.
>
> | Model | Base Input <br>Tokens | 5m Cache <br>Writes | 1h Cache <br>Writes | Cache Hits &<br> Refreshes | Output <br>Tokens |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | Claude Opus 4 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Haiku 3.5 | $0.80 / MTok | $1 / MTok | $1.6 / MTok | $0.08 / MTok | $4 / MTok |
> | Claude Opus 3 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Haiku 3 | $0.25 / MTok | $0.30 / MTok | $0.50 / MTok | $0.03 / MTok | $1.25 / MTok |
>
> Zdroj: [Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

A dále: jazykový model [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet), který Anthropic zveřejnil dne 21. června 12024 (korejského času) v [holocenním kalendáři](https://en.wikipedia.org/wiki/Holocene_calendar), dosahuje při stejné ceně a rychlosti jako původní Claude 3 Sonnet výkonu v uvažování, který překonává Claude 3 Opus. Převládá také názor, že zejména v psaní, jazykovém uvažování, vícejazyčném porozumění a překladu má oproti konkurenčnímu GPT‑4 řadu předností.  
![Ilustrační obrázek k Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Výsledky benchmarku výkonu Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> Zdroj obrázku: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Proč jsem pro překlad příspěvků zavedl Claude 3.5
I bez jazykových modelů jako Claude 3.5 či GPT‑4 existují komerční překladová API typu Google Translate nebo DeepL. Přesto jsem se rozhodl používat pro překlad LLM, protože na rozdíl od jiných komerčních překladových služeb může uživatel pomocí návrhu promptu dodat modelu nejen samotný text, ale i další kontext a požadavky, jako je účel článku nebo hlavní témata, a model pak může nabídnout překlad, který zohledňuje širší souvislosti.

DeepL i Google Translate obecně poskytují velmi kvalitní překlady, ale mají omezení: často nedokážou dobře zachytit téma a celkový kontext delších textů a nelze jim předat komplexní požadavky. Proto se při překladu dlouhých odborných článků (nikoli běžné konverzace) relativně častěji objevují nepřirozené formulace a je obtížné přesně vynutit konkrétní výstupní formát (Markdown, YAML frontmatter apod.).

Zejména u Claude, jak jsem uvedl výše, existovalo mnoho hodnocení, že je v psaní, jazykovém uvažování, vícejazyčném porozumění a překladu oproti konkurenčnímu GPT‑4 relativně lepší. Když jsem si to sám rychle otestoval, překlady byly oproti GPT‑4 plynulejší, a proto jsem v červnu 12024 usoudil, že je vhodný pro překlad technických (inženýrských) článků na tomto blogu do více jazyků.

## Historie aktualizací
### 12024.07.01.
Jak jsem shrnul v [samostatném článku](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), dokončil jsem úvodní práce: nasazení pluginu [Polyglot] a podle toho úpravy `_config.yml`{: .filepath}, HTML hlavičky a sitemap.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Následně jsem zvolil [model Claude 3.5 Sonnet pro účely překladu a po počáteční implementaci a ověření Python skriptu pro integraci s API, který tato série popisuje, jsem jej nasadil.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
Dne 22. října 12024 Anthropic oznámil upgrade API pro Claude 3.5 Sonnet („claude-3-5-sonnet-20241022“) a Claude 3.5 Haiku. Kvůli [problému popsanému níže](#prevence-lenosti-12024-10-31-halloween-patch) však na blogu stále používám původní API „claude-3-5-sonnet-20240620“.

### 12025.04.02.
[Přešel jsem z modelu „claude-3-5-sonnet-20240620“ na „claude-3-7-sonnet-20250219“.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Přešel jsem z modelu „claude-3-7-sonnet-20250219“ na „claude-sonnet-4-20250514“.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Výsledky benchmarku výkonu Claude 4](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> Zdroj obrázku: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

V závislosti na podmínkách použití se to může lišit, ale obecně panuje od vydání Claude 3.7 Sonnet poměrně široká shoda, že pro programování je Claude aktuálně nejvýkonnější model. Anthropic navíc aktivně prezentuje nadprůměrný výkon v programování jako jednu z hlavních předností svých modelů vůči konkurenci (OpenAI, Google atd.). I při oznámení Claude Opus 4 a Claude Sonnet 4 bylo patrné pokračování strategie, která zdůrazňuje programátorské schopnosti a míří na vývojáře jako hlavní cílovou skupinu.

Samozřejmě, z publikovaných benchmarků je vidět zlepšení napříč oblastmi i mimo programování. Pro překladovou práci, kterou tento článek řeší, se zejména zvýšení výkonu ve vícejazyčném Q&A (MMMLU) a v matematických úlohách (AIME 2025) jeví jako obzvlášť relevantní. Z vlastních krátkých testů jsem potvrdil, že oproti předchozímu modelu Claude 3.7 Sonnet jsou překlady Claude Sonnet 4 lepší v přirozenosti vyjadřování, odbornosti i konzistenci terminologie.

> V tuto chvíli si alespoň pro technické články psané korejsky (jako na tomto blogu) stále myslím, že pro vícejazyčný překlad jsou modely Claude nejlepší. V poslední době se však výkon modelů Google Gemini viditelně zlepšil a v květnu letošního roku byl zveřejněn dokonce i model Gemini 2.5 (zatím ve fázi Preview).  
> Při porovnání Gemini 2.0 Flash s Claude 3.7 Sonnet a Claude Sonnet 4 jsem vyhodnotil překladovou kvalitu Claude jako lepší, nicméně vícejazyčné schopnosti Gemini jsou také velmi silné. Navíc, i přes status Preview byl Gemini 2.5 Preview 05‑06 v matematice, řešení fyzikálních úloh i ve výkladových schopnostech dokonce lepší než Claude Opus 4. Proto si netroufám tvrdit, jak dopadne srovnání po oficiálním vydání.  
> Do určitého limitu lze používat [bezplatnou úroveň (Free Tier)](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits) a i v placené úrovni (Paid Tier) jsou poplatky za API výrazně nižší než u Claude, takže cenová konkurenceschopnost Gemini je výborná. Pokud by výkon byl alespoň srovnatelný, může být Gemini rozumnou alternativou. Protože je Gemini 2.5 stále v Preview, považuji jeho nasazení do automatizace zatím za předčasné, ale po vydání finální verze jej plánuji otestovat.
{: .prompt-tip }

### 12025.07.04.
- [Přidána funkce inkrementálního překladu](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/978032f52c7d85ecb6b213233d5404d844402965)
- Rozdělení používaných modelů podle cílového jazyka ([Commit 3890c82](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3890c820c1f3df34f8e4686b8903ca4ee770ba15), [Commit fe0fc63](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/fe0fc63ae4e2764f3dfe24ff259b4477f120b9ed))
  - Pro překlad do angličtiny, tchajwanské čínštiny a němčiny se používá „gemini-2.5-pro“
  - Pro překlad do japonštiny, španělštiny, portugalštiny a francouzštiny se nadále používá původní „claude-sonnet-4-20250514“
- Uvažoval jsem o zvýšení `temperature` z `0.0` na `0.2`, ale nakonec jsem se vrátil k původní hodnotě

Dne 4. července 12025 konečně modely Gemini 2.5 Pro a Gemini 2.5 Flash opustily fázi Preview a byly oficiálně vydány. Počet testovacích příkladů byl sice omezený, ale při osobním testování se mi zdálo, že i Gemini 2.5 Flash u anglických překladů v některých místech zpracovává text přirozeněji než dosavadní Claude Sonnet 4. Když se navíc vezme v úvahu, že cena za výstupní token je u Gemini 2.5 Pro a Flash (v placené úrovni) oproti Claude Sonnet 4 přibližně 1,5× a 6× nižší, lze říci, že pro angličtinu jde v červenci 12025 o nejkonkurenceschopnější model. U Gemini 2.5 Flash se však projevují limity menšího modelu: ačkoli jsou výstupy obecně kvalitní, občas dochází k problémům typu rozbití formátu markdown dokumentu nebo interních odkazů, takže se nehodí pro složité překlady a zpracování dokumentů. U angličtiny má Gemini 2.5 Pro jednoznačně špičkový výkon, ale u **většiny portugalských (pt‑BR) příspěvků** a u některých španělských příspěvků působil nejistě, pravděpodobně kvůli nedostatku trénovacích dat. Při analýze chyb šlo většinou o záměny podobných znaků jako „í“ vs. „i“, „ó“ vs. „o“, „ç“ vs. „c“ a „ã“ vs. „a“. U francouzštiny se takové problémy neobjevily, ale občas byly věty přehnaně rozvleklé, a tím hůře čitelné než u Claude Sonnet 4.

Jiné jazyky než angličtinu neovládám natolik, abych provedl detailní a přesné srovnání, ale zhruba mi kvalita odpovědí podle jazyků vyšla takto:
- angličtina, němčina, tchajwanská čínština: lepší je Gemini
- japonština, francouzština, španělština, portugalština: lepší je Claude

Dále jsem do překladového skriptu přidal funkci inkrementálního překladu (Incremental Translation). Při psaní se snažím být pečlivý, ale i tak se stává, že po publikaci později najdu drobné překlepy, nebo mě napadne doplnění či úprava. V takových případech, i když je změna jen malá, původní skript musel znovu přeložit a vypsat celý článek od začátku do konce, což bylo z hlediska spotřeby API poněkud neefektivní. Proto jsem přidal funkci, která je napojená na git: provede porovnání verzí korejského originálu, vytáhne změněné části ve formátu diff, ty pak spolu s celým původním překladem vloží do promptu a jako výstup získá diff patch pro překlad, takže lze selektivně upravit jen potřebné části. Protože cena za vstupní token je výrazně nižší než za výstupní token, lze očekávat smysluplné úspory. Do budoucna tak i při drobných úpravách nebudu muset ručně editovat překlady v jednotlivých jazycích a budu moci bez obav spouštět automatický překlad.

Parametr `temperature` je mimochodem proměnná, která při generování odpovědi určuje, jakou míru náhodnosti model použije při výběru dalšího slova. Jde o nezáporné reálné číslo (\*jak bude uvedeno níže, typicky v rozsahu $[0,1]$ nebo $[0,2]$): čím blíže k nule, tím determinističtější a konzistentnější odpovědi; čím vyšší hodnota, tím rozmanitější a kreativnější výstupy.  
Cílem překladu je předat význam a tón originálu co nejpřesněji a konzistentně, nikoli kreativně vytvářet nový obsah, takže pro přesnost, konzistenci a předvídatelnost je vhodné používat nízkou hodnotu `temperature`. Při `temperature = 0.0` však model vždy vybírá pouze nejpravděpodobnější slova, což může někdy vést k překladu příliš blízkému doslovnosti nebo k nepřirozeně strnulým větám. Proto jsem uvažoval o mírném zvýšení na `0.2`, aby se výstupy trochu „uvolnily“, ale narazil jsem na výrazný pokles přesnosti při zpracování složitých odkazů obsahujících fragment identifier, a tak jsem se rozhodl to nenasazovat.

> \* Ve většině praktických případů se `temperature` používá v intervalu 0 až 1 a povolený rozsah v Anthropic API je také $[0,1]$. OpenAI API a Gemini API umožňují širší rozsah $[0,2]$, ale to neznamená, že se škála „zdvojnásobí“; význam $T=1$ je stejný jako u modelů s rozsahem $[0,1]$. 
>
> Vnitřně jazykový model funguje jako určitý typ funkce: vezme prompt a dosud vygenerované tokeny jako vstup a jako výstup vrátí pravděpodobnostní rozdělení pro další token; výsledek vzorkování z tohoto rozdělení určí další token a ten se vypíše. Referenční stav je $T=1$: při $T<1$ se rozdělení „zúží a zostří“, takže model konzistentněji vybírá nejpravděpodobnější slova; při $T>1$ se naopak rozdělení „zploští“ a uměle se zvýší pravděpodobnost slov, která by si model jinak téměř nevybral.
>
> V oblasti $T>1$ může kvalita výstupu klesat a odpovědi mohou být nepředvídatelné: mohou se objevovat tokeny mimo kontext nebo gramaticky nesmyslné věty. Pro většinu úloh, zejména v produkčním prostředí (production), je vhodné držet `temperature` v rozsahu $[0,1]$. Hodnoty větší než 1 se hodí spíše experimentálně pro brainstorming či podporu tvorby (např. generování prvního návrhu scénáře), ale protože roste riziko halucinací a gramatických či logických chyb, je lepší je používat s lidským zásahem a kontrolou, nikoli plně automatizovaně.
>
> Pro podrobnější vysvětlení `temperature` u jazykových modelů lze odkázat na následující texty.
> - [Tamanna, *Understanding LLM Temperature* (2025).](https://medium.com/@tam.tamanna18/understanding-llm-temperature-7d838277a7d9)
> - [Tickr Data, *The Impact of Temperature on LLM Performance* (2023).](https://www.tickr.com/blog/posts/impact-of-temperature-on-llms/)
> - [Anik Das, *Temperature in Prompt Engineering* (2025).](https://peerlist.io/anikdas/articles/temperature-in-prompt-engineering)
> - [Peeperkorn et al., *Is Temperature the Creativity Parameter of LLMs?*, arXiv:2405.00492 (2024).](https://arxiv.org/abs/2405.00492)
> - [Colt Steele, *Understanding OpenAI’s Temperature Parameter* (2023).](https://www.coltsteele.com/tips/understanding-openai-s-temperature-parameter)
> - [Damon Garn, *Understanding the role of temperature settings in AI output*, TechTarget (2025).](https://www.techtarget.com/searchenterpriseai/tip/Understanding-the-role-of-temperature-settings-in-AI-output)
{: .prompt-info }

## Návrh promptu
### Základní principy při zadávání požadavků
Chcete‑li od jazykového modelu získat uspokojivý výstup, který odpovídá cíli, musíte mu dát adekvátní prompt. „Návrh promptu“ může působit abstraktně, ale ve skutečnosti se „jak dobře něco požádat“ příliš neliší podle toho, zda je protějšek člověk nebo jazykový model. Když k tomu přistoupíte z této perspektivy, není to nijak obtížné. Je dobré jasně popsat situaci a požadavky (kdo, co, kdy, kde, proč, jak) a případně přidat několik konkrétních příkladů. Existuje mnoho tipů a technik pro návrh promptů, ale většina z nich vychází z těchto základních principů.

#### Celkový tón
Existuje řada zpráv, že když je prompt napsán zdvořilým, prosícím tónem namísto autoritativních rozkazů, jazykový model často generuje kvalitnější odpovědi. V běžné společnosti také platí, že když někoho o něco žádáte zdvořile, je pravděpodobnější, že úkol udělá pečlivěji; zdá se, že jazykové modely napodobují podobné vzorce odpovědí, protože se je z dat naučily.

#### Přiřazení role a vysvětlení situace (kdo, proč)
Nejprve jsem přiřadil roli *„profesionální technický překladatel (professional technical translator)“* a poskytl kontext o uživateli jako o *„inženýrském blogerovi, který publikuje hlavně o matematice, fyzice a datové vědě“*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Požadavky ve velkých obrysech (co)
Dále jsem požádal, aby byl poskytnutý text v Markdownu přeložen ze {source_lang} do {target_lang} při zachování formátu.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Při volání Claude API se do míst {source_lang} a {target_lang} v promptu přes Python f-string vloží proměnné pro zdrojový a cílový jazyk překladu.
{: .prompt-info }

#### Upřesnění požadavků a příklady (jak)
U jednoduchých úloh může být výsledek požadované kvality dosažitelný už po předchozích krocích. U složitějších úkolů ale může být nutné přidat podrobnější vysvětlení.

Pokud je podmínek mnoho a jsou komplexní, je čitelnější je předat stručně jako seznam (namísto rozvláčného textu). Usnadňuje to pochopení jak čtenáři (ať už člověku, nebo modelu). A pokud je to potřeba, hodí se uvést i příklady.  
V tomto případě jsem přidal následující podmínky.

##### Zpracování YAML front matter
Ve front matter (YAML) na začátku markdown příspěvku, který se uploaduje na Jekyll blog, se zapisují informace jako `title`, `description`, `categories` a `tags`. Například YAML front matter tohoto článku vypadá takto:

```yaml
---
title: "Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인"
description: "마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic/Gemini API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

Při překladu příspěvku je třeba přeložit tagy `title` a `description`, ale kvůli konzistenci URL je z hlediska údržby výhodnější nepřekládat názvy kategorií (`categories`) a tagů (`tags`) a ponechat je v angličtině. Proto jsem přidal pokyn, aby se nepřekládalo nic jiného než `title` a `description`. Model už pravděpodobně ví, co je YAML front matter, takže většinou stačí i takto stručné vysvětlení.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Přidal jsem formulaci „under any circumstances, regardless of the language you are translating to“, abych zdůraznil, že ostatní tagy ve YAML front matter se nesmí měnit **bez výjimek**.
{: .prompt-tip }

(aktualizace 12025.04.02.)  
Dále jsem u tagu `description` dal pokyn, aby byl s ohledem na SEO napsán v přiměřené délce, takto:

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Zpracování případů, kdy originál obsahuje jiné jazyky než zdrojový
Když píšu korejský originál, často při prvním zavedení definice nějakého konceptu nebo při použití určitých odborných termínů připojuji do závorky i anglický výraz, například *중성자 감쇠 (Neutron Attenuation)*. Při překladu takových míst pak vznikal problém nekonzistence: někdy se závorky zachovaly, jindy se anglický výraz v závorce vynechal. Proto jsem stanovil následující podrobnější pravidla.
- U odborných termínů:
  - při překladu do jazyků nezaložených na latince (např. japonština) zachovat formát „překlad (anglický výraz)“;
  - při překladu do jazyků založených na latince (španělština, portugalština, francouzština) povolit jak samostatný „překlad“, tak i „překlad (anglický výraz)“ a nechat model zvolit vhodnější variantu.
- U vlastních jmen musí být původní pravopis uvedený v závorce v nějaké podobě zachován i v překladu.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language,
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Zpracování odkazů vedoucích na jiné příspěvky
Některé příspěvky obsahují odkazy na jiné příspěvky. Ve fázi testování, když jsem k tomu nedal žádné zvláštní instrukce, model často interpretoval jako „překládanou část“ i cestu v URL, a tím interní odkazy rozbil. Tento problém jsem vyřešil přidáním následující věty do promptu.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(aktualizace 12025.04.06.)  
Po přidání této instrukce model při překladu obvykle správně zachází s cestou v URL, takže frekvence rozbitých odkazů výrazně klesla. U odkazů s fragment identifier ale zůstával limit: pokud model nezná obsah cílového článku, musí fragment v podstatě jen odhadnout, takže problém nelze zcela odstranit. Proto jsem vylepšil Python skript i prompt tak, že do uživatelského promptu přidávám kontext o příspěvcích, na které odkazují hash fragmenty, uvnitř XML tagu `<reference_context>`. Pak se překlad odkazů zpracuje v souladu s tímto kontextem. Po nasazení aktualizace bylo možné většině problémů s rozbitými odkazy předejít a u těsně provázaných sérií článků lze očekávat i konzistentnější překlad napříč více příspěvky.

Do systémového promptu dávám následující instrukci.
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

A část `<reference_context>` v uživatelském promptu má následující formát a obsah; přidává se až za text hlavního článku, který se má přeložit.
```xml
<reference_context>
The following are contents of posts linked with hash fragments in the original post. 
Use these for context when translating links and references:

<referenced_post path="{post_1_path}" hash="{hash_fragment_1}">
{post_content}
</referenced_post>

<referenced_post path="{post__2_path}" hash="{hash_fragment_2}">
{post_content}
</referenced_post>

...

</reference_context>
```

> Konkrétní implementaci viz [díl 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) této série a Python skript v GitHub repozitáři: [Python script](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py).
{: .prompt-tip }

##### Vypisovat pouze samotný překlad
Nakonec dávám instrukci, aby model do odpovědi nepřidával žádné další věty a vypsal pouze samotný překlad.

```xml
<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or "```markdown" or something of that nature!!</important>
```

### Další techniky návrhu promptu
Na rozdíl od zadávání práce lidem existují u jazykových modelů i některé specifické techniky.

Na webu je k tomu mnoho užitečných materiálů; jako několik reprezentativních tipů, které se dají použít obecně, bych uvedl následující.  
Čerpal jsem hlavně z [průvodce prompt engineeringem v oficiální dokumentaci Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Strukturování pomocí XML tagů
Ve skutečnosti jsem to už výše průběžně používal. U složitých promptů, které obsahují více kontextu, instrukcí, formátů a příkladů, pomáhá používat vhodné XML tagy jako `<instructions>`, `<example>`, `<format>` apod. Jazykovému modelu to usnadňuje přesnou interpretaci promptu a vede k výstupům vyšší kvality odpovídajícím záměru. V GitHub repozitáři [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) jsou praktické XML tagy pro psaní promptů dobře shrnuté; doporučuji se podívat.

#### Technika krokového uvažování (CoT, Chain-of-Thought)
U úloh, které vyžadují vyšší míru uvažování (např. řešení matematických úloh nebo tvorba komplexních dokumentů), lze výkon výrazně zvýšit tím, že model navedete, aby přemýšlel po krocích. Je však třeba počítat s tím, že se může prodloužit latence odpovědi a že tato technika není užitečná pro všechny typy úloh.

#### Prompt chaining
U složitých úloh může mít jeden prompt své limity. V takovém případě lze zvážit rozdělení workflow do více kroků: pro každý krok dát specializovaný prompt a výstup z předchozího kroku použít jako vstup pro další. Tomu se říká prompt chaining.

#### Předvyplnění začátku odpovědi
Při zadávání promptu lze předem poskytnout začátek očekávané odpovědi a nechat model pokračovat. Tím lze přeskočit zbytečné úvody (např. pozdravy) nebo vynutit výstup v konkrétním formátu, jako je XML či JSON. [U Anthropic API lze tuto techniku použít tak, že při volání odešlete nejen zprávu `User`, ale i zprávu `Assistant`.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevence „flákání“ (12024.10.31. Halloween patch)
Od chvíle, kdy jsem článek původně napsal, jsem sice prompt jednou či dvakrát mírně vylepšil a některé instrukce zpřesnil, ale v zásadě během čtyř měsíců používání tohoto automatizačního systému nenastal žádný větší problém.

Jenže od 12024.10.31. kolem 18:00 (korejského času) se začal opakovaně objevovat podivný jev: když jsem nechal přeložit nově napsaný příspěvek, model přeložil pouze první část „TL;DR“ a pak překlad svévolně ukončil.

Předpokládané příčiny a řešení tohoto problému jsem popsal v [samostatném článku](/posts/does-ai-hate-to-work-on-halloween); doporučuji jej přečíst.

### Hotový systémový prompt
Výsledek návrhu promptu po výše uvedených krocích je k vidění v [dalším dílu](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Další čtení
Pokračování v [části 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
