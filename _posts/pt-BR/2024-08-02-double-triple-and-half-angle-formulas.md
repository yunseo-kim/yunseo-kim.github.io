---
title: "Fórmulas de Ângulo Múltiplo e Meio Ângulo"
description: >-
  Examinamos as fórmulas de ângulo duplo e triplo e as derivamos das Fórmulas de Adição Trigonométrica. Também derivamos as fórmulas de meio ângulo a partir das fórmulas de ângulo duplo.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Multiple-Angle Formulas, Half-Angle Formulas]
math: true
---

## TL;DR
> **Fórmulas de Ângulo Duplo**
>
> - $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
> - $$ \begin{align*} 
> \cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
> &= 2\cos^{2}\alpha - 1 \\
> &= 1 - 2\sin^{2}\alpha \end{align*} $$
> - $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$
{: .prompt-info }

> **Fórmulas de Ângulo Triplo**
>
> - $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
> - $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$
{: .prompt-info }

> **Fórmulas de Meio Ângulo**
>
> - $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
> - $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
> - $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
> - $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$
{: .prompt-info }

## Pré-requisitos
- [[Fórmulas de Adição Trigonométrica]](/posts/trigonometric-addition-formulas)

## Fórmulas de Ângulo Múltiplo
### Fórmulas de Ângulo Duplo
- $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
- $$ \begin{align*} 
\cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
&= 2\cos^{2}\alpha - 1 \\
&= 1 - 2\sin^{2}\alpha \end{align*} $$
- $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$

#### Derivação
Podemos derivar as fórmulas de ângulo duplo a partir das [Fórmulas de Adição Trigonométrica](/posts/trigonometric-addition-formulas).

$$ \begin{gather} \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \label{eqn:sin_add} \\
\cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \label{eqn:cos_add} \\
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_add} \end{gather} $$

Substituindo $\beta$ por $\alpha$:

Da equação ($\ref{eqn:sin_add}$)

$$\sin 2\alpha = 2\sin \alpha \cos \alpha$$

Da equação ($\ref{eqn:cos_add}$)

$$\begin{align*} \cos 2 \alpha &= \cos ^ { 2 } \alpha - \sin ^ { 2 } \alpha \\ &= 2 \cos ^ { 2 } \alpha - 1 \\ &= 1 - 2 \sin ^ { 2 } \alpha \end{align*}$$

Da equação ($\ref{eqn:tan_add}$)

$$ \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2} \alpha} $$

### Fórmulas de Ângulo Triplo
- $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
- $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$

#### Derivação
Usando $\sin 2\alpha = 2\sin\alpha \cos\alpha$ e $\cos 2 \alpha = 1 - 2\sin^{2}\alpha$:

$$ \begin{align*} \sin 3 \alpha &= \sin ( \alpha + 2 \alpha ) = \sin \alpha \cos 2 \alpha + \cos \alpha \sin 2 \alpha \\ &= \sin \alpha ( 1 - 2 \sin ^ { 2 } \alpha ) + \cos \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \sin a ( 1 - 2 \sin ^ { 2 } \alpha ) + 2 \sin \alpha ( 1 - \sin ^ { 2 } \alpha ) \\ &= 3 \sin \alpha - 4 \sin ^ { 3 } \alpha . \end{align*} $$

Da mesma forma, usando $\sin 2\alpha = 2\sin\alpha \cos\alpha$ e $\cos 2 \alpha = 2\cos^{2}\alpha - 1$:

$$ \begin{align*} \cos 3 \alpha &= \cos ( \alpha + 2 \alpha ) = \cos \alpha \cos 2 \alpha - \sin \alpha \sin 2 \alpha \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - \sin \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - 2 \cos \alpha ( 1 - \cos ^ { 2 } \alpha ) \\ &= 4 \cos ^ { 3 } \alpha - 3 \cos \alpha \end{align*} $$

## Fórmulas de Meio Ângulo
- $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
- $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
- $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
- $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$

#### Derivação
Da fórmula de ângulo duplo $\cos 2\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$, substituindo $\alpha$ por $\frac{\alpha}{2}$:

$$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} = 2 \cos^{2}\frac{\alpha}{2} - 1 .$$

De $ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} $:

$$ \sin^{2}\frac{\alpha}{2}=\frac{1-\cos \alpha}{2} .$$

De $ \cos \alpha = 2 \cos^{2}\frac{\alpha}{2} - 1 $:

$$ \cos^{2}\frac{\alpha}{2}=\frac{1+\cos \alpha}{2} .$$

A partir disso, podemos mostrar que:

$$ \tan ^ { 2 } \frac { \alpha } { 2 } = \left . \left( \sin ^ { 2 } \frac{\alpha}{2}\right) \middle/ \left( \cos ^ { 2 } \frac { \alpha } { 2 } \right) \right . = \frac { 1 - \cos \alpha } { 1 + \cos \alpha } $$

E também:

$$ \tan \frac { \alpha } { 2 } = \frac { \sin \frac { \alpha } { 2 } } { \cos \frac { \alpha } { 2 } } = \frac { 2 \sin \frac { \alpha } { 2 } \cos \frac { \alpha } { 2 } } { 2 \cos ^ { 2 } \frac { \alpha } { 2 } } = \frac { \sin \alpha } { 1 + \cos \alpha } $$
