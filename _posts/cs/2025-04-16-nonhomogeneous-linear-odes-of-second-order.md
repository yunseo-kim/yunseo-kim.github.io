---
title: "Nehomogenní lineární ODR druhého řádu (Nonhomogeneous Linear ODEs of Second Order)"
description: "Ukážeme tvar obecného řešení nehomogenní lineární ODR 2. řádu ve vztahu k příslušné homogenní rovnici a dokážeme existenci obecného řešení i neexistenci singulárního řešení."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Obecné řešení** nehomogenní lineární ODR 2. řádu $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: obecné řešení homogenní ODR $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, tj. $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: partikulární řešení dané nehomogenní ODR
> - Složka odezvy $y_p$ je určena pouze vstupem $r(x)$; pro tutéž nehomogenní ODR se $y_p$ nemění ani při změně počátečních podmínek. Rozdíl dvou partikulárních řešení téže nehomogenní ODR je řešením odpovídající homogenní ODR.
> - **Existence obecného řešení**: jsou-li koeficienty $p(x)$, $q(x)$ a vstupní funkce $r(x)$ spojité, pak obecné řešení vždy existuje
> - **Neexistence singulárního řešení**: obecné řešení obsahuje všechna řešení rovnice (tj. singulární řešení neexistuje)
{: .prompt-info }

## Předpoklady
- [Homogenní lineární ODR druhého řádu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskián, existence a jednoznačnost řešení](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Obecné a partikulární řešení nehomogenní lineární ODR 2. řádu
Uvažujme nehomogenní lineární ODR druhého řádu

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

kde $r(x) \not\equiv 0$. Na otevřeném intervalu $I$ má **obecné řešení** rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) tvar součtu obecného řešení odpovídající homogenní rovnice

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

tj. $y_h = c_1y_1 + c_2y_2$, a partikulárního řešení $y_p$ rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$):

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Dále, **partikulární řešení** rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) na intervalu $I$ je řešení získané z ($\ref{eqn:general_sol}$) dosazením konkrétních hodnot za libovolné konstanty $c_1$ a $c_2$ v $y_h$.

Jinými slovy: pokud k homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$) přidáme vstup $r(x)$ závislý pouze na nezávislé proměnné $x$, pak se v odezvě objeví odpovídající člen $y_p$. Tento přidaný člen odezvy $y_p$ je, nezávisle na počátečních podmínkách, určen výhradně vstupem $r(x)$. Jak uvidíme dále, vezmeme-li rozdíl dvou libovolných řešení $y_1$ a $y_2$ rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) (tj. rozdíl dvou partikulárních řešení pro dvě různé počáteční podmínky), pak se část $y_p$ nezávislá na počátečních podmínkách vyruší a zůstane pouze rozdíl ${y_h}_1$ a ${y_h}_2$. Ten je podle [principu superpozice](/posts/homogeneous-linear-odes-of-second-order/#princip-superpozice) řešením rovnice ($\ref{eqn:homogeneous_linear_ode}$).

## Vztah mezi řešeními nehomogenní ODR a řešeními odpovídající homogenní ODR
> **Věta 1: vztah mezi řešeními nehomogenní ODR ($\ref{eqn:nonhomogeneous_linear_ode}$) a homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Na libovolném otevřeném intervalu $I$ je součet řešení $y$ nehomogenní ODR ($\ref{eqn:nonhomogeneous_linear_ode}$) a řešení $\tilde{y}$ homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$) opět řešením rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) na $I$. Zejména výraz ($\ref{eqn:general_sol}$) je řešením rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) na $I$.  
> **(b)** Rozdíl dvou řešení nehomogenní ODR ($\ref{eqn:nonhomogeneous_linear_ode}$) na $I$ je řešením homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$) na $I$.
{: .prompt-info }

### Důkaz
#### (a)
Levé strany rovnic ($\ref{eqn:nonhomogeneous_linear_ode}$) a ($\ref{eqn:homogeneous_linear_ode}$) označme $L[y]$. Potom pro libovolné řešení $y$ rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) a libovolné řešení $\tilde{y}$ rovnice ($\ref{eqn:homogeneous_linear_ode}$) na intervalu $I$ platí:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Pro libovolná dvě řešení $y$ a $y^\*$ rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) na intervalu $I$ platí:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## Obecné řešení nehomogenní ODR obsahuje všechna řešení
Pro homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$) již [víme, že obecné řešení obsahuje všechna řešení](/posts/wronskian-existence-and-uniqueness-of-solutions/#obecne-reseni-obsahuje-vsechna-reseni). Ukažme, že totéž platí i pro nehomogenní ODR ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Věta 2: obecné řešení nehomogenní ODR obsahuje všechna řešení**  
> Jestliže jsou koeficienty $p(x)$, $q(x)$ a vstupní funkce $r(x)$ rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) spojité na nějakém otevřeném intervalu $I$, pak lze každé řešení rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) na $I$ získat z obecného řešení ($\ref{eqn:general_sol}$) vhodnou volbou hodnot konstant $c_1$ a $c_2$ v části $y_h$.
{: .prompt-info }

### Důkaz
Nechť $y^\*$ je nějaké řešení rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) na $I$ a nechť $x_0$ je nějaký bod z intervalu $I$. Podle [věty o existenci obecného řešení homogenní ODR se spojitými proměnnými koeficienty](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-obecneho-reseni) existuje $y_h = c_1y_1 + c_2y_2$; a protože (jak uvidíme později) existuje také $y_p$ díky **metodě variace parametrů (method of variation of parameters)**, existuje na intervalu $I$ i obecné řešení ($\ref{eqn:general_sol}$) rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$). Nyní podle právě dokázané věty [1(b)](#vztah-mezi-resenimi-nehomogenni-odr-a-resenimi-odpovidajici-homogenni-odr) je $Y = y^\* - y_p$ řešením homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$) na $I$ a v bodě $x_0$ platí

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Podle [věty o existenci a jednoznačnosti řešení počáteční úlohy](/posts/wronskian-existence-and-uniqueness-of-solutions/#veta-o-existenci-a-jedinecnosti-reseni-pocatecni-uloha) existuje na intervalu $I$ právě jedno řešení $Y$ homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$), které lze získat z $y_h$ vhodnou volbou konstant $c_1$, $c_2$ tak, aby splňovalo výše uvedené počáteční podmínky. Protože $y^\* = Y + y_p$, ukázali jsme, že libovolné partikulární řešení $y^\*$ nehomogenní ODR ($\ref{eqn:nonhomogeneous_linear_ode}$) lze získat z obecného řešení ($\ref{eqn:general_sol}$). $\blacksquare$
