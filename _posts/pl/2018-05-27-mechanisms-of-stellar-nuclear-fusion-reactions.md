---
title: "Mechanizmy reakcji syntezy jądrowej w gwiazdach"
description: "Wprowadzenie do reakcji syntezy jądrowej zachodzących w jądrach gwiazd: łańcucha proton–proton (pp) oraz cyklu CNO. Archiwalny esej autora z I klasy liceum, zachowany w oryginalnym, potocznym stylu."
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---

## Łańcuch proton–proton (proton-proton chain reaction)

To najpowszechniej znana ludziom reakcja syntezy jądrowej zachodząca w gwiazdach. Jądro deuteru, czyli deuteron (deuteron), powstaje przez połączenie jednego protonu ($p$) i jednego neutronu ($n$). Zatem, aby proton i proton połączyły się i utworzyły jądro deuteru, jeden z nich musi zmienić się w neutron. Jak więc proton może zamienić się w neutron?

- Proces, w którym neutron ($n$) zmienia się w proton ($p$), emitując elektron ($e⁻$) i antyneutrino elektronowe ($\nu_e$), to „[rozpad beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#ujemny-rozpad-beta-beta--decay)”. Zapis reakcji to $n \rightarrow p + e^{-} + \overline{\nu_e}$. 
- Proces, w którym proton ($p$) zmienia się w neutron ($n$), jest procesem odwrotnym do rozpadu beta. Dlatego nazywa się go „[odwrotnym rozpadem beta](/posts/Nuclear-Stability-and-Radioactive-Decay/#dodatni-rozpad-beta-beta-decay)”. Jak wygląda równanie reakcji odwrotnego rozpadu beta? W reakcji jądrowej nie ma nic „specjalnego”. Wystarczy zamienić miejscami proton i neutron, a elektron zastąpić pozytonem, zaś antyneutrino — neutrinem. W zapisie: $p \rightarrow n + e^{+} + \nu_e$.

Po utworzeniu jądra deuteru w powyższym procesie powstaje jądro helu-3 w reakcji $^2_1D + p \rightarrow {^3_2He}$, a na końcu zderzają się dwa jądra helu-3, tworząc jądro helu-4 oraz dwa protony.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

W rzeczywistości łańcuch proton–proton nie ma tylko jednej ścieżki reakcji. Powyższy przypadek jest najbardziej reprezentatywny, ale istnieje jeszcze kilka innych dróg. Jednak pozostałe ścieżki nie stanowią bardzo dużej części w gwiazdach o masie mniejszej niż masa Słońca, a w gwiazdach o masie co najmniej 1.5 masy Słońca znacznie większy udział niż łańcuch pp ma omawiany dalej cykl CNO, więc nie będę ich tu osobno omawiać.

Ten łańcuch proton–proton zachodzi dominująco w temperaturach rzędu około 10 mln K–14 mln K. W przypadku Słońca temperatura w centrum wynosi około 15 mln K, a łańcuch pp odpowiada za 98.3% reakcji (pozostałe 1.3% przypada na cykl CNO).

## Cykl węglowo–azotowo–tlenowy (CNO cycle)

Reakcja cyklu CNO to proces, w którym węgiel, pochłaniając proton, zamienia się w azot, a następnie azot, pochłaniając proton, zamienia się w tlen itd.; ostatecznie pochłaniane są łącznie cztery protony, emitowane jest jedno jądro helu, po czym układ wraca do węgla. Charakterystyczne jest to, że węgiel, azot i tlen pełnią rolę katalizatora. Teoretycznie cykl CNO dominuje w gwiazdach o masie co najmniej 1.5 masy Słońca. Różnica dominującej reakcji zależnie od masy gwiazdy wynika z odmiennej zależności temperaturowej łańcucha pp i cyklu CNO. Ten pierwszy startuje przy relatywnie niskich temperaturach w okolicach 4 mln K, a szybkość reakcji jest proporcjonalna do czwartej potęgi temperatury. Natomiast drugi zaczyna się około 15 mln K, ale jest bardzo wrażliwy na temperaturę (szybkość reakcji proporcjonalna do 16. potęgi temperatury), więc przy temperaturach powyżej 17 mln K większy udział zaczyna mieć cykl CNO.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Cykl CNO również ma różne ścieżki. Dzieli się go z grubsza na niskotemperaturowy cykl CNO (we wnętrzach gwiazd) oraz wysokotemperaturowy cykl CNO (nowe i supernowe), a w każdym z tych przypadków istnieje jeszcze po kilka (trzy–cztery) wariantów ścieżek reakcji. Chciałbym omówić wszystkie reakcje cyklu CNO, ale przy tej objętości tekstu to niemożliwe, więc zajmę się wyłącznie najbardziej podstawowym cyklem CN*, tj. CNO-I.

> *Powód, dla którego używa się nazwy „cykl CN” (bez O), jest taki, że w danym przebiegu reakcji nie występuje stabilny izotop tlenu.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Jak na powyższym rysunku, węgiel, azot i tlen krążą w cyklu, pełniąc rolę katalizatora. Jednak niezależnie od ścieżki reakcji, całkowite równanie reakcji i suma wydzielonej energii są takie same.

## Więcej lektur

- Inkyu Park (박인규, profesor Wydziału Fizyki Uniwersytetu Miejskiego w Seulu), [Naver Cast – spacer po fizyce: ile neutrin powstaje w Słońcu?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
