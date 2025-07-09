---
title: "Wronskien, Existence et Unicité de la Solution"
description: "Pour une EDO linéaire homogène du second ordre à coefficients variables continus, nous explorons le théorème d'existence et d'unicité, et l'utilisation du Wronskien pour déterminer la dépendance linéaire des solutions. Nous montrons que sa solution générale inclut toutes les solutions possibles."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Pour une équation différentielle ordinaire (EDO) linéaire homogène du second ordre avec des coefficients variables $p$ et $q$ continus sur un intervalle $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> et les conditions initiales
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> les quatre théorèmes suivants sont valables.
> 1. **Théorème d'existence et d'unicité pour les problèmes à valeur initiale** : Le problème à valeur initiale constitué de l'équation et des conditions initiales données possède une solution unique $y(x)$ sur l'intervalle $I$.
> 2. **Critère de dépendance/indépendance linéaire des solutions à l'aide du Wronskien** : Pour deux solutions $y_1$ et $y_2$ de l'équation, si il existe un $x_0$ dans l'intervalle $I$ où la valeur du **Wronskien** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ est $0$, alors les deux solutions sont linéairement dépendantes. De plus, s'il existe un $x_1$ dans l'intervalle $I$ où $W\neq 0$, alors les deux solutions sont linéairement indépendantes.
> 3. **Existence de la solution générale** : L'équation donnée possède une solution générale sur l'intervalle $I$.
> 4. **Non-existence de solutions singulières** : Cette solution générale inclut toutes les solutions de l'équation (c'est-à-dire qu'il n'existe pas de solutions singulières).
{: .prompt-info }

## Prérequis
- [Résolution des EDOs linéaires du premier ordre](/posts/Solution-of-First-Order-Linear-ODE/)
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs linéaires homogènes à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matrice inverse, matrice singulière et déterminant

## Équation différentielle ordinaire linéaire homogène à coefficients variables continus
Nous avons précédemment examiné la solution générale des [EDOs linéaires homogènes à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/) et de l'[équation d'Euler-Cauchy](/posts/euler-cauchy-equation/).
Dans cet article, nous étendons la discussion à un cas plus général, en examinant l'existence et la forme de la solution générale d'une EDO linéaire homogène du second ordre avec des **coefficients variables** continus arbitraires $p$ et $q$ :

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

De plus, nous examinerons l'unicité du [problème de valeur initiale](/posts/homogeneous-linear-odes-of-second-order/#problème-de-valeur-initiale-et-conditions-initiales) composé de l'EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et des deux conditions initiales suivantes :

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Pour anticiper la conclusion, le point essentiel de ce que nous allons aborder ici est que les EDO <u>linéaires</u> à coefficients continus n'ont pas de *solution singulière* (une solution qui ne peut être obtenue à partir de la solution générale).

## Théorème d'existence et d'unicité pour les problèmes à valeur initiale
> **Théorème d'existence et d'unicité pour les problèmes à valeur initiale**  
> Si $p(x)$ et $q(x)$ sont des fonctions continues sur un intervalle ouvert $I$, et si $x_0$ est dans l'intervalle $I$, alors le problème à valeur initiale constitué des équations ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et ($\ref{eqn:initial_conditions}$) possède une solution unique $y(x)$ sur l'intervalle $I$.
{: .prompt-info }

La démonstration de l'existence ne sera pas traitée ici ; nous nous concentrerons uniquement sur la démonstration de l'unicité. En général, prouver l'unicité est plus simple que de prouver l'existence.  
Si la démonstration ne vous intéresse pas, vous pouvez sauter cette partie et passer à la section [Dépendance et indépendance linéaires des solutions](#dépendance-et-indépendance-linéaires-des-solutions).

### Démonstration de l'unicité
Supposons que le problème à valeur initiale composé de l'EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et des conditions initiales ($\ref{eqn:initial_conditions}$) ait deux solutions $y_1(x)$ et $y_2(x)$ sur l'intervalle $I$. Si nous pouvons montrer que la différence de ces deux solutions

$$ y(x) = y_1(x) - y_2(x) $$

est identiquement nulle sur l'intervalle $I$, cela signifie que $y_1 \equiv y_2$ sur $I$, ce qui prouve l'unicité de la solution.

Puisque l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) est une EDO linéaire homogène, $y$, qui est une combinaison linéaire de $y_1$ et $y_2$, est une solution de l'équation sur $I$. Comme $y_1$ et $y_2$ satisfont les mêmes conditions initiales ($\ref{eqn:initial_conditions}$), $y$ satisfait les conditions

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Considérons maintenant la fonction

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

