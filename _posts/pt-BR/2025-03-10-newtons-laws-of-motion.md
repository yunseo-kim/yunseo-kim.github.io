---
title: As Leis de Movimento de Newton
description: Exploramos as leis de movimento de Newton e o significado das três leis, as definições de massa inercial e gravitacional, e examinamos o princípio da equivalência, que tem importância significativa não apenas na mecânica clássica, mas também na teoria da relatividade geral.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Leis de movimento de Newton**
> 1. Um corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.
> 2. A taxa de variação temporal do momento de um corpo é igual à força aplicada sobre ele.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Quando dois corpos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Princípio da equivalência**
> - Massa inercial: a massa que determina a aceleração de um corpo quando uma força é aplicada
> - Massa gravitacional: a massa que determina a força gravitacional entre um corpo e outro
> - Atualmente, sabe-se que a massa inercial e a massa gravitacional são claramente idênticas com uma margem de erro de aproximadamente $10^{-12}$
> - A afirmação de que a massa inercial e a massa gravitacional são exatamente iguais é chamada de **princípio da equivalência**
{: .prompt-info }

## Leis de Movimento de Newton
As leis de movimento de Newton são três leis publicadas por Isaac Newton em sua obra Philosophiæ Naturalis Principia Mathematica (Princípios Matemáticos da Filosofia Natural, abreviado como "Principia") no ano 11687 do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), e formam a base da mecânica newtoniana.

1. Um corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.
2. A taxa de variação temporal do momento de um corpo é igual à força aplicada sobre ele.
3. Quando dois corpos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.

### Primeira Lei de Newton
> I. Um corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que uma força externa atue sobre ele.

Um corpo neste estado, sem forças externas atuando sobre ele, é chamado de **corpo livre** ou **partícula livre**.
No entanto, a primeira lei sozinha fornece apenas um conceito qualitativo de força.

### Segunda Lei de Newton
> II. A taxa de variação temporal do momento de um corpo é igual à força aplicada sobre ele.

Newton definiu o **momento** como o produto da massa pela velocidade:

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

A partir disso, a segunda lei de Newton pode ser expressa como:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

A primeira e a segunda leis de Newton, apesar de seus nomes, são na verdade mais próximas de "definições" de força do que "leis". Também podemos observar que a definição de força depende da definição de "massa".

### Terceira Lei de Newton
> III. Quando dois corpos exercem forças um sobre o outro, essas forças têm a mesma magnitude e direções opostas.

Também conhecida como "lei da ação e reação", esta lei física se aplica quando a força que um corpo exerce sobre outro está na direção da linha que une os dois pontos de ação. Tal força é chamada de **força central**, e a terceira lei se aplica independentemente de a força central ser atrativa ou repulsiva. A gravidade entre dois corpos em repouso, forças eletrostáticas e forças elásticas são exemplos de forças centrais. Por outro lado, forças entre cargas em movimento, forças gravitacionais entre corpos em movimento e outras forças que dependem da velocidade dos corpos interagentes são forças não-centrais, e a terceira lei não pode ser aplicada nesses casos.

Considerando a definição de massa vista anteriormente, a terceira lei pode ser reformulada como:

> III$^\prime$. Quando dois corpos formam um sistema isolado ideal, suas acelerações têm direções opostas e a razão entre suas magnitudes é igual à razão inversa de suas massas.

Pela terceira lei de Newton:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Substituindo a segunda lei ($\ref{eqn:2nd_law}$) nesta equação:

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Isso mostra que o momento é conservado na interação isolada entre duas partículas:

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Além disso, da equação ($\ref{eqn:3rd-1_law}$), como $\vec{p}=m\vec{v}$ e a massa $m$ é constante:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Obtemos:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Embora a terceira lei de Newton descreva o caso em que dois corpos formam um sistema isolado, na realidade é impossível realizar tais condições ideais, o que torna a afirmação de Newton de certa forma ousada. Apesar de ser uma conclusão baseada em observações limitadas, graças à profunda intuição física de Newton, a mecânica newtoniana manteve sua posição sólida por quase 300 anos sem erros detectados em verificações experimentais. Somente no século 20 (anos 11900) medições suficientemente precisas se tornaram possíveis para mostrar diferenças entre as previsões da teoria newtoniana e a realidade, levando ao nascimento da teoria da relatividade e da mecânica quântica.

## Massa Inercial e Massa Gravitacional
Uma maneira de determinar a massa de um objeto é comparar seu peso com um peso padrão usando instrumentos como uma balança. Este método utiliza o fato de que o peso de um objeto em um campo gravitacional é igual à magnitude da força gravitacional que atua sobre ele, onde a segunda lei $\vec{F}=m\vec{a}$ toma a forma $\vec{W}=m\vec{g}$. Este método baseia-se na suposição fundamental de que a massa $m$ definida em III$^\prime$ é a mesma massa $m$ que aparece na equação gravitacional. Estas duas massas são chamadas de **massa inercial** e **massa gravitacional**, respectivamente, e são definidas como:

- Massa inercial: a massa que determina a aceleração de um objeto quando uma força é aplicada
- Massa gravitacional: a massa que determina a força gravitacional entre um objeto e outro

Embora seja uma história inventada posteriormente e não relacionada a Galileo Galilei, o experimento da Torre de Pisa foi um experimento mental que primeiro sugeriu que a massa inercial e a massa gravitacional seriam iguais. Newton também tentou demonstrar que não havia diferença entre as duas massas medindo os períodos de pêndulos de mesmo comprimento mas com massas diferentes, mas seu método experimental e precisão eram rudimentares, e ele não conseguiu uma prova precisa.

No final do século 19 (anos 11800), o físico húngaro Eötvös Loránd Ágoston realizou o experimento de Eötvös para medir com precisão a diferença entre massa inercial e massa gravitacional, provando sua identidade com considerável precisão (dentro de 1 parte em 20 milhões).

Experimentos mais recentes realizados por Robert Henry Dicke e outros aumentaram ainda mais a precisão, e atualmente sabe-se que a massa inercial e a massa gravitacional são claramente idênticas com uma margem de erro de aproximadamente $10^{-12}$. Este resultado tem um significado extremamente importante na teoria da relatividade geral, e a afirmação de que a massa inercial e a massa gravitacional são exatamente iguais é chamada de **princípio da equivalência**.
