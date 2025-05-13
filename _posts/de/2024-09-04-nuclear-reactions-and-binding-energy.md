---
title: Kernreaktionen und Bindungsenergie
description: Wir betrachten die Ausdrücke für Kernreaktionen, die Definition des Q-Werts
  (Q-value), sowie die Konzepte des Massendefekts (mass defect) und der Bindungsenergie
  (binding energy).
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Kernreaktion (Nuclear Reaction)
### Grundlegende Gesetze in Kernreaktionen
*Kernreaktion (nuclear reaction)*: Eine Reaktion, bei der zwei verschiedene Atomkerne oder ein Atomkern und ein Nukleon kollidieren und zwei oder mehr neue Kernpartikel oder Gammastrahlen erzeugen.

Wenn zwei Atomkerne $a$ und $b$ reagieren und Atomkerne oder Gammastrahlen $c$ und $d$ als Produkte erzeugen, wird diese Reaktion wie folgt dargestellt:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

In Kernreaktionen gelten die folgenden vier grundlegenden Gesetze:

- *Erhaltung der Nukleonenzahl (conservation of nucleon)*: Die Gesamtzahl der Nukleonen bleibt vor und nach der Reaktion gleich. Die Art der Nukleonen kann sich ändern, daher werden Protonen und Neutronen nicht einzeln erhalten.
- *Erhaltung der Ladung (conservation of charge)*: Die Summe der Ladungen der Teilchen bleibt vor und nach der Reaktion gleich.
- *Impulserhaltung (conservation of momentum)*: Die Summe der Impulse der Teilchen bleibt vor und nach der Reaktion gleich.
- *Energieerhaltung (conservation of energy)*: Die Gesamtenergie, <u>einschließlich der Ruhemassenenergie</u>, bleibt vor und nach der Reaktion gleich.

### Exotherme Reaktion (exothermic reaction) & Endotherme Reaktion (endothermic reaction)
In der Kernreaktion der Gleichung ($\ref{nuclear_reaction}$) ist die Gesamtenergie vor der Reaktion die Summe der Ruhemassenenergie und der kinetischen Energie von $a$ und $b$, und die Gesamtenergie nach der Reaktion ist die Summe der Ruhemassenenergie und der kinetischen Energie von $c$ und $d$. Daher gilt nach dem Energieerhaltungssatz:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Diese Gleichung lässt sich umformen zu:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Das heißt, der Unterschied in der kinetischen Energie vor und nach der Kernreaktion entspricht dem Unterschied in der Ruhemasse vor und nach der Reaktion.
Die rechte Seite der letzten Gleichung wird als *Q-Wert (Q-value)* der Kernreaktion bezeichnet und wie folgt definiert:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Der Q-Wert wird immer in MeV angegeben, und da die Ruhemassenenergie für 1 amu normalerweise 931 MeV beträgt, kann der Q-Wert auch wie folgt geschrieben werden:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Exotherme Reaktion (exothermic reaction)*: Kernreaktion mit $Q>0$, ein Teil der Masse wird in kinetische Energie umgewandelt, was zu einer Zunahme der kinetischen Energie nach der Reaktion führt
- *Endotherme Reaktion (endothermic reaction)*: Kernreaktion mit $Q<0$, ein Teil der kinetischen Energie wird in Masse umgewandelt, was zu einer Abnahme der kinetischen Energie nach der Reaktion führt

| Art der <br>Kernreaktion | Q-Wert | Massenänderung vor <br>und nach der Reaktion | Änderung der kinetischen <br>Energie vor und nach <br>der Reaktion |
| :---: | :---: | :---: | :---: |
| Exotherme <br>Reaktion | $Q>0$ | $\Delta m<0$ (Abnahme) | $\Delta E>0$ (Zunahme) |
| Endotherme <br>Reaktion | $Q<0$ | $\Delta m>0$ (Zunahme) | $\Delta E<0$ (Abnahme) |

### Kurzschreibweise für Kernreaktionen
Die Kernreaktion in Gleichung ($\ref{nuclear_reaction}$) kann wie folgt kurz dargestellt werden:

$$ a(b, c)d $$

Dies bedeutet eine Kernreaktion, bei der $b$ auf $a$ trifft, $c$ emittiert wird und $a$ in $d$ umgewandelt wird.

#### Beispiele:
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Bindungsenergie (Binding Energy)
### Massendefekt (Mass Defect)
Die Masse jedes Kerns ist etwas geringer als die Summe der Massen der Neutronen und Protonen, aus denen er besteht. Diese Differenz wird als *Massendefekt (mass defect)* bezeichnet.

