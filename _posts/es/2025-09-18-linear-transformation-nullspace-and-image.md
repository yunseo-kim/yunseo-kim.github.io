---
title: "Transformación lineal, núcleo e imagen"
description: "Definimos la transformación lineal y estudiamos dos subespacios fundamentales —núcleo (espacio nulo) e imagen— junto con sus dimensiones (nulidad y rango) y los teoremas más importantes relacionados."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Vectores y combinaciones lineales](/posts/vectors-and-linear-combinations/)
- [Espacios vectoriales, subespacios y matrices](/posts/vector-spaces-subspaces-and-matrices/)
- [Dependencia lineal e independencia lineal, base y dimensión](posts/linear-dependence-and-independence-basis-and-dimension/)
- inyección, sobreyección

## Transformación lineal

Una función especial que preserva la estructura de espacio vectorial se llama **transformación lineal (linear transformation)**; es un concepto clave que aparece con mucha frecuencia en matemáticas puras, matemáticas aplicadas, ciencias sociales, ciencias naturales e ingeniería.

> **Definición**  
> Sean $\mathbb{V}$ y $\mathbb{W}$ $F$-espacios vectoriales. Una función $T: \mathbb{V} \to \mathbb{W}$ que satisface las dos condiciones siguientes para todo $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ y todo $c \in F$ se llama **transformación lineal (linear transformation)** de $\mathbb{V}$ en $\mathbb{W}$.
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

Decimos simplemente que $T$ es **lineal**. Una transformación lineal $T: \mathbb{V} \to \mathbb{W}$ satisface las cuatro propiedades siguientes.

> 1. $T$ lineal $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ es lineal $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ lineal $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ es lineal $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> Para probar que una función es lineal, suele ser conveniente usar la propiedad 2.
{: .prompt-tip }

> El álgebra lineal tiene un uso amplio y variado en geometría porque muchas transformaciones geométricas importantes son lineales. En particular, las tres transformaciones principales —**rotación**, **simetría** y **proyección**— son transformaciones lineales.
{: .prompt-tip }

Dos transformaciones lineales aparecen especialmente a menudo.

> **Transformación identidad y transformación nula**  
> Para $F$-espacios vectoriales $\mathbb{V}, \mathbb{W}$:
> - **Transformación identidad (identity transformation)**: la función $I_\mathbb{V}: \mathbb{V} \to \mathbb{V}$ definida por $I_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ para todo $\mathbf{x} \in \mathbb{V}$
> - **Transformación nula (zero transformation)**: la función $T_0: \mathbb{V} \to \mathbb{W}$ definida por $T_0(\mathbf{x}) = \mathbf{0}$ para todo $\mathbf{x} \in \mathbb{V}$
{: .prompt-info }

Además de estas, muchos otros objetos son transformaciones lineales.

