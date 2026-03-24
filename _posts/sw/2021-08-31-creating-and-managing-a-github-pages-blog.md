---
title: "Kutengeneza na Kusimamia Blogu ya GitHub Pages"
description: "Jifunze sifa na tofauti za kurasa za wavuti tuli na za nguvu, elewa Static Site Generator, na uhost blogu ya Jekyll kwenye GitHub Pages."
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Tangu mwanzoni mwa mwaka 12021 nimekuwa nikihost blogu kwenye GitHub Pages kwa kutumia Jekyll. Hata hivyo, kwa kuwa sikuwa nimeandika vizuri mchakato wa usakinishaji wakati nilipokuwa nikiijenga blogu hiyo, baadaye nilipokuja kuifanyia matengenezo kulikuwa na ugumu fulani, kwa hiyo nimeamua kupanga kwa muhtasari mchakato wa usakinishaji na namna ya kuitunza.  

(+ yaliyomo yamesasishwa mnamo 12024.12)

## 1. Kijenzi cha tovuti tuli & web hosting

### 1-1. Ukurasa wa wavuti tuli vs ukurasa wa wavuti unaobadilika

#### Ukurasa wa wavuti tuli (Static Web Page)

- Ukurasa wa wavuti unaowasilisha kwa mtumiaji data iliyohifadhiwa kwenye seva kama ilivyo
- Seva ya wavuti huwasilisha ukurasa uliokuwa umehifadhiwa mapema unaolingana na ombi la mtumiaji
- Mtumiaji ataona ukurasa uleule wa wavuti isipokuwa data iliyohifadhiwa kwenye seva ibadilishwe
- Kwa kuwa inatosha kutuma faili zinazolingana na ombi, kazi za ziada hazihitajiki, hivyo kwa kawaida majibu huwa ya haraka
- Kwa kuwa imeundwa na faili rahisi tu, inatosha kusanidi seva ya wavuti pekee, hivyo gharama ya ujenzi huwa ndogo
- Kwa kuwa huonyesha tu taarifa zilizohifadhiwa, huduma zake huwa na mipaka
- Kuongeza, kurekebisha na kufuta data lazima kufanywe na msimamizi kwa mikono
- Muundo wake ni rahisi kwa injini za utafutaji kuutambaa, hivyo kwa kiasi ni bora zaidi kwa uboreshaji wa injini za utafutaji (SEO)

#### Ukurasa wa wavuti unaobadilika (Dynamic Web Page)

- Ukurasa wa wavuti unaowasilisha data iliyohifadhiwa kwenye seva baada ya kuichakata kwa script
- Seva ya wavuti hutafsiri ombi la mtumiaji, huchakata data, kisha huwasilisha ukurasa wa wavuti ulioundwa
- Mtumiaji huona ukurasa wa wavuti unaobadilika kulingana na hali, muda, ombi, n.k.
- Kwa kuwa ni lazima script ichakatwe ili kuwasilisha ukurasa wa wavuti, majibu huwa polepole zaidi kwa kulinganisha
- Mbali na seva ya wavuti, seva ya programu pia inahitajika, hivyo gharama ya ziada hutokea wakati wa kuijenga
- Kwa kuwa taarifa mbalimbali zinaweza kuunganishwa na kutolewa kwa namna ya kubadilika, huduma nyingi tofauti zinawezekana
- Kulingana na muundo wa ukurasa wa wavuti, mtumiaji anaweza kuongeza, kurekebisha na kufuta data kupitia kivinjari

### 1-2. Kijenzi cha tovuti tuli (SSG, Static Site Generator)

- Chombo kinachounda kurasa za wavuti tuli kwa kutegemea data raw (kwa kawaida faili za maandishi za markdown) na templeti zilizofafanuliwa mapema
- Badala ya kuandika kila ukurasa wa HTML moja kwa moja, unaandika post kwa markdown na mchakato wa ku-build ukurasa wa wavuti na kuusambaza mtandaoni hujiendesha kiotomatiki
- Mfano) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages

- Huduma ya bure ya kuhifadhi kurasa za wavuti tuli inayotolewa na GitHub
- Kwa kila akaunti unaweza kuhost ukurasa 1 wa binafsi unaowakilisha akaunti yako, na pia kuunda na kuhost bila kikomo kurasa za nyaraka za miradi kwa kila repozitori.
- Baada ya kuunda repozitori kwa jina la aina ya '{username}.github.io' linalolingana na GitHub username yako, unaweza kusukuma moja kwa moja kurasa za HTML ulizobuild kwenye repozitori hiyo, au kutumia GitHub Actions kufanya build na deploy.
- Ikiwa unamiliki domain yako mwenyewe, unaweza kuiunganisha kwenye mipangilio na kutumia anuani nyingine ya domain badala ya domain chaguomsingi ya aina ya '{username}.github.io'.

