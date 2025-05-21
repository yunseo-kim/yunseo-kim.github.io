---
title: Gravitationsfeld und Gravitationspotential
description: Wir betrachten die Definition des Gravitationsfeldvektors und des Gravitationspotentials nach Newtons Gravitationsgesetz und behandeln zwei wichtige Beispiele dazu: den Schalentheorem und die galaktische Rotationskurve.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Newtons Gravitationsgesetz: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Für kontinuierliche Massenverteilungen und Körper mit Ausdehnung: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: Massendichte am Punkt mit Ortsvektor $\mathbf{r^{\prime}}$ von einem beliebigen Ursprung aus
>   - $dv^{\prime}$: Volumenelement am Punkt mit Ortsvektor $\mathbf{r^{\prime}}$ von einem beliebigen Ursprung aus
> - **Gravitationsfeldvektor (gravitational field vector)**:
>   - Vektor, der die Kraft pro Masseneinheit darstellt, die ein Teilchen in einem von einer Masse $M$ erzeugten Feld erfährt
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - Hat die Dimension einer *Kraft pro Masseneinheit* oder einer *Beschleunigung*
> - **Gravitationspotential (gravitational potential)**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - Hat die Dimension von *Kraft pro Masseneinheit* $\times$ *Distanz* oder *Energie pro Masseneinheit*
>   - $\Phi = -G\cfrac{M}{r}$
>   - Beim Gravitationspotential sind nur relative Unterschiede bedeutsam, nicht absolute Werte
>   - Üblicherweise wird die Bedingung $\Phi \to 0$ für $r \to \infty$ willkürlich festgelegt, um Mehrdeutigkeiten zu beseitigen
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Gravitationspotential innerhalb und außerhalb einer Kugelschale (Schalentheorem)**
>   - Für $R>a$:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - Bei der Berechnung des Gravitationspotentials an einem Punkt außerhalb einer kugelsymmetrischen Massenverteilung kann der Körper als Punktmasse betrachtet werden
>   - Für $R<b$:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - Innerhalb einer kugelsymmetrischen Massenschale ist das Gravitationspotential ortsunabhängig konstant, und die wirkende Gravitationskraft ist $0$
>   - Für $b<R<a$: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## Gravitationsfeld
### Newtons Gravitationsgesetz
Newton hatte bereits vor 11666 HE das Gravitationsgesetz systematisiert und numerisch verifiziert. Dennoch dauerte es weitere 20 Jahre, bis er seine Ergebnisse 11687 HE in seinem Werk *Principia* veröffentlichte, da er seine Berechnungsmethode, bei der er die Erde und den Mond als ausdehnungslose Punktmassen betrachtete, nicht rechtfertigen konnte. Glücklicherweise können wir mit der [Infinitesimalrechnung, die Newton später selbst entwickelte, dieses Problem, das für Newton im 11600. Jahrhundert nicht einfach zu lösen war, viel leichter beweisen](#für-ra).

Nach Newtons Gravitationsgesetz (Newton's law of universal gravitation) *zieht jedes Massenteilchen jedes andere Teilchen im Universum an, wobei die Kraft proportional zum Produkt der beiden Massen und umgekehrt proportional zum Quadrat des Abstands zwischen ihnen ist*. Mathematisch ausgedrückt:

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Bildquelle*
> - Autor: Wikimedia-Nutzer [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - Lizenz: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

Der Einheitsvektor $\mathbf{e}_r$ zeigt von $M$ in Richtung $m$, und das negative Vorzeichen zeigt an, dass die Kraft anziehend ist. Das heißt, $m$ wird in Richtung $M$ gezogen.

### Cavendishs Experiment
Die experimentelle Bestätigung dieses Gesetzes und die Bestimmung des Wertes von $G$ erfolgte 11798 HE durch den britischen Physiker Henry Cavendish. Cavendishs Experiment verwendete eine Drehwaage, bestehend aus zwei kleinen Kugeln, die an den Enden eines leichten Stabs befestigt waren. Die beiden Kugeln wurden jeweils von zwei anderen, größeren Kugeln in ihrer Nähe angezogen. Der derzeit akzeptierte Wert für $G$ beträgt $6,673 \pm 0,010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> Obwohl $G$ eine der am längsten bekannten Fundamentalkonstanten ist, ist sie mit geringerer Präzision bekannt als die meisten anderen Fundamentalkonstanten wie $e$, $c$ oder $\hbar$. Auch heute noch gibt es viele Forschungsarbeiten, die darauf abzielen, den Wert von $G$ mit höherer Präzision zu bestimmen.
{: .prompt-tip }

### Für Körper mit Ausdehnung
Das Gesetz in Gleichung ($\ref{eqn:law_of_gravitation}$) gilt streng genommen nur für *Punktteilchen (point particles)*. Wenn eine oder beide Seiten Körper mit Ausdehnung sind, muss man zusätzlich annehmen, dass das Gravitationsfeld ein *lineares Feld (linear field)* ist, um die Kraft zu berechnen. Das heißt, die Gesamtgravitationskraft, die ein Teilchen der Masse $m$ von mehreren anderen Teilchen erfährt, kann durch Vektoraddition der einzelnen Kräfte berechnet werden. Für Körper mit kontinuierlicher Massenverteilung wird die Summe durch folgendes Integral ersetzt:

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: Massendichte am Punkt mit Ortsvektor $\mathbf{r^{\prime}}$ von einem beliebigen Ursprung aus
- $dv^{\prime}$: Volumenelement am Punkt mit Ortsvektor $\mathbf{r^{\prime}}$ von einem beliebigen Ursprung aus

Wenn sowohl der Körper mit Masse $M$ als auch der Körper mit Masse $m$ eine Ausdehnung haben, ist ein zweites Volumenintegral über $m$ erforderlich, um die Gesamtgravitationskraft zu berechnen.

### Gravitationsfeldvektor
Der **Gravitationsfeldvektor (gravitational field vector)** $\mathbf{g}$ wird definiert als die Kraft pro Masseneinheit, die ein Teilchen in einem von einer Masse $M$ erzeugten Feld erfährt:

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

oder

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

Hier variiert die Richtung von $\mathbf{e}_r$ mit $\mathbf{r^\prime}$.

Diese Größe $\mathbf{g}$ hat die Dimension einer *Kraft pro Masseneinheit* oder einer *Beschleunigung*. In der Nähe der Erdoberfläche entspricht der Betrag des Gravitationsfeldvektors $\mathbf{g}$ der **Gravitationsbeschleunigungskonstante (gravitational acceleration constant)** mit $\|\mathbf{g}\| \approx 9,80\mathrm{m/s^2}$.

## Gravitationspotential
### Definition
Der Gravitationsfeldvektor $\mathbf{g}$ variiert mit $1/r^2$ und erfüllt daher die Bedingung ($\nabla \times \mathbf{g} \equiv 0$), um als Gradient einer Skalarfunktion (Potential) dargestellt werden zu können. Daher können wir schreiben:

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

Hier wird $\Phi$ als **Gravitationspotential (gravitational potential)** bezeichnet und hat die Dimension von *Kraft pro Masseneinheit* $\times$ *Distanz* oder *Energie pro Masseneinheit*.

Da $\mathbf{g}$ nur vom Radius abhängt, hängt auch $\Phi$ nur von $r$ ab. Aus den Gleichungen ($\ref{eqn:g_vector}$) und ($\ref{eqn:gradient_phi}$) erhalten wir:

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

Durch Integration erhalten wir:

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

Da beim Gravitationspotential nur relative Unterschiede bedeutsam sind, nicht absolute Werte, kann die Integrationskonstante weggelassen werden. Üblicherweise wird die Bedingung $\Phi \to 0$ für $r \to \infty$ willkürlich festgelegt, um Mehrdeutigkeiten zu beseitigen, und Gleichung ($\ref{eqn:g_potential}$) erfüllt diese Bedingung.

Für kontinuierliche Massenverteilungen lautet das Gravitationspotential:

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Für Massen, die auf einer dünnen Schale verteilt sind:

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

Und für lineare Massenverteilungen mit Liniendichte $\rho_l$:

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Physikalische Bedeutung
Betrachten wir die Arbeit pro Masseneinheit $dW^\prime$, die geleistet wird, wenn sich ein Körper im Gravitationsfeld um $d\mathbf{r}$ bewegt:

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

In dieser Gleichung ist $\Phi$ eine Funktion nur der Ortskoordinaten, dargestellt als $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Daher ist die Arbeit pro Masseneinheit, die geleistet wird, wenn ein Körper im Gravitationsfeld von einem Punkt zu einem anderen bewegt wird, gleich der Differenz der Potentiale an diesen beiden Punkten.

Wenn wir das Gravitationspotential im Unendlichen als $0$ definieren, kann $\Phi$ an einem beliebigen Punkt als die Arbeit pro Masseneinheit interpretiert werden, die erforderlich ist, um den Körper vom Unendlichen zu diesem Punkt zu bewegen. Die potentielle Energie eines Körpers ist das Produkt seiner Masse und des Gravitationspotentials $\Phi$, also für die potentielle Energie $U$:

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

Daher ist die Gravitationskraft, die auf einen Körper wirkt, der negative Gradient seiner potentiellen Energie:

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Wenn ein Körper in einem Gravitationsfeld platziert wird, das von einer Masse erzeugt wird, entsteht immer eine potentielle Energie. Diese potentielle Energie befindet sich streng genommen im Feld selbst, wird aber konventionell als potentielle Energie des Körpers bezeichnet.

## Beispiel: Gravitationspotential innerhalb und außerhalb einer Kugelschale (Schalentheorem)
### Koordinateneinstellung & Darstellung des Gravitationspotentials als Integral
Berechnen wir das Gravitationspotential innerhalb und außerhalb einer homogenen Kugelschale mit innerem Radius $b$ und äußerem Radius $a$. Die Gravitation durch die Schale kann durch direkte Berechnung der Kraftkomponenten auf eine Einheitsmasse im Feld ermittelt werden, aber die Potentialmethode ist einfacher.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Berechnen wir das Potential am Punkt $P$ im Abstand $R$ vom Zentrum. Unter der Annahme einer homogenen Massenverteilung in der Schale gilt $\rho(r^\prime)=\rho$, und aufgrund der Symmetrie bezüglich des Azimutwinkels $\phi$ entlang der Linie, die das Zentrum der Kugel mit Punkt $P$ verbindet:

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

Nach dem Kosinussatz gilt:

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

Da $R$ konstant ist, erhalten wir durch Differenzieren dieser Gleichung nach $r^\prime$:

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

Einsetzen in Gleichung ($\ref{eqn:spherical_shell_1}$) ergibt:

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

Hier werden $r_\mathrm{max}$ und $r_\mathrm{min}$ durch die Position des Punktes $P$ bestimmt.

### Für $R>a$
$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

Die Masse $M$ der Kugelschale ist gegeben durch:

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

Somit lautet das Potential:

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> Vergleicht man das Gravitationspotential einer Punktmasse $M$ aus Gleichung ($\ref{eqn:g_potential}$) mit dem gerade erhaltenen Ergebnis ($\ref{eqn:spherical_shell_outside_2}$), stellt man fest, dass sie identisch sind. Dies bedeutet, dass bei der Berechnung des Gravitationspotentials an einem Punkt außerhalb einer kugelsymmetrischen Massenverteilung die gesamte Masse als im Zentrum konzentriert betrachtet werden kann. Die meisten kugelförmigen Himmelskörper wie die Erde oder der Mond fallen in diese Kategorie, da sie als Überlagerung unendlich vieler konzentrischer Kugelschalen mit unterschiedlichen Durchmessern betrachtet werden können, ähnlich einer [Matroschka](https://en.wikipedia.org/wiki/Matryoshka_doll). Dies [rechtfertigt die Annahme, Himmelskörper wie die Erde oder den Mond als ausdehnungslose Punktmassen zu behandeln](#newtons-gravitationsgesetz), wie zu Beginn dieses Artikels erwähnt.
{: .prompt-info }

### Für $R<b$
$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> Innerhalb einer kugelsymmetrischen Massenschale ist das Gravitationspotential ortsunabhängig konstant, und die wirkende Gravitationskraft ist $0$.
{: .prompt-info }

> Dies ist auch ein Hauptargument gegen eine der bekanntesten Pseudowissenschaften, die "Hohlerde-Theorie". Wenn die Erde, wie in der Hohlerde-Theorie behauptet, eine Kugelschale wäre und innen hohl, würde die Erdgravitation auf alle Objekte innerhalb dieser Höhlung nicht wirken. Angesichts der Masse und des Volumens der Erde kann es keine solche Höhlung geben, und selbst wenn es sie gäbe, würden Lebewesen dort nicht auf der Innenseite der Kugelschale leben, sondern wie in einer Raumstation schwerelos schweben.  
> [Mikroorganismen können zwar einige Kilometer tief im Untergrund leben](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), aber sicherlich nicht in der Form, wie sie in der Hohlerde-Theorie behauptet wird. Jules Vernes Roman "Reise zum Mittelpunkt der Erde" und der Film "Die Reise zum Mittelpunkt der Erde" sind zwar unterhaltsam, aber man sollte fiktionale Werke als solche genießen und nicht ernsthaft daran glauben.
{: .prompt-tip }

### Für $b<R<a$
$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Ergebnisse
Die zuvor berechneten Gravitationspotentiale $\Phi$ in den drei Bereichen und die entsprechenden Beträge des Gravitationsfeldvektors $\|\mathbf{g}\|$ als Funktion des Abstands $R$ sind in den folgenden Grafiken dargestellt:

![Gravitational Potential as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-gravitational-potential.png)
![Magnitude of the Field Vector as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-field-vector.png)
> - Python-Visualisierungscode: [yunseo-kim/physics-visualization Repository](https://github.com/yunseo-kim/physics-visualization/blob/main/src/shell_theorem.py)
> - Lizenz: [Siehe hier](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

Man kann erkennen, dass sowohl das Gravitationspotential als auch der Betrag des Gravitationsfeldvektors stetig sind. Wenn das Gravitationspotential an einem Punkt unstetig wäre, würde der Gradient des Potentials, also die Gravitationskraft, an diesem Punkt unendlich werden, was physikalisch nicht plausibel ist. Daher muss die Potentialfunktion an allen Punkten stetig sein. Die *Ableitung* des Gravitationsfeldvektors ist jedoch an der inneren und äußeren Oberfläche der Schale unstetig.

## Beispiel: Galaktische Rotationskurve
Astronomische Beobachtungen zeigen, dass in vielen Spiralgalaxien wie unserer Milchstraße oder der Andromeda-Galaxie, die um ihr Zentrum rotieren, die beobachtbare Masse hauptsächlich im Zentrum konzentriert ist. Die Orbitalgeschwindigkeiten der Massen in diesen Spiralgalaxien stimmen jedoch, wie im folgenden Diagramm zu sehen, nicht mit den theoretischen Vorhersagen basierend auf der beobachtbaren Massenverteilung überein und bleiben ab einem bestimmten Abstand nahezu konstant.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Bildquelle*
> - Autor: Wikipedia-Nutzer [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - Lizenz: Public Domain

![Rotation Curve of Spiral Galaxy M33](https://upload.wikimedia.org/wikipedia/commons/c/cd/Rotation_curve_of_spiral_galaxy_Messier_33_%28Triangulum%29.png)
> **Rotationskurve der Spiralgalaxie M33 (Dreiecksnebel)**
> - Autor: Wikimedia-Nutzer [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama)
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Wir wollen die theoretisch erwartete Orbitalgeschwindigkeit in Abhängigkeit vom Abstand für den Fall berechnen, dass die Galaxienmasse im Zentrum konzentriert ist, zeigen, dass diese Vorhersage nicht mit den Beobachtungen übereinstimmt, und nachweisen, dass die Masse $M(R)$ innerhalb des Radius $R$ proportional zu $R$ sein müsste, um die Beobachtungen zu erklären.

Zunächst berechnen wir die Orbitalgeschwindigkeit im Abstand $R$ für den Fall, dass die Galaxienmasse $M$ im Zentrum konzentriert ist:

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

In diesem Fall würde man eine Orbitalgeschwindigkeit erwarten, die mit $1/\sqrt{R}$ abnimmt, wie durch die gestrichelte Linie in den beiden obigen Grafiken dargestellt. Die Beobachtungen zeigen jedoch, dass die Orbitalgeschwindigkeit $v$ nahezu unabhängig vom Abstand $R$ ist, was nicht mit der Vorhersage übereinstimmt. Diese Beobachtung kann nur erklärt werden, wenn $M(R)\propto R$ gilt.

Wenn wir mit einer Proportionalitätskonstante $k$ annehmen, dass $M(R) = kR$, dann:

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(konstant)}. $$

Aus diesen Überlegungen schließen Astrophysiker, dass in vielen Galaxien unentdeckte "Dunkle Materie (dark matter)" existieren muss und dass diese dunkle Materie mehr als 90% der Masse des Universums ausmachen muss. Die genaue Natur der dunklen Materie ist jedoch noch nicht vollständig geklärt, und es gibt auch alternative Ansätze wie die Modifizierte Newtonsche Dynamik (Modified Newtonian Dynamics, MOND), die versuchen, die Beobachtungen ohne die Annahme dunkler Materie zu erklären, obwohl diese nicht zur Mainstream-Theorie gehören. Dieses Forschungsgebiet steht heute an der Spitze der Astrophysik.
