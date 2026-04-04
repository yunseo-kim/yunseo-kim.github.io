---
title: "ODE za Mstari za Daraja la Pili Zisizo Homojeni"
description: "Makala hii inachunguza umbo la suluhisho la jumla la ODE za mstari za daraja la pili zisizo homojeni kwa kuzingatia uhusiano wake na suluhisho la mlinganyo homojeni unaolingana, na kuonyesha kuwepo kwa suluhisho la jumla pamoja na kutokuwepo kwa suluhisho singula."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Kwa Muhtasari
> - **Suluhisho la jumla** la ODE ya mstari ya daraja la pili isiyo homojeni $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: suluhisho la jumla la ODE homojeni $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, yaani $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: suluhisho maalum la ODE hiyo isiyo homojeni
> - Neno la mwitikio $y_p$ huamuliwa tu na ingizo $r(x)$, na kwa ODE ileile isiyo homojeni, hata kama masharti ya awali yatabadilika, $y_p$ haibadiliki. Tofauti ya suluhisho mbili maalum za ODE isiyo homojeni huwa suluhisho la ODE homojeni unaolingana.
> - **Kuwepo kwa suluhisho la jumla**: kama vipatanishi $p(x)$, $q(x)$ na chaguo za ingizo $r(x)$ vya ODE isiyo homojeni ni endelevu, basi suluhisho la jumla huwa lipo daima
> - **Kutokuwepo kwa suluhisho singula**: suluhisho la jumla linajumuisha suluhisho zote za mlinganyo (yaani, hakuna suluhisho singula)
{: .prompt-info }

## Maarifa ya Awali
- [ODE za Mstari Homojeni za Daraja la Pili](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskian, kuwepo na upekee wa suluhisho](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Suluhisho la jumla na suluhisho maalum la ODE za mstari zisizo homojeni za daraja la pili
Fikiria ODE ya mstari ya daraja la pili isiyo homojeni

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

ambapo $r(x) \not\equiv 0$. Kwenye kipindi wazi $I$, **suluhisho la jumla** la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) lina umbo la jumla ya suluhisho la jumla $y_h = c_1y_1 + c_2y_2$ la ODE homojeni linalolingana na ODE hii isiyo homojeni,

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

na suluhisho maalum $y_p$ la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$),

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Aidha, **suluhisho maalum** la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$ ni suluhisho linalopatikana kutoka kwenye fomula ($\ref{eqn:general_sol}$) kwa kuwapa thamani mahususi vipengele vya kiholela $c_1$ na $c_2$ vya $y_h$.

Yaani, tukiongeza kwenye ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$) ingizo $r(x)$ linalotegemea tu kigeu huru $x$, basi neno linalolingana $y_p$ huongezwa kwenye mwitikio. Neno hili la ziada la mwitikio $y_p$ huamuliwa na ingizo $r(x)$ pekee, bila kutegemea masharti ya awali. Kama tutakavyoona baadaye, tukichukua tofauti ya suluhisho zozote mbili $y_1$ na $y_2$ za mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) (yaani, tofauti ya suluhisho mbili maalum zinazolingana na masharti mawili tofauti ya awali), sehemu ya $y_p$ ambayo haitegemei masharti ya awali hufutika na kubaki tu tofauti ya ${y_h}_1$ na ${y_h}_2$, ambayo kwa [kanuni ya superposition](/posts/homogeneous-linear-odes-of-second-order/#kanuni-ya-superposition) huwa suluhisho la mlinganyo ($\ref{eqn:homogeneous_linear_ode}$).

## Uhusiano kati ya suluhisho za ODE isiyo homojeni na suluhisho za ODE homojeni inayolingana
> **Nadharia 1: Uhusiano kati ya suluhisho za ODE isiyo homojeni ($\ref{eqn:nonhomogeneous_linear_ode}$) na ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Kwenye kipindi wazi $I$, jumla ya suluhisho $y$ la ODE isiyo homojeni ($\ref{eqn:nonhomogeneous_linear_ode}$) na suluhisho $\tilde{y}$ la ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$) ni suluhisho la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$. Hasa, fomula ($\ref{eqn:general_sol}$) ni suluhisho la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$.  
> **(b)** Tofauti ya suluhisho zozote mbili za ODE isiyo homojeni ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$ ni suluhisho la ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$) kwenye kipindi $I$.
{: .prompt-info }

