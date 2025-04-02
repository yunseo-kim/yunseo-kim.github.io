---
title: 級數的收斂/發散判定(Testing for Convergence or Divergence of a Series)
description: 綜合探討判定級數收斂/發散的各種方法。
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **一般項判定法($n$th-term test for divergence)**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{級數 }\sum a_n \text{發散}$
> - **幾何級數的收斂/發散**: 幾何級數 $\sum ar^{n-1}$
>   - $\|r\| < 1$時收斂
>   - $\|r\| \geq 1$時發散
> - **$p$-級數的收斂/發散**: $p$-級數 $\sum \cfrac{1}{n^p}$
>   - $p>1$時收斂
>   - $p\leq 1$時發散
> - **比較判定法(Comparison Test)**: 當 $0 \leq a_n \leq b_n$時,  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **極限比較判定法(Limit Comparison Test)**: 若 $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{為有限正數)}$，則兩個級數 $\sum a_n$和 $\sum b_n$要麼都收斂，要麼都發散
> - 對於正項級數 $\sum a_n$和正數 $\epsilon < 1$  
>   - 若對所有 $n$都有 $\sqrt[n]{a_n}< 1-\epsilon$，則級數 $\sum a_n$收斂
>   - 若對所有 $n$都有 $\sqrt[n]{a_n}> 1+\epsilon$，則級數 $\sum a_n$發散
> - **根式判定法(Root Test)**: 對於正項級數 $\sum a_n$，若極限值 $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$存在，則
>   - $r<1$時，級數 $\sum a_n$收斂
>   - $r>1$時，級數 $\sum a_n$發散
> - **比值判定法(Ratio Test)**: 對於正數數列 $(a_n)$和 $0 < r < 1$
>   - 若對所有 $n$都有 $a_{n+1}/a_n \leq r$，則級數 $\sum a_n$收斂
>   - 若對所有 $n$都有 $a_{n+1}/a_n \geq 1$，則級數 $\sum a_n$發散
> - 對於正數數列 $(a_n)$，若極限值 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$存在，則
>   - $\rho < 1$時，級數 $\sum a_n$收斂
>   - $\rho > 1$時，級數 $\sum a_n$發散
> - **積分判定法(Integral Test)**: 若連續函數 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$為遞減函數且始終 $f(x)>0$，則級數 $\sum f(n)$收斂的充要條件是積分 $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$收斂
> - **交錯級數判定法(Alternating Series Test)**: 若滿足以下條件，則交錯級數 $\sum a_n$收斂
>   1. 對所有 $n$，$a_n$和 $a_{n+1}$的符號不同
>   2. 對所有 $n$，$\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - 絕對收斂的級數必定收斂。反之則不成立。
{: .prompt-info }

## Prerequisites
- [數列與級數](/posts/sequences-and-series/)

