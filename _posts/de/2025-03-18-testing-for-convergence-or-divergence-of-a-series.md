---
title: Konvergenz-/Divergenztest für Reihen (Testing for Convergence or Divergence of a Series)
description: Wir betrachten verschiedene Methoden zur Bestimmung der Konvergenz/Divergenz von Reihen.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **n-ter Gliedtest für Divergenz**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{Reihe }\sum a_n \text{ divergiert}$
> - **Konvergenz/Divergenz geometrischer Reihen**: Geometrische Reihe $\sum ar^{n-1}$
>   - konvergiert, wenn $\|r\| < 1$
>   - divergiert, wenn $\|r\| \geq 1$
> - **Konvergenz/Divergenz von p-Reihen**: p-Reihe $\sum \cfrac{1}{n^p}$
>   - konvergiert, wenn $p>1$
>   - divergiert, wenn $p\leq 1$
> - **Vergleichstest**: Wenn $0 \leq a_n \leq b_n$, dann  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Grenzwertvergleichstest**: Wenn $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ ist eine endliche positive Zahl)}$, dann konvergieren oder divergieren beide Reihen $\sum a_n$ und $\sum b_n$
> - Für eine Reihe positiver Terme $\sum a_n$ und eine positive Zahl $\epsilon < 1$  
>   - Wenn $\sqrt[n]{a_n}< 1-\epsilon$ für alle $n$, dann konvergiert die Reihe $\sum a_n$
>   - Wenn $\sqrt[n]{a_n}> 1+\epsilon$ für alle $n$, dann divergiert die Reihe $\sum a_n$
> - **Wurzeltest**: Für eine Reihe positiver Terme $\sum a_n$, wenn der Grenzwert $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ existiert,
>   - konvergiert die Reihe $\sum a_n$, wenn $r<1$
>   - divergiert die Reihe $\sum a_n$, wenn $r>1$
> - **Quotientenkriterium**: Für eine Folge positiver Zahlen $(a_n)$ und $0 < r < 1$
>   - Wenn $a_{n+1}/a_n \leq r$ für alle $n$, dann konvergiert die Reihe $\sum a_n$
>   - Wenn $a_{n+1}/a_n \geq 1$ für alle $n$, dann divergiert die Reihe $\sum a_n$
> - Für eine Folge positiver Zahlen $(a_n)$, wenn der Grenzwert $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existiert,
>   - konvergiert die Reihe $\sum a_n$, wenn $\rho < 1$
>   - divergiert die Reihe $\sum a_n$, wenn $\rho > 1$
> - **Integraltest**: Für eine stetige, abnehmende Funktion $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ mit $f(x)>0$ für alle $x$, konvergiert die Reihe $\sum f(n)$ genau dann, wenn das Integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ konvergiert
> - **Leibniz-Kriterium für alternierende Reihen**: Eine alternierende Reihe $\sum a_n$ konvergiert, wenn
>   1. $a_n$ und $a_{n+1}$ haben für alle $n$ unterschiedliche Vorzeichen
>   2. $\|a_n\| \geq \|a_{n+1}\|$ für alle $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Absolut konvergente Reihen konvergieren. Die Umkehrung gilt nicht.
{: .prompt-info }

## Voraussetzungen
- [Folgen und Reihen](/posts/sequences-and-series/)

