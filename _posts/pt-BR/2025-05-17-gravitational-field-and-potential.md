---
title: Campo Gravitacional e Potencial Gravitacional
description: Exploramos as definições do vetor de campo gravitacional e do potencial gravitacional de acordo com a lei da gravitação universal de Newton, abordando dois exemplos importantes relacionados: o teorema da casca esférica e as curvas de rotação galáctica.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Lei da gravitação universal de Newton: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Para distribuições contínuas de massa e objetos com tamanho: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: densidade de massa em um ponto localizado pelo vetor posição $\mathbf{r^{\prime}}$ a partir de uma origem arbitrária
>   - $dv^{\prime}$: elemento de volume em um ponto localizado pelo vetor posição $\mathbf{r^{\prime}}$ a partir de uma origem arbitrária
> - **Vetor de campo gravitacional (gravitational field vector)**:
>   - Vetor que representa a força por unidade de massa que uma partícula experimenta em um campo criado por um objeto de massa $M$
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - Tem dimensão de *força por unidade de massa* ou *aceleração*
> - **Potencial gravitacional (gravitational potential)**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - Tem dimensão de *força por unidade de massa* $\times$ *distância* ou *energia por unidade de massa*
>   - $\Phi = -G\cfrac{M}{r}$
>   - Apenas a diferença relativa do potencial gravitacional tem significado, não o valor específico em si
>   - Geralmente, a ambiguidade é removida estabelecendo arbitrariamente a condição de que $\Phi \to 0$ quando $r \to \infty$
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Potencial gravitacional dentro e fora de uma casca esférica (teorema da casca)**
>   - Para $R>a$:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - Ao calcular o potencial gravitacional em um ponto externo devido a uma distribuição esfericamente simétrica de matéria, podemos considerar o objeto como uma massa pontual
>   - Para $R<b$:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - Dentro de uma casca de massa esfericamente simétrica, o potencial gravitacional é constante independentemente da posição, e a gravidade atuante é $0$
>   - Para $b<R<a$: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## Campo Gravitacional
### Lei da Gravitação Universal de Newton
Newton já havia sistematizado e verificado numericamente a lei da gravitação universal antes de 11666 HE. No entanto, levou mais 20 anos até publicar seus resultados em seu livro *Principia* em 11687 HE, porque não conseguia justificar o método de cálculo que assumia a Terra e a Lua como massas pontuais sem tamanho. Felizmente, usando o cálculo que o próprio Newton inventou posteriormente, podemos provar esse problema [muito mais facilmente do que Newton na época](#para-ra).

De acordo com a lei da gravitação universal de Newton, *cada partícula de massa atrai todas as outras partículas no universo com uma força proporcional ao produto das duas massas e inversamente proporcional ao quadrado da distância entre elas*. Matematicamente, isso é expresso como:

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - Licença: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

O vetor unitário $\mathbf{e}_r$ aponta de $M$ para $m$, e o sinal negativo indica que a força é atrativa. Ou seja, $m$ é atraído em direção a $M$.

### Experimento de Cavendish
A verificação experimental desta lei e a determinação do valor de $G$ foram realizadas em 11798 HE pelo físico britânico Henry Cavendish. O experimento de Cavendish utiliza uma balança de torção composta por duas pequenas esferas fixadas nas extremidades de uma haste leve. Essas duas esferas são atraídas por outras duas esferas maiores posicionadas próximas a elas. O valor oficial de $G$ obtido até agora é $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> Apesar de $G$ ser uma das constantes fundamentais conhecidas há mais tempo, ela é conhecida com menor precisão do que a maioria das outras constantes fundamentais como $e$, $c$ e $\hbar$. Ainda hoje, muitas pesquisas estão sendo realizadas para determinar o valor de $G$ com maior precisão.
{: .prompt-tip }

### Para objetos com tamanho
A lei na equação ($\ref{eqn:law_of_gravitation}$) só pode ser aplicada rigorosamente a *partículas pontuais*. Se um ou ambos os objetos tiverem tamanho, é necessário fazer a suposição adicional de que o campo gravitacional é um *campo linear* para calcular a força. Isso significa que a força gravitacional total exercida sobre uma partícula de massa $m$ por várias outras partículas pode ser obtida somando vetorialmente cada força individual. Para objetos com distribuição contínua de matéria, a soma é substituída por uma integral:

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: densidade de massa em um ponto localizado pelo vetor posição $\mathbf{r^{\prime}}$ a partir de uma origem arbitrária
- $dv^{\prime}$: elemento de volume em um ponto localizado pelo vetor posição $\mathbf{r^{\prime}}$ a partir de uma origem arbitrária

Se tanto o objeto de massa $M$ quanto o objeto de massa $m$ tiverem tamanho, uma segunda integral de volume para $m$ também será necessária para calcular a força gravitacional total.

### Vetor de Campo Gravitacional
O **vetor de campo gravitacional (gravitational field vector)** $\mathbf{g}$ é definido como o vetor que representa a força por unidade de massa que uma partícula experimenta em um campo criado por um objeto de massa $M$:

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

ou

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

onde a direção de $\mathbf{e}_r$ varia de acordo com $\mathbf{r^\prime}$.

Esta quantidade $\mathbf{g}$ tem dimensão de *força por unidade de massa* ou *aceleração*. A magnitude do vetor de campo gravitacional $\mathbf{g}$ próximo à superfície da Terra é igual à constante de aceleração gravitacional, com $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$.

## Potencial Gravitacional
### Definição
O vetor de campo gravitacional $\mathbf{g}$ varia com $1/r^2$, satisfazendo assim a condição ($\nabla \times \mathbf{g} \equiv 0$) para ser expresso como o gradiente de uma função escalar (potencial). Portanto, podemos escrever:

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

onde $\Phi$ é chamado de **potencial gravitacional**, com dimensão de *força por unidade de massa* $\times$ *distância* ou *energia por unidade de massa*.

Como $\mathbf{g}$ depende apenas do raio, $\Phi$ também varia apenas com $r$. Das equações ($\ref{eqn:g_vector}$) e ($\ref{eqn:gradient_phi}$), temos:

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

Integrando, obtemos:

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

A constante de integração pode ser omitida porque apenas a diferença relativa do potencial gravitacional tem significado, não o valor específico em si. Geralmente, a ambiguidade é removida estabelecendo arbitrariamente a condição de que $\Phi \to 0$ quando $r \to \infty$, e a equação ($\ref{eqn:g_potential}$) satisfaz essa condição.

Para uma distribuição contínua de matéria, o potencial gravitacional é:

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Para uma massa distribuída em uma casca fina, temos:

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

E para uma fonte de massa linear com densidade linear $\rho_l$:

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Significado Físico
Consideremos o trabalho por unidade de massa $dW^\prime$ realizado quando um objeto se move uma distância $d\mathbf{r}$ em um campo gravitacional:

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

Nesta equação, $\Phi$ é uma função apenas das coordenadas de posição, expressa como $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Portanto, o trabalho por unidade de massa realizado ao mover um objeto de um ponto a outro em um campo gravitacional é igual à diferença de potencial entre esses dois pontos.

Se definirmos o potencial gravitacional como zero no infinito, então $\Phi$ em qualquer ponto pode ser interpretado como o trabalho por unidade de massa necessário para mover o objeto desse ponto até o infinito. A energia potencial de um objeto é igual ao produto de sua massa pelo potencial gravitacional $\Phi$, então se $U$ for a energia potencial:

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

Portanto, a força gravitacional exercida sobre um objeto é obtida tomando-se o gradiente negativo de sua energia potencial:

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Quando um objeto está em um campo gravitacional criado por uma massa, sempre existe uma energia potencial associada. Embora esta energia potencial esteja rigorosamente no próprio campo, convencionalmente é referida como a energia potencial do objeto.

## Exemplo: Potencial Gravitacional Dentro e Fora de uma Casca Esférica (Teorema da Casca)
### Configuração de Coordenadas e Expressão do Potencial Gravitacional como Integral
Vamos calcular o potencial gravitacional dentro e fora de uma casca esférica uniforme com raio interno $b$ e raio externo $a$. A gravidade devido à casca esférica pode ser obtida calculando diretamente os componentes da força que atuam sobre uma unidade de massa no campo, mas o método do potencial é mais simples.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Vamos calcular o potencial no ponto $P$ a uma distância $R$ do centro. Assumindo uma distribuição de massa uniforme na casca, temos $\rho(r^\prime)=\rho$, e devido à simetria em relação ao ângulo azimutal $\phi$ ao longo da linha que conecta o centro da esfera e o ponto $P$:

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

Pela lei dos cossenos:

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

Como $R$ é constante, diferenciando esta equação em relação a $r^\prime$:

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

Substituindo na equação ($\ref{eqn:spherical_shell_1}$):

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

onde $r_\mathrm{max}$ e $r_\mathrm{min}$ são determinados pela posição do ponto $P$.

### Para $R>a$
$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

A massa $M$ da casca esférica é dada por:

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

Portanto, o potencial é:

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> Comparando o resultado que acabamos de obter ($\ref{eqn:spherical_shell_outside_2}$) com a equação do potencial gravitacional devido a uma massa pontual $M$ ($\ref{eqn:g_potential}$), vemos que são idênticos. Isso significa que ao calcular o potencial gravitacional em um ponto externo devido a uma distribuição esfericamente simétrica de matéria, podemos considerar toda a massa concentrada no centro. A maioria dos corpos celestes esféricos, como a Terra e a Lua, se enquadram nessa categoria, pois podem ser considerados como inúmeras cascas esféricas concêntricas, como uma [matryoshka](https://en.wikipedia.org/wiki/Matryoshka_doll). Isso fornece a [justificativa para considerar corpos celestes como a Terra e a Lua como massas pontuais sem tamanho para cálculos](#lei-da-gravitação-universal-de-newton), como mencionado no início deste artigo.
{: .prompt-info }

### Para $R<b$
$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> Dentro de uma casca de massa esfericamente simétrica, o potencial gravitacional é constante independentemente da posição, e a gravidade atuante é $0$.
{: .prompt-info }

> Isso também é uma das principais evidências de que a "Teoria da Terra Oca", uma pseudociência notória, é absurda. Se a Terra fosse uma casca esférica com interior vazio, como afirma essa teoria, não haveria gravidade atuando sobre qualquer objeto dentro dessa cavidade. Considerando a massa e o volume da Terra, não só é impossível que exista tal cavidade, mas mesmo que existisse, os seres vivos lá dentro não estariam andando na superfície interna da casca, mas flutuando em estado de gravidade zero, como em uma estação espacial.  
> [Pode haver micróbios vivendo a alguns quilômetros de profundidade nas camadas subterrâneas](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), mas certamente não da forma como a Teoria da Terra Oca sugere. Eu também adoro o romance de Júlio Verne "Viagem ao Centro da Terra" e o filme "Viagem ao Centro da Terra", mas devemos apreciar obras de ficção como ficção, e não acreditar nelas seriamente.
{: .prompt-tip }

### Para $b<R<a$
$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Resultados
Os gráficos a seguir mostram o potencial gravitacional $\Phi$ e a magnitude do vetor de campo gravitacional $\|\mathbf{g}\|$ como funções da distância $R$ para as três regiões que calculamos:

![Gravitational Potential as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-gravitational-potential.png)
![Magnitude of the Field Vector as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-field-vector.png)
> - Código de visualização em Python: [Repositório yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/shell_theorem.py)
> - Licença: [Veja aqui](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

Podemos observar que tanto o potencial gravitacional quanto a magnitude do vetor de campo gravitacional são contínuos. Se o potencial gravitacional fosse descontínuo em algum ponto, o gradiente do potencial, ou seja, a magnitude da gravidade, seria infinito nesse ponto, o que não é fisicamente plausível. Portanto, a função potencial deve ser contínua em todos os pontos. No entanto, a *derivada* do vetor de campo gravitacional é descontínua nas superfícies interna e externa da casca.

## Exemplo: Curvas de Rotação Galáctica
De acordo com observações astronômicas, a maior parte da massa observável em muitas galáxias espirais que rotacionam em torno de seus centros, como a Via Láctea ou Andrômeda, está concentrada próxima ao núcleo. No entanto, a velocidade orbital dessas massas em galáxias espirais difere significativamente das previsões teóricas baseadas na distribuição de massa observável, como pode ser visto no gráfico a seguir, permanecendo quase constante além de certa distância.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Fonte da imagem*
> - Autor: Usuário da Wikipedia [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - Licença: Domínio Público

![Rotation Curve of Spiral Galaxy M33](https://upload.wikimedia.org/wikipedia/commons/c/cd/Rotation_curve_of_spiral_galaxy_Messier_33_%28Triangulum%29.png)
> **Curva de rotação da galáxia espiral M33 (Galáxia do Triângulo)**
> - Autor: Usuário do Wikimedia [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama)
> - Licença: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Vamos prever a velocidade orbital em função da distância para o caso em que a massa da galáxia está concentrada no núcleo, verificar que essa previsão não corresponde às observações, e mostrar que a massa $M(R)$ distribuída dentro da distância $R$ do centro da galáxia deve ser proporcional a $R$ para explicar os resultados observados.

Primeiro, se a massa $M$ da galáxia estiver concentrada no núcleo, a velocidade orbital a uma distância $R$ seria:

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

Neste caso, prevê-se uma velocidade orbital que diminui com $1/\sqrt{R}$, como mostrado pela linha pontilhada nos dois gráficos acima. No entanto, de acordo com as observações, a velocidade orbital $v$ permanece quase constante independentemente da distância $R$, o que não corresponde à previsão. Esses resultados observacionais só podem ser explicados se $M(R)\propto R$.

Se definirmos $M(R) = kR$ com uma constante de proporcionalidade $k$, então:

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(constante)}. $$

A partir disso, os astrofísicos concluem que deve haver "matéria escura (dark matter)" não detectada em muitas galáxias, e que essa matéria escura deve constituir mais de 90% da massa do universo. No entanto, a natureza exata da matéria escura ainda não foi claramente identificada, e existem tentativas, embora não sejam teorias dominantes, de explicar os resultados observacionais sem assumir a existência de matéria escura, como a Dinâmica Newtoniana Modificada (Modified Newtonian Dynamics, MOND). Hoje, essas áreas de pesquisa estão na vanguarda da astrofísica.
