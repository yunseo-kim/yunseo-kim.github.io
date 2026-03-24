---
title: Kisima cha Mraba Kisicho na Kikomo cha 1D (The 1D Infinite Square Well)
description: Makala hii inachunguza kisima cha mraba kisicho na kikomo cha 1D, tatizo rahisi lakini muhimu la mekanika ya kwanta, na hupata hali tulivu, viwango vya nishati, sifa nne za ψ(x), na suluhisho la jumla Ψ(x,t).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Tatizo la kisima cha mraba kisicho na kikomo cha 1D: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{venginevyo}
>   \end{cases}$$
> - Masharti ya mpaka: $ \psi(0) = \psi(a) = 0 $
> - Kiwango cha nishati cha hali tulivu ya $n$: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Suluhisho la mlinganyo wa Schrödinger usiotegemea muda ndani ya kisima:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Tafsiri ya kifizikia ya kila hali tulivu $\psi_n$: 
>   - Umbo la wimbi simama linalojitokeza kwenye kamba yenye urefu $a$
>   - **hali ya msingi (ground state)**: hali tulivu $\psi_1$ yenye nishati ya chini kabisa
>   - **hali zilizochochewa (excited states)**: hali zilizosalia zenye $n\geq 2$, ambazo nishati yake huongezeka sawia na $n^2$
> - Sifa 4 muhimu za kihisabati za $\psi_n$:
>   1. Ikiwa potensheli $V(x)$ ina usimetri, basi kazi parifu na kazi impari hujitokeza kwa kupokezana kuhusu katikati ya kisima
>   2. Kadiri nishati inavyoongezeka, kila hali inayofuatana huongezeka kwa **nodi (node)** moja
>   3. Ina **uorthonormali (orthonormality)**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Ina **ukamilifu (completeness)**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Suluhisho la jumla la mlinganyo wa Schrödinger (muunganiko wa mstari wa hali tulivu):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{ambapo mgawo }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Mahitaji ya awali
- Mgawanyo endelevu wa uwezekano na msongamano wa uwezekano
- Uorthogonali na unormalishaji (aljebra ya mstari)
- Mfululizo wa Fourier na ukamilifu (aljebra ya mstari)
- [Mlinganyo wa Schrödinger na kazi ya wimbi](/posts/schrodinger-equation-and-the-wave-function/)
- [Theoremu ya Ehrenfest](/posts/ehrenfest-theorem/)
- [Mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/)

## Sharti la potensheli lililopewa
Iwapo potensheli ni

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{venginevyo}
\end{cases} \tag{1}$$

basi chembe iliyo ndani ya potensheli hii ni chembe huru katika eneo la $0<x<a$, na kwenye ncha zote mbili ($x=0$ na $x=a$) kuna nguvu isiyo na kikomo inayofanya isiweze kutoroka. Katika modeli ya klasiki, hili hufasiriwa kama mwendo wa kwenda na kurudi usio na mwisho, ambapo kunakuwa na migongano ya kikamilifu elastiki mbele na nyuma na hakuna nguvu zisizohifadhi zinazotenda. Ingawa potensheli ya aina hii ni ya kubuniwa sana na rahisi kupita kiasi, ni kwa sababu hiyo hiyo inaweza kuwa rejea yenye manufaa utakaposoma baadaye hali nyingine za kifizikia katika mekanika ya kwanta, hivyo inafaa kuichunguza kwa makini.

