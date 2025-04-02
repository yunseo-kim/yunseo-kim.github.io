---
title: Konvergenz/Divergenz-Tests für Reihen (Testing for Convergence or Divergence of a Series)
description: Eine umfassende Betrachtung verschiedener Methoden zur Bestimmung der Konvergenz oder Divergenz von Reihen.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **n-ter Glied-Test für Divergenz**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{Die Reihe }\sum a_n \text{ divergiert}$
> - **Konvergenz/Divergenz geometrischer Reihen**: Die geometrische Reihe $\sum ar^{n-1}$ 
>   - konvergiert, wenn $\|r\| < 1$
>   - divergiert, wenn $\|r\| \geq 1$
> - **Konvergenz/Divergenz von $p$-Reihen**: Die $p$-Reihe $\sum \cfrac{1}{n^p}$
>   - konvergiert, wenn $p>1$
>   - divergiert, wenn $p\leq 1$
> - **Vergleichstest**: Wenn $0 \leq a_n \leq b_n$, dann gilt:  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Grenzwert-Vergleichstest**: Wenn $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ ist eine endliche positive Zahl)}$, dann konvergieren oder divergieren beide Reihen $\sum a_n$ und $\sum b_n$ gemeinsam
> - Für eine Reihe positiver Terme $\sum a_n$ und eine positive Zahl $\epsilon < 1$ gilt:  
>   - Wenn für alle $n$ gilt: $\sqrt[n]{a_n}< 1-\epsilon$, dann konvergiert die Reihe $\sum a_n$
>   - Wenn für alle $n$ gilt: $\sqrt[n]{a_n}> 1+\epsilon$, dann divergiert die Reihe $\sum a_n$
> - **Wurzelkriterium**: Für eine Reihe positiver Terme $\sum a_n$, bei der der Grenzwert $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ existiert, gilt:
>   - Wenn $r<1$, dann konvergiert die Reihe $\sum a_n$
>   - Wenn $r>1$, dann divergiert die Reihe $\sum a_n$
> - **Quotientenkriterium**: Für eine Folge positiver Zahlen $(a_n)$ und $0 < r < 1$ gilt:
>   - Wenn für alle $n$ gilt: $a_{n+1}/a_n \leq r$, dann konvergiert die Reihe $\sum a_n$
>   - Wenn für alle $n$ gilt: $a_{n+1}/a_n \geq 1$, dann divergiert die Reihe $\sum a_n$
> - Für eine Folge positiver Zahlen $(a_n)$, bei der der Grenzwert $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existiert, gilt:
>   - Wenn $\rho < 1$, dann konvergiert die Reihe $\sum a_n$
>   - Wenn $\rho > 1$, dann divergiert die Reihe $\sum a_n$
> - **Integraltest**: Sei $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ eine stetige, monoton fallende Funktion mit $f(x)>0$ für alle $x$. Die Reihe $\sum f(n)$ konvergiert genau dann, wenn das Integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ konvergiert
> - **Leibniz-Kriterium für alternierende Reihen**: Eine alternierende Reihe $\sum a_n$ konvergiert, wenn:
>   1. Die Vorzeichen von $a_n$ und $a_{n+1}$ für alle $n$ verschieden sind
>   2. Für alle $n$ gilt: $\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Absolut konvergente Reihen konvergieren. Die Umkehrung gilt nicht.
{: .prompt-info }

## Voraussetzungen
- [Folgen und Reihen](/posts/sequences-and-series/)

