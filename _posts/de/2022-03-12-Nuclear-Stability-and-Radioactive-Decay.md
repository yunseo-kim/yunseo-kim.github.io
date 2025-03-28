---
title: Kernstabilität und radioaktiver Zerfall
description: Wir betrachten das Segré-Diagramm, Arten des radioaktiven Zerfalls und
  isomere Übergänge.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Segré-Diagramm oder Nuklidkarte
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Bildquelle*
> - Autor: Wikimedia-Benutzer [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Für Nuklide mit einer Ordnungszahl $Z$ größer als 20 sind mehr Neutronen als Protonen für die Stabilisierung erforderlich
- Neutronen spielen eine Rolle bei der Bindung des Kerns, indem sie die elektrische Abstoßung zwischen den Protonen überwinden

## Gründe für radioaktiven Zerfall
- Nur bestimmte Kombinationen von Neutronen und Protonen bilden stabile Nuklide
- Wenn das Verhältnis von Neutronen zu Protonen zu hoch oder zu niedrig ist, ist das Nuklid instabil und unterliegt dem *radioaktiven Zerfall*
- Der nach dem Zerfall gebildete Kern befindet sich meist in einem angeregten Zustand und gibt Energie in Form von Gamma- oder Röntgenstrahlung ab

## Beta-Zerfall ($\beta$-Zerfall)
### Positiver Beta-Zerfall ($\beta^+$-Zerfall)

 $$p \to n+\beta^+ +\nu_e$$
 
- Tritt auf, wenn relativ wenige Neutronen vorhanden sind
- Ein Proton ($p$) wird in ein Neutron ($n$) umgewandelt und ein Positron ($\beta^+$) sowie ein Elektron-Neutrino ($\nu_e$) werden emittiert
- Die Ordnungszahl nimmt um 1 ab, die Massenzahl bleibt unverändert

Beispiel: $^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### Negativer Beta-Zerfall ($\beta^-$-Zerfall)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Tritt auf, wenn relativ viele Neutronen vorhanden sind
- Ein Neutron ($n$) wird in ein Proton ($p$) umgewandelt und ein Elektron ($\beta^-$) sowie ein Elektron-Antineutrino ($\overline{\nu}_e$) werden emittiert
- Die Ordnungszahl nimmt um 1 zu, die Massenzahl bleibt unverändert

Beispiel: $^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### Energiespektrum der emittierten Elektronen (Positronen)
![Energiespektrum der beim Beta-Zerfall emittierten Elektronen](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Bildquelle*
> - Autor: Deutscher Wikipedia-Benutzer [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Die beim Beta-Zerfall emittierten Elektronen oder Positronen zeigen ein kontinuierliches Energiespektrum wie oben dargestellt.
- $\beta^-$-Zerfall: $\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$-Zerfall: $\overline{E}\approx 0.4E_{\text{max}}$

### Zerfallskette
Oft ist das durch Beta-Zerfall gebildete *Tochternuklid* ebenfalls instabil und unterliegt einem weiteren Beta-Zerfall. Dies führt zu einer *Zerfallskette* wie folgt:

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (stabil)} $$ 

## Elektroneneinfang oder K-Einfang

$$ p + e \to n + \nu_e $$

- Tritt auf, wenn relativ wenige Neutronen vorhanden sind
- Ein Elektron aus der innersten Schale (K-Schale) wird eingefangen und wandelt ein Proton im Kern in ein Neutron um
- Die Ordnungszahl nimmt um 1 ab, die Massenzahl bleibt unverändert
- Nach dem Elektroneneinfang entsteht eine Lücke in der Elektronenwolke, die später durch ein Elektron aus einer äußeren Schale gefüllt wird, wobei Röntgenstrahlung oder Auger-Elektronen emittiert werden
- Das durch Elektroneneinfang entstandene Tochternuklid ist identisch mit dem durch $\beta^+$-Zerfall entstandenen Kern, daher konkurrieren diese beiden Prozesse miteinander

## Alpha-Zerfall ($\alpha$-Zerfall)
- Emission eines Alpha-Teilchens ($\alpha$, $^4_2\text{He}$)
- Die Ordnungszahl nimmt um 2 ab und die Massenzahl um 4
- Tritt häufig bei Kernen schwerer als Blei auf
- Im Gegensatz zum Beta-Zerfall ist die Energie der emittierten Alpha-Teilchen quantisiert

Beispiel: $^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## Spontane Spaltung
- Sehr schwere und instabile Nuklide können sich ohne Neutronenabsorption selbst spalten
- Wird im weiteren Sinne zum radioaktiven Zerfall gezählt

## Protonenemission
- Bei extrem protonenreichen instabilen Nukliden kann ein einzelnes Proton emittiert werden
- Die Ordnungszahl und die Massenzahl nehmen um 1 ab
- Tritt sehr selten auf

## Zerfallsschema und isomerer Übergang
### Zerfallsschema
*Zerfallsschema*: Eine visuelle Darstellung aller Zerfallswege eines radioaktiven Materials

### Isomerer Übergang
- Kerne, die durch radioaktiven Zerfall gebildet werden, können nach der Umwandlung in einem angeregten Zustand verbleiben und Energie in Form von Gammastrahlung abgeben (obwohl die Emission von Gammastrahlung streng genommen kein Zerfall ist, da sich das Nuklid nicht ändert, wird der Begriff "Gammazerfall" manchmal umgangssprachlich verwendet).
- Die meisten angeregten Kerne geben sehr schnell Gammastrahlung ab und gehen in den Grundzustand über, aber in bestimmten Fällen kann die Emission von Gammastrahlung verzögert sein und wie ein metastabiler Zustand erscheinen. Dieser verzögerte Zustand wird als *isomerer Zustand* des Kerns bezeichnet.
- Der Übergang vom isomeren Zustand in den Grundzustand unter Emission von Gammastrahlung wird als *isomerer Übergang* bezeichnet und mit IT abgekürzt.
![Au-198 Zerfallsschema](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Bildquelle*
> - Autor: Britischer Wikimedia-Benutzer [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Lizenz: Frei zur Verwendung für jeden Zweck ohne Einschränkungen, sofern nicht gesetzlich verboten