> **Ejemplos de transformaciones lineales**  
> - rotación
> - simetría
> - proyección
> - [traspuesta](/posts/vector-spaces-subspaces-and-matrices/#matriz-traspuesta-simétrica-y-antisimétrica)
> - la derivada de una función diferenciable
> - la integral de una función continua
{: .prompt-tip }

## Núcleo e imagen

### Definición de núcleo e imagen

> **Definición**  
> Dados espacios vectoriales $\mathbb{V}, \mathbb{W}$ y una transformación lineal $T: \mathbb{V} \to \mathbb{W}$:
> - **Espacio nulo (null space)** o **núcleo (kernel)**: el conjunto de los $\mathbf{x} \in \mathbb{V}$ tales que $T(\mathbf{x}) = \mathbf{0}$; se denota por $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **Imagen (image)** o **rango (range)**: el subconjunto de $\mathbb{W}$ formado por los valores de $T$; se denota por $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **p. ej.** Para espacios vectoriales $\mathbb{V}, \mathbb{W}$, la identidad $I: \mathbb{V} \to \mathbb{V}$ y la transformación nula $T_0: \mathbb{V} \to \mathbb{W}$ satisfacen:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T_0) = \mathbb{V}$
> - $\mathrm{R}(T_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

Algo que será importante en adelante: el núcleo y la imagen de una transformación lineal son [subespacios](/posts/vector-spaces-subspaces-and-matrices/#subespacios).

> **Teorema 1**  
> Dado $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V} \to \mathbb{W}$ lineal, $\mathrm{N}(T)$ y $\mathrm{R}(T)$ son subespacios de $\mathbb{V}$ y $\mathbb{W}$, respectivamente.
>
> **Demostración**  
> Denotemos por $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$ los vectores cero de $\mathbb{V}$ y $\mathbb{W}$, respectivamente.
>
> Como $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, se tiene $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$. Además, para $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T)$ y $c \in F$:
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [Como $\mathbf{0}_\mathbb{V} \in \mathrm{N}(T)$, $\mathbf{x} + \mathbf{y} \in \mathrm{N}(T)$ y $c\mathbf{x} \in \mathrm{N}(T)$, $\mathrm{N}(T)$ es un subespacio de $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#subespacios).
>
> Del mismo modo, $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$ implica $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$; y como $\forall \mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F \ (\exists \mathbf{v}, \mathbf{w} \in \mathbb{V} \ (T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y}))$, entonces
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [Como $\mathbf{0}_\mathbb{W} \in \mathrm{R}(T)$, $\mathbf{x} + \mathbf{y} \in \mathrm{R}(T)$ y $c\mathbf{x} \in \mathrm{R}(T)$, $\mathrm{R}(T)$ es un subespacio de $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#subespacios). $\blacksquare$
{: .prompt-info }

Por otra parte, dados $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V} \to \mathbb{W}$ lineal, si conocemos una [base](/posts/linear-dependence-and-independence-basis-and-dimension/#base) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$, podemos hallar un [conjunto generador](/posts/vectors-and-linear-combinations/#generación) de la imagen $\mathrm{R}(T)$ como sigue.

> **Teorema 2**  
> Sean $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V} \to \mathbb{W}$ lineal, y sea $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ una [base](/posts/linear-dependence-and-independence-basis-and-dimension/#base) de $\mathbb{V}$. Entonces:
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Demostración**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Como $\mathrm{R}(T)$ es un subespacio, por el **Teorema 2** de [Espacios vectoriales, subespacios y matrices](/posts/vector-spaces-subspaces-and-matrices/#subespacios),
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> Además,
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Como $\beta$ es base de $\mathbb{V}$,
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(donde } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> Como $T$ es lineal,
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ Como $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ y a la vez $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$, se sigue que $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

Este teorema también vale cuando la base $\beta$ es infinita.

### Teorema de la dimensión

Como núcleo e imagen son subespacios muy importantes, sus [dimensiones](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensión) reciben nombres específicos.

> Sean $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V} \to \mathbb{W}$ lineal, y supongamos que $\mathrm{N}(T), \mathrm{R}(T)$ son de dimensión finita.
> - **Nulidad (nullity)**: la dimensión de $\mathrm{N}(T)$; se denota por $\mathrm{nullity}(T)$
> - **Rango (rank)**: la dimensión de $\mathrm{R}(T)$; se denota por $\mathrm{rank}(T)$
{: .prompt-info }

Para transformaciones lineales, cuanto mayor es la nulidad, menor es el rango, y viceversa.

> **Teorema 3: teorema de la dimensión**  
> Sean $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V}\to \mathbb{W}$ lineal. Si $\mathbb{V}$ es de dimensión finita, entonces:
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Demostración

Sea $\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$, y sea $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ una base de $\mathrm{N}(T)$.

Por el **Corolario 6-1** de ["Dependencia lineal e independencia lineal, base y dimensión"](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensión-de-subespacios), podemos ampliar $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ a una base de $\mathbb{V}$, $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$.

