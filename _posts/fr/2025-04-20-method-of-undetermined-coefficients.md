---
title: Méthode des coefficients indéterminés
description: Découvrons la méthode des coefficients indéterminés, une technique qui permet de résoudre simplement certains problèmes à valeur initiale pour des équations différentielles linéaires non homogènes à coefficients constants, très utilisée en ingénierie pour les systèmes vibratoires et les circuits RLC.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Méthode des coefficients indéterminés** s'applique à :
>   - Des équations différentielles linéaires avec **coefficients constants $a$ et $b$**
>   - Où l'entrée $r(x)$ est composée de fonctions exponentielles, puissances de $x$, $\cos$ ou $\sin$, ou de sommes et produits de ces fonctions
>   - Équation différentielle linéaire $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Règles de sélection pour la méthode des coefficients indéterminés**  
>   - **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Règle de modification** : Si le terme choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique).  
>   - **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prérequis
- [Équations différentielles linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskien, existence et unicité des solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Équations différentielles linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/)

## Méthode des coefficients indéterminés
Considérons une équation différentielle linéaire non homogène du second ordre avec $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

et l'équation différentielle homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Comme nous l'avons vu dans [Équations différentielles linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/), pour résoudre un problème à valeur initiale pour l'équation différentielle non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$), nous devons d'abord trouver $y_h$ en résolvant l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$), puis trouver une solution particulière $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) pour obtenir la solution générale

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Comment trouver $y_p$ ? La méthode générale est la **méthode de variation des paramètres**, mais dans certains cas, on peut appliquer la **méthode des coefficients indéterminés**, qui est beaucoup plus simple. Cette méthode est particulièrement utile en ingénierie pour les systèmes vibratoires et les circuits électriques RLC.

La méthode des coefficients indéterminés s'applique aux équations différentielles linéaires avec **coefficients constants $a$ et $b$**

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

où $r(x)$ est composée de fonctions exponentielles, puissances de $x$, $\cos$ ou $\sin$, ou de sommes et produits de ces fonctions. L'idée clé est que ces types de fonctions $r(x)$ ont des dérivées de forme similaire à elles-mêmes. Pour appliquer la méthode, on choisit $y_p$ de forme similaire à $r(x)$, avec des coefficients indéterminés qui seront déterminés en substituant dans l'équation différentielle. Les règles pour choisir $y_p$ pour les formes de $r(x)$ importantes en pratique sont les suivantes :

> **Règles de sélection pour la méthode des coefficients indéterminés**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Règle de modification** : Si le terme choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique).  
> **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Cette méthode est non seulement simple mais possède aussi une propriété d'auto-correction. Si vous choisissez mal $y_p$ ou trop peu de termes, vous aboutirez à une contradiction. Si vous choisissez trop de termes, les coefficients des termes inutiles seront nuls, donnant quand même le bon résultat. Même si quelque chose ne va pas lors de l'application de la méthode, vous le remarquerez naturellement pendant le processus de résolution, donc n'hésitez pas à essayer avec un $y_p$ raisonnablement choisi selon les règles ci-dessus.

### Preuve de la règle de somme
Considérons une équation différentielle linéaire non homogène avec $r(x) = r_1(x) + r_2(x)$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

Considérons maintenant deux équations avec le même membre de gauche mais des entrées $r_1$ et $r_2$

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

qui ont respectivement ${y_p}_1$ et ${y_p}_2$ comme solutions. Si nous notons le membre de gauche par $L[y]$, alors par la linéarité de $L[y]$, pour $y_p = {y_p}_1 + {y_p}_2$, nous avons

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

### Exemple : $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Selon la règle de base (a), posons $y_p = Ce^{\gamma x}$ et substituons dans l'équation donnée $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### Cas où $\gamma^2 + a\gamma + b \neq 0$
Nous pouvons déterminer le coefficient indéterminé $C$ et trouver $y_p$ comme suit :

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### Cas où $\gamma^2 + a\gamma + b = 0$
Dans ce cas, nous devons appliquer la règle de modification (b). D'abord, utilisons $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ pour trouver les racines de l'équation caractéristique de l'équation différentielle homogène $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Cela nous donne la base de l'équation différentielle homogène

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

##### Cas où $\gamma \neq -a-\gamma$
Comme $Ce^{\gamma x}$ que nous avons choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante mais pas une racine double, selon la règle de modification (b), nous multiplions ce terme par $x$ pour obtenir $y_p = Cxe^{\gamma x}$.

Substituons maintenant ce $y_p$ modifié dans l'équation donnée $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### Cas où $\gamma = -a-\gamma$
Dans ce cas, $Ce^{\gamma x}$ que nous avons choisi pour $y_p$ est une solution correspondant à une racine double de l'équation caractéristique, donc selon la règle de modification (b), nous multiplions ce terme par $x^2$ pour obtenir $y_p = Cx^2 e^{\gamma x}$.

Substituons maintenant ce $y_p$ modifié dans l'équation donnée $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