et sa dérivée

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

De l'EDO, nous obtenons

$$ y^{\prime\prime} = -py^{\prime} - qy $$

En substituant cela dans l'expression de $z^{\prime}$, nous avons

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Puisque $y$ et $y^{\prime}$ sont des nombres réels,

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

De cela et de la définition de $z$, nous obtenons deux inégalités :

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

De ces deux inégalités, nous pouvons voir que $|2yy^{\prime}|\leq z$, et donc pour le dernier terme de l'équation ($\ref{eqn:z_prime}$), l'inégalité suivante est valable :

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

En utilisant ce résultat ainsi que $-p \leq |p|$, et en appliquant l'inégalité ($\ref{eqn:inequalities}$a) au terme $2yy^{\prime}$ de l'équation ($\ref{eqn:z_prime}$), nous obtenons

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Puisque ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, nous avons

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

En posant la fonction entre parenthèses $h = 1 + 2|p| + |q|$, nous avons

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

De la même manière, à partir des équations ($\ref{eqn:z_prime}$) et ($\ref{eqn:inequalities}$), nous obtenons

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Ces deux inégalités ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$) sont équivalentes à l'inégalité suivante :

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

Les [facteurs intégrants](/posts/Solution-of-First-Order-Linear-ODE/#équation-différentielle-ordinaire-linéaire-non-homogène) pour les membres de gauche des deux équations sont

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{et} \qquad F_2 = e^{\int h(x)\ dx} $$

Comme $h$ est continue, l'intégrale indéfinie $\int h(x)\ dx$ existe, et puisque $F_1$ et $F_2$ sont positifs, de l'équation ($\ref{eqn:inequalities_7}$) nous obtenons

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Cela signifie que sur l'intervalle $I$, $F_1 z$ est non croissante et $F_2 z$ est non décroissante. Par l'équation ($\ref{eqn:initial_conditions_*}$), nous avons $z(x_0) = 0$, donc

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Enfin, en divisant les deux côtés des inégalités par les quantités positives $F_1$ et $F_2$, nous pouvons montrer l'unicité de la solution comme suit :

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dépendance et indépendance linéaires des solutions
Rappelons brièvement ce que nous avons abordé dans [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/#base-et-solution-générale). La solution générale sur un intervalle ouvert $I$ est construite à partir d'une **base** $y_1$, $y_2$ sur $I$, c'est-à-dire une paire de solutions linéairement indépendantes. Ici, le fait que $y_1$ et $y_2$ soient **linéairement indépendantes** sur l'intervalle $I$ signifie que pour tout $x$ dans l'intervalle, la condition suivante est satisfaite :

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ et }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Si ce qui précède n'est pas satisfait, et que $k_1y_1(x) + k_2y_2(x) = 0$ est vrai pour au moins un $k_1$ ou $k_2$ non nul, alors $y_1$ et $y_2$ sont **linéairement dépendantes** sur l'intervalle $I$. Dans ce cas, pour tout $x$ de l'intervalle $I$,

$$ \text{(a) } y_1 = ky_2 \quad \text{ou} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

et $y_1$ et $y_2$ sont proportionnelles.

Examinons maintenant le critère suivant pour la dépendance/indépendance linéaire des solutions.

> **Critère de dépendance/indépendance linéaire des solutions à l'aide du Wronskien**  
> **i.** Si l'EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a des coefficients continus $p(x)$ et $q(x)$ sur un intervalle ouvert $I$, alors une condition nécessaire et suffisante pour que deux solutions $y_1$ et $y_2$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) soient linéairement dépendantes sur $I$ est que leur *déterminant de Wronski*, ou plus simplement **Wronskien**, le déterminant suivant
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> soit nul en un certain point $x_0$ de l'intervalle $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ et } y_2 \text{ sont linéairement dépendantes} $$
>
> **ii.** Si $W=0$ en un point $x=x_0$ de l'intervalle $I$, alors $W=0$ pour tout $x$ dans l'intervalle $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> En d'autres termes, s'il existe un $x_1$ dans l'intervalle $I$ tel que $W\neq 0$, alors $y_1$ et $y_2$ sont linéairement indépendantes sur cet intervalle $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ et } y_2 \text{ sont linéairement indépendantes}
> \end{align*}$$
>
{: .prompt-info }

> Le Wronskien a été introduit pour la première fois par le mathématicien polonais Józef Maria Hoene-Wroński, et a été nommé ainsi après sa mort en 11882 EH par le mathématicien écossais Sir Thomas Muir.
{: .prompt-tip }

### Démonstration
#### i. (a)
Supposons que $y_1$ et $y_2$ soient linéairement dépendantes sur l'intervalle $I$. Alors, l'équation ($\ref{eqn:linearly_dependent}$a) ou ($\ref{eqn:linearly_dependent}$b) est valable sur $I$. Si l'équation ($\ref{eqn:linearly_dependent}$a) est valable, alors

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = (ky_2)y_2^{\prime} - y_2(ky_2^{\prime}) = 0 $$

et de même, si l'équation ($\ref{eqn:linearly_dependent}$b) est valable,

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1(ly_1^{\prime}) - (ly_1)y_1^{\prime} = 0 $$

donc nous pouvons confirmer que le Wronskien $W(y_1, y_2)=0$ <u>pour tout $x$ dans l'intervalle $I$</u>.

#### i. (b)
Inversement, supposons que $W(y_1, y_2)=0$ pour un certain $x = x_0$. Nous allons montrer que $y_1$ et $y_2$ sont linéairement dépendantes sur l'intervalle $I$. Considérons le système d'équations linéaires pour les inconnues $k_1$, $k_2$ :

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Cela peut être exprimé sous forme d'équation vectorielle :

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

La matrice des coefficients de cette équation vectorielle est

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

et le déterminant de cette matrice est précisément $W(y_1(x_0), y_2(x_0))$. Puisque $\det(A) = W=0$, $A$ est une **matrice singulière** qui n'a pas de **matrice inverse**, et donc le système d'équations ($\ref{eqn:linear_system}$) a une solution non triviale $(c_1, c_2)$ autre que le vecteur nul $(0,0)$, où au moins l'un des $k_1$ et $k_2$ n'est pas nul. Introduisons maintenant la fonction

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Puisque l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) est linéaire et homogène, selon le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), cette fonction est une solution de ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$. De l'équation ($\ref{eqn:linear_system}$), nous pouvons voir que cette solution satisfait les conditions initiales $y(x_0)=0$, $y^{\prime}(x_0)=0$.