![Kisima cha potensheli kisicho na kikomo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Chanzo cha picha*
> - Mwandishi: mtumiaji wa Wikimedia [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - Leseni: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Kuweka modeli na masharti ya mpaka
Nje ya kisima, uwezekano wa kumpata chembe ni $0$, hivyo $\psi(x)=0$. Ndani ya kisima, kwa kuwa $V(x)=0$, [mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/) unakuwa

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

na hivyo unaweza kuandikwa katika umbo

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ ambapo } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Hapa tunadhania kuwa $E\geq 0$.
{: .prompt-info }

Huu ni mlinganyo unaoelezea **osileta rahisi wa harmoniki (simple harmonic oscillator)**, na suluhisho lake la jumla ni

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

Hapa $A$ na $B$ ni viwango vya kiholela, na kwa kawaida viwango hivi huamuliwa na **masharti ya mpaka** yaliyopewa kwenye tatizo unapopata suluhisho maalumu linalolingana na hali husika. <u>Kwa $\psi(x)$, kwa kawaida masharti ya mpaka ni kwamba $\psi$ na $d\psi/dx$ viwe vyote endelevu, lakini mahali ambapo potensheli inakuwa isiyo na kikomo, ni $\psi$ pekee inayokuwa endelevu.</u>

## Kupata suluhisho la mlinganyo wa Schrödinger usiotegemea muda

Kwa kuwa $\psi(x)$ ni endelevu,

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

lazima iunganishwe na suluhisho la nje ya kisima. Katika mlinganyo ($\ref{eqn:psi_general_solution}$), tunapoweka $x=0$ tunapata

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

hivyo, kwa kuweka ($\ref{eqn:boundary_conditions}$), lazima $B=0$.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Basi $\psi(a)=A\sin{ka}$, kwa hiyo ili kutosheleza $\psi(a)=0$ ya mlinganyo ($\ref{eqn:boundary_conditions}$), ni lazima iwe ama $A=0$ (suluhisho la trivial) au $\sin{ka}=0$. Kwa hiyo,

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Hapa pia, $k=0$ ni suluhisho la trivial, na kwa kuwa husababisha $\psi(x)=0$ hivyo haliwezi kunormalishwa, si suluhisho tunalolitafuta kwenye tatizo hili. Aidha, kwa kuwa $\sin(-\theta)=-\sin(\theta)$, alama hasi inaweza kufyonzwa ndani ya $A$ katika mlinganyo ($\ref{eqn:psi_without_B}$), hivyo hatupotezi ujumla wowote kwa kuzingatia tu hali ya $ka>0$. Kwa hiyo suluhisho zinazowezekana kwa $k$ ni

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Basi $\psi_n=A\sin{k_n x}$ na $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, kwa hiyo tukiziweka katika mlinganyo ($\ref{eqn:t_independent_schrodinger_eqn}$), thamani zinazowezekana za $E$ ni kama ifuatavyo.

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

Kinyume kabisa na hali ya klasiki, chembe ya kwanta ndani ya kisima cha mraba kisicho na kikomo haiwezi kuwa na nishati yoyote tu, bali lazima iwe na moja kati ya thamani zinazoruhusiwa.

> Nishati huwa ya kwanta kwa sababu ya masharti ya mpaka yanayotumika kwa suluhisho za mlinganyo wa Schrödinger usiotegemea muda.
{: .prompt-info }

Sasa tunaweza kunormalisha $\psi$ ili kupata $A$.

> Kimsingi tunapaswa kunormalisha $\Psi(x,t)$, lakini kwa mujibu wa mlinganyo (11) wa [mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/#1-ni-hali-tulivu-stationary-states), hili ni sawa na kunormalisha $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Kwa ukali wa kihisabati, hili huamua ukubwa wa $A$ pekee, lakini kwa kuwa awamu ya $A$ haina maana yoyote ya kifizikia, tunaweza kutumia tu mzizi wa mraba halisi chanya kama $A$. Kwa hiyo, suluhisho ndani ya kisima ni

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Tafsiri ya kifizikia ya kila hali tulivu $\psi_n$
Kwa kutumia mlinganyo ($\ref{eqn:psi_n}$), tumepata suluhisho zisizo na kikomo kwa kila kiwango cha nishati $n$ kutoka kwenye mlinganyo wa Schrödinger usiotegemea muda. Tukichora chache za kwanza kati ya hizo, tunapata picha iliyo hapa chini.

![Kazi za wimbi za awali kwa hali nne za chini kabisa za kwanta](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Chanzo cha picha*
> - Mwandishi: mtumiaji wa Wikimedia [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - Leseni: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Hali hizi zina umbo la wimbi simama linalojitokeza kwenye kamba yenye urefu $a$. $\psi_1$ yenye nishati ya chini kabisa huitwa **hali ya msingi (ground state)**, na hali zilizosalia zenye $n\geq 2$ ambazo nishati yake huongezeka sawia na $n^2$ huitwa **hali zilizochochewa (excited states)**.

## Sifa 4 muhimu za kihisabati za $\psi_n$
Kila kazi $\psi_n(x)$ ina sifa 4 muhimu zifuatazo. Sifa hizi nne zina nguvu sana, na hazihusiani tu na kisima cha mraba kisicho na kikomo. Sifa ya kwanza hutimia kila mara ikiwa potensheli yenyewe ni kazi yenye usimetri, ilhali sifa ya pili, ya tatu, na ya nne ni sifa za jumla zinazoonekana bila kujali umbo la potensheli.

### 1. Kuhusu katikati ya kisima, kazi parifu na kazi impari hujitokeza kwa kupokezana.
Kwa kila nambari asilia $n$, $\psi_{2n-1}$ ni kazi parifu na $\psi_{2n}$ ni kazi impari.

### 2. Kadiri nishati inavyoongezeka, kila hali inayofuatana huwa na nodi moja zaidi.
Kwa kila nambari asilia $n$, $\psi_n$ ina **nodi (node)** $(n-1)$.

### 3. Hali hizi zina uorthogonali (orthogonality).

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

kwa maana hiyo, hali hizi ni **orthogonal** kwa kila nyingine.

> Katika kisima cha mraba kisicho na kikomo tunachokichunguza sasa, $\psi$ ni halisi, hivyo hakuna haja ya kuchukua konjugati changamani ($^*$) ya $\psi_m$, lakini ni vyema kuzoea kuiweka kila mara kwa ajili ya hali ambazo si hivyo.
{: .prompt-tip }

#### Uthibitisho
Wakati $m\neq n$,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Wakati $m=n$, kutokana na unormalishaji, integra hii huwa $1$, na tukitumia **delta ya Kronecker (Kronecker delta)** $\delta_{mn}$, tunaweza kuwakilisha pamoja uorthogonali na unormalishaji kama

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

kwa uandishi mmoja. Hapo tunasema kwamba $\psi$ ziko katika hali ya **uorthonormali (orthonormal)**.

### 4. Kazi hizi zina ukamilifu (completeness).
Kwa maana kwamba kazi yoyote nyingine holela $f(x)$ inaweza kuandikwa kama muunganiko wa mstari

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

kazi hizi ni **kamili (complete)**. Mlinganyo ($\ref{eqn:fourier_series}$) ni **mfululizo wa Fourier (Fourier series)** wa $f(x)$, na ukweli kwamba kazi yoyote holela inaweza kuendelezwa kwa namna hii huitwa **teoremu ya Dirichlet (Dirichlet's theorem)**.

## Kupata mgawo $c_n$ kwa kutumia mbinu ya Fourier (Fourier's trick)
Wakati $f(x)$ imepewa, kwa kutumia ukamilifu na uorthonormali hapo juu, tunaweza kupata mgawo $c_n$ kwa mbinu ifuatayo inayoitwa **mbinu ya Fourier (Fourier's trick)**. Tukizidisha pande zote mbili za mlinganyo ($\ref{eqn:fourier_series}$) kwa $\psi_m(x)^*$ na kisha kuintegra, kwa mujibu wa milinganyo ($\ref{eqn:orthonomality}$) na ($\ref{eqn:kronecker_delta}$), tunapata

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Zingatia kuwa kwa sababu ya delta ya Kronecker, vipengele vyote kwenye jumla hupotea isipokuwa kile chenye $n=m$.
{: .prompt-info }

Kwa hiyo, wakati wa kuendeleza $f(x)$, mgawo wa daraja la $n$ ni

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Kupata suluhisho la jumla $\Psi(x,t)$ la mlinganyo wa Schrödinger unaotegemea muda
Kila hali tulivu ya kisima cha mraba kisicho na kikomo, kwa mujibu wa [mlinganyo (10) wa chapisho la 'Mlinganyo wa Schrödinger usiotegemea muda'](/posts/time-independent-schrodinger-equation/#1-ni-hali-tulivu-stationary-states) na mlinganyo ($\ref{eqn:psi_n}$) tulioupata hapo juu, ni

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Pia, katika [mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/#3-suluhisho-la-jumla-la-mlinganyo-wa-schrodinger-unaotegemea-muda-ni-muunganiko-wa-mstari-wa-suluhisho-zilizopatikana-kwa-utenganishaji-wa-vigezo), tayari tumeona kuwa suluhisho la jumla la mlinganyo wa Schrödinger linaweza kuonyeshwa kama muunganiko wa mstari wa hali tulivu. Kwa hiyo,

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

inaweza kuandikwa. Sasa kinachobaki ni kupata mgawo $c_n$ unaotosheleza sharti lifuatalo.

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Kwa ukamilifu wa $\psi$ tuliouona hapo juu, siku zote upo mgawo $c_n$ unaotosheleza hili, na tunaweza kuupata kwa kuweka $\Psi(x,0)$ mahali pa $f(x)$ katika mlinganyo ($\ref{eqn:coefficients_n}$).

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Ikiwa $\Psi(x,0)$ imetolewa kama sharti la awali, tunapata mgawo wa uendelezaji $c_n$ kwa kutumia mlinganyo ($\ref{eqn:calc_of_cn}$), kisha tunaweka katika mlinganyo ($\ref{eqn:general_solution}$) ili kupata $\Psi(x,t)$. Baada ya hapo, tunaweza kuhesabu kiasi chochote cha kifizikia tunachopendezwa nacho kwa kufuata mchakato wa [Theoremu ya Ehrenfest](/posts/ehrenfest-theorem/). Njia hii inaweza kutumika si tu kwa kisima cha mraba kisicho na kikomo bali pia kwa potensheli yoyote ile; kinachobadilika ni umbo la kazi za $\psi$ na mlinganyo unaoelezea viwango vya nishati vinavyoruhusiwa.

## Utoaji wa uhifadhi wa nishati ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Kwa kutumia uorthonormali wa $\psi(x)$ (milinganyo [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]), hebu tutoe uhifadhi wa nishati ambao tuliuangalia kwa kifupi awali katika [mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/#uhifadhi-wa-nishati). Kwa kuwa $c_n$ hazitegemei muda, inatosha kuonyesha tu kwamba hili ni kweli kwa hali ya $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Pia,

$$ \hat{H}\psi_n = E_n\psi_n $$

hivyo tunapata yafuatayo.

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
