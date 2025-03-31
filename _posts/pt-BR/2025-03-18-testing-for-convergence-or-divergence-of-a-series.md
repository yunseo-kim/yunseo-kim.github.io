---
title: Teste de convergência/divergência de séries (Testing for Convergence or Divergence of a Series)
description: Examinamos vários métodos para testar a convergência/divergência de séries.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Teste do termo geral (n-ésimo termo) para divergência**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{a série }\sum a_n \text{ diverge}$
> - **Convergência/divergência da série geométrica**: A série geométrica $\sum ar^{n-1}$
>   - converge se $\|r\| < 1$
>   - diverge se $\|r\| \geq 1$
> - **Convergência/divergência da série p**: A série p $\sum \cfrac{1}{n^p}$
>   - converge se $p>1$
>   - diverge se $p\leq 1$
> - **Teste de comparação (Comparison Test)**: Se $0 \leq a_n \leq b_n$, então  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Teste de comparação no limite (Limit Comparison Test)**: Se $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ é um número positivo finito)}$, então as duas séries $\sum a_n$ e $\sum b_n$ convergem ou divergem juntas
> - Para uma série de termos positivos $\sum a_n$ e um número positivo $\epsilon < 1$  
>   - Se $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, então a série $\sum a_n$ converge
>   - Se $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, então a série $\sum a_n$ diverge
> - **Teste da raiz (Root Test)**: Para uma série de termos positivos $\sum a_n$, se o limite $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ existe,
>   - a série $\sum a_n$ converge se $r<1$
>   - a série $\sum a_n$ diverge se $r>1$
> - **Teste da razão (Ratio Test)**: Para uma sequência de números positivos $(a_n)$ e $0 < r < 1$
>   - Se $a_{n+1}/a_n \leq r$ para todo $n$, então a série $\sum a_n$ converge
>   - Se $a_{n+1}/a_n \geq 1$ para todo $n$, então a série $\sum a_n$ diverge
> - Para uma sequência de números positivos $(a_n)$, se o limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe,
>   - a série $\sum a_n$ converge se $\rho < 1$
>   - a série $\sum a_n$ diverge se $\rho > 1$
> - **Teste da integral (Integral Test)**: Para uma função contínua e decrescente $f: [1,\infty) \rightarrow \mathbb{R}$ com $f(x)>0$ sempre, a série $\sum f(n)$ converge se e somente se a integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converge
> - **Teste da série alternada (Alternating Series Test)**: Uma série alternada $\sum a_n$ converge se as seguintes condições são satisfeitas:
>   1. $a_n$ e $a_{n+1}$ têm sinais opostos para todo $n$
>   2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Uma série que converge absolutamente também converge. O inverso não é necessariamente verdadeiro.
{: .prompt-info }

## Pré-requisitos
- [Sequências e séries](/posts/sequences-and-series/)

