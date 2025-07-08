---
title: Solución de EDOs Lineales de Primer Orden
description: Aprenda cómo resolver ecuaciones diferenciales ordinarias lineales de primer orden, tanto homogéneas como no homogéneas.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Ecuación Diferencial Ordinaria Lineal de Primer Orden
Una ecuación diferencial ordinaria de primer orden que puede escribirse algebraicamente en la forma

$$ y'+p(x)y=r(x) \tag{1} $$

se denomina **lineal**, y si no, se denomina **no lineal**.

La forma de la ecuación (1) se conoce como la **forma estándar** de una ecuación diferencial ordinaria lineal de primer orden. Si el primer término de una ecuación diferencial lineal de primer orden dada es $f(x)y'$, se puede obtener la forma estándar dividiendo ambos lados de la ecuación por $f(x)$.

En ingeniería, a menudo se denomina a $r(x)$ la **entrada (input)**, y a $y(x)$ la **salida (output)** o la **respuesta (response)** a la entrada (y a las condiciones iniciales).

## Ecuación Diferencial Ordinaria Lineal Homogénea
Sea $J$ un intervalo $a<x<b$ en el que queremos resolver la ecuación (1). Si para el intervalo $J$, $r(x)\equiv 0$ en la ecuación (1), entonces

$$ y'+p(x)y=0 \tag{2}$$

y se denomina **homogénea**. En este caso, se puede utilizar el [método de separación de variables](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Si $c=0$, se obtiene la **solución trivial** $y(x)=0$.

## Ecuación Diferencial Ordinaria Lineal No Homogénea
Si $r(x)\not\equiv 0$ en el intervalo $J$, se denomina **no homogénea**. Se sabe que la ecuación diferencial ordinaria lineal no homogénea (1) tiene un factor integrante que depende solo de $x$. Este factor integrante $F(x)$ se puede encontrar usando la ecuación (11) del [Método para Encontrar el Factor Integrante](/posts/Exact-Differential-Equation-and-Integrating-Factor/#método-para-encontrar-el-factor-integrante), o se puede derivar directamente de la siguiente manera.

Multiplicando la ecuación (1) por $F(x)$, obtenemos

$$ Fy'+pFy=rF \tag{1*} $$

Si

$$ pF=F' $$

entonces el lado izquierdo de la ecuación (1*) se convierte en la derivada $(Fy)'=F'y+Fy'$. Separando las variables en $pF=F'$, obtenemos $dF/F=p\ dx$. Integrando y escribiendo $h=\int p\ dx$, tenemos

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Sustituyendo en la ecuación (1*), obtenemos

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrando, obtenemos

$$ e^hy=\int e^hr\ dx + c $$
y dividiendo por $e^h$, obtenemos la fórmula de la solución deseada.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Aquí, la constante de integración en $h$ no es un problema.

Dado que el único valor en la ecuación (4) que depende de la condición inicial dada es $c$, si escribimos la ecuación (4) como la suma de dos términos

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

podemos ver lo siguiente:

$$ \text{Salida total}=\text{Respuesta a la entrada }r+\text{Respuesta a la condición inicial} \tag{5} $$

## Ejemplo: Circuito RL
Supongamos un circuito $RL$ compuesto por una batería con una fuerza electromotriz $E=48\textrm{V}$, una resistencia de $R=11\mathrm{\Omega}$ y un inductor de $L=0.1\text{H}$, con una corriente inicial de cero. Modele este circuito $RL$ y resuelva la ecuación diferencial ordinaria resultante para la corriente $I(t)$.
> **Ley de Ohm (Ohm's law)**  
> La corriente $I$ en un circuito causa una caída de tensión (voltage drop) $RI$ a través de la resistencia.
{: .prompt-info }

> **Ley de inducción electromagnética de Faraday (Faraday's law of electromagnetic induction)**  
> La corriente $I$ en un circuito causa una caída de tensión $LI'=L\ dI/dt$ a través del inductor.
{: .prompt-info }

> **Ley de voltaje de Kirchhoff (Kirchhoff's Voltage Law; KVL)**  
> La fuerza electromotriz aplicada a un circuito cerrado es igual a la suma de las caídas de tensión a través de todos los demás elementos del circuito.
{: .prompt-info }

### Solución
Según las leyes anteriores, el modelo para el circuito $RL$ es $LI'+RI=E(t)$, y escrito en forma estándar, es

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Podemos resolver esta ecuación diferencial ordinaria lineal estableciendo $x=t, y=I, p=R/L, h=(R/L)t$ en la ecuación (4).

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Dado que $R/L=11/0.1=110$ y $E(t)=48$, tenemos

$$ I=\frac{48}{11}+ce^{-110t} $$

A partir de la condición inicial $I(0)=0$, obtenemos $I(0)=E/R+c=0$, de donde $c=-E/R$. Con esto, podemos encontrar la siguiente solución particular.

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
