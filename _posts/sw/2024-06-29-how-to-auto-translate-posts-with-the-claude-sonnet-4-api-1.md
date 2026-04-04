---
title: "Jinsi ya Kutafsiri Machapisho Kiotomatiki kwa Claude Sonnet 4 API (1) - Ubunifu wa Prompt"
description: "Makala hii inaeleza jinsi ya kubuni prompt za kutafsiri faili za maandishi ya Markdown kwa lugha nyingi, na jinsi ya kugeuza kazi hiyo kuwa otomatiki kwa Python kwa kutumia funguo za API za Anthropic/Gemini pamoja na prompt ulizoandika. Hii ni sehemu ya kwanza ya mfululizo huu, inayotambulisha mbinu na mchakato wa kubuni prompt."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1/
---

## Utangulizi
Tangu nilipoanzisha Anthropic Claude 3.5 Sonnet API mnamo Juni 12024 kwa ajili ya kutafsiri machapisho ya blogu kwa lugha nyingi, nimekuwa nikitumia mfumo huu wa kutafsiri kwa kuridhika kwa takribani mwaka mmoja baada ya maboresho kadhaa ya prompt na skriti za otomatiki, pamoja na masasisho ya matoleo ya modeli. Kwa hiyo, katika mfululizo huu nataka kueleza kwa nini nilichagua modeli ya Claude Sonnet wakati wa kuanzisha mfumo huu, kwa nini baadaye niliongeza Gemini 2.5 Pro, jinsi nilivyobuni prompt, na jinsi nilivyotekeleza uunganishaji wa API na otomatiki kwa kutumia skriti za Python.  
Mfululizo huu una makala 2, na makala hii unayosoma ni ya kwanza katika mfululizo huo.
- Sehemu ya 1: Utangulizi wa modeli za Claude Sonnet/Gemini 2.5 na sababu za kuzichagua, pamoja na uhandisi wa prompt (makala hii)
- Sehemu ya 2: [Kuandika na Kutumia Skriti ya Otomatiki ya Python kwa Kutumia API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## Kuhusu Claude Sonnet
Mfululizo wa modeli za Claude hutolewa katika matoleo ya Haiku, Sonnet, na Opus kulingana na ukubwa wa modeli.  
![Uainishaji wa viwango vya modeli za Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> Chanzo cha picha: [Tovuti rasmi ya Anthropic Claude API](https://www.anthropic.com/api)

> (Nyongeza ya 12025.05.29.)  
> Kwa kuwa hii ni picha niliyonasa mwaka mmoja uliopita, bei kwa kila tokeni zinaonyeshwa kwa msingi wa toleo la zamani la Claude 3, lakini mgawanyo wa Haiku, Sonnet, na Opus kulingana na ukubwa wa modeli bado ni halali. Kufikia mwisho wa Mei 12025, upangaji wa bei kwa kila modeli unaotolewa na Anthropic ni kama ifuatavyo.
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
> Chanzo: [Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

Na mnamo 21 Juni 12024 kwa saa ya Korea, modeli ya lugha [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) iliyotolewa na Anthropic ilionyesha uwezo wa kufikiri unaozidi Claude 3 Opus kwa gharama na kasi ileile ya Claude 3 Sonnet ya awali, na kwa ujumla maoni mengi yalikuwa kwamba ina nguvu dhidi ya modeli shindani GPT-4 katika uandishi, mantiki ya lugha, uelewa wa lugha nyingi, na tafsiri.  
![Picha ya utambulisho wa Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Matokeo ya benchmark ya utendaji wa Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> Chanzo cha picha: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Kwa nini nilianza kutumia Claude 3.5 kwa ajili ya kutafsiri machapisho
Hata bila kutumia modeli za lugha kama Claude 3.5 au GPT-4, tayari kulikuwa na API za kibiashara za kutafsiri kama Google Translate na DeepL. Hata hivyo, sababu niliyoamua kutumia LLM kwa tafsiri ni kwamba, tofauti na huduma nyingine za kibiashara za kutafsiri, mtumiaji anaweza kumpa modeli taarifa za ziada za muktadha au mahitaji kupitia ubunifu wa prompt—kama lengo la maandishi au mada kuu—mbali na maandishi yenyewe, na modeli inaweza kutoa tafsiri inayozingatia muktadha huo. 

DeepL na Google Translate pia huonyesha ubora mzuri wa tafsiri kwa ujumla, lakini zina kikomo cha kutoweza kuelewa vizuri mada na muktadha wa jumla wa makala, na pia haziwezi kupokea mahitaji changamano kwa urahisi. Kwa hiyo, unapozitaka zitafsiri maandishi marefu ya mada za kitaalamu badala ya mazungumzo ya kila siku, wakati mwingine matokeo huwa yasiyo ya asili, na pia huwa vigumu kupata matokeo yanayolingana kikamilifu na muundo maalumu unaohitajika kama Markdown au YAML front matter.

Hususan kwa Claude, kama nilivyotaja hapo juu, kulikuwa na tathmini nyingi kwamba ilikuwa bora zaidi kuliko GPT-4 katika uandishi, mantiki ya lugha, uelewa wa lugha nyingi, na tafsiri. Nilipoijaribu mwenyewe kwa kiwango kidogo, pia niliona ubora wa tafsiri laini zaidi kuliko GPT-4, hivyo nilihitimisha kwamba mnamo Juni 12024, wakati nilipokuwa nikifikiria kuianzisha, ilikuwa inafaa kwa kazi ya kutafsiri makala za kihandisi kwenye blogu hii kwa lugha mbalimbali.

## Historia ya masasisho
### 12024.07.01.
Kama nilivyoeleza katika [makala tofauti](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), [nilimaliza kazi ya awali ya kutumia plagini ya Polyglot na kurekebisha `_config.yml`{: .filepath}, header ya HTML, na sitemap ipasavyo.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Kisha [nilichukua modeli ya Claude 3.5 Sonnet kwa madhumuni ya tafsiri, nikakamilisha utekelezaji wa awali na uthibitishaji wa skriti ya Python ya kuunganisha API inayozungumziwa katika mfululizo huu, na kisha nikaianza kuitumia.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
Mnamo 22 Oktoba 12024, Anthropic ilitangaza toleo lililoboreshwa la API ya Claude 3.5 Sonnet (`"claude-3-5-sonnet-20241022"`) pamoja na Claude 3.5 Haiku. Hata hivyo, kwa sababu ya [tatizo nitakaloeleza baadaye](#kuzuia-uvivu-120241031-kiraka-cha-halloween), blogu hii bado inatumia API ya zamani ya `"claude-3-5-sonnet-20240620"`.

### 12025.04.02.
[nilibadilisha modeli inayotumika kutoka `"claude-3-5-sonnet-20240620"` kwenda `"claude-3-7-sonnet-20250219"`.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[nilibadilisha modeli inayotumika kutoka `"claude-3-7-sonnet-20250219"` kwenda `"claude-sonnet-4-20250514"`.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Matokeo ya benchmark ya utendaji wa Claude 4](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> Chanzo cha picha: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

Ingawa inaweza kutofautiana kulingana na masharti ya matumizi, tangu kutokea kwa modeli ya Claude 3.7 Sonnet kwa ujumla kumekuwa na makubaliano makubwa kwamba Claude ndiyo modeli yenye nguvu zaidi kwa masuala ya kuandika msimbo. Anthropic pia inasisitiza kwa nguvu uwezo wa juu wa usimbaji wa modeli zake kama faida kuu dhidi ya modeli pinzani za OpenAI na Google. Hata katika tangazo la Claude Opus 4 na Claude Sonnet 4, waliendelea kusisitiza utendaji wa coding na kulenga wasanidi kama kundi lao kuu la wateja.

Bila shaka, ukiangalia matokeo ya benchmark waliyochapisha, maboresho yamefanyika si katika coding tu bali pia kwa ujumla katika vipengele vingine, na kwa kazi ya kutafsiri inayozungumziwa katika makala hii, maboresho ya utendaji katika maswali na majibu ya lugha nyingi (MMMLU) na utatuzi wa matatizo ya hisabati (AIME 2025) yanaonekana kuwa muhimu hasa. Nilipojaribu mwenyewe kwa kifupi, nilithibitisha kwamba matokeo ya tafsiri ya Claude Sonnet 4 yalikuwa bora kuliko yale ya Claude 3.7 Sonnet katika asilia ya usemi, utaalamu, na uthabiti wa matumizi ya istilahi.

> Kwa sasa, angalau kwa kazi ya kutafsiri makala za kiufundi zilizoandikwa kwa Kikorea kama zile zinazoshughulikiwa kwenye blogu hii kwenda lugha nyingine, bado naona modeli za Claude ndizo bora zaidi. Hata hivyo, hivi karibuni utendaji wa modeli za Google Gemini umeboreshwa kwa njia inayoonekana, na mwezi Mei mwaka huu hata modeli za Gemini 2.5 zilitangazwa, japo bado katika hatua ya Preview.  
> Nilipolinganisha Gemini 2.0 Flash na Claude 3.7 Sonnet pamoja na Claude Sonnet 4, niliona utendaji wa tafsiri wa Claude kuwa bora zaidi, lakini uwezo wa Gemini katika lugha nyingi pia ni mzuri sana. Zaidi ya hayo, hata ikiwa bado ni Preview, Gemini 2.5 Preview 05-06 ilikuwa bora zaidi kuliko Claude Opus 4 katika utatuzi na uelezaji wa matatizo ya hisabati na fizikia, hivyo siwezi kusema kwa uhakika kitakachotokea modeli hiyo ikitolewa rasmi na ikalinganishwa tena.  
> Kwa kuwa inaweza kutumika hadi kiwango fulani cha matumizi kwa [daraja la bure (Free Tier)](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits), na hata katika daraja la kulipia (Paid Tier) ada ya API ni nafuu zaidi kuliko Claude, Gemini ina ushindani mkubwa sana wa bei. Kwa hiyo, hata ikitoa utendaji unaokaribiana tu, Gemini inaweza kuwa mbadala wenye mantiki. Kwa kuwa Gemini 2.5 bado iko katika hatua ya Preview, nimeona ni mapema kuitumia katika otomatiki halisi, hivyo siifuatilii kwa sasa, lakini nikipata toleo rasmi ninapanga kuijaribu.
{: .prompt-tip }

### 12025.07.04.
- [Kuongeza kipengele cha tafsiri ya hatua kwa hatua (incremental translation)](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/978032f52c7d85ecb6b213233d5404d844402965)
- Kugawa modeli inayotumika kulingana na lugha lengwa ya tafsiri ([Commit 3890c82](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3890c820c1f3df34f8e4686b8903ca4ee770ba15), [Commit fe0fc63](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/fe0fc63ae4e2764f3dfe24ff259b4477f120b9ed))
  - Kutafsiri kwenda Kiingereza, Kichina cha Taiwan, na Kijerumani: tumia `"gemini-2.5-pro"`
  - Kutafsiri kwenda Kijapani, Kihispania, Kireno, na Kifaransa: endelea kutumia `"claude-sonnet-4-20250514"`
- Nilifikiria kuongeza thamani ya `temperature` kutoka `0.0` hadi `0.2`, lakini nikairejesha kama ilivyokuwa

Mnamo 4 Julai 12025, hatimaye modeli za Gemini 2.5 Pro na Gemini 2.5 Flash zilitoka rasmi baada ya kuacha hatua ya Preview. Ingawa idadi ya mifano niliyotumia ilikuwa ndogo, katika majaribio yangu binafsi niliona kwamba kwa tafsiri ya Kiingereza, hata Gemini 2.5 Flash ilishughulikia baadhi ya sehemu kwa asilia zaidi kuliko Claude Sonnet 4 ya awali. Ukizingatia kwamba bei ya tokeni za pato ya Gemini 2.5 Pro na Flash ni nafuu mara 1.5 na mara 6 mtawalia kuliko Claude Sonnet 4 hata katika daraja la kulipia, basi kwa Kiingereza inaweza kusemwa kuwa ndiyo modeli yenye ushindani mkubwa zaidi kufikia Julai 12025. Hata hivyo, kwa Gemini 2.5 Flash, labda kutokana na mipaka ya modeli ndogo, ingawa matokeo yake kwa ujumla ni mazuri sana, kulikuwa na matatizo kama kuvunjika kwa baadhi ya miundo ya hati ya Markdown au viungo vya ndani, hivyo haikufaa kwa kazi changamano za kutafsiri na kuchakata hati. Zaidi ya hayo, ingawa Gemini 2.5 Pro ina utendaji mzuri kwa Kiingereza, ilionekana kupata shida kwa **machapisho mengi ya Kireno (pt-BR)** na baadhi ya machapisho ya Kihispania, pengine kwa sababu ya uhaba wa data iliyofunzwa. Nilipoangalia makosa yaliyotokea, mengi yalitokana na kuchanganya herufi zinazofanana kama 'í' na 'i', 'ó' na 'o', 'ç' na 'c', na 'ã' na 'a'. Pia kwa Kifaransa hakukuwa na tatizo hilo maalumu, lakini wakati mwingine sentensi zake zilikuwa ndefu kupita kiasi na zisizo rahisi kusoma ukilinganisha na Claude Sonnet 4.

Mimi sijui vizuri lugha nyingine mbali na Kiingereza, hivyo ni vigumu kufanya ulinganisho wa kina na sahihi, lakini kwa muhtasari wa ubora wa majibu kwa kila lugha, niliona hivi:
- Kiingereza, Kijerumani, Kichina cha Taiwan: Gemini ni bora
- Kijapani, Kifaransa, Kihispania, Kireno: Claude ni bora

Pia niliongeza kipengele cha tafsiri ya hatua kwa hatua (Incremental Translation) kwenye skriti ya kutafsiri machapisho. Ninapokuwa naandika makala mpya hujaribu kuikagua kwa makini, lakini bado wakati mwingine baada ya kuichapisha ninagundua makosa madogo kama ya tahajia, au ninapata wazo la kitu cha kuongeza au kurekebisha. Katika hali kama hizo, hata kama sehemu iliyorekebishwa ni ndogo, skriti ya awali ililazimika kutafsiri na kutoa upya makala nzima kutoka mwanzo hadi mwisho, jambo ambalo halikuwa na ufanisi sana upande wa matumizi ya API. Kwa hiyo niliunganisha na git ili kulinganisha matoleo ya maandishi asilia ya Kikorea, nikatoa sehemu zilizobadilika za maandishi asilia katika muundo wa diff, nikaziingiza kwenye prompt pamoja na tafsiri kamili ya awali, halafu nikapokea diff patch ya tafsiri kama pato ili kurekebisha kwa kuchagua sehemu zinazohitajika tu. Kwa kuwa gharama ya tokeni za ingizo ni nafuu sana ukilinganisha na ile ya tokeni za pato, hili linaweza kuleta punguzo la maana la gharama. Hivyo, kuanzia sasa hata nikirekebisha sehemu ndogo tu ya makala, nitaweza kutumia skriti ya kutafsiri kiotomatiki bila mzigo wa kurekebisha tafsiri za kila lugha kwa mkono.

Kwa upande mwingine, `temperature` ni kigezo kinachodhibiti kiwango cha u nasibu wakati modeli ya lugha inapochagua neno linalofuata katika mchakato wa kutoa jibu. Ni thamani halisi isiyo hasi (\*kama nitakavyoeleza baadaye, kwa kawaida katika safu ya $[0,1]$ au $[0,2]$), na kadri inavyokaribia 0 ndivyo jibu linavyokuwa la kidhahiri zaidi na lenye uthabiti, huku thamani kubwa ikizalisha majibu yenye utofauti na ubunifu zaidi.  
Lengo la tafsiri si kubuni maudhui mapya kwa ubunifu, bali kuwasilisha maana na toni ya maandishi asilia kwa usahihi na uthabiti mkubwa iwezekanavyo katika lugha nyingine. Kwa hiyo, ili kupata usahihi, uthabiti, na utabirikaji wa tafsiri, ni bora kutumia thamani ndogo ya `temperature`. Hata hivyo, ukiweka `temperature` kuwa `0.0`, modeli itachagua kila wakati neno lenye uwezekano mkubwa zaidi, jambo ambalo wakati mwingine linaweza kufanya tafsiri iwe ya moja kwa moja kupita kiasi au kutoa sentensi zisizo za asili na ngumu. Kwa hiyo nilifikiria kuongeza kidogo `temperature` hadi `0.2` ili kuzuia majibu yasikaze sana na kuruhusu unyumbufu kiasi, lakini kwa sababu usahihi wa kushughulikia viungo changamano vyenye sehemu ya kitambulishi (Fragment identifier) uliporomoka sana, niliamua kutolitumia.

> \* Mara nyingi, thamani za `temperature` zinazotumiwa kivitendo huwa katika safu ya 0 hadi 1, na safu inayoruhusiwa katika Anthropic API pia ni $[0,1]$. Katika OpenAI API na Gemini API, `temperature` inaweza kuruhusiwa hadi safu pana ya $[0,2]$, lakini hata kama safu imepanuliwa hadi $[0,2]$, hiyo haimaanishi kwamba kiwango chenyewe kimeongezeka mara mbili; maana ya $T=1$ inabaki ileile kama kwa modeli zinazotumia safu ya $[0,1]$. 
>
> Ndani yake, modeli ya lugha inapozalisha pato hufanya kazi kama aina ya funksi inayopokea prompt pamoja na tokeni za pato zilizotolewa hadi wakati huo kama ingizo, na kutoa mgawanyo wa uwezekano wa tokeni inayofuata. Kisha matokeo ya uteuzi kulingana na mgawanyo huo huamua tokeni inayofuata inayotolewa. Thamani ya msingi inayotumia mgawanyo huo kama ulivyo ni $T=1$. Kwa $T<1$, mgawanyo wa uwezekano huwa mwembamba na mkali zaidi, hivyo modeli huelekea kuchagua kwa uthabiti zaidi miongoni mwa maneno yenye uwezekano mkubwa. Kinyume chake, kwa $T>1$, mgawanyo huo husawazishwa zaidi, na uwezekano wa kuchagua maneno ambayo kawaida yangekuwa na nafasi ndogo sana huongezwa kwa njia ya bandia.
>
> Katika eneo la $T>1$, ubora wa pato unaweza kushuka na kuwa usiotabirika, kwa mfano kwa kuingiza tokeni zisizoendana na muktadha au kutoa sentensi zisizo na mantiki na zisizo sahihi kisarufi. Kwa kazi nyingi, hasa katika mazingira ya matumizi halisi ya uzalishaji (production), ni bora kuweka `temperature` ndani ya safu ya $[0,1]$. Thamani kubwa kuliko 1 zinaweza kutumiwa kwa majaribio wakati unataka pato lenye utofauti mkubwa, kama katika brainstorming au kusaidia ubunifu (kwa mfano rasimu ya awali ya hadithi), lakini kwa kuwa hatari ya hallucination na makosa ya kisarufi au kimantiki huongezeka, ni vyema matumizi hayo yafanyike kwa kuhusisha mtu na ukaguzi wa binadamu badala ya kuyaacha yawe otomatiki kabisa.
>
> Kwa maelezo zaidi kuhusu `temperature` katika modeli za lugha, unaweza kurejelea makala zifuatazo.
> - [Tamanna, *Understanding LLM Temperature* (2025).](https://medium.com/@tam.tamanna18/understanding-llm-temperature-7d838277a7d9)
> - [Tickr Data, *The Impact of Temperature on LLM Performance* (2023).](https://www.tickr.com/blog/posts/impact-of-temperature-on-llms/)
> - [Anik Das, *Temperature in Prompt Engineering* (2025).](https://peerlist.io/anikdas/articles/temperature-in-prompt-engineering)
> - [Peeperkorn et al., *Is Temperature the Creativity Parameter of LLMs?*, arXiv:2405.00492 (2024).](https://arxiv.org/abs/2405.00492)
> - [Colt Steele, *Understanding OpenAI’s Temperature Parameter* (2023).](https://www.coltsteele.com/tips/understanding-openai-s-temperature-parameter)
> - [Damon Garn, *Understanding the role of temperature settings in AI output*, TechTarget (2025).](https://www.techtarget.com/searchenterpriseai/tip/Understanding-the-role-of-temperature-settings-in-AI-output)
{: .prompt-info }

## Ubunifu wa Prompt
### Kanuni za msingi za kuomba jambo
Ili kupata matokeo ya kuridhisha kutoka kwa modeli ya lugha ambayo yanaendana na kusudi lako, ni lazima utoe prompt inayofaa. Maneno “ubunifu wa prompt” yanaweza kuonekana ya kutatanisha, lakini kwa kweli “jinsi ya kuomba jambo vizuri” haitofautiani sana iwapo unamwomba binadamu au modeli ya lugha, hivyo ukiikaribia kwa mtazamo huo si vigumu sana. Ni vizuri kueleza kwa uwazi hali ya sasa na ombi lako kulingana na vipengele vya msingi vya kuuliza nani, nini, lini, wapi, kwa nini, na jinsi gani, na ikiwa inahitajika unaweza pia kuongeza mifano michache mahususi. Kuna vidokezo na mbinu nyingi kuhusu ubunifu wa prompt, lakini nyingi hutokana na kanuni hizi za msingi nitakazoeleza baadaye.

#### Toni ya jumla
Kuna ripoti nyingi kwamba modeli za lugha hutoa majibu ya ubora wa juu zaidi unapounda na kuingiza prompt kwa sauti ya heshima ya kuomba kuliko kwa toni ya kuamuru kwa ukali. Kwa kawaida pia katika jamii, unapomwomba mtu mwingine jambo kwa heshima badala ya kumwamuru kwa ukali, huwa kuna uwezekano mkubwa zaidi kwamba atalifanya kwa umakini. Inaonekana modeli za lugha pia zimejifunza na kuiga mifumo kama hiyo ya majibu ya binadamu.

#### Kutoa jukumu na kueleza hali (nani, kwa nini)
Kwanza kabisa, niliipa jukumu la *“mtafsiri mtaalamu wa nyanja za kiufundi (professional technical translator)”*, na nikatoa taarifa za muktadha kuhusu mtumiaji kama *“mbloga wa uhandisi anayechapisha hasa makala kuhusu hisabati, fizikia, na sayansi ya data”*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Kueleza ombi kwa upana (nini)
Kisha, niliomba itafsiri maandishi ya muundo wa markdown yaliyotolewa na mtumiaji kutoka {source_lang} kwenda {target_lang} huku ikihifadhi muundo huo. 

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Wakati wa kuita Claude API, nafasi za {source_lang} na {target_lang} kwenye prompt hujazwa na vigezo vya lugha chanzi na lugha lengwa kupitia kipengele cha f-string cha skriti ya Python.
{: .prompt-info }

#### Kufafanua mahitaji na kutoa mifano (vipi)
Kwa kazi rahisi, wakati mwingine hata hatua zilizotangulia pekee zinatosha kupata matokeo unayotaka, lakini kwa kazi changamano maelezo ya ziada yanaweza kuhitajika. 

Mahitaji yanapokuwa mengi na changamano, kuyawasilisha katika orodha kwa muhtasari wa moja kwa moja huwa rahisi kusoma na kuelewa kuliko kuyaeleza kwa sentensi ndefu moja baada ya nyingine. Pia, inapohitajika, kusaidia kwa mifano ni jambo la manufaa. Katika kesi hii niliongeza masharti yafuatayo.

##### Namna ya kushughulikia YAML front matter
Ili kupakia makala iliyoandikwa kwa markdown kwenye blogu ya Jekyll, sehemu ya kwanza ya posti huwa na YAML front matter inayorekodi taarifa kama `title`, `description`, `categories`, na `tags`. Kwa mfano, YAML front matter ya makala hii ni kama ifuatavyo.

```yaml
---
title: "Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인"
description: "마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic/Gemini API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

Lakini unapoitafsiri posti, lebo za kichwa (`title`) na maelezo (`description`) zinahitaji kutafsiriwa kwa lugha nyingi, ilhali kwa ajili ya kudumisha uthabiti wa URL ya posti ni rahisi zaidi katika usimamizi kuacha majina ya kategoria (`categories`) na lebo (`tags`) yakiwa kwa Kiingereza bila kuyatafsiri. Kwa hiyo nilitoa maagizo kama yafuatayo ili lebo nyingine zote zisiguswe isipokuwa `title` na `description`. Kwa kuwa modeli tayari itakuwa imefunzwa na kujua YAML front matter ni nini, kiwango hiki cha maelezo kwa kawaida kinatosha.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Kwa kuongeza kifungu “under any circumstances, regardless of the language you are translating to”, nilisisitiza kwamba lebo nyingine za YAML front matter hazipaswi kubadilishwa **bila ubaguzi wowote**.
{: .prompt-tip }

(Sasisho la 12025.04.02.)  
Zaidi ya hayo, kwa kuzingatia SEO, niliagiza maudhui ya lebo ya `description` yaandikwe kwa urefu unaofaa kama ifuatavyo.

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Jinsi ya kushughulikia maandishi ya lugha nyingine ndani ya maandishi asilia
Ninapoandika maandishi asilia kwa Kikorea, mara nyingi ninapoanzisha ufafanuzi wa dhana kwa mara ya kwanza au ninapotumia istilahi fulani za kitaalamu, huwa naweka pia usemi wa Kiingereza ndani ya mabano, kama vile *중성자 감쇠 (Neutron Attenuation)*. Wakati wa kutafsiri misemo kama hii, kulikuwa na tatizo la kutokuwepo kwa uthabiti: wakati mwingine mabano yalihifadhiwa, wakati mwingine usemi wa Kiingereza ndani ya mabano uliondolewa. Kwa hiyo nilitengeneza mwongozo wa kina kama huu:
- Kwa istilahi za kitaalamu,
  - Ukizitafsiri kwenda lugha isiyotumia alfabeti ya Kilatini kama Kijapani, muundo wa “tafsiri (usemi wa Kiingereza)” udumishwe.
  - Kwa lugha zinazotumia alfabeti ya Kilatini kama Kihispania, Kireno, au Kifaransa, miundo yote miwili ya “tafsiri” pekee au “tafsiri (usemi wa Kiingereza)” inaruhusiwa, na modeli inaweza kuchagua yenye kufaa zaidi.
- Kwa majina maalumu,
  - Tahajia ya asili lazima ihifadhiwe kwa namna fulani katika matokeo ya tafsiri.

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

##### Namna ya kushughulikia viungo vinavyoelekeza kwenye machapisho mengine
Baadhi ya machapisho yana viungo vinavyoelekeza kwenye machapisho mengine. Katika hatua ya majaribio, nilipokuwa sijatoa mwongozo maalumu kuhusu hili, mara nyingi modeli ilitafsiri hata sehemu ya njia ya URL kana kwamba nayo inapaswa kutafsiriwa, jambo lililosababisha viungo vya ndani kuvunjika. Tatizo hili lilitatuliwa kwa kuongeza kifungu hiki kwenye prompt.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(Sasisho la 12025.04.06.)  
Ukipa mwongozo huu, sehemu ya njia ya kiungo hushughulikiwa vizuri zaidi wakati wa kutafsiri, na hivyo matukio ya kuvunjika kwa viungo hupungua kwa kiasi kikubwa. Hata hivyo, kwa viungo vinavyojumuisha sehemu ya kitambulishi (Fragment identifier), bila kujua maudhui ya posti inayolengwa, modeli ya lugha bado hulazimika kukisia tu sehemu hiyo kwa jumla, hivyo tatizo hilo halingeweza kutatuliwa kabisa. Kwa hiyo, niliboresha skriti ya Python na prompt ili kutoa pamoja taarifa za muktadha kuhusu machapisho mengine yanayounganishwa kupitia kiungo ndani ya lebo ya XML ya `<reference_context>` katika prompt ya mtumiaji, na nikaagiza tafsiri ya viungo ifanyike kulingana na muktadha huo. Baada ya kutumia sasisho hilo, tuliweza kuzuia kwa kiwango kikubwa tatizo la viungo kuvunjika, na kwa mfululizo wa machapisho yanayohusiana kwa karibu, pia ikawa inawezekana kutarajia uthabiti bora wa tafsiri katika machapisho kadhaa.

Ninatoa mwongozo huu kwenye system prompt:
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

Na sehemu ya `<reference_context>` kwenye prompt ya mtumiaji huundwa kwa muundo na maudhui kama yafuatayo, na huongezwa baada ya maudhui ya msingi yanayotakiwa kutafsiriwa.
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

> Kwa maelezo ya namna nilivyotekeleza hili kwa undani, rejelea [Sehemu ya 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) ya mfululizo huu na [skriti ya Python](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) iliyopo kwenye hazina ya GitHub.
{: .prompt-tip }

##### Toa tu matokeo ya tafsiri katika jibu
Mwisho, niliongeza sentensi ifuatayo ili kuagiza kwamba wakati wa kujibu, isiambatishe maneno mengine yoyote bali itoe tu matokeo ya tafsiri.

```xml
<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or "```markdown" or something of that nature!!</important>
```

### Mbinu za ziada za kubuni prompt
Hata hivyo, tofauti na kuomba kazi kwa binadamu, kwa modeli za lugha pia kuna mbinu za ziada zinazotumika mahususi.  
Kuna nyenzo nyingi muhimu mtandaoni kuhusu hili, lakini nikitaka kufupisha vidokezo kadhaa muhimu vinavyoweza kutumika kwa upana, ni hivi vifuatavyo.  
Nilitegemea hasa [mwongozo rasmi wa Anthropic wa uhandisi wa prompt](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Kutumia lebo za XML kuunda muundo
Kwa kweli, tayari nilikuwa nimetumia mbinu hii katika sehemu za awali. Kwa prompt changamano zinazojumuisha miktadha mingi, maagizo, miundo, na mifano, kutumia kwa usahihi lebo za XML kama `<instructions>`, `<example>`, na `<format>` kunaweza kusaidia modeli ya lugha kutafsiri prompt kwa usahihi na kutoa matokeo ya ubora wa juu yanayolingana na nia yako. Ninapendekeza pia uangalie hazina ya GitHub ya [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md), ambamo lebo za XML muhimu kwa uandishi wa prompt zimepangwa vizuri.

#### Mbinu ya kufikiri kwa hatua (CoT, Chain-of-Thought)
Kwa kazi zinazohitaji kiwango kikubwa cha mantiki, kama kutatua matatizo ya hisabati au kuandika hati changamano, unaweza kuboresha sana utendaji kwa kuongoza modeli ya lugha kufikiri kwa hatua. Hata hivyo, katika hali hiyo muda wa kuchelewa kwa jibu unaweza kuongezeka, na mbinu hii si lazima iwe na manufaa kila wakati kwa kila kazi, hivyo ni lazima kuwa mwangalifu. 

#### Mbinu ya prompt chaining
Unapolazimika kufanya kazi changamano, prompt moja pekee inaweza isiwe ya kutosha. Katika hali hiyo, unaweza pia kufikiria kugawanya mtiririko mzima wa kazi katika hatua kadhaa tangu mwanzo, ukitoa prompt maalumu kwa kila hatua na kupitisha majibu yaliyopatikana katika hatua ya awali kama ingizo la hatua inayofuata. Mbinu hii huitwa prompt chaining.

#### Kujaza mapema mwanzo wa jibu
Unapoingiza prompt, unaweza kuonyesha mapema sehemu ya mwanzo ya jibu linalotarajiwa na kumfanya modeli iendelee kutoka hapo. Hii inaweza kusaidia kuruka utangulizi usiohitajika kama salamu, au kulazimisha itoe jibu katika muundo maalumu kama XML au JSON. [Kwa Anthropic API, unaweza kutumia mbinu hii kwa kuwasilisha si ujumbe wa `User` pekee bali pia ujumbe wa `Assistant` wakati wa kuita API.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Kuzuia uvivu (Kiraka cha Halloween cha 12024.10.31.)
Baada ya kuandika makala hii kwa mara ya kwanza, kulikuwa na mabadiliko machache ya kati ya kuboresha prompt na kufafanua zaidi maagizo, lakini kwa jumla, katika kipindi cha miezi 4 ya kutumia mfumo huu wa otomatiki hakukuwa na tatizo kubwa lolote.

Lakini kuanzia takribani saa 6 jioni mnamo 12024.10.31. kwa saa ya Korea, kulianza kutokea tatizo la ajabu ambapo nilipoiomba itafsiri posti mpya, ilitafsiri sehemu ya kwanza ya 'TL;DR' tu na kisha kusitisha tafsiri kwa hiari katikati.

Nimejadili sababu inayoweza kuwa chanzo cha tatizo hilo pamoja na suluhisho lake katika [makala tofauti](/posts/does-ai-hate-to-work-on-halloween), hivyo tafadhali rejelea makala hiyo.

### System prompt iliyokamilika
Matokeo ya ubunifu wa prompt kupitia hatua zilizoelezwa hapo juu yanaweza kuonekana katika [sehemu inayofuata](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Visomo vya Ziada
Inaendelea katika [Sehemu ya 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
