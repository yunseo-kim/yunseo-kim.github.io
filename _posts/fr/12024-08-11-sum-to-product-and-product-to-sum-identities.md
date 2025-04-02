---
title: Formules de produit en somme et de somme en produit (Product-to-Sum and Sum-to-Product
  Identities)
description: Découvrez les formules pour transformer le produit de fonctions trigonométriques
  en somme ou différence, dérivez ces formules à partir des théorèmes d'addition trigonométrique,
  et utilisez-les pour déduire les formules transformant les sommes ou différences
  de fonctions trigonométriques en produits.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product
    Identities]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Formules de produit en somme (Product-to-Sum Identities)**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **Formules de somme en produit (Sum-to-Product Identities)**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> Il est recommandé d'apprendre non seulement les formules, mais aussi le processus de dérivation.
{: .prompt-tip }

## Prérequis
- [Formules d'addition trigonométriques](/posts/trigonometric-addition-formulas)

## Formules de produit en somme (Product-to-Sum Identities)
- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### Dérivation
Nous utilisons les [formules d'addition trigonométriques](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

En additionnant ($\ref{eqn:sin_add}$) et ($\ref{eqn:sin_dif}$), on obtient

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

En soustrayant ($\ref{eqn:sin_dif}$) de ($\ref{eqn:sin_add}$), on obtient

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

De la même manière, à partir de

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

En additionnant ($\ref{eqn:cos_add}$) et ($\ref{eqn:cos_dif}$), on obtient

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

En soustrayant ($\ref{eqn:cos_dif}$) de ($\ref{eqn:cos_add}$), on obtient

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## Formules de somme en produit (Sum-to-Product Identities)
- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### Dérivation
On peut dériver les formules de somme en produit (Sum-to-Product Identities) à partir des formules de produit en somme (Product-to-Sum Identities).

Posons $$ \alpha + \beta = A, \quad \alpha - \beta = B $$

En résolvant ces équations pour $\alpha$ et $\beta$, on obtient

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

En substituant ces valeurs dans les équations ($\ref{sin_product_to_sum}$), ($\ref{cos_product_to_dif}$), ($\ref{cos_product_to_sum}$), ($\ref{sin_product_to_dif}$) respectivement, on obtient les formules suivantes :

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
