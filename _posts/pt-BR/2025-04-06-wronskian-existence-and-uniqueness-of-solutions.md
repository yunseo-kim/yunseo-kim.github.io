---
title: Wronskiano, Existência e Unicidade de Soluções
description: Para equações diferenciais ordinárias lineares homogêneas de segunda ordem com coeficientes variáveis contínuos, exploramos o teorema de existência e unicidade para problemas de valor inicial, o método do Wronskiano para determinar dependência/independência linear de soluções, e demonstramos que tais equações sempre possuem solução geral que inclui todas as soluções possíveis.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Para um intervalo $I$ onde os coeficientes variáveis $p$ e $q$ são contínuos, considere a equação diferencial ordinária linear homogênea de segunda ordem
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> e as condições iniciais
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> Os seguintes quatro teoremas são válidos:
> 1. **Teorema de existência e unicidade para problemas de valor inicial**: O problema de valor inicial formado pela equação dada e pelas condições iniciais possui uma única solução $y(x)$ no intervalo $I$.
> 2. **Determinação de dependência/independência linear usando o Wronskiano**: Para duas soluções $y_1$ e $y_2$ da equação, se existir um ponto $x_0$ no intervalo $I$ onde o **Wronskiano** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ é igual a zero, então as soluções são linearmente dependentes. Além disso, se existir um ponto $x_1$ no intervalo $I$ onde $W\neq 0$, então as soluções são linearmente independentes.
> 3. **Existência da solução geral**: A equação dada possui uma solução geral no intervalo $I$.
> 4. **Inexistência de soluções singulares**: Esta solução geral inclui todas as soluções da equação (ou seja, não existem soluções singulares).
{: .prompt-info }

