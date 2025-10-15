---
title: "Dépendance et indépendance linéaires, base et dimension"
description: "Synthèse claire de la dépendance/indépendance linéaires, des bases et de la dimension des espaces vectoriels, avec définitions, théorèmes et corollaires clés."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prérequis
- [Vecteurs et combinaisons linéaires](/posts/vectors-and-linear-combinations/)
- [Espaces vectoriels, sous-espaces et matrices](/posts/vector-spaces-subspaces-and-matrices/)

## Dépendance linéaire et indépendance linéaire

Pour un [espace vectoriel](/posts/vector-spaces-subspaces-and-matrices/#espace-vectoriel) $\mathbb{V}$ et un [sous-espace](/posts/vector-spaces-subspaces-and-matrices/#sous-espace) $\mathbb{W}$, supposons que l’on veuille trouver le plus petit sous-ensemble fini $S$ qui [engendre](/posts/vectors-and-linear-combinations/#combinaison-linéaire-cmathbfv--dmathbfw) $\mathbb{W}$.

Étant donné $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ avec $\mathrm{span}(S) = \mathbb{W}$, comment déterminer s’il n’existe pas de sous-ensemble strict de $S$ qui engendre encore $\mathbb{W}$ ? Cela revient à décider si un vecteur extrait de $S$ peut s’écrire comme [combinaison linéaire](/posts/vectors-and-linear-combinations/#combinaison-linéaire-cmathbfv--dmathbfw) des autres. Par exemple, une condition nécessaire et suffisante pour exprimer $\mathbf{u}_4$ comme combinaison linéaire des trois autres est l’existence de scalaires $a_1, a_2, a_3$ satisfaisant

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

Or, il est fastidieux de monter à chaque fois un système linéaire pour chacun des quatre vecteurs $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4$. Modifions légèrement l’approche:

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

Si l’un des vecteurs de $S$ est combinaison linéaire des autres, alors il existe une écriture du vecteur nul comme combinaison linéaire des éléments de $S$ où au moins un des coefficients $a_1, a_2, a_3, a_4$ est non nul. La réciproque est vraie: s’il existe une écriture de $\mathbf{0}$ comme combinaison linéaire des vecteurs de $S$ avec au moins un coefficient non nul, alors l’un des vecteurs de $S$ est combinaison linéaire des autres.

Généralisons et définissons ainsi la **dépendance linéaire** et l’**indépendance linéaire**.

> **Définition**  
> Pour un sous-ensemble $S$ d’un espace vectoriel $\mathbb{V}$, s’il existe un nombre fini de vecteurs deux à deux distincts $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ et des scalaires $a_1, a_2, \dots, a_n$, pas tous nuls, tels que $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$, alors l’ensemble $S$ (et ces vecteurs) est dit **linéairement dépendant (linearly dependent)**. Dans le cas contraire, il est dit **linéairement indépendant (linearly independent)**.
{: .prompt-info }

Pour des vecteurs arbitraires $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$, on a $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$ lorsque $a_1 = a_2 = \cdots = a_n = 0$; c’est la **représentation triviale du vecteur nul (trivial representation of $\mathbf{0}$)**.

Les trois propositions suivantes sont toujours vraies dans tout espace vectoriel. En particulier, la **Proposition 3** est très utile pour décider si un ensemble fini est linéairement indépendant.

> - **Proposition 1**: L’ensemble vide est linéairement indépendant. Pour qu’un ensemble soit linéairement dépendant, il ne doit pas être vide.
> - **Proposition 2**: Un ensemble constitué d’un seul vecteur non nul est linéairement indépendant.
> - **Proposition 3**: Un ensemble est linéairement indépendant si et seulement si la seule combinaison linéaire qui donne $\mathbf{0}$ est la représentation triviale.
{: .prompt-info }

On aura également besoin des résultats suivants.

> **Théorème 1**  
> Si $\mathbb{V}$ est un espace vectoriel et $S_1 \subseteq S_2 \subseteq \mathbb{V}$, alors $S_1$ linéairement dépendant implique $S_2$ linéairement dépendant.
>
> **Corollaire 1-1**  
> Si $\mathbb{V}$ est un espace vectoriel et $S_1 \subseteq S_2 \subseteq \mathbb{V}$, alors $S_2$ linéairement indépendant implique $S_1$ linéairement indépendant.
{: .prompt-info }

> **Théorème 2**  
> Soient un espace vectoriel $\mathbb{V}$ et un sous-ensemble $S$ linéairement indépendant. Pour un vecteur $\mathbf{v} \in \mathbb{V}$ qui n’appartient pas à $S$, une condition nécessaire et suffisante pour que $S \cup \\{\mathbf{v}\\}$ soit linéairement dépendant est que $\mathbf{v} \in \mathrm{span}(S)$.
>
> En d’autres termes, **si aucun sous-ensemble strict de $S$ n’engendre le même espace que $S$, alors $S$ est linéairement indépendant.**
{: .prompt-info }

## Base et dimension

### Base

Un ensemble générateur $S$ de $\mathbb{W}$ qui est [linéairement indépendant](#dépendance-linéaire-et-indépendance-linéaire) possède une propriété remarquable: tout vecteur de $\mathbb{W}$ s’écrit nécessairement comme combinaison linéaire des vecteurs de $S$, et cette écriture est unique (**Théorème 3**). Ainsi, on appelle **base (basis)** d’un espace vectoriel tout ensemble générateur linéairement indépendant.

> **Définition d’une base**  
> Pour un espace vectoriel $\mathbb{V}$ et un sous-ensemble $\beta$, si $\beta$ est linéairement indépendant et engendre $\mathbb{V}$, alors $\beta$ est une **base (basis)** de $\mathbb{V}$. Les vecteurs de $\beta$ sont dits former une base de $\mathbb{V}$.
{: .prompt-info }

> On a $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ et $\emptyset$ est linéairement indépendant. Ainsi, l’ensemble vide est une base de l’espace réduit au point.
{: .prompt-tip }

En particulier, on appelle la base suivante de $F^n$ la **base canonique (standard basis)** de $F^n$.

> **Définition de la base canonique**  
> Dans l’espace vectoriel $F^n$, considérons les vecteurs
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> Alors l’ensemble $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ est une base de $F^n$, appelée **base canonique (standard basis)** de $F^n$.
{: .prompt-info }

> **Théorème 3**  
> Pour un espace vectoriel $\mathbb{V}$ et des vecteurs deux à deux distincts $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$, un ensemble $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ est une base de $\mathbb{V}$ si et seulement si « tout vecteur $\mathbf{v} \in \mathbb{V}$ s’écrit de manière unique comme combinaison linéaire de vecteurs de $\beta$ ». Autrement dit, il existe un unique $n$‑uplet de scalaires $(a_1, a_2, \dots, a_n)$ tel que
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

D’après le **Théorème 3**, lorsque $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ forment une base de l’espace vectoriel $\mathbb{V}$, alors, dans $\mathbb{V}$, à tout vecteur $\mathbf{v}$ correspond un unique $n$‑uplet de scalaires $(a_1, a_2, \dots, a_n)$, et réciproquement, à tout $n$‑uplet de scalaires correspond un unique vecteur $\mathbf{v}$. Nous y reviendrons en étudiant l’**invertibilité** et les **isomorphismes**; dans ce cas, $\mathbb{V}$ et $F^n$ sont <u>essentiellement équivalents</u>.

> **Théorème 4**  
> Si $S$ est un ensemble fini tel que $\mathrm{span}(S) = \mathbb{V}$, alors $S$ possède un sous-ensemble qui est une base de $\mathbb{V}$. En particulier, $\mathbb{V}$ admet une base finie dans ce cas.
{: .prompt-info }

> Un grand nombre d’espaces vectoriels satisfont le **Théorème 4**, mais pas tous. <u>Une base peut être infinie</u>.
{: .prompt-tip }

### Dimension

> **Théorème 5: théorème du remplacement (replacement theorem)**  
> Soit $G$ un ensemble de $n$ vecteurs tel que $\mathrm{span}(G) = \mathbb{V}$. Si $L$ est un sous-ensemble de $\mathbb{V}$ constitué de $m$ vecteurs linéairement indépendants, alors $m \leq n$. De plus, il existe un sous-ensemble $H \subseteq G$ de $n-m$ vecteurs tel que $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

On en déduit deux corollaires essentiels.

> **Corollaire 5-1 du théorème du remplacement**  
> Si l’espace vectoriel $\mathbb{V}$ admet une base finie, alors toute base de $\mathbb{V}$ est finie et elles ont toutes le même nombre de vecteurs.
{: .prompt-info }

Ainsi, le nombre de vecteurs d’une base de $\mathbb{V}$ est un invariant fondamental de $\mathbb{V}$, appelé sa **dimension (dimension)**.

> **Définition de la dimension**  
> Un espace vectoriel qui admet une base finie est **de dimension finie (finite dimension)**; le nombre d’éléments $n$ d’une base est la **dimension (dimension)** de l’espace, notée $\dim(\mathbb{V})$. Un espace vectoriel qui n’est pas de dimension finie est **de dimension infinie (infinite dimension)**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> La dimension d’un espace vectoriel dépend du corps sous-jacent.
> - Sur le corps des complexes $\mathbb{C}$, l’espace vectoriel $\mathbb{C}$ a dimension $1$; une base est $\\{1\\}$
> - Sur le corps des réels $\mathbb{R}$, l’espace vectoriel $\mathbb{C}$ a dimension $2$; une base est $\\{1,i\\}$
{: .prompt-tip }

Dans un espace vectoriel de dimension finie $\mathbb{V}$, aucun sous-ensemble ayant plus de $\dim(\mathbb{V})$ vecteurs ne peut être linéairement indépendant.

> **Corollaire 5-2 du théorème du remplacement**  
> Soit $\mathbb{V}$ un espace vectoriel de dimension $n$.
> 1. Tout ensemble générateur fini de $\mathbb{V}$ contient au moins $n$ vecteurs; tout ensemble générateur de $n$ vecteurs est une base de $\mathbb{V}$.
> 2. Tout sous-ensemble de $\mathbb{V}$ linéairement indépendant et formé de $n$ vecteurs est une base de $\mathbb{V}$.
        3. Tout sous-ensemble linéairement indépendant $L \subseteq \mathbb{V}$ peut être étendu en une base: il existe une base $\beta \supseteq L$ de $\mathbb{V}$.
{: .prompt-info }

### Dimension d’un sous-espace

> **Théorème 6**  
> Dans un espace vectoriel $\mathbb{V}$ de dimension finie, tout sous-espace $\mathbb{W}$ est de dimension finie et $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$. En particulier, si $\dim(\mathbb{W}) = \dim(\mathbb{V})$, alors $\mathbb{V} = \mathbb{W}$.
>
> **Corollaire 6-1**  
> Pour un sous-espace $\mathbb{W}$ d’un espace vectoriel $\mathbb{V}$ de dimension finie, toute base de $\mathbb{W}$ peut être étendue en une base de $\mathbb{V}$.
{: .prompt-info }

D’après le **Théorème 6**, la dimension d’un sous-espace de $\mathbb{R}^3$ peut être $0, 1, 2$ ou $3$.
- Dimension 0: l’espace réduit au point $\\{\mathbf{0}\\}$ (ne contenant que l’origine $\mathbf{0}$)
- Dimension 1: une droite passant par l’origine $\mathbf{0}$
- Dimension 2: un plan contenant l’origine $\mathbf{0}$
- Dimension 3: tout l’espace euclidien $\mathbb{R}^3$
