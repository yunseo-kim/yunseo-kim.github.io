---
title: "EDO linéaire homogène du second ordre à coefficients constants"
description: "Selon le signe du discriminant de l'équation caractéristique, nous examinons la forme que prend la solution générale de l'EDO linéaire homogène à coefficients constants dans chaque cas."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - EDO linéaire homogène du second ordre à coefficients constants : $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Équation caractéristique** : $\lambda^2 + a\lambda + b = 0$
> - Selon le signe du discriminant $a^2 - 4b$ de l'équation caractéristique, la forme de la solution générale peut être divisée en trois cas comme indiqué dans le tableau
>
> | Cas | Solutions de l'équation caractéristique | Base des solutions de l'EDO | Solution générale de l'EDO |
> | :---: | :---: | :---: | :---: |
> | I | Racines réelles distinctes<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Racine réelle double<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Racines complexes conjuguées<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prérequis
- [Équation de Bernoulli](/posts/Bernoulli-Equation/)
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- Formule d'Euler

## Équation caractéristique
Considérons l'EDO linéaire homogène du second ordre où les coefficients $a$ et $b$ sont des constantes

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Ce type d'équation trouve des applications importantes dans les vibrations mécaniques et électriques.

Nous avons précédemment trouvé la solution générale de l'équation logistique dans [l'équation de Bernoulli](/posts/Bernoulli-Equation/), et selon cela, l'EDO linéaire du premier ordre avec coefficient constant $k$

$$ y^\prime + ky = 0 $$

