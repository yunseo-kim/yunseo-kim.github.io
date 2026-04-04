---
title: "Suluhisho la kianalitiki la osileta harmoniki (The Harmonic Oscillator)"
description: "Tunaweka mlinganyo wa Schrödinger kwa osileta harmoniki katika mekaniki ya kwanta na kuchunguza njia ya suluhisho la kianalitiki. Kwa kuanzisha kigeu kisicho na vipimo 𝜉, tunatatua mlinganyo huo na kuwakilisha hali tuli zilizonormishwa kwa kutumia polinomu za Hermite."
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---

## Kwa kifupi

> - Iwapo amplitudo ni ndogo vya kutosha, mtetemo wowote unaweza kukaribiwa kama mtetemo harmoniki sahili (simple harmonic oscillation), na kwa sababu hiyo mtetemo harmoniki sahili una umuhimu mkubwa katika fizikia
> - Osileta harmoniki: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - Uanzishaji wa kigeu kisicho na vipimo $\xi$ na nishati $K$ iliyoandikwa katika vipimo vya $\cfrac{1}{2}\hbar\omega$:
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - Wakati $\|\xi\|^2 \to \infty$, suluhisho la asimptotiki linalokubalika kimwili ni $\psi(\xi) \to Ae^{-\xi^2/2}$, kwa hiyo
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(ambapo }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - Tukiwakilisha suluhisho la mlinganyo ulio juu kwa umbo la mfululizo $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$, tunapata
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - Ili suluhisho hili liweze kunormishwa, mfululizo $\sum a_j$ lazima uwe wa mwisho; yaani, lazima kuwe na thamani fulani ya “juu kabisa” ya $j$, $n\in \mathbb{N}$, kiasi kwamba $a_j=0$ kwa $j>n$, kwa hiyo
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - Kwa ujumla, $h_n(\xi)$ ni polinomu ya daraja la $n$ katika $\xi$, na sehemu inayobaki baada ya kuondoa mgawo wa mbele ($a_0$ au $a_1$) huitwa **polinomu za Hermite (Hermite polynomials)** $H_n(\xi)$
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - Hali tuli zilizonormishwa za osileta harmoniki:
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - Sifa za osileta ya kwanta
>   - Kazi zake za eigeni huonyesha mfuatano wa zamu wa kazi shufwa na kazi witiri
>   - Hata katika maeneo yasiyowezekana katika mekaniki ya klasiki (yaani, $x$ kubwa kuliko amplitudo ya klasiki kwa $E$ iliyotolewa), uwezekano wa kuipata si $0$, kwa hiyo chembe inaweza kuwepo humo ingawa kwa uwezekano mdogo
>   - Kwa hali tuli zote ambazo $n$ ni witiri, uwezekano wa kumpata chembe katikati ni $0$
>   - Kadiri $n$ inavyokuwa kubwa, ndivyo mfumo unavyozidi kufanana na osileta ya klasiki
{: .prompt-info }

## Maarifa ya Awali

