---
title: Équations différentielles linéaires non homogènes du second ordre
description: Découvrez la structure et les propriétés des équations différentielles ordinaires linéaires non homogènes du second ordre, leur solution générale et les relations entre les solutions homogènes et non homogènes.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solution générale** d'une équation différentielle linéaire non homogène du second ordre $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$ :
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$ : solution générale de l'équation homogène $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, soit $y_h = c_1y_1 + c_2y_2$
>   - $y_p$ : solution particulière de l'équation non homogène
> - Le terme de réponse $y_p$ est déterminé uniquement par l'entrée $r(x)$ et reste inchangé pour différentes conditions initiales de la même équation non homogène. La différence entre deux solutions particulières d'une équation non homogène est une solution de l'équation homogène correspondante.
> - **Existence de la solution générale** : Si les coefficients $p(x)$, $q(x)$ et la fonction d'entrée $r(x)$ sont continus, alors la solution générale existe toujours
> - **Absence de solutions singulières** : La solution générale englobe toutes les solutions possibles (c'est-à-dire qu'il n'existe pas de solutions singulières)
{: .prompt-info }

## Prérequis
- [Équations différentielles ordinaires linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskien, existence et unicité des solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solution générale et solution particulière des équations différentielles linéaires non homogènes du second ordre
Considérons l'équation différentielle linéaire non homogène du second ordre

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

où $r(x) \not\equiv 0$. Sur un intervalle ouvert $I$, la **solution générale** de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) est la somme de la solution générale $y_h = c_1y_1 + c_2y_2$ de l'équation homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

et d'une solution particulière $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) :

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

De plus, une **solution particulière** de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur l'intervalle $I$ est obtenue en attribuant des valeurs spécifiques aux constantes arbitraires $c_1$ et $c_2$ dans $y_h$.

En d'autres termes, lorsqu'on ajoute une entrée $r(x)$ dépendant uniquement de la variable indépendante $x$ à l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$), un terme de réponse correspondant $y_p$ s'ajoute à la solution, et ce terme $y_p$ est déterminé uniquement par l'entrée $r(x)$, indépendamment des conditions initiales. Comme nous le verrons plus loin, si l'on calcule la différence entre deux solutions particulières $y_1$ et $y_2$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) (c'est-à-dire la différence entre les solutions pour deux conditions initiales différentes), le terme $y_p$ indépendant des conditions initiales s'annule, ne laissant que la différence entre ${y_h}_1$ et ${y_h}_2$, qui, selon le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), est une solution de l'équation ($\ref{eqn:homogeneous_linear_ode}$).

## Relation entre les solutions de l'équation non homogène et celles de l'équation homogène correspondante
> **Théorème 1 : Relation entre les solutions de l'équation non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) et celles de l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Sur un intervalle ouvert $I$, la somme d'une solution $y$ de l'équation non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) et d'une solution $\tilde{y}$ de l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$) est une solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$. En particulier, l'expression ($\ref{eqn:general_sol}$) est une solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$.  
> **(b)** La différence entre deux solutions quelconques de l'équation non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$ est une solution de l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$) sur $I$.
{: .prompt-info }

### Démonstration
#### (a)
Notons $L[y]$ le membre de gauche des équations ($\ref{eqn:nonhomogeneous_linear_ode}$) et ($\ref{eqn:homogeneous_linear_ode}$). Alors, pour toute solution $y$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) et toute solution $\tilde{y}$ de l'équation ($\ref{eqn:homogeneous_linear_ode}$) sur $I$, nous avons :

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Pour deux solutions quelconques $y$ et $y^\*$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$, nous avons :

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## La solution générale englobe toutes les solutions
Nous savons déjà que pour l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$), [la solution générale englobe toutes les solutions possibles](/posts/wronskian-existence-and-uniqueness-of-solutions/#la-solution-générale-englobe-toutes-les-solutions). Montrons que cela est également vrai pour l'équation non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Théorème 2 : La solution générale de l'équation non homogène englobe toutes les solutions**  
> Si les coefficients $p(x)$, $q(x)$ et la fonction d'entrée $r(x)$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sont continus sur un intervalle ouvert $I$, alors toute solution de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$ peut être obtenue à partir de la solution générale ($\ref{eqn:general_sol}$) en attribuant des valeurs appropriées aux constantes arbitraires $c_1$ et $c_2$ dans $y_h$.
{: .prompt-info }

### Démonstration
Soit $y^\*$ une solution quelconque de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) sur $I$, et soit $x_0$ un point quelconque de $I$. D'après le [théorème d'existence de la solution générale pour les équations homogènes à coefficients continus](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-de-la-solution-générale), la solution générale $y_h = c_1y_1 + c_2y_2$ existe, et grâce à la **méthode de variation des paramètres** que nous étudierons ultérieurement, $y_p$ existe également. Par conséquent, la solution générale ($\ref{eqn:general_sol}$) de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) existe sur $I$. D'après le théorème [1(b)](#relation-entre-les-solutions-de-léquation-non-homogène-et-celles-de-léquation-homogène-correspondante) démontré précédemment, $Y = y^\* - y_p$ est une solution de l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$) sur $I$, et au point $x_0$ :

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

D'après le [théorème d'existence et d'unicité pour le problème à valeur initiale](/posts/wronskian-existence-and-uniqueness-of-solutions/#théorème-dexistence-et-dunicité-pour-le-problème-à-valeur-initiale), il existe une solution unique $Y$ de l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$) sur $I$ satisfaisant ces conditions initiales, et cette solution peut être obtenue en attribuant des valeurs appropriées aux constantes $c_1$ et $c_2$ dans $y_h$. Puisque $y^\* = Y + y_p$, nous avons montré que toute solution particulière $y^\*$ de l'équation non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$) peut être obtenue à partir de la solution générale ($\ref{eqn:general_sol}$). $\blacksquare$
