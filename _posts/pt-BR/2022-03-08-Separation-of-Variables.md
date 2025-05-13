---
title: Método de Separação de Variáveis
description: Aprenda sobre o método de separação de variáveis e veja alguns exemplos relacionados.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Método de Separação de Variáveis
**Equação separável**: Uma equação que pode ser expressa na forma $g(y)y'=f(x)$ através de manipulação algébrica.

Integrando ambos os lados da equação separável $g(y)y'=f(x)$ em relação a $x$, obtemos:

$$ \int g(y)y'dx = \int f(x)dx + c $$ 

Como $y'dx=dy$, temos:

$$ \int g(y)dy = \int f(x)dx + c $$

Assim, podemos separar as expressões em termos de $x$ e $y$ nos lados direito e esquerdo, respectivamente. Se $f$ e $g$ forem funções contínuas, podemos calcular essas integrais para obter a solução geral da equação diferencial dada. Este método de resolução é chamado de **método de separação de variáveis**.

## Exemplo de Modelagem: Datação por Radiocarbono
Oetzi é uma múmia do Neolítico descoberta nos Alpes de Oetztal em 11991 HE (Era Humana). Se a proporção de carbono-14 em relação ao carbono-12 nesta múmia é 52,5% da de um organismo vivo, aproximadamente quando Oetzi viveu e morreu?
> A proporção de carbono-14 radioativo em relação ao carbono-12 é constante na atmosfera e nos organismos vivos. Quando um organismo morre, a absorção de carbono-14 pela respiração e alimentação cessa, mas o decaimento do carbono-14 continua, reduzindo assim a proporção de carbono radioativo. Portanto, a idade de um fóssil pode ser estimada comparando a proporção de carbono radioativo no fóssil com a proporção na atmosfera. A meia-vida do carbono-14 é de 5715 anos.
{: .prompt-info }

### Solução
Separando as variáveis e integrando a equação diferencial ordinária $y'=ky$, obtemos:

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Para determinar a constante $k$, usamos a meia-vida $H=5715$:

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Finalmente, para encontrar o tempo $t$ em que Oetzi morreu, substituímos a proporção de 52,5%:

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{Estima-se que morreu há cerca de 5310 anos, por volta de 6680 HE}. $$

## Exemplo de Modelagem: Problema de Mistura
Inicialmente, um tanque contém 1000L de água com 10kg de sal dissolvido. Uma solução salina flui para o tanque a uma taxa de 10L por minuto, contendo 0,2kg de sal por litro. A solução no tanque é bem misturada e mantida uniforme, e esta solução salina flui para fora do tanque a uma taxa de 10L por minuto. Encontre a quantidade de sal $y(t)$ no tanque no tempo $t$.

### 1. Configuração do Modelo

$$ y'=\text{taxa de entrada} - \text{taxa de saída}. $$

A taxa de entrada de sal é 2kg por minuto. A taxa de saída de solução salina por minuto é 0,01 do volume total da solução salina, então a taxa de saída de sal por minuto é $0.01 y(t)$. Portanto, o modelo é a equação diferencial ordinária:

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Resolução do Modelo
A equação diferencial ordinária estabelecida anteriormente é separável. Vamos separar as variáveis, integrar e então aplicar a função exponencial em ambos os lados:

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Inicialmente, a quantidade de sal no tanque é 10kg, então a condição inicial é $y(0)=10$. Substituindo $y=10,\ t=0$ na equação acima, temos $10-200=ce^0=c$, portanto $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Isso significa que, na situação dada, a quantidade de sal no tanque se aproxima e converge exponencialmente para 200kg.

## Exemplo de Modelagem: Lei de Resfriamento de Newton
Durante o inverno, a temperatura diurna de um edifício de escritórios é mantida a 20°C. O aquecimento é desligado às 22h e ligado novamente às 6h. Em uma determinada madrugada, às 2h, a temperatura interna do edifício era de 17,4°C. A temperatura externa era de 10°C às 22h e caiu para 4°C às 6h. Qual era a temperatura interna do edifício às 6h quando o aquecimento foi ligado?
> **Lei de Resfriamento de Newton**  
> A taxa de variação da temperatura T de um objeto em relação ao tempo é proporcional à diferença entre a temperatura do objeto e a temperatura do ambiente ao seu redor.
{: .prompt-info }

