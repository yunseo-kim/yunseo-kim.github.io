---
title: "Wronskián (Wronskian), existence a jednoznačnost řešení"
description: "Pro homogenní lineární ODR 2. řádu se spojitými proměnnými koeficienty odvodíme větu o existenci a jednoznačnosti, použijeme Wronskián k určení (ne)závislosti řešení a ukážeme, že neexistují singulární řešení."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Pro homogenní lineární ODR 2. řádu s libovolnými spojitými proměnnými koeficienty $p$ a $q$ na intervalu $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> a s počátečními podmínkami
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> platí následující 4 tvrzení.
> 1. **Věta o existenci a jednoznačnosti řešení počáteční úlohy**: počáteční úloha daná rovnicí a počátečními podmínkami má na intervalu $I$ jediné řešení $y(x)$.
> 2. **Rozhodování lineární závislosti/nezávislosti pomocí Wronskiánu (Wronskian)**: pro dvě řešení $y_1$ a $y_2$ platí: existuje-li v intervalu $I$ bod $x_0$ takový, že **Wronskián (Wronskian)** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ nabývá hodnoty $0$, pak jsou řešení lineárně závislá. A pokud existuje $x_1\in I$ takové, že $W\neq 0$, pak jsou lineárně nezávislá.
> 3. **Existence obecného řešení**: daná rovnice má na intervalu $I$ obecné řešení.
> 4. **Neexistence singulárního řešení**: toto obecné řešení zahrnuje všechna řešení rovnice (tj. neexistuje singulární řešení).
{: .prompt-info }

## Prerequisites
- [Řešení lineárních ODR prvního řádu](/posts/Solution-of-First-Order-Linear-ODE/)
- [Lineární homogenní ODR druhého řádu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogenní lineární ODR druhého řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Eulerova–Cauchyho rovnice](/posts/euler-cauchy-equation/)
- inverzní matice a singulární matice, determinant

## Homogenní lineární ODR se spojitými proměnnými koeficienty
Dříve jsme si určili obecné řešení pro [homogenní lineární ODR druhého řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/) a pro [Eulerovu–Cauchyho rovnici](/posts/euler-cauchy-equation/).
V tomto článku rozšíříme diskusi na obecnější případ: homogenní lineární ODR druhého řádu s libovolnými spojitými **proměnnými koeficienty (variable coefficients)** $p$ a $q$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

