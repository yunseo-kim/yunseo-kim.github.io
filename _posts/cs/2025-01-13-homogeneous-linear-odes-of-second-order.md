---
title: "Lineární homogenní ODR druhého řádu (Homogeneous Linear ODEs of Second Order)"
description: "Seznámíme se s definicí a vlastnostmi lineárních ODR 2. řádu; zejména porozumíme principu superpozice pro homogenní lineární ODR a z něj plynoucímu pojmu báze (fundamentálního systému)."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Standardní tvar** lineární ODR 2. řádu: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **koeficienty (coefficients)**: funkce $p$, $q$
>   - **vstup (input)**: $r(x)$
>   - **výstup (output)** nebo **odezva (response)**: $y(x)$
> - Homogenní vs. nehomogenní
>   - **homogenní (homogeneous)**: ve standardním tvaru $r(x)\equiv0$
>   - **nehomogenní (nonhomogeneous)**: ve standardním tvaru $r(x)\not\equiv 0$
> - **Princip superpozice (superposition principle)**: pro <u>homogenní</u> lineární ODR $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ je na otevřeném intervalu $I$ libovolná lineární kombinace dvou řešení opět řešením dané rovnice. Tj. součet libovolných řešení dané homogenní lineární ODR a jejich násobky konstantou jsou také řešeními této rovnice.
> - **Báze (basis)** neboli **fundamentální systém (fundamental system)**: dvojice $(y_1, y_2)$ řešení homogenní lineární ODR, která jsou na intervalu $I$ lineárně nezávislá
> - **Snížení řádu (reduction of order)**: pro homogenní ODR 2. řádu platí, že pokud nalezneme jedno řešení, lze z něj získat druhé, s ním lineárně nezávislé řešení (tj. bázi) vyřešením ODR 1. řádu; tento postup se nazývá snížení řádu
> - Aplikace snížení řádu: obecnou ODR 2. řádu $F(x, y, y^\prime, y^{\prime\prime})=0$ lze (ať je lineární či nelineární) v následujících případech snížit na 1. řád pomocí snížení řádu
>   - když se $y$ explicitně nevyskytuje
>   - když se $x$ explicitně nevyskytuje
>   - když je rovnice homogenní lineární a jedno řešení již známe
{: .prompt-info }

## Prerequisites
- [Základní pojmy modelování (Modeling)](/posts/Basic-Concepts-of-Modeling/)
- [Metoda separace proměnných (Separation of Variables)](/posts/Separation-of-Variables/)
- [Řešení lineárních ODR prvního řádu](/posts/Solution-of-First-Order-Linear-ODE/)

## Lineární ODR druhého řádu
ODR druhého řádu se nazývá **lineární (linear)**, lze-li ji zapsat ve tvaru

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

a v opačném případě se nazývá **nelineární (nonlinear)**.

Jsou-li $p$, $q$, $r$ funkcemi libovolného $x$, je tato rovnice lineární vzhledem k $y$ a jeho derivacím.

Tvar jako v rovnici ($\ref{eqn:standard_form}$) se nazývá **standardní tvar (standard form)** lineární ODR 2. řádu. Pokud je první člen zadané lineární ODR 2. řádu tvaru $f(x)y^{\prime\prime}$, lze standardní tvar získat vydělením obou stran rovnice funkcí $f(x)$.

Funkce $p$, $q$ se nazývají **koeficienty (coefficients)**, $r(x)$ se nazývá **vstup (input)** a $y(x)$ se nazývá **výstup (output)**, případně **odezva (response)** na vstup a počáteční podmínky.

### Homogenní lineární ODR druhého řádu
Nechť $J$ je interval $a<x<b$, na němž chceme řešit rovnici ($\ref{eqn:standard_form}$). Pokud na intervalu $J$ platí $r(x)\equiv 0$, dostaneme

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

a tuto rovnici nazýváme **homogenní (homogeneous)**.

## Nehomogenní lineární ODR
V případě, že na intervalu $J$ platí $r(x)\not\equiv 0$, nazýváme rovnici **nehomogenní (nonhomogeneous)**.

