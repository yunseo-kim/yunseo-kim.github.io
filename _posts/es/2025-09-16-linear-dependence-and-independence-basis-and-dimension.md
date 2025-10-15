---
title: "Dependencia lineal e independencia lineal, base y dimensión"
description: "Resumen claro de dependencia e independencia lineal, y de los conceptos de base y dimensión en espacios vectoriales; teoremas clave y criterios de decisión."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Vectores y combinaciones lineales](/posts/vectors-and-linear-combinations/)
- [Espacios vectoriales, subespacios y matrices](/posts/vector-spaces-subspaces-and-matrices/)

## Dependencia lineal e independencia lineal

Dado un [espacio vectorial](/posts/vector-spaces-subspaces-and-matrices/#espacios-vectoriales) $\mathbb{V}$ y un [subespacio](/posts/vector-spaces-subspaces-and-matrices/#subespacios) $\mathbb{W}$, supongamos que queremos encontrar un subconjunto finito mínimo $S$ que [genere](/posts/vectors-and-linear-combinations/#combinación-lineal-cmathbfv--dmathbfw) $\mathbb{W}$.

Sea $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ tal que $\mathrm{span}(S) = \mathbb{W}$. ¿Cómo decidir si existe un subconjunto propio de $S$ que aún genere $\mathbb{W}$? Esto equivale a decidir si un vector de $S$ puede escribirse como [combinación lineal](/posts/vectors-and-linear-combinations/#combinación-lineal-de-vectores) de los demás. Por ejemplo, una condición necesaria y suficiente para poder expresar $\mathbf{u}_4$ como combinación lineal de los otros tres vectores es que existan escalares $a_1, a_2, a_3$ que satisfagan:

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

Sin embargo, plantear y resolver cada vez un sistema lineal para $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ sería engorroso; mejor reescribamos ligeramente:

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

Si algún vector de $S$ es combinación lineal de los otros, entonces existe una forma de expresar el vector cero como combinación lineal de elementos de $S$ en la que al menos uno de los coeficientes $a_1, a_2, a_3, a_4$ sea distinto de $0$. El recíproco también es cierto: si existe una combinación de los vectores de $S$ que da el vector cero con al menos un coeficiente no nulo, entonces algún vector de $S$ es combinación lineal de los demás.

Generalizando, definimos **dependencia lineal** e **independencia lineal** como sigue.

> **Definición**  
> Para un subconjunto $S$ de un espacio vectorial $\mathbb{V}$, si existen un número finito de vectores distintos $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ y escalares $a_1, a_2, \dots, a_n$, no todos nulos, tales que $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$, entonces el conjunto $S$ y esos vectores se dicen **linealmente dependientes**. En caso contrario, se dicen **linealmente independientes**.
{: .prompt-info }

Para cualesquiera vectores $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$, si $a_1 = a_2 = \cdots = a_n = 0$, entonces $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$; a esto se le llama la **representación trivial del vector cero (trivial representation of $\mathbf{0}$)**.

Los siguientes tres enunciados sobre conjuntos linealmente independientes son siempre verdaderos en cualquier espacio vectorial. En particular, la **Proposición 3** es muy útil para decidir si un conjunto finito es independiente.

> - **Proposición 1**: El conjunto vacío es linealmente independiente. Para que un conjunto sea linealmente dependiente debe ser no vacío.
> - **Proposición 2**: Un conjunto formado por un único vector no nulo es linealmente independiente.
> - **Proposición 3**: Un conjunto es linealmente independiente si y solo si la única forma de expresar $\mathbf{0}$ como combinación lineal de sus vectores es la representación trivial.
{: .prompt-info }

También son importantes los siguientes resultados.

> **Teorema 1**  
> Si $\mathbb{V}$ es un espacio vectorial y $S_1 \subseteq S_2 \subseteq \mathbb{V}$, entonces si $S_1$ es linealmente dependiente, $S_2$ también lo es.
>
> **Corolario 1-1**  
> Si $\mathbb{V}$ es un espacio vectorial y $S_1 \subseteq S_2 \subseteq \mathbb{V}$, entonces si $S_2$ es linealmente independiente, $S_1$ también lo es.
{: .prompt-info }

> **Teorema 2**  
> Sea $\mathbb{V}$ un espacio vectorial y $S$ un subconjunto linealmente independiente. Para un vector $\mathbf{v} \in \mathbb{V}$ que no pertenezca a $S$, una condición necesaria y suficiente para que $S \cup \\{\mathbf{v}\\}$ sea linealmente dependiente es que $\mathbf{v} \in \mathrm{span}(S)$.
>
> Dicho de otro modo, **si ningún subconjunto propio de $S$ genera el mismo espacio que $S$, entonces $S$ es linealmente independiente.**
{: .prompt-info }

## Base y dimensión

### Base

Un conjunto generador $S$ de $\mathbb{W}$ que sea [linealmente independiente](#dependencia-lineal-e-independencia-lineal) tiene una propiedad especial: todo vector de $\mathbb{W}$ puede expresarse necesariamente como combinación lineal de elementos de $S$, y además esa expresión es única (**Teorema 3**). Por ello, llamamos **base** a un conjunto generador linealmente independiente de un espacio vectorial.

> **Definición de base**  
> Dado un espacio vectorial $\mathbb{V}$ y un subconjunto $\beta$, si $\beta$ es linealmente independiente y genera $\mathbb{V}$, entonces $\beta$ es una **base** de $\mathbb{V}$. En tal caso, se dice que los vectores de $\beta$ forman una base de $\mathbb{V}$.
{: .prompt-info }

> Se tiene $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ y $\emptyset$ es linealmente independiente. Por tanto, $\emptyset$ es una base del espacio cero.
{: .prompt-tip }

En particular, la siguiente base especial de $F^n$ se llama **base estándar (standard basis)** de $F^n$.

> **Definición de base estándar**  
> Para el espacio vectorial $F^n$, consideremos los siguientes vectores:
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> Entonces, el conjunto $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ es una base de $F^n$, llamada la **base estándar** de $F^n$.
{: .prompt-info }

> **Teorema 3**  
> Sea $\mathbb{V}$ un espacio vectorial y sean $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$ vectores distintos. Un conjunto $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ es una base de $\mathbb{V}$ si y solo si todo vector $\mathbf{v} \in \mathbb{V}$ puede representarse como combinación lineal de los vectores de $\beta$, y dicha representación es única. Es decir, existe un único $n$-tuplo de escalares $(a_1, a_2, \dots, a_n)$ tal que
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

Según el **Teorema 3**, si $n$ vectores distintos $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ forman una base de $\mathbb{V}$, entonces en ese espacio queda determinado el $n$-tuplo de escalares $(a_1, a_2, \dots, a_n)$ asociado a un vector dado $\mathbf{v}$, y recíprocamente, dado un $n$-tuplo de escalares se obtiene el vector correspondiente $\mathbf{v}$. Más adelante, al estudiar la **invertibilidad** y el **isomorfismo**, volveremos sobre esto; en este caso, $\mathbb{V}$ y $F^n$ son <u>esencialmente iguales</u>.

> **Teorema 4**  
> Si $S$ es un conjunto finito con $\mathrm{span}(S) = \mathbb{V}$, entonces existe un subconjunto de $S$ que es base de $\mathbb{V}$. En particular, en este caso, cualquier base de $\mathbb{V}$ es finita.
{: .prompt-info }

> Muchos espacios vectoriales cumplen el **Teorema 4**, pero no todos. <u>Una base puede no ser un conjunto finito</u>.
{: .prompt-tip }

### Dimensión

> **Teorema 5: teorema del reemplazo (replacement theorem)**  
> Sea $G$ un conjunto de $n$ vectores tal que $\mathrm{span}(G) = \mathbb{V}$. Si $L$ es un subconjunto de $\mathbb{V}$ formado por $m$ vectores linealmente independientes, entonces $m \leq n$. Además, existe un conjunto $H \subseteq G$ con $n-m$ vectores tal que $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

De aquí se obtienen dos corolarios muy importantes.

> **Corolario 5-1 del teorema del reemplazo**  
> Si un espacio vectorial $\mathbb{V}$ tiene alguna base finita, entonces toda base de $\mathbb{V}$ es finita y todas tienen el mismo número de vectores.
{: .prompt-info }

Según esto, el número de vectores que forman una base de $\mathbb{V}$ es una propiedad esencial e invariante de $\mathbb{V}$, llamada **dimensión**.

> **Definición de dimensión**  
> Un espacio vectorial cuya base es finita se dice de **dimensión finita**; en tal caso, al número $n$ de elementos de una base se le llama la **dimensión** del espacio y se denota por $\dim(\mathbb{V})$. Un espacio vectorial que no es de dimensión finita es de **dimensión infinita**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> La dimensión de un espacio vectorial puede cambiar según el cuerpo de base.
> - Sobre el cuerpo de los complejos $\mathbb{C}$, la dimensión del espacio vectorial de los complejos es $1$, con base $\\{1\\}$
> - Sobre el cuerpo de los reales $\mathbb{R}$, la dimensión del espacio vectorial de los complejos es $2$, con base $\\{1,i\\}$
{: .prompt-tip }

En un espacio vectorial de dimensión finita $\mathbb{V}$, ningún subconjunto con más de $\dim(\mathbb{V})$ vectores puede ser linealmente independiente.

> **Corolario 5-2 del teorema del reemplazo**  
> Sea $\mathbb{V}$ un espacio vectorial de dimensión $n$.
> 1. Todo conjunto generador finito de $\mathbb{V}$ contiene al menos $n$ vectores, y cualquier conjunto generador de $\mathbb{V}$ con $n$ vectores es una base de $\mathbb{V}$.
> 2. Todo subconjunto de $\mathbb{V}$ con $n$ vectores linealmente independientes es una base de $\mathbb{V}$.
        3. Todo subconjunto linealmente independiente de $\mathbb{V}$ puede ampliarse a una base. Es decir, si $L \subseteq \mathbb{V}$ es linealmente independiente, existe una base $\beta$ de $\mathbb{V}$ con $\beta \supseteq L$.
{: .prompt-info }

### Dimensión de subespacios

> **Teorema 6**  
> Si $\mathbb{V}$ es un espacio vectorial de dimensión finita, entonces todo subespacio $\mathbb{W}$ es también de dimensión finita y se cumple $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$. En particular, si $\dim(\mathbb{W}) = \dim(\mathbb{V})$, entonces $\mathbb{V} = \mathbb{W}$.
>
> **Corolario 6-1**  
> Dado un subespacio $\mathbb{W}$ de un espacio vectorial de dimensión finita $\mathbb{V}$, cualquier base de $\mathbb{W}$ puede ampliarse a una base de $\mathbb{V}$.
{: .prompt-info }

Por el **Teorema 6**, la dimensión de los subespacios de $\mathbb{R}^3$ puede ser $0,1,2,3$.
- Dimensión 0: el espacio $\\{\mathbf{0}\\}$ que solo contiene el origen ($\mathbf{0}$)
- Dimensión 1: una recta que pasa por el origen ($\mathbf{0}$)
- Dimensión 2: un plano que contiene el origen ($\mathbf{0}$)
- Dimensión 3: todo el espacio euclídeo tridimensional
