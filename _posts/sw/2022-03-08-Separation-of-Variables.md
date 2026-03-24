---
title: "Mbinu ya Kutenganisha Vigeu (Separation of Variables)"
description: "Jifunze mbinu ya kutenganisha vigeu na uone mifano kadhaa ya matumizi yake."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Mbinu ya Kutenganisha Vigeu (Separation of Variables)

**Mlinganyo unaotenganishika (separable equation)**: mlinganyo unaoweza kuandikwa katika umbo la $g(y)y'=f(x)$ kupitia uendeshaji wa kialjebra.

Tukichukua integarali ya pande zote mbili za mlinganyo unaotenganishika $g(y)y'=f(x)$ kwa heshima ya $x$, tunapata

$$ \int g(y)y'dx = \int f(x)dx + c $$ 

na kwa kuwa $y'dx=dy$, basi

$$ \int g(y)dy = \int f(x)dx + c $$

hivyo tunaweza kutenganisha usemi unaohusiana na $x$ na usemi unaohusiana na $y$ katika upande wa kulia na wa kushoto mtawalia. Ikiwa $f$ na $g$ ni funzioni endelevu, tunaweza kukokotoa integarali zilizo juu na kupata suluhisho la jumla la mlinganyo tofauti uliotolewa. Mbinu hii ya utatuzi huitwa **mbinu ya kutenganisha vigeu (separation of variables)**.

## Mfano wa uundaji wa modeli: Upimaji wa Umri kwa Kaboni ya Mionzi (Radiocarbon Dating)

