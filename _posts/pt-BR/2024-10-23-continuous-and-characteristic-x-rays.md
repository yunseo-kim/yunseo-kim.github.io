---
title: Raios X Contínuos e Característicos
description: Exploramos os dois princípios de geração de raios X como radiação atômica
  e as características respectivas do bremsstrahlung e dos raios X característicos.
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **bremsstrahlung (radiação de frenagem)**: raios X de espectro contínuo emitidos quando partículas carregadas, como elétrons, passam perto de núcleos atômicos e são aceleradas devido à força elétrica
> - Comprimento de onda mínimo: $\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **Raios X característicos**: raios X de espectro descontínuo emitidos quando um elétron incidente colide com um elétron de uma camada interna do átomo, ionizando-o, e um elétron de uma camada externa transita para preencher a vacância, liberando energia equivalente à diferença entre os dois níveis energéticos
{: .prompt-info }

## Prerequisites
- [Partículas Subatômicas e Constituintes do Átomo](/posts/constituents-of-an-atom/)

## Descoberta dos Raios X
Röntgen descobriu que os raios X eram produzidos quando um feixe de elétrons era direcionado a um alvo. Como na época do descobrimento não se sabia que os raios X eram ondas eletromagnéticas, foram denominados **raios X** devido à sua natureza desconhecida, e também são chamados de **radiação Röntgen** em homenagem ao seu descobridor.

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

A imagem acima mostra a estrutura simplificada de um tubo de raios X típico. O tubo contém um cátodo com filamento de tungstênio e um ânodo com alvo fixo, selados em vácuo. Quando uma alta tensão de dezenas de kV é aplicada entre os eletrodos, elétrons são emitidos do cátodo e direcionados ao alvo no ânodo, produzindo raios X. No entanto, a eficiência de conversão em raios X é geralmente menor que 1%, com mais de 99% da energia sendo convertida em calor, necessitando assim de um sistema de resfriamento adicional.

## bremsstrahlung (radiação de frenagem)
Quando partículas carregadas, como elétrons, passam próximas a núcleos atômicos, são bruscamente desviadas e desaceleradas devido à força elétrica entre a partícula e o núcleo, liberando energia na forma de raios X. Como essa conversão de energia não é quantizada, os raios X emitidos apresentam um espectro contínuo, conhecido como **bremsstrahlung** ou **radiação de frenagem**.

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

Contudo, a energia dos fótons de raios X emitidos por bremsstrahlung não pode exceder a energia cinética do elétron incidente. Portanto, existe um comprimento de onda mínimo para os raios X emitidos, que pode ser calculado pela seguinte equação:

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

Como a constante de Planck $h$ e a velocidade da luz $c$ são constantes, este comprimento de onda mínimo é determinado apenas pela energia do elétron incidente. O comprimento de onda $\lambda$ correspondente a $1\text{eV}$ de energia é aproximadamente $1.24 \mu\text{m}=12400\text{Å}$. Assim, o comprimento de onda mínimo $\lambda_\text{min}$ quando uma tensão de $V$ volts é aplicada ao tubo de raios X é:

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

O gráfico a seguir mostra o espectro contínuo de raios X para diferentes tensões, mantendo a corrente do tubo constante. Pode-se observar que com o aumento da tensão, o comprimento de onda mínimo $\lambda_{\text{min}}$ diminui e a intensidade geral dos raios X aumenta.

