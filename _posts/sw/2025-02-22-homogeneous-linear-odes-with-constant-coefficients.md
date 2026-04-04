---
title: "ODE za Mstari za Homojenia za Daraja la Pili zenye Vigawo vya Kudumu"
description: "Kwa kutegemea ishara ya discriminant ya mlinganyo karakteristiki, tunaangalia maumbo ya suluhisho la jumla la ODE ya mstari ya homojenia ya daraja la pili yenye vigawo vya kudumu katika kila hali."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Kwa Ufupi
> - ODE ya mstari ya homojenia ya daraja la pili yenye vigawo vya kudumu: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Mlinganyo karakteristiki**: $\lambda^2 + a\lambda + b = 0$
> - Kulingana na ishara ya discriminant $a^2 - 4b$ ya mlinganyo karakteristiki, umbo la suluhisho la jumla linaweza kugawanywa katika hali tatu kama inavyoonyeshwa kwenye jedwali
>
> | Hali | Suluhisho za mlinganyo karakteristiki | Msingi wa suluhisho za ODE | Suluhisho la jumla la ODE |
> | :---: | :---: | :---: | :---: |
> | I | Mizizi halisi miwili tofauti<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Mzizi halisi wa marudio<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Mizizi changamano ya kiambatano<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Maarifa ya Awali
- [Mlinganyo wa Bernoulli](/posts/Bernoulli-Equation/)
- [ODE za Mstari za Homojenia za Daraja la Pili](/posts/homogeneous-linear-odes-of-second-order/)
- Fomula ya Euler

## Mlinganyo karakteristiki
Hebu tuangalie ODE ya mstari ya homojenia ya daraja la pili yenye vigawo $a$ na $b$ vya kudumu

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Milinganyo ya umbo hili hutumika kwa umuhimu mkubwa katika mitetemo ya kimakanika na ya kielektriki.

Tulipata tayari suluhisho la jumla la mlinganyo wa logistic katika [Mlinganyo wa Bernoulli](/posts/Bernoulli-Equation/), na kulingana na hilo, suluhisho la ODE ya mstari ya daraja la kwanza yenye kigawo cha kudumu $k$

$$ y^\prime + ky = 0 $$

ni kazi ya eksponenti $y = ce^{-kx}$. (Katika mlinganyo (4) wa makala hiyo, hii ni hali ya $A=-k$, $B=0$.)

Kwa hiyo, kwa mlinganyo wa umbo linalofanana, yaani ($\ref{eqn:ode_with_constant_coefficients}$), tunaweza kwanza kujaribu suluhisho la umbo

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Bila shaka, hili ni dhana tu, na hakuna uhakika wowote kwamba suluhisho la jumla litakuwa kweli katika umbo hili. Hata hivyo, vyovyote vile, tukifanikiwa kupata suluhisho mbili huru kwa mstari, basi kama tulivyoona katika [ODE za Mstari za Homojenia za Daraja la Pili](/posts/homogeneous-linear-odes-of-second-order/#msingi-na-suluhisho-la-jumla), tunaweza kupata suluhisho la jumla kwa kutumia [kanuni ya superposition](/posts/homogeneous-linear-odes-of-second-order/#kanuni-ya-superposition).  
> Kama tutakavyoona baada ya muda mfupi, pia kuna [hali ambapo tunapaswa kutafuta suluhisho la umbo tofauti](#ii-mzizi-halisi-wa-marudio-lambda---cfraca2).
{: .prompt-info }

Tukiingiza mlinganyo ($\ref{eqn:general_sol}$) pamoja na vitokavyo vyake

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

katika mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$), tunapata

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Kwa hiyo, ikiwa $\lambda$ ni suluhisho la **mlinganyo karakteristiki**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

basi kazi ya eksponenti ($\ref{eqn:general_sol}$) ni suluhisho la ODE ($\ref{eqn:ode_with_constant_coefficients}$). Tukipata suluhisho za mlinganyo wa daraja la pili ($\ref{eqn:characteristic_eqn}$), tunapata

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

na kutoka hapa kazi mbili

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

zinakuwa suluhisho za mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$).

> Maneno **mlinganyo karakteristiki** na **mlinganyo saidizi** mara nyingi hutumiwa kwa kubadilishana, lakini yana maana ileile kabisa. Unaweza kutumia lolote kati ya hayo mawili.
{: .prompt-tip }

Sasa, kulingana na ishara ya discriminant $a^2 - 4b$ ya mlinganyo karakteristiki ($\ref{eqn:characteristic_eqn}$), tunaweza kugawa hali katika tatu.
- $a^2 - 4b > 0$: mizizi halisi miwili tofauti
- $a^2 - 4b = 0$: mzizi halisi wa marudio
- $a^2 - 4b < 0$: mizizi changamano ya kiambatano

## Umbo la suluhisho la jumla kulingana na ishara ya discriminant ya mlinganyo karakteristiki
### I. Mizizi halisi miwili tofauti $\lambda_1$ na $\lambda_2$
Katika hali hii, msingi wa suluhisho za mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$) katika kipindi chochote ni

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

