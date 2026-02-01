---
title: "Technický dluh (Technical debt)"
description: "Podívejme se na pojem technického dluhu, proč vzniká a jak ho minimalizovat."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Technický dluh

> **Technický dluh (Technical debt)**  
> cena, kterou bude nutné zaplatit později za to, že si během vývoje zvolíme zkratku umožňující rychleji dokončit aktuální projekt, abychom splnili okamžité požadavky
{: .prompt-info }

Stejně jako když si v účetním smyslu vezmete dluh (debt) a půjčíte si peníze, můžete díky tomu rychle investovat tam, kde je to hned potřeba, ale zároveň se dostanete pod finanční tlak a musíte splatit jistinu i s úroky; podobně i když kvůli aktuálním požadavkům postupujete rychleji ve vývoji, byť trochu „nečistě“, kód se postupně komplikuje a duplikuje, a později vznikají potíže při implementaci nových funkcí nebo při rozšiřování.

Stejně jako firma může díky dluhu včas realizovat větší investice, vyvinout nový produkt a zvýšit podíl na trhu, nebo jednotlivec může díky úvěru uzavřít koupi domu, není ani přijetí technického dluhu a rychlá implementace nové funkce nutně vždy špatná. Je však žádoucí omezovat jeho hromadění a řídit jej na únosné úrovni.

## Proč technický dluh vzniká

I když má vývojář dostatečné schopnosti, technický dluh během vývoje nevyhnutelně vzniká a nelze mu v principu zcela zabránit.  
Jak se služba vyvíjí a narazí se na limity původně navrženého kódu, může být potřeba upravit existující návrh, i kdyby byl původně čitelný a dobře fungoval.  
Také s tím, jak se vyvíjejí samotné technologie, může nastat situace, kdy se přestane používat dříve dominantní knihovna/framework, a tým se rozhodne změnit technologický stack na jinou knihovnu/framework; i v takovém případě se dříve napsaný kód stává určitým druhem technického dluhu.

Kromě toho může technický dluh vznikat i z následujících důvodů:
- během projektu se navržené věci včas nedokumentují, takže jiný člověk (nebo vy sami po čase) má potíže daný kód znovu pochopit
- neodstraňují se proměnné nebo položky v DB, které se už nepoužívají
- rutinní práce (nasazení/build apod.) se neautomatizují, takže to pokaždé stojí další čas a úsilí
- urgentní změny specifikace

## Jak technický dluh minimalizovat

### Nastavení pravidel (Convention) mezi vývojáři

- pokud nejde o vývoj o samotě, je pro hladkou spolupráci potřeba shoda na používaném jazyce či technologickém stacku, adresářové struktuře projektu, stylu vývoje apod.
- je nutné rozhodnout, do jaké míry se bude postup sjednocovat a od jakého bodu se ponechá individuální volnost
- je potřeba si v rámci code review ověřovat styl vývoje navzájem a sdílet názory

### Psaní čistého kódu (Clean Code) a refaktoring (Refactoring)

- pokud je stávající kód nepořádný a brání vývoji, lze technický dluh „splácet“ refaktoringem, tedy zpřehledněním struktury kódu
- samozřejmě platí, že čím více je stávající kód „špagetový“ a nepořádný, tím je refaktoring obtížnější; v extrémních případech se refaktoring úplně vzdá, starý kód se zahodí a vyvine se znovu od začátku
- pokud možno je vhodné snažit se psát už od začátku kód, který je čitelný a snadno udržovatelný