a budeme zkoumat existenci a tvar jejího obecného řešení. Dále se podíváme i na jednoznačnost [počáteční úlohy](/posts/homogeneous-linear-odes-of-second-order/#pocatecni-uloha-a-pocatecni-podminky) složené z ODR ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a následujících dvou počátečních podmínek

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Ještě předem: klíčovým závěrem je, že <u>lineární</u> ODR se spojitými koeficienty nemá *singulární řešení (singular solution)* (tj. řešení, které nelze získat z obecného řešení).

## Věta o existenci a jednoznačnosti řešení počáteční úlohy
> **Věta o existenci a jednoznačnosti řešení počáteční úlohy (Existence and Uniqueness Theorem for Initial Value Problems)**  
> Jsou-li $p(x)$ a $q(x)$ spojité funkce na nějakém otevřeném intervalu $I$ a $x_0\in I$, pak počáteční úloha daná rovnicemi ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a ($\ref{eqn:initial_conditions}$) má na intervalu $I$ jediné řešení $y(x)$.
{: .prompt-info }

Důkaz existence zde řešit nebudeme a podíváme se pouze na důkaz jednoznačnosti. Obvykle je dokazování jednoznačnosti jednodušší než dokazování existence.  
Pokud vás důkaz nezajímá, můžete tuto část přeskočit a přejít na [Lineární závislost a nezávislost řešení](#linearni-zavislost-a-nezavislost-reseni).

### Důkaz jednoznačnosti
Předpokládejme, že počáteční úloha složená z ODR ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a počátečních podmínek ($\ref{eqn:initial_conditions}$) má na intervalu $I$ dvě řešení $y_1(x)$ a $y_2(x)$. Uvažujme jejich rozdíl

$$ y(x) = y_1(x) - y_2(x) $$

Pokud ukážeme, že na intervalu $I$ je identicky roven nule, tj. že $y(x)\equiv 0$ na $I$, pak z toho plyne $y_1 \equiv y_2$ na $I$, což znamená jednoznačnost.

Protože rovnice ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) je homogenní lineární ODR, je její řešení i libovolná lineární kombinace řešení; tedy $y$ je na $I$ rovněž řešením. Jelikož $y_1$ a $y_2$ splňují stejné počáteční podmínky ($\ref{eqn:initial_conditions}$), platí pro $y$ podmínky

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Nyní uvažujme funkci

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

a její derivaci

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

Z ODR dostaneme

$$ y^{\prime\prime} = -py^{\prime} - qy $$

a po dosazení do výrazu pro $z^{\prime}$ získáme

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Protože $y$ a $y^{\prime}$ jsou reálné, platí

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

Z toho a z definice $z$ plyne dvojice nerovností

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Odtud vidíme, že $\|2yy^{\prime}\|\leq z$, a tedy pro poslední člen v ($\ref{eqn:z_prime}$) platí

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Spolu s $-p \leq \|p\|$ a použitím ($\ref{eqn:inequalities}$a) na člen $2yy^{\prime}$ v ($\ref{eqn:z_prime}$) dostáváme

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Protože ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, plyne

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Označme funkci v závorce jako $h = 1 + 2\|p\| + \|q\|$. Potom

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Stejným postupem z ($\ref{eqn:z_prime}$) a ($\ref{eqn:inequalities}$) získáme

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Nerovnosti ($\ref{eqn:inequality_6a}$) a ($\ref{eqn:inequality_6b}$) jsou ekvivalentní s

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

a [integrační faktor](/posts/Solution-of-First-Order-Linear-ODE/#nehomogenni-linearni-odr) pro levou stranu těchto nerovností je

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{a} \qquad F_2 = e^{\int h(x)\ dx} $$

Protože $h$ je spojitá, neurčitý integrál $\int h(x)\ dx$ existuje; navíc $F_1$ a $F_2$ jsou kladné, takže z ($\ref{eqn:inequalities_7}$) plyne

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

To znamená: na intervalu $I$ funkce $F_1 z$ neroste a $F_2 z neklesá. Jelikož z ($\ref{eqn:initial_conditions_*}$) máme $z(x_0)=0$, dostáváme

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Nakonec po vydělení obou stran kladnými $F_1$ a $F_2$ dostaneme

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

tedy

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

a proto

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Lineární závislost a nezávislost řešení
Připomeňme si stručně obsah z článku [Lineární homogenní ODR druhého řádu](/posts/homogeneous-linear-odes-of-second-order/#baze-a-obecne-reseni). Obecné řešení na otevřeném intervalu $I$ je vytvořeno z **báze (basis)** $y_1$, $y_2$, tj. z dvojice lineárně nezávislých řešení. Říci, že $y_1$ a $y_2$ jsou na intervalu $I$ **lineárně nezávislé (linearly independent)**, znamená: pro všechna $x$ v daném intervalu platí

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ a }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Pokud tomu tak není a existují konstanty $k_1$, $k_2$ (alespoň jedna z nich nenulová), pro něž platí $k_1y_1(x) + k_2y_2(x) = 0$, pak jsou $y_1$ a $y_2$ na intervalu $I$ **lineárně závislé (linearly dependent)**. V takovém případě pro všechna $x\in I$ platí

$$ \text{(a) } y_1 = ky_2 \quad \text{nebo} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

tedy $y_1$ a $y_2$ jsou navzájem proporcionální.

Nyní si ukážeme kritérium pro rozhodnutí lineární (ne)závislosti.

> **Rozhodování lineární závislosti/nezávislosti pomocí Wronskiánu (Wronskian)**  
> **i.** Má-li ODR ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na otevřeném intervalu $I$ spojité koeficienty $p(x)$ a $q(x)$, pak nutnou a postačující podmínkou pro to, aby dvě řešení $y_1$ a $y_2$ byly na $I$ lineárně závislé, je, aby jejich *Wronskiho determinant (Wronski determinant)*, zkráceně **Wronskián (Wronskian)**,
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> byl v nějakém bodě $x_0\in I$ roven nule.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ a } y_2 \text{ jsou lineárně závislá} $$
>
> **ii.** Pokud v nějakém bodě $x=x_0$ z intervalu $I$ platí $W=0$, pak platí $W=0$ pro všechna $x\in I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> Jinými slovy: existuje-li v $I$ bod $x_1$ takový, že $W\neq 0$, pak jsou $y_1$, $y_2$ na $I$ lineárně nezávislá.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ a } y_2 \text{ jsou lineárně nezávislá}
> \end{align*}$$
>
{: .prompt-info }

