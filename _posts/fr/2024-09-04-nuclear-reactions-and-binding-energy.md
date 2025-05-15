---
title: Réactions nucléaires et énergie de liaison
description: Découvrez les expressions des réactions nucléaires, la définition de la valeur Q (Q-value), ainsi que les concepts de défaut de masse (mass defect) et d'énergie de liaison (binding energy).
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Réaction nucléaire (Nuclear Reaction)
### Lois fondamentales dans les réactions nucléaires
*Réaction nucléaire* : réaction où deux noyaux atomiques différents, ou un noyau atomique et un nucléon, entrent en collision pour produire deux ou plusieurs nouvelles particules nucléaires ou des rayons gamma

Lorsque deux noyaux atomiques $a$ et $b$ réagissent pour produire des noyaux atomiques ou des rayons gamma $c$ et $d$, cette réaction s'exprime comme suit :

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

Dans les réactions nucléaires, quatre lois fondamentales s'appliquent :

- *Conservation du nombre de nucléons* : le nombre total de nucléons reste identique avant et après la réaction. Le type de nucléons peut changer, donc les protons et neutrons ne sont pas conservés individuellement.
- *Conservation de la charge* : la somme des charges des particules reste identique avant et après la réaction.
- *Conservation de la quantité de mouvement* : la somme des quantités de mouvement des particules reste identique avant et après la réaction.
- *Conservation de l'énergie* : l'énergie totale, <u>y compris l'énergie de masse au repos</u>, reste identique avant et après la réaction.

### Réaction exothermique & réaction endothermique
Dans la réaction nucléaire de l'équation ($\ref{nuclear_reaction}$), l'énergie totale avant la réaction est la somme des énergies de masse au repos et des énergies cinétiques de $a$ et $b$, et l'énergie totale après la réaction est la somme des énergies de masse au repos et des énergies cinétiques de $c$ et $d$. Selon la loi de conservation de l'énergie :

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

En réarrangeant cette équation, on obtient :

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Cela signifie que la différence d'énergie cinétique avant et après la réaction nucléaire est égale à la différence de masse au repos.
Le terme de droite de la dernière équation est appelé *valeur Q* de la réaction nucléaire et se définit comme suit :

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

La valeur Q est toujours exprimée en MeV. Comme l'énergie de masse au repos pour 1 amu est généralement de 931 MeV, la valeur Q peut également s'écrire :

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Réaction exothermique* : réaction nucléaire où $Q>0$, une partie de la masse est convertie en énergie cinétique, augmentant l'énergie cinétique après la réaction
- *Réaction endothermique* : réaction nucléaire où $Q<0$, une partie de l'énergie cinétique est convertie en masse, diminuant l'énergie cinétique après la réaction

| Type de réaction nucléaire | Valeur Q | Changement de <br>masse avant/après | Changement d'énergie <br>cinétique avant/après |
| :---: | :---: | :---: | :---: |
| Réaction exothermique | $Q>0$ | $\Delta m<0$ (diminution) | $\Delta E>0$ (augmentation) |
| Réaction endothermique | $Q<0$ | $\Delta m>0$ (augmentation) | $\Delta E<0$ (diminution) |

### Notation abrégée des réactions nucléaires
La réaction nucléaire de l'équation ($\ref{nuclear_reaction}$) peut être exprimée de façon abrégée comme suit :

$$ a(b, c)d $$

Cela signifie que $b$ entre en collision avec $a$, émettant $c$ et transformant $a$ en $d$.

#### Exemples :
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Énergie de liaison (Binding Energy)
### Défaut de masse (Mass Defect)
La masse de tout noyau est légèrement inférieure à la somme des masses des neutrons et protons qui le composent. Cette différence est appelée *défaut de masse*.

Si la masse du noyau est $M_A$, le défaut de masse $\Delta$ pour n'importe quel noyau peut être calculé comme suit :

$$ \Delta = ZM_p + NM_n - M_A. $$

