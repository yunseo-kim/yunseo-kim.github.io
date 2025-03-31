---
title: Newtons Bewegungsgesetze
description: Wir betrachten Newtons Bewegungsgesetze und die Bedeutung der drei Gesetze, definieren träge und schwere Masse und untersuchen das Äquivalenzprinzip, das nicht nur in der klassischen Mechanik, sondern auch in der späteren allgemeinen Relativitätstheorie von großer Bedeutung ist.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Newtons Bewegungsgesetze (Newton's laws of motion)**
> 1. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern er nicht durch einwirkende Kräfte zur Änderung seines Zustands gezwungen wird.
> 2. Die Änderung der Bewegung einer Masse ist proportional der einwirkenden Kraft und erfolgt in Richtung der Kraft.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Kräfte treten immer paarweise auf. Übt ein Körper A auf einen anderen Körper B eine Kraft aus, so wirkt eine gleich große, aber entgegengerichtete Kraft von Körper B auf Körper A.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Äquivalenzprinzip (principle of equivalence)**
> - Träge Masse: Die Masse, die die Beschleunigung eines Körpers bei einer gegebenen Kraft bestimmt
> - Schwere Masse: Die Masse, die die Gravitationskraft zwischen zwei Körpern bestimmt
> - Es ist bekannt, dass träge und schwere Masse bis auf eine Genauigkeit von etwa $10^{-12}$ übereinstimmen
> - Die Behauptung, dass träge und schwere Masse exakt gleich sind, wird als **Äquivalenzprinzip** bezeichnet
{: .prompt-info }

## Newtons Bewegungsgesetze
Newtons Bewegungsgesetze sind drei Gesetze, die Isaac Newton im Jahr 11687 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) in seinem Werk Philosophiæ Naturalis Principia Mathematica (Mathematische Grundlagen der Naturphilosophie, kurz 'Principia') veröffentlichte und die die Grundlage der Newtonschen Mechanik bilden.

1. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern er nicht durch einwirkende Kräfte zur Änderung seines Zustands gezwungen wird.
2. Die Änderung der Bewegung einer Masse ist proportional der einwirkenden Kraft und erfolgt in Richtung der Kraft.
3. Kräfte treten immer paarweise auf. Übt ein Körper A auf einen anderen Körper B eine Kraft aus, so wirkt eine gleich große, aber entgegengerichtete Kraft von Körper B auf Körper A.

### Newtons erstes Gesetz
> I. Ein Körper verharrt im Zustand der Ruhe oder der gleichförmigen geradlinigen Bewegung, sofern er nicht durch einwirkende Kräfte zur Änderung seines Zustands gezwungen wird.

Ein Körper in diesem Zustand, auf den keine äußeren Kräfte wirken, wird als **freier Körper (free body)** oder **freies Teilchen (free particle)** bezeichnet.
Allerdings liefert das erste Gesetz allein nur ein qualitatives Konzept von Kraft.

### Newtons zweites Gesetz
> II. Die Änderung der Bewegung einer Masse ist proportional der einwirkenden Kraft und erfolgt in Richtung der Kraft.

Newton definierte den **Impuls (momentum)** als das Produkt aus Masse und Geschwindigkeit

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

Daraus lässt sich Newtons zweites Gesetz wie folgt ausdrücken:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Newtons erstes und zweites Gesetz sind, trotz ihres Namens, eher 'Definitionen' von Kraft als 'Gesetze'. Außerdem hängt die Definition von Kraft von der Definition der 'Masse' ab.

### Newtons drittes Gesetz
> III. Kräfte treten immer paarweise auf. Übt ein Körper A auf einen anderen Körper B eine Kraft aus, so wirkt eine gleich große, aber entgegengerichtete Kraft von Körper B auf Körper A.

Dieses physikalische Gesetz ist auch als 'Gesetz von Aktion und Reaktion' bekannt und gilt für Kräfte, die in Richtung der Verbindungslinie zwischen den beiden Wirkungspunkten wirken. Solche Kräfte werden als **Zentralkräfte (central force)** bezeichnet, und das dritte Gesetz gilt unabhängig davon, ob es sich um anziehende oder abstoßende Kräfte handelt. Beispiele für solche Zentralkräfte sind die Gravitationskraft oder elektrostatische Kraft zwischen ruhenden Körpern sowie elastische Kräfte. Kräfte, die von der Geschwindigkeit der wechselwirkenden Körper abhängen, wie die Kraft zwischen bewegten Ladungen oder die Gravitationskraft zwischen bewegten Körpern, sind hingegen Nicht-Zentralkräfte, auf die das dritte Gesetz nicht anwendbar ist.