## Einleitung
In [Folgen und Reihen](/posts/sequences-and-series/#konvergenz-und-divergenz-von-reihen) haben wir die Definition der Konvergenz und Divergenz von Reihen kennengelernt. In diesem Beitrag fassen wir verschiedene Methoden zusammen, mit denen die Konvergenz oder Divergenz von Reihen bestimmt werden kann. Im Allgemeinen ist es wesentlich einfacher, die Konvergenz oder Divergenz einer Reihe zu bestimmen, als ihre exakte Summe zu berechnen.

## n-ter Glied-Test
Bei einer Reihe $\sum a_n$ bezeichnet man $a_n$ als das **allgemeine Glied** der Reihe.

Der folgende Satz ermöglicht es uns, die Divergenz bestimmter Reihen leicht zu erkennen. Daher ist es sinnvoll, diesen Test als Erstes anzuwenden, um Zeit zu sparen.

> **n-ter Glied-Test für Divergenz**  
> Wenn eine Reihe $\sum a_n$ konvergiert, dann gilt:
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Das bedeutet:
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{Die Reihe }\sum a_n \text{ divergiert} $$
{: .prompt-info }

### Beweis
Sei $l$ die Summe einer konvergenten Reihe $\sum a_n$ und sei

$$ s_n := a_1 + a_2 + \cdots + a_n $$

die Summe der ersten $n$ Glieder. Dann gilt:

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Für hinreichend große $n > N$ gilt daher:

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Aus der Definition der Konvergenz einer Folge folgt:

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Wichtiger Hinweis
Die Umkehrung dieses Satzes gilt im Allgemeinen nicht. Ein klassisches Beispiel dafür ist die **harmonische Reihe**.

Die harmonische Reihe ist eine Reihe, deren Glieder die Kehrwerte einer **arithmetischen Folge** sind, also eine **harmonische Folge**. Die bekannteste harmonische Reihe ist:

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Diese Reihe divergiert, wie man folgendermaßen zeigen kann:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Obwohl die Reihe $H_n$ divergiert, konvergiert das allgemeine Glied $1/n$ gegen $0$.

> Wenn $\lim_{n\to\infty} a_n \neq 0$, dann divergiert die Reihe $\sum a_n$ definitiv. Aber wenn $\lim_{n\to\infty} a_n = 0$, bedeutet das nicht automatisch, dass die Reihe $\sum a_n$ konvergiert. In diesem Fall müssen andere Methoden zur Bestimmung der Konvergenz oder Divergenz angewendet werden.
{: .prompt-danger }

## Geometrische Reihen
Die **geometrische Reihe** mit erstem Glied 1 und **Quotient** $r$

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

ist eine der <u>wichtigsten und grundlegendsten Reihen</u>. Aus der Gleichung

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

erhalten wir

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Da

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

wissen wir, dass die geometrische Reihe ($\ref{eqn:geometric_series}$) genau dann konvergiert, wenn $\|r\| < 1$ ist.

> **Konvergenz/Divergenz geometrischer Reihen**  
> Die geometrische Reihe $\sum ar^{n-1}$
> - konvergiert, wenn $\|r\| < 1$
> - divergiert, wenn $\|r\| \geq 1$
{: .prompt-info }

Daraus folgt:

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Geometrische Reihen und Näherungswerte
Die Identität ($\ref{eqn:sum_of_geometric_series}$) ist nützlich, um Näherungswerte für $\cfrac{1}{1-r}$ zu finden, wenn $\|r\| < 1$.

Wenn wir $r=-\epsilon$ und $n=2$ einsetzen, erhalten wir:

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Für $0 < \epsilon < 1$ gilt daher:

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

Somit:

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Daraus folgt, dass für hinreichend kleine positive $\epsilon$ der Wert $\cfrac{1}{1 + \epsilon}$ durch $1 - \epsilon$ angenähert werden kann.

## p-Reihen-Test
Für eine positive reelle Zahl $p$ bezeichnet man eine Reihe der folgenden Form als **$p$-Reihe**:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Konvergenz/Divergenz von $p$-Reihen**  
> Die $p$-Reihe $\sum \cfrac{1}{n^p}$
> - konvergiert, wenn $p>1$
> - divergiert, wenn $p\leq 1$
{: .prompt-info }

Für $p=1$ erhalten wir die harmonische Reihe, die, wie bereits gezeigt, divergiert.  
Die Berechnung des Wertes der $p$-Reihe für $p=2$, also $\sum \cfrac{1}{n^2}$, ist als "Baseler Problem" bekannt, benannt nach dem Heimatort der Bernoulli-Familie, die mehrere berühmte Mathematiker über Generationen hinweg hervorbrachte. Die Lösung dieses Problems ist bekannt als $\cfrac{\pi^2}{6}$.

Allgemeiner werden $p$-Reihen mit $p>1$ als **Zeta-Funktion** bezeichnet. Diese wurde von Leonhard Euler im Jahr 11740 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) eingeführt und später von Riemann benannt. Sie ist definiert als:

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Dies geht über das Thema dieses Beitrags hinaus, und da ich Ingenieur und kein Mathematiker bin, werde ich nicht näher darauf eingehen. Leonhard Euler zeigte jedoch, dass die Zeta-Funktion auch als unendliches Produkt über Primzahlen, bekannt als **Euler-Produkt**, dargestellt werden kann. Die Zeta-Funktion spielt eine zentrale Rolle in verschiedenen Bereichen der analytischen Zahlentheorie. Die auf komplexe Zahlen erweiterte **Riemann-Zeta-Funktion** und die damit verbundene ungelöste **Riemann-Hypothese** sind bedeutende Themen in diesem Bereich.

