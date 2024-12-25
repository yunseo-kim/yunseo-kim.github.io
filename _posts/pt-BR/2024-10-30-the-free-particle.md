---
title: A Partícula Livre
description: Exploramos o fato de que a solução separável para uma partícula livre
  com V(x)=0 não pode ser normalizada e o que isso significa, demonstramos qualitativamente
  a relação de incerteza posição-momento para a solução geral e calculamos a velocidade
  de fase e de grupo de Ψ(x,t), interpretando-as fisicamente.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Partícula livre: $V(x)=0$, sem condições de contorno (energia arbitrária)
> - A solução separável $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ diverge para infinito quando integrada ao quadrado, portanto não pode ser normalizada, o que implica:
>   - Uma partícula livre não pode existir em um estado estacionário
>   - Uma partícula livre não pode ter sua energia definida como um único valor preciso (existe incerteza na energia)
> - No entanto, a solução geral da equação de Schrödinger dependente do tempo ainda é uma combinação linear de soluções separáveis, então as soluções separáveis ainda têm significado matemático importante. Porém, neste caso, sem condições restritivas, a solução geral é uma integral ($\int$) sobre a variável contínua $k$, em vez de uma soma ($\sum$) sobre a variável discreta $n$.
> - Solução geral da equação de Schrödinger:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{onde }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Relação entre incerteza na posição e incerteza no momento:
>   - Quando a incerteza na posição diminui, a incerteza no momento aumenta, e vice-versa
>   - Ou seja, quanticamente é impossível conhecer simultaneamente a posição e o momento exatos de uma partícula livre
> - Velocidade de fase e velocidade de grupo da função de onda $\Psi(x,t)$:
>   - Velocidade de fase: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - Velocidade de grupo: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Significado físico da velocidade de grupo e comparação com a mecânica clássica:
>   - Fisicamente, a velocidade de grupo representa a velocidade de movimento da partícula
>   - Assumindo que $\phi(k)$ tem uma forma muito acentuada em torno de algum valor $k_0$ (quando a incerteza no momento é suficientemente pequena), 
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Pré-requisitos
- Fórmula de Euler
- Transformada de Fourier & Teorema de Plancherel
- [Equação de Schrödinger e Função de Onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Equação de Schrödinger Independente do Tempo](/posts/time-independent-schrodinger-equation/)
- [Poço Quadrado Infinito Unidimensional](/posts/the-infinite-square-well/)

## Configuração do Modelo
Vamos examinar o caso mais simples de uma partícula livre ($V(x)=0$). Classicamente, isso é apenas um movimento com velocidade constante, mas na mecânica quântica, este problema é mais interessante.  
A [equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/) para uma partícula livre é

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

