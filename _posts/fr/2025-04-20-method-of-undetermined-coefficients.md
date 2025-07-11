---
title: "Méthode des coefficients indéterminés"
description: "Explorons la méthode des coefficients indéterminés, une méthode de résolution simple et utile pour les problèmes de valeurs initiales d'équations différentielles ordinaires linéaires non homogènes à coefficients constants de forme spécifique, fréquemment utilisée en ingénierie pour les systèmes oscillants, les modèles de circuits électriques RLC, etc."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Domaine d'application de la méthode des coefficients indéterminés** :
>   - Équations différentielles ordinaires linéaires ayant des **coefficients constants $a$ et $b$**
>   - Avec une entrée $r(x)$ composée de fonctions exponentielles, puissances de $x$, $\cos$ ou $\sin$, ou de sommes et produits de telles fonctions
>   - Équation différentielle ordinaire linéaire $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Règles de sélection pour la méthode des coefficients indéterminés**  
>   - **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir le $y_p$ correspondant de la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Règle de modification** : Si le terme choisi pour $y_p$ devient une solution de l'équation différentielle homogène $y^{\prime\prime} + ay^{\prime} + by = 0$ correspondant à l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$), multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'EDO homogène).  
>   - **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir comme $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
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
- Espaces vectoriels, génération linéaire (algèbre linéaire)

## Méthode des coefficients indéterminés
Considérons l'équation différentielle ordinaire linéaire non homogène du second ordre

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

avec $r(x) \not\equiv 0$ et l'équation différentielle ordinaire homogène correspondante

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Comme nous l'avons vu précédemment dans [EDOs linéaires non homogènes du second ordre](/posts/nonhomogeneous-linear-odes-of-second-order/), pour résoudre le problème de valeurs initiales de l'équation différentielle ordinaire linéaire non homogène ($\ref{eqn:nonhomogeneous_linear_ode}$), il faut résoudre l'équation différentielle ordinaire homogène ($\ref{eqn:homogeneous_linear_ode}$) pour obtenir $y_h$, puis trouver une solution $y_p$ de l'équation ($\ref{eqn:nonhomogeneous_linear_ode}$) pour obtenir la solution générale

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Comment peut-on alors trouver $y_p$ ? La méthode générale pour trouver $y_p$ est la **méthode de variation des paramètres**, mais dans certains cas, on peut appliquer la **méthode des coefficients indéterminés** qui est beaucoup plus simple. Cette méthode est particulièrement utile car elle peut être appliquée aux systèmes oscillants et aux modèles de circuits électriques RLC, et est donc fréquemment utilisée en ingénierie.

La méthode des coefficients indéterminés convient aux équations différentielles ordinaires linéaires ayant des **coefficients constants $a$ et $b$**, avec une entrée $r(x)$ composée de fonctions exponentielles, puissances de $x$, $\cos$ ou $\sin$, ou de sommes et produits de telles fonctions

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Le point clé de la méthode des coefficients indéterminés est que ce type de $r(x)$ a des dérivées de forme similaire à lui-même. Pour appliquer la méthode des coefficients indéterminés, on choisit un $y_p$ de forme similaire à $r(x)$ mais avec des coefficients indéterminés qui sont déterminés en substituant ce $y_p$ et ses dérivées dans l'équation différentielle ordinaire donnée. Les règles pour choisir un $y_p$ approprié pour les formes de $r(x)$ pratiquement importantes en ingénierie sont les suivantes.

> **Règles de sélection pour la méthode des coefficients indéterminés**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$) est l'une des fonctions de la première colonne du tableau, choisir le $y_p$ correspondant de la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Règle de modification** : Si le terme choisi pour $y_p$ devient une solution de l'équation différentielle homogène $y^{\prime\prime} + ay^{\prime} + by = 0$ correspondant à l'équation ($\ref{eqn:linear_ode_with_constant_coefficients}$), multiplier ce terme par $x$ (ou par $x^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'EDO homogène).  
> **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir comme $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Cette méthode est non seulement simple mais présente aussi l'avantage d'être auto-correctrice. Si on choisit mal $y_p$ ou si on sélectionne trop peu de termes, on aboutit à une contradiction, et si on choisit trop de termes, les coefficients des termes inutiles deviennent $0$ et on obtient le bon résultat. Même si quelque chose se passe mal lors de l'application de la méthode des coefficients indéterminés, on s'en aperçoit naturellement pendant le processus de résolution, donc si on a choisi un $y_p$ raisonnablement approprié selon les règles de sélection ci-dessus, on peut l'essayer sans crainte.

### Démonstration de la règle de somme
Considérons l'équation différentielle ordinaire linéaire non homogène

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

