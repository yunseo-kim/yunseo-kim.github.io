---
title: "Homogene Mischungen und molekulare Querschnitte"
description: >-
  Berechnen wir den makroskopischen Querschnitt einer homogenen Mischung aus zwei oder mehr Nukliden.
categories: [Technische Physik, Kerntechnik]
tags: [Kernphysik, Wechselwirkung von Strahlung mit Materie]
math: true
---
## Makroskopischer Querschnitt einer homogenen Mischung
Betrachten wir eine homogene Mischung aus zwei Nukliden $X$ und $Y$. Die Atomdichten der jeweiligen Nuklide seien $N_X$ und $N_Y$ $\text{Atom/cm}^3$, und die Wirkungsquerschnitte für eine bestimmte Reaktion mit Neutronen seien jeweils $\sigma_X$ und $\sigma_Y$. 

Die Wahrscheinlichkeit, dass ein Neutron pro Längeneinheit mit den Atomkernen $X$ und $Y$ kollidiert, beträgt dann jeweils $\Sigma_X=N_X\sigma_X$ und $\Sigma_Y=N_Y\sigma_Y$ (siehe [Makroskopischer Querschnitt](/posts/Neutron-Interactions-and-Cross-sections/#makroskopischer-querschnitt)). Die Gesamtwahrscheinlichkeit, dass ein Neutron pro Längeneinheit mit diesen beiden Atomkernen reagiert, ist daher:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Äquivalenter Querschnitt eines Moleküls
Wenn die oben betrachteten Kerne in molekularer Form vorliegen, können wir den äquivalenten Querschnitt (equivalent cross-section) dieses Moleküls definieren, indem wir den nach Gleichung (1) berechneten makroskopischen Querschnitt der Mischung durch die Anzahl der Moleküle pro Volumeneinheit teilen.

Wenn $N$ Moleküle $X_mY_n$ pro Volumeneinheit vorhanden sind, dann gilt $N_X=mN$ und $N_Y=nN$, und wir können den Querschnitt dieses Moleküls aus Gleichung (1) wie folgt berechnen:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> Die Gleichungen (1) und (2) gelten unter der Annahme, dass die Kerne $X$ und $Y$ unabhängig voneinander mit Neutronen reagieren. Daher können sie nicht auf die elastische Streuung durch Moleküle und Festkörper angewendet werden.
> Die Streuquerschnitte von Molekülen und Festkörpern bei niedrigen Neutronenenergien müssen experimentell bestimmt werden.
{: .prompt-warning }