Unter Berücksichtigung der zuvor betrachteten Definition der Masse kann das dritte Gesetz wie folgt umformuliert werden:

> III$^\prime$. Wenn zwei Körper ein ideales isoliertes System bilden, sind ihre Beschleunigungen entgegengesetzt gerichtet, und das Verhältnis ihrer Beträge ist gleich dem umgekehrten Verhältnis ihrer Massen.

Nach Newtons drittem Gesetz gilt:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Wenn wir das zuvor betrachtete zweite Gesetz ($\ref{eqn:2nd_law}$) hier einsetzen, erhalten wir:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Daraus können wir schließen, dass der Impuls in der isolierten Wechselwirkung zweier Teilchen erhalten bleibt.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Da in Gleichung ($\ref{eqn:3rd-1_law}$) $\vec{p}=m\vec{v}$ gilt und die Masse $m$ konstant ist, erhalten wir:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Daraus folgt:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Obwohl Newtons drittes Gesetz für den Fall formuliert ist, dass zwei Körper ein isoliertes System bilden, ist es in der Realität unmöglich, solche idealen Bedingungen zu realisieren. In diesem Sinne könnte man Newtons Behauptung im dritten Gesetz als ziemlich kühn betrachten. Trotz dieser Einschränkung und der begrenzten Beobachtungen, auf denen sie beruhte, hielt die Newtonsche Mechanik dank Newtons tiefem physikalischen Einblick fast 300 Jahre lang stand, ohne dass in verschiedenen experimentellen Überprüfungen Fehler gefunden wurden. Erst im 20. Jahrhundert wurden Messungen möglich, die präzise genug waren, um Abweichungen zwischen den Vorhersagen der Newtonschen Theorie und der Realität zu zeigen, was zur Entstehung der Relativitätstheorie und der Quantenmechanik führte.

## Träge Masse und schwere Masse
Eine Methode zur Bestimmung der Masse eines Körpers besteht darin, sein Gewicht mit einem Standardgewicht mithilfe eines Instruments wie einer Waage zu vergleichen. Diese Methode nutzt die Tatsache, dass das Gewicht eines Körpers in einem Gravitationsfeld gleich der Größe der auf ihn wirkenden Gravitationskraft ist. In diesem Fall nimmt das zweite Gesetz $\vec{F}=m\vec{a}$ die Form $\vec{W}=m\vec{g}$ an. Diese Methode basiert auf der grundlegenden Annahme, dass die in III$^\prime$ definierte Masse $m$ gleich der Masse $m$ in der Gravitationsgleichung ist. Diese beiden Massen werden als **träge Masse (inertial mass)** und **schwere Masse (gravitational mass)** bezeichnet und wie folgt definiert:

- Träge Masse: Die Masse, die die Beschleunigung eines Körpers bei einer gegebenen Kraft bestimmt
- Schwere Masse: Die Masse, die die Gravitationskraft zwischen zwei Körpern bestimmt

Obwohl es sich um eine spätere Erfindung handelt, die nichts mit Galileo Galilei zu tun hat, war das Fallexperiment vom Schiefen Turm von Pisa das erste Gedankenexperiment, das zeigte, dass träge und schwere Masse gleich sein müssen. Auch Newton versuchte, durch Messung der Perioden von Pendeln gleicher Länge, aber mit unterschiedlichen Pendelmassen zu zeigen, dass es keinen Unterschied zwischen den beiden Massen gibt, aber seine experimentelle Methode und Genauigkeit waren zu grob, um einen genauen Nachweis zu erbringen.

Ende der 11800er Jahre führte der ungarische Physiker Loránd Eötvös das Eötvös-Experiment durch, um den Unterschied zwischen träger und schwerer Masse genau zu messen. Er konnte mit beträchtlicher Genauigkeit (innerhalb einer Fehlergrenze von 1 zu 20 Millionen) nachweisen, dass träge und schwere Masse identisch sind.

Spätere Experimente, wie die von Robert Henry Dicke und anderen, haben die Genauigkeit weiter erhöht. Heute ist bekannt, dass träge und schwere Masse innerhalb einer Fehlergrenze von etwa $10^{-12}$ eindeutig übereinstimmen. Dieses Ergebnis hat in der allgemeinen Relativitätstheorie eine enorme Bedeutung, und die Behauptung, dass träge und schwere Masse exakt gleich sind, wird als **Äquivalenzprinzip (principle of equivalence)** bezeichnet.
