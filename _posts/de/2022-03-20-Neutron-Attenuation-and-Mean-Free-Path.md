---
title: "Neutronenabschwächung und mittlere freie Weglänge (Mean Free Path)"
description: >-
  Berechnung der Intensität eines Neutronenstrahls mit einer einzigen Energie bei Bestrahlung eines Ziels in Abhängigkeit von der Durchdringungstiefe und Ableitung der mittleren freien Weglänge der Neutronen daraus.
categories: [Ingenieurphysik, Kerntechnik]
tags: [Kernphysik, Wechselwirkung von Strahlung mit Materie]
math: true
---

## Neutronenabschwächung (Neutron Attenuation)
Ein Neutronenstrahl mit einer einzigen Energie und der Intensität $I_0$ bestrahlt ein Ziel der Dicke $X$, und in einiger Entfernung hinter dem Ziel befindet sich ein Neutronendetektor. Wir nehmen an, dass sowohl das Ziel als auch der Detektor sehr klein sind und der Detektor nur einen kleinen Raumwinkel hat, der nur einen Teil der durch das Ziel austretenden Neutronen erfassen kann. Folglich werden alle Neutronen, die auf das Ziel treffen, entweder absorbiert oder in andere Richtungen gestreut, sodass nur die Neutronen, die nicht mit dem Ziel reagiert haben, den Detektor erreichen.

Sei $I(x)$ die Intensität des Neutronenstrahls, der nach einer Strecke $x$ im Ziel ohne Kollision übrig bleibt. Wenn der Neutronenstrahl ein Ziel mit einer ausreichend dünnen Dicke $\tau$ durchdringt, ist die Anzahl der Kollisionen pro Flächeneinheit $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[Neutronen/cm}^2\cdot\text{s]}$ (siehe Gleichungen (1) und (4) in [Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/#Wirkungsquerschnitt-cross-section-oder-mikroskopischer-Wirkungsquerschnitt-microscopic-cross-section)). Daher ist die Abnahme der Neutronenstrahlintensität beim Durchgang durch $dx$ im Ziel wie folgt:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Die Integration dieser Gleichung ergibt:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Daraus folgt, dass die Intensität des Neutronenstrahls exponentiell mit zunehmender Durchdringungstiefe im Ziel abnimmt.

## Mittlere freie Weglänge (Mean Free Path)
- Die durchschnittliche Strecke, die ein Neutron nach einer Kollision mit einem Kern zurücklegt, bevor es mit einem anderen Kern kollidiert
- Mit anderen Worten, die durchschnittliche Strecke, die ein Neutron ohne Kollision zurücklegt
- Bezeichnet mit dem Symbol $\lambda$

$I(x)/I_0=e^{-\Sigma_t x}$ stellt die Wahrscheinlichkeit dar, dass ein Neutron die Strecke $x$ im Medium ohne Kollision mit einem Kern zurücklegt. Daher ist die Wahrscheinlichkeit $p(x)dx$, dass ein Neutron die Strecke $x$ im Medium ohne Kollision zurücklegt und dann innerhalb der Strecke $dx$ kollidiert, wie folgt:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

Daraus können wir die *mittlere freie Weglänge* $\lambda$ wie folgt berechnen:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$