---
title: "የሬዲዮአክቲቭ ሚዛን ስሌት"
description: "የሬዲዮአክቲቭ ኑክሊድ የመበስበስ ቋሚ፣ ግማሽ-ዕድሜ እና አማካይ ዕድሜ መካከል ያለውን ግንኙነት እንመለከታለን፣ እንዲሁም በተሰጠ የመበስበስ ሰንሰለት ውስጥ በማንኛውም ጊዜ t ላይ የሬዲዮአክቲቭ ኑክሊድ እንቅስቃሴን እናሰላለን።"
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Radioactive Decay]
math: true
mermaid: true
image: /assets/img/atoms.webp
---

## TL;DR

> **በማንኛውም ጊዜ t ላይ ያለ ሬዲዮአክቲቪቲ**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **የመበስበስ ቋሚ፣ ግማሽ-ዕድሜ እና አማካይ ዕድሜ ግንኙነት**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## የመበስበስ ቋሚ(Decay Constant)

- አንድ ኑክሌየስ በአንድ የጊዜ ክፍል ውስጥ የሚበሰብስበት እድል
- ከጊዜ ጋር የማይለዋወጥ፣ በኑክሊድ ብቻ የሚወሰን ቋሚ
- በምልክት $\lambda$ ይወከላል

## ሬዲዮአክቲቪቲ(Radioactivity)

በጊዜ $t$ ላይ ገና ያልተበሰበሱ ኑክሌይ ብዛትን $n(t)$ ብለን ከተወሰነ፣ በጊዜ $t$ እና $t+dt$ መካከል ባለው $dt$ ክፍተት ውስጥ በአማካይ $\lambda n(t)$ ኑክሌይ ይበሰብሳሉ። ይህን የመበስበስ ፍጥነት የዚያ ናሙና *ሬዲዮአክቲቪቲ(radioactivity)* ብለን እንጠራዋለን፣ በምልክት $\alpha$ ይወከላል። ስለዚህ በአንድ ጊዜ $t$ ላይ ያለው ሬዲዮአክቲቪቲ እንዲህ ነው።

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## የሬዲዮአክቲቪቲ መለኪያ አሃዶች

### ኩሪ(Curie, Ci)

- የቤክሬል አሃድ ከመጠቀሙ በፊት በተለምዶ የሚጠቀምበት አሃድ
- 1g የራዲየም-226 የሚይዘው ሬዲዮአክቲቪቲ
- በሰከንድ $3.7\times 10^{10}$ የኑክሌር መበስበሶች($3.7\times 10^{10}\text{Bq}$)

### ቤክሬል(Becquerel, Bq)

- ዓለም አቀፍ መደበኛ(SI) አሃድ
- በሰከንድ 1 የኑክሌር መበስበስ
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## በጊዜ ላይ የሬዲዮአክቲቪቲ ለውጥ ስሌት

በጊዜ $dt$ ውስጥ $\lambda n(t)$ ኑክሌይ ስለሚበሰብሱ፣ በ$dt$ ውስጥ በናሙናው ውስጥ ሳይበሰብሱ የሚቀሩ ኑክሌይ ቅነሳ በሚከተለው መልኩ ሊገለጽ ይችላል።

$$ -dn(t)=\lambda n(t)dt $$

ይህን ሲያጠናቅሉ

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

ይሆናል። በሁለቱም ወገኖች $\lambda$ን በማባዛት ሬዲዮአክቲቪቲው

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

ይሆናል።

ሬዲዮአክቲቪቲው በ*ግማሽ-ዕድሜ(half-life)* ውስጥ በግማሽ ይቀንሳል፣ ስለዚህ

$$ \alpha (T_{1/2})=\alpha_0/2 $$

ይህን ወደ ስሌት (3) ሲተኩሉ

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

ይሆናል። በሁለቱም ወገኖች ላይ ሎጋሪዝም በመውሰድ ለግማሽ-ዕድሜ $T_{1/2}$ ሲፈቱ

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

ይገኛል።

ከላይ ያለውን ስሌት ለ$\lambda$ በመፍታት ወደ ስሌት (3) ሲተኩሉ

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

ይሆናል።

ስሌት (5) ብዙ ጊዜ ከስሌት (3) ይልቅ በሬዲዮአክቲቭ መበስበስ ስሌት ላይ ለመጠቀም የቀለለ ነው፣ ምክንያቱም ከመበስበስ ቋሚ ይልቅ የግማሽ-ዕድሜ ዋጋ መሰጠት የበለጠ የተለመደ ስለሆነ ነው።

የሬዲዮአክቲቭ ኑክሌየስ *አማካይ ዕድሜ(mean-life)* $\overline{t}$ የመበስበስ ቋሚው ተቃራኒ ነው።

