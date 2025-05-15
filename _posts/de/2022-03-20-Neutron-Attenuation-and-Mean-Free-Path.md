---
title: Neutronenabschwächung (Neutron Attenuation) und mittlere freie Weglänge (Mean Free Path)
description: Berechnung der Intensität eines monoenergetischen Neutronenstrahls in Abhängigkeit von der Durchdringungstiefe im Zielmaterial und Ableitung der mittleren freien Weglänge der Neutronen.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---
## Neutronenabschwächung (Neutron Attenuation)
Ein monoenergetischer Neutronenstrahl mit der Intensität $I_0$ wird auf ein Zielmaterial der Dicke $X$ gerichtet, und in einiger Entfernung hinter dem Zielmaterial befindet sich ein Neutronendetektor. Nehmen wir an, dass sowohl das Zielmaterial als auch der Detektor sehr klein sind und der Detektor nur einen kleinen Raumwinkel abdeckt, sodass er nur einen Teil der durch das Zielmaterial austretenden Neutronen erfassen kann. Alle Neutronen, die mit dem Zielmaterial kollidieren, werden entweder absorbiert oder in andere Richtungen gestreut, sodass nur die Neutronen, die nicht mit dem Zielmaterial reagieren, den Detektor erreichen.

Bezeichnen wir mit $I(x)$ die Intensität des Neutronenstrahls, der nach einer Strecke $x$ im Zielmaterial ohne Kollision verbleibt. Wenn der Neutronenstrahl durch eine sehr dünne Schicht des Zielmaterials mit der Dicke $\tau$ hindurchtritt, ist die Anzahl der Kollisionen pro Flächeneinheit $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[Neutronen/cm}^2\cdot\text{s]}$ (siehe Gleichung (1) und (4) in [Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)). Daher ist die Abnahme der Neutronenstrahlintensität beim Durchgang durch die Strecke $dx$ im Zielmaterial:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Durch Integration dieser Gleichung erhalten wir:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Daraus folgt, dass die Intensität des Neutronenstrahls mit zunehmender Durchdringungstiefe im Zielmaterial exponentiell abnimmt.

## Mittlere freie Weglänge (Mean Free Path)
- Die durchschnittliche Strecke, die ein Neutron nach einer Kollision mit einem Kern zurücklegt, bevor es mit einem weiteren Kern kollidiert
- Das heißt, die durchschnittliche Strecke, die ein Neutron ohne Kollision zurücklegt
- Wird mit dem Symbol $\lambda$ bezeichnet

$I(x)/I_0=e^{-\Sigma_t x}$ gibt die Wahrscheinlichkeit an, dass ein Neutron die Strecke $x$ im Medium ohne Kollision mit einem Kern zurücklegt. Die Wahrscheinlichkeit $p(x)dx$, dass ein Neutron die Strecke $x$ ohne Kollision zurücklegt und dann innerhalb der Strecke $dx$ kollidiert, ist daher:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

Daraus können wir die *mittlere freie Weglänge (mean free path)* $\lambda$ wie folgt berechnen:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
