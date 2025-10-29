---
title: "Transformation linéaire, noyau et image"
description: "Définition des transformations linéaires, avec noyau et image. Nullité et rang, théorème de la dimension (rang‑nullité), liens avec injection/surjection et rôle des bases."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prérequis
- [Vecteurs et combinaisons linéaires](/posts/vectors-and-linear-combinations/)
- [Espaces vectoriels, sous-espaces et matrices](/posts/vector-spaces-subspaces-and-matrices/)
- [Dépendance et indépendance linéaires, base et dimension](posts/linear-dependence-and-independence-basis-and-dimension/)
- Injection, surjection

## Transformation linéaire

Une fonction particulière qui préserve la structure d’un espace vectoriel est appelée **transformation linéaire (linear transformation)**; c’est une notion fondamentale qui apparaît très fréquemment en mathématiques pures et appliquées, en sciences sociales et naturelles, ainsi qu’en ingénierie.

> **Définition**  
> Soient $\mathbb{V}$ et $\mathbb{W}$ des $F$‑espaces vectoriels. On appelle **transformation linéaire (linear transformation)** de $\mathbb{V}$ vers $\mathbb{W}$ toute application $T: \mathbb{V} \to \mathbb{W}$ qui satisfait, pour tous $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ et $c \in F$, les deux conditions:
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

Dire que $T$ est une transformation linéaire se résume souvent à dire que $T$ est **linéaire**. Une transformation linéaire $T: \mathbb{V} \to \mathbb{W}$ vérifie les quatre propriétés suivantes.

> 1. $T$ linéaire $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ linéaire $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ linéaire $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ linéaire $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> Pour montrer qu’une application est linéaire, il est en pratique commode d’utiliser la propriété 2.
{: .prompt-tip }

> L’algèbre linéaire a d’amples applications en géométrie car de nombreuses transformations géométriques importantes sont linéaires. En particulier, les trois transformations clés que sont la **rotation**, la **symétrie** et la **projection** sont linéaires.
{: .prompt-tip }

Deux transformations linéaires apparaissent tout particulièrement souvent.

> **Transformation identité et transformation nulle**  
> Pour des $F$‑espaces vectoriels $\mathbb{V}, \mathbb{W}$:
> - **Transformation identité (identity transformation)**: l’application $I\_\mathbb{V}: \mathbb{V} \to \mathbb{V}$ définie par $I\_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ pour tout $\mathbf{x} \in \mathbb{V}$
> - **Transformation nulle (zero transformation)**: l’application $T\_0: \mathbb{V} \to \mathbb{W}$ définie par $T\_0(\mathbf{x}) = \mathbf{0}$ pour tout $\mathbf{x} \in \mathbb{V}$
{: .prompt-info }

Bien d’autres notions entrent dans le cadre des transformations linéaires.

