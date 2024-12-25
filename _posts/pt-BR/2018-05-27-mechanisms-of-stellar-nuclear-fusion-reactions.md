---
title: Mecanismos de reação de fusão nuclear nas estrelas
description: Este artigo introduz a reação em cadeia próton-próton e o ciclo CNO,
  que são reações de fusão nuclear que ocorrem no núcleo das estrelas. Este é um ensaio
  que o autor escreveu para uma atividade do clube de ciências da escola quando estava
  no primeiro ano do ensino médio. Diferentemente de outros posts, está escrito em
  um estilo coloquial, mas foi carregado exatamente como o texto original na época
  para fins de arquivamento.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## Reação em cadeia próton-próton (proton-proton chain reaction)
Esta é a reação de fusão estelar mais conhecida pelas pessoas. O núcleo do deutério, o deuteron, é formado pela combinação de um próton (p) e um nêutron (n). Portanto, para que dois prótons se combinem para formar o núcleo de deutério, um dos prótons deve se transformar em um nêutron. Então, como um próton pode se transformar em um nêutron?

- O '[decaimento beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#decaimento-beta-negativo-beta--decay)' é quando um nêutron ($n$) se transforma em um próton ($p$), emitindo um elétron ($e⁻$) e um antineutrino ($\overline{\nu_e}$). Isso pode ser escrito como uma equação de reação: $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- O processo de um próton ($p$) se transformando em um nêutron ($n$) corresponde ao processo inverso do decaimento beta. Por isso, é chamado de '[decaimento beta inverso](/posts/Nuclear-Stability-and-Radioactive-Decay/#decaimento-beta-positivo-beta-decay)'. Então, como seria a equação de reação do decaimento beta inverso? Não há nada de especial em uma equação de reação nuclear. Basta trocar as posições do próton e do nêutron, mudar o elétron para um pósitron e o antineutrino para um neutrino. Expresso em uma equação, fica: $p \rightarrow n + e^{+} + \nu_e$.

Após o núcleo de deutério ser formado através do processo acima, o núcleo de hélio-3 é formado por $^2_1D + p \rightarrow {^3_2He}$, e finalmente, dois núcleos de hélio-3 colidem para formar um núcleo de hélio-4 e dois prótons.  
![reação em cadeia p-p](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

Na verdade, não há apenas um caminho de reação para a reação em cadeia próton-próton. O caso acima é o mais representativo, mas existem alguns outros caminhos além deste. No entanto, os outros caminhos não têm uma proporção muito alta em estrelas com massa inferior à do Sol, e em estrelas com massa 1,5 vezes maior que a do Sol, o ciclo CNO, que discutiremos mais adiante, tem uma proporção muito maior do que a reação em cadeia próton-próton, então não os abordaremos separadamente aqui.

Esta reação em cadeia próton-próton ocorre predominantemente em temperaturas de cerca de 10 milhões K a 14 milhões K. No caso do Sol, a temperatura central é de cerca de 15 milhões K, e a reação em cadeia pp representa 98,3% (o ciclo CNO representa os 1,3% restantes).

## Ciclo do carbono-nitrogênio-oxigênio (Ciclo CNO)
O ciclo CNO é uma reação onde o carbono aceita um próton e se transforma em nitrogênio, então o nitrogênio aceita um próton e se transforma em oxigênio, e assim por diante, até que finalmente, após aceitar 4 prótons, libera 1 hélio e volta a ser carbono. A característica é que o carbono, nitrogênio e oxigênio atuam como catalisadores. Teoricamente, este ciclo CNO é predominante em estrelas com massa 1,5 vezes maior que a do Sol. A diferença na reação de acordo com a massa estelar está na diferença de dependência da temperatura entre a reação em cadeia próton-próton e o ciclo CNO. A primeira começa em temperaturas relativamente baixas, em torno de 4 milhões K, e a taxa de reação é proporcional à quarta potência da temperatura. Por outro lado, a última começa em torno de 15 milhões K, mas é muito sensível à temperatura (a taxa de reação é proporcional à 16ª potência da temperatura), então em temperaturas acima de 17 milhões K, o ciclo CNO ocupa uma proporção maior.

![Geração de Energia Nuclear Estelar](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

O ciclo CNO também tem vários caminhos. Ele é amplamente dividido em ciclo CNO de baixa temperatura (interior estelar) e ciclo CNO de alta temperatura (nova, supernova), e cada caso tem três ou quatro caminhos de reação. Eu gostaria de abordar todas as reações do ciclo CNO, mas isso não seria suficiente com este volume, então vou tratar apenas do ciclo CN* mais básico, ou seja, o CNO-I.

> *A razão pela qual é chamado de ciclo CN, com o O omitido, é porque não há isótopos estáveis de oxigênio neste processo de reação.
{: .prompt-info }

![Ciclo CN](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Como mostrado na figura acima, o carbono, nitrogênio e oxigênio circulam e atuam como catalisadores. No entanto, independentemente do caminho da reação, a equação de reação geral e a quantidade total de energia gerada são as mesmas.

## Leituras Adicionais
- Inkyu Park (Professor do Departamento de Física da Universidade da Cidade de Seul), [Naver Cast Physics Walk: Quantos neutrinos são produzidos no Sol?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Cadeia próton-próton](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [Ciclo CNO](https://en.wikipedia.org/wiki/CNO_cycle)