D'autre part, il existe une solution triviale $y^\* \equiv 0$ qui satisfait les mêmes conditions initiales $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Puisque les coefficients $p$ et $q$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sont continus, l'unicité de la solution est garantie par le [Théorème d'existence et d'unicité pour les problèmes à valeur initiale](#théorème-dexistence-et-dunicité-pour-les-problèmes-à-valeur-initiale), et donc $y \equiv y^\*$. C'est-à-dire, sur l'intervalle $I$,

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Puisqu'au moins l'un de $c_1$ et $c_2$ n'est pas nul, la condition ($\ref{eqn:linearly_independent}$) n'est pas satisfaite, ce qui signifie que $y_1$ et $y_2$ sont linéairement dépendantes sur l'intervalle $I$.

#### ii.
Si $W(x_0)=0$ en un point $x_0$ de l'intervalle $I$, alors par [i.(b)](#i-b), $y_1$ et $y_2$ sont linéairement dépendantes sur $I$, et alors par [i.(a)](#i-a), $W\equiv 0$. Par conséquent, s'il existe ne serait-ce qu'un seul $x_1$ dans l'intervalle $I$ tel que $W(x_1)\neq 0$, alors $y_1$ et $y_2$ sont linéairement indépendantes. $\blacksquare$

## La solution générale inclut toutes les solutions
### Existence de la solution générale
> Si $p(x)$ et $q(x)$ sont continus sur un intervalle ouvert $I$, alors l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) possède une solution générale sur l'intervalle $I$.
{: .prompt-info }

