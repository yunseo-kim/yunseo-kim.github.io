---
title: Masa y energía, partículas y ondas
description: Exploremos el principio de equivalencia masa-energía de la teoría de la relatividad y calculemos la energía de un electrón en movimiento considerando los efectos relativistas.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## Principio de equivalencia masa-energía
La masa y la energía son idénticas y pueden convertirse mutuamente.

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
Según la teoría de la relatividad, la masa de un objeto en movimiento aumenta relativamente desde el punto de vista del observador, y la ecuación relacionada con la velocidad y la masa del objeto en movimiento se define de la siguiente manera:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: masa en reposo, $v$: velocidad

La *energía total* de una partícula es la suma de la *energía de masa en reposo* y la *energía cinética*, por lo que se cumple lo siguiente:

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

Especialmente cuando $v\ll c$, si establecemos $\cfrac{v^2}{c^2} = \epsilon$ y aproximamos mediante una expansión de Taylor alrededor de $\epsilon = 0$ (es decir, una expansión de Maclaurin):

$$
\begin{align*}
E_{kinetic} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

lo cual coincide con la fórmula de energía cinética en la mecánica clásica. En la práctica, cuando $v\leq 0.2c$ o $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$, se puede considerar que $v\ll c$ y usar esta aproximación (es decir, ignorar los efectos relativistas) para obtener un valor suficientemente preciso.

### Electrón
Como la energía de masa en reposo del electrón es $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$, cuando la energía cinética del electrón excede $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$, se debe aplicar la fórmula relativista de energía cinética. En ingeniería nuclear, la energía de los electrones es frecuentemente mayor a 10keV, por lo que generalmente se debe aplicar la ecuación (2).

### Neutrón
La energía de masa en reposo del neutrón es aproximadamente 1000MeV, por lo que $0.02E_{rest}=20\text{MeV}$. En ingeniería nuclear, es raro tratar con neutrones cuya energía cinética exceda los 20MeV, por lo que normalmente se utiliza la ecuación (3) para calcular la energía cinética de los neutrones.

### Fotón
Las ecuaciones (2) y (3) son válidas solo cuando la masa en reposo no es cero, por lo que no se pueden aplicar a los fotones, cuya masa en reposo es cero. La energía total de un fotón se calcula con la siguiente ecuación:

$$ E = h\nu \tag{4} $$

$h$: constante de Planck ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: frecuencia de la onda electromagnética

## Onda de materia
Toda materia en la naturaleza es simultáneamente partícula y onda. Es decir, todas las partículas tienen una longitud de onda correspondiente (*longitud de onda de de Broglie*). La longitud de onda $\lambda$ es una función del momento $p$ y la constante de Planck $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Además, el momento $p$ se define mediante la siguiente ecuación:

$$ p = mv \tag{6} $$

### Cuando se ignoran los efectos relativistas (p.ej., neutrón)
Como la energía cinética es $E=1/2 mv^2$, si expresamos la ecuación (6) en función de la energía, obtenemos:

$$ p=\sqrt{2mE} \tag{7} $$

Sustituyendo esto en la ecuación (5), la longitud de onda de la partícula es:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

En ingeniería nuclear, esta ecuación se aplica para calcular la longitud de onda de de Broglie de los neutrones. Sustituyendo la masa en reposo del neutrón, se expresa como:

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

donde $\lambda$ está en cm y $E$ es la energía cinética del neutrón expresada en eV.

### Cuando se consideran los efectos relativistas (p.ej., electrón)
Se calcula el momento $p$ resolviendo directamente las ecuaciones relativistas anteriores.

$$ p=\frac {1}{c} \sqrt{E^2_{total}-E^2_{rest}} \tag{10}$$

Entonces, la longitud de onda de de Broglie es:

$$ \lambda = \frac {hc}{\sqrt{E_{total}-E_{rest}}} \tag{11} $$

### Partículas con masa en reposo cero (p.ej., fotón)
El momento de una partícula con masa en reposo cero no se puede calcular con la ecuación (6), por lo que se expresa como:

$$ p=\frac {E}{c} \tag{12} $$

Sustituyendo la ecuación (12) en la (5):

$$ \lambda = \frac {hc}{E} \tag{13}$$

Sustituyendo los valores de $h$ y $c$, la ecuación final para la longitud de onda es:

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

donde $\lambda$ está en m y $E$ en eV.
