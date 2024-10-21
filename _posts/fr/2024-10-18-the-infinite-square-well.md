---
title: "Le puits carré infini unidimensionnel (The 1D Infinite Square Well)"
description: >-
  Examinons le problème du puits carré infini unidimensionnel, un exemple simple mais important qui illustre bien les concepts fondamentaux de la mécanique quantique. Dans cette situation idéale, nous déterminons le n-ième état stationnaire ψ(x) et l'énergie E d'une particule, et nous étudions quatre propriétés mathématiques importantes de ψ(x). À partir de là, nous obtenons la solution générale Ψ(x,t).
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - Problème du puits carré infini unidimensionnel : 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{ailleurs}
>   \end{cases}$$
> - Conditions aux limites : $ \psi(0) = \psi(a) = 0 $
> - Niveaux d'énergie du n-ième état stationnaire : $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Solution de l'équation de Schrödinger indépendante du temps dans le puits :
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Interprétation physique de chaque état stationnaire $\psi_n$ : 
>   - Forme d'onde stationnaire sur une corde de longueur $a$
>   - **État fondamental (ground state)** : état stationnaire $\psi_1$ avec l'énergie la plus basse
>   - **États excités (excited states)** : états restants avec $n\geq 2$ dont l'énergie augmente proportionnellement à $n^2$
> - Quatre propriétés mathématiques importantes de $\psi_n$ :
>   1. Si le potentiel $V(x)$ est symétrique, les fonctions paires et impaires alternent par rapport au centre du puits
>   2. À mesure que l'énergie augmente, chaque état consécutif a un **nœud (node)** de plus
>   3. Possède l'**orthonormalité (orthonormality)**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Possède la **complétude (completeness)**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Solution générale de l'équation de Schrödinger (combinaison linéaire des états stationnaires) :
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{où les coefficients }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Prérequis
- Distributions de probabilité continues et densité de probabilité
- Orthogonalité et normalisation (algèbre linéaire)
- Séries de Fourier et complétude (algèbre linéaire)
- [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/)
- [Théorème d'Ehrenfest](/posts/ehrenfest-theorem/)
- [Équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/)

## Conditions du potentiel donné
Si le potentiel est

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{ailleurs}
\end{cases} \tag{1}$$

alors la particule dans ce potentiel est une particule libre dans la plage $0<x<a$ et une force infinie agit aux deux extrémités ($x=0$ et $x=a$), l'empêchant de s'échapper. Dans un modèle classique, cela serait interprété comme un mouvement de va-et-vient infini avec des collisions parfaitement élastiques d'avant en arrière, sans forces non conservatives agissant. Bien que ce potentiel soit extrêmement artificiel et simple, c'est précisément pour cette raison qu'il peut servir de référence utile lors de l'étude d'autres situations physiques en mécanique quantique, et il mérite donc une attention particulière.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Établissement du modèle et des conditions aux limites
À l'extérieur du puits, la probabilité de trouver la particule est $0$, donc $\psi(x)=0$. À l'intérieur du puits, $V(x)=0$, donc [l'équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/) est

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

c'est-à-dire

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ où } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Ici, on suppose que $E\geq 0$.
{: .prompt-info }

C'est l'équation décrivant un **oscillateur harmonique simple (simple harmonic oscillator)** classique, et la solution générale est

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

où $A$ et $B$ sont des constantes arbitraires qui sont généralement déterminées par les **conditions aux limites** données dans le problème lors de la recherche d'une solution particulière. <u>Dans le cas de $\psi(x)$, les conditions aux limites sont généralement que $\psi$ et $d\psi/dx$ sont tous deux continus, mais là où le potentiel devient infini, seul $\psi$ est continu.</u>

## Résolution de l'équation de Schrödinger indépendante du temps

Comme $\psi(x)$ est continue,

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

doit être connectée à la solution à l'extérieur du puits. Dans l'équation ($\ref{eqn:psi_general_solution}$), lorsque $x=0$,

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

donc, en appliquant ($\ref{eqn:boundary_conditions}$), $B$ doit être égal à 0.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Alors $\psi(a)=A\sin{ka}$, donc pour satisfaire $\psi(a)=0$ de l'équation ($\ref{eqn:boundary_conditions}$), soit $A=0$ (solution triviale) soit $\sin{ka}=0$. Par conséquent,

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Ici aussi, $k=0$ est une solution triviale, résultant en $\psi(x)=0$, qui ne peut pas être normalisée et n'est donc pas la solution que nous recherchons dans ce problème. De plus, comme $\sin(-\theta)=-\sin(\theta)$, le signe négatif peut être absorbé dans $A$ de l'équation ($\ref{eqn:psi_without_B}$), donc nous pouvons considérer uniquement le cas où $ka>0$ sans perdre de généralité. Ainsi, les solutions possibles pour $k$ sont

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Alors $\psi_n=A\sin{k_n x}$ et $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, donc en substituant dans l'équation ($\ref{eqn:t_independent_schrodinger_eqn}$), les valeurs possibles de $E$ sont les suivantes.

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

En contraste frappant avec le cas classique, une particule quantique dans un puits carré infini ne peut pas avoir une énergie arbitraire, mais doit avoir l'une des valeurs autorisées.

> L'énergie est quantifiée par les conditions aux limites appliquées à la solution de l'équation de Schrödinger indépendante du temps.
{: .prompt-info }

Maintenant, nous pouvons normaliser $\psi$ pour trouver $A$.

> Normalement, c'est $\Psi(x,t)$ qui est normalisé, mais selon l'équation (11) de [l'équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/#1-ce-sont-des-états-stationnaires), cela équivaut à normaliser $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Cela détermine strictement seulement la magnitude de $A$, mais comme la phase de $A$ n'a aucune signification physique, nous pouvons simplement utiliser la racine carrée réelle positive comme $A$. Donc, la solution à l'intérieur du puits est

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Interprétation physique de chaque état stationnaire $\psi_n$
Comme dans l'équation ($\ref{eqn:psi_n}$), nous avons trouvé un nombre infini de solutions à partir de l'équation de Schrödinger indépendante du temps pour chaque niveau d'énergie $n$. Si nous traçons les premières d'entre elles, nous obtenons l'image suivante.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Ces états prennent la forme d'ondes stationnaires sur une corde de longueur $a$, avec $\psi_1$ ayant l'énergie la plus basse appelée **état fondamental (ground state)**, et les états restants $n\geq 2$ dont l'énergie augmente proportionnellement à $n^2$ appelés **états excités (excited states)**.

## Quatre propriétés mathématiques importantes de $\psi_n$
Toutes les fonctions $\psi_n(x)$ ont les quatre propriétés importantes suivantes. Ces quatre propriétés sont très puissantes et ne se limitent pas au puits carré infini. La première propriété est toujours valable si le potentiel lui-même est une fonction symétrique, et les deuxième, troisième et quatrième propriétés sont des propriétés générales qui apparaissent indépendamment de la forme du potentiel.

### 1. Les fonctions paires et impaires alternent par rapport au centre du puits.
Pour tout entier positif $n$, $\psi_{2n-1}$ est une fonction paire et $\psi_{2n}$ est une fonction impaire.

### 2. À mesure que l'énergie augmente, chaque état consécutif a un nœud de plus.
Pour tout entier positif $n$, $\psi_n$ a $(n-1)$ **nœuds (nodes)**.

### 3. Ces états possèdent l'orthogonalité (orthogonality).

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

Cela signifie qu'ils sont **orthogonaux (orthogonal)** entre eux.

> Dans le cas du puits carré infini que nous examinons actuellement, $\psi$ est réel, donc il n'est pas nécessaire de prendre le complexe conjugué ($^*$) de $\psi_m$, mais il est bon de prendre l'habitude de toujours l'inclure pour les cas où ce n'est pas le cas.
{: .prompt-tip }

#### Preuve
Quand $m\neq n$,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Quand $m=n$, cette intégrale est égale à 1 par normalisation, et en utilisant le **delta de Kronecker (Kronecker delta)** $\delta_{mn}$, l'orthogonalité et la normalisation peuvent être exprimées ensemble comme

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

Dans ce cas, on dit que $\psi$ est **orthonormé (orthonormal)**.

### 4. Ces fonctions possèdent la complétude (completeness).
Dans le sens où toute autre fonction arbitraire $f(x)$ peut être écrite comme une combinaison linéaire

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

ces fonctions sont dites **complètes (complete)**. L'équation ($\ref{eqn:fourier_series}$) est la **série de Fourier (Fourier series)** de $f(x)$, et le fait que toute fonction puisse être développée de cette manière est appelé **théorème de Dirichlet (Dirichlet's theorem)**.

## Calcul des coefficients $c_n$ en utilisant la méthode de Fourier (Fourier's trick)
Lorsque $f(x)$ est donné, en utilisant la complétude (completeness) et l'orthonormalité (orthonormality) de $\psi(x)$, nous pouvons trouver les coefficients $c_n$ par la méthode suivante, appelée **méthode de Fourier (Fourier's trick)**. Multiplions les deux côtés de l'équation ($\ref{eqn:fourier_series}$) par $\psi_m(x)^*$ et intégrons, en utilisant les équations ($\ref{eqn:orthonomality}$) et ($\ref{eqn:kronecker_delta}$) :

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Notez que tous les termes de la somme disparaissent sauf celui où $n=m$ à cause du delta de Kronecker.
{: .prompt-info }

