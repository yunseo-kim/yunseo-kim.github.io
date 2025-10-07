---
title: "Vectores y combinaciones lineales"
description: "Qué es un vector, cómo se representa y sus operaciones básicas (suma y multiplicación por un escalar); con ello entendemos la combinación lineal en álgebra lineal."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Definición de vector**
>   - **Vector en sentido estricto (vector euclidiano)**: magnitud física que tiene módulo y dirección
>   - **Vector en sentido amplio, en álgebra lineal**: elemento de un espacio vectorial
> - **Formas de representación de vectores**
>   - **Representación con flechas**: el módulo es la longitud de la flecha y la dirección es la de la flecha. Es visual e intuitiva, pero resulta problemática para vectores de dimensión ≥ 4 o no euclidianos.
>   - **Representación por componentes**: fijando el origen del vector en el origen del espacio de coordenadas, se expresa por las coordenadas de su extremo.
> - **Operaciones básicas con vectores**
>   - **Suma**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Multiplicación por un escalar**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Combinación lineal de vectores**
>   - Dado un número finito de vectores $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ y escalares $a_1, a_2, \dots, a_n$, se llama **combinación lineal** de $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ a cualquier vector $\mathbf{v}$ tal que $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$.
>   - En tal caso, a $a_1, a_2, \dots, a_n$ se les llama **coeficientes** de la combinación lineal.
{: .prompt-info }

## Prerequisites
- Plano/espacio de coordenadas
- Cuerpo

## ¿Qué es un vector?

### Sentido estricto: vector euclidiano

> Muchas magnitudes físicas —fuerza, velocidad, aceleración— poseen no solo módulo sino también dirección. A una magnitud que tiene ambos se le llama **vector**.
{: .prompt-info }

Esta es la definición de vector que se trata en mecánica y en matemáticas de nivel bachillerato. Un vector en este sentido, con el significado geométrico de “segmento orientado con módulo y dirección” basado en la intuición física, se denomina con propiedad **vector euclidiano**.

### Sentido amplio: elemento de un espacio vectorial

En álgebra lineal, más allá de los vectores euclidianos, se define el vector como una estructura algebraica más abstracta:

> **Definición**  
> Un **espacio vectorial** o **espacio lineal** $V$ sobre un cuerpo $F$ es un conjunto dotado de dos operaciones, **suma** y **multiplicación por un escalar**, que satisfacen las siguientes 8 condiciones. A los elementos de $F$ se les llama **escalares** y a los de $V$, **vectores**.
>
> - **Suma**: para cualesquiera $x, y \in V$ existe un único $x + y \in V$. A $x + y$ se le llama la **suma** de $x$ e $y$.
> - **Multiplicación por un escalar**: para cada $a \in F$ y $x \in V$ existe un único $ax \in V$. A $ax$ se le llama su **producto** escalar.
>
> 1. Para todo $x,y \in V$, $x + y = y + x$. (conmutatividad de la suma)
> 2. Para todo $x,y,z \in V$, $(x+y)+z = x+(y+z)$. (asociatividad de la suma)
> 3. Para todo $x \in V$, existe $0 \in V$ tal que $x + 0 = x$. (vector cero, elemento neutro de la suma)
> 4. Para cada $x \in V$, existe $y \in V$ tal que $x+y=0$. (inverso aditivo)
> 5. Para cada $x \in V$, $1x = x$. (elemento neutro de la multiplicación)
> 6. Para todo $a,b \in F$ y todo $x \in V$, $(ab)x = a(bx)$. (asociatividad de la multiplicación por escalar)
> 7. Para todo $a \in F$ y todo $x,y \in V$, $a(x+y) = ax + ay$. (distributividad del escalar respecto de la suma 1)
> 8. Para todo $a,b \in F$ y todo $x \in V$, $(a+b)x = ax + bx$. (distributividad del escalar respecto de la suma 2)
{: .prompt-info }

