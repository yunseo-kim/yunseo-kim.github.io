---
title: Principy pro psaní dobrého kódu
description: "Proč je nutné psát dobrý kód a jaké jsou hlavní obecné principy pro čitelný a dobře udržovatelný software."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## Proč je nutné psát dobrý kód
Pokud se soustředíte jen na rychlé napsání kódu kvůli okamžité implementaci, může [technický dluh](/posts/Technical-debt/) narůst do neúnosné míry a později způsobit problémy s údržbou. Proto je při vývoji projektu bez debat důležité psát od začátku čitelný a snadno udržovatelný dobrý kód.

U algoritmického řešení problémů (PS, Problem Solving) nebo programátorských soutěží (CP, Competitive Programming) se obvykle kód použitý k řešení po skončení úlohy či soutěže už znovu nepoužije a zejména u CP kvůli časovým limitům může zaznít názor, že rychlá implementace je důležitější než psaní dobrého kódu. Aby bylo možné na tuto otázku odpovědět, je potřeba si promyslet, proč PS/CP děláte a jaký směr sledujete.

Osobně si myslím, že pokud pomineme obecné rozvíjení schopnosti řešit problémy a omezíme se čistě na programátorskou stránku, lze se prostřednictvím PS/CP naučit následující:
- Při řešení úloh v rámci daných omezení (čas běhu, paměť apod.) si lze vyzkoušet a osvojit různé algoritmy a datové struktury; díky tomu získáte cit, jaký algoritmus či datovou strukturu použít v konkrétní situaci i v reálném projektu.
- Po odeslání kódu získáte okamžitou objektivní zpětnou vazbu (správně/špatně, čas běhu, spotřeba paměti), takže můžete trénovat rychlé a zručné psaní přesného kódu bez opomenutí detailů.
- Můžete se dívat na kód napsaný zkušenějšími lidmi, porovnávat ho se svým a hledat, co zlepšit.
- Protože opakovaně píšete relativně malé programy se podobnou funkcionalitou (zejména když PS trénujete sami), můžete bez tlaku termínů více dbát na detaily a trénovat psaní stručného a kvalitního kódu.

PS/CP lze samozřejmě dělat i čistě jako koníček, ale pokud PS/CP děláte pro zlepšení programátorských schopností, pak poslední bod – „trénink psaní dobrého kódu“ – je stejně velká výhoda jako předchozí tři. Psaní dobrého kódu totiž nepřijde samo od sebe; je potřeba se v něm postupně zlepšovat pravidelným opakováním. Navíc složitý a špatně čitelný kód se hůře debuguje a i pro autora bývá paradoxně těžší napsat ho napoprvé správně, takže ztráta času neefektivním laděním často vede k tomu, že implementace nakonec ani není tak rychlá. PS/CP se samozřejmě od praxe dost liší, ale úplně ignorovat psaní dobrého kódu a honit jen okamžitou implementaci je z výše uvedených důvodů (záměna prostředků za cíl) podle mě kontraproduktivní. Osobně si proto myslím, že i v PS/CP je dobré psát stručný a efektivní kód.

> Doplněný komentář 12024.12:  
> Podle současného vývoje má dál smysl budovat si znalosti algoritmů a datových struktur a rozvíjet schopnost řešit problémy, ale ve fázi převodu řešení do skutečně běžícího kódu už asi není nutné trvat na tom, že člověk musí vše psát ručně. Spíš se vyplatí aktivně využívat AI (GitHub Copilot, Cursor, Windsurf apod.), ušetřit čas a ten věnovat jiné práci nebo studiu. Pokud děláte PS/CP kvůli obecné schopnosti řešit problémy nebo kvůli studiu algoritmů/datových struktur, případně čistě jako hobby, není důvod to zakazovat. Ale věnovat PS/CP čas a energii pouze kvůli tréninku psaní kódu už dnes podle mě vychází výrazně hůř z hlediska poměru nákladů a přínosů. Dokonce i u vývojářských pozic očekávám, že význam coding testů jako součásti náboru pravděpodobně oproti minulosti výrazně klesne.
{: .prompt-warning }

## Principy pro psaní dobrého kódu
Ať už jde o kód psaný na soutěži nebo v praxi, podmínky, aby se dal označit za „dobrý“, se zásadně neliší. V tomto článku se věnuji hlavním principům pro psaní dobrého kódu obecně. V PS/CP se však může kvůli rychlé implementaci dělat více kompromisů než v praxi; takové případy zde zmíním zvlášť.

