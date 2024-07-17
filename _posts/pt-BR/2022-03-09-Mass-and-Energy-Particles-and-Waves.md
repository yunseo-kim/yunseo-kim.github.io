---
title: "Massa e Energia, Partículas e Ondas"
description: >-
  Vamos explorar o princípio da equivalência massa-energia da teoria da relatividade e calcular a energia de um elétron em movimento considerando os efeitos relativísticos.
categories: [Física de Engenharia, Engenharia Nuclear]
tags: [Física Nuclear, Teoria da Relatividade]
math: true
---

## Princípio da Equivalência Massa-Energia
Massa e energia são equivalentes e podem ser convertidas uma na outra.

$$ E=mc^2 $$

Onde $c$ é a velocidade da luz $2,9979 \times 10^{10}\ \text{cm/seg}$

## Elétron-volt (eV)
*Elétron-volt (eV)*: A energia cinética adquirida por um elétron ao passar por uma diferença de potencial de 1V

$$
\begin{align*} 
1 \text{eV} &= 1,60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1,60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Massa e Energia de um Objeto em Movimento
De acordo com a teoria da relatividade, a massa de um objeto em movimento aumenta relativamente do ponto de vista do observador, e a equação relacionando a velocidade e a massa de um objeto em movimento é definida como:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: massa de repouso, $v$: velocidade

A *energia total* de uma partícula é a soma da *energia de massa de repouso* e da *energia cinética*, portanto:

$$ E_{\text{total}} = E_{\text{repouso}}+E_{\text{cinética}} = mc^2$$

$$
\begin{align*}
E_{\text{cinética}} &= E_{\text{total}}-E_{\text{repouso}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

Especialmente, quando $v\ll c$, usando a expansão binomial para aproximação:

$$
\begin{align*}
E_{cinética} &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right]
\\ &= m_0c^2\left[\left(1+\frac{1}{2}v^2/c^2\right)-1\right]
\\ &= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

Que é igual à fórmula da energia cinética na mecânica clássica. Na prática, quando $v\leq 0,2c$ ou $E_{\text{cinética}} \leq 0,02E_{\text{repouso}}$, podemos considerar $v\ll c$ e usar esta aproximação (ou seja, ignorar os efeitos da teoria da relatividade) para obter um valor suficientemente preciso.

### Elétron
Como a energia de repouso do elétron é $E_{\text{repouso}}=m_ec^2=0,511 \text{MeV}$, devemos aplicar a fórmula relativística da energia cinética quando a energia cinética do elétron exceder $0,02\times 0,511 \text{MeV}=0,010 \text{MeV}=10 \text{keV}$. Na engenharia nuclear, a energia dos elétrons frequentemente excede 10keV, então na maioria dos casos devemos aplicar a equação (2).

### Nêutron
A energia de repouso do nêutron é aproximadamente 1000MeV, então $0,02E_{repouso}=20\text{MeV}$. Na engenharia nuclear, é raro lidar com situações onde a energia cinética do nêutron excede 20MeV, então geralmente usamos a equação (3) para calcular a energia cinética do nêutron.

### Fóton
As equações (2) e (3) são válidas apenas quando a massa de repouso não é zero, então não podem ser aplicadas ao fóton, que tem massa de repouso zero. A energia total do fóton é calculada pela seguinte equação:

$$ E = h\nu \tag{4} $$

$h$: constante de Planck ($4,316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: frequência da onda eletromagnética

## Onda de Matéria
Toda matéria na natureza é simultaneamente partícula e onda. Ou seja, todas as partículas têm um comprimento de onda correspondente (*comprimento de onda de de Broglie*). O comprimento de onda $\lambda$ é uma função do momento $p$ e da constante de Planck $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Além disso, o momento $p$ é definido pela seguinte equação:

$$ p = mv \tag{6} $$

### Ignorando efeitos relativísticos (ex: nêutron)
Como a energia cinética é $E=1/2 mv^2$, a equação (6) expressa em função da energia é:

$$ p=\sqrt{2mE} \tag{7} $$

Substituindo isso na equação (5), o comprimento de onda da partícula é:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Na engenharia nuclear, esta equação é usada para calcular o comprimento de onda de de Broglie do nêutron. Substituindo a massa de repouso do nêutron, temos:

$$ \lambda = \frac {2,860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Onde $\lambda$ está em cm e $E$ é a energia cinética do nêutron em eV.

### Considerando efeitos relativísticos (ex: elétron)
Resolvemos diretamente as equações relativísticas anteriores para calcular o momento $p$.

$$ p=\frac {1}{c} \sqrt{E^2_{total}-E^2_{repouso}} \tag{10}$$

Então o comprimento de onda de de Broglie é:

$$ \lambda = \frac {hc}{\sqrt{E_{total}-E_{repouso}}} \tag{11} $$

### Partículas com massa de repouso zero (ex: fóton)
Para partículas com massa de repouso zero, o momento não pode ser calculado pela equação (6), então usamos:

$$ p=\frac {E}{c} \tag{12} $$

Substituindo a equação (12) na equação (5), temos:

$$ \lambda = \frac {hc}{E} \tag{13}$$

Substituindo os valores de $h$ e $c$, a equação final para o comprimento de onda é:

$$ \lambda = \frac {1,240 \times 10^{-6}}{E} \tag{14}$$

Onde $\lambda$ está em m e $E$ está em eV.