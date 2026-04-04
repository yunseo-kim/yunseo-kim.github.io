---
title: የኤረንፌስት ቴዎሬም(Ehrenfest theorem)
description: በኳንተም መካኒክስ ውስጥ ከሞገድ ተግባር የቦታና የሞመንተም የተጠበቀ እሴቶችን እንዴት እንደሚሰሉ እንመለከታለን፣ ከዚያም ይህን ወደ ማንኛውም ሜካኒካዊ መጠን Q(x,p) እናሰፋለን። በመጨረሻም ከዚህ የኤረንፌስት ቴዎሬምን እንወጣለን።
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

## ቅድመ መስፈርቶች
- ቀጣይ የእድል ስርጭት እና የእድል እፍጋት
- [ሽሮዲንገር ስሌት(Schrödinger equation) እና የሞገድ ተግባር(wave function)](/posts/schrodinger-equation-and-the-wave-function/)

## ከሞገድ ተግባር የተጠበቀ እሴት ስሌት
### የቦታ $x$ የተጠበቀ እሴት
በ$\Psi$ ሁኔታ ውስጥ ላለ ቅንጣት የቦታ $x$ የተጠበቀ እሴት(expectation value) የሚሆነው

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

ነው። በተመሳሳይ $\Psi$ ሁኔታ ውስጥ ያሉ በቂ ብዛት ያላቸው ቅንጣቶችን ለያንዳንዳቸው ቦታ ካለንበት በኋላ የልኬት ውጤቶቹን አማካይ ካደረግን ከላይ ባለው ስሌት የተሰላውን $\langle x \rangle$ እናገኛለን።

