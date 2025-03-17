---
title: Sequências e Séries
description: Exploramos conceitos fundamentais do cálculo, incluindo definições de sequências e séries, convergência e divergência de sequências, convergência e divergência de séries, e a definição da base do logaritmo natural e.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## Sequências
No cálculo, uma **sequência** geralmente se refere a uma sequência infinita. Em outras palavras, uma sequência é uma função definida no conjunto de todos os **números naturais**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

* Se os valores desta função são números reais, chamamos de 'sequência real', se são números complexos, 'sequência complexa', se são pontos, 'sequência de pontos', se são matrizes, 'sequência de matrizes', se são funções, 'sequência de funções', se são conjuntos, 'sequência de conjuntos', mas todos estes podem ser simplesmente chamados de 'sequência'.

Normalmente, para o **corpo dos números reais** $\mathbb{R}$, em uma sequência $\mathbf{a}: \mathbb{N} \to \mathbb{R}$, definimos

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

e representamos esta sequência como

$$ a_1,\, a_2,\, a_3,\, \dots $$

ou

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

> *No processo de definir uma sequência, em vez do conjunto de todos os números naturais $\mathbb{N}$, podemos usar o conjunto de inteiros não negativos
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> ou
>
> $$\{2,3,4,\dots \}$$
>
> como domínio. Por exemplo, ao lidar com a teoria das séries de potências, é mais natural ter $\mathbb{N}_0$ como domínio.
{: .prompt-info }

## Convergência e Divergência
Se uma sequência $(a_n)$ converge para um número real $l$, escrevemos

$$ \lim_{n\to \infty} a_n = l $$

e chamamos $l$ de **valor limite** da sequência $(a_n)$.

> A definição rigorosa usando o **argumento épsilon-delta** é a seguinte:
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> Ou seja, se para qualquer número positivo $\epsilon$, por menor que seja, sempre existe um número natural $N$ tal que $\|a_n - l\| < \epsilon$ para $n>N$, isso significa que a diferença entre $a_n$ e $l$ se torna arbitrariamente pequena para $n$ suficientemente grande, e portanto definimos que a sequência $(a_n)$ converge para o número real $l$.
{: .prompt-info }

Uma sequência que não converge é dita **divergente**. *A convergência ou divergência de uma sequência não muda se um número finito de seus termos for alterado.*

Se cada termo da sequência $(a_n)$ cresce indefinidamente, escrevemos

$$ \lim_{n\to \infty} a_n = \infty $$

e dizemos que *diverge para mais infinito*. Da mesma forma, se cada termo da sequência $(a_n)$ decresce indefinidamente, escrevemos

$$ \lim_{n\to \infty} a_n = -\infty $$

e dizemos que *diverge para menos infinito*.

## Propriedades Básicas de Sequências Convergentes
Se as sequências $(a_n)$ e $(b_n)$ são ambas convergentes (ou seja, têm valores limite), então as sequências $(a_n + b_n)$ e $(a_n \cdot b_n)$ também são convergentes, e

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Além disso, para qualquer número real $t$,

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Estas propriedades são chamadas de **propriedades básicas de sequências convergentes** ou **propriedades básicas de limites**.

## A Base do Logaritmo Natural $e$
A **base do logaritmo natural** é definida como

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Esta é considerada uma das constantes mais importantes em matemática.

> Apenas na Coreia, a expressão 'constante natural' é bastante utilizada, mas não é um termo padrão. O termo oficial registrado no dicionário de termos matemáticos pela Sociedade Matemática da Coreia é ['base do logaritmo natural'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91), e a expressão 'constante natural' não pode ser encontrada neste dicionário. Além disso, no Dicionário Padrão da Língua Coreana do Instituto Nacional da Língua Coreana, a palavra 'constante natural' não pode ser encontrada, e na [definição de dicionário para 'logaritmo natural'](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8), apenas menciona "um número específico geralmente representado por e".  
> Em países de língua inglesa e no Japão, também não existe um termo correspondente, e em inglês, geralmente é referido como 'the base of the natural logarithm' ou abreviado como 'natural base', ou 'Euler's number' ou 'the number $e$'.  
> Como a origem é incerta e nunca foi reconhecida como um termo oficial pela Sociedade Matemática da Coreia, e além disso, não é usado em nenhum lugar do mundo exceto na Coreia, não há absolutamente nenhuma razão para insistir em tal termo. Portanto, daqui em diante, vou me referir a ele como 'base do logaritmo natural' ou simplesmente usar $e$.
{: .prompt-tip }

## Séries
Dada uma sequência

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

a sequência formada pelas somas parciais desta sequência

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
Das [propriedades básicas de sequências convergentes](#propriedades-básicas-de-sequências-convergentes), obtemos as seguintes propriedades básicas de séries convergentes. Para um número real $t$ e duas séries convergentes $\sum a_n$ e $\sum b_n$,

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

A convergência de uma série não é afetada pela mudança de um número finito de termos. Ou seja, se duas sequências $(a_n)$ e $(b_n)$ são iguais exceto para um número finito de $n$, a série $\sum a_n$ converge se e somente se a série $\sum b_n$ converge.
