---
title: "Espaces vectoriels, sous-espaces et matrices"
description: "Définition des espaces vectoriels et des sous‑espaces, avec exemples clés: espaces de matrices et de fonctions. Focus sur matrices symétriques/antisymétriques, triangulaires et diagonales."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Matrice**
>   - On note l’élément de la $i$-ème ligne et $j$-ème colonne d’une matrice $A$ par $A\_{ij}$ ou $a\_{ij}$
>   - **Élément diagonal (diagonal entry)**: l’élément $a\_{ij}$ avec $i=j$
>   - Les composantes $a\_{i1}, a\_{i2}, \dots, a\_{in}$ forment la $i$-ème **ligne (row)** de la matrice
>     - Chaque ligne d’une matrice peut être vue comme un vecteur de $F^n$
>     - Inversement, un vecteur ligne de $F^n$ peut être vu comme une autre matrice de taille $1 \times n$
>   - Les composantes $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ forment la $j$-ème **colonne (column)** de la matrice
>     - Chaque colonne d’une matrice peut être vue comme un vecteur de $F^m$
>     - Inversement, un vecteur colonne de $F^m$ peut être vu comme une autre matrice de taille $m \times 1$
>   - **Matrice nulle (zero matrix)**: matrice dont tous les éléments valent $0$, notée $O$
>   - **Matrice carrée (square matrix)**: matrice ayant autant de lignes que de colonnes
>   - Deux matrices $m \times n$ $A, B$ sont dites **égales** ($A=B$) si, pour tout $1 \leq i \leq m$, $1 \leq j \leq n$, on a $A\_{ij} = B\_{ij}$ (i.e. tous les éléments correspondants coïncident)
>   - **Matrice transposée (transpose matrix)**: pour une matrice $m \times n$ $A$, la matrice $n \times m$ $A^T$ obtenue en échangeant les lignes et les colonnes
>   - **Matrice symétrique (symmetric matrix)**: matrice carrée $A$ telle que $A^T = A$
>   - **Matrice antisymétrique (skew-symmetric matrix)**: matrice carrée $B$ telle que $B^T = -B$
>   - **Matrice triangulaire (triangular matrix)**
>     - **Triangulaire supérieure (upper triangular matrix)**: matrice dont tous les éléments sous la diagonale sont nuls (i.e. $i>j \Rightarrow A\_{ij}=0$), souvent notée $U$
>     - **Triangulaire inférieure (lower triangular matrix)**: matrice dont tous les éléments au-dessus de la diagonale sont nuls (i.e. $i<j \Rightarrow A\_{ij}=0$), souvent notée $L$
>   - **Matrice diagonale (diagonal matrix)**: matrice carrée $n \times n$ dont tous les éléments hors diagonale sont nuls (i.e. $i \neq j \Rightarrow M\_{ij}=0$), souvent notée $D$
> - Espaces vectoriels représentatifs
>   - **$n$-uplets $F^n$**:
>     - Ensemble de tous les $n$-uplets dont les composantes appartiennent à un corps $F$
>     - Noté $F^n$, c’est un espace vectoriel sur $F$
>   - **Espace des matrices (matrix space)**:
>     - Ensemble de toutes les matrices $m \times n$ à coefficients dans $F$
>     - Noté $\mathcal{M}\_{m \times n}(F)$, c’est un espace vectoriel
>   - **Espace des fonctions (function space)**:
>     - Pour un ensemble non vide $S$ sur $F$, l’ensemble de toutes les fonctions de $S$ vers $F$
>     - Noté $\mathcal{F}(S,F)$, c’est un espace vectoriel
> - **Sous-espace (subspace)**
>   - Un sous-ensemble $\mathbb{W}$ d’un espace vectoriel $\mathbb{V}$ sur $F$ est un **sous-espace** si, muni des mêmes opérations d’addition et de multiplication scalaire que $\mathbb{V}$, il est lui aussi un espace vectoriel sur $F$
>   - Pour tout espace vectoriel $\mathbb{V}$, $\mathbb{V}$ lui-même et $\\{0\\}$ sont des sous-espaces; en particulier, $\\{0\\}$ est le **sous-espace nul (zero subspace)**
>   - Si un sous-ensemble d’un espace vectoriel contient le vecteur nul et est fermé par rapport aux [combinaisons linéaires](/posts/vectors-and-linear-combinations/#combinaison-linéaire-de-vecteurs) (i.e. si $\mathrm{span}(\mathbb{W})=\mathbb{W}$), alors c’est un sous-espace
{: .prompt-info }

## Prérequis
- [Vecteurs et combinaisons linéaires](/posts/vectors-and-linear-combinations/)

## Espace vectoriel

Comme on l’a brièvement vu dans [Vecteurs et combinaisons linéaires](/posts/vectors-and-linear-combinations/#vecteur-au-sens-large--élément-dun-espace-vectoriel), la définition du vecteur et de l’espace vectoriel comme structure algébrique est la suivante.

> **Définition**  
> Un **espace vectoriel (vector space)** ou **espace linéaire (linear space)** $\mathbb{V}$ sur un corps $F$ est un ensemble muni de deux opérations, la **somme** et la **multiplication scalaire**, qui satisfont les huit axiomes suivants. Les éléments de $F$ sont des **scalaires (scalar)**, et les éléments de $\mathbb{V}$ sont des **vecteurs (vector)**.
>
> - **Somme (sum)**: pour $\mathbf{x}, \mathbf{y} \in \mathbb{V}$, l’opération associe un unique élément $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. On appelle $\mathbf{x} + \mathbf{y}$ la **somme** de $\mathbf{x}$ et $\mathbf{y}$.
> - **Multiplication scalaire (scalar multiplication)**: pour $a \in F$ et $\mathbf{x} \in \mathbb{V}$, l’opération associe un unique élément $a\mathbf{x} \in \mathbb{V}$. On appelle $a\mathbf{x}$ un **multiple scalaire (scalar multiple)** de $\mathbf{x}$.
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

On devrait écrire plus précisément « espace vectoriel sur $F$, $\mathbb{V}$ », mais le corps $F$ n’étant pas crucial dans le contexte, on le laisse souvent implicite et on écrit simplement « l’espace vectoriel $\mathbb{V}$ » lorsque cela ne prête pas à confusion.

### Espace des matrices

#### Vecteurs ligne et vecteurs colonne

On note $F^n$ l’ensemble de tous les $n$-uplets dont les composantes appartiennent au corps $F$. Pour $u = (a_1, a_2, \dots, a_n) \in F^n$ et $v = (b_1, b_2, \dots, b_n) \in F^n$, en définissant la somme et la multiplication scalaire comme suit, $F^n$ est un espace vectoriel sur $F$.

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

Isolés, les vecteurs de $F^n$ s’écrivent plutôt comme **vecteurs colonne (column vector)** que comme **vecteurs ligne (row vector)** $(a_1, a_2, \dots, a_n)$:

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

> Cependant, la notation en vecteur colonne prenant plus de place, on utilise souvent la [transposition](#matrice-transposée-matrice-symétrique-matrice-antisymétrique) et on écrit $(a_1, a_2, \dots, a_n)^T$.
{: .prompt-tip }

#### Matrices et espace des matrices

Une **matrice** $m \times n$ à coefficients dans $F$ est un tableau rectangulaire, noté par des lettres capitales en italique ($A, B, C$, etc.), de la forme suivante.

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- On note l’élément de la $i$-ème ligne et $j$-ème colonne d’une matrice $A$ par $A\_{ij}$ ou $a\_{ij}$.
- Chaque $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) appartient à $F$.
- Les éléments $a\_{ij}$ avec $i=j$ sont les **éléments diagonaux (diagonal entries)** de la matrice.
- Les composantes $a\_{i1}, a\_{i2}, \dots, a\_{in}$ forment la $i$-ème **ligne (row)** de la matrice. Chaque ligne peut être vue comme un vecteur de $F^n$; réciproquement, un vecteur ligne de $F^n$ peut être vu comme une autre matrice $1 \times n$.
- Les composantes $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ forment la $j$-ème **colonne (column)** de la matrice. Chaque colonne peut être vue comme un vecteur de $F^m$; réciproquement, un vecteur colonne de $F^m$ peut être vu comme une autre matrice $m \times 1$.
- La **matrice nulle (zero matrix)** $m \times n$ a tous ses éléments égaux à $0$ et se note $O$.
- Une **matrice carrée (square matrix)** a autant de lignes que de colonnes.
- Deux matrices $m \times n$ $A, B$ sont **égales** ($A=B$) si, pour tout $1 \leq i \leq m$, $1 \leq j \leq n$, $A\_{ij} = B\_{ij}$ (i.e. tous les éléments correspondants coïncident).

On note $\mathcal{M}\_{m \times n}(F)$ l’ensemble de toutes les matrices $m \times n$ dont les éléments appartiennent au corps $F$. Pour $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ et $c \in F$, en définissant la somme et la multiplication scalaire comme suit, $\mathcal{M}\_{m \times n}(F)$ est un espace vectoriel, appelé **espace des matrices (matrix space)**.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(où }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

Ces opérations prolongent naturellement celles définies sur $F^n$ et $F^m$.

### Espace des fonctions

Pour un ensemble non vide $S$ sur un corps $F$, $\mathcal{F}(S,F)$ désigne l’ensemble de toutes les fonctions de $S$ vers $F$. Dans $\mathcal{F}(S,F)$, pour tous $s \in S$, si $f(s) = g(s)$, alors on dit que les deux fonctions $f, g$ sont **égales** ($f=g$).

Pour $f,g \in \mathcal{F}(S,F)$, $c \in F$, $s \in S$, en définissant la somme et la multiplication scalaire comme suit, $\mathcal{F}(S,F)$ est un espace vectoriel, appelé **espace des fonctions (function space)**.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## Sous-espace

> **Définition**  
> Un sous-ensemble $\mathbb{W}$ d’un espace vectoriel $\mathbb{V}$ sur $F$ est un **sous-espace (subspace)** s’il est lui-même un espace vectoriel sur $F$ muni des mêmes opérations d’addition et de multiplication scalaire que $\mathbb{V}$.
{: .prompt-info }

Pour tout espace vectoriel $\mathbb{V}$, $\mathbb{V}$ lui-même et $\\{0\\}$ sont des sous-espaces; en particulier, $\\{0\\}$ est le **sous-espace nul (zero subspace)**.

On peut vérifier qu’un sous-ensemble est un sous-espace à l’aide du théorème suivant.

> **Théorème**  
> Pour un espace vectoriel $\mathbb{V}$ et un sous-ensemble $\mathbb{W}$, $\mathbb{W}$ est un sous-espace de $\mathbb{V}$ si et seulement s’il satisfait les trois conditions suivantes, les opérations étant celles définies dans $\mathbb{V}$.
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> En bref, s’il contient le vecteur nul et est fermé pour les [combinaisons linéaires](/posts/vectors-and-linear-combinations/#combinaison-linéaire-de-vecteurs) (i.e. si $\mathrm{span}(\mathbb{W})=\mathbb{W}$), alors c’est un sous-espace.
{: .prompt-info }

On a également les résultats suivants.

> **Théorème**  
> - Pour tout sous-ensemble $S$ d’un espace vectoriel $\mathbb{V}$, l’espace engendré $\mathrm{span}(S)$ est un sous-espace de $\mathbb{V}$ contenant $S$.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Tout sous-espace de $\mathbb{V}$ qui contient $S$ contient nécessairement l’espace engendré par $S$.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Théorème**  
> Pour les sous-espaces d’un espace vectoriel $\mathbb{V}$, l’intersection arbitraire de tels sous-espaces est à son tour un sous-espace de $\mathbb{V}$.
{: .prompt-info }

### Matrice transposée, matrice symétrique, matrice antisymétrique

La **matrice transposée (transpose matrix)** $A^T$ d’une matrice $m \times n$ $A$ est la matrice $n \times m$ obtenue en échangeant lignes et colonnes.

$$ (A^T)_{ij} = A_{ji} $$

$$ \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}^T
= \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 
\end{pmatrix} $$

Une matrice $A$ telle que $A^T = A$ est une **matrice symétrique (symmetric matrix)**; une matrice $B$ telle que $B^T = -B$ est une **matrice antisymétrique (skew-symmetric matrix)**. Les matrices symétriques et antisymétriques sont nécessairement carrées.

Les ensembles $\mathbb{W}\_1$ et $\mathbb{W}\_2$ constitués respectivement de toutes les matrices symétriques et de toutes les matrices antisymétriques de $\mathcal{M}\_{n \times n}(F)$ sont des sous-espaces de $\mathcal{M}\_{n \times n}(F)$. Autrement dit, $\mathbb{W}\_1$ et $\mathbb{W}\_2$ sont fermés pour la somme et la multiplication scalaire.

### Matrices triangulaires, matrice diagonale

Ces deux types de matrices sont particulièrement importants.

On regroupe d’abord les deux types suivants sous le nom de **matrices triangulaires (triangular matrix)**.
- **Triangulaire supérieure (upper triangular matrix)**: matrice dont tous les éléments sous la diagonale sont nuls (i.e. $i>j \Rightarrow A\_{ij}=0$), généralement notée $U$
- **Triangulaire inférieure (lower triangular matrix)**: matrice dont tous les éléments au-dessus de la diagonale sont nuls (i.e. $i<j \Rightarrow A\_{ij}=0$), généralement notée $L$

Une matrice carrée $n \times n$ dont tous les éléments hors diagonale sont nuls, i.e. $i \neq j \Rightarrow M\_{ij}=0$, est une **matrice diagonale (diagonal matrix)**, généralement notée $D$. Une matrice diagonale est à la fois triangulaire supérieure et triangulaire inférieure.

L’ensemble des matrices triangulaires supérieures, l’ensemble des matrices triangulaires inférieures et l’ensemble des matrices diagonales sont tous des sous-espaces de $\mathcal{M}\_{m \times n}(F)$.