## Einleitung
In [Folgen und Reihen](/posts/sequences-and-series/#konvergenz-und-divergenz-von-reihen) haben wir die Definition der Konvergenz und Divergenz von Reihen kennengelernt. In diesem Beitrag fassen wir verschiedene Methoden zusammen, die zur Bestimmung der Konvergenz/Divergenz von Reihen verwendet werden können. Im Allgemeinen ist es viel einfacher, die Konvergenz/Divergenz einer Reihe zu bestimmen, als ihre exakte Summe zu berechnen.

## n-ter Gliedtest
Für eine Reihe $\sum a_n$ wird $a_n$ als das **allgemeine Glied** dieser Reihe bezeichnet.

Der folgende Satz ermöglicht es uns, die offensichtliche Divergenz einiger Reihen leicht zu erkennen. Daher ist es klug, dies zuerst zu überprüfen, wenn man die Konvergenz/Divergenz einer Reihe bestimmt, um Zeitverschwendung zu vermeiden.

> **n-ter Gliedtest für Divergenz**  
> Wenn eine Reihe $\sum a_n$ konvergiert, dann gilt
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Mit anderen Worten:
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{Reihe }\sum a_n \text{ divergiert} $$
{: .prompt-info }

### Beweis
Sei $l$ die Summe einer konvergierenden Reihe $\sum a_n$ und $s_n$ die Summe der ersten $n$ Glieder:

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Dann gilt:

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Folglich gilt für hinreichend große $n$ (> N):

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Aus der Definition der Konvergenz einer Folge folgt:

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Vorsicht
Die Umkehrung dieses Satzes ist im Allgemeinen nicht wahr. Ein typisches Beispiel dafür ist die **harmonische Reihe**.

Die harmonische Reihe ist eine Reihe, deren Glieder die Kehrwerte einer **arithmetischen Folge** sind, also eine **harmonische Folge**. Die bekannteste harmonische Reihe ist:

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Man kann zeigen, dass diese Reihe divergiert:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Obwohl die Reihe $H_n$ divergiert, konvergiert das allgemeine Glied $1/n$ gegen 0.

> Wenn $\lim_{n\to\infty} a_n \neq 0$, dann divergiert die Reihe $\sum a_n$ sicher, aber es ist gefährlich anzunehmen, dass die Reihe $\sum a_n$ konvergiert, nur weil $\lim_{n\to\infty} a_n = 0$. In diesem Fall müssen andere Methoden verwendet werden, um die Konvergenz/Divergenz zu bestimmen.
{: .prompt-danger }

## Geometrische Reihe
Die **geometrische Reihe** mit erstem Glied 1 und **Quotient** $r$

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

ist die <u>wichtigste und grundlegendste Reihe</u>. Aus der Gleichung

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

erhalten wir

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Andererseits wissen wir, dass

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

Daher ist die notwendige und hinreichende Bedingung für die Konvergenz der geometrischen Reihe ($\ref{eqn:geometric_series}$) $\|r\| < 1$.

> **Konvergenz/Divergenz geometrischer Reihen**  
> Die geometrische Reihe $\sum ar^{n-1}$
> - konvergiert, wenn $\|r\| < 1$
> - divergiert, wenn $\|r\| \geq 1$
{: .prompt-info }

Daraus erhalten wir

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Geometrische Reihe und Näherungswerte
Die Identität ($\ref{eqn:sum_of_geometric_series}$) ist nützlich, um Näherungswerte für $\cfrac{1}{1-r}$ zu finden, wenn $\|r\| < 1$.

Wenn wir $r=-\epsilon$ und $n=2$ in diese Gleichung einsetzen, erhalten wir

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Daher, wenn $0 < \epsilon < 1$, gilt

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

Also erhalten wir

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Daraus können wir schließen, dass für hinreichend kleine positive $\epsilon$, $\cfrac{1}{1 + \epsilon}$ durch $1 - \epsilon$ angenähert werden kann.

## p-Reihentest (p-Series Test)  
Für eine positive reelle Zahl $p$ wird eine Reihe der folgenden Form als **p-Reihe** bezeichnet:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Konvergenz/Divergenz von p-Reihen**  
> Die p-Reihe $\sum \cfrac{1}{n^p}$
> - konvergiert, wenn $p>1$
> - divergiert, wenn $p\leq 1$
{: .prompt-info }

In einer p-Reihe wird der Fall $p=1$ zur harmonischen Reihe, von der wir bereits gezeigt haben, dass sie divergiert.  
Das Problem, den Wert der p-Reihe für $p=2$, also $\sum \cfrac{1}{n^2}$, zu finden, wird als 'Basel-Problem' bezeichnet, benannt nach dem Heimatort der Bernoulli-Familie, die über mehrere Generationen hinweg viele berühmte Mathematiker hervorbrachte und die Konvergenz dieser Reihe zuerst bewies. Es ist bekannt, dass die Antwort auf dieses Problem $\cfrac{\pi^2}{6}$ ist.

Allgemeiner wird die p-Reihe für $p>1$ als **Zeta-Funktion** bezeichnet. Diese wurde 1740 von Leonhard Euler eingeführt und später von Riemann benannt. Sie ist eine spezielle Funktion, definiert als

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Da dies etwas vom Thema dieses Beitrags abweicht und ich ehrlich gesagt als Ingenieurstudent und nicht als Mathematiker nicht viel darüber weiß, werde ich hier nicht weiter darauf eingehen. Leonhard Euler zeigte jedoch, dass die Zeta-Funktion auch als unendliches Produkt von Primzahlen, bekannt als **Euler-Produkt**, dargestellt werden kann. Seitdem nimmt die Zeta-Funktion eine zentrale Stellung in verschiedenen Bereichen der analytischen Zahlentheorie ein. Die **Riemann-Zeta-Funktion**, eine Erweiterung der Zeta-Funktion auf komplexe Zahlen, und das damit verbundene wichtige ungelöste Problem, die **Riemann-Hypothese**, sind Teil davon.

Um zum ursprünglichen Thema zurückzukehren: Für den Beweis des p-Reihentests benötigen wir den später behandelten [Vergleichstest](#vergleichstest) und den [Integraltest](#integraltest). Die Konvergenz/Divergenz von p-Reihen kann jedoch zusammen mit geometrischen Reihen nützlich im gleich folgenden [Vergleichstest](#vergleichstest) verwendet werden, weshalb sie absichtlich weiter vorne platziert wurde.

### Beweis
#### i) Für $p>1$
Das Integral

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

konvergiert, daher konvergiert nach dem [Integraltest](#integraltest) auch die Reihe $\sum \cfrac{1}{n^p}$.

#### ii) Für $p\leq 1$
In diesem Fall gilt

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Wir wissen, dass die harmonische Reihe $\sum \cfrac{1}{n}$ divergiert, daher divergiert nach dem [Vergleichstest](#vergleichstest) auch $\sum \cfrac{1}{n^p}$.

#### Schlussfolgerung
Aus i) und ii) folgt, dass die p-Reihe $\sum \cfrac{1}{n^p}$ für $p>1$ konvergiert und für $p \leq 1$ divergiert. $\blacksquare$

## Vergleichstest
Der **Vergleichstest** von Jakob Bernoulli ist nützlich, um die Konvergenz/Divergenz von **Reihen mit positiven Gliedern** zu bestimmen, deren allgemeine Glieder nicht-negative reelle Zahlen sind.

Eine Reihe mit positiven Gliedern $\sum a_n$ ist eine zunehmende Folge, daher konvergiert sie, wenn sie nicht gegen Unendlich divergiert ($\sum a_n = \infty$). Daher bedeutet der Ausdruck

$$ \sum a_n < \infty $$

für Reihen mit positiven Gliedern, dass sie <u>konvergieren</u>.

> **Vergleichstest**  
> Wenn $0 \leq a_n \leq b_n$, dann  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

Insbesondere bei Reihen mit positiven Gliedern, die ähnliche Formen wie die zuvor betrachteten geometrischen Reihen $\sum ar^{n-1}$ oder p-Reihen $\sum \cfrac{1}{n^p}$ haben, wie z.B. $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, ist es ratsam, den Vergleichstest aktiv auszuprobieren.

Viele der später diskutierten Konvergenz-/Divergenztests können aus diesem **Vergleichstest** abgeleitet werden, was seine Bedeutung unterstreicht.

### Grenzwertvergleichstest
Für Reihen mit positiven Gliedern $\sum a_n$ und $\sum b_n$, wenn das Verhältnis der allgemeinen Glieder $a_n/b_n$ so ist, dass die dominanten Terme im Zähler und Nenner sich aufheben und $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ ist eine endliche positive Zahl)}$, dann kann der folgende **Grenzwertvergleichstest** verwendet werden, wenn die Konvergenz/Divergenz der Reihe $\sum b_n$ bekannt ist.

