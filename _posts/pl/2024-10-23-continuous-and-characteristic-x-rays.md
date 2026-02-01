---
title: Ciągłe promieniowanie X i promieniowanie X charakterystyczne (Continuous and Characteristic X Rays)
description: Omawiamy dwa mechanizmy powstawania promieniowania X jako promieniowania atomowego oraz wynikające z nich cechy bremsstrahlung i promieniowania X charakterystycznego.
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **bremsstrahlung (promieniowanie hamowania, breaking radiation)**: promieniowanie X o widmie ciągłym emitowane, gdy naładowana cząstka (np. elektron) przechodzi w pobliżu jądra atomowego i jest przyspieszana przez oddziaływanie elektrostatyczne
> - minimalna długość fali: $\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **promieniowanie X charakterystyczne (characteristic X-ray)**: promieniowanie X o widmie nieciągłym, emitowane gdy elektron padający zjonizuje atom przez zderzenie z elektronem wewnętrznej powłoki, a następnie inny elektron z powłoki zewnętrznej przechodzi na powstałe wewnętrzne wakatowe miejsce, emitując foton o energii równej różnicy poziomów energii
{: .prompt-info }

## Wymagania wstępne
- [Cząstki subatomowe i składniki atomu](/posts/constituents-of-an-atom/)

## Odkrycie promieniowania X
Röntgen odkrył, że gdy wiązka elektronów pada na tarczę, powstaje promieniowanie X. W chwili odkrycia nie wiedziano jeszcze, że promieniowanie X jest falą elektromagnetyczną, dlatego — w znaczeniu „nieznane” — nazwano je **promieniowaniem X (X-ray)**. Nazywa się je też **promieniowaniem Röntgena (Röntgen radiation)** od nazwiska odkrywcy.

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

Powyższy rysunek w prosty sposób przedstawia typową budowę lampy rentgenowskiej (X-ray tube). W jej wnętrzu, w warunkach próżni, hermetycznie zamknięte są: katoda z żarnikiem wolframowym oraz anoda, do której przymocowana jest tarcza. Po przyłożeniu wysokiego napięcia rzędu kilkudziesięciu kV między elektrodami elektrony są emitowane z katody i bombardują tarczę anody, a z tego procesu emitowane jest promieniowanie X. Należy jednak pamiętać, że sprawność konwersji energii na promieniowanie X jest zwykle bardzo niska (zazwyczaj poniżej 1%), a pozostałe ponad 99% energii zamienia się w ciepło, dlatego potrzebne są dodatkowe układy chłodzenia.

## Bremsstrahlung (promieniowanie hamowania, braking radiation)
Gdy naładowana cząstka, taka jak elektron, przechodzi w pobliżu jądra atomowego, jej tor ulega gwałtownemu zakrzywieniu oraz następuje wyhamowanie wskutek elektrostatycznej siły przyciągania między cząstką a jądrem. Wówczas cząstka emituje energię w postaci promieniowania X. Ponieważ przemiana energii w tym procesie nie jest skwantowana, emitowane promieniowanie X ma widmo ciągłe; nazywa się je **bremsstrahlung** albo **promieniowaniem hamowania (braking radiation)**.

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

Oczywiście energia fotonu promieniowania X emitowanego w procesie bremsstrahlung nie może przekroczyć energii kinetycznej elektronu padającego. Zatem istnieje minimalna długość fali emitowanego promieniowania X, którą można łatwo wyznaczyć z poniższego wzoru.

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

Ponieważ stała Plancka $h$ i prędkość światła $c$ są stałymi, minimalna długość fali zależy wyłącznie od energii elektronu padającego. Długość fali $\lambda$ odpowiadająca energii $1\text{eV}$ wynosi około $1.24 \mu\text{m}=12400\text{Å}$. Zatem minimalna długość fali $\lambda_\text{min}$ dla lampy rentgenowskiej z przyłożonym napięciem $V$ wynosi jak poniżej. W praktyce często korzysta się właśnie z tego wzoru.

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

Poniższy wykres przedstawia widmo ciągłego promieniowania X przy zmianie napięcia, przy stałym prądzie lampy. Wraz ze wzrostem napięcia minimalna długość fali $\lambda_{\text{min}}$ skraca się, a całkowita intensywność promieniowania X rośnie.

