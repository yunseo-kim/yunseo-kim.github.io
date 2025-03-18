---
title: 級数の収束/発散判定（Testing for Convergence or Divergence of a Series）
description: 級数の収束/発散を判定する様々な方法を総合的に見ていく。
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **一般項判定法（$n$th-term test for divergence）**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{級数 }\sum a_n \text{は発散}$
> - **等比級数の収束/発散**: 等比級数 $\sum ar^{n-1}$は
>   - $\|r\| < 1$なら収束
>   - $\|r\| \geq 1$なら発散
> - **$p$-級数の収束/発散**: $p$-級数 $\sum \cfrac{1}{n^p}$は
>   - $p>1$なら収束
>   - $p\leq 1$なら発散
> - **比較判定法（Comparison Test）**: $0 \leq a_n \leq b_n$のとき、  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **極限比較判定法（Limit Comparison Test）**: もし $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{は有限な正数)}$ならば、二つの級数 $\sum a_n$と $\sum b_n$は共に収束するか共に発散する
> - 正項級数 $\sum a_n$と正数 $\epsilon < 1$に対して  
>   - すべての $n$に対して $\sqrt[n]{a_n}< 1-\epsilon$ならば級数 $\sum a_n$は収束
>   - すべての $n$に対して $\sqrt[n]{a_n}> 1+\epsilon$ならば級数 $\sum a_n$は発散
> - **冪根判定法（Root Test）**: 正項級数 $\sum a_n$において極限値 $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$が存在する場合、
>   - $r<1$ならば級数 $\sum a_n$は収束
>   - $r>1$ならば級数 $\sum a_n$は発散
> - **比判定法（Ratio Test）**: 正数の数列 $(a_n)$と $0 < r < 1$に対して
>   - すべての $n$に対して $a_{n+1}/a_n \leq r$ならば、級数 $\sum a_n$は収束
>   - すべての $n$に対して $a_{n+1}/a_n \geq 1$ならば、級数 $\sum a_n$は発散
> - 正数の数列 $(a_n)$において極限値 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$が存在するとすると、
>   - $\rho < 1$ならば級数 $\sum a_n$は収束
>   - $\rho > 1$ならば級数 $\sum a_n$は発散
> - **積分判定法（Integral Test）**: 連続関数 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$が減少関数で常に $f(x)>0$のとき、級数 $\sum f(n)$が収束する必要十分条件は積分 $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$が収束すること
> - **交代級数判定法（Alternating Series Test）**: 次の条件を満たす場合、交代級数 $\sum a_n$は収束する
>   1. すべての $n$に対して $a_n$と $a_{n+1}$の符号が異なる
>   2. すべての $n$に対して $\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - 絶対収束する級数は収束する。逆は成り立たない。
{: .prompt-info }

## Prerequisites
- [数列と級数](/posts/sequences-and-series/)

