---
title: "Transformação linear, núcleo e imagem"
description: "Definimos transformação linear e estudamos os subespaços associados — núcleo (espaço nulo) e imagem —, suas dimensões (nullity e rank) e teoremas fundamentais com provas."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Pré-requisitos
- [Vetores e combinações lineares](/posts/vectors-and-linear-combinations/)
- [Espaços vetoriais, subespaços e matrizes](/posts/vector-spaces-subspaces-and-matrices/)
- [Dependência linear e independência linear, base e dimensão](posts/linear-dependence-and-independence-basis-and-dimension/)
- Função injetora, função sobrejetora

## Transformação linear

Uma função especial que preserva a estrutura de um espaço vetorial é chamada de transformação linear, conceito central que aparece com muita frequência em matemática pura, aplicada, ciências sociais, ciências naturais e engenharia.

> **Definição**  
> Sejam $\mathbb{V}$ e $\mathbb{W}$ espaços vetoriais sobre um corpo $F$. Diz-se que uma função $T:\mathbb{V}\to\mathbb{W}$ é uma **transformação linear (linear transformation)** se, para todos $\mathbf{x}, \mathbf{y}\in\mathbb{V}$ e $c\in F$, valem:
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = c\,T(\mathbf{x})$
{: .prompt-info }

Dizemos simplesmente que $T$ é **linear**. Uma transformação linear $T:\mathbb{V}\to\mathbb{W}$ satisfaz as quatro propriedades abaixo.

> 1. $T$ linear $\quad \Rightarrow \quad T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ linear $\quad \Leftrightarrow \quad T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ linear $\quad \Rightarrow \quad T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ linear $\quad \Leftrightarrow \quad T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> Ao provar que uma função é linear, costuma ser conveniente usar a propriedade 2.
{: .prompt-tip }

> A Álgebra Linear tem aplicações geométricas vastas e diversas porque muitas transformações geométricas importantes são lineares. Em particular, as três transformações centrais — **rotação**, **simetria** e **projeção** — são lineares.
{: .prompt-tip }

Duas transformações lineares aparecem especialmente com frequência.

> **Transformação identidade e transformação nula**  
> Para espaços vetoriais $\mathbb{V}, \mathbb{W}$ sobre $F$:
> - **Transformação identidade (identity transformation)**: $I\_\mathbb{V}:\mathbb{V}\to\mathbb{V}$ definida por $I\_\mathbb{V}(\mathbf{x})=\mathbf{x}$ para todo $\mathbf{x}\in\mathbb{V}$
> - **Transformação nula (zero transformation)**: $T\_0:\mathbb{V}\to\mathbb{W}$ definida por $T\_0(\mathbf{x})=\mathbf{0}$ para todo $\mathbf{x}\in\mathbb{V}$
{: .prompt-info }

Outros exemplos relevantes também são transformações lineares.

