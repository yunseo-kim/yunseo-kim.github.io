---
title: "和または差の公式（積和公式と和積公式）"
description: >-
  三角関数の積を和または差の形に変形する公式を学び、三角関数の加法定理からその公式を導出します。そして、これらから三角関数の和または差の形を積の形に変形する公式も導出します。
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Product-to-Sum Identities, Sum-to-Product Identities]
math: true
---

## TL;DR
> **積を和または差に変形する公式（積和公式）**
>
> - $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
> - $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
> - $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$
{: .prompt-info }

> **和または差を積に変形する公式（和積公式）**
>
> - $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
> - $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
> - $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$
{: .prompt-info }

> 公式だけでなく、導出過程も一緒に覚えておくと良いでしょう。
{: .prompt-tip }

## 前提知識
- [三角関数の加法定理](/posts/trigonometric-addition-formulas)

## 積を和または差に変形する公式（積和公式）
- $$ \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \} $$
- $$ \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) + \cos ( \alpha - \beta )\} $$
- $$ \sin \alpha \sin \beta = - \frac { 1 } { 2 } \{ \cos ( \alpha + \beta ) - \cos ( \alpha - \beta ) \} $$

### 導出
[三角関数の加法定理](/posts/trigonometric-addition-formulas)

$$ \begin{align}
\sin(\alpha+\beta) &= \sin \alpha \cos \beta + \cos \alpha \sin \beta \tag{1}\label{eqn:sin_add}\\
\sin(\alpha-\beta) &= \sin \alpha \cos \beta - \cos \alpha \sin \beta \tag{2}\label{eqn:sin_dif}
\end{align}$$

を利用します。

($\ref{eqn:sin_add}$)+($\ref{eqn:sin_dif}$)すると

$$ \sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta \tag{3}\label{sin_product_to_sum} $$

$$ \therefore \sin \alpha \cos \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) + \sin ( \alpha - \beta ) \}. $$

($\ref{eqn:sin_add}$)-($\ref{eqn:sin_dif}$)すると

$$ \sin(\alpha+\beta) - \sin(\alpha-\beta) = 2 \cos \alpha \sin \beta \tag{4}\label{cos_product_to_dif} $$

$$ \therefore \cos \alpha \sin \beta = \frac { 1 } { 2 } \{ \sin ( \alpha + \beta ) - \sin ( \alpha - \beta ) \}. $$

同様の方法で

$$ \begin{align}
\cos(\alpha+\beta) &= \cos \alpha \cos \beta - \sin \alpha \sin \beta \tag{5}\label{eqn:cos_add} \\
\cos(\alpha-\beta ) &= \cos \alpha \cos \beta + \sin \alpha \sin \beta \tag{6}\label{eqn:cos_dif}
\end{align} $$

から

($\ref{eqn:cos_add}$)+($\ref{eqn:cos_dif}$)すると

$$ \cos(\alpha+\beta) + \cos(\alpha-\beta) = 2 \cos \alpha \cos \beta \tag{7}\label{cos_product_to_sum} $$

$$ \therefore \cos \alpha \cos \beta = \frac { 1 } { 2 } \{ \cos(\alpha+\beta) + \cos(\alpha-\beta) \}. $$

($\ref{eqn:cos_add}$)-($\ref{eqn:cos_dif}$)すると

$$ \cos(\alpha+\beta) - \cos(\alpha-\beta) = -2 \sin \alpha \sin \beta \tag{8}\label{sin_product_to_dif} $$

$$ \therefore \sin \alpha \sin \beta = -\frac { 1 } { 2 } \{ \cos(\alpha+\beta) - \cos(\alpha-\beta) \}. $$

## 和または差を積に変形する公式（和積公式）
- $$ \sin A + \sin B = 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \sin A - \sin B = 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} $$
- $$ \cos A + \cos B = 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} $$
- $$ \cos A - \cos B = -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} $$

### 導出
積を和または差に変形する公式（積和公式）から和または差を積に変形する公式（和積公式）も導出できます。

$$ \alpha + \beta = A, \quad \alpha - \beta = B $$

とおき、二つの式を$\alpha$、$\beta$について連立して解くと

$$ \alpha = \frac{A+B}{2}, \quad \beta = \frac{A-B}{2}. $$

これを前の($\ref{sin_product_to_sum}$)、($\ref{cos_product_to_dif}$)、($\ref{cos_product_to_sum}$)、($\ref{sin_product_to_dif}$)にそれぞれ代入すると、次の公式が得られます。

$$ \begin{align*}
\sin A + \sin B &= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\
\sin A - \sin B &= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\
\cos A + \cos B &= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\
\cos A - \cos B &= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2}.
\end{align*} $$
