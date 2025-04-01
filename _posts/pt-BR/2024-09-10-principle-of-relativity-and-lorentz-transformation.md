---
title: Princípio da Relatividade e Transformação de Lorentz
description: Exploramos o conceito de sistemas de referência e a transformação de Galileu amplamente utilizada na mecânica clássica. Também examinamos brevemente as equações de Maxwell e o experimento de Michelson-Morley, que serviram como pano de fundo para o surgimento da transformação de Lorentz, e derivamos a matriz de transformação de Lorentz.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Princípio da Relatividade**: O princípio de que todas as leis físicas devem ser idênticas em diferentes sistemas de referência que se movem com velocidade constante entre si
{: .prompt-info }

> **Fator de Lorentz $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Transformação de Lorentz**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **Transformação de Lorentz Inversa**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## Sistema de Referência e Princípio da Relatividade
### Sistema de Referência (frame of reference)
- **Sistema de Referência (frame of reference)**: Quando dizemos que um objeto está em movimento, significa que sua posição muda relativamente a outros objetos. Como todo movimento é relativo, para descrever qualquer movimento, é necessário estabelecer um sistema de referência.
- **Sistema de Referência Inercial (inertial frames of reference)**: Um sistema onde a primeira lei de Newton ("O estado de movimento de um corpo permanece inalterado enquanto a força resultante sobre ele for zero") é válida. Qualquer sistema de referência que se move com velocidade constante em relação a um sistema inercial também é um sistema inercial.

### Princípio da Relatividade (Principle of Relativity)
Um dos principais conceitos e premissas fundamentais da física, o princípio da relatividade estabelece que todas as leis físicas devem ser idênticas em diferentes sistemas de referência que se movem com velocidade constante entre si. Se observadores em movimento relativo experimentassem leis físicas diferentes, essa diferença poderia ser usada para estabelecer um sistema de referência absoluto, permitindo determinar quem está parado e quem está em movimento. No entanto, de acordo com o princípio da relatividade, tal distinção não existe, portanto, não há sistema de referência absoluto ou movimento absoluto em relação ao universo, e todos os sistemas inerciais são equivalentes.

## Limitações da Transformação de Galileu
### Transformação de Galileu (Galilean transformation)
Consideremos dois sistemas inerciais $S$ e $S^{\prime}$, onde $S^{\prime}$ se move em relação a $S$ com uma velocidade constante $\vec{v}$ na direção $+x$. Um mesmo evento é observado no sistema $S$ nas coordenadas $(x, y, z)$ no tempo $t$, e no sistema $S^{\prime}$ nas coordenadas $(x^{\prime}, y^{\prime}, z^{\prime})$ no tempo $t^{\prime}$.

Nesse caso, o valor do movimento na direção $x$ medido em $S^{\prime}$ será maior que o valor medido em $S$ pela distância que $S^{\prime}$ percorreu em relação a $S$ na direção $x$, que é $\vec{v}t$, portanto:

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

E como não há movimento relativo nas direções $y$ e $z$:

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

Intuitivamente, podemos assumir que:

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Essas equações, de ($\ref{eqn:galilean_transform_x}$) a ($\ref{eqn:galilean_transform_t}$), representam a **transformação de Galileu (Galilean transformation)**, que é a transformação de coordenadas entre diferentes sistemas inerciais tradicionalmente usada na física clássica. É simples e intuitiva, e funciona bem na maioria das situações cotidianas. No entanto, como veremos adiante, ela contradiz as equações de Maxwell.

### Equações de Maxwell
No final do século 118, Maxwell expandiu as ideias e resultados de pesquisas anteriores propostas por outros cientistas como Faraday e Ampère, revelando que a eletricidade e o magnetismo são, na verdade, uma única força, e derivou as seguintes quatro equações que descrevem o campo eletromagnético:

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: O fluxo elétrico através de qualquer superfície fechada é igual à carga líquida interna (Lei de Gauss).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Não existem monopolos magnéticos (cargas magnéticas).}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: A variação do campo magnético cria um campo elétrico (Lei de Faraday).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: A variação do campo elétrico e a corrente criam um campo magnético (Lei de Ampère-Maxwell).}
\end{gather*}$$

