---
title: "Wronskien, existence et unicité des solutions"
description: "Pour une EDO linéaire homogène du second ordre à coefficients variables continus, nous étudions le théorème d'existence et d'unicité des solutions du problème à valeur initiale, la méthode de discrimination de la dépendance/indépendance linéaire des solutions utilisant le Wronskien, et démontrons que de telles équations ont toujours une solution générale qui inclut toutes les solutions de l'équation."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Pour une équation différentielle ordinaire linéaire homogène du second ordre à coefficients variables $p$ et $q$ continus sur un intervalle $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> et les conditions initiales
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> les quatre théorèmes suivants sont valides :
> 1. **Théorème d'existence et d'unicité des solutions du problème à valeur initiale** : Le problème à valeur initiale constitué de l'équation donnée et des conditions initiales a une solution unique $y(x)$ sur l'intervalle $I$.
> 2. **Discrimination de la dépendance/indépendance linéaire des solutions utilisant le Wronskien** : Pour deux solutions $y_1$ et $y_2$ de l'équation, si le **Wronskien** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ s'annule en un point $x_0$ dans l'intervalle $I$, alors les deux solutions sont linéairement dépendantes. De plus, s'il existe un point $x_1$ dans l'intervalle $I$ où $W\neq 0$, alors les deux solutions sont linéairement indépendantes.
> 3. **Existence de la solution générale** : L'équation donnée a une solution générale sur l'intervalle $I$.
> 4. **Non-existence de solution singulière** : Cette solution générale inclut toutes les solutions de l'équation (c'est-à-dire qu'il n'existe pas de solution singulière).
{: .prompt-info }

## Prérequis
- [Résolution des EDOs linéaires du premier ordre](/posts/Solution-of-First-Order-Linear-ODE/)
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matrice inverse et matrice singulière, déterminant

## Équation différentielle ordinaire linéaire homogène à coefficients variables continus
Nous avons précédemment étudié les solutions générales des [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/) et de l'[équation d'Euler-Cauchy](/posts/euler-cauchy-equation/).
Dans cet article, nous étendons la discussion à un cas plus général, celui d'une équation différentielle ordinaire linéaire homogène du second ordre à **coefficients variables** continus arbitraires $p$ et $q$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

pour étudier l'existence et la forme de la solution générale. De plus, nous examinerons l'unicité du [problème à valeur initiale](/posts/homogeneous-linear-odes-of-second-order/#problème-à-valeur-initiale-et-conditions-initiales) constitué de l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et des deux conditions initiales suivantes

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Pour anticiper la conclusion, l'essentiel du contenu traité ici est que les équations différentielles ordinaires <u>linéaires</u> à coefficients continus n'ont pas de *solution singulière* (solution qui ne peut être obtenue à partir de la solution générale).

## Théorème d'existence et d'unicité des solutions du problème à valeur initiale
> **Théorème d'existence et d'unicité des solutions du problème à valeur initiale**  
> Si $p(x)$ et $q(x)$ sont des fonctions continues sur un intervalle ouvert $I$, et si $x_0$ est dans l'intervalle $I$, alors le problème à valeur initiale constitué des équations ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et ($\ref{eqn:initial_conditions}$) a une solution unique $y(x)$ sur l'intervalle $I$.
{: .prompt-info }

Nous ne traiterons pas ici la démonstration de l'existence, mais seulement celle de l'unicité. En général, démontrer l'unicité est plus simple que démontrer l'existence.  
Si vous n'êtes pas intéressé par la démonstration, vous pouvez passer cette partie et aller directement à [Dépendance et indépendance linéaires des solutions](#dépendance-et-indépendance-linéaires-des-solutions).

### Démonstration de l'unicité
Supposons que le problème à valeur initiale constitué de l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) et des conditions initiales ($\ref{eqn:initial_conditions}$) ait deux solutions $y_1(x)$ et $y_2(x)$ sur l'intervalle $I$. Si nous pouvons montrer que la différence de ces deux solutions

