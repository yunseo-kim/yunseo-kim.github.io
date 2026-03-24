---
title: "ያልተወሰኑ ኮኤፊሺየንቶች ዘዴ"
description: "ለተወሰኑ ቅርጾች ያላቸው ቋሚ-ኮኤፊሺየንት ያልሆሞጂኒየስ መስመራዊ ODE-ዎች የመጀመሪያ እሴት ችግሮችን በቀላሉ የሚፈታ እና በንዝረት ስርዓቶችና RLC ወረዳዎች በተደጋጋሚ የሚጠቅም የያልተወሰኑ ኮኤፊሺየንቶች ዘዴን እንመልከት።"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## አጭር ማጠቃለያ
> - **የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ** የሚተገበርባቸው:
>   - **ቋሚ ኮኤፊሺየንቶች $a$ እና $b$** ያላቸው
>   - ግቤቱ $r(x)$ ኤክስፖነንሻል ፋንክሽን, የ $x$ ኃይል, $\cos$ ወይም $\sin$, ወይም እነዚህን ፋንክሽኖች በመደመርና በማባዛት የተገነባ የሆነ
>   - መስመራዊ ተራ ዲፈረንሻል ስሌት $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **ለያልተወሰኑ ኮኤፊሺየንቶች ዘዴ የምርጫ ደንቦች**  
>   - **(a) መሠረታዊ ደንብ(basic rule)**: በስሌት ($\ref{eqn:linear_ode_with_constant_coefficients}$) ውስጥ $r(x)$ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ካሉት ፋንክሽኖች አንዱ ከሆነ, በተመሳሳይ ረድፍ ያለውን $y_p$ እንመርጣለን, እና $y_p$ እና አመጣጦቹን በስሌት ($\ref{eqn:linear_ode_with_constant_coefficients}$) ውስጥ በመተካት ያልተወሰኑትን ኮኤፊሺየንቶች እንወስናለን።  
>   - **(b) የማሻሻያ ደንብ(modification rule)**: ለ $y_p$ የተመረጠው አባል ከስሌት ($\ref{eqn:linear_ode_with_constant_coefficients}$) ጋር የሚዛመደው ሆሞጂኒየስ ተራ ዲፈረንሻል ስሌት $y^{\prime\prime} + ay^{\prime} + by = 0$ መፍትሄ ከሆነ, ይህን አባል በ $x$ (ወይም ይህ መፍትሄ የሆሞጂኒየስ ስሌቱ የባህሪ ስሌት ድርብ ሥር ከሆነ $x^2$) እንባዛዋለን።  
>   - **(c) የድምር ደንብ(sum rule)**: $r(x)$ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ያሉ ፋንክሽኖች ድምር ከሆነ, በሁለተኛው አምድ ያሉ ተዛማጅ ረድፎች ፋንክሽኖች ድምርን $y_p$ አድርገን እንመርጣለን።
>
> | የ $r(x)$ አባል | ለ $y_p(x)$ የምርጫ ቅጽ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## ቅድመ ዕውቀቶች
- [2ኛ ደረጃ ሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌቶች(Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [ቋሚ ኮኤፊሺየንቶች ያሏቸው 2ኛ ደረጃ ሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌቶች](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [ኦይለር-ኮሺ ስሌት(Euler-Cauchy equation)](/posts/euler-cauchy-equation/)
- [ውሮንስኪያን(Wronskian), የመፍትሄ መኖር እና አንድነት](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [2ኛ ደረጃ ያልሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌቶች(Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)
- ቬክተር ቦታ, መስመራዊ ስፋት(ሊኒየር አልጀብራ)

## ያልተወሰኑ ኮኤፊሺየንቶች ዘዴ
$r(x) \not\equiv 0$ የሆነ 2ኛ ደረጃ ያልሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌት

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

እና ከዚህ ያልሆሞጂኒየስ ስሌት ጋር የሚዛመደው ሆሞጂኒየስ ተራ ዲፈረንሻል ስሌት

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

እንመልከት።

ከዚህ ቀደም [2ኛ ደረጃ ያልሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌቶች(Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/) ላይ እንዳየነው, ለያልሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) የመጀመሪያ እሴት ችግርን ለመፍታት መጀመሪያ ሆሞጂኒየስ ስሌት ($\ref{eqn:homogeneous_linear_ode}$) በመፍታት $y_h$ ማግኘት አለብን, ከዚያም የስሌት ($\ref{eqn:nonhomogeneous_linear_ode}$) አንድ መፍትሄ $y_p$ በማግኘት አጠቃላይ መፍትሄውን

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

ማግኘት አለብን። እንግዲህ $y_p$ እንዴት እናገኛለን? $y_p$ ለማግኘት አጠቃላይ ዘዴው **የመለኪያ ለውጥ ዘዴ(method of variation of parameters)** ቢሆንም, በአንዳንድ ሁኔታዎች ከእርሱ በእጅጉ ቀላል የሆነውን **የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ(method of undetermined coefficients)** መተግበር እንችላለን። በተለይም, በንዝረት ስርዓቶች እና በ RLC የኤሌክትሪክ ወረዳ ሞዴሎች ላይ ስለሚተገበር በምህንድስና ብዙ ጊዜ የሚጠቀሙበት ዘዴ ነው።

የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ ለ **ቋሚ ኮኤፊሺየንቶች $a$ እና $b$** ያላቸው, እና ግቤቱ $r(x)$ ኤክስፖነንሻል ፋንክሽን, የ $x$ ኃይል, $\cos$ ወይም $\sin$, ወይም እነዚህን ፋንክሽኖች በመደመርና በማባዛት የተገነባ የሆነ መስመራዊ ተራ ዲፈረንሻል ስሌት

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

ተስማሚ ነው። ይህ አይነት $r(x)$ ከራሱ ጋር ተመሳሳይ ቅርጽ ያላቸውን አመጣጦች እንደሚኖሩት ያለው ነጥብ የዚህ ዘዴ ዋና ሐሳብ ነው። ይህን ዘዴ ለመተግበር, ከ $r(x)$ ጋር ተመሳሳይ ቅርጽ ያለው ነገር ግን ራሱን እና አመጣጦቹን በተሰጠው ስሌት ውስጥ በመተካት የሚወሰኑ ያልታወቁ ኮኤፊሺየንቶች ያሉትን $y_p$ እንመርጣለን። በምህንድስና አግባብ ያላቸው አስፈላጊ የ $r(x)$ ቅርጾች ላይ ተስማሚ $y_p$ ለመምረጥ የሚረዱ ደንቦች እነዚህ ናቸው።

> **ለያልተወሰኑ ኮኤፊሺየንቶች ዘዴ የምርጫ ደንቦች**  
> **(a) መሠረታዊ ደንብ(basic rule)**: በስሌት ($\ref{eqn:linear_ode_with_constant_coefficients}$) ውስጥ $r(x)$ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ካሉት ፋንክሽኖች አንዱ ከሆነ, በተመሳሳይ ረድፍ ያለውን $y_p$ እንመርጣለን, እና $y_p$ እና አመጣጦቹን በስሌት ($\ref{eqn:linear_ode_with_constant_coefficients}$) ውስጥ በመተካት ያልተወሰኑትን ኮኤፊሺየንቶች እንወስናለን።  
> **(b) የማሻሻያ ደንብ(modification rule)**: ለ $y_p$ የተመረጠው አባል ከስሌት ($\ref{eqn:linear_ode_with_constant_coefficients}$) ጋር የሚዛመደው ሆሞጂኒየስ ተራ ዲፈረንሻል ስሌት $y^{\prime\prime} + ay^{\prime} + by = 0$ መፍትሄ ከሆነ, ይህን አባል በ $x$ (ወይም ይህ መፍትሄ የሆሞጂኒየስ ስሌቱ የባህሪ ስሌት ድርብ ሥር ከሆነ $x^2$) እንባዛዋለን።  
> **(c) የድምር ደንብ(sum rule)**: $r(x)$ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ያሉ ፋንክሽኖች ድምር ከሆነ, በሁለተኛው አምድ ያሉ ተዛማጅ ረድፎች ፋንክሽኖች ድምርን $y_p$ አድርገን እንመርጣለን።
>
> | የ $r(x)$ አባል | ለ $y_p(x)$ የምርጫ ቅጽ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

ይህ ዘዴ ቀላል ብቻ ሳይሆን ራስ-አስተካካይነት እንዳለው የሚቆጠር ጥቅምም አለው። $y_p$ በትክክል ካልተመረጠ ወይም በጣም ጥቂት አባላት ከተመረጡ, ተቃርኖ ይከሰታል፤ እንዲሁም ከሚያስፈልገው በላይ ብዙ አባላት ከተመረጡ, አላስፈላጊ አባላት ኮኤፊሺየንቶች $0$ ሆነው ትክክለኛው ውጤት ይገኛል። ስለዚህ ይህን ዘዴ ሲተገብሩ የሆነ ነገር ቢሳሳት እንኳን, በመፍትሄ ሂደቱ ውስጥ በተፈጥሮ ማስተዋል ይቻላል፤ ስለዚህ ከላይ ባሉት የምርጫ ደንቦች መሠረት በአጠቃላይ ተገቢ የሆነ $y_p$ ከተመረጠ, ከልብ ያለ ጫና መሞከር ይቻላል።

### የድምር ደንብ ማረጋገጫ
$r(x) = r_1(x) + r_2(x)$ ቅርጽ ያለውን ያልሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌት

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

እንመልከት። አሁን ተመሳሳይ ግራ ክፍል ያላቸው, ግን እንደ ግቤት $r_1$, $r_2$ ያላቸውን ሁለት ስሌቶች

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

እያንዳንዳቸው ${y_p}_1$, ${y_p}_2$ መፍትሄ እንዳላቸው እንግምት። የተሰጠውን ስሌት ግራ ክፍል $L[y]$ ብለን ከጻፍን, በ $L[y]$ መስመራዊነት ምክንያት $y_p = {y_p}_1 + {y_p}_2$ ላይ የሚከተለው ስለሚሟላ, የድምር ደንብ ይረጋገጣል።

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## ምሳሌ: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
በመሠረታዊው ደንብ (a) መሠረት $y_p = Ce^{\gamma x}$ ብለን እንወስድ እና ይህን በተሰጠው ስሌት $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$ ውስጥ ካስተካከልን

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### $\gamma^2 + a\gamma + b \neq 0$ በሚሆንበት ጊዜ
እንደሚከተለው ያልተወሰነውን ኮኤፊሺየንት $C$ መወሰን እና $y_p$ ማግኘት እንችላለን።

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### $\gamma^2 + a\gamma + b = 0$ በሚሆንበት ጊዜ
በዚህ ሁኔታ የማሻሻያውን ደንብ (b) መተግበር አለብን። መጀመሪያ $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ መሆኑን በመጠቀም, የሆሞጂኒየስ ተራ ዲፈረንሻል ስሌት $y^{\prime\prime} + ay^{\prime} + by = 0$ የባህሪ ስሌት ሥሮችን እንፈልግ።

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

ከዚህ የሆሞጂኒየስ ስሌቱን መሠረት

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

እናገኛለን።

#### $\gamma \neq -a-\gamma$ በሚሆንበት ጊዜ
ለ $y_p$ መጀመሪያ የተመረጠው $Ce^{\gamma x}$ ከተሰጠው ስሌት ጋር የሚዛመደው ሆሞጂኒየስ ስሌት ድርብ ሥር ያልሆነ መፍትሄ ስለሆነ, በየማሻሻያው ደንብ (b) መሠረት ይህን አባል በ $x$ እንባዛው እና $y_p = Cxe^{\gamma x}$ ብለን እንወስዳለን።

አሁን ይህን የተሻሻለውን $y_p$ በተሰጠው ስሌት $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ ውስጥ እንደገና ካስተካከልን

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### $\gamma = -a-\gamma$ በሚሆንበት ጊዜ
በዚህ ሁኔታ ለ $y_p$ መጀመሪያ የተመረጠው $Ce^{\gamma x}$ ከተሰጠው ስሌት ጋር የሚዛመደው ሆሞጂኒየስ ስሌት ድርብ ሥር ስለሆነ, በየማሻሻያው ደንብ (b) መሠረት ይህን አባል በ $x^2$ እንባዛው እና $y_p = Cx^2 e^{\gamma x}$ ብለን እንወስዳለን።

አሁን ይህን የተሻሻለውን $y_p$ በተሰጠው ስሌት $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ ውስጥ እንደገና ካስተካከልን

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ መስፋፋት: $r(x)$ የፋንክሽኖች ውጤት ቅርጽ ሲሆን
$r(x) = k x^n e^{\alpha x}\cos(\omega x)$ ቅርጽ ያለውን ያልሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌት

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

እንመልከት። $r(x)$ እንደዚህ ያለ ኤክስፖነንሻል ፋንክሽን $e^{\alpha x}$, የ $x$ ኃይል $x^m$, $\cos{\omega x}$ ወይም $\sin{\omega x}$ (እዚህ $\cos$ ብለን እንመስላለን, እንዲህ ብለን ማስቀመጥ አጠቃላይነቱን አያጎድልም), ወይም እነዚህ ፋንክሽኖች ድምርና ውጤት ከሆነ (ማለትም, ቀደም ብሎ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ባሉ ፋንክሽኖች ድምርና ውጤት መግለጽ ከተቻለ), በተመሳሳይ ሰንጠረዥ ሁለተኛ አምድ ውስጥ ያሉ ፋንክሽኖች ድምርና ውጤት ቅርጽ ያለው የስሌቱ መፍትሄ $y_p$ እንዳለ እናሳያለን።

> ጥብቅ ማረጋገጫ ለማድረግ ሊኒየር አልጀብራን ተጠቅመን የገለጽናቸው ክፍሎች አሉ፤ እነዚህ ክፍሎች በ \* ተመልክተዋል። እነዚያን ክፍሎች በመዝለል የቀሩትን ብቻ ብታነቡም አጠቃላይ ግንዛቤ ለማግኘት ችግር የለውም።
{: .prompt-tip }

### የቬክተር ቦታ $V$ መግለጫ\*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

የሆነ $r(x)$ ላይ, $r(x) \in V$ እንዲሆን የቬክተር ቦታ $V$ እንደሚከተለው ማስያዝ ይቻላል።

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### የኤክስፖነንሻል ፋንክሽኖች, የፖሊኖሚያል ፋንክሽኖች, እና የትሪጎኖሜትሪክ ፋንክሽኖች አመጣጥ ቅርጾች
ቀደም ብሎ በሰንጠረዡ የመጀመሪያ አምድ የተሰጡት መሠረታዊ ፋንክሽኖች አመጣጥ ቅርጾች እነዚህ ናቸው።
- ኤክስፖነንሻል ፋንክሽን: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- ፖሊኖሚያል ፋንክሽን: $\cfrac{d}{dx}x^m = mx^{m-1}$
- ትሪጎኖሜትሪክ ፋንክሽን: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

እነዚህን ፋንክሽኖች በመለየት የሚገኙት አመጣጦችም <u>በተመሳሳይ ዓይነት ፋንክሽኖች ድምር</u> ሊገለጹ ይችላሉ።

ስለዚህ, ፋንክሽኖች $f$ እና $g$ ከላይ ያሉ ፋንክሽኖች ወይም እነርሱ ድምር ከሆኑ, $r(x) = f(x)g(x)$ ላይ የውጤት ልዩነት ሕግን በመተግበር

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

እናገኛለን፤ እዚህ $f$, $f^{\prime}$, $f^{\prime\prime}$ እና $g$, $g^{\prime}$, $g^{\prime\prime}$ ሁሉም ኤክስፖነንሻል ፋንክሽኖች, ፖሊኖሚያል ፋንክሽኖች, ትሪጎኖሜትሪክ ፋንክሽኖች ድምር ወይም በቋሚ ቁጥር የተባዙ ቅርጾች ናቸው። ስለዚህ $r^{\prime}(x) = (fg)^{\prime}$ እና $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ እንዲሁም እንደ $r(x)$ በእነዚህ ፋንክሽኖች ድምርና ውጤት ሊገለጹ ይችላሉ።

### $V$ በልዩነት ኦፕሬሽን $D$ እና በመስመራዊ ተለዋዋጭ $L$ ስር የማይለወጥ መሆን\*
ማለትም, $r(x)$ ብቻ ሳይሆን $r^{\prime}(x)$ እና $r^{\prime\prime}(x)$ ደግሞ $x^k e^{\alpha x}\cos(\omega x)$ ቅርጽ ያላቸው አባላትና $x^k e^{\alpha x}\sin(\omega x)$ ቅርጽ ያላቸው አባላት የመስመራዊ ጥምረት ስለሆኑ

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

ይህን ሐሳብ $r(x)$ ብቻ ሳይገድብ ከዚህ በፊት በተገለጸው የቬክተር ቦታ $V$ ሁሉም አባላት ላይ የልዩነት ኦፕሬተር $D$ በማስገባት አጠቃላይ ቅጽ ላይ እንጻፍ ከሆነ, *የቬክተር ቦታ $V$ በልዩነት ኦፕሬሽን $D$ ስር ዝግ ነው* ማለት ነው። ስለዚህ የተሰጠውን ስሌት ግራ ክፍል $y^{\prime\prime} + ay^{\prime} + by$ ን $L[y]$ ብለን ከጻፍን, *$V$ በ $L$ ስር የማይለወጥ(invariant) ነው*።

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

$r(x) \in V$ እና $V$ በ $L$ ስር የማይለወጥ ስለሆነ, $L[y_p] = r$ የሚያሟላ የ $V$ ሌላ አባል $y_p$ አለ።

$$ \exists y_p \in V: L[y_p] = r $$

### አንሳትዝ(Ansatz)
ስለዚህ, ሁሉንም የሚቻሉ የውጤት ቅርጽ አባላት ድምር እንዲሆን ተገቢውን $y_p$ በያልተወሰኑት ኮኤፊሺየንቶች $A_0, A_1, \dots, A_n$ እና $K$, $M$ በመጠቀም እንደሚከተለው ከመረጥን, በመሠረታዊው ደንብ (a) እና በየማሻሻያው ደንብ (b) መሠረት $y_p$ (ወይም $xy_p$, $x^2y_p$) እና አመጣጦቹን በተሰጠው ስሌት ውስጥ በመተካት ያልተወሰኑትን ኮኤፊሺየንቶች መወሰን ይቻላል። በዚህ ጊዜ $n$ በ $r(x)$ ውስጥ ያለው የ $x$ ዲግሪ መሠረት ይወሰናል።

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> ከተሰጠው ግቤት $r(x)$ ውስጥ የተለያዩ ብዙ $\alpha_i$, $\omega_j$ እሴቶች ካሉ, ለእያንዳንዱ $\alpha_i$ እና $\omega_j$ እሴት የሚቻሉ ሁሉንም $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ እና $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ ቅርጽ ያላቸው አባላት ሳይቀሩ እንዲካተቱ $y_p$ መመርጥ አለበት።  
> የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ ጥቅሙ ቀላልነቱ ስለሆነ, የመፍትሄ መነሻ ግምቱ(ansatz) በጣም ውስብስብ ሆኖ ይህን ጥቅም ካጠፋ, ይልቁንም ከዚህ በኋላ የምናየውን የመለኪያ ለውጥ ዘዴ መተግበር ይሻላል።
{: .prompt-warning }

## የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ መስፋፋት: ኦይለር-ኮሺ ስሌት(Euler-Cauchy equation)
[ቋሚ ኮኤፊሺየንቶች ያሏቸው 2ኛ ደረጃ ሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌቶች](/posts/homogeneous-linear-odes-with-constant-coefficients/) ብቻ ሳይሆን, [ኦይለር-ኮሺ ስሌት(Euler-Cauchy equation)](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

ላይም የያልተወሰኑ ኮኤፊሺየንቶች ዘዴን መጠቀም ይቻላል።

### ተለዋዋጭ መተካት
[$x = e^t$ በማድረግ ወደ ቋሚ ኮኤፊሺየንቶች ያላቸው 2ኛ ደረጃ ሆሞጂኒየስ መስመራዊ ተራ ዲፈረንሻል ስሌቶች መለወጥ](/posts/euler-cauchy-equation/#ወደ-ቋሚ-ኮኤፊሺየንቶች-ያላቸው-2ኛ-ደረጃ-ሆሞጂኒየስ-መስመራዊ-ተራ-ዲፈረንሻል-ስሌቶች-መለወጥ) ካደረግን

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

ይሆናል፤ ስለዚህ ኦይለር-ኮሺ ስሌቱን እንደሚከተለው በ $t$ ላይ ቋሚ ኮኤፊሺየንት ያለው መስመራዊ ተራ ዲፈረንሻል ስሌት መቀየር እንደሚቻል ቀደም ብለን አይተናል።

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

አሁን በስሌት ($\ref{eqn:substituted}$) ላይ [ከዚህ ቀደም ያየነውን የያልተወሰኑ ኮኤፊሺየንቶች ዘዴ](#ያልተወሰኑ-ኮኤፊሺየንቶች-ዘዴ) በተመሳሳይ መንገድ ለ $t$ እንተግብር, መጨረሻም $t = \ln x$ መሆኑን በመጠቀም በ $x$ ላይ ያለውን መፍትሄ እናገኛለን።

### $r(x)$ የ $x$ ኃይሎች, የተፈጥሮ ሎጋሪትም, ወይም እነዚህ ፋንክሽኖች ድምርና ውጤት በሚሆንበት ጊዜ
በተለይ, ግቤቱ $r(x)$ የ $x$ ኃይሎች, የተፈጥሮ ሎጋሪትም, ወይም እነዚህ ፋንክሽኖች ድምርና ውጤት ከሆነ, ለኦይለር-ኮሺ ስሌት የሚከተሉትን የምርጫ ደንቦች በመጠቀም ተገቢውን $y_p$ በቀጥታ መምረጥ ይቻላል።

> **ለያልተወሰኑ ኮኤፊሺየንቶች ዘዴ የምርጫ ደንቦች: ለኦይለር-ኮሺ ስሌት**  
> **(a) መሠረታዊ ደንብ(basic rule)**: በስሌት ($\ref{eqn:euler_cauchy}$) ውስጥ $r(x)$ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ካሉት ፋንክሽኖች አንዱ ከሆነ, በተመሳሳይ ረድፍ ያለውን $y_p$ እንመርጣለን, እና $y_p$ እና አመጣጦቹን በስሌት ($\ref{eqn:euler_cauchy}$) ውስጥ በመተካት ያልተወሰኑትን ኮኤፊሺየንቶች እንወስናለን።  
> **(b) የማሻሻያ ደንብ(modification rule)**: ለ $y_p$ የተመረጠው አባል ከስሌት ($\ref{eqn:euler_cauchy}$) ጋር የሚዛመደው ሆሞጂኒየስ ተራ ዲፈረንሻል ስሌት $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ መፍትሄ ከሆነ, ይህን አባል በ $\ln{x}$ (ወይም ይህ መፍትሄ የሆሞጂኒየስ ስሌቱ የባህሪ ስሌት ድርብ ሥር ከሆነ $(\ln{x})^2$) እንባዛዋለን።  
> **(c) የድምር ደንብ(sum rule)**: $r(x)$ በሰንጠረዡ የመጀመሪያ አምድ ውስጥ ያሉ ፋንክሽኖች ድምር ከሆነ, በሁለተኛው አምድ ያሉ ተዛማጅ ረድፎች ፋንክሽኖች ድምርን $y_p$ አድርገን እንመርጣለን።
>
> | የ $r(x)$ አባል | ለ $y_p(x)$ የምርጫ ቅጽ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

እንዲህ በማድረግ በአግባብ አስፈላጊ ቅርጽ ያለው ግቤት $r(x)$ ላይ, [ተለዋዋጭ መተካት](#ተለዋዋጭ-መተካት) በማድረግ ከሚገኘው ጋር ተመሳሳይ የሆነውን $y_p$ ከዚያ በላይ ፈጣንና ቀላል በሆነ መንገድ ማግኘት ይቻላል። ከዚህ ቀደም ባየነው [የመጀመሪያው የምርጫ ደንብ](#ያልተወሰኑ-ኮኤፊሺየንቶች-ዘዴ) ውስጥ በ $x$ ምትክ $\ln{x}$ ብቻ በመተካት, ይህን ለኦይለር-ኮሺ ስሌት የሚሆነውን የምርጫ ደንብ ማውጣት ይቻላል።