## Introdução
Anteriormente, em [Sequências e séries](/posts/sequences-and-series/#convergência-e-divergência-de-séries), vimos as definições de convergência e divergência de séries. Neste artigo, resumiremos vários métodos que podem ser usados para testar a convergência/divergência de séries. Geralmente, testar a convergência/divergência de uma série é muito mais fácil do que calcular sua soma exata.

## Teste do termo geral
Para uma série $\sum a_n$, $a_n$ é chamado de **termo geral** da série.

Pelo seguinte teorema, podemos facilmente ver que algumas séries obviamente divergem, e portanto, ao testar a convergência/divergência de uma série, é sábio verificar isso primeiro para evitar perda de tempo.

> **Teste do termo geral (n-ésimo termo) para divergência**  
> Se uma série $\sum a_n$ converge, então
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Ou seja,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{a série }\sum a_n \text{ diverge} $$
{: .prompt-info }

### Prova
Seja $l$ a soma de uma série convergente $\sum a_n$ e seja $s_n$ a soma dos primeiros $n$ termos:

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Então,

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Portanto, para $n$ suficientemente grande ($>N$),

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Assim, pela definição de convergência de sequência,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Observação
O inverso deste teorema geralmente não é verdadeiro. Um exemplo típico que demonstra isso é a **série harmônica**.

A série harmônica é uma série obtida de uma sequência cujos termos são os recíprocos de uma **progressão aritmética**, chamada **sequência harmônica**. A série harmônica típica é

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Pode-se mostrar que esta série diverge da seguinte maneira:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Assim, podemos ver que embora a série $H_n$ divirja, o termo geral $1/n$ converge para 0.

> Se $\lim_{n\to\infty} a_n \neq 0$, a série $\sum a_n$ certamente diverge, mas é perigoso pensar que a série $\sum a_n$ convergirá se $\lim_{n\to\infty} a_n = 0$, e neste caso, outros métodos devem ser usados para testar a convergência/divergência.
{: .prompt-danger }

## Série geométrica
A **série geométrica** obtida de uma progressão geométrica com primeiro termo 1 e **razão** $r$

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

é <u>a série mais importante e fundamental</u>. Da equação

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

obtemos

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Por outro lado,

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

Portanto, sabemos que a condição necessária e suficiente para que a série geométrica ($\ref{eqn:geometric_series}$) convirja é $\|r\| < 1$.

> **Convergência/divergência da série geométrica**  
> A série geométrica $\sum ar^{n-1}$
> - converge se $\|r\| < 1$
> - diverge se $\|r\| \geq 1$
{: .prompt-info }

A partir disso, obtemos

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Série geométrica e aproximação
A identidade ($\ref{eqn:sum_of_geometric_series}$) é útil para encontrar uma aproximação de $\cfrac{1}{1-r}$ quando $|r| < 1$.

Substituindo $r=-\epsilon$ e $n=2$ nesta equação, obtemos

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Portanto, se $0 < \epsilon < 1$,

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

assim,

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

A partir disso, podemos ver que para um número positivo $\epsilon$ suficientemente pequeno, $\cfrac{1}{1 + \epsilon}$ pode ser aproximado por $1 - \epsilon$.

## Teste da série p (p-Series Test)  
Para um número real positivo $p$, uma série da seguinte forma é chamada de **série p**:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Convergência/divergência da série p**  
> A série p $\sum \cfrac{1}{n^p}$
> - converge se $p>1$
> - diverge se $p\leq 1$
{: .prompt-info }

Na série p, quando $p=1$, torna-se a série harmônica, que já mostramos que diverge.  
O problema de encontrar o valor da série p quando $p=2$, ou seja, $\sum \cfrac{1}{n^2}$, é chamado de problema de 'Basel', em homenagem à cidade natal da família Bernoulli, que produziu vários matemáticos famosos ao longo de várias gerações e que foi a primeira a provar que esta série converge. A resposta para este problema é conhecida como $\cfrac{\pi^2}{6}$.

Mais generalmente, a série p para $p>1$ é chamada de **função zeta**. Esta é uma das funções especiais introduzidas por Leonhard Euler em 11740 do [calendário da era humana](https://en.wikipedia.org/wiki/Holocene_calendar) e posteriormente nomeada por Riemann, definida como

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Isso se afasta um pouco do tema deste artigo e, para ser honesto, como sou um estudante de engenharia e não um matemático, não sei muito sobre isso, então não vou abordar aqui, mas Leonhard Euler mostrou que a função zeta também pode ser expressa como um produto infinito de números primos chamado **produto de Euler (Euler Product)**, e posteriormente a função zeta ocupa uma posição central em vários campos da teoria analítica dos números. A **função zeta de Riemann (Riemann zeta function)**, que estende o domínio da função zeta para números complexos, e o importante problema não resolvido relacionado a ela, a **hipótese de Riemann (Riemann hypothesis)**, são alguns deles.

Voltando ao tema original, a prova do teste da série p requer o [teste de comparação](#teste-de-comparação) e o [teste da integral](#teste-da-integral), que serão discutidos posteriormente. No entanto, a convergência/divergência da série p pode ser útil no [teste de comparação](#teste-de-comparação) que será discutido logo após a série geométrica, por isso foi intencionalmente colocada mais perto do início.

### Prova
#### i) Quando $p>1$
A integral

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converge, então pelo [teste da integral](#teste-da-integral), podemos ver que a série $\sum \cfrac{1}{n^p}$ também converge.

#### ii) Quando $p\leq 1$
Neste caso,

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Aqui, sabemos que a série harmônica $\sum \cfrac{1}{n}$ diverge, então pelo [teste de comparação](#teste-de-comparação), podemos ver que $\sum \cfrac{1}{n^p}$ também diverge.

#### Conclusão
Por i) e ii), a série p $\sum \cfrac{1}{n^p}$ converge se $p>1$ e diverge se $p \leq 1$. $\blacksquare$

## Teste de comparação
O **teste de comparação (Comparison Test)** de Jakob Bernoulli é útil para testar a convergência/divergência de **séries de termos positivos**, que são séries cujo termo geral consiste em números reais não negativos.

Como uma série de termos positivos $\sum a_n$ é uma sequência crescente, ela necessariamente converge a menos que divirja para o infinito ($\sum a_n = \infty$). Portanto, para uma série de termos positivos, a expressão

$$ \sum a_n < \infty $$

significa que <u>a série converge</u>.

> **Teste de comparação (Comparison Test)**  
> Se $0 \leq a_n \leq b_n$, então  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

Em particular, para séries de termos positivos como $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, que têm formas semelhantes às séries geométricas $\sum ar^{n-1}$ ou séries p $\sum \cfrac{1}{n^p}$ que vimos anteriormente, é bom tentar ativamente o teste de comparação para julgar sua convergência/divergência.

Todos os outros vários testes de convergência/divergência que serão discutidos posteriormente podem ser derivados deste **teste de comparação**, e nesse sentido, pode-se dizer que o teste de comparação é o mais importante.

### Teste de comparação no limite
Para séries de termos positivos $\sum a_n$ e $\sum b_n$, suponha que a razão dos termos gerais das duas séries $a_n/b_n$ tenha os termos dominantes no numerador e denominador cancelados, resultando em $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ é um número positivo finito)}$. Se a convergência/divergência da série $\sum b_n$ é conhecida, então o seguinte **teste de comparação no limite (Limit Comparison Test)** pode ser utilizado.

> **Teste de comparação no limite (Limit Comparison Test)**  
> Se
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ é um número positivo finito)}$$
>
> então as duas séries $\sum a_n$ e $\sum b_n$ convergem ou divergem juntas. Ou seja, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Teste da raiz
> **Teorema**  
> Para uma série de termos positivos $\sum a_n$ e um número positivo $\epsilon < 1$  
> - Se $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, então a série $\sum a_n$ converge
> - Se $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, então a série $\sum a_n$ diverge
{: .prompt-info }

