---
title: "Masa y energía, partículas y ondas"
description: >-
  Exploremos el principio de equivalencia masa-energía de la teoría de la relatividad y calculemos la energía de un electrón en movimiento considerando los efectos relativistas.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Theory of Relativity]
math: true
---

## Principio de equivalencia masa-energía
La masa y la energía son idénticas y pueden convertirse entre sí.

$$ E=mc^2 $$

Donde $c$ es la velocidad de la luz $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Electronvoltio (Electron Volt, eV)
*Electronvoltio (electron volt, eV)*: La energía cinética que adquiere un electrón al pasar a través de una diferencia de potencial de 1V

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Masa y energía de un objeto en movimiento
Según la teoría de la relatividad, la masa de un objeto en movimiento aumenta relativamente desde el punto de vista del observador, y la ecuación para la velocidad y la masa de un objeto en movimiento se define de la siguiente manera:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: masa en reposo, $v$: velocidad

La *energía total* de una partícula es la suma de la *energía de la masa en reposo* y la *energía cinética*, por lo que se cumple lo siguiente:

$$ E_{\text{total}} = E_{\text{reposo}}+E_{\text{cinética}} = mc^2$$

$$
\begin{align*}
E_{\text{cinética}} &= E_{\text{total}}-E_{\text{reposo}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

En particular, cuando $v\ll c$, aproximando con el teorema del binomio:

$$
\begin{align*}
E_{cinética} &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right]
\\ &= m_0c^2\left[\left(1+\frac{1}{2}v^2/c^2\right)-1\right]
\\ &= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

Se convierte en la fórmula de energía cinética de la mecánica clásica. En la práctica, cuando $v\leq 0.2c$ o $E_{\text{cinética}} \leq 0.02E_{\text{reposo}}$, se puede considerar $v\ll c$ y usar esta fórmula aproximada (es decir, ignorar los efectos de la teoría de la relatividad) para obtener un valor suficientemente preciso.

### Electrón
Como la energía de la masa en reposo del electrón es $E_{\text{reposo}}=m_ec^2=0.511 \text{MeV}$, cuando la energía cinética del electrón excede $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$, se debe aplicar la fórmula de energía cinética relativista. En muchos casos, la energía de los electrones en ingeniería nuclear es mayor que 10keV, por lo que generalmente se debe aplicar la ecuación (2).

### Neutrón
La energía de la masa en reposo del neutrón es aproximadamente 1000MeV, por lo que $0.02E_{reposo}=20\text{MeV}$. Es raro tratar situaciones en ingeniería nuclear donde la energía cinética del neutrón exceda los 20MeV, por lo que generalmente se usa la ecuación (3) para calcular la energía cinética del neutrón.

### Fotón
Las ecuaciones (2) y (3) son válidas solo cuando la masa en reposo no es cero, por lo que no se pueden aplicar al fotón, cuya masa en reposo es cero. La energía total del fotón se calcula con la siguiente ecuación:

$$ E = h\nu \tag{4} $$

$h$: constante de Planck ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: frecuencia de la onda electromagnética

## Onda de materia
Toda la materia en la naturaleza es a la vez partícula y onda. Es decir, todas las partículas tienen una longitud de onda correspondiente (*longitud de onda de de Broglie*). La longitud de onda $\lambda$ es una función del momento $p$ y la constante de Planck $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Además, el momento $p$ se define por la siguiente ecuación:

$$ p = mv \tag{6} $$

### Cuando se ignoran los efectos relativistas (por ejemplo, neutrón)
Como la energía cinética es $E=1/2 mv^2$, la ecuación (6) expresada en función de la energía es:

$$ p=\sqrt{2mE} \tag{7} $$

Sustituyendo esto en la ecuación (5), la longitud de onda de la partícula es:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Esta ecuación se aplica para calcular la longitud de onda de de Broglie del neutrón en ingeniería nuclear. Sustituyendo la masa en reposo del neutrón, se expresa como:

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Donde $\lambda$ está en cm y $E$ es la energía cinética del neutrón expresada en eV.

### Cuando se consideran los efectos relativistas (por ejemplo, electrón)
Se calcula el momento $p$ resolviendo directamente las ecuaciones relativistas anteriores.

$$ p=\frac {1}{c} \sqrt{E^2_{total}-E^2_{reposo}} \tag{10}$$

Entonces, la longitud de onda de de Broglie es:

$$ \lambda = \frac {hc}{\sqrt{E_{total}-E_{reposo}}} \tag{11} $$

### Para partículas con masa en reposo cero (por ejemplo, fotón)
Como el momento de una partícula con masa en reposo cero no se puede calcular con la ecuación (6), se expresa como:

$$ p=\frac {E}{c} \tag{12} $$

Sustituyendo la ecuación (12) en la ecuación (5):

$$ \lambda = \frac {hc}{E} \tag{13}$$

Sustituyendo los valores de $h$ y $c$, la ecuación final para la longitud de onda es:

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

Donde $\lambda$ está en m y $E$ está en eV.