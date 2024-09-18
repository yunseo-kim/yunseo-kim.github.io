---
title: "Relativitätsprinzip und Lorentz-Transformation"
description: >-
  Wir betrachten das Konzept des Bezugssystems und die Galilei-Transformation, die in der klassischen Mechanik weit verbreitet war. Außerdem werfen wir einen kurzen Blick auf die Maxwell-Gleichungen und das Michelson-Morley-Experiment, die den Hintergrund für die Entstehung der Lorentz-Transformation bildeten, und leiten die Transformationsmatrix der Lorentz-Transformation her.
categories: [Engineering Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
---

## Bezugssysteme und Relativitätsprinzip
### Bezugssystem (frame of reference)
- **Bezugssystem (frame of reference)**: Die Bewegung eines Objekts bedeutet, dass sich seine Position relativ zu anderen Objekten ändert. Da alle Bewegungen relativ sind, muss ein Bezugssystem festgelegt werden, um eine Bewegung zu beschreiben.
- **Inertialsystem (inertial frames of reference)**: Ein System, in dem Newtons erstes Bewegungsgesetz ("Der Bewegungszustand eines Körpers bleibt unverändert, solange die resultierende Kraft auf den Körper null ist.") gilt. Jedes Bezugssystem, das sich mit konstanter Geschwindigkeit relativ zu einem Inertialsystem bewegt, ist ebenfalls ein Inertialsystem.

### Relativitätsprinzip (Principle of Relativity)
Es ist eines der Hauptkonzepte und eine grundlegende Voraussetzung der Physik, die besagt, dass alle physikalischen Gesetze in allen Bezugssystemen, die sich mit konstanter Geschwindigkeit zueinander bewegen, gleich sein müssen. Wenn die physikalischen Gesetze für relativ zueinander bewegte Beobachter unterschiedlich wären, könnte man diese Unterschiede nutzen, um ein absolutes Bezugssystem zu definieren und festzustellen, wer ruht und wer sich bewegt. Gemäß dem Relativitätsprinzip gibt es jedoch keine solche Unterscheidung, daher existiert kein absolutes Bezugssystem oder absolute Bewegung für das gesamte Universum, und alle Inertialsysteme sind gleichwertig.

## Grenzen der Galilei-Transformation
### Galilei-Transformation (Galilean transformation)
Angenommen, es gibt zwei Inertialsysteme $S$ und $S^{\prime}$, wobei sich $S^{\prime}$ mit einer konstanten Geschwindigkeit $\vec{v}$ in $+x$-Richtung relativ zu $S$ bewegt, und ein und dasselbe Ereignis wird in $S$ zum Zeitpunkt $t$ an den Koordinaten $(x, y, z)$ und in $S^{\prime}$ zum Zeitpunkt $t^{\prime}$ an den Koordinaten $(x^{\prime}, y^{\prime}, z^{\prime})$ beobachtet.

In diesem Fall wird der in $x$-Richtung gemessene Wert der Bewegung in $S^{\prime}$ um die Strecke $\vec{v}t$ größer sein als der in $S$ gemessene Wert, die $S^{\prime}$ relativ zu $S$ in $x$-Richtung zurückgelegt hat, also

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

und da es keine relative Bewegung in $y$- und $z$-Richtung gibt,

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

und intuitiv kann man annehmen, dass

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Die Koordinatentransformation zwischen verschiedenen Inertialsystemen, die in der Physik klassischerweise verwendet wurde, wie in den Gleichungen ($\ref{eqn:galilean_transform_x}$) bis ($\ref{eqn:galilean_transform_t}$), wird als **Galilei-Transformation (Galilean transformation)** bezeichnet und ist einfach und intuitiv, da sie in den meisten alltäglichen Situationen zutrifft. Wie später erläutert wird, steht sie jedoch im Widerspruch zu den Maxwell-Gleichungen.

### Maxwell-Gleichungen
Maxwell erweiterte Ende des 19. Jahrhunderts die Ideen und Forschungsergebnisse anderer Wissenschaftler wie Faraday und Ampère und zeigte, dass Elektrizität und Magnetismus tatsächlich eine einzige Kraft sind. Er leitete die folgenden vier Gleichungen ab, die das elektromagnetische Feld beschreiben:

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: Der elektrische Fluss durch eine beliebige geschlossene Oberfläche ist gleich der eingeschlossenen Nettoladung (Gaußsches Gesetz).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Es gibt keine magnetischen Monopole.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: Eine Änderung des Magnetfeldes erzeugt ein elektrisches Feld (Faradaysches Induktionsgesetz).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: Elektrische Feldänderungen und Ströme erzeugen ein Magnetfeld (Ampère-Maxwell-Gesetz).}
\end{gather*}$$

Die Maxwell-Gleichungen konnten alle bis dahin bekannten elektrischen und magnetischen Phänomene erfolgreich erklären, sagten die Existenz elektromagnetischer Wellen voraus und leiteten ab, dass die Geschwindigkeit elektromagnetischer Wellen im Vakuum $c$ eine unveränderliche Konstante ist, wodurch sie zu den Kernformeln der Elektrodynamik wurden.

