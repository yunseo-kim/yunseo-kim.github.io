---
title: Rayos X Continuos y Característicos
description: Exploramos los dos principios de generación de rayos X como radiación
  atómica, y las características respectivas de la radiación de frenado y los rayos
  X característicos.
categories: [Nuclear Engineering, Radiation]
tags: [Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **bremsstrahlung (radiación de frenado)**: rayos X de espectro continuo emitidos cuando partículas cargadas como electrones pasan cerca de núcleos atómicos y son aceleradas por fuerzas eléctricas
> - Longitud de onda mínima: $\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **rayos X característicos**: rayos X de espectro discreto emitidos cuando un electrón incidente colisiona con un electrón de una capa interna del átomo, ionizándolo, y otro electrón de una capa externa transita para llenar el espacio vacío, liberando energía igual a la diferencia entre los dos niveles energéticos
{: .prompt-info }

## Prerequisites
- [Partículas Subatómicas y Componentes del Átomo](/posts/constituents-of-an-atom/)

## Descubrimiento de los Rayos X
Röntgen descubrió que los rayos X se producían cuando un haz de electrones incidía sobre un objetivo. Como en el momento del descubrimiento no se sabía que los rayos X eran ondas electromagnéticas, se les llamó **rayos X** por su naturaleza desconocida, y también **radiación Röntgen** en honor a su descubridor.

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

La imagen anterior muestra la estructura básica de un tubo de rayos X típico. El tubo contiene un cátodo compuesto por un filamento de tungsteno y un ánodo con el objetivo, sellados al vacío. Cuando se aplica un voltaje de decenas de kV entre los electrodos, los electrones son emitidos desde el cátodo y bombardean el objetivo en el ánodo, produciendo rayos X. Sin embargo, la eficiencia de conversión a rayos X es típicamente menor al 1%, y más del 99% de la energía se convierte en calor, requiriendo dispositivos adicionales para la refrigeración.

## bremsstrahlung (radiación de frenado)
Cuando partículas cargadas como electrones pasan cerca de núcleos atómicos, sus trayectorias se curvan y desaceleran bruscamente debido a las fuerzas eléctricas entre la partícula y el núcleo, liberando energía en forma de rayos X. Como esta conversión de energía no está cuantizada, los rayos X emitidos presentan un espectro continuo. Este proceso se conoce como **bremsstrahlung** o **radiación de frenado**.

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

Sin embargo, la energía de los fotones de rayos X emitidos por bremsstrahlung no puede exceder la energía cinética del electrón incidente. Por lo tanto, existe una longitud de onda mínima para los rayos X emitidos, que se puede calcular simplemente con la siguiente ecuación:

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

Como la constante de Planck $h$ y la velocidad de la luz $c$ son constantes, esta longitud de onda mínima está determinada únicamente por la energía del electrón incidente. La longitud de onda $\lambda$ correspondiente a una energía de $1\text{eV}$ es aproximadamente $1.24 \mu\text{m}=12400\text{Å}$. Por lo tanto, la longitud de onda mínima $\lambda_\text{min}$ cuando se aplica un voltaje de $V$ voltios al tubo de rayos X es:

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

El siguiente gráfico muestra los espectros de rayos X continuos a diferentes voltajes manteniendo constante la corriente del tubo. Se puede observar que a medida que aumenta el voltaje, la longitud de onda mínima $\lambda_{\text{min}}$ disminuye y la intensidad general de los rayos X aumenta.

![Typical continuous X-ray spectra from tube operating
at three different peak voltages with the same current](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## Rayos X característicos
Si el voltaje aplicado al tubo de rayos X es suficientemente alto, los electrones incidentes pueden colisionar con electrones de las capas internas del átomo objetivo, ionizándolo. En este caso, un electrón de una capa externa rápidamente llena el espacio vacío en la capa interna, liberando energía, y en el proceso se emite un fotón de rayos X con energía igual a la diferencia entre los dos niveles energéticos. El espectro de rayos X emitido por este proceso es discreto y está determinado por los niveles de energía característicos del átomo objetivo, independientemente de la energía o intensidad del haz de electrones incidente. Estos se denominan **rayos X característicos**.

### Notación de Siegbahn

![Siegbahn notation of electron transitions between shells](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia en inglés [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Según la notación de Siegbahn, los rayos X emitidos cuando los electrones de las capas L, M, ... llenan un espacio vacío en la capa K se designan como $K_\alpha$, $K_\beta$, ... como se muestra en la imagen anterior. Sin embargo, después de la introducción de la notación de Siegbahn y con el advenimiento del modelo atómico moderno, se descubrió que para átomos multielectrónicos, los niveles de energía dentro de cada capa (niveles de energía con el mismo número cuántico principal) también varían según otros números cuánticos, lo que llevó a subdivisiones adicionales como $K_{\alpha_1}$, $K_{\alpha_2}$, ... para cada $K_\alpha$, $K_\beta$, ...

![Siegbahn notation](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

Esta notación tradicional todavía se usa ampliamente en espectroscopia. Sin embargo, debido a que la nomenclatura no es sistemática y a veces causa confusión, la *Unión Internacional de Química Pura y Aplicada (IUPAC)* recomienda usar una notación diferente.

### Notación IUPAC
La notación estándar recomendada por IUPAC para orbitales atómicos y rayos X característicos es la siguiente.
Primero, se asignan nombres a cada orbital atómico según la siguiente tabla:

| $n$(número <br>cuántico <br>principal) | $l$(número <br>cuántico <br>azimutal) | $s$(número <br>cuántico <br>de espín) | $j$(número <br>cuántico de <br>momento <br>angular total) | Orbital <br>atómico | Notación <br>de rayos X |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0$ | $\pm1/2$ | $1/2$ | $1s_{1/2}$ | $K_{(1)}$ |
| $2$ | $0$ | $\pm1/2$ | $1/2$ | $2s_{1/2}$ | $L_1$ |
| $2$ | $1$ | $-1/2$ | $1/2$ | $2p_{1/2}$ | $L_2$ |
| $2$ | $1$ | $+1/2$ | $3/2$ | $2p_{3/2}$ | $L_3$ |
| $3$ | $0$ | $\pm1/2$ | $1/2$ | $3s_{1/2}$ | $M_1$ |
| $3$ | $1$ | $-1/2$ | $1/2$ | $3p_{1/2}$ | $M_2$ |
| $3$ | $1$ | $+1/2$ | $3/2$ | $3p_{3/2}$ | $M_3$ |
| $3$ | $2$ | $-1/2$ | $3/2$ | $3d_{3/2}$ | $M_4$ |
| $3$ | $2$ | $+1/2$ | $5/2$ | $3d_{5/2}$ | $M_5$ |
| $4$ | $0$ | $\pm1/2$ | $1/2$ | $4s_{1/2}$ | $N_1$ |
| $4$ | $1$ | $-1/2$ | $1/2$ | $4p_{1/2}$ | $N_2$ |
| $4$ | $1$ | $+1/2$ | $3/2$ | $4p_{3/2}$ | $N_3$ |
| $4$ | $2$ | $-1/2$ | $3/2$ | $4d_{3/2}$ | $N_4$ |
| $4$ | $2$ | $+1/2$ | $5/2$ | $4d_{5/2}$ | $N_5$ |
| $4$ | $3$ | $-1/2$ | $5/2$ | $4f_{5/2}$ | $N_6$ |
| $4$ | $3$ | $+1/2$ | $7/2$ | $4f_{7/2}$ | $N_7$ |

> Número cuántico de momento angular total $j=\|l+s\|$.
{: .prompt-info }

Y los rayos X característicos emitidos cuando un electrón transita de un nivel de energía superior a uno inferior se designan según la siguiente regla:

$$ \text{(notación del nivel final)-(notación del nivel inicial)} $$

Por ejemplo, los rayos X característicos emitidos cuando un electrón transita del orbital $2p_{1/2}$ al $1s_{1/2}$ se denominan $\text{K-L}_2$.

## Espectro de rayos X

![Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

La imagen muestra el espectro de rayos X emitido cuando un haz de electrones acelerado a 60kV incide sobre un objetivo de rodio (Rh). Se observa una curva suave y continua debido al bremsstrahlung, y según la ecuación ($\ref{eqn:lambda_min}$), los rayos X solo se emiten para longitudes de onda mayores a aproximadamente $0.207\text{Å} = 20.7\text{pm}$. Los picos agudos que aparecen en el gráfico se deben a los rayos X característicos de la capa K del átomo de rodio. Como se mencionó anteriormente, cada átomo objetivo tiene su propio espectro característico de rayos X, por lo que al examinar las longitudes de onda donde aparecen los picos en el espectro de rayos X emitido al bombardear un objetivo con un haz de electrones, se pueden identificar los elementos que componen dicho objetivo.

> Por supuesto, también se emiten rayos X de menor energía como $L_\alpha$, $L_\beta$, ... además de $K_\alpha$, $K_\beta$, ... Sin embargo, estos tienen energías mucho menores y generalmente son absorbidos por la carcasa del tubo de rayos X antes de llegar al detector.
{: .prompt-info }