> **Exemplos de transformações lineares**  
> - Rotação
> - Simetria
> - Projeção
> - [Transposição](/posts/vector-spaces-subspaces-and-matrices/#matriz-transposta-matriz-simétrica-e-matriz-antissimétrica)
> - Derivada de função diferenciável
> - Integração de função contínua
{: .prompt-tip }

## Núcleo e imagem

### Definição de núcleo e imagem

> **Definição**  
> Dado $T:\mathbb{V}\to\mathbb{W}$ linear entre espaços vetoriais $\mathbb{V}, \mathbb{W}$:
> - **Núcleo (kernel)** ou **espaço nulo (null space)**: o conjunto dos vetores $\mathbf{x}\in\mathbb{V}$ tais que $T(\mathbf{x})=\mathbf{0}$; denotado por $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **Imagem (image)** ou **range**: o subconjunto de $\mathbb{W}$ formado pelos valores de $T$; denotado por $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** Para espaços vetoriais $\mathbb{V}, \mathbb{W}$, a identidade $I:\mathbb{V}\to\mathbb{V}$ e a transformação nula $T\_0:\mathbb{V}\to\mathbb{W}$ satisfazem:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T\_0) = \mathbb{V}$
> - $\mathrm{R}(T\_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

Será um tema recorrente: o núcleo e a imagem de uma transformação linear são [subespaços](/posts/vector-spaces-subspaces-and-matrices/#subespaços).

> **Teorema 1**  
> Se $T:\mathbb{V}\to\mathbb{W}$ é linear, então $\mathrm{N}(T)$ e $\mathrm{R}(T)$ são subespaços de $\mathbb{V}$ e $\mathbb{W}$, respectivamente.
>
> **Prova**  
> Denotemos os vetores nulos de $\mathbb{V}, \mathbb{W}$ por $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$.
>
> Como $T(\mathbf{0}\_\mathbb{V})=\mathbf{0}\_\mathbb{W}$, temos $\mathbf{0}\_\mathbb{V}\in \mathrm{N}(T)$. Além disso, para $\mathbf{x}, \mathbf{y}\in \mathrm{N}(T)$ e $c\in F$,
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [Como $\mathbf{0}_\mathbb{V} \in \mathrm{N}(T)$, $\mathbf{x} + \mathbf{y} \in \mathrm{N}(T)$ e $c\mathbf{x} \in \mathrm{N}(T)$, então $\mathrm{N}(T)$ é subespaço de $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#subespaços).
>
> De modo análogo, como $T(\mathbf{0}\_\mathbb{V})=\mathbf{0}\_\mathbb{W}$, temos $\mathbf{0}\_\mathbb{W}\in \mathrm{R}(T)$. Para quaisquer $\mathbf{x}, \mathbf{y}\in \mathrm{R}(T)$ e $c\in F$ (existem $\mathbf{v}, \mathbf{w}\in\mathbb{V}$ tais que $T(\mathbf{v})=\mathbf{x}$ e $T(\mathbf{w})=\mathbf{y}$), vale:
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [Como $\mathbf{0}_\mathbb{W}\in \mathrm{R}(T)$, $\mathbf{x} + \mathbf{y} \in \mathrm{R}(T)$ e $c\mathbf{x} \in \mathrm{R}(T)$, então $\mathrm{R}(T)$ é subespaço de $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#subespaços). $\blacksquare$
{: .prompt-info }

Além disso, dados $\mathbb{V}, \mathbb{W}$ e $T:\mathbb{V}\to\mathbb{W}$ lineares, conhecendo uma [base](/posts/linear-dependence-and-independence-basis-and-dimension/#base) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$, podemos obter um [conjunto gerador](/posts/vectors-and-linear-combinations/#geração) para $\mathrm{R}(T)$ como segue.

> **Teorema 2**  
> Sejam $\mathbb{V}, \mathbb{W}$ e $T:\mathbb{V}\to\mathbb{W}$ lineares, e $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ uma [base](/posts/linear-dependence-and-independence-basis-and-dimension/#base) de $\mathbb{V}$. Então
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Prova**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Como $\mathrm{R}(T)$ é subespaço, pelo **Teorema 2** de [Espaços vetoriais, subespaços e matrizes](/posts/vector-spaces-subspaces-and-matrices/#subespaços),
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> Além disso,
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Como $\beta$ é base de $\mathbb{V}$,
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(com } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> Como $T$ é linear,
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ Como simultaneamente $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ e $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$, conclui-se $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

Este teorema também vale quando a base $\beta$ é infinita.

### Teorema da dimensão

O núcleo e a imagem são subespaços muito importantes; por isso, suas [dimensões](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensão) recebem nomes específicos.

> Ditos $\mathbb{V}, \mathbb{W}$ e $T:\mathbb{V}\to\mathbb{W}$ lineares, suponha que $\mathrm{N}(T)$ e $\mathrm{R}(T)$ sejam finito-dimensionais.
> - **Dimensão do núcleo (nulidade, nullity)**: a dimensão de $\mathrm{N}(T)$, denotada por $\mathrm{nullity}(T)$
> - **Posto (rank)**: a dimensão de $\mathrm{R}(T)$, denotada por $\mathrm{rank}(T)$
{: .prompt-info }

Quanto maior a nulidade, menor o posto; e, reciprocamente, quanto maior o posto, menor a nulidade.

> **Teorema 3: Teorema da dimensão (dimension theorem)**  
> Se $T:\mathbb{V}\to\mathbb{W}$ é linear e $\mathbb{V}$ é finito-dimensional, então
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Prova

Seja $\dim(\mathbb{V}) = n$ e $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$, e seja $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ uma base de $\mathrm{N}(T)$.

Pelo **Corolário 6-1** de ["Dependência linear e independência linear, base e dimensão"](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensão-de-subespaços), podemos estender $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ a uma base $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$.

Mostraremos que $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ é uma base de $\mathrm{R}(T)$. Para $1 \leq i \leq k$, $T(\mathbf{v}_i)=0$; logo, pelo [**Teorema 2**](#definição-de-núcleo-e-imagem),

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Ou seja, $S$ gera $\mathrm{R}(T)$. Pelo **Corolário 5-2 do Teorema da troca** de [Dependência linear e independência linear, base e dimensão](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensão), basta provar que $S$ é linearmente independente para concluir que $S$ é base de $\mathrm{R}(T)$.

Se $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (com $b\_{k+1}, \dots, b\_n \in F$), como $T$ é linear,

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Portanto,

$$ \begin{align*}
&\exists c_1, \dots, c_k \in F \text{ tais que} \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

Como $\beta$ é base de $\mathbb{V}$, a única solução de $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ é

$$ c_1 = \cdots = c_k = b_{k+1} = \cdots = b_n = 0, $$

e daí

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Logo, $S$ é linearmente independente e é base de $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Transformações lineares e funções injetoras/sobrejetoras

Para transformações lineares, injeção e sobrejeção estão intimamente ligadas ao posto e à nulidade.

> **Teorema 4**  
> Para $T:\mathbb{V}\to\mathbb{W}$ linear,
>
> $$ T \text{ é injetora} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Teorema 5**  
> Se $\mathbb{V}$ e $\mathbb{W}$ são finito-dimensionais e têm a mesma dimensão, então, para $T:\mathbb{V}\to\mathbb{W}$ linear, as quatro afirmações são equivalentes:
> 1. $T$ é injetora.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ é sobrejetora.
{: .prompt-info }

Usando o [Teorema da dimensão](#teorema-da-dimensão), as [Propriedades 1 e 3 das transformações lineares](#transformação-linear) e o **Teorema 6** de ["Dependência linear e independência linear, base e dimensão"](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensão-de-subespaços), pode-se provar os Teoremas 4 e 5.

Estes dois teoremas são úteis para decidir se uma transformação linear é injetora ou sobrejetora.

> Para um espaço vetorial infinito-dimensional $\mathbb{V}$ e $T:\mathbb{V}\to\mathbb{V}$ linear, injeção e sobrejeção não são, em geral, equivalentes.
{: .prompt-warning }

Se uma transformação linear é injetora, o seguinte resultado pode ser útil, em certos casos, para testar a independência linear de um subconjunto dado.

> **Teorema 6**  
> Sejam $\mathbb{V}, \mathbb{W}$ espaços vetoriais e $T:\mathbb{V}\to\mathbb{W}$ linear injetora. Para um subconjunto $S\subseteq \mathbb{V}$, vale:
>
> $$ S \text{ é linearmente independente} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \} \text{ é linearmente independente.} $$
>
{: .prompt-info }

## Transformações lineares e base

Uma característica importante das transformações lineares é que seu comportamento fica determinado pela escolha de uma base.

> **Teorema 7**  
> Sejam $\mathbb{V}, \mathbb{W}$ espaços vetoriais sobre $F$, $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ uma base de $\mathbb{V}$ e $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$. Existe uma única transformação linear $T:\mathbb{V}\to\mathbb{W}$ tal que
>
> $$ T(\mathbf{v}_i) = \mathbf{w}_i \quad (i = 1, 2, \dots, n). $$
>
> **Prova**  
> Para $\mathbf{x}\in\mathbb{V}$, a representação por combinação linear na base é única:
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \quad (a_1, a_2, \dots, a_n \in F). $$
>
> Defina $T:\mathbb{V}\to\mathbb{W}$ por
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. $$
>
> i) Para $i=1,2,\dots,n$, $T(\mathbf{v}_i)=\mathbf{w}_i$.
>
> ii) Se $U:\mathbb{V}\to\mathbb{W}$ é outra transformação linear com $U(\mathbf{v}\_i)=\mathbf{w}\_i$ para $i=1,\dots,n$, então, para $\mathbf{x}=\sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$,
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}). $$
>
> $$ \therefore U = T. $$
>
> Pelos itens i) e ii), a única transformação linear com $T(\mathbf{v}\_i)=\mathbf{w}\_i$ para $i=1,\dots,n$ é
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. \quad \blacksquare $$
>
> **Corolário 7-1**  
> Se $\mathbb{V}, \mathbb{W}$ são espaços vetoriais e $\mathbb{V}$ possui uma base finita $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$, então duas transformações lineares $U, T:\mathbb{V}\to\mathbb{W}$ que satisfaçam $U(\mathbf{v}_i)=T(\mathbf{v}_i)$ para $i=1,\dots,n$ são iguais: $U=T$.  
> Isto é, <u>se coincidem nos valores da base, são a mesma transformação linear.</u>
{: .prompt-info }
