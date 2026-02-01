---
title: Pole grawitacyjne i potencjał grawitacyjny
description: "Definicje wektora pola grawitacyjnego i potencjału grawitacyjnego wynikające z newtonowskiego prawa powszechnego ciążenia, a także dwa kluczowe przykłady: twierdzenie o powłoce sferycznej i krzywe rotacji galaktyk."
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Prawo powszechnego ciążenia Newtona: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Dla ciągłego rozkładu masy i ciał o skończonych rozmiarach: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: gęstość masy w punkcie o wektorze położenia $\mathbf{r^{\prime}}$ względem dowolnie wybranego początku układu
>   - $dv^{\prime}$: element objętości w punkcie o wektorze położenia $\mathbf{r^{\prime}}$ względem dowolnie wybranego początku układu
> - **Wektor pola grawitacyjnego (gravitational field vector)**:
>   - wektor opisujący siłę przypadającą na jednostkę masy, jakiej doświadcza cząstka w polu wytworzonym przez masę $M$
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - ma wymiar *siły na jednostkę masy* albo *przyspieszenia*
> - **Potencjał grawitacyjny (gravitational potential)**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - ma wymiar $($*siła na jednostkę masy* $) \times ($*odległość* $)$ albo *energia na jednostkę masy*
>   - $\Phi = -G\cfrac{M}{r}$
>   - sens fizyczny ma jedynie różnica potencjałów, a nie bezwzględna wartość $\Phi$
>   - zwykle arbitralnie przyjmuje się warunek $\Phi \to 0$ dla $r \to \infty$, aby usunąć niejednoznaczność (ambiguity)
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Potencjał grawitacyjny wewnątrz i na zewnątrz powłoki sferycznej (twierdzenie o powłoce)**
>   - Gdy $R>a$:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - przy wyznaczaniu potencjału grawitacyjnego w punkcie zewnętrznym od sferycznie symetrycznego rozkładu masy (spherical symmetric distribution) można traktować ciało jak masę punktową (point mass)
>   - Gdy $R<b$:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - wewnątrz sferycznie symetrycznej powłoki masy potencjał jest stały (niezależny od położenia), a działająca grawitacja wynosi $0$
>   - Gdy $b<R<a$: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## Pole grawitacyjne
### Prawo powszechnego ciążenia Newtona
Newton już przed 11666 HE usystematyzował prawo powszechnego ciążenia i zweryfikował je także ilościowo. Mimo to publikacja jego wyników w dziele *Principia* w 11687 HE zajęła mu kolejne 20 lat — ponieważ nie potrafił uzasadnić metody obliczeń wykonywanych przy założeniu, że Ziemia i Księżyc są masami punktowymi (point mass), tj. nie mają rozmiaru. Na szczęście, korzystając z rachunku różniczkowego i całkowego, który Newton wynalazł później, możemy dziś dużo łatwiej udowodnić to, co w 11600 latach nie było dla Newtona proste: [że problem ten da się poprawnie rozwiązać](#gdy-ra).

Zgodnie z prawem powszechnego ciążenia Newtona (Newton's law of universal gravitation), *każda cząstka masy przyciąga każdą inną cząstkę we Wszechświecie siłą proporcjonalną do iloczynu ich mas i odwrotnie proporcjonalną do kwadratu odległości między nimi.* Matematycznie:

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - licencja: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

Wektor jednostkowy $\mathbf{e}_r$ jest skierowany od $M$ w stronę $m$, a znak minus oznacza, że siła jest przyciągająca. Innymi słowy, $m$ jest przyciągane w stronę $M$.

### Eksperyment Cavendisha
Eksperymentalna weryfikacja tego prawa oraz wyznaczenie wartości $G$ zostały dokonane w 11798 HE przez brytyjskiego fizyka Henry'ego Cavendisha (Henry Cavendish). Eksperyment Cavendisha wykorzystuje wagę skręceń (torsion balance) złożoną z dwóch małych kul przymocowanych do końców lekkiego pręta. Dwie małe kule są przyciągane przez dwie inne, duże kule znajdujące się w pobliżu. Oficjalna wartość $G$ wyznaczona dotychczas wynosi $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> Mimo że $G$ jest jedną z najdawniej znanych stałych fundamentalnych, znamy ją jedynie z mniejszą precyzją (precision) niż większość innych stałych, takich jak $e$, $c$ czy $\hbar$. Do dziś prowadzi się liczne badania mające na celu wyznaczenie $G$ z większą dokładnością.
{: .prompt-tip }

### Przypadek ciał o skończonych rozmiarach
Prawo z równania ($\ref{eqn:law_of_gravitation}$) ściśle rzecz biorąc można stosować tylko do *cząstek punktowych (point particle)*. Jeżeli jedno z ciał (lub oba) ma skończone rozmiary, aby obliczyć siłę, trzeba dodatkowo założyć, że pole grawitacyjne (gravitational force field) jest *polem liniowym (linear field)*. To znaczy: zakładamy, że całkowita grawitacja działająca na cząstkę o masie $m$ od wielu innych cząstek jest sumą wektorową poszczególnych sił. Dla ciągłego rozkładu materii zamieniamy sumę na całkę:

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: gęstość masy w punkcie o wektorze położenia $\mathbf{r^{\prime}}$ względem dowolnego początku układu
- $dv^{\prime}$: element objętości w punkcie o wektorze położenia $\mathbf{r^{\prime}}$ względem dowolnego początku układu

Jeśli zarówno ciało o masie $M$, jak i ciało o masie $m$ mają skończone rozmiary i chcemy wyznaczyć całkowitą siłę grawitacyjną, potrzebna jest także druga całka objętościowa po objętości ciała $m$.

### Wektor pola grawitacyjnego
**Wektor pola grawitacyjnego (gravitational field vector)** $\mathbf{g}$ definiuje się jako wektor siły przypadającej na jednostkę masy, jakiej doświadcza cząstka w polu wytworzonym przez ciało o masie $M$:

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

albo

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

Przy czym kierunek $\mathbf{e}_r$ zależy od $\mathbf{r^\prime}$.

Wielkość $\mathbf{g}$ ma wymiar *siły na jednostkę masy* albo *przyspieszenia*. W pobliżu powierzchni Ziemi moduł wektora pola grawitacyjnego $\mathbf{g}$ jest równy temu, co nazywamy **stałą przyspieszenia grawitacyjnego (gravitational acceleration constant)**: $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$.

## Potencjał grawitacyjny
### Definicja
Wektor pola grawitacyjnego $\mathbf{g}$ zmienia się jak $1/r^2$, zatem spełnia warunek umożliwiający przedstawienie go jako gradientu pewnej funkcji skalarnej (potencjału), tj. ($\nabla \times \mathbf{g} \equiv 0$). Wobec tego można napisać:

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

Tutaj $\Phi$ nazywamy **potencjałem grawitacyjnym (gravitational potential)**; ma on wymiar $($*siła na jednostkę masy* $) \times ($*odległość* $)$ albo *energia na jednostkę masy*.

Ponieważ $\mathbf{g}$ zależy tylko od promienia, $\Phi$ również zmienia się wraz z $r$. Z równań ($\ref{eqn:g_vector}$) i ($\ref{eqn:gradient_phi}$) wynika

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

a po scałkowaniu:

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

Ponieważ sens fizyczny ma tylko różnica potencjału grawitacyjnego, a nie jego wartość bezwzględna, stałą całkowania można pominąć. Zwykle arbitralnie narzuca się warunek $\Phi \to 0$ dla $r \to \infty$, aby usunąć niejednoznaczność (ambiguity); równanie ($\ref{eqn:g_potential}$) spełnia ten warunek.

Dla ciągłego rozkładu materii potencjał grawitacyjny ma postać:

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Jeśli masa jest rozłożona powierzchniowo na cienkiej powłoce:

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

Natomiast dla liniowego źródła masy o gęstości liniowej $\rho_l$:

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Znaczenie fizyczne
Rozważmy pracę na jednostkę masy $dW^\prime$, jaką wykonuje ciało, gdy przemieszcza się w polu grawitacyjnym o $d\mathbf{r}$.

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

W tym równaniu $\Phi$ jest funkcją wyłącznie współrzędnych położenia: $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Zatem, gdy przesuwamy ciało w polu grawitacyjnym z jednego punktu do drugiego, praca na jednostkę masy jest równa różnicy potencjałów między tymi punktami.

Jeśli zdefiniujemy potencjał grawitacyjny w nieskończoności jako $0$, to $\Phi$ w dowolnym punkcie można interpretować jako pracę na jednostkę masy potrzebną do przemieszczenia ciała z nieskończoności do tego punktu. Energia potencjalna ciała jest równa iloczynowi jego masy i potencjału grawitacyjnego $\Phi$, więc dla energii potencjalnej $U$:

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

W konsekwencji siłę grawitacyjną działającą na ciało otrzymujemy jako ujemny gradient jego energii potencjalnej:

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Gdy obiekt znajduje się w polu grawitacyjnym wytworzonym przez pewną masę, zawsze pojawia się pewna energia potencjalna. Ściśle rzecz biorąc, ta energia jest „w polu”, ale zwyczajowo mówi się o niej jako o energii potencjalnej danego obiektu.

## Przykład: potencjał grawitacyjny wewnątrz i na zewnątrz powłoki sferycznej (twierdzenie o powłoce)
### Ustalenie układu współrzędnych i zapis potencjału grawitacyjnego w postaci całki
Wyznaczmy potencjał grawitacyjny wewnątrz i na zewnątrz jednorodnej powłoki sferycznej (spherical shell) o promieniu wewnętrznym $b$ i zewnętrznym $a$. Grawitację od powłoki można otrzymać, licząc bezpośrednio składowe siły działającej na jednostkę masy, ale metoda potencjałowa jest prostsza.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Policzmy potencjał w punkcie $P$, oddalonym od środka o $R$. Przy założeniu jednorodnego rozkładu masy powłoki mamy $\rho(r^\prime)=\rho$, a ze względu na symetrię osiową względem prostej łączącej środek kuli z punktem $P$ (symetria względem kąta azymutalnego $\phi$):

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

Z prawa cosinusów:

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

a ponieważ $R$ jest stałe, różniczkując to równanie po $r^\prime$, otrzymujemy:

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

Po podstawieniu do ($\ref{eqn:spherical_shell_1}$):

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

Gdzie $r_\mathrm{max}$ i $r_\mathrm{min}$ zależą od położenia punktu $P$.

### Gdy $R>a$

$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

Masa powłoki sferycznej wynosi:

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

więc potencjał:

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> Porównując wzór na potencjał grawitacyjny od masy punktowej $M$ — równanie ($\ref{eqn:g_potential}$) — z dopiero co uzyskanym wynikiem ($\ref{eqn:spherical_shell_outside_2}$), widzimy, że są identyczne. Oznacza to, że wyznaczając potencjał grawitacyjny w dowolnym punkcie zewnętrznym od sferycznie symetrycznego rozkładu masy (spherical symmetric distribution), możemy bez szkody traktować całą masę jak skupioną w centrum. Dotyczy to większości obiektów astronomicznych o kształcie zbliżonym do kuli i dostatecznie dużych rozmiarach, takich jak Ziemia czy Księżyc; można je traktować jak [matrioszki](https://en.wikipedia.org/wiki/Matryoshka_doll): niezliczone powłoki sferyczne o wspólnym środku i różnych promieniach, nałożone jedna na drugą. Stanowi to uzasadnienie przyjętego na początku tego tekstu założenia, że [ciała niebieskie takie jak Ziemia czy Księżyc można traktować jak masy punktowe](#prawo-powszechnego-ci%C4%85%C5%BCenia-newtona).
{: .prompt-info }

### Gdy $R<b$

$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> Wewnątrz sferycznie symetrycznej powłoki masy potencjał grawitacyjny jest stały (niezależny od położenia), a działająca grawitacja wynosi $0$.
{: .prompt-info }

> Jest to też jedna z głównych przesłanek, że popularna pseudonauka w rodzaju „teorii pustej Ziemi” to kompletna bzdura. Gdyby Ziemia miała postać powłoki sferycznej z pustym wnętrzem — jak głosi ta teoria — wówczas na wszystkie obiekty znajdujące się w tej pustce nie działałaby grawitacja Ziemi. Patrząc na masę i objętość Ziemi, nie ma zresztą miejsca na taką „pustkę”; a nawet gdyby istniała, hipotetyczne istoty żywe nie chodziłyby po „wewnętrznej powierzchni” powłoki jak po ziemi, tylko unosiłyby się w stanie nieważkości jak na stacji kosmicznej.  
> [Mikroorganizmy mogą co prawda żyć głęboko pod powierzchnią, na głębokości kilku km](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), ale przynajmniej w formie postulowanej przez teorię pustej Ziemi jest to niemożliwe. Bardzo lubię powieść Juliusza Verne’a *Podróż do wnętrza Ziemi (Voyage au centre de la Terre)* i film „Podróż do wnętrza Ziemi (Journey to the Center of the Earth)”, ale fikcję trzeba traktować jako fikcję — nie wierzmy w nią na serio.
{: .prompt-tip }

### Gdy $b<R<a$

$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Wyniki
Wykresy potencjału grawitacyjnego $\Phi$ w trzech obszarach oraz odpowiadającego mu modułu wektora pola $\|\mathbf{g}\|$ jako funkcji odległości $R$ wyglądają następująco:

![Gravitational Potential as a Function of R](/physics-visualizations/figs/shell-theorem-gravitational-potential.png)  
![Magnitude of the Field Vector as a Function of R](/physics-visualizations/figs/shell-theorem-field-vector.png)  
> - Kod wizualizacji w Pythonie: [repozytorium yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/shell_theorem.py)
> - Licencja: [Zobacz tutaj](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Widać, że potencjał grawitacyjny i moduł wektora pola grawitacyjnego są funkcjami ciągłymi. Gdyby potencjał grawitacyjny był w jakimś punkcie nieciągły, wówczas gradient potencjału — czyli wartość grawitacji — byłby w tym punkcie nieskończony, co jest fizycznie nieuzasadnione; zatem funkcja potencjału musi być ciągła w każdym punkcie. Natomiast *pochodna* wektora pola grawitacyjnego jest nieciągła na wewnętrznej i zewnętrznej powierzchni powłoki.

## Przykład: krzywe rotacji galaktyk
Z obserwacji astronomicznych wynika, że w wielu galaktykach spiralnych obracających się wokół centrum — takich jak Droga Mleczna czy Galaktyka Andromedy — większość obserwowalnej masy jest silnie skoncentrowana w pobliżu centrum. Jednak prędkości orbitalne mas w tych galaktykach, jak widać na poniższym wykresie, znacząco odbiegają od wartości teoretycznie przewidywanych na podstawie obserwowalnego rozkładu masy i po pewnej odległości pozostają prawie stałe.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Źródło obrazu*
> - autor: użytkownik Wikipedii [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - licencja: Public Domain

{% 
  include embed/video.html 
  src='https://cdn.jsdelivr.net/gh/yunseo-kim/yunseo-kim.github.io/assets/video/gravitational-field-and-potential/Galaxy_rotation_under_the_influence_of_dark_matter.webm' 
  title="Po lewej: rotacja galaktyki przewidziana na podstawie obserwowalnej masy | Po prawej: rotacja galaktyki faktycznie obserwowana." 
  types='ogg'
  autoplay=true 
  loop=true 
%}
> *Źródło wideo*
> - link do pliku źródłowego (Ogg Theora video): <https://commons.wikimedia.org/wiki/File:Galaxy_rotation_under_the_influence_of_dark_matter.ogv>
> - autor: [Ingo Berg](https://beltoforion.de/en/index.php)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
> - wykorzystana metoda symulacji i kod: <https://beltoforion.de/en/spiral_galaxy_renderer/>

> Poprzednio osadzony na tej stronie plik obrazu `Rotation curve of spiral galaxy Messier 33 (Triangulum).png` został usunięty z Wikimedia Commons, ponieważ użytkownik Wikimedia [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama) okazał się opublikować go jako utwór zależny powstały w wyniku plagiatu nie-wolnego utworu należącego do [prof. Marka Whittle’a z University of Virginia](https://markwhittle.uvacreate.virginia.edu/), bez właściwego cytowania; w związku z tym usunąłem go również z tej strony: <https://commons.wikimedia.org/wiki/Commons:Deletion_requests/File:Rotation_curve_of_spiral_galaxy_Messier_33_(Triangulum).png>.
{: .prompt-danger }

Przewidźmy prędkość orbitalną w funkcji odległości w przypadku, gdy masa galaktyki jest skoncentrowana w centrum, i sprawdźmy, że taka prognoza nie zgadza się z obserwacjami. Następnie pokażmy, że aby wyjaśnić wyniki obserwacji, masa $M(R)$ rozłożona wewnątrz promienia $R$ od centrum galaktyki musi być proporcjonalna do $R$.

Najpierw, jeśli masa galaktyki $M$ jest skupiona w centrum, prędkość orbitalna w odległości $R$ wynosi:

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

W tym przypadku, jak pokazuje linia przerywana na wykresach powyżej, przewidujemy spadek prędkości orbitalnej jak $1/\sqrt{R}$. Jednak obserwacje wskazują, że prędkość orbitalna $v$ jest prawie stała niezależnie od odległości $R$, więc teoria i obserwacje nie są zgodne. Takie wyniki obserwacyjne można wyjaśnić tylko wtedy, gdy $M(R)\propto R$.

Wprowadzając stałą proporcjonalności $k$ i przyjmując $M(R) = kR$, dostajemy:

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(stała)}. $$

Na tej podstawie astrofizycy wnioskują, że w wielu galaktykach musi istnieć nieodkryta jeszcze „ciemna materia (dark matter)” i że taka ciemna materia powinna stanowić ponad 90% masy Wszechświata. Jednak natura ciemnej materii nadal nie jest jednoznacznie wyjaśniona; istnieją też próby wyjaśnienia obserwacji bez zakładania jej istnienia — niebędące jednak teorią dominującą — takie jak zmodyfikowana dynamika Newtonowska (Modified Newtonian Dynamics, MOND). Obecnie jest to jedna z najbardziej „frontowych” dziedzin badań w astrofizyce.
