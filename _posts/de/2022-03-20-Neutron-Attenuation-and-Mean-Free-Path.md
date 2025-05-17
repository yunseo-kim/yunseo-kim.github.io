---
title: Neutronenabschwächung (Neutron Attenuation) und mittlere freie Weglänge (Mean Free Path)
description: Berechnung der Intensität eines Neutronenstrahls in Abhängigkeit von der Durchdringungstiefe im Zielmaterial und Ableitung der mittleren freien Weglänge von Neutronen. Zusätzlich werden makroskopische Wirkungsquerschnitte für homogene Mischungen und Moleküle berechnet.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---

## Neutronenabschwächung (Neutron Attenuation)
Ein monoenergetischer Neutronenstrahl mit der Intensität $I_0$ wird auf ein Zielmaterial der Dicke $X$ gerichtet, und in einiger Entfernung hinter dem Ziel befindet sich ein Neutronendetektor. Wir nehmen an, dass sowohl das Ziel als auch der Detektor sehr klein sind und der Detektor nur einen kleinen Raumwinkel abdeckt, sodass er nur einen Teil der durch das Ziel austretenden Neutronen erfassen kann. Unter diesen Bedingungen werden alle Neutronen, die mit dem Zielmaterial kollidieren, entweder absorbiert oder in andere Richtungen gestreut, sodass nur die Neutronen, die keine Wechselwirkung mit dem Zielmaterial eingehen, den Detektor erreichen.

Sei $I(x)$ die Intensität des Neutronenstrahls, der die Strecke $x$ im Zielmaterial ohne Kollision zurückgelegt hat. Wenn der Neutronenstrahl eine dünne Schicht der Dicke $\tau$ durchdringt, ist die Anzahl der Kollisionen pro Flächeneinheit $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[Neutronen/cm}^2\cdot\text{s]}$ (siehe Gleichung [(1)](/posts/Neutron-Interactions-and-Cross-sections/#mjx-eqn%3Aeqn%3Amicroscopic_cross_section) und [(8)](/posts/Neutron-Interactions-and-Cross-sections/#mjx-eqn%3Aeqn%3Areaction_rate) im Artikel [Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/)). Daher ist die Abnahme der Neutronenstrahlintensität beim Durchgang durch eine Schicht der Dicke $dx$ wie folgt:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Durch Integration dieser Gleichung erhalten wir:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Daraus folgt, dass die Intensität des Neutronenstrahls mit zunehmender Durchdringungstiefe im Zielmaterial exponentiell abnimmt.

## Mittlere freie Weglänge (Mean Free Path)
- Die durchschnittliche Strecke, die ein Neutron zwischen aufeinanderfolgenden Kollisionen mit Atomkernen zurücklegt
- Das heißt, die durchschnittliche Strecke, die ein Neutron ohne Kollision zurücklegt
- Wird mit dem Symbol $\lambda$ bezeichnet

Der Ausdruck $I(x)/I_0=e^{-\Sigma_t x}$ gibt die Wahrscheinlichkeit an, dass ein Neutron die Strecke $x$ im Medium ohne Kollision zurücklegt. Die Wahrscheinlichkeit $p(x)dx$, dass ein Neutron die Strecke $x$ ohne Kollision zurücklegt und dann innerhalb der Strecke $dx$ eine Kollision erfährt, ist daher:

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
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Makroskopischer Wirkungsquerschnitt einer homogenen Mischung (Homogeneous Mixture)
Betrachten wir eine homogene Mischung aus zwei Nukliden $X$ und $Y$ mit den Atomdichten $N_X$ bzw. $N_Y$ $\text{Atom/cm}^3$ und den Wirkungsquerschnitten $\sigma_X$ bzw. $\sigma_Y$ für eine bestimmte Neutronenreaktion.

Die Wahrscheinlichkeit pro Längeneinheit, dass ein Neutron mit den Nukliden $X$ bzw. $Y$ kollidiert, beträgt $\Sigma_X=N_X\sigma_X$ bzw. $\Sigma_Y=N_Y\sigma_Y$ (siehe [Makroskopischer Wirkungsquerschnitt](/posts/Neutron-Interactions-and-Cross-sections/#makroskopischer-wirkungsquerschnitt-macroscopic-cross-section)). Die Gesamtwahrscheinlichkeit pro Längeneinheit, dass ein Neutron mit einem der beiden Nuklide reagiert, ist daher:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Äquivalenter Wirkungsquerschnitt (Equivalent Cross-section) eines Moleküls
Wenn die oben betrachteten Nuklide in Form von Molekülen vorliegen, können wir den äquivalenten Wirkungsquerschnitt (equivalent cross-section) des Moleküls definieren, indem wir den makroskopischen Wirkungsquerschnitt der Mischung aus Gleichung ($\ref{eqn:cross_section_of_mixture}$) durch die Anzahl der Moleküle pro Volumeneinheit teilen.

Wenn $N$ Moleküle $X_mY_n$ pro Volumeneinheit vorhanden sind, dann gilt $N_X=mN$ und $N_Y=nN$. Aus Gleichung ($\ref{eqn:cross_section_of_mixture}$) erhalten wir den Wirkungsquerschnitt dieses Moleküls:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> Die Gleichungen ($\ref{eqn:cross_section_of_mixture}$) und ($\ref{eqn:equivalent_cross_section}$) gelten unter der Annahme, dass die Nuklide $X$ und $Y$ unabhängig voneinander mit Neutronen wechselwirken, und sind für alle Arten von Neutronenreaktionen außer [elastischer Streuung](/posts/Neutron-Interactions-and-Cross-sections/#elastische-streuung-elastic-scattering) gültig.
> Für die elastische Streuung von Neutronen an Molekülen und Festkörpern (besonders im niedrigen Energiebereich) ist diese Annahme nicht anwendbar, und die Streuquerschnitte müssen experimentell bestimmt werden.
{: .prompt-warning }
