---
title: "የ2ኛ ደረጃ አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች (Homogeneous Linear ODEs of Second Order)"
description: "የ2ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌቶችን ትርጉምና ባህሪያት እንመለከታለን፣ በተለይም በአንድ-ዓይነት መስመራዊ ስሌቶች ላይ የሚሰራውን የልዕለት መርህና ከእሱ የሚከተለውን የመሠረት(basis) ጽንሰ-ሐሳብ እንረዳለን።"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## ማጠቃለያ
> - የ2ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌት의 **መደበኛ ቅጽ(standard form)**: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **ኮኤፊሺዎንቶች(coefficients)**: ተግባሮች $p$, $q$
>   - **ግብዓት(input)**: $r(x)$
>   - **ውጤት(output)** ወይም **ምላሽ(response)**: $y(x)$
> - አንድ-ዓይነት እና አንድ-ዓይነት ያልሆነ
>   - **አንድ-ዓይነት(homogeneous)**: በመደበኛ ቅጽ ሲገለጽ $r(x)\equiv0$ ከሆነ
>   - **አንድ-ዓይነት ያልሆነ(nonhomogeneous)**: በመደበኛ ቅጽ ሲገለጽ $r(x)\not\equiv 0$ ከሆነ
> - **የልዕለት መርህ(superposition principle)**: <u>አንድ-ዓይነት</u> መስመራዊ ተራ ልዩነት ስሌት $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ ስለሆነ፣ በክፍት ክልል $I$ ላይ ማንኛውም የሁለት መፍትሄዎች መስመራዊ ጥምረት እንዲሁ የተሰጠው ስሌት መፍትሄ ይሆናል። ማለትም ለተሰጠው አንድ-ዓይነት መስመራዊ ስሌት የማንኛውም መፍትሄዎች ድምርና በቋሚ ቁጥር መባዛት እንዲሁም የዚያ ስሌት መፍትሄዎች ናቸው።
> - **መሠረት(basis)** ወይም **መሠረታዊ ስርዓት(fundamental system)**: በክልል $I$ ላይ መስመራዊ ገለልተኛ የሆኑ የአንድ-ዓይነት መስመራዊ ስሌት መፍትሄዎች ጥንድ $(y_1, y_2)$
> - **የደረጃ መቀነስ(reduction of order)**: ለ2ኛ ደረጃ አንድ-ዓይነት ልዩነት ስሌት አንድ መፍትሄ ማግኘት ከተቻለ፣ ከዚህ መፍትሄ ጋር መስመራዊ ገለልተኛ የሆነ ሁለተኛ መፍትሄ፣ ማለትም መሠረትን፣ 1ኛ ደረጃ ተራ ልዩነት ስሌት በመፍታት ማግኘት ይቻላል፤ ይህን ዘዴ የደረጃ መቀነስ ብለን እንጠራዋለን
> - የደረጃ መቀነስ መተግበሪያ: አጠቃላይ 2ኛ ደረጃ ልዩነት ስሌት $F(x, y, y^\prime, y^{\prime\prime})=0$ መስመራዊ ይሁን ወይም ያልሆነ ምንም ቢሆን፣ በሚከተሉት ሁኔታዎች የደረጃ መቀነስ በመጠቀም ወደ 1ኛ ደረጃ ማውረድ ይቻላል
>   - $y$ በግልጽ አይነት የማይታይ ከሆነ
>   - $x$ በግልጽ አይነት የማይታይ ከሆነ
>   - አንድ-ዓይነት መስመራዊ ሲሆን አንድ መፍትሄ አስቀድሞ የሚታወቅ ከሆነ
{: .prompt-info }

## ቅድመ ሁኔታዎች
- [የሞዴሊንግ(Modeling) መሠረታዊ ጽንሰ-ሐሳቦች](/posts/Basic-Concepts-of-Modeling/)
- [የተለዋዋጮች መለያየት(Separation of Variables)](/posts/Separation-of-Variables/)
- [የ1ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌቶች መፍትሄ](/posts/Solution-of-First-Order-Linear-ODE/)

## የ2ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌቶች
2ኛ ደረጃ ልዩነት ስሌትን

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

በሚለው ቅጽ መጻፍ ከተቻለ **መስመራዊ(linear)** ይባላል፣ ካልተቻለ ግን **መስመራዊ ያልሆነ(nonlinear)** ይባላል።

$p$, $q$, $r$ ማንኛውም $x$ ላይ የሚወሰኑ ተግባሮች ሲሆኑ፣ ይህ ስሌት በ$y$ እና ተዋረዶቹ ላይ መስመራዊ ነው።

