---
title: "Das freie Teilchen"
description: >-
  Wir untersuchen die Tatsache, dass die separierte Lösung für ein freies Teilchen mit V(x)=0 nicht normierbar ist und was das bedeutet,
  zeigen qualitativ die Orts-Impuls-Unschärferelation für die allgemeine Lösung und berechnen die Phasen- und Gruppengeschwindigkeit von Ψ(x,t) mit physikalischer Interpretation.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
---

## TL;DR
> - Freies Teilchen: $V(x)=0$, keine Randbedingungen (beliebige Energie)
> - Die separierte Lösung $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ ist bei quadratischer Integration unendlich und daher nicht normierbar, was Folgendes impliziert:
>   - Freie Teilchen können nicht in stationären Zuständen existieren
>   - Freie Teilchen können keine exakt definierte Energie haben (Energieunschärfe existiert)
> - Dennoch ist die separierte Lösung mathematisch weiterhin wichtig, da die allgemeine Lösung der zeitabhängigen Schrödinger-Gleichung eine Linearkombination der separierten Lösungen ist. In diesem Fall gibt es jedoch keine Einschränkungen, sodass die allgemeine Lösung nicht eine Summe ($\sum$) über eine diskrete Variable $n$, sondern ein Integral ($\int$) über eine kontinuierliche Variable $k$ ist.
> - Allgemeine Lösung der Schrödinger-Gleichung:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{wobei }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Beziehung zwischen Orts- und Impulsunschärfe:
>   - Wenn die Ortsunschärfe abnimmt, nimmt die Impulsunschärfe zu, und umgekehrt
>   - Das bedeutet, dass es quantenmechanisch unmöglich ist, Ort und Impuls eines freien Teilchens gleichzeitig genau zu kennen
> - Phasen- und Gruppengeschwindigkeit der Wellenfunktion $\Psi(x,t)$:
>   - Phasengeschwindigkeit: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - Gruppengeschwindigkeit: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Physikalische Bedeutung der Gruppengeschwindigkeit und Vergleich mit der klassischen Mechanik:
>   - Physikalisch entspricht die Gruppengeschwindigkeit der Bewegungsgeschwindigkeit des Teilchens
>   - Unter der Annahme, dass $\phi(k)$ eine sehr scharfe Form in der Nähe eines Wertes $k_0$ hat (wenn die Impulsunschärfe ausreichend klein ist), gilt: 
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Voraussetzungen
- Eulersche Formel
- Fourier-Transformation & Plancherelscher Satz
- [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/)
- [Zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/)
- [Eindimensionaler unendlicher Potentialtopf](/posts/the-infinite-square-well/)

## Modellaufbau
Betrachten wir den einfachsten Fall eines freien Teilchens ($V(x)=0$). Klassisch ist dies lediglich eine Bewegung mit konstanter Geschwindigkeit, aber in der Quantenmechanik wird dieses Problem interessanter.  
Die [zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/) für ein freies Teilchen lautet

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

