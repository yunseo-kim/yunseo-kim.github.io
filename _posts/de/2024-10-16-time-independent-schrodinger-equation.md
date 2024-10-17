---
title: "Zeitunabhängige Schrödinger-Gleichung"
description: >-
  Wir leiten die zeitunabhängige Schrödinger-Gleichung ψ(x) her, indem wir die Methode der Variablentrennung auf die ursprüngliche Form der Schrödinger-Gleichung (zeitabhängige Schrödinger-Gleichung) Ψ(x,t) anwenden.
  Wir untersuchen die mathematische und physikalische Bedeutung und Wichtigkeit der so erhaltenen separierten Lösung.
  Schließlich betrachten wir die Methode zur Bestimmung der allgemeinen Lösung der Schrödinger-Gleichung durch Linearkombination der separierten Lösungen.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - Separierte Lösung: $ \Psi(x,t) = \psi(x)\phi(t)$
> - Zeitabhängigkeit ("Wiggle-Faktor"): $ \phi(t) = e^{-iEt/\hbar} $
> - Hamilton-Operator: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Zeitunabhängige Schrödinger-Gleichung: $ \hat H\psi = E\psi $
> - Physikalische und mathematische Bedeutung und Wichtigkeit der separierten Lösung:
>   1. Stationäre Zustände
>   2. Besitzt einen eindeutigen Gesamtenergie-Wert $E$
>   3. Die allgemeine Lösung der Schrödinger-Gleichung ist eine Linearkombination der separierten Lösungen
> - Allgemeine Lösung der zeitabhängigen Schrödinger-Gleichung: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Voraussetzungen
- Kontinuierliche Wahrscheinlichkeitsverteilung und Wahrscheinlichkeitsdichte
- [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest-Theorem](/posts/ehrenfest-theorem/)
- [Methode der Variablentrennung](/posts/separation-of-variables/)

## Herleitung mit der Methode der Variablentrennung
Im Beitrag über das [Ehrenfest-Theorem](/posts/ehrenfest-theorem/) haben wir untersucht, wie verschiedene physikalische Größen mit Hilfe der Wellenfunktion $\Psi$ berechnet werden können. Die wichtige Frage ist nun, wie man diese Wellenfunktion $\Psi(x,t)$ erhält. Normalerweise muss man die [Schrödinger-Gleichung](/posts/schrodinger-equation-and-the-wave-function/), eine partielle Differentialgleichung in Bezug auf Position $x$ und Zeit $t$, für ein gegebenes Potential $V(x,t)$ lösen.

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

Wenn das Potential $V$ zeitunabhängig ist, kann die obige Schrödinger-Gleichung mit der [Methode der Variablentrennung](/posts/Separation-of-Variables/) gelöst werden. Betrachten wir eine Lösung in der Form eines Produkts einer Funktion $\psi$, die nur von $x$ abhängt, und einer Funktion $\phi$, die nur von $t$ abhängt:

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

Auf den ersten Blick mag dies wie eine übermäßig einschränkende Darstellung erscheinen, die nur eine kleine Teilmenge der gesamten Lösungen liefern kann. Tatsächlich hat die so erhaltene Lösung jedoch eine wichtige Bedeutung, und durch eine bestimmte Art der Addition dieser separierbaren Lösungen kann die allgemeine Lösung gefunden werden.

Für die separierbare Lösung gilt:

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

Wenn wir dies in Gleichung ($\ref{eqn:schrodinger_eqn}$) einsetzen, können wir die Schrödinger-Gleichung wie folgt schreiben:

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

Wenn wir beide Seiten durch $\psi\phi$ teilen, erhalten wir:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

wobei die linke Seite nur eine Funktion von $t$ und die rechte Seite nur eine Funktion von $x$ ist. Damit diese Gleichung eine Lösung hat, müssen beide Seiten konstant sein. Andernfalls würde sich bei Änderung einer der Variablen $t$ oder $x$ nur eine Seite der Gleichung ändern, während die andere konstant bliebe, was die Gleichung ungültig machen würde. Daher können wir die linke Seite als Separationskonstante $E$ setzen:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

Dies führt zu zwei gewöhnlichen Differentialgleichungen, eine für den zeitabhängigen Teil:

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

und eine für den ortsabhängigen Teil:

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

Die gewöhnliche Differentialgleichung ($\ref{eqn:ode_t}$) für $t$ kann leicht gelöst werden. Die allgemeine Lösung dieser Gleichung ist $ce^{-iEt/\hbar}$, aber da wir mehr an dem Produkt $\psi\phi$ als an $\phi$ selbst interessiert sind, können wir die Konstante $c$ in $\psi$ einbeziehen. Somit erhalten wir:

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

Die gewöhnliche Differentialgleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) für $x$ wird als **zeitunabhängige Schrödinger-Gleichung** bezeichnet. Um diese Gleichung zu lösen, muss das Potential $V(x)$ bekannt sein.

