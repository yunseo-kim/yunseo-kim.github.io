---
title: "Wzory na iloczyn jako sumę lub różnicę (tożsamości Product-to-Sum i Sum-to-Product)"
description: "Poznaj wzory przekształcające iloczyn funkcji trygonometrycznych do postaci sumy lub różnicy oraz ich wyprowadzenie z twierdzeń o dodawaniu. Następnie wyprowadzimy też wzory odwrotne: sumę lub różnicę do postaci iloczynu."
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product Identities]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR

> **Wzory przekształcające iloczyn do postaci sumy lub różnicy (Product-to-Sum Identities)**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **Wzory przekształcające sumę lub różnicę do postaci iloczynu (Sum-to-Product Identities)**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> Dobrze jest zapamiętać nie tylko same wzory, ale także proces ich wyprowadzenia.
{: .prompt-tip }

## Wymagania wstępne
- [Twierdzenia o dodawaniu funkcji trygonometrycznych](/posts/trigonometric-addition-formulas)

## Wzory przekształcające iloczyn do postaci sumy lub różnicy (Product-to-Sum Identities)
- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### Wyprowadzenie
[Twierdzenia o dodawaniu funkcji trygonometrycznych](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

korzystamy z tych równań.

Dodając ($\ref{eqn:sin_add}$)+($\ref{eqn:sin_dif}$), otrzymujemy

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

Odejmując ($\ref{eqn:sin_add}$)-($\ref{eqn:sin_dif}$), otrzymujemy

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

W analogiczny sposób, z

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

mamy:

Dodając ($\ref{eqn:cos_add}$)+($\ref{eqn:cos_dif}$), otrzymujemy

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

Odejmując ($\ref{eqn:cos_add}$)-($\ref{eqn:cos_dif}$), otrzymujemy

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## Wzory przekształcające sumę lub różnicę do postaci iloczynu (Sum-to-Product Identities)
- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### Wyprowadzenie
Z wzorów przekształcających iloczyn do postaci sumy lub różnicy (Product-to-Sum Identities) można również wyprowadzić wzory przekształcające sumę lub różnicę do postaci iloczynu (Sum-to-Product Identities).

Przyjmijmy

$$ \alpha + \beta = A, \quad \alpha - \beta = B $$

i rozwiążmy ten układ równań względem $\alpha$, $\beta$:

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

Podstawiając to kolejno do wcześniejszych równań ($\ref{sin_product_to_sum}$), ($\ref{cos_product_to_dif}$), ($\ref{cos_product_to_sum}$), ($\ref{sin_product_to_dif}$), otrzymujemy następujące wzory:

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
