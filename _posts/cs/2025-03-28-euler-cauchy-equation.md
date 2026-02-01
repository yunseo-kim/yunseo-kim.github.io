---
title: "Eulerova–Cauchyho rovnice"
description: "Podle znaménka diskriminantu pomocné rovnice ukážeme, jaký tvar má obecné řešení Eulerovy–Cauchyho rovnice v jednotlivých případech."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Eulerova–Cauchyho rovnice: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Pomocná rovnice (auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - Podle znaménka diskriminantu pomocné rovnice $(1-a)^2 - 4b$ lze tvar obecného řešení rozdělit do tří případů (viz tabulka)
>
> | Případ | Řešení pomocné rovnice | Báze řešení Eulerovy–Cauchyho rovnice | Obecné řešení Eulerovy–Cauchyho rovnice |
> | :---: | :---: | :---: | :---: |
> | I | dva různé reálné kořeny<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | dvojnásobný reálný kořen<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | komplexně sdružené kořeny<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [Lineární homogenní ODR druhého řádu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Lineární homogenní ODR druhého řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Eulerův vzorec

## Pomocná rovnice (auxiliary equation)
**Eulerova–Cauchyho rovnice (Euler-Cauchy equation)** je obyčejná diferenciální rovnice tvaru

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

kde $a$ a $b$ jsou dané konstanty a $y(x)$ je hledaná funkce.

Dosadíme-li do rovnice ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

dostaneme

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

tj.

$$ [m(m-1) + am + b]x^m = 0. $$

Odtud získáme pomocnou rovnici

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

a nutná a postačující podmínka, aby $y=x^m$ bylo řešením Eulerovy–Cauchyho rovnice ($\ref{eqn:euler_cauchy_eqn}$), je, aby $m$ bylo řešením pomocné rovnice ($\ref{eqn:auxiliary_eqn}$).

Vyřešíme-li kvadratickou rovnici ($\ref{eqn:auxiliary_eqn}$), dostaneme

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

a z toho plyne, že dvě funkce

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

jsou řešeními rovnice ($\ref{eqn:euler_cauchy_eqn}$).

Stejně jako v článku [Lineární homogenní ODR druhého řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/) můžeme podle znaménka diskriminantu $(1-a)^2 - 4b$ pomocné rovnice ($\ref{eqn:auxiliary_eqn}$) rozlišit tři případy:
- $(1-a)^2 - 4b > 0$: dva různé reálné kořeny
- $(1-a)^2 - 4b = 0$: dvojnásobný reálný kořen
- $(1-a)^2 - 4b < 0$: komplexně sdružené kořeny

## Tvar obecného řešení podle znaménka diskriminantu pomocné rovnice
### I. Dva různé reálné kořeny $m_1$ a $m_2$
V tomto případě je na libovolném intervalu bází řešení rovnice ($\ref{eqn:euler_cauchy_eqn}$)

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

a odpovídající obecné řešení je

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

.

### II. Dvojnásobný reálný kořen $m = \cfrac{1-a}{2}$
Je-li $(1-a)^2 - 4b = 0$, tj. $b=\cfrac{(1-a)^2}{4}$, má kvadratická rovnice ($\ref{eqn:auxiliary_eqn}$) jediné řešení $m = m_1 = m_2 = \cfrac{1-a}{2}$. Jedno řešení tvaru $y=x^m$ je tedy

$$ y_1 = x^{(1-a)/2} $$

a Eulerova–Cauchyho rovnice ($\ref{eqn:euler_cauchy_eqn}$) nabývá tvaru

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Nyní najděme další lineárně nezávislé řešení $y_2$ pomocí metody [snížení řádu](/posts/homogeneous-linear-odes-of-second-order/#snížení-řádu-reduction-of-order).

Položíme-li druhé řešení ve tvaru $y_2=uy_1$, dostaneme

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right). $$

Protože $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$, máme

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x}, $$

a po integraci dostaneme $u = \ln x$.

Tedy $y_2 = uy_1 = y_1 \ln x$ a protože jejich podíl není konstanta, jsou $y_1$ a $y_2$ lineárně nezávislé. Obecné řešení odpovídající bázi $y_1$, $y_2$ je

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

.

### III. Komplexně sdružené kořeny
V tomto případě jsou kořeny pomocné rovnice ($\ref{eqn:auxiliary_eqn}$) rovny $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$. Odpovídající dvě komplexní řešení rovnice ($\ref{eqn:euler_cauchy_eqn}$) lze s využitím $x=e^{\ln x}$ zapsat takto:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Položíme-li $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ a použijeme Eulerův vzorec $e^{it} = \cos{t} + i\sin{t}$, dostaneme

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

a odtud dvě reálná řešení

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

.

Protože jejich podíl $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ není konstanta, jsou tato dvě řešení lineárně nezávislá, a tedy podle [principu superpozice](/posts/homogeneous-linear-odes-of-second-order/#princip-superpozice) tvoří bázi řešení Eulerovy–Cauchyho rovnice ($\ref{eqn:euler_cauchy_eqn}$). Z toho získáme následující reálné obecné řešení:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Je však třeba poznamenat, že případ komplexně sdružených kořenů pomocné rovnice nemá u Eulerovy–Cauchyho rovnice zpravidla příliš velký praktický význam.

## Převedení na lineární homogenní ODR 2. řádu s konstantními koeficienty
Eulerovu–Cauchyho rovnici lze vhodnou substitucí převést na [lineární homogenní ODR druhého řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/).

Provedeme-li substituci $x = e^t$, pak platí

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

a Eulerova–Cauchyho rovnice ($\ref{eqn:euler_cauchy_eqn}$) se změní na homogenní lineární ODR s konstantními koeficienty (v proměnné $t$):

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

Vyřešíme-li rovnici ($\ref{eqn:substituted}$) pro $t$ metodou z článku [lineární homogenní ODR druhého řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/) a pak převedeme řešení zpět na proměnnou $x$ s využitím $t = \ln{x}$, dostaneme [stejný výsledek jako výše](#tvar-obecného-řešení-podle-znaménka-diskriminantu-pomocné-rovnice).
