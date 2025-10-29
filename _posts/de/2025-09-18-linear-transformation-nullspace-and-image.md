---
title: "Lineare Abbildungen, Nullraum, Bild"
description: "Einführung in lineare Abbildungen: Definition sowie die Unterräume Nullraum (Kern) und Bild. Außerdem Nullität und Rang mit zentralen Sätzen wie dem Dimensionssatz."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Vektoren und lineare Kombinationen](/posts/vectors-and-linear-combinations/)
- [Vektorräume, Unterräume und Matrizen](/posts/vector-spaces-subspaces-and-matrices/)
- [Lineare Abhängigkeit und Unabhängigkeit, Basis und Dimension](posts/linear-dependence-and-independence-basis-and-dimension/)
- Injektion, Surjektion

## Lineare Abbildungen

Eine Abbildung, die die Struktur von Vektorräumen bewahrt, heißt **lineare Abbildung (linear transformation)**. Sie ist ein zentrales Konzept in der reinen und angewandten Mathematik, den Sozial- und Naturwissenschaften sowie der Technik.

> **Definition**  
> Seien $\mathbb{V}$ und $\mathbb{W}$ $F$-Vektorräume. Eine Abbildung $T: \mathbb{V} \to \mathbb{W}$ heißt **lineare Abbildung (linear transformation)** von $\mathbb{V}$ nach $\mathbb{W}$, wenn für alle $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ und $c \in F$ gilt:
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

Statt „$T$ ist eine lineare Abbildung“ sagt man kurz: $T$ ist **linear**. Eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ erfüllt die folgenden vier Eigenschaften.

> 1. $T$ linear $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ linear $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ linear $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ linear $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> Um die Linearität nachzuweisen, verwendet man in der Praxis häufig Eigenschaft 2.
{: .prompt-tip }

> Lineare Algebra lässt sich in der Geometrie breit einsetzen, da viele zentrale geometrische Transformationen linear sind. Insbesondere zählen **Rotation**, **Spiegelung** und **Projektion** zu den linearen Abbildungen.
{: .prompt-tip }

Die folgenden beiden linearen Abbildungen treten besonders häufig auf.

> **Identitätsabbildung und Nullabbildung**  
> Für $F$-Vektorräume $\mathbb{V}, \mathbb{W}$:
> - **Identitätsabbildung (identity transformation)**: $I_\mathbb{V}: \mathbb{V} \to \mathbb{V}$, definiert durch $I_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ für alle $\mathbf{x} \in \mathbb{V}$
> - **Nullabbildung (zero transformation)**: $T_0: \mathbb{V} \to \mathbb{W}$, definiert durch $T_0(\mathbf{x}) = \mathbf{0}$ für alle $\mathbf{x} \in \mathbb{V}$
{: .prompt-info }

Darüber hinaus fallen viele Konzepte unter lineare Abbildungen.

