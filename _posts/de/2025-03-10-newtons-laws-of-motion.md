---
title: Newtons Bewegungsgesetze
description: Wir betrachten Newtons Bewegungsgesetze und die Bedeutung der drei Gesetze, definieren die träge und die schwere Masse und untersuchen das Äquivalenzprinzip, das nicht nur in der klassischen Mechanik, sondern auch in der späteren allgemeinen Relativitätstheorie eine wichtige Rolle spielt.
categories: [Physics, Classical Dynamics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Newtons Bewegungsgesetze (Newton's laws of motion)**
> 1. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern er nicht durch einwirkende Kräfte zur Änderung seines Zustands gezwungen wird.
> 2. Die Änderung der Bewegung einer Masse ist der Einwirkung der bewegenden Kraft proportional und erfolgt nach der Richtung derjenigen geraden Linie, nach welcher jene Kraft wirkt.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Kräfte treten immer paarweise auf. Übt ein Körper A auf einen anderen Körper B eine Kraft aus, so wirkt eine gleich große, aber entgegengerichtete Kraft von Körper B auf Körper A.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Äquivalenzprinzip (principle of equivalence)**
> - Träge Masse: Die Masse, die die Beschleunigung eines Körpers bei einer gegebenen Kraft bestimmt
> - Schwere Masse: Die Masse, die die Gravitationskraft zwischen einem Körper und einem anderen Körper bestimmt
> - Es ist bekannt, dass die träge und die schwere Masse mit einer Genauigkeit von etwa $10^{-12}$ übereinstimmen
> - Die Behauptung, dass die träge und die schwere Masse exakt gleich sind, wird als **Äquivalenzprinzip** bezeichnet
{: .prompt-info }

## Newtons Bewegungsgesetze
Newtons Bewegungsgesetze sind drei Gesetze, die Isaac Newton 1687 in seinem Werk Philosophiæ Naturalis Principia Mathematica (Mathematische Prinzipien der Naturphilosophie, kurz 'Principia') veröffentlichte und die die Grundlage der Newtonschen Mechanik bilden.

1. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern er nicht durch einwirkende Kräfte zur Änderung seines Zustands gezwungen wird.
2. Die Änderung der Bewegung einer Masse ist der Einwirkung der bewegenden Kraft proportional und erfolgt nach der Richtung derjenigen geraden Linie, nach welcher jene Kraft wirkt.
3. Kräfte treten immer paarweise auf. Übt ein Körper A auf einen anderen Körper B eine Kraft aus, so wirkt eine gleich große, aber entgegengerichtete Kraft von Körper B auf Körper A.

### Newtons erstes Gesetz
> I. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern er nicht durch einwirkende Kräfte zur Änderung seines Zustands gezwungen wird.

Ein Körper in diesem Zustand, auf den keine äußeren Kräfte wirken, wird als **freier Körper (free body)** oder **freies Teilchen (free particle)** bezeichnet.
Allerdings liefert das erste Gesetz allein nur ein qualitatives Konzept von Kraft.

### Newtons zweites Gesetz
> II. Die Änderung der Bewegung einer Masse ist der Einwirkung der bewegenden Kraft proportional und erfolgt nach der Richtung derjenigen geraden Linie, nach welcher jene Kraft wirkt.

Newton definierte den **Impuls (momentum)** als das Produkt aus Masse und Geschwindigkeit

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

Daraus lässt sich Newtons zweites Gesetz wie folgt ausdrücken:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Newtons erstes und zweites Gesetz sind, trotz ihres Namens, eher 'Definitionen' von Kraft als 'Gesetze'. Außerdem hängt die Definition von Kraft von der Definition der 'Masse' ab.

### Newtons drittes Gesetz
> III. Kräfte treten immer paarweise auf. Übt ein Körper A auf einen anderen Körper B eine Kraft aus, so wirkt eine gleich große, aber entgegengerichtete Kraft von Körper B auf Körper A.

Dieses Gesetz ist auch als 'Gesetz von Aktion und Reaktion' bekannt und gilt für Kräfte, die in Richtung der Verbindungslinie zwischen den beiden Wirkungspunkten wirken. Solche Kräfte werden als **Zentralkräfte (central force)** bezeichnet, und das dritte Gesetz gilt unabhängig davon, ob es sich um anziehende oder abstoßende Kräfte handelt. Beispiele für Zentralkräfte sind die Gravitationskraft oder elektrostatische Kraft zwischen ruhenden Körpern sowie die elastische Kraft. Kräfte, die von der Geschwindigkeit der wechselwirkenden Körper abhängen, wie die Kraft zwischen bewegten Ladungen oder die Gravitationskraft zwischen bewegten Körpern, sind nicht-zentrale Kräfte und fallen nicht unter das dritte Gesetz.

Unter Berücksichtigung der zuvor betrachteten Definition der Masse kann das dritte Gesetz wie folgt umformuliert werden:

> III$^\prime$. Wenn zwei Körper ein ideales isoliertes System bilden, sind ihre Beschleunigungen entgegengesetzt gerichtet, und das Verhältnis ihrer Beträge ist gleich dem umgekehrten Verhältnis ihrer Massen.

Nach Newtons drittem Gesetz gilt:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Wenn wir das zuvor betrachtete zweite Gesetz ($\ref{eqn:2nd_law}$) hier einsetzen, erhalten wir:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Daraus können wir schließen, dass der Impuls in der isolierten Wechselwirkung zwischen zwei Teilchen erhalten bleibt.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Da in Gleichung ($\ref{eqn:3rd-1_law}$) $\vec{p}=m\vec{v}$ gilt und die Masse $m$ konstant ist, erhalten wir:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Daraus folgt:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Obwohl Newtons drittes Gesetz für den Fall formuliert ist, dass zwei Körper ein isoliertes System bilden, ist es in der Realität unmöglich, solche idealen Bedingungen zu realisieren. In diesem Sinne könnte man Newtons Behauptung im dritten Gesetz als ziemlich kühn betrachten. Trotz dieser Einschränkung der Beobachtungen blieb die Newtonsche Mechanik dank Newtons tiefem physikalischen Einblick fast 300 Jahre lang in verschiedenen experimentellen Überprüfungen fehlerfrei und behielt eine feste Position. Erst im 20. Jahrhundert wurden Messungen möglich, die präzise genug waren, um Unterschiede zwischen den Vorhersagen der Newtonschen Theorie und der Realität zu zeigen, was zur Entstehung der Relativitätstheorie und der Quantenmechanik führte.

## Träge Masse und schwere Masse
Eine Methode zur Bestimmung der Masse eines Körpers besteht darin, sein Gewicht mit einem Standardgewicht mithilfe eines Instruments wie einer Waage zu vergleichen. Diese Methode nutzt die Tatsache, dass das Gewicht eines Körpers in einem Gravitationsfeld gleich der Größe der auf ihn wirkenden Gravitationskraft ist. In diesem Fall nimmt das zweite Gesetz $\vec{F}=m\vec{a}$ die Form $\vec{W}=m\vec{g}$ an. Diese Methode basiert auf der grundlegenden Annahme, dass die in III$^\prime$ definierte Masse $m$ gleich der Masse $m$ in der Gravitationsgleichung ist. Diese beiden Massen werden als **träge Masse (inertial mass)** und **schwere Masse (gravitational mass)** bezeichnet und wie folgt definiert:

- Träge Masse: Die Masse, die die Beschleunigung eines Körpers bei einer gegebenen Kraft bestimmt
- Schwere Masse: Die Masse, die die Gravitationskraft zwischen einem Körper und einem anderen Körper bestimmt

Obwohl es sich um eine spätere Erfindung handelt, die nichts mit Galileo Galilei zu tun hat, war das Fallexperiment vom Schiefen Turm von Pisa das erste Gedankenexperiment, das zeigte, dass die träge und die schwere Masse gleich sein müssen. Newton versuchte ebenfalls, durch Messung der Perioden von Pendeln gleicher Länge, aber mit unterschiedlichen Pendelmassen zu zeigen, dass es keinen Unterschied zwischen den beiden Massen gibt, aber seine experimentelle Methode und Genauigkeit waren zu grob, um einen genauen Nachweis zu liefern.

Ende des 19. Jahrhunderts führte der ungarische Physiker Loránd Eötvös das Eötvös-Experiment durch, um den Unterschied zwischen träger und schwerer Masse genau zu messen. Er konnte mit beträchtlicher Genauigkeit (innerhalb von 1 zu 20 Millionen) nachweisen, dass die träge und die schwere Masse identisch sind.

Spätere Experimente von Robert Henry Dicke und anderen haben die Genauigkeit weiter erhöht, und es ist heute bekannt, dass die träge und die schwere Masse mit einer Genauigkeit von etwa $10^{-12}$ übereinstimmen. Dieses Ergebnis hat eine große Bedeutung in der allgemeinen Relativitätstheorie, und die Behauptung, dass die träge und die schwere Masse exakt gleich sind, wird als **Äquivalenzprinzip (principle of equivalence)** bezeichnet.
