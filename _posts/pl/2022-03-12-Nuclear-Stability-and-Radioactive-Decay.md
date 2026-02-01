---
title: Stabilność jądrowa i rozpad promieniotwórczy
description: Omawiamy wykres Segrégo i typy rozpadów promieniotwórczych, widmo energii elektronów/pozytonów w rozpadzie beta oraz tło odkrycia neutrina, łańcuchy rozpadu wybranych nuklidów (węgiel-14, potas-40, tryt, cez-137) oraz przejście izomeryczne.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.webp
---
## Wymagania wstępne
- [Cząstki subatomowe i składniki atomu](/posts/constituents-of-an-atom/)

## Wykres Segrégo (Segre Chart) lub mapa nuklidów
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Dla nuklidów o liczbie atomowej $Z$ większej niż 20, do stabilizacji potrzeba więcej neutronów niż protonów
- Neutrony pełnią rolę „spoiwa” jądra: przeciwdziałają elektrycznemu odpychaniu między protonami i utrzymują jądro razem

## Dlaczego zachodzi rozpad promieniotwórczy (Radioactive Decay)
- Tylko określone kombinacje liczby neutronów i protonów tworzą stabilne nuklidy
- Gdy liczba neutronów względem liczby protonów jest zbyt duża albo zbyt mała, dany nuklid jest niestabilny i wywołuje *rozpad promieniotwórczy (radioactive decay)*
- Jądro powstałe po rozpadzie jest w większości przypadków w stanie wzbudzonym, więc emituje energię w postaci promieniowania gamma lub promieniowania rentgenowskiego

## Rozpad beta ($\beta$-decay)
### Rozpad beta dodatni ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Zachodzi, gdy neutronów jest relatywnie za mało
- Proton ($p$) zamienia się w neutron ($n$), emitując pozyton ($\beta^+$) i neutrino elektronowe ($\nu_e$)
- Liczba atomowa maleje o 1, liczba masowa nie zmienia się

Przykład) $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Rozpad beta ujemny ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Zachodzi, gdy neutronów jest relatywnie za dużo
- Neutron ($n$) zamienia się w proton ($p$), emitując elektron ($\beta^-$) i antyneutrino elektronowe ($\overline{\nu}_e$)
- Liczba atomowa rośnie o 1, liczba masowa nie zmienia się

