---
title: "Die Schrödinger-Gleichung und die Wellenfunktion"
description: >-
  Wir betrachten die grundlegende Form der Schrödinger-Gleichung, die in der Quantenmechanik eine ähnliche Stellung einnimmt wie die Newtonschen Bewegungsgesetze in der klassischen Mechanik.
  Außerdem untersuchen wir die statistische Interpretation der physikalischen Bedeutung der Wellenfunktion, die als Lösung der Schrödinger-Gleichung erhalten wird, verschiedene Perspektiven auf die quantenmechanische Unbestimmtheit und die physikalische Bedeutung des Messvorgangs (Kollaps der Wellenfunktion) in der Kopenhagener Deutung.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
mermaid: true
---

## TL;DR
> - (Zeitabhängige) Schrödinger-Gleichung: 
>
> $$ i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi $$
>
> - Statistische Interpretation der Wellenfunktion $\Psi(x,t)$ (Born-Interpretation): Das Betragsquadrat der Wellenfunktion $\|\Psi(x,t)\|^2$ ist die **Wahrscheinlichkeitsdichtefunktion**, ein Teilchen zur Zeit $t$ am Ort $x$ zu finden.
> - Normierung der Wellenfunktion:
>   - $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx = 1$
>   - Wenn $\Psi(x,t)$ eine Lösung der Schrödinger-Gleichung ist, dann ist auch $A\Psi(x,t)$ für jede komplexe Konstante $A$ eine Lösung. Die Bestimmung von $A$ so, dass die obige Gleichung erfüllt wird, nennt man Normierung.
>   - **Nicht normierbare Lösungen** können kein Teilchen darstellen und sind daher keine gültigen Wellenfunktionen. Nur **quadratintegrierbare** Lösungen sind physikalisch mögliche Zustände.
>   - Eine zu einem Zeitpunkt normierte Wellenfunktion bleibt auch bei zeitlicher Entwicklung von $\Psi$ normiert.
> - Wahrscheinlichkeitsstrom:
>   - $J(x,t) \equiv \cfrac{i\hbar}{2m}\left(\Psi\cfrac{\partial \Psi^\*}{\partial x}-\Psi^\*\cfrac{\partial \Psi}{\partial x}\right)$
>   - Fluss der Wahrscheinlichkeit (Wahrscheinlichkeit pro Zeiteinheit), ein Teilchen am Punkt $x$ zu finden
>   - Wenn $P_{ab}(t)$ die Wahrscheinlichkeit ist, das Teilchen zur Zeit $t$ im Bereich $a<x<b$ zu finden, dann gilt $\cfrac{dP_{ab}}{dt} = J(a,t) - J(b,t)$
{: .prompt-info }

## Voraussetzungen
- Kontinuierliche Wahrscheinlichkeitsverteilungen und Wahrscheinlichkeitsdichte

## Die Schrödinger-Gleichung (Schrödinger equation)
Betrachten wir ein Teilchen der Masse $m$, das sich unter dem Einfluss einer gegebenen Kraft $F(x,t)$ entlang der $x$-Achse bewegt.

In der klassischen Mechanik ist das Hauptziel, Newtons Bewegungsgleichung $F=ma$ anzuwenden, um die Position $x(t)$ des Teilchens zu einem beliebigen Zeitpunkt zu bestimmen. Dieser Prozess kann grob durch das folgende Diagramm dargestellt werden:

```mermaid
flowchart TD
	conditions["Gegebene Bedingungen"] -- F=ma --> x["Position x(t)"]
	x --> quantities["Physikalische Größen"]
```

In der Quantenmechanik wird dasselbe Problem auf eine sehr unterschiedliche Weise angegangen. Der quantenmechanische Ansatz besteht darin, die folgende **Schrödinger-Gleichung** zu lösen, um die **Wellenfunktion** $\Psi(x,t)$ des Teilchens zu erhalten:

$$ \begin{gather*}
i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}\\
\text{(} i=\sqrt{-1}\text{, } \hbar=\frac{h}{2\pi}=1.054573\times10^{-34}\text{, } h\text{: Planck-Konstante, } V(x)\text{: potentielle Energie)}
\end{gather*} $$

