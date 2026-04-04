---
title: "ቋሚ ኮኤፊሺዎንቶችን ያላቸው 2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች"
description: "የባህሪ ስሌቱ ዲስክሪሚናንት ምልክት መሠረት በማድረግ፣ የቋሚ ኮኤፊሺዎንቶች አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌት አጠቃላይ መፍትሄ በሦስት አጋጣሚዎች ምን ቅርጽ እንደሚኖረው እንመልከታለን።"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## ማጠቃለያ
> - ቋሚ ኮኤፊሺዎንቶችን ያለው 2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌት: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **የባህሪ ስሌት(characteristic equation)**: $\lambda^2 + a\lambda + b = 0$
> - በየባህሪ ስሌቱ ዲስክሪሚናንት $a^2 - 4b$ ምልክት መሠረት የአጠቃላይ መፍትሄው ቅርጽ እንደሚከተለው በሶስት አጋጣሚዎች ሊከፈል ይችላል
>
> | አጋጣሚ | የባህሪ ስሌቱ ሥሮች | የተራ ልዩነት ስሌቱ መፍትሄዎች መሠረት | የተራ ልዩነት ስሌቱ አጠቃላይ መፍትሄ |
> | :---: | :---: | :---: | :---: |
> | I | የተለያዩ እውነተኛ ሥሮች<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | ድርብ እውነተኛ ሥር<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | የተዛማጅ ውስብስብ ሥሮች<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## ቅድመ ሁኔታዎች
- [የቤርኑሊ(Bernoulli) ስሌት](/posts/Bernoulli-Equation/)
- [የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- የኦይለር(Euler) ቀመር

## የባህሪ ስሌት (characteristic equation)
ኮኤፊሺዎንቶቹ $a$ እና $b$ ቋሚ የሆኑበትን 2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌት

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

እንመልከት። ይህ አይነት ስሌት በመካኒካዊ እና ኤሌክትሪካዊ ንዝረቶች ውስጥ ጠቃሚ ተግባራዊነት አለው።

ከዚህ በፊት [የቤርኑሊ(Bernoulli) ስሌት](/posts/Bernoulli-Equation/) ውስጥ የሎጂስቲክ ስሌቱን አጠቃላይ መፍትሄ አግኝተናል፣ በዚያም መሠረት ቋሚ ኮኤፊሺዎንት $k$ ያለው 1ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌት

$$ y^\prime + ky = 0 $$

መፍትሄው የኤክስፖነንሺያል ተግባር $y = ce^{-kx}$ ነው። (በዚያ ጽሑፍ ውስጥ ካለው ስሌት (4) ውስጥ $A=-k$, $B=0$ በሆነበት አጋጣሚ)

ስለዚህ፣ ከዚህ ጋር ተመሳሳይ ቅርጽ ላለው ስሌት ($\ref{eqn:ode_with_constant_coefficients}$) ውስጥም

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

የሚለውን ቅርጽ ያለ መፍትሄ በመጀመሪያ ልንሞክር እንችላለን።

> እርግጥ ይህ እስካሁን ድረስ ግምት ብቻ ነው፣ እና አጠቃላይ መፍትሄው በእርግጥ ይህን ቅርጽ ይይዛል ብሎ ማረጋገጥ አይቻልም። ነገር ግን ምንም ቢሆን መስመራዊ ገለልተኛ የሆኑ ሁለት መፍትሄዎችን ብቻ ካገኘን፣ [የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች](/posts/homogeneous-linear-odes-of-second-order/#መሠረት-እና-አጠቃላይ-መፍትሄ) ውስጥ እንዳየነው በ[የልዕለት መርህ](/posts/homogeneous-linear-odes-of-second-order/#የልዕለት-መርህ) መሠረት አጠቃላይ መፍትሄውን ማግኘት እንችላለን።  
> ትንሽ ቆይተን እንደምናየው፣ [ሌላ ቅርጽ ያለ መፍትሄ ማግኘት የሚያስፈልግበት አጋጣሚ](#ii-ድርብ-እውነተኛ-ሥር-lambda---cfraca2)ም አለ።
{: .prompt-info }

ስሌት ($\ref{eqn:general_sol}$) እና የእርሱ ተዋረዶች

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

ን ወደ ስሌት ($\ref{eqn:ode_with_constant_coefficients}$) በማስገባት

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

እናገኛለን። ስለዚህ $\lambda$ የ**ባህሪ ስሌቱ(characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

ሥር ከሆነ፣ የኤክስፖነንሺያል ተግባሩ ($\ref{eqn:general_sol}$) የተራ ልዩነት ስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) መፍትሄ ይሆናል። የኳድራቲክ ስሌቱ ($\ref{eqn:characteristic_eqn}$) ሥሮችን ከፈታን

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

እናገኛለን፣ ከዚህም ሁለቱ ተግባሮች

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

የስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) መፍትሄዎች ይሆናሉ።

> **የባህሪ ስሌት(characteristic equation)** እና **የረዳት ስሌት(auxiliary equation)** የሚሉት ሁለት ቃላት ብዙ ጊዜ በመተካከል ይጠቀማሉ፣ ግን ሙሉ በሙሉ አንድ ትርጉም አላቸው። የቱንም ብትጠቀሙ ችግር የለውም።
{: .prompt-tip }

አሁን በባህሪ ስሌቱ ($\ref{eqn:characteristic_eqn}$) ዲስክሪሚናንት $a^2 - 4b$ ምልክት መሠረት አጋጣሚዎቹን ሶስት ክፍሎች ማካፈል እንችላለን።
- $a^2 - 4b > 0$: ሁለት የተለያዩ እውነተኛ ሥሮች
- $a^2 - 4b = 0$: ድርብ እውነተኛ ሥር
- $a^2 - 4b < 0$: የተዛማጅ ውስብስብ ሥሮች

## በባህሪ ስሌቱ ዲስክሪሚናንት ምልክት መሠረት የአጠቃላይ መፍትሄ ቅርጽ
### I. ሁለት የተለያዩ እውነተኛ ሥሮች $\lambda_1$ እና $\lambda_2$
በዚህ አጋጣሚ በማንኛውም ክልል ላይ ያለው የስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) መፍትሄዎች መሠረት

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

ሲሆን፣ በዚህ መሠረት የሚገኘው አጠቃላይ መፍትሄ

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

ነው።

### II. ድርብ እውነተኛ ሥር $\lambda = -\cfrac{a}{2}$
$a^2 - 4b = 0$ ከሆነ የኳድራቲክ ስሌቱ ($\ref{eqn:characteristic_eqn}$) አንድ ብቻ ሥር $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$ ይኖረዋል፣ ስለዚህ ከእርሱ ልናገኘው የምንችለው $y = e^{\lambda x}$ ቅርጽ ያለ መፍትሄ

$$ y_1 = e^{-(a/2)x} $$

አንድ ብቻ ነው። መሠረት ለማግኘት $y_1$ ጋር ገለልተኛ የሆነ ሌላ ቅርጽ ያለ ሁለተኛ መፍትሄ $y_2$ ማግኘት አለብን። 

በእንደዚህ ያለ ሁኔታ ልንጠቀምበት የምንችለው ቀደም ሲል ያየነው [የደረጃ መቀነስ](/posts/homogeneous-linear-odes-of-second-order/#የደረጃ-መቀነስ-reduction-of-order) ነው። ልናገኘው የምንፈልገውን ሁለተኛ መፍትሄ $y_2=uy_1$ ብለን ብናስቀምጥ፣ 

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

እነዚህን ወደ ስሌት ($\ref{eqn:ode_with_constant_coefficients}$) በማስገባት

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

እናገኛለን። $u^{\prime\prime}$፣ $u^\prime$፣ $u$ ያላቸውን አባላት በየቡድናቸው ሰብስበን ካዘጋጀን

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

ይሆናል። እዚህ $y_1$ የስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) መፍትሄ ስለሆነ በመጨረሻው ቅንፍ ውስጥ ያለው ንግግር $0$ ነው፣

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

ስለሆነም በመጀመሪያው ቅንፍ ውስጥ ያለው ንግግርም $0$ ነው። ስለዚህ $u^{\prime\prime}y_1 = 0$ ብቻ ይቀራል፣ ከዚህም $u^{\prime\prime}=0$ እንደሆነ እናገኛለን። ሁለት ጊዜ ኢንተግሬት ካደረግን $u = c_1x + c_2$ ይሆናል፣ እና የኢንተግሬሽን ቋሚዎቹ $c_1$ እና $c_2$ ማንኛውም እሴት ሊኖራቸው ስለሚችል ቀላሉን $c_1=1$, $c_2=0$ በመምረጥ $u=x$ ብለን ማስቀመጥ እንችላለን። ከዚያ $y_2 = uy_1 = xy_1$ ይሆናል፣ እና $y_1$ እና $y_2$ መስመራዊ ገለልተኛ ስለሆኑ ሁለቱም መሠረት ይፈጥራሉ። ስለዚህ የባህሪ ስሌቱ ($\ref{eqn:characteristic_eqn}$) ድርብ ሥር ሲኖረው በማንኛውም ክልል ላይ ያለው የስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) መፍትሄዎች መሠረት

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

