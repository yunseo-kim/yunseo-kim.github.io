---
title: "Wronskiano, Existência e Unicidade da Solução"
description: "Para uma EDO linear homogênea de segunda ordem com coeficientes variáveis contínuos, exploramos o teorema de existência e unicidade da solução para o problema de valor inicial e o método para determinar a dependência/independência linear das soluções usando o Wronskiano. Mostramos também que tais equações sempre possuem uma solução geral que inclui todas as soluções possíveis."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Para uma equação diferencial ordinária linear homogênea de segunda ordem com coeficientes variáveis contínuos $p$ e $q$ em um intervalo $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> e condições iniciais
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> os seguintes 4 teoremas são válidos.
> 1. **Teorema de Existência e Unicidade para Problemas de Valor Inicial**: O problema de valor inicial, composto pela equação e condições iniciais dadas, tem uma solução única $y(x)$ no intervalo $I$.
> 2. **Critério de Dependência/Independência Linear usando o Wronskiano**: Para duas soluções $y_1$ e $y_2$ da equação, se existe um $x_0$ no intervalo $I$ onde o **Wronskiano** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ é $0$, as duas soluções são linearmente dependentes. Além disso, se existe um $x_1$ no intervalo $I$ onde $W\neq 0$, as duas soluções são linearmente independentes.
> 3. **Existência da Solução Geral**: A equação dada possui uma solução geral no intervalo $I$.
> 4. **Inexistência de Solução Singular**: Esta solução geral inclui todas as soluções da equação (ou seja, não existem soluções singulares).
{: .prompt-info }

## Pré-requisitos
- [Solução de EDOs Lineares de Primeira Ordem](/posts/Solution-of-First-Order-Linear-ODE/)
- [EDOs Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs Lineares Homogêneas de Segunda Ordem com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Equação de Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matriz inversa, matriz singular e determinante

## EDO Linear Homogênea com Coeficientes Variáveis Contínuos
Anteriormente, examinamos a solução geral para [EDOs lineares homogêneas de segunda ordem com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) e a [equação de Euler-Cauchy](/posts/euler-cauchy-equation/).
Neste artigo, estenderemos a discussão para um caso mais geral, investigando a existência e a forma da solução geral para uma equação diferencial ordinária linear homogênea de segunda ordem com **coeficientes variáveis** contínuos arbitrários $p$ e $q$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Além disso, investigaremos a unicidade do [problema de valor inicial](/posts/homogeneous-linear-odes-of-second-order/#problema-de-valor-inicial-e-condicoes-iniciais) composto pela equação diferencial ordinária ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) e as duas seguintes condições iniciais:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Para antecipar a conclusão, o ponto principal aqui é que uma equação diferencial ordinária <u>linear</u> com coeficientes contínuos não possui uma *solução singular* (uma solução que não pode ser obtida a partir da solução geral).

## Teorema de Existência e Unicidade para Problemas de Valor Inicial
> **Teorema de Existência e Unicidade para Problemas de Valor Inicial**  
> Se $p(x)$ e $q(x)$ são funções contínuas em um intervalo aberto $I$, e $x_0$ está dentro do intervalo $I$, então o problema de valor inicial composto pelas equações ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) e ($\ref{eqn:initial_conditions}$) tem uma solução única $y(x)$ no intervalo $I$.
{: .prompt-info }

A prova da existência não será abordada aqui; examinaremos apenas a prova da unicidade. Geralmente, provar a unicidade é mais simples do que provar a existência.  
Se você não estiver interessado na demonstração, pode pular esta parte e ir para [Dependência e Independência Linear das Soluções](#dependencia-e-independencia-linear-das-solucoes).

### Demonstração da Unicidade
Suponha que o problema de valor inicial composto pela equação diferencial ordinária ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) e as condições iniciais ($\ref{eqn:initial_conditions}$) tenha duas soluções, $y_1(x)$ e $y_2(x)$, no intervalo $I$. Se pudermos mostrar que a diferença entre essas duas soluções

$$ y(x) = y_1(x) - y_2(x) $$

é identicamente zero no intervalo $I$, isso implica que $y_1 \equiv y_2$ no intervalo $I$, significando a unicidade da solução.

Como a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) é uma EDO linear homogênea, $y$, que é uma combinação linear de $y_1$ e $y_2$, é uma solução da equação em $I$. Como $y_1$ e $y_2$ satisfazem as mesmas condições iniciais ($\ref{eqn:initial_conditions}$), $y$ satisfaz a condição

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Agora, considere a função

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

e sua derivada

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

Da equação diferencial ordinária, obtemos

$$ y^{\prime\prime} = -py^{\prime} - qy $$

Substituindo isso na equação para $z^{\prime}$, obtemos

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Agora, como $y$ e $y^{\prime}$ são reais,

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

