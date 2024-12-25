---
title: O Poço Quadrado Infinito Unidimensional
description: Examinamos o problema do poço quadrado infinito unidimensional, um exemplo
  simples mas importante que ilustra bem os conceitos básicos da mecânica quântica.
  Nesta situação ideal, determinamos o n-ésimo estado estacionário ψ(x) e a energia
  E da partícula, e exploramos quatro importantes propriedades matemáticas de ψ(x).
  A partir disso, obtemos a solução geral Ψ(x,t).
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Problema do poço quadrado infinito unidimensional: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{caso contrário}
>   \end{cases}$$
> - Condições de contorno: $ \psi(0) = \psi(a) = 0 $
> - Níveis de energia do n-ésimo estado estacionário: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Solução da equação de Schrödinger independente do tempo dentro do poço:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Interpretação física de cada estado estacionário $\psi_n$: 
>   - Forma de onda estacionária em uma corda de comprimento $a$
>   - **Estado fundamental**: estado estacionário $\psi_1$ com a menor energia
>   - **Estados excitados**: estados restantes com $n\geq 2$, cuja energia aumenta proporcionalmente a $n^2$
> - Quatro importantes propriedades matemáticas de $\psi_n$:
>   1. Se o potencial $V(x)$ tem simetria, funções pares e ímpares aparecem alternadamente em relação ao centro do poço
>   2. À medida que a energia aumenta, cada estado consecutivo tem um **nó** a mais
>   3. Possui **ortonormalidade**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Possui **completude**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Solução geral da equação de Schrödinger (combinação linear dos estados estacionários):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{onde os coeficientes }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Pré-requisitos
- Distribuições de probabilidade contínua e densidade de probabilidade
- Ortogonalidade e normalização (álgebra linear)
- Séries de Fourier e completude (álgebra linear)
- [Equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/)

## Condição de potencial dada
Se o potencial for

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{caso contrário}
\end{cases} \tag{1}$$

então a partícula dentro deste potencial é uma partícula livre no intervalo $0<x<a$ e está sujeita a uma força infinita nas extremidades ($x=0$ e $x=a$), não podendo escapar. No modelo clássico, isso é interpretado como um movimento de vai e vem infinito, repetindo colisões perfeitamente elásticas para frente e para trás, sem forças não conservativas atuando. Embora este potencial seja extremamente artificial e simples, é justamente por isso que pode servir como um caso de referência útil ao estudar outras situações físicas na mecânica quântica posteriormente, portanto é necessário examiná-lo cuidadosamente.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Configuração do modelo e condições de contorno
Fora do poço, a probabilidade de encontrar a partícula é $0$, então $\psi(x)=0$. Dentro do poço, $V(x)=0$, então a [equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/) é

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

ou seja,

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ onde } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Aqui, assumimos que $E\geq 0$.
{: .prompt-info }

Esta é a equação que descreve um **oscilador harmônico simples** clássico, e a solução geral é

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

onde $A$ e $B$ são constantes arbitrárias, que são tipicamente determinadas pelas **condições de contorno** dadas no problema ao buscar uma solução específica. <u>No caso de $\psi(x)$, geralmente a condição de contorno é que tanto $\psi$ quanto $d\psi/dx$ sejam contínuas, mas onde o potencial se torna infinito, apenas $\psi$ é contínua.</u>

## Encontrando a solução da equação de Schrödinger independente do tempo

Como $\psi(x)$ é contínua,

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

deve se conectar com a solução fora do poço. Na equação ($\ref{eqn:psi_general_solution}$), quando $x=0$

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

então, substituindo ($\ref{eqn:boundary_conditions}$), devemos ter $B=0$.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Então, $\psi(a)=A\sin{ka}$, e para satisfazer $\psi(a)=0$ da equação ($\ref{eqn:boundary_conditions}$), devemos ter $A=0$ (solução trivial) ou $\sin{ka}=0$. Portanto,

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Aqui também, $k=0$ é uma solução trivial, resultando em $\psi(x)=0$, que não pode ser normalizada e, portanto, não é a solução que estamos procurando neste problema. Além disso, como $\sin(-\theta)=-\sin(\theta)$, o sinal negativo pode ser absorvido em $A$ na equação ($\ref{eqn:psi_without_B}$), então podemos considerar apenas o caso $ka>0$ sem perder generalidade. Portanto, as soluções possíveis para $k$ são

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Então, $\psi_n=A\sin{k_n x}$ e $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, substituindo na equação ($\ref{eqn:t_independent_schrodinger_eqn}$), os valores possíveis de $E$ são:

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

Em contraste marcante com o caso clássico, uma partícula quântica em um poço quadrado infinito não pode ter qualquer energia, mas deve ter um dos valores permitidos.

> A energia é quantizada pelas condições de contorno aplicadas à solução da equação de Schrödinger independente do tempo.
{: .prompt-info }

Agora podemos encontrar $A$ normalizando $\psi$.

