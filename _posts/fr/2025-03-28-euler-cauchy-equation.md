---
title: Équation d'Euler-Cauchy
description: Examinons comment la forme de la solution générale de l'équation d'Euler-Cauchy varie selon le signe du discriminant de l'équation auxiliaire.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Équation d'Euler-Cauchy : $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Équation auxiliaire** : $m^2 + (a-1)m + b = 0$
> - La forme de la solution générale dépend du signe du discriminant $(1-a)^2 - 4b$ de l'équation auxiliaire, comme indiqué dans le tableau
>
> | Cas | Racines de l'équation auxiliaire | Base des solutions de l'équation d'Euler-Cauchy | Solution générale de l'équation d'Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Racines réelles distinctes<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Racine réelle double<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Racines complexes conjuguées<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prérequis
- [Équations différentielles ordinaires linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Équations différentielles ordinaires linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Formule d'Euler

## Équation auxiliaire
L'**équation d'Euler-Cauchy** est une équation différentielle de la forme

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

où $a$ et $b$ sont des constantes et $y(x)$ est la fonction inconnue. En substituant dans l'équation ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

on obtient

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

soit

$$ [m(m-1) + am + b]x^m = 0 $$

Ce qui nous donne l'équation auxiliaire

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

La condition nécessaire et suffisante pour que $y=x^m$ soit une solution de l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) est que $m$ soit une racine de l'équation auxiliaire ($\ref{eqn:auxiliary_eqn}$).

Les racines de cette équation quadratique ($\ref{eqn:auxiliary_eqn}$) sont

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

et par conséquent, les deux fonctions

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

sont des solutions de l'équation ($\ref{eqn:euler_cauchy_eqn}$).

Comme pour les [équations différentielles ordinaires linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/), nous pouvons distinguer trois cas selon le signe du discriminant $(1-a)^2 - 4b$ de l'équation auxiliaire ($\ref{eqn:auxiliary_eqn}$) :
- $(1-a)^2 - 4b > 0$ : deux racines réelles distinctes
- $(1-a)^2 - 4b = 0$ : une racine réelle double
- $(1-a)^2 - 4b < 0$ : deux racines complexes conjuguées

## Forme de la solution générale selon le signe du discriminant
### I. Deux racines réelles distinctes $m_1$ et $m_2$
Dans ce cas, la base des solutions de l'équation ($\ref{eqn:euler_cauchy_eqn}$) sur tout intervalle est

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

et la solution générale est

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Racine réelle double $m = \cfrac{1-a}{2}$
Lorsque $(1-a)^2 - 4b = 0$, c'est-à-dire $b=\cfrac{(1-a)^2}{4}$, l'équation quadratique ($\ref{eqn:auxiliary_eqn}$) n'a qu'une seule racine $m = m_1 = m_2 = \cfrac{1-a}{2}$, ce qui nous donne une solution de la forme

$$ y_1 = x^{(1-a)/2} $$

et l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) devient

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Trouvons maintenant une seconde solution linéairement indépendante $y_2$ en utilisant la [réduction d'ordre](/posts/homogeneous-linear-odes-of-second-order/#réduction-dordre).

Posons $y_2=uy_1$, ce qui nous donne

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Comme $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$, on a

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

En intégrant, on obtient $u = \ln x$.

Donc $y_2 = uy_1 = y_1 \ln x$, et $y_1$ et $y_2$ sont linéairement indépendants car leur rapport n'est pas constant. La solution générale est alors

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Racines complexes conjuguées
Dans ce cas, les racines de l'équation auxiliaire ($\ref{eqn:auxiliary_eqn}$) sont $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, et les deux solutions complexes correspondantes de l'équation ($\ref{eqn:euler_cauchy_eqn}$) peuvent s'écrire, en utilisant $x=e^{\ln x}$ :

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

En posant $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ et en utilisant la formule d'Euler $e^{it} = \cos{t} + i\sin{t}$, on obtient

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

Ce qui nous donne les deux solutions réelles suivantes :

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Ces deux solutions sont linéairement indépendantes car leur rapport $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ n'est pas constant. Par le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), elles forment une base des solutions de l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$). La solution générale réelle est donc

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Notons toutefois que le cas des racines complexes conjuguées dans l'équation d'Euler-Cauchy n'a pas une grande importance pratique.

## Transformation en équation différentielle ordinaire linéaire homogène à coefficients constants
L'équation d'Euler-Cauchy peut être transformée en une [équation différentielle ordinaire linéaire homogène à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/) par un changement de variable.

En posant $x = e^t$, on obtient

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

ce qui transforme l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) en l'équation différentielle à coefficients constants suivante :

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

En résolvant cette équation ($\ref{eqn:substituted}$) par les méthodes des [équations différentielles ordinaires linéaires homogènes à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/), puis en substituant $t = \ln{x}$, on retrouve les [résultats obtenus précédemment](#forme-de-la-solution-générale-selon-le-signe-du-discriminant).
