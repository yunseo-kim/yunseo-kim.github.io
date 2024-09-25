---
title: "Princípio da Relatividade e Transformação de Lorentz"
description: >-
  Exploramos o conceito de sistemas de referência e a transformação de Galileu amplamente utilizada na mecânica clássica. Também examinamos brevemente as equações de Maxwell e o experimento de Michelson-Morley, que serviram de base para o surgimento da transformação de Lorentz, e derivamos a matriz de transformação de Lorentz.
categories: [Engineering Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
---

## TL;DR
> **Princípio da relatividade**: Princípio de que todas as leis físicas devem ser as mesmas para diferentes referenciais que se movem com velocidade constante entre si
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

> **Transformação de Lorentz inversa**
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

## Sistemas de Referência e Princípio da Relatividade
### Sistema de Referência (frame of reference)
- **Sistema de Referência (frame of reference)**: O movimento de um objeto significa que sua posição muda em relação a outros objetos. Como todo movimento é relativo, para descrever qualquer movimento, é necessário estabelecer um sistema de referência como base.
- **Sistema de Referência Inercial (inertial frames of reference)**: Um sistema onde a Primeira Lei de Newton ("O estado de movimento de um objeto permanece inalterado enquanto a força resultante agindo sobre ele for zero") é válida. Qualquer sistema de referência que se move com velocidade constante em relação a um sistema inercial também é um sistema de referência inercial.

### Princípio da Relatividade (Principle of Relativity)
Um dos principais conceitos e premissas fundamentais da física, afirma que todas as leis físicas devem ser as mesmas em diferentes sistemas de referência que se movem com velocidade constante entre si. Se observadores em movimento relativo experimentassem leis físicas diferentes, essa diferença poderia ser usada para estabelecer um sistema de referência absoluto, permitindo determinar quem está parado e quem está em movimento. No entanto, de acordo com o princípio da relatividade, tal distinção não existe, portanto, não há sistema de referência absoluto ou movimento absoluto em relação ao universo inteiro, e todos os sistemas de referência inerciais são equivalentes.

## Limitações da Transformação de Galileu
### Transformação de Galileu (Galilean transformation)
Consideremos dois sistemas inerciais $S$ e $S^{\prime}$, onde $S^{\prime}$ se move em relação a $S$ com uma velocidade constante $\vec{v}$ na direção $+x$. Um mesmo evento é observado no sistema $S$ no tempo $t$ nas coordenadas $(x, y, z)$, e no sistema $S^{\prime}$ no tempo $t^{\prime}$ nas coordenadas $(x^{\prime}, y^{\prime}, z^{\prime})$.

Neste caso, o valor do movimento na direção $x$ medido em $S^{\prime}$ será maior que o valor medido em $S$ pela distância que $S^{\prime}$ se moveu em relação a $S$ na direção $x$, que é $\vec{v}t$, então:

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

Como não há movimento relativo nas direções $y$ e $z$:

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

E intuitivamente, podemos assumir que:

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

As equações ($\ref{eqn:galilean_transform_x}$) a ($\ref{eqn:galilean_transform_t}$) são conhecidas como **Transformação de Galileu (Galilean transformation)**, que era classicamente usada na física para transformações de coordenadas entre diferentes sistemas inerciais. É simples e intuitiva, e funciona bem na maioria das situações cotidianas. No entanto, como veremos, ela entra em contradição com as equações de Maxwell.

### Equações de Maxwell
No final do século XIX, Maxwell expandiu as ideias e resultados de pesquisas anteriores propostos por outros cientistas como Faraday e Ampère, revelando que a eletricidade e o magnetismo são, na verdade, uma única força, e derivou as seguintes quatro equações que descrevem o campo eletromagnético:

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: O fluxo elétrico através de qualquer superfície fechada é igual à carga líquida interna (Lei de Gauss).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Não existem monopolos magnéticos.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: A variação do campo magnético cria um campo elétrico (Lei de Faraday).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: A variação do campo elétrico e a corrente criam um campo magnético (Lei de Ampère-Maxwell).}
\end{gather*}$$

As equações de Maxwell explicavam com sucesso todos os fenômenos elétricos e magnéticos conhecidos até então, previam a existência de ondas eletromagnéticas e também derivavam que a velocidade $c$ das ondas eletromagnéticas no vácuo era uma constante invariável, tornando-se assim a fórmula central do eletromagnetismo.

### Contradição entre a Transformação de Galileu e as Equações de Maxwell
A mecânica newtoniana, que utiliza a transformação de Galileu, foi a base da física por mais de 200 anos, e as equações de Maxwell, como mencionado, são as equações fundamentais que descrevem os fenômenos elétricos e magnéticos. No entanto, existe uma contradição entre as duas:

