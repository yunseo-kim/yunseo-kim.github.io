---
title: Estabilidade Nuclear e Decaimento Radioativo
description: Exploramos a tabela de Segrè, vários tipos de decaimento radioativo, o espectro de energia de elétrons/pósitrons emitidos no decaimento beta e o contexto da descoberta do neutrino, as cadeias de decaimento de alguns nuclídeos importantes (carbono-14, potássio-40, trítio, césio-137), e a transição isomérica.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Pré-requisitos
- [Partículas subatômicas e componentes do átomo](/posts/constituents-of-an-atom/)

## Carta de Segre (Segre Chart) ou Tabela de Nuclídeos
![Carta de Segre](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Para nuclídeos com número atômico $Z$ maior que 20, são necessários mais nêutrons do que prótons para estabilização
- Os nêutrons têm a função de manter o núcleo unido, superando a repulsão elétrica entre os prótons

## Por que ocorre o Decaimento Radioativo
- Apenas certas combinações de nêutrons e prótons formam nuclídeos estáveis
- Se o número de nêutrons em relação ao número de prótons for muito alto ou muito baixo, o nuclídeo se torna instável e sofre *decaimento radioativo*
- O núcleo formado após o decaimento geralmente está em estado excitado, liberando energia na forma de raios gama ou raios-X

## Decaimento Beta ($\beta$-decay)
### Decaimento Beta Positivo ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Ocorre quando há uma deficiência relativa de nêutrons
- Um próton ($p$) se transforma em um nêutron ($n$), emitindo um pósitron ($\beta^+$) e um neutrino eletrônico ($\nu_e$)
- O número atômico diminui em 1, enquanto o número de massa permanece inalterado

Exemplo: $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Decaimento Beta Negativo ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Ocorre quando há um excesso relativo de nêutrons
- Um nêutron ($n$) se transforma em um próton ($p$), emitindo um elétron ($\beta^-$) e um antineutrino eletrônico ($\overline{\nu}_e$)
- O número atômico aumenta em 1, enquanto o número de massa permanece inalterado

Exemplo: $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Espectro de energia dos elétrons (pósitrons) emitidos
![espectro de energia dos elétrons emitidos no decaimento beta](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Fonte da imagem*
> - Autor: Usuário da Wikipédia alemã [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Licença: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Os elétrons ou pósitrons emitidos no decaimento beta apresentam um espectro contínuo de energia, como mostrado acima.
- Decaimento $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- Decaimento $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

> A energia total liberada no decaimento beta é quantizada, mas como o elétron/pósitron e o antineutrino/neutrino compartilham essa energia de forma arbitrária, o espectro de energia do elétron/pósitron aparece como contínuo.
> O fato de que o espectro de energia dos elétrons/pósitrons emitidos no decaimento beta não era quantizado, mas contínuo, era inconsistente com as previsões teóricas e parecia violar a lei de conservação de energia.
> Para explicar esse resultado, Wolfgang Ernst Pauli previu em 11930 a existência de uma '<u>partícula eletricamente neutra, com massa extremamente pequena e reatividade extremamente baixa</u>', propondo chamá-la de 'nêutron'. No entanto, quando Sir James Chadwick descobriu e nomeou o nêutron como o conhecemos hoje em 11932, surgiu um problema de duplicidade de nomes. Em 11933, Enrico Fermi, ao publicar sua teoria do decaimento beta, renomeou a partícula para *neutrino*, adicionando o sufixo italiano '-ino', que significa "pequeno".
> Posteriormente, em 11942, o físico nuclear chinês Wang Ganchang (王淦昌) foi o primeiro a propor um método para detectar neutrinos usando [captura eletrônica](#captura-eletrônica-electron-capture-ou-captura-k-k-capture). Em 11956, Clyde Cowan, Frederick Reines, Francis B. Harrison, Herald W. Kruse e Austin D. McGuire conseguiram detectar neutrinos através do experimento Cowan-Reines, publicando seus resultados na revista Science. Frederick Reines recebeu o Prêmio Nobel de Física em 11995 por essa contribuição.
> Assim, o estudo do decaimento beta tem grande significado na história da ciência por ter fornecido pistas sobre a existência dos neutrinos.
{: .prompt-info }

### Cadeia de Decaimento (Decay Chain)
Frequentemente, o *nuclídeo filho (daughter nuclide)* formado pelo decaimento beta também é instável e sofre decaimentos beta subsequentes. Isso leva a uma *cadeia de decaimento (decay chain)* como a seguinte:

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (estável)} $$

### Decaimentos Beta Importantes
A seguir, apresentarei alguns decaimentos beta importantes.

#### Carbono-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> O carbono-14 é produzido naturalmente na alta atmosfera pela radiação cósmica, mantendo uma concentração relativamente constante no ar. Animais e plantas também mantêm a mesma concentração de carbono-14 em seus corpos durante a vida, pois continuamente trocam gases com a atmosfera através da respiração. Após a morte, essa troca cessa e a concentração de carbono-14 no cadáver diminui com o tempo devido ao decaimento. Este é o princípio da datação por radiocarbono.
{: .prompt-tip }

#### Potássio-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> O potássio-40 é a maior fonte natural de radiação no corpo humano e em todos os animais, estando naturalmente presente em todos os alimentos que consumimos, especialmente em castanha-do-pará, feijão, espinafre, banana, abacate, café, peixe-espada e alho.
> Um adulto de 70kg tem cerca de 140g de potássio em seu corpo, mantido em nível constante, dos quais aproximadamente 0,014g é potássio-40, correspondendo a uma atividade radioativa de cerca de 4330 Bq.
{: .prompt-tip }

#### Trítio
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> O trítio é um material combustível que participa da reação de fusão D-T em reatores de fusão nuclear ou bombas de hidrogênio/bombas de nêutrons. É produzido naturalmente na atmosfera por raios cósmicos, mas devido à sua meia-vida relativamente curta de 12,32 anos, decai rapidamente e existe em proporções muito baixas na natureza. Quando utilizado em reatores de fusão ou armas nucleares, devido à sua rápida decomposição, em vez de carregar diretamente o trítio, utiliza-se um método que irradia nêutrons no lítio-6 para produzir trítio. Por esse motivo, o lítio-6 altamente enriquecido e de alta pureza para uso em armas nucleares é considerado um material essencial para o desenvolvimento nuclear e é um dos principais alvos de monitoramento da comunidade internacional, incluindo a AIEA.  
> Além dos usos mencionados, é um material usado em pequenas quantidades, mas comum, como em miras noturnas de equipamentos militares como o rifle K2 e a submetralhadora K1, relógios luminosos e sinalizações de saída de emergência em edifícios que precisam manter capacidade luminosa sem fornecimento de energia. O trítio é envolvido por fósforo, um material fluorescente, de modo que quando os raios beta emitidos durante o decaimento do trítio colidem com o fósforo, produzem luz. No caso das sinalizações de saída de emergência, são utilizados aproximadamente 900 bilhões de becquerels de trítio.  
> Devido à demanda constante e à impossibilidade de armazenamento a longo prazo, é tratado como um recurso estratégico importante, com preço aproximado de 30.000 dólares por grama. Atualmente, a maior parte do trítio produzido e vendido comercialmente vem de reatores CANDU (CANada Deuterium Uranium), que são reatores de água pesada pressurizada. Na Coreia, as unidades 1-4 de Wolsong são reatores CANDU.
{: .prompt-tip }

#### Césio-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> O césio-137 é um subproduto importante de reações de fissão em reatores nucleares e testes nucleares. Devido à sua meia-vida relativamente longa (cerca de 30 anos), à emissão de raios gama penetrantes e às propriedades químicas semelhantes às do potássio, que facilitam sua absorção pelo corpo, é um nuclídeo que requer monitoramento e gerenciamento cuidadosos. Originalmente quase inexistente na natureza, hoje está presente no solo em todo o planeta numa média de 7 μg/g, resultado do teste nuclear Trinity e das bombas atômicas de Hiroshima e Nagasaki lançadas pelos EUA para derrotar o Império Japonês, além de numerosos testes atmosféricos realizados principalmente nas décadas de 11950-11960 e alguns acidentes nucleares graves (como o acidente de Chernobyl e o acidente de Goiânia no Brasil).
> Quando mais de 10000 Bq de césio-137 são absorvidos pelo corpo, pode ser necessário tratamento médico e observação. Alguns moradores próximos ao acidente de Chernobyl tiveram dezenas de milhares de Bq de césio-137 absorvidos. No caso do acidente nuclear de Fukushima, os moradores próximos absorveram cerca de 50-250 Bq logo após o acidente.
> Embora haja variações individuais e entre diferentes fontes, a meia-vida biológica do césio-137 sem tratamento é de aproximadamente [110 dias, segundo o CDC](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp). Em caso de suspeita de exposição a grandes quantidades de césio-137, [a ingestão de comprimidos de azul da Prússia medicinal pode acelerar a excreção, reduzindo a meia-vida biológica para cerca de 30 dias](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp).
{: .prompt-tip }

## Captura Eletrônica (Electron Capture) ou Captura K (K-capture)

$$ p + e \to n + \nu_e $$

- Ocorre quando há uma deficiência relativa de nêutrons
- Captura um elétron da camada mais interna (camada K) para converter um próton do núcleo em um nêutron
- O número atômico diminui em 1, enquanto o número de massa permanece inalterado
- Após a captura eletrônica, forma-se um espaço vazio na nuvem eletrônica, que é posteriormente preenchido por um elétron de uma camada externa, resultando na emissão de raios-X ou elétrons Auger
- O nuclídeo filho produzido pela captura eletrônica é idêntico ao produzido pelo decaimento $\beta^+$, portanto esses dois processos competem entre si.

## Decaimento Alfa ($\alpha$-decay)
- Emissão de uma partícula alfa ($\alpha$, $^4_2\mathrm{He}$)
- O número atômico diminui em 2 e o número de massa diminui em 4
- Comum em núcleos mais pesados que o chumbo
- Diferentemente do decaimento beta, a energia das partículas alfa emitidas no decaimento alfa é quantizada.

Exemplo: $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Fissão Espontânea (Spontaneous Fission)
- Nuclídeos muito pesados e instáveis podem sofrer fissão espontaneamente, sem absorver nêutrons
- Incluída no conceito amplo de decaimento radioativo
- O urânio-238, por exemplo, sofre decaimento alfa com meia-vida de $10^9$ anos, mas também, raramente, fissão espontânea com meia-vida de aproximadamente $10^{16}$ anos. A tabela a seguir mostra a meia-vida de fissão espontânea de alguns nuclídeos.

| Nuclídeo | Meia-vida de fissão espontânea | Características |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | Aproximadamente $10^{16}$ anos | Ocorre muito raramente |
| $^{240}\mathrm{Pu}$ | Aproximadamente $10^{11}$ anos | Nuclídeo físsil usado em armas nucleares |
| $^{252}\mathrm{Cf}$ | Aproximadamente $2.6$ anos | Fissão espontânea extremamente ativa <br>$\rightarrow$ Usado como fonte de nêutrons para inicialização de reatores |

## Emissão de Prótons (Proton Emission)
- Nuclídeos extremamente instáveis com excesso de prótons podem emitir um único próton
- O número atômico e o número de massa diminuem em 1
- Ocorre muito raramente

## Esquema de Decaimento e Transição Isomérica
### Esquema de Decaimento (Decay Scheme)
*Esquema de decaimento (decay scheme)*: Diagrama visual que representa todas as vias de decaimento de um material radioativo

### Transição Isomérica (Isomeric Transition)
- Os núcleos formados após o decaimento radioativo podem permanecer em estado excitado, liberando energia na forma de raios gama (embora a emissão de raios gama não altere o nuclídeo, convencionalmente às vezes é chamada de decaimento gama).
- A maioria dos núcleos excitados emite raios gama e transita para o estado fundamental muito rapidamente, mas em casos específicos, a emissão de raios gama pode ser retardada, parecendo um estado metaestável. Esses estados retardados são chamados de *estados isoméricos (isomeric states)* do núcleo.
- A transição de um estado isomérico para o estado fundamental através da emissão de raios gama é chamada de *transição isomérica (isomeric transition)*, abreviada como IT.

![Esquema de Decaimento do Au-198](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia britânico [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Licença: Livre para uso sem restrições para qualquer finalidade, desde que não viole a lei

![Esquema de Decaimento do Cs-137](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> Licença: [Domínio Público](https://en.wikipedia.org/wiki/Public_domain)
