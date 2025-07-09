---
title: "EDOs Lineares Homogêneas de Segunda Ordem"
description: "Aprenda a definição e as características das EDOs lineares de segunda ordem. Entenda o princípio da superposição, um teorema fundamental para EDOs lineares homogêneas, e o conceito de base associado."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Forma Padrão** da EDO linear de segunda ordem: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coeficientes**: funções $p$, $q$
>   - **Entrada (input)**: $r(x)$
>   - **Saída (output)** ou **Resposta (response)**: $y(x)$
> - Homogênea e Não Homogênea
>   - **Homogênea**: caso em que $r(x)\equiv0$ na forma padrão.
>   - **Não Homogênea**: caso em que $r(x)\not\equiv 0$ na forma padrão.
> - **Princípio da Superposição**: Para uma EDO linear <u>homogênea</u> $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, qualquer combinação linear de duas soluções em um intervalo aberto $I$ também é uma solução da equação. Ou seja, a soma e o produto por constante de quaisquer soluções da EDO linear homogênea dada também são soluções.
> - **Base** ou **Sistema Fundamental**: Um par de soluções $(y_1, y_2)$ linearmente independentes da EDO linear homogênea no intervalo $I$.
> - **Redução de Ordem**: Se uma solução de uma EDO homogênea de segunda ordem for conhecida, uma segunda solução linearmente independente (formando uma base) pode ser encontrada resolvendo uma EDO de primeira ordem. Este método é chamado de redução de ordem.
> - Aplicações da Redução de Ordem: Uma EDO geral de segunda ordem $F(x, y, y^\prime, y^{\prime\prime})=0$, seja linear ou não, pode ser reduzida para primeira ordem usando redução de ordem nos seguintes casos:
>   - Quando $y$ não aparece explicitamente.
>   - Quando $x$ não aparece explicitamente.
>   - Quando a equação é linear homogênea e uma solução já é conhecida.
{: .prompt-info }

## Pré-requisitos
- [Conceitos Básicos de Modelagem](/posts/Basic-Concepts-of-Modeling/)
- [Separação de Variáveis](/posts/Separation-of-Variables/)
- [Solução de EDOs Lineares de Primeira Ordem](/posts/Solution-of-First-Order-Linear-ODE/)

## EDOs Lineares de Segunda Ordem
Uma equação diferencial ordinária (EDO) de segunda ordem é dita **linear** se puder ser escrita na forma

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

caso contrário, é dita **não linear**.

Quando $p$, $q$ e $r$ são funções de uma variável $x$ arbitrária, esta equação é linear em relação a $y$ e suas derivadas.

A forma da equação ($\ref{eqn:standard_form}$) é chamada de **forma padrão** de uma EDO linear de segunda ordem. Se o primeiro termo de uma EDO linear de segunda ordem dada for $f(x)y^{\prime\prime}$, podemos obter a forma padrão dividindo ambos os lados da equação por $f(x)$.

As funções $p$ e $q$ são chamadas de **coeficientes**, $r(x)$ é a **entrada (input)**, e $y(x)$ é a **saída (output)** ou a **resposta (response)** à entrada e às condições iniciais.

### EDOs Lineares Homogêneas de Segunda Ordem
Seja $J$ um intervalo $a<x<b$ no qual queremos resolver a equação ($\ref{eqn:standard_form}$). Se $r(x)\equiv 0$ no intervalo $J$, a equação ($\ref{eqn:standard_form}$) se torna

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

e é chamada de **homogênea**.

## EDOs Lineares Não Homogêneas
Se $r(x)\not\equiv 0$ no intervalo $J$, a equação é chamada de **não homogênea**.

## Princípio da Superposição

Uma função da forma

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ são constantes arbitrárias)}\tag{3}$$

é chamada de **combinação linear** de $y_1$ e $y_2$.

O seguinte princípio se aplica.

> **Princípio da Superposição**  
> Para a equação diferencial ordinária linear homogênea ($\ref{eqn:homogeneous_linear_ode}$), qualquer combinação linear de duas soluções em um intervalo aberto $I$ também é uma solução da equação ($\ref{eqn:homogeneous_linear_ode}$). Em outras palavras, a soma e o produto por constante de quaisquer soluções da EDO linear homogênea dada também são soluções dessa equação.
{: .prompt-info }

### Demonstração
Sejam $y_1$ e $y_2$ soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$. Substituindo $y=c_1y_1+c_2y_2$ na equação ($\ref{eqn:homogeneous_linear_ode}$), temos

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

o que se torna uma identidade. Portanto, $y$ é uma solução da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$. $\blacksquare$

> Note que o princípio da superposição se aplica apenas a EDOs lineares homogêneas e não é válido para EDOs lineares não homogêneas ou EDOs não lineares.
{: .prompt-warning }

## Base e Solução Geral
### Revisão dos Conceitos Principais de EDOs de Primeira Ordem
Como vimos anteriormente em [Conceitos Básicos de Modelagem](/posts/Basic-Concepts-of-Modeling/), um Problema de Valor Inicial (PVI) para uma EDO de primeira ordem consiste na EDO e uma condição inicial $y(x_0)=y_0$. A condição inicial é necessária para determinar a constante arbitrária $c$ na solução geral da EDO, e a solução assim determinada é chamada de solução particular. Agora, vamos estender esses conceitos para EDOs de segunda ordem.

