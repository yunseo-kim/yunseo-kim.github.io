---
title: "Résolution des EDOs linéaires du premier ordre"
description: "Découvrez la méthode de résolution des équations différentielles ordinaires (EDO) linéaires du premier ordre, y compris les cas homogènes et non homogènes, avec un exemple d'application sur un circuit RL."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Équation différentielle linéaire du premier ordre
Si une équation différentielle du premier ordre peut être mise sous la forme algébrique

$$ y'+p(x)y=r(x) \tag{1} $$

on dit qu'elle est **linéaire**, sinon elle est **non linéaire**.

La forme de l'équation (1) est appelée **forme standard** d'une équation différentielle linéaire du premier ordre. Si le premier terme d'une EDO linéaire du premier ordre donnée est $f(x)y'$, on peut obtenir la forme standard en divisant les deux côtés de l'équation par $f(x)$.

En ingénierie, $r(x)$ est souvent appelé **entrée (input)**, $y(x)$ est appelé **sortie (output)** ou **réponse (response)** à l'entrée (et aux conditions initiales).

## Équation différentielle linéaire homogène
Soit $J$ l'intervalle $a<x<b$ sur lequel nous cherchons à résoudre l'équation (1). Si $r(x)\equiv 0$ sur l'intervalle $J$ dans l'équation (1), alors

$$ y'+p(x)y=0 \tag{2}$$

et on dit que l'équation est **homogène**. Dans ce cas, on peut utiliser la [méthode de séparation des variables](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Lorsque $c=0$, on obtient la **solution triviale** $y(x)=0$.

## Équation différentielle linéaire non homogène
Si $r(x)\not\equiv 0$ sur l'intervalle $J$, on dit que l'équation est **non homogène**. Il est connu que l'équation différentielle linéaire non homogène (1) a un facteur intégrant qui ne dépend que de $x$. Ce facteur intégrant $F(x)$ peut être trouvé en utilisant [la méthode pour trouver le facteur intégrant](/posts/Exact-Differential-Equation-and-Integrating-Factor/#méthode-pour-trouver-le-facteur-intégrant) de l'équation (11), ou directement comme suit.

En multipliant l'équation (1) par $F(x)$, on obtient

$$ Fy'+pFy=rF \tag{1*} $$

Si

$$ pF=F' $$

alors le côté gauche de l'équation (1*) devient la dérivée $(Fy)'=F'y+Fy'$. En séparant les variables dans $pF=F'$, on obtient $dF/F=p\ dx$, et en intégrant et en écrivant $h=\int p\ dx$, on a

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

En substituant dans l'équation (1*), on obtient

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

En intégrant, on obtient

$$ e^hy=\int e^hr\ dx + c $$
et en divisant par $e^h$, on obtient la formule de solution souhaitée.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Ici, la constante d'intégration dans $h$ n'est pas un problème.

Dans l'équation (4), la seule valeur qui dépend de la condition initiale donnée est $c$, donc si on écrit l'équation (4) comme la somme de deux termes

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

on peut voir que

$$ \text{Sortie totale}=\text{Réponse à l'entrée }r+\text{Réponse à la condition initiale} \tag{5} $$

## Exemple : Circuit RL
Supposons qu'un circuit RL soit composé d'une batterie avec une force électromotrice $E=48\textrm{V}$, une résistance $R=11\mathrm{\Omega}$, et une inductance $L=0.1\text{H}$, et que le courant initial soit 0. Trouvez le modèle de ce circuit RL et résolvez l'équation différentielle résultante pour le courant $I(t)$.
> **Loi d'Ohm**  
> Le courant $I$ dans le circuit provoque une chute de tension $RI$ aux bornes de la résistance.
{: .prompt-info }

> **Loi de Faraday sur l'induction électromagnétique**  
> Le courant $I$ dans le circuit provoque une chute de tension $LI'=L\ dI/dt$ aux bornes de l'inductance.
{: .prompt-info }

> **Loi des mailles de Kirchhoff (KVL)**  
> La force électromotrice appliquée à un circuit fermé est égale à la somme des chutes de tension aux bornes de tous les autres éléments du circuit.
{: .prompt-info }

### Solution
Selon ces lois, le modèle du circuit RL est $LI'+RI=E(t)$, et sous forme standard

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Dans l'équation (4), en posant $x=t, y=I, p=R/L, h=(R/L)t$, on peut résoudre cette équation différentielle linéaire.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Ici, $R/L=11/0.1=110$ et $E(t)=48$, donc

$$ I=\frac{48}{11}+ce^{-110t} $$

De la condition initiale $I(0)=0$, on obtient $I(0)=E/R+c=0$, $c=-E/R$. À partir de cela, on peut trouver la solution particulière suivante.

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
