---
title: Kernreaktionen und Bindungsenergie
description: Wir betrachten die Ausdrücke für Kernreaktionen, die Definition des Q-Werts, sowie die Konzepte des Massendefekts und der Bindungsenergie.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Kernreaktion (Nuclear Reaction)
### Grundlegende Gesetze bei Kernreaktionen
*Kernreaktion (nuclear reaction)*: Eine Reaktion, bei der zwei verschiedene Atomkerne oder ein Atomkern und ein Nukleon kollidieren und dabei zwei oder mehr neue Kernpartikel oder Gammastrahlung erzeugen

Wenn zwei Atomkerne $a$ und $b$ reagieren und dabei die Produkte $c$ und $d$ (Atomkerne oder Gammastrahlung) entstehen, wird diese Reaktion wie folgt dargestellt:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

Bei Kernreaktionen gelten die folgenden vier Grundgesetze:

- *Erhaltung der Nukleonenzahl (conservation of nucleon)*: Die Gesamtzahl der Nukleonen bleibt vor und nach der Reaktion gleich. Die Art der Nukleonen kann sich ändern, daher werden Protonen und Neutronen nicht einzeln erhalten.
- *Erhaltung der Ladung (conservation of charge)*: Die Summe der Ladungen aller Teilchen bleibt vor und nach der Reaktion gleich.
- *Erhaltung des Impulses (conservation of momentum)*: Die Summe der Impulse aller Teilchen bleibt vor und nach der Reaktion gleich.
- *Erhaltung der Energie (conservation of energy)*: Die Gesamtenergie <u>einschließlich der Ruhemassenenergie</u> bleibt vor und nach der Reaktion gleich.

### Exotherme Reaktion (exothermic reaction) & Endotherme Reaktion (endothermic reaction)
Bei der Kernreaktion in Gleichung ($\ref{nuclear_reaction}$) ist die Gesamtenergie vor der Reaktion die Summe aus der Ruhemassenenergie und der kinetischen Energie von $a$ und $b$, und die Gesamtenergie nach der Reaktion ist die Summe aus der Ruhemassenenergie und der kinetischen Energie von $c$ und $d$. Nach dem Energieerhaltungssatz gilt daher:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Diese Gleichung lässt sich umformen zu:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Das bedeutet, dass der Unterschied der kinetischen Energie vor und nach der Kernreaktion gleich dem Unterschied der Ruhemasse ist.
Die rechte Seite der letzten Gleichung wird als *Q-Wert (Q-value)* der Kernreaktion bezeichnet und wie folgt definiert:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Der Q-Wert wird immer in MeV angegeben. Da die Ruhemassenenergie von 1 amu typischerweise 931 MeV beträgt, kann der Q-Wert auch wie folgt geschrieben werden:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Exotherme Reaktion (exothermic reaction)*: Kernreaktion mit $Q>0$, ein Teil der Masse wird in kinetische Energie umgewandelt, wodurch die kinetische Energie nach der Reaktion zunimmt
- *Endotherme Reaktion (endothermic reaction)*: Kernreaktion mit $Q<0$, ein Teil der kinetischen Energie wird in Masse umgewandelt, wodurch die kinetische Energie nach der Reaktion abnimmt

| Reaktionstyp | Q-Wert | Massenänderung <br>vor/nach Reaktion | Änderung der kinetischen <br>Energie vor/nach Reaktion |
| :---: | :---: | :---: | :---: |
| Exotherme Reaktion | $Q>0$ | $\Delta m<0$ (Abnahme) | $\Delta E>0$ (Zunahme) |
| Endotherme Reaktion | $Q<0$ | $\Delta m>0$ (Zunahme) | $\Delta E<0$ (Abnahme) |

### Kurzschreibweise für Kernreaktionen
Die Kernreaktion in Gleichung ($\ref{nuclear_reaction}$) kann wie folgt abgekürzt werden:

$$ a(b, c)d $$

Dies bedeutet, dass $b$ auf $a$ trifft, $c$ emittiert wird und $d$ als Ergebnis entsteht.

#### Beispiele:
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Bindungsenergie (Binding Energy)
### Massendefekt (Mass Defect)
Die Masse eines Atomkerns ist immer etwas geringer als die Summe der Massen der Neutronen und Protonen, aus denen er besteht. Diese Differenz wird als *Massendefekt (mass defect)* bezeichnet.

Wenn die Masse eines Kerns mit $M_A$ bezeichnet wird, kann der Massendefekt $\Delta$ eines beliebigen Kerns wie folgt berechnet werden:

$$ \Delta = ZM_p + NM_n - M_A. $$

