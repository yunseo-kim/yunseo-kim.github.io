---
title: Mecanismos de Reação de Fusão Nuclear nas Estrelas
description: Este artigo apresenta as reações de fusão nuclear que ocorrem no núcleo das estrelas, especificamente a reação em cadeia próton-próton (proton-proton chain reaction) e o ciclo carbono-nitrogênio-oxigênio (ciclo CNO). Este ensaio foi originalmente escrito pelo autor durante o primeiro ano do ensino médio para uma atividade de clube científico escolar.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## Reação em Cadeia Próton-Próton (proton-proton chain reaction)
Esta é a reação de fusão nuclear estelar mais conhecida pelas pessoas. O núcleo do deutério, chamado de dêuteron, é formado pela combinação de um próton (p) e um nêutron (n). Portanto, para que dois prótons se combinem e formem um núcleo de deutério, um dos prótons precisa se transformar em um nêutron. Então, como um próton pode se transformar em um nêutron?

- O '[decaimento beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#decaimento-beta-negativo-beta--decay)' é quando um nêutron ($n$) se transforma em um próton ($p$), liberando um elétron ($e⁻$) e um antineutrino ($\overline{\nu_e}$). Isso pode ser escrito como uma equação de reação: $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- O processo de um próton ($p$) se transformando em um nêutron ($n$) corresponde ao processo inverso do decaimento beta. Por isso, é chamado de '[decaimento beta inverso](/posts/Nuclear-Stability-and-Radioactive-Decay/#decaimento-beta-positivo-beta-decay)'. Então, como seria a equação de reação do decaimento beta inverso? Não há nada de especial em uma equação de reação nuclear. Basta trocar as posições do próton e do nêutron, mudar o elétron para um pósitron e o antineutrino para um neutrino. Expresso em uma equação, fica: $p \rightarrow n + e^{+} + \nu_e$.

Após a formação do núcleo de deutério através desse processo, forma-se o núcleo de hélio-3 através da reação $^2_1D + p \rightarrow {^3_2He}$, e finalmente, dois núcleos de hélio-3 colidem para formar um núcleo de hélio-4 e dois prótons.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

Na verdade, existem vários caminhos para a reação em cadeia próton-próton. O caso acima é o mais representativo, mas existem outros caminhos. No entanto, os outros caminhos não têm uma proporção significativa em estrelas com massa inferior à do Sol, e em estrelas com massa 1,5 vezes maior que a do Sol, o ciclo CNO (que veremos a seguir) tem uma proporção muito maior do que a reação em cadeia próton-próton, então não os abordaremos separadamente aqui.

Esta reação em cadeia próton-próton ocorre predominantemente em temperaturas entre 10 milhões e 14 milhões de Kelvin. No caso do Sol, a temperatura central é de aproximadamente 15 milhões de Kelvin, e a reação pp representa 98,3% (o ciclo CNO representa os 1,3% restantes).

## Ciclo Carbono-Nitrogênio-Oxigênio (Ciclo CNO)
O ciclo CNO é uma reação onde o carbono absorve prótons e se transforma em nitrogênio, e o nitrogênio absorve prótons e se transforma em oxigênio, e assim por diante, até que, finalmente, após absorver 4 prótons, libera 1 hélio e retorna ao carbono. A característica é que o carbono, nitrogênio e oxigênio atuam como catalisadores. Teoricamente, este ciclo CNO predomina em estrelas com massa 1,5 vezes maior que a do Sol. A diferença nas reações de acordo com a massa estelar está na diferença de dependência de temperatura entre a reação em cadeia próton-próton e o ciclo CNO. A primeira começa em temperaturas relativamente baixas, por volta de 4 milhões de Kelvin, e a taxa de reação é proporcional à quarta potência da temperatura. Por outro lado, a última começa em torno de 15 milhões de Kelvin, mas é muito sensível à temperatura (a taxa de reação é proporcional à 16ª potência da temperatura), de modo que em temperaturas acima de 17 milhões de Kelvin, o ciclo CNO passa a ter uma proporção maior.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

O ciclo CNO também tem vários caminhos. Divide-se amplamente em ciclo CNO de baixa temperatura (interior estelar) e ciclo CNO de alta temperatura (novas, supernovas), e em cada caso, existem três ou quatro caminhos de reação. Gostaria de abordar todas as reações do ciclo CNO, mas isso exigiria mais espaço do que temos disponível, então abordarei apenas o ciclo CN* mais básico, ou seja, o CNO-I.

> *A razão pela qual é chamado de ciclo CN, sem o O, é porque não existe um isótopo estável de oxigênio nesse processo de reação.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Como mostrado na figura acima, carbono, nitrogênio e oxigênio circulam e atuam como catalisadores. No entanto, independentemente do caminho da reação, a equação total da reação e a quantidade total de energia gerada são as mesmas.

## Leituras Adicionais
- Inkyu Park (Professor do Departamento de Física da Universidade da Cidade de Seul), [Naver Cast Physics Walk: Quantos neutrinos são produzidos no Sol?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
