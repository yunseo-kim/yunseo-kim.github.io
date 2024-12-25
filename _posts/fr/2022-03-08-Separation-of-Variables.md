---
title: Séparation des variables (Separation of Variables)
description: Nous explorons la méthode de séparation des variables et présentons quelques
  exemples connexes.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## Séparation des variables (Separation of Variables)
**Équation séparable (separable equation)** : Une équation qui peut être mise sous la forme $g(y)y'=f(x)$ par manipulation algébrique.

En intégrant les deux côtés de l'équation séparable $g(y)y'=f(x)$ par rapport à $x$, on obtient :

$$ \int g(y)y'dx = \int f(x)dx + c $$

Et comme $y'dx=dy$, on a :

$$ \int g(y)dy = \int f(x)dx + c $$

Ainsi, on peut séparer l'expression en $x$ et l'expression en $y$ respectivement dans le membre de droite et le membre de gauche. Si $f$ et $g$ sont des fonctions continues, on peut calculer ces intégrales pour obtenir la solution générale de l'équation différentielle donnée. Cette méthode de résolution est appelée **méthode de séparation des variables (separation of variables)**.

## Exemple de modélisation : Datation par le carbone radioactif (Radiocarbon Dating)
Ötzi est une momie néolithique découverte dans les Alpes de l'Ötztal en 1991. Si le rapport du carbone-14 au carbone-12 dans cette momie est de 52,5% de celui d'un organisme vivant, quand Ötzi a-t-il vécu et est-il mort approximativement ?
> Le rapport du carbone-14 radioactif au carbone-12 est constant dans l'atmosphère et dans les organismes vivants. Lorsqu'un organisme meurt, l'absorption de carbone-14 par la respiration et l'alimentation cesse, mais la désintégration du carbone-14 continue, ce qui entraîne une diminution du rapport de carbone radioactif. Ainsi, on peut estimer l'âge d'un fossile en comparant son rapport de carbone radioactif à celui de l'atmosphère. La demi-vie du carbone-14 est de 5715 ans.
{: .prompt-info }

### Solution
En séparant les variables de l'équation différentielle ordinaire $y'=ky$ et en intégrant, on obtient :

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Pour déterminer la constante $k$, on utilise la demi-vie $H=5715$ :

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Enfin, pour trouver le temps $t$ depuis la mort d'Ötzi, on substitue le rapport de 52,5% :

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{Il y a environ 5300 ans}. $$

## Exemple de modélisation : Problème de mélange
Initialement, un réservoir contient 1000L d'eau dans laquelle 10kg de sel sont dissous. Une solution saline contenant 0,2kg de sel par litre entre dans le réservoir à un débit de 10L par minute. La solution dans le réservoir est bien mélangée et maintenue homogène, et cette solution saline sort du réservoir à un débit de 10L par minute. Trouvez la quantité de sel $y(t)$ dans le réservoir au temps $t$.

### 1. Établissement du modèle

$$ y'=\text{taux d'entrée} - \text{taux de sortie}. $$

Le taux d'entrée du sel est de 2kg par minute. Le taux de sortie de la solution saline est de 0,01 du volume total de la solution saline par minute, donc le taux de sortie du sel est de $0.01 y(t)$ par minute. Par conséquent, le modèle est l'équation différentielle ordinaire :

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Résolution du modèle
L'équation différentielle ordinaire établie précédemment est séparable. Séparons les variables, intégrons, puis prenons l'exponentielle des deux côtés :

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Initialement, la quantité de sel dans le réservoir est de 10kg, donc la condition initiale est $y(0)=10$. En substituant $y=10,\ t=0$ dans l'équation ci-dessus, on obtient $10-200=ce^0=c$, donc $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Ainsi, dans la situation donnée, on peut voir que la quantité de sel dans le réservoir converge exponentiellement vers 200kg.

