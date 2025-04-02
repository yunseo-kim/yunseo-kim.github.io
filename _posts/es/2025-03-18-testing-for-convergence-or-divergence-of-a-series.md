---
title: Pruebas de convergencia/divergencia de series (Testing for Convergence or Divergence of a Series)
description: Examinamos varios métodos para determinar la convergencia o divergencia de series.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Prueba del término n-ésimo (n-th-term test for divergence)**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la serie }\sum a_n \text{ diverge}$
> - **Convergencia/divergencia de series geométricas**: La serie geométrica $\sum ar^{n-1}$:
>   - Converge si $\|r\| < 1$
>   - Diverge si $\|r\| \geq 1$
> - **Convergencia/divergencia de series p**: La serie p $\sum \cfrac{1}{n^p}$:
>   - Converge si $p>1$
>   - Diverge si $p\leq 1$
> - **Criterio de comparación (Comparison Test)**: Si $0 \leq a_n \leq b_n$, entonces:  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Criterio de comparación por límite (Limit Comparison Test)**: Si $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (donde }c\text{ es un número positivo finito)}$, entonces ambas series $\sum a_n$ y $\sum b_n$ convergen o ambas divergen
> - Para una serie de términos positivos $\sum a_n$ y un número positivo $\epsilon < 1$:  
>   - Si $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, entonces la serie $\sum a_n$ converge
>   - Si $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, entonces la serie $\sum a_n$ diverge
> - **Criterio de la raíz (Root Test)**: Para una serie de términos positivos $\sum a_n$, si existe el límite $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$:
>   - Si $r<1$, entonces la serie $\sum a_n$ converge
>   - Si $r>1$, entonces la serie $\sum a_n$ diverge
> - **Criterio del cociente (Ratio Test)**: Para una sucesión de números positivos $(a_n)$ y $0 < r < 1$:
>   - Si $a_{n+1}/a_n \leq r$ para todo $n$, entonces la serie $\sum a_n$ converge
>   - Si $a_{n+1}/a_n \geq 1$ para todo $n$, entonces la serie $\sum a_n$ diverge
> - Para una sucesión de números positivos $(a_n)$, si existe el límite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$:
>   - Si $\rho < 1$, entonces la serie $\sum a_n$ converge
>   - Si $\rho > 1$, entonces la serie $\sum a_n$ diverge
> - **Criterio de la integral (Integral Test)**: Si $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ es una función continua, decreciente y siempre $f(x)>0$, entonces la serie $\sum f(n)$ converge si y solo si la integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converge
> - **Criterio de las series alternadas (Alternating Series Test)**: Una serie alternada $\sum a_n$ converge si:
>   1. Los signos de $a_n$ y $a_{n+1}$ son diferentes para todo $n$
>   2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Una serie absolutamente convergente es convergente. El recíproco no es cierto.
{: .prompt-info }

## Prerrequisitos
- [Sucesiones y series](/posts/sequences-and-series/)

## Introducción
Anteriormente en [Sucesiones y series](/posts/sequences-and-series/#convergencia-y-divergencia-de-series), vimos la definición de convergencia y divergencia de series. En este artículo, resumiremos varios métodos que pueden utilizarse para determinar la convergencia o divergencia de una serie. En general, determinar si una serie converge o diverge es mucho más sencillo que calcular su suma exacta.

## Criterio del término n-ésimo
Para una serie $\sum a_n$, llamamos a $a_n$ el **término general** de la serie.

Gracias al siguiente teorema, podemos identificar fácilmente algunas series que claramente divergen, por lo que verificar esto primero es una estrategia inteligente para evitar perder tiempo.

> **Criterio del término n-ésimo (n-th-term test for divergence)**  
> Si una serie $\sum a_n$ converge, entonces:
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Es decir:
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la serie }\sum a_n \text{ diverge} $$
{: .prompt-info }

### Demostración
Sea $l$ la suma de una serie convergente $\sum a_n$ y definamos la suma de los primeros $n$ términos como:

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Entonces:

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Por lo tanto, para $n$ suficientemente grande ($>N$):

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Por la definición de convergencia de sucesiones:

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Advertencia
El recíproco de este teorema no es generalmente cierto. Un ejemplo clásico que lo demuestra es la **serie armónica (harmonic series)**.

La serie armónica es una serie cuyos términos son los recíprocos de una **sucesión aritmética**, es decir, una **sucesión armónica**. La serie armónica más representativa es:

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Podemos demostrar que esta serie diverge de la siguiente manera:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Como podemos ver, aunque la serie $H_n$ diverge, su término general $1/n$ converge a $0$.

> Si $\lim_{n\to\infty} a_n \neq 0$, entonces la serie $\sum a_n$ definitivamente diverge, pero asumir que una serie $\sum a_n$ converge solo porque $\lim_{n\to\infty} a_n = 0$ es peligroso. En este caso, se deben utilizar otros métodos para determinar la convergencia o divergencia.
{: .prompt-danger }

