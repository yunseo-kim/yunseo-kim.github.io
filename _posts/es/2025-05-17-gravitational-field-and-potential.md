---
title: El campo gravitatorio y el potencial gravitatorio
description: "Exploramos la definición del vector de campo gravitatorio y el potencial gravitatorio según la ley de gravitación universal de Newton, y abordamos dos ejemplos importantes relacionados: el teorema de la cáscara esférica y las curvas de rotación galáctica."
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Ley de gravitación universal de Newton: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Para distribuciones continuas de masa y objetos con tamaño: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: densidad de masa en el punto ubicado en el vector de posición $\mathbf{r^{\prime}}$ desde un origen arbitrario
>   - $dv^{\prime}$: elemento de volumen en el punto ubicado en el vector de posición $\mathbf{r^{\prime}}$ desde un origen arbitrario
> - **Vector de campo gravitatorio (gravitational field vector)**:
>   - Vector que representa la fuerza por unidad de masa que experimenta una partícula en un campo creado por un objeto de masa $M$
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - Tiene dimensiones de *fuerza por unidad de masa* o *aceleración*
> - **Potencial gravitatorio (gravitational potential)**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - Tiene dimensiones de *fuerza por unidad de masa* $\times$ *distancia* o *energía por unidad de masa*
>   - $\Phi = -G\cfrac{M}{r}$
>   - Solo las diferencias relativas del potencial gravitatorio tienen significado, no su valor absoluto
>   - Normalmente se elimina la ambigüedad estableciendo arbitrariamente la condición de que $\Phi \to 0$ cuando $r \to \infty$
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Potencial gravitatorio dentro y fuera de una cáscara esférica (teorema de la cáscara)**
>   - Para $R>a$:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - Al calcular el potencial gravitatorio en un punto exterior a una distribución esféricamente simétrica de materia, se puede considerar el objeto como una masa puntual
>   - Para $R<b$:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - Dentro de una cáscara de masa esféricamente simétrica, el potencial gravitatorio es constante independientemente de la posición, y la gravedad resultante es $0$
>   - Para $b<R<a$: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## El campo gravitatorio
### Ley de gravitación universal de Newton
Newton ya había sistematizado la ley de gravitación universal y la había verificado numéricamente antes de 11666 HE. Sin embargo, tardó 20 años más en publicar sus resultados en su obra *Principia* en 11687 HE, porque no podía justificar el método de cálculo que asumía que la Tierra y la Luna eran masas puntuales sin tamaño. Afortunadamente, [usando el cálculo que el propio Newton inventó posteriormente, podemos demostrar ese problema mucho más fácilmente que lo que le resultó a Newton en el siglo XVII](#para-ra).

Según la ley de gravitación universal de Newton, *cada partícula de materia atrae a todas las demás partículas del universo con una fuerza directamente proporcional al producto de sus masas e inversamente proporcional al cuadrado de la distancia entre ellas*. Matemáticamente, esto se expresa como:

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - Licencia: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

El vector unitario $\mathbf{e}_r$ apunta desde $M$ hacia $m$, y el signo negativo indica que la fuerza es atractiva. Es decir, $m$ es atraída hacia $M$.

### El experimento de Cavendish
La verificación experimental de esta ley y la determinación del valor de $G$ fueron realizadas por el físico británico Henry Cavendish en 11798 HE. El experimento de Cavendish utiliza una balanza de torsión compuesta por dos pequeñas esferas fijadas en los extremos de una varilla ligera. Estas dos esferas son atraídas hacia otras dos esferas más grandes situadas cerca de ellas. El valor oficial de $G$ obtenido hasta ahora es $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> A pesar de ser una de las constantes fundamentales conocidas desde hace más tiempo, $G$ se conoce con menor precisión que la mayoría de las otras constantes fundamentales como $e$, $c$ y $\hbar$. Incluso hoy, se realizan muchas investigaciones para determinar el valor de $G$ con mayor precisión.
{: .prompt-tip }

### Para objetos con tamaño
La ley expresada en la ecuación ($\ref{eqn:law_of_gravitation}$) solo se aplica estrictamente a *partículas puntuales*. Si uno o ambos objetos tienen cierto tamaño, se debe hacer la suposición adicional de que el campo gravitatorio es un *campo lineal* para calcular la fuerza. Es decir, se asume que la fuerza gravitatoria total que actúa sobre una partícula de masa $m$ debido a varias otras partículas puede obtenerse sumando vectorialmente cada fuerza individual. Para objetos con distribución continua de materia, la suma se convierte en una integral:

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: densidad de masa en el punto ubicado en el vector de posición $\mathbf{r^{\prime}}$ desde un origen arbitrario
- $dv^{\prime}$: elemento de volumen en el punto ubicado en el vector de posición $\mathbf{r^{\prime}}$ desde un origen arbitrario

Si tanto el objeto de masa $M$ como el de masa $m$ tienen tamaño, se necesitaría una segunda integral de volumen sobre $m$ para calcular la fuerza gravitatoria total.

### Vector de campo gravitatorio
El **vector de campo gravitatorio (gravitational field vector)** $\mathbf{g}$ se define como el vector que representa la fuerza por unidad de masa que experimenta una partícula en un campo creado por un objeto de masa $M$:

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

o

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

donde la dirección de $\mathbf{e}_r$ varía según $\mathbf{r^\prime}$.

Esta cantidad $\mathbf{g}$ tiene dimensiones de *fuerza por unidad de masa* o *aceleración*. La magnitud del vector de campo gravitatorio $\mathbf{g}$ cerca de la superficie terrestre es igual a lo que llamamos **constante de aceleración gravitatoria**, con un valor aproximado de $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$.

## Potencial gravitatorio
### Definición
El vector de campo gravitatorio $\mathbf{g}$ varía como $1/r^2$, por lo que satisface la condición ($\nabla \times \mathbf{g} \equiv 0$) para ser expresado como el gradiente de una función escalar (potencial). Por lo tanto, podemos escribir:

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

donde $\Phi$ es el **potencial gravitatorio (gravitational potential)**, que tiene dimensiones de *fuerza por unidad de masa* $\times$ *distancia* o *energía por unidad de masa*.

Como $\mathbf{g}$ solo depende del radio, $\Phi$ también varía con $r$. A partir de las ecuaciones ($\ref{eqn:g_vector}$) y ($\ref{eqn:gradient_phi}$):

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

Integrando, obtenemos:

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

Podemos omitir la constante de integración porque solo las diferencias relativas del potencial gravitatorio tienen significado, no su valor absoluto. Normalmente se elimina la ambigüedad estableciendo arbitrariamente la condición de que $\Phi \to 0$ cuando $r \to \infty$, y la ecuación ($\ref{eqn:g_potential}$) satisface esta condición.

Para una distribución continua de materia, el potencial gravitatorio es:

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Para una distribución superficial de masa en una cáscara delgada:

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

Y para una fuente de masa lineal con densidad lineal $\rho_l$:

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Significado físico
Consideremos el trabajo por unidad de masa $dW^\prime$ realizado cuando un objeto se mueve una distancia $d\mathbf{r}$ en un campo gravitatorio:

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

En esta ecuación, $\Phi$ es una función solo de las coordenadas de posición, expresada como $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Por lo tanto, el trabajo por unidad de masa realizado al mover un objeto de un punto a otro en un campo gravitatorio es igual a la diferencia de potencial entre esos dos puntos.

Si definimos el potencial gravitatorio como cero en el infinito, entonces $\Phi$ en cualquier punto puede interpretarse como el trabajo por unidad de masa necesario para mover el objeto desde ese punto hasta el infinito. La energía potencial de un objeto es el producto de su masa y el potencial gravitatorio $\Phi$, por lo que si $U$ es la energía potencial:

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

Por lo tanto, la fuerza gravitatoria que actúa sobre un objeto se obtiene como el gradiente negativo de su energía potencial:

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Cuando un objeto se encuentra en un campo gravitatorio creado por una masa, siempre existe una energía potencial asociada. Estrictamente hablando, esta energía potencial reside en el campo mismo, aunque convencionalmente se refiere a ella como la energía potencial del objeto.

## Ejemplo: Potencial gravitatorio dentro y fuera de una cáscara esférica (Teorema de la cáscara)
### Configuración de coordenadas y expresión del potencial gravitatorio como integral
Calculemos el potencial gravitatorio dentro y fuera de una cáscara esférica uniforme con radio interno $b$ y radio externo $a$. Aunque la fuerza gravitatoria debida a la cáscara podría calcularse directamente sumando las componentes de fuerza que actúan sobre una unidad de masa en el campo, el método del potencial es más sencillo.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Calculemos el potencial en el punto $P$ a una distancia $R$ del centro. Asumiendo una distribución uniforme de masa en la cáscara, $\rho(r^\prime)=\rho$, y debido a la simetría respecto al ángulo azimutal $\phi$ alrededor de la línea que conecta el centro de la esfera y el punto $P$:

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

Según la ley del coseno:

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

Como $R$ es constante, diferenciando esta ecuación respecto a $r^\prime$:

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

Sustituyendo en la ecuación ($\ref{eqn:spherical_shell_1}$):

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

donde $r_\mathrm{max}$ y $r_\mathrm{min}$ dependen de la posición del punto $P$.

### Para $R>a$
$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

La masa $M$ de la cáscara esférica es:

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

Por lo tanto, el potencial es:

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> Comparando el resultado que acabamos de obtener ($\ref{eqn:spherical_shell_outside_2}$) con la ecuación del potencial gravitatorio debido a una masa puntual $M$ ($\ref{eqn:g_potential}$), vemos que son idénticos. Esto significa que al calcular el potencial gravitatorio en un punto exterior a una distribución esféricamente simétrica de materia, podemos considerar que toda la masa está concentrada en el centro. La mayoría de los cuerpos celestes esféricos como la Tierra o la Luna entran en esta categoría, ya que pueden considerarse como innumerables cáscaras esféricas concéntricas de diferentes diámetros, como una [matrioshka](https://en.wikipedia.org/wiki/Matryoshka_doll). Esto proporciona [la justificación para tratar cuerpos celestes como la Tierra o la Luna como masas puntuales sin tamaño](#ley-de-gravitación-universal-de-newton) mencionada al principio de este artículo.
{: .prompt-info }

### Para $R<b$
$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> Dentro de una cáscara de masa esféricamente simétrica, el potencial gravitatorio es constante independientemente de la posición, y la gravedad resultante es $0$.
{: .prompt-info }

> Esto también es una de las principales razones por las que la "Teoría de la Tierra Hueca", una conocida pseudociencia, es absurda. Si la Tierra fuera una cáscara esférica con un interior hueco, como afirma esta teoría, la gravedad no actuaría sobre ningún objeto dentro de esa cavidad. Considerando la masa y el volumen de la Tierra, no solo es imposible que exista tal cavidad, sino que incluso si existiera, los seres vivos allí no estarían caminando sobre la superficie interior de la cáscara, sino flotando en un estado de ingravidez como en una estación espacial.  
> [Aunque pueden existir microorganismos a varios kilómetros de profundidad en las capas terrestres](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), esto no es posible en la forma que sugiere la Teoría de la Tierra Hueca. Me encantan la novela de Julio Verne "Viaje al centro de la Tierra" y la película "Viaje al centro de la Tierra", pero disfrutémoslas como obras de ficción sin creer seriamente en ellas.
{: .prompt-tip }

### Para $b<R<a$
$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Resultados
Los siguientes gráficos muestran el potencial gravitatorio $\Phi$ y la magnitud del vector de campo gravitatorio $\|\mathbf{g}\|$ como funciones de la distancia $R$ en las tres regiones que hemos calculado:

![Gravitational Potential as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-gravitational-potential.png)
![Magnitude of the Field Vector as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-field-vector.png)
> - Código de visualización en Python: [Repositorio yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/shell_theorem.py)
> - Licencia: [Ver aquí](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

Podemos observar que tanto el potencial gravitatorio como la magnitud del vector de campo gravitatorio son continuos. Si el potencial gravitatorio fuera discontinuo en algún punto, la magnitud de la gravedad (el gradiente del potencial) sería infinita en ese punto, lo cual no es físicamente plausible, por lo que la función potencial debe ser continua en todos los puntos. Sin embargo, la *derivada* del vector de campo gravitatorio es discontinua en las superficies interior y exterior de la cáscara.

## Ejemplo: Curvas de rotación galáctica
Según las observaciones astronómicas, la mayor parte de la masa observable en muchas galaxias espirales que rotan alrededor de su centro, como nuestra Vía Láctea o la galaxia de Andrómeda, se concentra cerca del núcleo. Sin embargo, como se puede ver en el siguiente gráfico, las velocidades orbitales de las masas en estas galaxias espirales difieren significativamente de las predicciones teóricas basadas en la distribución de masa observable, y permanecen casi constantes más allá de cierta distancia.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - Licencia: Dominio Público

![Rotation Curve of Spiral Galaxy M33](https://upload.wikimedia.org/wikipedia/commons/c/cd/Rotation_curve_of_spiral_galaxy_Messier_33_%28Triangulum%29.png)
> **Curva de rotación de la galaxia espiral M33 (Galaxia del Triángulo)**
> - Autor: Usuario de Wikimedia [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama)
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Vamos a predecir la velocidad orbital en función de la distancia para el caso en que la masa de la galaxia esté concentrada en el núcleo, verificar que esta predicción no coincide con las observaciones, y demostrar que la masa $M(R)$ distribuida dentro de la distancia $R$ desde el centro de la galaxia debe ser proporcional a $R$ para explicar los resultados observados.

Primero, si la masa $M$ de la galaxia está concentrada en el núcleo, la velocidad orbital a una distancia $R$ sería:

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

En este caso, se predice una velocidad orbital que disminuye como $1/\sqrt{R}$, como se muestra en las líneas punteadas de los dos gráficos anteriores. Sin embargo, según las observaciones, la velocidad orbital $v$ es casi constante independientemente de la distancia $R$, lo que contradice esta predicción. Este resultado observacional solo puede explicarse si $M(R)\propto R$.

Si escribimos $M(R) = kR$ con una constante de proporcionalidad $k$:

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(constante)}. $$

A partir de esto, los astrofísicos concluyen que debe existir "materia oscura" (dark matter) no detectada en muchas galaxias, y que esta materia oscura debe constituir más del 90% de la masa del universo. Sin embargo, la naturaleza exacta de la materia oscura aún no se ha determinado claramente, y aunque no es la teoría dominante, existen intentos como la Dinámica Newtoniana Modificada (Modified Newtonian Dynamics, MOND) que tratan de explicar los resultados observados sin asumir la existencia de materia oscura. Hoy en día, estos campos de investigación están en la vanguardia de la astrofísica.
