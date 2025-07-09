---
title: "EDOs Linéaires Homogènes du Second Ordre"
description: "Découvrez la définition des EDO linéaires du second ordre, le principe de superposition pour les équations homogènes, et le concept de base (système fondamental) pour trouver leurs solutions."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Forme standard** d'une EDO linéaire du second ordre : $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coefficients** : fonctions $p$, $q$
>   - **Entrée (input)** : $r(x)$
>   - **Sortie (output)** ou **Réponse (response)** : $y(x)$
> - Homogène et non homogène
>   - **Homogène** : cas où $r(x)\equiv0$ dans la forme standard
>   - **Non homogène** : cas où $r(x)\not\equiv 0$ dans la forme standard
> - **Principe de superposition** : Pour une EDO linéaire <u>homogène</u> $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, toute combinaison linéaire de deux solutions sur un intervalle ouvert $I$ est également une solution de l'équation donnée. Autrement dit, la somme et le produit par une constante de solutions quelconques de l'EDO linéaire homogène donnée sont aussi des solutions de cette équation.
> - **Base** ou **système fondamental** : une paire de solutions $(y_1, y_2)$ de l'EDO linéaire homogène, linéairement indépendantes sur un intervalle $I$.
> - **Réduction de l'ordre** : Si l'on peut trouver une solution à une EDO homogène du second ordre, une deuxième solution linéairement indépendante, c'est-à-dire une base, peut être trouvée en résolvant une EDO du premier ordre. Cette méthode est appelée réduction de l'ordre.
> - Application de la réduction de l'ordre : Une EDO générale du second ordre $F(x, y, y^\prime, y^{\prime\prime})=0$, qu'elle soit linéaire ou non, peut être réduite à une EDO du premier ordre par la méthode de réduction de l'ordre dans les cas suivants :
>   - $y$ n'apparaît pas explicitement.
>   - $x$ n'apparaît pas explicitement.
>   - L'équation est linéaire homogène et une solution est déjà connue.
{: .prompt-info }

## Prérequis
- [Concepts de Base de la Modélisation](/posts/Basic-Concepts-of-Modeling/)
- [Séparation des Variables](/posts/Separation-of-Variables/)
- [Résolution des EDO Linéaires du Premier Ordre](/posts/Solution-of-First-Order-Linear-ODE/)

## Équations Différentielles Ordinaires Linéaires du Second Ordre
Une équation différentielle ordinaire du second ordre est dite **linéaire** si elle peut s'écrire sous la forme

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

sinon, elle est dite **non linéaire**.

Lorsque $p$, $q$, et $r$ sont des fonctions d'une variable $x$, cette équation est linéaire par rapport à $y$ et ses dérivées.

La forme de l'équation ($\ref{eqn:standard_form}$) est appelée la **forme standard** d'une EDO linéaire du second ordre. Si le premier terme d'une EDO linéaire du second ordre donnée est $f(x)y^{\prime\prime}$, on peut obtenir la forme standard en divisant les deux côtés de l'équation par $f(x)$.

Les fonctions $p$ et $q$ sont appelées les **coefficients**, $r(x)$ est l'**entrée (input)**, et $y(x)$ est la **sortie (output)** ou la **réponse (response)** à l'entrée et aux conditions initiales.

### Équations Différentielles Ordinaires Linéaires Homogènes du Second Ordre
Soit $J$ un intervalle $a<x<b$ sur lequel nous cherchons à résoudre l'équation ($\ref{eqn:standard_form}$). Si $r(x)\equiv 0$ sur l'intervalle $J$ dans l'équation ($\ref{eqn:standard_form}$), on a

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

et l'équation est dite **homogène**.

## Équations Différentielles Ordinaires Linéaires Non Homogènes
Si $r(x)\not\equiv 0$ sur l'intervalle $J$, l'équation est dite **non homogène**.

## Principe de Superposition

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ sont des constantes arbitraires)}\tag{3}$$

Une fonction de cette forme est appelée une **combinaison linéaire** de $y_1$ et $y_2$.

Le théorème suivant s'applique.

> **Principe de superposition**  
> Pour l'équation différentielle ordinaire linéaire homogène ($\ref{eqn:homogeneous_linear_ode}$), toute combinaison linéaire de deux solutions sur un intervalle ouvert $I$ est également une solution de ($\ref{eqn:homogeneous_linear_ode}$). Autrement dit, la somme et le produit par une constante de solutions quelconques de l'EDO linéaire homogène donnée sont aussi des solutions de cette équation.
{: .prompt-info }

### Démonstration
Soient $y_1$ et $y_2$ des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur un intervalle $I$. En substituant $y=c_1y_1+c_2y_2$ dans l'équation ($\ref{eqn:homogeneous_linear_ode}$), on obtient

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

ce qui est une identité. Par conséquent, $y$ est une solution de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$. $\blacksquare$

> Notez que le principe de superposition ne s'applique qu'aux équations différentielles ordinaires linéaires homogènes, et non aux équations linéaires non homogènes ou aux équations non linéaires.
{: .prompt-warning }

## Base et Solution Générale
### Rappel des Concepts Clés des EDO du Premier Ordre
Comme nous l'avons vu précédemment dans [Concepts de Base de la Modélisation](/posts/Basic-Concepts-of-Modeling/), un problème de valeur initiale pour une EDO du premier ordre se compose de l'EDO et d'une condition initiale $y(x_0)=y_0$. La condition initiale est nécessaire pour déterminer la constante arbitraire $c$ de la solution générale de l'EDO, et la solution ainsi déterminée est appelée solution particulière. Étendons maintenant ces concepts aux EDO du second ordre.

