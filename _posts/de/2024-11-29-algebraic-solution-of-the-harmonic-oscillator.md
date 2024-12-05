---
title: "Algebraische Lösung des harmonischen Oszillators"
description: >-
  Wir stellen die Schrödinger-Gleichung für den harmonischen Oszillator in der Quantenmechanik auf und untersuchen ihre algebraische Lösungsmethode.
  Aus Kommutatoren, kanonischen Vertauschungsrelationen und Leiteroperatoren leiten wir die Wellenfunktion und Energieniveaus für beliebige stationäre Zustände ab.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder Operators]
math: true
---

## TL;DR
> - Jede Schwingung kann für kleine Amplituden als einfache harmonische Schwingung angenähert werden, was die große Bedeutung des harmonischen Oszillators in der Physik erklärt
> - Harmonischer Oszillator: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Kommutator**:
>   - Binäre Operation, die angibt, wie schlecht zwei Operatoren kommutieren
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Kanonische Vertauschungsrelation**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Leiteroperatoren**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ wird als **Erzeugungsoperator**, $\hat{a}\_-$ als **Vernichtungsoperator** bezeichnet
>   - Können für beliebige stationäre Zustände die Energieniveaus erhöhen oder senken, sodass alle Lösungen der zeitunabhängigen Schrödinger-Gleichung gefunden werden können, wenn eine Lösung bekannt ist
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Wellenfunktion und Energieniveau des $n$-ten stationären Zustands:
>   - Grundzustand ($0$-ter stationärer Zustand):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-ter stationärer Zustand:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ ist der **hermitesche Adjungierte** und **adjungierte Operator** von $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - Daraus lassen sich folgende Eigenschaften ableiten:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Methode zur Berechnung von Erwartungswerten physikalischer Größen, die Potenzen von $\hat{x}$ und $\hat{p}$ enthalten:
>   1. Ausdrücken von $\hat{x}$ und $\hat{p}$ durch Erzeugungs- und Vernichtungsoperatoren unter Verwendung der Definition der Leiteroperatoren
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Darstellung der physikalischen Größe, deren Erwartungswert berechnet werden soll, mit Hilfe der obigen Ausdrücke für $\hat{x}$ und $\hat{p}$
>   3. Ausnutzen der Tatsache, dass $\left(\hat{a}\_\pm \right)^m$ proportional zu $\psi\_{n\pm m}$ ist und daher orthogonal zu $\psi_n$, was zu Null führt
>   4. Berechnung des Integrals unter Verwendung der Eigenschaften der Leiteroperatoren
{: .prompt-info }

## Voraussetzungen
- [Methode der Trennung der Variablen](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest-Theorem](/posts/ehrenfest-theorem/)
- [Zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/)
- [Der eindimensionale unendliche Potentialtopf](/posts/the-infinite-square-well/)
- Hermitesch Adjungierter, adjungierter Operator

## Modellaufbau
### Der harmonische Oszillator in der klassischen Mechanik
Ein typisches Beispiel für einen klassischen harmonischen Oszillator ist eine Masse $m$, die an einer Feder mit der Federkonstante $k$ hängt (Reibung wird vernachlässigt).
Diese Bewegung folgt dem **Hookeschen Gesetz**:

$$ F = -kx = m\frac{d^2x}{dt^2} $$

Die Lösung dieser Gleichung lautet:

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

wobei

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

die Kreisfrequenz der Schwingung ist. Die potentielle Energie als Funktion der Position $x$ hat die Form einer Parabel:

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

