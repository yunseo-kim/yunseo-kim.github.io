---
title: Mecanismos de reacción de fusión nuclear en las estrellas
description: Este artículo introduce las reacciones de fusión nuclear que ocurren en el núcleo de las estrellas, específicamente la cadena protón-protón y el ciclo CNO. Es un ensayo que escribí para una actividad del club de ciencias cuando estaba en primer año de secundaria, y a diferencia de otras publicaciones, está escrito en un estilo coloquial que he mantenido intacto para fines de archivo.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## Cadena de reacción protón-protón (proton-proton chain reaction)
Es la reacción de fusión estelar más conocida por la gente. El núcleo del deuterio, el deuterón, se forma por la combinación de un protón (p) y un neutrón (n). Por lo tanto, para que dos protones se combinen y formen un núcleo de deuterio, uno de los protones debe convertirse en un neutrón. Entonces, ¿cómo puede un protón convertirse en un neutrón?

- La '[desintegración beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#desintegraci%C3%B3n-beta-negativa-beta--decay)' ocurre cuando un neutrón ($n$) se convierte en un protón ($p$) liberando un electrón ($e⁻$) y un antineutrino ($\nu_e$). Expresado como ecuación: $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- El proceso de conversión de un protón ($p$) en un neutrón ($n$) corresponde al proceso inverso de la desintegración beta. Por eso se llama '[desintegración beta inversa](/posts/Nuclear-Stability-and-Radioactive-Decay/#desintegraci%C3%B3n-beta-positiva-beta-decay)'. ¿Cómo se ve entonces la ecuación de la desintegración beta inversa? No hay nada especial en la ecuación de reacción nuclear. Simplemente intercambiamos las posiciones del protón y el neutrón, cambiamos el electrón por un positrón y el antineutrino por un neutrino. Expresado como ecuación: $p \rightarrow n + e^{+} + \nu_e$.

Después de que se forma el núcleo de deuterio a través del proceso anterior, se crea un núcleo de helio-3 mediante $^2_1D + p \rightarrow {^3_2He}$, y finalmente, cuando dos núcleos de helio-3 colisionan, se forman un núcleo de helio-4 y dos protones.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

En realidad, la cadena de reacción protón-protón no tiene una sola ruta. El caso anterior es el más representativo, pero existen algunas rutas adicionales. Sin embargo, las otras rutas no representan una proporción significativa en estrellas con masas inferiores a la del Sol, y en estrellas con masas superiores a 1.5 veces la del Sol, el ciclo CNO que veremos más adelante tiene una proporción mucho mayor que la cadena protón-protón, por lo que no las trataremos aquí por separado.

Esta cadena de reacción protón-protón ocurre predominantemente a temperaturas de aproximadamente 10-14 millones de Kelvin. En el caso del Sol, con una temperatura central de aproximadamente 15 millones de Kelvin, la cadena pp representa el 98.3% (el ciclo CNO representa el 1.3% restante).

## Ciclo del carbono-nitrógeno-oxígeno (CNO Cycle)
El ciclo CNO es una reacción en la que el carbono se convierte en nitrógeno al absorber un protón, luego el nitrógeno se convierte en oxígeno al absorber otro protón, y así sucesivamente, hasta que finalmente, después de absorber 4 protones, libera un núcleo de helio y vuelve a ser carbono. La característica distintiva es que el carbono, el nitrógeno y el oxígeno actúan como catalizadores. Teóricamente, este ciclo CNO predomina en estrellas con masas superiores a 1.5 veces la del Sol. La diferencia en las reacciones según la masa estelar radica en la dependencia de la temperatura entre la cadena protón-protón y el ciclo CNO. La primera comienza a temperaturas relativamente bajas, alrededor de 4 millones de Kelvin, y su velocidad de reacción es proporcional a la cuarta potencia de la temperatura. Por otro lado, el ciclo CNO comienza alrededor de los 15 millones de Kelvin, pero es muy sensible a la temperatura (la velocidad de reacción es proporcional a la decimosexta potencia de la temperatura), por lo que a temperaturas superiores a 17 millones de Kelvin, el ciclo CNO se vuelve predominante.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

El ciclo CNO también tiene varias rutas. Se divide principalmente en ciclo CNO frío (interior estelar) y ciclo CNO caliente (novas, supernovas), y en cada caso existen tres o cuatro rutas de reacción. Me gustaría cubrir todas las reacciones del ciclo CNO, pero esta extensión sería insuficiente, así que solo trataré el ciclo CN* más básico, es decir, el CNO-I.

> *La razón por la que se denomina ciclo CN, sin la O, es porque no existe un isótopo estable de oxígeno en este proceso de reacción.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Como se muestra en la imagen anterior, el carbono, el nitrógeno y el oxígeno circulan actuando como catalizadores. Sin embargo, independientemente de la ruta de reacción, la ecuación de reacción total y la cantidad total de energía generada son las mismas.

## Más lecturas
- Inkyu Park (Profesor de Física, Universidad de Seúl), [Naver Cast Physics Walk: ¿Cuántos neutrinos se producen en el Sol?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
