---
title: "ODE za Mstari za Homojenia za Daraja la Pili (Homogeneous Linear ODEs of Second Order)"
description: "Jifunze ufafanuzi na sifa za milinganyo tofauti ya kawaida ya mstari ya daraja la pili, hasa kanuni muhimu ya superposition katika ODE za mstari za homojenia na dhana ya basis inayotokana nayo."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Kwa Ufupi
> - **Umbo la kawaida(standard form)** la mlinganyo tofauti wa kawaida wa mstari wa daraja la pili: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Vigawo(coefficients)**: kazi $p$, $q$
>   - **Ingizo(input)**: $r(x)$
>   - **Tokeo(output)** au **itikio(response)**: $y(x)$
> - Homojenia na si homojenia
>   - **Homojenia(homogeneous)**: wakati, ukiandikwa katika umbo la kawaida, $r(x)\equiv0$
>   - **Si homojenia(nonhomogeneous)**: wakati, ukiandikwa katika umbo la kawaida, $r(x)\not\equiv 0$
> - **Kanuni ya superposition(superposition principle)**: kwa mlinganyo tofauti wa kawaida wa mstari wa <u>homojenia</u> $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, katika kipindi wazi $I$, mchanganyiko wa mstari wa suluhisho zozote mbili bado ni suluhisho la mlinganyo husika. Yaani, jumla ya suluhisho zozote na kuzidishwa kwake kwa konstanti kwa mlinganyo wa mstari wa homojenia uliotolewa pia ni suluhisho la mlinganyo huo.
> - **Msingi(basis)** au **mfumo msingi(fundamental system)**: jozi ya suluhisho $(y_1, y_2)$ za mlinganyo tofauti wa kawaida wa mstari wa homojenia ambazo ni huru kwa mstari katika kipindi $I$
> - **Upunguzaji wa daraja(reduction of order)**: kwa mlinganyo tofauti wa kawaida wa homojenia wa daraja la pili, ikiwa tunaweza kupata suluhisho moja, basi suluhisho la pili linalojitegemea kwa mstari na suluhisho hilo, yaani msingi, linaweza kupatikana kwa kutatua ODE ya daraja la kwanza; mbinu hii huitwa upunguzaji wa daraja
> - Matumizi ya upunguzaji wa daraja: mlinganyo wa kawaida wa daraja la pili wa jumla $F(x, y, y^\prime, y^{\prime\prime})=0$, iwe wa mstari au usio wa mstari, unaweza kupunguzwa hadi daraja la kwanza kwa kutumia upunguzaji wa daraja katika hali zifuatazo
>   - wakati $y$ haionekani moja kwa moja
>   - wakati $x$ haionekani moja kwa moja
>   - wakati ni wa mstari wa homojenia na tayari tunajua suluhisho moja
{: .prompt-info }

## Maarifa ya Awali
- [Dhana za Msingi za Uigaji(Modeling)](/posts/Basic-Concepts-of-Modeling/)
- [Mbinu ya Kutenganisha Vigeu(Separation of Variables)](/posts/Separation-of-Variables/)
- [Utatuzi wa ODE ya Mstari ya Daraja la Kwanza](/posts/Solution-of-First-Order-Linear-ODE/)

## Mlinganyo Tofauti wa Kawaida wa Mstari wa Daraja la Pili
Ikiwa mlinganyo tofauti wa kawaida wa daraja la pili unaweza kuandikwa katika umbo

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

basi huitwa **wa mstari(linear)**, na kama sivyo huitwa **usio wa mstari(nonlinear)**.

Wakati $p$, $q$, na $r$ ni kazi za $x$ ya aina yoyote, mlinganyo huu ni wa mstari kwa heshima ya $y$ na vitokavyo vyake.

Umbo kama lile la mlinganyo ($\ref{eqn:standard_form}$) huitwa **umbo la kawaida(standard form)** la mlinganyo tofauti wa kawaida wa mstari wa daraja la pili; ikiwa neno la kwanza la mlinganyo wa mstari wa daraja la pili uliotolewa ni $f(x)y^{\prime\prime}$, tunaweza kupata umbo la kawaida kwa kugawa pande zote za mlinganyo kwa $f(x)$.

Kazi $p$ na $q$ huitwa **vigawo(coefficients)**, $r(x)$ huitwa **ingizo(input)**, na $y(x)$ huitwa **tokeo(output)** au **itikio(response)** kwa ingizo na masharti ya awali.

### Mlinganyo Tofauti wa Kawaida wa Mstari wa Homojenia wa Daraja la Pili
Wacha kipindi fulani $a<x<b$ ambacho tunataka kutatua mlinganyo ($\ref{eqn:standard_form}$) kiitwe $J$. Ikiwa katika kipindi $J$, $r(x)\equiv 0$ katika mlinganyo ($\ref{eqn:standard_form}$), basi tunapata

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

