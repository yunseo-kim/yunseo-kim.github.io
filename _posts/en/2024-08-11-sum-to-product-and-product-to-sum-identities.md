---
title: "Product-to-Sum and Sum-to-Product Identities"
description: >-
  Explore formulas for transforming products of trigonometric functions into sums or differences, derive these formulas from trigonometric addition theorems, and then derive formulas for transforming sums or differences of trigonometric functions into products.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product Identities]
math: true
---

## TL;DR
> **Product-to-Sum Identities**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **Sum-to-Product Identities**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> It's beneficial to learn not only the formulas but also their derivation processes.
{: .prompt-tip }

## Prerequisites
- [Trigonometric Addition Formulas](/posts/trigonometric-addition-formulas)

## Product-to-Sum Identities
- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### Derivation
We use the [Trigonometric Addition Formulas](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

Adding ($\ref{eqn:sin_add}$) and ($\ref{eqn:sin_dif}$), we get

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

Subtracting ($\ref{eqn:sin_dif}$) from ($\ref{eqn:sin_add}$), we get

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

Similarly, using

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

Adding ($\ref{eqn:cos_add}$) and ($\ref{eqn:cos_dif}$), we get

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

Subtracting ($\ref{eqn:cos_dif}$) from ($\ref{eqn:cos_add}$), we get

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## Sum-to-Product Identities
- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### Derivation
We can derive the Sum-to-Product Identities from the Product-to-Sum Identities.

Let $$ \alpha + \beta = A, \quad \alpha - \beta = B $$

Solving these equations for $\alpha$ and $\beta$, we get

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

Substituting these into ($\ref{sin_product_to_sum}$), ($\ref{cos_product_to_dif}$), ($\ref{cos_product_to_sum}$), and ($\ref{sin_product_to_dif}$) respectively, we obtain the following formulas:

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
