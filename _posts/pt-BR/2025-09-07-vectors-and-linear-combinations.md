---
title: "Vetores e combinações lineares"
description: "O que é um vetor, as operações básicas (soma e multiplicação por escalar) e como entender combinações lineares. Introdução prática à Álgebra Linear."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Definição de vetor**
>   - **Vetor em sentido estrito (vetor euclidiano)**: grandeza física que possui magnitude e direção
>   - **Em sentido amplo, na Álgebra Linear**: elemento de um espaço vetorial
> - **Formas de representação de vetores**
>   - **Representação por setas**: a magnitude é o comprimento da seta e a direção é o sentido da seta. É intuitiva e fácil de visualizar, mas fica limitada para vetores em dimensão 4 ou superior e para vetores não euclidianos.
>   - **Representação por componentes**: fixa-se a cauda do vetor na origem do espaço de coordenadas e representa-se o vetor pelas coordenadas de sua ponta.
> - **Operações básicas com vetores**
>   - **Soma**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Multiplicação por escalar**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Combinação linear de vetores**
>   - Dado um número finito de vetores $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ e escalares $a_1, a_2, \dots, a_n$, um vetor $\mathbf{v}$ da forma $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$ é chamado de **combinação linear** de $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$
>   - Nesse caso, $a_1, a_2, \dots, a_n$ são os **coeficientes** dessa combinação linear
{: .prompt-info }

## Pré-requisitos
- Plano/espaco de coordenadas
- Corpo

## O que é um vetor?

### Vetor em sentido estrito: vetor euclidiano

> Muitas grandezas físicas como força, velocidade e aceleração possuem não apenas magnitude, mas também direção. Uma grandeza que possui magnitude e direção é chamada de **vetor**.
{: .prompt-info }

Essa é a definição de vetor adotada em mecânica e na matemática do ensino médio. Esse vetor, baseado em uma intuição geométrica de “segmento orientado com magnitude e direção”, é chamado mais precisamente de **vetor euclidiano (Euclidean vector)**.

### Vetor em sentido amplo: elemento de um espaço vetorial

Na Álgebra Linear, adota-se uma noção mais ampla e abstrata de vetor, como uma estrutura algébrica, definida assim:

> **Definição**  
> Um **espaço vetorial** (ou **espaço linear**) $\mathbb{V}$ sobre um corpo $F$ é um conjunto equipado com duas operações, **soma** e **multiplicação por escalar**, que satisfazem as 8 condições abaixo. Os elementos de $F$ são chamados de **escalares**, e os elementos de $\mathbb{V}$ são chamados de **vetores**.
>
> - **Soma**: para quaisquer $\mathbf{x}, \mathbf{y} \in \mathbb{V}$, existe um único elemento $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. Chamamos $\mathbf{x} + \mathbf{y}$ de **soma** de $\mathbf{x}$ e $\mathbf{y}$.
> - **Multiplicação por escalar**: para cada $a \in F$ e $\mathbf{x} \in \mathbb{V}$, existe um único elemento $a\mathbf{x} \in \mathbb{V}$. Chamamos $a\mathbf{x}$ de **múltiplo escalar** de $\mathbf{x}$.
>
> 1. Para todos $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (comutatividade da adição)
> 2. Para todos $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$, $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (associatividade da adição)
> 3. Existe $\mathbf{0} \in \mathbb{V}$ tal que, para todo $\mathbf{x} \in \mathbb{V}$, $\mathbf{x} + \mathbf{0} = \mathbf{x}$. (vetor zero, elemento neutro da adição)
> 4. Para cada $\mathbf{x} \in \mathbb{V}$, existe $\mathbf{y} \in \mathbb{V}$ tal que $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (inverso aditivo)
> 5. Para todo $\mathbf{x} \in \mathbb{V}$, $1\mathbf{x} = \mathbf{x}$. (identidade multiplicativa)
> 6. Para todos $a,b \in F$ e todo $\mathbf{x} \in \mathbb{V}$, $(ab)\mathbf{x} = a(b\mathbf{x})$. (associatividade da multiplicação por escalar)
> 7. Para todo $a \in F$ e todos $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (distributividade da multiplicação por escalar sobre a adição 1)
> 8. Para todos $a,b \in F$ e todo $\mathbf{x} \in \mathbb{V}$, $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (distributividade da multiplicação por escalar sobre a adição 2)
{: .prompt-info }

