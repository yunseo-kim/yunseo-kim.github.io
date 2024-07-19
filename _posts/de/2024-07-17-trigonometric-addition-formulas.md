---
title: "Additionstheoreme der trigonometrischen Funktionen"
description: >-
  Wir betrachten die Definition der trigonometrischen Funktionen und die Beziehungen zwischen ihnen, um daraus die Additionstheoreme der trigonometrischen Funktionen und abgeleitete Formeln herzuleiten.
categories: [Mathematics]
tags: [Trigonometry]
math: true
---

## Definition der trigonometrischen Funktionen
![Unit Circle and Radius Vector](/assets/img/trigonometry/definition.png)
Wie in der Abbildung gezeigt, sei $\theta$ die Größe des Winkels, den der Radiusvektor $\overline{OP}$ mit der positiven x-Achse bildet. Dann definieren wir:
$$
\begin{gather}\begin{split}
\sin \theta = \frac { y } { r } ,\; \cos \theta = \frac { x } { r } ,\; \tan \theta = \frac { y } { x } \\ \csc \theta = \frac { r } { y } ,\; \sec \theta = \frac { r } { x } ,\; \cot \theta = \frac { x } { y } \end{split}\end{gather}
$$
Diese Funktionen werden zusammen als trigonometrische Funktionen bezeichnet.

## Beziehungen zwischen trigonometrischen Funktionen
1. $$ \csc \theta = \frac { 1 } { \sin \theta } ,\; \sec \theta = \frac { 1 } { \cos \theta } ,\; \cot \theta = \frac { 1 } { \tan \theta } \tag{2}$$
2. $$ \tan \theta = \frac { \sin \theta } { \cos \theta } ,\; \cot \theta = \frac { \cos \theta } { \sin \theta } \tag{3}$$
3. $$ \tag{4} \begin{gather*}
\sin ^ { 2 } \theta + \cos ^ { 2 } \theta = 1 \\
\tan ^ { 2 } \theta + 1 = \sec ^ { 2 } \theta \\
1 + \cot ^ { 2 } \theta = \csc ^ { 2 } \theta 
\end{gather*} 
$$

## Additionstheoreme der trigonometrischen Funktionen
![Deriving the Trigonometric Addition Formulas](/assets/img/trigonometry/trigonometric-addition-formulas.png)
Wie in der Abbildung gezeigt, seien $P, Q, P^{\prime}, Q^{\prime}$ die Schnittpunkte des Einheitskreises mit vier Radiusvektoren, die mit der positiven x-Achse Winkel von $\alpha+\beta,\, 0,\, \alpha,\, -\beta$ bilden.

Die Koordinaten der beiden Punkte $P$ und $Q$ sind:

$$
P(\cos(\alpha+\beta), \sin(\alpha+\beta)),\; Q(1,0)
$$

Daher gilt:

$$
\begin{align*} \overline { P^ { \prime } Q^ { \prime } } ^2&= \{ \cos \alpha - \cos ( - \beta ) \} ^ { 2 } + \{ \sin \alpha - \sin ( - \beta ) \} ^ { 2 } \\
&= 2 - 2 \cos \alpha \cos ( - \beta ) - 2 \sin \alpha \sin ( - \beta ) \\
&= 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta. \end{align*}
$$

Da $\overline{PQ}=\overline{P^{\prime} Q^{\prime}}$, gilt $2 - 2 \cos ( \alpha + \beta ) = 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta.$

$$
 \therefore \cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta. \label{eqn:cos_1} \tag{5}
$$

Wenn wir in der obigen Gleichung $\beta$ durch $-\beta$ ersetzen und umformen, erhalten wir:

$$
\cos ( \alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta \label{eqn:cos_2} \tag{6}
$$

Da $\cos ( \frac { \pi } { 2 } - \theta ) = \sin \theta ,\, \sin ( \frac { \pi } { 2 } - \theta ) = \cos \theta$, gilt:

$$
\begin{align*} \sin ( \alpha + \beta ) &= \cos ( \frac { \pi } { 2 } - ( \alpha + \beta ) ) = \cos ( ( \frac { \pi } { 2 } - \alpha ) - \beta) \\ &= \cos ( \frac { \pi } { 2 } - x ) \cos \beta + \sin ( \frac { \pi } { 2 } - \alpha ) \sin \beta \\ &= \sin \alpha \cos \beta + \cos \alpha \sin \beta. \end{align*}
$$

$$
\therefore \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta. \label{eqn:sin_1} \tag{7}
$$

Wenn wir in dieser Gleichung $\beta$ durch $-\beta$ ersetzen und umformen, erhalten wir:

$$
\sin ( \alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta. \label{eqn:sin_2} \tag{8}
$$

Schließlich gilt:

$$
\tan ( \alpha + \beta ) = \frac { \sin ( \alpha + \beta ) } { \cos ( \alpha + \beta ) } = \frac { \sin \alpha \cos \beta + \cos \alpha \sin \beta } { \cos \alpha \cos \beta - \sin \alpha \sin \beta }
$$

Wenn wir Zähler und Nenner jeweils durch $\cos{\alpha} \cos{\beta}$ teilen und umformen, erhalten wir:

$$
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_1} \tag{9}
$$

Wenn wir in dieser Gleichung $\beta$ durch $-\beta$ ersetzen und umformen, erhalten wir:

$$
\tan ( \alpha - \beta ) = \frac { \tan \alpha - \tan \beta } { 1 + \tan \alpha \tan \beta } \label{eqn:tan_2} \tag{10}
$$

## Größe des spitzen Winkels zwischen zwei Geraden mit gegebenen Steigungen
![Angle formed by two lines](/assets/img/trigonometry/angle-formed-by-two-lines.png)
Mit Hilfe der Gleichung ($\ref{eqn:tan_2}$) können wir die Größe des spitzen Winkels zwischen zwei Geraden mit gegebenen Steigungen berechnen. Seien $\theta_{1}$ und $\theta_{2}$ die Winkel, die die beiden Geraden $y=mx+b$ und $y=m^{\prime} x+b^{\prime}$ mit der positiven x-Achse bilden. Dann gilt:

$$
\tan{\theta_{1}}=m,\, \tan{\theta_{2}}=m^{\prime}
$$

Wenn wir die Größe des spitzen Winkels zwischen den beiden Geraden mit $\theta$ bezeichnen, erhalten wir:

$$
\tag{11} \begin{align*}
\tan{\theta}&=\left\vert \tan{\theta_{2}-\theta_{1}} \right\vert=\left\vert \frac{\tan{\theta_2}-\tan{\theta_1}}{1+\tan{\theta_1}\tan{\theta_2}}\right\vert \\
&=\left\vert \frac{m-m^{\prime}}{1+mm^{\prime}} \right\vert.
\end{align*}
$$