de la forme $r(x) = r_1(x) + r_2(x)$. Supposons maintenant que les deux équations suivantes ayant le même membre de gauche mais avec $r_1$ et $r_2$ comme entrées

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

ont respectivement ${y_p}\_1$ et ${y_p}\_2$ comme solutions. En notant le membre de gauche de l'équation donnée par $L[y]$, par la linéarité de $L[y]$, pour $y_p = {y_p}\_1 + {y_p}\_2$, on satisfait ce qui suit, donc la règle de somme est établie.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Exemple : $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Selon la règle de base (a), on pose $y_p = Ce^{\gamma x}$ et on substitue dans l'équation donnée $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$ :

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Cas où $\gamma^2 + a\gamma + b \neq 0$
On peut déterminer le coefficient indéterminé $C$ et obtenir $y_p$ comme suit :

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Cas où $\gamma^2 + a\gamma + b = 0$
Dans ce cas, il faut appliquer la règle de modification (b). D'abord, en utilisant $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, trouvons les racines de l'équation caractéristique de l'EDO homogène $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

On obtient ainsi la base de l'EDO homogène

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Cas où $\gamma \neq -a-\gamma$
Puisque le $Ce^{\gamma x}$ choisi pour $y_p$ est une solution de l'EDO homogène correspondant à l'équation donnée mais n'est pas une racine double, selon la règle de modification (b), on multiplie ce terme par $x$ et on pose $y_p = Cxe^{\gamma x}$.

En substituant maintenant le $y_p$ modifié dans l'équation donnée $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ :

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Cas où $\gamma = -a-\gamma$
Dans ce cas, le $Ce^{\gamma x}$ choisi pour $y_p$ est une racine double de l'EDO homogène correspondant à l'équation donnée, donc selon la règle de modification (b), on multiplie ce terme par $x^2$ et on pose $y_p = Cx^2 e^{\gamma x}$.

En substituant maintenant le $y_p$ modifié dans l'équation donnée $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ :

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extension de la méthode des coefficients indéterminés : $r(x)$ sous forme de produits de fonctions
Considérons l'équation différentielle ordinaire linéaire non homogène

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

de la forme $r(x) = k x^n e^{\alpha x}\cos(\omega x)$. Si $r(x)$ peut s'exprimer comme une fonction exponentielle $e^{\alpha x}$, une puissance de $x$ $x^m$, $\cos{\omega x}$ ou $\sin{\omega x}$ (ici on suppose $\cos$, ce qui ne fait perdre aucune généralité), ou des sommes et produits de telles fonctions (c'est-à-dire qu'elle peut s'exprimer comme des sommes et produits des fonctions de la première colonne du tableau précédent), nous montrerons qu'il existe une solution $y_p$ de l'équation qui est une somme et un produit des fonctions de la deuxième colonne du même tableau.

> Pour une démonstration rigoureuse, certaines parties utilisent l'algèbre linéaire et sont marquées d'un \*. On peut ignorer ces parties et lire seulement le reste pour une compréhension générale.
{: .prompt-tip }

### Définition de l'espace vectoriel $V$\*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

Pour un tel $r(x)$, on peut définir l'espace vectoriel $V$ tel que $r(x) \in V$ comme suit :

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forme des dérivées des fonctions exponentielles, polynomiales et trigonométriques
Les formes des dérivées des fonctions de base présentées dans la première colonne du tableau précédent sont les suivantes :
- Fonction exponentielle : $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Fonction polynomiale : $\cfrac{d}{dx}x^m = mx^{m-1}$
- Fonctions trigonométriques : $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Les dérivées obtenues en dérivant ces fonctions s'expriment également comme <u>des sommes de fonctions du même type</u>.

Par conséquent, lorsque les fonctions $f$ et $g$ sont les fonctions ci-dessus ou leurs sommes, pour $r(x) = f(x)g(x)$, en appliquant la règle de dérivation du produit :

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

où $f$, $f^{\prime}$, $f^{\prime\prime}$ et $g$, $g^{\prime}$, $g^{\prime\prime}$ peuvent tous s'écrire sous forme de sommes ou de multiples constants de fonctions exponentielles, polynomiales et trigonométriques. Par conséquent, $r^{\prime}(x) = (fg)^{\prime}$ et $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ peuvent également s'exprimer comme des sommes et produits de ces fonctions, tout comme $r(x)$.

### Invariance de $V$ par l'opérateur de dérivation $D$ et la transformation linéaire $L$\*
Autrement dit, non seulement $r(x)$ lui-même, mais aussi $r^{\prime}(x)$ et $r^{\prime\prime}(x)$ sont des combinaisons linéaires de termes de la forme $x^k e^{\alpha x}\cos(\omega x)$ et de termes de la forme $x^k e^{\alpha x}\sin(\omega x)$, donc

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

