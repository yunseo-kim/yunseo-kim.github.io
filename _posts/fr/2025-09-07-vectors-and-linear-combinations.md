---
title: "Vecteurs et combinaisons linéaires"
description: "Qu’est-ce qu’un vecteur ? Représentations (flèche, composantes), opérations de base (addition, multiplication scalaire), définition des combinaisons linéaires en R^n et notion de sous-espace engendré (span)."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Définition du vecteur**
>   - **Vecteur au sens étroit (vecteur euclidien)**: grandeur physique qui possède à la fois une norme et une direction
>   - **Au sens large, en algèbre linéaire, vecteur**: élément d’un espace vectoriel
> - **Représentations du vecteur**
>   - **Représentation par flèche**: la norme d’un vecteur est donnée par la longueur de la flèche et sa direction par l’orientation de la flèche. Cette représentation est intuitive et facile à visualiser, mais elle devient difficile pour les vecteurs de dimension ≥ 4 ou pour les vecteurs non euclidiens.
>   - **Représentation par composantes**: on place l’origine du vecteur à l’origine de l’espace de coordonnées et on décrit le vecteur par les coordonnées de son extrémité.
> - **Opérations de base sur les vecteurs**
>   - **Somme**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Multiplication scalaire**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Combinaison linéaire de vecteurs**
>   - Pour des vecteurs $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ et des scalaires $a_1, a_2, \dots, a_n$, un vecteur $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$ est appelé une **combinaison linéaire** de $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
>   - Les nombres $a_1, a_2, \dots, a_n$ sont les **coefficients** de cette combinaison linéaire.
> - **Sous-espace engendré**
>   - Pour un sous-ensemble non vide $S$ de l’espace vectoriel $\mathbb{V}$, l’ensemble de toutes les combinaisons linéaires formées avec les vecteurs de $S$, $\mathrm{span}(S)$.
>   - Par convention, $\mathrm{span}(\emptyset) = \{0\}$.
>   - Pour un sous-ensemble $S$ de l’espace vectoriel $\mathbb{V}$, si $\mathrm{span}(S) = \mathbb{V}$, on dit que $S$ **engendre** $\mathbb{V}$ (génère, span).
{: .prompt-info }

## Prerequisites
- Plan/espace de coordonnées
- Corps

## Qu’est-ce qu’un vecteur ?

### Vecteur au sens étroit : vecteur euclidien

> De nombreuses grandeurs physiques comme la force, la vitesse ou l’accélération portent non seulement une norme mais aussi une direction. Une grandeur qui possède à la fois une norme et une direction est appelée un **vecteur**.
{: .prompt-info }

La définition ci-dessus est celle des vecteurs en mécanique ou au niveau lycée. Un vecteur au sens géométrique, fondé sur l’intuition physique de « segment orienté avec norme et direction », est appelé rigoureusement un **vecteur euclidien**.

### Vecteur au sens large : élément d’un espace vectoriel

En algèbre linéaire, on adopte une définition plus générale et plus abstraite d’un vecteur comme structure algébrique.

