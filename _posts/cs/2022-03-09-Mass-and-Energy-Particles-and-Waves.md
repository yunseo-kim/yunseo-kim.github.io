---
title: "Hmotnost a energie, částice a vlny"
description: "Prozkoumejme princip ekvivalence hmotnosti a energie ve speciální relativitě a spočítejme energii pohybujícího se elektronu se zohledněním relativistických efektů."
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---

## Princip ekvivalence hmotnosti a energie

Hmotnost a energie jsou si navzájem ekvivalentní a lze je vzájemně přeměňovat.

$$ E=mc^2 $$

Zde je $c$ rychlost světla $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Elektronvolt (Electron Volt, eV)

*Elektronvolt (electron volt, eV)*: kinetická energie, kterou získá jeden elektron při průchodu napětím 1 V

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Hmotnost a energie pohybujícího se tělesa

Podle teorie relativity se z pohledu pozorovatele hmotnost pohybujícího se tělesa relativně zvětšuje a vztah mezi rychlostí a hmotností pohybujícího se tělesa je definován následovně.

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: klidová hmotnost, $v$: rychlost

*Celková energie (total energy)* částice je součtem *klidové hmotnostní energie (rest-mass energy)* a *kinetické energie (kinetic energy)*, takže platí

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

Zejména pro $v\ll c$ položíme $\cfrac{v^2}{c^2} = \epsilon$ a aproximujeme Taylorovým rozvojem v okolí $\epsilon = 0$ (tj. Maclaurinovým rozvojem):

$$
\begin{align*}
E_{\text{kinetic}} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

což se shoduje se vzorcem pro kinetickou energii v klasické mechanice. Prakticky platí, že pokud $v\leq 0.2c$ nebo $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$, považuje se $v\ll c$ za splněné a použití této aproximace (tj. zanedbání relativistických efektů) poskytuje dostatečně přesnou hodnotu.

### Elektron

Protože klidová hmotnostní energie elektronu je $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$, je třeba použít relativistický vzorec pro kinetickou energii, pokud kinetická energie elektronu překročí $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$. V jaderném inženýrství jsou energie elektronů, se kterými se pracuje, v mnoha případech vyšší než 10 keV, takže je ve většině případů nutné použít rovnici (2).

### Neutron

Klidová hmotnostní energie neutronu dosahuje přibližně 1000 MeV, takže $0.02E_{rest}=20\text{MeV}$. Situace, kdy se v jaderném inženýrství řeší neutrony s kinetickou energií vyšší než 20 MeV, jsou vzácné, proto se pro výpočet kinetické energie neutronu obvykle používá rovnice (3).

### Foton

Rovnice (2) a (3) jsou platné pouze tehdy, když klidová hmotnost není nulová, proto je nelze použít pro foton, jehož klidová hmotnost je 0. Celková energie fotonu se určí podle vztahu

$$ E = h\nu \tag{4} $$

$h$: Planckova konstanta ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: frekvence elektromagnetické vlny

## Hmotnostní vlny

Veškerá hmota v přírodě je zároveň částicí i vlnou. To znamená, že všechny částice mají odpovídající vlnovou délku (*de Broglieho vlnová délka, de Broglie wavelength*). Vlnová délka $\lambda$ je funkcí hybnosti $p$ a Planckovy konstanty $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Hybnost $p$ je dále definována vztahem

$$ p = mv \tag{6} $$

### Pokud zanedbáme relativistické efekty (např. neutron)

Protože kinetická energie je $E=1/2 mv^2$, vyjádříme rovnici (6) jako funkci energie následovně:

$$ p=\sqrt{2mE} \tag{7} $$

Po dosazení do rovnice (5) dostaneme pro vlnovou délku částice

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

V jaderném inženýrství se tento vztah používá při určování de Broglieho vlnové délky neutronu. Po dosazení klidové hmotnosti neutronu lze psát

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

kde jednotkou $\lambda$ je cm a $E$ je kinetická energie neutronu vyjádřená v eV.

### Pokud zohledníme relativistické efekty (např. elektron)

Hybnost $p$ spočítáme přímým řešením předchozích relativistických vztahů:

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{rest}}} \tag{10}$$

Potom je de Broglieho vlnová délka

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{rest}}}} \tag{11} $$

### Částice s nulovou klidovou hmotností (např. foton)

Protože hybnost částice s nulovou klidovou hmotností nelze určit pomocí rovnice (6), vyjádříme ji jako

$$ p=\frac {E}{c} \tag{12} $$

Dosazením rovnice (12) do rovnice (5) dostaneme

$$ \lambda = \frac {hc}{E} \tag{13}$$

Po dosazení hodnot $h$ a $c$ dostaneme výsledný vztah pro vlnovou délku

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

kde jednotkou $\lambda$ je m a jednotkou $E$ je eV.
