---
title: "EDOs linéaires non homogènes du second ordre"
description: "Découvrez la forme de la solution générale des EDOs linéaires non homogènes du second ordre, sa relation avec la solution homogène correspondante, et la preuve de son existence et de l'absence de solutions singulières."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solution générale** de l'EDO linéaire non homogène du second ordre $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$ :
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$ : solution générale $y_h = c_1y_1 + c_2y_2$ de l'EDO homogène $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$
>   - $y_p$ : solution particulière de l'EDO non homogène correspondante
> - Le terme de réponse $y_p$ est déterminé uniquement par l'entrée $r(x)$, et pour une même EDO non homogène, $y_p$ ne change pas même si les conditions initiales changent. La différence entre deux solutions particulières d'une EDO non homogène est une solution de l'EDO homogène correspondante.
> - **Existence de la solution générale** : Si les coefficients $p(x)$, $q(x)$ et la fonction d'entrée $r(x)$ de l'EDO non homogène sont continus, alors une solution générale existe toujours.
> - **Inexistence de solutions singulières** : La solution générale inclut toutes les solutions de l'équation (c'est-à-dire qu'il n'existe pas de solutions singulières).
{: .prompt-info }

## Prérequis
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskien, Existence et Unicité de la Solution](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solution générale et solution particulière des EDOs linéaires non homogènes du second ordre
Considérons l'équation différentielle ordinaire linéaire non homogène du second ordre

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

où $r(x) \not\equiv 0$. Sur un intervalle ouvert $I$, la **solution générale** de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) est la somme de la solution générale $y_h = c_1y_1 + c_2y_2$ de l'équation différentielle homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

et d'une solution particulière $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$), sous la forme

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

De plus, une **solution particulière** de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$ est une solution obtenue à partir de l'équation ($\ref{eqn:general_sol}$) en attribuant des valeurs spécifiques aux constantes arbitraires $c_1$ et $c_2$ de $y_h$.

En d'autres termes, si l'on ajoute une entrée $r(x)$ dépendant uniquement de la variable indépendante $x$ à l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$), le terme correspondant $y_p$ est ajouté à la réponse. Ce terme de réponse ajouté $y_p$ est déterminé uniquement par l'entrée $r(x)$, indépendamment des conditions initiales. Comme nous le verrons plus tard, si nous prenons la différence de deux solutions quelconques $y_1$ et $y_2$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) (c'est-à-dire la différence entre deux solutions particulières pour deux conditions initiales différentes), la partie $y_p$, qui est indépendante des conditions initiales, s'annule, ne laissant que la différence entre ${y_h}_1$ et ${y_h}_2$. Selon le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), cette différence est une solution de l'équation ($\ref{eqn:homogeneous_linear_ode}$).

## Relation entre les solutions de l'EDO non homogène et de l'EDO homogène correspondante
> **Théorème 1 : Relation entre les solutions de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) et de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Sur un intervalle ouvert $I$, la somme d'une solution $y$ de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) et d'une solution $\tilde{y}$ de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) est une solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$. En particulier, l'équation ($\ref{eqn:general_sol}$) est une solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$.  
> **(b)** Sur un intervalle $I$, la différence de deux solutions de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) est une solution de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) sur $I$.
{: .prompt-info }

### Démonstration
#### (a)
Notons le membre de gauche des équations ($\ref{eqn:nonhomogeneous_linear_ode}$) et ($\ref{eqn:homogeneous_linear_ode}$) par $L[y]$. Alors, pour toute solution $y$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) et toute solution $\tilde{y}$ de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$, nous avons :

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Pour deux solutions quelconques $y$ et $y^\*$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$, nous avons :

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## La solution générale d'une EDO non homogène inclut toutes les solutions
Pour l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$), [nous savons que la solution générale inclut toutes les solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/#la-solution-générale-inclut-toutes-les-solutions). Montrons que la même chose est vraie pour l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Théorème 2 : La solution générale d'une EDO non homogène inclut toutes les solutions**  
> Si les coefficients $p(x)$, $q(x)$ et la fonction d'entrée $r(x)$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sont continus sur un intervalle ouvert $I$, alors toute solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$ peut être obtenue à partir de la solution générale ($\ref{eqn:general_sol}$) de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$ en attribuant des valeurs appropriées aux constantes arbitraires $c_1$ et $c_2$ de $y_h$.
{: .prompt-info }

### Démonstration
Soit $y^\*$ une solution quelconque de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$, et soit $x_0$ un point quelconque dans l'intervalle $I$. Selon le [théorème d'existence de la solution générale](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-de-la-solution-générale), $y_h = c_1y_1 + c_2y_2$ existe. De plus, comme nous le verrons plus tard, $y_p$ existe également grâce à la **méthode de la variation des paramètres**. Par conséquent, la solution générale ($\ref{eqn:general_sol}$) de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) existe sur l'intervalle $I$. Maintenant, par le théorème [1(b)](#relation-entre-les-solutions-de-ledo-non-homogène-et-de-ledo-homogène-correspondante) prouvé précédemment, $Y = y^\* - y_p$ est une solution de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$, et en $x_0$, nous avons

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Selon le [théorème d'existence et d'unicité pour les problèmes à valeur initiale](/posts/wronskian-existence-and-uniqueness-of-solutions/#théorème-dexistence-et-dunicité-pour-les-problèmes-à-valeur-initiale), il existe une unique solution particulière $Y$ de l'EDO homogène ($\ref{eqn:homogeneous_linear_ode}$) sur l'intervalle $I$ pour les conditions initiales ci-dessus, qui peut être obtenue en choisissant des valeurs appropriées pour $c_1$ et $c_2$ dans $y_h$. Puisque $y^\* = Y + y_p$, nous avons montré que toute solution particulière $y^\*$ de l'EDO non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) peut être obtenue à partir de la solution générale ($\ref{eqn:general_sol}$). $\blacksquare$
