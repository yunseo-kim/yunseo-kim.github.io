---
title: 급수의 수렴/발산 판정(Testing for Convergence or Divergence of a Series)
description: 급수의 수렴/발산을 판정하는 여러 방법들을 종합하여 살펴본다.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **일반항 판정법($n$th-term test for divergence)**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{급수 }\sum a_n \text{은 발산}$
> - **기하급수의 수렴/발산**: 기하급수 $\sum ar^{n-1}$은
>   - $\|r\| < 1$이면 수렴
>   - $\|r\| \geq 1$이면 발산
> - **$p$-급수의 수렴/발산**: $p$-급수 $\sum \cfrac{1}{n^p}$은
>   - $p>1$이면 수렴
>   - $p\leq 1$이면 발산
> - **비교판정법(Comparison Test)**: $0 \leq a_n \leq b_n$일 때,  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **극한비교판정법(Limit Comparison Test)**: 만약 $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{는 유한한 양수)}$라면, 두 급수 $\sum a_n$과 $\sum b_n$은 둘 다 수렴하거나 둘 다 발산
> - 양항급수 $\sum a_n$과 양수 $\epsilon < 1$에 대하여  
>   - 모든 $n$에 대하여 $\sqrt[n]{a_n}< 1-\epsilon$이면 급수 $\sum a_n$은 수렴
>   - 모든 $n$에 대하여 $\sqrt[n]{a_n}> 1+\epsilon$이면 급수 $\sum a_n$은 발산
> - **거듭제곱근 판정법(Root Test)**: 양항급수 $\sum a_n$에서 극한값 $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$이 존재할 경우,
>   - $r<1$이면 급수 $\sum a_n$은 수렴
>   - $r>1$이면 급수 $\sum a_n$은 발산
> - **비율판정법(Ratio Test)**: 양수의 수열 $(a_n)$과 $0 < r < 1$에 대하여
>   - 모든 $n$에 대하여 $a_{n+1}/a_n \leq r$이면, 급수 $\sum a_n$은 수렴
>   - 모든 $n$에 대하여 $a_{n+1}/a_n \geq 1$이면, 급수 $\sum a_n$은 발산
> - 양수의 수열 $(a_n)$에서 극한값 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$이 존재한다고 하면,
>   - $\rho < 1$이면 급수 $\sum a_n$은 수렴
>   - $\rho > 1$이면 급수 $\sum a_n$은 발산
> - **적분판정법(Integral Test)**: 연속함수 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$이 감소함수이고 항상 $f(x)>0$일 때, 급수 $\sum f(n)$이 수렴할 필요충분조건은 적분 $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$가 수렴하는 것
> - **교대급수 판정법(Alternating Series Test)**: 다음 조건을 만족하는 경우 교대급수 $\sum a_n$은 수렴
>   1. 모든 $n$에 대하여 $a_n$과 $a_{n+1}$의 부호가 다름
>   2. 모든 $n$에 대하여 $\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - 절대수렴하는 급수는 수렴함. 역은 성립하지 않음.
{: .prompt-info }

## Prerequisites
- [수열과 급수](/posts/sequences-and-series/)