እንደ ስሌት ($\ref{eqn:standard_form}$) ያለው ቅጽ የ2ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌት **መደበኛ ቅጽ(standard form)** ተብሎ ይጠራል፣ እና የተሰጠው 2ኛ ደረጃ መስመራዊ ስሌት የመጀመሪያ አካሉ $f(x)y^{\prime\prime}$ ከሆነ የስሌቱን ሁለት ጎኖች በ$f(x)$ በመካፈል መደበኛ ቅጹን ማግኘት ይቻላል።

ተግባሮች $p$, $q$ን **ኮኤፊሺዎንቶች(coefficients)** ፣ $r(x)$ን **ግብዓት(input)** ፣ $y(x)$ን **ውጤት(output)** ወይም ለግብዓትና ለመነሻ ሁኔታዎች የሚሰጥ **ምላሽ(response)** እንላለን።

### አንድ-ዓይነት 2ኛ ደረጃ መስመራዊ ተራ ልዩነት ስሌት
ስሌት ($\ref{eqn:standard_form}$)ን ለመፍታት የምንፈልገውን ክልል $a<x<b$ ብለን $J$ እንጠራው። በስሌት ($\ref{eqn:standard_form}$) ውስጥ ለክልል $J$ $r(x)\equiv 0$ ከሆነ

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

ይሆናል፣ ይህም **አንድ-ዓይነት(homogeneous)** ይባላል።

## አንድ-ዓይነት ያልሆነ መስመራዊ ተራ ልዩነት ስሌት
በክልል $J$ ላይ $r(x)\not\equiv 0$ ከሆነ **አንድ-ዓይነት ያልሆነ(nonhomogeneous)** ይባላል።

## የልዕለት መርህ

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ ማንኛውም ቋሚዎች ናቸው)}\tag{3}$$

በሚለው ቅጽ ያለ ተግባር የ$y_1$ እና $y_2$ **መስመራዊ ጥምረት(linear combination)** ተብሎ ይጠራል። 

በዚህ ጊዜ የሚከተለው ይሠራል።

> **የልዕለት መርህ(superposition principle)**  
> ለአንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$)፣ በክፍት ክልል $I$ ላይ ማንኛውም የሁለት መፍትሄዎች መስመራዊ ጥምረት እንዲሁ የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሄ ይሆናል። ማለትም ለተሰጠው አንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌት የማንኛውም መፍትሄዎች ድምርና በቋሚ ቁጥር መባዛት እንዲሁም የዚያ ስሌት መፍትሄዎች ናቸው።
{: .prompt-info }

### ማረጋገጫ
$y_1$ እና $y_2$ በክልል $I$ ላይ የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሄዎች ናቸው ብለን እንውሰድ። $y=c_1y_1+c_2y_2$ን በስሌት ($\ref{eqn:homogeneous_linear_ode}$) ውስጥ ካስቀመጥን

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

ይሆናል፣ ስለዚህ መለያ-አብራሪ ሆኖ ይታያል። ስለዚህ $y$ በክልል $I$ ላይ የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሄ ነው። $\blacksquare$

> የልዕለት መርህ ለአንድ-ዓይነት መስመራዊ ተራ ልዩነት ስሌቶች ብቻ የሚሠራ ሲሆን፣ ለአንድ-ዓይነት ያልሆኑ መስመራዊ ስሌቶች ወይም ለመስመራዊ ያልሆኑ ስሌቶች እንደማይሠራ ልብ ይበሉ።
{: .prompt-warning }

## መሠረት እና አጠቃላይ መፍትሄ
### በ1ኛ ደረጃ ተራ ልዩነት ስሌቶች ውስጥ ያሉ አስፈላጊ ጽንሰ-ሐሳቦችን እንደገና ማስታወስ
ከዚህ በፊት [የሞዴሊንግ(Modeling) መሠረታዊ ጽንሰ-ሐሳቦች](/posts/Basic-Concepts-of-Modeling/) ውስጥ እንደተመለከትነው፣ ለ1ኛ ደረጃ ተራ ልዩነት ስሌት የመነሻ ዋጋ ችግር(Initial Value Problem) ከተራ ልዩነት ስሌቱ እና ከመነሻ ሁኔታ(initial condition) $y(x_0)=y_0$ የተዋቀረ ነው። የመነሻ ሁኔታው በተሰጠው ተራ ልዩነት ስሌት አጠቃላይ መፍትሄ ውስጥ ያለውን ነጻ ቋሚ $c$ ለመወሰን ያስፈልጋል፣ እንዲህ ተወስኖ የሚገኘውን መፍትሄ ልዩ መፍትሄ ብለን እንጠራዋለን። አሁን እነዚህን ጽንሰ-ሐሳቦች ወደ 2ኛ ደረጃ ተራ ልዩነት ስሌቶች እናስፋፋ።

