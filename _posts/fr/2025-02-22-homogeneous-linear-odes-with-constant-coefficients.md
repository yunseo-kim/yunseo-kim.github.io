---
title: Équation différentielle linéaire homogène du second ordre à coefficients constants
description: Nous examinons la forme de la solution générale d'une équation différentielle linéaire homogène à coefficients constants selon le signe du discriminant de l'équation caractéristique.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Équation différentielle linéaire homogène du second ordre à coefficients constants : $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Équation caractéristique** : $\lambda^2 + a\lambda + b = 0$
> - La forme de la solution générale peut être divisée en trois cas selon le signe du discriminant $a^2 - 4b$ de l'équation caractéristique, comme indiqué dans le tableau
>
> | Cas | Racines de l'équation caractéristique | Base des solutions de l'EDO | Solution générale de l'EDO |
> | :---: | :---: | :---: | :---: |
> | I | Racines réelles distinctes<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Racine réelle double<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Racines complexes conjuguées<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$ <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prérequis
- [Équation de Bernoulli](/posts/Bernoulli-Equation/)
- [Équations différentielles linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- Formule d'Euler

## Équation caractéristique
Examinons l'équation différentielle linéaire homogène du second ordre à coefficients constants $a$ et $b$

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Ce type d'équation est important dans les applications des vibrations mécaniques et électriques.

Comme nous l'avons vu précédemment dans [l'équation de Bernoulli](/posts/Bernoulli-Equation/), la solution générale de l'équation différentielle linéaire du premier ordre à coefficient constant $k$

$$ y^\prime + ky = 0 $$

est la fonction exponentielle $y = ce^{-kx}$. (C'est le cas où $A=-k$, $B=0$ dans l'équation (4) de cet article)

Par conséquent, pour l'équation ($\ref{eqn:ode_with_constant_coefficients}$) qui a une forme similaire, nous pouvons d'abord essayer une solution de la forme

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Bien sûr, ce n'est qu'une supposition et il n'y a aucune garantie que la solution générale aura réellement cette forme. Cependant, si nous parvenons à trouver deux solutions linéairement indépendantes, quelle que soit leur forme, nous pourrons obtenir la solution générale grâce au [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), comme nous l'avons vu dans [les équations différentielles linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/#base-et-solution-générale).  
> Comme nous le verrons bientôt, il y a aussi [des cas où nous devons trouver une solution d'une forme différente](#ii-racine-réelle-double-lambda---cfraca2).
{: .prompt-info }

En substituant l'équation ($\ref{eqn:general_sol}$) et ses dérivées

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

dans l'équation ($\ref{eqn:ode_with_constant_coefficients}$), nous obtenons

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Par conséquent, si $\lambda$ est une solution de l'**équation caractéristique**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

alors la fonction exponentielle ($\ref{eqn:general_sol}$) est une solution de l'équation différentielle ($\ref{eqn:ode_with_constant_coefficients}$). En résolvant l'équation quadratique ($\ref{eqn:characteristic_eqn}$), nous obtenons

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a + \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

et à partir de cela, les deux fonctions

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

sont des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$).

Maintenant, nous pouvons diviser les cas en trois selon le signe du discriminant $a^2 - 4b$ de l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) :
- $a^2 - 4b > 0$ : deux racines réelles distinctes
- $a^2 - 4b = 0$ : une racine réelle double
- $a^2 - 4b < 0$ : deux racines complexes conjuguées

## Forme de la solution générale selon le signe du discriminant de l'équation caractéristique
### I. Deux racines réelles distinctes $\lambda_1$ et $\lambda_2$
Dans ce cas, la base des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sur tout intervalle est

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

et la solution générale correspondante est

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Racine réelle double $\lambda = -\cfrac{a}{2}$
Lorsque $a^2 - 4b = 0$, l'équation quadratique ($\ref{eqn:characteristic_eqn}$) n'a qu'une seule solution $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, et donc la seule solution de la forme $y = e^{\lambda x}$ que nous pouvons obtenir est

