---
title: "Cálculo del Equilibrio Radiactivo"
description: >-
  Exploramos la relación entre la constante de decaimiento, la vida media y la vida promedio de los radionucleidos, y calculamos la actividad de los radionucleidos en un tiempo t dado para una cadena de decaimiento específica.
categories: [Ingeniería Física, Ingeniería Nuclear]
tags: [Física Nuclear, Decaimiento Radiactivo]
math: true
mermaid: true
---

## TL;DR
> **Actividad en un tiempo t arbitrario**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **Relación entre la constante de decaimiento, la vida media y la vida promedio**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## Constante de Decaimiento
- Probabilidad de que un núcleo decaiga por unidad de tiempo
- Constante independiente del tiempo, determinada solo por el tipo de nucleido
- Representada por el símbolo $\lambda$

## Radiactividad
Si n(t) es el número de núcleos que aún no han decaído en el tiempo t, entonces en promedio $\lambda n(t)$ núcleos decaerán durante el intervalo dt entre t y t+dt. Esta tasa de decaimiento se llama *radiactividad* de la muestra y se representa con el símbolo $\alpha$. Por lo tanto, la radiactividad en un tiempo t dado es:

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## Unidades de Radiactividad
### Curie (Ci)
- Unidad tradicionalmente utilizada antes del becquerel
- Radiactividad de 1g de radio-226
- $3.7\times 10^{10}$ desintegraciones nucleares por segundo ($3.7\times 10^{10}\text{Bq}$)

### Becquerel (Bq)
- Unidad estándar internacional (SI)
- Una desintegración nuclear por segundo
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## Cálculo del Cambio de Radiactividad con el Tiempo
Como $\lambda n(t)$ núcleos decaen durante dt, la disminución en el número de núcleos que permanecen sin decaer en la muestra durante dt se puede expresar como:

$$ -dn(t)=\lambda n(t)dt $$

Integrando esto, obtenemos:

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

Multiplicando ambos lados por $\lambda$, la radiactividad es:

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

Como la radiactividad se reduce a la mitad durante la *vida media*:

$$ \alpha (T_{1/2})=\alpha_0/2 $$

Sustituyendo esto en la ecuación (3):

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

Tomando el logaritmo de ambos lados y resolviendo para la vida media $T_{1/2}$:

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

Resolviendo esta ecuación para $\lambda$ y sustituyendo en la ecuación (3):

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

La ecuación (5) es a menudo más útil para los cálculos de decaimiento radiactivo que la ecuación (3), ya que es más común que se proporcionen valores de vida media que constantes de decaimiento.

La *vida promedio* $\overline{t}$ de un núcleo radiactivo es el inverso de la constante de decaimiento:

$$ \overline{t}=1/\lambda $$

De la ecuación (3), podemos ver que durante una vida promedio, la radiactividad cae a $1/e$ de su valor inicial. De la ecuación (4), la relación entre la vida promedio y la vida media es:

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ Derivación de la vida promedio $\overline{t}$

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## Ejemplo: Cadena de Decaimiento Radiactivo 1
Supongamos que un radionucleido se produce a una tasa de R átomos/s. Estos núcleos comienzan a decaer radiactivamente tan pronto como se forman. Calcula la radiactividad de este nucleido en un tiempo t arbitrario.
```mermaid
flowchart LR
	Start[?] -- R --> A[Modelo matemático]
	A -- α --> End[?]
```

### 1. Establecimiento del modelo

$$ \text{Tasa de cambio del nucleido} = \text{Tasa de producción} - \text{Tasa de pérdida} $$

En notación matemática:

$$ dn/dt = -\lambda n + R $$

### 2. Solución general
Movamos todos los términos relacionados con n al lado izquierdo y multipliquemos ambos lados por $e^{\lambda t}$:

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

Como $\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$, podemos reorganizar como:

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

Integrando ambos lados, obtenemos la solución general:

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. Solución particular
Supongamos que el número de este nucleido en t=0 es $n_0$ y encontremos el valor de la constante c:

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

Por lo tanto, la solución particular para la situación dada es:

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

Multiplicando ambos lados por $\lambda$, podemos obtener la radiactividad de este nucleido:

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

Es decir, cuando $t\to\infty$, $\alpha_{\text{max}}=R$, $n_{\text{max}}=R/\lambda$.

## Ejemplo: Cadena de Decaimiento Radiactivo 2
Calcula la radiactividad del radionucleido B en la siguiente cadena de decaimiento:
```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. Establecimiento del modelo

$$ \text{Tasa de cambio de núcleos B} = \text{Tasa de producción por decaimiento de A} - \text{Tasa de decaimiento de B a C} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

Sustituyendo la ecuación (2) para $n_A$, obtenemos la siguiente ecuación diferencial para $n_B$:

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. Solución general
Para resolver la ecuación diferencial, movamos todos los términos relacionados con $n_B$ al lado izquierdo y multipliquemos ambos lados por $e^{\lambda_B t}$:

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

Como $\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$, podemos reorganizar como:

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

Integrando ambos lados:

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

Dividiendo ambos lados por $e^{\lambda_B t}$, obtenemos la solución general:

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. Solución particular
Supongamos que el número de elementos B en t=0 es $n_{B0}$ y encontremos el valor de la constante c:

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

Por lo tanto, la solución particular para la situación dada es:

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$