> **Définition**  
> Un **espace vectoriel** (ou **espace linéaire**) $\mathbb{V}$ sur un corps $F$ est un ensemble muni de deux opérations, la **somme** et la **multiplication scalaire**, qui satisfont les huit axiomes suivants. Les éléments de $F$ sont des **scalaires** et les éléments de $\mathbb{V}$ sont des **vecteurs**.
>
> - **Somme**: pour $\mathbf{x}, \mathbf{y} \in \mathbb{V}$, l’opération associe un unique élément $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. On appelle $\mathbf{x} + \mathbf{y}$ la **somme** de $\mathbf{x}$ et $\mathbf{y}$.
> - **Multiplication scalaire**: pour $a \in F$ et $\mathbf{x} \in \mathbb{V}$, l’opération associe un unique élément $a\mathbf{x} \in \mathbb{V}$. On appelle $a\mathbf{x}$ le **multiple scalaire** de $\mathbf{x}$.
>
> 1. Pour tous $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (commutativité de l’addition)
> 2. Pour tous $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$, $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (associativité de l’addition)
> 3. Pour tout $\mathbf{x} \in \mathbb{V}$, il existe $\mathbf{0} \in \mathbb{V}$ tel que $\mathbf{x} + \mathbf{0} = \mathbf{x}$. (vecteur nul, élément neutre pour l’addition)
> 4. Pour chaque $\mathbf{x} \in \mathbb{V}$, il existe $\mathbf{y} \in \mathbb{V}$ tel que $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (inverse additif)
> 5. Pour tout $\mathbf{x} \in \mathbb{V}$, $1\mathbf{x} = \mathbf{x}$. (élément neutre pour la multiplication)
> 6. Pour tous $a,b \in F$ et tout $\mathbf{x} \in \mathbb{V}$, $(ab)\mathbf{x} = a(b\mathbf{x})$. (associativité de la multiplication scalaire)
> 7. Pour tout $a \in F$ et tous $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (distributivité de la multiplication scalaire par rapport à l’addition 1)
> 8. Pour tous $a,b \in F$ et tout $\mathbf{x} \in \mathbb{V}$, $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (distributivité de la multiplication scalaire par rapport à l’addition 2)
{: .prompt-info }

