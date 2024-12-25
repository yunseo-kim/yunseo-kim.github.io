---
title: Fórmulas de Produto para Soma e Soma para Produto (Product-to-Sum and Sum-to-Product
  Identities)
description: Explore as fórmulas para transformar produtos de funções trigonométricas
  em somas ou diferenças, derivando essas fórmulas a partir dos teoremas de adição
  trigonométrica. Além disso, derive fórmulas para transformar somas ou diferenças
  de funções trigonométricas em produtos.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product
    Identities]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Fórmulas de Produto para Soma (Product-to-Sum Identities)**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **Fórmulas de Soma para Produto (Sum-to-Product Identities)**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> É bom memorizar não apenas as fórmulas, mas também o processo de derivação.
{: .prompt-tip }

## Pré-requisitos
- [Fórmulas de adição trigonométrica](/posts/trigonometric-addition-formulas)

## Fórmulas de Produto para Soma (Product-to-Sum Identities)
- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### Derivação
Usamos as [fórmulas de adição trigonométrica](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

Somando ($\ref{eqn:sin_add}$) e ($\ref{eqn:sin_dif}$), temos

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

Subtraindo ($\ref{eqn:sin_dif}$) de ($\ref{eqn:sin_add}$), temos

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

Da mesma forma, usando

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

Somando ($\ref{eqn:cos_add}$) e ($\ref{eqn:cos_dif}$), temos

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

Subtraindo ($\ref{eqn:cos_dif}$) de ($\ref{eqn:cos_add}$), temos

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## Fórmulas de Soma para Produto (Sum-to-Product Identities)
- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### Derivação
Podemos derivar as fórmulas de Soma para Produto (Sum-to-Product Identities) a partir das fórmulas de Produto para Soma (Product-to-Sum Identities).

Definimos

$$ \alpha + \beta = A, \quad \alpha - \beta = B $$

Resolvendo estas equações para $\alpha$ e $\beta$, obtemos

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

Substituindo estes valores em ($\ref{sin_product_to_sum}$), ($\ref{cos_product_to_dif}$), ($\ref{cos_product_to_sum}$), ($\ref{sin_product_to_dif}$) respectivamente, obtemos as seguintes fórmulas:

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