## Series geométricas
La **serie geométrica (geometric series)** con primer término 1 y razón $r$:

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

es una de las series más <u>importantes y fundamentales</u>. De la igualdad:

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

obtenemos:

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Por otro lado:

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

Por lo tanto, la condición necesaria y suficiente para que la serie geométrica ($\ref{eqn:geometric_series}$) converja es que $\|r\| < 1$.

> **Convergencia/divergencia de series geométricas**  
> La serie geométrica $\sum ar^{n-1}$:
> - Converge si $\|r\| < 1$
> - Diverge si $\|r\| \geq 1$
{: .prompt-info }

De esto obtenemos:

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Series geométricas y aproximaciones
La identidad ($\ref{eqn:sum_of_geometric_series}$) es útil para encontrar aproximaciones de $\cfrac{1}{1-r}$ cuando $\|r\| < 1$.

Sustituyendo $r=-\epsilon$ y $n=2$ en esta ecuación:

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Por lo tanto, si $0 < \epsilon < 1$:

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

Así:

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Esto nos muestra que para un valor positivo $\epsilon$ suficientemente pequeño, $\cfrac{1}{1 + \epsilon}$ puede aproximarse como $1 - \epsilon$.

## Criterio de las series p (p-Series Test)  
Para un número real positivo $p$, una serie de la forma:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

se denomina **serie p**.

> **Convergencia/divergencia de series p**  
> La serie p $\sum \cfrac{1}{n^p}$:
> - Converge si $p>1$
> - Diverge si $p\leq 1$
{: .prompt-info }

En el caso de $p=1$, la serie p se convierte en la serie armónica, que como ya vimos, diverge.  
El problema de encontrar el valor de la serie p cuando $p=2$, es decir, $\sum \cfrac{1}{n^2}$, se conoce como el "problema de Basilea" (Basel problem), nombrado así por la ciudad natal de la familia Bernoulli, que produjo varios matemáticos famosos a lo largo de generaciones. Se sabe que la respuesta a este problema es $\cfrac{\pi^2}{6}$.

Más generalmente, la serie p para $p>1$ se conoce como la **función zeta (zeta function)**. Esta es una función especial introducida por Leonhard Euler en el año 11740 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) y posteriormente nombrada por Riemann, definida como:

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Aunque se desvía un poco del tema principal de este artículo, y siendo sincero, como estudiante de ingeniería y no matemático, no profundizaré en ello, pero Leonhard Euler demostró que la función zeta también puede expresarse como un producto infinito de números primos, conocido como el **producto de Euler (Euler Product)**. Posteriormente, la función zeta ha ocupado un lugar central en varios campos de la teoría analítica de números. La **función zeta de Riemann (Riemann zeta function)**, que extiende el dominio de la función zeta a los números complejos, y la importante conjetura no resuelta conocida como la **hipótesis de Riemann (Riemann hypothesis)** son parte de este campo.

Volviendo a nuestro tema, la demostración del criterio de las series p requiere el [criterio de comparación](#criterio-de-comparación) y el [criterio de la integral](#criterio-de-la-integral) que veremos más adelante. Sin embargo, la convergencia/divergencia de las series p, junto con las series geométricas, puede ser útil en el [criterio de comparación](#criterio-de-comparación) que veremos a continuación, por lo que intencionalmente lo he colocado antes.

### Demostración
#### i) Cuando $p>1$
La integral:

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converge, por lo que según el [criterio de la integral](#criterio-de-la-integral), la serie $\sum \cfrac{1}{n^p}$ también converge.

#### ii) Cuando $p\leq 1$
En este caso:

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Sabemos que la serie armónica $\sum \cfrac{1}{n}$ diverge, por lo que según el [criterio de comparación](#criterio-de-comparación), $\sum \cfrac{1}{n^p}$ también diverge.

#### Conclusión
Por i) y ii), la serie p $\sum \cfrac{1}{n^p}$ converge si $p>1$ y diverge si $p \leq 1$. $\blacksquare$

## Criterio de comparación
El **criterio de comparación (Comparison Test)** de Jakob Bernoulli es útil para determinar la convergencia o divergencia de **series de términos positivos (series of positive terms)**, que son series cuyos términos generales son números reales no negativos.

Una serie de términos positivos $\sum a_n$ forma una sucesión creciente, por lo que si no diverge a infinito ($\sum a_n = \infty$), entonces necesariamente converge. Por lo tanto, en series de términos positivos, la expresión:

$$ \sum a_n < \infty $$

significa que <u>la serie converge</u>.

> **Criterio de comparación (Comparison Test)**  
> Si $0 \leq a_n \leq b_n$, entonces:  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

En particular, para series de términos positivos como $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, que tienen formas similares a las series geométricas $\sum ar^{n-1}$ o series p $\sum \cfrac{1}{n^p}$ que vimos anteriormente, es recomendable intentar aplicar el criterio de comparación.

Muchos de los otros criterios de convergencia/divergencia que veremos más adelante pueden derivarse de este **criterio de comparación**, lo que lo hace particularmente importante.

### Criterio de comparación por límite
Para series de términos positivos $\sum a_n$ y $\sum b_n$, si el cociente de sus términos generales $a_n/b_n$ tiene un límite $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c$ (donde $c$ es un número positivo finito) debido a la cancelación de términos dominantes en el numerador y denominador, y conocemos la convergencia o divergencia de la serie $\sum b_n$, podemos utilizar el siguiente **criterio de comparación por límite (Limit Comparison Test)**.

> **Criterio de comparación por límite (Limit Comparison Test)**  
> Si:
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (donde }c\text{ es un número positivo finito)}$$
>
> entonces ambas series $\sum a_n$ y $\sum b_n$ convergen o ambas divergen. Es decir, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Criterio de la raíz
> **Teorema**  
> Para una serie de términos positivos $\sum a_n$ y un número positivo $\epsilon < 1$:  
> - Si $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, entonces la serie $\sum a_n$ converge
> - Si $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, entonces la serie $\sum a_n$ diverge
{: .prompt-info }