> **Grenzwertvergleichstest**  
> Wenn
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ ist eine endliche positive Zahl)}$$
>
> dann konvergieren oder divergieren beide Reihen $\sum a_n$ und $\sum b_n$. Das heißt, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Wurzeltest
> **Satz**  
> Für eine Reihe positiver Terme $\sum a_n$ und eine positive Zahl $\epsilon < 1$  
> - Wenn $\sqrt[n]{a_n}< 1-\epsilon$ für alle $n$, dann konvergiert die Reihe $\sum a_n$
> - Wenn $\sqrt[n]{a_n}> 1+\epsilon$ für alle $n$, dann divergiert die Reihe $\sum a_n$
{: .prompt-info }

> **Korollar: Wurzeltest**  
> Für eine Reihe positiver Terme $\sum a_n$, wenn der Grenzwert
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> existiert, dann
> - konvergiert die Reihe $\sum a_n$, wenn $r<1$
> - divergiert die Reihe $\sum a_n$, wenn $r>1$
{: .prompt-info }

> Im obigen Korollar kann für den Fall $r=1$ keine Aussage über Konvergenz/Divergenz getroffen werden, und es müssen andere Methoden verwendet werden.
{: .prompt-warning }

## Quotientenkriterium
> **Quotientenkriterium**  
> Für eine Folge positiver Zahlen $(a_n)$ und $0 < r < 1$
> - Wenn $a_{n+1}/a_n \leq r$ für alle $n$, dann konvergiert die Reihe $\sum a_n$
> - Wenn $a_{n+1}/a_n \geq 1$ für alle $n$, dann divergiert die Reihe $\sum a_n$
{: .prompt-info }