Przykład) $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Widmo energii emitowanych elektronów (pozytonów)
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Źródło obrazu*
> - autor: użytkownik niemieckiej Wikipedii [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - licencja: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Elektrony lub pozytony emitowane w rozpadzie beta mają ciągłe widmo energii, jak pokazano powyżej.
- rozpad $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- rozpad $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

> Całkowita energia uwalniana w rozpadzie beta jest skwantowana, jednak elektron/pozyton oraz antyneutrino/neutrino dzielą tę energię w dowolnych proporcjach, więc jeśli patrzymy tylko na energię elektronu/pozytonu, obserwujemy widmo ciągłe.
> Fakt, że widmo energii elektronów/pozytonów w rozpadzie beta nie jest skwantowane, lecz ciągłe, był wynikiem niezgodnym z przewidywaniami teoretycznymi i wyglądał jak naruszenie zasady zachowania energii.  
> Aby to wyjaśnić, Wolfgang Ernst Pauli (Wolfgang Ernst Pauli) w 11930 roku przewidział istnienie „<u>elektrycznie obojętnej cząstki o ekstremalnie małej masie i skrajnie niskiej reaktywności</u>” i zaproponował nazwę „neutron (neutron)”. Jednak w 11932 roku Sir James Chadwick (Sir James Chadwick) odkrył i nazwał neutron w dzisiejszym znaczeniu, co spowodowało konflikt nazewnictwa. W konsekwencji w kolejnym roku, 11933, Enrico Fermi (Enrico Fermi) publikując teorię rozpadu beta, przemianował tę cząstkę na *neutrino (neutrino)*, dodając włoski przyrostek „-ino” oznaczający „mały”, i tak utrwaliła się obecna nazwa.  
> Następnie w 11942 roku chiński fizyk jądrowy Wang Ganchang (王淦昌, Wáng Gànchāng) jako pierwszy zaproponował metodę detekcji neutrin z użyciem [wychwytu elektronu](#wychwyt-elektronu-electron-capture-lub-wychwyt-k-k-capture). W 11956 roku Clyde Cowon (Clyde Cowon), Frederick Reines (Frederick Reines), Francis B. Harrison (Francis B. Harrison), Herald W. Kruse (Herald W. Kruse) oraz Austin D. McGuire (Austin D. McGuire) wykryli neutrino w eksperymencie Cowana–Reinesa (Cowan–Reines neutrino experiment) i przesłali wyniki do czasopisma *Science* (Science), potwierdzając rzeczywiste istnienie tej cząstki. Frederick Reines otrzymał za ten wkład Nagrodę Nobla z fizyki w 11995 roku.  
> W tym sensie badania rozpadu beta mają w historii nauki duże znaczenie także dlatego, że dostarczyły wskazówek dotyczących istnienia neutrina.
{: .prompt-info }

### Łańcuch rozpadu (Decay Chain)
Często zdarza się, że *nuklid potomny (daughter nuclide)* powstały w wyniku rozpadu beta również jest niestabilny, przez co kolejne rozpady beta zachodzą jeden po drugim. Prowadzi to do *łańcucha rozpadu (decay chain)*, jak poniżej.

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (stable)} $$

### Ważne rozpady beta
Poniżej przedstawiam kilka istotnych rozpadów beta.

#### Węgiel-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> Węgiel-14 jest naturalnie wytwarzany w górnych warstwach atmosfery przez promieniowanie kosmiczne, dzięki czemu jego stężenie w atmosferze utrzymuje się w przybliżeniu na stałym poziomie. Rośliny i zwierzęta podczas życia oddychają i wymieniają gazy z atmosferą, przez co mają w organizmie stężenie węgla-14 takie samo jak w powietrzu. Po śmierci wymiana ta ustaje i zawartość węgla-14 w szczątkach z czasem zanika. Wykorzystuje to datowanie radiowęglowe.
{: .prompt-tip }

#### Potas-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> Potas-40 jest największym (pod względem udziału w organizmie) naturalnym źródłem promieniowania w ciałach wszystkich zwierząt, w tym człowieka. Występuje naturalnie we wszystkich spożywanych na co dzień produktach, a szczególnie dużo jest go m.in. w orzechach brazylijskich, fasoli, szpinaku, bananach, awokado, kawie, włoszczuku, czosnku i podobnych produktach.  
> Ilość potasu w organizmie dorosłej osoby o masie 70 kg wynosi około 140 g i pozostaje w przybliżeniu stała; z tego około 0.014 g stanowi potas-40, co odpowiada aktywności ok. 4330 Bq.
{: .prompt-tip }

#### Tryt
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> Tryt jest paliwem biorącym udział w reakcji syntezy jądrowej D–T w reaktorach termojądrowych lub w broni typu bomba wodorowa$\cdot$bomba neutronowa. Powstaje naturalnie w atmosferze wskutek promieniowania kosmicznego, ale ponieważ ma krótki okres półtrwania (ok. 12.32 roku), szybko się rozpada i w przyrodzie występuje w bardzo małym udziale. Przy wykorzystaniu w reaktorach termojądrowych lub w broni jądrowej, ze względu na tę szybką degradację zwykle nie „ładuje się” trytu bezpośrednio, tylko napromieniowuje się neutronami lit-6, aby wytworzyć tryt. Dlatego wysoko wzbogacony$\cdot$wysokiej czystości lit-6 klasy wojskowej jest uznawany za kluczowy materiał w rozwoju broni jądrowej i stanowi jeden z głównych obiektów monitoringu społeczności międzynarodowej, w tym MAEA (IAEA).  
> Niezależnie od powyższych zastosowań, tryt bywa również używany w niewielkich ilościach: jako substancja świecąca w sprzęcie wojskowym (np. nocne przyrządy celownicze karabinu K2 i pistoletu maszynowego K1), w świecących zegarkach, czy w znakach „wyjście ewakuacyjne” w budynkach, które muszą świecić długo bez zasilania. Działa to tak, że tryt zamyka się w materiale fluorescencyjnym (fosforze); promieniowanie beta z rozpadu trytu wzbudza fosfor i powoduje emisję światła. W przypadku oznakowania wyjść ewakuacyjnych stosuje się ok. 900 miliardów bekereli trytu.  
> Ponieważ popyt jest stały, a długotrwałe magazynowanie jest niemożliwe, tryt jest traktowany jako ważny materiał strategiczny; jego cena zbliża się do 30 tys. dolarów za gram. Obecnie większość trytu produkowanego i sprzedawanego komercyjnie pochodzi z reaktorów CANDU (CANada Deuterium Uranium), czyli ciężkowodnych reaktorów ciśnieniowych; w Korei Południowej blokami CANDU są Wolsong 1–4.
{: .prompt-tip }

#### Cez-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> Cez-137 jest jednym z głównych produktów ubocznych reakcji rozszczepienia w reaktorach oraz prób jądrowych. Ze względu na stosunkowo długi okres półtrwania (ok. 30 lat), emisję silnie penetrującego promieniowania gamma oraz podobieństwo chemiczne do potasu (co ułatwia wchłanianie przez organizm) jest ważnym nuklidem podlegającym monitorowaniu i kontroli. Naturalnie praktycznie nie występował, ale obecnie w skali globalnej w glebie znajduje się średnio ok. 7 μg/g, co jest skutkiem m.in. testu jądrowego Trinity przeprowadzonego przez USA oraz zrzucenia bomb atomowych na Hiroszimę$\cdot$Nagasaki, a także licznych atmosferycznych prób jądrowych z lat 11950–11960 oraz kilku poważnych wypadków jądrowych (awaria elektrowni jądrowej w Czarnobylu, zdarzenie radiacyjne w Goiânii w Brazylii itp.).  
> W przypadku wchłonięcia do organizmu cezu-137 o aktywności przekraczającej 10000 Bq może być potrzebne postępowanie medyczne i obserwacja. Podczas awarii w Czarnobylu u części okolicznych mieszkańców raportowano wchłonięcie cezu-137 odpowiadające aktywności rzędu dziesiątek tysięcy Bq. W przypadku awarii w Fukushimie bezpośrednio po zdarzeniu w organizmach okolicznych mieszkańców miało zostać wchłonięte ok. 50–250 Bq.  
> Wartości różnią się osobniczo i między źródłami, ale bez leczenia biologiczny okres półtrwania cezu-137 według CDC wynosi [około 110 dni](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp). Jeśli podejrzewa się ekspozycję na duże ilości cezu-137, można [przyjąć medyczne tabletki „Prussian blue”, aby przyspieszyć wydalanie i skrócić biologiczny okres półtrwania do ok. 30 dni](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp).
{: .prompt-tip }

## Wychwyt elektronu (Electron Capture) lub wychwyt K (K-capture)

$$ p + e \to n + \nu_e $$

- Zachodzi, gdy neutronów jest relatywnie za mało
- Wychwytywany jest elektron z najbardziej wewnętrznej powłoki (powłoki K), co przekształca proton w jądrze w neutron
- Liczba atomowa maleje o 1, liczba masowa nie zmienia się
- Po wychwycie elektronu w chmurze elektronowej powstaje „dziura”, która następnie jest wypełniana przez przejście elektronu z bardziej zewnętrznej powłoki; w tym procesie emitowane jest promieniowanie rentgenowskie lub elektron Augera (Auger electron)
- Nuklid potomny (daughter nuclide) powstały w wyniku wychwytu elektronu jest taki sam jak jądro powstałe w rozpadzie $\beta^+$, więc oba procesy konkurują ze sobą.

## Rozpad alfa ($\alpha$-decay)
- Emisja cząstki alfa ($\alpha$, $^4_2\mathrm{He}$)
- Liczba atomowa maleje o 2, a liczba masowa maleje o 4
- Częsty w jądrach cięższych od ołowiu
- W przeciwieństwie do rozpadu beta, energia cząstki alfa emitowanej w rozpadzie alfa jest skwantowana.

Przykład) $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Samorzutne rozszczepienie (Spontaneous Fission)
- Bardzo ciężkie i niestabilne nuklidy potrafią ulegać rozszczepieniu samorzutnie, nawet bez pochłaniania neutronu
- W szerokim ujęciu zalicza się je do rozpadu promieniotwórczego
- Uran-238 rozpada się alfa z okresem półtrwania $10^9$ lat, ale jednocześnie bardzo rzadko ulega samorzutnemu rozszczepieniu z okresem półtrwania rzędu $10^{16}$ lat. Poniższa tabela przedstawia okresy półtrwania samorzutnego rozszczepienia dla kilku nuklidów.