As equações de Maxwell explicavam com sucesso todos os fenômenos elétricos e magnéticos conhecidos até então, previam a existência de ondas eletromagnéticas e também derivavam que a velocidade da luz no vácuo, $c$, é uma constante invariável, tornando-se assim as fórmulas fundamentais do eletromagnetismo.

### Contradição entre a Transformação de Galileu e as Equações de Maxwell
A mecânica newtoniana, que utiliza a transformação de Galileu, foi a base da física por mais de 200 anos, e as equações de Maxwell, como mencionado, são equações fundamentais que descrevem fenômenos elétricos e magnéticos. No entanto, existe uma contradição entre elas:

- De acordo com o princípio da relatividade, espera-se que as equações de Maxwell também mantenham a mesma forma em todos os sistemas inerciais, mas quando se aplicam as transformações de Galileu para converter medidas de um sistema inercial para outro, as equações de Maxwell assumem uma forma muito diferente.
- A partir das equações de Maxwell, pode-se calcular a velocidade da luz $c$, que é uma constante invariável, mas segundo a mecânica newtoniana e a transformação de Galileu, a velocidade da luz $c$ seria medida diferentemente em diferentes sistemas inerciais.

Portanto, as equações de Maxwell e a transformação de Galileu são incompatíveis, e pelo menos uma delas precisava ser modificada. Isso serviu como pano de fundo para o surgimento da **transformação de Lorentz (Lorentz transformation)**, que será discutida adiante.

## Teoria do Éter (aether) e o Experimento de Michelson-Morley
Enquanto isso, na física do século 118, acreditava-se que a luz, assim como outras ondas como as ondas na água ou o som, era transmitida por um meio hipotético chamado *éter (aether)*, e houve esforços para descobrir a existência desse éter.

