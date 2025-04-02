---
title: Teste de Convergência ou Divergência de Séries
description: Examinamos vários métodos para determinar a convergência ou divergência de séries.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Teste do termo geral**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{a série }\sum a_n \text{ diverge}$
> - **Convergência/divergência de séries geométricas**: A série geométrica $\sum ar^{n-1}$:
>   - Converge se $\|r\| < 1$
>   - Diverge se $\|r\| \geq 1$
> - **Convergência/divergência de séries-$p$**: A série-$p$ $\sum \cfrac{1}{n^p}$:
>   - Converge se $p>1$
>   - Diverge se $p\leq 1$
> - **Teste de comparação**: Se $0 \leq a_n \leq b_n$, então:  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Teste de comparação no limite**: Se $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ é um número positivo finito)}$, então as séries $\sum a_n$ e $\sum b_n$ ambas convergem ou ambas divergem
> - Para uma série de termos positivos $\sum a_n$ e um número positivo $\epsilon < 1$:  
>   - Se $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, então a série $\sum a_n$ converge
>   - Se $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, então a série $\sum a_n$ diverge
> - **Teste da raiz**: Para uma série de termos positivos $\sum a_n$, se o limite $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ existe:
>   - Se $r<1$, então a série $\sum a_n$ converge
>   - Se $r>1$, então a série $\sum a_n$ diverge
> - **Teste da razão**: Para uma sequência de números positivos $(a_n)$ e $0 < r < 1$:
>   - Se $a_{n+1}/a_n \leq r$ para todo $n$, então a série $\sum a_n$ converge
>   - Se $a_{n+1}/a_n \geq 1$ para todo $n$, então a série $\sum a_n$ diverge
> - Para uma sequência de números positivos $(a_n)$, se o limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe:
>   - Se $\rho < 1$, então a série $\sum a_n$ converge
>   - Se $\rho > 1$, então a série $\sum a_n$ diverge
> - **Teste da integral**: Se uma função contínua $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ é decrescente e sempre $f(x)>0$, então a série $\sum f(n)$ converge se e somente se a integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converge
> - **Teste da série alternada**: Uma série alternada $\sum a_n$ converge se:
>   1. Os sinais de $a_n$ e $a_{n+1}$ são diferentes para todo $n$
>   2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Uma série absolutamente convergente é convergente. A recíproca não é verdadeira.
{: .prompt-info }

## Pré-requisitos
- [Sequências e Séries](/posts/sequences-and-series/)

