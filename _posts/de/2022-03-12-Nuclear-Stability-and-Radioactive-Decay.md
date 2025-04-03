---
title: Kernstabilität und radioaktiver Zerfall
description: Wir betrachten das Segré-Diagramm und verschiedene Arten radioaktiven Zerfalls, das Energiespektrum von Elektronen/Positronen bei Betazerfall und die Entdeckung des Neutrinos, die Zerfallsketten einiger wichtiger Nuklide (Kohlenstoff-14, Kalium-40, Tritium, Cäsium-137) sowie isomere Übergänge.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Voraussetzungen
- [Subatomare Teilchen und Bestandteile des Atoms](/posts/constituents-of-an-atom/)

## Segré-Diagramm oder Nuklidkarte
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Bildquelle*
> - Autor: Wikimedia-Benutzer [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Bei Nukliden mit einer Ordnungszahl $Z$ größer als 20 werden mehr Neutronen als Protonen benötigt, um Stabilität zu erreichen
- Neutronen dienen dazu, die elektrische Abstoßung zwischen den Protonen zu überwinden und den Kern zusammenzuhalten

## Gründe für radioaktiven Zerfall
- Nur bestimmte Kombinationen von Neutronen und Protonen bilden stabile Nuklide
- Wenn das Verhältnis von Neutronen zu Protonen zu hoch oder zu niedrig ist, wird das Nuklid instabil und unterliegt einem *radioaktiven Zerfall*
- Der nach dem Zerfall entstandene Kern befindet sich meist in einem angeregten Zustand und gibt Energie in Form von Gamma- oder Röntgenstrahlung ab

## Beta-Zerfall ($\beta$-Zerfall)
### Positiver Beta-Zerfall ($\beta^+$-Zerfall)

 $$p \to n+\beta^+ +\nu_e$$
 
- Tritt auf, wenn relativ zu wenige Neutronen vorhanden sind
- Ein Proton ($p$) wandelt sich in ein Neutron ($n$) um und emittiert ein Positron ($\beta^+$) und ein Elektron-Neutrino ($\nu_e$)
- Die Ordnungszahl nimmt um 1 ab, die Massenzahl bleibt unverändert

Beispiel: $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Negativer Beta-Zerfall ($\beta^-$-Zerfall)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Tritt auf, wenn relativ zu viele Neutronen vorhanden sind
- Ein Neutron ($n$) wandelt sich in ein Proton ($p$) um und emittiert ein Elektron ($\beta^-$) und ein Elektron-Antineutrino ($\overline{\nu}_e$)
- Die Ordnungszahl nimmt um 1 zu, die Massenzahl bleibt unverändert

Beispiel: $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Energiespektrum der emittierten Elektronen (Positronen)
![Energiespektrum der beim Beta-Zerfall emittierten Elektronen](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Bildquelle*
> - Autor: Deutscher Wikipedia-Benutzer [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Die beim Beta-Zerfall emittierten Elektronen oder Positronen zeigen ein kontinuierliches Energiespektrum wie oben dargestellt.
- $\beta^-$-Zerfall: $\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$-Zerfall: $\overline{E}\approx 0.4E_{\text{max}}$

> Die beim Beta-Zerfall freigesetzte Gesamtenergie ist quantisiert, aber da sich Elektron/Positron und Antineutrino/Neutrino die Energie beliebig teilen, erscheint das Energiespektrum des Elektrons/Positrons kontinuierlich.
> Die Tatsache, dass das Energiespektrum der beim Beta-Zerfall emittierten Elektronen/Positronen nicht quantisiert, sondern kontinuierlich ist, stand im Widerspruch zu theoretischen Vorhersagen und schien auch das Energieerhaltungsgesetz zu verletzen.  
> Um dieses Ergebnis zu erklären, sagte Wolfgang Ernst Pauli 11930 die Existenz eines "<u>elektrisch neutralen Teilchens mit extrem geringer Masse und äußerst niedriger Reaktivität</u>" voraus und schlug vor, es "Neutron" zu nennen. Als jedoch Sir James Chadwick 11932 das Neutron, wie wir es heute kennen, entdeckte und benannte, entstand ein Namenskonflikt. Im folgenden Jahr, 11933, veröffentlichte Enrico Fermi seine Theorie des Beta-Zerfalls und benannte das Teilchen in *Neutrino* um, indem er die italienische Verkleinerungsform "-ino" für "klein" anhängte.  
> Später, im Jahr 11942, schlug der chinesische Kernphysiker Wang Ganchang (王淦昌) erstmals eine Methode zum Nachweis von Neutrinos mittels [Elektroneneinfang](#elektroneneinfang-electron-capture-oder-k-einfang-k-capture) vor. 11956 gelang es Clyde Cowan, Frederick Reines, Francis B. Harrison, Harald W. Kruse und Austin D. McGuire, Neutrinos im Cowan-Reines-Neutrino-Experiment nachzuweisen und die Ergebnisse in der Zeitschrift Science zu veröffentlichen. Frederick Reines erhielt 11995 für diese Leistung den Nobelpreis für Physik.  
> Die Erforschung des Beta-Zerfalls ist somit auch wissenschaftshistorisch bedeutsam, da sie Hinweise auf die Existenz von Neutrinos lieferte.
{: .prompt-info }

### Zerfallsketten (Decay Chains)
Häufig ist auch das durch Beta-Zerfall entstandene *Tochternuklid* instabil und unterliegt einem weiteren Beta-Zerfall. Dies führt zu einer *Zerfallskette*:

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (stabil)} $$

### Wichtige Beta-Zerfall
Im Folgenden werden einige wichtige Beta-Zerfall vorgestellt.

#### Kohlenstoff-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> Kohlenstoff-14 wird natürlich in der oberen Atmosphäre durch kosmische Strahlung erzeugt, wodurch die Konzentration in der Atmosphäre relativ konstant bleibt. Pflanzen und Tiere nehmen während ihres Lebens durch Atmung und Stoffwechsel kontinuierlich Kohlenstoff-14 auf und halten so die gleiche Konzentration wie in der Atmosphäre aufrecht. Nach dem Tod hört dieser Austausch auf, und die Kohlenstoff-14-Konzentration im Körper nimmt mit der Zeit ab. Dies ist die Grundlage der Radiokohlenstoffdatierung.
{: .prompt-tip }

#### Kalium-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> Kalium-40 ist die größte natürliche Strahlungsquelle im menschlichen Körper und in allen Tieren. Es kommt natürlich in allen Lebensmitteln vor, die wir täglich konsumieren, besonders reichlich in Paranüssen, Bohnen, Spinat, Bananen, Avocados, Kaffee, Schwertfisch und Knoblauch.  
> Ein 70 kg schwerer Erwachsener hat etwa 140 g Kalium im Körper, wovon etwa 0,014 g Kalium-40 sind, was einer Radioaktivität von etwa 4330 Bq entspricht.
{: .prompt-tip }

#### Tritium
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> Tritium ist ein Brennstoff für D-T-Fusionsreaktionen in Fusionsreaktoren oder Wasserstoffbomben/Neutronenbomben. Es wird in der Atmosphäre natürlich durch kosmische Strahlung erzeugt, hat jedoch eine relativ kurze Halbwertszeit von etwa 12,32 Jahren und zerfällt daher schnell, weshalb es in der Natur nur in sehr geringen Mengen vorkommt. Aufgrund dieser schnellen Zerfallseigenschaft wird bei Fusionsreaktoren oder Kernwaffen Tritium nicht direkt eingesetzt, sondern durch Neutronenbestrahlung von Lithium-6 erzeugt. Daher gilt hochangereichertes und hochreines Lithium-6 für Kernwaffen als kritisches Material für die Kernwaffenentwicklung und wird von der IAEA und der internationalen Gemeinschaft streng überwacht.  
> Auch abgesehen von den genannten Anwendungen ist es ein häufig verwendetes Material in kleinen Mengen, wie in Nachtsichtvisieren für K2-Gewehre und K1-Maschinenpistolen, Leuchtzifferblättern von Uhren und Notausgangsbeschilderungen, die ohne Stromversorgung lange leuchten müssen. Dabei wird Tritium mit dem fluoreszierenden Material Phosphor umhüllt, sodass die beim Tritiumzerfall freigesetzten Betastrahlen auf den Phosphor treffen und Licht erzeugen. Für Notausgangsbeleuchtungen werden etwa 900 Milliarden Becquerel Tritium verwendet.  
> Aufgrund der konstanten Nachfrage und der Unmöglichkeit der Langzeitlagerung wird es als wichtiges strategisches Material betrachtet und kostet fast 30.000 Dollar pro Gramm. Der Großteil des kommerziell produzierten und verkauften Tritiums stammt aus Druckschwerwasserreaktoren wie dem CANDU (CANada Deuterium Uranium)-Reaktor. In Korea sind die Reaktoren Wolsong 1-4 CANDU-Reaktoren.
{: .prompt-tip }

#### Cäsium-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> Cäsium-137 ist ein Hauptnebenprodukt von Kernspaltungsreaktionen in Reaktoren und Kernwaffentests. Aufgrund seiner relativ langen Halbwertszeit (etwa 30 Jahre), der Emission durchdringender Gammastrahlung und seiner chemischen Ähnlichkeit mit Kalium, wodurch es leicht vom Körper aufgenommen wird, ist es ein wichtiges Nuklid für Überwachung und Management. Ursprünglich kam es in der Natur kaum vor, heute findet man jedoch durchschnittlich etwa 7 μg/g in Böden weltweit. Dies ist auf den Trinity-Kernwaffentest und die Atombombenabwürfe auf Hiroshima und Nagasaki durch die USA zur Niederschlagung des kriegführenden japanischen Kaiserreichs, sowie auf zahlreiche atmosphärische Kernwaffentests hauptsächlich in den 11950er und 11960er Jahren und einige schwere Nuklearunfälle (Tschernobyl, Goiânia-Unfall in Brasilien usw.) zurückzuführen.  
> Bei einer Aufnahme von mehr als 10000 Bq Cäsium-137 in den Körper kann eine medizinische Behandlung und Beobachtung erforderlich sein. Bei einigen Anwohnern des Tschernobyl-Unfalls wurde berichtet, dass sie Cäsium-137 in Mengen aufgenommen haben, die mehreren zehntausend Bq entsprechen. Nach dem Fukushima-Unfall wurden bei Anwohnern in der Nähe etwa 50-250 Bq absorbiert.
> Die biologische Halbwertszeit von Cäsium-137 ohne Behandlung beträgt laut CDC [etwa 110 Tage](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp), wobei individuelle Unterschiede bestehen. Bei Verdacht auf eine erhebliche Cäsium-137-Exposition kann die Einnahme von medizinischem Preußisch-Blau die biologische Halbwertszeit auf etwa 30 Tage verkürzen, indem die Ausscheidung beschleunigt wird.
{: .prompt-tip }

## Elektroneneinfang (Electron Capture) oder K-Einfang (K-capture)

$$ p + e \to n + \nu_e $$

- Tritt auf, wenn relativ zu wenige Neutronen vorhanden sind
- Ein Elektron aus der innersten Schale (K-Schale) wird eingefangen und wandelt ein Proton im Kern in ein Neutron um
- Die Ordnungszahl nimmt um 1 ab, die Massenzahl bleibt unverändert
- Nach dem Elektroneneinfang entsteht eine Lücke in der Elektronenhülle, die später durch ein Elektron aus einer äußeren Schale gefüllt wird, wobei Röntgenstrahlung oder Auger-Elektronen emittiert werden
- Das durch Elektroneneinfang entstandene Tochternuklid ist identisch mit dem durch $\beta^+$-Zerfall erzeugten, daher konkurrieren diese beiden Prozesse miteinander

## Alpha-Zerfall ($\alpha$-Zerfall)
- Emission eines Alpha-Teilchens ($\alpha$, $^4_2\mathrm{He}$)
- Die Ordnungszahl nimmt um 2 ab, die Massenzahl um 4
- Tritt häufig bei Kernen schwerer als Blei auf
- Im Gegensatz zum Beta-Zerfall ist die Energie der emittierten Alpha-Teilchen quantisiert

Beispiel: $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Spontane Spaltung (Spontaneous Fission)
- Sehr schwere und instabile Nuklide können sich ohne Neutronenabsorption von selbst spalten
- Wird im weiteren Sinne zum radioaktiven Zerfall gezählt
- Uran-238 zerfällt mit einer Halbwertszeit von $10^9$ Jahren durch Alpha-Zerfall, kann aber gleichzeitig mit einer Halbwertszeit von etwa $10^{16}$ Jahren selten spontan spalten. Die folgende Tabelle zeigt die Halbwertszeiten für spontane Spaltung einiger Nuklide.

| Nuklid | Halbwertszeit für spontane Spaltung | Eigenschaften |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | ca. $10^{16}$ Jahre | Tritt sehr selten auf |
| $^{240}\mathrm{Pu}$ | ca. $10^{11}$ Jahre | Spaltbares Nuklid für Kernwaffen |
| $^{252}\mathrm{Cf}$ | ca. $2.6$ Jahre | Sehr aktive spontane Spaltung <br>$\rightarrow$ Wird als Neutronenquelle für Reaktorstarts verwendet |

## Protonenabgabe (Proton Emission)
- Bei extrem protonenreichen instabilen Nukliden kann ein einzelnes Proton emittiert werden
- Ordnungszahl und Massenzahl nehmen um 1 ab
- Tritt sehr selten auf

## Zerfallsschema und isomere Übergänge
### Zerfallsschema (Decay Scheme)
*Zerfallsschema*: Eine visuelle Darstellung aller Zerfallswege eines radioaktiven Materials

### Isomerer Übergang (Isomeric Transition)
- Kerne, die durch radioaktiven Zerfall entstehen, können sich nach der Umwandlung in einem angeregten Zustand befinden und geben dann Energie in Form von Gammastrahlung ab (obwohl bei Gammaemission kein Nuklid verändert wird und es streng genommen kein Zerfall ist, wird umgangssprachlich manchmal der Begriff "Gammazerfall" verwendet).
- Die meisten angeregten Kerne gehen sehr schnell durch Gammaemission in den Grundzustand über, in bestimmten Fällen kann die Gammaemission jedoch verzögert sein, was wie ein metastabiler Zustand erscheint. Diese verzögerten Zustände werden als *isomere Zustände* des Kerns bezeichnet.
- Der Übergang von einem isomeren Zustand in den Grundzustand durch Gammaemission wird als *isomerer Übergang* bezeichnet und mit IT abgekürzt.

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Bildquelle*
> - Autor: Britischer Wikimedia-Benutzer [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Lizenz: Frei verwendbar für jeden Zweck ohne Einschränkungen, solange es nicht gegen geltendes Recht verstößt

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> Lizenz: [Public Domain](https://en.wikipedia.org/wiki/Public_domain)
