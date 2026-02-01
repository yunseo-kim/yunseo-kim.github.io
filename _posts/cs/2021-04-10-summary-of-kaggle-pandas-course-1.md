---
title: "Shrnutí kurzu Kaggle „Pandas“ (1) – Lekce 1–3"
description: "Shrnutí práce s knihovnou Pandas pro čištění a úpravu dat. Souhrn veřejného kurzu Kaggle „Pandas“, místy doplněný o poznámky. Tato část pokrývá lekce 1–3."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Zde si poznamenávám, co jsem se naučil v kurzu Kaggle [Pandas](https://www.kaggle.com/learn/pandas).  
Protože je toho poměrně hodně, rozdělil jsem to na dvě části.
- 1. část: Lekce 1–3 (tento článek)
- [2. část: Lekce 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Certificate of Completion](/assets/img/kaggle-pandas/certificate.png)

## Lekce 1. Vytváření, čtení a zápis
### Načtení pandas

```python
import pandas as pd
```

V pandas existují dva klíčové objekty: **DataFrame** a **Series**.

### DataFrame
[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) lze chápat jako tabulku, případně jako [matici](/posts/vector-spaces-subspaces-and-matrices/#matice-a-prostor-matic). Je to matice složená z nezávislých *prvků (entries)*; každý prvek má určitou *hodnotu (value)* a odpovídá jednomu *řádku (row)* neboli *záznamu (record)* a jednomu *sloupci (column)*.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

Prvky DataFrame nemusí být nutně číselné; následující příklad je DataFrame se stringovými hodnotami (recenze od uživatelů).

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

Při vytváření objektu DataFrame se používá konstruktor `pd.DataFrame()` a deklaruje se pomocí syntaxe pythonového slovníku (dictionary). Do klíčů (key) se dávají názvy sloupců a do hodnot (value) seznamy (list) položek, které se mají zapsat. To je standardní způsob, jak vytvořit nový DataFrame.

Při deklaraci DataFrame se názvy sloupců nastavují jako *labely sloupců*, zatímco *labely řádků* se bez explicitního určení automaticky nastaví na celá čísla 0, 1, 2, ... V případě potřeby lze labely řádků nastavit ručně. V pandas se seznam labelů řádků nazývá [**Index**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html) a lze jej nastavit parametrem `index` konstruktoru.

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

| | Bob | Sue |
| --- | --- | --- |
| Product A | I liked it. | Pretty good. |
| Product B | It was awful. | Bland. |

### Series
[Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) je posloupnost (sequence) datových hodnot, případně [vektor](/posts/vector-spaces-subspaces-and-matrices/#radkove-a-sloupcove-vektory).

```python
pd.Series([1, 2, 3, 4, 5])
```

Series je v podstatě totéž co jeden sloupec DataFrame. Proto lze stejně jako u DataFrame nastavit [index](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html); jen místo „názvu sloupce“ má prostě „jméno“ ([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series a DataFrame spolu úzce souvisejí. Pomáhá si DataFrame představit jednoduše jako „balík“ (kolekci) objektů Series.

### Načtení datového souboru
V mnoha případech se data nepíší ručně, ale načítají se z existujícího zdroje. Data mohou být uložená v různých formátech; nejzákladnějším je CSV. Obsah CSV souboru obvykle vypadá takto:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

CSV je tedy tabulka, kde jsou hodnoty oddělené čárkami (comma). Odtud název „Comma-Separated Values“, CSV.

Pro načtení dat ve formátu CSV do DataFrame se používá funkce [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

Pomocí atributu [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) lze zkontrolovat rozměry DataFrame.

```python
product_reviews.shape
```

```
(129971, 14)
```

Výstup v ukázce znamená, že daný DataFrame má 129971 záznamů a 14 sloupců.

Pomocí metody [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) lze zobrazit prvních pět řádků DataFrame.

```python
product_reviews.head()
```

[Funkce `pd.read_csv()` má přes 30 parametrů](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Například pokud CSV soubor už obsahuje vlastní index, lze nastavit parametr `index_col`, aby pandas místo automatického indexování použil daný sloupec jako index.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Zápis datového souboru
Pomocí metody [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) lze DataFrame exportovat do CSV souboru. Použití je následující:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lekce 2. Indexování, výběr a přiřazování
Výběr konkrétních hodnot z DataFrame nebo Series je krok, kterým prochází téměř každé zpracování dat; proto je potřeba se nejdřív naučit rychle a efektivně vybírat potřebné datové body.

### Přístup přes nativní Python
Nativní pythonové objekty poskytují výborné způsoby indexování dat a pandas je nabízí ve stejné podobě.

#### Atributy objektu
V Pythonu lze k hodnotě atributu objektu přistoupit přes název atributu. Například pokud má objekt `example_obj` atribut `title`, lze jej číst jako `example_obj.title`. Stejně lze přistupovat i ke sloupcům pandas DataFrame.

```python
reviews.country
```

```
0            Italy
1         Portugal
            ...   
129969      France
129970      France
Name: country, Length: 129971, dtype: object
```

#### Indexování jako slovník
U pythonového slovníku (dictionary) lze k hodnotám přistupovat pomocí indexovacího operátoru (`[]`). Stejným způsobem lze přistupovat i ke sloupcům pandas DataFrame.

```python
reviews['country']
```

```
0            Italy
1         Portugal
            ...   
129969      France
129970      France
Name: country, Length: 129971, dtype: object
```

Přístup přes atribut i přes slovníkové indexování jsou oba validní, ale slovníkové indexování má výhodu v tom, že zvládá i názvy sloupců obsahující rezervované znaky, například mezery (např. `reviews['country providence']` je možné, ale `reviews.country providence` možné není).

I v takto vybraném pandas Series lze znovu použít indexovací operátor a načíst jednotlivou hodnotu.

```python
reviews['country'][0]
```

```
'Italy'
```

### Přístupory specifické pro pandas
Výše uvedené způsoby (indexovací operátor nebo přístup přes atribut) jsou skvělé tím, že dobře zapadají do ekosystému Pythonu. Kromě toho ale pandas poskytuje vlastní přístupory [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) a [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Výběr podle pozice (index-based selection)
Pomocí `iloc` lze provádět **výběr podle pozice (index-based selection)**. Vyberete požadované položky pomocí celočíselných pozic v datech.

Například první řádek DataFrame lze vybrat takto:

```python
reviews.iloc[0]
```

```
country                                                    Italy
description    Aromas include tropical fruit, broom, brimston...
                                     ...                        
variety                                              White Blend
winery                                                   Nicosia
Name: 0, Length: 13, dtype: object
```

Na rozdíl od nativního pythonového stylu, kde se nejdřív vybírá sloupec a pak řádek, `iloc` vybírá nejdřív řádek a potom sloupec. První sloupec DataFrame lze získat následovně:

```python
reviews.iloc[:, 0]
```

```
0            Italy
1         Portugal
            ...   
129969      France
129970      France
Name: country, Length: 129971, dtype: object
```

V ukázce výše se pomocí `:` vybraly všechny řádky a z nich pak první sloupec. Pokud chceme z prvního sloupce vybrat druhý (`1`) a třetí (`2`) řádek, uděláme to takto:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Případně lze předat seznam:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Lze použít i záporné indexy a vybírat data od konce. Následující příklad vybírá posledních 5 řádků:

```python
reviews.iloc[-5:]
```

#### Výběr podle štítků (label-based selection)
Další možností je použít `loc` pro **výběr podle štítků (label-based selection)**. V tomto případě se nevybírá podle pozice v matici dat, ale podle hodnot indexu.

Například prvek odpovídající sloupci `country` v řádku s indexem 0 lze získat takto:

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignoruje hodnoty indexu datasetu, chápe jej jako jednu velkou matici a přistupuje k prvkům podle pozice. Naproti tomu `loc` využívá indexové informace. Protože index často obsahuje smysluplné informace, bývá `loc` v mnoha případech intuitivnější než `iloc`.

#### Rozdíl ve vymezování rozsahů u `iloc` a `loc`
`iloc` používá stejné indexování jako standardní Python; proto `0:10` znamená polouzavřený interval od 0 do 10 **bez** 10, tedy `0,...,9`.

Naopak `loc` chápe rozsah jako uzavřený interval, takže `0:10` znamená 0 až 10 **včetně**, tedy `0,...,10`.

Důvodem je to, že `loc` může používat jako index nejen celá čísla, ale i libovolné standardní datové typy. Představme si DataFrame s indexy `Apples, ..., Potatoes, ...` a chceme vybrat plodiny v abecedním pořadí od `Apples` po `Potatoes`. V tomto případě je mnohem intuitivnější napsat „od `Apples` do `Potatoes`“ (`df.loc['Apples':'Potatoes']`), než nastavovat „od `Apples` do těsně před `Potatoet`“ (`df.loc['Apples':'Potatoet']`), protože po `Potatoes` by mohla následovat kombinace znaků typu `Potatoet`. Právě proto `loc` používá uzavřený interval.

Jinak je zbytek chování v zásadě stejný.

> Osobně v datasetech se vzestupně seřazeným celočíselným indexem preferuji při výběru rozsahu přes `:` spíš `iloc`, abych se vyhnul záměně dané rozdílným chováním vymezování rozsahů. V ostatních případech mám raději intuitivnější `loc`.
{: .prompt-tip }

### Úprava indexu
Index lze podle potřeby i upravovat. Pomocí metody [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) lze v datasetu nastavit určitý sloupec jako nový index, jako v následující ukázce:

```python
reviews.set_index("title")
```

### Podmíněný výběr
Doposud šlo o postupy, jak data vybírat a upravovat pomocí strukturálních vlastností DataFrame. Lze ale vybírat i data splňující složitější podmínky.

Například si představme DataFrame s informacemi o vínech a potřebujeme vybrat pouze italská vína s hodnocením alespoň 90 bodů.

```python
reviews.country == 'Italy'
```

Tato podmínka vrací Series složený z booleovských hodnot `True`/`False`.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` je primárně label-based, ale umí přijmout i booleovské pole nebo zarovnatelný booleovský Series](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). Proto lze vybrat jen italská vína takto:

```python
reviews.loc[reviews.country == 'Italy']
```

Více podmínek lze kombinovat operátory `&` nebo `|`. Pro výběr vín, která jsou **italská** a zároveň mají hodnocení alespoň 90 bodů, použijeme:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Vína, která jsou **italská** nebo mají hodnocení alespoň 90 bodů, lze vybrat takto:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas také nabízí několik vestavěných „podmíněných selektorů“, z nichž zvlášť užitečné jsou `isin` a `isnull`/`notnull`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) vrací booleovskou masku (`True` nebo `False`) podle toho, zda hodnota patří mezi položky v seznamu („is in“). Díky tomu lze data vyfiltrovat. Například vybrat vína z Itálie nebo Francie:

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) se používá při výběru řádků s chybějící hodnotou (`NaN`) nebo bez ní. Například vybrat jen vína, u kterých nechybí cena:

```python
reviews.loc[reviews.price.notna()]
```

> Mimochodem, v původním kurzu Kaggle to uvedené nebylo, ale [`iloc` umí přijmout i booleovské pole (array)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Na rozdíl od `loc` však podporuje pouze pole, nikoli Series, takže podobné použití jako výše je obtížnější.
{: .prompt-tip }

### Přiřazování dat
Do DataFrame lze také nově přiřazovat data nebo existující hodnoty přepisovat.

```python
reviews['critic'] = 'everyone'
reviews['critic']
```

```
0         everyone
1         everyone
            ...   
129969    everyone
129970    everyone
Name: critic, Length: 129971, dtype: object
```

```python
reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']
```

```
0         129971
1         129970
           ...  
129969         2
129970         1
Name: index_backwards, Length: 129971, dtype: int64
```

## Lekce 3. Souhrnné funkce a mapování
### Rychlý přehled dat
Metoda [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) poskytuje „high-level“ přehled daného sloupce.

```python
reviews.points.describe()
```

```
count    129971.000000
mean         88.447138
             ...      
75%          91.000000
max         100.000000
Name: points, Length: 8, dtype: float64
```

Výstup `describe()` závisí na datovém typu vstupu. Pro řetězcová data (ne číselná) vrací například toto:

```python
reviews.taster_name.describe()
```

```
count         103727
unique            19
top       Roger Voss
freq           25514
Name: taster_name, dtype: object
```

Případně lze získat jen konkrétní statistiku.

```python
reviews.points.mean()
```

```
88.44713820775404
```

```python
reviews.taster_name.unique()
```

```
array(['Kerin O’Keefe', 'Roger Voss', 'Paul Gregutt',
       'Alexander Peartree', 'Michael Schachner', 'Anna Lee C. Iijima',
       'Virginie Boone', 'Matt Kettmann', nan, 'Sean P. Sullivan',
       'Jim Gordon', 'Joe Czerwinski', 'Anne Krebiehl\xa0MW',
       'Lauren Buzzeo', 'Mike DeSimone', 'Jeff Jenssen',
       'Susan Kostrzewa', 'Carrie Dykes', 'Fiona Adams',
       'Christina Pickard'], dtype=object)
```

Pokud chcete vědět, kolikrát se v DataFrame vyskytuje každá unikátní hodnota, použijte metodu [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

```python
reviews.taster_name.value_counts()
```

```
Roger Voss           25514
Michael Schachner    15134
                     ...  
Fiona Adams             27
Christina Pickard        6
Name: taster_name, Length: 19, dtype: int64
```

### Zobrazení (Maps)
**Zobrazení (map)** je termín převzatý z matematiky a znamená funkci, která přiřazuje prvky jedné množiny prvkům jiné množiny. V data science je často potřeba převádět data do jiné reprezentace; k tomu se používají zobrazení, a proto jsou velmi důležitá.

Často se používají zejména dvě metody.

Metoda [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) přijme funkci, která převádí jednu <u>hodnotu</u> na jinou jedinou hodnotu. Tuto funkci pak hromadně aplikuje na všechny hodnoty v dané <u>Series</u> a vrátí novou Series. Například když chcete od bodového hodnocení vína odečíst průměr a získat odchylku, můžete to udělat takto:

```python
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
```

```
0        -1.447138
1        -1.447138
            ...   
129969    1.552862
129970    1.552862
Name: points, Length: 129971, dtype: float64
```

Metoda [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) se používá, když chcete volat vlastní funkci pro každý <u>řádek</u> a aplikovat transformaci na celý <u>DataFrame</u>.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Pokud `apply()` zavoláte s parametrem `axis='index'`, můžete funkci aplikovat ne po řádcích, ale po sloupcích.

`Series.map()` i `DataFrame.apply()` vracejí nový, transformovaný Series/DataFrame a původní data nijak nemění.

| Metoda | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Objekt | Series | DataFrame |
| Jednotka aplikace | aplikuje se na jednotlivé hodnoty <br>(pokud Series chápeme jako [sloupcový vektor](/posts/vector-spaces-subspaces-and-matrices/#radkove-a-sloupcove-vektory), jde o aplikaci po řádcích) | ve výchozím stavu se aplikuje po řádcích <br> volitelně lze aplikovat po sloupcích |

> Mimochodem existují i [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) a [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html).
> - `Series.apply()`:
>   - `by_row='compat'` (výchozí): chová se stejně jako `Series.map()`
>   - `by_row=False`: předá do funkce celou Series najednou (podobné chování jako `DataFrame.apply()` s `axis='index'`)
> - `DataFrame.map()`: aplikuje funkci na jednotlivé hodnoty v DataFrame (je podobné `Series.map()`, jen cílem je DataFrame místo Series)
{: .prompt-tip }

Ve skutečnosti pandas podporuje řadu běžně používaných zobrazení přímo. Předchozí příklad lze napsat mnohem jednodušeji a pandas i tak pochopí záměr a bude fungovat správně:

```python
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean
```

```
0        -1.447138
1        -1.447138
            ...   
129969    1.552862
129970    1.552862
Name: points, Length: 129971, dtype: float64
```

Navíc pandas podporuje i operace mezi Series stejné délky. V příkladu s vínem lze například spojit informaci o zemi a regionu do jednoho řetězce:

```python
reviews.country + " - " + reviews.region_1
```

```
0            Italy - Etna
1                     NaN
               ...       
129969    France - Alsace
129970    France - Alsace
Length: 129971, dtype: object
```

Tyto operace jsou rychlejší než `map()` nebo `apply()`, protože využívají interní techniky akcelerace v pandas. Pandas umí tímto způsobem pracovat se všemi standardními pythonovými operátory (`>`, `<`, `==` atd.). I tak je ale dobré znát `map()` a `apply()`, protože jsou flexibilnější a umožňují složitější transformace.
