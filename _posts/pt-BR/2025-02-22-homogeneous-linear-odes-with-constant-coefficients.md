---
title: Equação diferencial ordinária linear homogênea de segunda ordem com coeficientes constantes
description: Examinamos a forma da solução geral da equação diferencial ordinária linear homogênea com coeficientes constantes para cada caso, dependendo do sinal do discriminante da equação característica.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Equação diferencial ordinária linear homogênea de segunda ordem com coeficientes constantes: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Equação característica**: $\lambda^2 + a\lambda + b = 0$
> - A forma da solução geral pode ser dividida em três casos, conforme a tabela, dependendo do sinal do discriminante $a^2 - 4b$ da equação característica
>
> | Caso | Raízes da equação característica | Base das soluções da EDO | Solução geral da EDO |
> | :---: | :---: | :---: | :---: |
> | I | Raízes reais distintas<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Raiz real dupla<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Raízes complexas conjugadas<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$ <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Pré-requisitos
- [Equação de Bernoulli](/posts/Bernoulli-Equation/)
- [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- Fórmula de Euler

## Equação característica
Vamos examinar a equação diferencial ordinária linear homogênea de segunda ordem com coeficientes constantes $a$ e $b$

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Esse tipo de equação tem aplicações importantes em vibrações mecânicas e elétricas.

Anteriormente, na [Equação de Bernoulli](/posts/Bernoulli-Equation/), encontramos a solução geral para a equação logística, e de acordo com isso, a solução para uma equação diferencial ordinária linear de primeira ordem com coeficiente constante $k$

$$ y^\prime + ky = 0 $$

é a função exponencial $y = ce^{-kx}$. (No caso onde $A=-k$, $B=0$ na equação (4) daquele post)

Portanto, para uma equação de forma similar ($\ref{eqn:ode_with_constant_coefficients}$), podemos tentar primeiro uma solução da forma

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Claro, isso é apenas uma suposição, e não há garantia alguma de que a solução geral realmente terá essa forma. No entanto, se conseguirmos encontrar duas soluções linearmente independentes, seja qual for a forma, poderemos obter a solução geral pelo [princípio da superposição](/posts/homogeneous-linear-odes-of-second-order/#princípio-da-superposição), como vimos em [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/#base-e-solução-geral).  
> Como veremos em breve, há [casos em que precisamos encontrar soluções de outras formas](#ii-raiz-real-dupla-lambda---cfraca2).
{: .prompt-info }

Substituindo a equação ($\ref{eqn:general_sol}$) e suas derivadas

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

na equação ($\ref{eqn:ode_with_constant_coefficients}$), obtemos

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Portanto, se $\lambda$ for uma solução da **equação característica**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

então a função exponencial ($\ref{eqn:general_sol}$) é uma solução da equação diferencial ($\ref{eqn:ode_with_constant_coefficients}$). Resolvendo a equação quadrática ($\ref{eqn:characteristic_eqn}$), obtemos

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a + \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

e a partir disso, as duas funções

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

são soluções da equação ($\ref{eqn:ode_with_constant_coefficients}$).

Agora, podemos dividir em três casos dependendo do sinal do discriminante $a^2 - 4b$ da equação característica ($\ref{eqn:characteristic_eqn}$):
- $a^2 - 4b > 0$: Duas raízes reais distintas
- $a^2 - 4b = 0$: Uma raiz real dupla
- $a^2 - 4b < 0$: Raízes complexas conjugadas

## Forma da solução geral dependendo do sinal do discriminante da equação característica
### I. Duas raízes reais distintas $\lambda_1$ e $\lambda_2$
Neste caso, a base das soluções da equação ($\ref{eqn:ode_with_constant_coefficients}$) em qualquer intervalo é

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

e a solução geral correspondente é

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Raiz real dupla $\lambda = -\cfrac{a}{2}$
Quando $a^2 - 4b = 0$, a equação quadrática ($\ref{eqn:characteristic_eqn}$) tem apenas uma solução $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, e portanto, a única solução da forma $y = e^{\lambda x}$ que podemos obter é

$$ y_1 = e^{-(a/2)x} $$

Para obter uma base, precisamos encontrar uma segunda solução $y_2$ independente de $y_1$ e de forma diferente.

Nessa situação, podemos usar a [redução de ordem](/posts/homogeneous-linear-odes-of-second-order/#redução-de-ordem) que vimos anteriormente. Definimos a segunda solução que estamos procurando como $y_2=uy_1$, e

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Substituindo na equação ($\ref{eqn:ode_with_constant_coefficients}$), obtemos

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Agrupando os termos com $u^{\prime\prime}$, $u^\prime$, e $u$, temos

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Aqui, como $y_1$ é uma solução da equação ($\ref{eqn:ode_with_constant_coefficients}$), a expressão dentro do último parênteses é 0, e

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

então a expressão dentro do primeiro parênteses também é 0. Portanto, resta apenas $u^{\prime\prime}y_1 = 0$, do qual obtemos $u^{\prime\prime}=0$. Integrando duas vezes, temos $u = c_1x + c_2$, e como as constantes de integração $c_1$ e $c_2$ podem ser quaisquer valores, podemos simplesmente escolher $c_1=1$ e $c_2=0$, resultando em $u=x$. Então $y_2 = uy_1 = xy_1$, e como $y_1$ e $y_2$ são linearmente independentes, eles formam uma base. Portanto, quando a equação característica ($\ref{eqn:characteristic_eqn}$) tem uma raiz dupla, a base das soluções da equação ($\ref{eqn:ode_with_constant_coefficients}$) em qualquer intervalo é

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

e a solução geral correspondente é

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Raízes complexas conjugadas $-\cfrac{1}{2}a + i\omega$ e $-\cfrac{1}{2}a - i\omega$
Neste caso, $a^2 - 4b < 0$ e $\sqrt{-1} = i$, então da equação ($\ref{eqn:lambdas}$) temos

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

onde definimos o número real $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Com $\omega$ definido dessa forma, as soluções da equação característica ($\ref{eqn:characteristic_eqn}$) são as raízes complexas conjugadas $\lambda = -\cfrac{1}{2}a \pm i\omega$, e as duas soluções complexas correspondentes da equação ($\ref{eqn:ode_with_constant_coefficients}$) são

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

No entanto, mesmo neste caso, podemos obter uma base de soluções reais da seguinte maneira.

A fórmula de Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

e a equação obtida substituindo $t$ por $-t$ na equação acima

$$ e^{-it} = \cos t - i\sin t $$

podem ser somadas e subtraídas para obter:

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

A função exponencial complexa $e^z$ de uma variável complexa $z = r + it$ com parte real $r$ e parte imaginária $it$ pode ser definida usando as funções reais $e^r$, $\cos t$ e $\sin t$ da seguinte forma:

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + \sin t) \label{eqn:complex_exp}\tag{10}$$

Se fizermos $r=-\cfrac{1}{2}ax$ e $t=\omega x$, podemos escrever:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Pelo [princípio da superposição](/posts/homogeneous-linear-odes-of-second-order/#princípio-da-superposição), a soma e o produto por constante dessas soluções complexas também são soluções. Portanto, somando as duas equações e multiplicando ambos os lados por $\cfrac{1}{2}$, obtemos a primeira solução real $y_1$:

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Da mesma forma, subtraindo a segunda equação da primeira e multiplicando ambos os lados por $\cfrac{1}{2i}$, obtemos a segunda solução real $y_2$:

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Como $\cfrac{y_1}{y_2} = \cot{\omega x}$ não é constante, $y_1$ e $y_2$ são linearmente independentes em todos os intervalos e, portanto, formam uma base para as soluções reais da equação ($\ref{eqn:ode_with_constant_coefficients}$). A partir disso, obtemos a solução geral

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ são constantes arbitrárias)} \label{eqn:general_sol_3}\tag{13}$$