- [Mbinu ya utenganishaji wa vigeu](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Mlinganyo wa Schrödinger na kazi ya mawimbi](/posts/schrodinger-equation-and-the-wave-function/)
- [Nadharia ya Ehrenfest](/posts/ehrenfest-theorem/)
- [Mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/)
- [Kisanduku kisicho na kikomo cha mraba cha 1D](/posts/the-infinite-square-well/)
- [Suluhisho la kialjebra la osileta harmoniki](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## Uwekaji wa modeli

Kwa maelezo ya jinsi osileta harmoniki inavyoelezwa katika mekaniki ya klasiki na umuhimu wa tatizo la osileta harmoniki, rejea [makala iliyotangulia](/posts/algebraic-solution-of-the-harmonic-oscillator/).

### Osileta harmoniki katika mekaniki ya kwanta

Tatizo la osileta harmoniki ya kwanta ni kutatua mlinganyo wa Schrödinger kwa potensia

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

Mlinganyo wa Schrödinger usiotegemea muda kwa osileta harmoniki ni

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

Kuna njia mbili tofauti kabisa za kushughulikia tatizo hili. Moja ni njia ya kianalitiki (analytic method) inayotumia **mfululizo wa nguvu (power series)**, na nyingine ni njia ya kialjebra (algebraic method) inayotumia **opereta za ngazi (ladder operators)**. Njia ya kialjebra ni ya haraka na rahisi zaidi, lakini bado ni muhimu kusoma pia suluhisho la kianalitiki linalotumia mfululizo wa nguvu. [Tayari tumeshashughulikia njia ya suluhisho la kialjebra](/posts/algebraic-solution-of-the-harmonic-oscillator/), na hapa tutashughulikia njia ya suluhisho la kianalitiki.

## Kubadilisha umbo la mlinganyo wa Schrödinger

Tukianzisha kigeu kisicho na vipimo

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

basi mlinganyo wa Schrödinger usiotegemea muda ($\ref{eqn:t_independent_schrodinger_eqn}$) unaweza kuandikwa kwa umbo rahisi kama ifuatavyo:

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

Hapa $K$ ni nishati iliyoandikwa katika vipimo vya $\cfrac{1}{2}\hbar\omega$.

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

Sasa tunahitaji kutatua mlinganyo huu ulioandikwa upya ($\ref{eqn:schrodinger_eqn_with_xi}$). Kwanza, kwa $\xi$ kubwa sana (yaani kwa $x$ kubwa sana), tuna $\xi^2 \gg K$, kwa hiyo

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

na suluhisho lake la kukaribia ni

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

Hata hivyo, hapa neno la $B$ hutawanyika wakati $\|x\|\to \infty$, kwa hiyo haliwezi kunormishwa. Kwa hivyo, suluhisho la asimptotiki linalokubalika kimwili ni

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

Sasa tutenganishe sehemu ya eksponenti na kuandika

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(ambapo }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

> Ili kupata sehemu ya eksponenti $e^{-\xi^2/2}$, tulitumia mbinu ya kukaribia tu katika uderivesheni ili kubaini umbo la asimptotiki. Hata hivyo, mlinganyo tulioupata kwa njia hiyo, yaani ($\ref{eqn:psi_and_h}$), si mlinganyo wa kukaribia bali ni mlinganyo sahihi kabisa. Kutenganisha umbo la asimptotiki kwa namna hii ni hatua ya kwanza ya kawaida inayotumiwa wakati wa kutatua mlinganyo wa diferenshali kwa umbo la mfululizo wa nguvu.
{: .prompt-info }

Tukiderive mlinganyo ($\ref{eqn:psi_and_h}$) ili kupata $\cfrac{d\psi}{d\xi}$ na $\cfrac{d^2\psi}{d\xi^2}$, tunapata

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

kwa hiyo mlinganyo wa Schrödinger ($\ref{eqn:schrodinger_eqn_with_xi}$) sasa unakuwa

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

## Upanuzi wa mfululizo wa nguvu

Kwa mujibu wa nadharia ya Taylor (Taylor's theorem), kazi yoyote laini inaweza kuwakilishwa kwa mfululizo wa nguvu, kwa hiyo tutafute suluhisho la mlinganyo ($\ref{eqn:schrodinger_eqn_with_h}$) katika umbo la mfululizo wa $\xi$:

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

Tukiderive kila neno katika mfululizo huu, tunapata milinganyo miwili ifuatayo:

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

Tukiingiza tena milinganyo hii miwili katika mlinganyo wa Schrödinger (Mlinganyo [$\ref{eqn:schrodinger_eqn_with_h}$]), tunapata

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

Kwa sababu ya upekee wa upanuzi wa mfululizo wa nguvu, mgawo wa kila daraja la $\xi$ lazima uwe $0$, hivyo

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

**Fomula hii ya urejeleaji (recursion formula)** ni sawia kabisa na mlinganyo wa Schrödinger. Tukipewa viwango viwili vya kiholela $a_0$ na $a_1$, tunaweza kupata migawo ya maneno yote ya suluhisho $h(\xi)$.

Hata hivyo, suluhisho lililopatikana kwa namna hii haliwezi kunormishwa daima. Ikiwa mfululizo $\sum a_j$ ni mfululizo usio na mwisho (yaani, ikiwa $\lim_{j\to\infty} a_j\neq0$), basi kwa $j$ kubwa sana fomula ya urejeleaji hapo juu inakuwa kwa kukaribia

$$ a_{j+2} \approx \frac{2}{j}a_j $$

na suluhisho lake la kukaribia ni

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ ni konstanti ya kiholela)}$$

Katika hali hiyo, kwa thamani kubwa za $\xi$ ambapo maneno ya daraja la juu hutawala, tunapata

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

Kwa hiyo ikiwa $h(\xi)$ ina umbo la $Ce^{\xi^2}$, basi kutoka kwa mlinganyo ($\ref{eqn:psi_and_h}$), $\psi(\xi)$ itakuwa na umbo la $Ce^{\xi^2/2}$, na hivyo itatawanyika wakati $\xi \to \infty$. Hili linalingana na suluhisho lisiloweza kunormishwa la mlinganyo ($\ref{eqn:psi_approx}$) ambapo $A=0, B\neq0$.

Kwa hiyo mfululizo $\sum a_j$ lazima uwe wa mwisho. Lazima kuwe na thamani fulani ya “juu kabisa” ya $j$, $n\in \mathbb{N}$, kiasi kwamba $a_j=0$ kwa $j>n$. Ili hali hii itimie, ni lazima kwa $a_n\neq0$ tuwe na $a_{n+2}=0$, kwa hiyo kutokana na mlinganyo ($\ref{eqn:recursion_formula}$),

$$ K = 2n + 1 $$

Tukiingiza hili katika mlinganyo ($\ref{eqn:K}$), tunapata nishati zinazokubalika kimwili:

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