## はじめに
先に[数列と級数](/posts/sequences-and-series/#級数の収束と発散)で級数の収束と発散についての定義を見てきました。この記事では、級数の収束/発散を判定する際に使用できる様々な方法をまとめます。一般的に、級数の収束/発散の判定は、級数の和を正確に求めるよりもはるかに簡単です。

## 一般項判定法
級数 $\sum a_n$に対して、$a_n$をその級数の**一般項**と呼びます。

次の定理により、ある級数が明らかに発散することを簡単に知ることができ、したがって、ある級数の収束/発散を判定する際には、これを最初に確認してみることが時間の無駄を防ぐ賢明な方法です。

> **一般項判定法（$n$th-term test for divergence）**  
> 級数 $\sum a_n$が収束するならば、
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> である。つまり、
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{級数 }\sum a_n \text{は発散} $$
>
> である。
{: .prompt-info }

### 証明
収束するある級数 $\sum a_n$の和を $l$とし、最初の $n$項までの和を

$$ s_n := a_1 + a_2 + \cdots + a_n $$

とすると、

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

したがって、十分に大きい（$>N$）$n$に対して

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

となるので、数列の収束の定義から

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### 注意事項
この定理の逆は一般的に真ではありません。これを示す代表的な例は**調和級数（harmonic series）**です。

調和級数は各項が**等差数列**の逆数で与えられる数列、つまり**調和数列**から得られる級数です。代表的な調和級数は

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

です。この級数が発散することを次のように示すことができます。

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

このように級数 $H_n$が発散するにもかかわらず、一般項 $1/n$は $0$に収束することがわかります。

> $\lim_{n\to\infty} a_n \neq 0$ならば級数 $\sum a_n$は必ず発散しますが、$\lim_{n\to\infty} a_n = 0$だからといって級数 $\sum a_n$が収束すると考えるのは危険であり、この場合は他の方法を使用して収束/発散を判定する必要があります。
{: .prompt-danger }

## 等比級数
初項が1で**公比**が $r$の等比数列から得られる**等比級数（geometric series）**

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

は<u>最も重要で、基本的な級数</u>です。このとき等式

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

から

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

を得ます。一方

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

であるため、等比級数 ($\ref{eqn:geometric_series}$)が収束する必要十分条件は $\|r\| < 1$であることがわかります。

> **等比級数の収束/発散**  
> 等比級数 $\sum ar^{n-1}$は
> - $\|r\| < 1$なら収束
> - $\|r\| \geq 1$なら発散
{: .prompt-info }

これにより

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

を得ます。

### 等比級数と近似値
恒等式 ($\ref{eqn:sum_of_geometric_series}$)は $|r| < 1$のとき $\cfrac{1}{1-r}$の近似値を求めるのに有用に使われます。

この式に $r=-\epsilon$、$n=2$を代入すると

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

を得ます。したがって $0 < \epsilon < 1$ならば

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

となるので

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

を得ます。これにより、十分に小さい正数 $\epsilon$に対して $\cfrac{1}{1 + \epsilon}$は $1 - \epsilon$で近似できることがわかります。

## $p$-級数判定法（$p$-Series Test）  
正の実数 $p$に対して、次のような形の級数を**$p$-級数**と呼びます。

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **$p$-級数の収束/発散**  
> $p$-級数 $\sum \cfrac{1}{n^p}$は
> - $p>1$なら収束
> - $p\leq 1$なら発散
{: .prompt-info }

$p$-級数で $p=1$の場合は調和級数となり、これが発散することは先に示しました。  
$p=2$の場合の $p$-級数、つまり $\sum \cfrac{1}{n^2}$の値を求める問題は、この級数が収束することを最初に示し、また数世代にわたって有名な数学者を多数輩出したことでも知られるベルヌーイ家の拠点の名前を取って「バーゼル（Basel）問題」と呼ばれています。この問題の答えは $\cfrac{\pi^2}{6}$であることが知られています。

また、より一般的には、$p$-級数で $p>1$の場合を**ゼータ関数（zeta function）**と呼びます。これはレオンハルト・オイラー（Leonhard Euler）が1740年に導入し、その後リーマンが名付けた特殊関数の一つで、

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

と定義されます。

この記事のテーマからやや外れるうえ、正直に言えば私は工学部生であって数学者ではないので私もよく知らないため、ここでは扱いませんが、レオンハルト・オイラーは**オイラー積（Euler Product）**という素数（prime number）の無限積の形でもゼータ関数を表現できることを示し、その後ゼータ関数は解析的整数論の下位の様々な分野で中心的な位置を占めています。ゼータ関数の定義域を複素数に拡張した**リーマンゼータ関数（Riemann zeta function）**とそれに関する重要な未解決問題である**リーマン予想（Riemann hypothesis）**もその一つです。

元のテーマに戻って、$p$-級数判定法の証明には後述する[比較判定法](#比較判定法)と[積分判定法](#積分判定法)が必要です。しかし、$p$-級数の収束/発散は等比級数と共にすぐ後で扱う[比較判定法](#比較判定法)で有用に使えるため、意図的に前の方に配置しました。

### 証明
#### i) $p>1$のとき
積分

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

が収束するので、[積分判定法](#積分判定法)により級数 $\sum \cfrac{1}{n^p}$も収束することがわかります。

#### ii) $p\leq 1$のとき
この場合

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

です。ここで調和級数 $\sum \cfrac{1}{n}$は発散することを知っているので、[比較判定法](#比較判定法)により $\sum \cfrac{1}{n^p}$ も発散することがわかります。

#### 結論
i)、ii)により、$p$-級数 $\sum \cfrac{1}{n^p}$は $p>1$なら収束、$p \leq 1$なら発散します。$\blacksquare$

## 比較判定法
一般項が $0$ 以上の実数からなる級数である**正項級数（series of positive terms）**の収束/発散を判定するときは、ヤコブ・ベルヌーイ（Jakob Bernoulli）の**比較判定法（Comparison Test）**が有用です。

正項級数 $\sum a_n$は増加する数列であるため、無限大に発散する場合（$\sum a_n = \infty$）でなければ必ず収束するのです。したがって正項級数において

$$ \sum a_n < \infty $$

という表現は<u>収束する</u>という意味です。

> **比較判定法（Comparison Test）**  
> $0 \leq a_n \leq b_n$のとき、  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

特に、正項級数の中でも $\sum \cfrac{1}{n^2 + n}$、$\sum \cfrac{\log n}{n^3}$、$\sum \cfrac{1}{2^n + 3^n}$、$\sum \cfrac{1}{\sqrt{n}}$、$\sum \sin{\cfrac{1}{n}}$ などのように、先に見た等比級数 $\sum ar^{n-1}$や $p$-級数 $\sum \cfrac{1}{n^p}$と類似した形を持つ級数の収束/発散を判定するときは、比較判定法を積極的に試してみるのが良いでしょう。

後述する他の様々な収束/発散判定法はすべてこの**比較判定法**から導くことができ、その意味で比較判定法が最も重要だと言えます。

### 極限比較判定法
正項級数 $\sum a_n$と $\sum b_n$に対して、二つの級数の一般項の比 $a_n/b_n$で分子と分母の優勢な項（dominant term）が相殺されて $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{は有限な正数)}$とします。このとき級数 $\sum b_n$の収束/発散がわかっていれば、次の**極限比較判定法（Limit Comparison Test）**を活用できます。

> **極限比較判定法（Limit Comparison Test）**  
> もし
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{は有限な正数)}$$
>
> ならば、二つの級数 $\sum a_n$と $\sum b_n$は共に収束するか共に発散する。つまり、$ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$です。
{: .prompt-info }

