---
title: "Vectors and Linear Combinations"
description: "Learn what vectors are, how to represent them, and the basics of vector operations (addition, scalar multiplication). Build intuition for linear combinations and span."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Definition of a vector**
>   - **Vector in the narrow sense (Euclidean vector)**: a physical quantity that has both magnitude and direction
>   - **Vector in the broad, linear-algebraic sense**: an element of a vector space
> - **Ways to represent vectors**
>   - **Arrow representation**: the vector’s magnitude is the length of the arrow, and its direction is the arrow’s direction. It is easy to visualize and intuitive, but it is difficult to represent higher-dimensional vectors (4D and above) or non-Euclidean vectors.
>   - **Component representation**: place the tail of the vector at the origin of a coordinate space and express the vector by the coordinates of its head.
> - **Basic operations on vectors**
>   - **Sum**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Scalar multiplication**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Linear combination of vectors**
>   - For finitely many vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ and scalars $a_1, a_2, \dots, a_n$, a vector $\mathbf{v}$ satisfying $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$ is called a **linear combination** of $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
>   - The numbers $a_1, a_2, \dots, a_n$ are called the **coefficients** of this linear combination.
{: .prompt-info }

## Prerequisites
- Coordinate plane/coordinate space
- Field

## What is a vector?

### Vector in the narrow sense: Euclidean vector

> Many physical quantities such as force, velocity, and acceleration carry not only magnitude but also directional information. A physical quantity that has both magnitude and direction is called a **vector**.
{: .prompt-info }

The definition above is the one used in mechanics in physics and in high-school-level mathematics. A vector in this geometric sense—“the magnitude and direction of a directed line segment,” grounded in physical intuition—is more precisely called a **Euclidean vector**.

### Vector in the broad sense: an element of a vector space

In linear algebra, vectors are defined more broadly than Euclidean vectors, as an abstract algebraic structure:

> **Definition**  
> A **vector space** (or **linear space**) $V$ over a field $F$ is a set equipped with two operations, **sum** and **scalar multiplication**, satisfying the following eight axioms. Elements of the field $F$ are called **scalars**, and elements of the vector space $V$ are called **vectors**.
>
> - **Sum**: For any $x, y \in V$, there exists a unique element $x + y \in V$. We call $x + y$ the **sum** of $x$ and $y$.
> - **Scalar multiplication**: For any $a \in F$ and $x \in V$, there exists a unique element $ax \in V$. In this case, $ax$ is called the scalar **product** of $a$ and $x$.
>
> 1. For all $x,y \in V$, $x + y = y + x$. (commutativity of addition)
> 2. For all $x,y,z \in V$, $(x+y)+z = x+(y+z)$. (associativity of addition)
> 3. There exists $0 \in V$ such that $x + 0 = x$ for all $x \in V$. (zero vector, additive identity)
> 4. For each $x \in V$, there exists $y \in V$ such that $x + y = 0$. (additive inverse)
> 5. For each $x \in V$, $1x = x$. (multiplicative identity)
> 6. For all $a,b \in F$ and $x \in V$, $(ab)x = a(bx)$. (associativity of scalar multiplication)
> 7. For all $a \in F$ and $x,y \in V$, $a(x+y) = ax + ay$. (distributivity of scalar multiplication over vector addition)
> 8. For all $a,b \in F$ and $x \in V$, $(a+b)x = ax + bx$. (distributivity of scalar multiplication over field addition)
{: .prompt-info }

