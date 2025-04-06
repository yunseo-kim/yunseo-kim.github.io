---
title: Equação de Euler-Cauchy
description: Examinamos como a solução geral da equação de Euler-Cauchy assume diferentes formas dependendo do sinal do discriminante da equação auxiliar.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Equação de Euler-Cauchy: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Equação auxiliar**: $m^2 + (a-1)m + b = 0$
> - A forma da solução geral pode ser dividida em três casos conforme o sinal do discriminante da equação auxiliar $(1-a)^2 - 4b$, como mostrado na tabela
>
> | Caso | Raízes da equação auxiliar | Base das soluções da equação de Euler-Cauchy | Solução geral da equação de Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Raízes reais distintas<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Raiz real dupla<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Raízes complexas conjugadas<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Pré-requisitos
- [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [Equações Diferenciais Ordinárias Lineares Homogêneas com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Fórmula de Euler

## Equação auxiliar
A **equação de Euler-Cauchy** é uma equação diferencial da forma

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

onde $a$ e $b$ são constantes e $y(x)$ é a função desconhecida. Substituindo

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

na equação ($\ref{eqn:euler_cauchy_eqn}$), obtemos

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

ou seja,

$$ [m(m-1) + am + b]x^m = 0 $$

Isso nos leva à equação auxiliar

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

A condição necessária e suficiente para que $y=x^m$ seja uma solução da equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) é que $m$ seja uma solução da equação auxiliar ($\ref{eqn:auxiliary_eqn}$).

Resolvendo a equação quadrática ($\ref{eqn:auxiliary_eqn}$), obtemos

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

e, portanto, as duas funções

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

são soluções da equação ($\ref{eqn:euler_cauchy_eqn}$).

Assim como nas [Equações Diferenciais Ordinárias Lineares Homogêneas com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), podemos dividir em três casos dependendo do sinal do discriminante $(1-a)^2 - 4b$ da equação auxiliar ($\ref{eqn:auxiliary_eqn}$):
- $(1-a)^2 - 4b > 0$: duas raízes reais distintas
- $(1-a)^2 - 4b = 0$: uma raiz real dupla
- $(1-a)^2 - 4b < 0$: raízes complexas conjugadas

## Forma da solução geral dependendo do sinal do discriminante da equação auxiliar
### I. Duas raízes reais distintas $m_1$ e $m_2$
Neste caso, a base de soluções da equação ($\ref{eqn:euler_cauchy_eqn}$) em qualquer intervalo é

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

e a solução geral correspondente é

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Raiz real dupla $m = \cfrac{1-a}{2}$
Quando $(1-a)^2 - 4b = 0$, ou seja, $b=\cfrac{(1-a)^2}{4}$, a equação quadrática ($\ref{eqn:auxiliary_eqn}$) tem apenas uma solução $m = m_1 = m_2 = \cfrac{1-a}{2}$, e portanto obtemos uma solução da forma $y = x^m$:

$$ y_1 = x^{(1-a)/2} $$

e a equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) toma a forma

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Agora, vamos encontrar uma segunda solução linearmente independente $y_2$ usando o [método de redução de ordem](/posts/homogeneous-linear-odes-of-second-order/#redução-de-ordem).

Definindo a segunda solução como $y_2=uy_1$, obtemos

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Como $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$, temos

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

Integrando, obtemos $u = \ln x$.

Portanto, $y_2 = uy_1 = y_1 \ln x$, e $y_1$ e $y_2$ são linearmente independentes, pois sua razão não é constante. A solução geral correspondente às bases $y_1$ e $y_2$ é

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Raízes complexas conjugadas
Neste caso, as soluções da equação auxiliar ($\ref{eqn:auxiliary_eqn}$) são $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, e as duas soluções complexas correspondentes da equação ($\ref{eqn:euler_cauchy_eqn}$) podem ser escritas usando $x=e^{\ln x}$ como:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Definindo $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ e usando a fórmula de Euler $e^{it} = \cos{t} + i\sin{t}$, temos

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

A partir disso, obtemos duas soluções reais:

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Como a razão $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ não é constante, essas duas soluções são linearmente independentes e, portanto, pelo [princípio da superposição](/posts/homogeneous-linear-odes-of-second-order/#princípio-da-superposição), formam uma base para a equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$). Isso nos dá a seguinte solução geral real:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

No entanto, o caso em que a equação auxiliar da equação de Euler-Cauchy tem raízes complexas conjugadas não tem grande importância prática.
