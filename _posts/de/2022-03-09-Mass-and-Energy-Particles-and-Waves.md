---
title: Masse und Energie, Teilchen und Wellen
description: Erforschung des Masse-Energie-Äquivalenzprinzips der Relativitätstheorie und Berechnung der Energie eines bewegten Elektrons unter Berücksichtigung relativistischer Effekte.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## Masse-Energie-Äquivalenzprinzip
Masse und Energie sind identisch und können ineinander umgewandelt werden.

$$ E=mc^2 $$

Hier ist $c$ die Lichtgeschwindigkeit $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Elektronenvolt (eV)
*Elektronenvolt (eV)*: Die kinetische Energie, die ein Elektron beim Durchlaufen einer Potentialdifferenz von 1V erhält

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Masse und Energie eines bewegten Objekts
Nach der Relativitätstheorie nimmt die Masse eines bewegten Objekts aus Sicht des Beobachters relativ zu. Die Gleichung für die Masse eines bewegten Objekts in Abhängigkeit von seiner Geschwindigkeit lautet:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: Ruhemasse, $v$: Geschwindigkeit

Die *Gesamtenergie (total energy)* eines Teilchens ist die Summe aus *Ruheenergie (rest-mass energy)* und *kinetischer Energie (kinetic energy)*:

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

Insbesondere für den Fall $v\ll c$ können wir $\cfrac{v^2}{c^2} = \epsilon$ setzen und durch Taylor-Entwicklung um $\epsilon = 0$ (also Maclaurin-Reihe) approximieren:

$$
\begin{align*}
E_{kinetic} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

Dies entspricht der Formel für die kinetische Energie in der klassischen Mechanik. Praktisch kann diese Näherung (d.h. Vernachlässigung relativistischer Effekte) für $v\leq 0.2c$ oder $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$ verwendet werden und liefert dennoch ausreichend genaue Ergebnisse.

### Elektron
Da die Ruheenergie des Elektrons $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$ beträgt, muss die relativistische Formel für die kinetische Energie angewendet werden, wenn die kinetische Energie des Elektrons $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$ überschreitet. In der Kerntechnik haben Elektronen häufig Energien über 10 keV, daher muss meist Gleichung (2) angewendet werden.

### Neutron
Die Ruheenergie des Neutrons beträgt etwa 1000 MeV, somit ist $0.02E_{rest}=20\text{MeV}$. Da in der Kerntechnik selten Neutronen mit kinetischen Energien über 20 MeV behandelt werden, wird für die Berechnung der kinetischen Energie von Neutronen normalerweise Gleichung (3) verwendet.

### Photon
Die Gleichungen (2) und (3) gelten nur für Teilchen mit einer Ruhemasse ungleich Null und können daher nicht auf Photonen angewendet werden, deren Ruhemasse Null ist. Die Gesamtenergie eines Photons wird mit folgender Gleichung berechnet:

$$ E = h\nu \tag{4} $$

$h$: Planck-Konstante ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: Frequenz der elektromagnetischen Welle

## Materiewellen
Alle Materie in der Natur ist sowohl Teilchen als auch Welle. Das bedeutet, dass alle Teilchen eine entsprechende Wellenlänge (*de-Broglie-Wellenlänge*) haben. Diese Wellenlänge $\lambda$ ist eine Funktion des Impulses $p$ und der Planck-Konstante $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Der Impuls $p$ wird wie folgt definiert:

$$ p = mv \tag{6} $$

### Ohne Berücksichtigung relativistischer Effekte (z.B. Neutronen)
Da die kinetische Energie $E=1/2 mv^2$ ist, kann Gleichung (6) als Funktion der Energie ausgedrückt werden:

$$ p=\sqrt{2mE} \tag{7} $$

Durch Einsetzen in Gleichung (5) erhalten wir für die Wellenlänge des Teilchens:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Diese Gleichung wird in der Kerntechnik zur Berechnung der de-Broglie-Wellenlänge von Neutronen verwendet. Mit der Ruhemasse des Neutrons ergibt sich:

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Hier wird $\lambda$ in cm und $E$ in eV (kinetische Energie des Neutrons) angegeben.

### Mit Berücksichtigung relativistischer Effekte (z.B. Elektronen)
Der Impuls $p$ wird direkt aus den relativistischen Gleichungen berechnet:

$$ p=\frac {1}{c} \sqrt{E^2_{total}-E^2_{rest}} \tag{10}$$

Damit ergibt sich für die de-Broglie-Wellenlänge:

$$ \lambda = \frac {hc}{\sqrt{E_{total}-E_{rest}}} \tag{11} $$

### Teilchen mit Ruhemasse Null (z.B. Photonen)
Für Teilchen mit Ruhemasse Null kann der Impuls nicht mit Gleichung (6) berechnet werden, sondern mit:

$$ p=\frac {E}{c} \tag{12} $$

Durch Einsetzen in Gleichung (5) erhalten wir:

$$ \lambda = \frac {hc}{E} \tag{13}$$

Nach Einsetzen der Werte für $h$ und $c$ ergibt sich die endgültige Gleichung für die Wellenlänge:

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

Hier wird $\lambda$ in m und $E$ in eV angegeben.
