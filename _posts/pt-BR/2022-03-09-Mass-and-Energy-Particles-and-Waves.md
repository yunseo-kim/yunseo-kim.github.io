---
title: Massa e energia, partículas e ondas
description: Explore o princípio da equivalência massa-energia da teoria da relatividade e calcule a energia de elétrons em movimento considerando efeitos relativísticos.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## Princípio da equivalência massa-energia
Massa e energia são idênticas e podem ser convertidas uma na outra.

$$ E=mc^2 $$

Onde $c$ é a velocidade da luz $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Elétron-volt (Electron Volt, eV)
*Elétron-volt (electron volt, eV)*: A energia cinética adquirida por um elétron ao passar por uma diferença de potencial de 1V

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Massa e energia de objetos em movimento
De acordo com a teoria da relatividade, a massa de um objeto em movimento, do ponto de vista do observador, aumenta relativamente, e a equação relacionando a velocidade e a massa de um objeto em movimento é definida como:

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

Especialmente quando $v\ll c$, colocando $\cfrac{v^2}{c^2} = \epsilon$ e aproximando por expansão de Taylor em torno de $\epsilon = 0$ (ou seja, expansão de Maclaurin):

$$
\begin{align*}
E_{\text{cinética}} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

que é igual à fórmula da energia cinética na mecânica clássica. Na prática, quando $v\leq 0.2c$ ou $E_{\text{cinética}} \leq 0.02E_{\text{repouso}}$, podemos considerar $v\ll c$ e usar esta aproximação (ou seja, ignorar os efeitos relativísticos) para obter valores suficientemente precisos.

### Elétron
Como a energia de repouso do elétron é $E_{\text{repouso}}=m_ec^2=0.511 \text{MeV}$, quando a energia cinética do elétron excede $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$, devemos aplicar a fórmula relativística da energia cinética. Na engenharia nuclear, a energia dos elétrons frequentemente excede 10keV, portanto na maioria dos casos devemos aplicar a equação (2).

### Nêutron
A energia de repouso do nêutron é aproximadamente 1000MeV, então $0.02E_{repouso}=20\text{MeV}$. Na engenharia nuclear, raramente lidamos com situações onde a energia cinética do nêutron excede 20MeV, portanto geralmente calculamos a energia cinética do nêutron usando a equação (3).

### Fóton
As equações (2) e (3) são válidas apenas quando a massa de repouso não é zero, portanto não podem ser aplicadas ao fóton, que tem massa de repouso zero. A energia total do fóton é calculada pela seguinte equação:

$$ E = h\nu \tag{4} $$

$h$: constante de Planck ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: frequência da onda eletromagnética

## Onda de matéria
Toda matéria na natureza é simultaneamente partícula e onda. Ou seja, todas as partículas têm um comprimento de onda correspondente (*comprimento de onda de de Broglie*). O comprimento de onda $\lambda$ é uma função do momento $p$ e da constante de Planck $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Além disso, o momento $p$ é definido pela seguinte equação:

$$ p = mv \tag{6} $$

### Ignorando efeitos relativísticos (ex.: nêutron)
Como a energia cinética é $E=1/2 mv^2$, expressando a equação (6) em função da energia:

$$ p=\sqrt{2mE} \tag{7} $$

Substituindo na equação (5), o comprimento de onda da partícula é:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Na engenharia nuclear, aplicamos esta equação para calcular o comprimento de onda de de Broglie do nêutron. Substituindo a massa de repouso do nêutron:

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Onde $\lambda$ está em cm e $E$ é a energia cinética do nêutron em eV.

### Considerando efeitos relativísticos (ex.: elétron)
Calculamos o momento $p$ diretamente a partir das equações relativísticas anteriores:

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{repouso}}} \tag{10}$$

Então o comprimento de onda de de Broglie é:

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{repouso}}}} \tag{11} $$

### Partículas com massa de repouso zero (ex.: fóton)
Para partículas com massa de repouso zero, o momento não pode ser calculado pela equação (6), então usamos:

$$ p=\frac {E}{c} \tag{12} $$

Substituindo a equação (12) na equação (5):

$$ \lambda = \frac {hc}{E} \tag{13}$$

Substituindo os valores de $h$ e $c$, a equação final para o comprimento de onda é:

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

Onde $\lambda$ está em m e $E$ em eV.