### የመነሻ ዋጋ ችግር እና የመነሻ ሁኔታዎች
ለ2ኛ ደረጃ አንድ-ዓይነት ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) **የመነሻ ዋጋ ችግር(initial value problem)** የተሰጠው ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) እና 2 **የመነሻ ሁኔታዎች(initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

ከእነዚህ የተዋቀረ ነው። እነዚህ ሁኔታዎች የተራ ልዩነት ስሌቱ የ**አጠቃላይ መፍትሄ(general solution)**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

ውስጥ ያሉትን 2 ነጻ ቋሚዎች $c_1$ እና $c_2$ ለመወሰን ያስፈልጋሉ።

### መስመራዊ ገለልተኝነት እና መስመራዊ ጥገኝነት
እዚህ ላይ ለጥቂት ጊዜ የመስመራዊ ገለልተኝነትና የመስመራዊ ጥገኝነት ጽንሰ-ሐሳቦችን እንመልከት። በኋላ መሠረትን ለመግለጽ ይህን መረዳት ያስፈልጋል።  
ሁለት ተግባሮች $y_1$ እና $y_2$ በተገለጹበት ክልል $I$ ላይ ባሉ ሁሉም ነጥቦች

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ እና }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

ከሆነ እነዚህ ሁለት ተግባሮች $y_1$ እና $y_2$ በክልል $I$ ላይ **መስመራዊ ገለልተኛ(linearly independent)** ናቸው እንላለን፣ ካልሆነ ግን $y_1$ እና $y_2$ **መስመራዊ ጥገኛ(linearly dependent)** ናቸው እንላለን።

$y_1$ እና $y_2$ መስመራዊ ጥገኛ ከሆኑ (ማለትም አረፍተ ነገር ($\ref{eqn:linearly_independent}$) እውነት ካልሆነ)፣ $k_1 \neq 0$ ወይም $k_2 \neq 0$ ስለሆነ የስሌት ($\ref{eqn:linearly_independent}$)ን ሁለት ጎኖች በማካፈል

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{ወይም} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

በሚለው መልኩ መጻፍ ይቻላል፣ ስለዚህም $y_1$ እና $y_2$ ተመጣጣኝ እንደሆኑ ማወቅ ይቻላል።

### መሠረት፣ አጠቃላይ መፍትሄ፣ ልዩ መፍትሄ
ወደ ዋናው ርዕስ እንመለስ፤ ስሌት ($\ref{eqn:general_sol}$) አጠቃላይ መፍትሄ እንዲሆን $y_1$ እና $y_2$ የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሄዎች መሆን አለባቸው፣ በተጨማሪም በክልል $I$ ላይ እርስ በርሳቸው ያልተመጣጠኑ እና መስመራዊ ገለልተኛ(linearly independent) መሆን አለባቸው። እነዚህን ሁኔታዎች የሚያሟሉ፣ በክልል $I$ ላይ መስመራዊ ገለልተኛ የሆኑ የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሄዎች ጥንድ(pair) $(y_1, y_2)$ን በክልል $I$ ላይ የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሄዎች **መሠረት(basis)** ወይም **መሠረታዊ ስርዓት(fundamental system)** እንላለን።

የመነሻ ሁኔታዎችን በመጠቀም በአጠቃላይ መፍትሄ ($\ref{eqn:general_sol}$) ውስጥ ያሉትን ሁለት ቋሚዎች $c_1$ እና $c_2$ በመወሰን፣ በነጥብ $(x_0, K_0)$ የሚያልፍ እና በዚያ ነጥብ ላይ ያለው የታንጀንት አዝማሚያ $K_1$ የሆነ ልዩ አንድ መፍትሄ እናገኛለን። ይህን የተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) **ልዩ መፍትሄ(particular solution)** እንላለን።

ስሌት ($\ref{eqn:homogeneous_linear_ode}$) በክፍት ክልል $I$ ላይ ቀጣይ ከሆነ አስፈላጊ በሆነ መልኩ አጠቃላይ መፍትሄ ይኖረዋል፣ እና ይህ አጠቃላይ መፍትሄ ሊኖሩ የሚችሉ ሁሉንም ልዩ መፍትሄዎች ይዟል። ማለትም በዚህ ሁኔታ ስሌት ($\ref{eqn:homogeneous_linear_ode}$) ከአጠቃላይ መፍትሄ ሊገኝ የማይችል ልዩ ያልተለመደ መፍትሄ(singular solution) አይኖረውም።

