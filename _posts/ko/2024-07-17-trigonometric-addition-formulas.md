---
title: 삼각함수의 덧셈정리
description: 삼각함수의 정의와 삼각함수 사이의 관계식을 살펴보고, 이로부터 삼각함수의 덧셈정리 및 파생 공식을 유도한다.
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 삼각함수의 정의
![Unit Circle and Radius Vector](/assets/img/trigonometry/definition.png)
그림과 같이 동경 $\overline{OP}$가 $x$축의 양의 방향과 이루는 각의 크기를 $\theta$라 할 때,
$$
\begin{gather}\begin{split}
\sin \theta = \frac { y } { r } ,\; \cos \theta = \frac { x } { r } ,\; \tan \theta = \frac { y } { x } \\ \csc \theta = \frac { r } { y } ,\; \sec \theta = \frac { r } { x } ,\; \cot \theta = \frac { x } { y } \end{split}\end{gather}
$$
와 같이 정의하고, 이들을 통틀어 삼각함수라고 한다.

## 삼각함수 사이의 관계
1. $$ \csc \theta = \frac { 1 } { \sin \theta } ,\; \sec \theta = \frac { 1 } { \cos \theta } ,\; \cot \theta = \frac { 1 } { \tan \theta } \tag{2}$$
2. $$ \tan \theta = \frac { \sin \theta } { \cos \theta } ,\; \cot \theta = \frac { \cos \theta } { \sin \theta } \tag{3}$$
3. $$ \tag{4} \begin{gather*}
\sin ^ { 2 } \theta + \cos ^ { 2 } \theta = 1 \\
\tan ^ { 2 } \theta + 1 = \sec ^ { 2 } \theta \\
1 + \cot ^ { 2 } \theta = \csc ^ { 2 } \theta 
\end{gather*} 
$$

## 삼각함수의 덧셈정리
![Deriving the Trigonometric Addition Formulas](/assets/img/trigonometry/trigonometric-addition-formulas.png)
그림과 같이 $x$축의 양의 방향과 이루는 각의 크기가 $\alpha+\beta,\, 0,\, \alpha,\, -\beta$인 네 동경이 단위원과 만나는 점을 각각 $P, Q, P^{\prime}, Q^{\prime}$이라 하자.

두 점 $P, Q$의 좌표는

$$
P(\cos(\alpha+\beta), \sin(\alpha+\beta)),\; Q(1,0)
$$

이므로

$$
\begin{align*} \overline { P^ { \prime } Q^ { \prime } } ^2&= \{ \cos \alpha - \cos ( - \beta ) \} ^ { 2 } + \{ \sin \alpha - \sin ( - \beta ) \} ^ { 2 } \\
&= 2 - 2 \cos \alpha \cos ( - \beta ) - 2 \sin \alpha \sin ( - \beta ) \\
&= 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta. \end{align*}
$$

$\overline{PQ}=\overline{P^{\prime} Q^{\prime}}$이므로 $2 - 2 \cos ( \alpha + \beta ) = 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta.$

$$
 \therefore \cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta. \label{eqn:cos_1} \tag{5}
$$

위 식의 $\beta$에 $-\beta$를 대입하고 정리하면

$$
\cos ( \alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta \label{eqn:cos_2} \tag{6}
$$

$\cos ( \frac { \pi } { 2 } - \theta ) = \sin \theta ,\, \sin ( \frac { \pi } { 2 } - \theta ) = \cos \theta$이므로

$$
\begin{align*} \sin ( \alpha + \beta ) &= \cos ( \frac { \pi } { 2 } - ( \alpha + \beta ) ) = \cos ( ( \frac { \pi } { 2 } - \alpha ) - \beta) \\ &= \cos ( \frac { \pi } { 2 } - x ) \cos \beta + \sin ( \frac { \pi } { 2 } - \alpha ) \sin \beta \\ &= \sin \alpha \cos \beta + \cos \alpha \sin \beta. \end{align*}
$$

$$
\therefore \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta. \label{eqn:sin_1} \tag{7}
$$

이 식의 $\beta$에 $-\beta$를 대입하고 정리하면

$$
\sin ( \alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta. \label{eqn:sin_2} \tag{8}
$$

마지막으로,

$$
\tan ( \alpha + \beta ) = \frac { \sin ( \alpha + \beta ) } { \cos ( \alpha + \beta ) } = \frac { \sin \alpha \cos \beta + \cos \alpha \sin \beta } { \cos \alpha \cos \beta - \sin \alpha \sin \beta }
$$

에서 분모와 분자를 각각 $\cos{\alpha} \cos{\beta}$로 나누고 정리하면

$$
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_1} \tag{9}
$$

이고, 이 식의 $\beta$에 $-\beta$를 대입하고 정리하면

$$
\tan ( \alpha - \beta ) = \frac { \tan \alpha - \tan \beta } { 1 + \tan \alpha \tan \beta } \label{eqn:tan_2} \tag{10}
$$

이다.

## 기울기가 주어진 두 직선이 이루는 예각의 크기
![Angle formed by two lines](/assets/img/trigonometry/angle-formed-by-two-lines.png)
식 ($\ref{eqn:tan_2}$)을 이용하면 기울기가 주어진 두 직선이 이루는 예각의 크기를 구할 수 있다. 두 직선 $y=mx+b$, $y=m^{\prime} x+b^{\prime}$이 $x$축의 양의 방향과 이루는 각의 크기를 각각 $\theta_{1}$, $\theta_{2}$라 하면

$$
\tan{\theta_{1}}=m,\, \tan{\theta_{2}}=m^{\prime}
$$

이므로, 두 직선이 이루는 예각의 크기를 $\theta$라 하면

$$
\tag{11} \begin{align*}
\tan{\theta}&=\left\vert \tan{\theta_{2}-\theta_{1}} \right\vert=\left\vert \frac{\tan{\theta_2}-\tan{\theta_1}}{1+\tan{\theta_1}\tan{\theta_2}}\right\vert \\
&=\left\vert \frac{m-m^{\prime}}{1+mm^{\prime}} \right\vert.
\end{align*}
$$
