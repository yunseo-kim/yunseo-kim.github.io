---
title: "Espacios vectoriales, subespacios y matrices"
description: "Definimos espacios vectoriales y subespacios con ejemplos (F^n, espacios de matrices y de funciones). En matrices: simétricas, antisimétricas, triangulares y diagonales como subespacios."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Matriz**
>   - El elemento de la fila $i$ y columna $j$ de una matriz $A$ se denota por $A\_{ij}$ o $a\_{ij}$
>   - **Entrada diagonal**: el elemento $a\_{ij}$ con $i=j$
>   - Los elementos $a\_{i1}, a\_{i2}, \dots, a\_{in}$ forman la **fila** $i$-ésima de la matriz
>     - Cada fila de una matriz puede verse como un vector de $F^n$
>     - A su vez, un vector fila de $F^n$ puede representarse como otra matriz de tamaño $1 \times n$
>   - Los elementos $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ forman la **columna** $j$-ésima de la matriz
>     - Cada columna de una matriz puede verse como un vector de $F^m$
>     - A su vez, un vector columna de $F^m$ puede representarse como otra matriz de tamaño $m \times 1$
>   - **Matriz cero**: matriz cuyas entradas son todas $0$, se denota por $O$
>   - **Matriz cuadrada**: matriz con igual número de filas y de columnas
>   - Dadas dos matrices $m \times n$ $A, B$, si para todo $1 \leq i \leq m$, $1 \leq j \leq n$ se cumple $A\_{ij} = B\_{ij}$ (es decir, todas las entradas correspondientes coinciden), definimos que las dos matrices son **iguales** ($A=B$)
>   - **Matriz traspuesta**: para una matriz $m \times n$ $A$, la matriz $n \times m$ $A^T$ que se obtiene intercambiando filas y columnas de $A$
>   - **Matriz simétrica**: matriz cuadrada $A$ tal que $A^T = A$
>   - **Matriz antisimétrica**: matriz cuadrada $B$ tal que $B^T = -B$
>   - **Matriz triangular**
>     - **Triangular superior**: matriz cuyas entradas por debajo de la diagonal son $0$ (esto es, $i>j \Rightarrow A\_{ij}=0$), suele denotarse por $U$
>     - **Triangular inferior**: matriz cuyas entradas por encima de la diagonal son $0$ (esto es, $i<j \Rightarrow A\_{ij}=0$), suele denotarse por $L$
>   - **Matriz diagonal**: matriz cuadrada $n \times n$ en la que todas las entradas fuera de la diagonal son $0$ (esto es, $i \neq j \Rightarrow M\_{ij}=0$), suele denotarse por $D$
> - Espacios vectoriales representativos
>   - **$n$-tuplas $F^n$**:
>     - Conjunto de todas las $n$-tuplas con entradas en un cuerpo $F$
>     - Se denota $F^n$ y es un espacio vectorial sobre $F$
>   - **Espacio de matrices**:
>     - Conjunto de todas las matrices $m \times n$ con entradas en el cuerpo $F$
>     - Se denota $\mathcal{M}\_{m \times n}(F)$ y es un espacio vectorial
>   - **Espacio de funciones**:
>     - Para un conjunto no vacío $S$ y un cuerpo $F$, el conjunto de todas las funciones de $S$ en $F$
>     - Se denota $\mathcal{F}(S,F)$ y es un espacio vectorial
> - **Subespacio**
>   - Un subconjunto $\mathbb{W}$ de un $F$-espacio vectorial $\mathbb{V}$ es un **subespacio** de $\mathbb{V}$ si, con las mismas operaciones de suma y multiplicación por escalar definidas en $\mathbb{V}$, $\mathbb{W}$ es también un $F$-espacio vectorial
>   - Para todo espacio vectorial $\mathbb{V}$, $\mathbb{V}$ mismo y $\\{0\\}$ son subespacios; en particular, a $\\{0\\}$ se le llama **subespacio cero**
>   - Un subconjunto de un espacio vectorial que contiene el vector cero y es cerrado bajo [combinación lineal](/posts/vectors-and-linear-combinations/#combinación-lineal-de-vectores) ($\mathrm{span}(\mathbb{W})=\mathbb{W}$) es un subespacio
{: .prompt-info }

## Prerequisites
- [Vectores y combinaciones lineales](/posts/vectors-and-linear-combinations/)

## Espacios vectoriales

Como ya vimos brevemente en [Vectores y combinaciones lineales](/posts/vectors-and-linear-combinations/#sentido-amplio-elemento-de-un-espacio-vectorial), la definición algebraica de vector y de espacio vectorial es la siguiente.

> **Definición**  
> Un **espacio vectorial (vector space)** o **espacio lineal (linear space)** $\mathbb{V}$ sobre un cuerpo $F$ es un conjunto provisto de dos operaciones, **suma** y **multiplicación por un escalar**, que satisfacen las siguientes 8 condiciones. A los elementos de $F$ se les llama **escalares (scalar)** y a los de $\mathbb{V}$, **vectores (vector)**.
>
> - **Suma**: para cualesquiera $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ existe un único elemento $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. A $\mathbf{x} + \mathbf{y}$ se le llama la **suma** de $\mathbf{x}$ e $\mathbf{y}$.
> - **Multiplicación por un escalar**: para cada $a \in F$ y $\mathbf{x} \in \mathbb{V}$ existe un único elemento $a\mathbf{x} \in \mathbb{V}$. A $a\mathbf{x}$ se le llama un **múltiplo escalar (scalar multiple)** de $\mathbf{x}$.
>
> 1. Para todo $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (conmutatividad de la suma)
> 2. Para todo $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$, $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (asociatividad de la suma)
> 3. Para todo $\mathbf{x} \in \mathbb{V}$, existe $\mathbf{0} \in \mathbb{V}$ tal que $\mathbf{x} + \mathbf{0} = \mathbf{x}$. (vector cero, elemento neutro de la suma)
> 4. Para cada $\mathbf{x} \in \mathbb{V}$, existe $\mathbf{y} \in \mathbb{V}$ tal que $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (inverso aditivo)
> 5. Para cada $\mathbf{x} \in \mathbb{V}$, $1\mathbf{x} = \mathbf{x}$. (elemento neutro de la multiplicación)
> 6. Para todo $a,b \in F$ y todo $\mathbf{x} \in \mathbb{V}$, $(ab)\mathbf{x} = a(b\mathbf{x})$. (asociatividad de la multiplicación por escalar)
> 7. Para todo $a \in F$ y todo $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (distributividad del escalar respecto de la suma 1)
> 8. Para todo $a,b \in F$ y todo $\mathbf{x} \in \mathbb{V}$, $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (distributividad del escalar respecto de la suma 2)
{: .prompt-info }

Aunque estrictamente debería escribirse “$F$-espacio vectorial $\mathbb{V}$”, al tratar espacios vectoriales el cuerpo suele no ser el foco principal; por tanto, si no hay riesgo de confusión, omitimos $F$ y escribimos simplemente “espacio vectorial $\mathbb{V}$”.

### Espacio de matrices

#### Vectores fila y columna

Denotamos por $F^n$ el conjunto de todas las $n$-tuplas con entradas en el cuerpo $F$. Dados $u = (a_1, a_2, \dots, a_n) \in F^n$ y $v = (b_1, b_2, \dots, b_n) \in F^n$, si definimos la suma y el producto por escalar como sigue, $F^n$ es un $F$-espacio vectorial.

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

Cuando se escribe un vector de $F^n$ de forma aislada, suele representarse más como **vector columna** que como **vector fila** $(a_1, a_2, \dots, a_n)$:

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

> No obstante, esta notación como columna ocupa más espacio, por lo que a veces se recurre a la [traspuesta](#matriz-traspuesta-simétrica-y-antisimétrica) y se escribe $(a_1, a_2, \dots, a_n)^T$.
{: .prompt-tip }

#### Matrices y espacio de matrices

Por otra parte, una **matriz** $m \times n$ con entradas en $F$ es un arreglo rectangular como el siguiente, y se denota con letras mayúsculas en cursiva ($A, B, C$, etc.):

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- La entrada en la fila $i$ y columna $j$ de una matriz $A$ se denota por $A\_{ij}$ o $a\_{ij}$.
- Cada $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) pertenece a $F$.
- A la entrada $a\_{ij}$ con $i=j$ se le llama **entrada diagonal** de la matriz.
- Los elementos $a\_{i1}, a\_{i2}, \dots, a\_{in}$ constituyen la **fila** $i$-ésima. Cada fila puede verse como un vector de $F^n$ y, más aún, un vector fila de $F^n$ puede verse como otra matriz $1 \times n$.
- Los elementos $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ constituyen la **columna** $j$-ésima. Cada columna puede verse como un vector de $F^m$ y, más aún, un vector columna de $F^m$ puede verse como otra matriz $m \times 1$.
- Una matriz $m \times n$ cuyas entradas son todas $0$ se llama **matriz cero** y se denota por $O$.
- Una matriz con el mismo número de filas y columnas se llama **matriz cuadrada**.
- Dadas dos matrices $m \times n$ $A, B$, si para todo $1 \leq i \leq m$, $1 \leq j \leq n$ se cumple $A\_{ij} = B\_{ij}$ (es decir, todas las entradas correspondientes coinciden), definimos que $A$ y $B$ son **iguales** ($A=B$).

Denotamos por $\mathcal{M}\_{m \times n}(F)$ el conjunto de todas las matrices $m \times n$ con entradas en el cuerpo $F$. Para $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ y $c \in F$, si definimos la suma y el producto por escalar como sigue, $\mathcal{M}\_{m \times n}(F)$ es un espacio vectorial; lo llamamos **espacio de matrices**.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(con }1 \leq i \leq &m,\ 1 \leq j \leq n \text{)}
\end{align*} $$

Es la extensión natural de las operaciones definidas en $F^n$ y $F^m$.

### Espacio de funciones

Para un conjunto no vacío $S$ de un cuerpo $F$, $\mathcal{F}(S,F)$ es el conjunto de todas las funciones de $S$ en $F$. En $\mathcal{F}(S,F)$, dos funciones $f, g$ son **iguales** ($f=g$) si para todo $s \in S$ se cumple $f(s) = g(s)$.

Para $f,g \in \mathcal{F}(S,F)$, $c \in F$, $s \in S$, si definimos la suma y el producto por escalar como sigue, $\mathcal{F}(S,F)$ es un espacio vectorial; lo llamamos **espacio de funciones**.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## Subespacios

> **Definición**  
> Un subconjunto $\mathbb{W}$ de un $F$-espacio vectorial $\mathbb{V}$ es un **subespacio** de $\mathbb{V}$ si, con las mismas operaciones de suma y multiplicación por escalar definidas en $\mathbb{V}$, $\mathbb{W}$ es también un $F$-espacio vectorial.
{: .prompt-info }

Para todo espacio vectorial $\mathbb{V}$, $\mathbb{V}$ mismo y $\\{0\\}$ son subespacios; en particular, a $\\{0\\}$ se le llama **subespacio cero**.

Podemos verificar que un subconjunto es un subespacio usando el siguiente teorema.

> **Teorema**  
> Dado un espacio vectorial $\mathbb{V}$ y un subconjunto $\mathbb{W}$, $\mathbb{W}$ es un subespacio de $\mathbb{V}$ si y solo si satisface las siguientes tres condiciones (con las operaciones heredadas de $\mathbb{V}$):
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> En pocas palabras, si contiene el vector cero y es cerrado bajo [combinación lineal](/posts/vectors-and-linear-combinations/#combinación-lineal-de-vectores) (esto es, si $\mathrm{span}(\mathbb{W})=\mathbb{W}$), entonces es un subespacio.
{: .prompt-info }

Además, valen los siguientes resultados.

> **Teorema**  
> - Para cualquier subconjunto $S$ de un espacio vectorial $\mathbb{V}$, el subespacio generado $\mathrm{span}(S)$ es un subespacio de $\mathbb{V}$ que contiene a $S$.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Todo subespacio de $\mathbb{V}$ que contiene a $S$ contiene necesariamente al subespacio generado por $S$.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Teorema**  
> Dado un conjunto de subespacios de un espacio vectorial $\mathbb{V}$, su intersección arbitraria es también un subespacio de $\mathbb{V}$.
{: .prompt-info }

### Matriz traspuesta, simétrica y antisimétrica

La **matriz traspuesta** $A^T$ de una matriz $m \times n$ $A$ es la matriz $n \times m$ obtenida intercambiando filas y columnas:

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

Una matriz $A$ con $A^T = A$ se llama **matriz simétrica**; una matriz $B$ con $B^T = -B$ se llama **matriz antisimétrica**. Ambas deben ser matrices cuadradas.

Sean $\mathbb{W}\_1, \mathbb{W}\_2$ los subconjuntos de $\mathcal{M}\_{n \times n}(F)$ formados por todas las matrices simétricas y todas las antisimétricas, respectivamente. Entonces $\mathbb{W}\_1$ y $\mathbb{W}\_2$ son subespacios de $\mathcal{M}\_{n \times n}(F)$; es decir, son cerrados bajo suma y producto por escalar.

### Matrices triangulares y diagonal

Estos dos tipos de matrices son especialmente importantes.

Agrupamos los siguientes dos tipos bajo el nombre **matrices triangulares**:
- **Triangular superior**: todas las entradas por debajo de la diagonal son $0$ (esto es, $i>j \Rightarrow A\_{ij}=0$), suele denotarse por $U$
- **Triangular inferior**: todas las entradas por encima de la diagonal son $0$ (esto es, $i<j \Rightarrow A\_{ij}=0$), suele denotarse por $L$

Una **matriz diagonal** es una matriz cuadrada en la que todas las entradas fuera de la diagonal son $0$, es decir, una matriz $n \times n$ con $i \neq j \Rightarrow M\_{ij}=0$, y suele denotarse por $D$. Una matriz diagonal es a la vez triangular superior e inferior.

El conjunto de matrices triangulares superiores, el de triangulares inferiores y el de diagonales son todos subespacios de $\mathcal{M}\_{m \times n}(F)$.
