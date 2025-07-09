---
title: "EDOs Lineares Não Homogêneas de Segunda Ordem"
description: "Explore a solução geral de EDOs lineares não homogêneas de segunda ordem, sua relação com a solução homogênea correspondente, e a prova de sua existência e da ausência de soluções singulares."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solução geral** da EDO linear não homogênea de segunda ordem $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: solução geral da EDO homogênea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: solução particular da EDO não homogênea correspondente
> - O termo de resposta $y_p$ é determinado apenas pela entrada $r(x)$, e para a mesma EDO não homogênea, $y_p$ não muda mesmo com condições iniciais diferentes. A diferença entre duas soluções particulares da EDO não homogênea torna-se uma solução da EDO homogênea correspondente.
> - **Existência da Solução Geral**: Se os coeficientes $p(x)$, $q(x)$ e a função de entrada $r(x)$ da EDO não homogênea são contínuos, a solução geral sempre existe.
> - **Não Existência de Solução Singular**: A solução geral inclui todas as soluções da equação (ou seja, não existem soluções singulares).
{: .prompt-info }

## Pré-requisitos
- [EDOs Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskiano, Existência e Unicidade da Solução](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solução Geral e Particular de EDOs Lineares Não Homogêneas de Segunda Ordem
Considere a equação diferencial ordinária linear não homogênea de segunda ordem

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

onde $r(x) \not\equiv 0$. A **solução geral** da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) em um intervalo aberto $I$ é a soma da solução geral $y_h = c_1y_1 + c_2y_2$ da equação diferencial ordinária homogênea correspondente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

e uma solução particular $y_p$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$), dada por

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Além disso, uma **solução particular** da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$ é uma solução obtida a partir da equação ($\ref{eqn:general_sol}$) ao se atribuir valores específicos às constantes arbitrárias $c_1$ e $c_2$ de $y_h$.

Ou seja, se adicionarmos uma entrada $r(x)$, que depende apenas da variável independente $x$, à EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$), um termo correspondente $y_p$ é adicionado à resposta. Este termo de resposta adicionado, $y_p$, é determinado unicamente pela entrada $r(x)$, independentemente das condições iniciais. Como veremos mais adiante, se tomarmos a diferença entre duas soluções quaisquer $y_1$ e $y_2$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) (ou seja, a diferença entre as soluções particulares para duas condições iniciais diferentes), a parte $y_p$, que é independente das condições iniciais, é cancelada, restando apenas a diferença entre ${y_h}_1$ e ${y_h}_2$. Pelo [Princípio da Superposição](/posts/homogeneous-linear-odes-of-second-order/#principio-da-superposicao), esta diferença é uma solução da equação ($\ref{eqn:homogeneous_linear_ode}$).

## Relação entre a Solução da EDO Não Homogênea e a Solução da EDO Homogênea Correspondente
> **Teorema 1: Relação entre a Solução da EDO Não Homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) e a Solução da EDO Homogênea ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** A soma de uma solução $y$ da EDO não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) e uma solução $\tilde{y}$ da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) em um intervalo aberto $I$ é uma solução da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$. Em particular, a equação ($\ref{eqn:general_sol}$) é uma solução da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$.  
> **(b)** A diferença entre duas soluções da EDO não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) em um intervalo $I$ é uma solução da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$.
{: .prompt-info }

### Demonstração
#### (a)
Vamos denotar o lado esquerdo das equações ($\ref{eqn:nonhomogeneous_linear_ode}$) e ($\ref{eqn:homogeneous_linear_ode}$) como $L[y]$. Então, para qualquer solução $y$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) e qualquer solução $\tilde{y}$ da equação ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$, temos:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Para quaisquer duas soluções $y$ e $y^\*$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$, temos:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## A Solução Geral da EDO Não Homogênea Inclui Todas as Soluções
Para a EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$), [já sabemos que a solução geral inclui todas as soluções](/posts/wronskian-existence-and-uniqueness-of-solutions/#a-solucao-geral-inclui-todas-as-solucoes). Vamos mostrar que o mesmo vale para a EDO não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Teorema 2: A Solução Geral da EDO Não Homogênea Inclui Todas as Soluções**  
> Se os coeficientes $p(x)$, $q(x)$ e a função de entrada $r(x)$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) são contínuos em um intervalo aberto $I$, então todas as soluções da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$ podem ser obtidas a partir da solução geral ($\ref{eqn:general_sol}$) da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) no intervalo $I$, atribuindo-se valores apropriados às constantes arbitrárias $c_1$ e $c_2$ de $y_h$.
{: .prompt-info }

### Demonstração
Seja $y^\*$ uma solução qualquer da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) em $I$, e seja $x_0$ um ponto qualquer no intervalo $I$. Pelo [Teorema da Existência da Solução Geral](/posts/wronskian-existence-and-uniqueness-of-solutions/#existencia-da-solucao-geral), $y_h = c_1y_1 + c_2y_2$ existe, e pelo **método da variação de parâmetros**, que veremos mais tarde, $y_p$ também existe. Portanto, a solução geral ($\ref{eqn:general_sol}$) da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) existe no intervalo $I$. Agora, pelo Teorema [1(b)](#relacao-entre-a-solucao-da-edo-nao-homogenea-e-a-solucao-da-edo-homogenea-correspondente) demonstrado anteriormente, $Y = y^\* - y_p$ é uma solução da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) no intervalo $I$, e em $x_0$ temos:

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

De acordo com o [Teorema de Existência e Unicidade para Problemas de Valor Inicial](/posts/wronskian-existence-and-uniqueness-of-solutions/#teorema-de-existencia-e-unicidade-para-problemas-de-valor-inicial), existe uma única solução particular $Y$ da EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) para as condições iniciais acima no intervalo $I$, que pode ser obtida atribuindo-se valores apropriados a $c_1$ e $c_2$ de $y_h$. Como $y^\* = Y + y_p$, demonstramos que qualquer solução particular $y^\*$ da EDO não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$) pode ser obtida a partir da solução geral ($\ref{eqn:general_sol}$). $\blacksquare$