## Introdução
Anteriormente, em [Sequências e Séries](/posts/sequences-and-series/#convergência-e-divergência-de-séries), vimos a definição de convergência e divergência de séries. Neste artigo, resumiremos vários métodos que podem ser usados para determinar a convergência ou divergência de séries. Geralmente, determinar se uma série converge ou diverge é muito mais fácil do que calcular a soma exata da série.

## Teste do termo geral
Para uma série $\sum a_n$, chamamos $a_n$ de **termo geral** da série.

Pelo seguinte teorema, podemos facilmente identificar que algumas séries divergem claramente, e portanto, verificar isso primeiro é uma abordagem sensata para evitar perda de tempo ao determinar a convergência ou divergência de uma série.

> **Teste do termo geral**  
> Se uma série $\sum a_n$ converge, então
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Ou seja,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{a série }\sum a_n \text{ diverge} $$
{: .prompt-info }

### Prova
Seja $l$ a soma de uma série convergente $\sum a_n$ e defina a soma dos primeiros $n$ termos como

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Então,

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Portanto, para $n$ suficientemente grande ($>N$),

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Pela definição de convergência de sequência,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Observação importante
A recíproca deste teorema geralmente não é verdadeira. Um exemplo clássico que demonstra isso é a **série harmônica**.

A série harmônica é uma série cujos termos são os recíprocos de uma **progressão aritmética**, ou seja, uma **sequência harmônica**. A série harmônica mais representativa é

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Podemos mostrar que esta série diverge da seguinte forma:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Assim, vemos que a série $H_n$ diverge, apesar de seu termo geral $1/n$ convergir para $0$.

> Se $\lim_{n\to\infty} a_n \neq 0$, então a série $\sum a_n$ certamente diverge, mas é perigoso assumir que a série $\sum a_n$ converge apenas porque $\lim_{n\to\infty} a_n = 0$. Nesse caso, outros métodos devem ser usados para determinar a convergência ou divergência.
{: .prompt-danger }

## Séries geométricas
A **série geométrica** com primeiro termo 1 e **razão** $r$

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

é a <u>série mais importante e fundamental</u>. Da equação

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

obtemos

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Por outro lado,

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

Portanto, sabemos que a condição necessária e suficiente para a convergência da série geométrica ($\ref{eqn:geometric_series}$) é $\|r\| < 1$.

> **Convergência/divergência de séries geométricas**  
> A série geométrica $\sum ar^{n-1}$:
> - Converge se $\|r\| < 1$
> - Diverge se $\|r\| \geq 1$
{: .prompt-info }

Disso, obtemos

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Séries geométricas e aproximações
A identidade ($\ref{eqn:sum_of_geometric_series}$) é útil para encontrar aproximações de $\cfrac{1}{1-r}$ quando $\|r\| < 1$.

Substituindo $r=-\epsilon$ e $n=2$ nesta equação, obtemos

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Portanto, se $0 < \epsilon < 1$, então

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

Assim,

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Isso nos mostra que, para um valor positivo suficientemente pequeno $\epsilon$, $\cfrac{1}{1 + \epsilon}$ pode ser aproximado por $1 - \epsilon$.

## Teste da série-$p$ (Teste da série-$p$)  
Para um número real positivo $p$, uma série da seguinte forma é chamada de **série-$p$**:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Convergência/divergência de séries-$p$**  
> A série-$p$ $\sum \cfrac{1}{n^p}$:
> - Converge se $p>1$
> - Diverge se $p\leq 1$
{: .prompt-info }

No caso da série-$p$ onde $p=1$, temos a série harmônica, que já mostramos que diverge.  
O problema de encontrar o valor da série-$p$ para $p=2$, ou seja, $\sum \cfrac{1}{n^2}$, é conhecido como o "problema de Basel", nomeado após a cidade natal da família Bernoulli, que produziu vários matemáticos famosos ao longo de gerações e foi a primeira a demonstrar que esta série converge. A resposta para este problema é conhecida como $\cfrac{\pi^2}{6}$.

Mais geralmente, a série-$p$ para $p>1$ é chamada de **função zeta**. Esta é uma função especial introduzida por Leonhard Euler em 11740 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) e posteriormente nomeada por Riemann, definida como:

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Este tópico se afasta um pouco do nosso foco principal e, para ser honesto, como sou um estudante de engenharia e não um matemático, não vou entrar em detalhes aqui. No entanto, vale mencionar que Leonhard Euler mostrou que a função zeta também pode ser expressa como um produto infinito de números primos, conhecido como **Produto de Euler**, e desde então a função zeta ocupa uma posição central em vários campos da teoria analítica dos números. A **função zeta de Riemann**, que estende o domínio da função zeta para números complexos, e a importante conjectura não resolvida conhecida como **Hipótese de Riemann** são exemplos disso.

Voltando ao nosso tópico original, a prova do teste da série-$p$ requer o [teste de comparação](#teste-de-comparação) e o [teste da integral](#teste-da-integral), que serão discutidos mais adiante. No entanto, a convergência/divergência das séries-$p$ pode ser útil no [teste de comparação](#teste-de-comparação) que veremos a seguir, por isso foi intencionalmente colocada nesta posição.

### Prova
#### i) Quando $p>1$
A integral

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converge, então pelo [teste da integral](#teste-da-integral), a série $\sum \cfrac{1}{n^p}$ também converge.

#### ii) Quando $p\leq 1$
Neste caso,

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Sabemos que a série harmônica $\sum \cfrac{1}{n}$ diverge, então pelo [teste de comparação](#teste-de-comparação), $\sum \cfrac{1}{n^p}$ também diverge.

#### Conclusão
Por i) e ii), a série-$p$ $\sum \cfrac{1}{n^p}$ converge se $p>1$ e diverge se $p \leq 1$. $\blacksquare$

## Teste de comparação
O **teste de comparação** de Jakob Bernoulli é útil para determinar a convergência/divergência de **séries de termos positivos**, que são séries cujos termos gerais são números reais não negativos.

Uma série de termos positivos $\sum a_n$ é uma sequência crescente, então se não divergir para o infinito ($\sum a_n = \infty$), ela necessariamente converge. Portanto, para séries de termos positivos, a expressão

$$ \sum a_n < \infty $$

significa que <u>a série converge</u>.

> **Teste de comparação**  
> Se $0 \leq a_n \leq b_n$, então:  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

Em particular, para séries de termos positivos como $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, que têm formas semelhantes às séries geométricas $\sum ar^{n-1}$ ou séries-$p$ $\sum \cfrac{1}{n^p}$ que vimos anteriormente, é recomendável tentar ativamente o teste de comparação.

Vários outros testes de convergência/divergência que serão discutidos posteriormente podem ser derivados deste **teste de comparação**, o que o torna o mais importante nesse sentido.

### Teste de comparação no limite
Para séries de termos positivos $\sum a_n$ e $\sum b_n$, se a razão entre os termos gerais das duas séries $a_n/b_n$ tem os termos dominantes no numerador e denominador que se cancelam, resultando em $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ é um número positivo finito)}$, e se conhecemos a convergência/divergência da série $\sum b_n$, podemos usar o seguinte **teste de comparação no limite**.

