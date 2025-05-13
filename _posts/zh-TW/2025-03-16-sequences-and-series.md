---
title: 數列與級數
description: 探討數列與級數的定義、數列的收斂與發散、級數的收斂與發散、自然對數的底數e的定義等微積分的基礎概念。
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## 數列
在微積分中討論的**數列（sequence）**主要指無限數列。也就是說，數列是定義在**自然數（natural number）**全體集合上的函數

$$ \mathbb{N} := \{1,2,3,\dots\} $$

*如果這個函數的值是實數（real number），則稱為「實數列」；如果是複數（complex number），則稱為「複數列」；如果是點（point），則稱為「點列」；如果是矩陣（matrix），則稱為「矩陣列」；如果是函數（function），則稱為「函數列」；如果是集合（set），則稱為「集合列」等。但這些都可以簡單地稱為「列」或「數列」。

通常對於**實數體（the field of real numbers）** $\mathbb{R}$，數列 $\mathbf{a}: \mathbb{N} \to \mathbb{R}$ 中

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

等，這個數列可以表示為

$$ a_1,\, a_2,\, a_3,\, \dots $$

或

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

等。

> *在定義數列的過程中，定義域可以不用自然數全體集合 $\mathbb{N}$，而改用 $0$ 以上的整數集合
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> 或
>
> $$\{2,3,4,\dots \}$$
>
> 等。例如，在處理冪級數理論時，定義域為 $\mathbb{N}_0$ 會更自然。
{: .prompt-info }

## 收斂與發散
如果數列 $(a_n)$ 收斂於實數 $l$，則寫作

$$ \lim_{n\to \infty} a_n = l $$

這時，$l$ 稱為數列 $(a_n)$ 的**極限值**。

> 使用**ε-δ論證（epsilon-delta argument）**的嚴格定義如下：
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> 也就是說，對於任何小的正數 $\epsilon$，只要存在一個自然數 $N$，使得當 $n>N$ 時，總是滿足 $\|a_n - l \| < \epsilon$，這意味著對於足夠大的 $n$，$a_n$ 和 $l$ 的差會無限接近，因此我們定義滿足這個條件的數列 $(a_n)$ 收斂於實數 $l$。
{: .prompt-info }

不收斂的數列稱為**發散**。*數列的收斂或發散性質不會因為有限項的改變而改變。*

如果數列 $(a_n)$ 的每一項無限增大，則寫作

$$ \lim_{n\to \infty} a_n = \infty $$

稱為*發散到正無窮大*。同樣地，如果數列 $(a_n)$ 的每一項無限減小，則寫作

$$ \lim_{n\to \infty} a_n = -\infty $$

稱為*發散到負無窮大*。

## 收斂數列的基本性質
如果數列 $(a_n)$ 和 $(b_n)$ 都收斂（即有極限值），則數列 $(a_n + b_n)$ 和 $(a_n \cdot b_n)$ 也同樣收斂，且

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

此外，對於任意實數 $t$，

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

這些性質稱為**收斂數列的基本性質**或**極限的基本性質**。

## 自然對數的底數 $e$
**自然對數的底數**定義為

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

這可以說是數學中最重要的常數之一。

> 在韓國，「自然常數」這個表達方式相當普遍，但這並不是標準用語。韓國數學會在數學用語集中登錄的官方用語是['自然對數的底數'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91)，而「自然常數」這個表達在該用語集中找不到。甚至在國立國語院標準國語大辭典中也找不到「自然常數」這個詞，只在['自然對數'的辭典解釋](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8)中提到「通常用e表示的特定數字」。  
> 在英語圈和日本也不存在對應的用語，以英語為準，主要稱為'the base of the natural logarithm'或簡稱'natural base'，或者'Euler's number'或'the number $e$'。  
> 由於來源不明，韓國數學會也從未認可為官方用語，而且除了韓國以外，世界上沒有其他地方使用這樣的用語，因此我們沒有理由堅持使用這樣的用語。從現在開始，我也會稱之為「自然對數的底數」或直接表示為$e$。
{: .prompt-tip }

## 級數
對於數列

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

由這個數列的部分和組成的另一個數列

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

稱為數列 $\mathbf{a}$ 的**級數**。數列 $(a_n)$ 的級數表示為

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

等。

## 級數的收斂與發散
如果從數列 $(a_n)$ 得到的級數

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

收斂於某個實數 $l$，則表示為

$$ \sum_{n=1}^{\infty} a_n = l $$

這時，極限值 $l$ 稱為級數 $\sum a_n$ 的**和**。符號

$$ \sum a_n $$

根據情況可以表示<u>級數</u>，也可以表示該<u>級數的和</u>。

不收斂的級數稱為**發散**。

## 收斂級數的基本性質
從[收斂數列的基本性質](#收斂數列的基本性質)可以得到以下收斂級數的基本性質。對於實數 $t$ 和兩個收斂級數 $\sum a_n$, $\sum b_n$，

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

成立。

級數的收斂性不受有限項變化的影響。也就是說，對於兩個數列 $(a_n)$, $(b_n)$，如果除了有限個 $n$ 外，都有 $a_n=b_n$，則級數 $\sum a_n$ 收斂的充分必要條件是級數 $\sum b_n$ 收斂。