Wenn die Masse eines Kerns $M_A$ ist, kann der Massendefekt $\Delta$ eines beliebigen Kerns wie folgt berechnet werden:

$$ \Delta = ZM_p + NM_n - M_A. $$

Wenn der Massendefekt $\Delta$ in Energieeinheiten ausgedrückt wird, entspricht er der Energie, die benötigt wird, um einen beliebigen Kern in seine Bestandteile zu zerlegen. Da es sich um die Energie handelt, die die Nukleonen zusammenhält, wird sie als *Bindungsenergie (binding energy)* bezeichnet. Umgekehrt, wenn ein Atomkern aus A Nukleonen gebildet wird, sinkt das Energieniveau um die Bindungsenergie $\Delta$, sodass während des Kernreaktionsprozesses diese Energiemenge an die Umgebung abgegeben wird.

### Durchschnittliche Bindungsenergie pro Nukleon
Die Gesamtbindungsenergie eines Atomkerns nimmt mit zunehmender Massenzahl $A$ zu, aber die Steigung ist nicht konstant.  
![die durchschnittliche Bindungsenergie pro Nukleon für eine unterschiedliche Anzahl von Neutronen](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
Wie im obigen Bild zu sehen ist, steigt die durchschnittliche Bindungsenergie pro Nukleon $\Delta/A$ bei niedrigen Massenzahlen steil an, nimmt aber bei schweren Atomkernen mit $A\geq56$ mit einer sanften Steigung ab.

### Beziehung zwischen Q-Wert der Kernreaktion und Bindungsenergie
In der Kernreaktion der Gleichung ($\ref{nuclear_reaction}$) ist die Bindungsenergie des Kerns $a$

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

und die Masse von $a$ ist

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Auf die gleiche Weise gilt für die Kerne $b$, $c$ und $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Wenn wir annehmen, dass

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

und diese Gleichungen in Gleichung ($\ref{Q_value}$) einsetzen, erhalten wir

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Dies bedeutet, dass immer dann, wenn durch einen Kernreaktionsprozess zwei weniger stabile Kerne zu einem stabileren Kern verschmelzen, Energie freigesetzt wird.

### Kernfusion (Nuclear Fusion) und Kernspaltung (Nuclear Fission)
Im Fall einer Kernreaktion, bei der Deuterium mit einer Bindungsenergie von $2,23\text{MeV}$ und Tritium mit einer Bindungsenergie von $8,48\text{MeV}$ zu $^4\text{He}$ mit einer Bindungsenergie von $28,3\text{MeV}$ verschmelzen und ein Neutron freisetzen:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

wird die Energiedifferenz von $28,3-(2,23+8,48)=17,6\text{MeV}$ (entspricht $3,52\text{MeV}$ pro Nukleon) in Form von kinetischer Energie des Heliumkerns und des Neutrons freigesetzt.

Eine Reaktion wie in Gleichung ($\ref{nuclear_fusion}$), bei der zwei leichte Atomkerne mit kleiner Massenzahl zu einem schwereren Atomkern mit größerer Massenzahl als vor der Reaktion verschmelzen, wird als *Kernfusion (nuclear fusion)* bezeichnet. Dies ist die Energiequelle der Sonne und aller anderen Sterne, und eines Tages wird die Menschheit sie möglicherweise direkt als Energiequelle nutzen können.

Andererseits, bei einer Kernreaktion, in der $^{235}\text{U}$ mit einer Bindungsenergie von etwa $1780\text{MeV}$ ein Neutron absorbiert und dann in $^{92}\text{Kr}$ mit einer Bindungsenergie von $783\text{MeV}$ und $^{141}\text{Ba}$ mit etwa $1170\text{MeV}$ zerfällt und dabei 3 Neutronen freisetzt:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

wird eine Energie von $783+1170-1780=173\text{MeV}$ freigesetzt, was $0,733\text{MeV}$ pro Nukleon entspricht.

Eine Reaktion wie in Gleichung ($\ref{nuclear_fission}$), bei der ein schwerer Atomkern in leichtere Atomkerne zerfällt, wird als *Kernspaltung (nuclear fission)* bezeichnet. Seit der Rede "Atome für den Frieden" (Atoms for Peace) des 34. US-Präsidenten Eisenhower und dem Kernkraftwerk Obninsk in der Sowjetunion wird sie weithin als Energiequelle genutzt.
