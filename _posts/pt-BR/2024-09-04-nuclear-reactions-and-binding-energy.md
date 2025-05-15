---
title: Reações Nucleares e Energia de Ligação
description: Exploramos as expressões de reações nucleares, a definição do valor Q (Q-value), e os conceitos de defeito de massa (mass defect) e energia de ligação (binding energy).
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Reação Nuclear (Nuclear Reaction)
### Leis Fundamentais nas Reações Nucleares
*Reação nuclear*: reação em que dois núcleos atômicos diferentes, ou um núcleo atômico e um nucleon, colidem para produzir dois ou mais novos núcleos ou raios gama

Quando dois núcleos atômicos $a$ e $b$ reagem para produzir núcleos atômicos ou raios gama $c$ e $d$, esta reação é expressa da seguinte forma:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

Nas reações nucleares, aplicam-se as quatro leis fundamentais a seguir:

- *Lei da conservação de nucleons*: o número total de nucleons permanece o mesmo antes e depois da reação. Como o tipo de nucleon pode mudar, prótons e nêutrons não são conservados individualmente.
- *Lei da conservação de carga*: a soma total das cargas das partículas permanece a mesma antes e depois da reação.
- *Lei da conservação do momento*: a soma total do momento das partículas permanece a mesma antes e depois da reação.
- *Lei da conservação de energia*: a energia total, <u>incluindo a energia de massa de repouso</u>, permanece a mesma antes e depois da reação.

### Reação Exotérmica (exothermic reaction) & Reação Endotérmica (endothermic reaction)
Na reação nuclear da equação ($\ref{nuclear_reaction}$), a energia total antes da reação é a soma das energias de massa de repouso e energias cinéticas de $a$ e $b$, e a energia total após a reação é a soma das energias de massa de repouso e energias cinéticas de $c$ e $d$. Portanto, pela lei da conservação de energia, temos:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Reorganizando a equação acima, obtemos:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Ou seja, a diferença na energia cinética antes e depois da reação nuclear é igual à diferença na massa de repouso.
O lado direito da última equação é chamado de *valor Q (Q-value)* da reação nuclear e é definido como:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

O valor Q é sempre expresso em unidades de MeV, e como a energia de massa de repouso para 1 amu é geralmente 931 MeV, o valor Q também pode ser escrito como:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Reação exotérmica*: reação nuclear onde $Q>0$, parte da massa é convertida em energia cinética, aumentando a energia cinética após a reação
- *Reação endotérmica*: reação nuclear onde $Q<0$, parte da energia cinética é convertida em massa, diminuindo a energia cinética após a reação

| Tipo de reação nuclear | Valor Q | Mudança de massa antes e depois | Mudança de energia cinética antes e depois |
| :---: | :---: | :---: | :---: |
| Reação exotérmica | $Q>0$ | $\Delta m<0$ (diminui) | $\Delta E>0$ (aumenta) |
| Reação endotérmica | $Q<0$ | $\Delta m>0$ (aumenta) | $\Delta E<0$ (diminui) |

### Representação Simplificada de Reações Nucleares
A reação nuclear na equação ($\ref{nuclear_reaction}$) pode ser representada de forma simplificada como:

$$ a(b, c)d $$

Isso significa que $b$ incide sobre $a$, emitindo $c$ e transformando-se em $d$.

#### ex)
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Energia de Ligação (Binding Energy)
### Defeito de Massa (Mass Defect)
A massa de qualquer núcleo é ligeiramente menor que a soma das massas dos nêutrons e prótons que o compõem. Esta diferença é chamada de *defeito de massa*.

Se a massa do núcleo for $M_A$, o defeito de massa $\Delta$ de qualquer núcleo pode ser calculado como:

$$ \Delta = ZM_p + NM_n - M_A. $$

