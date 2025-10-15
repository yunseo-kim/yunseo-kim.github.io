---
title: "Dependência linear e independência linear, base e dimensão"
description: "Revisão de dependência e independência linear e das noções de base e dimensão em espaços vetoriais: definições, teoremas essenciais, corolários e exemplos."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Pré-requisitos
- [Vetores e combinações lineares](/posts/vectors-and-linear-combinations/)
- [Espaços vetoriais, subespaços e matrizes](/posts/vector-spaces-subspaces-and-matrices/)

## Dependência linear e independência linear

Dado um [espaço vetorial](/posts/vector-spaces-subspaces-and-matrices/#espaço-vetorial) $\mathbb{V}$ e um [subespaço](/posts/vector-spaces-subspaces-and-matrices/#subespaços) $\mathbb{W}$, queremos encontrar um subconjunto finito mínimo $S$ que [gere](/posts/vectors-and-linear-combinations/#combinação-linear-de-vetores) $\mathbb{W}$.

Seja $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ tal que $\mathrm{span}(S) = \mathbb{W}$. Como decidir se existe um subconjunto próprio de $S$ que ainda gera $\mathbb{W}$? Isso equivale a verificar se algum vetor de $S$ pode ser escrito como [combinação linear](/posts/vectors-and-linear-combinations/#combinação-linear-de-vetores) dos demais. Por exemplo, uma condição necessária e suficiente para expressar $\mathbf{u}_4$ como combinação linear dos outros três é a existência de escalares $a_1, a_2, a_3$ que satisfaçam:

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

No entanto, montar e resolver um sistema linear assim para cada uma de $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ é trabalhoso. Em vez disso, reescrevamos:

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

Se algum vetor de $S$ for combinação linear dos outros, então existe uma representação do vetor nulo como combinação linear dos vetores de $S$ em que pelo menos um dos coeficientes $a_1, a_2, a_3, a_4$ é não nulo. A recíproca também é verdadeira: se existe uma representação do vetor nulo como combinação linear dos vetores de $S$ com algum coeficiente não nulo, então algum vetor de $S$ é combinação linear dos demais.

Generalizando, definimos a seguir **dependência linear** e **independência linear**.

> **Definição**  
> Para um subconjunto $S$ de um espaço vetorial $\mathbb{V}$, se existirem vetores distintos $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ e escalares $a_1, a_2, \dots, a_n$, não todos nulos, tais que $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$, dizemos que $S$ (e esses vetores) é um conjunto de vetores **linearmente dependentes**. Caso contrário, é um conjunto **linearmente independente**.
{: .prompt-info }

Para quaisquer vetores $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$, se $a_1 = a_2 = \cdots = a_n = 0$, então $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$. Chamamos isso de **representação trivial do vetor nulo**.

As três proposições abaixo são sempre verdadeiras em qualquer espaço vetorial. Em particular, a **Proposição 3** é muito útil para testar a independência linear de um conjunto finito.

> - **Proposição 1**: O conjunto vazio é linearmente independente. Para um conjunto ser linearmente dependente, ele não pode ser vazio.
> - **Proposição 2**: Um conjunto formado por um único vetor não nulo é linearmente independente.
> - **Proposição 3**: Um conjunto é linearmente independente se, e somente se, a única maneira de representar $\mathbf{0}$ como combinação linear dos vetores do conjunto é a representação trivial.
{: .prompt-info }

Também são importantes os seguintes resultados.

> **Teorema 1**  
> Seja $\mathbb{V}$ um espaço vetorial e $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Se $S_1$ é linearmente dependente, então $S_2$ também é linearmente dependente.
>
> **Corolário 1-1**  
> Seja $\mathbb{V}$ um espaço vetorial e $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Se $S_2$ é linearmente independente, então $S_1$ também é linearmente independente.
{: .prompt-info }

> **Teorema 2**  
> Seja $\mathbb{V}$ um espaço vetorial e $S$ um subconjunto linearmente independente. Para $\mathbf{v} \in \mathbb{V}$ com $\mathbf{v} \notin S$, uma condição necessária e suficiente para que $S \cup \\{\mathbf{v}\\}$ seja linearmente dependente é que $\mathbf{v} \in \mathrm{span}(S)$.
>
> Em outras palavras, **se nenhum subconjunto próprio de $S$ gera o mesmo espaço que $S$, então $S$ é linearmente independente.**
{: .prompt-info }

## Base e dimensão

### Base

Se $S$ é um conjunto gerador de $\mathbb{W}$ e é [linearmente independente](#dependência-linear-e-independência-linear), então todo vetor de $\mathbb{W}$ pode ser expresso como combinação linear de vetores de $S$, e essa expressão é única (**Teorema 3**). Assim, definimos um conjunto gerador linearmente independente como **base (basis)** do espaço.

> **Definição de base**  
> Para um espaço vetorial $\mathbb{V}$ e um subconjunto $\beta$, se $\beta$ é linearmente independente e gera $\mathbb{V}$, então $\beta$ é uma **base (basis)** de $\mathbb{V}$. Dizemos que os vetores de $\beta$ formam uma base de $\mathbb{V}$.
{: .prompt-info }

> $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ e $\emptyset$ é linearmente independente. Logo, o conjunto vazio é uma base do espaço nulo.
{: .prompt-tip }

Em particular, a seguinte base especial de $F^n$ é chamada de **base padrão (standard basis)** de $F^n$.

> **Definição de base padrão**  
> Para o espaço vetorial $F^n$, considere os vetores
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> O conjunto $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ é uma base de $F^n$, chamada **base padrão (standard basis)** de $F^n$.
{: .prompt-info }

> **Teorema 3**  
> Para um espaço vetorial $\mathbb{V}$ e vetores distintos $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$, o conjunto $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ é uma base de $\mathbb{V}$ se, e somente se, todo vetor $\mathbf{v} \in \mathbb{V}$ pode ser escrito de forma única como combinação linear de vetores de $\beta$. Ou seja, existem escalares únicos $(a_1, a_2, \dots, a_n)$ tais que
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

Pelo **Teorema 3**, quando vetores distintos $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ formam uma base de um espaço vetorial $\mathbb{V}$, então dentro desse espaço existe uma correspondência biunívoca entre vetores $\mathbf{v}$ e $n$-uplas escalares $(a_1, a_2, \dots, a_n)$. Veremos mais adiante, ao estudar **invertibilidade** e **isomorfismo**, que, nesse caso, $\mathbb{V}$ e $F^n$ são <u>essencialmente iguais</u>.

> **Teorema 4**  
> Se $S$ é um conjunto finito tal que $\mathrm{span}(S) = \mathbb{V}$, então algum subconjunto de $S$ é uma base de $\mathbb{V}$. Portanto, nesse caso, $\mathbb{V}$ admite uma base finita.
{: .prompt-info }

> Muitos espaços vetoriais satisfazem o **Teorema 4**, mas não todos. <u>Uma base pode ser infinita</u>.
{: .prompt-tip }

### Dimensão

> **Teorema 5: Teorema da troca (replacement theorem)**  
> Seja $G$ um conjunto com $n$ vetores tal que $\mathrm{span}(G) = \mathbb{V}$. Se $L \subseteq \mathbb{V}$ é um conjunto de $m$ vetores linearmente independentes, então $m \leq n$. Além disso, existe um subconjunto $H \subseteq G$ com $n-m$ vetores tal que $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

Disso seguem dois corolários muito importantes.

> **Corolário 5-1 do Teorema da troca**  
> Se um espaço vetorial $\mathbb{V}$ possui alguma base finita, então toda base de $\mathbb{V}$ é finita e todas têm o mesmo número de vetores.
{: .prompt-info }

Portanto, o número de vetores de uma base de $\mathbb{V}$ é uma propriedade intrínseca do espaço e é chamado de **dimensão**.

> **Definição de dimensão**  
> Um espaço vetorial que admite uma base finita é dito de **dimensão finita**; nesse caso, o número $n$ de elementos de uma base é a **dimensão** do espaço e é denotado por $\dim(\mathbb{V})$. Se não admite base finita, o espaço é de **dimensão infinita**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> A dimensão de um espaço vetorial pode variar conforme o corpo de escalares.
> - Sobre o corpo dos complexos $\mathbb{C}$, o espaço vetorial dos complexos tem dimensão $1$, com base $\\{1\\}$
> - Sobre o corpo dos reais $\mathbb{R}$, o mesmo espaço (considerado como espaço real) tem dimensão $2$, com base $\\{1,i\\}$
{: .prompt-tip }

Em um espaço vetorial finito-dimensional $\mathbb{V}$, qualquer subconjunto com mais do que $\dim(\mathbb{V})$ vetores nunca é linearmente independente.

> **Corolário 5-2 do Teorema da troca**  
> Seja $\mathbb{V}$ um espaço vetorial de dimensão $n$.
> 1. Todo conjunto gerador finito de $\mathbb{V}$ tem pelo menos $n$ vetores, e todo conjunto gerador com $n$ vetores é uma base de $\mathbb{V}$.
> 2. Todo subconjunto linearmente independente de $\mathbb{V}$ com $n$ vetores é uma base de $\mathbb{V}$.
> 3. Todo subconjunto linearmente independente de $\mathbb{V}$ pode ser estendido a uma base. Isto é, se $L \subseteq \mathbb{V}$ é linearmente independente, então existe uma base $\beta \supseteq L$ de $\mathbb{V}$.
{: .prompt-info }

### Dimensão de subespaços

> **Teorema 6**  
> Se $\mathbb{V}$ é finito-dimensional e $\mathbb{W}$ é um subespaço de $\mathbb{V}$, então $\mathbb{W}$ é finito-dimensional e $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$. Em particular, se $\dim(\mathbb{W}) = \dim(\mathbb{V})$, então $\mathbb{W} = \mathbb{V}$.
>
> **Corolário 6-1**  
> Para um subespaço $\mathbb{W}$ de um espaço vetorial finito-dimensional $\mathbb{V}$, toda base de $\mathbb{W}$ pode ser estendida a uma base de $\mathbb{V}$.
{: .prompt-info }

Pelo **Teorema 6**, as dimensões dos subespaços de $\mathbb{R}^3$ podem ser $0,1,2,3$.
- Dimensão 0: o espaço nulo $\\{\mathbf{0}\\}$ (apenas a origem)
- Dimensão 1: reta que passa pela origem ($\mathbf{0}$)
- Dimensão 2: plano que contém a origem ($\mathbf{0}$)
- Dimensão 3: todo o espaço euclidiano tridimensional
