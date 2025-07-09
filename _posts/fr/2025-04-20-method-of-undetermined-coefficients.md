---
title: "Méthode des coefficients indéterminés"
description: "Découvrons la méthode des coefficients indéterminés, une technique de résolution utile et fréquemment employée en ingénierie pour les systèmes vibrants ou les circuits RLC, car elle permet de résoudre simplement les problèmes de valeur initiale pour certaines équations différentielles ordinaires linéaires non homogènes à coefficients constants."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Méthode des coefficients indéterminés** : Conditions d'application :
>   - Avec des **coefficients constants $a$ et $b$**
>   - Le terme source $r(x)$ est une fonction exponentielle, une puissance de $x$, un $\cos$ ou un $\sin$, ou une somme ou un produit de telles fonctions
>   - Équation différentielle ordinaire linéaire $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Règles de choix pour la méthode des coefficients indéterminés**  
>   - **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Règle de modification** : Si un terme choisi pour $y_p$ est une solution de l'équation différentielle ordinaire homogène correspondante $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'EDO homogène).  
>   - **(c) Règle de la somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prérequis
- [EDOs linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskien, existence et unicité des solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [EDOs linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Espace vectoriel, engendrement linéaire (algèbre linéaire)

## Méthode des coefficients indéterminés
Considérons une équation différentielle ordinaire linéaire non homogène du second ordre avec $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

et l'équation différentielle ordinaire homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Comme nous l'avons vu dans l'article sur les [EDOs linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/), pour résoudre un problème de valeur initiale pour l'équation non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$), il faut d'abord résoudre l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$) pour trouver $y_h$, puis trouver une solution particulière $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) pour obtenir la solution générale

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Alors, comment trouver $y_p$ ? La méthode générale pour trouver $y_p$ est la **méthode de la variation des paramètres**, mais dans certains cas, on peut appliquer une méthode beaucoup plus simple : la **méthode des coefficients indéterminés**. C'est une méthode particulièrement utilisée en ingénierie car elle s'applique aux modèles de systèmes vibrants et de circuits électriques RLC.

La méthode des coefficients indéterminés est adaptée aux équations différentielles ordinaires linéaires avec des **coefficients constants $a$ et $b$**, et où le terme source $r(x)$ est une fonction exponentielle, une puissance de $x$, un $\cos$ ou un $\sin$, ou une somme ou un produit de telles fonctions :

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Le point clé de la méthode des coefficients indéterminés est que ce type de fonction $r(x)$ a des dérivées de forme similaire à elle-même. Pour appliquer cette méthode, on choisit une solution particulière $y_p$ de forme similaire à $r(x)$, mais avec des coefficients inconnus qui seront déterminés en substituant $y_p$ et ses dérivées dans l'équation différentielle donnée. Pour les formes de $r(x)$ importantes en pratique dans l'ingénierie, les règles pour choisir un $y_p$ approprié sont les suivantes.

> **Règles de choix pour la méthode des coefficients indéterminés**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Règle de modification** : Si un terme choisi pour $y_p$ est une solution de l'équation différentielle ordinaire homogène correspondante $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'EDO homogène).  
> **(c) Règle de la somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Cette méthode a l'avantage d'être non seulement simple, mais aussi auto-correctrice. Si l'on choisit un $y_p$ incorrect ou avec trop peu de termes, on aboutit à une contradiction, tandis que si l'on choisit trop de termes, les coefficients des termes superflus deviendront nuls, menant au bon résultat. Même si quelque chose ne va pas lors de l'application de la méthode, on s'en rendra naturellement compte au cours du processus de résolution. Par conséquent, si l'on a choisi un $y_p$ raisonnablement approprié selon les règles de sélection ci-dessus, on peut l'essayer sans hésitation.

