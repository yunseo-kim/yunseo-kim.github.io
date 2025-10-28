---
title: "Espaços vetoriais, subespaços e matrizes"
description: "Definições de espaço vetorial e subespaço, com exemplos: espaços de matrizes e de funções. Destaque para matrizes simétricas, antissimétricas, triangulares e diagonais."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Matriz**
>   - O elemento da linha $i$ e coluna $j$ da matriz $A$ é denotado por $A\_{ij}$ ou $a\_{ij}$
>   - **Elemento diagonal**: o elemento $a\_{ij}$ com $i=j$
>   - Os elementos $a\_{i1}, a\_{i2}, \dots, a\_{in}$ formam a **linha** $i$-ésima da matriz
>     - Cada linha da matriz pode ser vista como um vetor em $F^n$
>     - Além disso, um vetor linha de $F^n$ pode ser visto como outra matriz $1 \times n$
>   - Os elementos $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ formam a **coluna** $j$-ésima da matriz
>     - Cada coluna da matriz pode ser vista como um vetor em $F^m$
>     - Além disso, um vetor coluna de $F^m$ pode ser visto como outra matriz $m \times 1$
>   - **Matriz nula**: matriz cujos elementos são todos $0$, denotada por $O$
>   - **Matriz quadrada**: matriz com o mesmo número de linhas e colunas
>   - Para duas matrizes $m \times n$ $A, B$, se para todos $1 \leq i \leq m$, $1 \leq j \leq n$ vale $A\_{ij} = B\_{ij}$ (isto é, todos os elementos correspondentes coincidem), então dizemos que as matrizes são **iguais** ($A=B$)
>   - **Matriz transposta**: para $A$ de tamanho $m \times n$, a transposta $A^T$ é a matriz $n \times m$ obtida trocando linhas por colunas
>   - **Matriz simétrica**: matriz quadrada $A$ com $A^T = A$
>   - **Matriz antissimétrica**: matriz quadrada $B$ com $B^T = -B$
>   - **Matriz triangular**
>     - **Triangular superior**: matriz cujos elementos abaixo da diagonal são todos $0$ (isto é, $i>j \Rightarrow A\_{ij}=0$), geralmente denotada por $U$
>     - **Triangular inferior**: matriz cujos elementos acima da diagonal são todos $0$ (isto é, $i<j \Rightarrow A\_{ij}=0$), geralmente denotada por $L$
>   - **Matriz diagonal**: matriz quadrada em que todos os elementos fora da diagonal são $0$ (isto é, $i \neq j \Rightarrow M\_{ij}=0$ numa $n \times n$), geralmente denotada por $D$
> - Espaços vetoriais representativos
>   - **$n$-uplas $F^n$**:
>     - Conjunto de todas as $n$-uplas com componentes em um corpo $F$
>     - Denotado por $F^n$, é um espaço vetorial sobre $F$
>   - **Espaço de matrizes**:
>     - Conjunto de todas as matrizes $m \times n$ com elementos em $F$
>     - Denotado por $\mathcal{M}\_{m \times n}(F)$, é um espaço vetorial
>   - **Espaço de funções**:
>     - Para um conjunto não vazio $S$ sobre um corpo $F$, o conjunto de todas as funções de $S$ em $F$
>     - Denotado por $\mathcal{F}(S,F)$, é um espaço vetorial
> - **Subespaço**
>   - Um subconjunto $\mathbb{W}$ de um espaço vetorial $\mathbb{V}$ sobre $F$ é um **subespaço** de $\mathbb{V}$ se, com as mesmas operações de soma e multiplicação por escalar definidas em $\mathbb{V}$, ele próprio for um espaço vetorial sobre $F$
>   - Para todo espaço vetorial $\mathbb{V}$, o próprio $\mathbb{V}$ e $\\{0\\}$ são subespaços; em particular, $\\{0\\}$ é o **subespaço nulo**
>   - Um subconjunto é subespaço se contiver o vetor nulo e for fechado para [combinação linear](/posts/vectors-and-linear-combinations/#combinação-linear-de-vetores) (isto é, se $\mathrm{span}(\mathbb{W})=\mathbb{W}$)
{: .prompt-info }

## Prerequisites
- [Vetores e combinações lineares](/posts/vectors-and-linear-combinations/)

## Espaço vetorial

Como vimos brevemente em [Vetores e combinações lineares](/posts/vectors-and-linear-combinations/#vetor-em-sentido-amplo-elemento-de-um-espaço-vetorial), a definição algébrica de vetor e de espaço vetorial é a seguinte.

> **Definição**  
> Um **espaço vetorial** (ou **espaço linear**) $\mathbb{V}$ sobre um corpo $F$ é um conjunto munido de duas operações, **soma** e **multiplicação por escalar**, que satisfazem as 8 condições abaixo. Os elementos de $F$ são chamados de **escalares**, e os de $\mathbb{V}$, de **vetores**.
>
> - **Soma**: para quaisquer $\mathbf{x}, \mathbf{y} \in \mathbb{V}$, existe um único elemento $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. Chamamos $\mathbf{x} + \mathbf{y}$ de **soma** de $\mathbf{x}$ e $\mathbf{y}$.
> - **Multiplicação por escalar**: para cada $a \in F$ e $\mathbf{x} \in \mathbb{V}$, existe um único elemento $a\mathbf{x} \in \mathbb{V}$. Chamamos $a\mathbf{x}$ de **múltiplo escalar** de $\mathbf{x}$.
>
> 1. Para todos $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (comutatividade da adição)
> 2. Para todos $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$, $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (associatividade da adição)
> 3. Existe $\mathbf{0} \in \mathbb{V}$ tal que, para todo $\mathbf{x} \in \mathbb{V}$, $\mathbf{x} + \mathbf{0} = \mathbf{x}$. (vetor nulo, elemento neutro da adição)
> 4. Para cada $\mathbf{x} \in \mathbb{V}$, existe $\mathbf{y} \in \mathbb{V}$ tal que $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (inverso aditivo)
> 5. Para todo $\mathbf{x} \in \mathbb{V}$, $1\mathbf{x} = \mathbf{x}$. (identidade multiplicativa)
> 6. Para todos $a,b \in F$ e todo $\mathbf{x} \in \mathbb{V}$, $(ab)\mathbf{x} = a(b\mathbf{x})$. (associatividade da multiplicação por escalar)
> 7. Para todo $a \in F$ e todos $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (distributividade da multiplicação por escalar sobre a adição 1)
> 8. Para todos $a,b \in F$ e todo $\mathbf{x} \in \mathbb{V}$, $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (distributividade da multiplicação por escalar sobre a adição 2)
{: .prompt-info }

Mais precisamente, deveríamos escrever “$\mathbb{V}$, espaço vetorial sobre $F$”, mas, ao tratar de espaços vetoriais, o corpo não é o foco principal; assim, quando não houver risco de ambiguidade, omitimos $F$ e escrevemos apenas “espaço vetorial $\mathbb{V}$”.

### Espaço de matrizes

#### Vetores linha e vetores coluna

Denotamos por $F^n$ o conjunto de todas as $n$-uplas com componentes em $F$. Para $u = (a_1, a_2, \dots, a_n) \in F^n$ e $v = (b_1, b_2, \dots, b_n) \in F^n$, definindo a soma e a multiplicação por escalar como abaixo, $F^n$ é um espaço vetorial sobre $F$.

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

Ao escrever um vetor de $F^n$ isoladamente, costuma-se representá-lo não como **vetor linha** $(a_1, a_2, \dots, a_n)$, mas como **vetor coluna**

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

> Como a notação em coluna ocupa mais espaço, às vezes usa-se a [transposição](#matriz-transposta-matriz-simétrica-e-matriz-antissimétrica) e escreve-se $(a_1, a_2, \dots, a_n)^T$.
{: .prompt-tip }

#### Matrizes e espaço de matrizes

Por sua vez, uma **matriz** $m \times n$ com elementos em $F$ é um arranjo retangular como abaixo, denotado por letras maiúsculas em itálico ($A, B, C$, etc.).

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- O elemento da linha $i$ e coluna $j$ da matriz $A$ é denotado por $A\_{ij}$ ou $a\_{ij}$.
- Cada $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) pertence a $F$.
- O elemento $a\_{ij}$ com $i=j$ é chamado de **elemento diagonal** da matriz.
- Os elementos $a\_{i1}, a\_{i2}, \dots, a\_{in}$ formam a **linha** $i$-ésima. Cada linha pode ser vista como um vetor de $F^n$ e, além disso, um vetor linha de $F^n$ pode ser visto como outra matriz $1 \times n$.
- Os elementos $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ formam a **coluna** $j$-ésima. Cada coluna pode ser vista como um vetor de $F^m$ e, além disso, um vetor coluna de $F^m$ pode ser visto como outra matriz $m \times 1$.
- A **matriz nula** $m \times n$ é aquela em que todos os elementos são $0$, denotada por $O$.
- Uma matriz é **quadrada** quando tem o mesmo número de linhas e colunas.
- Para duas matrizes $m \times n$ $A, B$, se para todos $1 \leq i \leq m$, $1 \leq j \leq n$ vale $A\_{ij} = B\_{ij}$ (isto é, todos os elementos correspondentes coincidem), definimos que as duas matrizes são **iguais** ($A=B$).

Denotamos por $\mathcal{M}\_{m \times n}(F)$ o conjunto de todas as matrizes $m \times n$ com elementos em $F$. Para $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ e $c \in F$, definindo a soma e a multiplicação por escalar como abaixo, $\mathcal{M}\_{m \times n}(F)$ é um espaço vetorial, chamado **espaço de matrizes**.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(onde }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

Trata-se de uma extensão natural das operações definidas em $F^n$ e $F^m$.

### Espaço de funções

Para um conjunto não vazio $S$ sobre um corpo $F$, $\mathcal{F}(S,F)$ é o conjunto de todas as funções de $S$ em $F$. Dizemos que duas funções $f, g \in \mathcal{F}(S,F)$ são **iguais** ($f=g$) se, para todo $s \in S$, $f(s) = g(s)$.

Para $f,g \in \mathcal{F}(S,F)$, $c \in F$, $s \in S$, definindo a soma e a multiplicação por escalar como abaixo, $\mathcal{F}(S,F)$ é um espaço vetorial, chamado **espaço de funções**.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## Subespaços

> **Definição**  
> Um subconjunto $\mathbb{W}$ de um espaço vetorial $\mathbb{V}$ sobre $F$ é chamado de **subespaço** de $\mathbb{V}$ se, com as mesmas operações de soma e multiplicação por escalar definidas em $\mathbb{V}$, ele próprio for um espaço vetorial sobre $F$.
{: .prompt-info }

Para todo espaço vetorial $\mathbb{V}$, o próprio $\mathbb{V}$ e $\\{0\\}$ são subespaços; em particular, $\\{0\\}$ é o **subespaço nulo**.

Podemos verificar se um subconjunto é subespaço usando o seguinte teorema.

> **Teorema 1**  
> Para um espaço vetorial $\mathbb{V}$ e um subconjunto $\mathbb{W}$, $\mathbb{W}$ é um subespaço de $\mathbb{V}$ se, e somente se, satisfizer as 3 condições abaixo. As operações são as mesmas definidas em $\mathbb{V}$.
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> Em resumo, se contém o vetor nulo e é fechado para [combinação linear](/posts/vectors-and-linear-combinations/#combinação-linear-de-vetores) (isto é, se $\mathrm{span}(\mathbb{W})=\mathbb{W}$), então é um subespaço.
{: .prompt-info }

Além disso, valem os seguintes resultados.

> **Teorema 2**  
> - Para qualquer subconjunto $S$ de um espaço vetorial $\mathbb{V}$, o espaço gerado $\mathrm{span}(S)$ é um subespaço de $\mathbb{V}$ que contém $S$.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Todo subespaço $\mathbb{W}$ de $\mathbb{V}$ que contenha $S$ contém necessariamente o espaço gerado por $S$.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Teorema 3**  
> Para subespaços de um espaço vetorial $\mathbb{V}$, a interseção arbitrária desses subespaços também é um subespaço de $\mathbb{V}$.
{: .prompt-info }

### Matriz transposta, matriz simétrica e matriz antissimétrica

Para uma matriz $m \times n$ $A$, a **matriz transposta** $A^T$ é a matriz $n \times m$ obtida trocando-se as linhas pelas colunas de $A$.

$$ (A^T)_{ij} = A_{ji} $$

$$ \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}^T
= \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 
\end{pmatrix} $$

Uma matriz $A$ com $A^T = A$ é chamada de **matriz simétrica**; uma matriz $B$ com $B^T = -B$ é chamada de **matriz antissimétrica**. Matrizes simétricas e antissimétricas devem ser, necessariamente, quadradas.

Seja $\mathbb{W}\_1$ o conjunto de todas as matrizes simétricas em $\mathcal{M}\_{n \times n}(F)$ e $\mathbb{W}\_2$ o conjunto de todas as matrizes antissimétricas em $\mathcal{M}\_{n \times n}(F)$. Então $\mathbb{W}\_1$ e $\mathbb{W}\_2$ são subespaços de $\mathcal{M}\_{n \times n}(F)$; isto é, são fechados para soma e multiplicação por escalar.

### Matrizes triangulares e matrizes diagonais

Esses dois tipos de matrizes também são especialmente importantes. 

Primeiro, chamamos de **matrizes triangulares** os dois tipos a seguir.
- **Triangular superior**: matriz em que todos os elementos abaixo da diagonal são $0$ (isto é, $i>j \Rightarrow A\_{ij}=0$), usualmente denotada por $U$
- **Triangular inferior**: matriz em que todos os elementos acima da diagonal são $0$ (isto é, $i<j \Rightarrow A\_{ij}=0$), usualmente denotada por $L$

Uma matriz quadrada em que todos os elementos fora da diagonal são $0$, isto é, uma $n \times n$ com $i \neq j \Rightarrow M\_{ij}=0$, é chamada de **matriz diagonal** e geralmente é denotada por $D$. Uma matriz diagonal é simultaneamente triangular superior e triangular inferior.

Os conjuntos das matrizes triangulares superiores, das triangulares inferiores e das diagonais são todos subespaços de $\mathcal{M}\_{m \times n}(F)$.