na suluhisho la jumla linalolingana ni

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Mzizi halisi wa marudio $\lambda = -\cfrac{a}{2}$
Iwapo $a^2 - 4b = 0$, mlinganyo wa daraja la pili ($\ref{eqn:characteristic_eqn}$) utakuwa na suluhisho moja tu, yaani $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, na kwa hiyo suluhisho la umbo $y = e^{\lambda x}$ tunaloweza kupata kutoka hapo ni moja tu:

$$ y_1 = e^{-(a/2)x} $$

Ili kupata msingi, tunahitaji kupata suluhisho la pili $y_2$ lenye umbo tofauti na lililo huru kwa mstari na $y_1$.

Njia inayoweza kutumika katika hali hii ni ile tuliyoona awali ya [upunguzaji wa daraja](/posts/homogeneous-linear-odes-of-second-order/#upunguzaji-wa-daraja-reduction-of-order). Tukiweka suluhisho la pili tunalotafuta kuwa $y_2=uy_1$, basi

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

na tukiviingiza katika mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$), tunapata

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Tukikusanya na kupanga kulingana na neno la $u^{\prime\prime}$, $u^\prime$, na $u$, tunapata

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Hapa, kwa kuwa $y_1$ ni suluhisho la mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$), basi kauli iliyo ndani ya mabano ya mwisho ni $0$, na kwa kuwa

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

kauli iliyo ndani ya mabano ya kwanza pia ni $0$. Kwa hiyo, kinachobaki ni $u^{\prime\prime}y_1 = 0$, na kutoka hapa tunapata $u^{\prime\prime}=0$. Tukifanya integresheni mara mbili, tunapata $u = c_1x + c_2$. Kwa kuwa konstantI za integresheni $c_1$ na $c_2$ zinaweza kuwa thamani zozote, tunaweza kuchagua tu $c_1=1$, $c_2=0$ na kuweka $u=x$. Hapo basi $y_2 = uy_1 = xy_1$, na kwa kuwa $y_1$ na $y_2$ ni huru kwa mstari, vinaunda msingi. Kwa hiyo, mlinganyo karakteristiki ($\ref{eqn:characteristic_eqn}$) unapokuwa na mzizi wa marudio, msingi wa suluhisho za mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$) katika kipindi chochote ni

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

na suluhisho la jumla linalolingana ni

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Mizizi changamano ya kiambatano $-\cfrac{1}{2}a + i\omega$ na $-\cfrac{1}{2}a - i\omega$
Katika hali hii, $a^2 - 4b < 0$ na $\sqrt{-1} = i$, hivyo kutoka mlinganyo ($\ref{eqn:lambdas}$) tunapata

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

na hapa tueleze idadi halisi $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Tukieleza $\omega$ kama hapo juu, suluhisho za mlinganyo karakteristiki ($\ref{eqn:characteristic_eqn}$) huwa mizizi changamano ya kiambatano $\lambda = -\cfrac{1}{2}a \pm i\omega$, na suluhisho mbili changamano za mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$) zinazolingana ni

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Hata hivyo, hata katika hali hii tunaweza kupata msingi wa suluhisho halisi zisizo za kufikirika kama ifuatavyo.

Kutoka kwenye fomula ya Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

na mlinganyo tunaoupata kwa kubadilisha $t$ na $-t$ katika mlinganyo huo,

$$ e^{-it} = \cos t - i\sin t $$

tukijumlisha na kutoa pande kwa pande, tunapata yafuatayo.

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

Kazi ya eksponenti changamano $e^z$ ya kigeu changamano $z = r + it$ chenye sehemu halisi $r$ na sehemu ya kufikirika $it$ inaweza kufafanuliwa kwa kutumia kazi halisi $e^r$, $\cos t$, na $\sin t$ kama ifuatavyo.

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Hapa tukiweka $r=-\cfrac{1}{2}ax$ na $t=\omega x$, tunaweza kuandika

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Kwa [kanuni ya superposition](/posts/homogeneous-linear-odes-of-second-order/#kanuni-ya-superposition), jumla na bidhaa kwa konstanti za suluhisho hizi changamano pia ni suluhisho. Kwa hiyo, tukijumlisha milinganyo hii miwili pande kwa pande na kuzidisha pande zote mbili kwa $\cfrac{1}{2}$, tunaweza kupata suluhisho la kwanza halisi $y_1$ kama ifuatavyo.

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Kwa njia hiyohiyo, tukitoa mlinganyo wa pili kutoka wa kwanza pande kwa pande na kuzidisha pande zote mbili kwa $\cfrac{1}{2i}$, tunaweza kupata suluhisho la pili halisi $y_2$.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Kwa kuwa $\cfrac{y_1}{y_2} = \cot{\omega x}$ na hii si konstanti, basi $y_1$ na $y_2$ ni huru kwa mstari katika kila kipindi, na hivyo huunda msingi wa suluhisho halisi za mlinganyo ($\ref{eqn:ode_with_constant_coefficients}$). Kutoka hapa tunapata suluhisho la jumla

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ ni konstanti zozote)} \label{eqn:general_sol_3}\tag{13}$$