In der Realität existiert kein perfekter harmonischer Oszillator. Selbst im Fall der hier als Beispiel genannten Feder wird diese reißen oder eine permanente Verformung erleiden, wenn man sie zu stark dehnt, und tatsächlich folgt sie schon vor diesem Punkt nicht mehr exakt dem Hookeschen Gesetz. Trotzdem ist der harmonische Oszillator in der Physik von großer Bedeutung, weil jedes beliebige Potential in der Nähe eines lokalen Minimums durch eine Parabel angenähert werden kann. Wenn wir ein beliebiges Potential $V(x)$ in der Nähe eines Minimums in eine Taylor-Reihe entwickeln, erhalten wir:

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Da das Hinzufügen einer Konstante zu $V(x)$ keinen Einfluss auf die Kraft hat, können wir hier $V(x_0)$ subtrahieren. Außerdem ist $V^\prime(x_0)=0$, da $x_0$ ein Minimum ist. Unter der Annahme, dass $(x-x_0)$ klein genug ist, können wir die höheren Terme vernachlässigen und erhalten:

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

Dies entspricht in der Nähe des Punktes $x_0$ der Bewegung eines harmonischen Oszillators mit einer effektiven Federkonstante $k=V^{\prime\prime}(x_0)$. Mit anderen Worten: Jede Schwingung kann für hinreichend kleine Amplituden als einfache harmonische Schwingung angenähert werden.

> \* Da wir angenommen haben, dass $V(x)$ bei $x_0$ ein Minimum hat, gilt hier $V^{\prime\prime}(x_0) \geq 0$. In sehr seltenen Fällen kann $V^{\prime\prime}(x_0)=0$ sein, und solche Bewegungen können nicht als einfache harmonische Schwingungen angenähert werden.
{: .prompt-info }

### Der harmonische Oszillator in der Quantenmechanik
Das quantenmechanische Problem des harmonischen Oszillators besteht darin, die Schrödinger-Gleichung für das Potential

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

zu lösen. Die [zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/) für den harmonischen Oszillator lautet:

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

Es gibt zwei völlig unterschiedliche Ansätze zur Lösung dieses Problems. Der eine ist eine analytische Methode unter Verwendung von **Potenzreihen**, der andere ist eine algebraische Methode unter Verwendung von **Leiteroperatoren**. Die algebraische Methode ist schneller und einfacher, aber es ist auch wichtig, die analytische Lösung mit Potenzreihen zu studieren. Hier werden wir die algebraische Lösungsmethode behandeln. Für die analytische Lösungsmethode verweise ich auf [diesen Artikel](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Kommutatoren und kanonische Vertauschungsrelation
Gleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) kann unter Verwendung des Impulsoperators $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ wie folgt geschrieben werden:

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Nun wollen wir den Hamilton-Operator

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

faktorisieren.

Wenn $p$ und $x$ Zahlen wären, könnten wir einfach faktorisieren:

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

Aber hier sind $\hat{p}$ und $\hat{x}$ Operatoren, und für Operatoren gilt im Allgemeinen nicht das **Kommutativgesetz** ($\hat{p}\hat{x}\neq \hat{x}\hat{p}$), sodass es nicht so einfach ist. Trotzdem kann es als Ausgangspunkt dienen, also beginnen wir damit, die folgende Größe zu betrachten:

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Für die oben definierten Operatoren $\hat{a}_\pm$ gilt für $\hat{a}\_-\hat{a}\_+$:

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Hier wird der Term $(\hat{x}\hat{p}-\hat{p}\hat{x})$ als **Kommutator** von $\hat{x}$ und $\hat{p}$ bezeichnet und gibt an, wie schlecht die beiden Operatoren kommutieren. Im Allgemeinen wird der Kommutator von zwei Operatoren $\hat{A}$ und $\hat{B}$ mit eckigen Klammern wie folgt dargestellt:

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

Mit dieser Notation kann Gleichung ($\ref{eqn:a_m_times_a_p_without_commutator}$) wie folgt umgeschrieben werden:

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Nun müssen wir den Kommutator von $\hat{x}$ und $\hat{p}$ bestimmen.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

Wenn wir die Testfunktion $f(x)$ weglassen, erhalten wir:

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

Dies wird als **kanonische Vertauschungsrelation** bezeichnet.

## Leiteroperatoren
Aufgrund der kanonischen Vertauschungsrelation wird Gleichung ($\ref{eqn:a_m_times_a_p}$) zu:

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