### Psaní stručného kódu
> "KISS(Keep It Simple, Stupid)"

- Čím je kód kratší a stručnější, tím menší je riziko překlepů nebo triviálních bugů a tím snazší je debugging.
- Pište kód tak, aby byl snadno pochopitelný i bez zvláštních komentářů; komentáře přidávejte jen když jsou opravdu potřeba, a pak doplňte podrobnější vysvětlení. Je vhodnější držet stručnou samotnou strukturu kódu než se spoléhat na komentáře.
- Pokud komentáře píšete, pište je jasně a stručně.
- Počet argumentů předávaných do jedné funkce držte na 3 nebo méně; pokud potřebujete předat argumentů více, zabalte je do jednoho objektu.
- Pokud se hloubka (depth) podmínkových výrazů zdvojuje či ztrojuje, zhoršuje to čitelnost; proto je vhodné se zvyšování hloubky podmínek pokud možno vyhnout.  
  např.) Níže uvedený kód využívající idiom guard clause je z hlediska čitelnosti výhodnější než kód výše.

  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if user:
          token = await user_service.get_token(user)
  
          if token :
              if token.purpose == 'reset':
                  return True
      return False
  ```
  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if not user:
          return False
    
      token = await user_service.get_token(user)
  
      if not token or token.purpose != 'reset':
          return False
    
    return True
  ```
- V PS/CP se někdy kvůli zkrácení kódu a rychlému psaní používají triky jako C/C++ makra. V časově napjaté soutěži to může být občas užitečné, ale je to metoda, která funguje hlavně v PS/CP; obecně je vhodné se používání maker v C++ vyhýbat.  
  např.)

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularizace kódu
> "DRY(Don't Repeat Yourself)"

- Pokud se stejný kód opakuje, oddělte danou část do funkce nebo třídy a znovu ji používejte.
- Aktivní znovupoužívání kódu pomocí modularizace zlepšuje čitelnost a usnadňuje údržbu, protože při změně stačí upravit danou funkci či třídu jen jednou.
- V principu je ideální, aby jedna funkce nedělala dvě a více věcí, ale vykonávala jen jednu konkrétní funkci. Kód v PS/CP však bývá malý a často má jednoduchou funkcionalitu, takže možnosti znovupoužití jsou omezené; navíc kvůli časovému limitu může být obtížné držet se těchto zásad tak přísně jako v praxi.

### Využívání standardní knihovny
> "Don't reinvent the wheel"

- Ve fázi studia algoritmů a datových struktur je užitečné implementovat si struktury jako fronta či zásobník nebo třídicí algoritmy ručně a pochopit princip; jinak je ale dobré standardní knihovnu aktivně využívat.
- Standardní knihovny jsou používány a ověřeny nesčetněkrát a bývají dobře optimalizované, takže jsou efektivnější než vlastní reimplementace.
- Když použijete existující knihovnu, nemusíte zbytečně plýtvat časem implementací téže funkcionality a při spolupráci je pro ostatní členy týmu snazší kódu porozumět.

### Používejte konzistentní a jednoznačné názvosloví
> "Follow standard conventions"

- Používejte nejednoznačné názvy proměnných a funkcí.
- Každý jazyk má obvykle vlastní pojmenovací konvence (naming convention); osvojte si konvence používané ve standardní knihovně daného jazyka a aplikujte je konzistentně při deklaraci tříd, funkcí, proměnných apod.
- Pojmenovávejte tak, aby bylo jasné, co která proměnná/funkce/třída dělá, a v případě booleovského typu aby bylo z názvu zřejmé, za jaké podmínky vrací True.

### Všechna data ukládejte v normalizované podobě
- Všechna data zpracovávejte v jednom konzistentním, normalizovaném formátu.
- Pokud stejná data existují ve dvou a více formátech, mohou vznikat jemné a těžko odhalitelné bugy (např. mírně odlišná řetězcová reprezentace nebo odlišné hash hodnoty).
- Při ukládání a zpracování dat jako časová pásma nebo řetězce je nutné je hned po načtení nebo výpočtu převést na jeden standardní formát (např. UTC, kódování UTF-8). Je vhodné provést normalizaci už v konstruktoru třídy, která data reprezentuje, nebo ji provést okamžitě ve funkci, která data přijímá.

### Oddělte logiku kódu od dat
- Data, která nesouvisí přímo s logikou kódu, nevkládejte přímo do podmínek, ale oddělte je do samostatné tabulky.  
  např.) Je vhodnější psát to jako v kódu níže než jako v kódu výše.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ~~~c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ~~~
