---
title: "የ2ኛ ደረጃ አል-ሆሞጄንየስ መስመራዊ ተራ ልዩነት ስሌቶች (Nonhomogeneous Linear ODEs of Second Order)"
description: "የ2ኛ ደረጃ አል-ሆሞጄንየስ መስመራዊ ተራ ልዩነት ስሌቶች አጠቃላይ መፍትሔ ከተዛማጅ ሆሞጄንየስ ስሌት መፍትሔ ጋር ያለውን ግንኙነት ይመለከታል፣ እንዲሁም የአጠቃላይ መፍትሔ መኖርና የልዩ መፍትሔ አለመኖርን ያሳያል።"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - የ2ኛ ደረጃ አል-ሆሞጄንየስ መስመራዊ ተራ ልዩነት ስሌት $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$ ၏ **አጠቃላይ መፍትሔ**:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: የሆሞጄንየስ ተራ ልዩነት ስሌት $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ አጠቃላይ መፍትሔ $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: ለተዛማጁ አል-ሆሞጄንየስ ተራ ልዩነት ስሌት የተለየ መፍትሔ
> - የምላሽ ክፍሉ $y_p$ የሚወሰነው በግቤት $r(x)$ ብቻ ሲሆን፣ ለአንድ አይነት አል-ሆሞጄንየስ ተራ ልዩነት ስሌት የመጀመሪያ ሁኔታዎች ቢለያዩም $y_p$ አይለወጥም። የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ሁለት የተለዩ መፍትሔዎች ልዩነት ደግሞ ተዛማጁ ሆሞጄንየስ ተራ ልዩነት ስሌት መፍትሔ ይሆናል።
> - **የአጠቃላይ መፍትሔ መኖር**: የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ኮኤፊሺየንቶች $p(x)$, $q(x)$ እና የግቤት ተግባር $r(x)$ ቀጣይ ከሆኑ አጠቃላይ መፍትሔ ሁልጊዜ ይኖራል
> - **የልዩ መፍትሔ አለመኖር**: አጠቃላይ መፍትሔው ሁሉንም መፍትሔዎች ይይዛል (ማለትም ልዩ መፍትሔ የለም)
{: .prompt-info }

## ቅድመ ዕውቀቶች
- [የ2ኛ ደረጃ ሆሞጄንየስ መስመራዊ ተራ ልዩነት ስሌቶች](/posts/homogeneous-linear-odes-of-second-order/)
- [ብሮንስኪያን(Wronskian), የመፍትሔ መኖር እና አንድነት](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## የ2ኛ ደረጃ አል-ሆሞጄንየስ መስመራዊ ተራ ልዩነት ስሌቶች አጠቃላይ መፍትሔ እና የተለየ መፍትሔ
የ2ኛ ደረጃ አል-ሆሞጄንየስ መስመራዊ ተራ ልዩነት ስሌት

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

እንመልከት። እዚህ $r(x) \not\equiv 0$ ነው። በክፍት ክልል $I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) **አጠቃላይ መፍትሔ** ማለት ከዚህ አል-ሆሞጄንየስ ተራ ልዩነት ስሌት ጋር የሚዛመደው ሆሞጄንየስ ተራ ልዩነት ስሌት

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

የአጠቃላይ መፍትሔው $y_h = c_1y_1 + c_2y_2$ እና የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) የተለየ መፍትሔ $y_p$ ድምር

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

በሚለው ቅርጽ ነው። በተጨማሪም በክልል $I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) **የተለየ መፍትሔ** ማለት በ$y_h$ ውስጥ ላሉ ማናቸውም ቋሚዎች $c_1$ እና $c_2$ ልዩ እሴቶችን በመመደብ ከስሌት ($\ref{eqn:general_sol}$) የሚገኘው መፍትሔ ነው።

በሌላ አነጋገር፣ በሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) ላይ በገለልተኛ ተለዋዋጭ $x$ ብቻ የሚወሰን ግቤት $r(x)$ ከተጨመረ፣ ከዚህ ጋር የሚዛመድ ክፍል $y_p$ በምላሹ ላይ ይጨመራል፤ ይህም የተጨመረው የምላሽ ክፍል $y_p$ ከመጀመሪያ ሁኔታዎች ጋር ግንኙነት ሳይኖረው በ$ r(x)$ ብቻ ይወሰናል። በኋላ እንደምናየው፣ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ማናቸውም ሁለት መፍትሔዎች $y_1$ እና $y_2$ ልዩነት ሲወሰድ (ማለትም ለሁለት የተለያዩ የመጀመሪያ ሁኔታዎች የሚሰጡ ሁለት የተለዩ መፍትሔዎች ልዩነት ሲወሰድ) ከመጀመሪያ ሁኔታዎች ነጻ የሆነው $y_p$ ክፍል ይጠፋል እና ${y_h}_1$ እና ${y_h}_2$ ልዩነት ብቻ ይቀራል፤ ይህም በ[የሱፐርፖዚሽን መርህ](/posts/homogeneous-linear-odes-of-second-order/#የሱፐርፖዚሽን-መርህ) መሠረት የስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሔ ይሆናል።

## በአል-ሆሞጄንየስ ተራ ልዩነት ስሌት መፍትሔዎችና ከእሱ ጋር ተዛማጅ በሆነው ሆሞጄንየስ ተራ ልዩነት ስሌት መፍትሔዎች መካከል ያለ ግንኙነት
> **ቲዎረም 1: በአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) መፍትሔዎችና በሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሔዎች መካከል ያለ ግንኙነት**  
> **(a)** በአንድ ክፍት ክልል $I$ ላይ የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) መፍትሔ $y$ እና የሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሔ $\tilde{y}$ ድምር በክልል $I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) መፍትሔ ነው። በተለይም ስሌት ($\ref{eqn:general_sol}$) በክልል $I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) መፍትሔ ነው።  
> **(b)** በክልል $I$ ላይ የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ሁለት መፍትሔዎች ልዩነት በክልል $I$ ላይ የሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሔ ነው።
{: .prompt-info }