$$ y(x) = y_1(x) - y_2(x) $$

est identiquement égale à $0$ sur l'intervalle $I$, cela signifie que $y_1 \equiv y_2$ sur l'intervalle $I$, ce qui implique l'unicité de la solution.

Comme l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) est une EDO linéaire homogène, la combinaison linéaire $y$ de $y_1$ et $y_2$ est une solution de l'équation sur $I$. Puisque $y_1$ et $y_2$ satisfont les mêmes conditions initiales ($\ref{eqn:initial_conditions}$), $y$ satisfait les conditions

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Considérons maintenant la fonction

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

et sa dérivée

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

À partir de l'équation différentielle, nous obtenons

$$ y^{\prime\prime} = -py^{\prime} - qy $$

En substituant ceci dans l'expression de $z^{\prime}$, nous obtenons

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Maintenant, puisque $y$ et $y^{\prime}$ sont réels, nous avons

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

À partir de ceci et de la définition de $z$, nous pouvons obtenir deux inégalités

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

À partir de ces deux inégalités, nous savons que $\|2yy^{\prime}\|\leq z$, et donc pour le dernier terme de l'équation ($\ref{eqn:z_prime}$), l'inégalité suivante est valide :

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

En utilisant ce résultat avec $-p \leq \|p\|$ et en appliquant l'équation ($\ref{eqn:inequalities}$a) au terme $2yy^{\prime}$ de l'équation ($\ref{eqn:z_prime}$), nous obtenons

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Puisque ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, nous obtenons

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

En posant $h = 1 + 2\|p\| + \|q\|$ pour la fonction entre parenthèses, nous avons

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

De la même manière, à partir des équations ($\ref{eqn:z_prime}$) et ($\ref{eqn:inequalities}$), nous obtenons

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Ces deux inégalités ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$) sont équivalentes aux inégalités suivantes

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

et les [facteurs intégrants](/posts/Solution-of-First-Order-Linear-ODE/#équation-différentielle-linéaire-non-homogène) pour les membres de gauche de ces deux équations sont

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{et} \qquad F_2 = e^{\int h(x)\ dx} $$

Puisque $h$ est continue, l'intégrale indéfinie $\int h(x)\ dx$ existe, et comme $F_1$ et $F_2$ sont positifs, nous obtenons à partir de l'équation ($\ref{eqn:inequalities_7}$)

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Cela signifie que $F_1 z$ ne croît pas et $F_2 z$ ne décroît pas sur l'intervalle $I$. Puisque $z(x_0) = 0$ d'après l'équation ($\ref{eqn:initial_conditions_\*}$), nous avons

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Enfin, en divisant les deux membres des inégalités par les nombres positifs $F_1$ et $F_2$, nous pouvons démontrer l'unicité de la solution comme suit :

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dépendance et indépendance linéaires des solutions
Rappelons brièvement le contenu traité dans [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/#base-et-solution-générale). La solution générale sur un intervalle ouvert $I$ est construite à partir d'une **base** $y_1$, $y_2$, c'est-à-dire une paire de solutions linéairement indépendantes sur $I$. Ici, le fait que $y_1$ et $y_2$ soient **linéairement indépendantes** sur l'intervalle $I$ signifie qu'elles satisfont ce qui suit pour tous les $x$ dans l'intervalle :

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ et }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Si ceci n'est pas satisfait et qu'il existe au moins un $k_1$, $k_2$ non nul tel que $k_1y_1(x) + k_2y_2(x) = 0$, alors $y_1$ et $y_2$ sont **linéairement dépendantes** sur l'intervalle $I$. Dans ce cas, pour tous les $x$ de l'intervalle $I$, nous avons

$$ \text{(a) } y_1 = ky_2 \quad \text{ou} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

et $y_1$ et $y_2$ sont proportionnelles.

Examinons maintenant la méthode suivante de discrimination de l'indépendance/dépendance linéaire des solutions.

> **Discrimination de la dépendance/indépendance linéaire des solutions utilisant le Wronskien**  
> **i.** Si l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a des coefficients $p(x)$ et $q(x)$ continus sur un intervalle ouvert $I$, alors la condition nécessaire et suffisante pour que deux solutions $y_1$ et $y_2$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$ soient linéairement dépendantes est que le *déterminant de Wronski*, abrégé **Wronskien**, défini par le déterminant suivant
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> s'annule en un point $x_0$ dans l'intervalle $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ et } y_2 \text{ sont linéairement dépendantes} $$
>
> **ii.** Si $W=0$ en un point $x=x_0$ dans l'intervalle $I$, alors $W=0$ en tous les points $x$ de l'intervalle $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> En d'autres termes, s'il existe un $x_1$ dans l'intervalle $I$ tel que $W\neq 0$, alors $y_1$, $y_2$ sont linéairement indépendantes sur cet intervalle $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ et } y_2 \text{ sont linéairement indépendantes}
> \end{align*}$$
>
{: .prompt-info }

