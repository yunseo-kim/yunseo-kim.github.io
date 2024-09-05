---
title: "Energía de fusión nuclear: desde el pinzamiento toroidal hasta el tokamak"
description: >-
  Este artículo aborda el concepto de fusión nuclear, el contexto que la convirtió en una fuente de energía prometedora para el futuro, los objetivos técnicos que deben alcanzarse para la comercialización de la energía de fusión, y la evolución de la tecnología de fusión desde el pinzamiento toroidal (toroidal pinch) hasta el ITER.
  Este ensayo fue escrito por el autor cuando estaba en segundo año de secundaria para una actividad del club de ciencias. Aunque puede haber algunas partes con descripciones insuficientes o imprecisas, se ha subido el texto original de aquel momento con fines de archivo.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
---

## ¿Qué es la fusión nuclear?
La fusión nuclear se refiere a la reacción en la que dos núcleos atómicos chocan y se transforman en un núcleo más pesado. Básicamente, como los núcleos atómicos tienen carga positiva debido a los protones en su interior, cuando dos núcleos se acercan, se repelen entre sí debido a la fuerza electrostática. Sin embargo, si los núcleos se calientan a temperaturas extremadamente altas, la energía cinética de los núcleos puede superar la repulsión eléctrica, permitiendo que los dos núcleos colisionen. Una vez que los dos núcleos se acercan lo suficiente, la fuerza nuclear fuerte actúa y los une en un solo núcleo.

A finales de la década de 1920, cuando se descubrió que la fuente de energía de las estrellas era la fusión nuclear y se pudo explicar físicamente la fusión nuclear, se discutió si la fusión nuclear podría utilizarse en beneficio de la humanidad. Poco después del final de la Segunda Guerra Mundial, se consideró seriamente la idea de controlar y utilizar la energía de fusión, y se iniciaron investigaciones en universidades británicas como la Universidad de Liverpool, la Universidad de Oxford y la Universidad de Londres.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Energía de enlace nuclear por nucleón en función de la masa atómica A.(crédito de la imagen:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Secciones eficaces medidas para diferentes reacciones de fusión en función de la energía promedio del centro de masa. Las secciones eficaces de reacción se miden en barn.(crédito de la imagen:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Representación esquemática de la energía potencial de dos núcleos en función de sus distancias.(crédito de la imagen:M. Decreton, SCK-CEN)"/></a>

## Punto de equilibrio y condición de ignición
Uno de los problemas más fundamentales para la energía de fusión es que la energía producida por la reacción de fusión debe ser mayor que la energía inicial invertida. En la reacción DT, se producen partículas alfa y neutrones, donde el 20% de la energía liberada por la fusión es llevada por las partículas alfa y el 80% por los neutrones. La energía de las partículas alfa se utiliza para calentar el plasma, mientras que la energía de los neutrones se convierte en energía eléctrica. Inicialmente, se debe aplicar energía externa para aumentar la temperatura del plasma, pero una vez que la tasa de reacción de fusión aumenta lo suficiente, la energía de las partículas alfa por sí sola puede calentar el plasma, permitiendo que la reacción de fusión se mantenga por sí misma. Este punto se llama ignición, y ocurre cuando $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, es decir, cuando $\text{presión del plasma}(P) \times \text{tiempo de confinamiento de energía}(\tau_{E}) > 5$ en el rango de temperatura de 10~20keV (aproximadamente 100~200 millones K).

![secciones eficaces y condiciones de ignición para las reacciones de fusión DD, DT y D-He3](/assets/img/fusion-power/cross-sections.png)

## Pinzamiento toroidal (toroidal pinch)
En 1946, Peter Thonemann realizó investigaciones en el Laboratorio Clarendon de la Universidad de Oxford sobre el confinamiento del plasma en un toro utilizando el efecto de pinzamiento (pinch effect).

Como se muestra en la figura, cuando se hace fluir una corriente a través del plasma, se forma un campo magnético alrededor de la corriente, y debido a la interacción entre la corriente y el campo magnético, se ejerce una fuerza hacia el interior. Por lo tanto, teóricamente, si la corriente es lo suficientemente grande, el efecto de pinzamiento podría evitar que el plasma toque las paredes. Sin embargo, los experimentos demostraron que este método era muy inestable, por lo que actualmente casi no se investiga.

![efecto de pinzamiento](/assets/img/fusion-power/pinch-effect.png)

<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Inestabilidades en pinzamientos lineales;(a)Tipo salchicha y (b)Tipo torcedura. (crédito de la imagen: libro de J.Freidberg)"/></a>

## Estelarador (stellarator)
A principios de la década de 1950, el astrofísico Lyman Spitzer de la Universidad de Princeton inventó un nuevo dispositivo de confinamiento de plasma y lo llamó estelarador. A diferencia del pinzamiento toroidal, donde el campo magnético es creado por la corriente que fluye a través del plasma mismo, en el estelarador el campo magnético es formado únicamente por bobinas externas. El estelarador tiene la ventaja de poder mantener el plasma estable durante largos períodos de tiempo, por lo que todavía se considera que tiene suficiente valor potencial para ser aplicado en centrales de fusión reales, y la investigación sigue siendo activa.

![estelarador](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)
En la década de 1960, la investigación sobre fusión entró en un período de estancamiento, pero en ese momento, el Instituto Kurchatov en Moscú ideó por primera vez el tokamak, encontrando un avance. Cuando se presentaron los resultados del tokamak en una conferencia académica en 1968, la mayoría de los países cambiaron su dirección de investigación hacia el tokamak, convirtiéndose en el método de confinamiento magnético más prometedor en la actualidad. El tokamak tiene la ventaja de poder mantener el plasma durante largos períodos de tiempo y tener una estructura mucho más simple que el estelarador.

![tokamak](/assets/img/fusion-power/tokamak.png)

## Dispositivos tokamak gigantes y el proyecto ITER
Desde la década de 1970, se han construido dispositivos tokamak a gran escala para acercarse aún más a la energía de fusión real, siendo los más representativos el JET de la Unión Europea, el TFTR de Princeton en Estados Unidos y el JT-60U de Japón. Como resultado de la investigación constante para aumentar la potencia en estos tokamaks gigantes basándose en los datos obtenidos de dispositivos experimentales a pequeña escala, se ha llegado casi al punto de equilibrio. Actualmente, para verificar finalmente la posibilidad de la energía de fusión, China, la Unión Europea, India, Japón, Corea, Rusia y Estados Unidos están colaborando en el proyecto ITER, el mayor proyecto internacional conjunto de la humanidad.

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## Referencias
- [Khatri, G.. (2010). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken, Peter Stott, 핵융합: 우주의 에너지, 유창모 외 2명 번역, 북스힐