A partir disso e da definição de $z$, obtemos duas desigualdades

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Dessas duas desigualdades, podemos ver que $\|2yy^{\prime}\|\leq z$, e então a seguinte desigualdade vale para o último termo da equação ($\ref{eqn:z_prime}$).

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Usando este resultado junto com $-p \leq \|p\|$ e aplicando a equação ($\ref{eqn:inequalities}$a) ao termo $2yy^{\prime}$ da equação ($\ref{eqn:z_prime}$), temos

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Como ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, obtemos

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

e, definindo a função entre parênteses como $h = 1 + 2\|p\| + \|q\|$, temos

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Da mesma forma, a partir das equações ($\ref{eqn:z_prime}$) e ($\ref{eqn:inequalities}$), obtemos

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Essas duas desigualdades ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$) são equivalentes à seguinte desigualdade

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

e os [fatores integrantes](/posts/Solution-of-First-Order-Linear-ODE/#equacao-diferencial-ordinaria-linear-nao-homogenea) para os lados esquerdos das duas equações são

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{e} \qquad F_2 = e^{\int h(x)\ dx} $$

Como $h$ é contínuo, a integral indefinida $\int h(x)\ dx$ existe, e como $F_1$ e $F_2$ são positivos, da equação ($\ref{eqn:inequalities_7}$) obtemos

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Isso significa que $F_1 z$ não é crescente e $F_2 z$ não é decrescente no intervalo $I$. Pela equação ($\ref{eqn:initial_conditions_*}$), $z(x_0) = 0$, então

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finalmente, dividindo ambos os lados das desigualdades pelos positivos $F_1$ e $F_2$, podemos mostrar a unicidade da solução da seguinte forma:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dependência e Independência Linear das Soluções
Vamos relembrar brevemente o que foi discutido em [EDOs Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/#base-e-solucao-geral). A solução geral em um intervalo aberto $I$ é construída a partir de uma **base** $y_1$, $y_2$ em $I$, ou seja, um par de soluções linearmente independentes. Aqui, dizer que $y_1$ e $y_2$ são **linearmente independentes** no intervalo $I$ significa que para todo $x$ no intervalo, o seguinte é satisfeito:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ e }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Se o acima não for satisfeito, e $k_1y_1(x) + k_2y_2(x) = 0$ for válido para pelo menos um $k_1$ ou $k_2$ não nulo, então $y_1$ e $y_2$ são **linearmente dependentes** no intervalo $I$. Neste caso, para todo $x$ no intervalo $I$,

$$ \text{(a) } y_1 = ky_2 \quad \text{ou} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

de modo que $y_1$ e $y_2$ são proporcionais.

Agora, vamos examinar o seguinte critério para dependência/independência linear das soluções.

> **Critério de Dependência/Independência Linear usando o Wronskiano**  
> **i.** Se a equação diferencial ordinária ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem coeficientes contínuos $p(x)$ e $q(x)$ em um intervalo aberto $I$, então a condição necessária e suficiente para que duas soluções $y_1$ e $y_2$ da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sejam linearmente dependentes no intervalo $I$ é que seu *determinante Wronskiano*, ou simplesmente **Wronskiano**, o seguinte determinante
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> seja zero em algum $x_0$ dentro do intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ e } y_2 \text{ são linearmente dependentes} $$
>
> **ii.** Se $W=0$ em um ponto $x=x_0$ dentro do intervalo $I$, então $W=0$ para todo $x$ no intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> Em outras palavras, se existe um $x_1$ no intervalo $I$ tal que $W\neq 0$, então $y_1$ e $y_2$ são linearmente independentes nesse intervalo $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ e } y_2 \text{ são linearmente independentes}
> \end{align*}$$
>
{: .prompt-info }

> O Wronskiano foi introduzido pela primeira vez pelo matemático polonês Józef Maria Hoene-Wroński e recebeu seu nome atual em 11882 HE, após sua morte, pelo matemático escocês Sir Thomas Muir.
{: .prompt-tip }

### Demonstração
#### i. (a)
Suponha que $y_1$ e $y_2$ sejam linearmente dependentes no intervalo $I$. Então, a equação ($\ref{eqn:linearly_dependent}$a) ou ($\ref{eqn:linearly_dependent}$b) é válida no intervalo $I$. Se a equação ($\ref{eqn:linearly_dependent}$a) for válida, então

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

e, da mesma forma, se a equação ($\ref{eqn:linearly_dependent}$b) for válida,

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Portanto, podemos confirmar que o Wronskiano $W(y_1, y_2)=0$ <u>para todo $x$ no intervalo $I$</u>.

#### i. (b)
Inversamente, suponha que $W(y_1, y_2)=0$ para algum $x = x_0$. Mostraremos que $y_1$ e $y_2$ são linearmente dependentes no intervalo $I$. Considere o sistema de equações lineares para as incógnitas $k_1$, $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Isso pode ser expresso na forma de uma equação vetorial:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

A matriz de coeficientes desta equação vetorial é

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

