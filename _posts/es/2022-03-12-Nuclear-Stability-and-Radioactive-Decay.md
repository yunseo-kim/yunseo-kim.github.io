---
title: "Estabilidad nuclear y desintegración radiactiva"
description: >-
  Exploramos la tabla de Segré, los tipos de desintegración radiactiva y las transiciones isoméricas.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Radiation, Nuclear Radiation, Radioactive Decay]
math: true
---

## Tabla de Segré (Segre Chart) o Tabla de Núclidos
![Tabla de Segré](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Para núclidos con número atómico $Z$ mayor que 20, se necesitan más neutrones que protones para la estabilización
- Los neutrones ayudan a mantener unido el núcleo superando la repulsión eléctrica entre los protones

## Razón de la desintegración radiactiva (Radioactive Decay)
- Solo ciertas combinaciones de neutrones y protones forman núclidos estables
- Si el número de neutrones es demasiado alto o bajo en relación con el número de protones, el núclido es inestable y sufre *desintegración radiactiva (radioactive decay)*
- El núcleo formado después de la desintegración generalmente está en un estado excitado, por lo que emite energía en forma de rayos gamma o rayos X

## Desintegración beta ($\beta$-decay)
### Desintegración beta positiva ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Ocurre cuando hay una relativa escasez de neutrones
- Un protón ($p$) se convierte en un neutrón ($n$) emitiendo un positrón ($\beta^+$) y un neutrino electrónico ($\nu_e$)
- El número atómico disminuye en 1, el número másico no cambia

Ejemplo: $^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### Desintegración beta negativa ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Ocurre cuando hay un exceso relativo de neutrones
- Un neutrón ($n$) se convierte en un protón ($p$) emitiendo un electrón ($\beta^-$) y un antineutrino electrónico ($\overline{\nu}_e$)
- El número atómico aumenta en 1, el número másico no cambia

Ejemplo: $^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### Espectro de energía de los electrones (positrones) emitidos
![Espectro de energía de los electrones emitidos en la desintegración beta](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia alemana [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Los electrones o positrones emitidos en la desintegración beta muestran un espectro de energía continuo como se muestra arriba.
- Desintegración $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- Desintegración $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

### Cadena de desintegración (Decay Chain)
A menudo, el *núclido hijo (daughter nuclide)* formado por la desintegración beta también es inestable y sufre desintegraciones beta sucesivas. Esto lleva a una *cadena de desintegración (decay chain)* como la siguiente:

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (estable)} $$ 

## Captura electrónica (Electron Capture) o Captura K (K-capture)

$$ p + e \to n + \nu_e $$

- Ocurre cuando hay una relativa escasez de neutrones
- Captura un electrón de la capa más interna (capa K) para convertir un protón del núcleo en un neutrón
- El número atómico disminuye en 1, el número másico no cambia
- Después de la captura electrónica, se forma un espacio vacío en la nube de electrones que luego se llena con un electrón de una capa exterior, emitiendo rayos X o electrones Auger
- El núclido hijo (daughter nuclide) formado por captura electrónica es idéntico al formado por desintegración $\beta^+$, por lo que estos dos procesos compiten entre sí.

## Desintegración alfa ($\alpha$-decay)
- Emite una partícula alfa ($\alpha$, $^4_2\text{He}$)
- El número atómico disminuye en 2 y el número másico disminuye en 4
- Común en núcleos más pesados que el plomo
- A diferencia de la desintegración beta, la energía de las partículas alfa emitidas en la desintegración alfa está cuantizada.

Ejemplo: $^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## Fisión espontánea (Spontaneous Fission)
- Los núclidos muy pesados e inestables pueden sufrir fisión por sí mismos sin absorber neutrones
- Se incluye en la desintegración radiactiva en un sentido amplio

## Emisión de protones (Proton Emission)
- En el caso de núclidos extremadamente inestables con un exceso de protones, se puede emitir un solo protón
- El número atómico y el número másico disminuyen en 1
- Ocurre muy raramente

## Esquema de desintegración y transición isomérica
### Esquema de desintegración (Decay Scheme)
*Esquema de desintegración (decay scheme)*: Un diagrama que representa visualmente todas las vías de desintegración de un material radiactivo

### Transición isomérica (Isomeric Transition)
- Los núcleos formados por desintegración radiactiva a menudo están en un estado excitado después de la transformación, en cuyo caso emiten energía en forma de rayos gamma (aunque la emisión de rayos gamma no cambia el núclido, a veces se usa el término "desintegración gamma" por convención).
- La mayoría de los núcleos excitados hacen una transición al estado fundamental emitiendo rayos gamma en un tiempo muy corto, pero en ciertos casos, la emisión de rayos gamma se retrasa, pareciendo un estado metaestable. Este estado de retraso se llama *estado isomérico (isomeric state)* del núcleo.
- La transición del estado isomérico al estado fundamental mediante la emisión de rayos gamma se llama *transición isomérica (isomeric transition)* y se denota como IT.
![Esquema de desintegración de Au-198](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia británico [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Licencia: Libre para usar para cualquier propósito sin restricciones bajo la ley aplicable