## 2. Kuchagua SSG na tema ya kutumia

### 2-1. Sababu ya kuchagua Jekyll

Kuna SSG nyingi kama Jekyll, Hugo, Gatsby, n.k., lakini niliamua kutumia Jekyll. Vigezo nilivyotumia kuchagua SSG na sababu zilizonifanya nichague Jekyll ni kama zifuatazo.
- Je, naweza kupunguza majaribio yasiyo ya lazima na kujikita katika kuandika makala na kuendesha blogu?
  - Jekyll ni kijenzi cha tovuti tuli kinachoungwa mkono rasmi na Github Pages. Bila shaka SSG nyingine kama Hugo na Gatsby pia zinaweza kuhostiwa kwenye Github Pages, na pia kuna chaguo la kutumia huduma nyingine kabisa za hosting kama Netlify, lakini kwa kweli katika kuendesha blogu ya binafsi ya ukubwa huu, mambo kama SSG gani ilitumika kuijenga, kasi ya build, au utendaji kwa ujumla si muhimu sana kiteknolojia. Hivyo niliona ni bora kuchagua kile ambacho ni rahisi zaidi kukitunza na chenye nyaraka nyingi za kutegemea.
  - Jekyll pia imekuwa ikitengenezwa kwa muda mrefu zaidi kuliko washindani wengine kama Hugo na Gatsby. Kwa hiyo nyaraka zake zimekamilika zaidi, na kwa vitendo kiasi cha marejeleo unachoweza kukitumia tatizo likitokea ni kikubwa sana.
- Je, kuna aina mbalimbali za tema na plagin zinazoweza kutumika?
  - Hata ukitumia SSG badala ya kuandika HTML moja kwa moja, kuunda mwenyewe templeti zote mbalimbali bado ni kazi ya kusumbua, inayochukua muda mwingi, na kwa kweli hakuna ulazima wa kufanya hivyo. Kuna tema nyingi nzuri zilizokwisha kuchapishwa mtandaoni, kwa hiyo unaweza tu kuchagua unayoipenda na kuitumia.
  - Zaidi ya hayo, kwa kuwa mimi hutumia hasa C au Python, sikuwa na ujuzi mkubwa wa Ruby ya Jekyll au lugha ya Go ya Hugo, kwa hiyo nilinuia zaidi kutumia kikamilifu tema na plagin zilizokwisha tengenezwa.
  - Kwa Jekyll niliweza kupata tema iliyonivutia mara moja, ilhali kwa Hugo au Gatsby ilionekana kwamba idadi ya tema zinazofaa kwa blogu ya binafsi haikuwa kubwa sana. Pengine, kama nilivyotaja hapo juu, uunganisho wake mzuri na Github Pages ambayo hutumiwa sana na waendelezaji kwa hosting ya blogu binafsi, pamoja na muda mrefu wa maendeleo, viliathiri sana jambo hili pia.

### 2-2. Kuchagua tema

#### Minimal Mistakes (12021.01 - 12022.04)

- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- Tema niliyotumia kwa takribani mwaka 1 na miezi 3 baada ya kuanzisha blogu kwa mara ya kwanza
- Inaauni kazi ya maoni kupitia Disqus, Discourse, utterances, n.k.
- Inaauni mpangilio wa kategoria na tagi
- Inaauni Google Analytics kwa msingi
- Inawezesha kuchagua skin zilizofafanuliwa mapema
- Baadaye nilikuja kugundua tema ya Chirpy ambayo muundo wake ulikuwa mzuri zaidi na kuhamia huko, lakini ukizingatia kwamba hii ni blogu yenye ladha ya kiumhandisi, ingawa haikuwa ya kuvutia sana, ilikuwa na muundo safi kiasi cha kutosha na haikuwa mbaya kuitumia.

#### Chirpy Jekyll Theme (12022.04 - sasa)

- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- Tema ambayo nimekuwa nikitumia tangu nihamishe tema ya blogu mnamo Aprili 12022 hadi sasa
- Inaauni mpangilio wa kategoria nyingi na kazi ya tagi
- Inaauni kwa msingi uonyeshaji wa fomula kwa sintaksia ya LaTex kwa kutumia MathJax
- Inaauni kwa msingi michoro ya diagramu kwa kutumia Mermaid
- Inaauni kazi ya maoni kupitia Disqus, Giscus, n.k.
- Inaauni Google Analytics na GoatCounter
- Inaauni tema nyepesi na tema nyeusi
- Wakati wa kuhamia tema hii, MathJax na Mermaid hazikuwa zinaungwa mkono moja kwa moja kwenye tema ya Minimal Mistakes, hivyo ilibidi niziongeze mwenyewe kwa customization, lakini kwenye tema ya Chirpy zinaungwa mkono kwa msingi. Bila shaka, customization yenyewe haikuwa jambo kubwa sana, lakini bado hilo linaweza kuhesabiwa kama faida ndogo.
- Zaidi ya yote, muundo wake ni mzuri. Tema ya Minimal Mistakes ni safi, lakini ina ukakamavu fulani unaoifanya ionekane inafaa zaidi kwa nyaraka rasmi za kiufundi za mradi au ukurasa wa portfolio kuliko blogu; kwa upande mwingine, tema ya Chirpy ina faida ya muundo ambao haupungui sana hata ukilinganisha na majukwaa ya blogu ya kibiashara kama Tistory, Medium, au velog.