### Uthibitisho
#### (a)
Tuweke upande wa kushoto wa milinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) na ($\ref{eqn:homogeneous_linear_ode}$) kama $L[y]$. Basi kwa suluhisho yoyote $y$ ya ($\ref{eqn:nonhomogeneous_linear_ode}$) na suluhisho yoyote $\tilde{y}$ ya ($\ref{eqn:homogeneous_linear_ode}$) kwenye kipindi $I$, yafuatayo hutimia:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Kwa suluhisho zozote mbili $y$ na $y^\*$ za ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$, yafuatayo hutimia:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## Suluhisho la jumla la ODE isiyo homojeni linajumuisha suluhisho zote
Kwa ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$), [tunajua kuwa suluhisho la jumla linajumuisha suluhisho zote](/posts/wronskian-existence-and-uniqueness-of-solutions/#suluhisho-la-jumla-linajumuisha-suluhisho-zote). Tuonyeshe kuwa jambo hilo hilo linatumika pia kwa ODE isiyo homojeni ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Nadharia 2: Suluhisho la jumla la ODE isiyo homojeni linajumuisha suluhisho zote**  
> Ikiwa vipatanishi $p(x)$, $q(x)$ na chaguo la ingizo $r(x)$ vya mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) ni endelevu kwenye kipindi wazi $I$, basi kila suluhisho la ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$ linaweza kupatikana kwa kuchagua thamani zinazofaa za vipengele vya kiholela $c_1$ na $c_2$ katika $y_h$ ya suluhisho la jumla ($\ref{eqn:general_sol}$) la ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye kipindi $I$.
{: .prompt-info }

### Uthibitisho
Chukua $y^\*$ kuwa suluhisho fulani la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) kwenye $I$, na $x_0$ iwe nukta fulani katika kipindi $I$. Kwa [nadharia ya kuwepo kwa suluhisho la jumla ya ODE homojeni yenye vipatanishi vinavyobadilika na endelevu](/posts/wronskian-existence-and-uniqueness-of-solutions/#kuwepo-kwa-suluhisho-la-jumla), $y_h = c_1y_1 + c_2y_2$ ipo; na kwa **mbinu ya mabadiliko ya vigezo (method of variation of parameters)** ambayo tutaijifunza baadaye, $y_p$ pia ipo. Hivyo suluhisho la jumla ($\ref{eqn:general_sol}$) la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) lipo kwenye kipindi $I$. Sasa, kwa Nadharia [1(b)](#uhusiano-kati-ya-suluhisho-za-ode-isiyo-homojeni-na-suluhisho-za-ode-homojeni-inayolingana) tuliyoithibitisha hapo juu, $Y = y^\* - y_p$ ni suluhisho la ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$) kwenye kipindi $I$, na katika $x_0$

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Kwa [nadharia ya kuwepo na upekee wa suluhisho la tatizo la thamani ya awali](/posts/wronskian-existence-and-uniqueness-of-solutions/#nadharia-ya-kuwepo-na-upekee-wa-suluhisho-la-tatizo-la-thamani-ya-awali), kuna kwa upekee suluhisho maalum $Y$ la ODE homojeni ($\ref{eqn:homogeneous_linear_ode}$) kwenye kipindi $I$ linaloweza kupatikana kwa kuchagua thamani zinazofaa za $c_1$, $c_2$ katika $y_h$ kwa masharti ya awali yaliyo juu. Kwa kuwa $y^\* = Y + y_p$, tumeonyesha kwamba suluhisho yoyote maalum $y^\*$ ya ODE isiyo homojeni ($\ref{eqn:nonhomogeneous_linear_ode}$) inaweza kupatikana kutoka kwenye suluhisho la jumla ($\ref{eqn:general_sol}$). $\blacksquare$