- De acordo com o princípio da relatividade, espera-se que as equações de Maxwell também tenham a mesma forma em todos os sistemas inerciais, mas ao aplicar a transformação de Galileu para converter valores medidos em um sistema inercial para valores medidos em outro sistema inercial, as equações de Maxwell assumem uma forma muito diferente.
- A velocidade da luz $c$ pode ser calculada a partir das equações de Maxwell e é uma constante invariável, mas de acordo com a mecânica newtoniana e a transformação de Galileu, a velocidade da luz $c$ é medida diferentemente em diferentes sistemas inerciais.

Portanto, as equações de Maxwell e a transformação de Galileu são incompatíveis, e pelo menos uma delas precisava ser modificada. Isso serviu de base para o surgimento da **Transformação de Lorentz (Lorentz transformation)**, que será discutida mais adiante.

## Teoria do Éter (aether) e o Experimento de Michelson-Morley
Por outro lado, na física do século XIX, acreditava-se que a luz, assim como outras ondas como ondas na água ou ondas sonoras, era transmitida por um meio hipotético chamado *éter (aether)*, e houve esforços para descobrir a existência deste éter.

De acordo com a teoria do éter, mesmo que o espaço cósmico fosse vácuo, estaria preenchido com éter, e devido à órbita da Terra, que se move a uma velocidade de cerca de 30km/s em relação ao Sol, acreditava-se que haveria um vento de éter atravessando a Terra.  
![Vento de Éter](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Para verificar esta hipótese, em 1887, Michelson, em colaboração com Morley, realizou o *Experimento de Michelson-Morley (Michelson-Morley Experiment)* utilizando o interferômetro mostrado abaixo.  
![Interferômetro de Michelson-Morley](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Fonte da imagem*
> - Autor: Albert Abraham Michelson com Edward Morley
> - Licença: domínio público

Neste experimento, o raio de luz é dividido em dois ao passar por um espelho semi-refletor, cada parte percorre ida e volta os dois braços perpendiculares do interferômetro, percorrendo um total de cerca de 11m, e se encontram no ponto médio, onde padrões de interferência construtiva ou destrutiva aparecem dependendo da diferença de fase entre os dois raios. De acordo com a teoria do éter, esperava-se que a velocidade relativa ao éter causasse uma diferença na velocidade da luz, resultando em uma mudança nesta diferença de fase e, consequentemente, uma mudança observável no padrão de interferência. No entanto, na realidade, nenhuma mudança no padrão de interferência foi observada. Houve várias tentativas de explicar este resultado experimental, entre as quais FitzGerald e Lorentz propuseram a *contração de Lorentz-FitzGerald (Lorentz–FitzGerald contraction)* ou *contração do comprimento (length contraction)*, que afirma que um objeto se contrai em comprimento quando <u>se move relativamente ao éter</u>, o que levou à transformação de Lorentz.

> Naquela época, Lorentz acreditava na existência do éter e pensava que a contração do comprimento ocorria devido ao movimento relativo ao éter. Posteriormente, Einstein interpretou o verdadeiro significado físico da transformação de Lorentz com sua *Teoria da Relatividade Especial (Theory of Special Relativity)*, explicando a contração do comprimento em termos do conceito de espaço-tempo em vez do éter, e também foi posteriormente descoberto que o éter não existe.
{: .prompt-info }

## Transformação de Lorentz (Lorentz transformation)
### Derivação da Transformação de Lorentz
Na mesma situação da transformação de Galileu (equações [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]) vista anteriormente, vamos assumir que a relação de transformação correta entre $x$ e $x^{\prime}$ que não contradiz as equações de Maxwell é a seguinte:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Aqui, $\gamma$ é independente de $x$ e $t$, mas pode ser uma função de $\vec{v}$. Podemos fazer esta suposição pelas seguintes razões:

- Para que haja uma correspondência um-a-um entre eventos em $S$ e $S^{\prime}$, $x$ e $x^{\prime}$ devem ter uma relação linear.
- Sabe-se que a transformação de Galileu está correta para a mecânica em situações cotidianas, então deve ser possível aproximá-la pela equação ($\ref{eqn:galilean_transform_x}$).
- Deve ser o mais simples possível.

Como as fórmulas físicas devem ter a mesma forma nos sistemas de referência $S$ e $S^{\prime}$, para expressar $x$ em termos de $x^{\prime}$ e $t$, basta mudar o sinal de $\vec{v}$ (a direção do movimento relativo), e como não deve haver diferença entre os dois sistemas de referência além do sinal de $\vec{v}$, $\gamma$ deve ser o mesmo.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Assim como na transformação de Galileu, não há razão para que as componentes perpendiculares à direção de $\vec{v}$, $y$ e $y^{\prime}$, e $z$ e $z^{\prime}$, sejam diferentes, então:

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Agora, substituindo a equação ($\ref{eqn:lorentz_transform_x}$) em ($\ref{eqn:lorentz_transform_x_inverse}$):

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Resolvendo para $t^{\prime}$:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Além disso, para não contradizer as equações de Maxwell, a velocidade da luz deve ser $c$ em ambos os sistemas de referência, o que pode ser usado para determinar $\gamma$. Se assumirmos que as origens dos dois sistemas de referência estavam no mesmo lugar quando $t=0$, então por esta condição inicial, $t^\prime = 0$. Agora, imagine que houve um flash de luz na origem comum de $S$ e $S^\prime$ quando $t=t^\prime=0$, e os observadores em cada sistema de referência estão medindo a velocidade desta luz. Neste caso, no sistema de referência $S$:

$$ x = ct \label{eqn:ct_S}\tag{9}$$

e no sistema de referência $S^\prime$:

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Substituindo $x$ e $t$ nas equações acima usando ($\ref{eqn:lorentz_transform_x}$) e ($\ref{eqn:lorentz_transform_t}$):

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Resolvendo esta equação para $x$:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Mas como vimos na equação ($\ref{eqn:ct_S}$), $x=ct$, então:

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Portanto,

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Substituindo esta expressão de $\gamma$ em função de $\vec{v}$ nas equações ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$), obtemos as equações finais de transformação do sistema de referência $S$ para $S^\prime$.

### Matriz de Transformação de Lorentz

As equações de transformação finais que obtivemos são as seguintes:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \tag{12}$$
- $$ y^\prime = y \tag{13}$$
- $$ z^\prime = z \tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \tag{15}$$

Estas equações são conhecidas como **Transformação de Lorentz (Lorentz transformation)**. Definindo $\vec{\beta}=\vec{v}/c$, podemos expressá-las na forma matricial da seguinte maneira:

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
\end{pmatrix}. \tag{16}$$

Lorentz mostrou que, usando estas equações de transformação, as fórmulas fundamentais do eletromagnetismo têm a mesma forma em todos os sistemas de referência inerciais. Além disso, podemos ver que quando a velocidade $v$ é muito menor que a velocidade da luz $c$, $\gamma \to 1$, então a transformação de Lorentz pode ser aproximada pela transformação de Galileu.

Generalizando para o caso em que a velocidade relativa de $S^\prime$ em relação ao sistema de referência inercial $S$ é $\vec{v}=v_x\hat{i}+v_y\hat{j}+v_z\hat{k}$, $\vec{\beta}=\vec{v}/c$, e os vetores de posição medidos nos dois sistemas de referência são $\vec{x}=x_1\hat{i}+x_2\hat{j}+x_3\hat{k}$ e $\vec{x^\prime}=x_1^\prime\hat{i}+x_2^\prime\hat{j}+x_3^\prime\hat{k}$ respectivamente, a transformação de Lorentz pode ser escrita como:

- $$ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct \label{eqn:lorentz_transform_x_vector}\tag{17}$$
- $$ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} \label{eqn:lorentz_transform_ct}\tag{18}$$

