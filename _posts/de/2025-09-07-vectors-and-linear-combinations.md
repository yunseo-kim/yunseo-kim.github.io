---
title: "Vektoren und lineare Kombinationen"
description: "Einführung in Vektoren: Definition, Darstellung, Grundoperationen (Addition, Skalarmultiplikation) und das Konzept der linearen Kombination im Vektorraum."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Definition des Vektors**
>   - **Vektor im engen Sinn (euklidischer Vektor)**: physikalische Größe mit Betrag und Richtung
>   - **Vektor im weiteren Sinn, in der Linearen Algebra**: Element eines Vektorraums
> - **Darstellungsweisen von Vektoren**
>   - **Pfeildarstellung**: Der Betrag eines Vektors entspricht der Länge des Pfeils, die Richtung dem Pfeilrichtungssinn. Gut visuell und intuitiv, aber für hochdimensionale (≥4D) oder nicht-euklidische Vektoren ungeeignet.
>   - **Komponentendarstellung**: Den Startpunkt des Vektors im Koordinatenraum auf den Ursprung legen und den Vektor durch die Koordinaten seines Endpunkts darstellen.
> - **Grundoperationen mit Vektoren**
>   - **Summe**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Skalarmultiplikation**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Lineare Kombination von Vektoren**
>   - Für endlich viele Vektoren $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ und Skalare $a_1, a_2, \dots, a_n$ heißt ein Vektor $\mathbf{v}$ mit $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$ eine **lineare Kombination** von $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
>   - Dabei heißen $a_1, a_2, \dots, a_n$ die **Koeffizienten** der linearen Kombination.
{: .prompt-info }

## Prerequisites
- Koordinatenebene/Koordinatenraum
- Körper

## Was ist ein Vektor?

### Vektor im engen Sinn: euklidischer Vektor

> Viele physikalische Größen wie Kraft, Geschwindigkeit oder Beschleunigung besitzen nicht nur einen Betrag, sondern auch eine Richtung. Solche Größen mit Betrag und Richtung nennt man **Vektoren (vector)**.
{: .prompt-info }

Die obige Definition ist diejenige, die in der Mechanik der Physik oder in der Schulmathematik verwendet wird. Ein Vektor in diesem engeren, geometrischen Sinn als „gerichtete Strecke mit Betrag und Richtung“, der auf physikalischer Intuition beruht, heißt präziser **euklidischer Vektor (Euclidean vector)**.

### Vektor im weiteren Sinn: Element eines Vektorraums

In der Linearen Algebra definiert man Vektoren als eine abstraktere algebraische Struktur mit weiter gefasstem Bedeutungsumfang als die euklidischen Vektoren:

> **Definition**  
> Ein **Vektorraum** (auch: **linearer Raum**) $V$ über einem Körper $F$ ist eine Menge mit zwei Operationen, **Addition** und **Skalarmultiplikation**, die die folgenden 8 Bedingungen erfüllen. Elemente von $F$ heißen **Skalare**, Elemente von $V$ heißen **Vektoren**.
>
> - **Addition (Summe)**: Jedem Paar $x, y \in V$ wird ein eindeutiges Element $x + y \in V$ zugeordnet. $x + y$ heißt die **Summe** von $x$ und $y$.
> - **Skalarmultiplikation**: Jedem $a \in F$ und $x \in V$ wird ein eindeutiges Element $ax \in V$ zugeordnet. $ax$ heißt die **Skalarmultiplikation** von $a$ und $x$.
>
> 1. Für alle $x,y \in V$ gilt $x + y = y + x$. (Kommutativgesetz der Addition)
> 2. Für alle $x,y,z \in V$ gilt $(x+y)+z = x+(y+z)$. (Assoziativgesetz der Addition)
> 3. Es existiert ein $0 \in V$ mit $x + 0 = x$ für alle $x \in V$. (**Nullvektor**, neutrales Element der Addition)
> 4. Zu jedem $x \in V$ existiert ein $y \in V$ mit $x+y=0$. (additives inverses Element)
> 5. Für alle $x \in V$ gilt $1x = x$. (neutrales Element der Multiplikation)
> 6. Für alle $a,b \in F$ und alle $x \in V$ gilt $(ab)x = a(bx)$. (Assoziativität der Skalarmultiplikation)
> 7. Für alle $a \in F$ und alle $x,y \in V$ gilt $a(x+y) = ax + ay$. (Distributivgesetz der Skalarmultiplikation über der Addition 1)
> 8. Für alle $a,b \in F$ und alle $x \in V$ gilt $(a+b)x = ax + bx$. (Distributivgesetz der Skalarmultiplikation über der Addition 2)
{: .prompt-info }

