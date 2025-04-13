---
title: Équations différentielles ordinaires linéaires homogènes du second ordre
description: Découvrez la définition et les caractéristiques des équations différentielles ordinaires linéaires du second ordre, en particulier le principe de superposition et le concept de base (basis) qui s'appliquent aux équations différentielles ordinaires linéaires homogènes.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Forme standard** d'une équation différentielle ordinaire linéaire du second ordre : $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coefficients** : fonctions $p$, $q$
>   - **Entrée (input)** : $r(x)$
>   - **Sortie (output)** ou **réponse (response)** : $y(x)$
> - Homogène et non homogène
>   - **Homogène** : lorsque $r(x)\equiv0$ dans la forme standard
>   - **Non homogène** : lorsque $r(x)\not\equiv 0$ dans la forme standard
> - **Principe de superposition** : Pour une équation différentielle ordinaire linéaire homogène $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, toute combinaison linéaire de deux solutions sur un intervalle ouvert $I$ est également une solution de l'équation donnée. En d'autres termes, la somme et le produit par une constante de solutions arbitraires de l'équation différentielle ordinaire linéaire homogène donnée sont également des solutions de cette équation.
> - **Base (basis)** ou **système fondamental (fundamental system)** : une paire de solutions $(y_1, y_2)$ linéairement indépendantes de l'équation différentielle ordinaire linéaire homogène sur l'intervalle $I$
> - **Réduction d'ordre (reduction of order)** : Si on peut trouver une solution d'une équation différentielle ordinaire homogène du second ordre, on peut trouver une deuxième solution linéairement indépendante, c'est-à-dire une base, en résolvant une équation différentielle du premier ordre. Cette méthode est appelée réduction d'ordre.
> - Application de la réduction d'ordre : Une équation différentielle générale du second ordre $F(x, y, y^\prime, y^{\prime\prime})=0$, qu'elle soit linéaire ou non linéaire, peut être réduite au premier ordre en utilisant la réduction d'ordre dans les cas suivants :
>   - Lorsque $y$ n'apparaît pas explicitement
>   - Lorsque $x$ n'apparaît pas explicitement
>   - Lorsqu'elle est linéaire homogène et qu'une solution est déjà connue
{: .prompt-info }

## Prérequis
- [Concepts de base de la modélisation](/posts/Basic-Concepts-of-Modeling/)
- [Séparation des variables](/posts/Separation-of-Variables/)
- [Solution des équations différentielles ordinaires linéaires du premier ordre](/posts/Solution-of-First-Order-Linear-ODE/)

## Équations différentielles ordinaires linéaires du second ordre
Une équation différentielle du second ordre est dite **linéaire** si elle peut être écrite sous la forme :

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

Si elle ne peut pas être écrite sous cette forme, elle est dite **non linéaire**.

Lorsque $p$, $q$, et $r$ sont des fonctions de $x$, cette équation est linéaire par rapport à $y$ et ses dérivées.

La forme de l'équation ($\ref{eqn:standard_form}$) est appelée **forme standard** d'une équation différentielle ordinaire linéaire du second ordre. Si le premier terme d'une équation différentielle ordinaire linéaire du second ordre donnée est $f(x)y^{\prime\prime}$, on peut obtenir la forme standard en divisant les deux côtés de l'équation par $f(x)$.

Les fonctions $p$ et $q$ sont appelées **coefficients**, $r(x)$ est appelée **entrée (input)**, et $y(x)$ est appelée **sortie (output)** ou **réponse (response)** à l'entrée et aux conditions initiales.

### Équation différentielle ordinaire linéaire homogène du second ordre
Soit $J$ l'intervalle $a<x<b$ sur lequel on cherche à résoudre l'équation ($\ref{eqn:standard_form}$). Si $r(x)\equiv 0$ sur l'intervalle $J$ dans l'équation ($\ref{eqn:standard_form}$), on obtient :

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

et cette équation est dite **homogène**.