![Komplexe Darstellung einer Wellenfunktion, die die nichtrelativistische Schrödinger-Gleichung mit V = 0 (freies Teilchen) erfüllt](https://upload.wikimedia.org/wikipedia/commons/b/b7/Wavepacket-a2k4-en.gif?20210105144724)
> *Bildquelle*
> - Autor: Wikimedia-Benutzer Xcodexif
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

```mermaid
flowchart TD
	conditions["Bedingungen Ψ(x,0)"] -- "Schrödinger-Gleichung" --> x["Wellenfunktion Ψ(x,t)"]
	x --> quantities["PD der Größen"]
```

## Statistische Interpretation der Wellenfunktion $\Psi(x,t)$ (Born-Interpretation)
Während ein Teilchen in der klassischen Mechanik an einem Punkt lokalisiert ist, ist die Wellenfunktion, die den Zustand eines Teilchens in der Quantenmechanik beschreibt, eine Funktion von $x$ für ein gegebenes $t$ und somit im Raum ausgedehnt. Wie soll man diese physikalische Bedeutung interpretieren?

Nach Borns **statistischer Interpretation** ist das Betragsquadrat der Wellenfunktion $\|\Psi(x,t)\|^2$ die Wahrscheinlichkeitsdichtefunktion, ein Teilchen zur Zeit $t$ am Ort $x$ zu finden. Obwohl die Wellenfunktion $\Psi$ selbst komplex ist, ist $\|\Psi\|^2=\Psi^\*\Psi$ ($\Psi^\*$ ist die komplexe Konjugation von $\Psi$) eine nicht-negative reelle Zahl, was diese Interpretation ermöglicht. Das kann wie folgt ausgedrückt werden:

$$ \int_a^b |\Psi(x,t)|^2 dx = \text{Wahrscheinlichkeit, das Teilchen zur Zeit }t\text{ zwischen }a\text{ und }b\text{ zu finden}. \tag{2}$$

Diese statistische Interpretation impliziert, dass die Quantenmechanik eine Art **Unbestimmtheit (indeterminacy)** beinhaltet. Selbst wenn man alles über ein Teilchen (seine Wellenfunktion) kennt, kann man nur die Wahrscheinlichkeitsverteilung möglicher Ergebnisse kennen, nicht aber einen bestimmten Wert festlegen.

Da dies intuitiv schwer zu akzeptieren war, wurden natürlich Fragen aufgeworfen, ob diese Unbestimmtheit auf einen Mangel in der Quantenmechanik zurückzuführen oder eine wesentliche Eigenschaft der Natur sei.

## Perspektiven auf die quantenmechanische Unbestimmtheit (quantum indeterminacy)
Angenommen, wir messen die Position eines Teilchens und stellen fest, dass es sich am Punkt $C$ befindet. Wo war das Teilchen dann unmittelbar vor der Messung?

### Realistische (realist) Position

> "Gott würfelt nicht." ("God does not play dice.")  
> *von Albert Einstein*

Das Teilchen war schon immer bei $C$. Dies war auch die Sichtweise von Einstein und Schrödinger. Aus dieser Perspektive betrachtet, war das Teilchen tatsächlich genau bei $C$, aber aufgrund der Grenzen der Theorie konnten wir die Position des Teilchens bis zur Messung nur als Wahrscheinlichkeitsverteilung kennen, was die Quantenmechanik zu einer unvollständigen Theorie macht. Mit anderen Worten, nach dieser Ansicht ist die Unbestimmtheit keine wesentliche Eigenschaft der Natur, sondern eine Folge der Grenzen der Quantenmechanik, und es müssen zusätzlich zu $\Psi$ noch einige verborgene Variablen existieren, die man kennen muss, um das Teilchen vollständig zu beschreiben.

> Schrödinger war einst Einsteins Assistent und arbeitete unter ihm. Später pflegte er weiterhin den Austausch mit Einstein. Es ist wahrscheinlich, dass Schrödingers realistische und deterministische Position auch von diesem Einfluss herrührt.
{: .prompt-info }

### Orthodoxe (orthodox) Position

> "Hören Sie auf, Gott vorzuschreiben, was er mit seinen Würfeln tun soll." ("Stop telling God what to do with his dice.")  
> *von Niels Bohr, als Antwort auf Einsteins früheres Zitat*
>
> "Beobachtungen stören nicht nur das zu Messende, sie erzeugen es" ("Observations not only disturb what is to be measured, they produce it")  
> ...  
> "Wir zwingen es, eine bestimmte Position einzunehmen." ("We compel to assume a definite position.")  
> *von Pascual Jordan*

Bis unmittelbar vor der Messung existiert das Teilchen nur in Form einer Wahrscheinlichkeitsverteilung und ist nirgendwo, und erst durch den Akt der Messung erscheint das Teilchen an einer bestimmten Position. Diese Interpretation wird als **Kopenhagener Deutung** bezeichnet und wurde von Bohr und Heisenberg an der Universität Kopenhagen vorgeschlagen.

> Interessanterweise war Heisenberg, ähnlich wie die Beziehung zwischen Einstein und Schrödinger, auch ein Schüler von Bohr.
{: .prompt-info }

### Agnostische (agnostic) Position

> "Man sollte sich den Kopf nicht darüber zerbrechen, ob etwas, über das man nichts wissen kann, trotzdem existiert, ebenso wenig wie über die alte Frage, wie viele Engel auf einer Nadelspitze Platz haben." ("One should no more rack one's brain about the problem of whether something one cannot know anything about exists all the same, than about the ancient question of how many angels are able to sit on the point of a needle.")  
> *von Wolfgang Pauli*

Man verweigert die Antwort. Welche Behauptung man auch immer über den Zustand des Teilchens vor der Messung aufstellt, wenn die einzige Möglichkeit, die Richtigkeit dieser Behauptung zu überprüfen, eine Messung ist, dann ist es nicht mehr "vor der Messung" - welchen Sinn hat das dann? Es ist lediglich Metaphysik, über etwas zu spekulieren, das grundsätzlich nicht überprüft oder erkannt werden kann.

### Heutige Konvention
1964 bewies John Bell, dass es beobachtbare Unterschiede gibt, je nachdem, ob ein Teilchen vor oder nach der Messung eine genaue Position hat oder nicht. Damit wurde zunächst die agnostische Position ausgeschlossen, und durch anschließende Experimente wurde die Kopenhagener Deutung zur vorherrschenden Interpretation. Daher wird, wenn nicht anders angegeben, in der Regel diese Kopenhagener Deutung vorausgesetzt, wenn man sich mit Quantenmechanik befasst.

> Es gibt immer noch andere mögliche Interpretationen neben der Kopenhagener Deutung, wie die nichtlokale Theorie verborgener Variablen (nonlocal hidden variable theories) oder die Viele-Welten-Interpretation (many worlds interpretation).
{: .prompt-info }

## Messung und Kollaps der Wellenfunktion
Ein Teilchen hat bis zur Messung keine genaue Position, sondern erhält erst durch die Messung eine bestimmte Position $C$ (tatsächlich hat auch diese Position aufgrund der Heisenbergschen Unschärferelation, die wir in einem späteren Artikel behandeln werden, einen gewissen Fehlerbereich und ist kein perfekt genauer Wert). Wenn man jedoch unmittelbar nach dieser ersten Messung eine weitere Messung durchführt, erhält man nicht bei jeder Messung einen anderen Wert, sondern immer das gleiche Ergebnis. Dies wird wie folgt erklärt:

Im Moment der ersten Messung ändert sich die Wellenfunktion des Messobjekts drastisch und konzentriert sich zu einer schmalen, spitzen Form des $\|\Psi(x,t)\|^2$-Graphen um den Punkt $C$. Man sagt, die Wellenfunktion sei durch die Messung zum Punkt $C$ **kollabiert (collapse)**.

Das heißt, physikalische Prozesse können in zwei unterschiedliche Arten unterteilt werden:
- Gewöhnliche (ordinary) Prozesse, bei denen sich die Wellenfunktion langsam gemäß der Schrödinger-Gleichung ändert
- Messprozesse (measurement), bei denen $\Psi$ plötzlich und diskontinuierlich kollabiert

> Eine durch Messung kollabierte Wellenfunktion breitet sich mit der Zeit gemäß der Schrödinger-Gleichung wieder räumlich aus. Um das gleiche Messergebnis zu reproduzieren, muss die zweite Messung daher unmittelbar erfolgen.
{: .prompt-tip }

## Normierung der Wellenfunktion (Normalization)
Da das Betragsquadrat der Wellenfunktion $\|\Psi(x,t)\|^2$ die Wahrscheinlichkeitsdichte ist, ein Teilchen zur Zeit $t$ am Ort $x$ zu finden, muss das Integral von $\|\Psi\|^2$ über alle $x$ gleich 1 sein.

$$ \int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1. \label{eqn:wavefunction_norm}\tag{3} $$

Aus Gleichung ($\ref{eqn:schrodinger_eqn}$) ist ersichtlich, dass wenn $\Psi(x,t)$ eine Lösung ist, auch $A\Psi(x,t)$ für jede komplexe Konstante $A$ eine Lösung ist. Daher muss $A$ so bestimmt werden, dass Gleichung ($\ref{eqn:wavefunction_norm}$) erfüllt wird. Dieser Prozess wird als Normierung der Wellenfunktion bezeichnet. Einige Lösungen der Schrödinger-Gleichung divergieren bei Integration gegen Unendlich, und in diesem Fall gibt es keine Konstante $A$, die Gleichung ($\ref{eqn:wavefunction_norm}$) erfüllt. Dasselbe gilt für die triviale Lösung $\Psi=0$. Solche **nicht normierbaren Lösungen (non-normalizable solutions)** können kein Teilchen darstellen und sind daher keine gültigen Wellenfunktionen. Physikalisch mögliche Zustände entsprechen den **quadratintegrierbaren (square-integrable)** Lösungen der Schrödinger-Gleichung.

Eine wichtige Eigenschaft der Schrödinger-Gleichung ist außerdem, dass <u>eine zu einem Zeitpunkt normierte Wellenfunktion auch bei zeitlicher Entwicklung von $\Psi$ normiert bleibt ($\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$)</u>. Wenn die Wellenfunktion zu jedem Zeitpunkt mit einem anderen $A$-Wert normiert werden müsste, wäre $A$ keine Konstante, sondern eine Funktion der Zeit $t$, und es wäre nicht mehr möglich, eine Lösung der Schrödinger-Gleichung zu finden. Aufgrund dieser Eigenschaft bleibt jedoch der $A$-Wert, der in den Anfangsbedingungen ($t=0$) normiert wurde, unabhängig von der Zeit $t$ erhalten.

### Beweis

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \int_{-\infty}^{\infty} \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx. \label{eqn:norm_proof_1}\tag{4} $$

> Da das Integral von $\|\Psi\|^2$ über $x$ nur eine Funktion von $t$ ist, verwenden wir auf der linken Seite die totale Ableitung ($d/dt$), während $\|\Psi\|^2$ selbst eine Funktion von zwei Variablen $x$ und $t$ ist, weshalb wir auf der rechten Seite die partielle Ableitung ($\partial/\partial t$) verwenden.
{: .prompt-tip }

Die obige Gleichung kann nach der Produktregel der Differentiation wie folgt umgeschrieben werden:

$$ \frac{\partial}{\partial t}|\Psi|^2 = \frac{\partial}{\partial t}(\Psi^*\Psi) = \Psi^*\frac{\partial \Psi}{\partial t} + \frac{\partial \Psi^*}{\partial t}\Psi. \label{eqn:norm_proof_2}\tag{5}$$

Wenn wir beide Seiten der Schrödinger-Gleichung ($\ref{eqn:schrodinger_eqn}$) mit $-\cfrac{i}{\hbar}$ multiplizieren, erhalten wir

$$ \frac{\partial \Psi}{\partial t} = \frac{i\hbar}{2m}\frac{\partial^2 \Psi}{\partial x^2}-\frac{i}{\hbar}V\Psi \label{eqn:norm_proof_3}\tag{6}$$

und wenn wir die komplexe Konjugation von $\cfrac{\partial \Psi}{\partial t}$ in der obigen Gleichung nehmen, erhalten wir

$$ \frac{\partial \Psi^*}{\partial t} = -\frac{i\hbar}{2m}\frac{\partial^2 \Psi^*}{\partial x^2}+\frac{i}{\hbar}V\Psi^* \label{eqn:norm_proof_4}\tag{7}$$

Wenn wir nun ($\ref{eqn:norm_proof_3}$) und ($\ref{eqn:norm_proof_4}$) in Gleichung ($\ref{eqn:norm_proof_2}$) einsetzen, erhalten wir

$$\begin{align*}
\frac{\partial}{\partial t}|\Psi|^2 &= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right) \\
&= \frac{\partial}{\partial x}\left[\frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right) \right] 
\end{align*} \label{eqn:norm_proof_5}\tag{8}$$

