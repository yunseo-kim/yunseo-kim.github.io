---
title: Sčítací vzorce pro goniometrické funkce
description: Probereme definice goniometrických funkcí a vztahy mezi nimi a z nich odvodíme sčítací vzorce a související odvozené formule.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Definice goniometrických funkcí
![Unit Circle and Radius Vector](/assets/img/trigonometry/definition.png)
Jak je na obrázku, nechť velikost úhlu, který svírá průvodič $\overline{OP}$ s kladným směrem osy $x$, je $\theta$. Potom definujeme
$$
\begin{gather}\begin{split}
\sin \theta = \frac { y } { r } ,\; \cos \theta = \frac { x } { r } ,\; \tan \theta = \frac { y } { x } \\ \csc \theta = \frac { r } { y } ,\; \sec \theta = \frac { r } { x } ,\; \cot \theta = \frac { x } { y } \end{split}\end{gather}
$$
a souhrnně jim říkáme goniometrické funkce.

## Vztahy mezi goniometrickými funkcemi
1. $$ \csc \theta = \frac { 1 } { \sin \theta } ,\; \sec \theta = \frac { 1 } { \cos \theta } ,\; \cot \theta = \frac { 1 } { \tan \theta } \tag{2}$$
2. $$ \tan \theta = \frac { \sin \theta } { \cos \theta } ,\; \cot \theta = \frac { \cos \theta } { \sin \theta } \tag{3}$$
3. $$ \tag{4} \begin{gather*}
\sin ^ { 2 } \theta + \cos ^ { 2 } \theta = 1 \\
\tan ^ { 2 } \theta + 1 = \sec ^ { 2 } \theta \\
1 + \cot ^ { 2 } \theta = \csc ^ { 2 } \theta 
\end{gather*} 
$$

## Sčítací vzorce pro goniometrické funkce
![Deriving the Trigonometric Addition Formulas](/assets/img/trigonometry/trigonometric-addition-formulas.png)
Jak je na obrázku, označme $P, Q, P^{\prime}, Q^{\prime}$ body, v nichž se jednotková kružnice protíná se čtyřmi průvodiči, které svírají s kladným směrem osy $x$ úhly $\alpha+\beta,\, 0,\, \alpha,\, -\beta$.

Souřadnice bodů $P, Q$ jsou

$$
P(\cos(\alpha+\beta), \sin(\alpha+\beta)),\; Q(1,0)
$$

tedy

$$
\begin{align*} \overline { P^ { \prime } Q^ { \prime } } ^2&= \{ \cos \alpha - \cos ( - \beta ) \} ^ { 2 } + \{ \sin \alpha - \sin ( - \beta ) \} ^ { 2 } \\
&= 2 - 2 \cos \alpha \cos ( - \beta ) - 2 \sin \alpha \sin ( - \beta ) \\
&= 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta. \end{align*}
$$

Protože $\overline{PQ}=\overline{P^{\prime} Q^{\prime}}$, platí $2 - 2 \cos ( \alpha + \beta ) = 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta.$

$$
 \therefore \cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta. \label{eqn:cos_1} \tag{5}
$$

Dosadíme-li do výše uvedeného vztahu za $\beta$ hodnotu $-\beta$ a upravíme, dostaneme

$$
\cos ( \alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta \label{eqn:cos_2} \tag{6}
$$

Jelikož $\cos ( \frac { \pi } { 2 } - \theta ) = \sin \theta ,\, \sin ( \frac { \pi } { 2 } - \theta ) = \cos \theta$, máme

$$
\begin{align*} \sin ( \alpha + \beta ) &= \cos ( \frac { \pi } { 2 } - ( \alpha + \beta ) ) = \cos ( ( \frac { \pi } { 2 } - \alpha ) - \beta) \\ &= \cos ( \frac { \pi } { 2 } - x ) \cos \beta + \sin ( \frac { \pi } { 2 } - \alpha ) \sin \beta \\ &= \sin \alpha \cos \beta + \cos \alpha \sin \beta. \end{align*}
$$

$$
\therefore \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta. \label{eqn:sin_1} \tag{7}
$$

Dosadíme-li do tohoto vztahu za $\beta$ hodnotu $-\beta$ a upravíme, vyjde

$$
\sin ( \alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta. \label{eqn:sin_2} \tag{8}
$$

Nakonec,

$$
\tan ( \alpha + \beta ) = \frac { \sin ( \alpha + \beta ) } { \cos ( \alpha + \beta ) } = \frac { \sin \alpha \cos \beta + \cos \alpha \sin \beta } { \cos \alpha \cos \beta - \sin \alpha \sin \beta }
$$

po vydělení čitatele i jmenovatele výrazem $\cos{\alpha} \cos{\beta}$ a po úpravě dostaneme

$$
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_1} \tag{9}
$$

a po dosazení $-\beta$ za $\beta$ a úpravě

$$
\tan ( \alpha - \beta ) = \frac { \tan \alpha - \tan \beta } { 1 + \tan \alpha \tan \beta } \label{eqn:tan_2} \tag{10}
$$

## Velikost ostrého úhlu mezi dvěma přímkami se zadaným sklonem
![Angle formed by two lines](/assets/img/trigonometry/angle-formed-by-two-lines.png)
Pomocí vztahu ($\ref{eqn:tan_2}$) lze určit velikost ostrého úhlu mezi dvěma přímkami se zadaným sklonem. Nechť přímky $y=mx+b$, $y=m^{\prime} x+b^{\prime}$ svírají s kladným směrem osy $x$ úhly $\theta_{1}$, $\theta_{2}$. Pak

$$
\tan{\theta_{1}}=m,\, \tan{\theta_{2}}=m^{\prime}
$$

a označíme-li velikost ostrého úhlu mezi těmito dvěma přímkami jako $\theta$, platí

$$
\tag{11} \begin{align*}
\tan{\theta}&=\left\vert \tan{\theta_{2}-\theta_{1}} \right\vert=\left\vert \frac{\tan{\theta_2}-\tan{\theta_1}}{1+\tan{\theta_1}\tan{\theta_2}}\right\vert \\
&=\left\vert \frac{m-m^{\prime}}{1+mm^{\prime}} \right\vert.
\end{align*}
$$
