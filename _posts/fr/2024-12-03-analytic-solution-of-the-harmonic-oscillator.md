---
title: Solution analytique de l'oscillateur harmonique (The Harmonic Oscillator)
description: Nous établissons l'équation de Schrödinger pour l'oscillateur harmonique
  en mécanique quantique et examinons sa solution analytique. Nous résolvons l'équation
  en introduisant la variable sans dimension 𝜉 et exprimons tout état stationnaire
  normalisé à l'aide des polynômes d'Hermite.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Toute oscillation peut être approximée par une oscillation harmonique simple si l'amplitude est suffisamment petite, ce qui donne à l'oscillation harmonique simple une importance significative en physique
> - Oscillateur harmonique : $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - Introduction de la variable sans dimension $\xi$ et de l'énergie $K$ exprimée en unités de $\cfrac{1}{2}\hbar\omega$ :
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - Lorsque $\|\xi\|^2 \to \infty$, la solution asymptotique physiquement admissible est $\psi(\xi) \to Ae^{-\xi^2/2}$, donc,
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(avec }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - En exprimant la solution de cette équation sous forme de série $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$,
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - Pour que cette solution soit normalisable, la série $\sum a_j$ doit être finie, c'est-à-dire qu'il doit exister une valeur 'maximale' de $j$, $n\in \mathbb{N}$, telle que $a_j=0$ pour $j>n$, donc
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - En général, $h_n(\xi)$ est un polynôme de degré $n$ en $\xi$, et on appelle **polynômes d'Hermite (Hermite polynomials)** $H_n(\xi)$ le reste après avoir exclu le coefficient initial ($a_0$ ou $a_1$)
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - États stationnaires normalisés de l'oscillateur harmonique :
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - Caractéristiques de l'oscillateur quantique
>   - Les fonctions propres alternent entre fonctions paires et impaires
>   - Il existe une probabilité non nulle de trouver la particule dans des régions classiquement interdites (au-delà de l'amplitude classique pour un $E$ donné)
>   - Pour tous les états stationnaires avec $n$ impair, la probabilité de trouver la particule au centre est nulle
>   - Plus $n$ est grand, plus l'oscillateur quantique ressemble à un oscillateur classique
{: .prompt-info }

## Prerequisites
- [Méthode de séparation des variables](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/)
- [Théorème d'Ehrenfest](/posts/ehrenfest-theorem/)
- [Équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/)
- [Le puits carré infini 1D](/posts/the-infinite-square-well/)
- [Solution algébrique de l'oscillateur harmonique](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## Configuration du modèle
Pour la description de l'oscillateur harmonique en mécanique classique et l'importance du problème de l'oscillateur harmonique, veuillez vous référer à [l'article précédent](/posts/algebraic-solution-of-the-harmonic-oscillator/).

### L'oscillateur harmonique en mécanique quantique
Le problème de l'oscillateur harmonique quantique consiste à résoudre l'équation de Schrödinger pour le potentiel

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

L'[équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/) pour l'oscillateur harmonique est

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

Il existe deux approches complètement différentes pour résoudre ce problème. L'une est la méthode analytique utilisant des **séries de puissances**, et l'autre est la méthode algébrique utilisant des **opérateurs d'échelle**. Bien que la méthode algébrique soit plus rapide et plus simple, il est également nécessaire d'étudier la solution analytique utilisant les séries de puissances. [Nous avons précédemment traité la méthode de solution algébrique](/posts/algebraic-solution-of-the-harmonic-oscillator/), et ici nous aborderons la méthode de solution analytique.

## Transformation de l'équation de Schrödinger
En introduisant la variable sans dimension

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

l'équation de Schrödinger indépendante du temps ($\ref{eqn:t_independent_schrodinger_eqn}$) peut être simplifiée comme suit :

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

Ici, $K$ est l'énergie exprimée en unités de $\cfrac{1}{2}\hbar\omega$.

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

Maintenant, il suffit de résoudre l'équation ($\ref{eqn:schrodinger_eqn_with_xi}$) ainsi réécrite. Pour de très grandes valeurs de $\xi$ (c'est-à-dire pour de très grandes valeurs de $x$), $\xi^2 \gg K$, donc

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

et la solution approximative est

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

Cependant, le terme $B$ diverge lorsque $\|x\|\to \infty$ et ne peut pas être normalisé, donc la solution asymptotique physiquement admissible est

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

Séparons maintenant la partie exponentielle et écrivons

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(avec }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

> Nous avons utilisé une méthode d'approximation dans le processus de dérivation pour trouver la forme asymptotique afin de déterminer le terme exponentiel $e^{-\xi^2/2}$, mais l'équation ($\ref{eqn:psi_and_h}$) obtenue n'est pas une approximation mais une équation exacte. Cette séparation de la forme asymptotique est la première étape standard lors de la résolution d'équations différentielles sous forme de séries de puissances.
{: .prompt-info }

En différenciant l'équation ($\ref{eqn:psi_and_h}$) pour obtenir $\cfrac{d\psi}{d\xi}$ et $\cfrac{d^2\psi}{d\xi^2}$, on obtient

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

donc l'équation de Schrödinger ($\ref{eqn:schrodinger_eqn_with_xi}$) devient maintenant

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

## Développement en série de puissances
Selon le théorème de Taylor, toute fonction variant doucement peut être exprimée sous forme de série de puissances, donc cherchons la solution de l'équation ($\ref{eqn:schrodinger_eqn_with_h}$) sous la forme d'une série en $\xi$ :

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

En différenciant chaque terme de cette série, on obtient les deux équations suivantes :

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

En substituant ces deux équations dans l'équation de Schrödinger (équation [$\ref{eqn:schrodinger_eqn_with_h}$]), on obtient :

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

Par l'unicité du développement en série de puissances, le coefficient de chaque puissance de $\xi$ doit être nul, donc

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

Cette **formule de récurrence** est équivalente à l'équation de Schrödinger. Étant donné deux constantes arbitraires $a_0$ et $a_1$, on peut déterminer tous les coefficients des termes de la solution $h(\xi)$.

Cependant, la solution ainsi obtenue n'est pas toujours normalisable. Si la série $\sum a_j$ est une série infinie (si $\lim_{j\to\infty} a_j\neq0$), pour de très grands $j$, la formule de récurrence ci-dessus devient approximativement

$$ a_{j+2} \approx \frac{2}{j}a_j $$

et la solution approximative est

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ est une constante arbitraire)}$$

