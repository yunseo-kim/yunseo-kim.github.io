---
title: "የድምር ወይም የልዩነት ቀመሮች (Product-to-Sum and Sum-to-Product Identities)"
description: "የትሪጎኖሜትሪ ፋንክሽኖችን ምርት ወደ ድምር ወይም ልዩነት የሚቀይሩ ቀመሮችን እንመለከታለን፣ እነሱንም ከመደመር ቀመሮች እንዴት እንደምናወጣ እናሳያለን። ከዚያም ድምር ወይም ልዩነትን ወደ ምርት የሚቀይሩ ቀመሮችንም እናወጣለን።"
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product Identities]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## አጭር ማጠቃለያ

> **ምርትን ወደ ድምር ወይም ልዩነት የሚቀይሩ ቀመሮች (Product-to-Sum Identities)**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **ድምርን ወይም ልዩነትን ወደ ምርት የሚቀይሩ ቀመሮች (Sum-to-Product Identities)**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> ቀመሮቹን ብቻ ሳይሆን የማውጣት ሂደታቸውንም አብሮ መማር ጥሩ ነው።
{: .prompt-tip }

## ቅድመ መስፈርቶች

- [የትሪጎኖሜትሪ ፋንክሽኖች የመደመር ቀመሮች](/posts/trigonometric-addition-formulas)

## ምርትን ወደ ድምር ወይም ልዩነት የሚቀይሩ ቀመሮች (Product-to-Sum Identities)

- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### ማውጣት

[የትሪጎኖሜትሪ ፋንክሽኖች የመደመር ቀመሮች](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

እንጠቀማለን።

($\ref{eqn:sin_add}$)+($\ref{eqn:sin_dif}$) ካደረግን

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

($\ref{eqn:sin_add}$)-($\ref{eqn:sin_dif}$) ካደረግን

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

በተመሳሳይ መንገድ

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

ከዚህ

($\ref{eqn:cos_add}$)+($\ref{eqn:cos_dif}$) ካደረግን

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

($\ref{eqn:cos_add}$)-($\ref{eqn:cos_dif}$) ካደረግን

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## ድምርን ወይም ልዩነትን ወደ ምርት የሚቀይሩ ቀመሮች (Sum-to-Product Identities)

- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### ማውጣት

ምርትን ወደ ድምር ወይም ልዩነት የሚቀይሩ ቀመሮች (Product-to-Sum Identities) ከሚባሉት መነሳት፣ ድምርን ወይም ልዩነትን ወደ ምርት የሚቀይሩ ቀመሮች (Sum-to-Product Identities) እንዲሁም ማውጣት ይቻላል።

$$ \alpha + \beta = A, \quad \alpha - \beta = B $$

ብለን ካስቀመጥን እና ሁለቱን ስሌቶች በ $\alpha$, $\beta$ ላይ በአንድነት ካፈታን

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

ይህንንም ቀደም ሲል ባሉት ($\ref{sin_product_to_sum}$), ($\ref{cos_product_to_dif}$), ($\ref{cos_product_to_sum}$), ($\ref{sin_product_to_dif}$) ውስጥ በየተራ በመተካት የሚከተሉትን ቀመሮች እናገኛለን።

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
