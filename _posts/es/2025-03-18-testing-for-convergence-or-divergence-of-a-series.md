---
title: Prueba de convergencia/divergencia de series (Testing for Convergence or Divergence of a Series)
description: Examinamos varios métodos para determinar la convergencia/divergencia de series.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Prueba del término n-ésimo para divergencia**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la serie }\sum a_n \text{ diverge}$
> - **Convergencia/divergencia de series geométricas**: La serie geométrica $\sum ar^{n-1}$
>   - converge si $\|r\| < 1$
>   - diverge si $\|r\| \geq 1$
> - **Convergencia/divergencia de series p**: La serie p $\sum \cfrac{1}{n^p}$
>   - converge si $p>1$
>   - diverge si $p\leq 1$
> - **Prueba de comparación**: Si $0 \leq a_n \leq b_n$, entonces  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Prueba del límite de comparación**: Si $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ es un número positivo finito)}$, entonces las dos series $\sum a_n$ y $\sum b_n$ convergen o divergen juntas
> - Para una serie de términos positivos $\sum a_n$ y un número positivo $\epsilon < 1$  
>   - Si $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, entonces la serie $\sum a_n$ converge
>   - Si $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, entonces la serie $\sum a_n$ diverge
> - **Prueba de la raíz**: Para una serie de términos positivos $\sum a_n$, si existe el límite $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$,
>   - Si $r<1$, entonces la serie $\sum a_n$ converge
>   - Si $r>1$, entonces la serie $\sum a_n$ diverge
> - **Prueba del cociente**: Para una sucesión de números positivos $(a_n)$ y $0 < r < 1$
>   - Si $a_{n+1}/a_n \leq r$ para todo $n$, entonces la serie $\sum a_n$ converge
>   - Si $a_{n+1}/a_n \geq 1$ para todo $n$, entonces la serie $\sum a_n$ diverge
> - Para una sucesión de números positivos $(a_n)$, si existe el límite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$,
>   - Si $\rho < 1$, entonces la serie $\sum a_n$ converge
>   - Si $\rho > 1$, entonces la serie $\sum a_n$ diverge
> - **Prueba de la integral**: Si $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ es una función continua, decreciente y siempre positiva, entonces la serie $\sum f(n)$ converge si y solo si la integral $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converge
> - **Prueba de series alternantes**: Una serie alternante $\sum a_n$ converge si se cumplen las siguientes condiciones:
>   1. $a_n$ y $a_{n+1}$ tienen signos opuestos para todo $n$
>   2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Una serie que converge absolutamente también converge. Lo contrario no es necesariamente cierto.
{: .prompt-info }

## Prerrequisitos
- [Sucesiones y series](/posts/sequences-and-series/)

## Introducción
Anteriormente, en [Sucesiones y series](/posts/sequences-and-series/#convergencia-y-divergencia-de-series), vimos la definición de convergencia y divergencia de series. En este artículo, resumiremos varios métodos que se pueden utilizar para determinar la convergencia/divergencia de series. En general, determinar la convergencia/divergencia de una serie es mucho más fácil que calcular su suma exacta.

## Prueba del término n-ésimo
Para una serie $\sum a_n$, $a_n$ se denomina el **término general** de dicha serie.

El siguiente teorema nos permite saber fácilmente que algunas series divergen obviamente, por lo que es prudente verificar esto primero al determinar la convergencia/divergencia de una serie para evitar perder tiempo.

> **Prueba del término n-ésimo para divergencia**  
> Si una serie $\sum a_n$ converge, entonces
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Es decir,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la serie }\sum a_n \text{ diverge} $$
{: .prompt-info }

### Demostración
Sea $l$ la suma de una serie convergente $\sum a_n$ y sea $s_n$ la suma de los primeros $n$ términos:

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Entonces,

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Por lo tanto, para $n$ suficientemente grande ($>N$)

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Así, por la definición de convergencia de sucesiones,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Precaución
El recíproco de este teorema generalmente no es cierto. Un ejemplo típico que lo demuestra es la **serie armónica**.

La serie armónica es una serie obtenida de una sucesión cuyos términos son los recíprocos de una **progresión aritmética**, es decir, una **sucesión armónica**. La serie armónica típica es

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Se puede demostrar que esta serie diverge de la siguiente manera:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Como se puede ver, aunque la serie $H_n$ diverge, el término general $1/n$ converge a $0$.

> Si $\lim_{n\to\infty} a_n \neq 0$, entonces la serie $\sum a_n$ definitivamente diverge, pero es peligroso pensar que la serie $\sum a_n$ convergerá si $\lim_{n\to\infty} a_n = 0$. En este caso, se deben usar otros métodos para determinar la convergencia/divergencia.
{: .prompt-danger }

## Series geométricas
La **serie geométrica** obtenida de una progresión geométrica con primer término 1 y **razón** $r$

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