also

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, wobei }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[Bis hierhin ist es wie im Inneren eines unendlichen Potentialtopfs mit $V=0$](/posts/the-infinite-square-well/#modell-und-randbedingungen-aufstellen). Diesmal schreiben wir jedoch die allgemeine Lösung in folgender Exponentialform:

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ und $C\cos{kx}+D\sin{kx}$ sind äquivalente Methoden, um die gleiche Funktion von $x$ zu schreiben. Durch die Eulersche Formel $e^{ix}=\cos{x}+i\sin{x}$ gilt
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> Das heißt, wenn wir $C=A+B$ und $D=i(A-B)$ setzen, erhalten wir 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> Umgekehrt, wenn wir $A$ und $B$ durch $C$ und $D$ ausdrücken, erhalten wir $A=\cfrac{C-iD}{2}$ und $B=\cfrac{C+iD}{2}$.
>
> In der Quantenmechanik stellt die Exponentialfunktion für $V=0$ eine sich bewegende Welle dar und ist am bequemsten für die Behandlung freier Teilchen. Sinus- und Kosinusfunktionen hingegen eignen sich besser zur Darstellung stehender Wellen und treten natürlich im Fall des unendlichen Potentialtopfs auf.
{: .prompt-info }

Im Gegensatz zum unendlichen Potentialtopf gibt es diesmal keine Randbedingungen, die $k$ und $E$ einschränken. Das bedeutet, dass ein freies Teilchen beliebige positive Energien haben kann.

## Separierte Lösung und Phasengeschwindigkeit
Wenn wir die Zeitabhängigkeit $e^{-iEt/\hbar}$ zu $\psi(x)$ hinzufügen, erhalten wir

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

Jede beliebige Funktion von $x$ und $t$, die von einer speziellen Form $(x\pm vt)$ abhängt, stellt eine Welle dar, die sich mit der Geschwindigkeit $v$ in $\mp x$-Richtung bewegt, ohne ihre Form zu ändern. Daher repräsentiert der erste Term in Gleichung ($\ref{eqn:Psi_seperated_solution}$) eine nach rechts laufende Welle, während der zweite Term eine Welle mit gleicher Wellenlänge und Ausbreitungsgeschwindigkeit, aber unterschiedlicher Amplitude darstellt, die sich nach links bewegt. Da sie sich nur im Vorzeichen vor $k$ unterscheiden, können wir schreiben

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

wobei die Ausbreitungsrichtung der Welle je nach Vorzeichen von $k$ wie folgt ist:

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{Bewegung nach rechts}, \\
k<0 \Rightarrow & \text{Bewegung nach links}.
\end{cases} \tag{6}$$

Der 'stationäre Zustand' eines freien Teilchens ist offensichtlich eine fortschreitende Welle*, deren Wellenlänge $\lambda = 2\pi/\|k\|$ ist und die nach der de-Broglie-Formel einen Impuls von

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

hat.

> *Ein 'stationärer Zustand', der eine fortschreitende Welle ist, ist physikalisch natürlich ein Widerspruch. Der Grund dafür wird bald klar.
{: .prompt-info }

Außerdem ist die Geschwindigkeit dieser Welle wie folgt:

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(Hier ist $\omega$ der Koeffizient vor $t$, also $\cfrac{\hbar k^2}{2m}$.)

Diese Wellenfunktion kann jedoch nicht normiert werden, da sie bei quadratischer Integration unendlich wird.

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

Das bedeutet, <u>im Fall eines freien Teilchens ist die separierte Lösung kein physikalisch möglicher Zustand.</u> Freie Teilchen können nicht in [stationären Zuständen](/posts/time-independent-schrodinger-equation/#1-es-sind-stationäre-zustände) existieren und können auch [keinen bestimmten Energiewert](/posts/time-independent-schrodinger-equation/#2-sie-besitzen-einen-eindeutigen-gesamtenergie-wert-e-nicht-eine-wahrscheinlichkeitsverteilung-über-einen-bereich) haben. Tatsächlich wäre es intuitiv betrachtet seltsamer, wenn sich ohne jegliche Randbedingungen an beiden Enden eine stehende Welle bilden würde.

## Berechnung der allgemeinen Lösung $\Psi(x,t)$ der zeitabhängigen Schrödinger-Gleichung
Trotzdem hat diese separierte Lösung weiterhin eine wichtige Bedeutung, da [die allgemeine Lösung der zeitabhängigen Schrödinger-Gleichung eine Linearkombination der separierten Lösungen ist](/posts/time-independent-schrodinger-equation/#3-die-allgemeine-lösung-der-zeitabhängigen-schrödinger-gleichung-ist-eine-linearkombination-der-separierten-lösungen), unabhängig von der physikalischen Interpretation. In diesem Fall gibt es jedoch keine Einschränkungen, sodass die allgemeine Lösung nicht eine Summe ($\sum$) über eine diskrete Variable $n$, sondern ein Integral ($\int$) über eine kontinuierliche Variable $k$ ist.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Hier spielt $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ die gleiche Rolle wie $c_n$ in [Gleichung (21) des Beitrags 'Zeitunabhängige Schrödinger-Gleichung'](/posts/time-independent-schrodinger-equation/#3-die-allgemeine-lösung-der-zeitabhängigen-schrödinger-gleichung-ist-eine-linearkombination-der-separierten-lösungen).
{: .prompt-info }

Diese Wellenfunktion kann für geeignete $\phi(k)$ normiert werden, muss aber notwendigerweise einen Bereich von $k$ haben und hat daher einen Bereich von Energien und Geschwindigkeiten. Dies wird als **Wellenpaket** bezeichnet.

> Eine Sinusfunktion ist räumlich unendlich ausgedehnt und kann daher nicht normiert werden. Wenn man jedoch mehrere solcher Wellen überlagert, werden sie durch Interferenz lokalisiert und können normiert werden.
{: .prompt-info }

## Berechnung von $\phi(k)$ mit dem Plancherelschen Satz

Jetzt, da wir die Form von $\Psi(x,t)$ (Gleichung [$\ref{eqn:Psi_general_solution}$]) kennen, müssen wir nur noch $\phi(k)$ bestimmen, das die anfängliche Wellenfunktion

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

erfüllt. Dies ist ein typisches Problem der Fourier-Analyse, und wir können die Antwort mit dem **Plancherelschen Satz** erhalten.

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ wird als **Fourier-Transformation** von $f(x)$ bezeichnet, und $f(x)$ ist die **inverse Fourier-Transformation** von $F(k)$. Wie man in Gleichung ($\ref{eqn:plancherel_theorem}$) leicht erkennen kann, unterscheiden sich die beiden nur im Vorzeichen des Exponenten. Natürlich gibt es die Einschränkung, dass nur Funktionen zugelassen sind, für die das Integral existiert.

> Die notwendige und hinreichende Bedingung für die Existenz von $f(x)$ ist, dass $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ endlich sein muss. In diesem Fall ist auch $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ endlich, und es gilt 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Manche bezeichnen diese Gleichung als Plancherelschen Satz, nicht Gleichung ($\ref{eqn:plancherel_theorem}$) (so wird es auch in [Wikipedia](https://en.wikipedia.org/wiki/Plancherel_theorem) beschrieben).
{: .prompt-info }

In unserem Fall existiert das Integral aufgrund der physikalischen Bedingung, dass $\Psi(x,0)$ normiert sein muss. Daher ist die quantenmechanische Lösung für ein freies Teilchen durch Gleichung ($\ref{eqn:Psi_general_solution}$) gegeben, wobei

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

ist.

> Allerdings gibt es in der Praxis kaum Fälle, in denen das Integral in Gleichung ($\ref{eqn:Psi_general_solution}$) analytisch gelöst werden kann. Normalerweise werden die Werte durch numerische Analyse mit Computern berechnet.
{: .prompt-tip }

## Berechnung der Gruppengeschwindigkeit des Wellenpakets und physikalische Interpretation

Im Wesentlichen ist ein Wellenpaket eine Überlagerung zahlreicher Sinusfunktionen, deren Amplituden durch $\phi$ bestimmt werden. Das heißt, es gibt 'Kräuselungen (ripples)' innerhalb einer 'Einhüllenden (envelope)', die das Wellenpaket bildet.

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *Lizenzhinweis und Quellenangabe für das Bild*
> - Quellcode zur Bilderstellung (gnuplot): [yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - Lizenz: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - Originalautor: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - Ursprünglicher Lizenzhinweis: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Physikalisch entspricht die Geschwindigkeit des Teilchens nicht der Geschwindigkeit der einzelnen Kräuselungen (**Phasengeschwindigkeit**), die wir zuvor in Gleichung ($\ref{eqn:phase_velocity}$) berechnet haben, sondern der Geschwindigkeit der äußeren Einhüllenden (**Gruppengeschwindigkeit**).

### Beziehung zwischen Orts- und Impulsunschärfe
Betrachten wir den Integranden $\int\phi(k)e^{ikx}dk$ aus Gleichung ($\ref{eqn:Psi_at_t_0}$) und den Integranden $\int\Psi(x,0)e^{-ikx}dx$ aus Gleichung ($\ref{eqn:phi}$) separat, um die Beziehung zwischen Orts- und Impulsunschärfe zu untersuchen.

#### Bei kleiner Ortsunschärfe
Wenn $\Psi$ im Ortsraum in einem sehr schmalen Bereich $[x_0-\delta, x_0+\delta]$ um einen Wert $x_0$ verteilt ist und außerhalb dieses Bereichs nahe Null ist (<u>kleine Ortsunschärfe</u>), ist $e^{-ikx} \approx e^{-ikx_0}$ nahezu konstant in Bezug auf $x$, sodass

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{Gl. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

gilt. Der Integralterm ist konstant in Bezug auf $p$, sodass $\phi$ aufgrund des vorderen Terms $e^{-ipx_0/\hbar}$ im Impulsraum die Form einer Sinuswelle in Bezug auf $p$ annimmt, also über einen breiten Impulsbereich verteilt ist (<u>große Impulsunschärfe</u>).

#### Bei kleiner Impulsunschärfe
Ebenso, wenn $\phi$ im Impulsraum in einem sehr schmalen Bereich $[p_0-\delta, p_0+\delta]$ um einen Wert $p_0$ verteilt ist und außerhalb dieses Bereichs nahe Null ist (<u>kleine Impulsunschärfe</u>), ist $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ nahezu konstant in Bezug auf $p$, und mit $dk=\frac{1}{\hbar}dp$ erhalten wir

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

Aufgrund des vorderen Terms $e^{ip_0x/\hbar}$ nimmt $\Psi$ im Ortsraum die Form einer Sinuswelle in Bezug auf $x$ an, ist also über einen breiten Ortsbereich verteilt (<u>große Ortsunschärfe</u>).

#### Schlussfolgerung
Wenn die Ortsunschärfe abnimmt, nimmt die Impulsunschärfe zu, und umgekehrt. Daher ist es quantenmechanisch unmöglich, Ort und Impuls eines freien Teilchens gleichzeitig genau zu kennen.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Bildquelle*
> - Autor: Englischer Wikipedia-Benutzer [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - Lizenz: public domain

> Tatsächlich gilt dies aufgrund der Unschärferelation (uncertainty principle) nicht nur für freie Teilchen, sondern in allen Fällen. Die Unschärferelation wird in einem späteren Beitrag ausführlicher behandelt.
{: .prompt-info }

### Gruppengeschwindigkeit des Wellenpakets
Wenn wir die allgemeine Lösung in Gleichung ($\ref{eqn:Psi_general_solution}$) wie in Gleichung ($\ref{eqn:phase_velocity}$) mit $\omega \equiv \cfrac{\hbar k^2}{2m}$ umschreiben, erhalten wir

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> Eine Gleichung, die $\omega$ als Funktion von $k$ darstellt, wie $\omega = \cfrac{\hbar k^2}{2m}$, wird als **Dispersionsrelation** bezeichnet. Der folgende Inhalt gilt allgemein für alle Wellenpakete, unabhängig von der Dispersionsrelation.
{: .prompt-info }

Nehmen wir nun an, dass $\phi(k)$ eine sehr scharfe Form in der Nähe eines geeigneten Wertes $k_0$ hat. (Es wäre in Ordnung, wenn es über $k$ breit verteilt wäre, aber solche Wellenpakete verzerren sich sehr schnell und ändern ihre Form. Da die Komponenten für verschiedene $k$ sich mit unterschiedlichen Geschwindigkeiten bewegen, verlieren sie die Bedeutung einer gut definierten 'Gruppe' mit einer Geschwindigkeit. Das heißt, <u>die Impulsunschärfe wird größer.</u>)  
Die zu integrierende Funktion kann außerhalb der Umgebung von $k_0$ vernachlässigt werden, sodass wir die Funktion $\omega(k)$ in der Nähe dieses Punktes in eine Taylor-Reihe entwickeln können. Wenn wir nur den linearen Term berücksichtigen, erhalten wir

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Wenn wir nun $s=k-k_0$ substituieren und um $k_0$ integrieren, erhalten wir

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

Der vordere Term $e^{i(k_0x-\omega_0t)}$ repräsentiert eine Sinuswelle ('Kräuselung'), die sich mit der Geschwindigkeit $\omega_0/k_0$ bewegt, und der Integralterm ('Einhüllende'), der die Amplitude dieser Sinuswelle bestimmt, bewegt sich aufgrund des $e^{is(x-\omega_0^\prime t)}$ Terms mit der Geschwindigkeit $\omega_0^\prime$. Daher ist die Phasengeschwindigkeit bei $k=k_0$

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

was den Wert aus Gleichung ($\ref{eqn:phase_velocity}$) bestätigt, und die Gruppengeschwindigkeit ist

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

was dem Doppelten der Phasengeschwindigkeit entspricht.

## Vergleich mit der klassischen Mechanik

Da wir wissen, dass die klassische Mechanik auf makroskopischer Ebene gilt, sollten die durch die Quantenmechanik erhaltenen Ergebnisse die Berechnungsergebnisse der klassischen Mechanik annähern, wenn die quantenmechanische Unschärfe ausreichend klein ist. Im Fall des freien Teilchens, das wir gerade betrachten, sollte die Gruppengeschwindigkeit $v_\text{group}$, die in der Quantenmechanik der Geschwindigkeit des Teilchens entspricht, für denselben $k$-Wert und die entsprechende Energie $E$ gleich der in der klassischen Mechanik berechneten Geschwindigkeit $v_\text{classical}$ des Teilchens sein, wenn $\phi(k)$, wie zuvor angenommen, eine sehr scharfe Form in der Nähe eines geeigneten Wertes $k_0$ hat (d.h. wenn die <u>Impulsunschärfe ausreichend klein ist</u>).

Wenn wir $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ aus Gleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) in die gerade berechnete Gruppengeschwindigkeit (Gleichung [$\ref{eqn:group_velocity}$]) einsetzen, erhalten wir

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

und die Geschwindigkeit eines freien Teilchens mit der kinetischen Energie $E$ in der klassischen Mechanik ist ebenso

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Da $v_\text{quantum}=v_\text{classical}$, können wir bestätigen, dass das durch Anwendung der Quantenmechanik erhaltene Ergebnis eine physikalisch plausible Lösung ist.