und wenn wir dies in die rechte Seite der ursprünglichen Gleichung ($\ref{eqn:norm_proof_1}$) einsetzen, erhalten wir

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|_{-\infty}^{\infty}. \label{eqn:norm_proof_6}\tag{9} $$

Damit die Wellenfunktion normiert und physikalisch gültig ist, muss $\Psi(x,t)$ für $x$ gegen $\pm\infty$ gegen $0$ konvergieren. Daher gilt

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 0 \label{eqn:norm_proof_fin}\tag{10} $$

was bedeutet, dass $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx$ eine zeitunabhängige Konstante ist.

$$ \therefore \text{Wenn }\Psi \text{ zu einem Zeitpunkt }t\text{ normiert ist, ist es zu allen anderen Zeitpunkten }t\text{ ebenfalls normiert.} \blacksquare $$

## Wahrscheinlichkeitsstrom (probability current)
Betrachten wir nun die Wahrscheinlichkeit $P_{ab}(t)$, ein Teilchen zur Zeit $t$ im Bereich $a<x<b$ zu finden. Dann gilt

$$ P_{ab}(t) = \int_a^b |\Psi(x,t)|^2 dx \tag{11}$$

und

$$ \begin{align*}
\frac{dP_{ab}}{dt} &= \frac{d}{dt}\int_a^b |\Psi(x,t)|^2 dx \\
&= \int_a^b \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx \quad \text{(vgl. Gleichung }\ref{eqn:norm_proof_1}\text{)}\\
&= \int_a^b \left(\frac{\partial \Psi^*}{\partial t}\Psi + \Psi^*\frac{\partial \Psi}{\partial t} \right)dx \quad \text{(vgl. Gleichung }\ref{eqn:norm_proof_2}\text{)} \\
&= \frac{i\hbar}{2m}\int_a^b \left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right)dx \\
&= \frac{i\hbar}{2m}\int_a^b\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \quad \text{(vgl. Gleichungen }\ref{eqn:norm_proof_3},\ref{eqn:norm_proof_4},\ref{eqn:norm_proof_5}\text{)}\\
&= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial \Psi}{\partial x}-\frac{\partial \Psi^*}{\partial x}\Psi \right)\Bigg|^b_a \\
&= \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x} \right)\Bigg|^a_b
\end{align*} $$

