---
title: Homogene Mischungen und molekulare Wirkungsquerschnitte
description: Berechnen wir den makroskopischen Wirkungsquerschnitt einer homogenen
  Mischung aus zwei oder mehr Nukliden.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## Makroskopischer Wirkungsquerschnitt einer homogenen Mischung
Betrachten wir eine homogene Mischung aus zwei Nukliden $X$ und $Y$. Die Atomdichten der jeweiligen Nuklide seien $N_X$ und $N_Y$ $\text{Atom/cm}^3$, und die Wirkungsquerschnitte für eine bestimmte Reaktion mit Neutronen seien jeweils $\sigma_X$ und $\sigma_Y$. 

Die Wahrscheinlichkeit für ein Neutron, pro Längeneinheit mit den Atomkernen $X$ und $Y$ zu kollidieren, beträgt dann jeweils $\Sigma_X=N_X\sigma_X$ und $\Sigma_Y=N_Y\sigma_Y$ (siehe [Makroskopischer Wirkungsquerschnitt](/posts/Neutron-Interactions-and-Cross-sections/#makroskopischer-wirkungsquerschnitt-macroscopic-cross-section)). Die Gesamtwahrscheinlichkeit für ein Neutron, pro Längeneinheit mit diesen beiden Atomkernen zu reagieren, ist daher:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Äquivalenter Wirkungsquerschnitt eines Moleküls
Wenn die oben betrachteten Kerne in molekularer Form vorliegen, können wir den äquivalenten Wirkungsquerschnitt (equivalent cross-section) dieses Moleküls definieren, indem wir den mit Gleichung (1) berechneten makroskopischen Wirkungsquerschnitt der Mischung durch die Anzahl der Moleküle pro Volumeneinheit teilen.

Wenn $N$ Moleküle $X_mY_n$ pro Volumeneinheit vorhanden sind, dann gilt $N_X=mN$ und $N_Y=nN$, und wir können den Wirkungsquerschnitt dieses Moleküls aus Gleichung (1) wie folgt berechnen:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> Die Gleichungen (1) und (2) gelten unter der Annahme, dass die Kerne $X$ und $Y$ unabhängig voneinander mit Neutronen reagieren. Daher können sie nicht auf die elastische Streuung durch Moleküle und Festkörper angewendet werden.
> Die Streuquerschnitte von Molekülen und Festkörpern bei niedrigen Neutronenenergien müssen experimentell bestimmt werden.
{: .prompt-warning }