> **Corolario: Criterio de la raíz (Root Test)**  
> Para una serie de términos positivos $\sum a_n$, si existe el límite:
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> Entonces:
> - Si $r<1$, la serie $\sum a_n$ converge
> - Si $r>1$, la serie $\sum a_n$ diverge
{: .prompt-info }

> En el corolario anterior, si $r=1$, no podemos determinar la convergencia o divergencia, por lo que debemos usar otro método.
{: .prompt-warning }

## Criterio del cociente
> **Criterio del cociente (Ratio Test)**  
> Para una sucesión de números positivos $(a_n)$ y $0 < r < 1$:
> - Si $a_{n+1}/a_n \leq r$ para todo $n$, entonces la serie $\sum a_n$ converge
> - Si $a_{n+1}/a_n \geq 1$ para todo $n$, entonces la serie $\sum a_n$ diverge
{: .prompt-info }

> **Corolario**  
> Para una sucesión de números positivos $(a_n)$, si existe el límite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$:
> - Si $\rho < 1$, entonces la serie $\sum a_n$ converge
> - Si $\rho > 1$, entonces la serie $\sum a_n$ diverge
{: .prompt-info }

## Criterio de la integral
El cálculo integral puede utilizarse para determinar la convergencia o divergencia de series compuestas por sucesiones decrecientes de términos positivos.

> **Criterio de la integral (Integral Test)**  
> Si $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ es una función continua, decreciente y siempre $f(x)>0$, entonces la serie $\sum f(n)$ converge si y solo si la integral:
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converge.
{: .prompt-info }

### Demostración
Si la función $f(x)$ es continua, decreciente y siempre positiva, entonces se cumple la desigualdad:

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

Sumando esta desigualdad desde $n=1$ hasta el término general, obtenemos:

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Aplicando el [criterio de comparación](#criterio-de-comparación), obtenemos el resultado deseado. $\blacksquare$

## Series alternadas
Una **serie alternada (alternating series)** es una serie $\sum a_n$ cuyos términos $a_n$ no son cero y tienen signos alternados, es decir, el signo de cada término $a_n$ es diferente al del siguiente término $a_{n+1}$.

Para las series alternadas, el siguiente teorema descubierto por el matemático alemán Gottfried Wilhelm Leibniz puede ser útil para determinar su convergencia o divergencia.

> **Criterio de las series alternadas (Alternating Series Test)**  
> Si:
> 1. Los signos de $a_n$ y $a_{n+1}$ son diferentes para todo $n$,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$, y
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> entonces la serie alternada $\sum a_n$ converge.
{: .prompt-info }

## Series absolutamente convergentes
Se dice que una serie $\sum a_n$ **converge absolutamente (converge absolutely)** si la serie $\sum \|a_n\|$ converge.

En este caso, se cumple el siguiente teorema:

> **Teorema**  
> Una serie absolutamente convergente es convergente.
{: .prompt-info }

> El recíproco del teorema anterior no es cierto.  
> Cuando una serie converge pero no converge absolutamente, se dice que **converge condicionalmente (converge conditionally)**.
{: .prompt-warning }

### Demostración
Para un número real $a$, definimos:

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Entonces:

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Como $0 \leq a^\pm \leq \|a\|$, por el [criterio de comparación](#criterio-de-comparación), si la serie $\sum \|a_n\|$ converge, entonces las series $\sum a_n^+$ y $\sum a_n^-$ también convergen, y por las [propiedades básicas de las series convergentes](/posts/sequences-and-series/#propiedades-básicas-de-las-series-convergentes):

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

también converge. $\blacksquare$
