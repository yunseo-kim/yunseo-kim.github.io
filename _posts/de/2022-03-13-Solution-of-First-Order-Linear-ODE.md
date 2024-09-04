---
title: "Lösung von linearen Differentialgleichungen erster Ordnung"
description: >-
  Lasst uns die Lösungsmethode für lineare Differentialgleichungen erster Ordnung betrachten.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
---

## Lineare Differentialgleichung erster Ordnung
Wenn eine Differentialgleichung erster Ordnung algebraisch in die Form

$$ y'+p(x)y=r(x) \tag{1} $$

gebracht werden kann, nennt man sie **linear**, andernfalls **nichtlinear**.

Die Form der Gleichung (1) wird als **Standardform** einer linearen Differentialgleichung erster Ordnung bezeichnet. Wenn der erste Term einer gegebenen linearen Differentialgleichung erster Ordnung $f(x)y'$ ist, kann man die Standardform erhalten, indem man beide Seiten der Gleichung durch $f(x)$ teilt.

In der Ingenieurwissenschaft wird $r(x)$ oft als **Eingang (input)**, $y(x)$ als **Ausgang (output)** oder **Antwort (response)** auf den Eingang (und die Anfangsbedingung) bezeichnet.

## Homogene lineare Differentialgleichung
Sei $J$ das Intervall $a<x<b$, in dem wir die Gleichung (1) lösen wollen. Wenn in Gleichung (1) $r(x)\equiv 0$ für das Intervall $J$ gilt, dann haben wir

$$ y'+p(x)y=0 \tag{2}$$

und dies wird als **homogen** bezeichnet. In diesem Fall können wir die [Methode der Trennung der Variablen](/posts/Separation-of-Variables/) anwenden.

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Für $c=0$ erhalten wir die **triviale Lösung** $y(x)=0$.

## Inhomogene lineare Differentialgleichung
Wenn $r(x)\not\equiv 0$ im Intervall $J$, nennen wir die Gleichung **inhomogen**. Es ist bekannt, dass die inhomogene lineare Differentialgleichung (1) einen Integrationsfaktor hat, der nur von $x$ abhängt. Dieser Integrationsfaktor $F(x)$ kann entweder mit der [Methode zur Bestimmung des Integrationsfaktors](/posts/Exact-Differential-Equation-and-Integrating-Factor/#methode-zur-bestimmung-des-integrierenden-faktors) aus Gleichung (11) oder direkt wie folgt bestimmt werden.

Multiplizieren wir Gleichung (1) mit $F(x)$, erhalten wir

$$ Fy'+pFy=rF \tag{1*} $$

Wenn

$$ pF=F' $$

gilt, wird die linke Seite von Gleichung (1*) zur Ableitung $(Fy)'=F'y+Fy'$. Trennen wir die Variablen in $pF=F'$, erhalten wir $dF/F=p\ dx$, und nach Integration mit $h=\int p\ dx$ haben wir

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Setzen wir dies in Gleichung (1*) ein, erhalten wir

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Nach Integration ergibt sich

$$ e^hy=\int e^hr\ dx + c $$
und durch Division durch $e^h$ erhalten wir die gewünschte Lösungsformel.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Hierbei spielt die Integrationskonstante in $h$ keine Rolle.

In Gleichung (4) ist $c$ der einzige Wert, der von der gegebenen Anfangsbedingung abhängt. Wenn wir Gleichung (4) als Summe von zwei Termen schreiben

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

können wir Folgendes erkennen:

$$ \text{Gesamtausgang}=\text{Antwort auf den Eingang }r+\text{Antwort auf die Anfangsbedingung} \tag{5} $$

## Beispiel: RL-Schaltkreis
Ein RL-Schaltkreis besteht aus einer Batterie mit einer elektromotorischen Kraft von $E=48\textrm{V}$, einem Widerstand von $R=11\mathrm{\Omega}$ und einer Induktivität von $L=0.1\text{H}$. Der anfängliche Strom ist 0. Bestimme das Modell dieses RL-Schaltkreises und löse die resultierende Differentialgleichung für den Strom $I(t)$.
> **Ohmsches Gesetz**  
> Der Strom $I$ im Schaltkreis verursacht einen Spannungsabfall $RI$ über dem Widerstand.
{: .prompt-info }

> **Faradaysches Induktionsgesetz**  
> Der Strom $I$ im Schaltkreis verursacht einen Spannungsabfall $LI'=L\ dI/dt$ über der Induktivität.
{: .prompt-info }

> **Kirchhoffsches Spannungsgesetz (KSG)**  
> Die in einem geschlossenen Schaltkreis angelegte elektromotorische Kraft ist gleich der Summe der Spannungsabfälle über allen anderen Elementen des Schaltkreises.
{: .prompt-info }

### Lösung
Nach den obigen Gesetzen ist das Modell des RL-Schaltkreises $LI'+RI=E(t)$, und in Standardform geschrieben

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Mit $x=t, y=I, p=R/L, h=(R/L)t$ in Gleichung (4) können wir diese lineare Differentialgleichung lösen.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Dabei ist $R/L=11/0.1=110$ und $E(t)=48$, also

$$ I=\frac{48}{11}+ce^{-110t} $$

Aus der Anfangsbedingung $I(0)=0$ erhalten wir $I(0)=E/R+c=0$, $c=-E/R$. Daraus können wir die folgende spezielle Lösung ableiten:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$