a pour solution la fonction exponentielle $y = ce^{-kx}$. (Dans l'équation (4) de cet article, cas où $A=-k$, $B=0$)

Par conséquent, pour l'équation ($\ref{eqn:ode_with_constant_coefficients}$) de forme similaire, nous pouvons d'abord essayer une solution de la forme

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Bien sûr, ceci n'est qu'une conjecture, et il n'y a aucune garantie que la solution générale soit vraiment de cette forme. Cependant, tant que nous trouvons deux solutions linéairement indépendantes, nous pouvons obtenir la solution générale grâce au [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition) comme nous l'avons vu dans [les EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/#base-et-solution-générale).  
> Comme nous le verrons bientôt, [il y a des cas où nous devons trouver des solutions d'une forme différente](#ii-racine-réelle-double-lambda---cfraca2).
{: .prompt-info }

En substituant l'équation ($\ref{eqn:general_sol}$) et ses dérivées

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

dans l'équation ($\ref{eqn:ode_with_constant_coefficients}$), nous obtenons

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Par conséquent, si $\lambda$ est une solution de l'**équation caractéristique**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

alors la fonction exponentielle ($\ref{eqn:general_sol}$) est une solution de l'EDO ($\ref{eqn:ode_with_constant_coefficients}$). En résolvant l'équation du second degré ($\ref{eqn:characteristic_eqn}$), nous obtenons

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

et de là, les deux fonctions

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

deviennent des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$).

> L'**équation caractéristique** et l'**équation auxiliaire** sont souvent utilisées de manière interchangeable, car elles ont exactement la même signification. Vous pouvez utiliser l'un ou l'autre terme.
{: .prompt-tip }

Maintenant, nous pouvons diviser en trois cas selon le signe du discriminant $a^2 - 4b$ de l'équation caractéristique ($\ref{eqn:characteristic_eqn}$).
- $a^2 - 4b > 0$ : deux racines réelles distinctes
- $a^2 - 4b = 0$ : racine réelle double
- $a^2 - 4b < 0$ : racines complexes conjuguées

## Forme de la solution générale selon le signe du discriminant de l'équation caractéristique
### I. Deux racines réelles distinctes $\lambda_1$ et $\lambda_2$
Dans ce cas, la base des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sur un intervalle arbitraire est

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

et la solution générale correspondante est

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Racine réelle double $\lambda = -\cfrac{a}{2}$
Lorsque $a^2 - 4b = 0$, l'équation du second degré ($\ref{eqn:characteristic_eqn}$) n'a qu'une seule solution $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, et par conséquent, nous ne pouvons obtenir qu'une seule solution de la forme $y = e^{\lambda x}$

$$ y_1 = e^{-(a/2)x} $$

Pour obtenir une base, nous devons trouver une deuxième solution $y_2$ indépendante de $y_1$ et d'une forme différente.

Dans cette situation, nous pouvons utiliser la [réduction d'ordre](/posts/homogeneous-linear-odes-of-second-order/#réduction-dordre) que nous avons étudiée précédemment. En posant la deuxième solution recherchée comme $y_2=uy_1$, et

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

en substituant dans l'équation ($\ref{eqn:ode_with_constant_coefficients}$), nous obtenons

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

En regroupant les termes en $u^{\prime\prime}$, $u^\prime$, $u$, nous obtenons

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Ici, puisque $y_1$ est une solution de l'équation ($\ref{eqn:ode_with_constant_coefficients}$), l'expression dans la dernière parenthèse est égale à $0$, et

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

donc l'expression dans la première parenthèse est également égale à $0$. Par conséquent, il ne reste que $u^{\prime\prime}y_1 = 0$, d'où $u^{\prime\prime}=0$. En intégrant deux fois, nous obtenons $u = c_1x + c_2$, et puisque les constantes d'intégration $c_1$ et $c_2$ peuvent prendre n'importe quelle valeur, nous pouvons simplement choisir $c_1=1$, $c_2=0$ pour poser $u=x$. Alors $y_2 = uy_1 = xy_1$, et puisque $y_1$ et $y_2$ sont linéairement indépendantes, elles forment une base. Par conséquent, lorsque l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) a une racine double, la base des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sur un intervalle arbitraire est

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

et la solution générale correspondante est

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Racines complexes conjuguées $-\cfrac{1}{2}a + i\omega$ et $-\cfrac{1}{2}a - i\omega$
Dans ce cas, $a^2 - 4b < 0$ et $\sqrt{-1} = i$, donc dans l'équation ($\ref{eqn:lambdas}$)

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

et définissons le nombre réel $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

En définissant $\omega$ comme ci-dessus, les solutions de l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) deviennent les racines complexes conjuguées $\lambda = -\cfrac{1}{2}a \pm i\omega$, et les deux solutions complexes correspondantes de l'équation ($\ref{eqn:ode_with_constant_coefficients}$)

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

sont obtenues. Cependant, dans ce cas aussi, nous pouvons obtenir une base de solutions réelles (non imaginaires) comme suit.

La formule d'Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

et en substituant $-t$ à la place de $t$ dans l'équation ci-dessus

$$ e^{-it} = \cos t - i\sin t $$

en additionnant et soustrayant ces deux équations membre à membre, nous obtenons

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

La fonction exponentielle complexe $e^z$ d'une variable complexe $z = r + it$ avec partie réelle $r$ et partie imaginaire $it$ peut être définie en utilisant les fonctions réelles $e^r$, $\cos t$ et $\sin t$ comme suit.

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

En posant $r=-\cfrac{1}{2}ax$, $t=\omega x$, nous pouvons écrire

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Par le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), les sommes et produits par des constantes des solutions complexes ci-dessus sont également des solutions. Par conséquent, en additionnant les deux équations membre à membre et en multipliant les deux côtés par $\cfrac{1}{2}$, nous pouvons obtenir la première solution réelle $y_1$ comme suit.

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

De même, en soustrayant la deuxième équation de la première membre à membre et en multipliant les deux côtés par $\cfrac{1}{2i}$, nous pouvons obtenir la deuxième solution réelle $y_2$.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Puisque $\cfrac{y_1}{y_2} = \cot{\omega x}$ et que ce n'est pas une constante, $y_1$ et $y_2$ sont linéairement indépendantes sur tout intervalle et forment donc une base des solutions réelles de l'équation ($\ref{eqn:ode_with_constant_coefficients}$). De là, nous obtenons la solution générale

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ sont des constantes arbitraires)} \label{eqn:general_sol_3}\tag{13}$$