Kwa njia hii, tumepata tena kwa mbinu tofauti kabisa hali ya quantization ya nishati katika mlinganyo (21) wa [Suluhisho la kialjebra la osileta harmoniki](/posts/algebraic-solution-of-the-harmonic-oscillator/#hali-tuli-psi_n-na-viwango-vya-nishati-e_n).

## Polinomu za Hermite (Hermite polynomials) $H_n(\xi)$ na hali tuli $\psi_n(x)$

### Polinomu za Hermite $H_n$

Kwa ujumla, $h_n(\xi)$ ni polinomu ya daraja la $n$ katika $\xi$, na ikiwa $n$ ni shufwa ina maneno ya madaraja shufwa pekee, huku ikiwa $n$ ni witiri ina maneno ya madaraja witiri pekee. Hapa, sehemu inayobaki baada ya kuondoa mgawo wa mbele ($a_0$ au $a_1$) huitwa **polinomu za Hermite (Hermite polynomials)** $H_n(\xi)$.

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

Kwa desturi, migawo huchaguliwa kiholela ili mgawo wa neno la daraja la juu zaidi katika $H_n$ uwe $2^n$.

Ifuatayo ni baadhi ya polinomu za Hermite za mwanzo.

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### Hali tuli $\psi_n(x)$

Hali tuli zilizonormishwa za osileta harmoniki ni kama ifuatavyo:

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

Hili linalingana na matokeo yaliyopatikana katika [Suluhisho la kialjebra la osileta harmoniki](/posts/algebraic-solution-of-the-harmonic-oscillator/#unormishaji) (Mlinganyo [27]).

Picha ifuatayo inaonyesha hali tuli $\psi_n(x)$ na msongamano wa uwezekano $\|\psi_n(x)\|^2$ kwa thamani 8 za kwanza za $n$. Tunaweza kuona kwamba kazi za eigeni za osileta ya kwanta huonyesha kwa zamu kazi shufwa na kazi witiri.

![Uwakilishi wa kazi za mawimbi kwa hali nane za kwanza za eigeni zilizofungwa, n = 0 hadi 7. Mhimili mlalo unaonyesha nafasi x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *Chanzo cha picha*
> - Mtunzi: mtumiaji wa Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Leseni: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Mison gamano ya uwezekano inayolingana.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *Chanzo cha picha*
> - Mtunzi: mtumiaji wa Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Leseni: Public Domain

Osileta ya kwanta ni tofauti sana na osileta yake ya klasiki inayolingana; si tu kwamba nishati yake imequantishwa, bali pia usambazaji wa uwezekano wa nafasi $x$ unaonyesha sifa za ajabu.
- Hata katika maeneo yasiyowezekana katika mekaniki ya klasiki (yaani, $x$ kubwa kuliko amplitudo ya klasiki kwa $E$ iliyotolewa), uwezekano wa kuipata si $0$, kwa hiyo chembe inaweza kuwepo humo ingawa kwa uwezekano mdogo
- Kwa hali tuli zote ambazo $n$ ni witiri, uwezekano wa kumpata chembe katikati ni $0$

Kadiri $n$ inavyokuwa kubwa, ndivyo osileta ya kwanta inavyoonyesha tabia inayofanana zaidi na osileta ya klasiki. Picha iliyo hapa chini inaonyesha usambazaji wa uwezekano wa nafasi $x$ wa klasiki (mstari wa vipande) na hali ya kwanta $\|\psi_{30}\|^2$ wakati $n=30$ (mstari kamili). Ukisawazisha sehemu zenye mipasuko, grafu hizo mbili huonekana kukaribiana kwa ujumla.

![Usambazaji wa uwezekano wa kwanta (mstari kamili) na wa klasiki (mstari wa vipande) wa hali iliyochochewa ya n = 30 ya osileta harmoniki ya kwanta. Mistari ya vipande wima inaonyesha nukta za kugeukia za klasiki.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *Chanzo cha picha*
> - Mtunzi: mtumiaji wa Wikimedia [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - Leseni: Public Domain

### Taswira ya kuingiliana ya usambazaji wa uwezekano wa osileta ya kwanta

Ifuatayo ni taswira responsivu niliyoiandika mwenyewe kwa msingi wa Plotly.js. Kwa kusogeza slaida ili kubadilisha thamani ya $n$, unaweza kuona umbo la usambazaji wa uwezekano wa klasiki wa nafasi $x$ pamoja na $\|\psi_n\|^2$.

<div class="plotly-iframe-container" style="position: relative; height: 850px; overflow: hidden;">
    <iframe id="plotly-iframe"
            src="/physics-visualizations/quantum-harmonic-oscillator.html"
            title="Quantum Harmonic Oscillator: Probability Density"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; overflow:hidden" 
            allow="fullscreen"
            scrolling="no"
            loading="lazy">
    </iframe>
</div>

> - Ukurasa wa asili wa taswira: <a {% static_href %}href="{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html"{% endstatic_href %}>{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html</a>
> - Msimbo chanzi: [hifadhi ya yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/quantum-harmonic-oscillator.html)
> - Leseni: [Tazama hapa](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Aidha, ikiwa unaweza kutumia Python kwenye kompyuta yako mwenyewe na una mazingira yenye maktaba za Numpy, Plotly, na Dash zimesakinishwa, unaweza pia kuona matokeo kwa kuendesha skripti ya Python [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/quantum_oscillator.py) ndani ya hifadhi hiyo hiyo.