Quando o defeito de massa $\Delta$ é expresso em unidades de energia, representa a energia necessária para separar um núcleo em seus nucleons constituintes. Como é a energia que mantém os nucleons unidos, é chamada de *energia de ligação*. Inversamente, quando um núcleo é formado a partir de A nucleons, o nível de energia diminui em $\Delta$, liberando essa quantidade de energia durante o processo de reação nuclear.

### Energia de Ligação Média por Nucleon
A energia de ligação total de um núcleo atômico aumenta com o aumento do número de massa $A$, mas a taxa de aumento não é constante.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
A energia de ligação média por nucleon $\Delta/A$ aumenta rapidamente para números de massa baixos, mas diminui gradualmente para núcleos atômicos pesados com $A\geq56$, como pode ser visto na imagem acima.

### Relação entre o Valor Q e a Energia de Ligação
Na reação nuclear da equação ($\ref{nuclear_reaction}$), a energia de ligação do núcleo $a$ é:

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

e a massa de $a$ é:

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Da mesma forma, para os núcleos $b$, $c$ e $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Considerando que:

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

e substituindo essas expressões na equação ($\ref{Q_value}$), obtemos:

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Isso significa que quando dois núcleos menos estáveis se combinam para formar um núcleo mais estável através de um processo de reação nuclear, sempre há liberação de energia.

### Fusão Nuclear (Nuclear Fusion) e Fissão Nuclear (Nuclear Fission)
No caso de uma reação nuclear onde o deutério, com energia de ligação de $2,23\text{MeV}$, e o trítio, com energia de ligação de $8,48\text{MeV}$, se combinam para produzir $^4\text{He}$ com energia de ligação de $28,3\text{MeV}$ e liberar um nêutron:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

A diferença na energia de ligação antes e depois da reação, $28,3-(2,23+8,48)=17,6\text{MeV}$ (ou $3,52\text{MeV}$ por nucleon), é liberada na forma de energia cinética do núcleo de hélio e do nêutron.

A reação como na equação ($\ref{nuclear_fusion}$), onde dois núcleos atômicos leves se combinam para formar um núcleo atômico mais pesado, é chamada de *fusão nuclear*. Esta é a fonte de energia do Sol e de todas as estrelas, e um dia poderá ser utilizada diretamente pela humanidade como fonte de energia.

Por outro lado, quando o $^{235}\text{U}$ com energia de ligação de aproximadamente $1780\text{MeV}$ absorve um nêutron e se divide em $^{92}\text{Kr}$ com energia de ligação de $783\text{MeV}$ e $^{141}\text{Ba}$ com energia de ligação de aproximadamente $1170\text{MeV}$, liberando três nêutrons:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

A diferença na energia de ligação antes e depois da reação, $783+1170-1780=173\text{MeV}$ (ou $0,733\text{MeV}$ por nucleon), é liberada.

A reação como na equação ($\ref{nuclear_fission}$), onde um núcleo atômico pesado se divide em núcleos atômicos mais leves, é chamada de *fissão nuclear*. Desde o discurso "Átomos para a Paz" (Atoms for Peace) do 34º presidente dos EUA, Eisenhower, e a usina nuclear de Obninsk na União Soviética, a fissão nuclear tem sido amplamente utilizada como fonte de energia elétrica.

## Números Mágicos
Quando o número de nêutrons ou prótons em um núcleo é 2, 6, 8, 14, 20, 28, 50, 82 ou 126, esse núcleo tende a ser particularmente estável. Esses números de nucleons são chamados de *números mágicos*. Eles correspondem ao número de nêutrons e prótons necessários para preencher as camadas nucleares, de forma semelhante ao preenchimento das camadas eletrônicas externas dos átomos.

Os isótopos com números mágicos têm aplicações práticas na engenharia nuclear. Um exemplo notável é o zircônio-90 ($^{90}_{40} \mathrm{Zr}$), que possui 50 nêutrons. Devido à sua estabilidade e baixa absorção de nêutrons, é amplamente utilizado como material de revestimento para varetas de combustível em núcleos de reatores.
