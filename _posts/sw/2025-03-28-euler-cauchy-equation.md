---
title: "Mlinganyo wa Euler-Cauchy"
description: "Kwa kutegemea ishara ya diskriminanti ya mlinganyo saidizi, tunaangalia maumbo ya suluhisho la jumla la mlinganyo wa Euler-Cauchy katika kila hali."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Kwa Ufupi
> - Mlinganyo wa Euler-Cauchy: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Mlinganyo saidizi(auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - Kulingana na ishara ya diskriminanti $(1-a)^2 - 4b$ ya mlinganyo saidizi, umbo la suluhisho la jumla linaweza kugawanywa katika hali tatu kama inavyoonyeshwa kwenye jedwali
>
> | Hali | Mizizi ya mlinganyo saidizi | Msingi wa suluhisho za mlinganyo wa Euler-Cauchy | Suluhisho la jumla la mlinganyo wa Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Mizizi halisi tofauti<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Mzizi halisi maradufu<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Mizizi changamani shirikishi<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Maarifa ya Awali
- [ODE za Mstari za Homojenia za Daraja la Pili (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [ODE za Mstari za Homojenia za Daraja la Pili zenye Vigawo Vya Kudumu](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Fomula ya Euler

## Mlinganyo saidizi (auxiliary equation)
**Mlinganyo wa Euler-Cauchy(Euler-Cauchy equation)** ni mlinganyo tofauti wa kawaida wa umbo

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

ambapo $a$ na $b$ ni konstanti zilizotolewa, na $y(x)$ ni kazi isiyojulikana.

Tukibadilisha katika mlinganyo ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

tunapata

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

yaani,

$$ [m(m-1) + am + b]x^m = 0 $$

Kutokana na hili tunapata mlinganyo saidizi

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

na sharti la lazima na la kutosha ili $y=x^m$ iwe suluhisho la mlinganyo wa Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) ni kwamba $m$ iwe suluhisho la mlinganyo saidizi ($\ref{eqn:auxiliary_eqn}$).

Tukitatua mlinganyo wa pili ($\ref{eqn:auxiliary_eqn}$), tunapata

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

na kutokana na hili kazi mbili

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

zinakuwa suluhisho za mlinganyo ($\ref{eqn:euler_cauchy_eqn}$).

Kama ilivyo katika [ODE za Mstari za Homojenia za Daraja la Pili zenye Vigawo Vya Kudumu](/posts/homogeneous-linear-odes-with-constant-coefficients/), kulingana na ishara ya diskriminanti $(1-a)^2 - 4b$ ya mlinganyo saidizi ($\ref{eqn:auxiliary_eqn}$), tunaweza kugawa hali katika tatu.
- $(1-a)^2 - 4b > 0$: mizizi miwili halisi tofauti
- $(1-a)^2 - 4b = 0$: mzizi halisi maradufu
- $(1-a)^2 - 4b < 0$: mizizi changamani shirikishi

## Umbo la suluhisho la jumla kulingana na ishara ya diskriminanti ya mlinganyo saidizi
### I. Mizizi miwili halisi tofauti $m_1$ na $m_2$
Katika hali hii, katika kipindi chochote msingi wa suluhisho za mlinganyo ($\ref{eqn:euler_cauchy_eqn}$) ni

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

na suluhisho la jumla linalolingana nayo ni

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Mzizi halisi maradufu $m = \cfrac{1-a}{2}$
Iwapo $(1-a)^2 - 4b = 0$, yaani $b=\cfrac{(1-a)^2}{4}$, basi mlinganyo wa pili ($\ref{eqn:auxiliary_eqn}$) unakuwa na suluhisho moja tu, $m = m_1 = m_2 = \cfrac{1-a}{2}$, na hivyo suluhisho moja la umbo $y = x^m$ linaloweza kupatikana kutokana na hilo ni

$$ y_1 = x^{(1-a)/2} $$

na mlinganyo wa Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) unakuwa katika umbo

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Sasa tupate suluhisho jingine $y_2$ lililo huru kwa mstari kwa kutumia [upunguzaji wa daraja(reduction of order)](/posts/homogeneous-linear-odes-of-second-order/#upunguzaji-wa-daraja-reduction-of-order).

Tukiweka suluhisho la pili tunalotafuta kuwa $y_2=uy_1$, tunapata

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Kwa kuwa $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

na tukifanya integra, tunapata $u = \ln x$.

Kwa hiyo $y_2 = uy_1 = y_1 \ln x$, na kwa kuwa uwiano wao si konstanti, $y_1$ na $y_2$ ni huru kwa mstari. Suluhisho la jumla linalolingana na msingi $y_1$ na $y_2$ ni

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Mizizi changamani shirikishi
Katika hali hii, suluhisho za mlinganyo saidizi ($\ref{eqn:auxiliary_eqn}$) ni $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, na suluhisho mbili changamani za mlinganyo ($\ref{eqn:euler_cauchy_eqn}$) zinazolingana nazo zinaweza kuandikwa kama ifuatavyo kwa kutumia kwamba $x=e^{\ln x}$.

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Tukiweka $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ na kutumia fomula ya Euler $e^{it} = \cos{t} + i\sin{t}$, tunapata

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

na kutokana na hili tunapata suluhisho mbili halisi zifuatazo

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Kwa kuwa uwiano wao $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ si konstanti, suluhisho hizi mbili ni huru kwa mstari, na kwa hiyo kwa [kanuni ya superposition](/posts/homogeneous-linear-odes-of-second-order/#kanuni-ya-superposition) zinaunda msingi wa mlinganyo wa Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$). Kutokana na hili tunapata suluhisho la jumla halisi lifuatalo.

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Hata hivyo, katika mlinganyo wa Euler-Cauchy, hali ambapo mlinganyo saidizi una mizizi changamani shirikishi haina umuhimu mkubwa sana kivitendo.

## Ubadilishaji kuwa ODE ya mstari ya homojenia ya daraja la pili yenye vigawo vya kudumu
Mlinganyo wa Euler-Cauchy unaweza kubadilishwa kuwa [ODE ya mstari ya homojenia ya daraja la pili yenye vigawo vya kudumu](/posts/homogeneous-linear-odes-with-constant-coefficients/) kwa kutumia ubadilishaji wa kigeu.

Tukifanya ubadilishaji $x = e^t$, tunapata

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

na hivyo mlinganyo wa Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) hubadilika kuwa ODE ya mstari ya homojenia yenye vigawo vya kudumu kwa $t$ kama ifuatavyo.

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

Tukitatua mlinganyo ($\ref{eqn:substituted}$) kwa $t$ kwa kutumia mbinu za [ODE za Mstari za Homojenia za Daraja la Pili zenye Vigawo Vya Kudumu](/posts/homogeneous-linear-odes-with-constant-coefficients/), kisha tukibadilisha suluhisho tulilopata tena kuwa suluhisho kwa $x$ kwa kutumia kwamba $t = \ln{x}$, tunapata [matokeo yale yale tuliyoona hapo juu](#umbo-la-suluhisho-la-jumla-kulingana-na-ishara-ya-diskriminanti-ya-mlinganyo-saidizi).