ou seja,

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, onde }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[Até aqui, é o mesmo que o interior do poço quadrado infinito com potencial 0](/posts/the-infinite-square-well/#configuração-do-modelo-e-condições-de-contorno). No entanto, desta vez, vamos escrever a solução geral na seguinte forma exponencial:

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ e $C\cos{kx}+D\sin{kx}$ são formas equivalentes de escrever a mesma função de $x$. Pela fórmula de Euler $e^{ix}=\cos{x}+i\sin{x}$,
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> Ou seja, se definirmos $C=A+B$, $D=i(A-B)$, então 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> Inversamente, expressando $A$ e $B$ em termos de $C$ e $D$, temos $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$.
>
> Na mecânica quântica, quando $V=0$, a função exponencial representa uma onda em movimento e é mais conveniente ao lidar com partículas livres. Por outro lado, as funções seno e cosseno são úteis para representar ondas estacionárias e aparecem naturalmente no caso do poço quadrado infinito.
{: .prompt-info }

Ao contrário do poço quadrado infinito, desta vez não há condições de contorno que restrinjam $k$ e $E$. Ou seja, uma partícula livre pode ter qualquer energia positiva.

## Solução Separável e Velocidade de Fase
Adicionando a dependência temporal $e^{-iEt/\hbar}$ a $\psi(x)$, obtemos

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

Qualquer função de $x$ e $t$ que dependa de uma forma especial $(x\pm vt)$ representa uma onda que se move na direção $\mp x$ com velocidade $v$, sem mudar de forma. Portanto, o primeiro termo na equação ($\ref{eqn:Psi_seperated_solution}$) representa uma onda se movendo para a direita, e o segundo termo representa uma onda com o mesmo comprimento de onda e velocidade de propagação, mas com amplitude diferente, se movendo para a esquerda. Como eles diferem apenas no sinal de $k$, podemos escrever

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

onde a direção de propagação da onda depende do sinal de $k$ da seguinte forma:

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{movimento para a direita}, \\
k<0 \Rightarrow & \text{movimento para a esquerda}.
\end{cases} \tag{6}$$

O 'estado estacionário' de uma partícula livre é claramente uma onda progressiva*, com comprimento de onda $\lambda = 2\pi/\|k\|$ e, pela fórmula de de Broglie,

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

de momento.

> *É claro que há uma contradição física em uma 'onda estacionária' ser uma onda progressiva. A razão será explicada em breve.
{: .prompt-info }

Além disso, a velocidade desta onda é:

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(Aqui, $\omega$ é o coeficiente de $t$, $\cfrac{\hbar k^2}{2m}$.)

No entanto, esta função de onda não pode ser normalizada porque diverge para infinito quando integrada ao quadrado.

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

Ou seja, <u>no caso de uma partícula livre, a solução separável não é um estado fisicamente possível.</u> Uma partícula livre não pode existir em um [estado estacionário](/posts/time-independent-schrodinger-equation/#1-são-estados-estacionários) e não pode ter [um valor específico de energia](/posts/time-independent-schrodinger-equation/#2-é-um-estado-com-um-valor-de-energia-total-claro-e-não-uma-distribuição-de-probabilidade-com-um-intervalo). Na verdade, intuitivamente, seria mais estranho se uma onda estacionária se formasse sem nenhuma condição de contorno em ambas as extremidades.

## Encontrando a Solução Geral $\Psi(x,t)$ da Equação de Schrödinger Dependente do Tempo
Apesar disso, esta solução separável ainda tem um significado importante porque, independentemente da interpretação física, [a solução geral da equação de Schrödinger dependente do tempo é uma combinação linear de soluções separáveis](/posts/time-independent-schrodinger-equation/#3-a-solução-geral-da-equação-de-schrödinger-dependente-do-tempo-é-uma-combinação-linear-de-soluções-separadas), o que tem um significado matemático. No entanto, neste caso, como não há condições restritivas, a solução geral tem a forma de uma integral ($\int$) sobre a variável contínua $k$, em vez de uma soma ($\sum$) sobre a variável discreta $n$.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Aqui, $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ desempenha o mesmo papel que $c_n$ na [equação (21) do post 'Equação de Schrödinger Independente do Tempo'](/posts/time-independent-schrodinger-equation/#3-a-solução-geral-da-equação-de-schrödinger-dependente-do-tempo-é-uma-combinação-linear-de-soluções-separadas).
{: .prompt-info }

Esta função de onda pode ser normalizada para $\phi(k)$ apropriado, mas deve ter um intervalo de $k$ e, portanto, um intervalo de energia e velocidade. Isso é chamado de **pacote de ondas (wave packet)**.

> Uma função seno é espacialmente infinitamente estendida e não pode ser normalizada. No entanto, quando várias dessas ondas são superpostas, elas se localizam por interferência e podem ser normalizadas.
{: .prompt-info }

## Encontrando $\phi(k)$ usando o Teorema de Plancherel

Agora que conhecemos a forma de $\Psi(x,t)$ (equação [$\ref{eqn:Psi_general_solution}$]), só precisamos determinar $\phi(k)$ que satisfaça a função de onda inicial

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

Este é um problema típico de análise de Fourier, e podemos obter a resposta usando o **Teorema de Plancherel**:

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ é chamada de **transformada de Fourier** de $f(x)$, e $f(x)$ é chamada de **transformada inversa de Fourier** de $F(k)$. A diferença entre as duas é apenas o sinal do expoente, como pode ser facilmente visto na equação ($\ref{eqn:plancherel_theorem}$). Claro, existe a condição restritiva de que a integral deve existir para as funções permitidas.

> A condição necessária e suficiente para que $f(x)$ exista é que $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ seja finito. Neste caso, $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ também é finito, e 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Algumas pessoas se referem a esta equação, em vez da equação ($\ref{eqn:plancherel_theorem}$), como o Teorema de Plancherel (a [Wikipedia](https://en.wikipedia.org/wiki/Plancherel_theorem) também a descreve desta forma).
{: .prompt-info }

Neste caso, a integral certamente existe devido à condição física de que $\Psi(x,0)$ deve ser normalizada. Portanto, a solução quântica para uma partícula livre é dada pela equação ($\ref{eqn:Psi_general_solution}$), onde

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> No entanto, na prática, quase nunca é possível resolver analiticamente a integral na equação ($\ref{eqn:Psi_general_solution}$). Geralmente, os valores são calculados usando análise numérica por computador.
{: .prompt-tip }

## Cálculo da Velocidade de Grupo do Pacote de Ondas e Interpretação Física

Essencialmente, um pacote de ondas é uma superposição de muitas funções seno com amplitudes determinadas por $\phi$. Ou seja, há 'ondulações (ripples)' dentro de um 'envelope' que forma o pacote de ondas.

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *Aviso de licença e fonte original da imagem*
> - Código fonte para geração da imagem (gnuplot): [yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - Licença: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - Autor original: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - Aviso de licença original: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Fisicamente, o que corresponde à velocidade da partícula não é a velocidade das ondulações individuais (**velocidade de fase, phase velocity**) calculada anteriormente na equação ($\ref{eqn:phase_velocity}$), mas a velocidade do envelope externo (**velocidade de grupo, group velocity**).

### Relação entre Incerteza na Posição e Incerteza no Momento
Vamos examinar a relação entre a incerteza na posição e a incerteza no momento, considerando separadamente o termo integral $\int\phi(k)e^{ikx}dk$ da equação ($\ref{eqn:Psi_at_t_0}$) e o termo integral $\int\Psi(x,0)e^{-ikx}dx$ da equação ($\ref{eqn:phi}$).

#### Quando a incerteza na posição é pequena
Quando $\Psi$ está distribuída em uma região muito estreita $[x_0-\delta, x_0+\delta]$ em torno de algum valor $x_0$ no espaço de posição e é próxima a zero fora dessa região (<u>quando a incerteza na posição é pequena</u>), $e^{-ikx} \approx e^{-ikx_0}$ é quase constante em relação a $x$, então

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{eq. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

O termo de integral definida é constante em relação a $p$, então devido ao termo $e^{-ipx_0/\hbar}$ na frente, $\phi$ terá a forma de uma onda senoidal em relação a $p$ no espaço de momento, ou seja, será distribuída em um amplo intervalo de momento (<u>a incerteza no momento é grande</u>).

#### Quando a incerteza no momento é pequena
Da mesma forma, quando $\phi$ está distribuída em uma região muito estreita $[p_0-\delta, p_0+\delta]$ em torno de algum valor $p_0$ no espaço de momento e é próxima a zero fora dessa região (<u>quando a incerteza no momento é pequena</u>), pela equação ($\ref{eqn:de_broglie_formula}$), $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ é quase constante em relação a $p$ e $dk=\frac{1}{\hbar}dp$, então

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

Devido ao termo $e^{ip_0x/\hbar}$ na frente, $\Psi$ terá a forma de uma onda senoidal em relação a $x$ no espaço de posição, ou seja, será distribuída em um amplo intervalo de posição (<u>a incerteza na posição é grande</u>).

#### Conclusão
Quando a incerteza na posição diminui, a incerteza no momento aumenta, e vice-versa. Portanto, quanticamente, é impossível conhecer simultaneamente a posição e o momento exatos de uma partícula livre.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Fonte da imagem*
> - Autor: Usuário da Wikipedia em inglês [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - Licença: domínio público

> Na verdade, devido ao princípio da incerteza (uncertainty principle), isso se aplica não apenas a partículas livres, mas a todos os casos. O princípio da incerteza será abordado em um post separado no futuro.
{: .prompt-info }

### Velocidade de Grupo do Pacote de Ondas
Reescrevendo a solução geral da equação ($\ref{eqn:Psi_general_solution}$) com $\omega \equiv \cfrac{\hbar k^2}{2m}$ como na equação ($\ref{eqn:phase_velocity}$), temos

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> Uma equação que expressa $\omega$ como uma função de $k$, como $\omega = \cfrac{\hbar k^2}{2m}$, é chamada de **relação de dispersão (dispersion relation)**. O conteúdo a seguir se aplica geralmente a todos os pacotes de ondas, independentemente da relação de dispersão.
{: .prompt-info }

Agora, vamos supor que $\phi(k)$ tem uma forma muito acentuada em torno de algum valor apropriado $k_0$. (Pode ser amplamente distribuída em $k$, mas tal forma de pacote de onda se distorce muito rapidamente e muda para outra forma. Como os componentes para diferentes $k$ se movem com velocidades diferentes, perde-se o significado de um 'grupo' total bem definido com uma velocidade. Ou seja, <u>a incerteza no momento aumenta.</u>)  
Como a função sendo integrada pode ser ignorada exceto perto de $k_0$, podemos expandir a função $\omega(k)$ em série de Taylor em torno deste ponto, e escrevendo apenas até o termo de primeira ordem, obtemos

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Agora, fazendo a substituição $s=k-k_0$ e integrando em torno de $k_0$, temos

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

O termo $e^{i(k_0x-\omega_0t)}$ na frente representa uma onda senoidal ('ondulações') se movendo com velocidade $\omega_0/k_0$, e o termo integral que determina a amplitude desta onda senoidal ('envelope') se move com velocidade $\omega_0^\prime$ devido à parte $e^{is(x-\omega_0^\prime t)}$. Portanto, a velocidade de fase em $k=k_0$ é

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

que é o mesmo valor da equação ($\ref{eqn:phase_velocity}$), e a velocidade de grupo é

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

que é o dobro da velocidade de fase.

## Comparação com a Mecânica Clássica

Sabendo que a mecânica clássica se aplica em escalas macroscópicas, os resultados obtidos através da mecânica quântica devem se aproximar dos resultados calculados na mecânica clássica quando a incerteza quântica é suficientemente pequena. No caso da partícula livre que estamos tratando agora, quando $\phi(k)$ tem uma forma muito acentuada em torno de um valor apropriado $k_0$ (ou seja, <u>quando a incerteza no momento é suficientemente pequena</u>), a velocidade de grupo $v_\text{group}$, que corresponde à velocidade da partícula na mecânica quântica, deve ser igual à velocidade da partícula $v_\text{classical}$ calculada na mecânica clássica para o mesmo $k$ e o valor de energia $E$ correspondente.

Substituindo $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ da equação ($\ref{eqn:t_independent_schrodinger_eqn}$) na velocidade de grupo que acabamos de calcular (equação [$\ref{eqn:group_velocity}$]), obtemos

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

e a velocidade de uma partícula livre com energia cinética $E$ na mecânica clássica é igualmente

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Portanto, como $v_\text{quantum}=v_\text{classical}$, podemos confirmar que o resultado obtido aplicando a mecânica quântica é uma solução fisicamente válida.
