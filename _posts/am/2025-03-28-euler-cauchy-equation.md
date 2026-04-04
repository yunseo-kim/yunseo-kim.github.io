---
title: "የኦይለር-ኮሺ ስሌት"
description: "በረዳት ስሌቱ ዲስክሪሚናንት ምልክት መሰረት፣ በእያንዳንዱ ሁኔታ የኦይለር-ኮሺ ስሌት አጠቃላይ መፍትሄ ምን አይነት ቅጽ እንደሚኖረው እንመለከታለን።"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## ማጠቃለያ
> - የኦይለር-ኮሺ ስሌት: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **ረዳት ስሌት(auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - በረዳት ስሌቱ ዲስክሪሚናንት $(1-a)^2 - 4b$ ምልክት መሰረት የአጠቃላይ መፍትሄውን ቅጽ ከታች እንደሚታየው በሦስት ሁኔታዎች መከፋፈል ይቻላል
>
> | ሁኔታ | የረዳት ስሌቱ መፍትሄ | የኦይለር-ኮሺ ስሌት መፍትሄ መሠረት | የኦይለር-ኮሺ ስሌት አጠቃላይ መፍትሄ |
> | :---: | :---: | :---: | :---: |
> | I | የተለያዩ ሁለት እውነተኛ ሥሮች<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | ድርብ እውነተኛ ሥር<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | የኮንጁጌት ኮምፕሌክስ ሥሮች<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## ቅድመ ሁኔታዎች
- [የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [ቋሚ ኮኤፊሺዎንቶች ያላቸው የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- የኦይለር ቀመር

## ረዳት ስሌት (auxiliary equation)
**የኦይለር-ኮሺ ስሌት(Euler-Cauchy equation)** የተሰጡ ቋሚዎች $a$ እና $b$፣ እንዲሁም ያልታወቀ ተግባር $y(x)$ ያለው

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

ቅጽ ያለው ተራ ልዩነት ስሌት ነው። በስሌት ($\ref{eqn:euler_cauchy_eqn}$) ውስጥ

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

ካስቀመጥን

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

ማለትም

$$ [m(m-1) + am + b]x^m = 0 $$

እናገኛለን። ከዚህም ረዳት ስሌቱን

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

እናገኛለን፤ $y=x^m$ የኦይለር-ኮሺ ስሌት ($\ref{eqn:euler_cauchy_eqn}$) መፍትሄ ለመሆን ያለው አስፈላጊና በቂ ሁኔታ $m$ የረዳት ስሌቱ ($\ref{eqn:auxiliary_eqn}$) መፍትሄ መሆኑ ነው።

የካሬ ስሌቱን ($\ref{eqn:auxiliary_eqn}$) መፍትሄዎች ካገኘን

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

ሲሆኑ፣ ከዚህም ሁለቱ ተግባሮች

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

የስሌቱ ($\ref{eqn:euler_cauchy_eqn}$) መፍትሄዎች ይሆናሉ።

[ቋሚ ኮኤፊሺዎንቶች ያላቸው የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች](/posts/homogeneous-linear-odes-with-constant-coefficients/) ውስጥ እንዳየነው በተመሳሳይ፣ በረዳት ስሌቱ ($\ref{eqn:auxiliary_eqn}$) ዲስክሪሚናንት $(1-a)^2 - 4b$ ምልክት መሰረት ሁኔታዎቹን በሦስት ማካፈል ይቻላል።
- $(1-a)^2 - 4b > 0$: የተለያዩ ሁለት እውነተኛ ሥሮች
- $(1-a)^2 - 4b = 0$: ድርብ እውነተኛ ሥር
- $(1-a)^2 - 4b < 0$: የኮንጁጌት ኮምፕሌክስ ሥሮች

## በረዳት ስሌቱ ዲስክሪሚናንት ምልክት መሰረት የአጠቃላይ መፍትሄ ቅጽ
### I. የተለያዩ ሁለት እውነተኛ ሥሮች $m_1$ እና $m_2$
በዚህ ሁኔታ፣ በማንኛውም ክፍት ክልል ላይ የስሌቱ ($\ref{eqn:euler_cauchy_eqn}$) መፍትሄ መሠረት

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

ሲሆን፣ ይህን የሚያመለክተው አጠቃላይ መፍትሄ

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

ነው።

### II. ድርብ እውነተኛ ሥር $m = \cfrac{1-a}{2}$
$(1-a)^2 - 4b = 0$፣ ማለትም $b=\cfrac{(1-a)^2}{4}$ ከሆነ የካሬ ስሌቱ ($\ref{eqn:auxiliary_eqn}$) አንድ ብቻ መፍትሄ $m = m_1 = m_2 = \cfrac{1-a}{2}$ ይኖረዋል፤ ስለዚህም ከዚህ የምናገኘው $y = x^m$ ቅጽ ያለው አንድ መፍትሄ

$$ y_1 = x^{(1-a)/2} $$

ሲሆን፣ የኦይለር-ኮሺ ስሌቱ ($\ref{eqn:euler_cauchy_eqn}$)

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

ቅጽ ይኖረዋል። አሁን ከዚህ ጋር መስመራዊ ገለልተኛ የሆነ ሌላ መፍትሄ $y_2$ን [የደረጃ መቀነስ](/posts/homogeneous-linear-odes-of-second-order/#የደረጃ-መቀነስ-reduction-of-order) በመጠቀም እንፈልግ።

የምንፈልገውን ሁለተኛ መፍትሄ $y_2=uy_1$ ብለን ካስቀመጥን

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

እናገኛለን።

$\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$ ስለሆነ፣

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

ይሆናል፣ እና ካካተትን $u = \ln x$ እናገኛለን።

ስለዚህ $y_2 = uy_1 = y_1 \ln x$ ሲሆን፣ $y_1$ እና $y_2$ ጥምርታቸው ቋሚ ስላልሆነ መስመራዊ ገለልተኛ ናቸው። ከመሠረቱ $y_1$ እና $y_2$ ጋር የሚዛመደው አጠቃላይ መፍትሄ

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

ነው።

### III. የኮንጁጌት ኮምፕሌክስ ሥሮች
በዚህ ሁኔታ የረዳት ስሌቱ ($\ref{eqn:auxiliary_eqn}$) መፍትሄዎች $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$ ይሆናሉ፣ እነዚህን የሚዛመዱ የስሌቱ ($\ref{eqn:euler_cauchy_eqn}$) ሁለት ኮምፕሌክስ መፍትሄዎች ደግሞ $x=e^{\ln x}$ መሆኑን በመጠቀም እንደሚከተለው ልንጽፋቸው እንችላለን።

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

$t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ ብለን ካስቀመጥን እና የኦይለር ቀመር $e^{it} = \cos{t} + i\sin{t}$ን ከተጠቀምን

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

እንደሚሆኑ እናውቃለን፣ ከዚህም የሚከተሉትን ሁለት እውነተኛ መፍትሄዎች

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

እናገኛለን።

እነዚህ ሁለት መፍትሄዎች ጥምርታቸው $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ ቋሚ ስላልሆነ፣ ከላይ ያሉት ሁለቱ መፍትሄዎች መስመራዊ ገለልተኛ ናቸው፣ ስለዚህ [የልዕለት መርህ](/posts/homogeneous-linear-odes-of-second-order/#የልዕለት-መርህ) መሰረት የኦይለር-ኮሺ ስሌት ($\ref{eqn:euler_cauchy_eqn}$) መሠረት ይፈጥራሉ። ከዚህም የሚከተለውን እውነተኛ አጠቃላይ መፍትሄ እናገኛለን።

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

ሆኖም፣ በኦይለር-ኮሺ ስሌት ውስጥ ረዳት ስሌቱ የኮንጁጌት ኮምፕሌክስ ሥሮች ያሉበት ሁኔታ በተግባር ያለው አስፈላጊነት እጅግ አይበዛም።

## ወደ ቋሚ ኮኤፊሺዎንቶች ያሉት የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች መቀየር
የኦይለር-ኮሺ ስሌት በተለዋዋጭ መተካት [ቋሚ ኮኤፊሺዎንቶች ያላቸው የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች](/posts/homogeneous-linear-odes-with-constant-coefficients/) ወደሚሆኑት ሊቀየር ይችላል።

$x = e^t$ ብለን ከተካነ

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

ይሆናል፣ ስለዚህ የኦይለር-ኮሺ ስሌቱ ($\ref{eqn:euler_cauchy_eqn}$) እንደሚከተለው በ $t$ ላይ ያለ ቋሚ ኮኤፊሺዎንት አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌት ይሆናል።

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

ስሌቱን ($\ref{eqn:substituted}$) በ[ቋሚ ኮኤፊሺዎንቶች ያላቸው የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች](/posts/homogeneous-linear-odes-with-constant-coefficients/) የመፍትሄ ዘዴ በመተግበር በ$t$ ላይ ከፈታነው በኋላ፣ እንዲሁ ያገኘነውን መፍትሄ $t = \ln{x}$ መሆኑን በመጠቀም እንደገና ወደ $x$ ላይ ያለ መፍትሄ ከቀየርነው [ከዚህ በፊት እንዳየነው ተመሳሳይ ውጤት](#በረዳት-ስሌቱ-ዲስክሪሚናንት-ምልክት-መሰረት-የአጠቃላይ-መፍትሄ-ቅጽ) እናገኛለን።
