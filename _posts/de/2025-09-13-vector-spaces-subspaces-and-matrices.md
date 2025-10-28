---
title: "Vektorräume, Unterräume und Matrizen"
description: "Definitionen von Vektorraum und Unterraum mit Beispielen (Matrix- und Funktionenräume). Fokus: symmetrische/schiefsymmetrische, obere/untere Dreiecksmatrizen sowie Diagonalmatrizen."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Matrix**
>   - Den Eintrag der i-ten Zeile und j-ten Spalte einer Matrix A schreibt man als $A\_{ij}$ oder $a\_{ij}$
>   - **Diagonaleintrag (diagonal entry)**: Eintrag $a\_{ij}$ mit $i=j$
>   - Die Einträge $a\_{i1}, a\_{i2}, \dots, a\_{in}$ heißen die i-te **Zeile (row)** der Matrix
>     - Jede Zeile einer Matrix lässt sich als Vektor in $F^n$ darstellen
>     - Zudem kann man einen Zeilenvektor in $F^n$ als eine weitere $1 \times n$-Matrix schreiben
>   - Die Einträge $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ heißen die j-te **Spalte (column)** der Matrix
>     - Jede Spalte einer Matrix lässt sich als Vektor in $F^m$ darstellen
>     - Zudem kann man einen Spaltenvektor in $F^m$ als eine weitere $m \times 1$-Matrix schreiben
>   - **Nullmatrix (zero matrix)**: Matrix, deren alle Einträge $0$ sind; mit $O$ bezeichnet
>   - **quadratische Matrix (square matrix)**: Matrix mit gleicher Zeilen- und Spaltenzahl
>   - Für zwei $m \times n$-Matrizen $A, B$ gilt: Wenn für alle $1 \leq i \leq m$, $1 \leq j \leq n$ die Gleichheit $A\_{ij} = B\_{ij}$ besteht (d. h. alle korrespondierenden Einträge stimmen überein), dann sind $A$ und $B$ **gleich** ($A=B$)
>   - **Transponierte Matrix (transpose matrix)**: Für eine $m \times n$-Matrix $A$ heißt die $n \times m$-Matrix $A^T$, die durch Vertauschen von Zeilen und Spalten entsteht, die Transponierte
>   - **symmetrische Matrix (symmetric matrix)**: quadratische Matrix $A$ mit $A^T = A$
>   - **schiefsymmetrische Matrix (skew-symmetric matrix)**: quadratische Matrix $B$ mit $B^T = -B$
>   - **Dreiecksmatrix (triangular matrix)**
>     - **obere Dreiecksmatrix (upper triangular matrix)**: Matrix, deren alle Einträge unterhalb der Diagonale $0$ sind (d. h. $i>j \Rightarrow A\_{ij}=0$); meist mit $U$ bezeichnet
>     - **untere Dreiecksmatrix (lower triangular matrix)**: Matrix, deren alle Einträge oberhalb der Diagonale $0$ sind (d. h. $i<j \Rightarrow A\_{ij}=0$); meist mit $L$ bezeichnet
>   - **Diagonalmatrix (diagonal matrix)**: quadratische $n \times n$-Matrix, deren alle Nicht-Diagonaleinträge $0$ sind (d. h. $i \neq j \Rightarrow M\_{ij}=0$); meist mit $D$ bezeichnet
> - typische Vektorräume
>   - **$n$-Tupel $F^n$**:
>     - die Menge aller $n$-Tupel mit Einträgen aus einem Körper $F$
>     - notiert als $F^n$; ein $F$-Vektorraum
>   - **Matrixraum (matrix space)**:
>     - die Menge aller $m \times n$-Matrizen mit Einträgen aus $F$
>     - notiert als $\mathcal{M}\_{m \times n}(F)$; ein Vektorraum
>   - **Funktionenraum (function space)**:
>     - für eine nichtleere Menge $S$ über $F$ die Menge aller Abbildungen von $S$ nach $F$
>     - notiert als $\mathcal{F}(S,F)$; ein Vektorraum
> - **Unterraum (subspace)**
>   - Ist eine Teilmenge $\mathbb{W}$ eines $F$-Vektorraums $\mathbb{V}$ mit denselben Operationen (Summe und Skalarmultiplikation) selbst ein $F$-Vektorraum, so heißt $\mathbb{W}$ ein **Unterraum (subspace)** von $\mathbb{V}$
>   - Für jeden Vektorraum $\mathbb{V}$ sind $\mathbb{V}$ selbst und $\\{0\\}$ Unterräume; insbesondere heißt $\\{0\\}$ der **Nullunterraum (zero subspace)**
>   - Enthält eine Teilmenge den Nullvektor und ist sie unter [linearen Kombinationen](/posts/vectors-and-linear-combinations/#lineare-kombinationen-von-vektoren) abgeschlossen ($\mathrm{span}(\mathbb{W})=\mathbb{W}$), so ist sie ein Unterraum
{: .prompt-info }

## Prerequisites
- [Vektoren und lineare Kombinationen](/posts/vectors-and-linear-combinations/)

## Vektorräume

Wie bereits kurz in [Vektoren und lineare Kombinationen](/posts/vectors-and-linear-combinations/#vektor-im-weiteren-sinn-element-eines-vektorraums) gesehen, lauten die Definitionen von Vektor und Vektorraum als algebraische Strukturen wie folgt.

> **Definition**  
> Ein **Vektorraum (vector space)** oder **linearer Raum (linear space)** $\mathbb{V}$ über einem Körper $F$ ist eine Menge mit zwei Operationen, **Addition** und **Skalarmultiplikation**, die die folgenden 8 Bedingungen erfüllen. Elemente von $F$ heißen **Skalare (scalar)**, Elemente von $\mathbb{V}$ heißen **Vektoren (vector)**.
>
> - **Summe (sum)**: Jedem Paar $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ wird ein eindeutiges Element $\mathbf{x} + \mathbf{y} \in \mathbb{V}$ zugeordnet. $\mathbf{x} + \mathbf{y}$ heißt die **Summe** von $\mathbf{x}$ und $\mathbf{y}$.
> - **Skalarmultiplikation (scalar multiplication)**: Jedem $a \in F$ und $\mathbf{x} \in \mathbb{V}$ wird ein eindeutiges Element $a\mathbf{x} \in \mathbb{V}$ zugeordnet. $a\mathbf{x}$ heißt die **Skalarmultiplikation (scalar multiple)** von $\mathbf{x}$ mit $a$.
>
> 1. Für alle $\mathbf{x},\mathbf{y} \in \mathbb{V}$ gilt $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (Kommutativgesetz der Addition)
> 2. Für alle $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$ gilt $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (Assoziativgesetz der Addition)
> 3. Es existiert ein $\mathbf{0} \in \mathbb{V}$ mit $\mathbf{x} + \mathbf{0} = \mathbf{x}$ für alle $\mathbf{x} \in \mathbb{V}$. (**Nullvektor**, neutrales Element der Addition)
> 4. Zu jedem $\mathbf{x} \in \mathbb{V}$ existiert ein $\mathbf{y} \in \mathbb{V}$ mit $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (additives Inverses)
> 5. Für alle $\mathbf{x} \in \mathbb{V}$ gilt $1\mathbf{x} = \mathbf{x}$. (neutrales Element der Multiplikation)
> 6. Für alle $a,b \in F$ und alle $\mathbf{x} \in \mathbb{V}$ gilt $(ab)\mathbf{x} = a(b\mathbf{x})$. (Assoziativität der Skalarmultiplikation)
> 7. Für alle $a \in F$ und alle $\mathbf{x},\mathbf{y} \in \mathbb{V}$ gilt $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (Distributivgesetz der Skalarmultiplikation über der Addition 1)
> 8. Für alle $a,b \in F$ und alle $\mathbf{x} \in \mathbb{V}$ gilt $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (Distributivgesetz der Skalarmultiplikation über der Addition 2)
{: .prompt-info }

Streng genommen sollte man “$F$-Vektorraum $\mathbb{V}$” schreiben; doch bei der Behandlung von Vektorräumen spielt der Körper nicht immer eine zentrale Rolle. Wenn keine Verwechslungsgefahr besteht, lassen wir $F$ weg und schreiben einfach “Vektorraum $\mathbb{V}$”.

### Matrixraum

#### Zeilen- und Spaltenvektoren

Die Menge aller $n$-Tupel mit Einträgen aus $F$ wird mit $F^n$ bezeichnet. Für $u = (a_1, a_2, \dots, a_n) \in F^n$, $v = (b_1, b_2, \dots, b_n) \in F^n$ ist $F^n$ ein $F$-Vektorraum, wenn man Summe und Skalarmultiplikation wie folgt definiert:

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

Vektoren aus $F^n$ schreibt man, wenn sie allein stehen, meist nicht als **Zeilenvektoren (row vector)** $(a_1, a_2, \dots, a_n)$, sondern als **Spaltenvektoren (column vector)**

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

.

> Da Spaltenvektoren jedoch viel Platz benötigen, verwendet man oft die [Transposition](#transponierte-matrix-symmetrische-matrix-schiefsymmetrische-matrix) und schreibt $(a_1, a_2, \dots, a_n)^T$.
{: .prompt-tip }

#### Matrizen und Matrixraum

Eine $m \times n$-**Matrix (matrix)** mit Einträgen aus $F$ ist ein rechteckiges Schema wie folgt und wird üblicherweise durch kursiv gesetzte Großbuchstaben ($A, B, C$ usw.) bezeichnet.

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- Den Eintrag der i-ten Zeile und j-ten Spalte einer Matrix $A$ schreibt man als $A\_{ij}$ oder $a\_{ij}$.
- Alle $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) sind Elemente von $F$.
- Ein Eintrag $a\_{ij}$ mit $i=j$ heißt **Diagonaleintrag (diagonal entry)**.
- Die Einträge $a\_{i1}, a\_{i2}, \dots, a\_{in}$ heißen die i-te **Zeile (row)** der Matrix. Jede Zeile lässt sich als Vektor in $F^n$ auffassen; ferner kann man einen Zeilenvektor aus $F^n$ als eine weitere $1 \times n$-Matrix schreiben.
- Die Einträge $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ heißen die j-te **Spalte (column)** der Matrix. Jede Spalte lässt sich als Vektor in $F^m$ auffassen; ferner kann man einen Spaltenvektor aus $F^m$ als eine weitere $m \times 1$-Matrix schreiben.
- Eine $m \times n$-Matrix, deren alle Einträge $0$ sind, heißt **Nullmatrix (zero matrix)** und wird mit $O$ bezeichnet.
- Eine Matrix mit gleicher Zeilen- und Spaltenzahl heißt **quadratische Matrix (square matrix)**.
- Für zwei $m \times n$-Matrizen $A, B$ gilt: Stimmen für alle $1 \leq i \leq m$, $1 \leq j \leq n$ die Einträge überein ($A\_{ij} = B\_{ij}$), so sind die Matrizen **gleich** ($A=B$).

Die Menge aller $m \times n$-Matrizen mit Einträgen aus $F$ wird mit $\mathcal{M}\_{m \times n}(F)$ bezeichnet. Für $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F),\ c \in F$ ist $\mathcal{M}\_{m \times n}(F)$ ein Vektorraum, wenn man Summe und Skalarmultiplikation wie folgt definiert; diesen Raum nennt man **Matrixraum (matrix space)**.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(wobei }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

Dies ist eine natürliche Erweiterung der in $F^n$ und $F^m$ definierten Operationen.

### Funktionenraum

Für eine nichtleere Menge $S$ über $F$ ist $\mathcal{F}(S,F)$ die Menge aller Abbildungen von $S$ nach $F$. Für $f,g \in \mathcal{F}(S,F)$ gilt: Sind für alle $s \in S$ die Funktionswerte gleich, $f(s) = g(s)$, so sind die Funktionen **gleich** ($f=g$).

Für $f,g \in \mathcal{F}(S,F),\ c \in F,\ s \in S$ ist $\mathcal{F}(S,F)$ ein Vektorraum, wenn man Summe und Skalarmultiplikation wie folgt definiert; diesen Raum nennt man **Funktionenraum (function space)**.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## Unterräume

> **Definition**  
> Ist eine Teilmenge $\mathbb{W}$ eines $F$-Vektorraums $\mathbb{V}$ mit denselben, in $\mathbb{V}$ definierten Operationen Summe und Skalarmultiplikation selbst ein $F$-Vektorraum, so heißt $\mathbb{W}$ ein **Unterraum (subspace)** von $\mathbb{V}$.
{: .prompt-info }

Für jeden Vektorraum $\mathbb{V}$ sind $\mathbb{V}$ selbst und $\\{0\\}$ Unterräume; insbesondere heißt $\\{0\\}$ der **Nullunterraum (zero subspace)**.

Ob eine Teilmenge ein Unterraum ist, lässt sich mit dem folgenden Satz prüfen.

> **Satz 1**  
> Für einen Vektorraum $\mathbb{V}$ und eine Teilmenge $\mathbb{W}$ ist $\mathbb{W}$ genau dann ein Unterraum von $\mathbb{V}$, wenn die folgenden drei Bedingungen erfüllt sind. Die Operationen sind dabei diejenigen von $\mathbb{V}$.
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> Kurz gesagt: Enthält die Menge den Nullvektor und ist sie unter [linearen Kombinationen](/posts/vectors-and-linear-combinations/#lineare-kombinationen-von-vektoren) abgeschlossen ($\mathrm{span}(\mathbb{W})=\mathbb{W}$), so ist sie ein Unterraum.
{: .prompt-info }

Außerdem gelten die folgenden Sätze.

> **Satz 2**  
> - Für jede Teilmenge $S$ eines Vektorraums $\mathbb{V}$ ist der von $S$ erzeugte Raum $\mathrm{span}(S)$ ein Unterraum von $\mathbb{V}$, der $S$ enthält.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Jeder Unterraum $\mathbb{W}$ von $\mathbb{V}$, der $S$ enthält, enthält notwendig auch den von $S$ erzeugten Raum.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Satz 3**  
> Für Unterräume eines Vektorraums $\mathbb{V}$ ist der beliebige Durchschnitt solcher Unterräume wiederum ein Unterraum von $\mathbb{V}$.
{: .prompt-info }

### Transponierte Matrix, symmetrische Matrix, schiefsymmetrische Matrix

Die **Transponierte (transpose matrix)** $A^T$ einer $m \times n$-Matrix $A$ ist die $n \times m$-Matrix, die durch Vertauschen von Zeilen und Spalten entsteht.

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

Eine Matrix $A$ mit $A^T = A$ heißt **symmetrische Matrix (symmetric matrix)**, eine Matrix $B$ mit $B^T = -B$ heißt **schiefsymmetrische Matrix (skew-symmetric matrix)**. Symmetrische und schiefsymmetrische Matrizen sind notwendigerweise quadratisch.

Bezeichnet $\mathbb{W}\_1$ bzw. $\mathbb{W}\_2$ die Menge aller symmetrischen bzw. schiefsymmetrischen Matrizen in $\mathcal{M}\_{n \times n}(F)$, so sind $\mathbb{W}\_1, \mathbb{W}\_2$ Unterräume von $\mathcal{M}\_{n \times n}(F)$, d. h. sie sind unter Addition und Skalarmultiplikation abgeschlossen.

### Dreiecksmatrizen, Diagonalmatrizen

Diese beiden Matrizenklassen sind besonders wichtig.

Zunächst fasst man die folgenden beiden Typen zur Klasse der **Dreiecksmatrizen (triangular matrix)** zusammen.
- **obere Dreiecksmatrix (upper triangular matrix)**: Matrix, deren alle Einträge unterhalb der Diagonale $0$ sind (d. h. $i>j \Rightarrow A\_{ij}=0$); meist mit $U$ bezeichnet
- **untere Dreiecksmatrix (lower triangular matrix)**: Matrix, deren alle Einträge oberhalb der Diagonale $0$ sind (d. h. $i<j \Rightarrow A\_{ij}=0$); meist mit $L$ bezeichnet

Eine quadratische $n \times n$-Matrix, deren alle Nicht-Diagonaleinträge $0$ sind, d. h. $i \neq j \Rightarrow M\_{ij}=0$, heißt **Diagonalmatrix (diagonal matrix)** und wird meist mit $D$ bezeichnet. Eine Diagonalmatrix ist zugleich obere wie untere Dreiecksmatrix.

Die Menge der oberen Dreiecksmatrizen, die Menge der unteren Dreiecksmatrizen und die Menge der Diagonalmatrizen sind allesamt Unterräume von $\mathcal{M}\_{m \times n}(F)$.