## Pré-requisitos
- [Solução de Equações Diferenciais Ordinárias Lineares de Primeira Ordem](/posts/Solution-of-First-Order-Linear-ODE/)
- [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Equação de Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matriz inversa e matriz singular, determinante

## Equações Diferenciais Ordinárias Lineares Homogêneas com Coeficientes Variáveis Contínuos
Anteriormente, estudamos a [solução geral de EDOs lineares homogêneas de segunda ordem com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) e a [equação de Euler-Cauchy](/posts/euler-cauchy-equation/).
Neste artigo, expandiremos nossa discussão para um caso mais geral, examinando a existência e a forma da solução geral de uma equação diferencial ordinária linear homogênea de segunda ordem com **coeficientes variáveis** $p$ e $q$ contínuos:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Além disso, também examinaremos a unicidade do [problema de valor inicial](/posts/homogeneous-linear-odes-of-second-order/#problema-de-valor-inicial-e-condições-iniciais) formado pela equação diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) e pelas seguintes duas condições iniciais:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Antecipando a conclusão, o ponto central do que discutiremos é que equações diferenciais ordinárias <u>lineares</u> com coeficientes contínuos não possuem *soluções singulares* (soluções que não podem ser obtidas da solução geral).

## Teorema de Existência e Unicidade para Problemas de Valor Inicial
> **Teorema de Existência e Unicidade para Problemas de Valor Inicial**  
> Se $p(x)$ e $q(x)$ são funções contínuas em algum intervalo aberto $I$, e $x_0$ está nesse intervalo $I$, então o problema de valor inicial formado pelas equações ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) e ($\ref{eqn:initial_conditions}$) possui uma única solução $y(x)$ no intervalo $I$.
{: .prompt-info }

Aqui abordaremos apenas a prova da unicidade, não da existência. Geralmente, provar a unicidade é mais simples do que provar a existência.  
Se você não estiver interessado na demonstração, pode pular esta seção e ir diretamente para [Dependência Linear e Independência Linear de Soluções](#dependência-linear-e-independência-linear-de-soluções).

### Prova da Unicidade
Suponha que o problema de valor inicial formado pela equação diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) e pelas condições iniciais ($\ref{eqn:initial_conditions}$) tenha duas soluções $y_1(x)$ e $y_2(x)$ no intervalo $I$. Se pudermos mostrar que a diferença entre essas soluções

$$ y(x) = y_1(x) - y_2(x) $$

é identicamente zero no intervalo $I$, isso significará que $y_1 \equiv y_2$ no intervalo $I$, provando assim a unicidade da solução.

Como a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) é uma EDO linear homogênea, a combinação linear de $y_1$ e $y_2$, que é $y$, também é uma solução da equação no intervalo $I$. Como $y_1$ e $y_2$ satisfazem as mesmas condições iniciais ($\ref{eqn:initial_conditions}$), $y$ satisfaz as condições

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_1(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Agora, consideremos a função

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

e sua derivada

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

Da equação diferencial, temos

$$ y^{\prime\prime} = -py^{\prime} - qy $$

Substituindo na expressão de $z^{\prime}$, obtemos

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Como $y$ e $y^{\prime}$ são números reais, temos

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

Pela definição de $z$, obtemos duas desigualdades:

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Dessas duas desigualdades, podemos concluir que $\|2yy^{\prime}\|\leq z$, e portanto, para o último termo da equação ($\ref{eqn:z_prime}$), temos a seguinte desigualdade:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Usando este resultado junto com o fato de que $-p \leq \|p\|$, e aplicando a desigualdade ($\ref{eqn:inequalities}$a) ao termo $2yy^{\prime}$ na equação ($\ref{eqn:z_prime}$), obtemos:

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Como ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, temos:

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Definindo a função entre parênteses como $h = 1 + 2\|p\| + \|q\|$, temos:

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

De maneira similar, usando as equações ($\ref{eqn:z_prime}$) e ($\ref{eqn:inequalities}$), obtemos:

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Estas duas desigualdades ($\ref{eqn:inequality_6a}$) e ($\ref{eqn:inequality_6b}$) são equivalentes a:

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

Os [fatores integrantes](/posts/Solution-of-First-Order-Linear-ODE/#equação-diferencial-ordinária-linear-não-homogênea) para os lados esquerdos dessas equações são:

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{e} \qquad F_2 = e^{\int h(x)\ dx} $$

Como $h$ é contínua, a integral indefinida $\int h(x)\ dx$ existe, e como $F_1$ e $F_2$ são positivos, das equações ($\ref{eqn:inequalities_7}$) obtemos:

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Isso significa que $F_1 z$ não aumenta e $F_2 z$ não diminui no intervalo $I$. Como $z(x_0) = 0$ pela equação ($\ref{eqn:initial_conditions_*}$), temos:

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finalmente, dividindo ambos os lados das desigualdades pelos valores positivos $F_1$ e $F_2$, podemos provar a unicidade da solução:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dependência Linear e Independência Linear de Soluções
Relembrando o que vimos em [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/#base-e-solução-geral), a solução geral em um intervalo aberto $I$ é construída a partir de uma **base** $y_1$, $y_2$, ou seja, um par de soluções linearmente independentes. Duas funções $y_1$ e $y_2$ são **linearmente independentes** no intervalo $I$ se, para todos os pontos nesse intervalo:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ e }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Se a condição acima não for satisfeita, ou seja, se existirem valores $k_1$, $k_2$ não ambos nulos tais que $k_1y_1(x) + k_2y_2(x) = 0$, então $y_1$ e $y_2$ são **linearmente dependentes** no intervalo $I$. Neste caso, para todos os pontos no intervalo $I$:

$$ \text{(a) } y_1 = ky_2 \quad \text{ou} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

ou seja, $y_1$ e $y_2$ são proporcionais.

Agora, vejamos o método para determinar a dependência/independência linear de soluções:

> **Determinação de Dependência/Independência Linear usando o Wronskiano**  
> **i.** Se a equação diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem coeficientes $p(x)$ e $q(x)$ contínuos em um intervalo aberto $I$, então uma condição necessária e suficiente para que duas soluções $y_1$ e $y_2$ da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$ sejam linearmente dependentes é que o *determinante wronskiano*, ou simplesmente **Wronskiano**
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> seja igual a zero em algum ponto $x_0$ do intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ e } y_2 \text{ são linearmente dependentes} $$
>
> **ii.** Se o Wronskiano $W=0$ em um ponto $x=x_0$ do intervalo $I$, então $W=0$ para todos os pontos $x$ do intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> Em outras palavras, se existir um ponto $x_1$ no intervalo $I$ onde $W\neq 0$, então $y_1$ e $y_2$ são linearmente independentes no intervalo $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ e } y_2 \text{ são linearmente independentes}
> \end{align*}$$
>
{: .prompt-info }

> O Wronskiano foi introduzido pelo matemático polonês Józef Maria Hoene-Wroński e recebeu seu nome atual do matemático escocês Sir Thomas Muir em 11882 EH, após a morte de Wroński.
{: .prompt-tip }

### Demonstração
#### i. (a)
Suponha que $y_1$ e $y_2$ sejam linearmente dependentes no intervalo $I$. Então, no intervalo $I$, vale a equação ($\ref{eqn:linearly_dependent}$a) ou ($\ref{eqn:linearly_dependent}$b). Se a equação ($\ref{eqn:linearly_dependent}$a) for válida, então:

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

Da mesma forma, se a equação ($\ref{eqn:linearly_dependent}$b) for válida:

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Portanto, podemos verificar que <u>para todos os pontos $x$ no intervalo $I$</u>, o Wronskiano $W(y_1, y_2)=0$.

#### i. (b)
Reciprocamente, vamos mostrar que se $W(y_1, y_2)=0$ em algum ponto $x = x_0$, então $y_1$ e $y_2$ são linearmente dependentes no intervalo $I$. Considere o sistema linear de equações com incógnitas $k_1$ e $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Isso pode ser expresso como uma equação vetorial:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

A matriz de coeficientes desta equação vetorial é:

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

e seu determinante é $W(y_1(x_0), y_2(x_0))$. Como $\det(A) = W=0$, $A$ é uma **matriz singular** que não possui **matriz inversa**, e portanto o sistema de equações ($\ref{eqn:linear_system}$) tem uma solução não-trivial $(c_1, c_2)$ onde pelo menos um dos valores $c_1$ ou $c_2$ é não-nulo. Agora, definamos a função:

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Como a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) é linear homogênea, pelo [princípio da superposição](/posts/homogeneous-linear-odes-of-second-order/#princípio-da-superposição), esta função é uma solução da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$. Da equação ($\ref{eqn:linear_system}$), esta solução satisfaz as condições iniciais $y(x_0)=0$ e $y^{\prime}(x_0)=0$.

Por outro lado, existe a solução trivial $y^\* \equiv 0$ que satisfaz as mesmas condições iniciais $y^\*(x_0)=0$ e ${y^\*}^{\prime}(x_0)=0$. Como os coeficientes $p$ e $q$ da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) são contínuos, pelo [Teorema de Existência e Unicidade para Problemas de Valor Inicial](#teorema-de-existência-e-unicidade-para-problemas-de-valor-inicial), a unicidade da solução é garantida, e portanto $y \equiv y^\*$. Ou seja, no intervalo $I$:

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Como pelo menos um dos valores $c_1$ ou $c_2$ é não-nulo, a condição ($\ref{eqn:linearly_independent}$) não é satisfeita, o que significa que $y_1$ e $y_2$ são linearmente dependentes no intervalo $I$.

#### ii.
Se o Wronskiano for zero em algum ponto $x_0$ do intervalo $I$, então pelo item [i.(b)](#i-b), $y_1$ e $y_2$ são linearmente dependentes no intervalo $I$, e pelo item [i.(a)](#i-a), $W\equiv 0$. Portanto, se existir um ponto $x_1$ no intervalo $I$ onde $W(x_1)\neq 0$, então $y_1$ e $y_2$ são linearmente independentes. $\blacksquare$

## A Solução Geral Inclui Todas as Soluções
### Existência da Solução Geral
> Se $p(x)$ e $q(x)$ são contínuas em um intervalo aberto $I$, então a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) possui uma solução geral no intervalo $I$.
{: .prompt-info }

#### Demonstração
Pelo [Teorema de Existência e Unicidade para Problemas de Valor Inicial](#teorema-de-existência-e-unicidade-para-problemas-de-valor-inicial), a equação diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) possui uma solução $y_1(x)$ no intervalo $I$ que satisfaz as condições iniciais:

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

e uma solução $y_2(x)$ no intervalo $I$ que satisfaz as condições iniciais:

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

O Wronskiano dessas duas soluções no ponto $x=x_0$ é não-nulo:

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Portanto, pela [Determinação de Dependência/Independência Linear usando o Wronskiano](#dependência-linear-e-independência-linear-de-soluções), $y_1$ e $y_2$ são linearmente independentes no intervalo $I$. Assim, essas duas soluções formam uma base para as soluções da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$, e a solução geral $y = c_1y_1 + c_2y_2$, com constantes arbitrárias $c_1$ e $c_2$, existe necessariamente no intervalo $I$. $\blacksquare$

### Inexistência de Soluções Singulares
> Se a equação diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem coeficientes $p(x)$ e $q(x)$ contínuos em algum intervalo aberto $I$, então qualquer solução $y=Y(x)$ da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$ pode ser escrita na forma:
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> onde $y_1$ e $y_2$ formam uma base para as soluções da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$, e $C_1$ e $C_2$ são constantes apropriadas.  
> Em outras palavras, a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) não possui **soluções singulares** (soluções que não podem ser obtidas da solução geral).
{: .prompt-info }

#### Demonstração
Seja $y=Y(x)$ uma solução qualquer da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$. Pelo [teorema de existência da solução geral](#existência-da-solução-geral), a equação diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) possui uma solução geral no intervalo $I$:

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Precisamos mostrar que, para qualquer $Y(x)$, existem constantes $c_1$ e $c_2$ tais que $y(x)=Y(x)$ no intervalo $I$. Primeiro, vamos mostrar que podemos encontrar valores de $c_1$ e $c_2$ tais que $y(x_0)=Y(x_0)$ e $y^{\prime}(x_0)=Y^{\prime}(x_0)$ para qualquer ponto $x_0$ escolhido no intervalo $I$. Da equação ($\ref{eqn:general_solution}$), temos:

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

Como $y_1$ e $y_2$ formam uma base, o determinante da matriz de coeficientes, $W(y_1(x_0), y_2(x_0))$, é não-nulo, e portanto a equação ($\ref{eqn:vector_equation_2}$) pode ser resolvida para $c_1$ e $c_2$. Sejam $(c_1, c_2) = (C_1, C_2)$ a solução. Substituindo na equação ($\ref{eqn:general_solution}$), obtemos a solução particular:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Como $C_1$ e $C_2$ são a solução da equação ($\ref{eqn:vector_equation_2}$), temos:

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Pela unicidade garantida pelo [Teorema de Existência e Unicidade para Problemas de Valor Inicial](#teorema-de-existência-e-unicidade-para-problemas-de-valor-inicial), temos $y^* \equiv Y$ para todos os pontos $x$ no intervalo $I$. $\blacksquare$