> **Exemples de transformations linéaires**  
> - Rotation
> - Symétrie
> - Projection
> - [Matrice transposée](/posts/vector-spaces-subspaces-and-matrices/#matrice-transposée-matrice-symétrique-matrice-antisymétrique)
> - Dérivation d’une fonction différentiable
> - Intégration d’une fonction continue
{: .prompt-tip }

## Noyau et image

### Définition: noyau et image

> **Définition**  
> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$ et une transformation linéaire $T: \mathbb{V} \to \mathbb{W}$:
> - **Noyau (kernel)**: l’ensemble des $\mathbf{x} \in \mathbb{V}$ tels que $T(\mathbf{x}) = \mathbf{0}$, noté $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **Image (range)**: le sous-ensemble de $\mathbb{W}$ constitué des valeurs de $T$, noté $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$, l’identité $I: \mathbb{V} \to \mathbb{V}$ et la transformation nulle $T\_0: \mathbb{V} \to \mathbb{W}$, on a:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T\_0) = \mathbb{V}$
> - $\mathrm{R}(T\_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

Point clé pour la suite: le noyau et l’image d’une transformation linéaire sont des [sous-espaces](/posts/vector-spaces-subspaces-and-matrices/#sous-espace).

> **Théorème 1**  
> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$ et une transformation linéaire $T: \mathbb{V} \to \mathbb{W}$, $\mathrm{N}(T)$ et $\mathrm{R}(T)$ sont des sous-espaces de $\mathbb{V}$ et $\mathbb{W}$ respectivement.
>
> **Preuve**  
> Notons $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$ les vecteurs nuls de $\mathbb{V}, \mathbb{W}$.
>
> Comme $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, on a $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$. De plus, pour $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T)$ et $c \in F$:
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [Puisque $\mathbf{0}_\mathbb{V} \in \mathrm{N}(T)$, $\mathbf{x} + \mathbf{y} \in \mathrm{N}(T)$ et $c\mathbf{x} \in \mathrm{N}(T)$, $\mathrm{N}(T)$ est un sous-espace de $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#sous-espace).
>
> De même, $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$ implique $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$, et comme $\forall \mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F \ (\exists \mathbf{v}, \mathbf{w} \in \mathbb{V} \ (T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y}))$, on a
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [Puisque $\mathbf{0}_\mathbb{W} \in \mathrm{R}(T)$, $\mathbf{x} + \mathbf{y} \in \mathrm{R}(T)$ et $c\mathbf{x} \in \mathrm{R}(T)$, $\mathrm{R}(T)$ est un sous-espace de $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#sous-espace). $\blacksquare$
{: .prompt-info }

D’autre part, si l’on connaît une [base](/posts/linear-dependence-and-independence-basis-and-dimension/#base) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$, on peut obtenir un [ensemble générateur](/posts/vectors-and-linear-combinations/#engendrement) de l’image $\mathrm{R}(T)$ comme suit.

> **Théorème 2**  
> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$, une transformation linéaire $T: \mathbb{V} \to \mathbb{W}$ et une [base](/posts/linear-dependence-and-independence-basis-and-dimension/#base) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$, on a:
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Preuve**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Comme $\mathrm{R}(T)$ est un sous-espace, par le **Théorème 2** de [Espaces vectoriels, sous-espaces et matrices](/posts/vector-spaces-subspaces-and-matrices/#sous-espace),
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> De plus,
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Puisque $\beta$ est une base de $\mathbb{V}$,
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(où } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> $T$ étant linéaire,
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ Comme à la fois $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ et $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$, on a $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

Ce théorème reste valable lorsque la base $\beta$ est infinie.

### Théorème de la dimension

Le noyau et l’image étant des sous‑espaces particulièrement importants, on nomme également leurs [dimensions](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension).

> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$ et une transformation linéaire $T: \mathbb{V} \to \mathbb{W}$, supposons $\mathrm{N}(T), \mathrm{R}(T)$ de dimension finie.
> - **Nullité (nullity)**: la dimension de $\mathrm{N}(T)$, notée $\mathrm{nullity}(T)$
> - **Rang (rank)**: la dimension de $\mathrm{R}(T)$, notée $\mathrm{rank}(T)$
{: .prompt-info }

Pour une transformation linéaire, plus la nullité est grande, plus le rang est petit, et réciproquement.

> **Théorème 3: théorème de la dimension (dimension theorem)**  
> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$ et $T: \mathbb{V}\to \mathbb{W}$, si $\mathbb{V}$ est de dimension finie, alors
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Preuve

Soient $\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$, et soit une base de $\mathrm{N}(T)$ donnée par $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$.

D’après le **Corollaire 6-1** de [« Dépendance et indépendance linéaires, base et dimension »](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension-d-un-sous-espace), on peut étendre $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ en une base $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$.

Montrons maintenant que $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ est une base de $\mathrm{R}(T)$. D’abord, pour $1 \leq i \leq k$, $T(\mathbf{v}_i) = 0$, donc, par le [**Théorème 2**](#définition-noyau-et-image),

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Autrement dit, $S$ engendre $\mathrm{R}(T)$. Par le [**Corollaire 5-2 du théorème du remplacement**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension), il suffit de montrer que $S$ est libre pour conclure que $S$ est une base de $\mathrm{R}(T)$.

Si $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (avec $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$), la linéarité de $T$ donne

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Donc

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

Comme $\beta$ est une base de $\mathbb{V}$, l’unique solution de $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ est

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

d’où

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Ainsi, $S$ est libre et c’est une base de $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Transformations linéaires, injections et surjections

Pour les transformations linéaires, injection et surjection sont étroitement liées au rang et à la nullité.

> **Théorème 4**  
> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$ et une transformation linéaire $T: \mathbb{V} \to \mathbb{W}$,
>
> $$ T \text{ est injective } \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Théorème 5**  
> Si des espaces vectoriels $\mathbb{V}, \mathbb{W}$ de dimension finie ont même dimension, alors, pour $T: \mathbb{V} \to \mathbb{W}$, les quatre propositions suivantes sont équivalentes.
> 1. $T$ est injective.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ est surjective.
{: .prompt-info }

On peut démontrer les **Théorèmes 4** et **5** en utilisant le [théorème de la dimension](#théorème-de-la-dimension), les [propriétés 1 et 3 des transformations linéaires](#transformation-linéaire), ainsi que le **Théorème 6** de [« Dépendance et indépendance linéaires, base et dimension »](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension-d-un-sous-espace).

Ces deux résultats sont utiles pour déterminer si une transformation linéaire donnée est injective ou surjective.

> Pour un espace vectoriel $\mathbb{V}$ de dimension infinie et une transformation linéaire $T: \mathbb{V} \to \mathbb{V}$, injectivité et surjectivité ne sont pas équivalentes.
{: .prompt-warning }

Si une transformation linéaire est injective, le théorème suivant peut être utile, selon les cas, pour décider si un sous-ensemble donné est linéairement indépendant.

> **Théorème 6**  
> Pour des espaces vectoriels $\mathbb{V}, \mathbb{W}$, une transformation linéaire injective $T: \mathbb{V} \to \mathbb{W}$, et un sous-ensemble $S \subseteq \mathbb{V}$, on a
>
> $$ S \text{ est linéairement indépendant } \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \}\text{ est linéairement indépendant.} $$
>
{: .prompt-info }

## Transformations linéaires et bases

Un point crucial: l’action d’une transformation linéaire est entièrement déterminée par ses valeurs sur une base.

> **Théorème 7**  
> Pour des $F$‑espaces vectoriels $\mathbb{V}, \mathbb{W}$, une base $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$ et des vecteurs $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$, il existe une unique transformation linéaire $T: \mathbb{V} \to \mathbb{W}$ telle que
>
> $$ i = 1, 2, \dots, n \text{, } T(\mathbf{v}_i) = \mathbf{w}_i $$
>
> **Preuve**  
> Pour $\mathbf{x} \in \mathbb{V}$, la décomposition en combinaison linéaire par rapport à la base est unique:
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> Définissons $T: \mathbb{V} \to \mathbb{W}$ par
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> Alors:
>
> i) pour $i = 1, 2, \dots, n$, $T(\mathbf{v}_i) = \mathbf{w}_i$;
>
> ii) si une autre transformation linéaire $U: \mathbb{V} \to \mathbb{W}$ vérifie $U(\mathbf{v}\_i) = \mathbf{w}\_i$ pour $i = 1, 2, \dots, n$, alors, pour $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$,
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> Par i) et ii), la transformation linéaire vérifiant $T(\mathbf{v}\_i) = \mathbf{w}\_i$ pour $i = 1, 2, \dots, n$ est
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> et elle est unique. $\blacksquare$
>
> **Corollaire 7-1**  
> Pour deux espaces vectoriels $\mathbb{V}, \mathbb{W}$, si $\mathbb{V}$ possède une base finie $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$, alors, pour deux transformations linéaires $U, T: \mathbb{V} \to \mathbf{W}$, si $U(\mathbf{v}_i) = T(\mathbf{v}_i)$ pour $i = 1, 2, \dots, n$, on a $U = T$.  
> Autrement dit, <u>si deux transformations coïncident sur une base, elles sont égales</u>.
{: .prompt-info }
