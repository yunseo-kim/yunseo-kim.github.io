---
title: "Reações Nucleares e Energia de Ligação"
description: >-
  Aprenda sobre a expressão de reações nucleares, a definição do valor Q (Q-value), e os conceitos de defeito de massa (mass defect) e energia de ligação (binding energy).
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
---

## Reação Nuclear (Nuclear Reaction)
### Leis Fundamentais nas Reações Nucleares
*Reação nuclear (nuclear reaction)*: Uma reação onde dois núcleos atômicos diferentes ou um núcleo atômico e um nucleon colidem para produzir duas ou mais novas partículas nucleares ou raios gama.

Quando dois núcleos atômicos $a$ e $b$ reagem para produzir núcleos atômicos ou raios gama $c$ e $d$, esta reação é expressa da seguinte forma:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

Nas reações nucleares, as quatro leis fundamentais a seguir são aplicáveis:

- *Lei da conservação do número de nucleons (conservation of nucleon)*: O número total de nucleons é o mesmo antes e depois da reação. O tipo de nucleon pode mudar, então prótons e nêutrons não são conservados individualmente.
- *Lei da conservação da carga (conservation of charge)*: A soma total das cargas das partículas é a mesma antes e depois da reação.
- *Lei da conservação do momento (conservation of momentum)*: A soma total do momento das partículas é a mesma antes e depois da reação.
- *Lei da conservação da energia (conservation of energy)*: A energia total, <u>incluindo a energia de massa de repouso</u>, é a mesma antes e depois da reação.

### Reação Exotérmica (exothermic reaction) & Reação Endotérmica (endothermic reaction)
Na reação nuclear da equação ($\ref{nuclear_reaction}$), a energia total antes da reação é a soma das energias de massa de repouso e cinética de $a$ e $b$, e a energia total após a reação é a soma das energias de massa de repouso e cinética de $c$ e $d$. Portanto, pela lei da conservação da energia, temos:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Reorganizando esta equação, obtemos:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Isso mostra que a diferença na energia cinética antes e depois da reação nuclear é igual à diferença na massa de repouso.
O lado direito da última equação é chamado de *valor Q (Q-value)* da reação nuclear e é definido como:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

O valor Q é sempre expresso em unidades de MeV, e como a energia de massa de repouso para 1 amu é geralmente 931MeV, o valor Q também pode ser escrito como:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Reação exotérmica (exothermic reaction)*: Reação nuclear onde $Q>0$, parte da massa é convertida em energia cinética, aumentando a energia cinética após a reação
- *Reação endotérmica (endothermic reaction)*: Reação nuclear onde $Q<0$, parte da energia cinética é convertida em massa, diminuindo a energia cinética após a reação

| Tipo de Reação Nuclear | Valor Q | Mudança na Massa | Mudança na Energia Cinética |
| :---: | :---: | :---: | :---: |
| Reação Exotérmica | $Q>0$ | $\Delta m<0$ (diminui) | $\Delta E>0$ (aumenta) |
| Reação Endotérmica | $Q<0$ | $\Delta m>0$ (aumenta) | $\Delta E<0$ (diminui) |

### Representação Abreviada de Reações Nucleares
A reação nuclear na equação ($\ref{nuclear_reaction}$) pode ser representada de forma abreviada como:

$$ a(b, c)d $$

Isso significa uma reação nuclear onde $b$ incide sobre $a$, emitindo $c$ e transformando-se em $d$.

#### ex)
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Energia de Ligação (Binding Energy)
### Defeito de Massa (Mass Defect)
A massa de todos os núcleos é ligeiramente menor que a soma das massas dos nêutrons e prótons que o compõem. Esta diferença é chamada de *defeito de massa (mass defect)*.

Se a massa do núcleo for $M_A$, o defeito de massa $\Delta$ de qualquer núcleo pode ser calculado como:

$$ \Delta = ZM_p + NM_n - M_A. $$

Quando o defeito de massa $\Delta$ é expresso em unidades de energia, representa a energia necessária para separar um núcleo em seus nucleons constituintes. Como é a energia que mantém os nucleons unidos, é chamada de *energia de ligação (binding energy)*. Inversamente, quando um núcleo atômico é formado a partir de A nucleons, o nível de energia diminui em $\Delta$, então essa quantidade de energia é liberada para o ambiente durante o processo de reação nuclear.

### Energia de Ligação Média por Nucleon
A energia de ligação total de um núcleo atômico aumenta com o aumento do número de massa $A$, mas a inclinação não é constante.  
![a energia de ligação média por nucleon para um número variado de nêutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
Como pode ser visto na imagem acima, a energia de ligação média por nucleon $\Delta/A$ aumenta acentuadamente para números de massa baixos, mas diminui com uma inclinação suave para núcleos atômicos pesados com $A\geq56$.

### Relação entre o Valor Q da Reação Nuclear e a Energia de Ligação
Na reação nuclear da equação ($\ref{nuclear_reaction}$), a energia de ligação do núcleo $a$ é

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

e a massa de $a$ é

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Da mesma forma, para os núcleos $b$, $c$, e $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Considerando que

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

e substituindo estas equações na equação ($\ref{Q_value}$), obtemos

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Isso significa que sempre que dois núcleos menos estáveis se combinam para formar um núcleo mais estável através de um processo de reação nuclear, energia é liberada.

### Fusão Nuclear (Nuclear Fusion) e Fissão Nuclear (Nuclear Fission)
No caso de uma reação nuclear onde o deutério, com energia de ligação de $2.23\text{MeV}$, e o trítio, com energia de ligação de $8.48\text{MeV}$, se combinam para produzir $^4\text{He}$ com energia de ligação de $28.3\text{MeV}$ e emitem um nêutron:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

A diferença na energia de ligação antes e depois da reação, $28.3-(2.23+8.48)=17.6\text{MeV}$ de energia (3.52MeV por nucleon), é liberada na forma de energia cinética do núcleo de hélio e do nêutron.

Reações como a equação ($\ref{nuclear_fusion}$), onde dois núcleos atômicos leves se combinam para formar um núcleo atômico mais pesado do que antes da reação, são chamadas de *fusão nuclear (nuclear fusion)*. Esta é a fonte de energia de todas as estrelas, incluindo o Sol, e um dia poderá ser utilizada diretamente pela humanidade como fonte de energia.

Por outro lado, em uma reação nuclear onde $^{235}\text{U}$, com energia de ligação de aproximadamente $1780\text{MeV}$, absorve um nêutron e então se divide em $^{92}\text{Kr}$ com energia de ligação de $783\text{MeV}$ e $^{141}\text{Ba}$ com aproximadamente $1170\text{MeV}$, emitindo 3 nêutrons:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

A diferença na energia de ligação antes e depois da reação, $783+1170-1780=173\text{MeV}$ de energia (0.733MeV por nucleon), é liberada.

Reações como a equação ($\ref{nuclear_fission}$), onde um núcleo atômico pesado se divide em núcleos atômicos mais leves, são chamadas de *fissão nuclear (nuclear fission)*. Desde o discurso "Átomos para a Paz" (Atoms for Peace) do 34º presidente dos EUA, Dwight D. Eisenhower, e a usina nuclear de Obninsk na União Soviética, a fissão nuclear tem sido amplamente utilizada como fonte de energia elétrica.
