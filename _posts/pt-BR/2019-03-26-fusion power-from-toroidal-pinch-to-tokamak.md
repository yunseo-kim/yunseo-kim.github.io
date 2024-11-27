---
title: "Fusão Nuclear: Do Pinch Toroidal ao Tokamak"
description: >-
  Aborda o conceito de fusão nuclear, o contexto que a tornou uma fonte de energia promissora, os objetivos técnicos para a comercialização da energia de fusão e a evolução da tecnologia de fusão desde o pinch toroidal até o ITER.
  O autor esclarece que este é um ensaio escrito para uma atividade de clube de ciências quando estava no segundo ano do ensino médio, e está em um estilo mais coloquial do que outros posts, mas foi carregado na forma original para fins de arquivamento.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
---

## O que é fusão nuclear?
Fusão nuclear é a reação em que dois núcleos atômicos colidem e se transformam em um único núcleo mais pesado. Basicamente, como os núcleos atômicos têm carga positiva devido aos prótons em seu interior, quando dois núcleos se aproximam, eles se repelem devido à força eletrostática. No entanto, se os núcleos forem aquecidos a temperaturas extremamente altas, sua energia cinética pode superar a repulsão elétrica, permitindo que colidam. Uma vez que os núcleos se aproximam o suficiente, a força nuclear forte atua, fazendo com que se combinem em um único núcleo.

No final da década de 1920, quando se descobriu que a fusão nuclear era a fonte de energia das estrelas e foi possível explicá-la fisicamente, começaram as discussões sobre como a fusão poderia ser utilizada em benefício da humanidade. Pouco depois do fim da Segunda Guerra Mundial, a ideia de controlar e utilizar a energia de fusão começou a ser seriamente considerada, e pesquisas foram iniciadas nas Universidades de Liverpool, Oxford e Londres, no Reino Unido.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Energia de ligação nuclear por nucleon em função da massa atômica A.(crédito da imagem:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Seções de choque medidas para diferentes reações de fusão em função da energia média do centro de massa. As seções de choque das reações são medidas em barn.(crédito da imagem:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Representação esquemática da energia potencial de dois núcleos em função de suas distâncias.(crédito da imagem:M. Decreton, SCK-CEN)"/></a>

## Ponto de equilíbrio e condição de ignição
Um dos problemas fundamentais para a geração de energia por fusão nuclear é que a energia produzida pela reação de fusão deve ser maior do que a energia inicialmente fornecida. Na reação DT, são produzidas partículas alfa e nêutrons, com 20% da energia liberada pela fusão sendo carregada pelas partículas alfa e 80% pelos nêutrons. A energia das partículas alfa é usada para aquecer o plasma, enquanto a energia dos nêutrons é convertida em energia elétrica. Inicialmente, é necessário fornecer energia externa para aumentar a temperatura do plasma, mas quando a taxa de reação de fusão aumenta suficientemente, a energia das partículas alfa sozinha pode aquecer o plasma, permitindo que a reação de fusão se sustente. Este ponto é chamado de ignição, e ocorre quando $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, ou seja, quando $\text{pressão do plasma}(P) \times \text{tempo de confinamento de energia}(\tau_{E}) > 5$, na faixa de temperatura de 10~20keV (aproximadamente 1~2 x 10^8 K).

![seções de choque e condições de ignição para reações de fusão DD, DT e D-He3](/assets/img/fusion-power/cross-sections.png)

## Pinch toroidal
Em 1946, Peter Thonemann conduziu pesquisas no Laboratório Clarendon da Universidade de Oxford sobre o confinamento de plasma em um toro usando o efeito pinch.

Como mostrado na figura, quando uma corrente é passada através do plasma, um campo magnético é formado ao redor da corrente, e a interação entre a corrente e o campo magnético resulta em uma força direcionada para o interior. Teoricamente, se a corrente for suficientemente alta, o efeito pinch poderia impedir que o plasma tocasse as paredes. No entanto, os experimentos mostraram que este método era muito instável e, portanto, atualmente quase não é mais pesquisado.

![efeito pinch](/assets/img/fusion-power/pinch-effect.png)

<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilidades em pinches lineares;(a)Tipo salsicha e (b)Tipo dobra. (crédito da imagem: livro de J.Freidberg)"/></a>

## Stellarator
No início da década de 1950, Lyman Spitzer, um astrofísico da Universidade de Princeton, inventou um novo dispositivo de confinamento de plasma e o chamou de stellarator. Diferentemente do pinch toroidal, onde o campo magnético é criado pela corrente que flui no próprio plasma, no stellarator o campo magnético é formado apenas por bobinas externas. O stellarator tem a vantagem de poder manter o plasma estável por longos períodos, e ainda é considerado como tendo potencial suficiente para ser aplicado em usinas de fusão reais. As pesquisas continuam ativamente.

![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)
Na década de 1960, a pesquisa em fusão entrou em um período de estagnação, mas foi nessa época que o Instituto Kurchatov em Moscou concebeu o primeiro tokamak, encontrando uma nova direção. Quando os resultados do tokamak foram apresentados em uma conferência científica em 1968, a maioria dos países mudou a direção de suas pesquisas para o tokamak, que se tornou o método de confinamento magnético mais promissor atualmente. O tokamak tem a vantagem de poder manter o plasma por longos períodos e ter uma estrutura muito mais simples do que o stellarator.

![tokamak](/assets/img/fusion-power/tokamak.png)

## Grandes dispositivos tokamak e o projeto ITER
Desde a década de 1970, grandes dispositivos tokamak foram construídos para se aproximar ainda mais da geração real de energia por fusão, com o JET da União Europeia, o TFTR de Princeton nos EUA e o JT-60U do Japão sendo os mais representativos. Com base nos dados obtidos de dispositivos experimentais menores, a pesquisa para aumentar a potência nesses grandes tokamaks foi conduzida constantemente, chegando muito perto do ponto de equilíbrio. Atualmente, para verificar finalmente a viabilidade da energia de fusão, China, União Europeia, Índia, Japão, Coreia, Rússia e Estados Unidos estão colaborando no projeto ITER, o maior projeto internacional conjunto da humanidade.

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## Referências
- [Khatri, G.. (2010). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken e Peter Stott, Fusion: The Energy of the Universe, Elsevier (2005)