Cette définition en algèbre linéaire englobe une portée plus large, incluant le [vecteur euclidien](#vecteur-au-sens-étroit-vecteur-euclidien). On peut vérifier que les [vecteurs euclidiens](#vecteur-au-sens-étroit-vecteur-euclidien) satisfont aussi les huit axiomes ci-dessus.

L’origine et le développement de la notion de vecteur sont intimement liés aux problèmes pratiques soulevés en physique — quantifier des concepts tels que force, mouvement, rotation ou champ. D’abord introduit comme [vecteur euclidien](#vecteur-au-sens-étroit-vecteur-euclidien) pour modéliser mathématiquement des phénomènes naturels, le concept a été généralisé et théorisé par les mathématiciens, qui ont formalisé des structures telles que l’espace vectoriel, le produit scalaire et le produit vectoriel. Autrement dit, le vecteur est un concept demandé par la physique et établi par les mathématiques — un produit interdisciplinaire né de leurs interactions étroites.

Les vecteurs euclidiens de la mécanique classique peuvent être exprimés dans un [cadre plus général](#vecteur-au-sens-large-élément-d-un-espace-vectoriel), et la physique moderne utilise non seulement les [vecteurs euclidiens](#vecteur-au-sens-étroit-vecteur-euclidien) mais aussi des concepts plus abstraits définis en mathématiques (espaces vectoriels, espaces fonctionnels, etc.) auxquels on attribue un sens physique. Il est donc inapproprié d’opposer simplement une « définition physique » et une « définition mathématique » du vecteur.

Nous reviendrons plus tard sur les espaces vectoriels; concentrons-nous d’abord sur le vecteur au sens étroit, le vecteur euclidien que l’on peut représenter géométriquement dans un espace de coordonnées. Disposer d’exemples intuitifs de vecteurs euclidiens aide à comprendre ensuite la généralisation à d’autres types de vecteurs.

## Représentations du vecteur
### Représentation par flèche

C’est la représentation la plus intuitive et la plus répandue. La norme du vecteur est donnée par la longueur de la flèche, et sa direction par l’orientation de la flèche.

![Vecteur euclidien de A vers B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Source de l’image*
> - Auteur: utilisateur Wikipédia [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - Licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

Bien qu’intuitive, cette représentation a des limites évidentes en dimension 4 et au-delà. De plus, nous aurons à traiter des vecteurs non euclidiens, difficiles à représenter géométriquement; il est donc utile de se familiariser avec la représentation par composantes décrite ci-dessous.

### Représentation par composantes

Indépendamment de sa position, deux vecteurs sont identiques s’ils ont même norme et même direction. Ainsi, dans un espace de coordonnées donné, en plaçant l’origine du vecteur à l’origine de l’espace, <u>un vecteur de dimension $n$ correspond à un point quelconque de l’espace de dimension $n$</u>, et on peut représenter le vecteur par les coordonnées de son extrémité. C’est la **représentation par composantes**.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ or } \mathbb{C}^n $$

![Vecteur position](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Source de l’image*
> - Auteur: utilisateur Wikimédia [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - Licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Opérations de base sur les vecteurs

Les opérations de base sont la **somme** et la **multiplication scalaire**. Toute opération vectorielle peut s’exprimer comme combinaison de ces deux opérations.

### Somme

La somme de deux vecteurs est encore un vecteur, et les composantes du vecteur somme sont les sommes composante par composante.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Multiplication scalaire

On peut agrandir ou réduire un vecteur en le multipliant par un scalaire. Le résultat s’obtient en multipliant chaque composante par ce scalaire.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Multiplication scalaire de vecteurs](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Source de l’image*
> - Auteur: utilisateur Wikipédia [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - Licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Combinaison linéaire de vecteurs

De même que l’analyse part des nombres $x$ et des fonctions $f(x)$, l’algèbre linéaire part des vecteurs $\mathbf{v}, \mathbf{w}, \dots$ et des combinaisons linéaires $c\mathbf{v} + d\mathbf{w} + \cdots$. Toute combinaison linéaire se compose des deux opérations de base, [somme](#somme) et [multiplication scalaire](#multiplication-scalaire).

> Pour des vecteurs $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ et des scalaires $a_1, a_2, \dots, a_n$, un vecteur $\mathbf{v}$ vérifiant
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> est appelé une **combinaison linéaire** de $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$. Les nombres $a_1, a_2, \dots, a_n$ en sont les **coefficients**.
{: .prompt-info }

Pourquoi les combinaisons linéaires sont-elles importantes ? Considérons la situation suivante: **$n$ vecteurs d’un espace de dimension $m$ constituent les $n$ colonnes d’une matrice $m \times n$**.

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

Voici les deux points essentiels.

1. **Exprimez toutes les combinaisons linéaires possibles $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n$.** Que forment-elles ?
2. **Trouvez des nombres $x_1, x_2, \dots, x_n$** tels que la sortie désirée $Ax = b$ soit obtenue.

Nous reviendrons plus tard sur la deuxième question; concentrons-nous d’abord sur la première. Pour simplifier, examinons le cas de deux vecteurs non nuls ($n=2$) dans le plan ($m=2$).

### Combinaison linéaire $c\mathbf{v} + d\mathbf{w}$

Dans le plan, un vecteur $\mathbf{v}$ possède deux composantes. Pour tout scalaire $c$, <u>le vecteur $c\mathbf{v}$ est parallèle à $\mathbf{v}$ et décrit une droite infinie dans le plan $xy$ passant par l’origine</u>.

Si un second vecteur $\mathbf{w}$ n’est pas sur cette droite (i.e. $\mathbf{v}$ et $\mathbf{w}$ ne sont pas parallèles), alors $d\mathbf{w}$ décrit une autre droite. En combinant ces deux droites, on voit que **la combinaison linéaire $c\mathbf{v} + d\mathbf{w}$ remplit un plan passant par l’origine**.

![Combinaisons linéaires de deux vecteurs](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Source de l’image*
> - Auteur: utilisateur Wikimédia [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

### Engendrement

Ainsi, les combinaisons linéaires de vecteurs engendrent un espace; on parle de **sous-espace engendré (span)**.

> **Définition**  
> Soit $S$ un sous-ensemble non vide de l’espace vectoriel $\mathbb{V}$. L’ensemble de toutes les combinaisons linéaires formées avec les vecteurs de $S$ s’appelle le **sous-espace engendré** de $S$ (span) et se note $\mathrm{span}(S)$. Par convention, $\mathrm{span}(\emptyset)=\{0\}$.
{: .prompt-info }

> **Définition**  
> Pour un sous-ensemble $S$ de l’espace vectoriel $\mathbb{V}$, si $\mathrm{span}(S)=\mathbb{V}$, on dit que $S$ **engendre** $\mathbb{V}$ (génère, span).
{: .prompt-info }

Bien que nous n’ayons pas encore présenté des notions comme sous-espace ou base, garder cet exemple en tête aidera à comprendre la notion d’espace vectoriel.