Le défaut de masse $\Delta$ exprimé en unités d'énergie représente l'énergie nécessaire pour décomposer un noyau en ses nucléons constitutifs. On l'appelle *énergie de liaison* car c'est l'énergie qui maintient les nucléons ensemble. Inversement, lorsqu'un noyau atomique est formé à partir de A nucléons, le niveau d'énergie diminue de l'énergie de liaison $\Delta$, libérant cette quantité d'énergie dans l'environnement pendant le processus de réaction nucléaire.

### Énergie de liaison moyenne par nucléon
L'énergie de liaison totale d'un noyau atomique augmente avec le nombre de masse $A$, mais pas de façon linéaire.  
![l'énergie de liaison moyenne par nucléon pour un nombre varié de neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
L'énergie de liaison moyenne par nucléon $\Delta/A$ augmente rapidement pour les faibles nombres de masse, mais diminue progressivement pour les noyaux lourds avec $A\geq56$, comme on peut le voir sur l'image ci-dessus.

### Relation entre la valeur Q et l'énergie de liaison
Dans la réaction nucléaire de l'équation ($\ref{nuclear_reaction}$), l'énergie de liaison du noyau $a$ est :

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

et la masse de $a$ est :

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

De même, pour les noyaux $b$, $c$ et $d$ :

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

En considérant que :

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

et en substituant ces expressions dans l'équation ($\ref{Q_value}$), on obtient :

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Cela signifie que lorsque deux noyaux moins stables se combinent pour former un noyau plus stable par un processus de réaction nucléaire, de l'énergie est toujours libérée.

### Fusion nucléaire et Fission nucléaire
Dans le cas d'une réaction nucléaire où le deutérium, avec une énergie de liaison de $2,23\text{MeV}$, et le tritium, avec une énergie de liaison de $8,48\text{MeV}$, se combinent pour produire de l'hélium-4 avec une énergie de liaison de $28,3\text{MeV}$ et libérer un neutron :

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

La différence d'énergie de liaison avant et après la réaction, soit $28,3-(2,23+8,48)=17,6\text{MeV}$ (soit $3,52\text{MeV}$ par nucléon), est libérée sous forme d'énergie cinétique du noyau d'hélium et du neutron.

La réaction décrite dans l'équation ($\ref{nuclear_fusion}$), où deux noyaux légers se combinent pour former un noyau plus lourd, est appelée *fusion nucléaire*. C'est la source d'énergie du Soleil et de toutes les étoiles, et pourrait un jour être utilisée directement comme source d'énergie par l'humanité.

D'autre part, dans une réaction où l'uranium-235, avec une énergie de liaison d'environ $1780\text{MeV}$, absorbe un neutron puis se divise en krypton-92 (énergie de liaison de $783\text{MeV}$) et baryum-141 (énergie de liaison d'environ $1170\text{MeV}$), tout en libérant trois neutrons :

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

La différence d'énergie de liaison avant et après la réaction, soit $783+1170-1780=173\text{MeV}$ (soit $0,733\text{MeV}$ par nucléon), est libérée.

La réaction décrite dans l'équation ($\ref{nuclear_fission}$), où un noyau lourd se divise en noyaux plus légers, est appelée *fission nucléaire*. Depuis le discours "Atoms for Peace" (Les atomes pour la paix) du 34e président américain Eisenhower et la centrale nucléaire d'Obninsk en Union soviétique, cette réaction est largement utilisée comme source d'énergie électrique.

## Nombres magiques
Lorsqu'un noyau contient 2, 6, 8, 14, 20, 28, 50, 82 ou 126 neutrons ou protons, il tend à être particulièrement stable. Ces nombres de nucléons sont appelés *nombres magiques*. Ils correspondent au nombre de neutrons et de protons nécessaires pour remplir les couches nucléaires, de façon similaire au remplissage des couches électroniques autour de l'atome.

Les isotopes correspondant aux nombres magiques ont des applications pratiques en génie nucléaire. Un exemple notable est le zirconium-90 ($^{90}_{40} \mathrm{Zr}$), qui possède 50 neutrons. Sa stabilité et sa faible capacité d'absorption des neutrons en font un matériau largement utilisé pour le gainage des barres de combustible dans les cœurs de réacteurs nucléaires.