### Problema de Valor Inicial e Condições Iniciais
Um **problema de valor inicial** para a EDO homogênea de segunda ordem ($\ref{eqn:homogeneous_linear_ode}$) consiste na EDO ($\ref{eqn:homogeneous_linear_ode}$) e duas **condições iniciais**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Essas condições são necessárias para determinar as duas constantes arbitrárias $c_1$ e $c_2$ na **solução geral**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

da equação.

### Independência e Dependência Linear
Vamos revisar brevemente os conceitos de independência e dependência linear. Isso é necessário para definir uma base mais adiante.  
Duas funções $y_1$ e $y_2$ são ditas **linearmente independentes** em um intervalo $I$ onde estão definidas se, para todos os pontos em $I$,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ e }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

Caso contrário, $y_1$ e $y_2$ são ditas **linearmente dependentes**.

Se $y_1$ e $y_2$ são linearmente dependentes (ou seja, a proposição ($\ref{eqn:linearly_independent}$) não é verdadeira), então $k_1 \neq 0$ ou $k_2 \neq 0$. Podemos dividir a equação em ($\ref{eqn:linearly_independent}$) para obter

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{ou} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

o que mostra que $y_1$ e $y_2$ são proporcionais.

### Base, Solução Geral e Solução Particular
Voltando, para que a equação ($\ref{eqn:general_sol}$) seja a solução geral, $y_1$ e $y_2$ devem ser soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) e, ao mesmo tempo, não serem proporcionais e serem linearmente independentes no intervalo $I$. Um par de soluções $(y_1, y_2)$ da equação ($\ref{eqn:homogeneous_linear_ode}$) que satisfaz essas condições, sendo linearmente independente no intervalo $I$, é chamado de **base** ou **sistema fundamental** de soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$.

Usando as condições iniciais para determinar as duas constantes $c_1$ e $c_2$ na solução geral ($\ref{eqn:general_sol}$), obtemos uma solução única que passa pelo ponto $(x_0, K_0)$ e tem uma inclinação da tangente de $K_1$ nesse ponto. Isso é chamado de **solução particular** da EDO ($\ref{eqn:homogeneous_linear_ode}$).

Se a equação ($\ref{eqn:homogeneous_linear_ode}$) for contínua em um intervalo aberto $I$, ela certamente terá uma solução geral, e essa solução geral incluirá todas as soluções particulares possíveis. Ou seja, neste caso, a equação ($\ref{eqn:homogeneous_linear_ode}$) não possui soluções singulares que não possam ser obtidas a partir da solução geral.

## Redução de Ordem
Se uma solução de uma EDO homogênea de segunda ordem for conhecida, uma segunda solução linearmente independente, ou seja, uma base, pode ser encontrada resolvendo uma EDO de primeira ordem, como se segue. Este método é chamado de **redução de ordem**.

Para uma EDO homogênea de segunda ordem <u>na forma padrão, que tem $y^{\prime\prime}$ em vez de $f(x)y^{\prime\prime}$</u>

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

suponha que conhecemos uma solução $y_1$ desta equação em um intervalo aberto $I$.

Agora, vamos procurar a segunda solução na forma $y_2 = uy_1$ e definir

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Substituindo na equação, obtemos

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Agrupando os termos por $u^{\prime\prime}$, $u^{\prime}$ e $u$, temos

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Como $y_1$ é uma solução da equação dada, a expressão no último parêntese é zero. Assim, o termo com $u$ desaparece, restando uma EDO para $u^{\prime}$ e $u^{\prime\prime}$. Dividindo a equação restante por $y_1$ e fazendo $u^{\prime}=U$ e $u^{\prime\prime}=U^{\prime}$, obtemos a seguinte EDO de primeira ordem.

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[Separando as variáveis](/posts/Separation-of-Variables/) e integrando,

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

e, aplicando a função exponencial em ambos os lados, obtemos finalmente

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Como definimos $U=u^{\prime}$, temos $u=\int U dx$. Portanto, a segunda solução $y_2$ que procuramos é

$$ y_2 = uy_1 = y_1 \int U dx $$

Como $\cfrac{y_2}{y_1} = u = \int U dx$ não pode ser uma constante (desde que $U>0$), $y_1$ e $y_2$ formam uma base de soluções.

### Aplicações da Redução de Ordem
Uma EDO geral de segunda ordem $F(x, y, y^\prime, y^{\prime\prime})=0$, seja linear ou não, pode ser reduzida para primeira ordem usando redução de ordem quando $y$ não aparece explicitamente, quando $x$ não aparece explicitamente, ou, como vimos, quando a equação é linear homogênea e uma solução já é conhecida.

#### Caso em que $y$ não aparece explicitamente
Em $F(x, y^\prime, y^{\prime\prime})=0$, fazendo $z=y^{\prime}$, podemos reduzir a equação para uma EDO de primeira ordem em $z$, $F(x, z, z^{\prime})$.

#### Caso em que $x$ não aparece explicitamente
Em $F(y, y^\prime, y^{\prime\prime})=0$, fazendo $z=y^{\prime}$, temos $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$. Assim, podemos reduzir a equação para uma EDO de primeira ordem em $z$, $F(y,z,z^\prime)$, onde $y$ atua como a variável independente no lugar de $x$.