> **Teste de comparação no limite**  
> Se
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ é um número positivo finito)}$$
>
> então as séries $\sum a_n$ e $\sum b_n$ ambas convergem ou ambas divergem. Ou seja, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Teste da raiz
> **Teorema**  
> Para uma série de termos positivos $\sum a_n$ e um número positivo $\epsilon < 1$:  
> - Se $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, então a série $\sum a_n$ converge
> - Se $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, então a série $\sum a_n$ diverge
{: .prompt-info }

> **Corolário: Teste da raiz**  
> Para uma série de termos positivos $\sum a_n$, se o limite
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> existe, então:
> - Se $r<1$, a série $\sum a_n$ converge
> - Se $r>1$, a série $\sum a_n$ diverge
{: .prompt-info }

> No corolário acima, se $r=1$, não podemos determinar a convergência/divergência e devemos usar outros métodos.
{: .prompt-warning }

## Teste da razão
> **Teste da razão**  
> Para uma sequência de números positivos $(a_n)$ e $0 < r < 1$:
> - Se $a_{n+1}/a_n \leq r$ para todo $n$, então a série $\sum a_n$ converge
> - Se $a_{n+1}/a_n \geq 1$ para todo $n$, então a série $\sum a_n$ diverge
{: .prompt-info }

> **Corolário**  
> Para uma sequência de números positivos $(a_n)$, se o limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe, então:
> - Se $\rho < 1$, a série $\sum a_n$ converge
> - Se $\rho > 1$, a série $\sum a_n$ diverge
{: .prompt-info }

## Teste da integral
O cálculo integral pode ser usado para determinar a convergência/divergência de séries compostas por sequências decrescentes de termos positivos.

> **Teste da integral**  
> Se uma função contínua $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ é decrescente e sempre $f(x)>0$, então a série $\sum f(n)$ converge se e somente se a integral
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converge.
{: .prompt-info }

### Prova
Como a função $f(x)$ é contínua, decrescente e sempre positiva, a desigualdade

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

é válida. Somando esta desigualdade de $n=1$ até o termo geral, obtemos

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Usando o [teste de comparação](#teste-de-comparação), obtemos o resultado desejado. $\blacksquare$

## Séries alternadas
Uma **série alternada** é uma série $\sum a_n$ onde os termos $a_n$ são não nulos e o sinal de cada termo $a_n$ é diferente do sinal do termo seguinte $a_{n+1}$, ou seja, termos positivos e negativos aparecem alternadamente.

Para séries alternadas, o seguinte teorema descoberto pelo matemático alemão Gottfried Wilhelm Leibniz pode ser útil para determinar a convergência/divergência.

> **Teste da série alternada**  
> Se:
> 1. Os sinais de $a_n$ e $a_{n+1}$ são diferentes para todo $n$,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$, e
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> então a série alternada $\sum a_n$ converge.
{: .prompt-info }

## Convergência absoluta
Dizemos que uma série $\sum a_n$ **converge absolutamente** se a série $\sum \|a_n\|$ converge.

O seguinte teorema é válido:

> **Teorema**  
> Uma série absolutamente convergente é convergente.
{: .prompt-info }

> A recíproca do teorema acima não é verdadeira.  
> Quando uma série converge, mas não converge absolutamente, dizemos que ela **converge condicionalmente**.
{: .prompt-warning }

### Prova
Para um número real $a$, definimos

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Então,

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Como $0 \leq a^\pm \leq \|a\|$, pelo [teste de comparação](#teste-de-comparação), se a série $\sum \|a_n\|$ converge, então as séries $\sum a_n^+$ e $\sum a_n^-$ também convergem, e portanto, pelas [propriedades básicas de séries convergentes](/posts/sequences-and-series/#propriedades-básicas-de-séries-convergentes),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

também converge. $\blacksquare$
