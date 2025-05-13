---
title: 방사 평형 계산
description: 방사성 핵종의 붕괴상수와 반감기, 평균수명의 상관관계에 대해 알아보고, 주어진 붕괴 사슬에서 임의의 시간 t에서의 방사성 핵종의 방사능을 계산해 본다.
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Radioactive Decay]
math: true
mermaid: true
image: /assets/img/atoms.webp
---
## TL;DR
> **임의의 시간 t에서의 방사능**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **붕괴상수와 반감기, 평균수명의 관계**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## 붕괴상수(Decay Constant)
- 어떤 핵이 단위시간당 붕괴할 확률
- 시간에 무관하게 일정한, 핵종에 따라서만 결정되는 상수
- 기호 $\lambda$로 표기

## 방사능(Radioactivity)
시간 $t$에서 아직 붕괴하지 않은 핵의 개수를 n(t)라 하면, 시간 $t$와 $t+dt$ 사이의 간격 $dt$ 동안 평균적으로 $\lambda n(t)$개의 핵이 붕괴한다. 이러한 붕괴율을 그 샘플의 *방사능(radioactivity)* 라 하며, 기호 $\alpha$로 표기한다. 따라서 어떤 시간 $t$에서의 방사능은 다음과 같다.

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## 방사능의 단위
### 퀴리(Curie, Ci)
- 베크렐 단위를 사용하기 전에 전통적으로 사용한 단위
- 라듐-226 1g이 지닌 방사능
- 초당 $3.7\times 10^{10}$회의 핵붕괴($3.7\times 10^{10}\text{Bq}$)

### 베크렐(Becquerel, Bq)
- 국제표준(SI) 단위
- 초당 1회의 핵붕괴
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## 시간에 따른 방사능 변화 계산
시간 $dt$ 동안 $\lambda n(t)$개의 핵이 붕괴하므로, $dt$ 동안 샘플 안에서 붕괴하지 않고 남아 있는 핵의 감소량은 다음과 같이 표현할 수 있다.

$$ -dn(t)=\lambda n(t)dt $$

이를 적분하면

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

이 된다. 양변에 $\lambda$를 곱하면 방사능은

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

이다.

방사능은 *반감기(half-life)* 동안 반으로 줄어드므로

$$ \alpha (T_{1/2})=\alpha_0/2 $$

이를 식 (3)에 대입하면

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

이 된다. 양변에 로그를 취하고 반감기 $T_{1/2}$에 대해 구하면

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

위 식을 $\lambda$에 대해 풀어 식 (3)에 대입하면

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

식 (5)가 식(3)보다 방사성 붕괴 계산에 사용하기 더 용이한 경우가 많은데, 붕괴상수보다는 반감기 값이 주어지는 경우가 더 흔하기 때문이다.

방사성 핵의 *평균수명(mean-life)* $\overline{t}$는 붕괴상수의 역수이다.

$$ \overline{t}=1/\lambda $$

식 (3)으로부터, 한 번의 평균수명 동안 방사능은 초깃값의 $1/e$로 떨어진다는 것을 알 수 있다. 식 (4)로부터 평균수명과 반감기는 아래와 같은 관계가 성립한다.

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ 평균수명 $\overline{t}$ 유도

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## 예제: 방사성 붕괴 사슬 1
어떤 방사성 핵종이 $R$ atom/s의 속도로 생성된다고 가정하자. 이 핵은 생기자마자 바로 방사성 붕괴가 일어난다. 임의의 시각 t에서 이 핵종의 방사능을 구하라.
```mermaid
flowchart LR
	Start[?] -- R --> A[수학적 모델]
	A -- α --> End[?]
```

### 1. 모델 설정

$$ \text{시간에 따른 핵종 변화율} = \text{생성률}-\text{손실률} $$

수학 기호로 표현하면

$$ dn/dt = -\lambda n + R $$

이다. 

### 2. 일반해
$n$에 관한 항을 모두 좌변으로 이항하고, 양변에 $e^{\lambda t}$를 곱하자.

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

$\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$이므로 다음과 같이 정리할 수 있다.

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

양변을 적분하면 다음의 일반해를 얻는다.

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. 특수해
$t=0$일 때 이 핵종의 개수가 $n_0$라 하고 상수 $c$의 값을 구하자.

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

따라서 주어진 상황에 맞는 특수해는 다음과 같다.

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

이다. 위 식의 양변에 $\lambda$를 곱해 이 핵종의 방사능을 구할 수 있다.

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

즉, $t\to\infty$ 일 때 $\alpha_{\text{max}}=R$, $n_{\text{max}}=R/\lambda$로 수렴한다.

## 예제: 방사성 붕괴 사슬 2
아래와 같은 붕괴 사슬에서 방사성 핵종 B의 방사능을 계산하라.
```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. 모델 설정

$$ \text{B 핵의 개수 변화율}=\text{A의 붕괴로 인한 생성률}-\text{B의 C로의 붕괴율} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

$n_A$에 대해 식 (2)를 대입하면 $n_B$에 대한 다음의 미분방정식을 얻는다.

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. 일반해
미분방정식을 풀기 위해 $n_B$에 대한 항을 모두 좌변으로 이항하고, 양변에 $e^{\lambda_B t}$를 곱하자.

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

$\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$이므로 다음과 같이 정리할 수 있다.

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

양변을 적분하면

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

이다. 양변을 $e^{\lambda_B t}$로 나누면 다음의 일반해를 얻는다.

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. 특수해
$t=0$일 때 B 원소의 개수가 $n_{B0}$라고 하고 상수 $c$의 값을 구하자.

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

따라서 주어진 상황에 맞는 특수해는 다음과 같다.

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$
