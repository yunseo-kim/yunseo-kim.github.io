---
title: Ehrenfestova věta (Ehrenfest theorem)
description: Jak z vlnové funkce v kvantové mechanice spočítat střední hodnoty polohy a hybnosti, zobecnit to na Q(x,p) a odvodit Ehrenfestovu větu.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Předpoklady
- spojité rozdělení pravděpodobnosti a hustota pravděpodobnosti
- [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/)

## Výpočet střední hodnoty z vlnové funkce
### Střední hodnota polohy $x$
Střední hodnota (expectation value) polohy $x$ pro částici ve stavu $\Psi$ je

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

Platí, že když pro dostatečně velký počet částic ve stejném stavu $\Psi$ změříme polohu a zprůměrujeme výsledky, získáme $\langle x \rangle$ vypočtené výše uvedeným vztahem.

> Pozor: „střední hodnota“ zde neznamená průměr z opakovaných měření na jedné částici, ale průměr výsledků měření nad **ansámblem (ensemble)** systémů ve stejném stavu. Pokud bychom stejnou částici měřili opakovaně v krátkých časových intervalech, při prvním měření dojde ke [kolapsu vlnové funkce](/posts/schrodinger-equation-and-the-wave-function/#mereni-a-kolaps-vlnove-funkce), takže v dalších měřeních budeme stále dostávat tutéž hodnotu.
{: .prompt-warning }

### Střední hodnota hybnosti $p$
Protože $\Psi$ závisí na čase, bude se s časem měnit i $\langle x \rangle$. Pak z rovnice (8) v příspěvku [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/) a z výše uvedeného vztahu ($\ref{eqn:x_exp}$) plyne:

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> V přechodu z ($\ref{eqn:dx/dt_1}$) na ($\ref{eqn:dx/dt_2}$) a z ($\ref{eqn:dx/dt_2}$) na ($\ref{eqn:dx/dt_3}$) jsme dvakrát použili per partes; protože $\lim_{x\rightarrow\pm\infty}\Psi=0$, okrajový člen (boundary term) jsme zanedbali.
{: .prompt-tip }

Proto získáme střední hodnotu **hybnosti** následovně:

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Střední hodnota libovolné veličiny $Q(x,p)$
Výrazy pro $\langle x \rangle$ a $\langle p \rangle$ lze přepsat do tvaru

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

Operátor $\hat x \equiv x$ reprezentuje polohu a operátor $\hat p \equiv -i\hbar(\partial/\partial x)$ reprezentuje hybnost. V případě operátoru hybnosti $\hat p$ lze v rozšíření do 3D prostoru definovat $\hat p \equiv -i\hbar\nabla$.

Protože všechny klasické mechanické proměnné lze vyjádřit pomocí polohy a hybnosti, lze toto rozšířit na střední hodnotu libovolné fyzikální veličiny. Chceme-li spočítat střední hodnotu libovolné veličiny $Q(x,p)$, stačí všude nahradit $p$ výrazem $-i\hbar\nabla$, takto získaný operátor vložit mezi $\Psi^\*$ a $\Psi$ a integrovat.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Například, protože kinetická energie je $T=\cfrac{p^2}{2m}$, platí

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

Z rovnice ($\ref{eqn:Q_exp}$) tedy můžeme počítat střední hodnotu libovolné fyzikální veličiny pro částici ve stavu $\Psi$.

## Ehrenfestova věta (Ehrenfest theorem)
### Výpočet $d\langle p \rangle/dt$
Zderivujme obě strany rovnice ($\ref{eqn:p_op}$) podle času $t$ a spočítejme časovou derivaci střední hodnoty hybnosti $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Do ($\ref{eqn:dp/dt_1}$) lze dosadit rovnice (6) a (7) z příspěvku [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/) a získat tak ($\ref{eqn:dp/dt_2}$). V přechodu z ($\ref{eqn:dp/dt_3}$) na ($\ref{eqn:dp/dt_4}$) jsme použili per partes; stejně jako dříve, protože $\lim_{x\rightarrow\pm\infty}\Psi=0$, okrajový člen (boundary term) jsme zanedbali.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Vztah mezi Ehrenfestovou větou a Newtonovým 2. zákonem pohybu
Následující dvě rovnice, které jsme odvodili, se nazývají Ehrenfestova věta (Ehrenfest theorem).

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

Ehrenfestova věta má tvar velmi podobný vztahu mezi potenciální energií a konzervativní silou v klasické mechanice: $F=\cfrac{dp}{dt}=-\nabla V$.  
Když oba vztahy položíme vedle sebe a porovnáme je, dostaneme:

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

Když pravou stranu druhé rovnice Ehrenfestovy věty $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (rovnice [$\ref{eqn:ehrenfest_theorem_2nd}$]) rozvineme v Taylorově řadě podle $x$ v okolí $\langle x \rangle$, získáme

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

Pokud je zde $x-\langle x \rangle$ dostatečně malé, můžeme všechny vyšší členy kromě prvního zanedbat a aproximovat

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

Jinými slovy: **pokud je vlnová funkce částice v prostoru velmi ostře lokalizovaná v blízkosti jednoho bodu (tj. rozptyl $\|\Psi\|^2$ vzhledem k $x$ je velmi malý), lze Ehrenfestovu větu aproximovat Newtonovým 2. zákonem pohybu klasické mechaniky.** V makroskopickém měřítku lze prostorové rozprostření vlnové funkce zanedbat a polohu částice fakticky považovat za bod, takže Newtonův 2. zákon platí; v mikroskopickém měřítku však kvantové efekty zanedbat nelze, Newtonův 2. zákon už obecně neplatí a je třeba použít Ehrenfestovu větu.