![Typical continuous X-ray spectra from tube operating
at three different peak voltages with the same current](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## Raios X característicos
Se a tensão aplicada ao tubo de raios X for suficientemente alta, o elétron incidente pode colidir com um elétron de uma camada interna do átomo alvo, ionizando-o. Neste caso, um elétron de uma camada externa rapidamente preenche a vacância na camada interna, liberando um fóton de raio X com energia igual à diferença entre os dois níveis energéticos. O espectro dos raios X emitidos neste processo é descontínuo e é determinado pelos níveis de energia característicos do átomo alvo, independentemente da energia ou intensidade do feixe de elétrons incidente. Estes são chamados de **raios X característicos**.

### Notação de Siegbahn

![Siegbahn notation of electron transitions between shells](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *Fonte da imagem*
> - Autor: usuário da Wikipedia em inglês [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Na notação de Siegbahn, os raios X emitidos quando elétrons das camadas L, M, ... preenchem uma vacância na camada K são designados como $K_\alpha$, $K_\beta$, ... como mostrado na imagem acima. Com o advento do modelo atômico moderno após a notação de Siegbahn, descobriu-se que para átomos multieletrônicos, os níveis de energia dentro de cada camada (níveis com mesmo número quântico principal) também variam de acordo com outros números quânticos, levando a subdivisões como $K_{\alpha_1}$, $K_{\alpha_2}$, ... para cada $K_\alpha$, $K_\beta$, ...

![Siegbahn notation](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

Esta notação tradicional ainda é amplamente utilizada em espectroscopia. No entanto, devido à sua falta de sistematização e possíveis confusões, a *União Internacional de Química Pura e Aplicada (IUPAC)* recomenda o uso de uma notação alternativa.

### Notação IUPAC
A IUPAC recomenda a seguinte notação padrão para orbitais atômicos e raios X característicos.
Primeiro, cada orbital atômico recebe um nome conforme a tabela abaixo:

| $n$(número <br>quântico <br>principal) | $l$(número <br>quântico <br>azimutal) | $s$(número <br>quântico <br>de spin) | $j$(número <br>quântico de <br>momento <br>angular total) | Orbital <br>atômico | Notação <br>de raio X |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0$ | $\pm1/2$ | $1/2$ | $1s_{1/2}$ | $K_{(1)}$ |
| $2$ | $0$ | $\pm1/2$ | $1/2$ | $2s_{1/2}$ | $L_1$ |
| $2$ | $1$ | $-1/2$ | $1/2$ | $2p_{1/2}$ | $L_2$ |
| $2$ | $1$ | $+1/2$ | $3/2$ | $2p_{3/2}$ | $L_3$ |
| $3$ | $0$ | $\pm1/2$ | $1/2$ | $3s_{1/2}$ | $M_1$ |
| $3$ | $1$ | $-1/2$ | $1/2$ | $3p_{1/2}$ | $M_2$ |
| $3$ | $1$ | $+1/2$ | $3/2$ | $3p_{3/2}$ | $M_3$ |
| $3$ | $2$ | $-1/2$ | $3/2$ | $3d_{3/2}$ | $M_4$ |
| $3$ | $2$ | $+1/2$ | $5/2$ | $3d_{5/2}$ | $M_5$ |
| $4$ | $0$ | $\pm1/2$ | $1/2$ | $4s_{1/2}$ | $N_1$ |
| $4$ | $1$ | $-1/2$ | $1/2$ | $4p_{1/2}$ | $N_2$ |
| $4$ | $1$ | $+1/2$ | $3/2$ | $4p_{3/2}$ | $N_3$ |
| $4$ | $2$ | $-1/2$ | $3/2$ | $4d_{3/2}$ | $N_4$ |
| $4$ | $2$ | $+1/2$ | $5/2$ | $4d_{5/2}$ | $N_5$ |
| $4$ | $3$ | $-1/2$ | $5/2$ | $4f_{5/2}$ | $N_6$ |
| $4$ | $3$ | $+1/2$ | $7/2$ | $4f_{7/2}$ | $N_7$ |

> Número quântico de momento angular total $j=\|l+s\|$.
{: .prompt-info }

Os raios X característicos emitidos quando um elétron transita de um nível de energia mais alto para um mais baixo são designados seguindo a regra:

$$ \text{(notação do nível final)-(notação do nível inicial)} $$

Por exemplo, um raio X característico emitido quando um elétron transita do orbital $2p_{1/2}$ para $1s_{1/2}$ é denominado $\text{K-L}_2$.

## Espectro de Raios X

![Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

A imagem acima mostra o espectro de raios X emitido quando um feixe de elétrons acelerado a 60kV incide sobre um alvo de ródio (Rh). Observa-se uma curva suave e contínua devido ao bremsstrahlung, com raios X emitidos apenas para comprimentos de onda maiores que aproximadamente $0.207\text{Å} = 20.7\text{pm}$, conforme a equação ($\ref{eqn:lambda_min}$). Os picos agudos no gráfico são devidos aos raios X característicos da camada K do ródio. Como cada átomo alvo possui seu próprio espectro característico de raios X, é possível identificar os elementos constituintes de um alvo analisando os comprimentos de onda onde ocorrem os picos no espectro de raios X emitido.

> Embora raios X de menor energia como $L_\alpha$, $L_\beta$, ... também sejam emitidos além de $K_\alpha$, $K_\beta$, ..., eles possuem energia muito menor e geralmente são absorvidos pela carcaça do tubo de raios X antes de alcançar o detector.
{: .prompt-info }