Zurück zum Thema: Der Beweis des $p$-Reihen-Tests erfordert den [Vergleichstest](#vergleichstest) und den [Integraltest](#integraltest), die später behandelt werden. Da die Konvergenz/Divergenz von $p$-Reihen jedoch zusammen mit geometrischen Reihen im [Vergleichstest](#vergleichstest) nützlich sein kann, habe ich diesen Abschnitt bewusst vorangestellt.

### Beweis
#### i) Für $p>1$
Das Integral

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

konvergiert. Nach dem [Integraltest](#integraltest) konvergiert daher auch die Reihe $\sum \cfrac{1}{n^p}$.

#### ii) Für $p\leq 1$
In diesem Fall gilt:

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Da die harmonische Reihe $\sum \cfrac{1}{n}$ divergiert, divergiert nach dem [Vergleichstest](#vergleichstest) auch $\sum \cfrac{1}{n^p}$.

#### Fazit
Aus i) und ii) folgt, dass die $p$-Reihe $\sum \cfrac{1}{n^p}$ konvergiert, wenn $p>1$, und divergiert, wenn $p \leq 1$. $\blacksquare$

## Vergleichstest
Der **Vergleichstest** von Jakob Bernoulli ist nützlich zur Bestimmung der Konvergenz oder Divergenz von **Reihen mit positiven Gliedern**.

Eine Reihe mit positiven Gliedern $\sum a_n$ bildet eine monoton wachsende Folge. Wenn sie nicht gegen unendlich divergiert ($\sum a_n = \infty$), muss sie konvergieren. Daher bedeutet der Ausdruck

$$ \sum a_n < \infty $$

für Reihen mit positiven Gliedern, dass die Reihe <u>konvergiert</u>.

> **Vergleichstest**  
> Wenn $0 \leq a_n \leq b_n$, dann gilt:  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

Besonders bei Reihen mit positiven Gliedern, die ähnliche Formen wie geometrische Reihen $\sum ar^{n-1}$ oder $p$-Reihen $\sum \cfrac{1}{n^p}$ haben, wie z.B. $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$ oder $\sum \sin{\cfrac{1}{n}}$, ist es ratsam, den Vergleichstest anzuwenden.

Viele der später behandelten Konvergenz- und Divergenztests können aus diesem **Vergleichstest** abgeleitet werden, was seine grundlegende Bedeutung unterstreicht.

### Grenzwert-Vergleichstest
Für zwei Reihen mit positiven Gliedern $\sum a_n$ und $\sum b_n$, bei denen das Verhältnis der allgemeinen Glieder $a_n/b_n$ gegen einen endlichen positiven Wert $c$ konvergiert, kann der **Grenzwert-Vergleichstest** angewendet werden, wenn die Konvergenz oder Divergenz von $\sum b_n$ bekannt ist.

> **Grenzwert-Vergleichstest**  
> Wenn
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ ist eine endliche positive Zahl)}$$
>
> dann konvergieren oder divergieren beide Reihen $\sum a_n$ und $\sum b_n$ gemeinsam. Das heißt, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Wurzelkriterium
> **Satz**  
> Für eine Reihe positiver Terme $\sum a_n$ und eine positive Zahl $\epsilon < 1$ gilt:  
> - Wenn für alle $n$ gilt: $\sqrt[n]{a_n}< 1-\epsilon$, dann konvergiert die Reihe $\sum a_n$
> - Wenn für alle $n$ gilt: $\sqrt[n]{a_n}> 1+\epsilon$, dann divergiert die Reihe $\sum a_n$
{: .prompt-info }