Esta definición en álgebra lineal abarca un ámbito más amplio que incluye al [vector euclidiano](#sentido-estricto-vector-euclidiano). También puede verificarse que un [vector euclidiano](#sentido-estricto-vector-euclidiano) satisface las 8 propiedades anteriores.

El origen y desarrollo del concepto de vector están estrechamente ligados a problemas prácticos planteados por la física: describir cuantitativamente nociones como fuerza, movimiento, rotación y campos. La necesidad física de expresar fenómenos naturales de forma matemática llevó primero al concepto de [vector euclidiano](#sentido-estricto-vector-euclidiano); posteriormente, al generalizar y formalizar estas ideas, las matemáticas establecieron estructuras como espacios vectoriales, producto interno y producto vectorial, llegando a la definición actual de vector. En suma, el vector es un concepto demandado por la física y formalizado por las matemáticas; más que un producto de las matemáticas puras, es un fruto del intercambio entre la comunidad matemática y la física.

El [vector euclidiano](#sentido-estricto-vector-euclidiano) tratado en la mecánica clásica puede expresarse dentro de un [marco más general](#sentido-amplio-elemento-de-un-espacio-vectorial); hoy en física se emplean activamente no solo vectores euclidianos, sino también espacios vectoriales, espacios de funciones y otros conceptos más abstractos definidos en matemáticas, dotándolos de significado físico. Por tanto, no es adecuado entender las dos definiciones de vector simplemente como “definición física” y “definición matemática”.

Pospondremos un estudio más profundo de los espacios vectoriales y nos centraremos primero en el vector en sentido estricto, el vector euclidiano, que puede representarse geométricamente en un espacio de coordenadas. Ver ejemplos intuitivos de vectores euclidianos ayuda luego a generalizar a otros tipos de vectores.

## Representación de vectores
### Representación con flechas

Es la forma más habitual y la que mejor aprovecha la intuición geométrica: el módulo del vector es la longitud de la flecha y su dirección es la de la flecha.

![Vector euclidiano de A a B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Fuente de la imagen*
> - Autor: usuario de Wikipedia [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

Aunque es intuitiva, esta representación con flechas tiene límites claros para vectores de dimensión 4 o superior. Además, más adelante habrá que tratar vectores no euclidianos que ni siquiera se pueden representar geométricamente, por lo que conviene familiarizarse con la representación por componentes que se expone a continuación.

### Representación por componentes

Independientemente de su ubicación, si dos vectores tienen el mismo módulo y dirección, se consideran iguales. Por tanto, dado un espacio de coordenadas, si fijamos el origen del vector en el origen del espacio, <u>un vector de dimensión $n$ corresponde a un punto cualquiera del espacio de dimensión $n$</u>, y así podemos expresar el vector por las coordenadas de su extremo. A esta forma se la llama **representación por componentes** del vector.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ o } \mathbb{C}^n $$

![Vector de posición](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Fuente de la imagen*
> - Autor: usuario de Wikimedia [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Operaciones básicas con vectores

Las operaciones básicas son la **suma** y la **multiplicación por un escalar**. Toda operación con vectores puede expresarse como combinación de estas dos.

### Suma de vectores

La suma de dos vectores es de nuevo un vector, y sus componentes son la suma componente a componente de los vectores dados.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Multiplicación por un escalar

Un vector puede escalarse (ampliarse o reducirse) multiplicándolo por un número (escalar). El resultado equivale a multiplicar cada componente por dicho escalar.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Multiplicación por un escalar de vectores](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Fuente de la imagen*
> - Autor: usuario de Wikipedia [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Combinación lineal de vectores

Así como el cálculo diferencial parte de los números $x$ y las funciones $f(x)$, el álgebra lineal parte de vectores $\mathbf{v}, \mathbf{w}, \dots$ y de combinaciones lineales $c\mathbf{v} + d\mathbf{w} + \cdots$. Toda combinación lineal de vectores se compone de las dos operaciones básicas: [suma](#suma-de-vectores) y [multiplicación por un escalar](#multiplicación-por-un-escalar).

> Dados un número finito de vectores $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ y escalares $a_1, a_2, \dots, a_n$, cualquier vector $\mathbf{v}$ que satisfaga
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> se llama **combinación lineal** de $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$. En este caso, a $a_1, a_2, \dots, a_n$ se les llama **coeficientes** de la combinación lineal.
{: .prompt-info }

¿Por qué son importantes las combinaciones lineales? Considera la situación en la que **$n$ vectores en un espacio de dimensión $m$ constituyen las $n$ columnas de una matriz $m \times n$**:

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

Las claves aquí son dos:

1. **Describe todas las combinaciones lineales posibles $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n$.** ¿Qué conjunto forman?
2. Dado un vector objetivo $b$, **encuentra $x_1, x_2, \dots, x_n$ tales que $Ax = b$.**

Responderemos a la segunda pregunta más adelante; por ahora centrémonos en la primera. Para simplificar, consideremos el caso de dos vectores en 2 dimensiones ($m=2$, $n=2$) distintos de cero.

### Combinación lineal $c\mathbf{v} + d\mathbf{w}$

En el plano, un vector $\mathbf{v}$ tiene dos componentes. Para cualquier escalar $c$, <u>el conjunto de vectores $c\mathbf{v}$ forma una recta infinita en el plano $xy$, que pasa por el origen y es paralela a $\mathbf{v}$.</u>

Si un segundo vector $\mathbf{w}$ no está sobre esa recta (es decir, si $\mathbf{v}$ y $\mathbf{w}$ no son paralelos), entonces los vectores $d\mathbf{w}$ forman otra recta. Al combinar ambas rectas, vemos que **la combinación lineal $c\mathbf{v} + d\mathbf{w}$ barre un plano que contiene al origen**.

![Combinaciones lineales de dos vectores](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Fuente de la imagen*
> - Autor: usuario de Wikimedia [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

Así, las combinaciones lineales de vectores generan un espacio vectorial; a esto se le llama **generación (span)**. Aunque todavía no hemos definido formalmente el concepto de espacio vectorial, este ejemplo te ayudará a comprenderlo más adelante.
