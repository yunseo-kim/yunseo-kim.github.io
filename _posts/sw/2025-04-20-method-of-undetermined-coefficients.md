---
title: "Mbinu ya Vigawo Visivyojulikana"
description: "Tujifunze mbinu ya vigawo visivyojulikana, njia rahisi ya kutatua matatizo ya thamani ya awali kwa baadhi ya mlinganyo wa kawaida wa tofauti wa mstari usio homojeni wenye vigawo thabiti, inayotumika sana katika uhandisi kwa mifumo ya mtetemo na miundo ya saketi za umeme za RLC."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Mbinu ya vigawo visivyojulikana** hutumika kwa:
>   - mlinganyo wenye **vigawo thabiti $a$ na $b$**
>   - ambapo ingizo $r(x)$ limeundwa na funsi ya eksponenti, nguvu za $x$, $\cos$ au $\sin$, au jumla na bidhaa za funsi kama hizo
>   - yaani mlinganyo wa kawaida wa tofauti wa mstari $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Kanuni za kuchagua kwa mbinu ya vigawo visivyojulikana**  
>   - **(a) kanuni ya msingi (basic rule)**: Katika mlinganyo ($\ref{eqn:linear_ode_with_constant_coefficients}$), ikiwa $r(x)$ ni mojawapo ya funsi zilizo kwenye safu ya kwanza ya jedwali, chagua $y_p$ ya safu hiyo hiyo, kisha amua vigawo visivyojulikana kwa kuingiza $y_p$ na viambajengo vyake katika mlinganyo ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) kanuni ya marekebisho (modification rule)**: Ikiwa neno lililochaguliwa kama $y_p$ ni suluhisho la mlinganyo wa kawaida wa tofauti wa homojeni $y^{\prime\prime} + ay^{\prime} + by = 0$ unaolingana na mlinganyo ($\ref{eqn:linear_ode_with_constant_coefficients}$), basi lizidishe kwa $x$ (au kwa $x^2$ ikiwa suluhisho hilo linalingana na mzizi wa maradufu wa mlinganyo bainishi wa mlinganyo wa homojeni).  
>   - **(c) kanuni ya kujumlisha (sum rule)**: Ikiwa $r(x)$ ni jumla ya funsi zilizo kwenye safu ya kwanza ya jedwali, chagua kama $y_p$ jumla ya funsi zilizo kwenye safu ya pili katika mistari inayolingana.
>
> | Neno la $r(x)$ | Uteuzi wa $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Maarifa ya awali
- [Mlinganyo wa kawaida wa tofauti wa mstari wa homojeni wa mpangilio wa pili](/posts/homogeneous-linear-odes-of-second-order/)
- [Mlinganyo wa kawaida wa tofauti wa mstari wa homojeni wa mpangilio wa pili wenye vigawo thabiti](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Mlinganyo wa Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskian, uwepo na upekee wa suluhisho](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Mlinganyo wa kawaida wa tofauti wa mstari usio homojeni wa mpangilio wa pili](/posts/nonhomogeneous-linear-odes-of-second-order/)
- nafasi za vekta, linear span (aljebra ya mstari)

## Mbinu ya vigawo visivyojulikana
Fikiria mlinganyo wa kawaida wa tofauti wa mstari usio homojeni wa mpangilio wa pili ambapo $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

na mlinganyo wa kawaida wa tofauti wa homojeni unaolingana nao

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Kama tulivyoona hapo awali katika [Mlinganyo wa kawaida wa tofauti wa mstari usio homojeni wa mpangilio wa pili](/posts/nonhomogeneous-linear-odes-of-second-order/), ili kutatua tatizo la thamani ya awali kwa mlinganyo wa tofauti usio homojeni wa mstari ($\ref{eqn:nonhomogeneous_linear_ode}$), tunapaswa kwanza kutatua mlinganyo wa homojeni ($\ref{eqn:homogeneous_linear_ode}$) na kupata $y_h$, kisha tutafute suluhisho moja $y_p$ la mlinganyo ($\ref{eqn:nonhomogeneous_linear_ode}$) ili tupate suluhisho la jumla

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Basi tunawezaje kupata $y_p$? Njia ya jumla ya kupata $y_p$ ni **mbinu ya kubadilisha parameta (method of variation of parameters)**, lakini katika hali fulani tunaweza kutumia **mbinu ya vigawo visivyojulikana (method of undetermined coefficients)**, ambayo ni rahisi zaidi. Hasa, ni njia inayotumiwa mara nyingi katika uhandisi kwa sababu inaweza kutumika kwa mifumo ya mtetemo na miundo ya saketi za umeme za RLC.