Par conséquent, le coefficient de n-ième ordre lors du développement de $f(x)$ est

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Trouver la solution générale $\Psi(x,t)$ de l'équation de Schrödinger dépendante du temps
Chaque état stationnaire du puits carré infini est, selon l'équation (10) du post ['Équation de Schrödinger indépendante du temps'](/posts/time-independent-schrodinger-equation/#1-ce-sont-des-états-stationnaires) et l'équation ($\ref{eqn:psi_n}$) que nous avons trouvée précédemment,

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

De plus, nous avons vu précédemment dans [l'équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/#3-la-solution-générale-de-léquation-de-schrödinger-dépendante-du-temps-est-une-combinaison-linéaire-des-solutions-à-variables-séparées) que la solution générale de l'équation de Schrödinger peut être exprimée comme une combinaison linéaire d'états stationnaires. Par conséquent,

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Il ne reste plus qu'à trouver les coefficients $c_n$ qui satisfont la condition suivante :

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Grâce à la complétude de $\psi$ que nous avons examinée précédemment, il existe toujours des $c_n$ qui satisfont cette condition, et ils peuvent être trouvés en substituant $\Psi(x,0)$ à $f(x)$ dans l'équation ($\ref{eqn:coefficients_n}$).

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Si la condition initiale $\Psi(x,0)$ est donnée, on utilise l'équation ($\ref{eqn:calc_of_cn}$) pour trouver les coefficients de développement $c_n$, puis on les substitue dans l'équation ($\ref{eqn:general_solution}$) pour obtenir $\Psi(x,t)$. Ensuite, on peut calculer toute quantité physique d'intérêt selon le processus du [théorème d'Ehrenfest](/posts/ehrenfest-theorem/). Cette méthode peut être appliquée non seulement au puits carré infini mais aussi à tout potentiel arbitraire, seules la forme des fonctions $\psi$ et l'expression des niveaux d'énergie autorisés changeront.

## Dérivation de la conservation de l'énergie ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Utilisons l'orthonormalité de $\psi(x)$ (équations [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]) pour dériver la conservation de l'énergie que nous avons brièvement examinée dans [l'équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/#conservation-de-lénergie). Comme $c_n$ est indépendant du temps, il suffit de prouver que c'est vrai pour le cas où $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

De plus, comme

$$ \hat{H}\psi_n = E_n\psi_n $$

nous obtenons :

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
