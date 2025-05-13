---
title: Réactions nucléaires et énergie de liaison
description: Découvrez les expressions des réactions nucléaires, la définition de
  la valeur Q (Q-value), et les concepts de défaut de masse (mass defect) et d'énergie
  de liaison (binding energy).
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Réaction nucléaire (Nuclear Reaction)
### Lois fondamentales dans les réactions nucléaires
*Réaction nucléaire (nuclear reaction)* : Une réaction où deux noyaux atomiques différents ou un noyau atomique et un nucléon entrent en collision pour produire deux ou plusieurs nouvelles particules nucléaires ou des rayons gamma.

Lorsque deux noyaux atomiques $a$ et $b$ réagissent pour produire des noyaux atomiques ou des rayons gamma $c$ et $d$, cette réaction est exprimée comme suit :

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

Dans les réactions nucléaires, quatre lois fondamentales s'appliquent :

- *Loi de conservation du nombre de nucléons (conservation of nucleon)* : Le nombre total de nucléons est le même avant et après la réaction. Le type de nucléons peut changer, donc les protons et les neutrons ne sont pas conservés individuellement.
- *Loi de conservation de la charge (conservation of charge)* : La somme totale des charges des particules est la même avant et après la réaction.
- *Loi de conservation de la quantité de mouvement (conservation of momentum)* : La somme totale des quantités de mouvement des particules est la même avant et après la réaction.
- *Loi de conservation de l'énergie (conservation of energy)* : L'énergie totale, <u>y compris l'énergie de masse au repos</u>, est la même avant et après la réaction.

### Réaction exothermique (exothermic reaction) & Réaction endothermique (endothermic reaction)
Dans la réaction nucléaire de l'équation ($\ref{nuclear_reaction}$), l'énergie totale avant la réaction est la somme des énergies de masse au repos et des énergies cinétiques de $a$ et $b$, et l'énergie totale après la réaction est la somme des énergies de masse au repos et des énergies cinétiques de $c$ et $d$. Donc, selon la loi de conservation de l'énergie, on a :

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

En réarrangeant cette équation, on obtient :

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Cela signifie que la différence d'énergie cinétique avant et après la réaction nucléaire est égale à la différence de masse au repos avant et après la réaction.
Le côté droit de la dernière équation est appelé *valeur Q (Q-value)* de la réaction nucléaire et est défini comme suit :

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

La valeur Q est toujours exprimée en MeV, et comme l'énergie de masse au repos pour 1 amu est généralement de 931 MeV, la valeur Q peut également être écrite comme suit :

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Réaction exothermique (exothermic reaction)* : Réaction nucléaire où $Q>0$, une partie de la masse est convertie en énergie cinétique, augmentant l'énergie cinétique après la réaction
- *Réaction endothermique (endothermic reaction)* : Réaction nucléaire où $Q<0$, une partie de l'énergie cinétique est convertie en masse, diminuant l'énergie cinétique après la réaction

| Type de réaction <br>nucléaire | Valeur Q | Changement de <br>masse avant et <br>après la réaction | Changement d'énergie <br>cinétique avant et <br>après la réaction |
| :---: | :---: | :---: | :---: |
| Réaction <br>exothermique | $Q>0$ | $\Delta m<0$ <br>(diminution) | $\Delta E>0$ (augmentation) |
| Réaction <br>endothermique | $Q<0$ | $\Delta m>0$ <br>(augmentation) | $\Delta E<0$ (diminution) |

### Expression simplifiée des réactions nucléaires
La réaction nucléaire de l'équation ($\ref{nuclear_reaction}$) peut être exprimée de manière simplifiée comme suit :

$$ a(b, c)d $$

Cela signifie une réaction nucléaire où $b$ est incident sur $a$, émettant $c$ et se transformant en $d$.

#### ex)
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Énergie de liaison (Binding Energy)
### Défaut de masse (Mass Defect)
La masse de tous les noyaux est légèrement inférieure à la somme des masses des neutrons et des protons qui les composent. Cette différence est appelée *défaut de masse (mass defect)*.