also

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Hier ist die Reihenfolge von $\hat{a}\_-$ und $\hat{a}\_+$ wichtig. Wenn wir $\hat{a}\_+$ links platzieren, erhalten wir:

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

und es gilt:

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

In diesem Fall kann der Hamilton-Operator auch geschrieben werden als:

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Daher kann die zeitunabhängige Schrödinger-Gleichung ($\hat{H}\psi=E\psi$) mit $\hat{a}_\pm$ ausgedrückt werden als:

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(Doppelvorzeichen in gleicher Reihenfolge).

Nun können wir die folgende wichtige Eigenschaft ableiten:

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Beweis:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> Ebenso gilt:
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Daher können wir, wenn wir eine Lösung der zeitunabhängigen Schrödinger-Gleichung finden können, alle anderen Lösungen finden. Da wir für jeden beliebigen stationären Zustand das Energieniveau erhöhen oder senken können, werden $\hat{a}\_\pm$ als **Leiteroperatoren** bezeichnet, wobei $\hat{a}\_+$ der **Erzeugungsoperator** und $\hat{a}\_-$ der **Vernichtungsoperator** ist.

## Stationäre Zustände des harmonischen Oszillators
### Stationäre Zustände $\psi_n$ und Energieniveaus $E_n$
Wenn wir den Vernichtungsoperator wiederholt anwenden, erhalten wir irgendwann einen Zustand mit negativer Energie, der physikalisch nicht existieren kann. Mathematisch gesehen ist $\hat{a}_-\psi$ zwar eine Lösung der Schrödinger-Gleichung, wenn $\psi$ eine Lösung ist, aber es gibt keine Garantie, dass diese neue Lösung immer normiert ist (d.h. einen physikalisch möglichen Zustand darstellt). Wenn wir den Vernichtungsoperator weiter anwenden, erhalten wir schließlich die triviale Lösung $\psi=0$.

Daher gibt es für die stationären Zustände $\psi$ des harmonischen Oszillators eine "niedrigste Stufe" $\psi_0$, für die gilt:

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(es existiert kein niedrigeres Energieniveau). Dieses $\psi_0$ erfüllt:

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

also,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

Dies ist eine [trennbare gewöhnliche Differentialgleichung](/posts/Separation-of-Variables/), die wie folgt einfach gelöst werden kann:

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Diese Funktion kann wie folgt normiert werden:

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Hier ist $A^2 = \sqrt{m\omega / \pi\hbar}$, also

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Wenn wir nun diese Lösung in die zuvor gefundene Schrödinger-Gleichung ($\ref{eqn:schrodinger_eqn_with_ladder}$) einsetzen und berücksichtigen, dass $\hat{a}_-\psi_0=0$ ist, erhalten wir:

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Ausgehend von diesem **Grundzustand** können wir durch wiederholte Anwendung des Erzeugungsoperators angeregte Zustände erhalten, wobei die Energie bei jeder Anwendung des Erzeugungsoperators um $\hbar\omega$ zunimmt.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

Hier ist $A_n$ die Normierungskonstante. Auf diese Weise können wir, nachdem wir den Grundzustand gefunden haben, durch Anwendung des Erzeugungsoperators alle stationären Zustände und erlaubten Energieniveaus des harmonischen Oszillators bestimmen.

### Normierung
Die Normierungskonstante kann auch algebraisch bestimmt werden. Wir wissen, dass $\hat{a}\_{\pm}\psi_n$ proportional zu $\psi\_{n\pm 1}$ ist, also können wir schreiben:

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Beachten wir nun, dass für beliebige integrierbare Funktionen $f(x)$ und $g(x)$ Folgendes gilt:

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ ist das **hermitesche Konjugat (hermitian conjugate)** und der **adjungierte Operator (adjoint operator)** von $\hat{a}\_\pm$.

> **Beweis:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

