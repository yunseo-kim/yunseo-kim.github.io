---
title: Sucesiones y series
description: Exploramos conceptos básicos del cálculo como la definición de sucesiones y series, convergencia y divergencia de sucesiones, convergencia y divergencia de series, y la definición del número e.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## Sucesiones
En cálculo, una **sucesión (sequence)** generalmente se refiere a una sucesión infinita. Es decir, una sucesión es una función definida en el conjunto de los **números naturales (natural numbers)**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

Si los valores de esta función son números reales, se llama 'sucesión real', si son números complejos, 'sucesión compleja', si son puntos, 'sucesión de puntos', si son matrices, 'sucesión de matrices', si son funciones, 'sucesión de funciones', si son conjuntos, 'sucesión de conjuntos', etc., pero todos estos pueden denominarse simplemente 'sucesión'.

Normalmente, para el **cuerpo de los números reales (the field of real numbers)** $\mathbb{R}$, en una sucesión $\mathbf{a}: \mathbb{N} \to \mathbb{R}$, se denota

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

y esta sucesión se representa como

$$ a_1,\, a_2,\, a_3,\, \dots $$

o

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

> *En el proceso de definir una sucesión, en lugar del conjunto de todos los números naturales $\mathbb{N}$ como dominio, se puede usar el conjunto de enteros no negativos
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> o
>
> $$\{2,3,4,\dots \}$$
>
> Por ejemplo, al tratar la teoría de series de potencias, es más natural que el dominio sea $\mathbb{N}_0$.
{: .prompt-info }

## Convergencia y divergencia
Si una sucesión $(a_n)$ converge a un número real $l$, se escribe

$$ \lim_{n\to \infty} a_n = l $$

y $l$ se llama el **valor límite** de la sucesión $(a_n)$.

> La definición rigurosa utilizando el **argumento épsilon-delta (epsilon-delta argument)** es la siguiente:
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> Es decir, si para cualquier número positivo $\epsilon$, por pequeño que sea, siempre existe un número natural $N$ tal que $\|a_n - l \| < \epsilon$ cuando $n>N$, significa que la diferencia entre $a_n$ y $l$ se vuelve arbitrariamente pequeña para $n$ suficientemente grande, por lo que se define que una sucesión $(a_n)$ que satisface esto converge al número real $l$.
{: .prompt-info }

Se dice que una sucesión que no converge **diverge**. *La convergencia o divergencia de una sucesión no cambia si se modifican un número finito de sus términos.*

Si cada término de la sucesión $(a_n)$ crece indefinidamente, se escribe

$$ \lim_{n\to \infty} a_n = \infty $$

y se dice que *diverge a infinito positivo*. De manera similar, si cada término de la sucesión $(a_n)$ decrece indefinidamente, se escribe

$$ \lim_{n\to \infty} a_n = -\infty $$

y se dice que *diverge a infinito negativo*.

## Propiedades básicas de las sucesiones convergentes
Si las sucesiones $(a_n)$ y $(b_n)$ convergen ambas (es decir, tienen valores límite), entonces las sucesiones $(a_n + b_n)$ y $(a_n \cdot b_n)$ también convergen, y en este caso

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Además, para cualquier número real $t$

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Estas propiedades se conocen como **propiedades básicas de las sucesiones convergentes** o **propiedades básicas del límite**.

## Número e
El **número e** se define como

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Este es uno de los números más importantes en matemáticas.

## Series
Dada una sucesión

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

la sucesión de sumas parciales

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

se llama **serie** de la sucesión $\mathbf{a}$. La serie de la sucesión $(a_n)$ se denota como

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

## Convergencia y divergencia de series
Si la serie obtenida de la sucesión $(a_n)$

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

converge a algún número real $l$, se denota como

$$ \sum_{n=1}^{\infty} a_n = l $$

En este caso, el valor límite $l$ se llama la **suma** de la serie $\sum a_n$. El símbolo

$$ \sum a_n $$

puede representar tanto la <u>serie</u> como la <u>suma de la serie</u>, dependiendo del contexto.

Se dice que una serie que no converge **diverge**.

## Propiedades básicas de las series convergentes
De las [propiedades básicas de las sucesiones convergentes](#propiedades-básicas-de-las-sucesiones-convergentes), obtenemos las siguientes propiedades básicas de las series convergentes. Para un número real $t$ y dos series convergentes $\sum a_n$, $\sum b_n$:

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n $$

La convergencia de una serie no se ve afectada por el cambio de un número finito de términos. Es decir, si para dos sucesiones $(a_n)$, $(b_n)$, $a_n=b_n$ excepto para un número finito de $n$, entonces la serie $\sum a_n$ converge si y solo si la serie $\sum b_n$ converge.
