---
title: 三角函數的加法定理
description: 探討三角函數的定義和三角函數之間的關係式，並由此推導出三角函數的加法定理及相關公式。
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 三角函數的定義
![單位圓和半徑向量](/assets/img/trigonometry/definition.png)
如圖所示，當半徑向量 $\overline{OP}$ 與 $x$ 軸正方向形成的角度大小為 $\theta$ 時，
$$
\begin{gather}\begin{split}
\sin \theta = \frac { y } { r } ,\; \cos \theta = \frac { x } { r } ,\; \tan \theta = \frac { y } { x } \\ \csc \theta = \frac { r } { y } ,\; \sec \theta = \frac { r } { x } ,\; \cot \theta = \frac { x } { y } \end{split}\end{gather}
$$
這些定義統稱為三角函數。

## 三角函數之間的關係
1. $$ \csc \theta = \frac { 1 } { \sin \theta } ,\; \sec \theta = \frac { 1 } { \cos \theta } ,\; \cot \theta = \frac { 1 } { \tan \theta } \tag{2}$$
2. $$ \tan \theta = \frac { \sin \theta } { \cos \theta } ,\; \cot \theta = \frac { \cos \theta } { \sin \theta } \tag{3}$$
3. $$ \tag{4} \begin{gather*}
\sin ^ { 2 } \theta + \cos ^ { 2 } \theta = 1 \\
\tan ^ { 2 } \theta + 1 = \sec ^ { 2 } \theta \\
1 + \cot ^ { 2 } \theta = \csc ^ { 2 } \theta 
\end{gather*} 
$$

## 三角函數的加法定理
![推導三角函數加法定理](/assets/img/trigonometry/trigonometric-addition-formulas.png)
如圖所示，設與 $x$ 軸正方向形成角度大小為 $\alpha+\beta,\, 0,\, \alpha,\, -\beta$ 的四個半徑向量與單位圓相交的點分別為 $P, Q, P^{\prime}, Q^{\prime}$。

兩點 $P, Q$ 的坐標為

$$
P(\cos(\alpha+\beta), \sin(\alpha+\beta)),\; Q(1,0)
$$

因此

$$
\begin{align*} \overline { P^ { \prime } Q^ { \prime } } ^2&= \{ \cos \alpha - \cos ( - \beta ) \} ^ { 2 } + \{ \sin \alpha - \sin ( - \beta ) \} ^ { 2 } \\
&= 2 - 2 \cos \alpha \cos ( - \beta ) - 2 \sin \alpha \sin ( - \beta ) \\
&= 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta. \end{align*}
$$

由於 $\overline{PQ}=\overline{P^{\prime} Q^{\prime}}$，所以 $2 - 2 \cos ( \alpha + \beta ) = 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta.$

$$
 \therefore \cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta. \label{eqn:cos_1} \tag{5}
$$

將上式中的 $\beta$ 替換為 $-\beta$ 並整理，得到

$$
\cos ( \alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta \label{eqn:cos_2} \tag{6}
$$

由於 $\cos ( \frac { \pi } { 2 } - \theta ) = \sin \theta ,\, \sin ( \frac { \pi } { 2 } - \theta ) = \cos \theta$，所以

$$
\begin{align*} \sin ( \alpha + \beta ) &= \cos ( \frac { \pi } { 2 } - ( \alpha + \beta ) ) = \cos ( ( \frac { \pi } { 2 } - \alpha ) - \beta) \\ &= \cos ( \frac { \pi } { 2 } - x ) \cos \beta + \sin ( \frac { \pi } { 2 } - \alpha ) \sin \beta \\ &= \sin \alpha \cos \beta + \cos \alpha \sin \beta. \end{align*}
$$

$$
\therefore \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta. \label{eqn:sin_1} \tag{7}
$$

將此式中的 $\beta$ 替換為 $-\beta$ 並整理，得到

$$
\sin ( \alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta. \label{eqn:sin_2} \tag{8}
$$

最後，

$$
\tan ( \alpha + \beta ) = \frac { \sin ( \alpha + \beta ) } { \cos ( \alpha + \beta ) } = \frac { \sin \alpha \cos \beta + \cos \alpha \sin \beta } { \cos \alpha \cos \beta - \sin \alpha \sin \beta }
$$

將分子和分母分別除以 $\cos{\alpha} \cos{\beta}$ 並整理，得到

$$
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_1} \tag{9}
$$

將此式中的 $\beta$ 替換為 $-\beta$ 並整理，得到

$$
\tan ( \alpha - \beta ) = \frac { \tan \alpha - \tan \beta } { 1 + \tan \alpha \tan \beta } \label{eqn:tan_2} \tag{10}
$$

## 已知斜率的兩直線所形成的銳角大小
![兩直線形成的角度](/assets/img/trigonometry/angle-formed-by-two-lines.png)
利用式 ($\ref{eqn:tan_2}$)，我們可以計算已知斜率的兩直線所形成的銳角大小。設兩直線 $y=mx+b$、$y=m^{\prime} x+b^{\prime}$ 與 $x$ 軸正方向形成的角度大小分別為 $\theta_{1}$、$\theta_{2}$，則

$$
\tan{\theta_{1}}=m,\, \tan{\theta_{2}}=m^{\prime}
$$

因此，若兩直線形成的銳角大小為 $\theta$，則

$$
\tag{11} \begin{align*}
\tan{\theta}&=\left\vert \tan{\theta_{2}-\theta_{1}} \right\vert=\left\vert \frac{\tan{\theta_2}-\tan{\theta_1}}{1+\tan{\theta_1}\tan{\theta_2}}\right\vert \\
&=\left\vert \frac{m-m^{\prime}}{1+mm^{\prime}} \right\vert.
\end{align*}
$$
