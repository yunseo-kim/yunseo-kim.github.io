---
title: Deni la kiufundi
description: "Hebu tuchunguze dhana ya deni la kiufundi, sababu zinazolifanya litokee, na mbinu za kupunguza kwa kiwango cha chini."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Deni la kiufundi
> **Deni la kiufundi(Technical debt)**  
> Gharama itakayolazimika kulipwa baadaye kutokana na kuchagua njia ya mkato inayoweza kukamilisha mradi wa sasa haraka zaidi ili kutimiza mahitaji ya papo hapo katika mchakato wa maendeleo
{: .prompt-info }

Kama ilivyo kwa kuchukua deni la kifedha na kukopa pesa ili kuwekeza haraka mahali panapohitajika kwa wakati huo, lakini baadaye ukalazimika kubeba shinikizo la kifedha na kulipa pamoja na riba juu ya kiasi cha msingi, vivyo hivyo ukiharakisha maendeleo ya programu ili kutatua mahitaji ya sasa hata kama utekelezaji huo ni mchafu kidogo, msimbo huwa mgumu na wenye marudio mengi, na baadaye husababisha ugumu katika kutekeleza au kupanua vipengele vipya.

Kama vile kampuni zinavyoweza kutumia deni kufanya uwekezaji zaidi kwa wakati unaofaa ili kuunda bidhaa mpya na kuongeza sehemu ya soko, au mtu binafsi kutumia mkopo kununua nyumba, vivyo hivyo kubeba deni la kiufundi na kutekeleza vipengele vipya haraka si jambo baya kila wakati. Hata hivyo, ni vyema kupunguza mkusanyiko wa deni la kiufundi na kulisimamia katika kiwango kinachoweza kubebeka.

## Sababu zinazofanya deni la kiufundi litokee
Hata kama uwezo wa msanidi ni wa kutosha, deni la kiufundi hutokea kwa namna isiyoepukika katika mchakato wa maendeleo, na haiwezekani kulizuia kabisa tangu mwanzo.
Kadiri huduma inavyoendelea kukua, msimbo ulioundwa awali unaweza kufikia mipaka yake, na hata kama hapo mwanzo ulikuwa rahisi kusomeka na ulifanya kazi vizuri, inaweza kuwa lazima kurekebisha usanifu wa awali.
Pia, kadiri teknolojia yenyewe inavyoendelea, maktaba au fremu zilizokuwa maarufu zamani zinaweza kuacha kutumika sana, na hivyo mtu anaweza kuamua kubadilisha tech stack kwenda kwenye maktaba au fremu nyingine. Hata katika hali hii, msimbo uliokuwa umeandikwa awali huwa aina fulani ya deni la kiufundi.

Mbali na hayo, deni la kiufundi linaweza kutokea pia kwa sababu zifuatazo.
- Kutoweka nyaraka kwa wakati kuhusu kile kilichobuniwa wakati wa kuendeleza mradi, jambo linalofanya wengine au hata wewe mwenyewe baada ya muda kupata ugumu wa kutafsiri msimbo huo tena
- Kutondoa vigezo au vipengee vya DB ambavyo havitumiki tena
- Kutofanya otomatiki kwa kazi za kurudiwa-rudiwa (kama vile usambazaji/deployment na build), hivyo kila mara kuhitaji muda na juhudi za ziada
- Mabadiliko ya dharura ya spec

## Jinsi ya kupunguza deni la kiufundi
### Kuweka kanuni (Convention) kati ya wasanidi
- Ikiwa maendeleo hayafanywi na mtu mmoja pekee, ni lazima kuwe na makubaliano kuhusu lugha au tech stack itakayotumika, muundo wa saraka za mradi, mtindo wa maendeleo, na kadhalika ili kuwezesha ushirikiano mzuri
- Inapaswa kuamuliwa ni kwa kiwango gani mbinu zitaunganishwa kwa pamoja katika maendeleo, na ni kuanzia wapi uhuru wa binafsi utaachwa
- Ni muhimu kuthibitisha mitindo ya maendeleo ya kila mmoja na kubadilishana maoni kupitia code review

### Kuandika clean code & kufanya refactoring
- Ikiwa msimbo uliopo ni mchafu na unazuia maendeleo, deni la kiufundi linaweza kusafishwa kupitia refactoring, yaani kubadilisha muundo wa msimbo kuwa safi zaidi
- Bila shaka, kadiri msimbo wa zamani unavyokuwa mchafu zaidi na kuwa spaghetti code, ndivyo ugumu wa refactoring unavyoongezeka; katika hali za kupindukia, kuna wakati refactoring huachwa kabisa, msimbo wa zamani hutupwa, na maendeleo huanza upya kutoka mwanzo
- Inafaa kujitahidi tangu mwanzo kuandika msimbo ulio rahisi kusomeka na ulio rahisi kutunza na kuboresha
