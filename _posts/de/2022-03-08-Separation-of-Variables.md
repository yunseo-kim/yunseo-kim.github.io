---
title: Separationsansatz (Separation of Variables)
description: Wir untersuchen den Separationsansatz und stellen einige relevante Beispiele vor.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Separationsansatz (Separation of Variables)
**Separierbare Gleichung (separable equation)**: Eine Gleichung, die durch algebraische Manipulation in die Form $g(y)y'=f(x)$ gebracht werden kann.

Wenn wir beide Seiten einer separierbaren Gleichung $g(y)y'=f(x)$ in Bezug auf $x$ integrieren, erhalten wir

$$ \int g(y)y'dx = \int f(x)dx + c $$ 

und da $y'dx=dy$ ist, erhalten wir

$$ \int g(y)dy = \int f(x)dx + c $$

wodurch wir den Ausdruck in Bezug auf die Variable $x$ und den Ausdruck in Bezug auf $y$ jeweils auf die rechte und linke Seite trennen können. Wenn $f$ und $g$ stetige Funktionen sind, können wir diese Integrale berechnen, um die allgemeine Lösung der gegebenen Differentialgleichung zu erhalten. Diese Lösungsmethode wird **Separationsansatz (separation of variables)** genannt.

## Modellierungsbeispiel: Radiokohlenstoffdatierung (Radiocarbon Dating)
Ötzi ist eine neolithische Mumie, die [12991 HE](https://en.wikipedia.org/wiki/Holocene_calendar) in den Ötztaler Alpen entdeckt wurde. Wenn das Verhältnis von Kohlenstoff-14 zu Kohlenstoff-12 in dieser Mumie 52,5% des Verhältnisses in lebenden Organismen beträgt, wann ungefähr lebte und starb Ötzi?
> In der Atmosphäre und in lebenden Organismen ist das Verhältnis von radioaktivem Kohlenstoff-14 zu Kohlenstoff-12 konstant. Wenn ein Organismus stirbt, hört die Aufnahme von Kohlenstoff-14 durch Atmung und Nahrung auf, aber der Zerfall von Kohlenstoff-14 setzt sich fort, wodurch der Anteil des radioaktiven Kohlenstoffs abnimmt. Daher kann das Alter eines Fossils durch Vergleich des Anteils an radioaktivem Kohlenstoff mit dem in der Atmosphäre geschätzt werden. Die Halbwertszeit von Kohlenstoff-14 beträgt 5715 Jahre.
{: .prompt-info }

### Lösung
Wenn wir die gewöhnliche Differentialgleichung $y'=ky$ separieren und integrieren, erhalten wir

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Um die Konstante $k$ zu bestimmen, verwenden wir die Halbwertszeit $H=5715$.

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Schließlich setzen wir das Verhältnis von 52,5% ein, um die Zeit $t$ zu bestimmen, zu der Ötzi starb:

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{Geschätzter Tod vor etwa 5310 Jahren, um 6680 HE}. $$

## Modellierungsbeispiel: Mischungsproblem
Anfänglich enthält ein Tank 1000 L Wasser, in dem 10 kg Salz gelöst sind. Eine Salzlösung fließt mit einer Rate von 10 L pro Minute in den Tank, wobei diese Lösung 0,2 kg Salz pro Liter enthält. Die Mischung im Tank wird gut umgerührt und bleibt homogen, und diese Salzlösung fließt mit einer Rate von 10 L pro Minute aus dem Tank. Bestimmen Sie die Menge des Salzes $y(t)$ im Tank zur Zeit $t$.

### 1. Modellaufstellung

$$ y'=\text{Zuflussrate} - \text{Abflussrate}. $$

Die Zuflussrate des Salzes beträgt 2 kg pro Minute. Die Abflussrate der Salzlösung beträgt 0,01 des Gesamtvolumens der Salzlösung pro Minute, daher ist die Abflussrate des Salzes $0.01 y(t)$ pro Minute. Folglich ist das Modell die gewöhnliche Differentialgleichung

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Lösung des Modells
Die zuvor aufgestellte gewöhnliche Differentialgleichung ist separierbar. Separieren wir die Variablen, integrieren und wenden dann die Exponentialfunktion auf beide Seiten an.

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Anfänglich beträgt die Salzmenge im Tank 10 kg, daher ist die Anfangsbedingung $y(0)=10$. Wenn wir $y=10,\ t=0$ in die obige Gleichung einsetzen, erhalten wir $10-200=ce^0=c$, also $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Das bedeutet, dass die Salzmenge im Tank unter den gegebenen Bedingungen exponentiell gegen 200 kg konvergiert.

## Modellierungsbeispiel: Newtonsches Abkühlungsgesetz (Newton's Law of Cooling)
In einem Bürogebäude wird die Temperatur tagsüber im Winter bei 20°C gehalten. Die Heizung wird um 22 Uhr ausgeschaltet und um 6 Uhr morgens wieder eingeschaltet. An einem bestimmten Tag betrug die Innentemperatur des Gebäudes um 2 Uhr morgens 17,4°C. Die Außentemperatur betrug um 22 Uhr 10°C und fiel bis 6 Uhr morgens auf 4°C. Wie hoch war die Innentemperatur des Gebäudes um 6 Uhr morgens, als die Heizung wieder eingeschaltet wurde?
> **Newtonsches Abkühlungsgesetz (Newton's law of cooling)**  
> Die Änderungsrate der Temperatur T eines Objekts in Bezug auf die Zeit ist proportional zur Temperaturdifferenz zwischen dem Objekt und seiner Umgebung
{: .prompt-info }

### 1. Modellaufstellung
Sei $T(t)$ die Innentemperatur des Gebäudes und $T_A$ die Außentemperatur. Dann gilt nach dem Newtonschen Abkühlungsgesetz:

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Allgemeine Lösung
Da wir nur wissen, dass $T_A$ zwischen 10°C und 4°C variiert, aber nicht genau wissen, welchen Wert es annimmt, können wir die zuvor aufgestellte Gleichung nicht lösen. In solchen Fällen kann es hilfreich sein, *die Situation zu vereinfachen und eine einfachere Problemstellung zu versuchen*. Der Durchschnitt der beiden bekannten Werte beträgt 7°C, also nehmen wir an, dass die unbekannte Funktion $T_A$ eine Konstante $T_A=7$ ist. Auch wenn es nicht genau ist, können wir erwarten, eine Näherung für die gesuchte Innentemperatur $T$ um 6 Uhr morgens zu erhalten.

Für die Konstante $T_A=7$ ist die zuvor aufgestellte gewöhnliche Differentialgleichung separierbar. Durch Separation der Variablen, Integration und Anwendung der Exponentialfunktion erhalten wir die allgemeine Lösung:

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Spezielle Lösung
Wählen wir 22 Uhr als $t=0$, dann ist die gegebene Anfangsbedingung $T(0)=20$. Nennen wir die daraus resultierende spezielle Lösung $T_p$. Durch Einsetzen erhalten wir:

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Bestimmung von $k$
Um 2 Uhr morgens betrug die Innentemperatur des Gebäudes 17,4°C, also $T(4)=17.4$. Wenn wir den Wert von $k$ algebraisch bestimmen und in $T_p(t)$ einsetzen, erhalten wir:

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Antwort und Interpretation
6 Uhr morgens entspricht $t=8$, also:

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[°C]}. $$

## Modellierungsbeispiel: Torricellisches Gesetz (Torricelli's Theorem)
Ein Tank hat einen Durchmesser von 2 m und ein Loch mit einem Durchmesser von 1 cm. Die anfängliche Wasserhöhe beim Öffnen des Lochs beträgt 2,25 m. Bestimmen Sie die Wasserhöhe im Tank zu einem beliebigen Zeitpunkt und die Zeit, die benötigt wird, bis der Tank leer ist.
> **Torricellisches Gesetz (Torricelli's theorem)**  
> Die Geschwindigkeit des unter dem Einfluss der Schwerkraft austretenden Wassers ist:
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: Wasserhöhe über dem Loch zum Zeitpunkt $t$
> $g=980\text{cm/s²}$: Erdbeschleunigung an der Erdoberfläche
{: .prompt-info }

### 1. Modellaufstellung
Das Ausflusvolumen $\Delta V$ während einer kurzen Zeit $\Delta t$ ist:

$$ \Delta V = Av\Delta t \qquad (A: \text{Fläche des Lochs})$$

$\Delta V$ muss gleich der Änderung des Wasservolumens $\Delta V^*$ im Tank sein. Außerdem gilt:

$$ \Delta V^* = -B\Delta h \qquad (B: \text{Querschnittsfläche des Tanks}) $$

wobei $\Delta h(>0)$ die Abnahme der Wasserhöhe $h(t)$ ist. Wenn wir $\Delta V$ und $\Delta V^*$ gleichsetzen, erhalten wir:

$$ -B\Delta h = Av\Delta t $$

Wenn wir nun $v$ gemäß dem Torricellischen Gesetz ausdrücken und $\Delta t$ gegen 0 gehen lassen, erhalten wir das folgende Modell in Form einer gewöhnlichen Differentialgleichung erster Ordnung:

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Allgemeine Lösung
Diese gewöhnliche Differentialgleichung ist separierbar. Durch Separation der Variablen und Integration erhalten wir:

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Wenn wir beide Seiten durch 2 teilen und quadrieren, erhalten wir $h=(c-13.28At/B)^2$. Setzen wir $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$ ein, erhalten wir die allgemeine Lösung:

$$ h(t)=(c-0.000332t)^2 $$

### 3. Spezielle Lösung
Die Anfangsbedingung ist $h(0)=225\text{cm}$. Wenn wir $t=0$ und $h=225$ in die allgemeine Lösung einsetzen, erhalten wir $c^2=225, c=15.00$, und damit die spezielle Lösung:

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Zeit bis zur Entleerung des Tanks

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Umwandlung in separierbare Form (separable form)
In einigen Fällen können nicht separierbare gewöhnliche Differentialgleichungen durch die Einführung einer neuen unbekannten Funktion von $y$ in eine separierbare Form umgewandelt werden.

$$ y'=f\left(\frac {y}{x}\right). $$

Um eine solche gewöhnliche Differentialgleichung zu lösen, setzen wir $y/x=u$. Dann gilt:

$$ y=ux,\quad y'=u'x+u $$

Wenn wir dies in $y'=f(y/x)$ einsetzen, erhalten wir $u'x=f(u)-u$. Wenn $f(u)-u\neq0$, dann können wir die Gleichung separieren zu:

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$
