---
title: "Rozwiązanie liniowego równania różniczkowego zwyczajnego 1. rzędu"
description: "Poznaj metodę rozwiązywania liniowych równań różniczkowych zwyczajnych pierwszego rzędu."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Liniowe równanie różniczkowe zwyczajne 1. rzędu

Jeśli równanie różniczkowe zwyczajne 1. rzędu da się algebraicznie sprowadzić do postaci

$$ y'+p(x)y=r(x) \tag{1} $$

to nazywamy je **liniowym (linear)**, a jeśli nie — **nieliniowym (nonlinear)**.

Postać jak w (1) nazywa się **postacią standardową (standard form)** liniowego ODE 1. rzędu. Jeżeli pierwszy wyraz danego liniowego ODE 1. rzędu ma postać $f(x)y'$, to dzieląc obie strony równania przez $f(x)$ można otrzymać postać standardową.

W inżynierii często $r(x)$ nazywa się **wejściem (input)**, a $y(x)$ **wyjściem (output)** lub **odpowiedzią (response)** na wejście (oraz warunek początkowy).

## Jednorodne liniowe równanie różniczkowe

Niech $J$ będzie pewnym przedziałem $a<x<b$, na którym chcemy rozwiązać (1). Jeżeli w (1) na przedziale $J$ zachodzi $r(x)\equiv 0$, to

$$ y'+p(x)y=0 \tag{2}$$

i mówimy, że równanie jest **jednorodne (homogeneous)**. W tym przypadku można użyć [metody rozdzielania zmiennych](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Dla $c=0$ otrzymujemy **rozwiązanie trywialne (trivial solution)** $y(x)=0$.

## Niejednorodne liniowe równanie różniczkowe

Jeżeli na przedziale $J$ zachodzi $r(x)\not\equiv 0$, to równanie nazywamy **niejednorodnym (nonhomogeneous)**. Wiadomo, że niejednorodne liniowe ODE (1) ma czynnik całkujący zależny wyłącznie od $x$. Ten czynnik całkujący $F(x)$ można wyznaczyć z wzoru (11) w sekcji [metody wyznaczania czynnika całkującego](/posts/Exact-Differential-Equation-and-Integrating-Factor/#jak-wyznaczyc-czynnik-calkujacy), albo obliczyć bezpośrednio, jak poniżej.

Mnożąc (1) przez $F(x)$, dostajemy

$$ Fy'+pFy=rF \tag{1*} $$

Jeśli

$$ pF=F' $$

to lewa strona (1*) staje się pochodną $(Fy)'=F'y+Fy'$. Rozdzielając zmienne w równaniu $pF=F'$, mamy $dF/F=p\ dx$, a po scałkowaniu, pisząc $h=\int p\ dx$, otrzymujemy

$$ \log |F|=h=\inf p\ dx $$

$$ F = e^h $$

Podstawiając do (1*), dostajemy

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Całkując,

$$ e^hy=\int e^hr\ dx + c $$
a po podzieleniu przez $e^h$ otrzymujemy poszukiwany wzór na rozwiązanie:

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Przy tym w $h$ stała całkowania nie stanowi problemu.

Ponieważ w (4) jedyną wielkością zależną od zadanego warunku początkowego jest $c$, zapisując (4) jako sumę dwóch składników

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

możemy stwierdzić:

$$ \text{całkowite wyjście}=\text{odpowiedź na wejście }r+\text{odpowiedź na warunek początkowy} \tag{5} $$

## Przykład: obwód RL

Załóżmy, że pewien obwód $RL$ składa się z baterii o SEM $E=48\textrm{V}$, rezystora o oporze $R=11\mathrm{\Omega}$ oraz cewki o indukcyjności $L=0.1\text{H}$, a prąd początkowy wynosi 0. Wyznacz model tego obwodu $RL$ i rozwiąż otrzymane równanie różniczkowe względem prądu $I(t)$.
> **Prawo Ohma (Ohm's law)**  
> Prąd w obwodzie $I$ powoduje spadek napięcia (voltage drop) $RI$ na rezystorze.
{: .prompt-info }

> **Prawo indukcji elektromagnetycznej Faradaya (Faraday's law of electromagnetic induction)**  
> Prąd w obwodzie $I$ powoduje spadek napięcia $LI'=L\ dI/dt$ na cewce.
{: .prompt-info }

> **Prawo napięciowe Kirchhoffa (Kirchhoff's Voltage Law;KVL)**  
> SEM przyłożona do zamkniętego obwodu jest równa sumie spadków napięć na wszystkich pozostałych elementach obwodu.
{: .prompt-info }

### Rozwiązanie

Z powyższych praw wynika, że model obwodu $RL$ ma postać $LI'+RI=E(t)$, a w postaci standardowej:

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

W (4) podstawiamy $x=t, y=I, p=R/L, h=(R/L)t$, aby rozwiązać to liniowe równanie różniczkowe.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Ponieważ $R/L=11/0.1=110$ oraz $E(t)=48$, mamy

$$ I=\frac{48}{11}+ce^{-110t} $$

Z warunku początkowego $I(0)=0$ otrzymujemy $I(0)=E/R+c=0$, czyli $c=-E/R$. Stąd dostajemy następujące rozwiązanie szczególne:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
