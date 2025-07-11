---
title: "EDOs Lineares Não-Homogêneas de Segunda Ordem"
description: "Entenda a solução geral de EDOs lineares não-homogêneas de segunda ordem, a relação entre soluções homogêneas e não-homogêneas, e a existência e unicidade de soluções."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - A **solução geral** de uma EDO linear não-homogênea de segunda ordem $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: solução geral da EDO homogênea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, onde $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: solução particular da EDO não-homogênea
> - O termo de resposta $y_p$ é determinado apenas pela entrada $r(x)$, e não muda mesmo que as condições iniciais sejam alteradas para a mesma EDO não-homogênea. A diferença entre duas soluções particulares de uma EDO não-homogênea é uma solução da EDO homogênea correspondente.
> - **Existência da solução geral**: Se os coeficientes $p(x)$, $q(x)$ e a função de entrada $r(x)$ são contínuos, a solução geral sempre existe
> - **Inexistência de soluções singulares**: A solução geral inclui todas as soluções possíveis (ou seja, não existem soluções singulares)
{: .prompt-info }

## Pré-requisitos
- [EDOs Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskiano, Existência e Unicidade de Soluções](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solução Geral e Solução Particular de EDOs Lineares Não-Homogêneas de Segunda Ordem
Consideremos a EDO linear não-homogênea de segunda ordem

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

onde $r(x) \not\equiv 0$. A **solução geral** da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) em um intervalo aberto $I$ é a soma da solução geral $y_h = c_1y_1 + c_2y_2$ da EDO homogênea correspondente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

e uma solução particular $y_p$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$):

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Uma **solução particular** da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$ é obtida atribuindo valores específicos às constantes arbitrárias $c_1$ e $c_2$ em $y_h$.

Em outras palavras, quando adicionamos uma entrada $r(x)$ que depende apenas da variável independente $x$ à EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$), um termo de resposta correspondente $y_p$ é adicionado à solução, e este termo adicional $y_p$ é determinado apenas pela entrada $r(x)$, independentemente das condições iniciais. Como veremos adiante, se calcularmos a diferença entre duas soluções particulares $y_1$ e $y_2$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) (ou seja, a diferença entre soluções para diferentes condições iniciais), o termo $y_p$ independente das condições iniciais é eliminado, restando apenas a diferença entre ${y_h}_1$ e ${y_h}_2$, que pelo [princípio da superposição](/posts/homogeneous-linear-odes-of-second-order/#princípio-da-superposição) é uma solução da equação ($\ref{eqn:homogeneous_linear_ode}$).

## Relação entre Soluções de EDOs Não-Homogêneas e suas EDOs Homogêneas Correspondentes
> **Teorema 1: Relação entre soluções de EDOs não-homogêneas e suas EDOs homogêneas correspondentes**  
> **(a)** Em um intervalo aberto $I$, a soma de uma solução $y$ da EDO não-homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) e uma solução $\tilde{y}$ da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) é uma solução da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$. Em particular, a expressão ($\ref{eqn:general_sol}$) é uma solução da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$.  
> **(b)** A diferença entre duas soluções da EDO não-homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$ é uma solução da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$.
{: .prompt-info }

### Demonstração
#### (a)
Denotemos o lado esquerdo das equações ($\ref{eqn:nonhomogeneous_linear_ode}$) e ($\ref{eqn:homogeneous_linear_ode}$) como $L[y]$. Então, para qualquer solução $y$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) e qualquer solução $\tilde{y}$ da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$, temos:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Para quaisquer duas soluções $y$ e $y^\*$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$, temos:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## A Solução Geral Inclui Todas as Soluções
Sabemos que para EDOs homogêneas ($\ref{eqn:homogeneous_linear_ode}$), a [solução geral inclui todas as soluções possíveis](/posts/wronskian-existence-and-uniqueness-of-solutions/#a-solução-geral-inclui-todas-as-soluções). Vamos mostrar que o mesmo é válido para EDOs não-homogêneas ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Teorema 2: A solução geral de uma EDO não-homogênea inclui todas as soluções**  
> Se os coeficientes $p(x)$, $q(x)$ e a função de entrada $r(x)$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) são contínuos em um intervalo aberto $I$, então todas as soluções da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$ podem ser obtidas da solução geral ($\ref{eqn:general_sol}$) atribuindo valores apropriados às constantes arbitrárias $c_1$ e $c_2$ em $y_h$.
{: .prompt-info }

### Demonstração
Seja $y^\*$ uma solução qualquer da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$, e seja $x_0$ um ponto qualquer nesse intervalo. Pelo [teorema de existência da solução geral](/posts/wronskian-existence-and-uniqueness-of-solutions/#existência-da-solução-geral) para EDOs homogêneas com coeficientes contínuos, sabemos que $y_h = c_1y_1 + c_2y_2$ existe, e pelo **método de variação de parâmetros** (que veremos posteriormente), $y_p$ também existe. Portanto, a solução geral ($\ref{eqn:general_sol}$) da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) existe no intervalo $I$. Pelo teorema [1(b)](#relação-entre-soluções-de-edos-não-homogêneas-e-suas-edos-homogêneas-correspondentes) demonstrado anteriormente, $Y = y^\* - y_p$ é uma solução da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$, e no ponto $x_0$:

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Pelo [teorema de existência e unicidade para problemas de valor inicial](/posts/wronskian-existence-and-uniqueness-of-solutions/#teorema-de-existência-e-unicidade-para-problemas-de-valor-inicial), existe uma única solução particular $Y$ da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$ que satisfaz as condições iniciais acima, e esta solução pode ser obtida atribuindo valores apropriados às constantes $c_1$ e $c_2$ em $y_h$. Como $y^\* = Y + y_p$, demonstramos que qualquer solução particular $y^\*$ da EDO não-homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) pode ser obtida da solução geral ($\ref{eqn:general_sol}$). $\blacksquare$
