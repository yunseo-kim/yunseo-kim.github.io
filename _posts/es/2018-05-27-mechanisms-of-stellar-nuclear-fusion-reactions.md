---
title: "Mecanismos de reacción de fusión nuclear en las estrellas"
description: >-
  Este artículo introduce la reacción en cadena protón-protón y el ciclo carbono-nitrógeno-oxígeno (CNO), que son reacciones de fusión nuclear que ocurren en el núcleo de las estrellas.
  Este es un ensayo que escribí para una actividad del club de ciencias cuando estaba en el primer año de la escuela secundaria. Está escrito en un estilo coloquial y la descripción del contenido puede ser deficiente o parcialmente inexacta, pero lo subo tal como estaba originalmente con fines de archivo.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
---

## Reacción en cadena protón-protón (proton-proton chain reaction)
Esta es la reacción de fusión estelar más comúnmente conocida por la gente. El núcleo del deuterio, el deuterón, está formado por la combinación de un protón (p) y un neutrón (n). Por lo tanto, para que dos protones se combinen para formar el núcleo de deuterio, uno de los dos protones debe convertirse en un neutrón. Entonces, ¿cómo puede un protón convertirse en un neutrón?

- La '[desintegración beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#negative-beta-decay-beta--decay)' es cuando un neutrón ($n$) se convierte en un protón ($p$) liberando un electrón ($e⁻$) y un antineutrino ($\overline{\nu_e}$). Esto se puede escribir como una ecuación de reacción: $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- El proceso de conversión de un protón ($p$) en un neutrón ($n$) corresponde al proceso inverso de la desintegración beta. Por eso se llama '[desintegración beta inversa](/posts/Nuclear-Stability-and-Radioactive-Decay/#positive-beta-decay-beta-decay)'. Entonces, ¿cómo se ve la ecuación de reacción de la desintegración beta inversa? No hay nada especial en la ecuación de reacción nuclear. Solo necesitas intercambiar las posiciones del protón y el neutrón, cambiar el electrón por un positrón y el antineutrino por un neutrino. Expresado en una ecuación, sería $p \rightarrow n + e^{+} + \nu_e$.

Después de que se forma el núcleo de deuterio a través de este proceso, se forma un núcleo de helio-3 mediante $^2_1D + p \rightarrow {^3_2He}$, y finalmente, cuando dos núcleos de helio-3 colisionan, se forma un núcleo de helio-4 y dos protones.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

En realidad, la ruta de reacción de la cadena protón-protón no es única. El caso anterior es el más representativo, pero hay algunas rutas más. Sin embargo, las otras rutas no tienen una proporción tan alta en estrellas con masas inferiores a la del Sol, y en estrellas con masas 1.5 veces mayores que la del Sol, el ciclo CNO que veremos más adelante tiene una proporción mucho mayor que la reacción en cadena protón-protón, así que no las trataremos aquí por separado.

Esta reacción en cadena protón-protón ocurre predominantemente a temperaturas de alrededor de 10-14 millones de K. En el caso del Sol, la temperatura central es de unos 15 millones de K, y la reacción pp representa el 98.3% (el 1.3% restante es el ciclo CNO).

## Ciclo carbono-nitrógeno-oxígeno (CNO Cycle)
El ciclo CNO es una reacción en la que el carbono se convierte en nitrógeno al absorber un protón, luego el nitrógeno se convierte en oxígeno al absorber otro protón, y así sucesivamente, hasta que finalmente absorbe 4 protones, libera 1 helio y vuelve a ser carbono. La característica es que el carbono, el nitrógeno y el oxígeno actúan como catalizadores. Teóricamente, este ciclo CNO predomina en estrellas con masas 1.5 veces mayores que la del Sol. La diferencia en la reacción según la masa estelar radica en la diferencia de dependencia de la temperatura entre la reacción en cadena protón-protón y el ciclo CNO. La primera comienza a temperaturas relativamente bajas de alrededor de 4 millones de K, y se dice que la velocidad de reacción es proporcional a la cuarta potencia de la temperatura. Por otro lado, la última comienza alrededor de los 15 millones de K, pero es muy sensible a la temperatura (la velocidad de reacción es proporcional a la decimosexta potencia de la temperatura), por lo que a temperaturas superiores a 17 millones de K, el ciclo CNO ocupa una mayor proporción.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

El ciclo CNO también tiene varias rutas. Se divide en general en ciclo CNO frío (interior estelar) y ciclo CNO caliente (nova, supernova), y cada caso tiene tres o cuatro rutas de reacción. Me gustaría tratar todas las reacciones del ciclo CNO, pero esta extensión no es suficiente para eso, así que solo trataré el ciclo CN* más básico, es decir, el CNO-I.

> *La razón por la que se llama ciclo CN, sin la O, es porque no existe un isótopo estable de oxígeno en este proceso de reacción.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Como se muestra en la figura anterior, el carbono, el nitrógeno y el oxígeno circulan y actúan como catalizadores. Sin embargo, independientemente de la ruta de reacción, la ecuación de reacción total y la cantidad total de energía generada son las mismas.

## Más lecturas
- Inkyu Park (Profesor del Departamento de Física de la Universidad de Seúl), [Paseo por la física de Naver Cast: ¿Cuántos neutrinos se producen en el Sol?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Cadena protón-protón](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [Ciclo CNO](https://en.wikipedia.org/wiki/CNO_cycle)
