---
title: Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem
description: Entenda a definição e características das equações diferenciais ordinárias lineares de segunda ordem, especialmente o princípio da superposição e o conceito de base que se aplicam às equações homogêneas.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Forma padrão** de uma EDO linear de segunda ordem: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coeficientes**: funções $p$, $q$
>   - **Entrada**: $r(x)$
>   - **Saída** ou **resposta**: $y(x)$
> - Homogênea e não-homogênea
>   - **Homogênea**: quando $r(x)\equiv0$ na forma padrão
>   - **Não-homogênea**: quando $r(x)\not\equiv 0$ na forma padrão
> - **Princípio da superposição**: Para uma EDO linear homogênea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, qualquer combinação linear de duas soluções em um intervalo aberto $I$ também é uma solução da equação dada. Ou seja, a soma e o produto por constante de quaisquer soluções da EDO linear homogênea dada também são soluções da mesma equação.
> - **Base** ou **sistema fundamental**: Um par de soluções $(y_1, y_2)$ linearmente independentes da EDO linear homogênea no intervalo $I$
> - **Redução de ordem**: Se uma solução de uma EDO homogênea de segunda ordem é conhecida, uma segunda solução linearmente independente, ou seja, uma base, pode ser encontrada resolvendo uma EDO de primeira ordem; este método é chamado de redução de ordem
> - Aplicações da redução de ordem: Uma EDO geral de segunda ordem $F(x, y, y^\prime, y^{\prime\prime})=0$, seja linear ou não-linear, pode ser reduzida a primeira ordem usando redução de ordem nos seguintes casos:
>   - Quando $y$ não aparece explicitamente
>   - Quando $x$ não aparece explicitamente
>   - Quando é linear homogênea e uma solução já é conhecida
{: .prompt-info }

## Pré-requisitos
- [Conceitos Básicos de Modelagem](/posts/Basic-Concepts-of-Modeling/)
- [Separação de Variáveis](/posts/Separation-of-Variables/)
- [Solução de EDOs Lineares de Primeira Ordem](/posts/Solution-of-First-Order-Linear-ODE/)

## Equações Diferenciais Ordinárias Lineares de Segunda Ordem
Uma equação diferencial de segunda ordem é chamada **linear** se pode ser escrita na forma

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

e **não-linear** caso contrário.

Quando $p$, $q$, e $r$ são funções de $x$, esta equação é linear em $y$ e suas derivadas.

A forma ($\ref{eqn:standard_form}$) é chamada de **forma padrão** de uma EDO linear de segunda ordem. Se o primeiro termo de uma EDO linear de segunda ordem dada for $f(x)y^{\prime\prime}$, podemos obter a forma padrão dividindo ambos os lados da equação por $f(x)$.

As funções $p$ e $q$ são chamadas de **coeficientes**, $r(x)$ é chamada de **entrada**, e $y(x)$ é chamada de **saída** ou **resposta** à entrada e às condições iniciais.

### EDO Linear Homogênea de Segunda Ordem
Seja $J$ o intervalo $a<x<b$ onde queremos resolver a equação ($\ref{eqn:standard_form}$). Se $r(x)\equiv 0$ no intervalo $J$ na equação ($\ref{eqn:standard_form}$), temos

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

e esta é chamada de **homogênea**.

## EDO Linear Não-Homogênea
Se $r(x)\not\equiv 0$ no intervalo $J$, a equação é chamada de **não-homogênea**.

## Princípio da Superposição

Uma função da forma

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ são constantes arbitrárias)}\tag{3}$$

é chamada de **combinação linear** de $y_1$ e $y_2$.

Neste caso, o seguinte princípio se aplica:

> **Princípio da Superposição**  
> Para uma EDO linear homogênea ($\ref{eqn:homogeneous_linear_ode}$), qualquer combinação linear de duas soluções em um intervalo aberto $I$ também é uma solução da equação ($\ref{eqn:homogeneous_linear_ode}$). Ou seja, a soma e o produto por constante de quaisquer soluções da EDO linear homogênea dada também são soluções da mesma equação.
{: .prompt-info }

### Prova
Sejam $y_1$ e $y_2$ soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$. Substituindo $y=c_1y_1+c_2y_2$ na equação ($\ref{eqn:homogeneous_linear_ode}$), temos

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

que é uma identidade. Portanto, $y$ é uma solução da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$. $\blacksquare$

> Note que o princípio da superposição se aplica apenas a EDOs lineares homogêneas e não se aplica a EDOs lineares não-homogêneas ou EDOs não-lineares.
{: .prompt-warning }

## Base e Solução Geral
### Revisão de Conceitos Principais de EDOs de Primeira Ordem
Como vimos anteriormente em [Conceitos Básicos de Modelagem](/posts/Basic-Concepts-of-Modeling/), um problema de valor inicial (PVI) para uma EDO de primeira ordem consiste na EDO e na condição inicial (CI) $y(x_0)=y_0$. A CI é necessária para determinar a constante arbitrária $c$ na solução geral da EDO dada, e a solução assim determinada é chamada de solução particular. Agora, vamos estender esses conceitos para EDOs de segunda ordem.

