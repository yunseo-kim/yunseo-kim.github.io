---
title: Método de separación de variables
description: Exploramos el método de separación de variables y presentamos algunos ejemplos relacionados.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## Método de separación de variables
**Ecuación separable**: Una ecuación que puede expresarse en la forma $g(y)y'=f(x)$ mediante manipulación algebraica.

Si integramos ambos lados de la ecuación separable $g(y)y'=f(x)$ con respecto a $x$, obtenemos:

$$ \int g(y)y'dx = \int f(x)dx + c $$ 

y como $y'dx=dy$, tenemos:

$$ \int g(y)dy = \int f(x)dx + c $$

De esta manera, podemos separar las expresiones en términos de la variable $x$ y la variable $y$ en los lados derecho e izquierdo respectivamente. Si $f$ y $g$ son funciones continuas, podemos calcular estas integrales para obtener la solución general de la ecuación diferencial dada. Este método de resolución se denomina **método de separación de variables**.

## Ejemplo de modelado: Datación por radiocarbono
Oetzi es una momia neolítica descubierta en los Alpes de Ötztal en el año 11991 del [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar). Si la proporción de carbono-14 respecto al carbono-12 en esta momia es el 52.5% de la de un organismo vivo, ¿aproximadamente cuándo vivió y murió Oetzi?
> La proporción de carbono-14 radiactivo respecto al carbono-12 es constante en la atmósfera y en los organismos vivos. Cuando un organismo muere, cesa la absorción de carbono-14 por respiración y alimentación, pero la desintegración del carbono-14 continúa, por lo que la proporción de carbono radiactivo disminuye. Por lo tanto, se puede estimar la edad de un fósil comparando su proporción de carbono radiactivo con la proporción atmosférica. La vida media del carbono-14 es de 5715 años.
{: .prompt-info }

### Solución
Si separamos las variables y integramos la ecuación diferencial ordinaria $y'=ky$, obtenemos:

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Para determinar la constante $k$, usamos la vida media $H=5715$:

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Finalmente, para encontrar el tiempo $t$ en que murió Oetzi, sustituimos la proporción de 52.5%:

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{Se estima que murió hace unos 5310 años, alrededor del año 6680 del calendario holoceno}. $$

## Ejemplo de modelado: Problema de mezcla
Inicialmente, un tanque contiene 1000L de agua con 10kg de sal disuelta. Una solución salina que contiene 0.2kg de sal por litro fluye hacia el tanque a una velocidad de 10L por minuto. La solución en el tanque se mantiene bien mezclada y uniforme, y sale del tanque a una velocidad de 10L por minuto. Encuentra la cantidad de sal $y(t)$ en el tanque en el tiempo $t$.

### 1. Establecimiento del modelo

$$ y'=\text{tasa de entrada} - \text{tasa de salida}. $$

La tasa de entrada de sal es 2kg por minuto. La tasa de salida de la solución salina es 0.01 del volumen total de la solución salina por minuto, por lo que la tasa de salida de sal es $0.01 y(t)$ por minuto. Por lo tanto, el modelo es la ecuación diferencial ordinaria:

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Resolución del modelo
La ecuación diferencial ordinaria que hemos establecido es separable. Separemos las variables, integremos y luego apliquemos la función exponencial a ambos lados:

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Inicialmente, la cantidad de sal en el tanque es 10kg, por lo que la condición inicial es $y(0)=10$. Sustituyendo $y=10,\ t=0$ en la ecuación anterior, obtenemos $10-200=ce^0=c$, por lo tanto $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Es decir, en la situación dada, la cantidad de sal en el tanque se acerca y converge exponencialmente a 200kg.

## Ejemplo de modelado: Ley de enfriamiento de Newton
Durante el día, la temperatura de un edificio de oficinas en invierno se mantiene a 20°C. La calefacción se apaga a las 10 PM y se vuelve a encender a las 6 AM. Un día, a las 2 AM, la temperatura interior del edificio era de 17.4°C. La temperatura exterior era de 10°C a las 10 PM y bajó a 4°C a las 6 AM. ¿Cuál era la temperatura interior del edificio cuando se encendió la calefacción a las 6 AM?
> **Ley de enfriamiento de Newton**  
> La tasa de cambio de la temperatura T de un objeto con respecto al tiempo es proporcional a la diferencia entre la temperatura del objeto y la temperatura de sus alrededores.
{: .prompt-info }