### 1. Configuração do Modelo
Seja $T(t)$ a temperatura interna do edifício e $T_A$ a temperatura externa. Então, pela Lei de Resfriamento de Newton:

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Solução Geral
Sabemos apenas que $T_A$ varia entre 10°C e 4°C, mas não sabemos exatamente que valores assume, então não podemos resolver a equação estabelecida anteriormente. Nestes casos, *pode ser útil simplificar a situação para um problema mais fácil*. A média dos dois valores conhecidos é 7°C, então vamos assumir que a função desconhecida $T_A$ é uma função constante $T_A=7$. Mesmo que não seja exato, podemos esperar obter um valor aproximado para a temperatura interna do edifício $T$ às 6h, que é o que queremos determinar.

Para a constante $T_A=7$, a equação diferencial ordinária estabelecida anteriormente é separável. Separando as variáveis, integrando e aplicando a função exponencial, podemos obter a solução geral:

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Solução Particular
Escolhendo 22h como $t=0$, a condição inicial dada é $T(0)=20$. Vamos chamar a solução particular obtida neste caso de $T_p$. Substituindo:

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Determinação de $k$
Como a temperatura interna do edifício era 17,4°C às 2h, temos $T(4)=17.4$. Determinando algebricamente o valor de $k$ e inserindo-o em $T_p(t)$:

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Resposta e Interpretação
6h corresponde a $t=8$, então:

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[°C]}. $$

## Exemplo de Modelagem: Teorema de Torricelli
Um tanque tem um diâmetro de 2m e um orifício com diâmetro de 1cm. A altura inicial da água quando o orifício é aberto é de 2,25m. Determine a altura da água no tanque em qualquer momento e o tempo necessário para o tanque esvaziar completamente.
> **Teorema de Torricelli**  
> A velocidade da água que escoa sob a influência da gravidade é:
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: altura da água acima do orifício no tempo $t$
> $g=980\text{cm/s²}$: aceleração da gravidade na superfície terrestre
{: .prompt-info }

### 1. Configuração do Modelo
O volume $\Delta V$ que escoa durante um curto intervalo de tempo $\Delta t$ é:

$$ \Delta V = Av\Delta t \qquad (A: \text{área do orifício})$$

$\Delta V$ deve ser igual à mudança de volume $\Delta V^*$ dentro do tanque. Além disso:

$$ \Delta V^* = -B\Delta h \qquad (B: \text{área da seção transversal do tanque}) $$

onde $\Delta h(>0)$ é a diminuição na altura da água $h(t)$. Igualando $\Delta V$ e $\Delta V^*$:

$$ -B\Delta h = Av\Delta t $$

Agora, expressando $v$ de acordo com o Teorema de Torricelli e fazendo $\Delta t$ se aproximar de 0, obtemos o seguinte modelo expresso como uma equação diferencial ordinária de primeira ordem:

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Solução Geral
Esta equação diferencial ordinária é separável. Separando as variáveis e integrando:

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Dividindo ambos os lados por 2 e elevando ao quadrado, obtemos $h=(c-13.28At/B)^2$. Substituindo $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$, obtemos a solução geral:

$$ h(t)=(c-0.000332t)^2 $$

### 3. Solução Particular
A condição inicial é $h(0)=225\text{cm}$. Substituindo $t=0$ e $h=225$ na solução geral, obtemos $c^2=225, c=15.00$, e portanto a solução particular:

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Tempo necessário para o tanque esvaziar

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Transformação para a Forma Separável
Em alguns casos, é possível transformar uma equação diferencial ordinária não separável em uma forma separável introduzindo uma nova função desconhecida de $y$.

$$ y'=f\left(\frac {y}{x}\right). $$

Para resolver uma equação diferencial ordinária deste tipo, fazemos $y/x=u$, então:

$$ y=ux,\quad y'=u'x+u $$

Substituindo em $y'=f(y/x)$, obtemos $u'x=f(u)-u$. Se $f(u)-u\neq0$, então:

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$

que está na forma separada.