e o determinante desta matriz é $W(y_1(x_0), y_2(x_0))$. Como $\det(A) = W=0$, $A$ é uma **matriz singular** que não possui **matriz inversa**, e, portanto, o sistema de equações ($\ref{eqn:linear_system}$) tem uma solução não trivial $(c_1, c_2)$ diferente do vetor nulo $(0,0)$, onde pelo menos um de $k_1$ e $k_2$ não é zero. Agora, introduza a função

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Como a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) é linear homogênea, pelo [Princípio da Superposição](/posts/homogeneous-linear-odes-of-second-order/#principio-da-superposicao), esta função é uma solução de ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$. Da equação ($\ref{eqn:linear_system}$), podemos ver que esta solução satisfaz as condições iniciais $y(x_0)=0$, $y^{\prime}(x_0)=0$.

Por outro lado, existe a solução trivial $y^\* \equiv 0$ que satisfaz as mesmas condições iniciais $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Como os coeficientes $p$ e $q$ da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) são contínuos, a unicidade da solução é garantida pelo [Teorema de Existência e Unicidade para Problemas de Valor Inicial](#teorema-de-existencia-e-unicidade-para-problemas-de-valor-inicial), e, portanto, $y \equiv y^\*$. Ou seja, no intervalo $I$,

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Como pelo menos um de $c_1$ e $c_2$ não é zero, a condição ($\ref{eqn:linearly_independent}$) não é satisfeita, o que significa que $y_1$ e $y_2$ são linearmente dependentes no intervalo $I$.

#### ii.
Se $W(x_0)=0$ em algum ponto $x_0$ no intervalo $I$, então por [i.(b)](#i-b), $y_1$ e $y_2$ são linearmente dependentes no intervalo $I$, e então por [i.(a)](#i-a), $W\equiv 0$. Portanto, se existe pelo menos um $x_1$ no intervalo $I$ tal que $W(x_1)\neq 0$, então $y_1$ e $y_2$ são linearmente independentes. $\blacksquare$

## A Solução Geral Inclui Todas as Soluções
### Existência da Solução Geral
> Se $p(x)$ e $q(x)$ são contínuos em um intervalo aberto $I$, então a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem uma solução geral no intervalo $I$.
{: .prompt-info }

#### Demonstração
Pelo [Teorema de Existência e Unicidade para Problemas de Valor Inicial](#teorema-de-existencia-e-unicidade-para-problemas-de-valor-inicial), a equação diferencial ordinária ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem uma solução $y_1(x)$ que satisfaz as condições iniciais

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

no intervalo $I$, e uma solução $y_2(x)$ que satisfaz as condições iniciais

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

no intervalo $I$. O Wronskiano dessas duas soluções em $x=x_0$ tem um valor não nulo

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Portanto, pelo [Critério de Dependência/Independência Linear usando o Wronskiano](#dependencia-e-independencia-linear-das-solucoes), $y_1$ e $y_2$ são linearmente independentes no intervalo $I$. Assim, essas duas soluções formam uma base de soluções para a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$, e uma solução geral $y = c_1y_1 + c_2y_2$ com constantes arbitrárias $c_1$, $c_2$ deve existir no intervalo $I$. $\blacksquare$

### Inexistência de Solução Singular
> Se a equação diferencial ordinária ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem coeficientes contínuos $p(x)$ e $q(x)$ em um intervalo aberto $I$, então toda solução $y=Y(x)$ da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$ é da forma
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> onde $y_1$, $y_2$ são uma base de soluções da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$ e $C_1$, $C_2$ são constantes apropriadas.  
> Ou seja, a equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) não possui uma **solução singular**, que é uma solução que não pode ser obtida a partir da solução geral.
{: .prompt-info }

#### Demonstração
Seja $y=Y(x)$ qualquer solução da equação ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no intervalo $I$. Agora, pelo [Teorema da Existência da Solução Geral](#existencia-da-solucao-geral), a equação diferencial ordinária ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tem uma solução geral no intervalo $I$

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Agora, devemos mostrar que para qualquer $Y(x)$, existem constantes $c_1$, $c_2$ tais que $y(x)=Y(x)$ no intervalo $I$. Primeiro, vamos mostrar que podemos encontrar valores de $c_1$, $c_2$ tais que $y(x_0)=Y(x_0)$ e $y^{\prime}(x_0)=Y^{\prime}(x_0)$ para um $x_0$ arbitrário no intervalo $I$. Da equação ($\ref{eqn:general_solution}$), temos

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

Como $y_1$ e $y_2$ formam uma base, o determinante da matriz de coeficientes, $W(y_1(x_0), y_2(x_0))$, é diferente de zero, e, portanto, a equação ($\ref{eqn:vector_equation_2}$) pode ser resolvida para $c_1$ e $c_2$. Seja a solução $(c_1, c_2) = (C_1, C_2)$. Substituindo isso na equação ($\ref{eqn:general_solution}$), obtemos a seguinte solução particular:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Como $C_1$, $C_2$ são a solução da equação ($\ref{eqn:vector_equation_2}$),

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Pela unicidade do [Teorema de Existência e Unicidade para Problemas de Valor Inicial](#teorema-de-existencia-e-unicidade-para-problemas-de-valor-inicial), $y^\* \equiv Y$ para todo $x$ no intervalo $I$. $\blacksquare$