Mbinu ya vigawo visivyojulikana inafaa kwa mlinganyo wa kawaida wa tofauti wa mstari

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

wenye **vigawo thabiti $a$ na $b$**, ambapo ingizo $r(x)$ limeundwa na funsi ya eksponenti, nguvu za $x$, $\cos$ au $\sin$, au jumla na bidhaa za funsi kama hizo. Kiini cha mbinu hii ni kwamba $r(x)$ wa umbo hili huwa na viambajengo vinavyobaki na umbo linalofanana na lake. Ili kutumia mbinu ya vigawo visivyojulikana, huchagua $y_p$ yenye umbo linalofanana na $r(x)$, lakini ikiwa na vigawo visivyojulikana ambavyo huamuliwa kwa kuingiza $y_p$ na viambajengo vyake kwenye mlinganyo wa tofauti uliotolewa. Kwa maumbo ya $r(x)$ yaliyo muhimu kivitendo katika uhandisi, kanuni za kuchagua $y_p$ ipasavyo ni kama zifuatazo.

> **Kanuni za kuchagua kwa mbinu ya vigawo visivyojulikana**  
> **(a) kanuni ya msingi (basic rule)**: Katika mlinganyo ($\ref{eqn:linear_ode_with_constant_coefficients}$), ikiwa $r(x)$ ni mojawapo ya funsi zilizo kwenye safu ya kwanza ya jedwali, chagua $y_p$ ya safu hiyo hiyo, kisha amua vigawo visivyojulikana kwa kuingiza $y_p$ na viambajengo vyake katika mlinganyo ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) kanuni ya marekebisho (modification rule)**: Ikiwa neno lililochaguliwa kama $y_p$ ni suluhisho la mlinganyo wa kawaida wa tofauti wa homojeni $y^{\prime\prime} + ay^{\prime} + by = 0$ unaolingana na mlinganyo ($\ref{eqn:linear_ode_with_constant_coefficients}$), basi lizidishe kwa $x$ (au kwa $x^2$ ikiwa suluhisho hilo linalingana na mzizi wa maradufu wa mlinganyo bainishi wa mlinganyo wa homojeni).  
> **(c) kanuni ya kujumlisha (sum rule)**: Ikiwa $r(x)$ ni jumla ya funsi zilizo kwenye safu ya kwanza ya jedwali, chagua kama $y_p$ jumla ya funsi zilizo kwenye safu ya pili katika mistari inayolingana.
>
> | Neno la $r(x)$ | Uteuzi wa $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Njia hii si rahisi tu, bali pia ina sifa ya kujisahihisha yenyewe. Ukichagua $y_p$ vibaya au ukichagua idadi ndogo mno ya maneno, utapata mkanganyiko; ukichagua maneno mengi kupita kiasi, vigawo vya maneno yasiyohitajika vitakuwa $0$ na utapata jibu sahihi. Hivyo, hata kama kitu kitaenda vibaya wakati wa kutumia mbinu ya vigawo visivyojulikana, utaweza kugundua hilo kwa kawaida katika hatua za utatuzi; kwa hiyo ukiwa umechagua $y_p$ ya kiwango kinachofaa kulingana na kanuni zilizo juu, unaweza kuijaribu bila wasiwasi mkubwa.

### Uthibitisho wa kanuni ya kujumlisha
Fikiria mlinganyo wa kawaida wa tofauti wa mstari usio homojeni wa umbo $r(x) = r_1(x) + r_2(x)$

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Sasa tuchukue kwamba milinganyo miwili ifuatayo, yenye upande wa kushoto unaofanana na ingizo $r_1$, $r_2$ mtawalia,

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