![Typical continuous X-ray spectra from tube operating
at three different peak voltages with the same current](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## Promieniowanie X charakterystyczne (characteristic X-ray)
Jeśli napięcie przyłożone do lampy rentgenowskiej jest dostatecznie wysokie, elektron padający może zderzyć się z elektronem znajdującym się na wewnętrznej powłoce atomu tarczy i zjonizować ten atom. W takiej sytuacji elektron z powłoki zewnętrznej szybko oddaje energię i wypełnia wakat na powłoce wewnętrznej; w tym procesie powstaje foton promieniowania X o energii równej różnicy między dwoma poziomami energii. Widmo promieniowania X emitowanego w tym mechanizmie jest nieciągłe, jest wyznaczone przez własne poziomy energetyczne atomu tarczy i nie zależy od energii ani natężenia wiązki elektronów padających. Nazywa się je **promieniowaniem X charakterystycznym (characteristic X-ray)**.

### Notacja Siegbahna

![Siegbahn notation of electron transitions between shells](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *Źródło grafiki*
> - autor: użytkownik angielskiej Wikipedii [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Zgodnie z notacją Siegbahna, gdy wakat na powłoce K jest wypełniany przez elektron z powłoki L, M, ... emitowane promieniowanie X oznacza się — jak na rysunku — jako $K_\alpha$, $K_\beta$, ... Jednak po wprowadzeniu nowoczesnego modelu atomu (po notacji Siegbahna) ustalono, że w atomach wieloelektronowych nawet w obrębie danej „powłoki” w sensie modelu Bohra (poziomów o tej samej głównej liczbie kwantowej) energie zależą od innych liczb kwantowych. W konsekwencji także linie $K_\alpha$, $K_\beta$, ... podzielono dalej na bardziej szczegółowe klasy, takie jak $K_{\alpha_1}$, $K_{\alpha_2}$, ... .

![Siegbahn notation](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

Ta tradycyjna notacja jest nadal szeroko stosowana w spektroskopii. Ponieważ jednak nazewnictwo nie jest w pełni systematyczne i bywa źródłem nieporozumień, *Międzynarodowa Unia Chemii Czystej i Stosowanej (IUPAC)* zaleca używanie alternatywnej notacji przedstawionej poniżej.

### Notacja IUPAC
Standardowa notacja zalecana przez IUPAC dla orbitali atomowych i promieniowania X charakterystycznego jest następująca. Najpierw poszczególnym orbitalom przypisuje się nazwy zgodnie z tabelą poniżej.

| $n$(główna liczba kwantowa) | $l$(poboczna/azymutalna liczba kwantowa) | $s$(spinowa liczba kwantowa) | $j$(liczba kwantowa całkowitego momentu pędu) | orbital atomowy | oznaczenie promieniowania X |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0$ | $\pm1/2$ | $1/2$ | $1s_{1/2}$ | $K_{(1)}$ |
| $2$ | $0$ | $\pm1/2$ | $1/2$ | $2s_{1/2}$ | $L_1$ |
| $2$ | $1$ | $-1/2$ | $1/2$ | $2p_{1/2}$ | $L_2$ |
| $2$ | $1$ | $+1/2$ | $3/2$ | $2p_{3/2}$ | $L_3$ |
| $3$ | $0$ | $\pm1/2$ | $1/2$ | $3s_{1/2}$ | $M_1$ |
| $3$ | $1$ | $-1/2$ | $1/2$ | $3p_{1/2}$ | $M_2$ |
| $3$ | $1$ | $+1/2$ | $3/2$ | $3p_{3/2}$ | $M_3$ |
| $3$ | $2$ | $-1/2$ | $3/2$ | $3d_{3/2}$ | $M_4$ |
| $3$ | $2$ | $+1/2$ | $5/2$ | $3d_{5/2}$ | $M_5$ |
| $4$ | $0$ | $\pm1/2$ | $1/2$ | $4s_{1/2}$ | $N_1$ |
| $4$ | $1$ | $-1/2$ | $1/2$ | $4p_{1/2}$ | $N_2$ |
| $4$ | $1$ | $+1/2$ | $3/2$ | $4p_{3/2}$ | $N_3$ |
| $4$ | $2$ | $-1/2$ | $3/2$ | $4d_{3/2}$ | $N_4$ |
| $4$ | $2$ | $+1/2$ | $5/2$ | $4d_{5/2}$ | $N_5$ |
| $4$ | $3$ | $-1/2$ | $5/2$ | $4f_{5/2}$ | $N_6$ |
| $4$ | $3$ | $+1/2$ | $7/2$ | $4f_{7/2}$ | $N_7$ |

> Całkowita liczba kwantowa momentu pędu $j=\|l+s\|$.
{: .prompt-info }

Następnie promieniowanie X charakterystyczne emitowane, gdy elektron w atomie przechodzi z danego poziomu energii na poziom niższy, oznacza się zgodnie z regułą:

$$ \text{(oznaczenie X dla późniejszego poziomu energii)-(oznaczenie X dla wcześniejszego poziomu energii)} $$

Na przykład promieniowanie X charakterystyczne emitowane przy przejściu elektronu z orbitali $2p_{1/2}$ na $1s_{1/2}$ można oznaczyć jako $\text{K-L}_2$.

## Widmo promieniowania X

![Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

Powyżej pokazano widmo promieniowania X emitowanego podczas bombardowania tarczy z rodu (Rh) wiązką elektronów przyspieszoną napięciem 60 kV. Widać gładką, ciągłą krzywą pochodzącą od bremsstrahlung, a zgodnie ze wzorem ($\ref{eqn:lambda_min}$) można potwierdzić, że promieniowanie X jest emitowane tylko dla długości fali większych niż około $0.207\text{Å} = 20.7\text{pm} $. Ponadto ostre piki widoczne miejscami na wykresie pochodzą od charakterystycznego promieniowania X związanego z powłoką K atomu rodu. Jak wspomniano wcześniej, ponieważ widmo promieniowania X charakterystycznego jest unikalne dla danego pierwiastka tarczy, analizując długości fal, przy których w widmie pojawiają się „spike’i” (piki), można zidentyfikować skład pierwiastkowy tarczy.

> Oprócz $K_\alpha, K_\beta, \dots$ emitowane jest oczywiście także promieniowanie X o niższej energii, takie jak $L_\alpha, L_\beta, \dots$. Ma ono jednak znacznie mniejszą energię i zwykle jest pochłaniane przez obudowę lampy (housing), przez co nie dociera do detektora.
{: .prompt-info }
