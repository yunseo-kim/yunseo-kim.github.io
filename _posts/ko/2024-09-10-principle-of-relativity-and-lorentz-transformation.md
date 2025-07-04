---
title: 상대성 원리와 로런츠 변환
description: 기준계의 개념과 고전역학에서 널리 사용해왔던 좌표 변환인 갈릴레이 변환에 대해 알아본다. 또한 로런츠 변환의 등장 배경이 된
  맥스웰 방정식과 마이컬슨-몰리 실험을 간단히 살펴보고, 로런츠 변환의 변환행렬을 유도한다.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **상대성 원리**: 등속도로 운동하는 서로 다른 기준계에 대해 모든 물리 법칙이 동일해야 한다는 원리
{: .prompt-info }

> **로런츠 인자 $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **로런츠 변환**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **역 로런츠 변환**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## 기준계와 상대성 원리
### 기준계 (frame of reference)
- **기준계(frame of reference)**: 어떤 물체가 움직인다는 것은 그 위치가 다른 물체에 대하여 상대적으로 변한다는 것으로, 모든 운동은 상대적이기 때문에 어떤 운동을 기술하기 위해서는 그 기준이 되는 기준계를 설정해야 한다.
- **관성기준계(inertial frames of reference)**: 뉴턴(Newton)의 운동 제 1법칙("물체에 작용하는 알짜힘이 0인 한 물체의 운동 상태는 불변한다.")이 성립하는 계. 어느 한 관성계에 대해 등속도로 움직이는 임의의 기준계는 관성기준계이다.

### 상대성 원리 (Principle of Relativity)
물리학의 주요 개념 중 하나이자 기본 전제로, 등속도로 운동하는 서로 다른 기준계에 대해 모든 물리 법칙이 동일해야 한다는 원리이다. 만약 상대적으로 움직이는 관측자들에게 물리 법칙이 서로 다르다면 이 차이를 이용해 하나의 절대기준계를 설정하여 누가 정지해 있고 누가 움직이는지 알 수 있게 된다. 그러나 상대성 원리에 따르면 이러한 구별은 없으므로, 전 우주에 대한 절대기준계 또는 절대운동은 존재하지 않으며 모든 관성기준계는 동등하다.

## 갈릴레이 변환의 한계점
### 갈릴레이 변환 (Galilean transformation)
두 관성계 $S$와 $S^{\prime}$이 존재하고, $S^{\prime}$은 $S$에 대해 $+x$ 방향의 일정한 속도 $\vec{v}$로 움직이며, 동일한 한 사건을 $S$에서는 시각 $t$일 때 좌표 $(x, y, z)$에서 일어난 것으로, $S^{\prime}$에서는 시각 $t^{\prime}$일 때 좌표 $(x^{\prime}, y^{\prime}, z^{\prime})$에서 일어난 것으로 관찰했다고 하자.

이때, $S^{\prime}$에서 측정한 운동의 $x$ 방향 값은 $S$에서 측정한 값보다 $S^{\prime}$이 $S$에 대해 $x$방향으로 움직인 거리인 $\vec{v}t$만큼 더 작을 것이므로

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

이고, $y$와 $z$ 방향으로는 상대적인 운동이 없으므로

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

이며, 직관적으로

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

일 것이라 가정할 수 있다. 위의 식 ($\ref{eqn:galilean_transform_x}$)에서 ($\ref{eqn:galilean_transform_t}$)까지와 같이 물리학에서 고전적으로 사용하던 서로 다른 관성계 간의 좌표 변환을 **갈릴레이 변환(Galilean transformation)**이라고 하며, 이는 일상적인 상황에서 대부분 맞아떨어지기에 간단하면서도 직관적이다. 그러나 후술하겠지만 이는 맥스웰 방정식과 모순된다.

### 맥스웰 방정식
패러데이(Faraday), 앙페르(Ampere) 등의 다른 과학자들이 제안한 아이디어와 선행 연구 결과를 11800년대 후반에 맥스웰(Maxwell)이 확장하여 전기와 자기는 사실 하나의 힘이라는 것을 밝혔으며, 전자기장을 기술하는 다음 4개의 방정식을 유도하였다.

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: 임의의 폐곡면을 통과하는 전기 선속은 내부의 알짜 전하량과 동일하다(가우스 법칙).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: 자기 홀극(자하)은 존재하지 않는다.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: 자기장의 변화는 전기장을 만든다(패러데이 법칙).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: 전기장의 변화와 전류는 자기장을 만든다.(앙페르-맥스웰 법칙)}
\end{gather*}$$

