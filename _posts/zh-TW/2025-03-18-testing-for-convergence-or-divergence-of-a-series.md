---
title: 級數的收斂/發散判定（Testing for Convergence or Divergence of a Series）
description: 綜合探討判定級數收斂/發散的各種方法。
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **一般項判定法（$n$th-term test for divergence）**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{級數 }\sum a_n \text{發散}$
> - **幾何級數的收斂/發散**: 幾何級數 $\sum ar^{n-1}$
>   - $\|r\| < 1$ 時收斂
>   - $\|r\| \geq 1$ 時發散
> - **$p$-級數的收斂/發散**: $p$-級數 $\sum \cfrac{1}{n^p}$
>   - $p>1$ 時收斂
>   - $p\leq 1$ 時發散
> - **比較判定法（Comparison Test）**: 當 $0 \leq a_n \leq b_n$ 時，  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **極限比較判定法（Limit Comparison Test）**: 若 $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{為有限正數)}$，則兩個級數 $\sum a_n$ 和 $\sum b_n$ 要麼都收斂，要麼都發散
> - 對於正項級數 $\sum a_n$ 和正數 $\epsilon < 1$  
>   - 若對所有 $n$ 都有 $\sqrt[n]{a_n}< 1-\epsilon$，則級數 $\sum a_n$ 收斂
>   - 若對所有 $n$ 都有 $\sqrt[n]{a_n}> 1+\epsilon$，則級數 $\sum a_n$ 發散
> - **根式判定法（Root Test）**: 對於正項級數 $\sum a_n$，若極限值 $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ 存在，則
>   - $r<1$ 時級數 $\sum a_n$ 收斂
>   - $r>1$ 時級數 $\sum a_n$ 發散
> - **比值判定法（Ratio Test）**: 對於正數序列 $(a_n)$ 和 $0 < r < 1$
>   - 若對所有 $n$ 都有 $a_{n+1}/a_n \leq r$，則級數 $\sum a_n$ 收斂
>   - 若對所有 $n$ 都有 $a_{n+1}/a_n \geq 1$，則級數 $\sum a_n$ 發散
> - 對於正數序列 $(a_n)$，若極限值 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ 存在，則
>   - $\rho < 1$ 時級數 $\sum a_n$ 收斂
>   - $\rho > 1$ 時級數 $\sum a_n$ 發散
> - **積分判定法（Integral Test）**: 對於連續函數 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$，若 $f$ 為遞減函數且恆為正，則級數 $\sum f(n)$ 收斂的充要條件是積分 $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ 收斂
> - **交錯級數判定法（Alternating Series Test）**: 若滿足以下條件，則交錯級數 $\sum a_n$ 收斂
>   1. 對所有 $n$，$a_n$ 和 $a_{n+1}$ 的符號不同
>   2. 對所有 $n$，$\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - 絕對收斂的級數必定收斂。反之則不成立。
{: .prompt-info }

## 先備知識
- [序列與級數](/posts/sequences-and-series/)