ina suluhisho ${y_p}_1$ na ${y_p}_2$ mtawalia. Tukiandika upande wa kushoto wa mlinganyo uliotolewa kama $L[y]$, basi kwa ulinari wa $L[y]$, kwa $y_p = {y_p}_1 + {y_p}_2$ tuna

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Mfano: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Kwa kufuata kanuni ya msingi (a), weka $y_p = Ce^{\gamma x}$ na uiingize katika mlinganyo uliotolewa $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$, basi

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Wakati $\gamma^2 + a\gamma + b \neq 0$
Tunaweza kuamua kigawo kisichojulikana $C$ kama ifuatavyo na kupata $y_p$.

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Wakati $\gamma^2 + a\gamma + b = 0$
Katika hali hii tunapaswa kutumia kanuni ya marekebisho (b). Kwanza, tumia ukweli kwamba $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ ili kupata mizizi ya mlinganyo bainishi wa mlinganyo wa tofauti wa homojeni $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Kutokana na hili tunapata msingi wa mlinganyo wa tofauti wa homojeni

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Wakati $\gamma \neq -a-\gamma$
Kwa kuwa $Ce^{\gamma x}$, ambayo ilikuwa imechaguliwa kama $y_p$, ni suluhisho la mlinganyo wa homojeni unaolingana na mlinganyo uliotolewa lakini si la mzizi wa maradufu, basi kulingana na kanuni ya marekebisho (b) tunazidisha neno hili kwa $x$ na kuweka $y_p = Cxe^{\gamma x}$.

Sasa tukiingiza $y_p$ iliyorekebishwa katika mlinganyo uliotolewa $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$, tunapata

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Wakati $\gamma = -a-\gamma$
Katika hali hii $Ce^{\gamma x}$, ambayo ilikuwa imechaguliwa kama $y_p$, ni suluhisho la mzizi wa maradufu wa mlinganyo wa homojeni unaolingana na mlinganyo uliotolewa, kwa hiyo kulingana na kanuni ya marekebisho (b) tunazidisha neno hili kwa $x^2$ na kuweka $y_p = Cx^2 e^{\gamma x}$.

Sasa tukiingiza $y_p$ iliyorekebishwa katika mlinganyo uliotolewa $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$, tunapata

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Upanuzi wa mbinu ya vigawo visivyojulikana: $r(x)$ katika umbo la bidhaa ya funsi
Fikiria mlinganyo wa kawaida wa tofauti wa mstari usio homojeni wa umbo $r(x) = k x^n e^{\alpha x}\cos(\omega x)$

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Tukisema kuwa $r(x)$ imeundwa na funsi ya eksponenti $e^{\alpha x}$, nguvu ya $x$ ya umbo $x^m$, $\cos{\omega x}$ au $\sin{\omega x}$ (hapa tunadhania ni $\cos$, na kufanya hivyo hakupotezi ujumla), au jumla na bidhaa za funsi kama hizo (yaani, inaweza kuandikwa kama jumla na bidhaa za funsi zilizo kwenye safu ya kwanza ya jedwali lililotangulia), tutaonyesha kuwa kuna suluhisho $y_p$ la mlinganyo hilo ambalo pia ni jumla na bidhaa za funsi zilizo kwenye safu ya pili ya jedwali hilo.

> Kuna sehemu zilizoelezwa kwa kutumia aljebra ya mstari kwa ajili ya uthibitisho mkali, na sehemu hizo zimewekwa alama kwa \*. Hata ukiruka sehemu hizo na kusoma zilizobaki tu, haitaleta shida katika kupata uelewa wa jumla.
{: .prompt-tip }

### Ufafanuzi wa nafasi ya vekta $V$\*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

