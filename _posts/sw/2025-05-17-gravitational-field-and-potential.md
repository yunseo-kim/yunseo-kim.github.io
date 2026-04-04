---
title: Uga wa graviti na potenshali ya graviti
description: "Jifunze ufafanuzi wa vekta ya uga wa graviti na potenshali ya graviti chini ya sheria ya Newton ya mvutano wa ulimwengu wote, pamoja na mifano muhimu ya teorema ya ganda la sfera na mikunjo ya mzunguko wa galaksi."
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Sheria ya Newton ya mvutano wa ulimwengu wote: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Kwa mgawanyo endelevu wa wingi na kwa kitu chenye ukubwa: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: msongamano wa wingi katika nukta iliyoko kwenye vekta ya mahali $\mathbf{r^{\prime}}$ kutoka kwenye asili yoyote ile
>   - $dv^{\prime}$: elementi ya ujazo katika nukta iliyoko kwenye vekta ya mahali $\mathbf{r^{\prime}}$ kutoka kwenye asili yoyote ile
> - **Vekta ya uga wa graviti**:
>   - vekta inayoonyesha nguvu kwa kila kitengo cha wingi inayopokelewa na chembe fulani ndani ya uga uliotengenezwa na kitu chenye wingi $M$
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - ina vipimo vya *nguvu kwa kila kitengo cha wingi* au *uongezaji kasi*
> - **Potenshali ya graviti**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - ina vipimo vya $($*nguvu kwa kila kitengo cha wingi* $) \times ($*umbali* $)$ au *nishati kwa kila kitengo cha wingi*
>   - $\Phi = -G\cfrac{M}{r}$
>   - kwa potenshali ya graviti, tofauti zake za jamaa pekee ndizo zenye maana; thamani maalum yenyewe haina maana
>   - kwa kawaida, hali ya $\Phi \to 0$ wakati $r \to \infty$ huwekwa kiholela ili kuondoa utata
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Potenshali ya graviti ndani na nje ya ganda la sfera (teorema ya ganda la sfera)**
>   - Wakati $R>a$:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - wakati wa kupata potenshali ya graviti katika nukta ya nje inayotokana na mgawanyo wa wingi wenye ulinganifu wa kisfera, kitu hicho kinaweza kuchukuliwa kama wingi wa nukta
>   - Wakati $R<b$:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - ndani ya ganda la wingi lenye ulinganifu wa kisfera, potenshali ya graviti ni thabiti bila kujali mahali, na nguvu ya graviti inayofanya kazi ni $0$
>   - Wakati $b<R<a$: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## Uga wa graviti
### Sheria ya Newton ya mvutano wa ulimwengu wote
Newton alikuwa tayari ameshapanga kwa utaratibu na hata kuthibitisha kwa namba sheria ya mvutano wa ulimwengu wote kabla ya 11666 HE. Hata hivyo, ilimchukua miaka 20 zaidi hadi alipochapisha matokeo yake katika *Principia* mnamo 11687 HE, kwa sababu hakuweza kuhalalisha mbinu ya hesabu iliyodhani Dunia na Mwezi kuwa wingi za nukta zisizo na ukubwa. Kwa bahati nzuri, [tukitumia kalkulasi ambayo Newton mwenyewe aliibuni baadaye, tunaweza kuthibitisha kwa urahisi zaidi tatizo hilo ambalo halikuwa rahisi kwa Newton katika miaka ya 11600](#wakati-ra).

Kwa mujibu wa sheria ya Newton ya mvutano wa ulimwengu wote, *kila chembe yenye wingi huvuta chembe nyingine zote katika ulimwengu, na nguvu hiyo ni sawia na zao la wingi hizo mbili na ni kinyume sawia na mraba wa umbali kati yao.* Kwa namna ya kihisabati, hii huandikwa kama ifuatavyo.

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Chanzo cha picha*
> - Mwandishi: mtumiaji wa Wikimedia [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - Leseni: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

Vekta ya kitengo $\mathbf{e}_r$ inaelekea kutoka $M$ kwenda kwa $m$, na ishara hasi inaonyesha kwamba nguvu hiyo ni ya mvutano. Yaani, $m$ huvutwa kuelekea $M$.

### Jaribio la Cavendish
Uthibitisho wa kimaabara wa sheria hii na uamuzi wa thamani ya $G$ ulifanywa mwaka 11798 HE na mwanafizikia wa Uingereza Henry Cavendish. Jaribio la Cavendish hutumia mizani ya msokoto iliyo na mipira miwili midogo iliyofungwa kwenye ncha za fimbo nyepesi. Kila mmoja wa mipira hiyo miwili huvutwa kuelekea mipira mingine miwili mikubwa iliyo karibu nayo. Thamani rasmi ya $G$ iliyopatikana hadi sasa ni $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> Ingawa $G$ ni mojawapo ya konstanti za msingi zilizojulikana kwa muda mrefu zaidi, bado inajulikana kwa usahihi mdogo kuliko konstanti nyingine nyingi za msingi kama $e$, $c$, na $\hbar$. Hata leo, kuna tafiti nyingi zinazofanyika ili kupata thamani ya $G$ kwa usahihi wa juu zaidi.
{: .prompt-tip }

### Kwa vitu vyenye ukubwa
Sheria katika fomula ($\ref{eqn:law_of_gravitation}$) inaweza kutumika kwa ukali tu kwa *chembe ya nukta*. Ikiwa upande mmoja au yote mawili ni vitu vyenye ukubwa fulani, basi ili kuhesabu nguvu ni lazima kuongeza dhana kwamba uga wa nguvu ya graviti ni *uga wa mstari*. Yaani, hudhaniwa kwamba jumla ya graviti inayopokelewa na chembe moja yenye wingi $m$ kutoka kwa chembe nyingi nyingine inaweza kupatikana kwa kujumlisha vekta za nguvu za kila moja. Katika hali ya kitu ambamo dutu imesambazwa kwa mwendelezo, jumla hiyo hubadilishwa kuwa integresheni kama ifuatavyo.

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: msongamano wa wingi katika nukta iliyoko kwenye vekta ya mahali $\mathbf{r^{\prime}}$ kutoka kwenye asili yoyote ile
- $dv^{\prime}$: elementi ya ujazo katika nukta iliyoko kwenye vekta ya mahali $\mathbf{r^{\prime}}$ kutoka kwenye asili yoyote ile

Ikiwa tunataka kupata jumla ya nguvu ya graviti wakati kitu chenye wingi $M$ na kitu chenye wingi $m$ vyote vina ukubwa, basi integresheni ya pili ya ujazo kwa ajili ya $m$ pia inahitajika.

### Vekta ya uga wa graviti
**Vekta ya uga wa graviti** $\mathbf{g}$ hufafanuliwa kama vekta inayoonyesha nguvu kwa kila kitengo cha wingi inayopokelewa na chembe fulani ndani ya uga uliotengenezwa na kitu chenye wingi $M$, hivyo

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

au

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

huandikwa hivyo. Hapa mwelekeo wa $\mathbf{e}_r$ hubadilika kulingana na $\mathbf{r^\prime}$.

Kiasi hiki $\mathbf{g}$ kina vipimo vya *nguvu kwa kila kitengo cha wingi* au *uongezaji kasi*. Karibu na uso wa Dunia, ukubwa wa vekta ya uga wa graviti $\mathbf{g}$ ni sawa na kiasi tunachokiita **konstanti ya uongezaji kasi wa graviti**, na $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$.

## Potenshali ya graviti
### Ufafanuzi
Vekta ya uga wa graviti $\mathbf{g}$ hubadilika kama $1/r^2$, na hivyo hutimiza sharti la kuweza kuonyeshwa kama gradient ya skala fulani (potenshali), yaani $\nabla \times \mathbf{g} \equiv 0$. Kwa hiyo tunaweza kuandika kama ifuatavyo.

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

Hapa $\Phi$ huitwa **potenshali ya graviti**, na ina vipimo vya $($*nguvu kwa kila kitengo cha wingi* $) \times ($*umbali* $)$ au *nishati kwa kila kitengo cha wingi*.

Kwa kuwa $\mathbf{g}$ hutegemea radius pekee, basi $\Phi$ pia hubadilika kulingana na $r$. Kutoka fomula ($\ref{eqn:g_vector}$) na ($\ref{eqn:gradient_phi}$),

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

na tukiiintegra tunapata

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

Potenshali ya graviti ina maana tu kwa tofauti zake za jamaa, na ukubwa wa thamani yake halisi hauna maana, kwa hiyo konstanti ya integresheni inaweza kuachwa. Kwa kawaida, hali ya $\Phi \to 0$ wakati $r \to \infty$ huwekwa kiholela ili kuondoa utata, na fomula ($\ref{eqn:g_potential}$) pia hutimiza hali hii.

Wakati dutu imesambazwa kwa mwendelezo, potenshali ya graviti huwa kama ifuatavyo.

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Iwapo wingi umesambazwa juu ya uso wa ganda jembamba, basi

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

Na kwa chanzo cha wingi wa mstari chenye msongamano wa mstari $\rho_l$, tunaweza kuandika kama ifuatavyo.

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Maana ya kifizikia
Hebu tufikirie kazi kwa kila kitengo cha wingi $dW^\prime$ inayofanywa na kitu kinaposogea kwa $d\mathbf{r}$ ndani ya uga wa graviti.

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

Katika fomula hii, $\Phi$ ni funksi ya koordinate za nafasi pekee, na huonyeshwa kama $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Kwa hiyo, tunajua kwamba kiasi cha kazi kwa kila kitengo cha wingi kinachofanywa na kitu kinapohamishwa ndani ya uga wa graviti kutoka nukta moja hadi nyingine ni sawa na tofauti ya potenshali kati ya nukta hizo mbili.

Iwapo potenshali ya graviti katika umbali usio na kikomo hufafanuliwa kuwa $0$, basi $\Phi$ katika nukta yoyote inaweza kutafsiriwa kama kazi kwa kila kitengo cha wingi inayohitajika kuhamisha kitu hicho kutoka umbali usio na kikomo hadi nukta hiyo. Kwa kuwa nishati potenshali ya kitu ni sawa na zao la wingi wa kitu hicho na potenshali ya graviti $\Phi$, tukiiita $U$ kuwa nishati potenshali,

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

Kwa hiyo, nguvu ya graviti inayopokelewa na kitu hupatikana kwa kuweka ishara hasi kwenye gradient ya nishati potenshali yake.

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Kitu kinapowekwa ndani ya uga wa graviti uliotengenezwa na wingi fulani, daima huzalishwa nishati potenshali fulani. Kwa ukali, nishati hii potenshali ipo katika uga wenyewe, lakini kwa desturi mara nyingi huiitwa nishati potenshali ya kitu hicho.

## Mfano: Potenshali ya graviti ndani na nje ya ganda la sfera (teorema ya ganda la sfera)
### Kuweka koordinate & kuandika potenshali ya graviti kwa fomula ya integresheni
Hebu tupate potenshali ya graviti ndani na nje ya ganda la sfera lenye msongamano sare, lenye radius ya ndani $b$ na radius ya nje $a$. Nguvu ya graviti ya ganda la sfera inaweza kupatikana kwa kuhesabu moja kwa moja vipengele vya nguvu vinavyofanya kazi kwa kitengo cha wingi ndani ya uga, lakini kutumia mbinu ya potenshali ni rahisi zaidi.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Katika mchoro hapo juu, hebu tuhesabu potenshali katika nukta $P$ iliyo umbali $R$ kutoka kituo. Tukidhani mgawanyo wa wingi wa ganda ni sare, tuna $\rho(r^\prime)=\rho$, na kwa kuwa kuna ulinganifu kwa pembe ya azimuthi $\phi$ kwa kuzingatia mstari unaounganisha kituo cha sfera na nukta $P$,

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

Kwa mujibu wa sheria ya kosaini,

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

na kwa kuwa $R$ ni konstanti, tukidiferenshia fomula hii kwa heshima ya $r^\prime$ tunapata

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

Tukiingiza haya kwenye fomula ($\ref{eqn:spherical_shell_1}$), tunapata

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

Hapa $r_\mathrm{max}$ na $r_\mathrm{min}$ huamuliwa kulingana na mahali pa nukta $P$.

### Wakati $R>a$

$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

Kwa kuwa wingi wa ganda la sfera $M$ hutolewa na

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

potenshali huwa kama ifuatavyo.

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> Tukilinganisha fomula ya potenshali ya graviti inayotokana na wingi wa nukta wenye wingi $M$, yaani ($\ref{eqn:g_potential}$), na matokeo tuliyopata sasa hivi, ($\ref{eqn:spherical_shell_outside_2}$), tunaona kuwa ni sawa kabisa. Hii ina maana kwamba wakati wa kupata potenshali ya graviti katika nukta ya nje inayotokana na mgawanyo wa wingi wenye ulinganifu wa kisfera, ni sawa kufikiri kwamba wingi wote umejikusanya katikati. Miili mingi ya anga ya kisfera yenye ukubwa fulani au zaidi, kama Dunia au Mwezi, huingia katika hali hii, na inaweza kuchukuliwa kuwa ni mkusanyiko wa maganda mengi sana ya kisfera yenye vituo vinavyofanana lakini vipenyo tofauti, kama [matryoshka](https://en.wikipedia.org/wiki/Matryoshka_doll). Hili pia ndilo [msingi halali wa kudhani miili ya anga kama Dunia au Mwezi kuwa wingi za nukta zisizo na ukubwa wakati wa kufanya hesabu](#sheria-ya-newton-ya-mvutano-wa-ulimwengu-wote), kama ilivyotajwa mwanzoni mwa makala hii.
{: .prompt-info }

### Wakati $R<b$

$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> Ndani ya ganda la wingi lenye ulinganifu wa kisfera, potenshali ya graviti ni thabiti bila kujali mahali, na nguvu ya graviti inayofanya kazi ni $0$.
{: .prompt-info }

> Na hili pia ni mojawapo ya misingi mikuu inayoonyesha kwamba 'nadharia ya Dunia tupu' ni upuuzi, ambayo ni mfano maarufu wa sayansi ya uongo. Kama Dunia ingekuwa katika umbo la ganda la sfera lenye ndani tupu, kama inavyodaiwa na nadharia hiyo, basi graviti ya Dunia isingefanya kazi kwa vitu vyote vilivyomo ndani ya tundu hilo. Tukizingatia wingi na ujazo wa Dunia, tundu kama hilo la Dunia haliwezi kuwepo; na hata kama lingewepo, viumbe wa humo wasingeishi wakitumia upande wa ndani wa ganda hilo kama ardhi, bali wangeelea katika hali ya kutokuwa na uzito kama kwenye kituo cha anga.  
> [Huenda vijiumbe vinaweza kuishi kwenye kina cha tabaka za ardhi cha kilomita chache chini ya uso](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), lakini angalau si kwa umbo linalodaiwa na nadharia ya Dunia tupu. Ninapenda sana riwaya ya Jules Verne *Voyage au centre de la Terre* na filamu *Journey to the Center of the Earth*, lakini kazi za ubunifu zinapaswa kufurahiwa kama kazi za ubunifu; tusiziamini kwa uzito kana kwamba ni ukweli.
{: .prompt-tip }

### Wakati $b<R<a$

$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Matokeo
Tukichora kwa grafu potenshali ya graviti $\Phi$ katika maeneo matatu tuliyopata hapo juu, pamoja na ukubwa wa vekta ya uga wa graviti $\|\mathbf{g}\|$ unaotokana nayo, kama funksi ya umbali $R$, tunapata yafuatayo.

![Gravitational Potential as a Function of R](/physics-visualizations/figs/shell-theorem-gravitational-potential.png)  
![Magnitude of the Field Vector as a Function of R](/physics-visualizations/figs/shell-theorem-field-vector.png)  
> - Msimbo wa kuona kwa Python: [hazina ya yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/shell_theorem.py)
> - Leseni: [Tazama hapa](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Tunaona kwamba potenshali ya graviti na ukubwa wa vekta ya uga wa graviti ni endelevu. Ikiwa potenshali ya graviti ingekuwa na mkatiko katika nukta fulani, basi gradient ya potenshali katika nukta hiyo, yaani ukubwa wa graviti, ungekuwa usio na kikomo, jambo ambalo si halali kifizikia; kwa hiyo funksi ya potenshali lazima iwe endelevu katika kila nukta. Hata hivyo, *derivative* ya vekta ya uga wa graviti haiko endelevu kwenye uso wa ndani na wa nje wa ganda.

## Mfano: Mkunjo wa mzunguko wa galaksi
Kwa mujibu wa uchunguzi wa kiastronomia, katika galaksi nyingi za spiral zinazozunguka kuhusu kituo chao, kama Njia Nyeupe na galaksi ya Andromeda, wingi unaoweza kuonekana husambazwa hasa karibu na sehemu ya kati. Hata hivyo, kasi za obiti za wingi huo katika galaksi za spiral hazilingani kabisa na thamani zinazotabiriwa kinadharia kutokana na mgawanyo wa wingi unaoweza kuonekana, na hubaki karibu thabiti baada ya umbali fulani, kama inavyoonekana katika grafu ifuatayo.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Chanzo cha picha*
> - Mwandishi: mtumiaji wa Wikipedia [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - Leseni: Public Domain

{% 
  include embed/video.html 
  src='https://cdn.jsdelivr.net/gh/yunseo-kim/yunseo-kim.github.io/assets/video/gravitational-field-and-potential/Galaxy_rotation_under_the_influence_of_dark_matter.webm' 
  title="Kushoto: mzunguko wa galaksi uliotabiriwa kutoka kwa wingi unaoonekana | Kulia: mzunguko wa galaksi uliochunguzwa kwa kweli." 
  types='ogg'
  autoplay=true 
  loop=true 
%}
> *Chanzo cha video*
> - Kiungo cha faili asili (video ya Ogg Theora): <https://commons.wikimedia.org/wiki/File:Galaxy_rotation_under_the_influence_of_dark_matter.ogv>
> - Mwandishi: [Ingo Berg](https://beltoforion.de/en/index.php)
> - Leseni: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
> - Mbinu ya uigaji na msimbo uliotumika: <https://beltoforion.de/en/spiral_galaxy_renderer/>

> Faili ya picha `Rotation curve of spiral galaxy Messier 33 (Triangulum).png` ambayo hapo awali ilikuwa imeingizwa kwenye ukurasa huu imeondolewa pia kutoka ukurasa huu, kwa kuwa ilifutwa kutoka Wikimedia Commons baada ya kubainika kuwa ilikuwa kazi ya kisanii ya kiderivati iliyoplagiarizwa bila nukuu ifaayo na mtumiaji wa Wikimedia [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama), kutoka kwa kazi isiyo huru ya Profesa Mark Whittle wa [Chuo Kikuu cha Virginia](https://markwhittle.uvacreate.virginia.edu/), [kama ilivyobainishwa hapa](https://commons.wikimedia.org/wiki/Commons:Deletion_requests/File:Rotation_curve_of_spiral_galaxy_Messier_33_(Triangulum).png).
{: .prompt-danger }

Iwapo wingi wa galaksi umejikusanya katikati, hebu tutabiri kasi ya obiti kulingana na umbali na kuonyesha kwamba utabiri huo haulingani na matokeo ya uchunguzi; kisha tuonyeshe kwamba ili kueleza matokeo ya uchunguzi, wingi $M(R)$ unaosambazwa ndani ya umbali $R$ kutoka kituo cha galaksi lazima uwe sawia na $R$.

Kwanza, ikiwa wingi wa galaksi $M$ umejikusanya katikati, kasi ya obiti katika umbali $R$ ni kama ifuatavyo.

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

Katika hali hii, kasi ya obiti inayopungua kama $1/\sqrt{R}$ hutabiriwa, kama mstari wa nukta ulivyoonyeshwa katika grafu hizo hapo juu; lakini kwa mujibu wa uchunguzi, kasi ya obiti $v$ hubaki karibu thabiti bila kujali umbali $R$, kwa hiyo utabiri na uchunguzi havilingani. Matokeo haya ya uchunguzi yanaweza kuelezeka tu ikiwa $M(R)\propto R$.

Tukiweka $M(R) = kR$ kwa kutumia konstanti ya uwiano $k$,

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(konstanti)}. $$

Kutokana na hili, wanaastrofizikia hufikia hitimisho kwamba katika galaksi nyingi lazima kuwepo 'dark matter' ambayo haijagunduliwa, na kwamba dark matter hiyo lazima ichangie zaidi ya 90% ya wingi wa ulimwengu. Hata hivyo, asili halisi ya dark matter bado haijafafanuliwa wazi, na ingawa si nadharia kuu, pia yapo majaribio kama Modified Newtonian Dynamics (MOND) yanayojaribu kueleza uchunguzi bila kudhani uwepo wa dark matter. Leo hii, eneo hili la utafiti liko mstari wa mbele kabisa wa astrofizikia.