## 引言
在之前的[序列與級數](/posts/sequences-and-series/#級數的收斂與發散)中，我們了解了級數收斂和發散的定義。本文將整理判定級數收斂/發散時可以使用的各種方法。一般來說，判定級數的收斂/發散比精確計算級數的和要容易得多。

## 一般項判定法
對於級數 $\sum a_n$，我們稱 $a_n$ 為該級數的**一般項**。

根據以下定理，我們可以輕易判斷某些級數明顯發散，因此在判定級數的收斂/發散時，首先檢查這一點是避免浪費時間的明智做法。

> **一般項判定法（$n$th-term test for divergence）**  
> 若級數 $\sum a_n$ 收斂，則
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> 也就是說，
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{級數 }\sum a_n \text{發散} $$
{: .prompt-info }

### 證明
假設某個收斂的級數 $\sum a_n$ 的和為 $l$，並將前 $n$ 項的和表示為

$$ s_n := a_1 + a_2 + \cdots + a_n $$

則有

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

因此，對於足夠大的（$>N$）$n$，我們有

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

根據序列收斂的定義，我們得到

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### 注意事項
這個定理的逆命題通常不成立。一個典型的例子是**調和級數（harmonic series）**。

調和級數是由**等差數列**的倒數，即**調和數列**得到的級數。最典型的調和級數是

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

我們可以如下證明這個級數發散：

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

儘管級數 $H_n$ 發散，但我們可以看到其一般項 $1/n$ 收斂於 $0$。

> 如果 $\lim_{n\to\infty} a_n \neq 0$，則級數 $\sum a_n$ 必定發散，但如果 $\lim_{n\to\infty} a_n = 0$，並不能保證級數 $\sum a_n$ 會收斂。在這種情況下，我們需要使用其他方法來判定收斂/發散。
{: .prompt-danger }

## 幾何級數
首項為 1，**公比**為 $r$ 的等比數列所得到的**幾何級數（geometric series）**

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

是<u>最重要且基本的級數</u>。從等式

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

我們得到

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

另一方面，

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

因此，我們知道幾何級數 ($\ref{eqn:geometric_series}$) 收斂的充要條件是 $\|r\| < 1$。

> **幾何級數的收斂/發散**  
> 幾何級數 $\sum ar^{n-1}$
> - $\|r\| < 1$ 時收斂
> - $\|r\| \geq 1$ 時發散
{: .prompt-info }

由此我們得到

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### 幾何級數與近似值
當 $\|r\| < 1$ 時，恆等式 ($\ref{eqn:sum_of_geometric_series}$) 在計算 $\cfrac{1}{1-r}$ 的近似值時非常有用。

將 $r=-\epsilon$, $n=2$ 代入這個式子，我們得到

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

因此，當 $0 < \epsilon < 1$ 時，

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

所以我們得到

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

由此可知，對於足夠小的正數 $\epsilon$，$\cfrac{1}{1 + \epsilon}$ 可以近似為 $1 - \epsilon$。

## $p$-級數判定法（$p$-Series Test）  
對於正實數 $p$，以下形式的級數稱為 **$p$-級數**：

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **$p$-級數的收斂/發散**  
> $p$-級數 $\sum \cfrac{1}{n^p}$
> - $p>1$ 時收斂
> - $p\leq 1$ 時發散
{: .prompt-info }

在 $p$-級數中，當 $p=1$ 時就是調和級數，我們之前已經證明它發散。  
當 $p=2$ 時的 $p$-級數，即 $\sum \cfrac{1}{n^2}$ 的值的計算問題，被稱為"巴塞爾（Basel）問題"，這個名字來源於首次證明這個級數收斂的伯努利家族的根據地。這個問題的答案已知為 $\cfrac{\pi^2}{6}$。

更一般地，$p$-級數中 $p>1$ 的情況被稱為**zeta 函數（zeta function）**。這是由萊昂哈德·歐拉（Leonhard Euler）在 1740 年引入，後來由黎曼命名的特殊函數之一，定義為

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

這個話題有點偏離本文的主題，而且說實話，我是工科生而不是數學家，所以我也不太了解，因此在這裡不詳細討論。但值得一提的是，萊昂哈德·歐拉證明了 zeta 函數也可以用**歐拉乘積（Euler Product）**的形式表示，這是素數（prime number）的無限乘積形式。此後，zeta 函數在解析數論的多個分支中佔據了核心地位。將 zeta 函數的定義域擴展到複數的**黎曼 zeta 函數（Riemann zeta function）**以及與之相關的重要未解決難題**黎曼假設（Riemann hypothesis）**就是其中之一。

回到原來的主題，$p$-級數判定法的證明需要後面將要討論的[比較判定法](#比較判定法)和[積分判定法](#積分判定法)。然而，$p$-級數的收斂/發散可以與幾何級數一起在接下來的[比較判定法](#比較判定法)中有效使用，因此我特意將其放在前面。

### 證明
#### i) 當 $p>1$ 時
積分

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

收斂，因此根據[積分判定法](#積分判定法)，我們知道級數 $\sum \cfrac{1}{n^p}$ 也收斂。

#### ii) 當 $p\leq 1$ 時
在這種情況下，

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

我們知道調和級數 $\sum \cfrac{1}{n}$ 發散，因此根據[比較判定法](#比較判定法)，$\sum \cfrac{1}{n^p}$ 也發散。

#### 結論
根據 i) 和 ii)，$p$-級數 $\sum \cfrac{1}{n^p}$ 在 $p>1$ 時收斂，在 $p \leq 1$ 時發散。$\blacksquare$

## 比較判定法
當判定一般項為非負實數的級數（即**正項級數（series of positive terms）**）的收斂/發散時，雅各布·伯努利（Jakob Bernoulli）的**比較判定法（Comparison Test）**非常有用。

正項級數 $\sum a_n$ 是遞增數列，因此如果不是發散到無窮大（$\sum a_n = \infty$），就必定收斂。因此，對於正項級數，

$$ \sum a_n < \infty $$

這樣的表達意味著<u>收斂</u>。

> **比較判定法（Comparison Test）**  
> 當 $0 \leq a_n \leq b_n$ 時，  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

特別是，對於正項級數中類似於我們之前討論的等比級數 $\sum ar^{n-1}$ 或 $p$-級數 $\sum \cfrac{1}{n^p}$ 的形式，如 $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$ 等，積極嘗試使用比較判定法是個好主意。

後面將討論的其他幾種收斂/發散判定法都可以從這個**比較判定法**推導出來，從這個意義上說，比較判定法可以說是最重要的。

### 極限比較判定法
對於正項級數 $\sum a_n$ 和 $\sum b_n$，如果兩個級數的一般項之比 $a_n/b_n$ 中分子和分母的主導項（dominant term）相互抵消，使得 $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{為有限正數)}$，且我們知道級數 $\sum b_n$ 的收斂/發散情況，那麼我們可以使用以下的**極限比較判定法（Limit Comparison Test）**。

> **極限比較判定法（Limit Comparison Test）**  
> 如果
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{為有限正數)}$$
>
> 則兩個級數 $\sum a_n$ 和 $\sum b_n$ 要麼都收斂，要麼都發散。也就是說，$ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$。
{: .prompt-info }