es <u>la serie más importante y fundamental</u>. De la igualdad

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

obtenemos

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Por otro lado,

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

por lo que sabemos que la condición necesaria y suficiente para que la serie geométrica ($\ref{eqn:geometric_series}$) converja es $\|r\| < 1$.

> **Convergencia/divergencia de series geométricas**  
> La serie geométrica $\sum ar^{n-1}$
> - converge si $\|r\| < 1$
> - diverge si $\|r\| \geq 1$
{: .prompt-info }

De esto obtenemos

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Series geométricas y valores aproximados
La identidad ($\ref{eqn:sum_of_geometric_series}$) es útil para encontrar valores aproximados de $\cfrac{1}{1-r}$ cuando $\|r\| < 1$.

Sustituyendo $r=-\epsilon$, $n=2$ en esta ecuación, obtenemos

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Por lo tanto, si $0 < \epsilon < 1$

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

así que obtenemos

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

De esto, podemos ver que para un número positivo $\epsilon$ suficientemente pequeño, $\cfrac{1}{1 + \epsilon}$ se puede aproximar por $1 - \epsilon$.

## Prueba de series p (Prueba de series p)  
Para un número real positivo $p$, una serie de la siguiente forma se llama **serie p**:

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Convergencia/divergencia de series p**  
> La serie p $\sum \cfrac{1}{n^p}$
> - converge si $p>1$
> - diverge si $p\leq 1$
{: .prompt-info }

En el caso de $p=1$ en una serie p, se convierte en la serie armónica, que ya hemos demostrado que diverge.  
El problema de encontrar el valor de la serie p cuando $p=2$, es decir, $\sum \cfrac{1}{n^2}$, se llama el 'problema de Basilea', nombrado así por la ciudad base de la familia Bernoulli, que demostró por primera vez que esta serie converge y produjo varios matemáticos famosos a lo largo de varias generaciones. Se sabe que la respuesta a este problema es $\cfrac{\pi^2}{6}$.

Más generalmente, la serie p para $p>1$ se llama **función zeta**. Esta es una función especial introducida por Leonhard Euler en el año 11740 del [calendario de la era humana](https://en.wikipedia.org/wiki/Holocene_calendar) y posteriormente nombrada por Riemann, definida como

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Esto se desvía un poco del tema de este artículo y, para ser honesto, como soy un estudiante de ingeniería y no un matemático, no lo sé muy bien, así que no lo trataré aquí, pero Leonhard Euler demostró que la función zeta también se puede expresar como un producto infinito de números primos llamado **producto de Euler**, y posteriormente la función zeta ocupa una posición central en varios campos de la teoría analítica de números. La **función zeta de Riemann**, que extiende el dominio de la función zeta a los números complejos, y la importante conjetura no resuelta relacionada con ella, la **hipótesis de Riemann**, son ejemplos de ello.

Volviendo al tema original, la demostración de la prueba de series p requiere la [prueba de comparación](#prueba-de-comparación) y la [prueba de la integral](#prueba-de-la-integral) que se discutirán más adelante. Sin embargo, la convergencia/divergencia de las series p puede ser útil en la [prueba de comparación](#prueba-de-comparación) que se discutirá justo después de las series geométricas, por lo que se ha colocado intencionalmente hacia el principio.

### Demostración
#### i) Cuando $p>1$
La integral

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converge, por lo que por la [prueba de la integral](#prueba-de-la-integral), sabemos que la serie $\sum \cfrac{1}{n^p}$ también converge.

#### ii) Cuando $p\leq 1$
En este caso

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Aquí sabemos que la serie armónica $\sum \cfrac{1}{n}$ diverge, por lo que por la [prueba de comparación](#prueba-de-comparación), sabemos que $\sum \cfrac{1}{n^p}$ también diverge.

#### Conclusión
Por i) y ii), la serie p $\sum \cfrac{1}{n^p}$ converge si $p>1$ y diverge si $p \leq 1$. $\blacksquare$

## Prueba de comparación
La **prueba de comparación** de Jakob Bernoulli es útil para determinar la convergencia/divergencia de **series de términos positivos**, que son series cuyos términos generales son números reales no negativos.

Como una serie de términos positivos $\sum a_n$ es una sucesión creciente, si no diverge a infinito ($\sum a_n = \infty$), debe converger. Por lo tanto, en una serie de términos positivos, la expresión

$$ \sum a_n < \infty $$

significa que <u>converge</u>.

> **Prueba de comparación**  
> Si $0 \leq a_n \leq b_n$, entonces  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

En particular, para series de términos positivos como $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, que tienen formas similares a las series geométricas $\sum ar^{n-1}$ o las series p $\sum \cfrac{1}{n^p}$ que vimos anteriormente, es bueno intentar activamente la prueba de comparación para determinar su convergencia/divergencia.

Todas las demás pruebas de convergencia/divergencia que se discutirán más adelante se pueden derivar de esta **prueba de comparación**, y en ese sentido, se puede decir que la prueba de comparación es la más importante.

### Prueba del límite de comparación
Para series de términos positivos $\sum a_n$ y $\sum b_n$, supongamos que el término dominante en el numerador y el denominador de la razón de los términos generales de las dos series $a_n/b_n$ se cancela, resultando en $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ es un número positivo finito)}$. Si conocemos la convergencia/divergencia de la serie $\sum b_n$, podemos utilizar la siguiente **prueba del límite de comparación**.

