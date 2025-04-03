---
title: Stabilité nucléaire et désintégration radioactive
description: Découvrez le tableau de Segrè, les différents types de désintégration radioactive, le spectre d'énergie des électrons/positrons émis lors de la désintégration bêta et le contexte de la découverte du neutrino, les chaînes de désintégration de certains nucléides importants (carbone-14, potassium-40, tritium, césium-137), ainsi que la transition isomère.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Prérequis
- [Particules subatomiques et constituants de l'atome](/posts/constituents-of-an-atom/)

## Tableau de Segré (Segre Chart) ou carte des nucléides
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Source de l'image*
> - Auteur: Utilisateur Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Pour les nucléides dont le numéro atomique $Z$ est supérieur à 20, davantage de neutrons que de protons sont nécessaires pour assurer la stabilité
- Les neutrons jouent un rôle dans la cohésion du noyau en contrebalançant la répulsion électrique entre les protons

## Raisons de la désintégration radioactive
- Seules certaines combinaisons de neutrons et de protons forment des nucléides stables
- Si le nombre de neutrons est trop élevé ou trop faible par rapport au nombre de protons, le nucléide est instable et subit une *désintégration radioactive*
- Le noyau formé après la désintégration est généralement dans un état excité et libère de l'énergie sous forme de rayons gamma ou de rayons X

## Désintégration bêta ($\beta$-decay)
### Désintégration bêta plus ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Se produit lorsque le nombre de neutrons est relativement insuffisant
- Un proton ($p$) se transforme en neutron ($n$) en émettant un positron ($\beta^+$) et un neutrino électronique ($\nu_e$)
- Le numéro atomique diminue de 1, le nombre de masse reste inchangé

Exemple: $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Désintégration bêta moins ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Se produit lorsque le nombre de neutrons est relativement excessif
- Un neutron ($n$) se transforme en proton ($p$) en émettant un électron ($\beta^-$) et un antineutrino électronique ($\overline{\nu}_e$)
- Le numéro atomique augmente de 1, le nombre de masse reste inchangé

Exemple: $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Spectre d'énergie des électrons (positrons) émis
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Source de l'image*
> - Auteur: Utilisateur Wikipédia allemand [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Les électrons ou positrons émis lors de la désintégration bêta présentent un spectre d'énergie continu comme ci-dessus.
- Désintégration $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- Désintégration $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

> Bien que l'énergie totale libérée lors de la désintégration bêta soit quantifiée, l'électron/positron et l'antineutrino/neutrino se partagent cette énergie de manière aléatoire, ce qui explique le spectre continu observé pour l'énergie de l'électron/positron.
> Le fait que le spectre d'énergie des électrons/positrons émis lors de la désintégration bêta ne soit pas quantifié mais continu était en contradiction avec les prédictions théoriques et semblait violer la loi de conservation de l'énergie.  
> Pour expliquer ce phénomène, Wolfgang Ernst Pauli a prédit en 11930 l'existence d'une "<u>particule électriquement neutre, de masse extrêmement faible et de très faible réactivité</u>" qu'il proposa d'appeler "neutron". Cependant, lorsque Sir James Chadwick découvrit et nomma le neutron tel que nous le connaissons aujourd'hui en 11932, un problème de duplication de nom surgit. En 11933, Enrico Fermi, en publiant sa théorie de la désintégration bêta, renomma cette particule *neutrino* en ajoutant le suffixe italien '-ino' signifiant "petit".  
> Plus tard, en 11942, le physicien nucléaire chinois Wang Ganchang (王淦昌) proposa pour la première fois une méthode de détection du neutrino utilisant la [capture électronique](#capture-électronique-electron-capture-ou-capture-k-k-capture). En 11956, Clyde Cowan, Frederick Reines, Francis B. Harrison, Herald W. Kruse et Austin D. McGuire réussirent à détecter le neutrino grâce à l'expérience Cowan-Reines et publièrent leurs résultats dans la revue Science, confirmant ainsi son existence. Frederick Reines reçut le prix Nobel de physique en 11995 pour cette contribution.  
> L'étude de la désintégration bêta a donc une importance historique majeure dans l'histoire des sciences car elle a fourni des indices sur l'existence du neutrino.
{: .prompt-info }

### Chaînes de désintégration (Decay Chain)
Souvent, le *nucléide fils (daughter nuclide)* formé par désintégration bêta est également instable et subit une désintégration bêta supplémentaire. Cela conduit à une *chaîne de désintégration* comme suit:

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (stable)} $$

Voici quelques chaînes de désintégration bêta importantes:

#### Carbone-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> Le carbone-14 est produit naturellement dans la haute atmosphère par les rayons cosmiques, maintenant ainsi une concentration relativement constante dans l'atmosphère. Les animaux et les plantes maintiennent également une concentration de carbone-14 identique à celle de l'atmosphère tant qu'ils respirent et échangent des gaz avec l'environnement. Après leur mort, ces échanges cessent et la concentration de carbone-14 dans les restes diminue progressivement. C'est ce principe qui est utilisé dans la datation au carbone radioactif.
{: .prompt-tip }

#### Potassium-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> Le potassium-40 est la source de radioactivité naturelle la plus importante dans le corps de tous les animaux, y compris les humains. Il est naturellement présent dans tous les aliments que nous consommons quotidiennement, particulièrement dans les noix du Brésil, les haricots, les épinards, les bananes, les avocats, le café, le poisson-sabre et l'ail.  
> Un adulte de 70 kg contient environ 140 g de potassium qui reste à un niveau constant, dont environ 0,014 g de potassium-40, ce qui représente une radioactivité d'environ 4330 Bq.
{: .prompt-tip }

#### Tritium
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> Le tritium est un matériau combustible participant aux réactions de fusion D-T dans les réacteurs à fusion ou les bombes à hydrogène/neutrons. Il est produit naturellement dans l'atmosphère par les rayons cosmiques, mais sa demi-vie relativement courte de 12,32 ans entraîne sa désintégration rapide, ce qui explique sa faible présence dans la nature. Dans les réacteurs à fusion ou les armes nucléaires, en raison de cette désintégration rapide, plutôt que d'utiliser directement le tritium, on préfère irradier du lithium-6 avec des neutrons pour produire du tritium. C'est pourquoi le lithium-6 hautement enrichi et purifié de qualité militaire est considéré comme un matériau essentiel au développement nucléaire et fait l'objet d'une surveillance internationale stricte, notamment par l'AIEA.  
> Même en dehors de ces applications, le tritium est utilisé en petites quantités dans divers produits : viseurs nocturnes des fusils K2 et des mitraillettes K1, montres luminescentes, et signalisation des issues de secours nécessitant une luminosité durable sans alimentation électrique. Le tritium est enveloppé de phosphore, un matériau fluorescent, de sorte que les rayons bêta émis lors de sa désintégration frappent le phosphore et produisent de la lumière. Les panneaux d'issues de secours contiennent environ 900 milliards de becquerels de tritium.  
> En raison de sa demande constante et de l'impossibilité de le stocker à long terme, le tritium est considéré comme un matériau stratégique important, avec un prix avoisinant les 30 000 dollars par gramme. Actuellement, la majorité du tritium produit et vendu commercialement provient des réacteurs à eau lourde pressurisée CANDU (CANada Deuterium Uranium), dont les unités 1 à 4 de Wolsong en Corée.
{: .prompt-tip }

#### Césium-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> Le césium-137 est un sous-produit majeur des réactions de fission dans les réacteurs nucléaires et des essais nucléaires. Il fait l'objet d'une surveillance et d'une gestion particulières en raison de sa demi-vie relativement longue (environ 30 ans), de l'émission de rayons gamma pénétrants, et de ses propriétés chimiques similaires au potassium qui facilitent son absorption par l'organisme. Pratiquement inexistant naturellement, il est aujourd'hui présent dans les sols du monde entier à une concentration moyenne d'environ 7 μg/g, résultant de l'essai nucléaire Trinity et des bombardements atomiques d'Hiroshima et Nagasaki par les États-Unis pour vaincre l'Empire japonais, ainsi que des nombreux essais nucléaires atmosphériques principalement menés dans les années 11950-11960 et de quelques accidents nucléaires majeurs (accident de Tchernobyl, accident de Goiânia au Brésil, etc.).  
> Une absorption de plus de 10000 Bq de césium-137 peut nécessiter une intervention médicale et une surveillance. Lors de l'accident de Tchernobyl, certains habitants des environs auraient absorbé plusieurs dizaines de milliers de Bq de césium-137. Après l'accident de Fukushima, les habitants des environs auraient absorbé entre 50 et 250 Bq.
> La demi-vie biologique du césium-137 sans traitement est d'environ [110 jours selon le CDC](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp), bien que cela varie selon les individus et les sources. En cas de suspicion d'exposition importante au césium-137, [l'ingestion de comprimés de bleu de Prusse médical peut accélérer son élimination et réduire sa demi-vie biologique à environ 30 jours](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp).
{: .prompt-tip }

## Capture électronique (Electron Capture) ou capture K (K-capture)

$$ p + e \to n + \nu_e $$

- Se produit lorsque le nombre de neutrons est relativement insuffisant
- Capture d'un électron de la couche la plus interne (couche K) pour convertir un proton du noyau en neutron
- Le numéro atomique diminue de 1, le nombre de masse reste inchangé
- Après la capture électronique, un vide se forme dans le nuage électronique, qui sera ensuite comblé par un électron d'une couche externe, émettant des rayons X ou des électrons Auger
- Le nucléide fils produit par capture électronique est identique à celui produit par désintégration $\beta^+$, ces deux processus sont donc en compétition.

## Désintégration alpha ($\alpha$-decay)
- Émission d'une particule alpha ($\alpha$, $^4_2\mathrm{He}$)
- Le numéro atomique diminue de 2 et le nombre de masse diminue de 4
- Fréquente chez les noyaux plus lourds que le plomb
- Contrairement à la désintégration bêta, l'énergie des particules alpha émises lors de la désintégration alpha est quantifiée.

Exemple: $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Fission spontanée (Spontaneous Fission)
- Les nucléides très lourds et instables peuvent subir une fission sans absorption préalable de neutrons
- Considérée au sens large comme une forme de désintégration radioactive
- L'uranium-238, par exemple, se désintègre par émission alpha avec une demi-vie de $10^9$ ans, mais subit également, rarement, une fission spontanée avec une demi-vie d'environ $10^16$ ans. Le tableau suivant présente les demi-vies de fission spontanée de quelques nucléides.

| Nucléide | Demi-vie de fission spontanée | Caractéristiques |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | Environ $10^{16}$ ans | Très rare |
| $^{240}\mathrm{Pu}$ | Environ $10^{11}$ ans | Nucléide fissile utilisé dans les armes nucléaires |
| $^{252}\mathrm{Cf}$ | Environ $2.6$ ans | Fission spontanée très active <br>$\rightarrow$ Utilisé comme source de neutrons pour le démarrage des réacteurs |

## Émission de proton (Proton Emission)
- Les nucléides extrêmement riches en protons et instables peuvent émettre un seul proton
- Le numéro atomique et le nombre de masse diminuent de 1
- Phénomène très rare

## Schéma de désintégration et transition isomérique
### Schéma de désintégration (Decay Scheme)
*Schéma de désintégration*: Diagramme visuel représentant toutes les voies de désintégration d'une substance radioactive

### Transition isomérique (Isomeric Transition)
- Les noyaux formés par désintégration radioactive peuvent rester dans un état excité et libérer de l'énergie sous forme de rayons gamma (bien que l'émission de rayons gamma ne change pas le nucléide, on utilise parfois par convention le terme "désintégration gamma").
- La plupart des noyaux excités émettent des rayons gamma et passent à l'état fondamental très rapidement, mais dans certains cas, l'émission de rayons gamma est retardée, créant un état quasi-stable. Ces états retardés sont appelés *états isomériques* du noyau.
- Le passage d'un état isomérique à l'état fondamental par émission de rayons gamma est appelé *transition isomérique* et est noté IT.

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Source de l'image*
> - Auteur: Utilisateur Wikimedia britannique [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Licence: Libre d'utilisation sans restriction pour tout usage, dans la mesure où cela ne contrevient pas à la loi

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> Licence: [Domaine public](https://en.wikipedia.org/wiki/Public_domain)