### ማረጋገጫ
#### (a)
የስሌቶች ($\ref{eqn:nonhomogeneous_linear_ode}$) እና ($\ref{eqn:homogeneous_linear_ode}$) የግራ በኩል ክፍልን $L[y]$ ብለን እንሰይም። እንግዲህ በክልል $I$ ላይ ለስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ማንኛውም መፍትሔ $y$ እና ለስሌት ($\ref{eqn:homogeneous_linear_ode}$) ማንኛውም መፍትሔ $\tilde{y}$ የሚከተለው ይሟላል።

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
በክልል $I$ ላይ ለስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ማንኛውም ሁለት መፍትሔዎች $y$ እና $y^\*$ የሚከተለው ይሟላል።

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት አጠቃላይ መፍትሔ ሁሉንም መፍትሔዎች ይይዛል
ለሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) [አጠቃላይ መፍትሔው ሁሉንም መፍትሔዎች እንደሚይዝ እናውቃለን](/posts/wronskian-existence-and-uniqueness-of-solutions/#አጠቃላይ-መፍትሔ-ሁሉንም-መፍትሔዎች-ይይዛል)። ለአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ደግሞ ይህ እንደሚሠራ እናሳይ።

> **ቲዎረም 2: የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት አጠቃላይ መፍትሔ ሁሉንም መፍትሔዎች ይይዛል**  
> የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ኮኤፊሺየንቶች $p(x)$, $q(x)$ እና የግቤት ተግባር $r(x)$ በአንድ ክፍት ክልል $I$ ላይ ቀጣይ ከሆኑ፣ በክልል $I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ሁሉም መፍትሔዎች በክልል $I$ ላይ ያለው የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) አጠቃላይ መፍትሔ ($\ref{eqn:general_sol}$) ውስጥ ባለው $y_h$ የማንኛውም ቋሚዎች $c_1$ እና $c_2$ ላይ ተገቢ እሴቶችን በመመደብ ሊገኙ ይችላሉ።
{: .prompt-info }

### ማረጋገጫ
$y^\*$ በ$I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) አንድ መፍትሔ ይሁን፣ $x_0$ ደግሞ በክልል $I$ ውስጥ ያለ አንድ $x$ ይሁን። [ቀጣይ ተለዋዋጭ ኮኤፊሺየንቶች ያሉት የሆሞጄንየስ ተራ ልዩነት ስሌት አጠቃላይ መፍትሔ መኖር ቲዎረም](/posts/wronskian-existence-and-uniqueness-of-solutions/#የአጠቃላይ-መፍትሔ-መኖር) መሠረት $y_h = c_1y_1 + c_2y_2$ አለ፣ እና በኋላ የምንማረው **የመለኪያ ለውጥ ዘዴ(method of variation of parameters)** በመጠቀም $y_p$ ደግሞ ስለሚኖር በክልል $I$ ላይ የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) አጠቃላይ መፍትሔ ($\ref{eqn:general_sol}$) ይኖራል። አሁን ከዚህ በፊት በማረጋገጫው ያሳየነው ቲዎረም [1(b)](#በአል-ሆሞጄንየስ-ተራ-ልዩነት-ስሌት-መፍትሔዎችና-ከእሱ-ጋር-ተዛማጅ-በሆነው-ሆሞጄንየስ-ተራ-ልዩነት-ስሌት-መፍትሔዎች-መካከል-ያለ-ግንኙነት) መሠረት $Y = y^\* - y_p$ በክልል $I$ ላይ የሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) መፍትሔ ነው፣ እና በ$x_0$ ላይ

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

ነው። [የመነሻ እሴት ችግር መፍትሔ መኖርና አንድነት ቲዎረም](/posts/wronskian-existence-and-uniqueness-of-solutions/#የመነሻ-እሴት-ችግር-መፍትሔ-መኖርና-አንድነት-ቲዎረም) መሠረት በክልል $I$ ላይ ለእነዚህ መነሻ ሁኔታዎች $y_h$ ውስጥ ላሉት $c_1$, $c_2$ ተገቢ እሴቶችን በመመደብ የሚገኝ የሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:homogeneous_linear_ode}$) የተለየ መፍትሔ $Y$ ብቻውን ይኖራል። $y^\* = Y + y_p$ ስለሆነ፣ የአል-ሆሞጄንየስ ተራ ልዩነት ስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) ማንኛውም የተለየ መፍትሔ $y^\*$ ከአጠቃላይ መፍትሔው ($\ref{eqn:general_sol}$) ሊገኝ እንደሚችል አሳይተናል። $\blacksquare$