> እዚህ የሚባለው የተጠበቀ እሴት ማለት አንድን ቅንጣት ደጋግመን በመለካት የምናገኘው አማካይ ሳይሆን፣ ተመሳሳይ ሁኔታ ያላቸው ሥርዓቶች **ኤንሰምብል(ensemble)** ላይ የሚደረጉ ልኬቶች አማካይ መሆኑን ማስታወስ አለብን። አንድን ተመሳሳይ ቅንጣት በአጭር የጊዜ ልዩነት ብዙ ጊዜ ካለንበት፣ በመጀመሪያው ልኬት [የሞገድ ተግባሩ መፍረስ(collapse)](/posts/schrodinger-equation-and-the-wave-function/#መለኪያና-የሞገድ-ተግባር-መፍረስ) ስለሚከሰት ቀጣይ ልኬቶች ሁሉ ተመሳሳይ እሴት ብቻ ይሰጣሉ።
{: .prompt-warning }

### የሞመንተም $p$ የተጠበቀ እሴት
$\Psi$ በጊዜ ላይ የሚመረኮዝ ስለሆነ፣ ጊዜ እያለፈ $\langle x \rangle$ ይለዋዋጣል። በዚህ ጊዜ [ሽሮዲንገር ስሌት(Schrödinger equation) እና የሞገድ ተግባር(wave function)](/posts/schrodinger-equation-and-the-wave-function/) ውስጥ ያለው ስሌት (8) እና ከላይ ያለው ስሌት ($\ref{eqn:x_exp}$) መሠረት የሚከተለው ይጸናል።

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> ከስሌት ($\ref{eqn:dx/dt_1}$) ወደ ($\ref{eqn:dx/dt_2}$) እና ከ($\ref{eqn:dx/dt_2}$) ወደ ($\ref{eqn:dx/dt_3}$) በሚሄዱበት ሂደት ሁለት ጊዜ በክፍል ኢንቴግሬሽን(partial integration) ተጠቅመናል፣ እንዲሁም $\lim_{x\rightarrow\pm\infty}\Psi=0$ ስለሆነ የወሰን እሴቱን(boundary term) ትተናል።
{: .prompt-tip }

ስለዚህ **ሞመንተም** የተጠበቀ እሴት እንደሚከተለው ይገኛል።

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### ለማንኛውም አካላዊ መጠን $Q(x,p)$ የተጠበቀ እሴት
ከዚህ በፊት ያገኘነውን $\langle x \rangle$ እና $\langle p \rangle$ መግለጫ በሚከተለው ቅርጽ ማጻፍ እንችላለን።

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

ኦፕሬተሩ $\hat x \equiv x$ ቦታን ይወክላል፣ እና ኦፕሬተሩ $\hat p \equiv -i\hbar(\partial/\partial x)$ ሞመንተምን ይወክላል። የሞመንተም ኦፕሬተር $\hat p$ ጉዳይ ወደ 3-ልኬት ህዋ ሲሰፋ $\hat p \equiv -i\hbar\nabla$ ብለን ልንወስነው እንችላለን።

ሁሉም የክላሲካል መካኒክስ ተለዋዋጮች በቦታና በሞመንተም ሊገለጹ ስለሚችሉ፣ ይህን ወደ ማንኛውም አካላዊ መጠን የተጠበቀ እሴት ማስፋት እንችላለን። ለማንኛውም $Q(x,p)$ መጠን የተጠበቀ እሴት ለማስላት ሁሉንም $p$ በ $-i\hbar\nabla$ መቀየር እና በዚህ መንገድ የተገኘውን ኦፕሬተር በ$\Psi^\*$ እና $\Psi$ መካከል አስገብተን ኢንቴግሬሽን ማድረግ ነው።

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

ለምሳሌ፣ ኪኔቲክ ኢነርጂ(kinetic energy) $T=\cfrac{p^2}{2m}$ ስለሆነ

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

ነው።

በስሌት ($\ref{eqn:Q_exp}$) አማካኝነት በ$\Psi$ ሁኔታ ውስጥ ላለ ቅንጣት ማንኛውንም አካላዊ መጠን የተጠበቀ እሴት ማስላት ይቻላል።

## የኤረንፌስት ቴዎሬም (Ehrenfest theorem)
### የ $d\langle p \rangle/dt$ ስሌት
የሞመንተም የተጠበቀ እሴት በጊዜ የሚከሰተውን ተዋጽኦ $\cfrac{d\langle p \rangle}{dt}$ ለማግኘት፣ በስሌት ($\ref{eqn:p_op}$) ውስጥ ያሉትን ሁለቱንም ጎኖች በጊዜ $t$ እንለይ።

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

> በስሌት ($\ref{eqn:dp/dt_1}$) ውስጥ [ሽሮዲንገር ስሌት(Schrödinger equation) እና የሞገድ ተግባር(wave function)](/posts/schrodinger-equation-and-the-wave-function/) ውስጥ ያሉትን ስሌቶች (6) እና (7) በመተካት ስሌት ($\ref{eqn:dp/dt_2}$) ማግኘት ይቻላል። ከስሌት ($\ref{eqn:dp/dt_3}$) ወደ ($\ref{eqn:dp/dt_4}$) በሚሄደው ሂደት በክፍል ኢንቴግሬሽን ተጠቅመናል፣ እና እንደ ቀደሙት ሁሉ $\lim_{x\rightarrow\pm\infty}\Psi=0$ ስለሆነ የወሰን እሴቱን(boundary term) ትተናል።
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### በኤረንፌስት ቴዎሬም እና በኒውተን(Newton) ሁለተኛ የእንቅስቃሴ ህግ መካከል ያለው ግንኙነት
ከዚህ በፊት ያገኘናቸውን የሚከተሉትን ሁለት ስሌቶች የኤረንፌስት ቴዎሬም(Ehrenfest theorem) ብለን እንጠራቸዋለን።

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

የኤረንፌስት ቴዎሬም በክላሲካል መካኒክስ ውስጥ በፖቴንሻል ኢነርጂ(potential energy) እና በጠባቂ ኃይል(conservative force) መካከል ያለው ግንኙነት $F=\cfrac{dp}{dt}=-\nabla V$ ጋር በጣም የሚመሳሰል ቅርጽ አለው።  
ሁለቱን ስሌቶች ጎን ለጎን በማስቀመጥ ካነጻጸርናቸው እንደሚከተለው ነው።

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

በኤረንፌስት ቴዎሬም ውስጥ ያለውን ሁለተኛውን ስሌት $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$(ስሌት [$\ref{eqn:ehrenfest_theorem_2nd}$]) የቀኝ ጎን በ $\langle x \rangle$ አቅራቢያ ለ $x$ ቴይለር ስፋት(Taylor expansion) ካደረግን

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

ይሆናል። እዚህ ላይ $x-\langle x \rangle$ በቂ ትንሽ ከሆነ፣ ከመጀመሪያው አባል ውጭ ያሉ ሁሉንም ከፍተኛ ደረጃ አባላት በመተው

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

ብለን ልንጠጋግም እንችላለን።

ማለትም፣ **የአንድ ቅንጣት የሞገድ ተግባር በህዋ ውስጥ በአንድ ነጥብ አቅራቢያ በጣም የተሰበሰበ ሹል ቅርጽ ካሳየ ($\|\Psi\|^2$ በ $x$ ላይ ያለው ስርጭት በጣም ትንሽ ከሆነ)፣ የኤረንፌስት ቴዎሬምን ወደ ክላሲካል መካኒክስ የኒውተን ሁለተኛ የእንቅስቃሴ ህግ ማቅረብ ይቻላል።** በማክሮስኮፒክ መጠን ላይ የሞገድ ተግባሩ በህዋ ውስጥ የሚዘረጋውን መጠን ችላ ብለን የቅንጣቱን ቦታ ለማለት እንደ አንድ ነጥብ ማየት ስለሚቻል የኒውተን ሁለተኛ የእንቅስቃሴ ህግ ይሰራል። ነገር ግን በማይክሮስኮፒክ መጠን ላይ የኳንተም መካኒክስ ተፅእኖዎችን ችላ ማለት አይቻልም፣ ስለዚህ የኒውተን ሁለተኛ የእንቅስቃሴ ህግ ከእንግዲህ በኋላ በቀጥታ አይሰራም እና የኤረንፌስት ቴዎሬምን መጠቀም ያስፈልጋል።
