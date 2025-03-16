---
title: 数列と級数
description: 数列と級数の定義、数列の収束と発散、級数の収束と発散、自然数eの定義など、微積分学の基礎概念を見ていきます。
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## 数列
微積分学で扱う**数列（sequence）**は主に無限数列を指します。つまり、数列とは**自然数（natural number）**の全体集合

$$ \mathbb{N} := \{1,2,3,\dots\} $$

で定義された関数です。* この関数の値が実数（real number）であれば「実数列」、複素数（complex number）であれば「複素数列」、点（point）であれば「点列」、行列（matrix）であれば「行列列」、関数（function）であれば「関数列」、集合（set）であれば「集合列」などと呼ぶことができますが、これらすべてを簡単に「列」または「数列」と呼ぶことができます。

通常、**実数体（the field of real numbers）** $\mathbb{R}$に対して、数列 $\mathbf{a}: \mathbb{N} \to \mathbb{R}$で

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

などとし、この数列を

$$ a_1,\, a_2,\, a_3,\, \dots $$

または

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

などと表します。

> *数列を定義する過程で、定義域を自然数全体集合 $\mathbb{N}$ の代わりに $0$ 以上の整数の集合
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> または
>
> $$\{2,3,4,\dots \}$$
>
> などとすることもあります。例えば、べき級数理論を扱う際には、定義域が $\mathbb{N}_0$ であるほうが自然です。
{: .prompt-info }

## 収束と発散
数列 $(a_n)$ が実数 $l$ に収束するとき

$$ \lim_{n\to \infty} a_n = l $$

と書き、このとき $l$ を数列 $(a_n)$ の**極限値**と呼びます。

> **イプシロン-デルタ論法（epsilon-delta argument）**を用いた厳密な定義は次のとおりです。
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> つまり、どんなに小さな正数 $\epsilon$ に対しても、$n>N$ のとき $\|a_n - l \| < \epsilon$ を満たす自然数 $N$ が常に存在するならば、十分大きな $n$ に対して $a_n$ と $l$ の差が限りなく小さくなるという意味であり、これを満たす数列 $(a_n)$ は実数 $l$ に収束すると定義します。
{: .prompt-info }

収束しない数列は**発散**すると言います。*数列の収束または発散の可否は、その数列の有限個の項が変わっても変わりません。*

もし数列 $(a_n)$ の各項が限りなく大きくなるなら

$$ \lim_{n\to \infty} a_n = \infty $$

と書き、*正の無限大に発散する*と言います。同様に、数列 $(a_n)$ の各項が限りなく小さくなるなら

$$ \lim_{n\to \infty} a_n = -\infty $$

と書き、*負の無限大に発散する*と言います。

## 収束する数列の基本的性質
数列 $(a_n)$ と $(b_n)$ がともに収束するとき（つまり極限値を持つとき）、数列 $(a_n + b_n)$ と $(a_n \cdot b_n)$ も同様に収束し、このとき

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

となります。また、任意の実数 $t$ に対して

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

が成り立ちます。これらの性質を**収束する数列の基本的性質**または**極限の基本的性質**と呼びます。

## 自然対数の底
**自然対数の底**は

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

と定義されます。これは数学で最も重要な定数の一つと言えます。

## 級数
数列

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

に対して、この数列の部分和からなる別の数列

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

を数列 $\mathbf{a}$ の**級数**と呼びます。数列 $(a_n)$ の級数は

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

などと表します。

## 級数の収束と発散
数列 $(a_n)$ から得られる級数

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

がある実数 $l$ に収束するとき

$$ \sum_{n=1}^{\infty} a_n = l $$

と表します。このとき極限値 $l$ を級数 $\sum a_n$ の**和**と呼びます。記号

$$ \sum a_n $$

は状況に応じて<u>級数</u>を表したり、その<u>級数の和</u>を表したりします。

収束しない級数は**発散**すると言います。

## 収束する級数の基本的性質
[収束する数列の基本的性質](#収束する数列の基本的性質)から、次のような収束する級数の基本的性質が得られます。実数 $t$ と収束する二つの級数 $\sum a_n$、$\sum b_n$ に対して

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n $$

が成り立ちます。

級数の収束性は有限個の項の変化に影響を受けません。つまり、二つの数列 $(a_n)$、$(b_n)$ で有限個の $n$ を除いて $a_n=b_n$ であれば、級数 $\sum a_n$ が収束する必要十分条件は級数 $\sum b_n$ が収束することです。