## 3. Kuunda repozitori ya GitHub, kufanya build na deploy

Maelezo hapa yanaandikwa kwa msingi wa Chirpy Jekyll Theme ninayotumia kwa sasa (12024.06), na yanachukulia kwamba Git tayari imesakinishwa.  
Tazama [mwongozo rasmi wa usakinishaji wa Jekyll](https://jekyllrb.com/docs/installation/) na [ukurasa rasmi wa Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Kusakinisha Ruby & Jekyll

Fuata [mwongozo rasmi wa usakinishaji wa Jekyll](https://jekyllrb.com/docs/installation/) kusakinisha Ruby na Jekyll kulingana na mazingira ya mfumo wako wa uendeshaji.

### 3-2. Kuunda repozitori ya GitHub

[Ukurasa rasmi wa Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) unaanzisha njia mbili zifuatazo.
1. Njia ya kupakia faili kuu kwa gem ya "jekyll-theme-chirpy" na kuchukua rasilimali zilizobaki kutoka kwenye templeti ya [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Faida: kama nitakavyoeleza baadaye, ni rahisi kutumia upgrades za matoleo.
  - Hasara: inaweza kuwa ya usumbufu zaidi unapofanya customization kubwa.
2. Njia ya kufork repozitori ya [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) kama repozitori ya blogu yako mwenyewe
  - Faida: kwa kuwa faili zote zinasimamiwa moja kwa moja ndani ya repozitori, ni rahisi kufanya customization kama kurekebisha moja kwa moja code na kuongeza vipengele ambavyo tema haiungi mkono.
  - Hasara: ili kutumia upgrade ya toleo, ni lazima umerge [upstream tag ya hivi karibuni ya repozitori asili](https://github.com/cotes2020/jekyll-theme-chirpy/tags), na kutegemea hali, code uliyoibadilisha mwenyewe inaweza kugongana na code ya toleo jipya. Katika hali hiyo, utalazimika kutatua mgongano huo mwenyewe.

Nilichagua njia ya 1. Kwa tema ya Chirpy, kwa msingi wake kiwango cha ukamilifu ni cha juu na kwa watumiaji wengi hakuna mambo mengi ya kufanya customization, na zaidi ya hayo hadi mwaka 12024 maendeleo na uboreshaji wa vipengele bado vinaendelea kwa nguvu, hivyo isipokuwa kama unapanga kuifanyia mageuzi makubwa sana, faida ya kwenda sambamba kwa wakati na upstream asili ni kubwa kuliko faida ya kutumia customization ya moja kwa moja. Mwongozo rasmi wa tema ya Chirpy pia unapendekeza njia ya 1 kwa watumiaji wengi.

### 3-3. Mipangilio muhimu

Tumia mipangilio inayohitajika kwenye faili `_config.yml`{: .filepath} ya saraka kuu, pamoja na faili `_data/contact.yml`{: .filepath} na `_data/share.yml`{: .filepath}. Maoni ya ndani yameandikwa vizuri na mipangilio ni ya moja kwa moja, hivyo unaweza kuitumia bila ugumu mkubwa. Kwa kiasi fulani, mipangilio inayohitaji kazi ya ziada nje ya hapo ni kama kusajili msimbo wa uthibitishaji kwa ajili ya kuunganisha Google Search Console na kuunganisha zana za webmaster kama Google Analytics au GoatCounter, lakini hata hayo si taratibu ngumu sana na pia si mada kuu ninayotaka kushughulikia katika makala hii, kwa hiyo sitaeleza kwa kina.

### 3-4. Kufanya build ndani ya mazingira ya local

Si hatua ya lazima, lakini unapokuwa umeandika post mpya au umefanya marekebisho fulani kwenye tovuti, unaweza kutaka kuhakiki mapema kama itaonyeshwa sawasawa mtandaoni. Katika hali hiyo, fungua terminal kwenye saraka kuu ya repozitori ya local na utekeleze amri ifuatayo.

```console
$ bundle exec jekyll s
```

Ukisubiri kidogo, tovuti itajengwa katika local na utaweza kuona matokeo kwenye anuani ya <http://127.0.0.1:4000>.

### 3-5. Kufanya deploy

Kuna njia mbili.
1. Kutumia GitHub Actions (ikiwa unahost kwenye GitHub Pages)
  - Ikiwa unatumia GitHub Free Plan, ni lazima uiweke repozitori kuwa public
  - Kwenye ukurasa wa GitHub wa repozitori, chagua kichupo cha *Settings*, kisha kwenye navigation bar ya kushoto bofya *Code and automation > Pages* na uchague chaguo la **GitHub Actions** katika sehemu ya **Source**
  - Baada ya kukamilisha mipangilio, kila unapofanya Push ya commit mpya, workflow ya *Build and Deploy* itaendeshwa kiotomatiki
2. Kufanya build mwenyewe na kisha deploy (ikiwa unatumia huduma nyingine ya hosting au self-hosting)
  - Tekeleza amri ifuatayo ili ku-build tovuti mwenyewe
    ```console
    $ JEKYLL_ENV=production bundle exec jekyll b
    ```
  - Upload matokeo ya build yaliyopo kwenye saraka ya `_site` kwenda kwenye seva

## 4. Kuandika post

Njia ya kuandika post na chaguo unazoweza kutumia zimeandikwa vizuri kwenye [mwongozo wa kuandika post](https://chirpy.cotes.page/posts/write-a-new-post/) wa tema ya Chirpy. Mbali na yale yanayoelezwa katika makala hii, kuna vipengele mbalimbali vingine pia, hivyo ni maudhui mazuri ya marejeo ikiwa utayahitaji. Aidha, sintaksia za msingi za GitHub Flavored Markdown tayari nimezihitimisha katika [makala tofauti](/posts/github-markdown-syntax-summary/). Hapa nitaweka kwa muhtasari mambo muhimu ya kuzingatia kila mara unapoposti.

### Kuunda faili ya markdown

- Muundo wa jina: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Mahali: saraka ya `_posts`{: .filepath}

### Kuandika Front Matter

Mwanzoni mwa faili ya markdown, ni lazima uandike Front Matter ipasavyo.

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

- **title**: kichwa cha post
- **description**: muhtasari. Usipouandika, sehemu ya mwanzo ya maudhui ya mwili itachukuliwa kiotomatiki, lakini kwa uboreshaji wa injini za utafutaji (SEO) inashauriwa kuandika mwenyewe kwa usahihi meta tag ya description. Kwa alfabeti za Kirumi, urefu unaofaa ni takribani herufi 135 hadi 160; kwa Kikorea, takribani herufi 80 hadi 110.
- **date**: tarehe na saa kamili ya kuandika post pamoja na timezone (inaweza kuachwa; ikiachwa, tarehe ya kuunda faili au taarifa ya tarehe ya kurekebishwa itatambuliwa na kutumiwa kiotomatiki)
- **categories**: uainishaji wa kategoria za post
- **tags**: uainishaji wa tagi za post
- **image**: kuingiza picha ya preview juu ya post
  - **path**: njia ya faili ya picha
  - **alt**: maandishi mbadala (si lazima)
- **toc**: iwapo utumie kazi ya jedwali la yaliyomo kwenye sidebar ya kulia, thamani chaguomsingi ni `true`
- **comments**: hutumika pale unapotaka kubainisha wazi iwapo maoni yatumiwe kwa post ya binafsi bila kujali mipangilio ya msingi ya tovuti
- **math**: huwasha kazi ya ndani ya kuonyesha fomula inayotegemea [MathJax](https://www.mathjax.org/), thamani chaguomsingi ni kuzimwa (`false`) kwa ajili ya utendaji wa ukurasa
- **mermaid**: huwasha kazi ya ndani ya kuonyesha diagramu inayotegemea [Mermaid](https://github.com/mermaid-js/mermaid), thamani chaguomsingi ni kuzimwa (`false`)

## 5. Kuboresha toleo

Maelezo hapa yanaandikwa kwa kudhani kwamba katika [3-2](#3-2-kuunda-repozitori-ya-github) umechagua njia ya 1. Ikiwa umechagua njia ya 2, basi kama ilivyoelezwa hapo juu, ni lazima umerge upstream tag ya hivi karibuni moja kwa moja.

1. Hariri `Gemfile`{: .filepath} na ubainishe upya toleo la gem ya "jekyll-theme-chirpy".
2. Kwa major upgrade, faili kuu na chaguo za mipangilio ambazo hazijajumuishwa ndani ya gem ya "jekyll-theme-chirpy" pia zinaweza kuwa zimebadilika. Katika hali hiyo, utalazimika kukagua mabadiliko kupitia GitHub API iliyo hapa chini na kuyatumia mwenyewe.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
