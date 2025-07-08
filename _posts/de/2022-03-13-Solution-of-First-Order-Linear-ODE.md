---
title: Lösung linearer GDGL erster Ordnung
description: Wir untersuchen die Lösungsmethoden für lineare gewöhnliche Differentialgleichungen erster Ordnung.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Lineare gewöhnliche Differentialgleichungen erster Ordnung
Eine gewöhnliche Differentialgleichung erster Ordnung, die algebraisch in die Form

$$ y'+p(x)y=r(x) \tag{1} $$

gebracht werden kann, wird als **linear** bezeichnet, andernfalls als **nichtlinear**.

Die Form von Gleichung (1) wird als **Standardform** einer linearen gewöhnlichen Differentialgleichung erster Ordnung bezeichnet. Wenn der erste Term einer gegebenen linearen DGL erster Ordnung $f(x)y'$ ist, kann die Standardform durch Division beider Seiten der Gleichung durch $f(x)$ erhalten werden.

In der Ingenieurwissenschaft wird $r(x)$ oft als **Eingangssignal (Input)** und $y(x)$ als **Ausgangssignal (Output)** oder als **Antwort (Response)** auf den Eingang (und die Anfangsbedingungen) bezeichnet.

## Homogene lineare gewöhnliche Differentialgleichungen
Sei $J$ ein Intervall $a<x<b$, in dem wir Gleichung (1) lösen wollen. Wenn für das Intervall $J$ in Gleichung (1) $r(x)\equiv 0$ gilt, dann haben wir

$$ y'+p(x)y=0 \tag{2}$$

und dies wird als **homogen** bezeichnet. In diesem Fall kann die [Trennung der Variablen](/posts/Separation-of-Variables/) angewendet werden.

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Für $c=0$ erhalten wir die **triviale Lösung** $y(x)=0$.

## Inhomogene lineare gewöhnliche Differentialgleichungen
Wenn im Intervall $J$ $r(x)\not\equiv 0$ gilt, wird dies als **inhomogen** bezeichnet. Es ist bekannt, dass die inhomogene lineare DGL (1) einen integrierenden Faktor besitzt, der nur von $x$ abhängt. Dieser integrierende Faktor $F(x)$ kann mit Gleichung (11) aus der [Methode zur Bestimmung des integrierenden Faktors](/posts/Exact-Differential-Equation-and-Integrating-Factor/#methode-zur-bestimmung-des-integrierenden-faktors) oder direkt wie folgt bestimmt werden.

Multipliziert man Gleichung (1) mit $F(x)$, erhält man

$$ Fy'+pFy=rF \tag{1*} $$

Wenn

$$ pF=F' $$

gilt, wird die linke Seite von Gleichung (1*) zur Ableitung $(Fy)'=F'y+Fy'$. Trennt man die Variablen in $pF=F'$, erhält man $dF/F=p\ dx$. Integriert man dies und setzt $h=\int p\ dx$, so ergibt sich

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Setzt man dies in Gleichung (1*) ein, erhält man

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Durch Integration erhält man

$$ e^hy=\int e^hr\ dx + c $$
und durch Division durch $e^h$ ergibt sich die gewünschte Lösungsformel.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Hierbei spielt die Integrationskonstante in $h$ keine Rolle.

Da in Gleichung (4) $c$ der einzige Wert ist, der von der gegebenen Anfangsbedingung abhängt, können wir, wenn wir Gleichung (4) als Summe von zwei Termen schreiben

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

Folgendes erkennen:

$$ \text{Gesamtausgang}=\text{Antwort auf Eingang }r+\text{Antwort auf Anfangsbedingung} \tag{5} $$

## Beispiel: RL-Schaltkreis
Angenommen, ein $RL$-Schaltkreis besteht aus einer Batterie mit einer elektromotorischen Kraft (EMK) von $E=48\textrm{V}$, einem Widerstand von $R=11\mathrm{\Omega}$ und einer Induktivität von $L=0.1\text{H}$. Der Anfangsstrom sei Null. Erstellen Sie das Modell für diesen $RL$-Schaltkreis und lösen Sie die resultierende gewöhnliche Differentialgleichung für den Strom $I(t)$.
> **Ohmsches Gesetz (Ohm's law)**  
> Der Strom $I$ im Schaltkreis verursacht einen Spannungsabfall $RI$ über dem Widerstand.
{: .prompt-info }

> **Faradaysches Induktionsgesetz (Faraday's law of electromagnetic induction)**  
> Der Strom $I$ im Schaltkreis verursacht einen Spannungsabfall $LI'=L\ dI/dt$ über der Induktivität.
{: .prompt-info }

> **Kirchhoffsche Maschenregel (Kirchhoff's Voltage Law; KVL)**  
> Die in einer geschlossenen Masche angelegte elektromotorische Kraft ist gleich der Summe der Spannungsabfälle über allen anderen Elementen im Kreis.
{: .prompt-info }

### Lösung
Nach den oben genannten Gesetzen lautet das Modell für den $RL$-Schaltkreis $LI'+RI=E(t)$. In Standardform geschrieben, ergibt sich:

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Diese lineare DGL kann gelöst werden, indem wir in Gleichung (4) $x=t, y=I, p=R/L, h=(R/L)t$ setzen.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Da $R/L=11/0.1=110$ und $E(t)=48$ ist, gilt:

$$ I=\frac{48}{11}+ce^{-110t} $$

Aus der Anfangsbedingung $I(0)=0$ erhalten wir $I(0)=E/R+c=0$, also $c=-E/R$. Daraus lässt sich die folgende partikuläre Lösung bestimmen:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
