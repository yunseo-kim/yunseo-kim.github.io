---
title: Kanuni za pembe maradufu, mara tatu, na nusu
description: Tunaangalia kanuni za pembe maradufu na pembe mara tatu, na kuzipata kutoka kwa kanuni za kujumlisha za trigonometria. Kisha pia tunapata kanuni za pembe nusu kutoka kwa kanuni za pembe maradufu.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Multiple-Angle Formulas, Half-Angle Formulas]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Kanuni za pembe maradufu**
>
> - $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
> - $$ \begin{align*} 
> \cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
> &= 2\cos^{2}\alpha - 1 \\
> &= 1 - 2\sin^{2}\alpha \end{align*} $$
> - $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$
{: .prompt-info }

> **Kanuni za pembe mara tatu**
>
> - $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
> - $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$
{: .prompt-info }

> **Kanuni za pembe nusu**
>
> - $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
> - $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
> - $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
> - $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$
{: .prompt-info }

## Maarifa ya awali
- [Kanuni za kujumlisha za trigonometria](/posts/trigonometric-addition-formulas)

## Kanuni za pembe za mara nyingi
### Kanuni za pembe maradufu
- $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
- $$ \begin{align*} 
\cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
&= 2\cos^{2}\alpha - 1 \\
&= 1 - 2\sin^{2}\alpha \end{align*} $$
- $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$

#### Utoaji
Kutoka kwa [kanuni za kujumlisha za trigonometria](/posts/trigonometric-addition-formulas), tunaweza kupata kanuni za pembe maradufu.

$$ \begin{gather} \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \label{eqn:sin_add} \\
\cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \label{eqn:cos_add} \\
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_add} \end{gather} $$

Tukiweka $\alpha$ badala ya $\beta$,

katika fomula ($\ref{eqn:sin_add}$),

$$\sin 2\alpha = 2\sin \alpha \cos \alpha$$

katika fomula ($\ref{eqn:cos_add}$),

$$\begin{align*} \cos 2 \alpha &= \cos ^ { 2 } \alpha - \sin ^ { 2 } \alpha \\ &= 2 \cos ^ { 2 } \alpha - 1 \\ &= 1 - 2 \sin ^ { 2 } \alpha \end{align*}$$

na katika fomula ($\ref{eqn:tan_add}$),

$$ \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2} \alpha} $$

### Kanuni za pembe mara tatu
- $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
- $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$

#### Utoaji
Kwa kutumia $\sin 2\alpha = 2\sin\alpha \cos\alpha$ na $\cos 2 \alpha = 1 - 2\sin^{2}\alpha$,

$$ \begin{align*} \sin 3 \alpha &= \sin ( \alpha + 2 \alpha ) = \sin \alpha \cos 2 \alpha + \cos \alpha \sin 2 \alpha \\ &= \sin \alpha ( 1 - 2 \sin ^ { 2 } \alpha ) + \cos \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \sin a ( 1 - 2 \sin ^ { 2 } \alpha ) + 2 \sin \alpha ( 1 - \sin ^ { 2 } \alpha ) \\ &= 3 \sin \alpha - 4 \sin ^ { 3 } \alpha . \end{align*} $$

Kwa njia hiyo hiyo, tukitumia $\sin 2\alpha = 2\sin\alpha \cos\alpha$ na $\cos 2 \alpha = 2\cos^{2}\alpha - 1$,

$$ \begin{align*} \cos 3 \alpha &= \cos ( \alpha + 2 \alpha ) = \cos \alpha \cos 2 \alpha - \sin \alpha \sin 2 \alpha \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - \sin \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - 2 \cos \alpha ( 1 - \cos ^ { 2 } \alpha ) \\ &= 4 \cos ^ { 3 } \alpha - 3 \cos \alpha \end{align*} $$

## Kanuni za pembe nusu
- $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
- $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
- $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
- $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$

#### Utoaji
Katika kanuni ya pembe maradufu $\cos 2\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$, tukiweka $\frac{\alpha}{2}$ badala ya $\alpha$,

$$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} = 2 \cos^{2}\frac{\alpha}{2} - 1 .$$

Kutoka kwa $ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} $,

$$ \sin^{2}\frac{\alpha}{2}=\frac{1-\cos \alpha}{2} .$$

Kutoka kwa $ \cos \alpha = 2 \cos^{2}\frac{\alpha}{2} - 1 $,

$$ \cos^{2}\frac{\alpha}{2}=\frac{1+\cos \alpha}{2} .$$

Kutokana na hili,

$$ \tan ^ { 2 } \frac { \alpha } { 2 } = \left . \left( \sin ^ { 2 } \frac{\alpha}{2}\right) \middle/ \left( \cos ^ { 2 } \frac { \alpha } { 2 } \right) \right . = \frac { 1 - \cos \alpha } { 1 + \cos \alpha } $$

inaweza kuonyeshwa, na pia

$$ \tan \frac { \alpha } { 2 } = \frac { \sin \frac { \alpha } { 2 } } { \cos \frac { \alpha } { 2 } } = \frac { 2 \sin \frac { \alpha } { 2 } \cos \frac { \alpha } { 2 } } { 2 \cos ^ { 2 } \frac { \alpha } { 2 } } = \frac { \sin \alpha } { 1 + \cos \alpha } $$

pia ni kweli.