### Démonstration de la règle de la somme
Considérons une équation différentielle ordinaire linéaire non homogène où $r(x) = r_1(x) + r_2(x)$ :

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Supposons maintenant que les deux équations suivantes, avec le même côté gauche mais avec les termes sources $r_1$ et $r_2$, ont pour solutions respectives ${y_p}_1$ et ${y_p}_2$.

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Si nous notons le côté gauche de l'équation donnée par $L[y]$, alors par la linéarité de $L[y]$, pour $y_p = {y_p}_1 + {y_p}_2$, nous avons la relation suivante, ce qui prouve la règle de la somme.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Exemple : $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Selon la règle de base (a), posons $y_p = Ce^{\gamma x}$ et substituons-le dans l'équation donnée $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$ :

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Cas où $\gamma^2 + a\gamma + b \neq 0$
On peut déterminer le coefficient indéterminé $C$ et trouver $y_p$ comme suit.

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Cas où $\gamma^2 + a\gamma + b = 0$
Dans ce cas, il faut appliquer la règle de modification (b). D'abord, utilisons le fait que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ pour trouver les racines de l'équation caractéristique de l'EDO homogène $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

De là, nous obtenons la base de l'EDO homogène

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Cas où $\gamma \neq -a-\gamma$
Puisque le terme $Ce^{\gamma x}$ que nous avions choisi pour $y_p$ est une solution (non double) de l'EDO homogène correspondante, nous multiplions ce terme par $x$ selon la règle de modification (b), et posons $y_p = Cxe^{\gamma x}$.

Maintenant, en substituant ce $y_p$ modifié dans l'équation donnée $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ :

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Cas où $\gamma = -a-\gamma$
Dans ce cas, le terme $Ce^{\gamma x}$ que nous avions choisi pour $y_p$ est une racine double de l'EDO homogène correspondante, donc nous multiplions ce terme par $x^2$ selon la règle de modification (b), et posons $y_p = Cx^2 e^{\gamma x}$.

Maintenant, en substituant ce $y_p$ modifié dans l'équation donnée $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ :

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extension de la méthode des coefficients indéterminés : $r(x)$ sous forme de produit de fonctions
Considérons une équation différentielle ordinaire linéaire non homogène où $r(x)$ est de la forme $k x^n e^{\alpha x}\cos(\omega x)$ :

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Si $r(x)$ est un produit ou une somme de fonctions telles que l'exponentielle $e^{\alpha x}$, une puissance de $x$ ($x^m$), $\cos{\omega x}$ ou $\sin{\omega x}$ (nous supposerons ici $\cos$ sans perte de généralité), c'est-à-dire si $r(x)$ peut être exprimé comme une somme et un produit des fonctions de la première colonne du tableau précédent, nous allons montrer qu'il existe une solution $y_p$ qui est une somme et un produit des fonctions de la deuxième colonne du même tableau.

> Certaines parties, marquées d'un *, utilisent l'algèbre linéaire pour une démonstration rigoureuse. Il est possible de sauter ces sections et de ne lire que le reste pour une compréhension générale.
{: .prompt-tip }

### Définition de l'espace vectoriel $V$*
Pour un $r(x)$ de la forme
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

on peut définir un espace vectoriel $V$ tel que $r(x) \in V$ comme suit :

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forme des dérivées des fonctions exponentielles, polynomiales et trigonométriques
Les formes des dérivées des fonctions de base présentées dans la première colonne du tableau précédent sont les suivantes :
- Fonction exponentielle : $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Fonction polynomiale : $\cfrac{d}{dx}x^m = mx^{m-1}$
- Fonctions trigonométriques : $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Les dérivées obtenues en différenciant ces fonctions sont également exprimées comme une <u>somme de fonctions du même type</u>.

Par conséquent, si les fonctions $f$ et $g$ sont les fonctions ci-dessus ou leurs sommes, en appliquant la règle du produit à $r(x) = f(x)g(x)$, nous obtenons

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

et ici, $f$, $f^{\prime}$, $f^{\prime\prime}$ ainsi que $g$, $g^{\prime}$, $g^{\prime\prime}$ peuvent tous être écrits comme des sommes ou des multiples scalaires de fonctions exponentielles, polynomiales et trigonométriques. Par conséquent, $r^{\prime}(x) = (fg)^{\prime}$ et $r^{\prime\prime}(x) = (fg)^{\prime\prime}$, tout comme $r(x)$, peuvent également être exprimés comme des sommes et des produits de ces fonctions.

