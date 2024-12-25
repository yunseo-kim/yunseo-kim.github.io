---
title: Mezclas homogéneas y sección transversal de moléculas
description: Calculemos la sección transversal macroscópica de una mezcla homogénea
  que contiene dos o más nucleidos.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## Sección transversal macroscópica de una mezcla homogénea (Homogeneous Mixture)
Consideremos una mezcla homogénea de dos nucleidos $X$ e $Y$. Las densidades atómicas de cada nucleido son $N_X$ y $N_Y$ $\text{átomo/cm}^3$ respectivamente, y las secciones transversales para una reacción específica de neutrones con estos núcleos son $\sigma_X$ y $\sigma_Y$. 

Entonces, la probabilidad de colisión por unidad de longitud de un neutrón con los núcleos $X$ e $Y$ es $\Sigma_X=N_X\sigma_X$ y $\Sigma_Y=N_Y\sigma_Y$ respectivamente (consulte [sección transversal macroscópica](/posts/Neutron-Interactions-and-Cross-sections/#sección-eficaz-macroscópica-macroscopic-cross-section)). La probabilidad total de que un neutrón reaccione con estos dos tipos de núcleos por unidad de longitud es:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Sección transversal equivalente de una molécula (Equivalent Cross-section)
Si los núcleos considerados anteriormente existen en forma molecular, podemos definir la sección transversal equivalente de esa molécula dividiendo la sección transversal macroscópica de la mezcla calculada por la ecuación (1) por el número de moléculas por unidad de volumen.

Si hay $N$ moléculas de $X_mY_n$ por unidad de volumen, entonces $N_X=mN$, $N_Y=nN$, y podemos calcular la sección transversal de esta molécula a partir de la ecuación (1) de la siguiente manera:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> Las ecuaciones (1) y (2) son válidas bajo la suposición de que los núcleos $X$ e $Y$ reaccionan independientemente con los neutrones, por lo que no se pueden aplicar a la dispersión elástica por moléculas y sólidos.
> Las secciones transversales de dispersión para neutrones de baja energía por moléculas y sólidos deben determinarse experimentalmente.
{: .prompt-warning }