Si la masse du noyau est $M_A$, le défaut de masse $\Delta$ d'un noyau arbitraire peut être calculé comme suit :

$$ \Delta = ZM_p + NM_n - M_A. $$

Lorsque le défaut de masse $\Delta$ est exprimé en unités d'énergie, il représente l'énergie nécessaire pour diviser un noyau arbitraire en ses nucléons constitutifs. On l'appelle *énergie de liaison (binding energy)* car c'est l'énergie qui maintient les nucléons ensemble. Inversement, lorsqu'un noyau atomique est formé à partir de A nucléons, le niveau d'énergie diminue de l'énergie de liaison $\Delta$, donc cette quantité d'énergie est libérée dans l'environnement pendant le processus de réaction nucléaire.

### Énergie de liaison moyenne par nucléon
L'énergie de liaison totale d'un noyau atomique augmente avec le nombre de masse $A$, mais la pente n'est pas constante.  
![l'énergie de liaison moyenne par nucléon pour un nombre varié de neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
On peut voir dans l'image ci-dessus que l'énergie de liaison moyenne par nucléon $\Delta/A$ augmente rapidement pour les faibles nombres de masse, mais diminue avec une pente douce pour les noyaux atomiques lourds avec $A\geq56$.

### Relation entre la valeur Q de la réaction nucléaire et l'énergie de liaison
Dans la réaction nucléaire de l'équation ($\ref{nuclear_reaction}$), l'énergie de liaison du noyau $a$ est 

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

et la masse de $a$ est

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

De la même manière, pour les noyaux $b$, $c$, et $d$

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

En considérant que

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

et en substituant ces équations dans l'équation ($\ref{Q_value}$), on obtient

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Cela signifie que lorsque deux noyaux moins stables se combinent pour former un noyau plus stable par un processus de réaction nucléaire, de l'énergie est toujours libérée.

### Fusion nucléaire (Nuclear Fusion) et Fission nucléaire (Nuclear Fission)
Dans le cas d'une réaction nucléaire où le deutérium avec une énergie de liaison de $2,23\text{MeV}$ et le tritium avec une énergie de liaison de $8,48\text{MeV}$ se combinent pour produire $^4\text{He}$ avec une énergie de liaison de $28,3\text{MeV}$ et émettent un neutron

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

l'énergie correspondant à la différence d'énergie de liaison avant et après la réaction, soit $28,3-(2,23+8,48)=17,6\text{MeV}$ (soit $3,52\text{MeV}$ par nucléon), est libérée sous forme d'énergie cinétique du noyau d'hélium et du neutron.

Une réaction comme l'équation ($\ref{nuclear_fusion}$), où deux noyaux atomiques légers de petit nombre de masse se combinent pour former un noyau atomique lourd de plus grand nombre de masse qu'avant la réaction, est appelée *fusion nucléaire (nuclear fusion)*. C'est la source d'énergie de toutes les étoiles, y compris le Soleil, et un jour, l'humanité pourra l'utiliser directement comme source d'énergie.

D'autre part, dans le cas d'une réaction nucléaire où $^{235}\text{U}$ avec une énergie de liaison d'environ $1780\text{MeV}$ absorbe un neutron puis se sépare en $^{92}\text{Kr}$ avec une énergie de liaison de $783\text{MeV}$ et $^{141}\text{Ba}$ avec environ $1170\text{MeV}$, émettant 3 neutrons

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

l'énergie correspondant à la différence d'énergie de liaison avant et après la réaction, soit $783+1170-1780=173\text{MeV}$ (soit $0,733\text{MeV}$ par nucléon), est libérée.

Une réaction comme l'équation ($\ref{nuclear_fission}$), où un noyau atomique lourd se sépare en noyaux atomiques plus légers, est appelée *fission nucléaire (nuclear fission)*. Depuis le discours "Atomes pour la paix" (Atoms for Peace) du 34e président américain Eisenhower et la centrale nucléaire d'Obninsk en Union soviétique, elle est largement utilisée comme source d'énergie électrique.
