---
title: Reacciones nucleares y energía de enlace
description: Exploramos las expresiones de reacciones nucleares, la definición del valor Q (Q-value), y los conceptos de defecto de masa (mass defect) y energía de enlace (binding energy).
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Reacción Nuclear (Nuclear Reaction)
### Leyes fundamentales en las reacciones nucleares
*Reacción nuclear (nuclear reaction)*: Reacción en la que dos núcleos atómicos diferentes, o un núcleo atómico y un nucleón, colisionan para producir dos o más nuevas partículas nucleares o rayos gamma

Cuando dos núcleos atómicos $a$ y $b$ reaccionan para producir núcleos atómicos o rayos gamma $c$ y $d$, esta reacción se expresa de la siguiente manera:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

En las reacciones nucleares se cumplen las siguientes cuatro leyes fundamentales:

- *Ley de conservación de nucleones (conservation of nucleon)*: El número total de nucleones es el mismo antes y después de la reacción. El tipo de nucleón puede cambiar, por lo que los protones y neutrones no se conservan individualmente.
- *Ley de conservación de la carga (conservation of charge)*: La suma total de las cargas de las partículas es la misma antes y después de la reacción.
- *Ley de conservación del momento (conservation of momentum)*: La suma total del momento de las partículas es la misma antes y después de la reacción.
- *Ley de conservación de la energía (conservation of energy)*: La energía total, <u>incluyendo la energía de masa en reposo</u>, es la misma antes y después de la reacción.

### Reacción exotérmica (exothermic reaction) y reacción endotérmica (endothermic reaction)
En la reacción nuclear de la ecuación ($\ref{nuclear_reaction}$), la energía total antes de la reacción es la suma de las energías de masa en reposo y las energías cinéticas de $a$ y $b$, y la energía total después de la reacción es la suma de las energías de masa en reposo y las energías cinéticas de $c$ y $d$. Por lo tanto, según la ley de conservación de la energía, se cumple lo siguiente:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Reorganizando esta ecuación, obtenemos:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Es decir, la diferencia en la energía cinética antes y después de la reacción nuclear es igual a la diferencia en la masa en reposo.
El lado derecho de la última ecuación se denomina *valor Q (Q-value)* de la reacción nuclear y se define como:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

El valor Q siempre se expresa en unidades de MeV, y dado que la energía de masa en reposo para 1 amu es aproximadamente 931 MeV, el valor Q también puede escribirse como:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Reacción exotérmica (exothermic reaction)*: Reacción nuclear con $Q>0$, parte de la masa se convierte en energía cinética, aumentando la energía cinética después de la reacción
- *Reacción endotérmica (endothermic reaction)*: Reacción nuclear con $Q<0$, parte de la energía cinética se convierte en masa, disminuyendo la energía cinética después de la reacción

| Tipo de reacción nuclear | Valor Q | Cambio de masa antes y después | Cambio de energía cinética antes y después |
| :---: | :---: | :---: | :---: |
| Reacción exotérmica | $Q>0$ | $\Delta m<0$ (disminución) | $\Delta E>0$ (aumento) |
| Reacción endotérmica | $Q<0$ | $\Delta m>0$ (aumento) | $\Delta E<0$ (disminución) |

### Notación abreviada de reacciones nucleares
La reacción nuclear de la ecuación ($\ref{nuclear_reaction}$) puede expresarse de forma abreviada como:

$$ a(b, c)d $$

Esto significa que $b$ incide sobre $a$, emitiendo $c$ y transformándose en $d$.

#### Ejemplos:
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Energía de Enlace (Binding Energy)
### Defecto de Masa (Mass Defect)
La masa de cualquier núcleo es ligeramente menor que la suma de las masas de los neutrones y protones que lo componen. Esta diferencia se denomina *defecto de masa (mass defect)*.

Si la masa del núcleo es $M_A$, el defecto de masa $\Delta$ de cualquier núcleo puede calcularse como:

$$ \Delta = ZM_p + NM_n - M_A. $$

