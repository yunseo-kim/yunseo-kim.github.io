---
title: "Metoda separace proměnných (Separation of Variables)"
description: "Seznámíme se s metodou separace proměnných a představíme několik souvisejících příkladů."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Metoda separace proměnných (Separation of Variables)

**Separovatelná rovnice (separable equation)**: rovnice, kterou lze pomocí algebraických úprav převést do tvaru $g(y)y'=f(x)$.

Zintegrujeme-li obě strany separovatelné rovnice $g(y)y'=f(x)$ podle $x$, dostaneme

$$ \int g(y)y'dx = \int f(x)dx + c $$

a protože $y'dx=dy$,

$$ \int g(y)dy = \int f(x)dx + c $$

tak lze členy závislé na $x$ a na $y$ oddělit na pravou, resp. levou stranu. Jsou-li $f$ a $g$ spojité funkce, lze uvedené integrály spočítat a získat obecné řešení dané diferenciální rovnice. Tento postup se nazývá **metoda separace proměnných (separation of variables)**.

## Příklad modelování: radiokarbonové datování (Radiocarbon Dating)

Ötzi (Oetzi) je neolitická mumie nalezená v Ötztalských Alpách (Oetztal) v roce 11991 [holocénního kalendáře](https://en.wikipedia.org/wiki/Holocene_calendar). Pokud je poměr uhlíku-14 vůči uhlíku-12 v této mumii 52,5 % oproti živému organismu, kdy asi Ötzi žil a zemřel?
> V atmosféře i v živých organismech je poměr radioaktivního uhlíku-14 vůči uhlíku-12 konstantní. Jakmile organismus zemře, přestane docházet k příjmu uhlíku-14 dýcháním a potravou, ale rozpad uhlíku-14 pokračuje, takže jeho podíl klesá. Proto lze stáří fosilie odhadnout porovnáním jejího podílu radioaktivního uhlíku s podílem radioaktivního uhlíku v atmosféře. Poločas rozpadu uhlíku-14 je 5715 let.
{: .prompt-info }

### Řešení

Provedeme separaci proměnných a integraci pro obyčejnou diferenciální rovnici $y'=ky$:

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Konstantu $k$ určíme pomocí poločasu rozpadu $H=5715$.

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Nakonec dosadíme poměr 52,5 % a určíme čas úmrtí Ötziho (Oetzi), tj. $t$:

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{přibližně před 5310 lety, odhad úmrtí kolem roku 6680 holocénního kalendáře}. $$

## Příklad modelování: úloha o mísení

Zpočátku je v nádrži 1000 L vody, ve které je rozpuštěno 10 kg soli. Slaná voda přitéká rychlostí 10 L za minutu a obsahuje 0,2 kg soli na litr. Směs v nádrži je dobře promíchána a zůstává homogenní; zároveň odtéká slaná voda rychlostí 10 L za minutu. Určete množství soli $y(t)$ v nádrži v čase $t$.

### 1. Sestavení modelu

$$ y'=\text{rate in} - \text{rate out}. $$

Přítok soli je 2 kg za minutu. Odtok slané vody za minutu je 0,01 celkového objemu směsi, takže odtok soli je $0.01\,y(t)$ za minutu. Model je tedy obyčejná diferenciální rovnice

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Řešení modelu

Dříve sestavená ODR je separovatelná. Provedeme separaci proměnných, integraci a na obě strany použijeme exponenciálu.

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Na začátku je v nádrži 10 kg soli, takže počáteční podmínka je $y(0)=10$. Dosazením $y=10,\ t=0$ do výrazu výše dostaneme $10-200=ce^0=c$, tedy $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Jinými slovy: v dané situaci se množství soli v nádrži exponenciálně blíží k 200 kg a konverguje.

## Příklad modelování: Newtonův zákon ochlazování (Newton's Law of Cooling)

V zimě se denní teplota v jedné kancelářské budově udržuje na 20 ℃. Topení se vypíná ve 22:00 a znovu zapíná v 6:00 ráno. Jednoho dne ve 2:00 ráno byla vnitřní teplota budovy 17,4 ℃. Venkovní teplota byla ve 22:00 10 ℃ a do 6:00 ráno klesla na 4 ℃. Jaká byla vnitřní teplota budovy v 6:00, když se topení zapnulo?

> **Newtonův zákon ochlazování (Newton's law of cooling)**  
> Rychlost změny teploty $T$ tělesa v čase je úměrná teplotnímu rozdílu mezi tělesem a jeho okolím.
{: .prompt-info }

### 1. Sestavení modelu

Nechť $T(t)$ je vnitřní teplota budovy a $T_A$ je venkovní teplota. Podle Newtonova zákona ochlazování platí

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Obecné řešení

Víme pouze, že $T_A$ se mění mezi 10 ℃ a 4 ℃, ale neznáme jeho přesnou hodnotu, takže předchozí rovnici nelze přímo vyřešit. V takové situaci může pomoci *zjednodušit zadání na snazší problém a zkusit ho vyřešit*. Průměr známých dvou hodnot je 7 ℃, proto předpokládejme, že neznámá funkce $T_A$ je konstantní funkce $T_A=7$. I když to nebude přesné, můžeme očekávat, že dostaneme přibližnou hodnotu hledané vnitřní teploty $T$ v 6:00.

Pro konstantu $T_A=7$ je předchozí ODR separovatelná. Separací proměnných, integrací a použitím exponenciály získáme obecné řešení.

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Partikulární řešení

Zvolme 22:00 jako $t=0$; pak je počáteční podmínka $T(0)=20$. Označme získané partikulární řešení jako $T_p$. Dosazením dostaneme

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Určení $k$

Ve 2:00 ráno byla vnitřní teplota 17,4 ℃, tedy $T(4)=17.4$. Algebraicky určíme $k$ a dosadíme jej do $T_p(t)$:

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Odpověď a interpretace

V 6:00 je $t=8$, takže

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[℃]}. $$

## Příklad modelování: Torricelliho věta (Torricelli's Theorem)

Nádrž má průměr 2 m, otvor má průměr 1 cm a počáteční výška vody při otevření otvoru je 2,25 m. Určete výšku hladiny vody v nádrži v libovolném čase a dobu, za kterou se nádrž vyprázdní.

> **Torricelliho věta (Torricelli's theorem)**  
> Rychlost vytékající vody pod vlivem gravitace je
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: výška vody nad otvorem v čase $t$  
> $g=980\text{cm/s²}$: tíhové zrychlení na povrchu Země
{: .prompt-info }

### 1. Sestavení modelu

Objem, který odteče během krátkého času $\Delta t$, je

$$ \Delta V = Av\Delta t \qquad (A: \text{plocha otvoru})$$

Tento objem $\Delta V$ se musí rovnat změně objemu vody v nádrži $\Delta V^*$. Dále platí

$$ \Delta V^* = -B\Delta h \qquad (B: \text{plocha průřezu nádrže}) $$

kde $\Delta h(>0)$ je pokles výšky hladiny $h(t)$. Položíme-li $\Delta V=\Delta V^*$, dostaneme

$$ -B\Delta h = Av\Delta t $$

Nyní vyjádříme $v$ pomocí Torricelliho věty a necháme-li $\Delta t$ směřovat k nule, získáme model ve tvaru diferenciální rovnice 1. řádu:

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Obecné řešení

Tato ODR je separovatelná. Separací proměnných a integrací dostaneme

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Vydělíme-li obě strany dvěma a umocníme na druhou, získáme $h=(c-13.28At/B)^2$. Po dosazení $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$ dostaneme obecné řešení

$$ h(t)=(c-0.000332t)^2 $$

### 3. Partikulární řešení

Počáteční podmínka je $h(0)=225\text{cm}$. Dosazením $t=0$ a $h=225$ do obecného řešení dostaneme $c^2=225, c=15.00$, a tedy partikulární řešení

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Doba do vyprázdnění nádrže

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Převod do separovatelného tvaru (separable form)

Někdy lze i neseparovatelnou obyčejnou diferenciální rovnici převést na separovatelnou pomocí transformace, ve které zavedeme novou neznámou funkci v závislosti na $y$.

$$ y'=f\left(\frac {y}{x}\right). $$

Při řešení takové ODR položíme $y/x=u$. Pak

$$ y=ux,\quad y'=u'x+u $$

a po dosazení do $y'=f(y/x)$ dostaneme $u'x=f(u)-u$. Jestliže $f(u)-u\neq0$, lze rovnici separovat jako

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$