## 根式判定法
> **定理**  
> 對於正項級數 $\sum a_n$ 和正數 $\epsilon < 1$  
> - 若對所有 $n$ 都有 $\sqrt[n]{a_n}< 1-\epsilon$，則級數 $\sum a_n$ 收斂
> - 若對所有 $n$ 都有 $\sqrt[n]{a_n}> 1+\epsilon$，則級數 $\sum a_n$ 發散
{: .prompt-info }

> **推論：根式判定法（Root Test）**  
> 對於正項級數 $\sum a_n$，若極限值
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> 存在，則
> - $r<1$ 時級數 $\sum a_n$ 收斂
> - $r>1$ 時級數 $\sum a_n$ 發散
{: .prompt-info }

> 在上述推論中，當 $r=1$ 時無法判定收斂/發散，需要使用其他方法。
{: .prompt-warning }

## 比值判定法
> **比值判定法（Ratio Test）**  
> 對於正數序列 $(a_n)$ 和 $0 < r < 1$
> - 若對所有 $n$ 都有 $a_{n+1}/a_n \leq r$，則級數 $\sum a_n$ 收斂
> - 若對所有 $n$ 都有 $a_{n+1}/a_n \geq 1$，則級數 $\sum a_n$ 發散
{: .prompt-info }

> **推論**  
> 對於正數序列 $(a_n)$，若極限值 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ 存在，則
> - $\rho < 1$ 時級數 $\sum a_n$ 收斂
> - $\rho > 1$ 時級數 $\sum a_n$ 發散
{: .prompt-info }

## 積分判定法
使用積分法可以判定由遞減的正數列組成的級數的收斂/發散。

> **積分判定法（Integral Test）**  
> 對於連續函數 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$，若 $f$ 為遞減函數且恆為正，則級數 $\sum f(n)$ 收斂的充要條件是積分
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> 收斂。
{: .prompt-info }

### 證明
由於函數 $f(x)$ 連續且為遞減函數，同時恆為正，因此不等式

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

成立。將這個不等式從 $n=1$ 到一般項逐項相加，我們得到不等式

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

現在使用[比較判定法](#比較判定法)，我們就得到了想要的結果。$\blacksquare$

## 交錯級數
如果級數 $\sum a_n$ 的一般項不為零，且每一項 $a_n$ 的符號與其下一項 $a_{n+1}$ 的符號相反，即正項和負項交替出現的級數，我們稱之為**交錯級數（alternating series）**。

對於交錯級數，我們可以有效地利用以下由德國數學家戈特弗里德·威廉·萊布尼茨（Gottfried Wilhelm Leibniz）發現的定理來判定其收斂/發散。

> **交錯級數判定法（Alternating Series Test）**  
> 如果
> 1. 對所有 $n$，$a_n$ 和 $a_{n+1}$ 的符號不同，
> 2. 對所有 $n$，$\|a_n\| \geq \|a_{n+1}\|$，
> 3. $\lim_{n\to\infty} a_n = 0$，
>
> 則交錯級數 $\sum a_n$ 收斂。
{: .prompt-info }

## 絕對收斂級數
對於級數 $\sum a_n$，如果級數 $\sum \|a_n\|$ 收斂，我們說"級數 $\sum a_n$ **絕對收斂**（**converge absolutely**）"。

此時，以下定理成立：

> **定理**  
> 絕對收斂的級數必定收斂。
{: .prompt-info }

> 上述定理的逆命題不成立。  
> 如果一個級數收斂但不絕對收斂，我們稱之為"**條件收斂**（**converge conditionally**）"。
{: .prompt-warning }

### 證明
對於實數 $a$，定義

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

則有

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

因為 $0 \leq a^\pm \leq \|a\|$，根據[比較判定法](#比較判定法)，如果級數 $\sum \|a_n\|$ 收斂，則級數 $\sum a_n^+$ 和 $\sum a_n^-$ 也都收斂。因此，根據[收斂級數的基本性質](/posts/sequences-and-series/#收斂級數的基本性質)，

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

也收斂。$\blacksquare$
