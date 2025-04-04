---
title: Masse und Energie, Teilchen und Wellen
description: Erforschen Sie das Masse-Energie-Äquivalenzprinzip der Relativitätstheorie
  und berechnen Sie die Energie eines bewegten Elektrons unter Berücksichtigung relativistischer
  Effekte.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.png
---
## Masse-Energie-Äquivalenzprinzip
Masse und Energie sind identisch und können ineinander umgewandelt werden.

$$ E=mc^2 $$

Hier ist $c$ die Lichtgeschwindigkeit $2,9979 \times 10^{10}\ \text{cm/sec}$.

## Elektronenvolt (eV)
*Elektronenvolt (eV)*: Die kinetische Energie, die ein Elektron beim Durchlaufen einer Spannung von 1V gewinnt

$$
\begin{align*} 
1 \text{eV} &= 1,60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1,60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Masse und Energie bewegter Objekte
Nach der Relativitätstheorie nimmt die Masse eines bewegten Objekts aus Sicht des Beobachters relativ zu. Die Gleichung für die Geschwindigkeit und Masse eines bewegten Objekts ist wie folgt definiert:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: Ruhemasse, $v$: Geschwindigkeit

Die *Gesamtenergie* eines Teilchens ist die Summe aus *Ruheenergie* und *kinetischer Energie*, daher gilt:

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

Insbesondere für $v\ll c$ kann man mit dem binomischen Lehrsatz annähern:

$$
\begin{align*}
E_{kinetic} &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right]
\\ &= m_0c^2\left[\left(1+\frac{1}{2}v^2/c^2\right)-1\right]
\\ &= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

Dies entspricht der Formel für die kinetische Energie in der klassischen Mechanik. Praktisch kann diese Näherungsformel für $v\leq 0,2c$ oder $E_{\text{kinetic}} \leq 0,02E_{\text{rest}}$ verwendet werden (d.h. relativistische Effekte können vernachlässigt werden), um hinreichend genaue Werte zu erhalten.

### Elektron
Da die Ruheenergie des Elektrons $E_{\text{rest}}=m_ec^2=0,511 \text{MeV}$ beträgt, muss die relativistische Formel für die kinetische Energie angewendet werden, wenn die kinetische Energie des Elektrons $0,02\times 0,511 \text{MeV}=0,010 \text{MeV}=10 \text{keV}$ übersteigt. In der Kerntechnik haben Elektronen oft Energien über 10keV, daher muss meist Gleichung (2) angewendet werden.

### Neutron
Die Ruheenergie des Neutrons beträgt etwa 1000MeV, daher ist $0,02E_{rest}=20\text{MeV}$. In der Kerntechnik sind Situationen, in denen die kinetische Energie von Neutronen 20MeV übersteigt, selten, daher wird für die Berechnung der kinetischen Energie von Neutronen normalerweise Gleichung (3) verwendet.

### Photon
Gleichungen (2) und (3) gelten nur für Teilchen mit nicht-verschwindender Ruhemasse und können daher nicht auf Photonen angewendet werden, deren Ruhemasse Null ist. Die Gesamtenergie eines Photons wird mit folgender Gleichung berechnet:

$$ E = h\nu \tag{4} $$

$h$: Planck-Konstante ($4,316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: Frequenz der elektromagnetischen Welle

## Materiewellen
Alle Materie in der Natur ist sowohl Teilchen als auch Welle. Das heißt, alle Teilchen haben eine entsprechende Wellenlänge (*de-Broglie-Wellenlänge*). Die Wellenlänge $\lambda$ ist eine Funktion des Impulses $p$ und der Planck-Konstante $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Der Impuls $p$ ist wie folgt definiert:

$$ p = mv \tag{6} $$

### Vernachlässigung relativistischer Effekte (z.B. Neutronen)
Da die kinetische Energie $E=1/2 mv^2$ ist, kann Gleichung (6) als Funktion der Energie wie folgt ausgedrückt werden:

$$ p=\sqrt{2mE} \tag{7} $$

Setzt man dies in Gleichung (5) ein, erhält man für die Wellenlänge des Teilchens:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Diese Gleichung wird in der Kerntechnik verwendet, um die de-Broglie-Wellenlänge von Neutronen zu berechnen. Setzt man die Ruhemasse des Neutrons ein, erhält man:

$$ \lambda = \frac {2,860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Hier ist $\lambda$ in cm und $E$ ist die kinetische Energie des Neutrons in eV.

### Berücksichtigung relativistischer Effekte (z.B. Elektronen)
Man berechnet den Impuls $p$ direkt aus den obigen relativistischen Gleichungen:

$$ p=\frac {1}{c} \sqrt{E^2_{total}-E^2_{rest}} \tag{10}$$

Dann ergibt sich für die de-Broglie-Wellenlänge:

$$ \lambda = \frac {hc}{\sqrt{E_{total}-E_{rest}}} \tag{11} $$

### Teilchen mit Ruhemasse Null (z.B. Photonen)
Für Teilchen mit Ruhemasse Null kann der Impuls nicht mit Gleichung (6) berechnet werden, stattdessen verwendet man:

$$ p=\frac {E}{c} \tag{12} $$

Setzt man Gleichung (12) in Gleichung (5) ein, erhält man:

$$ \lambda = \frac {hc}{E} \tag{13}$$

Setzt man die Werte für $h$ und $c$ ein, ergibt sich schließlich für die Wellenlänge:

$$ \lambda = \frac {1,240 \times 10^{-6}}{E} \tag{14}$$

Hier ist $\lambda$ in m und $E$ in eV.