Diese vektoralgebraische Definition umfasst einen größeren Bereich und schließt den zuvor erwähnten [euklidischen Vektor](#vektor-im-engen-sinn-euklidischer-vektor) mit ein. Man kann überprüfen, dass auch der [euklidische Vektor](#vektor-im-engen-sinn-euklidischer-vektor) die acht Eigenschaften erfüllt.

Der Ursprung und die Entwicklung des Vektorbegriffs sind eng mit praktischen Fragestellungen der Physik verknüpft, etwa dem Bestreben, Größen wie Kräfte, Bewegungen, Rotationen oder Felder quantitativ zu beschreiben. Aus physikalischer Motivation wurde der Begriff zunächst als [euklidischer Vektor](#vektor-im-engen-sinn-euklidischer-vektor) formuliert; später hat die Mathematik diese physikalischen Konzepte verallgemeinert und theoretisch gefasst und dabei formale Strukturen wie Vektorraum, Skalarprodukt und Kreuzprodukt etabliert. Vektoren sind somit ein Konzept, das die Physik fordert und die Mathematik präzisiert hat, und eher ein interdisziplinäres Produkt als ein rein mathematisches.

Die in der klassischen Mechanik behandelten [euklidischen Vektoren](#vektor-im-engen-sinn-euklidischer-vektor) lassen sich in einem [allgemeineren Rahmen](#vektor-im-weiteren-sinn-element-eines-vektorraums) mathematisch darstellen; und in der modernen Physik verwendet man neben [euklidischen Vektoren](#vektor-im-engen-sinn-euklidischer-vektor) auch abstraktere, in der Mathematik definierte Begriffe wie Vektorräume oder Funktionenräume und versieht sie mit physikalischer Bedeutung. Es ist daher unangemessen, die beiden Definitionen schlicht als „physikalische“ bzw. „mathematische“ Definition zu verstehen.

Eine ausführlichere Betrachtung von Vektorräumen folgt später. Zunächst fokussieren wir uns auf den engeren, geometrisch im Koordinatenraum darstellbaren Begriff, den euklidischen Vektor. Intuitive Beispiele euklidischer Vektoren helfen auch beim späteren Verallgemeinern auf andere Vektortypen.

## Darstellung von Vektoren
### Pfeildarstellung

Dies ist die geläufigste, die geometrische Intuition am besten nutzende Darstellung. Der Betrag eines Vektors entspricht der Länge des Pfeils, die Richtung dem Pfeilrichtungssinn.

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Bildquelle*
> - Urheber: Wikipedia-Nutzer [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

So anschaulich diese Darstellung ist, hat sie doch klare Grenzen für hochdimensionale Vektoren (ab 4D). Außerdem werden wir später nicht-euklidische Vektoren betrachten, die sich von vornherein kaum geometrisch visualisieren lassen. Daher lohnt es sich, die folgende Komponentendarstellung einzuüben.

### Komponentendarstellung

Vektoren gelten als identisch, wenn sie unabhängig von ihrer Lage den gleichen Betrag und die gleiche Richtung besitzen. Ist also ein Koordinatenraum gegeben, so kann man den Startpunkt des Vektors auf den Ursprung fixieren; dann <u>entspricht ein $n$-dimensionaler Vektor einem beliebigen Punkt im $n$-dimensionalen Raum</u>, und man kann den Vektor durch die Koordinaten seines Endpunkts darstellen. Diese Darstellung heißt **Komponentendarstellung**.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ oder } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Bildquelle*
> - Urheber: Wikimedia-Nutzer [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Grundoperationen mit Vektoren

Die grundlegenden Operationen sind **Summe** und **Skalarmultiplikation**. Alle weiteren Vektoroperationen lassen sich als Kombination dieser beiden ausdrücken.

### Vektorsumme

Die Summe zweier Vektoren ist wieder ein Vektor; dessen Komponenten ergeben sich komponentenweise als Summe der Komponenten der Summanden.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Skalarmultiplikation

Vektoren lassen sich strecken oder stauchen; dies wird durch die Multiplikation mit einem Skalar ausgedrückt. Das Ergebnis entspricht der komponentenweisen Multiplikation mit dem Skalar.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Bildquelle*
> - Urheber: Wikipedia-Nutzer [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Lineare Kombinationen von Vektoren

Wie die Analysis von Zahlen $x$ und Funktionen $f(x)$ ausgeht, beginnt die Lineare Algebra mit Vektoren $\mathbf{v}, \mathbf{w}, \dots$ und linearen Kombinationen $c\mathbf{v} + d\mathbf{w} + \cdots$. Jede lineare Kombination von Vektoren ist eine Kombination der beiden Grundoperationen, [Summe](#vektorsumme) und [Skalarmultiplikation](#skalarmultiplikation).

> Für endlich viele Vektoren $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ und Skalare $a_1, a_2, \dots, a_n$ heißt ein Vektor $\mathbf{v}$, der
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> erfüllt, eine **lineare Kombination** von $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
> Dabei heißen $a_1, a_2, \dots, a_n$ die **Koeffizienten** dieser linearen Kombination.
{: .prompt-info }

Warum sind lineare Kombinationen wichtig? Betrachte folgende Situation: **$n$ Vektoren im $m$-dimensionalen Raum bilden die $n$ Spalten einer $m \times n$-Matrix.**

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

Zentral sind zwei Fragen:

1. **Beschreibe alle möglichen linearen Kombinationen $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n$.** Welche Menge bilden sie?
2. Finde **Zahlen $x_1, x_2, \dots, x_n$**, die einen gewünschten Ausgabeverktor $Ax = b$ ergeben.

Die Antwort auf die zweite Frage betrachten wir später; zunächst konzentrieren wir uns auf die erste. Zur Vereinfachung nehmen wir als Beispiel zwei 2D-Vektoren ($m=2$, $n=2$), die beide nicht der Nullvektor sind.

### Lineare Kombination $c\mathbf{v} + d\mathbf{w}$

Ein Vektor $\mathbf{v}$ in der Ebene besitzt zwei Komponenten. Für jedes Skalar $c$ bildet <u>$c\mathbf{v}$ eine unendliche Gerade in der $xy$-Ebene durch den Ursprung, die parallel zu $\mathbf{v}$ verläuft</u>.

Liegt ein zweiter Vektor $\mathbf{w}$ nicht auf dieser Geraden (d. h. $\mathbf{v}$ und $\mathbf{w}$ sind nicht parallel), dann bildet $d\mathbf{w}$ eine zweite Gerade. Kombiniert man beide, so erkennt man, dass **die lineare Kombination $c\mathbf{v} + d\mathbf{w}$ eine durch den Ursprung verlaufende Ebene bildet**.

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Bildquelle*
> - Urheber: Wikimedia-Nutzer [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

Lineare Kombinationen von Vektoren erzeugen somit einen Vektorraum; dies nennt man die **lineare Hülle (span)**. Auch ohne die Begriffe des Vektorraums bereits formal eingeführt zu haben, hilft dieses Beispiel, das Konzept später besser zu verstehen.
