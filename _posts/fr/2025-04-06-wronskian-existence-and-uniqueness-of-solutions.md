---
title: Wronskien, existence et unicité des solutions
description: Pour une équation différentielle ordinaire linéaire homogène du second ordre à coefficients variables continus, nous examinons le théorème d'existence et d'unicité des solutions pour le problème à valeur initiale, la méthode de détermination de la dépendance/indépendance linéaire des solutions à l'aide du Wronskien. Nous démontrons également que ces équations possèdent toujours une solution générale qui englobe toutes les solutions possibles.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> Pour une équation différentielle ordinaire linéaire homogène du second ordre à coefficients variables continus $p$ et $q$ sur un intervalle $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> avec les conditions initiales
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> les quatre théorèmes suivants sont valables :
> 1. **Théorème d'existence et d'unicité pour le problème à valeur initiale** : Le problème à valeur initiale composé de l'équation donnée et des conditions initiales admet une solution unique $y(x)$ sur l'intervalle $I$.
> 2. **Détermination de la dépendance/indépendance linéaire des solutions à l'aide du Wronskien** : Pour deux solutions $y_1$ et $y_2$ de l'équation, s'il existe un point $x_0$ dans l'intervalle $I$ où le **Wronskien** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ est égal à zéro, alors ces solutions sont linéairement dépendantes. De plus, s'il existe un point $x_1$ dans $I$ où $W\neq 0$, alors les solutions sont linéairement indépendantes.
> 3. **Existence de la solution générale** : L'équation donnée admet une solution générale sur l'intervalle $I$.
> 4. **Absence de solutions singulières** : Cette solution générale englobe toutes les solutions de l'équation (c'est-à-dire qu'il n'existe pas de solutions singulières).
{: .prompt-info }