> **Beispiele für lineare Abbildungen**  
> - Rotation
> - Spiegelung
> - Projektion
> - [Transposition](/posts/vector-spaces-subspaces-and-matrices/#transponierte-matrix-symmetrische-matrix-schiefsymmetrische-matrix)
> - Ableitung differenzierbarer Funktionen
> - Integral stetiger Funktionen
{: .prompt-tip }

## Nullraum und Bild

### Definition von Nullraum und Bild

> **Definition**  
> Für Vektorräume $\mathbb{V}, \mathbb{W}$ und eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$:
> - **Nullraum (null space)** bzw. **Kern (kernel)**: die Menge aller $\mathbf{x} \in \mathbb{V}$ mit $T(\mathbf{x}) = \mathbf{0}$; bezeichnet mit $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **Bild (image)** bzw. **Wertebereich (range)**: die von $T$ angenommenen Funktionswerte; Teilmenge von $\mathbb{W}$, bezeichnet mit $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **z. B.** Für Vektorräume $\mathbb{V}, \mathbb{W}$, die Identitätsabbildung $I: \mathbb{V} \to \mathbb{V}$ und die Nullabbildung $T_0: \mathbb{V} \to \mathbb{W}$ gilt:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T_0) = \mathbb{V}$
> - $\mathrm{R}(T_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

Wichtig und immer wieder verwendet: Nullraum und Bild einer linearen Abbildung sind [Unterräume](/posts/vector-spaces-subspaces-and-matrices/#unterräume) der jeweiligen Vektorräume.

> **Satz 1**  
> Für Vektorräume $\mathbb{V}, \mathbb{W}$ und eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ sind $\mathrm{N}(T)$ bzw. $\mathrm{R}(T)$ Unterräume von $\mathbb{V}$ bzw. $\mathbb{W}$.
>
> **Beweis**  
> Bezeichne die Nullvektoren von $\mathbb{V}, \mathbb{W}$ mit $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$.
>
> Aus $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$ folgt $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$. Für $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T)$ und $c \in F$ gilt zudem:
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [Da $\mathbf{0}_\mathbb{V} \in \mathrm{N}(T)$ sowie $\mathbf{x} + \mathbf{y} \in \mathrm{N}(T)$ und $c\mathbf{x} \in \mathrm{N}(T)$ gilt, ist $\mathrm{N}(T)$ ein Unterraum von $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#unterräume).
>
> Ebenso folgt aus $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, dass $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$ ist. Für alle $\mathbf{x}, \mathbf{y} \in \mathrm{R}(T)$ und $c \in F$ existieren $\mathbf{v}, \mathbf{w} \in \mathbb{V}$ mit $T(\mathbf{v}) = \mathbf{x}$ und $T(\mathbf{w}) = \mathbf{y}$, sodass
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [Da $\mathbf{0}_\mathbb{W} \in \mathrm{R}(T)$ sowie $\mathbf{x} + \mathbf{y} \in \mathrm{R}(T)$ und $c\mathbf{x} \in \mathrm{R}(T)$ gilt, ist $\mathrm{R}(T)$ ein Unterraum von $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#unterräume). $\blacksquare$
{: .prompt-info }

Kennt man für Vektorräume $\mathbb{V}, \mathbb{W}$ und eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ eine [Basis](/posts/linear-dependence-and-independence-basis-and-dimension/#basis) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ von $\mathbb{V}$, so lässt sich eine [Erzeugermenge](/posts/vectors-and-linear-combinations/#erzeugung) von $\mathrm{R}(T)$ wie folgt finden.

> **Satz 2**  
> Für Vektorräume $\mathbb{V}, \mathbb{W}$, eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ und eine [Basis](/posts/linear-dependence-and-independence-basis-and-dimension/#basis) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ von $\mathbb{V}$ gilt
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Beweis**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Da $\mathrm{R}(T)$ ein Unterraum ist, folgt nach **Satz 2** aus [Vektorräume, Unterräume und Matrizen](/posts/vector-spaces-subspaces-and-matrices/#unterräume):
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> Außerdem gilt
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Da $\beta$ eine Basis von $\mathbb{V}$ ist,
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(mit } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> Wegen der Linearität von $T$ gilt
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ Da zugleich $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ und $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ gilt, folgt $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

Dieser Satz gilt auch, wenn $\beta$ unendlich ist.

### Dimensionssatz

Da Nullraum und Bild besonders wichtige Unterräume sind, versieht man auch ihre [Dimension](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension) mit speziellen Bezeichnungen.

> Für Vektorräume $\mathbb{V}, \mathbb{W}$ und eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ seien $\mathrm{N}(T), \mathrm{R}(T)$ endlichdimensional.
> - **Nullität (nullity)**: die Dimension von $\mathrm{N}(T)$; notiert als $\mathrm{nullity}(T)$
> - **Rang (rank)**: die Dimension von $\mathrm{R}(T)$; notiert als $\mathrm{rank}(T)$
{: .prompt-info }

Bei linearen Abbildungen gilt: Je größer die Nullität, desto kleiner der Rang – und umgekehrt.

> **Satz 3: Dimensionssatz (dimension theorem)**  
> Für Vektorräume $\mathbb{V}, \mathbb{W}$ und $T: \mathbb{V}\to \mathbb{W}$ gilt, falls $\mathbb{V}$ endlichdimensional ist:
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Beweis

Sei $\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$, und sei $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ eine Basis von $\mathrm{N}(T)$.

Nach ["Lineare Abhängigkeit und Unabhängigkeit, Basis und Dimension", **Korollar 6-1**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension-von-unterräumen) lässt sich $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ zu einer Basis $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ von $\mathbb{V}$ erweitern.

Wir zeigen nun, dass $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ eine Basis von $\mathrm{R}(T)$ ist. Für $1 \leq i \leq k$ gilt $T(\mathbf{v}_i) = 0$, daher folgt aus [**Satz 2**](#definition-von-nullraum-und-bild),

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Also ist $S$ eine Erzeugermenge von $\mathrm{R}(T)$. Nach [**Korollar 5-2 zum Austauschsatz**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension) genügt es, die lineare Unabhängigkeit von $S$ zu zeigen.

Gelte $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (mit $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$). Aus der Linearität von $T$ folgt

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Also existieren $c_1, \dots, c_k \in F$ mit

$$ \sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i
\ \Leftrightarrow\ 
\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0. $$

Da $\beta$ eine Basis von $\mathbb{V}$ ist, ist die einzige Lösung

$$ c_1 = \cdots = c_k = b_{k+1} = \cdots = b_n = 0, $$

und damit

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Somit ist $S$ linear unabhängig und eine Basis von $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Lineare Abbildungen sowie Injektion und Surjektion

Injektivität und Surjektivität stehen in engem Zusammenhang mit Rang und Nullität.

> **Satz 4**  
> Für Vektorräume $\mathbb{V}, \mathbb{W}$ und eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ gilt
>
> $$ T \text{ ist injektiv } \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Satz 5**  
> Haben die endlichdimensionalen Vektorräume $\mathbb{V}, \mathbb{W}$ dieselbe Dimension, so sind für eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ die folgenden Aussagen äquivalent:
> 1. $T$ ist injektiv.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ ist surjektiv.
{: .prompt-info }

Mit dem [Dimensionssatz](#dimensionssatz), den [Eigenschaften linearer Abbildungen 1 und 3](#lineare-abbildungen) sowie ["Lineare Abhängigkeit und Unabhängigkeit, Basis und Dimension", **Satz 6**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension-von-unterräumen) lassen sich **Satz 4** und **Satz 5** beweisen.

Beide Sätze sind nützlich, um zu entscheiden, ob eine gegebene lineare Abbildung injektiv oder surjektiv ist.

> Für einen unendlichdimensionalen Vektorraum $\mathbb{V}$ und $T: \mathbb{V} \to \mathbb{V}$ sind Injektivität und Surjektivität nicht äquivalent.
{: .prompt-warning }

Ist eine lineare Abbildung injektiv, kann folgender Satz beim Test der linearen Unabhängigkeit nützlich sein.

> **Satz 6**  
> Für Vektorräume $\mathbb{V}, \mathbb{W}$, eine injektive lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ und eine Teilmenge $S \subseteq \mathbb{V}$ gilt:
>
> $$ S \text{ ist linear unabhängig } \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \} \text{ ist linear unabhängig.} $$
>
{: .prompt-info }

## Lineare Abbildungen und Basen

Eine zentrale Eigenschaft linearer Abbildungen ist: Ihr Verhalten ist durch die Wirkung auf eine Basis festgelegt.

> **Satz 7**  
> Seien $\mathbb{V}, \mathbb{W}$ $F$-Vektorräume, $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ eine Basis von $\mathbb{V}$ und $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$ Vektoren. Dann existiert genau eine lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ mit
>
> $$ T(\mathbf{v}_i) = \mathbf{w}_i \quad \text{für } i = 1, 2, \dots, n. $$
>
> **Beweis**  
> Für jedes $\mathbf{x} \in \mathbb{V}$ existiert eindeutig eine Darstellung
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \quad (a_1, a_2, \dots, a_n \in F). $$
>
> Definiere die lineare Abbildung $T: \mathbb{V} \to \mathbb{W}$ durch
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. $$
>
> i) Für $i = 1, 2, \dots, n$ gilt $T(\mathbf{v}_i) = \mathbf{w}_i$.
>
> ii) Sei $U: \mathbb{V} \to \mathbb{W}$ eine weitere lineare Abbildung mit $U(\mathbf{v}\_i) = \mathbf{w}\_i$ für $i = 1, 2, \dots, n$. Für $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$ gilt dann
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}) $$
>
> $$ \therefore U = T. $$
>
> Aus i) und ii) folgt: Die lineare Abbildung mit $T(\mathbf{v}\_i) = \mathbf{w}\_i$ für $i = 1, 2, \dots, n$ ist eindeutig gegeben durch
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. $$
>
> $\blacksquare$
>
> **Korollar 7-1**  
> Seien $\mathbb{V}, \mathbb{W}$ Vektorräume und enthalte $\mathbb{V}$ eine endliche Basis $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$. Erfüllen zwei lineare Abbildungen $U, T: \mathbb{V} \to \mathbf{W}$ für $i = 1, 2, \dots, n$ die Gleichheit $U(\mathbf{v}_i) = T(\mathbf{v}_i)$, so gilt $U = T$.  
> Das heißt: <u>Stimmen die Funktionswerte auf einer Basis überein, so sind die linearen Abbildungen gleich.</u>
{: .prompt-info }
