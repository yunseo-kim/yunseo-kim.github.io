---
title: Testing for Convergence or Divergence of a Series
description: A comprehensive examination of various methods for determining whether a series converges or diverges.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **$n$th-term test for divergence**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{series }\sum a_n \text{ diverges}$
> - **Convergence/divergence of geometric series**: The geometric series $\sum ar^{n-1}$ 
>   - converges if $\|r\| < 1$
>   - diverges if $\|r\| \geq 1$
> - **Convergence/divergence of $p$-series**: The $p$-series $\sum \cfrac{1}{n^p}$
>   - converges if $p>1$
>   - diverges if $p\leq 1$
> - **Comparison Test**: If $0 \leq a_n \leq b_n$, then  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Limit Comparison Test**: If $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ is a finite positive number)}$, then both series $\sum a_n$ and $\sum b_n$ either both converge or both diverge
> - For a series of positive terms $\sum a_n$ and a positive number $\epsilon < 1$  
>   - If $\sqrt[n]{a_n}< 1-\epsilon$ for all $n$, then the series $\sum a_n$ converges
>   - If $\sqrt[n]{a_n}> 1+\epsilon$ for all $n$, then the series $\sum a_n$ diverges
> - **Root Test**: For a series of positive terms $\sum a_n$, if the limit $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ exists, then
>   - the series $\sum a_n$ converges if $r<1$
>   - the series $\sum a_n$ diverges if $r>1$
> - **Ratio Test**: For a sequence of positive terms $(a_n)$ and $0 < r < 1$
>   - If $a_{n+1}/a_n \leq r$ for all $n$, then the series $\sum a_n$ converges
>   - If $a_{n+1}/a_n \geq 1$ for all $n$, then the series $\sum a_n$ diverges
> - For a sequence of positive numbers $(a_n)$, if the limit $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ exists, then
>   - the series $\sum a_n$ converges if $\rho < 1$
>   - the series $\sum a_n$ diverges if $\rho > 1$
> - **Integral Test**: For a continuous, decreasing function $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ with $f(x)>0$ for all $x$, the series $\sum f(n)$ converges if and only if the integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converges
> - **Alternating Series Test**: An alternating series $\sum a_n$ converges if the following conditions are satisfied:
>   1. $a_n$ and $a_{n+1}$ have opposite signs for all $n$
>   2. $\|a_n\| \geq \|a_{n+1}\|$ for all $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - A series that converges absolutely also converges. The converse is not true.
{: .prompt-info }

## Prerequisites
- [Sequences and Series](/posts/sequences-and-series/)