ሲሆን፣ ከእርሱ ጋር የሚዛመደው አጠቃላይ መፍትሄ

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

ነው።

### III. የተዛማጅ ውስብስብ ሥሮች $-\cfrac{1}{2}a + i\omega$ እና $-\cfrac{1}{2}a - i\omega$
በዚህ አጋጣሚ $a^2 - 4b < 0$ እና $\sqrt{-1} = i$ ስለሆነ ከስሌት ($\ref{eqn:lambdas}$)

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

እንደምናገኝ፣ እዚህ እውነተኛውን $\sqrt{b-\cfrac{1}{4}a^2} = \omega$ ብለን እንግለጽ።

$\omega$ ን ከላይ እንደተገለጸው ካቀረብን፣ የባህሪ ስሌቱ ($\ref{eqn:characteristic_eqn}$) ሥሮች የተዛማጅ ውስብስብ ሥሮች $\lambda = -\cfrac{1}{2}a \pm i\omega$ ይሆናሉ፣ እና ከእነርሱ ጋር የሚዛመዱ ሁለቱ የስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) ውስብስብ መፍትሄዎች

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

ን እናገኛለን። ነገር ግን በዚህ አጋጣሚም የማይምሳሌ እውነተኛ መፍትሄዎችን መሠረት እንደሚከተለው ማግኘት እንችላለን።