> **Folgerung: Wurzelkriterium**  
> Für eine Reihe positiver Terme $\sum a_n$, bei der der Grenzwert
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> existiert, gilt:
> - Wenn $r<1$, dann konvergiert die Reihe $\sum a_n$
> - Wenn $r>1$, dann divergiert die Reihe $\sum a_n$
{: .prompt-info }

> Im Fall $r=1$ kann das Wurzelkriterium keine Aussage über Konvergenz oder Divergenz treffen, und andere Methoden müssen angewendet werden.
{: .prompt-warning }

## Quotientenkriterium
> **Quotientenkriterium**  
> Für eine Folge positiver Zahlen $(a_n)$ und $0 < r < 1$ gilt:
> - Wenn für alle $n$ gilt: $a_{n+1}/a_n \leq r$, dann konvergiert die Reihe $\sum a_n$
> - Wenn für alle $n$ gilt: $a_{n+1}/a_n \geq 1$, dann divergiert die Reihe $\sum a_n$
{: .prompt-info }

> **Folgerung**  
> Für eine Folge positiver Zahlen $(a_n)$, bei der der Grenzwert $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existiert, gilt:
> - Wenn $\rho < 1$, dann konvergiert die Reihe $\sum a_n$
> - Wenn $\rho > 1$, dann divergiert die Reihe $\sum a_n$
{: .prompt-info }

## Integraltest
Mit Hilfe der Integralrechnung kann die Konvergenz oder Divergenz von Reihen mit monoton fallenden positiven Gliedern bestimmt werden.

> **Integraltest**  
> Sei $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ eine stetige, monoton fallende Funktion mit $f(x)>0$ für alle $x$. Die Reihe $\sum f(n)$ konvergiert genau dann, wenn das Integral
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> konvergiert.
{: .prompt-info }

### Beweis
Da die Funktion $f(x)$ stetig, monoton fallend und stets positiv ist, gilt die Ungleichung:

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

Durch Summation dieser Ungleichung von $n=1$ bis zum allgemeinen Glied erhalten wir:

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Mit dem [Vergleichstest](#vergleichstest) erhalten wir das gewünschte Ergebnis. $\blacksquare$

## Alternierende Reihen
Eine Reihe $\sum a_n$, bei der die Vorzeichen der aufeinanderfolgenden Glieder $a_n$ und $a_{n+1}$ verschieden sind, also positive und negative Glieder abwechselnd auftreten, nennt man **alternierende Reihe**.

Für alternierende Reihen kann der folgende Satz, der vom deutschen Mathematiker Gottfried Wilhelm Leibniz entdeckt wurde, zur Bestimmung der Konvergenz nützlich sein.

> **Leibniz-Kriterium für alternierende Reihen**  
> Eine alternierende Reihe $\sum a_n$ konvergiert, wenn:
> 1. Die Vorzeichen von $a_n$ und $a_{n+1}$ für alle $n$ verschieden sind,
> 2. Für alle $n$ gilt: $\|a_n\| \geq \|a_{n+1}\|$, und
> 3. $\lim_{n\to\infty} a_n = 0$.
{: .prompt-info }

## Absolute Konvergenz
Eine Reihe $\sum a_n$ **konvergiert absolut**, wenn die Reihe $\sum \|a_n\|$ konvergiert.

Es gilt der folgende Satz:

> **Satz**  
> Jede absolut konvergente Reihe konvergiert.
{: .prompt-info }

> Die Umkehrung dieses Satzes gilt nicht.  
> Eine Reihe, die konvergiert, aber nicht absolut konvergiert, nennt man **bedingt konvergent**.
{: .prompt-warning }

### Beweis
Für eine reelle Zahl $a$ definieren wir:

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Dann gilt:

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Da $0 \leq a^\pm \leq \|a\|$, folgt aus dem [Vergleichstest](#vergleichstest), dass wenn die Reihe $\sum \|a_n\|$ konvergiert, auch die Reihen $\sum a_n^+$ und $\sum a_n^-$ konvergieren. Nach den [grundlegenden Eigenschaften konvergenter Reihen](/posts/sequences-and-series/#grundlegende-eigenschaften-konvergenter-reihen) konvergiert dann auch:

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

$\blacksquare$