### Problema de Valor Inicial e Condições Iniciais
Um **problema de valor inicial** para a EDO linear homogênea de segunda ordem ($\ref{eqn:homogeneous_linear_ode}$) consiste na EDO dada ($\ref{eqn:homogeneous_linear_ode}$) e em duas **condições iniciais**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Estas condições são necessárias para determinar as duas constantes arbitrárias $c_1$ e $c_2$ na **solução geral**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Independência Linear e Dependência Linear
Vamos revisar brevemente os conceitos de independência linear e dependência linear. Isso é necessário para definir a base mais adiante.  
Duas funções $y_1$ e $y_2$ são ditas **linearmente independentes** em um intervalo $I$ se, para todos os pontos nesse intervalo,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ e }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

Caso contrário, $y_1$ e $y_2$ são ditas **linearmente dependentes**.

Se $y_1$ e $y_2$ são linearmente dependentes (ou seja, se a proposição ($\ref{eqn:linearly_independent}$) não é verdadeira), podemos dividir ambos os lados da equação em ($\ref{eqn:linearly_independent}$) por $k_1 \neq 0$ ou $k_2 \neq 0$, obtendo

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{ou} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

o que mostra que $y_1$ e $y_2$ são proporcionais.

### Base, Solução Geral e Solução Particular
Voltando ao nosso tema, para que ($\ref{eqn:general_sol}$) seja a solução geral, $y_1$ e $y_2$ devem ser soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) e, ao mesmo tempo, devem ser linearmente independentes (não proporcionais) no intervalo $I$. Um par $(y_1, y_2)$ de soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) que satisfaz essas condições e é linearmente independente no intervalo $I$ é chamado de **base** ou **sistema fundamental** de soluções da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$.

Ao usar as condições iniciais para determinar as duas constantes $c_1$ e $c_2$ na solução geral ($\ref{eqn:general_sol}$), obtemos uma única solução que passa pelo ponto $(x_0, K_0)$ e tem inclinação $K_1$ nesse ponto. Esta é chamada de **solução particular** da EDO ($\ref{eqn:homogeneous_linear_ode}$).

Se a equação ($\ref{eqn:homogeneous_linear_ode}$) é contínua em um intervalo aberto $I$, ela sempre tem uma solução geral, e esta solução geral inclui todas as soluções particulares possíveis. Ou seja, neste caso, a equação ($\ref{eqn:homogeneous_linear_ode}$) não tem soluções singulares que não possam ser obtidas da solução geral.

## Redução de Ordem
Se uma solução de uma EDO homogênea de segunda ordem é conhecida, uma segunda solução linearmente independente, ou seja, uma base, pode ser encontrada resolvendo uma EDO de primeira ordem da seguinte maneira. Este método é chamado de **redução de ordem**.

Considere uma EDO linear homogênea de segunda ordem na forma padrão (ou seja, com $y^{\prime\prime}$ em vez de $f(x)y^{\prime\prime}$):

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

Suponha que conhecemos uma solução $y_1$ desta equação em um intervalo aberto $I$.

Agora, vamos procurar uma segunda solução na forma $y_2 = uy_1$, e substituir

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

na equação, obtendo

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Agrupando os termos com $u^{\prime\prime}$, $u^{\prime}$, e $u$, temos

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Como $y_1$ é uma solução da equação dada, a expressão entre parênteses no último termo é zero, então o termo com $u$ desaparece, deixando uma EDO em $u^{\prime}$ e $u^{\prime\prime}$. Dividindo ambos os lados desta EDO restante por $y_1$ e fazendo $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, obtemos a seguinte EDO de primeira ordem:

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Separando as variáveis e integrando, temos

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

e aplicando a função exponencial em ambos os lados, obtemos finalmente

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Como definimos $U=u^{\prime}$, temos $u=\int U dx$, então a segunda solução $y_2$ que estamos procurando é

$$ y_2 = uy_1 = y_1 \int U dx $$

Como $\cfrac{y_2}{y_1} = u = \int U dx$ não pode ser constante desde que $U>0$, $y_1$ e $y_2$ formam uma base de soluções.

### Aplicações da Redução de Ordem
Uma EDO geral de segunda ordem $F(x, y, y^\prime, y^{\prime\prime})=0$, seja linear ou não-linear, pode ser reduzida a primeira ordem usando redução de ordem quando $y$ não aparece explicitamente, quando $x$ não aparece explicitamente, ou quando é linear homogênea e uma solução já é conhecida, como vimos anteriormente.

#### Quando $y$ não aparece explicitamente
Em $F(x, y^\prime, y^{\prime\prime})=0$, fazendo $z=y^{\prime}$, podemos reduzir a uma EDO de primeira ordem em $z$: $F(x, z, z^{\prime})$.

#### Quando $x$ não aparece explicitamente
Em $F(y, y^\prime, y^{\prime\prime})=0$, fazendo $z=y^{\prime}$, temos $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$, então podemos reduzir a uma EDO de primeira ordem em $z$ com $y$ desempenhando o papel de variável independente no lugar de $x$: $F(y,z,z^\prime)$.