Wenn der Massendefekt $\Delta$ in Energieeinheiten ausgedrückt wird, entspricht er der Energie, die benötigt wird, um einen Kern in seine Bestandteile zu zerlegen. Da diese Energie die Nukleonen zusammenhält, wird sie als *Bindungsenergie (binding energy)* bezeichnet. Umgekehrt wird bei der Bildung eines Atomkerns aus A Nukleonen die Bindungsenergie $\Delta$ als Energieniveau gesenkt, wodurch während des Kernreaktionsprozesses entsprechend Energie an die Umgebung abgegeben wird.

### Durchschnittliche Bindungsenergie pro Nukleon
Die Gesamtbindungsenergie eines Atomkerns nimmt mit steigender Massenzahl $A$ zu, jedoch nicht mit konstanter Steigung.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
Wie im obigen Bild zu sehen ist, steigt die durchschnittliche Bindungsenergie pro Nukleon $\Delta/A$ bei niedrigen Massenzahlen steil an, nimmt aber bei schweren Atomkernen mit $A\geq56$ mit einer flacheren Steigung ab.

### Beziehung zwischen Q-Wert und Bindungsenergie
Bei der Kernreaktion in Gleichung ($\ref{nuclear_reaction}$) ist die Bindungsenergie des Kerns $a$:

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

und die Masse von $a$ ist:

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Auf die gleiche Weise gilt für die Kerne $b$, $c$ und $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Unter der Annahme, dass

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

und durch Einsetzen der obigen Gleichungen in Gleichung ($\ref{Q_value}$) erhalten wir:

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Dies bedeutet, dass bei einem Kernreaktionsprozess, bei dem zwei weniger stabile Kerne zu einem stabileren Kern verschmelzen, immer Energie freigesetzt wird.

### Kernfusion (Nuclear Fusion) und Kernspaltung (Nuclear Fission)
Bei einer Kernreaktion, bei der Deuterium mit einer Bindungsenergie von $2,23\text{MeV}$ und Tritium mit einer Bindungsenergie von $8,48\text{MeV}$ zu $^4\text{He}$ mit einer Bindungsenergie von $28,3\text{MeV}$ verschmelzen und ein Neutron freisetzen:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

wird die Differenz der Bindungsenergien vor und nach der Reaktion, also $28,3-(2,23+8,48)=17,6\text{MeV}$ (oder $3,52\text{MeV}$ pro Nukleon), in Form von kinetischer Energie des Heliumkerns und des Neutrons freigesetzt.

Reaktionen wie in Gleichung ($\ref{nuclear_fusion}$), bei denen zwei leichte Atomkerne mit kleiner Massenzahl zu einem schwereren Atomkern mit größerer Massenzahl verschmelzen, werden als *Kernfusion (nuclear fusion)* bezeichnet. Dies ist die Energiequelle der Sonne und aller anderen Sterne, und eines Tages wird die Menschheit diese direkt als Energiequelle nutzen können.

Andererseits gibt es Reaktionen wie die, bei der $^{235}\text{U}$ mit einer Bindungsenergie von etwa $1780\text{MeV}$ ein Neutron absorbiert und dann in $^{92}\text{Kr}$ mit einer Bindungsenergie von $783\text{MeV}$ und $^{141}\text{Ba}$ mit etwa $1170\text{MeV}$ zerfällt, wobei 3 Neutronen freigesetzt werden:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

Hierbei wird die Differenz der Bindungsenergien vor und nach der Reaktion, also $783+1170-1780=173\text{MeV}$ (oder $0,733\text{MeV}$ pro Nukleon), freigesetzt.

Reaktionen wie in Gleichung ($\ref{nuclear_fission}$), bei denen ein schwerer Atomkern in leichtere Atomkerne zerfällt, werden als *Kernspaltung (nuclear fission)* bezeichnet. Seit der Rede "Atoms for Peace" des 34. US-Präsidenten Eisenhower und dem sowjetischen Kernkraftwerk Obninsk wird diese Technologie weithin als Energiequelle genutzt.

## Magische Zahlen
Wenn die Anzahl der Neutronen oder Protonen in einem Kern 2, 6, 8, 14, 20, 28, 50, 82 oder 126 beträgt, neigt dieser Kern dazu, besonders stabil zu sein. Diese Nukleonenzahlen werden als *magische Zahlen (magic number)* bezeichnet. Diese Zahlen entsprechen der Anzahl von Neutronen und Protonen, die benötigt werden, um die Nukleonenschalen im Kern zu füllen, ähnlich wie bei den Elektronenschalen außerhalb des Atoms.

Isotope mit magischen Zahlen finden praktische Anwendungen in der Kerntechnik. Ein bekanntes Beispiel ist Zirkonium-90 ($^{90}_{40} \mathrm{Zr}$) mit 50 Neutronen, das aufgrund seiner Stabilität und geringen Neutronenabsorption häufig als Hüllmaterial für Brennstäbe in Reaktorkernen verwendet wird.