$$ \overline{t}=1/\lambda $$

ከስሌት (3) መሠረት፣ በአንድ አማካይ ዕድሜ ውስጥ ሬዲዮአክቲቪቲው ወደ መጀመሪያ ዋጋው $1/e$ እንደሚወርድ ማወቅ ይቻላል። ከስሌት (4) መሠረት አማካይ ዕድሜና ግማሽ-ዕድሜ በሚከተለው ግንኙነት ይገናኛሉ።

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ የአማካይ ዕድሜ $\overline{t}$ አመጣጥ

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## ምሳሌ: የሬዲዮአክቲቭ መበስበስ ሰንሰለት 1

አንድ ሬዲዮአክቲቭ ኑክሊድ በ $R$ atom/s ፍጥነት ይፈጠራል ብለን እንግምት። ይህ ኑክሌየስ እንደተፈጠረ ወዲያውኑ ሬዲዮአክቲቭ መበስበስ ይጀምራል። በማንኛውም ጊዜ t ላይ የዚህን ኑክሊድ ሬዲዮአክቲቪቲ አግኝ።

```mermaid
flowchart LR
	Start[?] -- R --> A[የሂሳብ ሞዴል]
	A -- α --> End[?]
```

### 1. ሞዴል ማቋቋም

$$ \text{በጊዜ ላይ ያለ የኑክሊድ ለውጥ ፍጥነት} = \text{የመፍጠር ፍጥነት}-\text{የጥፋት ፍጥነት} $$

በሂሳብ ምልክት ሲገለጽ

$$ dn/dt = -\lambda n + R $$

ነው። 

### 2. አጠቃላይ መፍትሔ

ከ$n$ ጋር የተያያዙ ቃላትን ሁሉ ወደ ግራ ወገን እናስተላልፍ፣ ከዚያም በሁለቱም ወገኖች $e^{\lambda t}$ን እናባዛ።

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

$\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$ ስለሆነ እንዲህ ማደራጀት ይቻላል።

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

በሁለቱም ወገኖች ላይ ሲያጠናቅሉ የሚከተለውን አጠቃላይ መፍትሔ ያገኛሉ።

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. ልዩ መፍትሔ

$t=0$ ላይ የዚህ ኑክሊድ ብዛት $n_0$ ነው ብለን ቋሚውን $c$ እናግኝ።

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

ስለዚህ ለተሰጠው ሁኔታ የሚስማማው ልዩ መፍትሔ የሚከተለው ነው።

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

ነው። ከላይ ባለው ስሌት ሁለቱንም ወገኖች በ $\lambda$ በማባዛት የዚህን ኑክሊድ ሬዲዮአክቲቪቲ ማግኘት ይቻላል።

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

ማለትም፣ $t\to\infty$ ሲሆን $\alpha_{\text{max}}=R$, $n_{\text{max}}=R/\lambda$ ወደነዚህ እሴቶች ይቀርባሉ።

## ምሳሌ: የሬዲዮአክቲቭ መበስበስ ሰንሰለት 2

ከታች ባለው የመበስበስ ሰንሰለት ውስጥ የሬዲዮአክቲቭ ኑክሊድ B ሬዲዮአክቲቪቲን አስላ።

```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. ሞዴል ማቋቋም

$$ \text{የB ኑክሌይ ብዛት ለውጥ ፍጥነት}=\text{በA መበስበስ ምክንያት የመፍጠር ፍጥነት}-\text{የB ወደ C የመበስበስ ፍጥነት} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

ለ$n_A$ ስሌት (2) ሲተኩሉ ለ$n_B$ የሚከተለውን የልዩነት ስሌት ያገኛሉ።

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. አጠቃላይ መፍትሔ

የልዩነት ስሌቱን ለመፍታት ከ$n_B$ ጋር የተያያዙ ቃላትን ሁሉ ወደ ግራ ወገን እናስተላልፍ፣ ከዚያም በሁለቱም ወገኖች $e^{\lambda_B t}$ን እናባዛ።

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

$\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$ ስለሆነ እንዲህ ማደራጀት ይቻላል።

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

በሁለቱም ወገኖች ላይ ሲያጠናቅሉ

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

ይሆናል። ሁለቱንም ወገኖች በ $e^{\lambda_B t}$ በመካፈል የሚከተለውን አጠቃላይ መፍትሔ ያገኛሉ።

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. ልዩ መፍትሔ

$t=0$ ላይ የB ንጥረ ነገር ብዛት $n_{B0}$ ነው ብለን ቋሚውን $c$ እናግኝ።

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

ስለዚህ ለተሰጠው ሁኔታ የሚስማማው ልዩ መፍትሔ የሚከተለው ነው።

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$
