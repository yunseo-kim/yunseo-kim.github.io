---
title: "Teoremas de Adição de Funções Trigonométricas"
description: >-
  Examinamos as definições de funções trigonométricas e as relações entre elas, e a partir disso derivamos os teoremas de adição de funções trigonométricas e fórmulas relacionadas.
categories: [Mathematics]
tags: [Trigonometry]
math: true
---

## Definição de Funções Trigonométricas
![Círculo Unitário e Vetor Raio](/assets/img/trigonometry/definition.png)
Como mostrado na figura, quando o tamanho do ângulo formado pelo raio vetor $\overline{OP}$ e a direção positiva do eixo $x$ é $\theta$,
$$
\begin{gather}\begin{split}
\sin \theta = \frac { y } { r } ,\; \cos \theta = \frac { x } { r } ,\; \tan \theta = \frac { y } { x } \\ \csc \theta = \frac { r } { y } ,\; \sec \theta = \frac { r } { x } ,\; \cot \theta = \frac { x } { y } \end{split}\end{gather}
$$
são definidas assim, e coletivamente chamadas de funções trigonométricas.

## Relações entre Funções Trigonométricas
1. $$ \csc \theta = \frac { 1 } { \sin \theta } ,\; \sec \theta = \frac { 1 } { \cos \theta } ,\; \cot \theta = \frac { 1 } { \tan \theta } \tag{2}$$
2. $$ \tan \theta = \frac { \sin \theta } { \cos \theta } ,\; \cot \theta = \frac { \cos \theta } { \sin \theta } \tag{3}$$
3. $$ \tag{4} \begin{gather*}
\sin ^ { 2 } \theta + \cos ^ { 2 } \theta = 1 \\
\tan ^ { 2 } \theta + 1 = \sec ^ { 2 } \theta \\
1 + \cot ^ { 2 } \theta = \csc ^ { 2 } \theta 
\end{gather*} 
$$

## Teoremas de Adição de Funções Trigonométricas
![Derivando as Fórmulas de Adição Trigonométrica](/assets/img/trigonometry/trigonometric-addition-formulas.png)
Como mostrado na figura, sejam $P, Q, P^{\prime}, Q^{\prime}$ os pontos onde quatro raios vetores que formam ângulos de $\alpha+\beta,\, 0,\, \alpha,\, -\beta$ com a direção positiva do eixo $x$ encontram o círculo unitário, respectivamente.

As coordenadas dos dois pontos $P, Q$ são

$$
P(\cos(\alpha+\beta), \sin(\alpha+\beta)),\; Q(1,0)
$$

portanto

$$
\begin{align*} \overline { P^ { \prime } Q^ { \prime } } ^2&= \{ \cos \alpha - \cos ( - \beta ) \} ^ { 2 } + \{ \sin \alpha - \sin ( - \beta ) \} ^ { 2 } \\
&= 2 - 2 \cos \alpha \cos ( - \beta ) - 2 \sin \alpha \sin ( - \beta ) \\
&= 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta. \end{align*}
$$

Como $\overline{PQ}=\overline{P^{\prime} Q^{\prime}}$, temos $2 - 2 \cos ( \alpha + \beta ) = 2 - 2 \cos \alpha \cos \beta + 2 \sin \alpha \sin \beta.$

$$
 \therefore \cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta. \label{eqn:cos_1} \tag{5}
$$

Substituindo $\beta$ por $-\beta$ na equação acima e reorganizando, obtemos

$$
\cos ( \alpha - \beta ) = \cos \alpha \cos \beta + \sin \alpha \sin \beta \label{eqn:cos_2} \tag{6}
$$

Como $\cos ( \frac { \pi } { 2 } - \theta ) = \sin \theta ,\, \sin ( \frac { \pi } { 2 } - \theta ) = \cos \theta$, temos

$$
\begin{align*} \sin ( \alpha + \beta ) &= \cos ( \frac { \pi } { 2 } - ( \alpha + \beta ) ) = \cos ( ( \frac { \pi } { 2 } - \alpha ) - \beta) \\ &= \cos ( \frac { \pi } { 2 } - x ) \cos \beta + \sin ( \frac { \pi } { 2 } - \alpha ) \sin \beta \\ &= \sin \alpha \cos \beta + \cos \alpha \sin \beta. \end{align*}
$$

$$
\therefore \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta. \label{eqn:sin_1} \tag{7}
$$

Substituindo $\beta$ por $-\beta$ nesta equação e reorganizando, obtemos

$$
\sin ( \alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta. \label{eqn:sin_2} \tag{8}
$$

Finalmente,

$$
\tan ( \alpha + \beta ) = \frac { \sin ( \alpha + \beta ) } { \cos ( \alpha + \beta ) } = \frac { \sin \alpha \cos \beta + \cos \alpha \sin \beta } { \cos \alpha \cos \beta - \sin \alpha \sin \beta }
$$

Dividindo o numerador e o denominador por $\cos{\alpha} \cos{\beta}$ e reorganizando, obtemos

$$
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_1} \tag{9}
$$

e substituindo $\beta$ por $-\beta$ nesta equação e reorganizando, obtemos

$$
\tan ( \alpha - \beta ) = \frac { \tan \alpha - \tan \beta } { 1 + \tan \alpha \tan \beta } \label{eqn:tan_2} \tag{10}
$$

## Tamanho do Ângulo Agudo Formado por Duas Retas com Inclinações Dadas
![Ângulo formado por duas retas](/assets/img/trigonometry/angle-formed-by-two-lines.png)
Usando a equação ($\ref{eqn:tan_2}$), podemos calcular o tamanho do ângulo agudo formado por duas retas com inclinações dadas. Se $\theta_{1}$ e $\theta_{2}$ são os tamanhos dos ângulos formados pelas duas retas $y=mx+b$ e $y=m^{\prime} x+b^{\prime}$ com a direção positiva do eixo $x$, respectivamente, então

$$
\tan{\theta_{1}}=m,\, \tan{\theta_{2}}=m^{\prime}
$$

Portanto, se $\theta$ é o tamanho do ângulo agudo formado pelas duas retas, temos

$$
\tag{11} \begin{align*}
\tan{\theta}&=\left\vert \tan{\theta_{2}-\theta_{1}} \right\vert=\left\vert \frac{\tan{\theta_2}-\tan{\theta_1}}{1+\tan{\theta_1}\tan{\theta_2}}\right\vert \\
&=\left\vert \frac{m-m^{\prime}}{1+mm^{\prime}} \right\vert.
\end{align*}
$$