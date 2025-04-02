---
title: Fórmulas de ángulo múltiple y medio ángulo
description: Examinamos las fórmulas de ángulo doble y triple, y las derivamos de
  las fórmulas de adición trigonométrica. También derivamos las fórmulas de medio
  ángulo a partir de las fórmulas de ángulo doble.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Multiple-Angle Formulas, Half-Angle Formulas]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Fórmulas de ángulo doble (Double-Angle Formulas)**
>
> - $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
> - $$ \begin{align*} 
> \cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
> &= 2\cos^{2}\alpha - 1 \\
> &= 1 - 2\sin^{2}\alpha \end{align*} $$
> - $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$
{: .prompt-info }

> **Fórmulas de ángulo triple (Triple-Angle Formulas)**
>
> - $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
> - $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$
{: .prompt-info }

> **Fórmulas de medio ángulo (Half-Angle Formulas)**
>
> - $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
> - $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
> - $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
> - $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$
{: .prompt-info }

## Prerrequisitos
- [Fórmulas de adición trigonométrica](/posts/trigonometric-addition-formulas)

## Fórmulas de ángulo múltiple
### Fórmulas de ángulo doble
- $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
- $$ \begin{align*} 
\cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
&= 2\cos^{2}\alpha - 1 \\
&= 1 - 2\sin^{2}\alpha \end{align*} $$
- $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$

#### Derivación
Podemos derivar las fórmulas de ángulo doble a partir de las [fórmulas de adición trigonométrica](/posts/trigonometric-addition-formulas).

$$ \begin{gather} \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \label{eqn:sin_add} \\
\cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \label{eqn:cos_add} \\
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_add} \end{gather} $$

Si sustituimos $\alpha$ por $\beta$,

De la ecuación ($\ref{eqn:sin_add}$)

$$\sin 2\alpha = 2\sin \alpha \cos \alpha$$

De la ecuación ($\ref{eqn:cos_add}$)

$$\begin{align*} \cos 2 \alpha &= \cos ^ { 2 } \alpha - \sin ^ { 2 } \alpha \\ &= 2 \cos ^ { 2 } \alpha - 1 \\ &= 1 - 2 \sin ^ { 2 } \alpha \end{align*}$$

De la ecuación ($\ref{eqn:tan_add}$)

$$ \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2} \alpha} $$

### Fórmulas de ángulo triple
- $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
- $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$

#### Derivación
Usando $\sin 2\alpha = 2\sin\alpha \cos\alpha$ y $\cos 2 \alpha = 1 - 2\sin^{2}\alpha$,

$$ \begin{align*} \sin 3 \alpha &= \sin ( \alpha + 2 \alpha ) = \sin \alpha \cos 2 \alpha + \cos \alpha \sin 2 \alpha \\ &= \sin \alpha ( 1 - 2 \sin ^ { 2 } \alpha ) + \cos \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \sin a ( 1 - 2 \sin ^ { 2 } \alpha ) + 2 \sin \alpha ( 1 - \sin ^ { 2 } \alpha ) \\ &= 3 \sin \alpha - 4 \sin ^ { 3 } \alpha . \end{align*} $$

De manera similar, usando $\sin 2\alpha = 2\sin\alpha \cos\alpha$ y $\cos 2 \alpha = 2\cos^{2}\alpha - 1$,

$$ \begin{align*} \cos 3 \alpha &= \cos ( \alpha + 2 \alpha ) = \cos \alpha \cos 2 \alpha - \sin \alpha \sin 2 \alpha \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - \sin \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - 2 \cos \alpha ( 1 - \cos ^ { 2 } \alpha ) \\ &= 4 \cos ^ { 3 } \alpha - 3 \cos \alpha \end{align*} $$

## Fórmulas de medio ángulo
- $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
- $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
- $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
- $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$

#### Derivación
De la fórmula de ángulo doble $\cos 2\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$, sustituyendo $\frac{\alpha}{2}$ por $\alpha$,

$$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} = 2 \cos^{2}\frac{\alpha}{2} - 1 .$$

De $ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} $,

$$ \sin^{2}\frac{\alpha}{2}=\frac{1-\cos \alpha}{2} .$$

De $ \cos \alpha = 2 \cos^{2}\frac{\alpha}{2} - 1 $,

$$ \cos^{2}\frac{\alpha}{2}=\frac{1+\cos \alpha}{2} .$$

De esto, podemos demostrar que

$$ \tan ^ { 2 } \frac { \alpha } { 2 } = \left . \left( \sin ^ { 2 } \frac{\alpha}{2}\right) \middle/ \left( \cos ^ { 2 } \frac { \alpha } { 2 } \right) \right . = \frac { 1 - \cos \alpha } { 1 + \cos \alpha } $$

y también que

$$ \tan \frac { \alpha } { 2 } = \frac { \sin \frac { \alpha } { 2 } } { \cos \frac { \alpha } { 2 } } = \frac { 2 \sin \frac { \alpha } { 2 } \cos \frac { \alpha } { 2 } } { 2 \cos ^ { 2 } \frac { \alpha } { 2 } } = \frac { \sin \alpha } { 1 + \cos \alpha } $$

se cumple.