## 引言
在之前的[數列與級數](/posts/sequences-and-series/#級數的收斂與發散)中，我們了解了級數收斂與發散的定義。本文將整理判定級數收斂/發散時可以使用的各種方法。一般來說，判定級數的收斂/發散比精確計算級數的和要容易得多。

## 一般項判定法
對於級數 $\sum a_n$，$a_n$稱為該級數的**一般項**。

根據以下定理，我們可以輕易判斷某些級數明顯發散，因此在判定級數收斂/發散時，首先檢查這一點是避免浪費時間的明智做法。

> **一般項判定法($n$th-term test for divergence)**  
> 若級數 $\sum a_n$收斂，則
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> 也就是說，
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{級數 }\sum a_n \text{發散} $$
{: .prompt-info }

### 證明
設某收斂級數 $\sum a_n$的和為 $l$，前 $n$項的和為

$$ s_n := a_1 + a_2 + \cdots + a_n $$

則，

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

因此，對於足夠大的($>N$) $n$，

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

由數列收斂的定義，

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### 注意事項
這個定理的逆命題一般不成立。一個典型的例子是**調和級數(harmonic series)**。

調和級數是由**等差數列**的倒數形成的數列，即**調和數列**所得的級數。最典型的調和級數是

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

這個級數發散，可以如下證明：

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

如此可見，儘管級數 $H_n$發散，但其一般項 $1/n$確實收斂於 $0$。

> 若 $\lim_{n\to\infty} a_n \neq 0$，則級數 $\sum a_n$必定發散，但若 $\lim_{n\to\infty} a_n = 0$，不能因此認為級數 $\sum a_n$會收斂，這種情況下需要使用其他方法來判定收斂/發散。
{: .prompt-danger }

## 幾何級數
首項為1，**公比**為 $r$的等比數列所形成的**幾何級數(geometric series)**

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

是<u>最重要且基本的級數</u>。從等式

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

得到

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

另一方面，

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

因此，幾何級數 ($\ref{eqn:geometric_series}$)收斂的充要條件是 $\|r\| < 1$。

> **幾何級數的收斂/發散**  
> 幾何級數 $\sum ar^{n-1}$
> - $\|r\| < 1$時收斂
> - $\|r\| \geq 1$時發散
{: .prompt-info }

由此得到

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### 幾何級數與近似值
恆等式 ($\ref{eqn:sum_of_geometric_series}$)在 $\|r\| < 1$時對計算 $\cfrac{1}{1-r}$的近似值很有用。

將 $r=-\epsilon$, $n=2$代入這個式子，得到

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

因此，若 $0 < \epsilon < 1$，則

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

所以

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

由此可知，對於足夠小的正數 $\epsilon$，$\cfrac{1}{1 + \epsilon}$可以近似為 $1 - \epsilon$。

## $p$-級數判定法 ($p$-Series Test)  
對於正實數 $p$，以下形式的級數稱為**$p$-級數**：

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **$p$-級數的收斂/發散**  
> $p$-級數 $\sum \cfrac{1}{n^p}$
> - $p>1$時收斂
> - $p\leq 1$時發散
{: .prompt-info }

在 $p$-級數中，當 $p=1$時就是調和級數，我們已經證明它發散。  
當 $p=2$時的 $p$-級數，即 $\sum \cfrac{1}{n^2}$的值計算問題，被稱為「巴塞爾(Basel)問題」，這個名稱來源於首次證明該級數收斂的伯努利家族的發源地。這個問題的答案已知為 $\cfrac{\pi^2}{6}$。

更一般地，$p$-級數中 $p>1$的情況被稱為**zeta函數(zeta function)**。這是由萊昂哈德·歐拉(Leonhard Euler)在[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 11740年引入，後來由黎曼命名的特殊函數之一，定義為：

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

這個主題稍微偏離本文範圍，而且坦白說，我是工科生而非數學家，所以我也不太了解，因此不在此詳述。但值得一提的是，萊昂哈德·歐拉證明了zeta函數也可以用**歐拉乘積(Euler Product)**的形式表示，即素數(prime number)的無限乘積，此後zeta函數在解析數論的多個領域中佔據核心地位。將zeta函數的定義域擴展到複數的**黎曼zeta函數(Riemann zeta function)**以及與之相關的重要未解難題**黎曼猜想(Riemann hypothesis)**就是其中之一。

回到原主題，$p$-級數判定法的證明需要後面將介紹的[比較判定法](#比較判定法)和[積分判定法](#積分判定法)。但由於 $p$-級數的收斂/發散與幾何級數一起在接下來的[比較判定法](#比較判定法)中非常有用，所以我有意將其放在前面。

### 證明
#### i) 當 $p>1$時
積分

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

收斂，因此根據[積分判定法](#積分判定法)，級數 $\sum \cfrac{1}{n^p}$也收斂。

#### ii) 當 $p\leq 1$時
在這種情況下

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

我們知道調和級數 $\sum \cfrac{1}{n}$發散，所以根據[比較判定法](#比較判定法)，$\sum \cfrac{1}{n^p}$也發散。

#### 結論
根據i)和ii)，$p$-級數 $\sum \cfrac{1}{n^p}$在 $p>1$時收斂，在 $p \leq 1$時發散。$\blacksquare$

## 比較判定法
在判定一般項為非負實數的級數（即**正項級數(series of positive terms)**）的收斂/發散時，雅各布·伯努利(Jakob Bernoulli)的**比較判定法(Comparison Test)**非常有用。

正項級數 $\sum a_n$是遞增數列，因此如果不是發散到無窮大（$\sum a_n = \infty$），那麼它必定收斂。所以對於正項級數，

$$ \sum a_n < \infty $$

這樣的表達意味著<u>收斂</u>。

> **比較判定法(Comparison Test)**  
> 當 $0 \leq a_n \leq b_n$時,  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

特別是，對於那些形式類似於前面討論的等比級數 $\sum ar^{n-1}$或 $p$-級數 $\sum \cfrac{1}{n^p}$的正項級數，如 $\sum \cfrac{1}{n^2 + n}$、$\sum \cfrac{\log n}{n^3}$、$\sum \cfrac{1}{2^n + 3^n}$、$\sum \cfrac{1}{\sqrt{n}}$、$\sum \sin{\cfrac{1}{n}}$等，積極嘗試使用比較判定法是個好主意。

後面將介紹的其他多種收斂/發散判定法都可以從這個**比較判定法**推導出來，從這個意義上說，比較判定法可以說是最重要的。

### 極限比較判定法
對於正項級數 $\sum a_n$和 $\sum b_n$，如果兩個級數一般項的比 $a_n/b_n$中分子和分母的主導項(dominant term)相互抵消，使得 $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{為有限正數)}$，且我們已知級數 $\sum b_n$的收斂/發散情況，那麼可以使用以下**極限比較判定法(Limit Comparison Test)**。

> **極限比較判定法(Limit Comparison Test)**  
> 若
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{為有限正數)}$$
>
> 則兩個級數 $\sum a_n$和 $\sum b_n$要麼都收斂，要麼都發散。即 $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$。
{: .prompt-info }

## 根式判定法
> **定理**  
> 對於正項級數 $\sum a_n$和正數 $\epsilon < 1$  
> - 若對所有 $n$都有 $\sqrt[n]{a_n}< 1-\epsilon$，則級數 $\sum a_n$收斂
> - 若對所有 $n$都有 $\sqrt[n]{a_n}> 1+\epsilon$，則級數 $\sum a_n$發散
{: .prompt-info }

> **推論：根式判定法(Root Test)**  
> 對於正項級數 $\sum a_n$，若極限值
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> 存在，則
> - $r<1$時，級數 $\sum a_n$收斂
> - $r>1$時，級數 $\sum a_n$發散
{: .prompt-info }

> 在上述推論中，若 $r=1$，則無法判定收斂/發散，需要使用其他方法。
{: .prompt-warning }

## 比值判定法
> **比值判定法(Ratio Test)**  
> 對於正數數列 $(a_n)$和 $0 < r < 1$
> - 若對所有 $n$都有 $a_{n+1}/a_n \leq r$，則級數 $\sum a_n$收斂
> - 若對所有 $n$都有 $a_{n+1}/a_n \geq 1$，則級數 $\sum a_n$發散
{: .prompt-info }

> **推論**  
> 對於正數數列 $(a_n)$，若極限值 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$存在，則
> - $\rho < 1$時，級數 $\sum a_n$收斂
> - $\rho > 1$時，級數 $\sum a_n$發散
{: .prompt-info }

## 積分判定法
使用積分法可以判定由遞減正數列組成的級數的收斂/發散。

> **積分判定法(Integral Test)**  
> 若連續函數 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$為遞減函數且始終 $f(x)>0$，則級數 $\sum f(n)$收斂的充要條件是積分
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> 收斂。
{: .prompt-info }

### 證明
由於函數 $f(x)$連續且遞減，同時始終為正，因此不等式

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

成立。將這個不等式從 $n=1$到一般項逐項相加，得到不等式

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

現在使用[比較判定法](#比較判定法)即可得到所需結果。$\blacksquare$

## 交錯級數
一般項不為 $0$且每項 $a_n$的符號與下一項 $a_{n+1}$的符號不同，即正項和負項交替出現的級數 $\sum a_n$稱為**交錯級數(alternating series)**。

對於交錯級數，德國數學家戈特弗里德·威廉·萊布尼茨(Gottfried Wilhelm Leibniz)發現的以下定理在判定收斂/發散時非常有用。

> **交錯級數判定法(Alternating Series Test)**  
> 若滿足以下條件：
> 1. 對所有 $n$，$a_n$和 $a_{n+1}$的符號不同，
> 2. 對所有 $n$，$\|a_n\| \geq \|a_{n+1}\|$，
> 3. $\lim_{n\to\infty} a_n = 0$，
>
> 則交錯級數 $\sum a_n$收斂。
{: .prompt-info }

## 絕對收斂級數
對於級數 $\sum a_n$，若級數 $\sum \|a_n\|$收斂，則稱「級數 $\sum a_n$**絕對收斂**(**converge absolutely**)」。

此時以下定理成立：

> **定理**  
> 絕對收斂的級數必定收斂。
{: .prompt-info }

> 上述定理的逆命題不成立。  
> 若級數收斂但不絕對收斂，則稱其「**條件收斂**(**converge conditionally**)」。
{: .prompt-warning }

### 證明
對於實數 $a$，定義

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

則，

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

由於 $0 \leq a^\pm \leq \|a\|$，根據[比較判定法](#比較判定法)，若級數 $\sum \|a_n\|$收斂，則級數 $\sum a_n^+$和 $\sum a_n^-$也都收斂，因此根據[收斂級數的基本性質](/posts/sequences-and-series/#收斂級數的基本性質)，

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

也收斂。$\blacksquare$
