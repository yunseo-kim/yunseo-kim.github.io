---
title: "Řešení lineární obyčejné diferenciální rovnice 1. řádu"
description: "Podívejme se na metodu řešení lineárních obyčejných diferenciálních rovnic 1. řádu."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Lineární obyčejná diferenciální rovnice 1. řádu

Pokud lze ODR 1. řádu algebraicky převést do tvaru

$$ y'+p(x)y=r(x) \tag{1} $$

pak ji nazýváme **lineární (linear)**; pokud to možné není, jde o **nelineární (nonlinear)** rovnici.

Tvar jako v (1) se nazývá **standardní tvar (standard form)** lineární ODR 1. řádu. Pokud je první člen dané lineární ODR 1. řádu ve tvaru $f(x)y'$, lze standardní tvar získat tak, že obě strany rovnice vydělíme $f(x)$.

V inženýrství se často $r(x)$ označuje jako **vstup (input)** a $y(x)$ jako **výstup (output)**, případně jako **odezva (response)** na vstup (a počáteční podmínky).

## Homogenní lineární ODR

Nechť $J$ je interval $a<x<b$, na němž chceme řešit rovnici (1). Pokud pro interval $J$ platí $r(x)\equiv 0$, pak

$$ y'+p(x)y=0 \tag{2}$$

a takovou rovnici nazýváme **homogenní (homogeneous)**. V tomto případě lze použít [metodu separace proměnných](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

Pro $c=0$ dostaneme **triviální řešení (trivial solution)** $y(x)=0$.

## Nehomogenní lineární ODR

Pokud na intervalu $J$ platí $r(x)\not\equiv 0$, nazývá se rovnice **nehomogenní (nonhomogeneous)**. Je známo, že nehomogenní lineární ODR (1) má integrační faktor závislý pouze na $x$. Tento integrační faktor $F(x)$ lze získat buď ze vzorce (11) v části [jak najít integrační faktor](/posts/Exact-Differential-Equation-and-Integrating-Factor/#jak-najit-integracni-faktor), nebo přímo následovně.

Vynásobíme-li rovnici (1) výrazem $F(x)$, dostaneme

$$ Fy'+pFy=rF \tag{1*} $$

Pokud platí

$$ pF=F' $$

pak levá strana (1*) je derivací $(Fy)'=F'y+Fy'$. Po separaci proměnných z $pF=F'$ dostaneme $dF/F=p\ dx$ a po integraci, značíme-li $h=\int p\ dx$, platí

$$ \log |F|=h=\inf p\ dx $$

$$ F = e^h $$

Po dosazení do (1*) dostaneme

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrací vyjde

$$ e^hy=\int e^hr\ dx + c $$
a po vydělení $e^h$ získáme hledaný vzorec pro řešení.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Zde integrační konstanta v $h$ nepředstavuje problém.

Protože v (4) je jedinou hodnotou jednoznačně závislou na dané počáteční podmínce konstanta $c$, můžeme (4) zapsat jako součet dvou členů

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

a vyplývá z toho

$$ \text{celkový výstup}=\text{odezva na vstup }r+\text{odezva na počáteční podmínky} \tag{5} $$

## Příklad: obvod RL

Uvažujme obvod $RL$ složený z baterie s elektromotorickým napětím $E=48\textrm{V}$, rezistoru s odporem $R=11\mathrm{\Omega}$ a induktoru s indukčností $L=0.1\text{H}$. Nechť počáteční proud je 0. Sestavte model tohoto obvodu $RL$ a vzniklou ODR vyřešte pro proud $I(t)$.
> **Ohmův zákon (Ohm's law)**  
> Proud v obvodu $I$ způsobuje na rezistoru úbytek napětí (voltage drop) $RI$.
{: .prompt-info }

> **Faradayův zákon elektromagnetické indukce (Faraday's law of electromagnetic induction)**  
> Proud v obvodu $I$ způsobuje na induktoru úbytek napětí $LI'=L\ dI/dt$.
{: .prompt-info }

> **Kirchhoffův zákon napětí (Kirchhoff's Voltage Law;KVL)**  
> Elektromotorické napětí působící v uzavřeném obvodu se rovná součtu úbytků napětí na všech ostatních prvcích obvodu.
{: .prompt-info }

### Řešení

Podle výše uvedených zákonů je model obvodu $RL$ dán rovnicí $LI'+RI=E(t)$ a ve standardním tvaru

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

V rovnici (4) položíme $x=t, y=I, p=R/L, h=(R/L)t$ a tuto lineární ODR vyřešíme.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Zde $R/L=11/0.1=110$ a $E(t)=48$, takže

$$ I=\frac{48}{11}+ce^{-110t} $$

Z počáteční podmínky $I(0)=0$ dostaneme $I(0)=E/R+c=0$, tedy $c=-E/R$. Odtud získáme následující partikulární řešení.

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
