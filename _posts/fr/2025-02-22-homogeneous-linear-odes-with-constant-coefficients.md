---
title: "EDO linéaires homogènes du second ordre à coefficients constants"
description: "Découvrez comment la forme de la solution générale d'une EDO linéaire homogène à coefficients constants dépend du signe du discriminant de son équation caractéristique."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## En bref
> - EDO linéaire homogène du second ordre à coefficients constants : $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Équation caractéristique** : $\lambda^2 + a\lambda + b = 0$
> - Selon le signe du discriminant $a^2 - 4b$ de l'équation caractéristique, la forme de la solution générale peut être divisée en trois cas, comme le montre le tableau suivant :
>
> | Cas | Solutions de l'équation caractéristique | Base de solutions de l'EDO | Solution générale de l'EDO |
> | :---: | :---: | :---: | :---: |
> | I | Deux racines réelles distinctes<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Une racine réelle double<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Racines complexes conjuguées<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prérequis
- [Équation de Bernoulli](/posts/Bernoulli-Equation/)
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- Formule d'Euler

## Équation caractéristique
Considérons l'équation différentielle ordinaire linéaire homogène du second ordre à coefficients constants $a$ et $b$

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Ce type d'équation a des applications importantes dans les vibrations mécaniques et électriques.

Nous avons déjà trouvé la solution générale de l'équation logistique dans l'article sur l'[équation de Bernoulli](/posts/Bernoulli-Equation/). Selon cet article, la solution de l'équation différentielle ordinaire linéaire du premier ordre à coefficient constant $k$

$$ y^\prime + ky = 0 $$

est la fonction exponentielle $y = ce^{-kx}$. (C'est le cas où $A=-k$ et $B=0$ dans l'équation (4) de cet article).

Par conséquent, pour une équation de forme similaire comme ($\ref{eqn:ode_with_constant_coefficients}$), nous pouvons d'abord essayer une solution de la forme

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Bien sûr, ce n'est qu'une supposition, et il n'y a aucune garantie que la solution générale aura réellement cette forme. Cependant, si nous parvenons à trouver deux solutions linéairement indépendantes, quelles qu'elles soient, nous pouvons trouver la solution générale grâce au [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), comme nous l'avons vu dans l'article sur les [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/#base-et-solution-générale).  
> Comme nous le verrons bientôt, il existe également des cas où nous devons trouver [une solution d'une forme différente](#ii-une-racine-réelle-double-lambda--cfraca2).
{: .prompt-info }

En substituant l'équation ($\ref{eqn:general_sol}$) et ses dérivées

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

dans l'équation ($\ref{eqn:ode_with_constant_coefficients}$), on obtient

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Par conséquent, si $\lambda$ est une solution de l'**équation caractéristique**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

alors la fonction exponentielle ($\ref{eqn:general_sol}$) est une solution de l'EDO ($\ref{eqn:ode_with_constant_coefficients}$). En résolvant l'équation du second degré ($\ref{eqn:characteristic_eqn}$), on obtient

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

et de là, les deux fonctions

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

sont des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$).

> Les termes **équation caractéristique** et **équation auxiliaire** sont souvent utilisés de manière interchangeable ; ils ont exactement la même signification. L'un ou l'autre terme peut être utilisé.
{: .prompt-tip }

Maintenant, nous pouvons diviser la situation en trois cas selon le signe du discriminant $a^2 - 4b$ de l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) :
- $a^2 - 4b > 0$ : Deux racines réelles distinctes
- $a^2 - 4b = 0$ : Une racine réelle double
- $a^2 - 4b < 0$ : Racines complexes conjuguées

## Forme de la solution générale selon le signe du discriminant de l'équation caractéristique
### I. Deux racines réelles distinctes $\lambda_1$ et $\lambda_2$
Dans ce cas, une base de solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sur n'importe quel intervalle est

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

