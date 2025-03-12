---
title: Leis do Movimento de Newton
description: Exploramos as Leis do Movimento de Newton, o significado das três leis, as definições de massa inercial e gravitacional, e examinamos o princípio da equivalência, que é importante não apenas na mecânica clássica, mas também na teoria da relatividade geral.
categories: [Physics, Classical Dynamics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Leis do Movimento de Newton**
> 1. Um objeto permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.
> 2. A taxa de variação temporal do momento de um objeto é igual à força aplicada sobre ele.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Quando dois objetos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Princípio da equivalência**
> - Massa inercial: A massa que determina a aceleração de um objeto quando uma força é aplicada
> - Massa gravitacional: A massa que determina a força gravitacional entre um objeto e outro
> - Atualmente, sabe-se que a massa inercial e a massa gravitacional são claramente idênticas dentro de uma margem de erro de cerca de $10^{-12}$
> - A afirmação de que a massa inercial e a massa gravitacional são exatamente iguais é chamada de **princípio da equivalência**
{: .prompt-info }

## Leis do Movimento de Newton
As Leis do Movimento de Newton são três leis publicadas por Isaac Newton em 1687 em sua obra Philosophiæ Naturalis Principia Mathematica (Princípios Matemáticos da Filosofia Natural, abreviado como 'Principia'), que formam a base da mecânica newtoniana.

1. Um objeto permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.
2. A taxa de variação temporal do momento de um objeto é igual à força aplicada sobre ele.
3. Quando dois objetos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.

### Primeira Lei de Newton
> I. Um objeto permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.

Um objeto neste estado, sem forças externas atuando sobre ele, é chamado de **corpo livre** ou **partícula livre**.
No entanto, a Primeira Lei sozinha fornece apenas um conceito qualitativo de força.

### Segunda Lei de Newton
> II. A taxa de variação temporal do momento de um objeto é igual à força aplicada sobre ele.

Newton definiu o **momento** como o produto da massa pela velocidade:

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

A partir disso, a Segunda Lei de Newton pode ser expressa como:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

A Primeira e a Segunda Lei de Newton, apesar de seus nomes, são na verdade mais próximas de uma 'definição' de força do que de 'leis'. Também podemos ver que a definição de força depende da definição de 'massa'.

### Terceira Lei de Newton
> III. Quando dois objetos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.

Esta lei também é conhecida como 'lei da ação e reação' e se aplica quando a força que um objeto exerce sobre outro está na direção da linha que une os dois pontos de ação. Tais forças são chamadas de **forças centrais** e a Terceira Lei se aplica independentemente de serem forças atrativas ou repulsivas. A gravidade ou força eletrostática entre dois objetos em repouso, e a força elástica são exemplos de tais forças centrais. Por outro lado, forças que dependem da velocidade dos objetos interagentes, como a força entre cargas em movimento ou a gravidade entre objetos em movimento, são forças não centrais e a Terceira Lei não se aplica a esses casos.

Considerando a definição de massa que vimos anteriormente, podemos reformular a Terceira Lei da seguinte maneira:

> III$^\prime$. Se dois objetos formam um sistema isolado ideal, as acelerações desses dois objetos têm direções opostas e a razão de suas magnitudes é igual à razão inversa das massas dos objetos.

Pela Terceira Lei de Newton:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Substituindo a Segunda Lei ($\ref{eqn:2nd_law}$) aqui:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Isso mostra que o momento é conservado na interação isolada entre duas partículas.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Além disso, na equação ($\ref{eqn:3rd-1_law}$), como $\vec{p}=m\vec{v}$ e a massa $m$ é constante:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Obtemos assim:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

No entanto, a Terceira Lei de Newton descreve o caso em que dois objetos formam um sistema isolado, mas na realidade é impossível realizar tais condições ideais, então a afirmação de Newton na Terceira Lei pode ser considerada bastante ousada. Apesar de ser uma conclusão obtida de observações limitadas, graças à profunda intuição física de Newton, a mecânica newtoniana manteve uma posição sólida por quase 300 anos sem erros detectados em várias verificações experimentais. Somente no século XX, quando medições precisas o suficiente para mostrar diferenças entre as previsões da teoria de Newton e a realidade se tornaram possíveis, a teoria da relatividade e a mecânica quântica nasceram.

## Massa Inercial e Massa Gravitacional
Uma maneira de determinar a massa de um objeto é usar um instrumento como uma balança para comparar o peso do objeto com um peso padrão. Este método utiliza o fato de que o peso de um objeto em um campo gravitacional é igual à magnitude da força gravitacional atuando sobre ele. Neste caso, a Segunda Lei $\vec{F}=m\vec{a}$ toma a forma $\vec{W}=m\vec{g}$. Este método baseia-se na suposição fundamental de que a massa $m$ definida em III$^\prime$ é a mesma que a massa $m$ que aparece na equação gravitacional. Essas duas massas são chamadas de **massa inercial** e **massa gravitacional**, respectivamente, e são definidas da seguinte forma:

- Massa inercial: A massa que determina a aceleração de um objeto quando uma força é aplicada
- Massa gravitacional: A massa que determina a força gravitacional entre um objeto e outro

Embora seja uma história inventada posteriormente e não relacionada a Galileo Galilei, o experimento de queda da Torre de Pisa é considerado o primeiro experimento mental a mostrar que a massa inercial e a massa gravitacional seriam iguais. Newton também tentou demonstrar que não havia diferença entre as duas massas medindo os períodos de pêndulos de mesmo comprimento com massas diferentes, mas seu método experimental e precisão eram rudimentares e ele falhou em fornecer uma prova precisa.

No final do século XIX, o físico húngaro Loránd Eötvös realizou o experimento de Eötvös para medir precisamente a diferença entre a massa inercial e a massa gravitacional, demonstrando que eram idênticas com uma precisão considerável (dentro de uma margem de erro de 1 em 20 milhões).

Experimentos mais recentes realizados por Robert Henry Dicke e outros aumentaram ainda mais a precisão, e atualmente sabe-se que a massa inercial e a massa gravitacional são claramente idênticas dentro de uma margem de erro de cerca de $10^{-12}$. Este resultado tem um significado extremamente importante na teoria geral da relatividade, e a afirmação de que a massa inercial e a massa gravitacional são exatamente iguais é chamada de **princípio da equivalência**.