> **Prueba del límite de comparación**  
> Si
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ es un número positivo finito)}$$
>
> entonces las dos series $\sum a_n$ y $\sum b_n$ convergen o divergen juntas. Es decir, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Prueba de la raíz
> **Teorema**  
> Para una serie de términos positivos $\sum a_n$ y un número positivo $\epsilon < 1$  
> - Si $\sqrt[n]{a_n}< 1-\epsilon$ para todo $n$, entonces la serie $\sum a_n$ converge
> - Si $\sqrt[n]{a_n}> 1+\epsilon$ para todo $n$, entonces la serie $\sum a_n$ diverge
{: .prompt-info }

> **Corolario: Prueba de la raíz**  
> Para una serie de términos positivos $\sum a_n$, supongamos que existe el límite
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> Entonces
> - Si $r<1$, la serie $\sum a_n$ converge
> - Si $r>1$, la serie $\sum a_n$ diverge
{: .prompt-info }

> En el corolario anterior, si $r=1$, no se puede determinar la convergencia/divergencia, por lo que se debe usar otro método.
{: .prompt-warning }

## Prueba del cociente
> **Prueba del cociente**  
> Para una sucesión de números positivos $(a_n)$ y $0 < r < 1$
> - Si $a_{n+1}/a_n \leq r$ para todo $n$, entonces la serie $\sum a_n$ converge
> - Si $a_{n+1}/a_n \geq 1$ para todo $n$, entonces la serie $\sum a_n$ diverge
{: .prompt-info }

> **Corolario**  
> Para una sucesión de números positivos $(a_n)$, supongamos que existe el límite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$. Entonces
> - Si $\rho < 1$, la serie $\sum a_n$ converge
> - Si $\rho > 1$, la serie $\sum a_n$ diverge
{: .prompt-info }

## Prueba de la integral
Usando el cálculo integral, podemos determinar la convergencia/divergencia de series compuestas por sucesiones decrecientes de términos positivos.

> **Prueba de la integral**  
> Si $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ es una función continua, decreciente y siempre positiva, entonces la serie $\sum f(n)$ converge si y solo si la integral
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converge.
{: .prompt-info }

### Demostración
Como la función $f(x)$ es continua, decreciente y siempre positiva, se cumple la desigualdad

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

Sumando esta desigualdad desde $n=1$ hasta el término general, obtenemos la desigualdad

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Ahora, aplicando la [prueba de comparación](#prueba-de-comparación), obtenemos el resultado deseado. $\blacksquare$

## Series alternantes
Una serie $\sum a_n$ cuyos términos generales no son cero y el signo de cada término $a_n$ es diferente del signo del siguiente término $a_{n+1}$, es decir, una serie donde los términos positivos y negativos aparecen alternativamente, se llama **serie alternante**.

Para las series alternantes, el siguiente teorema descubierto por el matemático alemán Gottfried Wilhelm Leibniz puede ser útilmente aplicado para determinar la convergencia/divergencia.

> **Prueba de series alternantes**  
> Si
> 1. $a_n$ y $a_{n+1}$ tienen signos opuestos para todo $n$,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ para todo $n$, y
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> entonces la serie alternante $\sum a_n$ converge.
{: .prompt-info }

## Series absolutamente convergentes
Si para una serie $\sum a_n$, la serie $\sum \|a_n\|$ converge, se dice que "la serie $\sum a_n$ **converge absolutamente**".

En este caso, se cumple el siguiente teorema.

> **Teorema**  
> Una serie que converge absolutamente también converge.
{: .prompt-info }

> El recíproco del teorema anterior no es cierto.  
> Cuando una serie converge pero no converge absolutamente, se dice que "**converge condicionalmente**".
{: .prompt-warning }

### Demostración
Para un número real $a$, definimos

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Entonces obtenemos,

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Como $0 \leq a^\pm \leq \|a\|$, por la [prueba de comparación](#prueba-de-comparación), si la serie $\sum \|a_n\|$ converge, las series $\sum a_n^+$ y $\sum a_n^-$ también convergen, y por lo tanto, por las [propiedades básicas de las series convergentes](/posts/sequences-and-series/#propiedades-básicas-de-las-series-convergentes),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

también converge. $\blacksquare$
