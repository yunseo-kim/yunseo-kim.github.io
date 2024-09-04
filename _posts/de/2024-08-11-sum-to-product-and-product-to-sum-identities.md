---
title: "Produkt-zu-Summe und Summe-zu-Produkt Identitäten"
description: >-
  Wir untersuchen Formeln zur Umwandlung von Produkten trigonometrischer Funktionen in Summen oder Differenzen und leiten diese aus den trigonometrischen Additionstheoreme ab. Daraus leiten wir auch Formeln ab, um Summen oder Differenzen trigonometrischer Funktionen in Produkte umzuwandeln.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product Identities]
math: true
---

## TL;DR
> **Produkt-zu-Summe Identitäten**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **Summe-zu-Produkt Identitäten**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> Es ist ratsam, nicht nur die Formeln, sondern auch den Ableitungsprozess zu lernen.
{: .prompt-tip }

## Voraussetzungen
- [Trigonometrische Additionstheoreme](/posts/trigonometric-addition-formulas)

## Produkt-zu-Summe Identitäten
- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### Ableitung
Wir verwenden die [trigonometrischen Additionstheoreme](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

Wenn wir ($\ref{eqn:sin_add}$)+($\ref{eqn:sin_dif}$) berechnen, erhalten wir

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

Wenn wir ($\ref{eqn:sin_add}$)-($\ref{eqn:sin_dif}$) berechnen, erhalten wir

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

Auf die gleiche Weise erhalten wir aus

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

Wenn wir ($\ref{eqn:cos_add}$)+($\ref{eqn:cos_dif}$) berechnen, erhalten wir

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

Wenn wir ($\ref{eqn:cos_add}$)-($\ref{eqn:cos_dif}$) berechnen, erhalten wir

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## Summe-zu-Produkt Identitäten
- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### Ableitung
Wir können die Summe-zu-Produkt Identitäten aus den Produkt-zu-Summe Identitäten ableiten.

Setzen wir

$$ \alpha + \beta = A, \quad \alpha - \beta = B $$

und lösen diese Gleichungen nach $\alpha$ und $\beta$ auf, erhalten wir

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

Wenn wir diese in die vorherigen Gleichungen ($\ref{sin_product_to_sum}$), ($\ref{cos_product_to_dif}$), ($\ref{cos_product_to_sum}$), ($\ref{sin_product_to_dif}$) einsetzen, erhalten wir die folgenden Formeln:

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