## 들어가며
앞서 [수열과 급수](/posts/sequences-and-series/#급수의-수렴과-발산)에서 급수의 수렴과 발산에 대한 정의를 알아보았다. 이 글에서는 급수의 수렴/발산을 판정할 때 사용할 수 있는 여러 가지 방법들을 정리한다. 일반적으로 급수의 수렴/발산 판정은 급수의 합을 정확하게 구하는 것보다는 훨씬 쉽다.

## 일반항 판정법
급수 $\sum a_n$에 대하여, $a_n$을 해당 급수의 **일반항**이라고 한다.

다음 정리에 의해 어떤 급수는 명백하게 발산함을 쉽게 알 수 있으며, 따라서 어떤 급수의 수렴/발산을 판정할 때는 이를 제일 먼저 확인해 보는 것이 시간 낭비를 막을 수 있는 현명한 방법이다.

> **일반항 판정법($n$th-term test for divergence)**  
> 급수 $\sum a_n$이 수렴하면,
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> 이다. 즉,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{급수 }\sum a_n \text{은 발산} $$
>
> 이다.
{: .prompt-info }

### 증명
수렴하는 어떤 급수 $\sum a_n$의 합을 $l$이라 하고 처음 $n$항까지의 합을

$$ s_n := a_1 + a_2 + \cdots + a_n $$

으로 두면,

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

따라서 충분히 큰($>N$) $n$에 대하여

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

이므로, 수열의 수렴의 정의로부터

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### 주의사항
이 정리의 역은 일반적으로 참이 아니다. 이를 보여주는 대표적인 예시는 **조화급수(harmonic series)**이다.

조화급수는 각 항이 **등차수열**의 역수로 주어진 수열, 즉 **조화수열**에서 얻은 급수이다. 대표적인 조화급수는

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

이다. 이 급수는 발산함을 다음과 같이 보일 수 있다.

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

이처럼 급수 $H_n$이 발산함에도 불구하고, 일반항 $1/n$은 $0$에 수렴함을 알 수 있다.

> $\lim_{n\to\infty} a_n \neq 0$이면 급수 $\sum a_n$은 반드시 발산하지만, $\lim_{n\to\infty} a_n = 0$이라고 해서 급수 $\sum a_n$이 수렴할 거라고 생각하는 것은 위험하며 이 경우 다른 방법들을 사용하여 수렴/발산을 판정해야 한다.
{: .prompt-danger }

## 기하급수
첫항이 1이고 **공비**가 $r$인 등비수열에서 얻은 **기하급수(geometric series)**

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

는 <u>가장 중요하고, 기본적인 급수</u>이다. 이때 등식

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

에서

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

을 얻는다. 한편

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

이므로, 기하급수 ($\ref{eqn:geometric_series}$)가 수렴할 필요충분조건은 $\|r\| < 1$임을 안다.

> **기하급수의 수렴/발산**  
> 기하급수 $\sum ar^{n-1}$은
> - $\|r\| < 1$이면 수렴
> - $\|r\| \geq 1$이면 발산
{: .prompt-info }

이로부터

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

을 얻는다.

### 기하급수와 근삿값
항등식 ($\ref{eqn:sum_of_geometric_series}$)은 $\|r\| < 1$일 때 $\cfrac{1}{1-r}$의 근삿값을 구하는 데에 유용하게 쓰인다.

이 식에 $r=-\epsilon$, $n=2$를 대입하면

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

을 얻는다. 따라서 $0 < \epsilon < 1$이면

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

이므로

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

을 얻는다. 이로부터, 충분히 작은 양수 $\epsilon$에 대하여 $\cfrac{1}{1 + \epsilon}$은 $1 - \epsilon$으로 근사할 수 있음을 알 수 있다.

## $p$-급수 판정법 ($p$-Series Test)  
양의 실수 $p$에 대하여, 다음과 같은 형태의 급수를 **$p$-급수**라고 한다.

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **$p$-급수의 수렴/발산**  
> $p$-급수 $\sum \cfrac{1}{n^p}$은
> - $p>1$이면 수렴
> - $p\leq 1$이면 발산
{: .prompt-info }

$p$-급수에서 $p=1$인 경우 조화급수가 되며, 이는 발산함을 앞서 보였다.  
$p=2$인 경우의 $p$-급수, 즉 $\sum \cfrac{1}{n^2}$의 값을 구하는 문제는, 이 급수가 수렴함을 처음 보였으며 여러 대에 걸쳐 유명한 수학자 여럿을 배출해 낸 가문이기도 한 베르누이 집안의 근거지 이름을 따서 '바젤(Basel) 문제'라고 부른다. 이 문제의 답은 $\cfrac{\pi^2}{6}$임이 알려져 있다.

또한 더 일반적으로는, $p$-급수에서 $p>1$인 경우를 **제타 함수(zeta function)**라고 한다. 이는 레온하르트 오일러(Leonhard Euler)가 [인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 11740년에 도입하고 이후 리만이 이름을 지은 특수함수의 하나로,

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

로 정의한다. 

이 글의 주제에서 다소 벗어나는 데다, 솔직히 말해서 난 공대생이지 수학자는 아니므로 나도 잘 모르기 때문에 여기서 다루진 않으나, 레온하르트 오일러는 **오일러 곱(Euler Product)**이라는 소수(prime number)의 무한곱 형태로도 제타 함수를 표현할 수 있음을 보였으며 이후 제타 함수는 해석적 정수론 하위의 여러 분야에서 핵심적인 위치를 차지한다. 제타 함수의 정의역을 복소수로 확장한 **리만 제타 함수(Riemann zeta function)**와 그에 관한 중요한 미해결 난제인 **리만 가설(Riemann hypothesis)**도 그 중 하나이다.

원래의 주제로 돌아와서, $p$-급수 판정법의 증명을 위해서는 후술할 [비교판정법](#비교판정법)과 [적분판정법](#적분판정법)이 필요하다. 그러나 $p$-급수의 수렴/발산은 기하급수와 함께 바로 뒤에 다룰 [비교판정법](#비교판정법)에서 유용하게 쓰일 수 있기 때문에 의도적으로 앞쪽에 배치하였다.

### 증명
#### i) $p>1$일 때
적분

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

이 수렴하므로, [적분판정법](#적분판정법)에 의해 급수 $\sum \cfrac{1}{n^p}$도 수렴함을 알 수 있다.

#### ii) $p\leq 1$일 때
이 경우

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

이다. 여기서 조화급수 $\sum \cfrac{1}{n}$은 발산함을 알고 있으므로, [비교판정법](#비교판정법)에 의해 $\sum \cfrac{1}{n^p}$ 또한 발산함을 알 수 있다.

#### 결론
i), ii)에 의하여, $p$-급수 $\sum \cfrac{1}{n^p}$은 $p>1$이면 수렴, $p \leq 1$이면 발산한다. $\blacksquare$

## 비교판정법
일반항이 $0$ 이상의 실수로 이루어진 급수인 **양항급수(series of positive terms)**의 수렴/발산을 판정할 때는 야코프 베르누이(Jakob Bernoulli)의 **비교판정법(Comparison Test)**이 유용하다.

양항급수 $\sum a_n$은 증가하는 수열이므로, 무한대로 발산하는 경우($\sum a_n = \infty$)가 아니라면 반드시 수렴하는 것이다. 그러므로 양항급수에서

$$ \sum a_n < \infty $$

와 같은 표현은 <u>수렴한다</u>는 의미이다.

> **비교판정법(Comparison Test)**  
> $0 \leq a_n \leq b_n$일 때,  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

특히, 양항급수 중에서도 $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$ 등과 같이 앞서 살펴본 등비급수 $\sum ar^{n-1}$이나 $p$-급수 $\sum \cfrac{1}{n^p}$과 유사한 형태를 가진 급수의 수렴/발산을 판정할 때는 비교판정법을 적극적으로 시도해 보는 것이 좋다.

후술하는 다른 여러 수렴/발산 판정법들은 모두 이 **비교판정법**으로부터 유도할 수 있으며, 그런 의미에서 비교판정법이 가장 중요하다고 할 수 있다.

### 극한비교판정법
양항급수 $\sum a_n$과 $\sum b_n$에 대하여, 두 급수의 일반항의 비 $a_n/b_n$에서 분자와 분모의 우세한 항(dominant term)이 상쇄되어 $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{는 유한한 양수)}$라고 하자. 이때 급수 $\sum b_n$의 수렴/발산 여부를 알고 있다면 다음의 **극한비교판정법(Limit Comparison Test)**을 활용할 수 있다.

> **극한비교판정법(Limit Comparison Test)**  
> 만약
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{는 유한한 양수)}$$
>
> 라면, 두 급수 $\sum a_n$과 $\sum b_n$은 둘 다 수렴하거나 둘 다 발산한다. 즉, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$이다.
{: .prompt-info }

## 거듭제곱근 판정법
> **정리**  
> 양항급수 $\sum a_n$과 양수 $\epsilon < 1$에 대하여  
> - 모든 $n$에 대하여 $\sqrt[n]{a_n}< 1-\epsilon$이면 급수 $\sum a_n$은 수렴
> - 모든 $n$에 대하여 $\sqrt[n]{a_n}> 1+\epsilon$이면 급수 $\sum a_n$은 발산
{: .prompt-info }

> **따름정리: 거듭제곱근 판정법(Root Test)**  
> 양항급수 $\sum a_n$에서 극한값
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> 이 존재한다고 하자. 이때
> - $r<1$이면 급수 $\sum a_n$은 수렴
> - $r>1$이면 급수 $\sum a_n$은 발산
{: .prompt-info }

> 위의 따름정리에서 $r=1$일 경우에는 수렴/발산을 판정할 수 없으므로 다른 방법을 사용해야 한다.
{: .prompt-warning }

## 비율판정법
> **비율판정법(Ratio Test)**  
> 양수의 수열 $(a_n)$과 $0 < r < 1$에 대하여
> - 모든 $n$에 대하여 $a_{n+1}/a_n \leq r$이면, 급수 $\sum a_n$은 수렴
> - 모든 $n$에 대하여 $a_{n+1}/a_n \geq 1$이면, 급수 $\sum a_n$은 발산
{: .prompt-info }

> **따름정리**  
> 양수의 수열 $(a_n)$에서 극한값 $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$이 존재한다고 하자. 이때
> - $\rho < 1$이면 급수 $\sum a_n$은 수렴
> - $\rho > 1$이면 급수 $\sum a_n$은 발산
{: .prompt-info }

## 적분판정법
적분법을 이용하면 감소하는 양의 수열로 이루어진 급수의 수렴/발산을 판정할 수 있다.

> **적분판정법(Integral Test)**  
> 연속함수 $f: \left[1,\infty \right) \rightarrow \mathbb{R}$이 감소함수이고 항상 $f(x)>0$일 때, 급수 $\sum f(n)$이 수렴할 필요충분조건은 적분
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> 가 수렴하는 것이다.
{: .prompt-info }

### 증명
함수 $f(x)$가 연속이고 감소함수이면서 부호는 항상 양수이므로, 부등식

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

가 성립한다. 이 부등식을 $n=1$부터 일반항까지 변끼리 더하면 부등식

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

을 얻는다. 이제 [비교판정법](#비교판정법)을 쓰면 원하는 결과를 얻는다. $\blacksquare$

## 교대급수
일반항이 $0$이 아니면서 각 항 $a_n$의 부호가 그 다음 항 $a_{n+1}$의 부호와 다른, 즉 양항과 음항이 번갈아 가며 나타나는 급수 $\sum a_n$을 **교대급수(alternating series)**라고 한다.

교대급수에 대하여, 독일의 수학자 고트프리트 빌헬름 라이프니츠(Gottfried Wilhelm Leibniz)가 발견한 다음 정리를 수렴/발산 판정에 유용하게 활용할 수 있다.

> **교대급수 판정법(Alternating Series Test)**  
> 1. 모든 $n$에 대하여 $a_n$과 $a_{n+1}$의 부호가 다르고,
> 2. 모든 $n$에 대하여 $\|a_n\| \geq \|a_{n+1}\|$이며,
> 3. $\lim_{n\to\infty} a_n = 0$이면,
>
> 교대급수 $\sum a_n$은 수렴한다.
{: .prompt-info }

## 절대수렴급수
급수 $\sum a_n$에 대하여 급수 $\sum \|a_n\|$이 수렴하면, "급수 $\sum a_n$은 **절대수렴**한다(**converge absolutely**)"라고 한다.

이때 다음 정리가 성립한다.

> **정리**  
> 절대수렴하는 급수는 수렴한다.
{: .prompt-info }

> 위 정리의 역은 성립하지 않는다.  
> 급수가 수렴하지만 절대수렴하지는 않는 경우 "**조건수렴**한다(**converge conditionally**)"라고 한다.
{: .prompt-warning }

### 증명
실수 $a$에 대하여

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

로 두면,

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

를 얻는다. 그러면 $0 \leq a^\pm \leq \|a\|$이므로, [비교판정법](#비교판정법)에 의하여 급수 $\sum \|a_n\|$이 수렴할 경우 급수 $\sum a_n^+$와 $\sum a_n^-$도 모두 수렴하고, 따라서 [수렴하는 급수의 기본 성질](/posts/sequences-and-series/#수렴하는-급수의-기본-성질)에 의해

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

도 수렴한다. $\blacksquare$