#### Démonstration
Selon le [Théorème d'existence et d'unicité pour les problèmes à valeur initiale](#théorème-dexistence-et-dunicité-pour-les-problèmes-à-valeur-initiale), l'EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) possède une solution $y_1(x)$ sur l'intervalle $I$ satisfaisant les conditions initiales

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

et une solution $y_2(x)$ sur l'intervalle $I$ satisfaisant les conditions initiales

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

Le Wronskien de ces deux solutions en $x=x_0$ a une valeur non nulle :

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Par conséquent, selon le [critère de dépendance/indépendance linéaire des solutions à l'aide du Wronskien](#dépendance-et-indépendance-linéaires-des-solutions), $y_1$ et $y_2$ sont linéairement indépendantes sur l'intervalle $I$. Ces deux solutions forment donc une base de solutions pour l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$, et une solution générale $y = c_1y_1 + c_2y_2$ avec des constantes arbitraires $c_1$, $c_2$ existe nécessairement sur l'intervalle $I$. $\blacksquare$

### Non-existence de solutions singulières
> Si l'EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a des coefficients continus $p(x)$ et $q(x)$ sur un intervalle ouvert $I$, alors toute solution $y=Y(x)$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$ est de la forme
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> où $y_1$, $y_2$ est une base de solutions de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$ et $C_1$, $C_2$ sont des constantes appropriées.  
> C'est-à-dire que l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) n'a pas de **solution singulière**, qui est une solution ne pouvant être obtenue à partir de la solution générale.
{: .prompt-info }

#### Démonstration
Soit $y=Y(x)$ une solution quelconque de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$. Par le [théorème d'existence de la solution générale](#existence-de-la-solution-générale), l'EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a une solution générale sur l'intervalle $I$ :

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Nous devons maintenant montrer que pour tout $Y(x)$, il existe des constantes $c_1$, $c_2$ telles que $y(x)=Y(x)$ sur l'intervalle $I$. Montrons d'abord que nous pouvons trouver des valeurs de $c_1$, $c_2$ telles que $y(x_0)=Y(x_0)$ et $y^{\prime}(x_0)=Y^{\prime}(x_0)$ pour un $x_0$ arbitraire dans l'intervalle $I$. De l'équation ($\ref{eqn:general_solution}$), nous avons

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

Puisque $y_1$ et $y_2$ forment une base, le déterminant de la matrice des coefficients, qui est le Wronskien $W(y_1(x_0), y_2(x_0))$, est non nul. Par conséquent, l'équation ($\ref{eqn:vector_equation_2}$) peut être résolue pour $c_1$ et $c_2$. Appelons la solution $(c_1, c_2) = (C_1, C_2)$. En substituant cela dans l'équation ($\ref{eqn:general_solution}$), nous obtenons la solution particulière suivante :

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Puisque $C_1$, $C_2$ est la solution de l'équation ($\ref{eqn:vector_equation_2}$),

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Par l'unicité du [Théorème d'existence et d'unicité pour les problèmes à valeur initiale](#théorème-dexistence-et-dunicité-pour-les-problèmes-à-valeur-initiale), nous avons $y^\* \equiv Y$ pour tout $x$ dans l'intervalle $I$. $\blacksquare$
