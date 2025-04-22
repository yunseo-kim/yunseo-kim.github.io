---
title: Méthode des coefficients indéterminés
description: Découvrons la méthode des coefficients indéterminés, une technique simple et efficace pour résoudre certaines équations différentielles linéaires non homogènes à coefficients constants, particulièrement utile en ingénierie pour modéliser les systèmes vibratoires et les circuits RLC.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - La **méthode des coefficients indéterminés** s'applique à :
>   - Des équations différentielles linéaires non homogènes $y^{\prime\prime} + ay^{\prime} + by = r(x)$ avec **coefficients constants $a$ et $b$**
>   - Où l'entrée $r(x)$ est composée de fonctions exponentielles, de puissances de $x$, de fonctions $\cos$ ou $\sin$, ou de sommes et produits de ces fonctions
> - **Règles de sélection pour la méthode des coefficients indéterminés**  
>   - **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne de la deuxième colonne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Règle de modification** : Si le terme choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'équation différentielle homogène).  
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
- [Équations différentielles ordinaires linéaires homogènes du second ordre](/posts/homogeneous-linear-odes-of-second-order/)
- [Équations différentielles ordinaires linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskien, existence et unicité des solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Équations différentielles ordinaires linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Espaces vectoriels, génération linéaire (algèbre linéaire)

## Méthode des coefficients indéterminés
Considérons une équation différentielle linéaire non homogène du second ordre avec $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

et l'équation différentielle homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Comme nous l'avons vu dans [Équations différentielles ordinaires linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/), pour résoudre un problème à valeur initiale pour l'équation différentielle non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$), nous devons d'abord résoudre l'équation homogène ($\ref{eqn:homogeneous_linear_ode}$) pour trouver $y_h$, puis trouver une solution particulière $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) pour obtenir la solution générale

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Comment trouver $y_p$ ? La méthode générale est la **méthode de variation des paramètres**, mais dans certains cas, on peut appliquer la **méthode des coefficients indéterminés**, beaucoup plus simple. Cette méthode est particulièrement utilisée en ingénierie pour les systèmes vibratoires et les modèles de circuits RLC.

La méthode des coefficients indéterminés s'applique aux équations différentielles linéaires avec **coefficients constants $a$ et $b$** où l'entrée $r(x)$ est composée de fonctions exponentielles, de puissances de $x$, de fonctions $\cos$ ou $\sin$, ou de sommes et produits de ces fonctions :

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

L'idée clé de la méthode des coefficients indéterminés est que ces types de fonctions $r(x)$ ont des dérivées de forme similaire. Pour appliquer cette méthode, on choisit un $y_p$ de forme similaire à $r(x)$, mais avec des coefficients indéterminés qui seront déterminés en substituant $y_p$ et ses dérivées dans l'équation différentielle donnée. Les règles pour choisir la forme appropriée de $y_p$ sont les suivantes :

> **Règles de sélection pour la méthode des coefficients indéterminés**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne de la deuxième colonne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Règle de modification** : Si le terme choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'équation différentielle homogène).  
> **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Cette méthode présente l'avantage d'être non seulement simple mais aussi auto-correctrice. Si vous choisissez mal $y_p$ ou sélectionnez trop peu de termes, vous aboutirez à une contradiction ; si vous sélectionnez trop de termes, les coefficients des termes inutiles seront simplement égaux à zéro. Même si quelque chose ne va pas lors de l'application de la méthode, vous le remarquerez naturellement pendant le processus de résolution, donc n'hésitez pas à essayer avec un $y_p$ raisonnablement choisi selon les règles de sélection ci-dessus.

### Preuve de la règle de somme
Considérons une équation différentielle linéaire non homogène de la forme

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Considérons maintenant les deux équations suivantes avec le même membre de gauche mais des entrées $r_1$ et $r_2$ :

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Supposons que ces équations aient respectivement ${y_p}_1$ et ${y_p}_2$ comme solutions. En notant le membre de gauche par $L[y]$, la linéarité de $L[y]$ implique que pour $y_p = {y_p}_1 + {y_p}_2$, nous avons :

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Exemple : $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Selon la règle de base (a), posons $y_p = Ce^{\gamma x}$ et substituons dans l'équation donnée $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$ :

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Cas où $\gamma^2 + a\gamma + b \neq 0$
Nous pouvons déterminer le coefficient indéterminé $C$ et trouver $y_p$ comme suit :

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Cas où $\gamma^2 + a\gamma + b = 0$
Dans ce cas, nous devons appliquer la règle de modification (b). Tout d'abord, utilisons le fait que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ pour trouver les racines de l'équation caractéristique de l'équation différentielle homogène $y^{\prime\prime} + ay^{\prime} + by = 0$ :

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Cela nous donne la base de l'équation différentielle homogène :

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Cas où $\gamma \neq -a-\gamma$
Puisque $Ce^{\gamma x}$ que nous avons choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante mais pas une solution correspondant à une racine double, selon la règle de modification (b), nous multiplions ce terme par $x$ pour obtenir $y_p = Cxe^{\gamma x}$.

Substituons maintenant ce $y_p$ modifié dans l'équation donnée $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ :

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Cas où $\gamma = -a-\gamma$
Dans ce cas, $Ce^{\gamma x}$ que nous avons choisi pour $y_p$ est une solution correspondant à une racine double de l'équation caractéristique de l'équation différentielle homogène. Selon la règle de modification (b), nous multiplions ce terme par $x^2$ pour obtenir $y_p = Cx^2 e^{\gamma x}$.

Substituons ce $y_p$ modifié dans l'équation donnée $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ :

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extension de la méthode des coefficients indéterminés : $r(x)$ sous forme de produit de fonctions
Considérons une équation différentielle linéaire non homogène de la forme

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

où $r(x) = k x^n e^{\alpha x}\cos(\omega x)$. Si $r(x)$ peut s'exprimer comme un produit de fonctions exponentielles $e^{\alpha x}$, de puissances de $x$ ($x^m$), de fonctions $\cos{\omega x}$ ou $\sin{\omega x}$ (ici nous supposons $\cos$, sans perte de généralité), ou comme une somme et un produit de telles fonctions (c'est-à-dire si $r(x)$ peut s'exprimer comme une somme et un produit des fonctions de la première colonne du tableau précédent), alors il existe une solution $y_p$ de l'équation qui est également une somme et un produit des fonctions de la deuxième colonne du tableau.

> Pour une démonstration rigoureuse, j'utilise l'algèbre linéaire et j'ai marqué ces parties avec \*. Vous pouvez sauter ces parties et lire le reste pour une compréhension générale.
{: .prompt-tip }

### Définition de l'espace vectoriel $V$\*
Pour $r(x)$ de la forme
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

nous pouvons définir un espace vectoriel $V$ tel que $r(x) \in V$ comme suit :

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forme des dérivées des fonctions exponentielles, polynomiales et trigonométriques
Les dérivées des fonctions de base présentées dans la première colonne du tableau sont :
- Fonction exponentielle : $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Fonction polynomiale : $\cfrac{d}{dx}x^m = mx^{m-1}$
- Fonctions trigonométriques : $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Les dérivées de ces fonctions s'expriment également comme <u>sommes de fonctions du même type</u>.

Par conséquent, si $f$ et $g$ sont des fonctions du type ci-dessus ou des sommes de telles fonctions, alors pour $r(x) = f(x)g(x)$, en appliquant la règle de dérivation du produit :

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

où $f$, $f^{\prime}$, $f^{\prime\prime}$ et $g$, $g^{\prime}$, $g^{\prime\prime}$ peuvent tous s'exprimer comme sommes ou multiples constants de fonctions exponentielles, polynomiales et trigonométriques. Par conséquent, $r^{\prime}(x) = (fg)^{\prime}$ et $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ peuvent également s'exprimer comme sommes et produits de ces fonctions, tout comme $r(x)$.

### Invariance de $V$ par rapport à l'opérateur de dérivation $D$ et à la transformation linéaire $L$\*
Ainsi, non seulement $r(x)$ lui-même, mais aussi $r^{\prime}(x)$ et $r^{\prime\prime}(x)$ sont des combinaisons linéaires de termes de la forme $x^k e^{\alpha x}\cos(\omega x)$ et $x^k e^{\alpha x}\sin(\omega x)$, donc :

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Plus généralement, en introduisant l'opérateur de dérivation $D$ pour tous les éléments de l'espace vectoriel $V$ défini précédemment, on peut dire que *l'espace vectoriel $V$ est fermé par rapport à l'opération de dérivation $D$*. Par conséquent, si nous notons le membre de gauche de l'équation donnée $y^{\prime\prime} + ay^{\prime} + by$ par $L[y]$, alors *$V$ est invariant par rapport à $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Puisque $r(x) \in V$ et que $V$ est invariant par rapport à $L$, il existe un autre élément $y_p$ de $V$ tel que $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Par conséquent, nous pouvons choisir un $y_p$ approprié comme somme de tous les termes produits possibles, en utilisant les coefficients indéterminés $A_0, A_1, \dots, A_n$ et $K$, $M$ comme suit, et déterminer ces coefficients en substituant $y_p$ (ou $xy_p$, $x^2y_p$ selon les règles de base (a) et de modification (b)) et ses dérivées dans l'équation donnée. Ici, $n$ est déterminé par le degré de $x$ dans $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Si l'entrée donnée $r(x)$ contient différentes valeurs de $\alpha_i$ et $\omega_j$, il faut choisir $y_p$ pour inclure tous les termes possibles de la forme $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ et $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ pour chaque valeur de $\alpha_i$ et $\omega_j$.  
> L'avantage de la méthode des coefficients indéterminés est sa simplicité, donc si l'ansatz devient trop complexe et fait perdre cet avantage, il peut être préférable d'appliquer la méthode de variation des paramètres que nous aborderons ultérieurement.
{: .prompt-warning }

## Extension de la méthode des coefficients indéterminés : équation d'Euler-Cauchy
La méthode des coefficients indéterminés peut également être appliquée aux [équations d'Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Substitution de variable
En [substituant $x = e^t$ pour transformer l'équation en une équation différentielle linéaire homogène à coefficients constants](/posts/euler-cauchy-equation/#transformation-en-équation-différentielle-ordinaire-linéaire-homogène-à-coefficients-constants), nous obtenons

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

ce qui transforme l'équation d'Euler-Cauchy en l'équation différentielle à coefficients constants suivante :

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Nous pouvons maintenant appliquer la [méthode des coefficients indéterminés vue précédemment](#méthode-des-coefficients-indéterminés) à l'équation ($\ref{eqn:substituted}$) pour la résoudre par rapport à $t$, puis utiliser $t = \ln x$ pour obtenir la solution en fonction de $x$.

### Cas où $r(x)$ est une puissance de $x$, un logarithme naturel, ou une somme et un produit de telles fonctions
En particulier, si l'entrée $r(x)$ est une puissance de $x$, un logarithme naturel, ou une somme et un produit de telles fonctions, nous pouvons choisir directement un $y_p$ approprié selon les règles de sélection suivantes pour les équations d'Euler-Cauchy :

> **Règles de sélection pour la méthode des coefficients indéterminés : version pour les équations d'Euler-Cauchy**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:euler_cauchy}$) est l'une des fonctions de la première colonne du tableau, choisir $y_p$ dans la même ligne de la deuxième colonne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:euler_cauchy}$).  
> **(b) Règle de modification** : Si le terme choisi pour $y_p$ est une solution de l'équation différentielle homogène correspondante $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplier ce terme par $\ln{x}$ (ou par $(\ln{x})^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'équation différentielle homogène).  
> **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir pour $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Cette approche permet de trouver rapidement et facilement le même $y_p$ que celui obtenu par [substitution de variable](#substitution-de-variable) pour les formes d'entrée $r(x)$ pratiquement importantes. On peut dériver ces règles de sélection pour les équations d'Euler-Cauchy en remplaçant $x$ par $\ln{x}$ dans les [règles de sélection originales](#méthode-des-coefficients-indéterminés).
