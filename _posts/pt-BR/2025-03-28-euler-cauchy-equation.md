---
title: "Equação de Euler-Cauchy"
description: "Examinamos a forma da solução geral da equação de Euler-Cauchy para cada caso, dependendo do sinal do discriminante da equação auxiliar."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Equação de Euler-Cauchy: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Equação auxiliar**: $m^2 + (a-1)m + b = 0$
> - A forma da solução geral pode ser dividida em três casos, conforme a tabela, dependendo do sinal do discriminante da equação auxiliar, $(1-a)^2 - 4b$.
>
> | Caso | Solução da Equação Auxiliar | Base da Solução da Equação de Euler-Cauchy | Solução Geral da Equação de Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Raízes reais distintas<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Raiz real dupla<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Raízes complexas conjugadas<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Pré-requisitos
- [EDOs Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs Lineares Homogêneas de Segunda Ordem com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Fórmula de Euler

## Equação Auxiliar
A **equação de Euler-Cauchy** é uma equação diferencial ordinária da forma

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

com constantes dadas $a$ e $b$, e uma função desconhecida $y(x)$. Na equação ($\ref{eqn:euler_cauchy_eqn}$), substituindo

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

obtemos

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

ou seja,

$$ [m(m-1) + am + b]x^m = 0 $$

A partir disso, obtemos a equação auxiliar

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

e a condição necessária e suficiente para que $y=x^m$ seja uma solução da equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) é que $m$ seja uma solução da equação auxiliar ($\ref{eqn:auxiliary_eqn}$).

Resolvendo a equação quadrática ($\ref{eqn:auxiliary_eqn}$), obtemos as soluções

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

e, a partir disso, as duas funções

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

são soluções da equação ($\ref{eqn:euler_cauchy_eqn}$).

Assim como no caso das [EDOs lineares homogêneas de segunda ordem com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), podemos dividir em três casos dependendo do sinal do discriminante da equação auxiliar ($\ref{eqn:auxiliary_eqn}$), $(1-a)^2 - 4b$.
- $(1-a)^2 - 4b > 0$: Duas raízes reais distintas
- $(1-a)^2 - 4b = 0$: Raiz real dupla
- $(1-a)^2 - 4b < 0$: Raízes complexas conjugadas

## Forma da Solução Geral de Acordo com o Sinal do Discriminante da Equação Auxiliar
### I. Duas Raízes Reais Distintas $m_1$ e $m_2$
Neste caso, a base de soluções da equação ($\ref{eqn:euler_cauchy_eqn}$) em qualquer intervalo é

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

e a solução geral correspondente é

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Raiz Real Dupla $m = \cfrac{1-a}{2}$
No caso em que $(1-a)^2 - 4b = 0$, ou seja, $b=\cfrac{(1-a)^2}{4}$, a equação quadrática ($\ref{eqn:auxiliary_eqn}$) tem apenas uma solução $m = m_1 = m_2 = \cfrac{1-a}{2}$. Portanto, a única solução da forma $y = x^m$ que podemos obter é

$$ y_1 = x^{(1-a)/2} $$

e a equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) assume a forma

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Agora, vamos encontrar outra solução linearmente independente, $y_2$, usando o método de [redução de ordem](/posts/homogeneous-linear-odes-of-second-order/#reducao-de-ordem).

Se definirmos a segunda solução que procuramos como $y_2=uy_1$, obtemos

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Como $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

e integrando, obtemos $u = \ln x$.

Portanto, $y_2 = uy_1 = y_1 \ln x$. Como a razão entre $y_1$ e $y_2$ não é uma constante, elas são linearmente independentes. A solução geral correspondente à base $y_1$ e $y_2$ é

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Raízes Complexas Conjugadas
Neste caso, as soluções da equação auxiliar ($\ref{eqn:auxiliary_eqn}$) são $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, e as duas soluções complexas correspondentes da equação ($\ref{eqn:euler_cauchy_eqn}$) podem ser escritas da seguinte forma, usando o fato de que $x=e^{\ln x}$.

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Definindo $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ e usando a fórmula de Euler $e^{it} = \cos{t} + i\sin{t}$, podemos ver que

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

e a partir disso, obtemos as duas seguintes soluções reais

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Como a razão entre elas, $\tan\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$, não é uma constante, as duas soluções acima são linearmente independentes e, portanto, formam uma base para a equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) pelo [princípio da superposição](/posts/homogeneous-linear-odes-of-second-order/#principio-da-superposicao). A partir disso, obtemos a seguinte solução geral real.

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

No entanto, o caso em que a equação auxiliar da equação de Euler-Cauchy tem raízes complexas conjugadas não é de grande importância prática.

## Transformação para uma EDO Linear Homogênea de Segunda Ordem com Coeficientes Constantes
A equação de Euler-Cauchy pode ser transformada em uma [EDO linear homogênea de segunda ordem com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) através de uma substituição de variável.

Fazendo a substituição $x = e^t$, temos

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

e a equação de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) se transforma na seguinte EDO linear homogênea com coeficientes constantes em termos de $t$.

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

Se resolvermos a equação ($\ref{eqn:substituted}$) para $t$ aplicando o método de solução para [EDOs lineares homogêneas de segunda ordem com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) e, em seguida, convertermos a solução obtida de volta para uma solução em termos de $x$ usando $t = \ln{x}$, obteremos [os mesmos resultados que vimos anteriormente](#forma-da-solucao-geral-de-acordo-com-o-sinal-do-discriminante-da-equacao-auxiliar).
