---
title: Sucesiones y series
description: Exploramos conceptos básicos del cálculo como la definición de sucesiones y series, convergencia y divergencia de sucesiones, convergencia y divergencia de series, y la definición del número e como base del logaritmo natural.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Sucesiones
En cálculo, una **sucesión (sequence)** generalmente se refiere a una sucesión infinita. Es decir, una sucesión es una función definida en el conjunto de todos los **números naturales (natural numbers)**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

Si los valores de esta función son números reales, se llama 'sucesión real', si son números complejos, 'sucesión compleja', si son puntos, 'sucesión de puntos', si son matrices, 'sucesión de matrices', si son funciones, 'sucesión de funciones', si son conjuntos, 'sucesión de conjuntos', etc., pero todos estos pueden ser simplemente referidos como 'sucesión'.

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

> *En el proceso de definir una sucesión, en lugar del conjunto de todos los números naturales $\mathbb{N}$, el dominio puede ser el conjunto de enteros no negativos
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> o
>
> $$\{2,3,4,\dots \}$$
>
> Por ejemplo, al tratar la teoría de las series de potencias, es más natural que el dominio sea $\mathbb{N}_0$.
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

y se dice que *diverge a más infinito*. De manera similar, si cada término de la sucesión $(a_n)$ decrece indefinidamente, se escribe

$$ \lim_{n\to \infty} a_n = -\infty $$

y se dice que *diverge a menos infinito*.

## Propiedades básicas de las sucesiones convergentes
Si las sucesiones $(a_n)$ y $(b_n)$ convergen (es decir, tienen valores límite), las sucesiones $(a_n + b_n)$ y $(a_n \cdot b_n)$ también convergen, y en este caso

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Además, para cualquier número real $t$

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Estas propiedades se conocen como **propiedades básicas de las sucesiones convergentes** o **propiedades básicas del límite**.

## La base $e$ del logaritmo natural
**La base del logaritmo natural** se define como

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Esta es una de las constantes más importantes en matemáticas.

> Aunque en Corea se usa ampliamente la expresión 'constante natural', este no es un término estándar. El término oficial registrado en el diccionario de términos matemáticos de la Sociedad Matemática de Corea es ['base del logaritmo natural'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91), y la expresión 'constante natural' no se encuentra en dicho diccionario. Incluso en el Diccionario Estándar del Instituto Nacional de la Lengua Coreana, no se puede encontrar la palabra 'constante natural', y en la [definición de diccionario de 'logaritmo natural'](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8) solo se menciona como "un número específico comúnmente denotado por e".  
> En los países de habla inglesa y en Japón tampoco existe un término correspondiente, y en inglés generalmente se refiere como 'the base of the natural logarithm' o abreviado como 'natural base', o 'Euler's number' o 'the number $e$'.  
> No hay razón para insistir en un término cuyo origen es incierto, que nunca ha sido reconocido oficialmente por la Sociedad Matemática de Corea, y que no se usa en ninguna parte del mundo excepto en Corea, así que de ahora en adelante aquí me referiré a él como 'la base del logaritmo natural' o simplemente lo denotaré como $e$.
{: .prompt-tip }

## Series
Dada una sucesión

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

la nueva sucesión formada por las sumas parciales de esta sucesión

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
De las [propiedades básicas de las sucesiones convergentes](#propiedades-básicas-de-las-sucesiones-convergentes), obtenemos las siguientes propiedades básicas de las series convergentes. Para un número real $t$ y dos series convergentes $\sum a_n$, $\sum b_n$, se cumple que

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

La convergencia de una serie no se ve afectada por el cambio de un número finito de términos. Es decir, si para dos sucesiones $(a_n)$, $(b_n)$, $a_n=b_n$ excepto para un número finito de $n$, la serie $\sum a_n$ converge si y solo si la serie $\sum b_n$ converge.
