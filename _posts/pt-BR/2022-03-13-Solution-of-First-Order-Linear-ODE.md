---
title: Solução de EDOs Lineares de Primeira Ordem
description: Aprenda o método de solução para equações diferenciais ordinárias (EDOs) lineares de primeira ordem, incluindo casos homogêneos e não homogêneos.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Equação Diferencial Ordinária Linear de Primeira Ordem
Se uma equação diferencial ordinária de primeira ordem pode ser escrita algebricamente na forma

$$ y'+p(x)y=r(x) \tag{1} $$

ela é chamada de **linear**, caso contrário, é chamada de **não linear**.

A forma da equação (1) é chamada de **forma padrão** de uma EDO linear de primeira ordem. Se o primeiro termo de uma dada EDO linear de primeira ordem for $f(x)y'$, podemos obter a forma padrão dividindo ambos os lados da equação por $f(x)$.

Na engenharia, $r(x)$ é frequentemente chamado de **entrada (input)**, e $y(x)$ é chamado de **saída (output)** ou **resposta (response)** à entrada (e às condições iniciais).

## Equação Diferencial Ordinária Linear Homogênea
Seja $J$ um intervalo $a<x<b$ no qual queremos resolver a equação (1). Se $r(x)\equiv 0$ no intervalo $J$, a equação se torna

$$ y'+p(x)y=0 \tag{2}$$

e é chamada de **homogênea**. Neste caso, podemos usar o [método de separação de variáveis](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Para $c=0$, obtemos a **solução trivial** $y(x)=0$.

## Equação Diferencial Ordinária Linear Não Homogênea
Se $r(x)\not\equiv 0$ no intervalo $J$, a equação é chamada de **não homogênea**. Sabe-se que a equação diferencial linear não homogênea (1) possui um fator integrante que depende apenas de $x$. Este fator integrante $F(x)$ pode ser encontrado usando a equação (11) do [método para encontrar o fator integrante](/posts/Exact-Differential-Equation-and-Integrating-Factor/#método-para-encontrar-o-fator-integrante), ou pode ser derivado diretamente como a seguir.

Multiplicando a equação (1) por $F(x)$, obtemos

$$ Fy'+pFy=rF \tag{1*} $$

Se

$$ pF=F' $$

então o lado esquerdo da equação (1*) se torna a derivada $(Fy)'=F'y+Fy'$. Separando as variáveis em $pF=F'$, obtemos $dF/F=p\ dx$. Integrando e definindo $h=\int p\ dx$, temos

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Substituindo na equação (1*), obtemos

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrando,

$$ e^hy=\int e^hr\ dx + c $$
e, dividindo por $e^h$, obtemos a fórmula da solução desejada.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Aqui, a constante de integração em $h$ não importa.

Como o único valor na equação (4) que depende da condição inicial dada é $c$, se escrevermos a equação (4) como a soma de dois termos

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

podemos ver o seguinte:

$$ \text{Saída total}=\text{Resposta à entrada }r+\text{Resposta à condição inicial} \tag{5} $$

## Exemplo: Circuito RL
Considere um circuito $RL$ composto por uma bateria com uma força eletromotriz (f.e.m.) de $E=48\textrm{V}$, um resistor de $R=11\mathrm{\Omega}$ e um indutor de $L=0.1\text{H}$. A corrente inicial é zero. Modele este circuito $RL$ e resolva a equação diferencial ordinária resultante para a corrente $I(t)$.
> **Lei de Ohm**  
> A corrente $I$ em um circuito causa uma queda de tensão $RI$ através do resistor.
{: .prompt-info }

> **Lei de Faraday da indução eletromagnética**  
> A corrente $I$ em um circuito causa uma queda de tensão $LI'=L\ dI/dt$ através do indutor.
{: .prompt-info }

> **Lei de Kirchhoff das Tensões (LKT)**  
> A força eletromotriz aplicada a um circuito fechado é igual à soma das quedas de tensão em todos os outros elementos do circuito.
{: .prompt-info }

### Solução
De acordo com as leis acima, o modelo para o circuito $RL$ é $LI'+RI=E(t)$. Escrevendo-o na forma padrão:

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Podemos resolver esta EDO linear substituindo $x=t, y=I, p=R/L, h=(R/L)t$ na equação (4).

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Aqui, como $R/L=11/0.1=110$ e $E(t)=48$:

$$ I=\frac{48}{11}+ce^{-110t} $$

A partir da condição inicial $I(0)=0$, obtemos $I(0)=E/R+c=0$, então $c=-E/R$. Com isso, podemos encontrar a seguinte solução particular:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