맥스웰 방정식은 이전까지 알려진 전기와 자기 현상을 모두 성공적으로 설명할 수 있었으며, 전자기파의 존재를 예측하였고 또한 진공에서 전자기파의 속력 $c$는 불변하는 상수임을 도출해 내며 전자기학의 핵심 공식으로 자리하였다.

### 갈릴레이 변환과 맥스웰 방정식 사이의 모순
갈릴레이 변환을 활용하는 뉴턴 역학은 200년 넘게 물리학의 근간이 되어 왔고, 맥스웰 방정식은 상술하였듯 전기와 자기 현상을 기술하는 핵심 방정식이다. 그러나 이 둘 사이에는 다음과 같은 모순이 발생한다.

- 상대성 원리에 따라 맥스웰 방정식 역시 모든 관성계에서 동일한 형태를 지닐 것이 기대되지만, 한 관성계에서 측정한 값을 갈릴레이 변환을 적용하여 다른 관성계에서 측정한 값으로 전환할 경우 맥스웰 방정식은 매우 다른 형태를 갖게 된다.
- 맥스웰 방정식으로부터 광속 $c$의 크기를 계산할 수 있고 이는 불변하는 상수이나, 뉴턴 역학과 갈릴레이 변환에 따르면 광속 $c$는 관성계에 따라 다르게 측정된다.

따라서 맥스웰 방정식과 갈릴레이 변환은 서로 맞지 않으며, 둘 중에 적어도 하나는 수정해야만 했다. 이는 후술할 **로런츠 변환(Lorentz transformation)**의 등장 배경이 된다.

## 에테르(aether) 이론과 마이컬슨-몰리 실험
한편 11800년대 물리학에서는 빛도 수면파나 음파와 같은 다른 파동과 마찬가지로 *에테르(aether)*라는 가상의 매질에 의해 전달된다고 여겼으며, 이 에테르의 존재를 발견하고자 노력하였다.

에테르 이론에 따르면 우주공간은 진공이라 할지라도 에테르로 가득 채워져 있으므로, 태양에 대해 약 30km/s의 속력으로 운동하는 지구의 공전에 의해 지구를 가로지르는 에테르 바람이 형성될 것이라 생각하였다.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