Wenn wir nun

$$ J(x,t) \equiv \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x}\right) \label{eqn:probability_current}\tag{12}$$

definieren, erhalten wir

$$ \frac{dP_{ab}}{dt} = J(a,t) - J(b,t) \label{eqn:probability_over_time}\tag{13}$$

Die in Gleichung ($\ref{eqn:probability_current}$) definierte Größe $J(x,t)$ wird als **Wahrscheinlichkeitsstrom (probability current)** bezeichnet und repräsentiert den Fluss der Wahrscheinlichkeit (d.h. die Wahrscheinlichkeit pro Zeiteinheit), ein Teilchen am Punkt $x$ zu finden. Aus Gleichung ($\ref{eqn:probability_over_time}$) folgt, dass $P_{ab}$ zunimmt, wenn der Wahrscheinlichkeitsstrom $J(a,t)$, der zu einem bestimmten Zeitpunkt $t$ an einem Ende einfließt, größer ist als der Wahrscheinlichkeitsstrom $J(b,t)$, der am anderen Ende ausfließt, und umgekehrt abnimmt.

> *Man kann sich das vorstellen wie den Volumenstrom (flow rate) in der Fluiddynamik, wobei hier die Masse oder das Volumen der Flüssigkeit durch die Wahrscheinlichkeit ersetzt wird.
{: .prompt-info }