## Introduction
In the previous post on [Sequences and Series](/posts/sequences-and-series/#convergence-and-divergence-of-series), we covered the definitions of convergence and divergence of series. In this post, we will summarize various methods for determining whether a series converges or diverges. Generally, testing for convergence or divergence of a series is much easier than finding the exact sum of the series.

## The $n$th-Term Test
For a series $\sum a_n$, we call $a_n$ the **general term** of the series.

The following theorem allows us to easily identify some obviously divergent series, making it a wise first step when testing for convergence or divergence to avoid wasting time.

> **$n$th-term test for divergence**  
> If a series $\sum a_n$ converges, then
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> That is,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{series }\sum a_n \text{ diverges} $$
{: .prompt-info }

### Proof
Let $l$ be the sum of a convergent series $\sum a_n$ and define the partial sum of the first $n$ terms as

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Then,

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Therefore, for sufficiently large $n$ (where $n > N$),

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

From the definition of convergence of a sequence,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Caution
The converse of this theorem is generally not true. A classic example that demonstrates this is the **harmonic series**.

The harmonic series is a series whose terms are the reciprocals of an **arithmetic sequence**, forming a **harmonic sequence**. The most well-known harmonic series is

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

This series diverges, as can be shown by:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Thus, despite the fact that the harmonic series $H_n$ diverges, its general term $1/n$ converges to $0$.

> If $\lim_{n\to\infty} a_n \neq 0$, then the series $\sum a_n$ must diverge, but assuming that a series $\sum a_n$ converges just because $\lim_{n\to\infty} a_n = 0$ is dangerous. In such cases, other methods must be used to determine convergence or divergence.
{: .prompt-danger }

## Geometric Series
The **geometric series** derived from a geometric sequence with first term 1 and common ratio $r$,

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

is <u>the most important and fundamental series</u>. From the equation

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

we get

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Meanwhile,

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

Therefore, we know that the necessary and sufficient condition for the geometric series ($\ref{eqn:geometric_series}$) to converge is $\|r\| < 1$.

> **Convergence/divergence of geometric series**  
> The geometric series $\sum ar^{n-1}$
> - converges if $\|r\| < 1$
> - diverges if $\|r\| \geq 1$
{: .prompt-info }

From this, we obtain

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Geometric Series and Approximations
The identity ($\ref{eqn:sum_of_geometric_series}$) is useful for finding approximations of $\cfrac{1}{1-r}$ when $\|r\| < 1$.

Substituting $r=-\epsilon$ and $n=2$ into this equation, we get

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Therefore, if $0 < \epsilon < 1$, then

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

which gives us

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

From this, we can see that for sufficiently small positive $\epsilon$, $\cfrac{1}{1 + \epsilon}$ can be approximated by $1 - \epsilon$.

## $p$-Series Test
For a positive real number $p$, a series of the following form is called a **$p$-series**:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Convergence/divergence of $p$-series**  
> The $p$-series $\sum \cfrac{1}{n^p}$
> - converges if $p>1$
> - diverges if $p\leq 1$
{: .prompt-info }

When $p=1$ in a $p$-series, we get the harmonic series, which we've already shown diverges.  
The problem of finding the value of the $p$-series when $p=2$, i.e., $\sum \cfrac{1}{n^2}$, is known as the 'Basel problem', named after the hometown of the Bernoulli family, which produced several famous mathematicians over multiple generations and first proved that this series converges. The answer to this problem is known to be $\cfrac{\pi^2}{6}$.

More generally, the $p$-series where $p>1$ is called the **zeta function**. This is a special function introduced by Leonhard Euler in 11740 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) and later named by Riemann, defined as

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

This topic somewhat deviates from the main subject of this post, and frankly, as an engineering student rather than a mathematician, I don't know much about it, so I won't cover it here. However, Leonhard Euler showed that the zeta function can also be expressed as an infinite product of primes, known as the **Euler Product**, and subsequently, the zeta function has occupied a central position in various fields under analytic number theory. The **Riemann zeta function**, which extends the domain of the zeta function to complex numbers, and the important unsolved problem related to it, the **Riemann hypothesis**, are among these.

Returning to our original topic, the proof of the $p$-series test requires the [Comparison Test](#comparison-test) and the [Integral Test](#integral-test), which will be discussed later. However, the convergence/divergence of $p$-series can be usefully applied in the [Comparison Test](#comparison-test) along with geometric series, which is why I've intentionally placed it earlier in this post.

### Proof
#### i) When $p>1$
The integral

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converges, so by the [Integral Test](#integral-test), the series $\sum \cfrac{1}{n^p}$ also converges.

#### ii) When $p\leq 1$
In this case,

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Since we know that the harmonic series $\sum \cfrac{1}{n}$ diverges, by the [Comparison Test](#comparison-test), $\sum \cfrac{1}{n^p}$ also diverges.

#### Conclusion
By i) and ii), the $p$-series $\sum \cfrac{1}{n^p}$ converges if $p>1$ and diverges if $p \leq 1$. $\blacksquare$

## Comparison Test
Jakob Bernoulli's **Comparison Test** is useful for determining the convergence/divergence of a **series of positive terms**, where each term is a non-negative real number.

Since a series of positive terms forms an increasing sequence, it must converge unless it diverges to infinity ($\sum a_n = \infty$). Therefore, in a series of positive terms, the expression

$$ \sum a_n < \infty $$

means that <u>the series converges</u>.

> **Comparison Test**  
> If $0 \leq a_n \leq b_n$, then  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

In particular, for series of positive terms that have forms similar to the geometric series $\sum ar^{n-1}$ or the $p$-series $\sum \cfrac{1}{n^p}$ that we've examined earlier, such as $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, it's a good idea to actively try the Comparison Test.

All the other convergence/divergence tests that will be discussed later can be derived from this **Comparison Test**, making it arguably the most important test.

### Limit Comparison Test
For series of positive terms $\sum a_n$ and $\sum b_n$, if the dominant terms in the numerator and denominator of the ratio $a_n/b_n$ cancel out, resulting in $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ is a finite positive number)}$, and if we know whether the series $\sum b_n$ converges or diverges, then we can use the following **Limit Comparison Test**.