### Problème de Valeur Initiale et Conditions Initiales
Un **problème de valeur initiale** pour une EDO homogène du second ordre ($\ref{eqn:homogeneous_linear_ode}$) se compose de l'EDO donnée ($\ref{eqn:homogeneous_linear_ode}$) et de deux **conditions initiales**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Ces conditions sont nécessaires pour déterminer les deux constantes arbitraires $c_1$ et $c_2$ de la **solution générale**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

de l'EDO.

### Indépendance et Dépendance Linéaire
Faisons une pause pour examiner les concepts d'indépendance et de dépendance linéaire. Il est nécessaire de les comprendre pour définir une base plus tard.  
Si pour toutes les valeurs de $x$ dans un intervalle $I$ où deux fonctions $y_1$ et $y_2$ sont définies,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ et }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

alors ces deux fonctions $y_1$ et $y_2$ sont dites **linéairement indépendantes** sur l'intervalle $I$. Sinon, $y_1$ et $y_2$ sont dites **linéairement dépendantes**.

Si $y_1$ et $y_2$ sont linéairement dépendantes (c'est-à-dire que la proposition ($\ref{eqn:linearly_independent}$) n'est pas vraie), alors avec $k_1 \neq 0$ ou $k_2 \neq 0$, on peut diviser les deux côtés de l'équation dans ($\ref{eqn:linearly_independent}$) pour écrire

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{ou} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

ce qui montre que $y_1$ et $y_2$ sont proportionnelles.

### Base, Solution Générale et Solution Particulière
Revenons à notre sujet. Pour que l'équation ($\ref{eqn:general_sol}$) soit une solution générale, $y_1$ et $y_2$ doivent être des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) et être linéairement indépendantes (non proportionnelles) sur l'intervalle $I$. Une telle paire de solutions $(y_1, y_2)$ de l'équation ($\ref{eqn:homogeneous_linear_ode}$), qui sont linéairement indépendantes sur l'intervalle $I$, est appelée une **base** ou un **système fondamental** de solutions de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$.

En utilisant les conditions initiales pour déterminer les deux constantes $c_1$ et $c_2$ de la solution générale ($\ref{eqn:general_sol}$), on obtient une solution unique qui passe par le point $(x_0, K_0)$ et dont la pente de la tangente en ce point est $K_1$. Ceci est appelé une **solution particulière** de l'EDO ($\ref{eqn:homogeneous_linear_ode}$).

Si l'équation ($\ref{eqn:homogeneous_linear_ode}$) est continue sur un intervalle ouvert $I$, elle possède nécessairement une solution générale, et cette solution générale inclut toutes les solutions particulières possibles. En d'autres termes, dans ce cas, l'équation ($\ref{eqn:homogeneous_linear_ode}$) n'a pas de solution singulière qui ne puisse être obtenue à partir de la solution générale.

## Réduction de l'Ordre (Reduction of Order)
Si l'on peut trouver une solution à une EDO homogène du second ordre, une deuxième solution linéairement indépendante, c'est-à-dire une base, peut être trouvée en résolvant une EDO du premier ordre. Cette méthode est appelée **réduction de l'ordre**.

Pour une EDO homogène du second ordre <u>sous forme standard avec $y^{\prime\prime}$ et non $f(x)y^{\prime\prime}$</u>

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

supposons que nous connaissions une solution $y_1$ de cette équation sur un intervalle ouvert $I$.

Posons maintenant la deuxième solution que nous cherchons comme étant $y_2 = uy_1$, et

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

En substituant cela dans l'équation,

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

on obtient. En regroupant les termes en $u^{\prime\prime}$, $u^{\prime}$, et $u$, on a

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Cependant, comme $y_1$ est une solution de l'équation donnée, l'expression dans la dernière parenthèse est égale à $0$. Le terme en $u$ disparaît donc, laissant une EDO en $u^{\prime}$ et $u^{\prime\prime}$. En divisant les deux côtés de cette EDO restante par $y_1$ et en posant $u^{\prime}=U$ et $u^{\prime\prime}=U^{\prime}$, nous obtenons l'EDO du premier ordre suivante.

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

En [séparant les variables](/posts/Separation-of-Variables/) et en intégrant,

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

et en appliquant la fonction exponentielle aux deux côtés, on obtient finalement

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Comme nous avons posé $U=u^{\prime}$, on a $u=\int U dx$, et la deuxième solution $y_2$ que nous cherchons est

$$ y_2 = uy_1 = y_1 \int U dx $$

Puisque $\cfrac{y_2}{y_1} = u = \int U dx$ ne peut pas être une constante tant que $U>0$, $y_1$ et $y_2$ forment une base de solutions.

### Application de la Réduction de l'Ordre
Une EDO générale du second ordre $F(x, y, y^\prime, y^{\prime\prime})=0$, qu'elle soit linéaire ou non, peut être réduite à une EDO du premier ordre en utilisant la réduction de l'ordre lorsque $y$ n'apparaît pas explicitement, lorsque $x$ n'apparaît pas explicitement, ou, comme vu précédemment, lorsque l'équation est linéaire homogène et qu'une solution est déjà connue.

#### Cas où $y$ n'apparaît pas explicitement
Dans $F(x, y^\prime, y^{\prime\prime})=0$, en posant $z=y^{\prime}$, on peut la réduire à une EDO du premier ordre en $z$, $F(x, z, z^{\prime})$.

#### Cas où $x$ n'apparaît pas explicitement
Dans $F(y, y^\prime, y^{\prime\prime})=0$, en posant $z=y^{\prime}$, on a $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$. L'équation peut donc être réduite à une EDO du premier ordre en $z$, $F(y,z,z^\prime)$, où $y$ joue le rôle de la variable indépendante à la place de $x$.