$$ y_1 = e^{-(a/2)x} $$

Pour obtenir une base, nous devons trouver une deuxième solution $y_2$ d'une forme différente et indépendante de $y_1$.

Dans cette situation, nous pouvons utiliser la [méthode de réduction d'ordre](/posts/homogeneous-linear-odes-of-second-order/#réduction-dordre) que nous avons vue précédemment. En posant la deuxième solution recherchée comme $y_2=uy_1$, et en substituant

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

dans l'équation ($\ref{eqn:ode_with_constant_coefficients}$), nous obtenons

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

En regroupant les termes en $u^{\prime\prime}$, $u^\prime$, et $u$, nous obtenons

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Ici, comme $y_1$ est une solution de l'équation ($\ref{eqn:ode_with_constant_coefficients}$), l'expression entre les dernières parenthèses est égale à 0, et

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

donc l'expression entre les premières parenthèses est aussi égale à 0. Il ne reste donc que $u^{\prime\prime}y_1 = 0$, d'où $u^{\prime\prime}=0$. En intégrant deux fois, nous obtenons $u = c_1x + c_2$, où les constantes d'intégration $c_1$ et $c_2$ peuvent prendre n'importe quelle valeur. Nous pouvons simplement choisir $c_1=1$ et $c_2=0$ pour avoir $u=x$. Alors $y_2 = uy_1 = xy_1$, et comme $y_1$ et $y_2$ sont linéairement indépendants, ils forment une base. Donc, dans le cas où l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) a une racine double, la base des solutions de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sur tout intervalle est

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

et la solution générale correspondante est

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Racines complexes conjuguées $-\cfrac{1}{2}a + i\omega$ et $-\cfrac{1}{2}a - i\omega$
Dans ce cas, $a^2 - 4b < 0$ et $\sqrt{-1} = i$, donc à partir de l'équation ($\ref{eqn:lambdas}$),

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

Définissons ici le nombre réel $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Avec $\omega$ défini comme ci-dessus, les solutions de l'équation caractéristique ($\ref{eqn:characteristic_eqn}$) sont les racines complexes conjuguées $\lambda = -\cfrac{1}{2}a \pm i\omega$, et les deux solutions complexes correspondantes de l'équation ($\ref{eqn:ode_with_constant_coefficients}$) sont

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Cependant, dans ce cas aussi, nous pouvons obtenir une base de solutions réelles comme suit.

La formule d'Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

et l'équation obtenue en remplaçant $t$ par $-t$ dans l'équation ci-dessus

$$ e^{-it} = \cos t - i\sin t $$

nous donnent, en additionnant et soustrayant ces deux équations :

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

La fonction exponentielle complexe $e^z$ d'une variable complexe $z = r + it$ avec partie réelle $r$ et partie imaginaire $it$ peut être définie en utilisant les fonctions réelles $e^r$, $\cos t$ et $\sin t$ comme suit :

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + \sin t) \label{eqn:complex_exp}\tag{10}$$

En posant $r=-\cfrac{1}{2}ax$ et $t=\omega x$, nous pouvons écrire :

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Par le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), la somme et le produit par une constante de ces solutions complexes sont également des solutions. Donc, en additionnant ces deux équations membre à membre et en multipliant les deux côtés par $\cfrac{1}{2}$, nous obtenons la première solution réelle $y_1$ :

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

De la même manière, en soustrayant la deuxième équation de la première et en multipliant les deux côtés par $\cfrac{1}{2i}$, nous obtenons la deuxième solution réelle $y_2$ :

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Comme $\cfrac{y_1}{y_2} = \cot{\omega x}$ n'est pas une constante, $y_1$ et $y_2$ sont linéairement indépendants sur tout intervalle et forment donc une base des solutions réelles de l'équation ($\ref{eqn:ode_with_constant_coefficients}$). À partir de cela, nous obtenons la solution générale

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ sont des constantes arbitraires)} \label{eqn:general_sol_3}\tag{13}$$
