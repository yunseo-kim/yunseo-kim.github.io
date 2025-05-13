---
title: Estabilidad nuclear y desintegración radiactiva
description: Exploramos la tabla de Segrè, varios tipos de desintegración radiactiva, el espectro energético de electrones/positrones emitidos en la desintegración beta y el trasfondo del descubrimiento del neutrino, las cadenas de desintegración de algunos nucleidos importantes (carbono-14, potasio-40, tritio, cesio-137), y la transición isomérica.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.webp
---
## Prerrequisitos
- [Partículas subatómicas y componentes del átomo](/posts/constituents-of-an-atom/)

## Tabla de Segré (Segre Chart) o Tabla de núclidos
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Para núclidos con número atómico $Z$ mayor que 20, se necesitan más neutrones que protones para estabilizarlos
- Los neutrones cumplen la función de mantener unido el núcleo, superando la repulsión eléctrica entre protones

## Razones para la desintegración radiactiva
- Solo ciertas combinaciones de neutrones y protones forman núclidos estables
- Si la proporción de neutrones respecto a protones es demasiado alta o baja, el núclido es inestable y sufre *desintegración radiactiva*
- El núcleo formado tras la desintegración suele estar en estado excitado, por lo que emite energía en forma de rayos gamma o rayos X

## Desintegración beta ($\beta$-decay)
### Desintegración beta positiva ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Ocurre cuando hay una deficiencia relativa de neutrones
- Un protón ($p$) se convierte en un neutrón ($n$), emitiendo un positrón ($\beta^+$) y un neutrino electrónico ($\nu_e$)
- El número atómico disminuye en 1, mientras que el número másico permanece igual

Ejemplo: $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Desintegración beta negativa ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Ocurre cuando hay un exceso relativo de neutrones
- Un neutrón ($n$) se convierte en un protón ($p$), emitiendo un electrón ($\beta^-$) y un antineutrino electrónico ($\overline{\nu}_e$)
- El número atómico aumenta en 1, mientras que el número másico permanece igual