> Wronskián byl poprvé zaveden polským matematikem Józefem Mariou Hoene-Wrońským (Józef Maria Hoene-Wroński) a po jeho smrti mu v roce 11882 HE dal dnešní název skotský matematik Sir Thomas Muir (Sir Thomas Muir).
{: .prompt-tip }

### Důkaz
#### i. (a)
Nechť jsou $y_1$ a $y_2$ na intervalu $I$ lineárně závislá. Pak na $I$ platí buď ($\ref{eqn:linearly_dependent}$a), nebo ($\ref{eqn:linearly_dependent}$b). Platí-li ($\ref{eqn:linearly_dependent}$a), potom

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

a stejně tak, platí-li ($\ref{eqn:linearly_dependent}$b),

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Tedy ověříme, že <u>pro všechna $x$ na intervalu $I$</u> platí $W(y_1,y_2)=0$.

#### i. (b)
Naopak předpokládejme, že pro nějaké $x=x_0$ platí $W(y_1,y_2)=0$. Ukážeme, že pak jsou $y_1$ a $y_2$ na intervalu $I$ lineárně závislá. Uvažujme soustavu lineárních rovnic pro neznámé $k_1$, $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Tu lze zapsat jako vektorovou rovnici

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

Koeficientní matice je

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

a její determinant je právě $W(y_1(x_0), y_2(x_0))$. Protože $\det(A)=W=0$, matice $A$ nemá **inverzní matici (inverse matrix)**, je to tedy **singulární matice (singular matrix)**, a soustava ($\ref{eqn:linear_system}$) má netriviální řešení $(c_1,c_2)\neq(0,0)$, tj. alespoň jedna z konstant $c_1$, $c_2$ je nenulová.

