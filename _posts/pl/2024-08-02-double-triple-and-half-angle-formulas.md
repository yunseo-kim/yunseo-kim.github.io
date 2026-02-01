---
title: Wzory na wielokrotność i połowę kąta (Multiple-Angle and Half-Angle Formulas)
description: Omawiamy wzory na podwojenie i potrojenie kąta oraz wyprowadzamy je z twierdzeń o dodawaniu funkcji trygonometrycznych. Następnie z wzorów na podwojenie kąta wyprowadzamy także wzory na połowę kąta.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Multiple-Angle Formulas, Half-Angle Formulas]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Wzory na podwojenie kąta (Double-Angle Formulas)**
>
> - $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
> - $$ \begin{align*} 
> \cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
> &= 2\cos^{2}\alpha - 1 \\
> &= 1 - 2\sin^{2}\alpha \end{align*} $$
> - $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$
{: .prompt-info }

> **Wzory na potrojenie kąta (Triple-Angle Formulas)**
>
> - $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
> - $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$
{: .prompt-info }

> **Wzory na połowę kąta (Half-Angle Formulas)**
>
> - $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
> - $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
> - $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
> - $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$
{: .prompt-info }

## Wymagania wstępne
- [Twierdzenia o dodawaniu funkcji trygonometrycznych](/posts/trigonometric-addition-formulas)

## Wzory na wielokrotność kąta
### Wzory na podwojenie kąta
- $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
- $$ \begin{align*} 
\cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
&= 2\cos^{2}\alpha - 1 \\
&= 1 - 2\sin^{2}\alpha \end{align*} $$
- $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$

#### Wyprowadzenie
Wzory na podwojenie kąta można wyprowadzić z [twierdzeń o dodawaniu funkcji trygonometrycznych](/posts/trigonometric-addition-formulas).

$$ \begin{gather} \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \label{eqn:sin_add} \\
\cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \label{eqn:cos_add} \\
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_add} \end{gather} $$

Po podstawieniu $\alpha$ w miejsce $\beta$:

Z równania ($\ref{eqn:sin_add}$):

$$\sin 2\alpha = 2\sin \alpha \cos \alpha$$

Z równania ($\ref{eqn:cos_add}$):

$$\begin{align*} \cos 2 \alpha &= \cos ^ { 2 } \alpha - \sin ^ { 2 } \alpha \\ &= 2 \cos ^ { 2 } \alpha - 1 \\ &= 1 - 2 \sin ^ { 2 } \alpha \end{align*}$$

Z równania ($\ref{eqn:tan_add}$):

$$ \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2} \alpha} $$

### Wzory na potrojenie kąta
- $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
- $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$

#### Wyprowadzenie
Korzystając z $\sin 2\alpha = 2\sin\alpha \cos\alpha$ oraz $\cos 2 \alpha = 1 - 2\sin^{2}\alpha$, otrzymujemy

$$ \begin{align*} \sin 3 \alpha &= \sin ( \alpha + 2 \alpha ) = \sin \alpha \cos 2 \alpha + \cos \alpha \sin 2 \alpha \\ &= \sin \alpha ( 1 - 2 \sin ^ { 2 } \alpha ) + \cos \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \sin a ( 1 - 2 \sin ^ { 2 } \alpha ) + 2 \sin \alpha ( 1 - \sin ^ { 2 } \alpha ) \\ &= 3 \sin \alpha - 4 \sin ^ { 3 } \alpha . \end{align*} $$

Analogicznie, korzystając z $\sin 2\alpha = 2\sin\alpha \cos\alpha$ oraz $\cos 2 \alpha = 2\cos^{2}\alpha - 1$, dostajemy

$$ \begin{align*} \cos 3 \alpha &= \cos ( \alpha + 2 \alpha ) = \cos \alpha \cos 2 \alpha - \sin \alpha \sin 2 \alpha \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - \sin \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - 2 \cos \alpha ( 1 - \cos ^ { 2 } \alpha ) \\ &= 4 \cos ^ { 3 } \alpha - 3 \cos \alpha \end{align*} $$

## Wzory na połowę kąta
- $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
- $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
- $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
- $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$

#### Wyprowadzenie
Wzór na podwojenie kąta $\cos 2\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$: po podstawieniu $\frac{\alpha}{2}$ w miejsce $\alpha$ otrzymujemy

$$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} = 2 \cos^{2}\frac{\alpha}{2} - 1 .$$

Z $ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} $ wynika

$$ \sin^{2}\frac{\alpha}{2}=\frac{1-\cos \alpha}{2} .$$

Z $ \cos \alpha = 2 \cos^{2}\frac{\alpha}{2} - 1 $ wynika

$$ \cos^{2}\frac{\alpha}{2}=\frac{1+\cos \alpha}{2} .$$

Stąd

$$ \tan ^ { 2 } \frac { \alpha } { 2 } = \left . \left( \sin ^ { 2 } \frac{\alpha}{2}\right) \middle/ \left( \cos ^ { 2 } \frac { \alpha } { 2 } \right) \right . = \frac { 1 - \cos \alpha } { 1 + \cos \alpha } $$

oraz

$$ \tan \frac { \alpha } { 2 } = \frac { \sin \frac { \alpha } { 2 } } { \cos \frac { \alpha } { 2 } } = \frac { 2 \sin \frac { \alpha } { 2 } \cos \frac { \alpha } { 2 } } { 2 \cos ^ { 2 } \frac { \alpha } { 2 } } = \frac { \sin \alpha } { 1 + \cos \alpha } $$

również zachodzi.
