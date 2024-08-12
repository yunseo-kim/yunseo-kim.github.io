---
title: "Mehrfach- und Halbwinkelformeln (Multiple-Angle and Half-Angle Formulas)"
description: >-
  Wir betrachten die Formeln für den doppelten und dreifachen Winkel und leiten diese aus den trigonometrischen Additionstheoreme (Trigonometric Addition Formulas) ab. Außerdem leiten wir die Halbwinkelformeln aus den Formeln für den doppelten Winkel ab.
categories: [Mathematics]
tags: [Trigonometry]
math: true
---

## TL;DR
> **Formeln für den doppelten Winkel (Double-Angle Formulas)**
>
> - $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
> - $$ \begin{align*} 
> \cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
> &= 2\cos^{2}\alpha - 1 \\
> &= 1 - 2\sin^{2}\alpha \end{align*} $$
> - $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$
{: .prompt-info }

> **Formeln für den dreifachen Winkel (Triple-Angle Formulas)**
>
> - $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
> - $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$
{: .prompt-info }

> **Halbwinkelformeln (Half-Angle Formulas)**
>
> - $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
> - $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
> - $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
> - $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$
{: .prompt-info }

## Voraussetzungen
- [[Trigonometrische Additionstheoreme]](/posts/trigonometric-addition-formulas)

## Mehrfachwinkelformeln
### Formeln für den doppelten Winkel
- $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
- $$ \begin{align*} 
\cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
&= 2\cos^{2}\alpha - 1 \\
&= 1 - 2\sin^{2}\alpha \end{align*} $$
- $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$

#### Herleitung
Wir können die Formeln für den doppelten Winkel aus den [trigonometrischen Additionstheoremen](/posts/trigonometric-addition-formulas) herleiten.

$$ \begin{gather} \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \label{eqn:sin_add} \\
\cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \label{eqn:cos_add} \\
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_add} \end{gather} $$

Wenn wir $\beta$ durch $\alpha$ ersetzen, erhalten wir:

Aus Gleichung ($\ref{eqn:sin_add}$):

$$\sin 2\alpha = 2\sin \alpha \cos \alpha$$

Aus Gleichung ($\ref{eqn:cos_add}$):

$$\begin{align*} \cos 2 \alpha &= \cos ^ { 2 } \alpha - \sin ^ { 2 } \alpha \\ &= 2 \cos ^ { 2 } \alpha - 1 \\ &= 1 - 2 \sin ^ { 2 } \alpha \end{align*}$$

Aus Gleichung ($\ref{eqn:tan_add}$):

$$ \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2} \alpha} $$

### Formeln für den dreifachen Winkel
- $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
- $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$

#### Herleitung
Mit Hilfe von $\sin 2\alpha = 2\sin\alpha \cos\alpha$ und $\cos 2 \alpha = 1 - 2\sin^{2}\alpha$ erhalten wir:

$$ \begin{align*} \sin 3 \alpha &= \sin ( \alpha + 2 \alpha ) = \sin \alpha \cos 2 \alpha + \cos \alpha \sin 2 \alpha \\ &= \sin \alpha ( 1 - 2 \sin ^ { 2 } \alpha ) + \cos \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \sin a ( 1 - 2 \sin ^ { 2 } \alpha ) + 2 \sin \alpha ( 1 - \sin ^ { 2 } \alpha ) \\ &= 3 \sin \alpha - 4 \sin ^ { 3 } \alpha . \end{align*} $$

Auf ähnliche Weise können wir mit $\sin 2\alpha = 2\sin\alpha \cos\alpha$ und $\cos 2 \alpha = 2\cos^{2}\alpha - 1$ herleiten:

$$ \begin{align*} \cos 3 \alpha &= \cos ( \alpha + 2 \alpha ) = \cos \alpha \cos 2 \alpha - \sin \alpha \sin 2 \alpha \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - \sin \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - 2 \cos \alpha ( 1 - \cos ^ { 2 } \alpha ) \\ &= 4 \cos ^ { 3 } \alpha - 3 \cos \alpha \end{align*} $$

## Halbwinkelformeln
- $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
- $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
- $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
- $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$

#### Herleitung
Wenn wir in der Formel für den doppelten Winkel $\cos 2\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$ $\alpha$ durch $\frac{\alpha}{2}$ ersetzen, erhalten wir:

$$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} = 2 \cos^{2}\frac{\alpha}{2} - 1 .$$

Aus $ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} $ folgt:

$$ \sin^{2}\frac{\alpha}{2}=\frac{1-\cos \alpha}{2} .$$

Aus $ \cos \alpha = 2 \cos^{2}\frac{\alpha}{2} - 1 $ folgt:

$$ \cos^{2}\frac{\alpha}{2}=\frac{1+\cos \alpha}{2} .$$

Daraus können wir ableiten:

$$ \tan ^ { 2 } \frac { \alpha } { 2 } = \left . \left( \sin ^ { 2 } \frac{\alpha}{2}\right) \middle/ \left( \cos ^ { 2 } \frac { \alpha } { 2 } \right) \right . = \frac { 1 - \cos \alpha } { 1 + \cos \alpha } $$

Außerdem gilt:

$$ \tan \frac { \alpha } { 2 } = \frac { \sin \frac { \alpha } { 2 } } { \cos \frac { \alpha } { 2 } } = \frac { 2 \sin \frac { \alpha } { 2 } \cos \frac { \alpha } { 2 } } { 2 \cos ^ { 2 } \frac { \alpha } { 2 } } = \frac { \sin \alpha } { 1 + \cos \alpha } $$