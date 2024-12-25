---
title: Ehrenfest-Theorem
description: Wir untersuchen, wie man in der Quantenmechanik Erwartungswerte für Position
  und Impuls aus der Wellenfunktion berechnet, und erweitern dies auf eine Formel
  für den Erwartungswert einer beliebigen mechanischen Variable Q(x,p). Daraus leiten
  wir dann das Ehrenfest-Theorem ab.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Voraussetzungen
- Kontinuierliche Wahrscheinlichkeitsverteilung und Wahrscheinlichkeitsdichte
- [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/)

## Berechnung von Erwartungswerten aus der Wellenfunktion
### Erwartungswert der Position $x$
Der Erwartungswert der Position $x$ für ein Teilchen im Zustand $\Psi$ ist

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

Wenn man die Position einer ausreichend großen Anzahl von Teilchen im gleichen Zustand $\Psi$ misst und den Durchschnitt der Messergebnisse bildet, erhält man $\langle x \rangle$, berechnet durch die obige Gleichung.

> Es ist zu beachten, dass der hier erwähnte Erwartungswert nicht der Durchschnitt wiederholter Messungen an einem einzelnen Teilchen ist, sondern der Durchschnitt der Messergebnisse für ein **Ensemble** von Systemen im gleichen Zustand. Wenn man dasselbe Teilchen in kurzen Zeitabständen mehrmals misst, würde der [Kollaps der Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/#messung-und-kollaps-der-wellenfunktion) bei der ersten Messung dazu führen, dass bei allen folgenden Messungen immer der gleiche Wert erhalten wird.
{: .prompt-warning }

### Erwartungswert des Impulses $p$
Da $\Psi$ zeitabhängig ist, wird sich $\langle x \rangle$ mit der Zeit ändern. Gemäß Gleichung (8) aus [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/) und der obigen Gleichung ($\ref{eqn:x_exp}$) gilt:

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> In den Schritten von Gleichung ($\ref{eqn:dx/dt_1}$) zu ($\ref{eqn:dx/dt_2}$) und von ($\ref{eqn:dx/dt_2}$) zu ($\ref{eqn:dx/dt_3}$) wurde zweimal partielle Integration angewendet, und da $\lim_{x\rightarrow\pm\infty}\Psi=0$, wurden die Randterme vernachlässigt.
{: .prompt-tip }

Daraus ergibt sich der Erwartungswert des **Impulses** wie folgt:

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Erwartungswert für eine beliebige physikalische Größe $Q(x,p)$
Die zuvor berechneten Ausdrücke für $\langle x \rangle$ und $\langle p \rangle$ können wie folgt geschrieben werden:

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

Der Operator $\hat x \equiv x$ repräsentiert die Position, und der Operator $\hat p \equiv -i\hbar(\partial/\partial x)$ repräsentiert den Impuls. Für den Impulsoperator $\hat p$ kann man in drei Dimensionen $\hat p \equiv -i\hbar\nabla$ definieren.

Da alle klassischen mechanischen Variablen durch Position und Impuls ausgedrückt werden können, kann dies auf den Erwartungswert einer beliebigen physikalischen Größe erweitert werden. Um den Erwartungswert einer beliebigen Größe $Q(x,p)$ zu berechnen, ersetzt man alle $p$ durch $-i\hbar\nabla$ und integriert den so erhaltenen Operator zwischen $\Psi^\*$ und $\Psi$.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Zum Beispiel, für die kinetische Energie $T=\cfrac{p^2}{2m}$ gilt:

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

Mit Gleichung ($\ref{eqn:Q_exp}$) kann man den Erwartungswert einer beliebigen physikalischen Größe für ein Teilchen im Zustand $\Psi$ berechnen.

## Ehrenfest-Theorem
### Berechnung von $d\langle p \rangle/dt$
Differenzieren wir beide Seiten von Gleichung ($\ref{eqn:p_op}$) nach der Zeit $t$, um die zeitliche Ableitung des Impulserwartungswerts $\cfrac{d\langle p \rangle}{dt}$ zu erhalten.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Gleichung ($\ref{eqn:dp/dt_2}$) erhält man durch Einsetzen der Gleichungen (6) und (7) aus [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/) in Gleichung ($\ref{eqn:dp/dt_1}$). Im Schritt von Gleichung ($\ref{eqn:dp/dt_3}$) zu ($\ref{eqn:dp/dt_4}$) wurde partielle Integration angewendet, und wie zuvor wurden die Randterme aufgrund von $\lim_{x\rightarrow\pm\infty}\Psi=0$ vernachlässigt.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Beziehung zwischen dem Ehrenfest-Theorem und Newtons zweitem Bewegungsgesetz
Die folgenden beiden Gleichungen, die wir zuvor abgeleitet haben, werden als Ehrenfest-Theorem bezeichnet:

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

Das Ehrenfest-Theorem hat eine sehr ähnliche Form wie die Beziehung zwischen potentieller Energie und konservativer Kraft in der klassischen Mechanik, $F=\cfrac{dp}{dt}=-\nabla V$.  
Wenn wir die beiden Gleichungen nebeneinander stellen, sehen wir:

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest-Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newtons zweites Bewegungsgesetz]}$$

Wenn wir die rechte Seite der zweiten Gleichung des Ehrenfest-Theorems $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (Gleichung [$\ref{eqn:ehrenfest_theorem_2nd}$]) in der Nähe von $\langle x \rangle$ nach $x$ in eine Taylor-Reihe entwickeln, erhalten wir:

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

Wenn $x-\langle x \rangle$ klein genug ist, können wir alle Terme höherer Ordnung außer dem ersten vernachlässigen und erhalten die Näherung:

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

Das bedeutet, **wenn die Wellenfunktion eines Teilchens räumlich sehr eng um einen Punkt verteilt ist (d.h. wenn die Streuung von $\|\Psi\|^2$ in Bezug auf $x$ sehr klein ist), kann das Ehrenfest-Theorem durch Newtons zweites Bewegungsgesetz der klassischen Mechanik angenähert werden.** Auf makroskopischer Ebene können wir die räumliche Ausbreitung der Wellenfunktion vernachlässigen und die Position des Teilchens praktisch als einen Punkt betrachten, sodass Newtons zweites Bewegungsgesetz gilt. Auf mikroskopischer Ebene können quantenmechanische Effekte jedoch nicht vernachlässigt werden, sodass Newtons zweites Bewegungsgesetz nicht mehr gilt und stattdessen das Ehrenfest-Theorem verwendet werden muss.
