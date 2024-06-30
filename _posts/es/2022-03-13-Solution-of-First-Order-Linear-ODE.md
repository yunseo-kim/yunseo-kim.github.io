---
title: "Solución de ecuaciones diferenciales lineales de primer orden"
description: >-
  Veamos cómo resolver ecuaciones diferenciales lineales de primer orden.
categories: [Matemáticas, Ecuación Diferencial]
tags: [EDO, EDOs de Primer Orden]
math: true
---

## Ecuación diferencial lineal de primer orden
Si una ecuación diferencial de primer orden se puede llevar algebraicamente a la forma

$$ y'+p(x)y=r(x) \tag{1} $$

se dice que es **lineal**, y si no, se dice que es **no lineal**.

La forma de la ecuación (1) se llama **forma estándar** de una ecuación diferencial lineal de primer orden, y si el primer término de una ecuación diferencial lineal de primer orden dada es $f(x)y'$, se puede obtener la forma estándar dividiendo ambos lados de la ecuación por $f(x)$.

En ingeniería, a menudo se llama a $r(x)$ **entrada (input)**, y a $y(x)$ **salida (output)** o **respuesta (response)** a la entrada (y las condiciones iniciales).

## Ecuación diferencial lineal homogénea
Sea $J$ el intervalo $a<x<b$ en el que queremos resolver la ecuación (1). Si $r(x)\equiv 0$ para el intervalo $J$ en la ecuación (1), entonces

$$ y'+p(x)y=0 \tag{2}$$

y esto se llama **homogénea**. En este caso, podemos usar el [método de separación de variables](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Cuando $c=0$, obtenemos la **solución trivial** $y(x)=0$.

## Ecuación diferencial lineal no homogénea
Si $r(x)\not\equiv 0$ en el intervalo $J$, se dice que es **no homogénea**. Se sabe que la ecuación diferencial lineal no homogénea (1) tiene un factor integrante que depende solo de $x$. Este factor integrante $F(x)$ se puede encontrar usando la ecuación (11) del [método para encontrar el factor integrante](/posts/Exact-Differential-Equation-and-Integrating-Factor/#método-para-encontrar-el-factor-integrante), o se puede encontrar directamente de la siguiente manera.

Multiplicando la ecuación (1) por $F(x)$, obtenemos

$$ Fy'+pFy=rF \tag{1*} $$

Si

$$ pF=F' $$

entonces el lado izquierdo de la ecuación (1*) se convierte en la derivada $(Fy)'=F'y+Fy'$. Separando variables en $pF=F'$, tenemos $dF/F=p\ dx$, y al integrar y escribir $h=\int p\ dx$, obtenemos

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Sustituyendo en la ecuación (1*), tenemos

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrando, obtenemos

$$ e^hy=\int e^hr\ dx + c $$
y dividiendo por $e^h$, obtenemos la fórmula de solución deseada.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Aquí, la constante de integración en $h$ no es un problema.

En la ecuación (4), el único valor que depende de la condición inicial dada es $c$, por lo que si escribimos la ecuación (4) como la suma de dos términos

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

podemos ver que:

$$ \text{Salida total}=\text{Respuesta a la entrada }r+\text{Respuesta a la condición inicial} \tag{5} $$

## Ejemplo: Circuito RL
Supongamos que un circuito $RL$ está compuesto por una batería con fuerza electromotriz $E=48\textrm{V}$, una resistencia $R=11\mathrm{\Omega}$, y un inductor $L=0.1\text{H}$, y que la corriente inicial es 0. Construye el modelo de este circuito $RL$ y resuelve la ecuación diferencial resultante para la corriente $I(t)$.
> **Ley de Ohm**  
> La corriente $I$ en el circuito causa una caída de tensión $RI$ en los terminales de la resistencia.
{: .prompt-info }

> **Ley de inducción electromagnética de Faraday**  
> La corriente $I$ en el circuito causa una caída de tensión $LI'=L\ dI/dt$ en los terminales del inductor.
{: .prompt-info }

> **Ley de voltajes de Kirchhoff (KVL)**  
> La fuerza electromotriz aplicada a un circuito cerrado es igual a la suma de las caídas de tensión en todos los demás elementos del circuito.
{: .prompt-info }

### Solución
Según estas leyes, el modelo del circuito $RL$ es $LI'+RI=E(t)$, y en forma estándar es

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

Podemos resolver esta ecuación diferencial lineal usando la ecuación (4) con $x=t, y=I, p=R/L, h=(R/L)t$.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Aquí, $R/L=11/0.1=110$ y $E(t)=48$, por lo que

$$ I=\frac{48}{11}+ce^{-110t} $$

De la condición inicial $I(0)=0$, obtenemos $I(0)=E/R+c=0$, $c=-E/R$. A partir de esto, podemos obtener la siguiente solución particular:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$