Kwa $r(x)$ ya aina hii, tunaweza kuchagua nafasi ya vekta $V$ ambayo $r(x) \in V$ kama ifuatavyo.

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Umbo la viambajengo vya funsi za eksponenti, polinomu, na trigonometria
Umbo la viambajengo vya funsi za msingi zilizoorodheshwa katika safu ya kwanza ya jedwali lililotangulia ni kama lifuatalo.
- Funsi ya eksponenti: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Funsi ya polinomu: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Funsi za trigonometria: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Viambajengo vinavyopatikana kwa kutofautisha funsi hizi pia vinaweza kuandikwa kama <u>jumla ya funsi za aina hiyo hiyo</u>.

Kwa hiyo, ikiwa funsi $f$ na $g$ ni miongoni mwa funsi zilizo hapo juu au jumla zake, basi kwa $r(x) = f(x)g(x)$ tukitumia kanuni ya kutofautisha bidhaa tunapata

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

na hapa $f$, $f^{\prime}$, $f^{\prime\prime}$ pamoja na $g$, $g^{\prime}$, $g^{\prime\prime}$ zote zinaweza kuandikwa kama jumla ya funsi za eksponenti, polinomu, na trigonometria, au kama vizidisho vya thabiti. Hivyo $r^{\prime}(x) = (fg)^{\prime}$ na $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ pia, kama ilivyo kwa $r(x)$, vinaweza kuandikwa kama jumla na bidhaa za funsi hizi.

### Kutobadilika kwa $V$ chini ya operesheni ya utofautishaji $D$ na ubadilishaji wa mstari $L$\*
Yaani, si $r(x)$ yenyewe tu bali pia $r^{\prime}(x)$ na $r^{\prime\prime}(x)$ ni mchanganyiko wa mstari wa maneno ya umbo $x^k e^{\alpha x}\cos(\omega x)$ na $x^k e^{\alpha x}\sin(\omega x)$, kwa hiyo

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Tusipoizuia kwa $r(x)$ pekee na tukianzisha opereta ya utofautishaji $D$ kwa vipengele vyote vya nafasi ya vekta $V$ iliyofafanuliwa hapo juu, tunaweza kusema kwa ujumla zaidi kwamba, *nafasi ya vekta $V$ imefungwa kwa operesheni ya utofautishaji $D$*. Kwa hiyo, tukiandika upande wa kushoto wa mlinganyo uliotolewa $y^{\prime\prime} + ay^{\prime} + by$ kama $L[y]$, basi *$V$ haibadiliki (invariant) kwa $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Kwa kuwa $r(x) \in V$ na $V$ haibadiliki kwa $L$, kuna kipengele kingine $y_p$ cha $V$ kinachotosheleza $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Kwa hiyo, tukichagua $y_p$ ifuatayo kwa kutumia vigawo visivyojulikana $A_0, A_1, \dots, A_n$ pamoja na $K$, $M$ ili iwe jumla ya maneno yote ya bidhaa yanayowezekana, basi kulingana na kanuni ya msingi (a) na kanuni ya marekebisho (b), tunaweza kuamua vigawo visivyojulikana kwa kuingiza $y_p$ (au $xy_p$, $x^2y_p$) na viambajengo vyake katika mlinganyo uliotolewa. Hapa $n$ huamuliwa kulingana na daraja la $x$ ndani ya $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Ikiwa ingizo $r(x)$ lililotolewa lina thamani nyingi tofauti za $\alpha_i$ na $\omega_j$, basi unapaswa kuchagua $y_p$ kwa namna ambayo itajumuisha bila kukosa maneno yote yanayowezekana ya umbo $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ na $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ kwa kila thamani ya $\alpha_i$ na $\omega_j$.  
> Kwa kuwa faida ya mbinu ya vigawo visivyojulikana ni urahisi wake, ikiwa ansatz inakuwa tata kiasi cha kufifisha faida hiyo, basi inaweza kuwa bora zaidi kutumia mbinu ya kubadilisha parameta, ambayo tutaiangalia baadaye.
{: .prompt-warning }