## Princip superpozice

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ jsou libovolné konstanty)}\tag{3}$$

Funkce tohoto tvaru se nazývá **lineární kombinace (linear combination)** funkcí $y_1$ a $y_2$.

V tom případě platí následující tvrzení.

> **Princip superpozice (superposition principle)**  
> Pro homogenní lineární ODR ($\ref{eqn:homogeneous_linear_ode}$) platí, že na otevřeném intervalu $I$ je libovolná lineární kombinace dvou řešení opět řešením rovnice ($\ref{eqn:homogeneous_linear_ode}$). Jinými slovy: součet libovolných řešení dané homogenní lineární ODR a jejich násobky konstantou jsou rovněž řešeními této rovnice.
{: .prompt-info }

### Důkaz
Nechť $y_1$ a $y_2$ jsou na intervalu $I$ řešeními rovnice ($\ref{eqn:homogeneous_linear_ode}$). Dosadíme-li $y=c_1y_1+c_2y_2$ do ($\ref{eqn:homogeneous_linear_ode}$), dostaneme

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

což je identita. Tedy $y$ je na intervalu $I$ řešením rovnice ($\ref{eqn:homogeneous_linear_ode}$). $\blacksquare$

> Upozorňujeme, že princip superpozice platí pouze pro homogenní lineární ODR; pro nehomogenní lineární ODR ani pro nelineární ODR neplatí.
{: .prompt-warning }

## Báze a obecné řešení
### Připomenutí klíčových pojmů pro ODR prvního řádu
Jak jsme viděli dříve v článku [Základní pojmy modelování (Modeling)](/posts/Basic-Concepts-of-Modeling/), počáteční úloha (Initial Value Problem) pro ODR prvního řádu se skládá z ODR a počáteční podmínky (initial condition) $y(x_0)=y_0$. Počáteční podmínka je potřebná k určení libovolné konstanty $c$ v obecném řešení dané ODR; takto určené řešení se nazývá partikulární řešení. Nyní tyto pojmy rozšíříme na ODR druhého řádu.

### Počáteční úloha a počáteční podmínky
**Počáteční úloha (initial value problem)** pro homogenní ODR druhého řádu ($\ref{eqn:homogeneous_linear_ode}$) se skládá ze zadané ODR ($\ref{eqn:homogeneous_linear_ode}$) a dvou **počátečních podmínek (initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

které jsou potřebné k určení dvou libovolných konstant $c_1$ a $c_2$ v **obecném řešení (general solution)**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

.

### Lineární nezávislost a lineární závislost
Na chvíli se zastavme u pojmů lineární nezávislosti a lineární závislosti. Pro definici báze je budeme potřebovat.

Řekneme, že dvě funkce $y_1$ a $y_2$ jsou na intervalu $I$ **lineárně nezávislé (linearly independent)**, jestliže pro všechna $x\in I$ platí

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ a }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

a v opačném případě jsou $y_1$ a $y_2$ na intervalu $I$ **lineárně závislé (linearly dependent)**.

Pokud jsou $y_1$ a $y_2$ lineárně závislé (tj. výrok ($\ref{eqn:linearly_independent}$) není pravdivý), pak při $k_1 \neq 0$ nebo $k_2 \neq 0$ můžeme vydělit rovnici ($\ref{eqn:linearly_independent}$) jednou ze stran a dostaneme

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{nebo} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

takže je vidět, že $y_1$ a $y_2$ jsou navzájem proporcionální.

### Báze, obecné řešení, partikulární řešení
Vraťme se zpět: aby byl výraz ($\ref{eqn:general_sol}$) obecným řešením, musí být $y_1$ a $y_2$ jednak řešeními rovnice ($\ref{eqn:homogeneous_linear_ode}$), a zároveň na intervalu $I$ nesmějí být navzájem proporcionální, tj. musí být lineárně nezávislé (linearly independent). Dvojice (pair) $(y_1, y_2)$ řešení rovnice ($\ref{eqn:homogeneous_linear_ode}$), která jsou na intervalu $I$ lineárně nezávislá, se nazývá **báze (basis)** řešení rovnice ($\ref{eqn:homogeneous_linear_ode}$) na intervalu $I$, případně **fundamentální systém (fundamental system)**.