Ejemplo: $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Espectro de energía de los electrones (positrones) emitidos
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia alemana [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Los electrones o positrones emitidos en la desintegración beta muestran un espectro continuo de energía como el de arriba.
- Desintegración $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- Desintegración $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

> Aunque la energía total emitida en la desintegración beta está cuantizada, el electrón/positrón y el antineutrino/neutrino comparten esta energía de manera arbitraria, lo que resulta en un espectro continuo cuando solo se observa la energía del electrón/positrón.
> El hecho de que el espectro de energía de los electrones/positrones emitidos en la desintegración beta no estuviera cuantizado sino que fuera continuo era inconsistente con las predicciones teóricas y parecía violar la ley de conservación de la energía.  
> Para explicar este resultado, Wolfgang Ernst Pauli predijo en 11930 la existencia de una '<u>partícula eléctricamente neutra, con masa extremadamente pequeña y reactividad extremadamente baja</u>', proponiendo llamarla 'neutrón'. Sin embargo, cuando Sir James Chadwick descubrió y nombró el neutrón tal como lo conocemos hoy en 11932, surgió un problema de duplicación de nombres. En 11933, Enrico Fermi, al publicar su teoría de la desintegración beta, renombró la partícula como *neutrino* añadiendo el sufijo italiano '-ino' que significa "pequeño", dándole su nombre actual.  
> Posteriormente, en 11942, el físico nuclear chino Wang Ganchang (王淦昌) propuso por primera vez un método para detectar neutrinos utilizando la [captura electrónica](#captura-electrónica-electron-capture-o-captura-k-k-capture), y en 11956, Clyde Cowan, Frederick Reines, Francis B. Harrison, Harold W. Kruse y Austin D. McGuire lograron detectar neutrinos a través del experimento de neutrinos Cowan-Reines, publicando sus resultados en la revista Science, verificando así su existencia real. Frederick Reines recibió el Premio Nobel de Física en 11995 por esta contribución.  
> Así, el estudio de la desintegración beta tiene gran importancia en la historia de la ciencia por proporcionar pistas sobre la existencia de los neutrinos.
{: .prompt-info }

### Cadenas de desintegración (Decay Chain)
A menudo, el *núclido hijo (daughter nuclide)* formado por la desintegración beta también es inestable y sufre desintegraciones beta consecutivas. Esto lleva a una *cadena de desintegración (decay chain)* como la siguiente:

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (estable)} $$

### Desintegraciónes beta importantes
A continuación, presentaré algunas desintegraciónes beta importantes.

#### Carbono-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> El carbono-14 se produce naturalmente en la atmósfera superior debido a la radiación cósmica, manteniendo así una concentración relativamente constante en la atmósfera. Los animales y plantas también mantienen la misma concentración de carbono-14 que la atmósfera mientras viven, debido al intercambio continuo de gases a través de la respiración. Sin embargo, después de la muerte, este intercambio cesa y la concentración de carbono-14 en el cadáver disminuye con el tiempo. Este principio es la base del método de datación por radiocarbono.
{: .prompt-tip }

#### Potasio-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> El potasio-40 es la fuente de radiación natural más abundante en el cuerpo de todos los animales, incluidos los humanos, y está presente naturalmente en todos los alimentos que consumimos habitualmente, especialmente en nueces de Brasil, frijoles, espinacas, plátanos, aguacates, café, pez sable y ajo.  
> Un adulto de 70 kg tiene aproximadamente 140 g de potasio en su cuerpo, que se mantiene constante, de los cuales unos 0.014 g son potasio-40, lo que representa una radiactividad de aproximadamente 4330 Bq.
{: .prompt-tip }

#### Tritio
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> El tritio es un material combustible que participa en la reacción de fusión D-T en reactores de fusión o bombas de hidrógeno/neutrones. Se produce naturalmente en la atmósfera debido a la radiación cósmica, pero como su vida media es relativamente corta (aproximadamente 12,32 años), se desintegra rápidamente y existe en proporciones muy bajas en la naturaleza. En reactores de fusión o armas nucleares, debido a esta rápida desintegración, en lugar de incorporar directamente el tritio, se utiliza un método donde se irradia litio-6 con neutrones para generar tritio. Por esta razón, el litio-6 altamente enriquecido y de alta pureza para uso en armas nucleares se considera un material crucial para el desarrollo nuclear y es uno de los principales objetivos de vigilancia de la comunidad internacional, incluido el OIEA.  
> Además, aunque no sea para los usos mencionados anteriormente, es un material que se utiliza comúnmente en pequeñas cantidades, como en las miras nocturnas del rifle K2 y la subametralladora K1, relojes luminosos, y señales de salida de emergencia en edificios que deben mantener su capacidad de iluminación durante mucho tiempo sin suministro eléctrico. El tritio se envuelve con fósforo, un material fluorescente, para que cuando los rayos beta emitidos durante la desintegración del tritio colisionen con el fósforo, se produzca luz. En el caso de las señales de salida de emergencia, se utilizan aproximadamente 900 mil millones de becquerelios de tritio.  
> Debido a esta demanda constante y a la imposibilidad de almacenamiento a largo plazo, se trata como un material estratégico importante, con un precio que se acerca a los 30.000 dólares por gramo. Actualmente, la mayor parte del tritio producido y vendido comercialmente proviene de reactores CANDU (CANada Deuterium Uranium), que son reactores de agua pesada a presión. En Corea, las unidades 1-4 de Wolsong son reactores CANDU.
{: .prompt-tip }

#### Cesio-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> El cesio-137 es un subproducto principal de las reacciones de fisión en reactores nucleares o pruebas nucleares. Debido a su vida media relativamente larga (aproximadamente 30 años), su emisión de rayos gamma altamente penetrantes, y sus propiedades químicas similares al potasio que facilitan su absorción por el cuerpo, es un isótopo que requiere vigilancia y gestión especial. Originalmente casi inexistente en la naturaleza, ahora está presente en el suelo de todo el planeta a un nivel promedio de 7 μg/g, resultado de la prueba nuclear Trinity y los bombardeos atómicos de Hiroshima y Nagasaki realizados por Estados Unidos para someter al Imperio Japonés, así como numerosas pruebas nucleares atmosféricas principalmente en las décadas de 11950-11960 y varios accidentes nucleares graves (como el accidente de Chernóbil y el incidente de Goiânia en Brasil).  
> La absorción de más de 10000 Bq de cesio-137 puede requerir tratamiento médico y observación. Durante el accidente de Chernóbil, se informó que algunos residentes cercanos absorbieron decenas de miles de Bq de cesio-137. En el caso del accidente nuclear de Fukushima, se estima que los residentes cercanos absorbieron entre 50-250 Bq inmediatamente después del accidente.
> Aunque hay variaciones individuales y entre diferentes fuentes, según los CDC, la vida media biológica del cesio-137 sin tratamiento es de [aproximadamente 110 días](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp). Si se sospecha exposición a cantidades significativas de cesio-137, [se puede reducir la vida media biológica a unos 30 días mediante la ingesta de tabletas médicas de azul de Prusia, que aceleran su eliminación del cuerpo](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp).
{: .prompt-tip }

## Captura electrónica (Electron Capture) o Captura K (K-capture)

$$ p + e \to n + \nu_e $$

- Ocurre cuando hay una deficiencia relativa de neutrones
- Captura un electrón de la capa más interna (capa K) para convertir un protón del núcleo en un neutrón
- El número atómico disminuye en 1, mientras que el número másico permanece igual
- Después de la captura electrónica, se forma un vacío en la nube de electrones que posteriormente se llena cuando un electrón de una capa exterior se mueve hacia adentro, emitiendo rayos X o electrones Auger
- El núclido hijo producido por captura electrónica es idéntico al producido por desintegración $\beta^+$, por lo que estos dos procesos compiten entre sí.

## Desintegración alfa ($\alpha$-decay)
- Emisión de una partícula alfa ($\alpha$, $^4_2\mathrm{He}$)
- El número atómico disminuye en 2 y el número másico disminuye en 4
- Común en núcleos más pesados que el plomo
- A diferencia de la desintegración beta, la energía de las partículas alfa emitidas está cuantizada.

Ejemplo: $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Fisión espontánea (Spontaneous Fission)
- Los núclidos muy pesados e inestables pueden sufrir fisión por sí mismos sin absorber neutrones
- Se incluye en un sentido amplio dentro de la desintegración radiactiva
- El uranio-238, por ejemplo, sufre desintegración alfa con una vida media de $10^9$ años, pero también, raramente, fisión espontánea con una vida media de aproximadamente $10^{16}$ años. La siguiente tabla muestra las vidas medias de fisión espontánea de varios núclidos.

| Núclido | Vida media de fisión espontánea | Características |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | Aproximadamente $10^{16}$ años | Ocurre muy raramente |
| $^{240}\mathrm{Pu}$ | Aproximadamente $10^{11}$ años | Núclido de fisión usado en armas nucleares |
| $^{252}\mathrm{Cf}$ | Aproximadamente $2.6$ años | La fisión espontánea ocurre muy activamente <br>$\rightarrow$ Se usa como fuente de neutrones para el arranque de reactores |

## Emisión de protones (Proton Emission)
- En núclidos extremadamente inestables con exceso de protones, a veces se emite un solo protón
- El número atómico y el número másico disminuyen en 1
- Ocurre muy raramente

## Esquema de desintegración y transición isomérica
### Esquema de desintegración (Decay Scheme)
*Esquema de desintegración (decay scheme)*: Diagrama visual que representa todas las vías de desintegración de un material radiactivo

### Transición isomérica (Isomeric Transition)
- Los núcleos formados por desintegración radiactiva a menudo quedan en estado excitado y emiten energía en forma de rayos gamma (aunque técnicamente no es una desintegración ya que el núclido no cambia, convencionalmente a veces se usa el término "desintegración gamma").
- La mayoría de los núcleos excitados emiten rayos gamma y pasan al estado fundamental muy rápidamente, pero en ciertos casos, la emisión de rayos gamma se retrasa, aparentando un estado metaestable. Estos estados retardados se denominan *estados isoméricos (isomeric states)* del núcleo.
- La transición de un estado isomérico al estado fundamental mediante la emisión de rayos gamma se denomina *transición isomérica (isomeric transition)* y se denota como IT.

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia británico [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Licencia: Libre para cualquier uso sin restricciones, siempre que no infrinja la ley

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> Licencia: [Dominio Público](https://en.wikipedia.org/wiki/Public_domain)
