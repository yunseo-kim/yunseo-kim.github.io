---
title: "Homogenní lineární ODR druhého řádu s konstantními koeficienty"
description: "Ukážeme, jak se podle znaménka diskriminantu charakteristické rovnice mění tvar obecného řešení homogenní lineární ODR 2. řádu s konstantními koeficienty."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Homogenní lineární ODR druhého řádu s konstantními koeficienty: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Charakteristická rovnice (characteristic equation)**: $\lambda^2 + a\lambda + b = 0$
> - Podle znaménka diskriminantu charakteristické rovnice $a^2 - 4b$ lze tvar obecného řešení rozdělit do tří případů jako v tabulce
>
> | Případ | Kořeny charakteristické rovnice | Báze řešení ODR | Obecné řešení ODR |
> | :---: | :---: | :---: | :---: |
> | I | dva různé reálné kořeny<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | reálný dvojnásobný kořen<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | komplexně sdružené kořeny<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [Bernoulliho rovnice (Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [Lineární homogenní ODR druhého řádu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- Eulerův vzorec

## Charakteristická rovnice (characteristic equation)
Podívejme se na homogenní lineární ODR druhého řádu s konstantními koeficienty $a$ a $b$:

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Rovnice tohoto typu se důležitě uplatňují například v mechanických a elektrických kmitech.

Dříve jsme v článku [Bernoulliho rovnice (Bernoulli Equation)](/posts/Bernoulli-Equation/) našli obecné řešení logistické rovnice; podle něj má lineární ODR prvního řádu s konstantním koeficientem $k$

$$ y^\prime + ky = 0 $$

řešení v podobě exponenciální funkce $y = ce^{-kx}$. (V daném článku jde o případ $A=-k$, $B=0$ v rovnici (4).)

Proto lze i pro rovnici podobného tvaru, tj. ($\ref{eqn:ode_with_constant_coefficients}$), nejprve zkusit řešení ve tvaru

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Samozřejmě jde pouze o domněnku a vůbec není zaručeno, že obecné řešení bude skutečně tohoto tvaru. Nicméně jakmile se nám podaří najít dvě lineárně nezávislá řešení, můžeme — jak bylo rozebráno v článku [Lineární homogenní ODR druhého řádu](/posts/homogeneous-linear-odes-of-second-order/#baze-a-obecne-reseni) — díky [principu superpozice](/posts/homogeneous-linear-odes-of-second-order/#princip-superpozice) zapsat obecné řešení.  
> Jak uvidíme za chvíli, existují i případy, kdy je nutné [hledat řešení jiného tvaru](#ii-realny-dvojnasobny-koren-lambda---cfrac-a2).
{: .prompt-info }

Dosadíme-li výraz ($\ref{eqn:general_sol}$) a jeho derivace

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

do rovnice ($\ref{eqn:ode_with_constant_coefficients}$), dostaneme

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0. $$

Tedy pokud je $\lambda$ kořenem **charakteristické rovnice (characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

pak exponenciální funkce ($\ref{eqn:general_sol}$) je řešením ODR ($\ref{eqn:ode_with_constant_coefficients}$). Kořeny kvadratické rovnice ($\ref{eqn:characteristic_eqn}$) jsou

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

a z toho plyne, že dvě funkce

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

jsou řešeními rovnice ($\ref{eqn:ode_with_constant_coefficients}$).

> Pojmy **charakteristická rovnice (characteristic equation)** a **pomocná rovnice (auxiliary equation)** se často zaměňují; významově jsou však úplně totožné. Můžete použít kterýkoli z nich.
{: .prompt-tip }

Nyní můžeme podle znaménka diskriminantu charakteristické rovnice ($\ref{eqn:characteristic_eqn}$), tj. $a^2 - 4b$, rozlišit tři případy:
- $a^2 - 4b > 0$: dva různé reálné kořeny
- $a^2 - 4b = 0$: reálný dvojnásobný kořen
- $a^2 - 4b < 0$: komplexně sdružené kořeny

## Tvar obecného řešení podle znaménka diskriminantu charakteristické rovnice
### I. Dva různé reálné kořeny $\lambda_1$ a $\lambda_2$
V tomto případě je báze (fundamentální systém) řešení rovnice ($\ref{eqn:ode_with_constant_coefficients}$) na libovolném intervalu dána funkcemi

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x}, $$

a odpovídající obecné řešení je

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Reálný dvojnásobný kořen $\lambda = -\cfrac{a}{2}$
Je-li $a^2 - 4b = 0$, má kvadratická rovnice ($\ref{eqn:characteristic_eqn}$) jediný kořen $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$. Potom z tvaru $y = e^{\lambda x}$ získáme pouze jedno řešení

$$ y_1 = e^{-(a/2)x}. $$

Abychom dostali bázi, musíme najít druhé řešení $y_2$ jiného tvaru, které je na $y_1$ nezávislé.

V takové situaci lze použít postup, který jsme už probírali: [snížení řádu](/posts/homogeneous-linear-odes-of-second-order/#snizeni-radu-reduction-of-order). Druhé řešení položme jako $y_2=uy_1$ a pak

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Dosazením do rovnice ($\ref{eqn:ode_with_constant_coefficients}$) dostaneme

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0. $$

Seskládáním členů podle $u^{\prime\prime}$, $u^\prime$ a $u$ získáme

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0. $$

Protože $y_1$ je řešením rovnice ($\ref{eqn:ode_with_constant_coefficients}$), je výraz v poslední závorce roven $0$, a navíc platí

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1, $$

takže i výraz v první závorce je $0$. Zůstává tedy pouze $u^{\prime\prime}y_1 = 0$, a odtud $u^{\prime\prime}=0$. Dvojnásobnou integrací dostaneme $u = c_1x + c_2$. Protože integrační konstanty $c_1$ a $c_2$ mohou být libovolné, můžeme pro jednoduchost zvolit $c_1=1$, $c_2=0$ a položit $u=x$. Potom $y_2 = uy_1 = xy_1$. Jelikož $y_1$ a $y_2$ jsou lineárně nezávislé, tvoří bázi. Tedy v případě dvojnásobného kořene má báze řešení rovnice ($\ref{eqn:ode_with_constant_coefficients}$) na libovolném intervalu tvar

$$ e^{-ax/2}, \quad xe^{-ax/2}, $$

a odpovídající obecné řešení je

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Komplexně sdružené kořeny $-\cfrac{1}{2}a + i\omega$ a $-\cfrac{1}{2}a - i\omega$
V tomto případě platí $a^2 - 4b < 0$ a $\sqrt{-1} = i$, takže ze vztahů ($\ref{eqn:lambdas}$) máme

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2}, $$

kde zavedeme reálné číslo $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

S touto definicí je řešením charakteristické rovnice ($\ref{eqn:characteristic_eqn}$) dvojice komplexně sdružených kořenů $\lambda = -\cfrac{1}{2}a \pm i\omega$, a odpovídající dvě komplexní řešení rovnice ($\ref{eqn:ode_with_constant_coefficients}$) jsou

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}.
\end{align*} $$

I v tomto případě však můžeme z těchto komplexních řešení získat bázi reálných řešení následovně.

Eulerův vzorec (Euler formula)

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

a rovnice, kterou dostaneme dosazením $-t$ místo $t$,

$$ e^{-it} = \cos t - i\sin t, $$

po sečtení a odečtení po stranách dávají

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

Komplexní exponenciální funkci $e^z$ pro komplexní proměnnou $z = r + it$ (s reálnou částí $r$ a imaginární částí $it$) lze definovat pomocí reálných funkcí $e^r$, $\cos t$ a $\sin t$ takto:

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Položíme-li $r=-\cfrac{1}{2}ax$, $t=\omega x$, můžeme psát

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}), \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x}).
\end{align*} $$

Podle [principu superpozice](/posts/homogeneous-linear-odes-of-second-order/#princip-superpozice) je součet těchto komplexních řešení i jejich násobky konstantou opět řešením. Sečteme-li obě rovnosti po stranách a vynásobíme-li $\cfrac{1}{2}$, získáme první reálné řešení $y_1$:

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Stejně tak odečtením druhé rovnosti od první (po stranách) a vynásobením $\cfrac{1}{2i}$ dostaneme druhé reálné řešení $y_2$:

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Protože $\cfrac{y_1}{y_2} = \cot{\omega x}$ není konstanta, jsou $y_1$ a $y_2$ lineárně nezávislé na každém intervalu, a tedy tvoří bázi reálných řešení rovnice ($\ref{eqn:ode_with_constant_coefficients}$). Odtud dostáváme obecné řešení

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ jsou libovolné konstanty)} \label{eqn:general_sol_3}\tag{13}$$