## Équation différentielle ordinaire linéaire non homogène
Si $r(x)\not\equiv 0$ sur l'intervalle $J$, l'équation est dite **non homogène**.

## Principe de superposition

Une fonction de la forme

$$ y = c_1y_1 + c_2y_2 \quad \text{(où }c_1, c_2\text{ sont des constantes arbitraires)}\tag{3}$$

est appelée **combinaison linéaire** de $y_1$ et $y_2$.

Dans ce cas, le principe suivant s'applique :

> **Principe de superposition**  
> Pour une équation différentielle ordinaire linéaire homogène ($\ref{eqn:homogeneous_linear_ode}$), toute combinaison linéaire de deux solutions sur un intervalle ouvert $I$ est également une solution de l'équation ($\ref{eqn:homogeneous_linear_ode}$). En d'autres termes, la somme et le produit par une constante de solutions arbitraires de l'équation différentielle ordinaire linéaire homogène donnée sont également des solutions de cette équation.
{: .prompt-info }

### Démonstration
Supposons que $y_1$ et $y_2$ soient des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$. En substituant $y=c_1y_1+c_2y_2$ dans l'équation ($\ref{eqn:homogeneous_linear_ode}$), on obtient :

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

Ce qui est une identité. Par conséquent, $y$ est une solution de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$. $\blacksquare$

> Il est important de noter que le principe de superposition ne s'applique qu'aux équations différentielles ordinaires linéaires homogènes, et non aux équations différentielles ordinaires linéaires non homogènes ou aux équations différentielles non linéaires.
{: .prompt-warning }

## Base et solution générale
### Rappel des concepts clés pour les équations différentielles du premier ordre
Comme nous l'avons vu précédemment dans [Concepts de base de la modélisation](/posts/Basic-Concepts-of-Modeling/), un problème à valeur initiale (Initial Value Problem) pour une équation différentielle du premier ordre se compose de l'équation différentielle et d'une condition initiale (initial condition) $y(x_0)=y_0$. La condition initiale est nécessaire pour déterminer la constante arbitraire $c$ dans la solution générale de l'équation différentielle donnée, et la solution ainsi déterminée est appelée solution particulière. Étendons maintenant ces concepts aux équations différentielles du second ordre.

### Problème à valeur initiale et conditions initiales
Un **problème à valeur initiale (initial value problem)** pour une équation différentielle ordinaire linéaire homogène du second ordre ($\ref{eqn:homogeneous_linear_ode}$) se compose de l'équation différentielle donnée ($\ref{eqn:homogeneous_linear_ode}$) et de deux **conditions initiales (initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Ces conditions sont nécessaires pour déterminer les deux constantes arbitraires $c_1$ et $c_2$ dans la **solution générale (general solution)** de l'équation différentielle

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Indépendance linéaire et dépendance linéaire
Prenons un moment pour comprendre les concepts d'indépendance linéaire et de dépendance linéaire. Cette compréhension est nécessaire pour définir la base plus tard.  
Deux fonctions $y_1$ et $y_2$ sont dites **linéairement indépendantes (linearly independent)** sur un intervalle $I$ si, pour tous les points de l'intervalle $I$,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ et }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

Si ce n'est pas le cas, $y_1$ et $y_2$ sont dites **linéairement dépendantes (linearly dependent)**.

Si $y_1$ et $y_2$ sont linéairement dépendantes (c'est-à-dire si la proposition ($\ref{eqn:linearly_independent}$) n'est pas vraie), on peut diviser les deux côtés de l'équation dans ($\ref{eqn:linearly_independent}$) par $k_1 \neq 0$ ou $k_2 \neq 0$ pour obtenir

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{ou} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

ce qui montre que $y_1$ et $y_2$ sont proportionnelles.

### Base, solution générale, solution particulière
Revenons à notre sujet principal. Pour que l'équation ($\ref{eqn:general_sol}$) soit une solution générale, $y_1$ et $y_2$ doivent être des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) et en même temps être linéairement indépendantes (non proportionnelles) sur l'intervalle $I$. Une paire $(y_1, y_2)$ de solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) qui sont linéairement indépendantes sur l'intervalle $I$ est appelée **base (basis)** ou **système fondamental (fundamental system)** des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$.