> Originalmente, normalizamos $\Psi(x,t)$, mas pela equação (11) da [equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/#1-são-estados-estacionários), isso equivale a normalizar $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Isso determina estritamente apenas a magnitude de $A$, mas como a fase de $A$ não tem significado físico, podemos simplesmente usar a raiz quadrada real positiva como $A$. Portanto, a solução dentro do poço é

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Interpretação física de cada estado estacionário $\psi_n$
Como na equação ($\ref{eqn:psi_n}$), encontramos infinitas soluções da equação de Schrödinger independente do tempo para cada nível de energia $n$. A imagem abaixo mostra os primeiros deles graficamente.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Fonte da imagem*
> - Autor: Usuário do Wikimedia [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - Licença: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Esses estados têm a forma de ondas estacionárias em uma corda de comprimento $a$, com $\psi_1$, que tem a menor energia, sendo chamado de **estado fundamental**, e os estados restantes com $n\geq 2$, cuja energia aumenta proporcionalmente a $n^2$, sendo chamados de **estados excitados**.

## Quatro importantes propriedades matemáticas de $\psi_n$
Todas as funções $\psi_n(x)$ têm as seguintes quatro propriedades importantes. Essas quatro propriedades são muito poderosas e não se limitam apenas ao poço quadrado infinito. A primeira propriedade sempre se mantém se o próprio potencial for uma função simétrica, e a segunda, terceira e quarta propriedades são características gerais que aparecem independentemente da forma do potencial.

### 1. Funções pares e ímpares aparecem alternadamente em relação ao centro do poço.
Para números inteiros positivos $n$, $\psi_{2n-1}$ é uma função par e $\psi_{2n}$ é uma função ímpar.

### 2. À medida que a energia aumenta, cada estado consecutivo tem um nó a mais.
Para números inteiros positivos $n$, $\psi_n$ tem $(n-1)$ **nós**.

### 3. Esses estados possuem ortogonalidade.

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

Isso significa que eles são **ortogonais** entre si.

> No caso do poço quadrado infinito que estamos examinando agora, $\psi$ é real, então não precisamos tomar o complexo conjugado ($^*$) de $\psi_m$, mas é bom criar o hábito de sempre incluí-lo para casos em que isso não é verdade.
{: .prompt-tip }

#### Prova
Quando $m\neq n$,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Quando $m=n$, esta integral é 1 devido à normalização, e podemos expressar a ortogonalidade e a normalização juntas usando o **delta de Kronecker** $\delta_{mn}$:

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

Neste caso, dizemos que $\psi$ é **ortonormal**.

### 4. Essas funções possuem completude.
No sentido de que qualquer outra função $f(x)$ pode ser escrita como uma combinação linear

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

essas funções são **completas**. A equação ($\ref{eqn:fourier_series}$) é a **série de Fourier** de $f(x)$, e o fato de que qualquer função pode ser expandida dessa maneira é chamado de **teorema de Dirichlet**.

## Encontrando os coeficientes $c_n$ usando o método de Fourier
Quando $f(x)$ é dado, podemos usar a completude (completeness) e a ortonormalidade (orthonormality) mencionadas acima para encontrar os coeficientes $c_n$ usando o seguinte método, conhecido como **método de Fourier**. Multiplicando ambos os lados da equação ($\ref{eqn:fourier_series}$) por $\psi_m(x)^*$ e integrando, pelas equações ($\ref{eqn:orthonomality}$) e ($\ref{eqn:kronecker_delta}$), obtemos:

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Note que o delta de Kronecker faz com que todos os termos da soma desapareçam, exceto o termo onde $n=m$.
{: .prompt-info }

Portanto, o coeficiente de n-ésima ordem ao expandir $f(x)$ é

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Encontrando a solução geral $\Psi(x,t)$ da equação de Schrödinger dependente do tempo
Cada estado estacionário do poço quadrado infinito, de acordo com a equação (10) do post ['Equação de Schrödinger independente do tempo'](/posts/time-independent-schrodinger-equation/#1-são-estados-estacionários) e a equação ($\ref{eqn:psi_n}$) que encontramos anteriormente, é

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Além disso, vimos anteriormente na [Equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/#3-a-solução-geral-da-equação-de-schrödinger-dependente-do-tempo-é-uma-combinação-linear-de-soluções-separadas) que a solução geral da equação de Schrödinger pode ser expressa como uma combinação linear de estados estacionários. Portanto, podemos escrever

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Agora, só precisamos encontrar os coeficientes $c_n$ que satisfazem a seguinte condição:

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Pela completude de $\psi$ que vimos anteriormente, sempre existem $c_n$ que satisfazem isso, e podemos encontrá-los substituindo $\Psi(x,0)$ por $f(x)$ na equação ($\ref{eqn:coefficients_n}$).

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Se $\Psi(x,0)$ for dado como condição inicial, usamos a equação ($\ref{eqn:calc_of_cn}$) para encontrar os coeficientes de expansão $c_n$, e os substituímos na equação ($\ref{eqn:general_solution}$) para encontrar $\Psi(x,t)$. Depois disso, podemos calcular qualquer quantidade física de interesse seguindo o processo do [teorema de Ehrenfest](/posts/ehrenfest-theorem/). Este método pode ser aplicado não apenas ao poço quadrado infinito, mas a qualquer potencial, mudando apenas a forma das funções $\psi$ e a equação para os níveis de energia permitidos.

## Derivação da conservação de energia ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Vamos derivar a conservação de energia que vimos brevemente na [Equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/#conservação-de-energia) usando a ortonormalidade de $\psi(x)$ (equações [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]). Como $c_n$ é independente do tempo, basta provar para o caso $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Além disso, como

$$ \hat{H}\psi_n = E_n\psi_n $$

obtemos:

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
