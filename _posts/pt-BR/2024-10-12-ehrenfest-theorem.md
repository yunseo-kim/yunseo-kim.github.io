---
title: Teorema de Ehrenfest
description: Aprenda como calcular os valores esperados de posição e momento a partir
  da função de onda na mecânica quântica, e estenda isso para uma fórmula de cálculo
  do valor esperado para qualquer variável mecânica Q(x,p). Em seguida, derive o teorema
  de Ehrenfest a partir disso.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Pré-requisitos
- Distribuição de probabilidade contínua e densidade de probabilidade
- [Equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/)

## Cálculo do valor esperado a partir da função de onda
### Valor esperado da posição $x$
O valor esperado (expectation value) da posição $x$ para uma partícula no estado $\Psi$ é

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

Se medirmos a posição de um número suficientemente grande de partículas no mesmo estado $\Psi$ e calcularmos a média dos resultados, obteremos $\langle x \rangle$ calculado pela equação acima.

> Note que o valor esperado mencionado aqui não é a média obtida por medições repetidas de uma única partícula, mas sim a média dos resultados de medição para um **ensemble** de sistemas no mesmo estado. Se a mesma partícula for medida repetidamente em intervalos curtos de tempo, a [função de onda colapsará (collapse)](/posts/schrodinger-equation-and-the-wave-function/#medição-e-colapso-da-função-de-onda) na primeira medição, e as medições subsequentes sempre darão o mesmo valor.
{: .prompt-warning }

### Valor esperado do momento $p$
Como $\Psi$ depende do tempo, $\langle x \rangle$ mudará com o tempo. Neste caso, pela [equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/) equação (8) e pela equação ($\ref{eqn:x_exp}$) acima, temos:

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> A integração por partes foi aplicada duas vezes no processo de ($\ref{eqn:dx/dt_1}$) para ($\ref{eqn:dx/dt_2}$) e de ($\ref{eqn:dx/dt_2}$) para ($\ref{eqn:dx/dt_3}$), e os termos de fronteira foram descartados porque $\lim_{x\rightarrow\pm\infty}\Psi=0$.
{: .prompt-tip }

Portanto, obtemos o valor esperado do **momento** como:

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Valor esperado para uma quantidade física arbitrária $Q(x,p)$
As expressões para $\langle x \rangle$ e $\langle p \rangle$ que obtivemos anteriormente podem ser escritas na seguinte forma:

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

O operador $\hat x \equiv x$ representa a posição, e o operador $\hat p \equiv -i\hbar(\partial/\partial x)$ representa o momento. No caso do operador de momento $\hat p$, quando estendido para o espaço tridimensional, pode ser definido como $\hat p \equiv -i\hbar\nabla$.

Como todas as variáveis da mecânica clássica podem ser expressas em termos de posição e momento, podemos estender isso para o valor esperado de qualquer quantidade física. Para calcular o valor esperado de uma quantidade arbitrária $Q(x,p)$, substituímos todos os $p$ por $-i\hbar\nabla$, inserimos o operador resultante entre $\Psi^\*$ e $\Psi$, e integramos.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Por exemplo, como a energia cinética é $T=\cfrac{p^2}{2m}$, temos

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

Através da equação ($\ref{eqn:Q_exp}$), podemos calcular o valor esperado de qualquer quantidade física para uma partícula no estado $\Psi$.

## Teorema de Ehrenfest
### Cálculo de $d\langle p \rangle/dt$
Vamos diferenciar ambos os lados da equação ($\ref{eqn:p_op}$) em relação ao tempo $t$ para obter a derivada temporal do valor esperado do momento $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Podemos obter a equação ($\ref{eqn:dp/dt_2}$) substituindo as equações (6) e (7) da [equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/) na equação ($\ref{eqn:dp/dt_1}$). No processo de ($\ref{eqn:dp/dt_3}$) para ($\ref{eqn:dp/dt_4}$), aplicamos a integração por partes e, como antes, descartamos os termos de fronteira porque $\lim_{x\rightarrow\pm\infty}\Psi=0$.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Relação entre o Teorema de Ehrenfest e a Segunda Lei de Newton do Movimento
As duas equações seguintes que obtivemos são chamadas de teorema de Ehrenfest:

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

O teorema de Ehrenfest tem uma forma muito semelhante à relação entre energia potencial e força conservativa na mecânica clássica, $F=\cfrac{dp}{dt}=-\nabla V$.  
Comparando as duas equações lado a lado:

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Teorema de Ehrenfest]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Segunda Lei de Newton do Movimento]}$$

Se expandirmos o lado direito da segunda equação do teorema de Ehrenfest $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (equação [$\ref{eqn:ehrenfest_theorem_2nd}$]) em uma série de Taylor em torno de $\langle x \rangle$, temos:

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

Se $x-\langle x \rangle$ for suficientemente pequeno, podemos ignorar todos os termos de ordem superior exceto o primeiro e aproximar:

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

Ou seja, **se a função de onda de uma partícula tiver uma distribuição espacial muito próxima a um ponto (se a dispersão de $\|\Psi\|^2$ em relação a $x$ for muito pequena), o teorema de Ehrenfest pode ser aproximado pela segunda lei de Newton da mecânica clássica.** Em escala macroscópica, podemos ignorar a extensão espacial da função de onda e considerar a posição da partícula essencialmente como um ponto, então a segunda lei de Newton do movimento se aplica. No entanto, em escala microscópica, os efeitos quânticos não podem ser ignorados, então a segunda lei de Newton do movimento não se aplica mais e devemos usar o teorema de Ehrenfest.
