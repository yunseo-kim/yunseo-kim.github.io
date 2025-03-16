---
title: Sequências e Séries
description: Exploramos conceitos fundamentais do cálculo, incluindo definições de sequências e séries, convergência e divergência de sequências, convergência e divergência de séries, e a definição do número de Euler e.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## Sequências
No cálculo, uma **sequência** geralmente se refere a uma sequência infinita. Em outras palavras, uma sequência é uma função definida no conjunto dos **números naturais**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

Se os valores dessa função são números reais, chamamos de 'sequência real', se são números complexos, 'sequência complexa', se são pontos, 'sequência de pontos', se são matrizes, 'sequência de matrizes', se são funções, 'sequência de funções', se são conjuntos, 'sequência de conjuntos', mas todos esses podem ser simplesmente chamados de 'sequência'.*

Geralmente, para o **corpo dos números reais** $\mathbb{R}$, em uma sequência $\mathbf{a}: \mathbb{N} \to \mathbb{R}$, definimos

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

e representamos esta sequência como

$$ a_1,\, a_2,\, a_3,\, \dots $$

ou

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

> *Ao definir uma sequência, podemos usar como domínio, em vez do conjunto de todos os números naturais $\mathbb{N}$, o conjunto dos inteiros não negativos
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> ou
>
> $$\{2,3,4,\dots \}$$
>
> Por exemplo, ao lidar com a teoria das séries de potências, é mais natural ter $\mathbb{N}_0$ como domínio.
{: .prompt-info }

## Convergência e Divergência
Se uma sequência $(a_n)$ converge para um número real $l$, escrevemos

$$ \lim_{n\to \infty} a_n = l $$

e chamamos $l$ de **valor limite** da sequência $(a_n)$.

> A definição rigorosa usando o **argumento epsilon-delta** é a seguinte:
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> Ou seja, se para qualquer número positivo $\epsilon$, por menor que seja, sempre existe um número natural $N$ tal que $\|a_n - l \| < \epsilon$ para todo $n>N$, então dizemos que a sequência $(a_n)$ converge para o número real $l$, pois a diferença entre $a_n$ e $l$ se torna arbitrariamente pequena para $n$ suficientemente grande.
{: .prompt-info }

Uma sequência que não converge é dita **divergente**. *A convergência ou divergência de uma sequência não muda se um número finito de seus termos for alterado.*

Se os termos de uma sequência $(a_n)$ crescem indefinidamente, escrevemos

$$ \lim_{n\to \infty} a_n = \infty $$

e dizemos que a sequência *diverge para mais infinito*. Da mesma forma, se os termos de uma sequência $(a_n)$ decrescem indefinidamente, escrevemos

$$ \lim_{n\to \infty} a_n = -\infty $$

e dizemos que a sequência *diverge para menos infinito*.

## Propriedades Básicas de Sequências Convergentes
Se as sequências $(a_n)$ e $(b_n)$ são ambas convergentes (ou seja, têm valores limite), então as sequências $(a_n + b_n)$ e $(a_n \cdot b_n)$ também são convergentes, e

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Além disso, para qualquer número real $t$,

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Essas propriedades são chamadas de **propriedades básicas de sequências convergentes** ou **propriedades básicas de limites**.

## Número de Euler
O **número de Euler** é definido como

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Este é considerado uma das constantes mais importantes em matemática.

## Séries
Dada uma sequência

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

a sequência de suas somas parciais

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

é chamada de **série** da sequência $\mathbf{a}$. A série da sequência $(a_n)$ é representada como

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

## Convergência e Divergência de Séries
Se a série obtida da sequência $(a_n)$

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

converge para algum número real $l$, escrevemos

$$ \sum_{n=1}^{\infty} a_n = l $$

Neste caso, o valor limite $l$ é chamado de **soma** da série $\sum a_n$. O símbolo

$$ \sum a_n $$

pode representar tanto a <u>série</u> quanto a <u>soma da série</u>, dependendo do contexto.

Uma série que não converge é dita **divergente**.

## Propriedades Básicas de Séries Convergentes
Das [propriedades básicas de sequências convergentes](#propriedades-básicas-de-sequências-convergentes), obtemos as seguintes propriedades básicas de séries convergentes. Para um número real $t$ e duas séries convergentes $\sum a_n$ e $\sum b_n$:

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n $$

A convergência de uma série não é afetada pela mudança de um número finito de termos. Ou seja, se duas sequências $(a_n)$ e $(b_n)$ são iguais exceto para um número finito de $n$, então a série $\sum a_n$ converge se e somente se a série $\sum b_n$ converge.