### Widerspruch zwischen Galilei-Transformation und Maxwell-Gleichungen
Die Newtonsche Mechanik, die die Galilei-Transformation verwendet, war über 200 Jahre lang die Grundlage der Physik, und die Maxwell-Gleichungen sind, wie bereits erwähnt, die Kerngleichungen zur Beschreibung elektrischer und magnetischer Phänomene. Zwischen den beiden gibt es jedoch folgende Widersprüche:

- Nach dem Relativitätsprinzip würde man erwarten, dass auch die Maxwell-Gleichungen in allen Inertialsystemen die gleiche Form haben, aber wenn man die in einem Inertialsystem gemessenen Werte mit der Galilei-Transformation in Werte umrechnet, die in einem anderen Inertialsystem gemessen wurden, nehmen die Maxwell-Gleichungen eine sehr unterschiedliche Form an.
- Aus den Maxwell-Gleichungen kann man die Größe der Lichtgeschwindigkeit $c$ berechnen, und diese ist eine unveränderliche Konstante, aber nach der Newtonschen Mechanik und der Galilei-Transformation wird die Lichtgeschwindigkeit $c$ in verschiedenen Inertialsystemen unterschiedlich gemessen.

Daher passen die Maxwell-Gleichungen und die Galilei-Transformation nicht zusammen, und mindestens eine von beiden musste modifiziert werden. Dies bildete den Hintergrund für die Entstehung der später zu besprechenden **Lorentz-Transformation (Lorentz transformation)**.

## Äthertheorie und Michelson-Morley-Experiment
In der Physik des 19. Jahrhunderts nahm man an, dass Licht, wie andere Wellen wie Wasserwellen oder Schallwellen, durch ein hypothetisches Medium namens *Äther (aether)* übertragen wird, und man bemühte sich, die Existenz dieses Äthers nachzuweisen.

