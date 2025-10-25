---
title: "Lineare Abhängigkeit und Unabhängigkeit, Basis und Dimension"
description: "Überblick über lineare Abhängigkeit und Unabhängigkeit sowie Basis und Dimension von Vektorräumen: Definitionen, zentrale Sätze, Korollare und anschauliche Beispiele."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Vektoren und lineare Kombinationen](/posts/vectors-and-linear-combinations/)
- [Vektorräume, Unterräume und Matrizen](/posts/vector-spaces-subspaces-and-matrices/)

## Lineare Abhängigkeit und lineare Unabhängigkeit

Für einen [Vektorraum](/posts/vector-spaces-subspaces-and-matrices/#vektorräume) $\mathbb{V}$ und einen [Unterraum](/posts/vector-spaces-subspaces-and-matrices/#unterräume) $\mathbb{W}$ wollen wir eine möglichst kleine endliche Teilmenge $S$ finden, die $\mathbb{W}$ [erzeugt](/posts/vectors-and-linear-combinations/#lineare-kombination-cmathbfv--dmathbfw).

Sei $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ mit $\mathrm{span}(S) = \mathbb{W}$. Wie entscheidet man, ob es eine echte Teilmenge von $S$ gibt, die $\mathbb{W}$ ebenfalls erzeugt? Das ist gleichbedeutend mit der Frage, ob sich ein aus $S$ entnommener Vektor als [lineare Kombination](/posts/vectors-and-linear-combinations/#lineare-kombinationen-von-vektoren) der übrigen Vektoren schreiben lässt. Beispielsweise ist hierfür für $\mathbf{u}_4$ genau dann eine Darstellung durch die restlichen drei Vektoren möglich, wenn es Skalare $a_1, a_2, a_3$ gibt mit

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

Da es jedoch lästig wäre, für jedes der vier Elemente $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4$ jeweils ein lineares Gleichungssystem aufzustellen, ändern wir die Gleichung geringfügig:

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

Ist ein Vektor aus $S$ eine lineare Kombination der anderen, so existiert bei der Darstellung des Nullvektors als lineare Kombination der Elemente aus $S$ eine Wahl von Koeffizienten $a_1, a_2, a_3, a_4$, von denen mindestens einer ungleich $0$ ist. Die Umkehrung gilt ebenso: Existiert eine solche nichttriviale Darstellung des Nullvektors, so ist ein Vektor aus $S$ eine lineare Kombination der übrigen.

Dies verallgemeinert man zur Definition von **linearer Abhängigkeit** und **linearer Unabhängigkeit**.

> **Definition**  
> Für eine Teilmenge $S$ eines Vektorraums $\mathbb{V}$ heißen $S$ und seine Vektoren **linear abhängig (linearly dependent)**, wenn es endlich viele paarweise verschiedene Vektoren $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ und Skalare $a_1, a_2, \dots, a_n$, von denen mindestens einer nicht $0$ ist, gibt mit $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$. Andernfalls heißen sie **linear unabhängig (linearly independent)**.
{: .prompt-info }

Für beliebige Vektoren $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ gilt: Wenn $a_1 = a_2 = \cdots = a_n = 0$, dann ist $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$. Dies heißt die **triviale Darstellung des Nullvektors (trivial representation of 0)**.

Für linear unabhängige Mengen gelten in jedem Vektorraum die folgenden drei Aussagen; insbesondere ist **Proposition 3** beim Testen der Unabhängigkeit einer endlichen Menge sehr nützlich.

> - **Proposition 1**: Die leere Menge ist linear unabhängig. Linear abhängig kann nur eine nichtleere Menge sein.
> - **Proposition 2**: Eine Menge, die nur aus einem einzigen von $0$ verschiedenen Vektor besteht, ist linear unabhängig.
> - **Proposition 3**: Eine Menge ist genau dann linear unabhängig, wenn die Darstellung von $\mathbf{0}$ als lineare Kombination der gegebenen Vektoren nur trivial ist.
{: .prompt-info }

Wichtige Sätze:

> **Satz 1**  
> Sei $\mathbb{V}$ ein Vektorraum und $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Ist $S_1$ linear abhängig, so ist es auch $S_2$.
>
> **Korollar 1-1**  
> Sei $\mathbb{V}$ ein Vektorraum und $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Ist $S_2$ linear unabhängig, so ist es auch $S_1$.
{: .prompt-info }

> **Satz 2**  
> Sei $\mathbb{V}$ ein Vektorraum und $S$ eine linear unabhängige Teilmenge. Für einen Vektor $\mathbf{v} \in \mathbb{V}$ mit $\mathbf{v} \notin S$ gilt: $S \cup \\{\mathbf{v}\\}$ ist genau dann linear abhängig, wenn $\mathbf{v} \in \mathrm{span}(S)$.
>
> Anders ausgedrückt: **Wenn keine echte Teilmenge von $S$ denselben Raum erzeugt wie $S$, dann ist $S$ linear unabhängig.**
{: .prompt-info }

## Basis und Dimension

### Basis

Eine [linear unabhängige](#lineare-abhängigkeit-und-lineare-unabhängigkeit) Erzeugermenge $S$ von $\mathbb{W}$ hat die Besonderheit, dass jeder Vektor aus $\mathbb{W}$ sich notwendigerweise als lineare Kombination der Elemente von $S$ darstellen lässt und diese Darstellung eindeutig ist (**Satz 3**). Daher nennt man eine linear unabhängige Erzeugermenge eines Vektorraums eine **Basis (basis)**.

> **Definition der Basis**  
> Ist $\mathbb{V}$ ein Vektorraum und $\beta \subseteq \mathbb{V}$, so heißt $\beta$ eine **Basis (basis)** von $\mathbb{V}$, wenn $\beta$ linear unabhängig ist und $\mathbb{V}$ erzeugt. In diesem Fall sagt man: Die Vektoren in $\beta$ bilden eine Basis von $\mathbb{V}$.
{: .prompt-info }

> Es gilt $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ und $\emptyset$ ist linear unabhängig. Daher ist $\emptyset$ eine Basis des Nullunterraums.
{: .prompt-tip }

Insbesondere heißt die folgende spezielle Basis von $F^n$ die **Standardbasis (standard basis)** von $F^n$.

> **Definition der Standardbasis**  
> Für den Vektorraum $F^n$ betrachten wir die Vektoren
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> Dann ist $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ eine Basis von $F^n$; sie heißt die **Standardbasis (standard basis)** von $F^n$.
{: .prompt-info }

> **Satz 3**  
> Sei $\mathbb{V}$ ein Vektorraum und seien $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$ paarweise verschieden. Dann ist $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ genau dann eine Basis von $\mathbb{V}$, wenn sich jeder Vektor $\mathbf{v} \in \mathbb{V}$ eindeutig als lineare Kombination der Vektoren aus $\beta$ schreiben lässt. Das heißt: Es existiert genau ein Skalar-$n$-Tupel $(a_1, a_2, \dots, a_n)$ mit
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

Nach **Satz 3** gilt: Bilden $n$ verschiedene Vektoren $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ eine Basis des Vektorraums $\mathbb{V}$, so ist innerhalb dieses Raums zu gegebenem $\mathbf{v}$ das zugehörige Skalar-$n$-Tupel $(a_1, a_2, \dots, a_n)$ eindeutig bestimmt und umgekehrt. Wir werden dies später im Rahmen von **Invertierbarkeit** und **Isomorphismus** erneut zusammenfassen; in diesem Fall sind $\mathbb{V}$ und $F^n$ <u>wesentlich gleich</u>.

> **Satz 4**  
> Sei $S$ eine endliche Menge mit $\mathrm{span}(S) = \mathbb{V}$. Dann enthält $S$ eine Teilmenge, die eine Basis von $\mathbb{V}$ ist. Insbesondere hat $\mathbb{V}$ in diesem Fall eine endliche Basis.
{: .prompt-info }

> Viele Vektorräume fallen in den Anwendungsbereich von **Satz 4**, aber nicht zwingend alle. <u>Eine Basis kann auch unendlich sein</u>.
{: .prompt-tip }

### Dimension

> **Satz 5: Austauschsatz (replacement theorem)**  
> Sei $G$ eine Menge aus $n$ Vektoren mit $\mathrm{span}(G) = \mathbb{V}$. Ist $L \subseteq \mathbb{V}$ eine Teilmenge aus $m$ linear unabhängigen Vektoren, so gilt $m \leq n$. Außerdem existiert eine Menge $H \subseteq G$ mit $n-m$ Elementen, so dass $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

Daraus folgen zwei äußerst wichtige Korollare.

> **Korollar 5-1 zum Austauschsatz**  
> Enthält der Vektorraum $\mathbb{V}$ eine endliche Basis, so sind alle Basen von $\mathbb{V}$ endlich und bestehen aus gleich vielen Vektoren.
{: .prompt-info }

Demnach ist die Anzahl der Vektoren in einer Basis von $\mathbb{V}$ eine unveränderliche, wesentliche Eigenschaft von $\mathbb{V}$; sie heißt **Dimension (dimension)**.

> **Definition der Dimension**  
> Ein Vektorraum heißt **endlichdimensional (finite dimension)**, wenn er eine endliche Basis besitzt; die Anzahl $n$ der Basiselemente heißt die **Dimension (dimension)** des gegebenen Vektorraums und wird mit $\dim(\mathbb{V})$ bezeichnet. Ein Vektorraum, der nicht endlichdimensional ist, heißt **unendlichdimensional (infinite dimension)**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> Die Dimension eines Vektorraums hängt vom zugrunde liegenden Körper ab.
> - Über dem komplexen Körper $\mathbb{C}$ hat der komplexe Vektorraum Dimension $1$, Basis $\\{1\\}$
> - Über dem reellen Körper $\mathbb{R}$ hat derselbe Raum Dimension $2$, Basis $\\{1,i\\}$
{: .prompt-tip }

In einem endlichdimensionalen Vektorraum $\mathbb{V}$ kann keine Teilmenge mit mehr als $\dim(\mathbb{V})$ Vektoren linear unabhängig sein.

> **Korollar 5-2 zum Austauschsatz**  
> Sei $\mathbb{V}$ ein Vektorraum der Dimension $n$.
> 1. Jede endliche Erzeugermenge von $\mathbb{V}$ enthält mindestens $n$ Vektoren; eine Erzeugermenge aus genau $n$ Vektoren ist eine Basis von $\mathbb{V}$.
> 2. Eine linear unabhängige Teilmenge von $\mathbb{V}$ mit genau $n$ Vektoren ist eine Basis von $\mathbb{V}$.
        3. Jede linear unabhängige Teilmenge $L \subseteq \mathbb{V}$ lässt sich zu einer Basis erweitern. Das heißt: Ist $L$ linear unabhängig, so existiert eine Basis $\beta \supseteq L$ von $\mathbb{V}$.
{: .prompt-info }

### Dimension von Unterräumen

> **Satz 6**  
> Ist $\mathbb{V}$ endlichdimensional, so ist jeder Unterraum $\mathbb{W}$ von $\mathbb{V}$ endlichdimensional und es gilt $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$. Insbesondere gilt aus $\dim(\mathbb{W}) = \dim(\mathbb{V}) \quad \Rightarrow \quad \mathbb{V} = \mathbb{W}.$
>
> **Korollar 6-1**  
> Zu einem Unterraum $\mathbb{W}$ eines endlichdimensionalen Vektorraums $\mathbb{V}$ lässt sich jede Basis von $\mathbb{W}$ zu einer Basis von $\mathbb{V}$ erweitern.
{: .prompt-info }

Nach **Satz 6** kann die Dimension eines Unterraums von $\mathbb{R}^3$ die Werte $0,1,2,3$ annehmen.
- 0-dimensional: der Nullunterraum $\\{\mathbf{0}\\}$
- 1-dimensional: eine durch den Ursprung ($\mathbf{0}$) verlaufende Gerade
- 2-dimensional: eine durch den Ursprung ($\mathbf{0}$) verlaufende Ebene
- 3-dimensional: der gesamte euklidische 3D-Raum