## የደረጃ መቀነስ (reduction of order)
ለ2ኛ ደረጃ አንድ-ዓይነት ተራ ልዩነት ስሌት አንድ መፍትሄ ማግኘት ከተቻለ፣ ከዚህ መፍትሄ ጋር መስመራዊ ገለልተኛ የሆነ ሁለተኛ መፍትሄ፣ ማለትም መሠረትን፣ እንደሚከተለው 1ኛ ደረጃ ተራ ልዩነት ስሌት በመፍታት ማግኘት ይቻላል። ይህን ዘዴ **የደረጃ መቀነስ(reduction of order)** ብለን እንጠራዋለን።

<u>$f(x)y^{\prime\prime}$ ሳይሆን $y^{\prime\prime}$ ያለው መደበኛ ቅጽ ያለው</u> 2ኛ ደረጃ አንድ-ዓይነት ተራ ልዩነት ስሌት

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

ስለሆነ፣ በክፍት ክልል $I$ ላይ የዚህን ስሌት አንድ መፍትሄ $y_1$ እንደምናውቅ እንውሰድ።

አሁን የምንፈልገውን ሁለተኛ መፍትሄ $y_2 = uy_1$ ብለን እናስቀምጥ፣

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

እነዚህን በስሌቱ ውስጥ ካስገባን

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

እናገኛለን። $u^{\prime\prime}$፣ $u^{\prime}$፣ $u$ የሚያካትቱ አካሎችን በተናጠል ከሰበሰብን በኋላ

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

ይሆናል። ግን $y_1$ የተሰጠው ስሌት መፍትሄ ስለሆነ፣ በመጨረሻው ቅንፍ ውስጥ ያለው ንግግር $0$ ነው፣ ስለዚህ $u$ ያለው አካል ይጠፋል እና $u^{\prime}$ እና $u^{\prime\prime}$ ላይ ብቻ የተመሠረተ ተራ ልዩነት ስሌት ይቀራል። የቀረውን ይህን ተራ ልዩነት ስሌት ሁለት ጎኖቹን በ$y_1$ ከፍለን፣ $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$ ብለን ካስቀመጥን የሚከተለውን 1ኛ ደረጃ ተራ ልዩነት ስሌት እናገኛለን።

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[የተለዋዋጮች መለያየት](/posts/Separation-of-Variables/) በመጠቀም ካዘጋጀንና ካካተትን

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

ይሆናል፣ እና በሁለት ጎኖቹ ላይ ኤክስፖነንሺያል ተግባር ከተጠቀምን በመጨረሻ

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

እናገኛለን። ከዚህ በፊት $U=u^{\prime}$ ብለን አስቀምጠን ነበር፣ ስለዚህ $u=\int U dx$ ይሆናል፣ እና የምንፈልገው ሁለተኛ መፍትሄ $y_2$ የሚከተለው ነው።

$$ y_2 = uy_1 = y_1 \int U dx $$

$\cfrac{y_2}{y_1} = u = \int U dx$ ከ$U>0$ በላይ ቋሚ ሊሆን አይችልም፣ ስለዚህ $y_1$ እና $y_2$ የመፍትሄዎች መሠረት ይፈጥራሉ።

### የደረጃ መቀነስ መተግበሪያዎች
አጠቃላይ 2ኛ ደረጃ ተራ ልዩነት ስሌት $F(x, y, y^\prime, y^{\prime\prime})=0$ መስመራዊ ይሁን ወይም መስመራዊ ያልሆነ ምንም ቢሆን፣ $y$ በግልጽ አይነት የማይታይ ከሆነ፣ ወይም $x$ በግልጽ አይነት የማይታይ ከሆነ፣ ወይም ከላይ እንዳየነው አንድ-ዓይነት መስመራዊ ሲሆን አንድ መፍትሄ አስቀድሞ የሚታወቅ ከሆነ የደረጃ መቀነስ በመጠቀም ወደ 1ኛ ደረጃ ማውረድ ይቻላል።

#### $y$ በግልጽ አይነት የማይታይ ከሆነ
$F(x, y^\prime, y^{\prime\prime})=0$ ውስጥ $z=y^{\prime}$ ብለን ካስቀመጥን፣ ለ$z$ የ1ኛ ደረጃ ተራ ልዩነት ስሌት $F(x, z, z^{\prime})$ ወደሚሆነው ማውረድ ይቻላል።

#### $x$ በግልጽ አይነት የማይታይ ከሆነ
$F(y, y^\prime, y^{\prime\prime})=0$ ውስጥ $z=y^{\prime}$ ብለን ካስቀመጥን፣ $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$ ስለሚሆን $y$ የገለልተኛ ተለዋዋጭ $x$ ሚናን የሚተካ ስለሆነ፣ ለ$z$ የ1ኛ ደረጃ ተራ ልዩነት ስሌት $F(y,z,z^\prime)$ ወደሚሆነው ማውረድ ይቻላል።
