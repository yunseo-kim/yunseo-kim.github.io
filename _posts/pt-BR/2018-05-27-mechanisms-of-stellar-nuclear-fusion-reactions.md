---
title: "Mecanismos de Reação de Fusão Nuclear nas Estrelas"
description: >-
  Este artigo apresenta as reações de fusão nuclear que ocorrem no núcleo das estrelas, incluindo a reação em cadeia próton-próton e o ciclo CNO.
  Este é um ensaio que escrevi para uma atividade do clube de ciências quando estava no primeiro ano do ensino médio. Está escrito em um estilo coloquial e o conteúdo pode ser escasso ou parcialmente impreciso em alguns pontos, mas foi carregado na sua forma original para fins de arquivamento.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
---

## Reação em Cadeia Próton-Próton (proton-proton chain reaction)
Esta é a reação de fusão nuclear mais conhecida nas estrelas. O núcleo do deutério, chamado de deuteron, é formado pela combinação de um próton (p) e um nêutron (n). Portanto, para que dois prótons se combinem para formar o núcleo de deutério, um dos prótons deve se transformar em um nêutron. Então, como um próton pode se transformar em um nêutron?

- O '[decaimento beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#negative-beta-decay-beta--decay)' ocorre quando um nêutron ($n$) se transforma em um próton ($p$), emitindo um elétron ($e⁻$) e um antineutrino ($\overline{\nu_e}$). A equação desta reação é $n \rightarrow p + e^{-} + \overline{\nu_e}$. 
- O processo de um próton ($p$) se transformar em um nêutron ($n$) é o oposto do decaimento beta. Por isso, é chamado de '[decaimento beta inverso](/posts/Nuclear-Stability-and-Radioactive-Decay/#positive-beta-decay-beta-decay)'. Como seria a equação do decaimento beta inverso? Não há nada de especial na equação da reação nuclear. Basta trocar as posições do próton e do nêutron, mudar o elétron para um pósitron e o antineutrino para um neutrino. Expresso em uma equação, fica $p \rightarrow n + e^{+} + \nu_e$.

Após a formação do núcleo de deutério através desse processo, o núcleo de hélio-3 é formado por $^2_1D + p \rightarrow {^3_2He}$, e finalmente, dois núcleos de hélio-3 colidem para formar um núcleo de hélio-4 e dois prótons.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

Na verdade, existem vários caminhos para a reação em cadeia próton-próton. O caso acima é o mais representativo, mas existem alguns outros caminhos. No entanto, os outros caminhos não têm uma proporção significativa em estrelas com massa inferior à do Sol, e em estrelas com massa 1,5 vezes maior que a do Sol, o ciclo CNO, que discutiremos mais adiante, tem uma proporção muito maior do que a reação em cadeia próton-próton, então não os abordaremos separadamente aqui.

Esta reação em cadeia próton-próton ocorre predominantemente em temperaturas de cerca de 10 a 14 milhões de Kelvin. No caso do Sol, a temperatura central é de cerca de 15 milhões de Kelvin, e a reação pp representa 98,3% (o ciclo CNO representa os 1,3% restantes).

## Ciclo Carbono-Nitrogênio-Oxigênio (CNO Cycle)
O ciclo CNO é uma reação onde o carbono absorve um próton e se transforma em nitrogênio, então o nitrogênio absorve um próton e se transforma em oxigênio, e assim por diante, até que finalmente, após absorver 4 prótons, libera 1 hélio e volta a ser carbono. Uma característica é que o carbono, nitrogênio e oxigênio atuam como catalisadores. Teoricamente, este ciclo CNO é predominante em estrelas com massa 1,5 vezes maior que a do Sol. A diferença na reação de acordo com a massa da estrela está na diferença de dependência da temperatura entre a reação em cadeia próton-próton e o ciclo CNO. A primeira começa em temperaturas relativamente baixas, em torno de 4 milhões de Kelvin, e a taxa de reação é proporcional à quarta potência da temperatura. Por outro lado, a última começa em torno de 15 milhões de Kelvin, mas é muito sensível à temperatura (a taxa de reação é proporcional à 16ª potência da temperatura), de modo que em temperaturas acima de 17 milhões de Kelvin, o ciclo CNO passa a ter uma proporção maior.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

O ciclo CNO também tem vários caminhos. Ele é amplamente dividido em ciclo CNO de baixa temperatura (interior estelar) e ciclo CNO de alta temperatura (novas, supernovas), e cada caso tem três ou quatro caminhos de reação. Eu gostaria de abordar todas as reações do ciclo CNO, mas isso seria insuficiente com este volume, então vou tratar apenas do ciclo CN* mais básico, ou seja, o CNO-I.

> *A razão pela qual é chamado de ciclo CN, com o O omitido, é porque não existe um isótopo estável de oxigênio neste processo de reação.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Como mostrado na figura acima, o carbono, nitrogênio e oxigênio circulam e atuam como catalisadores. No entanto, independentemente do caminho da reação, a equação geral da reação e a quantidade total de energia gerada são as mesmas.

## Leituras Adicionais
- Inkyu Park (Professor do Departamento de Física da Universidade da Cidade de Seul), [Naver Cast Physics Walk: Quantos neutrinos são produzidos no Sol?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