Využitím počátečních podmínek určíme dvě konstanty $c_1$ a $c_2$ v obecném řešení ($\ref{eqn:general_sol}$), čímž získáme jediné řešení, které prochází bodem $(x_0, K_0)$ a jehož směrnice tečny v tomto bodě je $K_1$. Tomuto řešení říkáme **partikulární řešení (particular solution)** ODR ($\ref{eqn:homogeneous_linear_ode}$).

Je-li rovnice ($\ref{eqn:homogeneous_linear_ode}$) na otevřeném intervalu $I$ spojitá, pak nutně má obecné řešení a toto obecné řešení zahrnuje všechna možná partikulární řešení. Jinými slovy, v tomto případě rovnice ($\ref{eqn:homogeneous_linear_ode}$) nemá singulární řešení (singular solution), která by nebyla získatelná z obecného řešení.

## Snížení řádu (reduction of order)
Pro homogenní ODR druhého řádu platí, že pokud se nám podaří najít jedno řešení, lze druhé řešení, lineárně nezávislé na prvním (tj. bázi), nalézt vyřešením ODR prvního řádu následujícím postupem. Tento postup se nazývá **snížení řádu (reduction of order)**.

Pro <u>homogenní lineární ODR 2. řádu ve standardním tvaru</u> s druhou derivací $y^{\prime\prime}$ (nikoli $f(x)y^{\prime\prime}$)

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

předpokládejme, že na otevřeném intervalu $I$ známe jedno řešení $y_1$ této rovnice.

Druhé hledané řešení zvolme ve tvaru $y_2 = uy_1$ a položme

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Dosazením do rovnice dostaneme

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Sečtením členů u $u^{\prime\prime}$, $u^{\prime}$ a $u$ získáme

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Protože $y_1$ je řešením zadané rovnice, je výraz v poslední závorce roven $0$, takže člen s $u$ vypadne a zůstane ODR pro $u^{\prime}$ a $u^{\prime\prime}$. Vydělíme-li tuto zbylou rovnici $y_1$ a položíme-li $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, získáme následující ODR prvního řádu:

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Provedeme [separaci proměnných](/posts/Separation-of-Variables/) a integrujeme:

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

Po umocnění obou stran exponenciálou nakonec dostaneme

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Jelikož jsme položili $U=u^{\prime}$, platí $u=\int U dx$, takže hledané druhé řešení $y_2$ je

$$ y_2 = uy_1 = y_1 \int U dx $$

Protože $\cfrac{y_2}{y_1} = u = \int U dx$ nemůže být (za předpokladu $U>0$) konstanta, jsou $y_1$ a $y_2$ lineárně nezávislá řešení a tvoří bázi řešení.

### Aplikace snížení řádu
Obecnou ODR druhého řádu $F(x, y, y^\prime, y^{\prime\prime})=0$ lze bez ohledu na to, zda je lineární nebo nelineární, snížit pomocí snížení řádu na rovnici prvního řádu v případech, kdy se $y$ explicitně nevyskytuje, kdy se $x$ explicitně nevyskytuje, anebo kdy (jak jsme viděli výše) jde o homogenní lineární rovnici a jedno řešení již známe.

#### Když se $y$ explicitně nevyskytuje
V rovnici $F(x, y^\prime, y^{\prime\prime})=0$ položíme $z=y^{\prime}$; tím ji lze snížit na ODR prvního řádu pro $z$, tj. $F(x, z, z^{\prime})$.

#### Když se $x$ explicitně nevyskytuje
V rovnici $F(y, y^\prime, y^{\prime\prime})=0$ položíme $z=y^{\prime}$. Potom

$$ y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z $$

a tedy ji lze snížit na ODR prvního řádu pro $z$, v níž $y$ hraje roli nezávislé proměnné místo $x$, tj. na rovnici tvaru $F(y,z,z^\prime)$.
