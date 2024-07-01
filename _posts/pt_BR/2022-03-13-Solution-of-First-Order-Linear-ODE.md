---
title: "Solução de Equações Diferenciais Ordinárias Lineares de Primeira Ordem"
description: >-
  Vamos aprender como resolver equações diferenciais ordinárias lineares de primeira ordem.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
---

## Equação Diferencial Ordinária Linear de Primeira Ordem
Se uma equação diferencial ordinária de primeira ordem pode ser algebricamente colocada na forma

$$ y'+p(x)y=r(x) \tag{1} $$

ela é chamada de **linear**; caso contrário, é chamada de **não linear**.

A forma da equação (1) é chamada de **forma padrão** de uma equação diferencial ordinária linear de primeira ordem. Se o primeiro termo de uma equação diferencial ordinária linear de primeira ordem dada for $f(x)y'$, podemos obter a forma padrão dividindo ambos os lados da equação por $f(x)$.

Na engenharia, $r(x)$ é frequentemente chamado de **entrada (input)**, e $y(x)$ é chamado de **saída (output)** ou **resposta (response)** à entrada (e às condições iniciais).

## Equação Diferencial Ordinária Linear Homogênea
Seja $J$ o intervalo $a<x<b$ no qual queremos resolver a equação (1). Se $r(x)\equiv 0$ na equação (1) para o intervalo $J$, temos

$$ y'+p(x)y=0 \tag{2}$$

e isso é chamado de **homogêneo**. Neste caso, podemos usar o [método de separação de variáveis](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Quando $c=0$, obtemos a **solução trivial** $y(x)=0$.

## Equação Diferencial Ordinária Linear Não Homogênea
Quando $r(x)\not\equiv 0$ no intervalo $J$, chamamos de **não homogêneo**. Sabe-se que a equação diferencial ordinária linear não homogênea (1) tem um fator integrante que depende apenas de $x$. Este fator integrante $F(x)$ pode ser encontrado usando a equação (11) do [método para encontrar fatores integrantes](/posts/Exact-Differential-Equation-and-Integrating-Factor/#método-para-encontrar-o-fator-integrante), ou pode ser encontrado diretamente da seguinte maneira:

Multiplicando a equação (1) por $F(x)$, obtemos

$$ Fy'+pFy=rF \tag{1*} $$

Se

$$ pF=F' $$

então o lado esquerdo da equação (1*) se torna a derivada $(Fy)'=F'y+Fy'$. Separando as variáveis em $pF=F'$, temos $dF/F=p\ dx$, e integrando e escrevendo $h=\int p\ dx$, temos

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Substituindo na equação (1*), obtemos

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrando, temos

$$ e^hy=\int e^hr\ dx + c $$
e dividindo por $e^h$, obtemos a fórmula da solução desejada.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Neste caso, a constante de integração em $h$ não é um problema.

Na equação (4), o único valor que depende da condição inicial dada é $c$, então podemos escrever a equação (4) como a soma de dois termos

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

a partir disso, podemos ver que:

$$ \text{Saída total}=\text{Resposta à entrada }r+\text{Resposta à condição inicial} \tag{5} $$

## Exemplo: Circuito RL
Suponha que um circuito RL consiste em uma bateria com força eletromotriz $E=48\textrm{V}$, um resistor com $R=11\mathrm{\Omega}$, e um indutor com $L=0.1\text{H}$, e que a corrente inicial é 0. Encontre o modelo deste circuito RL e resolva a equação diferencial resultante para a corrente $I(t)$.
> **Lei de Ohm**  
> A corrente $I$ no circuito causa uma queda de tensão $RI$ nos terminais do resistor.
{: .prompt-info }

> **Lei de Faraday da indução eletromagnética**  
> A corrente $I$ no circuito causa uma queda de tensão $LI'=L\ dI/dt$ nos terminais do indutor.
{: .prompt-info }

> **Lei das Tensões de Kirchhoff (KVL)**  
> A força eletromotriz aplicada a um circuito fechado é igual à soma das quedas de tensão em todos os outros elementos do circuito.
{: .prompt-info }

### Solução
De acordo com as leis acima, o modelo do circuito RL é $LI'+RI=E(t)$, e na forma padrão é

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Podemos resolver esta equação diferencial linear usando a equação (4) com $x=t, y=I, p=R/L, h=(R/L)t$.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Onde $R/L=11/0.1=110$ e $E(t)=48$, então

$$ I=\frac{48}{11}+ce^{-110t} $$

Da condição inicial $I(0)=0$, obtemos $I(0)=E/R+c=0$, $c=-E/R$. A partir disso, podemos encontrar a seguinte solução particular:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$