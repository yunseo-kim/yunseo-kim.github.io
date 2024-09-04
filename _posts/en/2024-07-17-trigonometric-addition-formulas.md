---
title: "Addition Formulas for Trigonometric Functions"
description: >-
  Examine the definitions of trigonometric functions and the relationships between them, and derive the addition formulas for trigonometric functions and their derivative formulas.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas]
math: true
---

## Definition of Trigonometric Functions
![Unit Circle and Radius Vector](/assets/img/trigonometry/definition.png)
As shown in the figure, when the angle between the radius vector $\overline{OP}$ and the positive direction of the $x$-axis is $\theta$,
$$
\begin{gather}\begin{split}
\sin \theta = \frac { y } { r } ,\; \cos \theta = \frac { x } { r } ,\; \tan \theta = \frac { y } { x } \\ \csc \theta = \frac { r } { y } ,\; \sec \theta = \frac { r } { x } ,\; \cot \theta = \frac { x } { y } \end{split}\end{gather}
$$
are defined as such, and collectively called trigonometric functions.

## Relationships Between Trigonometric Functions
1. $$ \csc \theta = \frac { 1 } { \sin \theta } ,\; \sec \theta = \frac { 1 } { \cos \theta } ,\; \cot \theta = \frac { 1 } { \tan \theta } \tag{2}$$
2. $$ \tan \theta = \frac { \sin \theta } { \cos \theta } ,\; \cot \theta = \frac { \cos \theta } { \sin \theta } \tag{3}$$
3. $$ \tag{4} \begin{gather*}
\sin ^ { 2 } \theta + \cos ^ { 2 } \theta = 1 \\
\tan ^ { 2 } \theta + 1 = \sec ^ { 2 } \theta \\
1 + \cot ^ { 2 } \theta = \csc ^ { 2 } \theta 
\end{gather*} 
$$

## Addition Formulas for Trigonometric Functions
![Deriving the Trigonometric Addition Formulas](/assets/img/trigonometry/trigonometric-addition-formulas.png)
As shown in the figure, let $P, Q, P^{\prime}, Q^{\prime}$ be the points where four radius vectors forming angles of $\alpha+\beta,\, 0,\, \alpha,\, -\beta$ with the positive direction of the $x$-axis intersect the unit circle.

The coordinates of the two points $P, Q$ are

$$
P(\cos(\alpha+\beta), \sin(\alpha+\beta)),\; Q(1,0)
$$

therefore

$$
\begin{align*} \overline { P^ { \prime } Q^ { \prime } } ^2&= \{ \cos \alpha - \cos ( - \beta ) \} ^ { 2 } + \{ \sin \alpha - \sin ( - \beta ) \} ^ { 2 } \\
&= 2 - 2 \cos \alpha \cos ( - \beta ) - 2 \sin \alpha \sin ( - \beta ) \\
&= 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta. \end{align*}
$$

Since $\overline{PQ}=\overline{P^{\prime} Q^{\prime}}$, $2 - 2 \cos ( \alpha + \beta ) = 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta.$

$$
 \therefore \cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta. \label{eqn:cos_1} \tag{5}
$$

Substituting $-\beta$ for $\beta$ in the above equation and simplifying:

$$
\cos ( \alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta \label{eqn:cos_2} \tag{6}
$$

Since $\cos ( \frac { \pi } { 2 } - \theta ) = \sin \theta ,\, \sin ( \frac { \pi } { 2 } - \theta ) = \cos \theta$,

$$
\begin{align*} \sin ( \alpha + \beta ) &= \cos ( \frac { \pi } { 2 } - ( \alpha + \beta ) ) = \cos ( ( \frac { \pi } { 2 } - \alpha ) - \beta) \\ &= \cos ( \frac { \pi } { 2 } - x ) \cos \beta + \sin ( \frac { \pi } { 2 } - \alpha ) \sin \beta \\ &= \sin \alpha \cos \beta + \cos \alpha \sin \beta. \end{align*}
$$

$$
\therefore \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta. \label{eqn:sin_1} \tag{7}
$$

Substituting $-\beta$ for $\beta$ in this equation and simplifying:

$$
\sin ( \alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta. \label{eqn:sin_2} \tag{8}
$$

Finally,

$$
\tan ( \alpha + \beta ) = \frac { \sin ( \alpha + \beta ) } { \cos ( \alpha + \beta ) } = \frac { \sin \alpha \cos \beta + \cos \alpha \sin \beta } { \cos \alpha \cos \beta - \sin \alpha \sin \beta }
$$

Dividing both numerator and denominator by $\cos{\alpha} \cos{\beta}$ and simplifying:

$$
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_1} \tag{9}
$$

Substituting $-\beta$ for $\beta$ in this equation and simplifying:

$$
\tan ( \alpha - \beta ) = \frac { \tan \alpha - \tan \beta } { 1 + \tan \alpha \tan \beta } \label{eqn:tan_2} \tag{10}
$$

## Acute Angle Formed by Two Lines with Given Slopes
![Angle formed by two lines](/assets/img/trigonometry/angle-formed-by-two-lines.png)
Using equation ($\ref{eqn:tan_2}$), we can find the size of the acute angle formed by two lines with given slopes. If $\theta_{1}$ and $\theta_{2}$ are the angles that two lines $y=mx+b$ and $y=m^{\prime} x+b^{\prime}$ make with the positive direction of the $x$-axis, respectively, then

$$
\tan{\theta_{1}}=m,\, \tan{\theta_{2}}=m^{\prime}
$$

Therefore, if $\theta$ is the size of the acute angle formed by the two lines,

$$
\tag{11} \begin{align*}
\tan{\theta}&=\left\vert \tan{\theta_{2}-\theta_{1}} \right\vert=\left\vert \frac{\tan{\theta_2}-\tan{\theta_1}}{1+\tan{\theta_1}\tan{\theta_2}}\right\vert \\
&=\left\vert \frac{m-m^{\prime}}{1+mm^{\prime}} \right\vert.
\end{align*}
$$