En utilisant les conditions initiales pour déterminer les deux constantes $c_1$ et $c_2$ dans la solution générale ($\ref{eqn:general_sol}$), on obtient une solution unique qui passe par le point $(x_0, K_0)$ avec une pente $K_1$ en ce point. Cette solution est appelée **solution particulière (particular solution)** de l'équation différentielle ($\ref{eqn:homogeneous_linear_ode}$).

Si l'équation ($\ref{eqn:homogeneous_linear_ode}$) est continue sur un intervalle ouvert $I$, elle a nécessairement une solution générale, et cette solution générale inclut toutes les solutions particulières possibles. En d'autres termes, dans ce cas, l'équation ($\ref{eqn:homogeneous_linear_ode}$) n'a pas de solution singulière (singular solution) qui ne peut pas être obtenue à partir de la solution générale.

## Réduction d'ordre
Si on peut trouver une solution d'une équation différentielle ordinaire homogène du second ordre, on peut trouver une deuxième solution linéairement indépendante, c'est-à-dire une base, en résolvant une équation différentielle du premier ordre comme suit. Cette méthode est appelée **réduction d'ordre (reduction of order)**.

Considérons une équation différentielle ordinaire linéaire homogène du second ordre <u>sous forme standard avec $y^{\prime\prime}$ et non $f(x)y^{\prime\prime}$</u> :

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

Supposons que nous connaissions une solution $y_1$ de cette équation sur un intervalle ouvert $I$.

Posons maintenant la deuxième solution que nous cherchons comme $y_2 = uy_1$, et

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

En substituant dans l'équation, on obtient :

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

En regroupant les termes en $u^{\prime\prime}$, $u^{\prime}$, et $u$, on obtient :

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Cependant, comme $y_1$ est une solution de l'équation donnée, l'expression entre parenthèses du dernier terme est égale à 0, donc le terme en $u$ disparaît, laissant une équation différentielle en $u^{\prime}$ et $u^{\prime\prime}$. En divisant les deux côtés de cette équation différentielle restante par $y_1$ et en posant $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, on obtient l'équation différentielle du premier ordre suivante :

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

En [séparant les variables](/posts/Separation-of-Variables/) et en intégrant, on obtient :

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

En prenant l'exponentielle des deux côtés, on obtient finalement :

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Comme on a posé $U=u^{\prime}$, on a $u=\int U dx$, donc la deuxième solution $y_2$ que nous cherchions est :

$$ y_2 = uy_1 = y_1 \int U dx $$

Comme $\cfrac{y_2}{y_1} = u = \int U dx$ ne peut pas être une constante tant que $U>0$, $y_1$ et $y_2$ forment une base de solutions.

### Application de la réduction d'ordre
Une équation différentielle générale du second ordre $F(x, y, y^\prime, y^{\prime\prime})=0$, qu'elle soit linéaire ou non linéaire, peut être réduite au premier ordre en utilisant la réduction d'ordre lorsque $y$ n'apparaît pas explicitement, lorsque $x$ n'apparaît pas explicitement, ou comme nous l'avons vu précédemment, lorsqu'elle est linéaire homogène et qu'une solution est déjà connue.

#### Lorsque $y$ n'apparaît pas explicitement
Dans $F(x, y^\prime, y^{\prime\prime})=0$, en posant $z=y^{\prime}$, on peut réduire l'équation à une équation différentielle du premier ordre en $z$, $F(x, z, z^{\prime})$.

#### Lorsque $x$ n'apparaît pas explicitement
Dans $F(y, y^\prime, y^{\prime\prime})=0$, en posant $z=y^{\prime}$, on a $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$, donc on peut réduire l'équation à une équation différentielle du premier ordre en $z$, $F(y,z,z^\prime)$, où $y$ joue le rôle de la variable indépendante $x$.
