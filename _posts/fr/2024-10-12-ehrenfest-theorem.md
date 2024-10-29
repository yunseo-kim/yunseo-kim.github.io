---
title: "Théorème d'Ehrenfest"
description: >-
  Nous explorons comment calculer les valeurs attendues de la position et de l'impulsion à partir de la fonction d'onde en mécanique quantique,
  puis nous étendons cela à une formule de calcul de la valeur attendue pour toute variable mécanique Q(x,p).
  Enfin, nous dérivons le théorème d'Ehrenfest à partir de ces résultats.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
---

## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Prérequis
- Distribution de probabilité continue et densité de probabilité
- [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/)

## Calcul des valeurs attendues à partir de la fonction d'onde
### Valeur attendue de la position $x$
La valeur attendue (expectation value) de la position $x$ pour une particule dans l'état $\Psi$ est

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

Si on mesure la position d'un grand nombre de particules dans le même état $\Psi$ et qu'on fait la moyenne des résultats, on obtient $\langle x \rangle$ calculé par l'équation ci-dessus.

> Notez que la valeur attendue dont on parle ici n'est pas la moyenne obtenue en mesurant répétitivement une seule particule, mais la moyenne des résultats de mesure pour un **ensemble** de systèmes dans le même état. Si on mesure la même particule plusieurs fois à de courts intervalles, la fonction d'onde [s'effondre (collapse)](/posts/schrodinger-equation-and-the-wave-function/#mesure-et-effondrement-de-la-fonction-donde) lors de la première mesure, donc on obtiendrait continuellement la même valeur dans les mesures suivantes.
{: .prompt-warning }

### Valeur attendue de l'impulsion $p$
Comme $\Psi$ dépend du temps, $\langle x \rangle$ changera avec le temps. Selon l'équation (8) de [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/) et l'équation ($\ref{eqn:x_exp}$) ci-dessus, on a :

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> Dans le processus de ($\ref{eqn:dx/dt_1}$) à ($\ref{eqn:dx/dt_2}$) et de ($\ref{eqn:dx/dt_2}$) à ($\ref{eqn:dx/dt_3}$), l'intégration par parties a été appliquée deux fois, et comme $\lim_{x\rightarrow\pm\infty}\Psi=0$, les termes de bord (boundary terms) ont été éliminés.
{: .prompt-tip }

Ainsi, on obtient la valeur attendue de l'**impulsion** comme suit :

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Valeur attendue pour une quantité physique arbitraire $Q(x,p)$
Les expressions de $\langle x \rangle$ et $\langle p \rangle$ que nous avons obtenues précédemment peuvent être écrites sous la forme suivante :

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

L'opérateur $\hat x \equiv x$ représente la position, et l'opérateur $\hat p \equiv -i\hbar(\partial/\partial x)$ représente l'impulsion. Pour l'opérateur d'impulsion $\hat p$, on peut le définir comme $\hat p \equiv -i\hbar\nabla$ lorsqu'on l'étend à l'espace tridimensionnel.

Comme toutes les variables de la mécanique classique peuvent être exprimées en termes de position et d'impulsion, on peut étendre cela à la valeur attendue d'une quantité physique arbitraire. Pour calculer la valeur attendue d'une quantité arbitraire $Q(x,p)$, il faut remplacer tous les $p$ par $-i\hbar\nabla$, puis insérer l'opérateur ainsi obtenu entre $\Psi^*$ et $\Psi$ et intégrer.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Par exemple, comme l'énergie cinétique est $T=\cfrac{p^2}{2m}$, on a

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

L'équation ($\ref{eqn:Q_exp}$) permet de calculer la valeur attendue de toute quantité physique pour une particule dans l'état $\Psi$.

## Théorème d'Ehrenfest
### Calcul de $d\langle p \rangle/dt$
Dérivons les deux côtés de l'équation ($\ref{eqn:p_op}$) par rapport au temps $t$ pour obtenir la dérivée temporelle de la valeur attendue de l'impulsion $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> On peut obtenir l'équation ($\ref{eqn:dp/dt_2}$) en substituant les équations (6) et (7) de [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/) dans l'équation ($\ref{eqn:dp/dt_1}$). Dans le processus de ($\ref{eqn:dp/dt_3}$) à ($\ref{eqn:dp/dt_4}$), l'intégration par parties a été appliquée, et comme précédemment, $\lim_{x\rightarrow\pm\infty}\Psi=0$, donc les termes de bord (boundary terms) ont été éliminés.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Relation entre le théorème d'Ehrenfest et la deuxième loi du mouvement de Newton
Les deux équations suivantes que nous avons obtenues sont appelées le théorème d'Ehrenfest :

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

Le théorème d'Ehrenfest a une forme très similaire à la relation entre l'énergie potentielle et la force conservative en mécanique classique, $F=\cfrac{dp}{dt}=-\nabla V$.  
Comparons les deux équations côte à côte :

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Théorème d'Ehrenfest]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Deuxième loi du mouvement de Newton]}$$

Si on développe en série de Taylor le terme de droite de la deuxième équation du théorème d'Ehrenfest $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (équation [$\ref{eqn:ehrenfest_theorem_2nd}$]) autour de $\langle x \rangle$, on obtient :

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

Si $x-\langle x \rangle$ est suffisamment petit, on peut négliger tous les termes d'ordre supérieur sauf le premier terme et approximer :

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

En d'autres termes, **si la fonction d'onde d'une particule a une distribution spatiale très étroite et pointue (si la dispersion de $\|\Psi\|^2$ par rapport à $x$ est très petite), le théorème d'Ehrenfest peut être approximé par la deuxième loi du mouvement de Newton de la mécanique classique.** À l'échelle macroscopique, on peut ignorer l'étendue spatiale de la fonction d'onde et considérer la position de la particule comme essentiellement un point, donc la deuxième loi du mouvement de Newton s'applique. Cependant, à l'échelle microscopique, les effets quantiques ne peuvent pas être ignorés, donc la deuxième loi du mouvement de Newton ne s'applique plus et il faut utiliser le théorème d'Ehrenfest.