Ou

$$ \begin{pmatrix}
\vec{x}^\prime \\ ct^\prime
\end{pmatrix}
= \begin{pmatrix}
\gamma & -\gamma\vec{\beta} \\
-\gamma\vec{\beta} & \gamma
\end{pmatrix}
\begin{pmatrix}
\vec{x} \\ ct
\end{pmatrix}. \tag{19}\label{lorentz_transform_matrix}
$$

### Transformação de Lorentz Inversa (inverse Lorentz transformation)
Às vezes, pode ser mais conveniente transformar medições do sistema em movimento $S^\prime$ para medições no sistema em repouso $S$, em vez de transformar medições do sistema em repouso $S$ para o sistema em movimento $S^\prime$.
Nestes casos, podemos usar a **Transformação de Lorentz Inversa (inverse Lorentz transformation)**.  
Calculando a matriz inversa de ($\ref{lorentz_transform_matrix}$), obtemos a seguinte matriz de transformação de Lorentz inversa:

$$ \begin{pmatrix}
\vec{x} \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & \gamma\vec{\beta} \\
\gamma\vec{\beta} & \gamma
\end{pmatrix}
\begin{pmatrix}
\vec{x^\prime} \\ ct^\prime
\end{pmatrix}. \tag{20}
$$

Isso é equivalente a trocar as quantidades físicas com e sem linha nas equações ($\ref{eqn:lorentz_transform_x_vector}$)-($\ref{eqn:lorentz_transform_ct}$) e substituir $v$ por $-v$ (ou seja, $\beta$ por $-\beta$).

- $$ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime \tag{21}$$
- $$ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} \tag{22}$$