Dans ce cas, pour de grandes valeurs de $\xi$ où les termes d'ordre supérieur deviennent dominants,

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

et si $h(\xi)$ prend cette forme $Ce^{\xi^2}$, $\psi(\xi)$ dans l'équation ($\ref{eqn:psi_and_h}$) devient de la forme $Ce^{\xi^2/2}$ et diverge lorsque $\xi \to \infty$. Cela correspond à la solution non normalisable avec $A=0, B\neq0$ dans l'équation ($\ref{eqn:psi_approx}$).

Par conséquent, la série $\sum a_j$ doit être finie. Il doit exister une valeur 'maximale' de $j$, $n\in \mathbb{N}$, telle que $a_j=0$ pour $j>n$, et pour que cela se produise, il faut que $a_{n+2}=0$ pour $a_n$ non nul, donc d'après l'équation ($\ref{eqn:recursion_formula}$)

$$ K = 2n + 1 $$

En substituant cela dans l'équation ($\ref{eqn:K}$), on obtient l'énergie physiquement admissible

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

Ainsi, nous avons obtenu la condition de quantification de l'énergie identique à celle de l'équation (21) dans la [solution algébrique de l'oscillateur harmonique](/posts/algebraic-solution-of-the-harmonic-oscillator/#états-stationnaires-psi_n-et-niveaux-dénergie-e_n) en utilisant une méthode complètement différente.

## Polynômes d'Hermite $H_n(\xi)$ et états stationnaires $\psi_n(x)$
### Polynômes d'Hermite $H_n$
En général, $h_n(\xi)$ est un polynôme de degré $n$ en $\xi$, et ne contient que des termes pairs si $n$ est pair, et que des termes impairs si $n$ est impair. On appelle **polynômes d'Hermite** $H_n(\xi)$ le reste après avoir exclu le coefficient initial ($a_0$ ou $a_1$).

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

Traditionnellement, on choisit arbitrairement les coefficients de sorte que le coefficient du terme de plus haut degré de $H_n$ soit $2^n$.

Voici les premiers polynômes d'Hermite :

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### États stationnaires $\psi_n(x)$
Les états stationnaires normalisés pour l'oscillateur harmonique sont les suivants :

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

Ceci est cohérent avec le résultat obtenu dans la [solution algébrique de l'oscillateur harmonique](/posts/algebraic-solution-of-the-harmonic-oscillator/#normalisation) (équation [27]).

L'image suivante montre les états stationnaires $\psi_n(x)$ et les densités de probabilité $\|\psi_n(x)\|^2$ pour les 8 premières valeurs de $n$. On peut voir que les fonctions propres de l'oscillateur quantique alternent entre fonctions paires et impaires.

![Représentations des fonctions d'onde pour les huit premiers états propres liés, n = 0 à 7. L'axe horizontal montre la position x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Densités de probabilité correspondantes.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Licence : Domaine public

L'oscillateur quantique est très différent de l'oscillateur classique correspondant, non seulement l'énergie est quantifiée, mais la distribution de probabilité de la position $x$ présente également des caractéristiques étranges.
- Il existe une probabilité non nulle de trouver la particule dans des régions classiquement interdites (au-delà de l'amplitude classique pour un $E$ donné)
- Pour tous les états stationnaires avec $n$ impair, la probabilité de trouver la particule au centre est nulle

Plus $n$ est grand, plus l'oscillateur quantique ressemble à un oscillateur classique. L'image ci-dessous montre la distribution de probabilité classique de la position $x$ (en pointillés) et l'état quantique $\|\psi_{30}\|^2$ pour $n=30$ (en trait plein). Si on lisse les parties rugueuses, les deux graphiques montrent une forme approximativement concordante.

![Distributions de probabilité quantique (trait plein) et classique (pointillés) de l'état excité n = 30 de l'oscillateur harmonique quantique. Les lignes verticales en pointillés représentent les points de retournement classiques.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - Licence : Domaine public

### Visualisation interactive des distributions de probabilité de l'oscillateur quantique
Voici une visualisation réactive basée sur Plotly.js que j'ai créée moi-même. Vous pouvez ajuster la valeur de $n$ avec le curseur pour voir la forme de la distribution de probabilité classique et de $\|\psi_n\|^2$ en fonction de la position $x$.

<div class="plotly-iframe-container" style="position: relative; padding-bottom: 110%; overflow: hidden;">
    <iframe id="plotly-iframe"
            src="/physics-visualizations/quantum-harmonic-oscillator.html"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 120%; border: none;" 
            allow="fullscreen">
    </iframe>
</div>

> - Page de visualisation originale : <{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html>
> - Code source : [Dépôt yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/quantum-harmonic-oscillator.html)
> - Licence : [Voir ici](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

De plus, si vous pouvez utiliser Python sur votre propre ordinateur et que vous avez un environnement avec les bibliothèques Numpy, Plotly et Dash installées, vous pouvez également exécuter le script Python [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/quantum_oscillator.py) dans le même dépôt pour voir les résultats.