Zaveďme funkci

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Protože rovnice ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) je homogenní lineární, plyne z [principu superpozice](/posts/homogeneous-linear-odes-of-second-order/#princip-superpozice), že tato funkce je na $I$ řešením ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$). Ze soustavy ($\ref{eqn:linear_system}$) vidíme, že toto řešení splňuje počáteční podmínky $y(x_0)=0$, $y^{\prime}(x_0)=0$.

Zároveň existuje triviální řešení $y^\*\equiv 0$, které splňuje stejné počáteční podmínky $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Protože koeficienty $p$ a $q$ jsou spojité, z [věty o existenci a jednoznačnosti řešení počáteční úlohy](#veta-o-existenci-a-jednoznacnosti-reseni-pocatecni-ulohy) plyne jednoznačnost, a tedy $y\equiv y^\*$. Jinými slovy, na $I$ platí

$$ c_1y_1 + c_2y_2 \equiv 0 $$

A jelikož alespoň jedna z konstant $c_1$, $c_2$ je nenulová, neplatí ($\ref{eqn:linearly_independent}$), což znamená, že $y_1$, $y_2$ jsou na intervalu $I$ lineárně závislá.

#### ii.
Pokud v nějakém bodě $x_0\in I$ platí $W(x_0)=0$, pak podle [i.(b)](#i-b) jsou $y_1$, $y_2$ na $I$ lineárně závislá, a tedy podle [i.(a)](#i-a) platí $W\equiv 0$. Proto existuje-li alespoň jeden bod $x_1\in I$ takový, že $W(x_1)\neq 0$, musí být $y_1$ a $y_2$ lineárně nezávislá. $\blacksquare$

## Obecné řešení zahrnuje všechna řešení
### Existence obecného řešení
> Jsou-li $p(x)$ a $q(x)$ na otevřeném intervalu $I$ spojité, pak má rovnice ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na intervalu $I$ obecné řešení.
{: .prompt-info }

#### Důkaz
Z [věty o existenci a jednoznačnosti řešení počáteční úlohy](#veta-o-existenci-a-jednoznacnosti-reseni-pocatecni-ulohy) plyne, že ODR ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) má na $I$ řešení $y_1(x)$ splňující počáteční podmínky

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

a také řešení $y_2(x)$ splňující na $I$ počáteční podmínky

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

Wronskián těchto dvou řešení v bodě $x=x_0$ nabývá nenulové hodnoty

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

a proto jsou podle kritéria z části [Lineární závislost a nezávislost řešení](#linearni-zavislost-a-nezavislost-reseni) funkce $y_1$ a $y_2$ na $I$ lineárně nezávislé. Tedy tvoří bázi řešení na $I$ a obecné řešení tvaru $y=c_1y_1+c_2y_2$ (pro libovolné konstanty $c_1$, $c_2$) na $I$ nutně existuje. $\blacksquare$

### Neexistence singulárního řešení
> Má-li ODR ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na nějakém otevřeném intervalu $I$ spojité koeficienty $p(x)$ a $q(x)$, pak lze každé její řešení $y=Y(x)$ na $I$ zapsat ve tvaru
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> kde $y_1$, $y_2$ tvoří bázi řešení rovnice ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na $I$ a $C_1$, $C_2$ jsou vhodné konstanty.  
> Jinými slovy: rovnice ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) nemá **singulární řešení (singular solution)**, tj. řešení, které by nešlo získat z obecného řešení.
{: .prompt-info }

#### Důkaz
Nechť $y=Y(x)$ je nějaké řešení rovnice ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na intervalu $I$. Z [věty o existenci obecného řešení](#existence-obecneho-reseni) víme, že tato ODR má na $I$ obecné řešení

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Nyní musíme ukázat, že pro libovolné $Y(x)$ existují konstanty $c_1$, $c_2$ tak, aby na $I$ platilo $y(x)=Y(x)$. Nejprve ukážeme, že pro libovolně zvolené $x_0\in I$ lze najít $c_1$, $c_2$ tak, aby platilo $y(x_0)=Y(x_0)$ a $y^{\prime}(x_0)=Y^{\prime}(x_0)$. Z ($\ref{eqn:general_solution}$) plyne

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

Protože $y_1$, $y_2$ tvoří bázi, je determinant koeficientní matice $W(y_1(x_0),y_2(x_0))\neq 0$, takže soustavu ($\ref{eqn:vector_equation_2}$) lze vyřešit pro $c_1$, $c_2$. Označme její řešení jako $(c_1,c_2)=(C_1,C_2)$. Dosazením do ($\ref{eqn:general_solution}$) dostaneme partikulární řešení

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Protože $C_1$, $C_2$ jsou řešením ($\ref{eqn:vector_equation_2}$), platí

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Z jednoznačnosti v [větě o existenci a jednoznačnosti řešení počáteční úlohy](#veta-o-existenci-a-jednoznacnosti-reseni-pocatecni-ulohy) plyne, že pro všechna $x\in I$ je $y^\*\equiv Y$. $\blacksquare$