## Upanuzi wa mbinu ya vigawo visivyojulikana: mlinganyo wa Euler-Cauchy
Siyo tu kwa [Mlinganyo wa kawaida wa tofauti wa mstari wa homojeni wa mpangilio wa pili wenye vigawo thabiti](/posts/homogeneous-linear-odes-with-constant-coefficients/), bali pia kwa [Mlinganyo wa Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

tunaweza kutumia mbinu ya vigawo visivyojulikana.

### Ubadilishaji wa kigeu
Tuki[fanya badiliko $x = e^t$ ili kuubadilisha kuwa mlinganyo wa kawaida wa tofauti wa mstari wa homojeni wa mpangilio wa pili wenye vigawo thabiti](/posts/euler-cauchy-equation/#ubadilishaji-kuwa-mlinganyo-wa-kawaida-wa-tofauti-wa-mstari-wa-homojeni-wa-mpangilio-wa-pili-wenye-vigawo-thabiti), tunapata

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

na hivyo, kama tulivyoona hapo awali, tunaweza kuubadilisha mlinganyo wa Euler-Cauchy kuwa mlinganyo wa kawaida wa tofauti wa mstari wenye vigawo thabiti kwa $t$ kama ifuatavyo.

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Sasa tumia kwa namna ileile [mbinu ya vigawo visivyojulikana tuliyoiona hapo juu](#mbinu-ya-vigawo-visivyojulikana) kwa mlinganyo ($\ref{eqn:substituted}$) kwa heshima ya $t$, kisha mwishoni tumia ukweli kwamba $t = \ln x$ ili kupata suluhisho kwa heshima ya $x$.

### Wakati $r(x)$ ni nguvu ya $x$, logariti ya asili, au jumla na bidhaa za funsi kama hizo
Hasa, ikiwa ingizo $r(x)$ limeundwa na nguvu za $x$, logariti ya asili, au jumla na bidhaa za funsi kama hizo, basi tunaweza kuchagua moja kwa moja $y_p$ inayofaa kwa kufuata kanuni za kuchagua zifuatazo kwa mlinganyo wa Euler-Cauchy.

> **Kanuni za kuchagua kwa mbinu ya vigawo visivyojulikana: kwa mlinganyo wa Euler-Cauchy**  
> **(a) kanuni ya msingi (basic rule)**: Katika mlinganyo ($\ref{eqn:euler_cauchy}$), ikiwa $r(x)$ ni mojawapo ya funsi zilizo kwenye safu ya kwanza ya jedwali, chagua $y_p$ ya safu hiyo hiyo, kisha amua vigawo visivyojulikana kwa kuingiza $y_p$ na viambajengo vyake katika mlinganyo ($\ref{eqn:euler_cauchy}$).  
> **(b) kanuni ya marekebisho (modification rule)**: Ikiwa neno lililochaguliwa kama $y_p$ ni suluhisho la mlinganyo wa kawaida wa tofauti wa homojeni $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ unaolingana na mlinganyo ($\ref{eqn:euler_cauchy}$), basi lizidishe kwa $\ln{x}$ (au kwa $(\ln{x})^2$ ikiwa suluhisho hilo linalingana na mzizi wa maradufu wa mlinganyo bainishi wa mlinganyo wa homojeni).  
> **(c) kanuni ya kujumlisha (sum rule)**: Ikiwa $r(x)$ ni jumla ya funsi zilizo kwenye safu ya kwanza ya jedwali, chagua kama $y_p$ jumla ya funsi zilizo kwenye safu ya pili katika mistari inayolingana.
>
> | Neno la $r(x)$ | Uteuzi wa $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Kwa kufanya hivi, kwa maumbo ya ingizo $r(x)$ yaliyo muhimu kivitendo, tunaweza kupata $y_p$ sawa na ile inayopatikana kwa [ubadilishaji wa kigeu](#ubadilishaji-wa-kigeu) kwa njia ya haraka na rahisi zaidi. Tunaweza kupata kanuni hizi za kuchagua kwa mlinganyo wa Euler-Cauchy kwa kuchukua [kanuni za awali za kuchagua](#mbinu-ya-vigawo-visivyojulikana) tulizoona hapo juu na kubadilisha $x$ kwa $\ln{x}$.