> **Corolário: Teste da raiz (Root Test)**  
> Para uma série de termos positivos $\sum a_n$, suponha que o limite
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> exista. Então
> - a série $\sum a_n$ converge se $r<1$
> - a série $\sum a_n$ diverge se $r>1$
{: .prompt-info }

> No corolário acima, se $r=1$, a convergência/divergência não pode ser determinada, então outro método deve ser usado.
{: .prompt-warning }

## Teste da razão
> **Teste da razão (Ratio Test)**  
> Para uma sequência de números positivos $(a_n)$ e $0 < r < 1$
> - Se $a_{n+1}/a_n \leq r$ para todo $n$, então a série $\sum a_n$ converge
> - Se $a_{n+1}/a_n \geq 1$ para todo $n$, então a série $\sum a_n$ diverge
{: .prompt-info }

> **Corolário**  
> Para uma sequência de números positivos $(a_n)$, suponha que o limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ exista. Então
> - a série $\sum a_n$ converge se $\rho < 1$
> - a série $\sum a_n$ diverge se $\rho > 1$
{: .prompt-info }

## Teste da integral
O cálculo integral pode ser usado para testar a convergência/divergência de séries compostas por sequências decrescentes de números positivos.

> **Teste da integral (Integral Test)**  
> Para uma função contínua e decrescente $f: [1,\infty) \rightarrow \mathbb{R}$ com $f(x)>0$ sempre, a série $\sum f(n)$ converge se e somente se a integral
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converge.
{: .prompt-info }

### Prova
Se a função $f(x)$ é contínua, decrescente e sempre positiva, então a desigualdade

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

é válida. Somando esta desigualdade termo a termo de $n=1$ até o termo geral, obtemos a desigualdade

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Agora, usando o [teste de comparação](#teste-de-comparação), obtemos o resultado desejado. $\blacksquare$

## Série alternada
Uma série $\sum a_n$ cujos termos gerais $a_n$ são não nulos e têm sinais alternados, ou seja, onde termos positivos e negativos aparecem alternadamente, é chamada de **série alternada**.

Para séries alternadas, o seguinte teorema descoberto pelo matemático alemão Gottfried Wilhelm Leibniz pode ser utilmente aplicado para testar a convergência/divergência.

> **Teste da série alternada (Alternating Series Test)**  
> Se
> 1. $a_n$ e $a_{n+1}$ têm sinais opostos para todo $n$,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$, e
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> então a série alternada $\sum a_n$ converge.
{: .prompt-info }

## Série absolutamente convergente
Se para uma série $\sum a_n$, a série $\sum \|a_n\|$ converge, dizemos que "a série $\sum a_n$ **converge absolutamente**".

Neste caso, o seguinte teorema é válido.

> **Teorema**  
> Uma série que converge absolutamente também converge.
{: .prompt-info }

> O inverso do teorema acima não é necessariamente verdadeiro.  
> Quando uma série converge, mas não converge absolutamente, dizemos que ela "**converge condicionalmente**".
{: .prompt-warning }

### Prova
Para um número real $a$, definimos

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Então, obtemos

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Como $0 \leq a^\pm \leq \|a\|$, pelo [teste de comparação](#teste-de-comparação), se a série $\sum \|a_n\|$ converge, as séries $\sum a_n^+$ e $\sum a_n^-$ também convergem, e portanto, pelas [propriedades básicas de séries convergentes](/posts/sequences-and-series/#propriedades-básicas-de-séries-convergentes),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

também converge. $\blacksquare$