na huu huitwa **homojenia(homogeneous)**.

## Mlinganyo Tofauti wa Kawaida wa Mstari usio wa Homojenia
Ikiwa katika kipindi $J$, $r(x)\not\equiv 0$, basi huitwa **si homojenia(nonhomogeneous)**.

## Kanuni ya Superposition

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ ni konstanti zozote)}\tag{3}$$

Kazi ya umbo hili huitwa **mchanganyiko wa mstari(linear combination)** wa $y_1$ na $y_2$. 

Sasa yafuatayo yanathibitika.

> **Kanuni ya superposition(superposition principle)**  
> Kwa mlinganyo tofauti wa kawaida wa mstari wa homojenia ($\ref{eqn:homogeneous_linear_ode}$), katika kipindi wazi $I$, mchanganyiko wa mstari wa suluhisho zozote mbili bado ni suluhisho la mlinganyo ($\ref{eqn:homogeneous_linear_ode}$). Yaani, jumla ya suluhisho zozote na kuzidishwa kwake kwa konstanti kwa mlinganyo wa mstari wa homojenia uliotolewa pia ni suluhisho la mlinganyo huo.
{: .prompt-info }

### Uthibitisho
Tuseme $y_1$ na $y_2$ ni suluhisho za mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) katika kipindi $I$. Tukibadilisha $y=c_1y_1+c_2y_2$ katika mlinganyo ($\ref{eqn:homogeneous_linear_ode}$), tunapata

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

hivyo tunapata utambulisho. Kwa hiyo, $y$ ni suluhisho la mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) katika kipindi $I$. $\blacksquare$

> Zingatia kwamba kanuni ya superposition hutumika tu kwa milinganyo tofauti ya kawaida ya mstari ya homojenia, na haitumiki kwa milinganyo tofauti ya kawaida ya mstari isiyo ya homojenia wala kwa milinganyo tofauti isiyo ya mstari.
{: .prompt-warning }

## Msingi na Suluhisho la Jumla
### Kukumbuka dhana kuu katika ODE ya daraja la kwanza
Kama tulivyoona awali katika [Dhana za Msingi za Uigaji(Modeling)](/posts/Basic-Concepts-of-Modeling/), tatizo la thamani ya awali(Initial Value Problem) kwa ODE ya daraja la kwanza linaundwa na mlinganyo tofauti wa kawaida pamoja na sharti la awali(initial condition) $y(x_0)=y_0$. Sharti la awali linahitajika ili kubaini konstanti holela $c$ katika suluhisho la jumla la ODE iliyotolewa, na suluhisho linalopatikana kwa namna hiyo huitwa suluhisho maalum. Sasa tuongeze dhana hizi kwa ODE za daraja la pili.

### Tatizo la thamani ya awali na masharti ya awali
**Tatizo la thamani ya awali(initial value problem)** kwa mlinganyo tofauti wa kawaida wa homojenia wa daraja la pili ($\ref{eqn:homogeneous_linear_ode}$) linaundwa na mlinganyo tofauti wa kawaida uliotolewa ($\ref{eqn:homogeneous_linear_ode}$) na **masharti mawili ya awali(initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Masharti haya yanahitajika ili kubaini konstanti mbili holela $c_1$ na $c_2$ katika **suluhisho la jumla(general solution)**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Uhuru wa mstari na utegemezi wa mstari
Hapa tusimame kidogo kuangalia dhana za uhuru wa mstari na utegemezi wa mstari. Ili kufafanua msingi baadaye, tunahitaji kuzielewa.  
Ikiwa kwa kila nukta ya kipindi $I$ ambacho kazi mbili $y_1$ na $y_2$ zimefafanuliwa,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ na }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

basi kazi hizi mbili $y_1$ na $y_2$ huitwa **huru kwa mstari(linearly independent)** katika kipindi $I$; vinginevyo, $y_1$ na $y_2$ huitwa **tegemezi kwa mstari(linearly dependent)**.

Ikiwa $y_1$ na $y_2$ ni tegemezi kwa mstari (yaani, kauli ($\ref{eqn:linearly_independent}$) si kweli), basi kwa kugawa pande zote za mlinganyo wa ($\ref{eqn:linearly_independent}$) kwa $k_1 \neq 0$ au $k_2 \neq 0$, tunaweza kuandika

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{au} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

hivyo tunaona kwamba $y_1$ na $y_2$ ni sawia.

### Msingi, suluhisho la jumla, na suluhisho maalum
Tukirudi tena, ili mlinganyo ($\ref{eqn:general_sol}$) uwe suluhisho la jumla, $y_1$ na $y_2$ lazima ziwe suluhisho za mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) na pia zisiwe sawia bali ziwe huru kwa mstari(linearly independent) katika kipindi $I$. Jozi $(y_1, y_2)$ ya suluhisho za mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) zinazotimiza masharti haya na zilizo huru kwa mstari katika kipindi $I$ huitwa **msingi(basis)** au **mfumo msingi(fundamental system)** wa suluhisho za mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) katika kipindi $I$.