> Le Wronskien a été introduit pour la première fois par le mathématicien polonais Józef Maria Hoene-Wroński, et a reçu son nom actuel en 11882 EH par le mathématicien écossais Thomas Muir.
{: .prompt-tip }

### Démonstration
#### i. (a)
Supposons que $y_1$ et $y_2$ soient linéairement dépendantes sur l'intervalle $I$. Alors l'équation ($\ref{eqn:linearly_dependent}$a) ou ($\ref{eqn:linearly_dependent}$b) est valide sur l'intervalle $I$. Si l'équation ($\ref{eqn:linearly_dependent}$a) est valide, alors

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

et de même, si l'équation ($\ref{eqn:linearly_dependent}$b) est valide,

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

donc nous pouvons confirmer que le Wronskien $W(y_1, y_2)=0$ pour <u>tous les $x$ dans l'intervalle $I$</u>.

#### i. (b)
Réciproquement, supposons que $W(y_1, y_2)=0$ pour un certain $x = x_0$, et montrons que $y_1$ et $y_2$ sont linéairement dépendantes sur l'intervalle $I$. Considérons le système d'équations linéaires en les inconnues $k_1$, $k_2$ :

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Ceci peut être exprimé sous la forme d'équation vectorielle suivante :

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

et le déterminant de cette matrice est précisément $W(y_1(x_0), y_2(x_0))$. Puisque $\det(A) = W=0$, $A$ est une **matrice singulière** qui n'a pas de **matrice inverse**, et donc le système d'équations ($\ref{eqn:linear_system}$) a une solution $(c_1, c_2)$ autre que le vecteur nul $(0,0)$ où au moins un de $k_1$ et $k_2$ n'est pas nul. Introduisons maintenant la fonction 

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Puisque l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) est linéaire homogène, cette fonction est une solution de ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$ par le [principe de superposition](/posts/homogeneous-linear-odes-of-second-order/#principe-de-superposition). À partir de l'équation ($\ref{eqn:linear_system}$), nous pouvons voir que cette solution satisfait les conditions initiales $y(x_0)=0$, $y^{\prime}(x_0)=0$.

D'autre part, il existe une solution triviale $y^\* \equiv 0$ qui satisfait les mêmes conditions initiales $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Puisque les coefficients $p$ et $q$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sont continus, l'unicité de la solution est garantie par le [théorème d'existence et d'unicité des solutions du problème à valeur initiale](#théorème-dexistence-et-dunicité-des-solutions-du-problème-à-valeur-initiale), donc $y \equiv y^\*$. C'est-à-dire, sur l'intervalle $I$,

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Puisque au moins un de $c_1$ et $c_2$ n'est pas nul, ($\ref{eqn:linearly_independent}$) n'est pas satisfait, ce qui signifie que $y_1$, $y_2$ sont linéairement dépendantes sur l'intervalle $I$.

#### ii.
Si $W(x_0)=0$ en un point $x_0$ dans l'intervalle $I$, alors par [i.(b)](#i-b), $y_1$, $y_2$ sont linéairement dépendantes sur l'intervalle $I$, et alors par [i.(a)](#i-a), $W\equiv 0$. Par conséquent, s'il existe ne serait-ce qu'un $x_1$ dans l'intervalle $I$ tel que $W(x_1)\neq 0$, alors $y_1$ et $y_2$ sont linéairement indépendantes. $\blacksquare$

## La solution générale inclut toutes les solutions
### Existence de la solution générale
> Si $p(x)$ et $q(x)$ sont continues sur un intervalle ouvert $I$, alors l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a une solution générale sur l'intervalle $I$.
{: .prompt-info }

#### Démonstration
Par le [théorème d'existence et d'unicité des solutions du problème à valeur initiale](#théorème-dexistence-et-dunicité-des-solutions-du-problème-à-valeur-initiale), l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a une solution $y_1(x)$ sur l'intervalle $I$ qui satisfait les conditions initiales

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

et une solution $y_2(x)$ sur l'intervalle $I$ qui satisfait les conditions initiales

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

Le Wronskien de ces deux solutions a une valeur non nulle en $x=x_0$ :

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

donc par la [discrimination de la dépendance/indépendance linéaire des solutions utilisant le Wronskien](#dépendance-et-indépendance-linéaires-des-solutions), $y_1$ et $y_2$ sont linéairement indépendantes sur l'intervalle $I$. Par conséquent, ces deux solutions forment une base des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$, et la solution générale $y = c_1y_1 + c_2y_2$ avec des constantes arbitraires $c_1$, $c_2$ existe nécessairement sur l'intervalle $I$. $\blacksquare$

### Absence de solution singulière
> Si l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a des coefficients $p(x)$ et $q(x)$ continus sur un intervalle ouvert $I$, alors toute solution $y=Y(x)$ de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$ est de la forme
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> où $y_1$, $y_2$ sont une base des solutions de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$ et $C_1$, $C_2$ sont des constantes appropriées.  
> C'est-à-dire que l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) n'a pas de **solution singulière** qui ne peut être obtenue à partir de la solution générale.
{: .prompt-info }

#### Démonstration
Soit $y=Y(x)$ une solution quelconque de l'équation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sur l'intervalle $I$. Maintenant, par le [théorème d'existence de la solution générale](#existence-de-la-solution-générale), l'équation différentielle ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) a une solution générale

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

sur l'intervalle $I$. Il faut maintenant montrer que pour tout $Y(x)$ arbitraire, il existe des constantes $c_1$, $c_2$ telles que $y(x)=Y(x)$ sur l'intervalle $I$. Montrons d'abord que nous pouvons trouver les valeurs de $c_1$, $c_2$ telles que $y(x_0)=Y(x_0)$ et $y^{\prime}(x_0)=Y^{\prime}(x_0)$ pour un $x_0$ arbitraire dans l'intervalle $I$. À partir de l'équation ($\ref{eqn:general_solution}$), nous obtenons

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

Puisque $y_1$ et $y_2$ sont une base, le déterminant de la matrice des coefficients $W(y_1(x_0), y_2(x_0))\neq 0$, donc l'équation ($\ref{eqn:vector_equation_2}$) peut être résolue pour $c_1$ et $c_2$. Soit $(c_1, c_2) = (C_1, C_2)$ la solution. En substituant ceci dans l'équation ($\ref{eqn:general_solution}$), nous obtenons la solution particulière suivante :

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Puisque $C_1$, $C_2$ sont les solutions de l'équation ($\ref{eqn:vector_equation_2}$), nous avons

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Par l'unicité du [théorème d'existence et d'unicité des solutions du problème à valeur initiale](#théorème-dexistence-et-dunicité-des-solutions-du-problème-à-valeur-initiale), $y^\* \equiv Y$ pour tous les $x$ dans l'intervalle $I$. $\blacksquare$
