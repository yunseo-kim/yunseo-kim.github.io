---
title: "Muhtasari wa Sintaksia ya Markdown ya GitHub"
description: "Makala hii inaeleza Markdown ni nini na inafupisha sintaksia kuu za Markdown kulingana na GitHub Flavored Markdown kwa ajili ya kuandika na kuhosti blogu ya GitHub Pages."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Ili kutumia GitHub Pages, ni muhimu kujua sintaksia ya **markdown**.
Makala hii imeandaliwa kwa kurejelea nyaraka rasmi za GitHub: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) na [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Markdown ni nini
> **Markdown** ni lugha nyepesi ya markup inayotegemea maandishi ya kawaida. Hutumiwa kuandika hati zenye mpangilio kwa maandishi ya kawaida, na sifa yake kuu ni kuwa sintaksia yake ni rahisi na nyepesi ukilinganisha na lugha za kawaida za markup. Kwa kuwa inaweza kubadilishwa kwa urahisi kuwa hati zenye mpangilio kama HTML na Rich Text Format (RTF), hutumika sana katika faili za README zinazosambazwa pamoja na programu au katika machapisho ya mtandaoni.  
> John Gruber aliunda lugha ya Markdown mnamo mwaka 12004 wa [kalenda ya Holocene](https://en.wikipedia.org/wiki/Holocene_calendar), kupitia ushirikiano muhimu na Aaron Swartz katika upande wa sintaksia, na lengo lilikuwa kufanya iwezekane kwa watu kuandika kwa kutumia muundo wa maandishi ya kawaida ulio rahisi kusoma na kuandika, huku ukiruhusu ubadilishaji wa hiari kuwa XHTML (au HTML) iliyo halali kimuundo.

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Sintaksia ya Markdown
Kwa kuwa Markdown haina kiwango kimoja rasmi kilichowekwa, sintaksia ya kina inaweza kutofautiana kidogo kulingana na mahali inapotumika. Sintaksia ya Markdown iliyopangwa hapa inategemea [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Kuvunja mstari, kutenganisha paragrafu
Katika Markdown, kubonyeza Enter mara moja hakutambuliwi kama kuvunja mstari.
~~~
Sentensi ya kwanza.
Sentensi ya pili.
Sentensi ya tatu.
~~~
Sentensi ya kwanza.
Sentensi ya pili.
Sentensi ya tatu.

Kuvunja mstari hutumika ukiweka nafasi mbili au zaidi mfululizo.
~~~
Sentensi ya kwanza.  
Sentensi ya pili.  
Sentensi ya tatu.
~~~
Sentensi ya kwanza.  
Sentensi ya pili.  
Sentensi ya tatu.

Paragrafu hutenganishwa kwa mstari tupu kati yake (kubonyeza Enter mara mbili).
~~~
Paragrafu moja.

Paragrafu nyingine.
~~~
Paragrafu moja.

Paragrafu nyingine.

### 2.2. Vichwa (Headers)
Kuna viwango 6 kwa jumla.
```
# Hiki ni kichwa cha H1
## Hiki ni kichwa cha H2
### Hiki ni kichwa cha H3
#### Hiki ni kichwa cha H4
##### Hiki ni kichwa cha H5
###### Hiki ni kichwa cha H6
```
Kimsingi, lebo ya H1 inapaswa kuwepo mara moja tu katika ukurasa mmoja, hivyo kwa kawaida haitumiki sana moja kwa moja wakati wa kuandika chapisho au hati.

### 2.3. Msisitizo
```
*Maandishi haya yameandikwa kwa italiki*
_Haya pia yameandikwa kwa italiki_

**Haya ni maandishi ya herufi nzito**
__Haya pia ni maandishi ya herufi nzito__

~~Haya yalikuwa maandishi yenye makosa~~

_Unaweza **kuyachanganya**_

***Maandishi haya yote ni muhimu***
```
*Maandishi haya yameandikwa kwa italiki*  
_Haya pia yameandikwa kwa italiki_

**Haya ni maandishi ya herufi nzito**  
__Haya pia ni maandishi ya herufi nzito__

~~Haya yalikuwa maandishi yenye makosa~~

_Unaweza **kuyachanganya**_

***Maandishi haya yote ni muhimu***

### 2.4. Nukuu ya maandishi
Tumia \>.
```
> Hii ni blockquote ya kwanza.
>> Hii ni blockquote ya pili.
>>> Hii ni blockquote ya tatu.
```
> Hii ni blockquote ya kwanza.
>> Hii ni blockquote ya pili.
>>> Hii ni blockquote ya tatu.

### 2.5. Nukuu ya msimbo
Tumia \``` au \~~~.
~~~
```
git status
git add
git commit
```
~~~
```
git status
git add
git commit
```

Unaweza pia kuwezesha uakifishaji wa sintaksia kwa kubainisha lugha ya programu.
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### 2.6. Viungo
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

Unaweza pia kutumia viungo vya njia jamaa vinavyoelekeza kwenye faili nyingine ndani ya repository. Matumizi yake ni sawa na yale ya terminal.
```
[README](../README.md)
```

### 2.7. Orodha isiyo na mpangilio
Tumia \- au \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Orodha yenye mpangilio
Tumia nambari.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Orodha zilizopachikwa
```
1. Kipengee cha kwanza cha orodha
   - Kipengee cha kwanza kilichopachikwa
     - Kipengee cha pili kilichopachikwa
```
1. Kipengee cha kwanza cha orodha
   - Kipengee cha kwanza kilichopachikwa
     - Kipengee cha pili kilichopachikwa

### 2.10. Orodha ya kazi
Ili kuunda orodha ya kazi, ongeza \[ ] mbele ya kila kipengee.
Ili kuonyesha kazi iliyokamilika, tumia \[x].
```
- [x] Maliza mabadiliko yangu
- [ ] Tuma commit zangu GitHub
- [ ] Fungua pull request
```
- [x] Maliza mabadiliko yangu
- [ ] Tuma commit zangu GitHub
- [ ] Fungua pull request

### 2.11. Kuambatisha picha
```
Njia: ![(si lazima, inapendekezwa)maelezo ya picha](url){(si lazima)chaguo la ziada}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Kuunda jedwali
Unaweza kuunda jedwali kwa kutumia | na -.
Ni lazima uache mstari mmoja tupu kabla ya jedwali ili lionyeshwe ipasavyo.
Lazima utumie angalau alama 3 za - ili litambuliwe kwa usahihi.
```
 
| Kushoto | Katikati | Kulia |
| :---    |  :---:   |   ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Kushoto | Katikati | Kulia |
| :---    |  :---:   |   ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
