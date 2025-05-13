---
title: Sequences and Series
description: We examine fundamental concepts of calculus such as the definition of sequences and series, convergence and divergence of sequences, convergence and divergence of series, and the definition of e, the base of natural logarithm.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Sequences
In calculus, a **sequence** primarily refers to an infinite sequence. That is, a sequence is a function defined on the set of all **natural numbers**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

* If the values of this function are real numbers, we call it a 'real sequence'; if complex numbers, a 'complex sequence'; if points, a 'point sequence'; if matrices, a 'matrix sequence'; if functions, a 'function sequence'; if sets, a 'set sequence'. However, all of these can be simply referred to as 'sequences'.

Usually, for the **field of real numbers** $\mathbb{R}$, in a sequence $\mathbf{a}: \mathbb{N} \to \mathbb{R}$, we denote

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

and represent this sequence as

$$ a_1,\, a_2,\, a_3,\, \dots $$

or

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

> *In the process of defining a sequence, instead of using the set of all natural numbers $\mathbb{N}$ as the domain, we can also use the set of non-negative integers
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> or
>
> $$\{2,3,4,\dots \}$$
>
> For example, when dealing with power series theory, it's more natural to have $\mathbb{N}_0$ as the domain.
{: .prompt-info }

## Convergence and Divergence
If a sequence $(a_n)$ converges to a real number $l$, we write

$$ \lim_{n\to \infty} a_n = l $$

and call $l$ the **limit** of the sequence $(a_n)$.

> The rigorous definition using the **epsilon-delta argument** is as follows:
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> In other words, if for any positive $\epsilon$, there always exists a natural number $N$ such that $\|a_n - l \| < \epsilon$ when $n>N$, it means that the difference between $a_n$ and $l$ becomes infinitely small for sufficiently large $n$. Therefore, we define that a sequence $(a_n)$ satisfying this condition converges to the real number $l$.
{: .prompt-info }

A sequence that does not converge is said to **diverge**. *The convergence or divergence of a sequence does not change even if a finite number of its terms are altered.*

If each term of the sequence $(a_n)$ grows infinitely large, we write

$$ \lim_{n\to \infty} a_n = \infty $$

and say that it *diverges to positive infinity*. Similarly, if each term of the sequence $(a_n)$ becomes infinitely small, we write

$$ \lim_{n\to \infty} a_n = -\infty $$

and say that it *diverges to negative infinity*.

## Basic Properties of Convergent Sequences
If sequences $(a_n)$ and $(b_n)$ both converge (i.e., have limits), then the sequences $(a_n + b_n)$ and $(a_n \cdot b_n)$ also converge, and

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Also, for any real number $t$,

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

These properties are called the **basic properties of convergent sequences** or **basic properties of limits**.

## $e$, the Base of Natural Logarithm
**The base of natural logarithm** is defined as

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

This is considered one of the most important constants in mathematics.

> The term 'natural constant' is widely used only in Korea, but this is not a standard term. The official term registered in the mathematics terminology dictionary by the Korean Mathematical Society is ['base of natural logarithm'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91), and the expression 'natural constant' cannot be found in this dictionary. Even in the Standard Korean Language Dictionary of the National Institute of Korean Language, the word 'natural constant' cannot be found, and in the [dictionary definition of 'natural logarithm'](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8), it only mentions "a specific number usually denoted as e".  
> In English-speaking countries and Japan, there is no corresponding term, and in English, it's mainly referred to as 'the base of the natural logarithm' or shortened to 'natural base', or 'Euler's number' or 'the number $e$'.  
> Since the origin is unclear and it has never been recognized as an official term by the Korean Mathematical Society, and it's not used anywhere else in the world except Korea, there's no reason to insist on using such a term. Therefore, from now on, I will refer to it as 'the base of natural logarithm' or simply denote it as $e$.
{: .prompt-tip }

## Series
For a sequence

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

the sequence of partial sums

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

is called the **series** of the sequence $\mathbf{a}$. The series of the sequence $(a_n)$ is denoted as

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

## Convergence and Divergence of Series
If the series obtained from the sequence $(a_n)$

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

converges to some real number $l$, we write

$$ \sum_{n=1}^{\infty} a_n = l $$

The limit value $l$ is called the **sum** of the series $\sum a_n$. The symbol

$$ \sum a_n $$

can represent either the <u>series</u> or the <u>sum of the series</u>, depending on the context.

A series that does not converge is said to **diverge**.

## Basic Properties of Convergent Series
From the [basic properties of convergent sequences](#basic-properties-of-convergent-sequences), we obtain the following basic properties of convergent series. For a real number $t$ and two convergent series $\sum a_n$, $\sum b_n$,

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

The convergence of a series is not affected by changes in a finite number of terms. That is, if $a_n=b_n$ for all but finitely many $n$ in two sequences $(a_n)$, $(b_n)$, the series $\sum a_n$ converges if and only if the series $\sum b_n$ converges.