### Invariance de $V$ sous l'opérateur de dérivation $D$ et la transformation linéaire $L$*
En d'autres termes, non seulement $r(x)$ lui-même, mais aussi $r^{\prime}(x)$ et $r^{\prime\prime}(x)$ sont des combinaisons linéaires de termes de la forme $x^k e^{\alpha x}\cos(\omega x)$ et $x^k e^{\alpha x}\sin(\omega x)$, donc

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Sans se limiter à $r(x)$, si nous introduisons l'opérateur de dérivation $D$ pour tous les éléments de l'espace vectoriel $V$ défini précédemment et l'exprimons de manière plus générale, *l'espace vectoriel $V$ est stable par l'opérateur de dérivation $D$*. Par conséquent, si nous notons le côté gauche de l'équation donnée $y^{\prime\prime} + ay^{\prime} + by$ par $L[y]$, alors *$V$ est invariant sous $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Puisque $r(x) \in V$ et que $V$ est invariant sous $L$, il existe un autre élément $y_p$ de $V$ qui satisfait $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Par conséquent, si nous choisissons un $y_p$ approprié comme une somme de tous les termes produits possibles en utilisant les coefficients indéterminés $A_0, A_1, \dots, A_n$ et $K, M$ comme suit, nous pouvons déterminer les coefficients indéterminés en substituant $y_p$ (ou $xy_p$, $x^2y_p$) et ses dérivées dans l'équation donnée, conformément à la règle de base (a) et à la règle de modification (b). Ici, $n$ doit être déterminé en fonction du degré de $x$ dans $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Si le terme source $r(x)$ donné contient plusieurs valeurs différentes de $\alpha_i$ et $\omega_j$, il faut choisir $y_p$ de manière à inclure sans omission tous les termes possibles de la forme $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ et $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ pour chaque valeur de $\alpha_i$ et $\omega_j$.  
> L'avantage de la méthode des coefficients indéterminés est sa simplicité. Si l'ansatz devient trop complexe au point que cet avantage s'estompe, il peut être préférable d'appliquer la méthode de la variation des paramètres, qui sera abordée ultérieurement.
{: .prompt-warning }

## Extension de la méthode des coefficients indéterminés : Équation d'Euler-Cauchy
La méthode des coefficients indéterminés peut être utilisée non seulement pour les [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/), mais aussi pour l'[équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Changement de variable
En effectuant le [changement de variable $x = e^t$ pour transformer l'équation en une EDO linéaire homogène du second ordre à coefficients constants](/posts/euler-cauchy-equation/#transformation-en-edo-linéaire-homogène-du-second-ordre-à-coefficients-constants), on a

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

ce qui, comme nous l'avons vu précédemment, permet de transformer l'équation d'Euler-Cauchy en l'équation différentielle ordinaire linéaire homogène à coefficients constants en $t$ suivante.

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

On peut maintenant appliquer la [méthode des coefficients indéterminés examinée précédemment](#méthode-des-coefficients-indéterminés) à l'équation ($\ref{eqn:substituted}$) pour la résoudre par rapport à $t$, puis utiliser $t = \ln x$ pour obtenir la solution en $x$.

### Cas où $r(x)$ est une puissance de $x$, un logarithme naturel, ou une somme ou un produit de telles fonctions
En particulier, si le terme source $r(x)$ est composé de puissances de $x$, de logarithmes naturels, ou de sommes et produits de telles fonctions, on peut choisir directement un $y_p$ approprié en suivant les règles de sélection suivantes pour l'équation d'Euler-Cauchy.

> **Règles de choix pour la méthode des coefficients indéterminés : Pour l'équation d'Euler-Cauchy**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:euler_cauchy}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:euler_cauchy}$).  
> **(b) Règle de modification** : Si un terme choisi pour $y_p$ est une solution de l'équation différentielle ordinaire homogène correspondante $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplier ce terme par $\ln{x}$ (ou par $(\ln{x})^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'EDO homogène).  
> **(c) Règle de la somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

De cette manière, pour des formes de $r(x)$ importantes en pratique, on peut trouver le même $y_p$ que celui obtenu par le [changement de variable](#changement-de-variable), mais de façon plus rapide et simple. On peut dériver ces règles de sélection pour l'équation d'Euler-Cauchy en remplaçant $x$ par $\ln{x}$ dans les [règles de sélection originales](#méthode-des-coefficients-indéterminés) examinées précédemment.
