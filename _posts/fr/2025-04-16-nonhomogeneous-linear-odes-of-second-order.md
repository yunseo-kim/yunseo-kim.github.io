---
title: "EDOs linéaires non homogènes du second ordre"
description: "Examen de la forme de la solution générale des EDOs linéaires non homogènes du second ordre en relation avec les solutions des EDOs linéaires homogènes correspondantes, et démonstration de l'existence de la solution générale et de l'absence de solutions singulières."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solution générale** de l'EDO linéaire non homogène du second ordre $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$ :
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$ : solution générale de l'EDO homogène $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, soit $y_h = c_1y_1 + c_2y_2$
>   - $y_p$ : solution particulière de l'EDO non homogène correspondante
> - Le terme de réponse $y_p$ est déterminé uniquement par l'entrée $r(x)$, et pour la même EDO non homogène, $y_p$ ne change pas même si les conditions initiales changent. La différence entre deux solutions particulières de l'EDO non homogène devient une solution de l'EDO homogène correspondante.
> - **Existence de la solution générale** : Si les coefficients $p(x)$, $q(x)$ de l'EDO non homogène et la fonction d'entrée $r(x)$ sont continues, alors la solution générale existe toujours
> - **Absence de solutions singulières** : La solution générale inclut toutes les solutions de l'équation (c'est-à-dire qu'il n'existe pas de solutions singulières)
{: .prompt-info }

## Prérequis
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskien, existence et unicité des solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solution générale et solution particulière des EDOs linéaires non homogènes du second ordre
Considérons l'EDO linéaire non homogène du second ordre

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

où $r(x) \not\equiv 0$. La **solution générale** de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur un intervalle ouvert $I$ est de la forme

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

qui est la somme de la solution générale $y_h = c_1y_1 + c_2y_2$ de l'EDO homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

et d'une solution particulière $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$). De plus, une **solution particulière** de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$ est une solution obtenue à partir de l'équation ($\ref{eqn:general_sol}$) en attribuant des valeurs spécifiques aux constantes arbitraires $c_1$ et $c_2$ dans $y_h$.

En d'autres termes, lorsqu'on ajoute une entrée $r(x)$ qui ne dépend que de la variable indépendante $x$ à l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$), un terme correspondant $y_p$ est ajouté à la réponse, et ce terme de réponse ajouté $y_p$ est déterminé uniquement par l'entrée $r(x)$, indépendamment des conditions initiales. Comme nous le verrons plus tard, si on calcule la différence entre deux solutions arbitraires $y_1$ et $y_2$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) (c'est-à-dire la différence entre les solutions particulières respectives pour deux conditions initiales différentes), la partie $y_p$ indépendante des conditions initiales s'annule, ne laissant que la différence entre ${y_h}\_1$ et ${y_h}\_2$, qui devient une solution de l'équation ($\ref{eqn:homogeneous_linear_ode}$) par le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition).

## Relation entre les solutions de l'EDO non homogène et les solutions de l'EDO homogène correspondante
> **Théorème 1 : Relation entre les solutions de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) et les solutions de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Sur un intervalle ouvert $I$, la somme d'une solution $y$ de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) et d'une solution $\tilde{y}$ de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) est une solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$. En particulier, l'équation ($\ref{eqn:general_sol}$) est une solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$.  
> **(b)** Sur un intervalle $I$, la différence entre deux solutions de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) est une solution de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$.
{: .prompt-info }

### Démonstration
#### (a)
Notons $L[y]$ le membre de gauche des équations ($\ref{eqn:nonhomogeneous_linear_ode}$) et ($\ref{eqn:homogeneous_linear_ode}$). Alors, pour toute solution $y$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$ et toute solution $\tilde{y}$ de l'équation ($\ref{eqn:homogeneous_linear_ode}$), nous avons :

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Pour deux solutions arbitraires $y$ et $y^\*$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$, nous avons :

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## La solution générale de l'EDO non homogène inclut toutes les solutions
Nous savons que pour l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$), [la solution générale inclut toutes les solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/#la-solution-générale-inclut-toutes-les-solutions). Montrons que la même propriété est valide pour l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Théorème 2 : La solution générale de l'EDO non homogène inclut toutes les solutions**  
> Si les coefficients $p(x)$, $q(x)$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) et la fonction d'entrée $r(x)$ sont continues sur un intervalle ouvert $I$, alors toute solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$ peut être obtenue en attribuant des valeurs appropriées aux constantes arbitraires $c_1$ et $c_2$ dans $y_h$ de la solution générale ($\ref{eqn:general_sol}$) de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$.
{: .prompt-info }

### Démonstration
Soit $y^\*$ une solution quelconque de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$, et soit $x_0$ un $x$ quelconque dans l'intervalle $I$. Par le [théorème d'existence de la solution générale pour les EDOs homogènes à coefficients variables continus](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-de-la-solution-générale), $y_h = c_1y_1 + c_2y_2$ existe, et par la **méthode de variation des paramètres** que nous étudierons plus tard, $y_p$ existe également, donc la solution générale ($\ref{eqn:general_sol}$) de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) existe sur l'intervalle $I$. Maintenant, par le théorème [1(b)](#relation-entre-les-solutions-de-ledo-non-homogène-et-les-solutions-de-ledo-homogène-correspondante) démontré précédemment, $Y = y^\* - y_p$ est une solution de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$, et en $x_0$ :

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Par le [théorème d'existence et d'unicité des solutions du problème à valeur initiale](/posts/wronskian-existence-and-uniqueness-of-solutions/#théorème-dexistence-et-dunicité-des-solutions-du-problème-à-valeur-initiale), il existe une solution particulière unique $Y$ de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$ pour les conditions initiales ci-dessus, qui peut être obtenue en attribuant des valeurs appropriées à $c_1$, $c_2$ dans $y_h$. Puisque $y^\* = Y + y_p$, nous avons montré que toute solution particulière $y^\*$ de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) peut être obtenue à partir de la solution générale ($\ref{eqn:general_sol}$). $\blacksquare$