## 冪根判定法
> **定理**  
> 正項級数 $\sum a_n$と正数 $\epsilon < 1$に対して  
> - すべての $n$に対して $\sqrt[n]{a_n}< 1-\epsilon$ならば級数 $\sum a_n$は収束
> - すべての $n$に対して $\sqrt[n]{a_n}> 1+\epsilon$ならば級数 $\sum a_n$は発散
{: .prompt-info }

> **系：冪根判定法（Root Test）**  
> 正項級数 $\sum a_n$において極限値
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> が存在するとする。このとき
> - $r<1$ならば級数 $\sum a_n$は収束
> - $r>1$ならば級数 $\sum a_n$は発散
{: .prompt-info }

> 上の系で $r=1$の場合は収束/発散を判定できないので、他の方法を使用する必要があります。
{: .prompt-warning }

## 比判定法
> **比判定法（Ratio Test）**  
> 正数の数列 $(a_n)$と $0 < r < 1$に対して
> - すべての $n$に対して $a_{n+1}/a_n \leq r$ならば、級数 $\sum a_n$は収束
> - すべての $n$に対して $a_{n+1}/a_n \geq 1$ならば、級数 $\sum a_n$は発散
{: .prompt-info }

> **系**  
> 正数の数列 $(a_n)$において極限値 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$が存在するとする。このとき
> - $\rho < 1$ならば級数 $\sum a_n$は収束
> - $\rho > 1$ならば級数 $\sum a_n$は発散
{: .prompt-info }

## 積分判定法
積分法を用いると、減少する正の数列からなる級数の収束/発散を判定できます。

> **積分判定法（Integral Test）**  
> 連続関数 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$が減少関数で常に $f(x)>0$のとき、級数 $\sum f(n)$が収束する必要十分条件は積分
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> が収束することです。
{: .prompt-info }

### 証明
関数 $f(x)$が連続で減少関数であり、符号は常に正であるため、不等式

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

が成り立ちます。この不等式を $n=1$から一般項まで辺々足すと不等式

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

を得ます。ここで[比較判定法](#比較判定法)を使うと望む結果を得ます。$\blacksquare$

## 交代級数
一般項が $0$でなく、各項 $a_n$の符号がその次の項 $a_{n+1}$の符号と異なる、つまり正項と負項が交互に現れる級数 $\sum a_n$を**交代級数（alternating series）**と呼びます。

交代級数について、ドイツの数学者ゴットフリート・ヴィルヘルム・ライプニッツ（Gottfried Wilhelm Leibniz）が発見した次の定理を収束/発散判定に有用に活用できます。

> **交代級数判定法（Alternating Series Test）**  
> 1. すべての $n$に対して $a_n$と $a_{n+1}$の符号が異なり、
> 2. すべての $n$に対して $\|a_n\| \geq \|a_{n+1}\|$であり、
> 3. $\lim_{n\to\infty} a_n = 0$ならば、
>
> 交代級数 $\sum a_n$は収束します。
{: .prompt-info }

## 絶対収束級数
級数 $\sum a_n$に対して級数 $\sum \|a_n\|$が収束するとき、"級数 $\sum a_n$は**絶対収束**する（**converge absolutely**）"と言います。

このとき次の定理が成り立ちます。

> **定理**  
> 絶対収束する級数は収束する。
{: .prompt-info }

> 上の定理の逆は成り立ちません。  
> 級数が収束するが絶対収束はしない場合、"**条件収束**する（**converge conditionally**）"と言います。
{: .prompt-warning }

### 証明
実数 $a$に対して

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

とおくと、

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

を得ます。すると $0 \leq a^\pm \leq \|a\|$なので、[比較判定法](#比較判定法)により級数 $\sum \|a_n\|$が収束する場合、級数 $\sum a_n^+$と $\sum a_n^-$もすべて収束し、したがって[収束する級数の基本的性質](/posts/sequences-and-series/#収束する級数の基本的性質)により

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

も収束します。$\blacksquare$
