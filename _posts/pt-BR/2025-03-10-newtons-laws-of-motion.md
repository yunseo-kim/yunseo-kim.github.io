---
title: As Leis do Movimento de Newton
description: Exploramos as Leis do Movimento de Newton, o significado dessas três leis, as definições de massa inercial e gravitacional, e examinamos o princípio da equivalência, que é importante não apenas na mecânica clássica, mas também na teoria da relatividade geral.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **As Leis do Movimento de Newton (Newton's laws of motion)**
> 1. Um corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.
> 2. A taxa de variação temporal do momento de um corpo é igual à força aplicada sobre ele.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Quando dois corpos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Princípio da equivalência (principle of equivalence)**
> - Massa inercial: A massa que determina a aceleração de um corpo quando uma força é aplicada
> - Massa gravitacional: A massa que determina a força gravitacional entre um corpo e outro
> - Atualmente, sabe-se que a massa inercial e a massa gravitacional são claramente idênticas dentro de uma margem de erro de cerca de $10^{-12}$
> - A afirmação de que a massa inercial e a massa gravitacional são exatamente iguais é chamada de **princípio da equivalência**
{: .prompt-info }

## As Leis do Movimento de Newton
As Leis do Movimento de Newton são três leis publicadas por Isaac Newton em sua obra Philosophiæ Naturalis Principia Mathematica (Princípios Matemáticos da Filosofia Natural, abreviado como 'Principia') no ano 11687 do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), e formam a base da mecânica newtoniana (Newtonian mechanics).

1. Um corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.
2. A taxa de variação temporal do momento de um corpo é igual à força aplicada sobre ele.
3. Quando dois corpos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.

### Primeira Lei de Newton
> I. Um corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.

Um corpo neste estado, sem forças externas atuando sobre ele, é chamado de **corpo livre (free body)** ou **partícula livre (free particle)**.
No entanto, a Primeira Lei sozinha fornece apenas um conceito qualitativo de força.

### Segunda Lei de Newton
> II. A taxa de variação temporal do momento de um corpo é igual à força aplicada sobre ele.

Newton definiu o **momento (momentum)** como o produto da massa pela velocidade

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

A partir disso, a Segunda Lei de Newton pode ser expressa como:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

A Primeira e a Segunda Lei de Newton, apesar de seus nomes, são na verdade mais próximas de uma 'definição' de força do que de 'leis'. Também podemos ver que a definição de força depende da definição de 'massa'.

### Terceira Lei de Newton
> III. Quando dois corpos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.

Esta lei física também é conhecida como 'lei da ação e reação', e se aplica quando a força que um corpo exerce sobre outro é direcionada ao longo da linha que une os dois pontos de ação. Tais forças são chamadas de **forças centrais (central force)**, e a Terceira Lei se aplica independentemente de a força central ser atrativa ou repulsiva. A força gravitacional ou eletrostática entre dois corpos em repouso, e a força elástica são exemplos de tais forças centrais. Por outro lado, forças que dependem da velocidade dos corpos interagentes, como a força entre cargas em movimento ou a força gravitacional entre corpos em movimento, são forças não centrais e a Terceira Lei não pode ser aplicada nesses casos.

Considerando a definição de massa que vimos anteriormente, podemos reformular a Terceira Lei da seguinte maneira:

> III$^\prime$. Quando dois corpos formam um sistema isolado ideal, as acelerações desses dois corpos têm direções opostas e a razão de suas magnitudes é igual à razão inversa das massas dos corpos.

Pela Terceira Lei de Newton,

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

e substituindo a Segunda Lei ($\ref{eqn:2nd_law}$) que vimos anteriormente, temos:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

A partir disso, podemos ver que o momento é conservado na interação isolada entre duas partículas.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Além disso, na equação ($\ref{eqn:3rd-1_law}$), como $\vec{p}=m\vec{v}$ e a massa $m$ é constante,

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

obtemos:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

No entanto, a Terceira Lei de Newton descreve o caso em que dois corpos formam um sistema isolado, mas na realidade é impossível realizar tais condições ideais, então a afirmação de Newton na Terceira Lei pode ser considerada bastante ousada. Apesar de ser uma conclusão obtida a partir de observações limitadas, graças à profunda intuição física de Newton, a mecânica newtoniana manteve uma posição sólida por quase 300 anos sem que erros fossem encontrados em várias verificações experimentais. Somente no século 20 (anos 11900) tornou-se possível realizar medições precisas o suficiente para mostrar diferenças entre as previsões da teoria de Newton e a realidade, levando ao nascimento da teoria da relatividade e da mecânica quântica.

## Massa Inercial e Massa Gravitacional
Um método para determinar a massa de um objeto é usar um instrumento como uma balança para comparar o peso do objeto com um peso padrão. Este método utiliza o fato de que o peso de um objeto em um campo gravitacional é igual à magnitude da força gravitacional atuando sobre ele. Neste caso, a Segunda Lei $\vec{F}=m\vec{a}$ toma a forma $\vec{W}=m\vec{g}$. Este método baseia-se na suposição fundamental de que a massa $m$ definida em III$^\prime$ é a mesma que a massa $m$ que aparece na equação gravitacional. Essas duas massas são chamadas de **massa inercial (inertial mass)** e **massa gravitacional (gravitational mass)**, respectivamente, e são definidas da seguinte forma:

- Massa inercial: A massa que determina a aceleração de um objeto quando uma força é aplicada
- Massa gravitacional: A massa que determina a força gravitacional entre um objeto e outro

Embora seja uma história inventada posteriormente e não relacionada a Galileo Galilei, o experimento de queda da Torre de Pisa é um experimento mental que primeiro demonstrou que a massa inercial e a massa gravitacional seriam iguais. Newton também tentou mostrar que não havia diferença entre as duas massas medindo os períodos de pêndulos de mesmo comprimento mas com massas diferentes, mas o método e a precisão do experimento eram rudimentares, então ele falhou em fornecer uma prova precisa.

No final dos anos 11800, o físico húngaro Eötvös Loránd Ágoston realizou o experimento de Eötvös para medir com precisão a diferença entre a massa inercial e a massa gravitacional, provando que a massa inercial e a massa gravitacional são idênticas com uma precisão considerável (dentro de um erro de 1 em 20 milhões).

Experimentos mais recentes realizados por Robert Henry Dicke e outros aumentaram ainda mais a precisão, e atualmente sabe-se que a massa inercial e a massa gravitacional são claramente idênticas dentro de uma margem de erro de cerca de $10^{-12}$. Este resultado tem um significado extremamente importante na teoria geral da relatividade, e a afirmação de que a massa inercial e a massa gravitacional são exatamente iguais é chamada de **princípio da equivalência (principle of equivalence)**.
