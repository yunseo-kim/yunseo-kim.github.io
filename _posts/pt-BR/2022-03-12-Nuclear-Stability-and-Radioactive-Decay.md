---
title: Estabilidade Nuclear e Decaimento Radioativo
description: Aprenda sobre o gráfico de Segré, tipos de decaimento radioativo e transição
  isomérica.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Gráfico de Segré ou Tabela de Nuclídeos
![Gráfico de Segré](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Para nuclídeos com número atômico $Z$ maior que 20, são necessários mais nêutrons do que prótons para estabilização
- Os nêutrons desempenham o papel de manter o núcleo unido, superando a repulsão elétrica entre os prótons

## Por que ocorre o Decaimento Radioativo
- Apenas certas combinações de nêutrons e prótons formam nuclídeos estáveis
- Se o número de nêutrons em relação ao número de prótons for muito alto ou muito baixo, o nuclídeo é instável e sofre *decaimento radioativo*
- O núcleo formado após o decaimento geralmente está em um estado excitado, liberando energia na forma de raios gama ou raios X

## Decaimento Beta ($\beta$-decay)
### Decaimento Beta Positivo ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Ocorre quando há uma relativa falta de nêutrons
- Um próton ($p$) se transforma em um nêutron ($n$), emitindo um pósitron ($\beta^+$) e um neutrino eletrônico ($\nu_e$)
- O número atômico diminui em 1, o número de massa não muda

Exemplo: $^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### Decaimento Beta Negativo ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Ocorre quando há um excesso relativo de nêutrons
- Um nêutron ($n$) se transforma em um próton ($p$), emitindo um elétron ($\beta^-$) e um antineutrino eletrônico ($\overline{\nu}_e$)
- O número atômico aumenta em 1, o número de massa não muda

Exemplo: $^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### Espectro de Energia dos Elétrons (Pósitrons) Emitidos
![Espectro de energia dos elétrons emitidos no decaimento beta](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Fonte da imagem*
> - Autor: Usuário da Wikipédia alemã [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Licença: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Os elétrons ou pósitrons emitidos no decaimento beta mostram um espectro de energia contínuo como o mostrado acima.
- Decaimento $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- Decaimento $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

### Cadeia de Decaimento
Frequentemente, o *nuclídeo filho* formado pelo decaimento beta também é instável e sofre decaimento beta subsequente. Isso leva a uma *cadeia de decaimento* como a seguinte:

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (estável)} $$ 

## Captura de Elétrons ou Captura K

$$ p + e \to n + \nu_e $$

- Ocorre quando há uma relativa falta de nêutrons
- Captura um elétron da camada mais interna (camada K) e converte um próton do núcleo em um nêutron
- O número atômico diminui em 1, o número de massa não muda
- Após a captura de elétrons, forma-se um espaço vazio na nuvem de elétrons, que é posteriormente preenchido por um elétron de uma camada externa, emitindo raios X ou elétrons Auger
- O nuclídeo filho formado pela captura de elétrons é idêntico ao formado pelo decaimento $\beta^+$, então esses dois processos competem entre si.

## Decaimento Alfa ($\alpha$-decay)
- Emite uma partícula alfa ($\alpha$, $^4_2\text{He}$)
- O número atômico diminui em 2 e o número de massa diminui em 4
- Comum em núcleos mais pesados que o chumbo
- Diferentemente do decaimento beta, a energia das partículas alfa emitidas no decaimento alfa é quantizada.

Exemplo: $^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## Fissão Espontânea
- Nuclídeos muito pesados e instáveis podem sofrer fissão espontaneamente, sem absorver nêutrons
- Incluído no decaimento radioativo em sentido amplo

## Emissão de Prótons
- Em nuclídeos extremamente instáveis com excesso de prótons, um único próton pode ser emitido
- O número atômico e o número de massa diminuem em 1
- Ocorre muito raramente

## Esquema de Decaimento e Transição Isomérica
### Esquema de Decaimento
*Esquema de decaimento*: Um diagrama que representa visualmente todas as vias de decaimento de um material radioativo

### Transição Isomérica
- Os núcleos formados pelo decaimento radioativo podem permanecer em um estado excitado após a transformação, emitindo energia na forma de raios gama (embora a emissão de raios gama não mude o nuclídeo, convencionalmente às vezes é chamada de decaimento gama).
- A maioria dos núcleos excitados emite raios gama e transita para o estado fundamental em um tempo muito curto, mas em certos casos, a emissão de raios gama é atrasada, parecendo um estado metaestável. Este estado atrasado é chamado de *estado isomérico* do núcleo.
- A transição do estado isomérico para o estado fundamental através da emissão de raios gama é chamada de *transição isomérica* e é indicada por IT.
![Esquema de Decaimento do Au-198](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia do Reino Unido [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Licença: Pode ser usado livremente para qualquer propósito sem restrições, desde que não viole a lei