## Exemple de modélisation : Loi de refroidissement de Newton (Newton's Law of Cooling)
En hiver, la température diurne d'un immeuble de bureaux est maintenue à 20°C. Le chauffage est éteint à 22h et rallumé à 6h du matin. Un jour, à 2h du matin, la température intérieure du bâtiment était de 17,4°C. La température extérieure était de 10°C à 22h et est tombée à 4°C à 6h du matin. Quelle était la température intérieure du bâtiment à 6h du matin lorsque le chauffage a été rallumé ?
> **Loi de refroidissement de Newton (Newton's law of cooling)**  
> Le taux de variation de la température T d'un objet par rapport au temps est proportionnel à la différence de température entre l'objet et son environnement.
{: .prompt-info }

### 1. Établissement du modèle
Soit $T(t)$ la température intérieure du bâtiment et $T_A$ la température extérieure. Alors, selon la loi de refroidissement de Newton :

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Solution générale
Comme nous ne savons pas exactement quelle valeur prend $T_A$ entre 10°C et 4°C, nous ne pouvons pas résoudre l'équation établie précédemment. Dans ce cas, *il peut être utile de simplifier la situation en la réduisant à un problème plus simple*. La moyenne des deux valeurs connues est 7°C, donc supposons que la fonction inconnue $T_A$ est une fonction constante $T_A=7$. Même si ce n'est pas exact, nous pouvons espérer obtenir une valeur approximative de la température intérieure du bâtiment $T$ à 6h du matin, que nous cherchons à déterminer.

Pour la constante $T_A=7$, l'équation différentielle ordinaire établie précédemment est séparable. En séparant les variables, en intégrant et en prenant l'exponentielle, on peut obtenir la solution générale :

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Solution particulière
Choisissons 22h comme $t=0$, alors la condition initiale donnée est $T(0)=20$. Appelons $T_p$ la solution particulière obtenue dans ce cas. En substituant :

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Détermination de $k$
À 2h du matin, la température intérieure du bâtiment était de 17,4°C, donc $T(4)=17.4$. En déterminant algébriquement la valeur de $k$ et en l'insérant dans $T_p(t)$ :

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Réponse et interprétation
6h du matin correspond à $t=8$, donc :

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[°C]}. $$

## Exemple de modélisation : Théorème de Torricelli (Torricelli's Theorem)
Un réservoir a un diamètre de 2m et un trou de 1cm de diamètre. La hauteur initiale de l'eau lorsque le trou est ouvert est de 2,25m. Trouvez la hauteur de l'eau dans le réservoir à tout moment et le temps nécessaire pour que le réservoir se vide.
> **Théorème de Torricelli (Torricelli's theorem)**  
> La vitesse de l'eau s'écoulant sous l'influence de la gravité est :
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$ : hauteur de l'eau au-dessus du trou au temps $t$
> $g=980\text{cm/s²}$ : accélération due à la gravité à la surface de la Terre
{: .prompt-info }

### 1. Établissement du modèle
Le volume $\Delta V$ écoulé pendant un court intervalle de temps $\Delta t$ est :

$$ \Delta V = Av\Delta t \qquad (A: \text{surface du trou})$$

$\Delta V$ doit être égal au changement de volume $\Delta V^*$ de l'eau dans le réservoir. De plus,

$$ \Delta V^* = -B\Delta h \qquad (B: \text{section transversale du réservoir}) $$

où $\Delta h(>0)$ est la diminution de la hauteur d'eau $h(t)$. En égalant $\Delta V$ et $\Delta V^*$, on obtient :

$$ -B\Delta h = Av\Delta t $$

Maintenant, en exprimant $v$ selon le théorème de Torricelli et en faisant tendre $\Delta t$ vers 0, on obtient le modèle exprimé sous forme d'une équation différentielle ordinaire du premier ordre :

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Solution générale
Cette équation différentielle ordinaire est séparable. En séparant les variables et en intégrant, on obtient :

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

En divisant les deux côtés par 2 et en élevant au carré, on obtient $h=(c-13.28At/B)^2$. En substituant $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$, on obtient la solution générale :

$$ h(t)=(c-0.000332t)^2 $$

### 3. Solution particulière
La condition initiale est $h(0)=225\text{cm}$. En substituant $t=0$ et $h=225$ dans la solution générale, on obtient $c^2=225, c=15.00$, et donc la solution particulière :

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Temps nécessaire pour que le réservoir se vide

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Transformation en forme séparable (separable form)
Dans certains cas, il est possible de transformer une équation différentielle ordinaire non séparable en une forme séparable en introduisant une nouvelle fonction inconnue de $y$.

$$ y'=f\left(\frac {y}{x}\right). $$

Pour résoudre une telle équation différentielle ordinaire, on pose $y/x=u$, alors :

$$ y=ux,\quad y'=u'x+u $$

En substituant dans $y'=f(y/x)$, on obtient $u'x=f(u)-u$. Si $f(u)-u\neq0$, alors :

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$

est séparable.