## Prérequis
- [Solution des équations différentielles ordinaires linéaires du premier ordre](/posts/Solution-of-First-Order-Linear-ODE/)
- [Équations différentielles ordinaires linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Équations différentielles ordinaires linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matrices inverses et singulières, déterminants

## Équations différentielles ordinaires linéaires homogènes à coefficients variables continus
Nous avons précédemment étudié la solution générale des [équations différentielles ordinaires linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/) et de [l'équation d'Euler-Cauchy](/posts/euler-cauchy-equation/).
Dans cet article, nous élargissons notre discussion à un cas plus général, celui des équations différentielles ordinaires linéaires homogènes du second ordre à **coefficients variables** $p$ et $q$ continus :

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Nous examinerons l'existence et la forme de la solution générale de cette équation. De plus, nous étudierons l'unicité du [problème à valeur initiale](/posts/homogeneous-linear-odes-of-second-order/#problème-à-valeur-initiale-et-conditions-initiales) composé de l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et des deux conditions initiales suivantes :

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Pour anticiper la conclusion, le point essentiel de notre discussion est qu'une équation différentielle <u>linéaire</u> à coefficients continus ne possède pas de *solution singulière* (solution qui ne peut pas être obtenue à partir de la solution générale).

## Théorème d'existence et d'unicité pour le problème à valeur initiale
> **Théorème d'existence et d'unicité pour le problème à valeur initiale**  
> Si $p(x)$ et $q(x)$ sont des fonctions continues sur un intervalle ouvert $I$, et si $x_0$ est un point de cet intervalle, alors le problème à valeur initiale composé des équations ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et ($\ref{eqn:initial_conditions}$) admet une solution unique $y(x)$ sur l'intervalle $I$.
{: .prompt-info }

Nous ne traiterons pas ici la preuve de l'existence, mais seulement celle de l'unicité, qui est généralement plus simple.  
Si vous n'êtes pas intéressé par la démonstration, vous pouvez passer directement à la section [Dépendance et indépendance linéaire des solutions](#dépendance-et-indépendance-linéaire-des-solutions).

### Démonstration de l'unicité
Supposons que le problème à valeur initiale composé de l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et des conditions initiales ($\ref{eqn:initial_conditions}$) admette deux solutions $y_1(x)$ et $y_2(x)$ sur l'intervalle $I$. Si nous pouvons montrer que leur différence

$$ y(x) = y_1(x) - y_2(x) $$

est identiquement nulle sur l'intervalle $I$, cela signifiera que $y_1 \equiv y_2$ sur $I$, prouvant ainsi l'unicité de la solution.

Comme l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) est une équation différentielle linéaire homogène, $y$, combinaison linéaire de $y_1$ et $y_2$, est aussi une solution de l'équation sur $I$. Puisque $y_1$ et $y_2$ satisfont les mêmes conditions initiales ($\ref{eqn:initial_conditions}$), $y$ satisfait les conditions

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_1(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Considérons maintenant la fonction

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

et sa dérivée

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

De l'équation différentielle, nous obtenons

$$ y^{\prime\prime} = -py^{\prime} - qy $$

En substituant dans l'expression de $z^{\prime}$, nous avons

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Comme $y$ et $y^{\prime}$ sont réels, nous avons

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

De cela et de la définition de $z$, nous obtenons deux inégalités

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Ces inégalités impliquent que $\|2yy^{\prime}\|\leq z$, et donc pour le dernier terme de l'équation ($\ref{eqn:z_prime}$), nous avons

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Avec ce résultat et le fait que $-p \leq \|p\|$, et en appliquant l'inégalité ($\ref{eqn:inequalities}$a) au terme $2yy^{\prime}$ de l'équation ($\ref{eqn:z_prime}$), nous obtenons

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Comme ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, nous avons

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

En posant $h = 1 + 2\|p\| + \|q\|$, nous obtenons

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

De même, à partir des équations ($\ref{eqn:z_prime}$) et ($\ref{eqn:inequalities}$), nous avons

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Ces deux inégalités ($\ref{eqn:inequality_6a}$) et ($\ref{eqn:inequality_6b}$) sont équivalentes à

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

Les [facteurs intégrants](/posts/Solution-of-First-Order-Linear-ODE/#équation-différentielle-linéaire-non-homogène) pour les membres de gauche de ces équations sont

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{et} \qquad F_2 = e^{\int h(x)\ dx} $$

Comme $h$ est continue, l'intégrale indéfinie $\int h(x)\ dx$ existe, et comme $F_1$ et $F_2$ sont positifs, les inégalités ($\ref{eqn:inequalities_7}$) donnent

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Cela signifie que $F_1 z$ ne croît pas et que $F_2 z$ ne décroît pas sur l'intervalle $I$. Comme $z(x_0) = 0$ d'après l'équation ($\ref{eqn:initial_conditions_*}$), nous avons

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finalement, en divisant les deux côtés des inégalités par les nombres positifs $F_1$ et $F_2$, nous pouvons prouver l'unicité de la solution :

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dépendance et indépendance linéaire des solutions
Rappelons ce que nous avons vu dans [Équations différentielles ordinaires linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/#base-et-solution-générale). La solution générale sur un intervalle ouvert $I$ est construite à partir d'une **base** $y_1$, $y_2$, c'est-à-dire une paire de solutions linéairement indépendantes. Deux fonctions $y_1$ et $y_2$ sont **linéairement indépendantes** sur l'intervalle $I$ si, pour tout $x$ dans cet intervalle :

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ et }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Si cette condition n'est pas satisfaite, et s'il existe des constantes $k_1$, $k_2$ non toutes nulles telles que $k_1y_1(x) + k_2y_2(x) = 0$, alors $y_1$ et $y_2$ sont **linéairement dépendantes** sur $I$. Dans ce cas, pour tout $x$ dans $I$ :

$$ \text{(a) } y_1 = ky_2 \quad \text{ou} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

c'est-à-dire que $y_1$ et $y_2$ sont proportionnelles.

Voyons maintenant comment déterminer la dépendance ou l'indépendance linéaire des solutions.

> **Détermination de la dépendance/indépendance linéaire des solutions à l'aide du Wronskien**  
> **i.** Si l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a des coefficients $p(x)$ et $q(x)$ continus sur un intervalle ouvert $I$, alors une condition nécessaire et suffisante pour que deux solutions $y_1$ et $y_2$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur $I$ soient linéairement dépendantes est que leur *déterminant wronskien*, ou simplement **Wronskien**
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> s'annule en un point $x_0$ de l'intervalle $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ et } y_2 \text{ sont linéairement dépendantes} $$
>
> **ii.** Si le Wronskien $W$ s'annule en un point $x=x_0$ de l'intervalle $I$, alors il s'annule en tout point de $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> En d'autres termes, s'il existe un point $x_1$ dans $I$ où $W\neq 0$, alors $y_1$ et $y_2$ sont linéairement indépendantes sur $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ et } y_2 \text{ sont linéairement indépendantes}
> \end{align*}$$
>
{: .prompt-info }

> Le Wronskien a été introduit par le mathématicien polonais Józef Maria Hoene-Wroński, et a reçu son nom actuel du mathématicien écossais Sir Thomas Muir en 11882 EH, après la mort de Wroński.
{: .prompt-tip }

### Démonstration
#### i. (a)
Supposons que $y_1$ et $y_2$ soient linéairement dépendantes sur $I$. Alors l'équation ($\ref{eqn:linearly_dependent}$a) ou ($\ref{eqn:linearly_dependent}$b) est satisfaite sur $I$. Si c'est l'équation ($\ref{eqn:linearly_dependent}$a) qui est satisfaite, alors

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

De même, si c'est l'équation ($\ref{eqn:linearly_dependent}$b) qui est satisfaite, alors

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Donc, <u>pour tout $x$ dans $I$</u>, le Wronskien $W(y_1, y_2)=0$.

#### i. (b)
Réciproquement, supposons qu'il existe un point $x=x_0$ dans $I$ tel que $W(y_1, y_2)=0$. Nous allons montrer que $y_1$ et $y_2$ sont linéairement dépendantes sur $I$. Considérons le système d'équations linéaires à deux inconnues $k_1$ et $k_2$ :

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Ce système peut être écrit sous forme d'équation vectorielle :

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

La matrice des coefficients de cette équation est

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

et son déterminant est $W(y_1(x_0), y_2(x_0))$. Comme $\det(A) = W=0$, $A$ est une **matrice singulière** qui n'admet pas d'**inverse**, et donc le système d'équations ($\ref{eqn:linear_system}$) admet une solution non triviale $(c_1, c_2)$ où au moins l'une des valeurs $c_1$ ou $c_2$ est non nulle. Considérons maintenant la fonction

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Comme l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) est linéaire homogène, par le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition), cette fonction est une solution de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur $I$. D'après l'équation ($\ref{eqn:linear_system}$), cette solution satisfait les conditions initiales $y(x_0)=0$ et $y^{\prime}(x_0)=0$.