이러한 가설을 검증하기 위해, [인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 11887년 마이컬슨(Michelson)은 몰리(Morley)와 협력하여 아래의 간섭계를 활용한 *마이컬슨-몰리 실험(Michelson-Morley Experiment)*을 수행했다.  
![마이컬슨-몰리 간섭계](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *이미지 출처*
> - 저작자: Albert Abraham Michelson with Edward Morley
> - 라이선스: public domain

이 실험에서 광선은 반거울을 통과하며 2개로 나눠진 뒤 각각 간섭계의 직교하는 두 팔을 앞뒤로 왕복하며 총 11m 정도를 진행하고 중간 지점에서 만나며, 이때 두 광선의 위상차에 따라 보강간섭 또는 상쇄간섭 무늬가 나타난다. 에테르 이론에 따르면 에테르에 대한 상대속도에 따라 빛의 속도에 차이가 발생하므로 이 위상차도 변하여 간섭무늬의 변화를 관측할 수 있을 것이라고 기대하였으나, 실제로는 간섭무늬 변화를 관측할 수 없었다. 이러한 실험 결과를 설명하고자 여러 시도들이 있었는데, 그 중에서도 피츠제럴드(FitzGerald)와 로런츠(Lorentz)는 어떤 물체가 <u>에테르에 대해 상대적으로 운동할 경우</u> 길이가 수축한다는 *로런츠-피츠제럴드 수축(Lorentz–FitzGerald contraction)* 또는 *길이 수축(length contraction)*을 제안하였고 이는 로런츠 변환으로 이어진다.

> 로런츠는 이 당시에 에테르가 존재하리라 믿었으며, 길이 수축이 에테르에 대한 상대적 운동에 의해 일어난다고 생각하였다. 이후 아인슈타인(Einstein)이 *특수상대성 이론(Theory of Special Relativity)*으로 로런츠 변환이 갖는 진정한 물리적 의미를 해석함으로써 에테르가 아닌 시공간의 개념으로 길이 수축을 설명하였으며, 에테르는 존재하지 않는다는 것 또한 이후 밝혀진다.
{: .prompt-info }

## 로런츠 변환 (Lorentz transformation)
### 로런츠 변환의 유도
앞서 살펴본 갈릴레이 변환(식 [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$])에서와 같은 상황에서, 맥스웰 방정식과 모순되지 않는 $x$와 $x^{\prime}$ 사이의 올바른 변환 관계가 다음과 같다고 가정하자.

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

여기서 $\gamma$는 $x$와 $t$에는 무관하지만 $\vec{v}$의 함수일 수는 있다. 이와 같이 가정할 수 있는 이유는 다음과 같다.

- $S$에서 일어나는 사건과 $S^{\prime}$에서 일어나는 사건이 일대일 대응하기 위해 $x$와 $x^{\prime}$은 선형 관계이어야 한다.
- 갈릴레이 변환이 일상적인 상황의 역학에서는 옳다는 것이 알려져 있으므로, 식 ($\ref{eqn:galilean_transform_x}$)로 근사할 수 있어야 한다.
- 가급적이면 단순한 형태이어야 한다.

물리 공식들은 기준계 $S$와 $S^{\prime}$에서 같은 모양이어야 하므로 $x$를 $x^{\prime}$과 $t$로 나타내려면 $\vec{v}$의 부호(상대 운동의 방향)만 바꾸면 되며, 두 기준계 사이에는 $\vec{v}$의 부호 외에는 아무런 차이가 없어야 하므로 $\gamma$는 같아야 한다.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

갈릴레이 변환에서와 마찬가지로 $\vec{v}$의 방향에 수직인 성분인 $y$와 $y^{\prime}$, 그리고 $z$와 $z^{\prime}$은 다를 이유가 없으므로,

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

로 놓는다. 이제 식 ($\ref{eqn:lorentz_transform_x}$)를 ($\ref{eqn:lorentz_transform_x_inverse}$)에 대입하면

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

이므로, $t^{\prime}$에 대해 정리하면

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

이 성립한다.

또한 맥스웰 방정식과 모순되지 않기 위해 두 기준계에서 광속은 $c$로 같아야 하므로, 이를 이용하여 $\gamma$를 구할 수 있다. $t=0$일 때 두 기준계의 원점이 같은 장소에 있었다고 하면, 이 초기 조건에 의해 $t^\prime = 0$이다. 이제 $t=t^\prime=0$일 때 $S$와 $S^\prime$의 공통원점에서 섬광이 있었고, 각 기준계의 관측자가 이 빛의 속력을 측정하는 상황을 생각해 보자. 이 경우 기준계 $S$에서는

$$ x = ct \label{eqn:ct_S}\tag{9}$$

이고, 기준계 $S^\prime$에서는

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

이다. 식 ($\ref{eqn:lorentz_transform_x}$)와 ($\ref{eqn:lorentz_transform_t}$)를 이용하여 위 식의 $x$와 $t$를 치환하면

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

가 된다. 이 식을 $x$에 대해 풀면

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

이 된다. 그런데 앞서 식 ($\ref{eqn:ct_S}$)에서 $x=ct$이므로,

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

이고, 따라서

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

이다. 이 $\vec{v}$에 대한 $\gamma$의 식을 식 ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$)에 대입하면 최종적으로 기준계 $S$에서 $S^\prime$으로의 변환식을 얻는다.

### 로런츠 변환의 변환 행렬

앞에서 최종적으로 얻은 변환식은 다음과 같다.

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

이 식들이 **로런츠 변환(Lorentz transformation)**이다. $\vec{\beta}=\vec{v}/c$로 놓으면 행렬로는 아래와 같이 표현할 수 있다.

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

로런츠(Lorentz)는 이 변환식을 사용할 때 모든 관성기준계에서 전자기의 기본 공식들이 같은 형태로 성립함을 보였다. 또한 속력 $v$가 광속 $c$에 비해 매우 작을 때는 $\gamma \to 1$이므로 갈릴레이 변환으로 근사할 수 있다는 것도 확인할 수 있다.

### 역 로런츠 변환 (inverse Lorentz transformation)
때로는 정지한 계 $S$에서의 측정을 움직이는 계 $S^\prime$에서의 측정으로 변환하는 것보다 역으로 움직이는 계 $S^\prime$에서의 측정을 $S$에서의 측정으로 변환시키는 것이 더 편리한 경우가 있다.
이런 경우에는 **역 로런츠 변환(inverse Lorentz transformation)**을 사용할 수 있다.  
($\ref{lorentz_transform_matrix}$)의 역행렬을 구하면 다음과 같은 역 로런츠 변환 행렬을 얻는다.

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

이는 식 ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$)의 프라임이 붙은 물리량과 붙지 않은 물리량을 서로 바꾸고 $v$를 $-v$로(즉, $\beta$를 $-\beta$로) 대체한 것과 같다.

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