Nach der Äthertheorie wäre der Weltraum, selbst wenn er ein Vakuum wäre, mit Äther gefüllt, und durch die Erdumlaufbahn, die sich mit einer Geschwindigkeit von etwa 30 km/s relativ zur Sonne bewegt, würde ein Ätherwind entstehen, der die Erde durchquert.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Bildquelle*
> - Autor: Wikimedia-Benutzer [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Um diese Hypothese zu überprüfen, führte Michelson 1887 in Zusammenarbeit mit Morley das *Michelson-Morley-Experiment* durch, bei dem das folgende Interferometer verwendet wurde:  
![Michelson-Morley-Interferometer](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Bildquelle*
> - Autor: Albert Abraham Michelson mit Edward Morley
> - Lizenz: public domain

In diesem Experiment wird der Lichtstrahl durch einen halbdurchlässigen Spiegel in zwei Teile geteilt, die jeweils die beiden senkrecht zueinander stehenden Arme des Interferometers hin und zurück durchlaufen, insgesamt etwa 11 m zurücklegen und sich in der Mitte treffen. Dabei entstehen je nach Phasenunterschied der beiden Lichtstrahlen konstruktive oder destruktive Interferenzmuster. Nach der Äthertheorie sollte sich aufgrund der unterschiedlichen Lichtgeschwindigkeiten relativ zum Äther dieser Phasenunterschied ändern, was zu einer beobachtbaren Veränderung des Interferenzmusters führen sollte. Tatsächlich konnte jedoch keine Veränderung des Interferenzmusters beobachtet werden. Es gab mehrere Versuche, dieses experimentelle Ergebnis zu erklären, darunter schlugen FitzGerald und Lorentz die *Lorentz-FitzGerald-Kontraktion (Lorentz–FitzGerald contraction)* oder *Längenkontraktion (length contraction)* vor, die besagt, dass sich die Länge eines Objekts verkürzt, wenn es sich <u>relativ zum Äther bewegt</u>. Dies führte zur Lorentz-Transformation.

> Lorentz glaubte zu dieser Zeit an die Existenz des Äthers und dachte, dass die Längenkontraktion durch die relative Bewegung zum Äther verursacht würde. Später interpretierte Einstein mit seiner *Speziellen Relativitätstheorie (Theory of Special Relativity)* die wahre physikalische Bedeutung der Lorentz-Transformation und erklärte die Längenkontraktion nicht durch den Äther, sondern durch das Konzept der Raumzeit. Es wurde auch später gezeigt, dass der Äther nicht existiert.
{: .prompt-info }

## Lorentz-Transformation (Lorentz transformation)
### Herleitung der Lorentz-Transformation
Nehmen wir an, dass in der gleichen Situation wie bei der Galilei-Transformation (Gleichungen [$\ref{eqn:galilean_transform_x}$]~[$\ref{eqn:galilean_transform_t}$]) die korrekte Transformationsbeziehung zwischen $x$ und $x^{\prime}$, die nicht im Widerspruch zu den Maxwell-Gleichungen steht, wie folgt ist:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Hier ist $\gamma$ unabhängig von $x$ und $t$, kann aber eine Funktion von $\vec{v}$ sein. Die Gründe für diese Annahme sind:

- Damit die Ereignisse in $S$ und $S^{\prime}$ eins zu eins korrespondieren, müssen $x$ und $x^{\prime}$ in einer linearen Beziehung stehen.
- Da bekannt ist, dass die Galilei-Transformation in alltäglichen mechanischen Situationen korrekt ist, sollte sie durch Gleichung ($\ref{eqn:galilean_transform_x}$) angenähert werden können.
- Die Form sollte möglichst einfach sein.

Da physikalische Formeln in den Bezugssystemen $S$ und $S^{\prime}$ die gleiche Form haben müssen, sollte man, um $x$ durch $x^{\prime}$ und $t$ auszudrücken, nur das Vorzeichen von $\vec{v}$ (die Richtung der relativen Bewegung) ändern müssen, und da es zwischen den beiden Bezugssystemen außer dem Vorzeichen von $\vec{v}$ keinen Unterschied geben sollte, muss $\gamma$ gleich sein.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Wie bei der Galilei-Transformation gibt es keinen Grund, warum sich die zu $\vec{v}$ senkrechten Komponenten $y$ und $y^{\prime}$ sowie $z$ und $z^{\prime}$ unterscheiden sollten, daher setzen wir:

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Wenn wir nun Gleichung ($\ref{eqn:lorentz_transform_x}$) in ($\ref{eqn:lorentz_transform_x_inverse}$) einsetzen, erhalten wir:

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Nach $t^{\prime}$ aufgelöst ergibt sich:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Um nicht im Widerspruch zu den Maxwell-Gleichungen zu stehen, muss die Lichtgeschwindigkeit in beiden Bezugssystemen $c$ sein, was wir nutzen können, um $\gamma$ zu bestimmen. Wenn zum Zeitpunkt $t=0$ die Ursprünge beider Bezugssysteme am gleichen Ort waren, dann ist aufgrund dieser Anfangsbedingung $t^\prime = 0$. Stellen wir uns nun vor, dass zum Zeitpunkt $t=t^\prime=0$ am gemeinsamen Ursprung von $S$ und $S^\prime$ ein Lichtblitz auftrat und die Beobachter in jedem Bezugssystem die Geschwindigkeit dieses Lichts messen. In diesem Fall gilt im Bezugssystem $S$:

$$ x = ct \label{eqn:ct_S}\tag{9}$$

und im Bezugssystem $S^\prime$:

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Wenn wir $x$ und $t$ in dieser Gleichung mit Hilfe der Gleichungen ($\ref{eqn:lorentz_transform_x}$) und ($\ref{eqn:lorentz_transform_t}$) ersetzen, erhalten wir:

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Lösen wir diese Gleichung nach $x$ auf, ergibt sich:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Da wir jedoch aus Gleichung ($\ref{eqn:ct_S}$) wissen, dass $x=ct$, muss gelten:

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Daraus folgt:

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Wenn wir diese Gleichung für $\gamma$ als Funktion von $\vec{v}$ in die Gleichungen ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$) einsetzen, erhalten wir die endgültigen Transformationsgleichungen vom Bezugssystem $S$ zu $S^\prime$.

### Transformationsmatrix der Lorentz-Transformation

Die endgültigen Transformationsgleichungen, die wir erhalten haben, lauten:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} $$
- $$ y^\prime = y $$
- $$ z^\prime = z $$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} $$

Dies sind die **Lorentz-Transformationen (Lorentz transformations)**. Wenn wir $\vec{\beta}=\vec{v}/c$ setzen, können wir sie in Matrixform wie folgt darstellen:

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}.$$

Lorentz zeigte, dass bei Verwendung dieser Transformationsgleichungen die grundlegenden Formeln der Elektrodynamik in allen Inertialsystemen die gleiche Form haben. Außerdem können wir sehen, dass für Geschwindigkeiten $v$, die sehr klein im Vergleich zur Lichtgeschwindigkeit $c$ sind, $\gamma \to 1$ gilt, sodass die Lorentz-Transformation durch die Galilei-Transformation angenähert werden kann.

Für den allgemeinen Fall, in dem die Relativgeschwindigkeit von $S^\prime$ bezüglich des Inertialsystems $S$ $\vec{v}=v_x\hat{i}+v_y\hat{j}+v_z\hat{k}$ ist, $\vec{\beta}=\vec{v}/c$, und die in den beiden Bezugssystemen gemessenen Ortsvektoren jeweils $\vec{x}=x_1\hat{i}+x_2\hat{j}+x_3\hat{k}$ und $\vec{x^\prime}=x_1^\prime\hat{i}+x_2^\prime\hat{j}+x_3^\prime\hat{k}$ sind, kann die Lorentz-Transformation wie folgt geschrieben werden:

- $$ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $$
- $$ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $$

Oder:

$$ \begin{pmatrix}
\vec{x}^\prime \\ ct^\prime
\end{pmatrix}
= \begin{pmatrix}
\gamma & -\gamma\vec{\beta} \\
-\gamma\vec{\beta} & \gamma
\end{pmatrix}
\begin{pmatrix}
\vec{x} \\ ct
\end{pmatrix}.
$$