This definition of a vector in linear algebra encompasses a broader class than the previously mentioned [Euclidean vector](#vector-in-the-narrow-sense-euclidean-vector). You can verify that [Euclidean vectors](#vector-in-the-narrow-sense-euclidean-vector) satisfy these eight properties.

The origin and development of vectors are closely tied to practical problems in physics—such as describing force, motion, rotation, and fields quantitatively. The concept was first introduced as [Euclidean vectors](#vector-in-the-narrow-sense-euclidean-vector) to meet the physical need to mathematically express natural phenomena. Mathematics then generalized and systematized these physical ideas, establishing formal structures such as vector spaces, inner products, and exterior products, leading to today’s definition of vectors. In other words, vectors are concepts demanded by physics and formalized by mathematics—an interdisciplinary product developed through close interaction between the two communities, rather than a creation of pure mathematics alone.

The [Euclidean vectors](#vector-in-the-narrow-sense-euclidean-vector) handled in classical mechanics can be expressed within a [more general framework](#vector-in-the-broad-sense-an-element-of-a-vector-space) mathematically. Modern physics actively uses not only [Euclidean vectors](#vector-in-the-narrow-sense-euclidean-vector) but also more abstract notions defined in mathematics—vector spaces, function spaces, etc.—and attaches physical meaning to them. Hence it is inappropriate to regard the two definitions of a vector as merely “the physical definition” and “the mathematical definition.”

We will defer a deeper dive into vector spaces and, for now, focus on Euclidean vectors—vectors in the narrow sense that admit geometric representation in coordinate spaces. Building intuition with Euclidean vectors first will be helpful when generalizing to other kinds of vectors later.

## Ways to represent vectors
### Arrow representation

This is the most common and most geometrically intuitive representation. The vector’s magnitude is represented by the length of an arrow, and its direction by the direction of the arrow.

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Image credits*
> - Author: Wikipedia user [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

While intuitive, this arrow representation has clear limitations for higher-dimensional vectors (4D and above). Moreover, we will eventually need to handle non-Euclidean vectors that are not easily depicted geometrically, so it is important to become comfortable with the component representation described next.

### Component representation

Regardless of where a vector is located, if its magnitude and direction are the same, we consider it the same vector. Therefore, given a coordinate space, if we fix the tail of the vector at the origin of that coordinate space, then <u>an $n$-dimensional vector corresponds to an arbitrary point in $n$-dimensional space</u>, and we can represent the vector by the coordinates of its head. This is called the **component representation** of a vector.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ or } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Image credits*
> - Author: Wikimedia user [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Basic operations on vectors

The two basic operations on vectors are **sum** and **scalar multiplication**. Every vector operation can be expressed as a combination of these two.

### Vector addition

The sum of two vectors is again a vector; its components are obtained by adding the corresponding components of the two vectors.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Scalar multiplication of vectors

A vector can be scaled up or down by multiplying it by a scalar (a constant); the result is obtained by multiplying each component by that scalar.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Image credits*
> - Author: Wikipedia user [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Linear combinations of vectors

Just as calculus starts from numbers $x$ and functions $f(x)$, linear algebra starts from vectors $\mathbf{v}, \mathbf{w}, \dots$ and their linear combinations $c\mathbf{v} + d\mathbf{w} + \cdots$. Every linear combination of vectors is built from the two basic operations above, [sum](#vector-addition) and [scalar multiplication](#scalar-multiplication-of-vectors).

> Given finitely many vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ and scalars $a_1, a_2, \dots, a_n$, a vector $\mathbf{v}$ satisfying
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> is called a **linear combination** of $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
> The numbers $a_1, a_2, \dots, a_n$ are the **coefficients** of this linear combination.
{: .prompt-info }

Why are linear combinations important? Consider the following situation: **$n$ vectors in $m$-dimensional space form the $n$ columns of an $m \times n$ matrix.**

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

The key questions are:

1. **Describe all possible linear combinations $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n$.** What do they form?
2. Given a desired output vector $b$, **find numbers $x_1, x_2, \dots, x_n$ such that $Ax = b$.**

We will return to the second question later; for now, focus on the first. To simplify, consider the case of two nonzero 2D vectors ($m=2$, $n=2$).

### The linear combination $c\mathbf{v} + d\mathbf{w}$

A vector $\mathbf{v}$ in 2D has two components. For any scalar $c$, <u>the vector $c\mathbf{v}$ traces an infinitely long line through the origin in the $xy$-plane, parallel to the original vector $\mathbf{v}$.</u>

If the given second vector $\mathbf{w}$ is not on this line (i.e., $\mathbf{v}$ and $\mathbf{w}$ are not parallel), then $d\mathbf{w}$ traces another line. Combining these two lines, we see that **the linear combination $c\mathbf{v} + d\mathbf{w}$ fills a single plane that includes the origin.**

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Image credits*
> - Author: Wikimedia user [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

In this way, linear combinations of vectors form a vector space, a process called **spanning**. Although we have not yet defined vector spaces rigorously in this post, recalling this example will help you understand the concept of a vector space later on.