> **Korollar**  
> Für eine Folge positiver Zahlen $(a_n)$, wenn der Grenzwert $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existiert, dann
> - konvergiert die Reihe $\sum a_n$, wenn $\rho < 1$
> - divergiert die Reihe $\sum a_n$, wenn $\rho > 1$
{: .prompt-info }

## Integraltest
Mit Hilfe der Integralrechnung kann die Konvergenz/Divergenz von Reihen mit abnehmenden positiven Folgen bestimmt werden.

> **Integraltest**  
> Sei $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ eine stetige, abnehmende Funktion mit $f(x)>0$ für alle $x$. Die Reihe $\sum f(n)$ konvergiert genau dann, wenn das Integral
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> konvergiert.
{: .prompt-info }

### Beweis
Da die Funktion $f(x)$ stetig, abnehmend und immer positiv ist, gilt die Ungleichung

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

Wenn wir diese Ungleichung von $n=1$ bis zum allgemeinen Glied Seite für Seite addieren, erhalten wir die Ungleichung

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Nun erhalten wir das gewünschte Ergebnis durch Anwendung des [Vergleichstests](#vergleichstest). $\blacksquare$

## Alternierende Reihen
Eine Reihe $\sum a_n$, bei der jedes Glied $a_n$ ein Vorzeichen hat, das sich vom Vorzeichen des nächsten Gliedes $a_{n+1}$ unterscheidet, d.h. positive und negative Glieder abwechselnd auftreten, wird als **alternierende Reihe** bezeichnet.

Für alternierende Reihen kann der folgende Satz, der vom deutschen Mathematiker Gottfried Wilhelm Leibniz entdeckt wurde, nützlich zur Bestimmung der Konvergenz/Divergenz sein.

> **Leibniz-Kriterium für alternierende Reihen**  
> Eine alternierende Reihe $\sum a_n$ konvergiert, wenn
> 1. $a_n$ und $a_{n+1}$ haben für alle $n$ unterschiedliche Vorzeichen,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ für alle $n$, und
> 3. $\lim_{n\to\infty} a_n = 0$
{: .prompt-info }

## Absolut konvergente Reihen
Eine Reihe $\sum a_n$ wird als **absolut konvergent** bezeichnet, wenn die Reihe $\sum \|a_n\|$ konvergiert.

In diesem Fall gilt der folgende Satz:

> **Satz**  
> Absolut konvergente Reihen konvergieren.
{: .prompt-info }

> Die Umkehrung des obigen Satzes gilt nicht.  
> Wenn eine Reihe konvergiert, aber nicht absolut konvergiert, sagt man, sie **konvergiert bedingt**.
{: .prompt-warning }

### Beweis
Für eine reelle Zahl $a$ definieren wir

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Dann erhalten wir

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Da $0 \leq a^\pm \leq \|a\|$, konvergieren nach dem [Vergleichstest](#vergleichstest) auch die Reihen $\sum a_n^+$ und $\sum a_n^-$, wenn die Reihe $\sum \|a_n\|$ konvergiert. Daher konvergiert nach den [grundlegenden Eigenschaften konvergenter Reihen](/posts/sequences-and-series/#grundlegende-eigenschaften-konvergenter-reihen) auch

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

$\blacksquare$
