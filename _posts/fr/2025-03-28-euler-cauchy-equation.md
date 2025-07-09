---
title: "Équation d'Euler-Cauchy"
description: "Découvrez comment la forme de la solution générale de l'équation d'Euler-Cauchy varie selon le signe du discriminant de son équation auxiliaire."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Équation d'Euler-Cauchy : $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Équation auxiliaire** : $m^2 + (a-1)m + b = 0$
> - Selon le signe du discriminant de l'équation auxiliaire, $(1-a)^2 - 4b$, la forme de la solution générale peut être classée en trois cas, comme le montre le tableau suivant :
>
> | Cas | Solutions de l'équation auxiliaire | Base de solutions de l'équation d'Euler-Cauchy | Solution générale de l'équation d'Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Deux racines réelles distinctes<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Racine réelle double<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Racines complexes conjuguées<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prérequis
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Formule d'Euler

## Équation auxiliaire
L'**équation d'Euler-Cauchy** est une équation différentielle ordinaire de la forme

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

où $a$ et $b$ sont des constantes données et $y(x)$ est la fonction inconnue. En substituant

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

dans l'équation ($\ref{eqn:euler_cauchy_eqn}$), on obtient

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

c'est-à-dire

$$ [m(m-1) + am + b]x^m = 0 $$

De là, on déduit l'équation auxiliaire

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

et la condition nécessaire et suffisante pour que $y=x^m$ soit une solution de l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) est que $m$ soit une solution de l'équation auxiliaire ($\ref{eqn:auxiliary_eqn}$).

En résolvant l'équation du second degré ($\ref{eqn:auxiliary_eqn}$), on trouve les solutions

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

et de là, les deux fonctions

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

sont des solutions de l'équation ($\ref{eqn:euler_cauchy_eqn}$).

Comme pour les [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/), on peut distinguer trois cas selon le signe du discriminant de l'équation auxiliaire ($\ref{eqn:auxiliary_eqn}$), $(1-a)^2 - 4b$.
- $(1-a)^2 - 4b > 0$: Deux racines réelles distinctes
- $(1-a)^2 - 4b = 0$: Racine réelle double
- $(1-a)^2 - 4b < 0$: Racines complexes conjuguées

## Forme de la solution générale selon le signe du discriminant de l'équation auxiliaire
### I. Deux racines réelles distinctes $m_1$ et $m_2$
Dans ce cas, une base de solutions de l'équation ($\ref{eqn:euler_cauchy_eqn}$) sur un intervalle quelconque est

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

et la solution générale correspondante est

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Racine réelle double $m = \cfrac{1-a}{2}$
Dans le cas où $(1-a)^2 - 4b = 0$, c'est-à-dire $b=\cfrac{(1-a)^2}{4}$, l'équation du second degré ($\ref{eqn:auxiliary_eqn}$) n'a qu'une seule solution $m = m_1 = m_2 = \cfrac{1-a}{2}$, et donc la seule solution de la forme $y = x^m$ que l'on peut obtenir est

$$ y_1 = x^{(1-a)/2} $$

et l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) prend la forme

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Cherchons maintenant une autre solution linéairement indépendante, $y_2$, en utilisant la [réduction de l'ordre](/posts/homogeneous-linear-odes-of-second-order/#réduction-de-lordre).

En posant la seconde solution que nous cherchons $y_2=uy_1$, on obtient

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Puisque $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

et en intégrant, on obtient $u = \ln x$.

Par conséquent, $y_2 = uy_1 = y_1 \ln x$, et comme leur quotient n'est pas une constante, $y_1$ et $y_2$ sont linéairement indépendantes. La solution générale correspondant à la base $y_1$ et $y_2$ est

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Racines complexes conjuguées
Dans ce cas, les solutions de l'équation auxiliaire ($\ref{eqn:auxiliary_eqn}$) sont $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, et les deux solutions complexes correspondantes de l'équation ($\ref{eqn:euler_cauchy_eqn}$) peuvent s'écrire comme suit, en utilisant le fait que $x=e^{\ln x}$.

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

En posant $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ et en utilisant la formule d'Euler $e^{it} = \cos{t} + i\sin{t}$, on peut voir que

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

et de là, on obtient les deux solutions réelles suivantes

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Leur quotient, $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$, n'étant pas une constante, les deux solutions ci-dessus sont linéairement indépendantes et forment donc une base pour l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) selon le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition). De là, on obtient la solution générale réelle suivante.

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Cependant, le cas où l'équation auxiliaire de l'équation d'Euler-Cauchy a des racines complexes conjuguées n'est pas d'une grande importance pratique.

## Transformation en EDO linéaire homogène du second ordre à coefficients constants
L'équation d'Euler-Cauchy peut être transformée en une [EDO linéaire homogène du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/) par un changement de variable.

En posant le changement de variable $x = e^t$, on a

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

ce qui transforme l'équation d'Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) en l'EDO linéaire homogène à coefficients constants en $t$ suivante.

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

En résolvant l'équation ($\ref{eqn:substituted}$) pour $t$ en utilisant la méthode de résolution des [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/), puis en retransformant la solution obtenue en une solution en $x$ à l'aide de $t = \ln{x}$, on obtient [les mêmes résultats que ceux examinés précédemment](#forme-de-la-solution-générale-selon-le-signe-du-discriminant-de-léquation-auxiliaire).