> **Limit Comparison Test**  
> If
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ is a finite positive number)}$$
>
> then both series $\sum a_n$ and $\sum b_n$ either both converge or both diverge. That is, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Root Test
> **Theorem**  
> For a series of positive terms $\sum a_n$ and a positive number $\epsilon < 1$  
> - If $\sqrt[n]{a_n}< 1-\epsilon$ for all $n$, then the series $\sum a_n$ converges
> - If $\sqrt[n]{a_n}> 1+\epsilon$ for all $n$, then the series $\sum a_n$ diverges
{: .prompt-info }

> **Corollary: Root Test**  
> For a series of positive terms $\sum a_n$, if the limit
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> exists, then
> - the series $\sum a_n$ converges if $r<1$
> - the series $\sum a_n$ diverges if $r>1$
{: .prompt-info }

> In the corollary above, if $r=1$, the test is inconclusive, and other methods must be used to determine convergence or divergence.
{: .prompt-warning }

## Ratio Test
> **Ratio Test**  
> For a sequence of positive terms $(a_n)$ and $0 < r < 1$
> - If $a_{n+1}/a_n \leq r$ for all $n$, then the series $\sum a_n$ converges
> - If $a_{n+1}/a_n \geq 1$ for all $n$, then the series $\sum a_n$ diverges
{: .prompt-info }

> **Corollary**  
> For a sequence of positive terms $(a_n)$, if the limit $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ exists, then
> - the series $\sum a_n$ converges if $\rho < 1$
> - the series $\sum a_n$ diverges if $\rho > 1$
{: .prompt-info }

## Integral Test
Integration can be used to determine the convergence/divergence of a series composed of a decreasing sequence of positive terms.

> **Integral Test**  
> For a continuous, decreasing function $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ with $f(x)>0$ for all $x$, the series $\sum f(n)$ converges if and only if the integral
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converges.
{: .prompt-info }

### Proof
Since the function $f(x)$ is continuous, decreasing, and always positive, the inequality

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

holds. Adding these inequalities from $n=1$ to the general term, we get

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Now, using the [Comparison Test](#comparison-test), we obtain the desired result. $\blacksquare$

## Alternating Series
A series $\sum a_n$ where each term $a_n$ is non-zero and has a sign opposite to that of the next term $a_{n+1}$, i.e., where positive and negative terms alternate, is called an **alternating series**.

For alternating series, the following theorem discovered by the German mathematician Gottfried Wilhelm Leibniz can be usefully applied to determine convergence/divergence.

> **Alternating Series Test**  
> If
> 1. $a_n$ and $a_{n+1}$ have opposite signs for all $n$,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ for all $n$, and
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> then the alternating series $\sum a_n$ converges.
{: .prompt-info }

## Absolute Convergence
For a series $\sum a_n$, if the series $\sum \|a_n\|$ converges, we say that "the series $\sum a_n$ **converges absolutely**."

The following theorem holds:

> **Theorem**  
> A series that converges absolutely also converges.
{: .prompt-info }

> The converse of the above theorem is not true.  
> If a series converges but does not converge absolutely, we say it "**converges conditionally**."
{: .prompt-warning }

### Proof
For a real number $a$, define

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Then,

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Since $0 \leq a^\pm \leq \|a\|$, by the [Comparison Test](#comparison-test), if the series $\sum \|a_n\|$ converges, then both series $\sum a_n^+$ and $\sum a_n^-$ also converge, and therefore, by the [basic properties of convergent series](/posts/sequences-and-series/#basic-properties-of-convergent-series),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

also converges. $\blacksquare$