Kwa kutumia masharti ya awali kubaini konstanti mbili $c_1$ na $c_2$ katika suluhisho la jumla ($\ref{eqn:general_sol}$), tunapata suluhisho la kipekee linalopita kwenye nukta $(x_0, K_0)$ na ambalo mteremko wa tangent yake katika nukta hiyo ni $K_1$. Hili huitwa **suluhisho maalum(particular solution)** la mlinganyo tofauti wa kawaida ($\ref{eqn:homogeneous_linear_ode}$).

Ikiwa mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) ni endelevu katika kipindi wazi $I$, basi lazima uwe na suluhisho la jumla, na suluhisho hilo la jumla linajumuisha suluhisho zote maalum zinazowezekana. Yaani, katika hali hii mlinganyo ($\ref{eqn:homogeneous_linear_ode}$) hauna suluhisho la ajabu(singular solution) lisiloweza kupatikana kutoka kwenye suluhisho la jumla.

## Upunguzaji wa Daraja (reduction of order)
Kwa mlinganyo tofauti wa kawaida wa homojenia wa daraja la pili, ikiwa tunaweza kupata suluhisho moja, basi tunaweza kupata suluhisho la pili linalojitegemea kwa mstari na suluhisho hilo, yaani msingi, kwa kutatua ODE ya daraja la kwanza kama ifuatavyo. Mbinu hii huitwa **upunguzaji wa daraja(reduction of order)**.

Kwa mlinganyo tofauti wa kawaida wa homojenia wa daraja la pili <u>ulio katika umbo la kawaida lenye</u> $y^{\prime\prime}$ <u>badala ya</u> $f(x)y^{\prime\prime}$

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

tuseme tunajua suluhisho moja $y_1$ la mlinganyo huu katika kipindi wazi $I$.

Sasa tukiweka suluhisho la pili tunalotafuta kuwa $y_2 = uy_1$, basi

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

na tukibadilisha haya katika mlinganyo tunapata

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Tukikusanya na kupanga kwa mujibu wa neno la $u^{\prime\prime}$, $u^{\prime}$, na $u$, tunapata

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Lakini kwa kuwa $y_1$ ni suluhisho la mlinganyo uliotolewa, kauli iliyo ndani ya mabano ya mwisho ni $0$, kwa hiyo neno la $u$ hutoweka na kubaki ODE inayohusisha $u^{\prime}$ na $u^{\prime\prime}$ pekee. Tukigawa pande zote za ODE iliyobaki kwa $y_1$, na kuweka $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, tunapata ODE ya daraja la kwanza ifuatayo.

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Tukifanya [utenganishaji wa vigeu](/posts/Separation-of-Variables/) na kuintegrali, tunapata

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

na tukichukua eksponenti kwa pande zote mbili, hatimaye tunapata

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Kwa kuwa hapo awali tuliweka $U=u^{\prime}$, basi $u=\int U dx$, hivyo suluhisho la pili $y_2$ tunalotafuta ni

$$ y_2 = uy_1 = y_1 \int U dx $$

Kwa kuwa $\cfrac{y_2}{y_1} = u = \int U dx$ haiwezi kuwa konstanti mradi $U>0$, basi $y_1$ na $y_2$ huunda msingi wa suluhisho.

### Matumizi ya upunguzaji wa daraja
Mlinganyo wa kawaida wa daraja la pili wa jumla $F(x, y, y^\prime, y^{\prime\prime})=0$, iwe wa mstari au usio wa mstari, unaweza kupunguzwa hadi daraja la kwanza kwa kutumia upunguzaji wa daraja ikiwa $y$ haionekani moja kwa moja, au $x$ haionekani moja kwa moja, au kama tulivyoona hapo juu ni wa mstari wa homojenia na tayari tunajua suluhisho moja.

#### Wakati $y$ haionekani moja kwa moja
Katika $F(x, y^\prime, y^{\prime\prime})=0$, tukiweka $z=y^{\prime}$, tunaweza kuupunguza hadi ODE ya daraja la kwanza kwa $z$, yaani $F(x, z, z^{\prime})$.

#### Wakati $x$ haionekani moja kwa moja
Katika $F(y, y^\prime, y^{\prime\prime})=0$, tukiweka $z=y^{\prime}$, basi kwa kuwa $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$, tunaweza kuupunguza hadi ODE ya daraja la kwanza kwa $z$ ambamo $y$ huchukua nafasi ya kigeu huru $x$, yaani $F(y,z,z^\prime)$.