El defecto de masa $\Delta$ expresado en unidades de energía representa la energía necesaria para dividir un núcleo en sus nucleones constituyentes. Esta energía se denomina *energía de enlace (binding energy)* porque es la energía que mantiene unidos a los nucleones. A la inversa, cuando se forma un núcleo atómico a partir de A nucleones, el nivel de energía disminuye en la cantidad de energía de enlace $\Delta$, por lo que se libera esa cantidad de energía al entorno durante el proceso de reacción nuclear.

### Energía de enlace promedio por nucleón
La energía de enlace total de un núcleo atómico aumenta con el número másico $A$, pero la pendiente no es constante.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
Como se puede ver en la imagen anterior, la energía de enlace promedio por nucleón $\Delta/A$ aumenta rápidamente para números másicos bajos, pero disminuye con una pendiente suave para núcleos atómicos pesados con $A\geq56$.

### Relación entre el valor Q de la reacción nuclear y la energía de enlace
En la reacción nuclear de la ecuación ($\ref{nuclear_reaction}$), la energía de enlace del núcleo $a$ es:

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

y la masa de $a$ es:

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

De manera similar, para los núcleos $b$, $c$ y $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Considerando que:

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

y sustituyendo estas ecuaciones en la ecuación ($\ref{Q_value}$), obtenemos:

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Esto significa que siempre se libera energía cuando dos núcleos menos estables se combinan para formar un núcleo más estable mediante un proceso de reacción nuclear.

### Fusión Nuclear (Nuclear Fusion) y Fisión Nuclear (Nuclear Fission)
En el caso de la reacción nuclear donde el deuterio, con una energía de enlace de $2.23\text{MeV}$, y el tritio, con una energía de enlace de $8.48\text{MeV}$, se combinan para producir $^4\text{He}$ con una energía de enlace de $28.3\text{MeV}$ y emitir un neutrón:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

Se libera una energía de $28.3-(2.23+8.48)=17.6\text{MeV}$ (equivalente a $3.52\text{MeV}$ por nucleón) en forma de energía cinética del núcleo de helio y el neutrón.

La reacción como la de la ecuación ($\ref{nuclear_fusion}$), donde dos núcleos atómicos ligeros con números másicos pequeños se combinan para formar un núcleo atómico más pesado con un número másico mayor que antes de la reacción, se denomina *fusión nuclear (nuclear fusion)*. Esta es la fuente de energía del Sol y todas las estrellas, y algún día la humanidad podrá utilizarla directamente como fuente de energía.

Por otro lado, en el caso de la reacción nuclear donde el $^{235}\text{U}$, con una energía de enlace de aproximadamente $1780\text{MeV}$, absorbe un neutrón y luego se divide en $^{92}\text{Kr}$ con una energía de enlace de $783\text{MeV}$ y $^{141}\text{Ba}$ con aproximadamente $1170\text{MeV}$, emitiendo tres neutrones:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

Se libera una energía de $783+1170-1780=173\text{MeV}$ (equivalente a $0.733\text{MeV}$ por nucleón).

La reacción como la de la ecuación ($\ref{nuclear_fission}$), donde un núcleo atómico pesado se divide en núcleos atómicos más ligeros, se denomina *fisión nuclear (nuclear fission)*. Desde el discurso "Átomos para la Paz" (Atoms for Peace) del 34º presidente de Estados Unidos, Eisenhower, y la central nuclear de Obninsk en la Unión Soviética, se ha utilizado ampliamente como fuente de energía eléctrica.

## Números Mágicos
Cuando el número de neutrones o protones que forman un núcleo es 2, 6, 8, 14, 20, 28, 50, 82 o 126, ese núcleo tiende a ser particularmente estable. Estos números de nucleones se denominan *números mágicos (magic numbers)*. Estos números corresponden al número de neutrones y protones necesarios para llenar las capas nucleares dentro del núcleo, similar a cómo se llenan las capas electrónicas externas del átomo.

Los isótopos que corresponden a números mágicos también se utilizan de manera práctica en la ingeniería nuclear. Un ejemplo representativo es el circonio-90 ($^{90}_{40} \mathrm{Zr}$), que tiene 50 neutrones. Debido a su estabilidad y baja capacidad para absorber neutrones, se utiliza ampliamente como material de revestimiento para las barras de combustible en el núcleo del reactor.