De acordo com a teoria do éter, mesmo que o espaço fosse vácuo, estaria preenchido com éter, e devido à órbita da Terra, que se move a aproximadamente 30km/s em relação ao Sol, haveria um "vento de éter" atravessando a Terra.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Fonte da imagem*
> - Autor: Usuário da Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Para verificar essa hipótese, em 11887 do [calendário da era humana](https://en.wikipedia.org/wiki/Holocene_calendar), Michelson, em colaboração com Morley, realizou o *Experimento de Michelson-Morley (Michelson-Morley Experiment)* utilizando o interferômetro mostrado abaixo:  
![Interferômetro de Michelson-Morley](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Fonte da imagem*
> - Autor: Albert Abraham Michelson com Edward Morley
> - Licença: domínio público

Neste experimento, o raio de luz é dividido em dois ao passar por um semi-espelho, e cada parte percorre os dois braços perpendiculares do interferômetro, indo e voltando, percorrendo um total de aproximadamente 11m, e se encontrando no ponto central. Nesse momento, dependendo da diferença de fase entre os dois raios, ocorre interferência construtiva ou destrutiva. De acordo com a teoria do éter, a velocidade relativa ao éter causaria diferenças na velocidade da luz, o que alteraria essa diferença de fase e, consequentemente, o padrão de interferência. No entanto, na prática, não foi possível observar mudanças no padrão de interferência. Houve várias tentativas de explicar esse resultado experimental, entre as quais FitzGerald e Lorentz propuseram a *contração de Lorentz-FitzGerald (Lorentz–FitzGerald contraction)* ou *contração de comprimento (length contraction)*, sugerindo que um objeto se contrai em comprimento quando <u>se move relativamente ao éter</u>, o que levou à transformação de Lorentz.

> Lorentz acreditava na existência do éter naquela época e pensava que a contração de comprimento ocorria devido ao movimento relativo ao éter. Posteriormente, Einstein interpretou o verdadeiro significado físico da transformação de Lorentz com sua *Teoria da Relatividade Especial (Theory of Special Relativity)*, explicando a contração de comprimento em termos do conceito de espaço-tempo, não de éter, e também foi posteriormente descoberto que o éter não existe.
{: .prompt-info }

## Transformação de Lorentz (Lorentz transformation)
### Derivação da Transformação de Lorentz
Na mesma situação descrita anteriormente para a transformação de Galileu (equações [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]), vamos assumir que a relação de transformação correta entre $x$ e $x^{\prime}$ que não contradiz as equações de Maxwell é:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Aqui, $\gamma$ pode ser uma função de $\vec{v}$, mas não depende de $x$ e $t$. Podemos fazer essa suposição pelas seguintes razões:

- Para que haja uma correspondência um-para-um entre eventos em $S$ e $S^{\prime}$, $x$ e $x^{\prime}$ devem ter uma relação linear.
- Como sabemos que a transformação de Galileu é correta para a mecânica em situações cotidianas, deve ser possível aproximá-la pela equação ($\ref{eqn:galilean_transform_x}$).
- A forma deve ser o mais simples possível.

Como as fórmulas físicas devem ter a mesma forma nos sistemas de referência $S$ e $S^{\prime}$, para expressar $x$ em termos de $x^{\prime}$ e $t$, basta mudar o sinal de $\vec{v}$ (a direção do movimento relativo), e como não deve haver diferença entre os dois sistemas de referência além do sinal de $\vec{v}$, $\gamma$ deve ser o mesmo:

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Assim como na transformação de Galileu, não há razão para que as componentes perpendiculares à direção de $\vec{v}$, ou seja, $y$ e $y^{\prime}$, e $z$ e $z^{\prime}$, sejam diferentes, então:

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Agora, substituindo a equação ($\ref{eqn:lorentz_transform_x}$) em ($\ref{eqn:lorentz_transform_x_inverse}$):

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Reorganizando para $t^{\prime}$:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Além disso, para não contradizer as equações de Maxwell, a velocidade da luz deve ser a mesma, $c$, em ambos os sistemas de referência, o que nos permite determinar $\gamma$. Se no tempo $t=0$ as origens dos dois sistemas estavam no mesmo lugar, então por essa condição inicial, $t^\prime = 0$. Agora, consideremos que em $t=t^\prime=0$ houve um flash de luz na origem comum de $S$ e $S^\prime$, e cada observador nos respectivos sistemas mede a velocidade dessa luz. Nesse caso, no sistema $S$:

$$ x = ct \label{eqn:ct_S}\tag{9}$$

E no sistema $S^\prime$:

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Substituindo $x$ e $t$ nas equações acima usando ($\ref{eqn:lorentz_transform_x}$) e ($\ref{eqn:lorentz_transform_t}$):

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Resolvendo para $x$:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Mas, da equação ($\ref{eqn:ct_S}$), sabemos que $x=ct$, portanto:

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

E assim:

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Substituindo esta expressão de $\gamma$ em função de $\vec{v}$ nas equações ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$) e ($\ref{eqn:lorentz_transform_t}$), obtemos as equações finais de transformação do sistema $S$ para o sistema $S^\prime$.

### Matriz de Transformação de Lorentz

As equações de transformação finais que obtivemos são:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

Estas são as **transformações de Lorentz (Lorentz transformation)**. Definindo $\vec{\beta}=\vec{v}/c$, podemos expressá-las na forma matricial:

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

Lorentz mostrou que, usando essas transformações, as fórmulas fundamentais do eletromagnetismo mantêm a mesma forma em todos os sistemas de referência inerciais. Além disso, podemos verificar que quando a velocidade $v$ é muito menor que a velocidade da luz $c$, $\gamma \to 1$, e as transformações de Lorentz se aproximam das transformações de Galileu.

### Transformação de Lorentz Inversa (inverse Lorentz transformation)
Às vezes, é mais conveniente transformar medidas do sistema em movimento $S^\prime$ para o sistema em repouso $S$, em vez do contrário. Nesses casos, podemos usar a **transformação de Lorentz inversa (inverse Lorentz transformation)**.  
Calculando a matriz inversa de ($\ref{lorentz_transform_matrix}$), obtemos a seguinte matriz de transformação de Lorentz inversa:

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

Isso é equivalente a trocar as quantidades físicas com e sem prime nas equações ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) e substituir $v$ por $-v$ (ou seja, $\beta$ por $-\beta$):

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