Mostraremos ahora que $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ es una base de $\mathrm{R}(T)$. Como $T(\mathbf{v}_i) = 0$ para $1 \leq i \leq k$, por el [**Teorema 2**](#definición-de-núcleo-e-imagen) se tiene

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Es decir, $S$ es un conjunto generador de $\mathrm{R}(T)$. Por el [**Corolario 5-2 del teorema del reemplazo**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensión), bastará probar que $S$ es linealmente independiente para concluir que es base de $\mathrm{R}(T)$.

Si $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (con $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$), como $T$ es lineal,

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Por tanto,

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

Como $\beta$ es base de $\mathbb{V}$, la única solución de $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ es

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

y de aquí

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Así, $S$ es linealmente independiente y base de $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Transformación lineal, inyectividad y sobreyectividad

En transformaciones lineales, la inyectividad (injection) y la sobreyectividad (surjection) están estrechamente relacionadas con el rango y la nulidad.

> **Teorema 4**  
> Dados $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V} \to \mathbb{W}$ lineal,
>
> $$ T \text{ es inyectiva} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Teorema 5**  
> Si $\mathbb{V}, \mathbb{W}$ son espacios vectoriales de dimensión finita con la misma dimensión y $T: \mathbb{V} \to \mathbb{W}$ es lineal, entonces son equivalentes las cuatro afirmaciones:
> 1. $T$ es inyectiva.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ es sobreyectiva.
{: .prompt-info }

Usando el [teorema de la dimensión](#teorema-de-la-dimensión), las [propiedades 1 y 3 de las transformaciones lineales](#transformación-lineal) y el [**Teorema 6** de "Dependencia lineal e independencia lineal, base y dimensión"](/posts/linear-dependence-and-independence-basis-and-dimension/#dimensión-de-subespacios), se pueden demostrar los **Teoremas 4** y **5**.

Estos dos teoremas son útiles para decidir si una transformación lineal dada es inyectiva o sobreyectiva.

> Para un espacio vectorial infinito dimensional $\mathbb{V}$ y $T: \mathbb{V} \to \mathbb{V}$ lineal, inyectividad y sobreyectividad no son equivalentes.
{: .prompt-warning }

Además, si una transformación lineal es inyectiva, el siguiente teorema puede ser útil para decidir si un subconjunto dado de un espacio vectorial es linealmente independiente.

> **Teorema 6**  
> Sean $\mathbb{V}, \mathbb{W}$ y $T: \mathbb{V} \to \mathbb{W}$ lineal e inyectiva, y sea $S \subseteq \mathbb{V}$. Entonces:
>
> $$ S \text{ es linealmente independiente} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \} \text{ es linealmente independiente.} $$
>
{: .prompt-info }

## Transformación lineal y bases

Una propiedad importante de las transformaciones lineales es que su comportamiento queda determinado por su acción sobre una base.

> **Teorema 7**  
> Sean los $F$-espacios vectoriales $\mathbb{V}, \mathbb{W}$, una base $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ de $\mathbb{V}$ y vectores $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$. Existe una única transformación lineal $T: \mathbb{V} \to \mathbb{W}$ que satisface:
>
> $$ T(\mathbf{v}_i) = \mathbf{w}_i \quad \text{para } i = 1, 2, \dots, n $$
>
> **Demostración**  
> Para cada $\mathbf{x} \in \mathbb{V}$, la siguiente representación como combinación lineal es única:
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> Definamos la transformación lineal $T: \mathbb{V} \to \mathbb{W}$ por
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> i) Para $i = 1, 2, \dots, n$, se cumple $T(\mathbf{v}_i) = \mathbf{w}_i$.
>
> ii)
>
> Si otra transformación lineal $U: \mathbb{V} \to \mathbb{W}$ satisface $U(\mathbf{v}\_i) = \mathbf{w}\_i$ para $i = 1, 2, \dots, n$, entonces, para $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$,
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> Por i) y ii), la transformación lineal que cumple $T(\mathbf{v}\_i) = \mathbf{w}\_i$ para $i = 1, 2, \dots, n$ es
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> y es única. $\blacksquare$
>
> **Corolario 7-1**  
> Sean espacios vectoriales $\mathbb{V}, \mathbb{W}$ y supongamos que $\mathbb{V}$ tiene una base finita $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$. Si dos transformaciones lineales $U, T: \mathbb{V} \to \mathbf{W}$ satisfacen $U(\mathbf{v}_i) = T(\mathbf{v}_i)$ para $i = 1, 2, \dots, n$, entonces $U = T$.  
> Es decir, <u>si dos transformaciones lineales coinciden en una base, son la misma transformación</u>.
{: .prompt-info }