## Physikalische und mathematische Bedeutung
Mit der Methode der Variablentrennung haben wir die Funktion $\phi(t)$, die nur von der Zeit $t$ abhängt, und die zeitunabhängige Schrödinger-Gleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) erhalten. Obwohl die meisten Lösungen der ursprünglichen **zeitabhängigen Schrödinger-Gleichung** ($\ref{eqn:schrodinger_eqn}$) nicht in der Form $\psi(x)\phi(t)$ dargestellt werden können, ist die Form der zeitunabhängigen Schrödinger-Gleichung dennoch wichtig, weil ihre Lösungen die folgenden drei Eigenschaften besitzen:

### 1. Sie sind stationäre Zustände.
Obwohl die Wellenfunktion selbst

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

von $t$ abhängt, ist die Wahrscheinlichkeitsdichte

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

zeitunabhängig, da sich die Zeitabhängigkeit aufhebt.

> Für normierbare Lösungen muss die Separationskonstante $E$ reell sein.
>
> Wenn wir $E$ in Gleichung ($\ref{eqn:separation_of_variables}$) als komplexe Zahl $E_0+i\Gamma$ ($E_0$, $\Gamma$ sind reell) annehmen, erhalten wir
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> Wie wir in [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/#normierung-der-wellenfunktion-normalization) gesehen haben, muss $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ eine zeitunabhängige Konstante sein, daher muss $\Gamma=0$ sein. $\blacksquare$
{: .prompt-info }

Dasselbe gilt für die Berechnung des Erwartungswerts einer beliebigen physikalischen Größe, sodass Gleichung (8) des [Ehrenfest-Theorems](/posts/ehrenfest-theorem/) zu

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

wird, und somit sind alle Erwartungswerte zeitunabhängig. Insbesondere ist $\langle x \rangle$ konstant, daher ist $\langle p \rangle=0$.

### 2. Sie besitzen einen eindeutigen Gesamtenergie-Wert $E$, nicht eine Wahrscheinlichkeitsverteilung über einen Bereich.
In der klassischen Mechanik wird die Gesamtenergie (kinetische Energie plus potentielle Energie) als **Hamiltonian** bezeichnet und definiert als

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Wenn wir $p$ durch $-i\hbar(\partial/\partial x)$ ersetzen, erhalten wir den entsprechenden Hamilton-Operator in der Quantenmechanik:

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

Daher kann die zeitunabhängige Schrödinger-Gleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) geschrieben werden als

$$ \hat H \psi = E\psi \tag{15}$$

und der Erwartungswert des Hamiltonians ist:

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

Außerdem gilt

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

daher

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

und folglich ist die Varianz des Hamiltonians $H$

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

Das bedeutet, dass bei der Messung der Gesamtenergie für die separierte Lösung immer der konstante Wert $E$ gemessen wird.

### 3. Die allgemeine Lösung der zeitabhängigen Schrödinger-Gleichung ist eine Linearkombination der separierten Lösungen.

Die zeitunabhängige Schrödinger-Gleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) hat unendlich viele Lösungen $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Nennen wir diese \{$\psi_n(x)$\}. Für jede dieser Lösungen existiert eine Separationskonstante $E_1,E_2,E_3,\dots=$\{$E_n$\}, sodass für jedes **mögliche Energieniveau** eine entsprechende Wellenfunktion existiert.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

Die zeitabhängige Schrödinger-Gleichung ($\ref{eqn:schrodinger_eqn}$) hat die Eigenschaft, dass eine Linearkombination zweier beliebiger Lösungen ebenfalls eine Lösung ist. Sobald wir also die separierten Lösungen gefunden haben, können wir sofort eine allgemeinere Form der Lösung erhalten:

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

Jede Lösung der zeitabhängigen Schrödinger-Gleichung kann in dieser Form geschrieben werden. Die verbleibende Aufgabe besteht darin, die geeigneten Konstanten $c_1, c_2, \dots$ zu finden, die die im Problem gegebenen Anfangsbedingungen erfüllen, um die gesuchte spezielle Lösung zu erhalten. Mit anderen Worten, sobald wir die zeitunabhängige Schrödinger-Gleichung gelöst haben, ist es einfach, die allgemeine Lösung der zeitabhängigen Schrödinger-Gleichung zu finden.

> Es ist zu beachten, dass die separierte Lösung 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> ein stationärer Zustand ist, bei dem alle Wahrscheinlichkeiten und Erwartungswerte zeitunabhängig sind, während die allgemeine Lösung in Gleichung ($\ref{eqn:general_solution}$) diese Eigenschaft nicht besitzt.
{: .prompt-warning }

## Energieerhaltung
In der allgemeinen Lösung ($\ref{eqn:general_solution}$) repräsentiert das Quadrat des Absolutbetrags der Koeffizienten \{$c_n$\}, also $\|c_n\|^2$, physikalisch die Wahrscheinlichkeit, dass bei der Messung der Energie eines Teilchens im Zustand $\Psi$ der Wert $E_n$ gemessen wird. Daher muss die Summe dieser Wahrscheinlichkeiten

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

gleich 1 sein, und der Erwartungswert des Hamiltonians ist

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Da sowohl die Energieniveaus $E_n$ der einzelnen stationären Zustände als auch die Koeffizienten \{$c_n$\} zeitunabhängig sind, bleiben sowohl die Wahrscheinlichkeit, eine bestimmte Energie $E_n$ zu messen, als auch der Erwartungswert des Hamiltonians $H$ zeitlich konstant.