Wenn wir also $f=\hat{a}_\pm \psi_n$, $g=\psi_n$ setzen, erhalten wir:

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Aus den Gleichungen ($\ref{eqn:schrodinger_eqn_with_ladder}$) und ($\ref{eqn:psi_n_and_E_n}$) folgt dann:

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

Aus den Gleichungen ($\ref{eqn:norm_const}$) und ($\ref{eqn:norm_const_2}$) erhalten wir:

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

Da $\psi_n$ und $\psi_{n\pm1}$ alle normiert sind, gilt $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, und daher:

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

Daraus können wir jeden normierten stationären Zustand $\psi_n$ wie folgt bestimmen:

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

Das heißt, in Gleichung ($\ref{eqn:psi_n_and_E_n}$) ist die Normierungskonstante $A_n=\cfrac{1}{\sqrt{n!}}$.

### Orthogonalität der stationären Zustände
Wie beim [eindimensionalen unendlichen Potentialtopf](/posts/the-infinite-square-well/#3-diese-zust%C3%A4nde-besitzen-orthogonalit%C3%A4t) sind die stationären Zustände des harmonischen Oszillators orthogonal zueinander.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Beweis
Der Beweis kann mit Hilfe der zuvor gezeigten Gleichungen ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$) und ($\ref{eqn:norm_const_3}$) durchgeführt werden. In Gleichung ($\ref{eqn:hermitian_conjugate}$) setzen wir $f=\hat{a}_-\psi_m,\ g=\psi_n$ und verwenden:

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

Mit Hilfe der Orthogonalität können wir, [wie in Gleichung (19) für den eindimensionalen unendlichen Potentialtopf](/posts/the-infinite-square-well/#berechnung-der-allgemeinen-l%C3%B6sung-psixt-der-zeitabh%C3%A4ngigen-schr%C3%B6dinger-gleichung), die Koeffizienten $c_n$ bei der Entwicklung von $\Psi(x,0)$ als Linearkombination der stationären Zustände $\sum c_n\psi_n(x)$ mit der [Fourier-Methode](/posts/the-infinite-square-well/#berechnung-der-koeffizienten-c_n-mit-dem-fourier-trick) bestimmen.

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Auch hier ist $\|c_n\|^2$ die Wahrscheinlichkeit, bei einer Energiemessung den Wert $E_n$ zu erhalten.

## Erwartungswert der potentiellen Energie $\langle V \rangle$ in einem beliebigen stationären Zustand $\psi_n$
Um $\langle V \rangle$ zu berechnen, müssen wir das folgende Integral auswerten:

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

Für die Berechnung solcher Integrale, die Potenzen von $\hat{x}$ und $\hat{p}$ enthalten, ist die folgende Methode nützlich:

Zunächst drücken wir $\hat{x}$ und $\hat{p}$ mit Hilfe der Definition der Leiteroperatoren in Gleichung ($\ref{eqn:ladder_operators}$) durch Erzeugungs- und Vernichtungsoperatoren aus:

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Nun stellen wir die physikalische Größe, deren Erwartungswert wir berechnen möchten, mit Hilfe dieser Ausdrücke für $\hat{x}$ und $\hat{p}$ dar. Hier interessieren wir uns für $x^2$, also:

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

Daraus erhalten wir:

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

Hier sind $\left(\hat{a}\_\pm \right)^2$ proportional zu $\psi\_{n\pm2}$ und daher orthogonal zu $\psi\_n$, sodass die beiden Terme $\left(\hat{a}\_+ \right)^2$ und $\left(\hat{a}\_- \right)^2$ zu $0$ werden. Schließlich berechnen wir die verbleibenden zwei Terme mit Hilfe von Gleichung ($\ref{eqn:norm_const_2}$):

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Mit Bezug auf Gleichung ($\ref{eqn:psi_n_and_E_n}$) sehen wir, dass der Erwartungswert der potentiellen Energie genau die Hälfte der Gesamtenergie beträgt, und die andere Hälfte ist natürlich die kinetische Energie $T$. Dies ist eine charakteristische Eigenschaft des harmonischen Oszillators.