### 1. Establecimiento del modelo
Sea $T(t)$ la temperatura interior del edificio y $T_A$ la temperatura exterior. Entonces, según la ley de enfriamiento de Newton:

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Solución general
Como solo sabemos que $T_A$ varía entre 10°C y 4°C, pero no conocemos su valor exacto, no podemos resolver la ecuación que acabamos de establecer. En estos casos, *puede ser útil intentar resolver simplificando la situación a un problema más sencillo*. El promedio de los dos valores conocidos es 7°C, así que asumamos que la función desconocida $T_A$ es una función constante $T_A=7$. Aunque no sea exacto, podemos esperar obtener un valor aproximado de la temperatura interior del edificio $T$ a las 6 AM, que es lo que buscamos.

Para la constante $T_A=7$, la ecuación diferencial ordinaria que establecimos anteriormente es separable. Separando las variables, integrando y aplicando la función exponencial, podemos obtener la solución general:

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Solución particular
Elijamos las 10 PM como $t=0$, entonces la condición inicial dada es $T(0)=20$. Llamemos $T_p$ a la solución particular que obtenemos en este caso. Sustituyendo:

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Determinación de $k$
Como la temperatura interior del edificio era de 17.4°C a las 2 AM, tenemos que $T(4)=17.4$. Resolviendo algebraicamente para $k$ y sustituyendo en $T_p(t)$:

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Respuesta e interpretación
Las 6 AM corresponden a $t=8$, por lo tanto:

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[°C]}. $$

## Ejemplo de modelado: Teorema de Torricelli
Un tanque tiene un diámetro de 2m y un orificio de 1cm de diámetro. La altura inicial del agua cuando se abre el orificio es de 2.25m. Encuentra la altura del agua en el tanque en cualquier momento y el tiempo que tarda en vaciarse el tanque.
> **Teorema de Torricelli**  
> La velocidad del agua que sale bajo la influencia de la gravedad es:
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: altura del agua sobre el orificio en el tiempo $t$
> $g=980\text{cm/s²}$: aceleración de la gravedad en la superficie terrestre
{: .prompt-info }

### 1. Establecimiento del modelo
El volumen de agua que sale en un corto período de tiempo $\Delta t$ es:

$$ \Delta V = Av\Delta t \qquad (A: \text{área del orificio})$$

Este $\Delta V$ debe ser igual al cambio de volumen $\Delta V^*$ dentro del tanque. Además:

$$ \Delta V^* = -B\Delta h \qquad (B: \text{área de la sección transversal del tanque}) $$

donde $\Delta h(>0)$ es la disminución en la altura del agua $h(t)$. Igualando $\Delta V$ y $\Delta V^*$:

$$ -B\Delta h = Av\Delta t $$

Ahora, expresando $v$ según el teorema de Torricelli y haciendo que $\Delta t$ se acerque a 0, obtenemos el siguiente modelo expresado como una ecuación diferencial ordinaria de primer orden:

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Solución general
Esta ecuación diferencial ordinaria es separable. Separando las variables e integrando:

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Dividiendo ambos lados por 2 y elevando al cuadrado, obtenemos $h=(c-13.28At/B)^2$. Sustituyendo $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$, obtenemos la solución general:

$$ h(t)=(c-0.000332t)^2 $$

### 3. Solución particular
La condición inicial es $h(0)=225\text{cm}$. Sustituyendo $t=0$ y $h=225$ en la solución general, obtenemos $c^2=225, c=15.00$, y por lo tanto la solución particular:

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Tiempo que tarda en vaciarse el tanque

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Transformación a forma separable
En algunos casos, es posible transformar una ecuación diferencial ordinaria no separable en una separable introduciendo una nueva función desconocida de $y$.

$$ y'=f\left(\frac {y}{x}\right). $$

Para resolver una ecuación diferencial ordinaria de este tipo, ponemos $y/x=u$, entonces:

$$ y=ux,\quad y'=u'x+u $$

Sustituyendo en $y'=f(y/x)$, obtenemos $u'x=f(u)-u$. Si $f(u)-u\neq0$, entonces:

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$

que está separada.
