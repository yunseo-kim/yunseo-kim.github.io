---
title: Folgen und Reihen
description: Wir betrachten grundlegende Konzepte der Infinitesimalrechnung wie die Definition von Folgen und Reihen, Konvergenz und Divergenz von Folgen, Konvergenz und Divergenz von Reihen sowie die Definition der Eulerschen Zahl e.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## Folgen
In der Infinitesimalrechnung bezieht sich der Begriff **Folge(sequence)** hauptsächlich auf unendliche Folgen. Eine Folge ist also eine Funktion, die auf der Menge der **natürlichen Zahlen(natural number)** definiert ist:

$$ \mathbb{N} := \{1,2,3,\dots\} $$

* Wenn die Werte dieser Funktion reelle Zahlen sind, spricht man von einer 'reellen Folge', bei komplexen Zahlen von einer 'komplexen Folge', bei Punkten von einer 'Punktfolge', bei Matrizen von einer 'Matrizenfolge', bei Funktionen von einer 'Funktionenfolge' und bei Mengen von einer 'Mengenfolge'. All diese können einfach als 'Folge' bezeichnet werden.

Für den **Körper der reellen Zahlen(the field of real numbers)** $\mathbb{R}$ und eine Folge $\mathbf{a}: \mathbb{N} \to \mathbb{R}$ setzt man üblicherweise:

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

Diese Folge wird dann dargestellt als:

$$ a_1,\, a_2,\, a_3,\, \dots $$

oder

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

> *Bei der Definition einer Folge kann man statt der Menge der natürlichen Zahlen $\mathbb{N}$ auch die Menge der nicht-negativen ganzen Zahlen
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> oder
>
> $$\{2,3,4,\dots \}$$
>
> als Definitionsbereich wählen. Zum Beispiel ist bei der Theorie der Potenzreihen ein Definitionsbereich von $\mathbb{N}_0$ natürlicher.
{: .prompt-info }

## Konvergenz und Divergenz
Wenn eine Folge $(a_n)$ gegen eine reelle Zahl $l$ konvergiert, schreibt man:

$$ \lim_{n\to \infty} a_n = l $$

Dabei wird $l$ als **Grenzwert** der Folge $(a_n)$ bezeichnet.

> Die strenge Definition unter Verwendung des **Epsilon-Delta-Arguments(epsilon-delta argument)** lautet wie folgt:
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> Das bedeutet, wenn für jede noch so kleine positive Zahl $\epsilon$ immer eine natürliche Zahl $N$ existiert, so dass für alle $n>N$ gilt: $\|a_n - l \| < \epsilon$, dann wird die Differenz zwischen $a_n$ und $l$ für hinreichend große $n$ beliebig klein. Eine Folge $(a_n)$, die diese Bedingung erfüllt, wird als konvergent gegen die reelle Zahl $l$ definiert.
{: .prompt-info }

Eine Folge, die nicht konvergiert, wird als **divergent** bezeichnet. *Die Konvergenz oder Divergenz einer Folge ändert sich nicht, wenn eine endliche Anzahl ihrer Glieder geändert wird.*

Wenn die Glieder einer Folge $(a_n)$ unbegrenzt größer werden, schreibt man:

$$ \lim_{n\to \infty} a_n = \infty $$

und sagt, die Folge *divergiert gegen positiv unendlich*. Analog dazu, wenn die Glieder einer Folge $(a_n)$ unbegrenzt kleiner werden, schreibt man:

$$ \lim_{n\to \infty} a_n = -\infty $$

und sagt, die Folge *divergiert gegen negativ unendlich*.

## Grundlegende Eigenschaften konvergenter Folgen
Wenn die Folgen $(a_n)$ und $(b_n)$ beide konvergieren (d.h. Grenzwerte haben), dann konvergieren auch die Folgen $(a_n + b_n)$ und $(a_n \cdot b_n)$, und es gilt:

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Außerdem gilt für jede reelle Zahl $t$:

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Diese Eigenschaften werden als **grundlegende Eigenschaften konvergenter Folgen** oder **grundlegende Eigenschaften von Grenzwerten** bezeichnet.

## Eulersche Zahl
Die **Eulersche Zahl** wird definiert als:

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Sie gilt als eine der wichtigsten Konstanten in der Mathematik.

## Reihen
Für eine Folge

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

bezeichnet man die Folge ihrer Partialsummen

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

als **Reihe** der Folge $\mathbf{a}$. Die Reihe einer Folge $(a_n)$ wird dargestellt als:

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

## Konvergenz und Divergenz von Reihen
Wenn die aus der Folge $(a_n)$ gebildete Reihe

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

gegen eine reelle Zahl $l$ konvergiert, schreibt man:

$$ \sum_{n=1}^{\infty} a_n = l $$

Der Grenzwert $l$ wird als **Summe** der Reihe $\sum a_n$ bezeichnet. Das Symbol

$$ \sum a_n $$

kann je nach Kontext entweder die <u>Reihe</u> selbst oder ihre <u>Summe</u> bezeichnen.

Eine Reihe, die nicht konvergiert, wird als **divergent** bezeichnet.

## Grundlegende Eigenschaften konvergenter Reihen
Aus den [grundlegenden Eigenschaften konvergenter Folgen](#grundlegende-eigenschaften-konvergenter-folgen) ergeben sich die folgenden grundlegenden Eigenschaften konvergenter Reihen. Für eine reelle Zahl $t$ und zwei konvergente Reihen $\sum a_n$, $\sum b_n$ gilt:

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n $$

Die Konvergenz einer Reihe wird durch die Änderung einer endlichen Anzahl von Gliedern nicht beeinflusst. Das heißt, wenn für zwei Folgen $(a_n)$ und $(b_n)$ gilt, dass $a_n=b_n$ für alle $n$ außer einer endlichen Anzahl, dann konvergiert die Reihe $\sum a_n$ genau dann, wenn die Reihe $\sum b_n$ konvergiert.