| Nuklid | Okres półtrwania samorzutnego rozszczepienia | Cechy |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | ok. $10^{16}$ lat | zachodzi bardzo rzadko |
| $^{240}\mathrm{Pu}$ | ok. $10^{11}$ lat | rozszczepialny nuklid używany w broni jądrowej |
| $^{252}\mathrm{Cf}$ | ok. $2.6$ roku | samorzutne rozszczepienie zachodzi wyjątkowo intensywnie <br>$\rightarrow$ używany jako źródło neutronów np. do rozruchu reaktorów |

## Emisja protonu (Proton Emission)
- W przypadku niestabilnych nuklidów o skrajnie dużej liczbie protonów zdarza się emisja pojedynczego protonu
- Liczba atomowa i liczba masowa maleją o 1
- Zjawisko bardzo rzadkie

## Schemat rozpadu i przejście izomeryczne
### Schemat rozpadu (Decay Scheme)
*Szmat rozpadu (decay scheme)*: diagram, który wizualnie przedstawia wszystkie drogi rozpadu substancji promieniotwórczej

### Przejście izomeryczne (Isomeric Transition)
- Jądro powstałe w wyniku rozpadu promieniotwórczego może pozostać w stanie wzbudzonym; wówczas emituje energię w postaci promieniowania gamma (ponieważ przy emisji gamma nuklid się nie zmienia, ściśle rzecz biorąc nie jest to rozpad, ale zwyczajowo używa się też określenia „rozpad gamma”). 
- Stan wzbudzony zwykle w bardzo krótkim czasie emituje promieniowanie gamma i przechodzi do stanu podstawowego, ale w pewnych przypadkach emisja gamma jest opóźniona i jądro wygląda jakby było w stanie metastabilnym. Taki stan opóźniony nazywa się *stanem izomerycznym (isomeric states)*.
- Emisję gamma w stanie izomerycznym i przejście do stanu podstawowego nazywa się *przejściem izomerycznym (isomeric transition)* i oznacza się jako IT.

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia z Wielkiej Brytanii [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - licencja: o ile nie jest to sprzeczne z prawem, można używać swobodnie bez ograniczeń i na dowolny cel

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> licencja: [Public Domain](https://en.wikipedia.org/wiki/Public_domain)
