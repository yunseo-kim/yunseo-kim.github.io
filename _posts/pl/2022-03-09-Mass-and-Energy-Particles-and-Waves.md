---
title: "Masa i energia, cząstki i fale"
description: "Zbadaj zasadę równoważności masy i energii w teorii względności oraz oblicz energię poruszającego się elektronu, uwzględniając efekty relatywistyczne."
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---

## Zasada równoważności masy i energii

Masa i energia są sobie równoważne i mogą wzajemnie się przekształcać.

$$ E=mc^2 $$

Tutaj $c$ jest prędkością światła równą $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Elektronowolt (Electron Volt, eV)

*Elektronowolt (electron volt, eV)*: energia kinetyczna, jaką uzyskuje pojedynczy elektron, przechodząc przez różnicę potencjałów 1 V

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Masa i energia poruszającego się obiektu

Zgodnie z teorią względności, z punktu widzenia obserwatora masa poruszającego się obiektu relatywistycznie rośnie, a zależność między prędkością poruszającego się obiektu i jego masą definiuje się następująco:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: masa spoczynkowa, $v$: prędkość

*Energia całkowita (total energy)* cząstki jest sumą *energii masy spoczynkowej (rest-mass energy)* oraz *energii kinetycznej (kinetic energy)*, zatem zachodzi:

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

W szczególności, gdy $v\ll c$, kładąc $\cfrac{v^2}{c^2} = \epsilon$ i rozwijając w szereg Taylora (tj. w szereg Maclaurina) w pobliżu $\epsilon = 0$, otrzymujemy przybliżenie:

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

co sprowadza się do wzoru na energię kinetyczną z mechaniki klasycznej. W praktyce, gdy $v\leq 0.2c$ lub $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$, uznaje się, że $v\ll c$, i nawet stosując to przybliżenie (tj. ignorując efekty wynikające z teorii względności) otrzymuje się wystarczająco dokładne wartości.

### Elektron

Ponieważ energia masy spoczynkowej elektronu wynosi $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$, to gdy energia kinetyczna elektronu przekracza $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$, należy stosować relatywistyczny wzór na energię kinetyczną. W inżynierii jądrowej energie elektronów są w wielu przypadkach większe niż 10 keV, więc w większości należy stosować wzór (2).

### Neutron

Energia masy spoczynkowej neutronu wynosi w przybliżeniu 1000 MeV, zatem $0.02E_{rest}=20\text{MeV}$. Ponieważ w inżynierii jądrowej rzadko rozpatruje się sytuacje, w których energia kinetyczna neutronu przekracza 20 MeV, do obliczeń energii kinetycznej neutronów zwykle używa się wzoru (3).

### Foton

Wzory (2), (3) są ważne, gdy masa spoczynkowa jest różna od zera, więc nie można ich zastosować do fotonu, którego masa spoczynkowa wynosi 0. Energię całkowitą fotonu wyznacza się ze wzoru:

$$ E = h\nu \tag{4} $$

$h$: stała Plancka ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: częstotliwość fali elektromagnetycznej

## Fale materii

Wszystka materia w przyrodzie jest jednocześnie cząstką i falą. To znaczy, wszystkie cząstki mają odpowiadającą im długość fali (*długość fali de Broglie’a, de Broglie wavelength*). Długość fali $\lambda$ jest wówczas funkcją pędu $p$ i stałej Plancka $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Ponadto pęd $p$ definiuje się następująco:

$$ p = mv \tag{6} $$

### Gdy pomijamy efekty relatywistyczne (np. neutron)

Ponieważ energia kinetyczna wynosi $E=1/2 mv^2$, wyrażając wzór (6) jako funkcję energii, otrzymujemy:

$$ p=\sqrt{2mE} \tag{7} $$

Podstawiając to do (5), długość fali cząstki wynosi:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

W inżynierii jądrowej powyższy wzór stosuje się przy wyznaczaniu długości fali de Broglie’a neutronu. Po podstawieniu masy spoczynkowej neutronu można to zapisać następująco:

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Tutaj jednostką $\lambda$ jest cm, a $E$ jest energią kinetyczną neutronu wyrażoną w eV.

### Gdy uwzględniamy efekty relatywistyczne (np. elektron)

Bezpośrednio rozwiązując wcześniejsze zależności relatywistyczne, oblicza się pęd $p$.

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{rest}}} \tag{10}$$

Wówczas długość fali de Broglie’a wynosi:

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{rest}}}} \tag{11} $$

### Cząstki o masie spoczynkowej równej 0 (np. foton)

Ponieważ pędu cząstek o masie spoczynkowej równej 0 nie można wyznaczyć ze wzoru (6), zapisuje się go jako:

$$ p=\frac {E}{c} \tag{12} $$

Podstawiając (12) do (5), otrzymujemy:

$$ \lambda = \frac {hc}{E} \tag{13}$$

Po podstawieniu wartości $h$ i $c$ ostatecznie dostajemy zależność na długość fali:

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

Tutaj jednostką $\lambda$ jest m, a jednostką $E$ jest eV.
