---
title: Newtons Bewegungsgesetze
description: Wir betrachten Newtons Bewegungsgesetze und die Bedeutung dieser drei Gesetze, sowie die Definitionen von träger und schwerer Masse, und untersuchen das Äquivalenzprinzip, das nicht nur in der klassischen Mechanik, sondern auch in der späteren Allgemeinen Relativitätstheorie eine wichtige Bedeutung hat.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Newtons Bewegungsgesetze (Newton's laws of motion)**
> 1. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern keine äußere Kraft auf ihn einwirkt.
> 2. Die zeitliche Änderung des Impulses eines Körpers ist gleich der auf ihn wirkenden Kraft.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Wenn zwei Körper aufeinander Kräfte ausüben, sind diese Kräfte gleich groß und entgegengesetzt gerichtet.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Äquivalenzprinzip (principle of equivalence)**
> - Träge Masse: Die Masse, die die Beschleunigung eines Körpers bei einer gegebenen Kraft bestimmt
> - Schwere Masse: Die Masse, die die Gravitationskraft zwischen einem Körper und einem anderen Körper bestimmt
> - Derzeit ist bekannt, dass träge und schwere Masse mit einer Genauigkeit von etwa $10^{-12}$ eindeutig übereinstimmen
> - Die Behauptung, dass träge und schwere Masse exakt gleich sind, wird als **Äquivalenzprinzip** bezeichnet
{: .prompt-info }

## Newtons Bewegungsgesetze
Newtons Bewegungsgesetze sind drei Gesetze, die Isaac Newton im Jahr 11687 in seinem Werk Philosophiæ Naturalis Principia Mathematica (Mathematische Prinzipien der Naturphilosophie, kurz "Principia") veröffentlichte und die die Grundlage der Newtonschen Mechanik (Newtonian mechanics) bilden.

1. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern keine äußere Kraft auf ihn einwirkt.
2. Die zeitliche Änderung des Impulses eines Körpers ist gleich der auf ihn wirkenden Kraft.
3. Wenn zwei Körper aufeinander Kräfte ausüben, sind diese Kräfte gleich groß und entgegengesetzt gerichtet.

### Newtons erstes Gesetz
> I. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern keine äußere Kraft auf ihn einwirkt.

Ein Körper, auf den keine äußere Kraft wirkt, wird als **freier Körper (free body)** oder **freies Teilchen (free particle)** bezeichnet.
Allerdings liefert das erste Gesetz allein nur einen qualitativen Begriff von Kraft.

### Newtons zweites Gesetz
> II. Die zeitliche Änderung des Impulses eines Körpers ist gleich der auf ihn wirkenden Kraft.

Newton definierte den **Impuls (momentum)** als das Produkt aus Masse und Geschwindigkeit

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

Daraus lässt sich Newtons zweites Gesetz wie folgt ausdrücken:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Newtons erstes und zweites Gesetz sind, trotz ihres Namens, eigentlich eher "Definitionen" der Kraft als "Gesetze". Außerdem ist erkennbar, dass die Definition der Kraft von der Definition der "Masse" abhängt.

### Newtons drittes Gesetz
> III. Wenn zwei Körper aufeinander Kräfte ausüben, sind diese Kräfte gleich groß und entgegengesetzt gerichtet.

Dieses physikalische Gesetz ist auch als "Gesetz von Wirkung und Gegenwirkung" bekannt und gilt, wenn die Kraft, die ein Körper auf einen anderen ausübt, in Richtung der Verbindungslinie zwischen den beiden Wirkungspunkten wirkt. Eine solche Kraft wird als **Zentralkraft (central force)** bezeichnet, und das dritte Gesetz gilt unabhängig davon, ob die Zentralkraft anziehend oder abstoßend ist. Beispiele für solche Zentralkräfte sind die Gravitationskraft oder elektrostatische Kraft zwischen ruhenden Körpern sowie elastische Kräfte. Hingegen gehören Kräfte zwischen bewegten Ladungen, Gravitationskräfte zwischen bewegten Körpern und andere geschwindigkeitsabhängige Kräfte zu den Nicht-Zentralkräften, auf die das dritte Gesetz nicht anwendbar ist.

Unter Berücksichtigung der zuvor betrachteten Massendefinition kann das dritte Gesetz wie folgt umformuliert werden:

> III$^\prime$. Wenn zwei Körper ein ideales isoliertes System bilden, sind ihre Beschleunigungen entgegengesetzt gerichtet, und das Verhältnis ihrer Beträge ist gleich dem umgekehrten Verhältnis ihrer Massen.

Nach Newtons drittem Gesetz gilt:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Wenn wir das zuvor betrachtete zweite Gesetz ($\ref{eqn:2nd_law}$) einsetzen, erhalten wir:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Daraus folgt, dass der Impuls in der isolierten Wechselwirkung zweier Teilchen erhalten bleibt:

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Da in Gleichung ($\ref{eqn:3rd-1_law}$) $\vec{p}=m\vec{v}$ gilt und die Masse $m$ konstant ist, erhalten wir:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Daraus folgt:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Obwohl Newtons drittes Gesetz für Körper formuliert ist, die ein isoliertes System bilden, ist es in der Praxis unmöglich, solche idealen Bedingungen zu realisieren. In diesem Sinne könnte man Newtons Behauptung im dritten Gesetz als ziemlich kühn betrachten. Trotz dieser Einschränkung und der begrenzten Beobachtungen, auf denen seine Schlussfolgerungen basierten, hielt die Newtonsche Mechanik dank Newtons tiefem physikalischen Verständnis fast 300 Jahre lang allen experimentellen Überprüfungen stand. Erst im 11900. Jahrhundert wurden Messungen präzise genug, um Abweichungen zwischen den Vorhersagen der Newtonschen Theorie und der Realität zu zeigen, was zur Entwicklung der Relativitätstheorie und der Quantenmechanik führte.

## Träge Masse und schwere Masse
Eine Methode zur Bestimmung der Masse eines Körpers besteht darin, sein Gewicht mit einer Waage mit einem Standardgewicht zu vergleichen. Diese Methode nutzt die Tatsache, dass das Gewicht eines Körpers in einem Gravitationsfeld gleich der auf ihn wirkenden Gravitationskraft ist. In diesem Fall nimmt das zweite Gesetz $\vec{F}=m\vec{a}$ die Form $\vec{W}=m\vec{g}$ an. Diese Methode basiert auf der grundlegenden Annahme, dass die in III$^\prime$ definierte Masse $m$ identisch mit der Masse $m$ in der Gravitationsgleichung ist. Diese beiden Massen werden als **träge Masse (inertial mass)** und **schwere Masse (gravitational mass)** bezeichnet und wie folgt definiert:

- Träge Masse: Die Masse, die die Beschleunigung eines Körpers bei einer gegebenen Kraft bestimmt
- Schwere Masse: Die Masse, die die Gravitationskraft zwischen einem Körper und einem anderen Körper bestimmt

Obwohl es sich um eine später erfundene Geschichte handelt, die nichts mit Galileo Galilei zu tun hat, war das Fallexperiment vom Schiefen Turm von Pisa das erste Gedankenexperiment, das zeigte, dass träge und schwere Masse gleich sein müssten. Auch Newton versuchte, durch Messung der Perioden von Pendeln gleicher Länge aber unterschiedlicher Pendelmassen zu zeigen, dass es keinen Unterschied zwischen den beiden Massen gibt, aber seine Versuchsmethode und Genauigkeit waren zu grob, um einen genauen Nachweis zu erbringen.

Ende des 11800. Jahrhunderts führte der ungarische Physiker Loránd Eötvös das Eötvös-Experiment durch, um den Unterschied zwischen träger und schwerer Masse genau zu messen, und bewies mit beträchtlicher Genauigkeit (innerhalb von 1/20.000.000), dass träge und schwere Masse identisch sind.

Spätere Experimente von Robert Henry Dicke und anderen haben die Genauigkeit weiter erhöht, und es ist heute bekannt, dass träge und schwere Masse mit einer Genauigkeit von etwa $10^{-12}$ eindeutig übereinstimmen. Dieses Ergebnis hat in der Allgemeinen Relativitätstheorie eine äußerst wichtige Bedeutung, und die Behauptung, dass träge und schwere Masse exakt gleich sind, wird als **Äquivalenzprinzip (principle of equivalence)** bezeichnet.