Essa definição de vetor na Álgebra Linear é mais geral e inclui o [vetor euclidiano](#vetor-em-sentido-estrito-vetor-euclidiano). Pode-se verificar que o [vetor euclidiano](#vetor-em-sentido-estrito-vetor-euclidiano) satisfaz as 8 propriedades acima.

A origem e o desenvolvimento do conceito de vetor estão intimamente ligados a problemas práticos levantados pela Física, como descrever quantitativamente força, movimento, rotação e campos. A necessidade de expressar fenômenos naturais de forma matemática levou primeiro à noção de [vetor euclidiano](#vetor-em-sentido-estrito-vetor-euclidiano); depois, a Matemática generalizou e formalizou essas ideias, estabelecendo estruturas como espaço vetorial, produto interno e produto externo, culminando na definição atual de vetor. Em suma, o vetor é um conceito demandado pela Física e formalizado pela Matemática, fruto de um desenvolvimento interdisciplinar.

Os [vetores euclidianos](#vetor-em-sentido-estrito-vetor-euclidiano) da mecânica clássica podem ser expressos em uma [estrutura mais geral](#vetor-em-sentido-amplo-elemento-de-um-espaco-vetorial), e, na Física contemporânea, além dos [vetores euclidianos](#vetor-em-sentido-estrito-vetor-euclidiano), empregam-se ativamente conceitos mais abstratos definidos na Matemática, como espaços vetoriais e espaços de funções, atribuindo-lhes significado físico. Portanto, não é adequado entender as duas definições de vetor simplesmente como “definição física” e “definição matemática”.

Voltaremos ao estudo de espaços vetoriais mais adiante; por ora, vamos focar no vetor em sentido estrito, o vetor euclidiano, que pode ser representado geometricamente em um espaço de coordenadas. Ver exemplos intuitivos de vetores euclidianos ajuda quando generalizarmos para outros tipos de vetores.

## Representação de vetores
### Representação por setas

É a forma de representação mais comum e geométrica. A magnitude do vetor é o comprimento da seta, e a direção do vetor é o sentido da seta.

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Fonte da imagem*
> - Autor: usuário da Wikipédia [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

Embora intuitiva, essa representação tem limitações claras para vetores de alta dimensão (4D ou mais). Além disso, mais adiante lidaremos com vetores não euclidianos, cuja representação geométrica é difícil; por isso, é útil se familiarizar com a representação por componentes descrita a seguir.

### Representação por componentes

Independentemente da posição do vetor, se sua magnitude e direção forem as mesmas, consideramo-lo o mesmo vetor. Assim, dado um espaço de coordenadas, fixando a cauda do vetor na origem desse espaço, <u>um vetor em dimensão $n$ corresponde a um ponto arbitrário no espaço $n$-dimensional</u>; nesse caso, podemos representar o vetor pelas coordenadas de sua ponta. Essa forma de representação é chamada de **representação por componentes**.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ or } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Fonte da imagem*
> - Autor: usuário da Wikimedia [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Operações básicas com vetores

As operações básicas são duas: **soma** e **multiplicação por escalar**. Toda operação com vetores pode ser expressa como combinação dessas duas.

### Soma de vetores

A soma de dois vetores é um vetor, e seus componentes são as somas componente a componente dos vetores dados.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Multiplicação por escalar

Podemos ampliar ou reduzir a magnitude de um vetor multiplicando-o por um escalar. O resultado é igual a multiplicar cada componente pelo mesmo escalar.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Fonte da imagem*
> - Autor: usuário da Wikipédia [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Combinação linear de vetores

Assim como o Cálculo parte de números $x$ e funções $f(x)$, a Álgebra Linear parte de vetores $\mathbf{v}, \mathbf{w}, \dots$ e de combinações lineares $c\mathbf{v} + d\mathbf{w} + \cdots$. Toda combinação linear de vetores é composta pelas duas operações básicas acima, [soma](#soma-de-vetores) e [multiplicação por escalar](#multiplicacao-por-escalar).

> Dado um número finito de vetores $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ e escalares $a_1, a_2, \dots, a_n$, um vetor $\mathbf{v}$ é chamado de **combinação linear** de $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ se
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> Nesse caso, $a_1, a_2, \dots, a_n$ são os **coeficientes** dessa combinação linear.
{: .prompt-info }

Por que a combinação linear é importante? Considere a situação em que **$n$ vetores em um espaço de dimensão $m$ compõem as $n$ colunas de uma matriz $m \times n$**.

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

Os pontos essenciais são dois:

1. **Expresse todas as combinações lineares possíveis $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n$. O que elas formam?**
2. Dado um vetor de saída desejado $Ax = b$, **encontre os números $x_1, x_2, \dots, x_n$** que o produzem.

Responderemos ao segundo ponto depois; por enquanto, foquemos no primeiro. Para simplificar, considere o caso de 2 vetores ($n=2$) em 2 dimensões ($m=2$), distintos de $\mathbf{0}$.

### Combinação linear $c\mathbf{v} + d\mathbf{w}$

Um vetor $\mathbf{v}$ em 2D tem dois componentes. Para todo escalar $c$, <u>o vetor $c\mathbf{v}$ é paralelo a $\mathbf{v}$ e forma, no plano $xy$, uma reta infinita que passa pela origem.</u>

Se um segundo vetor $\mathbf{w}$ não está sobre essa reta (isto é, se $\mathbf{v}$ e $\mathbf{w}$ não são paralelos), então $d\mathbf{w}$ forma uma segunda reta. Combinando essas duas retas, vemos que **a combinação linear $c\mathbf{v} + d\mathbf{w}$ preenche um plano que contém a origem**.

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Fonte da imagem*
> - Autor: usuário da Wikimedia [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - Licença: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

Assim, as combinações lineares de vetores formam um espaço vetorial; a isso chamamos de **geração** do espaço (span).

> **Definição**  
> Dado um subconjunto não vazio $S$ de um espaço vetorial $\mathbb{V}$, o conjunto de todas as combinações lineares feitas com vetores de $S$ é chamado de **espaço gerado (span)** de $S$ e é denotado por $\mathrm{span}(S)$. Define-se $\mathrm{span}(\emptyset) = \{0\}$.
{: .prompt-info }

> **Definição**  
> Para um subconjunto $S$ de $\mathbb{V}$, se $\mathrm{span}(S) = \mathbb{V}$, então diz-se que $S$ **gera** $\mathbb{V}$ (generate, span).
{: .prompt-info }

Ainda não estudamos conceitos como subespaço e base, mas ter em mente este exemplo ajudará a entender a noção de espaço vetorial mais adiante.
