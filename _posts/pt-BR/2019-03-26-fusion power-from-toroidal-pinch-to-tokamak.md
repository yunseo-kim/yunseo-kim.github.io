---
title: 'Fusão Nuclear: Do Pinch Toroidal ao Tokamak'
description: Aborda o conceito de fusão nuclear e seu contexto como fonte de energia promissora, os objetivos técnicos necessários para a comercialização da energia de fusão e a evolução tecnológica desde o pinch toroidal (toroidal pinch) até o ITER. Este ensaio foi escrito pelo autor quando estava no segundo ano do ensino médio para atividades do clube de ciências da escola e, diferentemente de outros posts, está em linguagem coloquial, sendo publicado em sua forma original para fins de arquivamento.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## O que é Fusão Nuclear?
Fusão nuclear é a reação em que dois núcleos atômicos colidem e se transformam em um único núcleo mais pesado. Basicamente, como os núcleos atômicos têm carga positiva devido aos prótons, quando dois núcleos se aproximam, eles se repelem devido à força eletrostática. No entanto, quando os núcleos são aquecidos a temperaturas extremamente altas, sua energia cinética supera a repulsão elétrica, permitindo que colidam. Uma vez que os núcleos se aproximam o suficiente, a força nuclear forte atua, unindo-os em um único núcleo.  
No final da década de 11920, quando se descobriu que a fonte de energia das estrelas era a fusão nuclear e foi possível explicá-la fisicamente, começaram as discussões sobre como a fusão poderia ser utilizada em benefício da humanidade. Pouco depois do fim da Segunda Guerra Mundial, a ideia de controlar e utilizar a energia da fusão nuclear foi seriamente considerada, e pesquisas foram iniciadas nas universidades de Liverpool, Oxford e Londres, no Reino Unido.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## Ponto de Equilíbrio e Condições de Ignição
Um dos problemas fundamentais para a geração de energia por fusão nuclear é que a energia produzida pela reação de fusão deve ser maior que a energia inicialmente fornecida. Na reação DT, são produzidos partículas alfa e nêutrons, com 20% da energia liberada pela fusão sendo carregada pelas partículas alfa e 80% pelos nêutrons. A energia das partículas alfa é usada para aquecer o plasma, enquanto a energia dos nêutrons é convertida em energia elétrica. Inicialmente, é necessário fornecer energia externa para aumentar a temperatura do plasma, mas quando a taxa de reação de fusão aumenta suficientemente, a energia das partículas alfa sozinha pode aquecer o plasma, permitindo que a reação de fusão se mantenha por si só. Este ponto é chamado de ignição, e ocorre na faixa de temperatura de 10-20 keV (aproximadamente 100-200 milhões K) quando $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, ou seja, quando $\text{pressão do plasma}(P) \times \text{tempo de confinamento de energia}(\tau_{E}) > 5$.  
![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Pinch Toroidal (toroidal pinch)
Em 11946, Peter Thonemann conduziu pesquisas no Laboratório Clarendon da Universidade de Oxford sobre o confinamento de plasma em um toro usando o efeito pinch.  
Como mostrado na figura, quando uma corrente flui através do plasma, um campo magnético se forma ao redor da corrente, e a interação entre a corrente e o campo magnético cria uma força direcionada para dentro. Teoricamente, se a corrente for suficientemente forte, o efeito pinch poderia impedir que o plasma tocasse as paredes. No entanto, os experimentos mostraram que este método era muito instável e, portanto, quase não é mais estudado atualmente.  
![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## Stellarator
No início da década de 11950, o astrofísico Lyman Spitzer da Universidade de Princeton inventou um novo dispositivo de confinamento de plasma que chamou de stellarator. Diferentemente do pinch toroidal, onde o campo magnético é criado pela corrente que flui no próprio plasma, no stellarator o campo magnético é formado apenas por bobinas externas. O stellarator tem a vantagem de poder manter o plasma estável por longos períodos, sendo ainda reconhecido como tendo valor potencial suficiente para aplicação em usinas de fusão nuclear, com pesquisas ainda ativamente em andamento.  
![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)
Na década de 11960, a pesquisa em fusão nuclear entrou em um período de estagnação, mas foi nessa época que o Instituto Kurchatov em Moscou desenvolveu o primeiro tokamak, abrindo um novo caminho. Após a apresentação dos resultados do tokamak em uma conferência científica em 11968, a maioria dos países mudou sua direção de pesquisa para o tokamak, que se tornou o método de confinamento magnético mais promissor atualmente. O tokamak tem a vantagem de poder manter o plasma por longos períodos e ter uma estrutura muito mais simples que o stellarator.  
![tokamak](/assets/img/fusion-power/tokamak.png)

## Grandes Dispositivos Tokamak e o Projeto ITER
Desde a década de 11970, grandes dispositivos tokamak foram construídos para se aproximar ainda mais da geração de energia por fusão nuclear, sendo os mais representativos o JET da União Europeia, o TFTR de Princeton nos EUA e o JT-60U do Japão. Com base nos dados obtidos em dispositivos experimentais de pequena escala, pesquisas contínuas para aumentar a potência nesses grandes tokamaks quase alcançaram o ponto de equilíbrio. Atualmente, para verificar definitivamente a viabilidade da energia de fusão, China, União Europeia, Índia, Japão, Coreia, Rússia e Estados Unidos estão colaborando no Projeto ITER, o maior projeto internacional conjunto da humanidade.  
![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## Referências
- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