Oetzi ni mumia ya Enzi ya Neolithic iliyogunduliwa mwaka 11991 wa [Kalenda ya Holocene](https://en.wikipedia.org/wiki/Holocene_calendar) katika milima ya Alps ya Oetztal. Ikiwa uwiano wa kaboni-14 kwa kaboni-12 katika mumia hii ni 52.5% ya ule wa viumbe hai, basi Oetzi alikufa takribani lini?
> Katika angahewa na viumbe hai, uwiano wa kaboni-14 ya mionzi kwa kaboni-12 ni thabiti. Kiumbe kinapokufa, ufyonzwaji wa kaboni-14 kwa kupumua na kula hukoma, lakini kuoza kwa kaboni-14 huendelea, hivyo uwiano wa kaboni ya mionzi hupungua. Kwa hiyo, umri wa kisukuku unaweza kukadiriwa kwa kulinganisha uwiano wa kaboni ya mionzi katika kisukuku na ule wa angahewa. Nusu-uhai wa kaboni-14 ni miaka 5715.
{: .prompt-info }

### Suluhisho

Tukitenganisha vigeu na kuchukua integarali ya mlinganyo tofauti wa kawaida $y'=ky$, tunapata

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Ili kubaini konstanti $k$, tunatumia nusu-uhai $H=5715$.

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Hatimaye, ili kupata wakati $t$ ambao Oetzi alikufa, tunaweka uwiano wa 52.5%.

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{inakisiwa alikufa takribani miaka 5310 iliyopita, karibu mwaka 6680 wa Kalenda ya Holocene}. $$

## Mfano wa uundaji wa modeli: Tatizo la mchanganyiko

Mwanzoni, tanki lina 1000L za maji zenye 10kg ya chumvi iliyoyeyushwa. Maji ya chumvi yanaingia kwa kasi ya 10L kwa dakika, na maji hayo yana 0.2kg ya chumvi kwa kila lita. Mchanganyiko ndani ya tanki unakorogwa vizuri na hubaki wa sare, na maji ya chumvi hayo hutoka kwa kasi ya 10L kwa dakika. Tafuta kiasi cha chumvi $y(t)$ ndani ya tanki kwa wakati $t$.

### 1. Kuweka modeli

$$ y'=\text{kiwango cha kuingia} - \text{kiwango cha kutoka}. $$

Kiwango cha chumvi kinachoingia ni 2kg kwa dakika. Kwa kuwa kiwango cha maji ya chumvi kinachotoka kwa dakika ni 0.01 ya ujazo wote wa mchanganyiko, kiwango cha chumvi kinachotoka kwa dakika ni $0.01 y(t)$. Kwa hiyo modeli ni mlinganyo tofauti wa kawaida

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Kutatua modeli

Mlinganyo tofauti wa kawaida tulioweka hapo juu unaweza kutenganishwa. Tukitenganisha vigeu, kuchukua integarali, na kisha kuchukua eksponenti ya pande zote mbili, tunapata

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Kwa kuwa mwanzoni kiasi cha chumvi ndani ya tanki ni 10kg, sharti la awali ni $y(0)=10$. Tukibadilisha $y=10,\ t=0$ katika usemi wa juu, tunapata $10-200=ce^0=c$, hivyo $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Yaani, katika hali hii kiasi cha chumvi ndani ya tanki hukaribia 200kg kwa namna ya eksponenti na kutulia kwenye thamani hiyo.

## Mfano wa uundaji wa modeli: Sheria ya Newton ya Kupoa (Newton's Law of Cooling)

Wakati wa mchana katika jengo fulani la ofisi wakati wa baridi, joto hudumishwa kwenye 20℃. Mfumo wa kupasha joto huzimwa saa 22:00 na kuwashwa tena saa 06:00. Siku moja, saa 02:00 asubuhi joto la ndani la jengo lilikuwa 17.4℃. Joto la nje lilikuwa 10℃ saa 22:00 na likashuka hadi 4℃ saa 06:00. Joto la ndani la jengo lilikuwa nyuzi ngapi wakati hita ilipowashwa saa 06:00?

> **Sheria ya Newton ya kupoa (Newton's law of cooling)**  
> Kiwango cha mabadiliko ya joto $T$ cha kitu kwa wakati ni sawia na tofauti ya joto kati ya kitu na mazingira yake
{: .prompt-info }

### 1. Kuweka modeli

$T(t)$ liwe joto la ndani la jengo, na $T_A$ liwe joto la nje. Basi, kwa mujibu wa sheria ya Newton ya kupoa,

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Suluhisho la jumla

Kwa kuwa tunajua tu kwamba $T_A$ hubadilika kati ya 10℃ na 4℃, lakini hatujui hasa inachukua thamani gani, hatuwezi kusuluhisha mlinganyo tulioweka hapo juu. Katika hali kama hii, *inaweza kusaidia kurahisisha hali kuwa tatizo rahisi zaidi na kujaribu kupata suluhisho*. Kwa kuwa wastani wa thamani mbili tunazozijua ni 7℃, tuchukulie kwamba kazi isiyojulikana $T_A$ ni kazi thabiti $T_A=7$. Hata kama si sahihi kabisa, tunaweza kutarajia kupata thamani ya kukaribia ya joto la ndani la jengo $T$ saa 06:00 tunalotaka.

Kwa konstanti $T_A=7$, mlinganyo tofauti wa kawaida tulioweka hapo juu unaweza kutenganishwa. Tukitenganisha vigeu, kuchukua integarali, na kisha kuchukua eksponenti ya pande zote mbili, tunaweza kupata suluhisho la jumla.

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Suluhisho maalum

Tukichagua saa 22:00 kuwa $t=0$, sharti la awali lililotolewa ni $T(0)=20$. Tuiite suluhisho maalum tunalopata hapa $T_p$. Tukibadilisha, tunapata

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Kubaini $k$

Kwa kuwa saa 02:00 asubuhi joto la ndani la jengo lilikuwa 17.4℃, basi $T(4)=17.4$. Tukipata thamani ya $k$ kialjebra na kuiweka kwenye $T_p(t)$, tunapata

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Jibu na tafsiri

Kwa kuwa saa 06:00 ni $t=8$,

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[℃]}. $$

## Mfano wa uundaji wa modeli: Nadharia ya Torricelli (Torricelli's Theorem)

Tanki lina kipenyo cha 2m, tundu lina kipenyo cha 1cm, na urefu wa awali wa maji wakati tundu linafunguliwa ni 2.25m. Tafuta urefu wa maji ndani ya tanki kwa wakati wowote, pamoja na muda unaochukua hadi tanki kuwa tupu.

> **Nadharia ya Torricelli (Torricelli's theorem)**  
> Chini ya athari ya graviti, kasi ya maji yanayotoka ni
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: urefu wa maji juu ya tundu wakati $t$  
> $g=980\text{cm/s²}$: uongezaji kasi wa graviti kwenye uso wa dunia
{: .prompt-info }

### 1. Kuweka modeli

Katika muda mfupi $\Delta t$, kiasi cha maji kinachotoka $\Delta V$ ni

$$ \Delta V = Av\Delta t \qquad (A: \text{eneo la tundu})$$

Hiki lazima kiwe sawa na mabadiliko ya ujazo wa maji ndani ya tanki, yaani $\Delta V^*$. Pia,

$$ \Delta V^* = -B\Delta h \qquad (B: \text{eneo la sehemu-tambuka ya tanki}) $$

ambapo $\Delta h(>0)$ ni kiasi cha kupungua kwa urefu wa maji $h(t)$. Tukichukulia $\Delta V$ na $\Delta V^*$ kuwa sawa, tunapata

$$ -B\Delta h = Av\Delta t $$

Sasa, kwa mujibu wa nadharia ya Torricelli, tukiandika $v$ na kuruhusu $\Delta t$ ikaribie 0 bila kikomo, tunapata modeli ifuatayo iliyo katika umbo la mlinganyo tofauti wa kawaida wa daraja la kwanza.

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Suluhisho la jumla

Mlinganyo huu tofauti wa kawaida unaweza kutenganishwa. Tukitenganisha vigeu na kuchukua integarali, tunapata

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Tukigawanya pande zote mbili kwa 2 na kisha kuziinua mraba, tunapata $h=(c-13.28At/B)^2$. Tukibadilisha $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$, tunapata suluhisho la jumla

$$ h(t)=(c-0.000332t)^2 $$

### 3. Suluhisho maalum

Sharti la awali ni $h(0)=225\text{cm}$. Tukibadilisha $t=0$ na $h=225$, tunapata kutoka kwenye suluhisho la jumla kwamba $c^2=225, c=15.00$, na hivyo suluhisho maalum

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Muda mpaka tanki liwe tupu

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Ubadilishaji kuwa umbo linalotenganishika (separable form)

Pia kuna hali ambapo mlinganyo tofauti wa kawaida ambao hauwezi kutenganishwa unaweza kufanywa utenganishike kupitia badiliko linaloanzisha kigeu kipya kisichojulikana.

$$ y'=f\left(\frac {y}{x}\right). $$

Wakati wa kusuluhisha mlinganyo tofauti wa kawaida wa aina hii, tukiweka $y/x=u$, basi

$$ y=ux,\quad y'=u'x+u $$

hivyo tukibadilisha katika $y'=f(y/x)$, tunapata $u'x=f(u)-u$. Ikiwa $f(u)-u\neq0$, basi

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$

na mlinganyo unakuwa umetenganishwa.
