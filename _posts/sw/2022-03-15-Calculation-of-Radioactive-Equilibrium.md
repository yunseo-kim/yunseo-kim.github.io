---
title: "Hesabu ya usawa wa mionzi"
description: "Jifunze uhusiano kati ya konstanti ya kuoza, nusu-maisha, na wastani wa muda wa kuishi wa nuklidi za mionzi, na ukokotoe shughuli ya mionzi ya nuklidi katika muda wowote t ndani ya mnyororo wa kuoza uliopewa."
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Radioactive Decay]
math: true
mermaid: true
image: /assets/img/atoms.webp
---

## TL;DR

> **Shughuli ya mionzi katika muda wowote t**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **Uhusiano kati ya konstanti ya kuoza, nusu-maisha, na wastani wa muda wa kuishi**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## Konstanti ya kuoza (Decay Constant)

- Uwezekano kwamba kiini fulani kitaharibika katika kila kitengo cha muda
- Konstanti isiyobadilika kulingana na muda, inayotegemea tu aina ya nuklidi
- Huonyeshwa kwa alama $\lambda$

## Shughuli ya mionzi (Radioactivity)

Tukisema idadi ya viini ambavyo bado havijaharibika katika muda $t$ ni $n(t)$, basi kwa wastani viini $\lambda n(t)$ huharibika katika kipindi cha $dt$ kati ya muda $t$ na $t+dt$. Kiwango hiki cha kuoza huitwa *shughuli ya mionzi (radioactivity)* ya sampuli hiyo, na huonyeshwa kwa alama $\alpha$. Kwa hiyo, shughuli ya mionzi katika muda wowote $t$ ni kama ifuatavyo.

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## Vipimo vya shughuli ya mionzi

### Curie (Ci)

- Kipimo kilichotumika kijadi kabla ya kutumia kitengo cha becquerel
- Shughuli ya mionzi iliyomo katika 1 g ya radium-226
- Muozo wa viini $3.7\times 10^{10}$ kwa sekunde ($3.7\times 10^{10}\text{Bq}$)

### Becquerel (Bq)

- Kitengo cha kiwango cha kimataifa (SI)
- Muozo 1 wa kiini kwa sekunde
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## Kukokotoa mabadiliko ya shughuli ya mionzi kadiri muda unavyopita

Kwa kuwa viini $\lambda n(t)$ huharibika katika muda $dt$, kiasi cha kupungua kwa viini vilivyosalia bila kuoza ndani ya sampuli katika muda huo $dt$ kinaweza kuandikwa kama ifuatavyo.

$$ -dn(t)=\lambda n(t)dt $$

Tukifanya ujumuishaji hupatikana

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

Tukizidisha pande zote mbili kwa $\lambda$, shughuli ya mionzi huwa

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

Shughuli ya mionzi hupungua kwa nusu ndani ya *nusu-maisha (half-life)*, hivyo

$$ \alpha (T_{1/2})=\alpha_0/2 $$

Tukiweka hili katika mlinganyo (3), tunapata

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

Tukichukua logaritimu ya pande zote mbili na kutatua kwa nusu-maisha $T_{1/2}$, tunapata

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

Tukitatua mlinganyo wa juu kwa $\lambda$ na kuuweka katika mlinganyo (3), tunapata

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

Mara nyingi mlinganyo (5) ni rahisi zaidi kutumia kuliko mlinganyo (3) katika hesabu za muozo wa mionzi, kwa sababu mara nyingi nusu-maisha hutolewa badala ya konstanti ya kuoza.

*Wastani wa muda wa kuishi (mean-life)* wa kiini cha mionzi, $\overline{t}$, ni kinyume cha konstanti ya kuoza.

$$ \overline{t}=1/\lambda $$

Kutokana na mlinganyo (3), tunaweza kuona kwamba katika wastani wa muda mmoja wa kuishi, shughuli ya mionzi hushuka hadi $1/e$ ya thamani yake ya awali. Kutokana na mlinganyo (4), wastani wa muda wa kuishi na nusu-maisha vina uhusiano ufuatao.

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ Utoaji wa wastani wa muda wa kuishi $\overline{t}$

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## Mfano: mnyororo wa muozo wa mionzi 1

Tuchukulie kwamba nuklidi fulani ya mionzi huzalishwa kwa kasi ya $R$ atom/s. Kiini hiki huanza kuoza kwa mionzi mara tu kinapozalishwa. Tafuta shughuli ya mionzi ya nuklidi hii katika muda wowote $t$.

```mermaid
flowchart LR
	Start[?] -- R --> A[Mtindo wa kihisabati]
	A -- α --> End[?]
```

### 1. Kuweka mtindo

$$ \text{Kiwango cha mabadiliko ya nuklidi kwa muda} = \text{kiwango cha uzalishaji}-\text{kiwango cha upotevu} $$

Kwa alama za hisabati,

$$ dn/dt = -\lambda n + R $$

### 2. Suluhisho la jumla

Tuhamishe viambajengo vyote vya $n$ kwenda upande wa kushoto, kisha tuzidishe pande zote mbili kwa $e^{\lambda t}$.

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

Kwa kuwa $\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$, tunaweza kuandika

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

Tukijumuisha pande zote mbili, tunapata suluhisho la jumla lifuatalo.

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. Suluhisho maalum

Tuseme wakati $t=0$ idadi ya nuklidi hii ni $n_0$, na tutafute thamani ya konstanti $c$.

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

Kwa hiyo, suluhisho maalum linalolingana na hali iliyotolewa ni kama ifuatavyo.

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

Tukizidisha pande zote mbili za mlinganyo huu kwa $\lambda$, tunaweza kupata shughuli ya mionzi ya nuklidi hii.

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

Yaani, wakati $t\to\infty$, hupatikana ukomo $\alpha_{\text{max}}=R$ na $n_{\text{max}}=R/\lambda$.

## Mfano: mnyororo wa muozo wa mionzi 2

Katika mnyororo wa muozo ufuatao, kokotoa shughuli ya mionzi ya nuklidi B.

```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. Kuweka mtindo

$$ \text{Kiwango cha mabadiliko ya idadi ya viini vya B}=\text{kiwango cha uzalishaji kutokana na muozo wa A}-\text{kiwango cha muozo wa B kwenda C} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

Tukiweka mlinganyo (2) kwa $n_A$, tunapata mlinganyo tofautishi ufuatao wa $n_B$.

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. Suluhisho la jumla

Ili kutatua mlinganyo tofautishi, tuhame viambajengo vyote vya $n_B$ kwenda upande wa kushoto, kisha tuzidishe pande zote mbili kwa $e^{\lambda_B t}$.

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

Kwa kuwa $\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$, tunaweza kuandika

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

Tukijumuisha pande zote mbili, tunapata

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

Tukigawanya pande zote mbili kwa $e^{\lambda_B t}$, tunapata suluhisho la jumla lifuatalo.

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. Suluhisho maalum

Tuseme wakati $t=0$ idadi ya atomi za kipengele B ni $n_{B0}$, na tutafute thamani ya konstanti $c$.

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

Kwa hiyo, suluhisho maalum linalolingana na hali iliyotolewa ni kama ifuatavyo.

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$