D'autre part, la solution triviale $y^* \equiv 0$ satisfait les mêmes conditions initiales $y^*(x_0)=0$ et ${y^*}^{\prime}(x_0)=0$. Comme les coefficients $p$ et $q$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sont continus, le [théorème d'existence et d'unicité pour le problème à valeur initiale](#théorème-dexistence-et-dunicité-pour-le-problème-à-valeur-initiale) garantit l'unicité de la solution, donc $y \equiv y^*$. Cela signifie que sur l'intervalle $I$,

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Comme au moins l'un des coefficients $c_1$ ou $c_2$ est non nul, l'équation ($\ref{eqn:linearly_independent}$) n'est pas satisfaite, ce qui prouve que $y_1$ et $y_2$ sont linéairement dépendantes sur $I$.

#### ii.
Si le Wronskien s'annule en un point $x_0$ de l'intervalle $I$, alors d'après [i.(b)](#i-b), $y_1$ et $y_2$ sont linéairement dépendantes sur $I$, et d'après [i.(a)](#i-a), le Wronskien est identiquement nul sur $I$. Donc, si $W(x_1)\neq 0$ pour un certain $x_1$ dans $I$, alors $y_1$ et $y_2$ sont linéairement indépendantes. $\blacksquare$

## La solution générale englobe toutes les solutions
### Existence de la solution générale
> Si $p(x)$ et $q(x)$ sont continues sur un intervalle ouvert $I$, alors l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) admet une solution générale sur $I$.
{: .prompt-info }

#### Démonstration
D'après le [théorème d'existence et d'unicité pour le problème à valeur initiale](#théorème-dexistence-et-dunicité-pour-le-problème-à-valeur-initiale), l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) admet une solution $y_1(x)$ sur $I$ satisfaisant les conditions initiales

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

et une solution $y_2(x)$ sur $I$ satisfaisant les conditions initiales

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

Le Wronskien de ces deux solutions au point $x=x_0$ est non nul :

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Donc, d'après la [détermination de la dépendance/indépendance linéaire des solutions à l'aide du Wronskien](#dépendance-et-indépendance-linéaire-des-solutions), $y_1$ et $y_2$ sont linéairement indépendantes sur $I$. Par conséquent, ces deux solutions forment une base des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur $I$, et la solution générale $y = c_1y_1 + c_2y_2$ avec des constantes arbitraires $c_1$ et $c_2$ existe nécessairement sur $I$. $\blacksquare$

### Absence de solutions singulières
> Si l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a des coefficients $p(x)$ et $q(x)$ continus sur un intervalle ouvert $I$, alors toute solution $y=Y(x)$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur $I$ est de la forme
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> où $y_1$ et $y_2$ forment une base des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur $I$, et $C_1$ et $C_2$ sont des constantes appropriées.  
> En d'autres termes, l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) n'admet pas de **solution singulière** (solution qui ne peut pas être obtenue à partir de la solution générale).
{: .prompt-info }

#### Démonstration
Soit $y=Y(x)$ une solution quelconque de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur $I$. D'après le [théorème d'existence de la solution générale](#existence-de-la-solution-générale), l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) admet une solution générale

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

sur $I$. Nous devons montrer qu'il existe des constantes $c_1$ et $c_2$ telles que $y(x)=Y(x)$ sur $I$. Montrons d'abord qu'il est possible de trouver des valeurs de $c_1$ et $c_2$ telles que $y(x_0)=Y(x_0)$ et $y^{\prime}(x_0)=Y^{\prime}(x_0)$ pour un $x_0$ arbitraire dans $I$. De l'équation ($\ref{eqn:general_solution}$), nous avons

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

Comme $y_1$ et $y_2$ forment une base, le déterminant de la matrice des coefficients, $W(y_1(x_0), y_2(x_0))$, est non nul, donc l'équation ($\ref{eqn:vector_equation_2}$) peut être résolue pour $c_1$ et $c_2$. Soit $(c_1, c_2) = (C_1, C_2)$ cette solution. En substituant dans l'équation ($\ref{eqn:general_solution}$), nous obtenons la solution particulière

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Comme $C_1$ et $C_2$ satisfont l'équation ($\ref{eqn:vector_equation_2}$), nous avons

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

D'après l'unicité garantie par le [théorème d'existence et d'unicité pour le problème à valeur initiale](#théorème-dexistence-et-dunicité-pour-le-problème-à-valeur-initiale), $y^* \equiv Y$ sur tout l'intervalle $I$. $\blacksquare$