et la solution générale correspondante est

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Une racine réelle double $\lambda = -\cfrac{a}{2}$
Si $a^2 - 4b = 0$, l'équation du second degré ($\ref{eqn:characteristic_eqn}$) n'a qu'une seule solution $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$. Par conséquent, la seule solution de la forme $y = e^{\lambda x}$ que nous pouvons obtenir est

$$ y_1 = e^{-(a/2)x} $$

Pour obtenir une base, nous devons trouver une deuxième solution $y_2$ d'une forme différente, qui soit linéairement indépendante de $y_1$.

Dans cette situation, nous pouvons utiliser la [réduction de l'ordre](/posts/homogeneous-linear-odes-of-second-order/#réduction-de-lordre) que nous avons examinée précédemment. Posons la deuxième solution que nous cherchons comme $y_2=uy_1$, et

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

en substituant dans l'équation ($\ref{eqn:ode_with_constant_coefficients}$), on obtient

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

En regroupant les termes en $u^{\prime\prime}$, $u^\prime$ et $u$, on obtient

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Ici, comme $y_1$ est une solution de l'équation ($\ref{eqn:ode_with_constant_coefficients}$), l'expression dans la dernière parenthèse est nulle. De plus, comme

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

l'expression dans la première parenthèse est également nulle. Il ne reste donc que $u^{\prime\prime}y_1 = 0$, d'où $u^{\prime\prime}=0$. En intégrant deux fois, on obtient $u = c_1x + c_2$. Comme les constantes d'intégration $c_1$ et $c_2$ peuvent être quelconques, nous pouvons simplement choisir $c_1=1$ et $c_2=0$ pour obtenir $u=x$. Alors $y_2 = uy_1 = xy_1$, et comme $y_1$ et $y_2$ sont linéairement indépendantes, elles forment une base. Par conséquent, lorsque l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) a une racine double, une base de solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sur n'importe quel intervalle est

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

et la solution générale correspondante est

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Racines complexes conjuguées $-\cfrac{1}{2}a + i\omega$ et $-\cfrac{1}{2}a - i\omega$
Dans ce cas, $a^2 - 4b < 0$, et comme $\sqrt{-1} = i$, l'équation ($\ref{eqn:lambdas}$) donne

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

où nous définissons le nombre réel $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

En définissant $\omega$ comme ci-dessus, les solutions de l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) sont les racines complexes conjuguées $\lambda = -\cfrac{1}{2}a \pm i\omega$. Les deux solutions complexes correspondantes de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sont

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Cependant, même dans ce cas, nous pouvons obtenir une base de solutions réelles comme suit.

À partir de la formule d'Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

et de l'équation obtenue en remplaçant $t$ par $-t$ dans la formule ci-dessus

$$ e^{-it} = \cos t - i\sin t $$

en additionnant et soustrayant ces deux équations membre à membre, on obtient ce qui suit :

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

La fonction exponentielle complexe $e^z$ d'une variable complexe $z = r + it$ avec une partie réelle $r$ et une partie imaginaire $it$ peut être définie en utilisant les fonctions réelles $e^r$, $\cos t$ et $\sin t$ comme suit :

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Ici, en posant $r=-\cfrac{1}{2}ax$ et $t=\omega x$, nous pouvons écrire :

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Selon le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), la somme et les multiples par une constante des solutions complexes ci-dessus sont également des solutions. Par conséquent, en additionnant les deux équations membre à membre et en multipliant les deux côtés par $\cfrac{1}{2}$, nous pouvons obtenir la première solution réelle $y_1$ comme suit :

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

De la même manière, en soustrayant la deuxième équation de la première membre à membre et en multipliant les deux côtés par $\cfrac{1}{2i}$, nous pouvons obtenir la deuxième solution réelle $y_2$.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Puisque $\cfrac{y_1}{y_2} = \cot{\omega x}$, qui n'est pas une constante, $y_1$ et $y_2$ sont linéairement indépendantes sur tout intervalle et forment donc une base de solutions réelles pour l'équation ($\ref{eqn:ode_with_constant_coefficients}$). De là, nous obtenons la solution générale

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ sont des constantes arbitraires)} \label{eqn:general_sol_3}\tag{13}$$