የኦይለር(Euler) ቀመር

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

እና በላዩ ውስጥ $t$ ቦታ $-t$ በማስገባት የምናገኘው

$$ e^{-it} = \cos t - i\sin t $$

የሚለውን ሁለቱን ስሌቶች በየጎናቸው በመደመርና በመቀነስ የሚከተለውን እናገኛለን።

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

እውነተኛ ክፍሉ $r$ እና ምናባዊ ክፍሉ $it$ የሆነ ውስብስብ ተለዋዋጭ $z = r + it$ ያለው ውስብስብ ኤክስፖነንሺያል ተግባር $e^z$ እውነተኛ ተግባሮቹን $e^r$, $\cos t$ እና $\sin t$ በመጠቀም እንደሚከተለው ልንገልጸው እንችላለን።

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

እዚህ $r=-\cfrac{1}{2}ax$, $t=\omega x$ ብለን ካስቀመጥን የሚከተለውን እንጽፋለን።

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

በ[የልዕለት መርህ](/posts/homogeneous-linear-odes-of-second-order/#የልዕለት-መርህ) መሠረት ከላይ ያሉት ውስብስብ መፍትሄዎች ድምርና በቋሚ ቁጥር መባዛት ደግሞ መፍትሄ ይሆናሉ። ስለዚህ ሁለቱን እኩልነቶች በየጎናቸው በመደመር ከዚያም በሁለቱም ጎኖች $\cfrac{1}{2}$ በመባዛት የመጀመሪያውን እውነተኛ መፍትሄ $y_1$ እንደሚከተለው እናገኛለን።

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

በተመሳሳይ መንገድ ከመጀመሪያው እኩልነት ሁለተኛውን በየጎናቸው በመቀነስ ከዚያም በሁለቱም ጎኖች $\cfrac{1}{2i}$ በመባዛት ሁለተኛውን እውነተኛ መፍትሄ $y_2$ ማግኘት እንችላለን።

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

$\cfrac{y_1}{y_2} = \cot{\omega x}$ ሲሆን ይህ ቋሚ አይደለም፣ ስለዚህ $y_1$ እና $y_2$ በሁሉም ክልሎች መስመራዊ ገለልተኛ ናቸው፤ በዚህም ምክንያት የስሌቱ ($\ref{eqn:ode_with_constant_coefficients}$) እውነተኛ መፍትሄዎች መሠረትን ይፈጥራሉ። ከዚህም የሚከተለውን አጠቃላይ መፍትሄ

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ ማንኛውም ቋሚዎች ናቸው)} \label{eqn:general_sol_3}\tag{13}$$

እናገኛለን።
