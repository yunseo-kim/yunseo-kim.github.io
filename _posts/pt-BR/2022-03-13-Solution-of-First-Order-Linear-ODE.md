---
title: Solução de EDOs Lineares de Primeira Ordem
description: Aprenda o método de solução para equações diferenciais ordinárias lineares de primeira ordem.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Equação Diferencial Ordinária Linear de Primeira Ordem
Uma equação diferencial ordinária de primeira ordem que pode ser escrita algebricamente na forma

$$ y'+p(x)y=r(x) \tag{1} $$

é chamada de **linear**, e caso contrário, é chamada de **não linear**.

A forma da equação (1) é chamada de **forma padrão (standard form)** de uma equação diferencial ordinária linear de primeira ordem. Se o primeiro termo de uma EDO linear de primeira ordem dada for $f(x)y'$, podemos obter a forma padrão dividindo ambos os lados da equação por $f(x)$.

Na engenharia, $r(x)$ é frequentemente chamado de **entrada (input)**, e $y(x)$ é chamado de **saída (output)** ou **resposta (response)** à entrada (e às condições iniciais).

## Equação Diferencial Ordinária Linear Homogênea
Seja $J$ um intervalo $a<x<b$ no qual queremos resolver a equação (1). Se $r(x)\equiv 0$ no intervalo $J$, a equação se torna

$$ y'+p(x)y=0 \tag{2}$$

e é chamada de **homogênea**. Neste caso, podemos usar o [método de separação de variáveis](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Para o caso $c=0$, obtemos a **solução trivial** $y(x)=0$.

## Equação Diferencial Ordinária Linear Não Homogênea
Se $r(x)\not\equiv 0$ no intervalo $J$, a equação é chamada de **não homogênea**. Sabe-se que a equação diferencial linear não homogênea (1) possui um fator integrante que depende apenas de $x$. Este fator integrante $F(x)$ pode ser obtido pela equação (11) do [método para encontrar o fator integrante](/posts/Exact-Differential-Equation-and-Integrating-Factor/#metodo-para-encontrar-o-fator-integrante), ou pode ser derivado diretamente como se segue.

Multiplicando a equação (1) por $F(x)$, obtemos

$$ Fy'+pFy=rF \tag{1*} $$

Se

$$ pF=F' $$

então o lado esquerdo da equação (1*) se torna a derivada $(Fy)'=F'y+Fy'$. Separando as variáveis em $pF=F'$, obtemos $dF/F=p\ dx$. Integrando e definindo $h=\int p\ dx$, temos:

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Substituindo na equação (1*), temos

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrando, obtemos

$$ e^hy=\int e^hr\ dx + c $$
e, dividindo por $e^h$, encontramos a fórmula da solução desejada.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Aqui, a constante de integração em $h$ não importa.

Na equação (4), o único valor que depende da condição inicial dada é $c$. Portanto, se escrevermos a equação (4) como a soma de dois termos

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

podemos ver o seguinte:

$$ \text{Saída total}=\text{Resposta à entrada }r+\text{Resposta à condição inicial} \tag{5} $$

## Exemplo: Circuito RL
Considere um circuito $RL$ composto por uma bateria com força eletromotriz $E=48\textrm{V}$, um resistor com $R=11\mathrm{\Omega}$ e um indutor com $L=0.1\text{H}$. A corrente inicial é zero. Modele este circuito $RL$ e resolva a equação diferencial ordinária resultante para a corrente $I(t)$.
> **Lei de Ohm (Ohm's law)**  
> A corrente $I$ em um circuito causa uma queda de tensão (voltage drop) $RI$ através do resistor.
{: .prompt-info }

> **Lei da indução eletromagnética de Faraday (Faraday's law of electromagnetic induction)**  
> A corrente $I$ em um circuito causa uma queda de tensão $LI'=L\ dI/dt$ através do indutor.
{: .prompt-info }

> **Lei das Malhas de Kirchhoff (Kirchhoff's Voltage Law; KVL)**  
> A força eletromotriz aplicada a um circuito fechado é igual à soma das quedas de tensão em todos os outros elementos do circuito.
{: .prompt-info }

### Solução
De acordo com as leis acima, o modelo para o circuito $RL$ é $LI'+RI=E(t)$. Escrevendo na forma padrão, temos:

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Podemos resolver esta equação diferencial linear substituindo $x=t, y=I, p=R/L, h=(R/L)t$ na equação (4).

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Neste caso, como $R/L=11/0.1=110$ e $E(t)=48$, temos:

$$ I=\frac{48}{11}+ce^{-110t} $$

A partir da condição inicial $I(0)=0$, obtemos $I(0)=E/R+c=0$, o que implica $c=-E/R$. Com isso, podemos encontrar a seguinte solução particular:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