En introduisant l'opérateur de dérivation $D$ pour tous les éléments de l'espace vectoriel $V$ défini précédemment, et non pas seulement pour $r(x)$, on peut exprimer plus généralement que *l'espace vectoriel $V$ est fermé par l'opération de dérivation $D$*. Par conséquent, en notant le membre de gauche de l'équation donnée $y^{\prime\prime} + ay^{\prime} + by$ par $L[y]$, *$V$ est invariant par $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Puisque $r(x) \in V$ et que $V$ est invariant par $L$, il existe un autre élément $y_p$ de $V$ tel que $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Par conséquent, en choisissant un $y_p$ approprié comme somme de tous les termes possibles sous forme de produits, en utilisant les coefficients indéterminés $A_0, A_1, \dots, A_n$ et $K$, $M$ comme suit, on peut déterminer les coefficients indéterminés selon les règles de base (a) et de modification (b) en substituant $y_p$ (ou $xy_p$, $x^2y_p$) et ses dérivées dans l'équation donnée. Ici, $n$ est déterminé selon le degré de $r(x)$ par rapport à $x$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Si l'entrée donnée $r(x)$ contient plusieurs valeurs différentes $\alpha_i$, $\omega_j$, il faut choisir $y_p$ de manière à inclure sans exception tous les termes possibles de la forme $x^{k}e^{\alpha_i x}\cos(\omega_j x)$, $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ pour chaque valeur $\alpha_i$ et $\omega_j$.  
> L'avantage de la méthode des coefficients indéterminés étant sa simplicité, si l'hypothèse (ansatz) devient trop complexe et que cet avantage s'estompe, il peut être préférable d'appliquer plutôt la méthode de variation des paramètres qui sera traitée ultérieurement.
{: .prompt-warning }

## Extension de la méthode des coefficients indéterminés : équation d'Euler-Cauchy
La méthode des coefficients indéterminés peut être utilisée non seulement pour les [EDOs linéaires homogènes du second ordre à coefficients constants](/posts/homogeneous-linear-odes-with-constant-coefficients/), mais aussi pour l'[équation d'Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Substitution de variable
En [substituant $x = e^t$ pour transformer en EDO linéaire homogène du second ordre à coefficients constants](/posts/euler-cauchy-equation/#transformation-en-edo-linéaire-homogène-du-second-ordre-à-coefficients-constants), on obtient

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

et l'équation d'Euler-Cauchy peut être transformée en l'EDO homogène à coefficients constants suivante en $t$, comme nous l'avons vu précédemment.

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Il suffit maintenant d'appliquer la [méthode des coefficients indéterminés examinée précédemment](#méthode-des-coefficients-indéterminés) à l'équation ($\ref{eqn:substituted}$) pour résoudre par rapport à $t$, puis d'obtenir la solution par rapport à $x$ en utilisant $t = \ln x$ à la fin.

### Cas où $r(x)$ est une puissance de $x$, un logarithme naturel, ou des sommes et produits de telles fonctions
En particulier, lorsque l'entrée $r(x)$ est composée de puissances de $x$, de logarithmes naturels, ou de sommes et produits de telles fonctions, on peut choisir directement un $y_p$ approprié selon les règles de sélection suivantes pour l'équation d'Euler-Cauchy.

> **Règles de sélection pour la méthode des coefficients indéterminés : pour l'équation d'Euler-Cauchy**  
> **(a) Règle de base** : Si $r(x)$ dans l'équation ($\ref{eqn:euler_cauchy}$) est l'une des fonctions de la première colonne du tableau, choisir le $y_p$ correspondant de la même ligne et déterminer les coefficients indéterminés en substituant $y_p$ et ses dérivées dans l'équation ($\ref{eqn:euler_cauchy}$).  
> **(b) Règle de modification** : Si le terme choisi pour $y_p$ devient une solution de l'équation différentielle homogène $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ correspondant à l'équation ($\ref{eqn:euler_cauchy}$), multiplier ce terme par $\ln{x}$ (ou par $(\ln{x})^2$ si cette solution correspond à une racine double de l'équation caractéristique de l'EDO homogène).  
> **(c) Règle de somme** : Si $r(x)$ est une somme de fonctions de la première colonne du tableau, choisir comme $y_p$ la somme des fonctions correspondantes de la deuxième colonne.
>
> | Terme de $r(x)$ | Choix pour $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Cela permet de trouver plus rapidement et simplement le même $y_p$ que celui obtenu par [substitution de variable](#substitution-de-variable) pour les formes d'entrée $r(x)$ pratiquement importantes. On peut dériver ces règles de sélection pour l'équation d'Euler-Cauchy en remplaçant $x$ par $\ln{x}$ dans les [règles de sélection originales](#méthode-des-coefficients-indéterminés).
