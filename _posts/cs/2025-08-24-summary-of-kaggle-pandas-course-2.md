---
title: "Shrnutí kurzu Kaggle „Pandas“ (2) – Lekce 4–6"
description: "Shrnutí práce s knihovnou Pandas pro čištění a úpravu dat. Souhrn veřejného kurzu Kaggle „Pandas“, místy doplněný. Tato část pokrývá lekce 4–6."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Zde si poznamenávám, co jsem se naučil v kurzu Kaggle [Pandas](https://www.kaggle.com/learn/pandas).  
Protože je toho poměrně hodně, rozdělil jsem to na dvě části.
- [1. část: Lekce 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- 2. část: Lekce 4–6 (tento článek)

![Certifikát o absolvování](/assets/img/kaggle-pandas/certificate.png)

## Lekce 4. Seskupování a řazení
Často je potřeba data rozdělit do skupin a provést nad nimi nějaké operace po skupinách, případně je seřadit podle určitého kritéria.

### Analýza po skupinách
Pomocí metody [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) lze seskupit řádky s totožnou hodnotou v daném sloupci a následně nad každou skupinou provést přehled nebo transformaci.

Už jsme si ukázali [metodu `value_counts()`](/posts/summary-of-kaggle-pandas-course-1/#rychly-prehled-dat); stejnou funkcionalitu lze pomocí `groupby()` realizovat například takto:

```python
reviews.groupby('taster_name').size()
```

1. DataFrame `reviews` se seskupí podle toho, které řádky mají stejnou hodnotu ve sloupci `taster_name`.
2. Vrátí se Series s velikostmi jednotlivých skupin (počet řádků ve skupině).

Nebo:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. DataFrame `reviews` se seskupí podle hodnot ve sloupci `taster_name`.
2. V každé skupině se vybere sloupec `taster_name`.
3. Vrátí se Series s počtem hodnot v daném sloupci, přičemž se nepočítají chybějící hodnoty (NaN).

Jinými slovy, `value_counts()` je ve skutečnosti jen zkratka pro chování typu výše. A stejně tak lze použít i jiné souhrnné funkce než jen [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html). Například pokud chcete z dat o vínech zjistit minimální cenu pro každé bodové hodnocení, můžete udělat:

```python
reviews.groupby('points').price.min()
```

```
points
80      5.0
81      5.0
       ... 
99     44.0
100    80.0
Name: price, Length: 21, dtype: float64
```

1. DataFrame `reviews` se seskupí podle hodnot ve sloupci `points`.
2. V každé skupině se vybere sloupec `price`.
3. Vrátí se Series s minimální hodnotou v dané skupině.

Je možné seskupovat i podle více sloupců. Pokud chcete vybrat pouze informace o víně s nejvyšším hodnocením pro každou kombinaci země a provincie, můžete použít:

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Další užitečnou metodou objektu DataFrameGroupBy je [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html). Ta umožňuje po seskupení spustit nad každou skupinou více funkcí najednou.

> Jako argument lze předat:
> - funkci,
> - řetězec se jménem funkce,
> - seznam funkcí nebo řetězců se jmény funkcí,
> - slovník, kde klíčem je popisek osy a hodnotou je funkce nebo seznam funkcí aplikovaných na danou osu.
>
> Funkce zde musí být taková, která buď:
> - umí přijmout DataFrame jako vstup, nebo
> - ji lze předat jako argument metody [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html), o které byla řeč [dříve](/posts/summary-of-kaggle-pandas-course-1/#zobrazeni-maps).
>
> Toto vysvětlení v původním kurzu Kaggle nebylo; je doplněné na základě oficiální dokumentace pandas.
{: .prompt-tip }

Například takto lze spočítat statistiky cen podle země:

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> Zde `len` znamená vestavěnou pythonovou funkci [`len()`](https://docs.python.org/3/library/functions.html#len); v tomto příkladu ji používáme k tomu, abychom vypsali počet cen (`price`) v každé skupině (`country`) <u>včetně chybějících hodnot</u>. Protože jde o funkci, která umí pracovat s DataFrame/Series jako vstupem, lze ji použít tímto způsobem.
>
> Naproti tomu metoda [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) v pandas vrací <u>pouze počet platných (nechybějících) hodnot</u>, takže se chová jinak.
>
> Toto vysvětlení v původním kurzu Kaggle nebylo; je doplněné na základě oficiální dokumentace Pythonu a pandas.
{: .prompt-tip }

### Víceúrovňový index

Při zpracování a analýze dat pomocí `groupby()` se občas stane, že jako výsledek dostanete DataFrame s indexem, který není tvořen jedním labelem, ale více úrovněmi (MultiIndex).

```python
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
```

<table>
  <tr>
    <th></th>
    <th></th>
    <th>len</th>
  </tr>
  <tr>
    <th>Country</th>
    <th>province</th>
    <th></th>
  </tr>
  <tr>
    <td rowspan="2">Argentina</td>
    <td>Mendoza Province</td>
    <td>3264</td>
  </tr>
  <tr>
    <td>Other</td>
    <td>536</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td rowspan="2">Uruguay</td>
    <td>San Jose</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Uruguay</td>
    <td>24</td>
  </tr>
</table>

```python
mi = countries_reviewed.index
type(mi)
```

```
pandas.core.indexes.multi.MultiIndex
```

MultiIndex má několik metod, které běžný (jednoúrovňový) index nemá, a které se hodí pro práci s hierarchickými strukturami. Podrobnější příklady a doporučení najdete v sekci [MultiIndex / advanced indexing v pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

V praxi ale nejčastěji využijete metodu [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html), která MultiIndex převede zpět na „normální“ index:

```python
countries_reviewed.reset_index()
```

| | country | province | len |
| --- | --- | --- | --- |
| 0 | Argentina | Mendoza Province | 3264 |
| 1 | Argentina | Other | 536 |
| ... | ... | ... | ... |
| 423 | Uruguay | San Jose | 3 |
| 424 | Uruguay | Uruguay | 24 |

### Řazení

Když se podíváte na `countries_reviewed`, můžete si všimnout, že výsledek seskupení se vrací v pořadí daném indexem. Jinými slovy: pořadí řádků výsledku `groupby` je určeno hodnotami indexu, ne samotným obsahem dat.

Podle potřeby si data můžete seřadit jinak. K tomu se hodí metoda [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). Například takto lze seřadit země a provincie vzestupně podle počtu záznamů (`len`):

```python
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')
```

| | country | province | len |
| --- | --- | --- | --- |
| 179 | Greece | Muscat of Kefallonian | 1 |
| 192 | Greece | Sterea Ellada | 1 |
| ... | ... | ... | ... |
| 415 | US | Washington | 8639 |
| 392 | US | California | 36247 |

`sort_values()` standardně řadí vzestupně (od menších hodnot k větším). Pokud ale nastavíte volbu, můžete řadit i sestupně:

```python
countries_reviewed.sort_values(by='len', ascending=False)
```

| | country | province | len |
| --- | --- | --- | --- |
| 392 | US | California | 36247 |
| 415 | US | Washington | 8639 |
| ... | ... | ... | ... |
| 63 | Chile | Coelemu | 1 |
| 149 | Greece | Beotia | 1 |

Pokud chcete řadit podle indexu, použijte metodu [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html). Má stejné argumenty i stejné výchozí chování jako `sort_values()`, takže způsob použití je stejný.

```python
countries_reviewed.sort_index()
```

| | country | province | len |
| --- | --- | --- | --- |
| 0 | Argentina | Mendoza Province | 3264 |
| 1 | Argentina | Other | 536 |
| ... | ... | ... | ... |
| 423 | Uruguay | San Jose | 3 |
| 424 | Uruguay | Uruguay | 24 |

Nakonec je možné řadit i podle více sloupců současně, například:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lekce 5. Datové typy a chybějící hodnoty

V praxi není zaručeno, že data budou vždy dobře vyčištěná. Často bývá potřeba převést datové typy na požadované, nebo řešit chybějící hodnoty, které se v datech objevují tu a tam. Při zpracování a analýze dat je tohle ve většině případů nejtěžší etapa.

### Datové typy

Datový typ konkrétního sloupce DataFrame nebo Series se označuje jako **dtype**. Pomocí atributu `dtype` lze zjistit datový typ daného sloupce. Následuje příklad pro sloupec `price` v DataFrame `reviews`:

```python
reviews.price.dtype
```

```
dtype('float64')
```

Případně lze přes atribut `dtypes` zjistit `dtype` všech sloupců najednou:

```python
reviews.dtypes
```

```
country        object
description    object
                ...  
variety        object
winery         object
Length: 13, dtype: object
```

Datový typ vyjadřuje, jak pandas daná data interně ukládá. Například `float64` znamená 64bitové číslo s plovoucí desetinnou čárkou, `int64` pak 64bitové celé číslo.

Zajímavostí je, že sloupec tvořený čistě řetězci nemá vlastní „string“ dtype (v tomto kontextu), ale je považován za objekt (`object`).

Pomocí [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) lze sloupec převést z jednoho datového typu na jiný. Například v předchozích ukázkách lze sloupec `points`, který byl typu `int64`, převést na `float64`:

```python
reviews.points.astype('float64')
```

```
0         87.0
1         87.0
          ... 
129969    90.0
129970    90.0
Name: points, Length: 129971, dtype: float64
```

Datový typ má i index DataFrame/Series:

```python
reviews.index.dtype
```

```
dtype('int64')
```

Kromě toho pandas podporuje i další typy, například kategoriální data nebo časové řady.

### Chybějící hodnoty

Prázdné položky (entries), které nemají hodnotu, dostávají hodnotu `NaN` (zkratka „Not a Number“). Z technických důvodů má `NaN` vždy typ `float64`.

Pandas poskytuje několik funkcí specializovaných na chybějící hodnoty. [Už jsme něco podobného krátce viděli dříve](/posts/summary-of-kaggle-pandas-course-1/#podmineny-vyber): kromě metod existují i samostatné funkce [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) a [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). Vrací buď jednu booleovskou hodnotu, nebo booleovské pole podle toho, zda je daná položka chybějící (resp. nechybějící). Lze je použít například takto:

```python
reviews[pd.isna(reviews.country)]
```

Obvykle chcete zjistit, zda data chybějící hodnoty obsahují, a pokud ano, nějak je vhodně doplnit. Existuje více strategií. Metoda [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) umožňuje chybějící hodnoty nahradit nějakou „rozumnou“ konstantou. Například takto lze ve sloupci `region_2` v DataFrame `reviews` nahradit všechna `NaN` hodnotou `"Unknown"`:

```python
reviews.region_2.fillna("Unknown")
```

Případně lze doplňovat chybějící hodnoty nejbližší platnou hodnotou před/za (forward fill / backward fill). To lze realizovat metodami [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) a [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html).

> Dříve šlo použít i `fillna()` s argumentem `method='ffill'` nebo `method='bfill'`, ale od pandas 2.1.0 je tento způsob deprecated a nedoporučuje se. Místo toho je potřeba použít `ffill()` nebo `bfill()` podle situace.
{: .prompt-danger }

A někdy je potřeba hromadně nahradit jednu hodnotu jinou i v případech, kdy nejde o `NaN`. Původní kurz Kaggle uvádí příklad se změnou twitterového handle konkrétního recenzenta; i to je dobrý příklad, ale zkusme si představit jiný, „bližší“ příklad.

Představme si hypotetickou situaci, kdy by se v Jižní Koreji oddělila severní část provincie Gyeonggi a vznikla nová správní jednotka **Gyeonggibuk-do**, a máte dataset, kde už je tento název zohledněn. Pak ale někdo přijde s absurdním nápadem přejmenovat **Gyeonggibuk-do** na **Pyeonghwanuri Special Self-Governing Province** (nebo třeba **Pyeonghwanuri State**) a nakonec to skutečně prosadí. ~~Je to hypotetické, ale děsivá část je, že něco podobného se ve skutečnosti klidně mohlo stát.~~ Pak bude potřeba v existujícím datasetu nahradit `"Gyeonggibuk-do"` nějakou z těchto nových hodnot. Jedním ze způsobů, jak takovou práci udělat v pandas, je metoda [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html).

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

Pomocí výše uvedeného kódu lze ve sloupci `province` datasetu `rok_2030_census` efektivně nahradit všechny výskyty řetězce `"Gyeonggibuk-do"` „tím dlouhým“. ~~Znovu si jen oddechnu, že se v reálném světě nestalo nic, kvůli čemu by tohle někdo musel opravdu pouštět.~~

Takové nahrazování řetězců se hodí i při čištění dat a práci s chybějícími hodnotami, protože chybějící hodnota nemusí být vždy `NaN`, ale často bývá reprezentována řetězci typu `"Unknown"`, `"Undisclosed"`, `"Invalid"` apod. V reálných projektech, například při vytváření datasetů z OCR skenů starších úředních dokumentů, to může být dokonce častější případ.

## Lekce 6. Přejmenování a slučování

Někdy je potřeba přejmenovat určité sloupce nebo indexy v datasetu. Také je časté, že potřebujete spojovat více DataFrame nebo Series.

### Přejmenování

Metoda [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) umožňuje přejmenovat sloupce nebo indexy v datasetu. `rename()` podporuje více vstupních formátů, ale nejpohodlnější bývá použít pythonový slovník (dictionary). Následují příklady, kdy v DataFrame `reviews` přejmenujeme sloupec `points` na `score` a indexy `0`, `1` na `firstEntry`, `secondEntry`.

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

Ve skutečnosti se názvy sloupců přejmenovávají poměrně často, ale přejmenování samotných hodnot indexu bývá vzácné. A pro podobné účely je obvykle praktičtější používat, [jak jsme viděli dříve](/posts/summary-of-kaggle-pandas-course-1/#uprava-indexu), metodu [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html).

Index řádků i index sloupců mají navíc i vlastní atribut `name` a pomocí metody `rename_axis()` lze přejmenovat i tyto názvy os. Například indexovou osu datasetu lze pojmenovat `wines` a sloupcovou osu `fields`:

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Kombinování datasetů

Někdy je potřeba kombinovat DataFrame s DataFrame, nebo Series se Series. Pandas pro to poskytuje tři klíčové funkce; od nejjednodušší po nejsložitější jsou to [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) a [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). Kurz Kaggle uvádí, že většinu toho, co lze udělat pomocí `merge()`, lze jednodušeji vyřešit přes `join()`, takže se zaměřuje jen na první dvě.

Funkce `concat()` je nejjednodušší: vezme několik DataFrame nebo Series a „přilepí“ je za sebe podél zvolené osy. Je užitečná, pokud mají spojované objekty stejné pole (sloupce). Ve výchozím stavu se spojuje podél indexové osy; pokud nastavíte `axis=1` nebo `axis='columns'`, bude se spojovat podél osy sloupců.

```python
>>> s1 = pd.Series(['a', 'b'])
>>> s2 = pd.Series(['c', 'd'])
>>> pd.concat([s1, s2])
0    a
1    b
0    c
1    d
dtype: object
```

```python
>>> df1 = pd.DataFrame([['a', 1], ['b', 2]],
...                    columns=['letter', 'number'])
>>> df1
  letter  number
0      a       1
1      b       2
>>> df2 = pd.DataFrame([['c', 3], ['d', 4]],
...                    columns=['letter', 'number'])
>>> df2
  letter  number
0      c       3
1      d       4
>>> pd.concat([df1, df2])
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
>>> df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
...                    columns=['animal', 'name'])
>>> df4
   animal    name
0    bird   polly
1  monkey  george
>>> pd.concat([df1, df4], axis=1)
  letter  number  animal    name
0      a       1    bird   polly
1      b       2  monkey  george
```

> Podle [oficiální dokumentace pandas]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html)) se v případech, kdy potřebujete poskládat více řádků do jednoho DataFrame, nedoporučuje přidávat řádky po jednom uvnitř smyčky. Místo toho je lepší připravit seznam řádků a spojit je najednou jedním `concat()`.
{: .prompt-tip }

Metoda `join()` je o něco složitější: připojí k jednomu DataFrame další DataFrame podle indexu. Pokud se v obou DataFrame vyskytují sloupce se stejným názvem, je nutné přes argumenty `lsuffix` a `rsuffix` určit přípony, které se přidají ke kolidujícím názvům sloupců kvůli odlišení.

```python
>>> df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
...                    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
>>> df
  key   A
0  K0  A0
1  K1  A1
2  K2  A2
3  K3  A3
4  K4  A4
5  K5  A5
>>> other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
...                       'B': ['B0', 'B1', 'B2']})
>>> other
  key   B
0  K0  B0
1  K1  B1
2  K2  B2
>>> df.join(other, lsuffix='_caller', rsuffix='_other')
  key_caller   A key_other    B
0         K0  A0        K0   B0
1         K1  A1        K1   B1
2         K2  A2        K2   B2
3         K3  A3       NaN  NaN
4         K4  A4       NaN  NaN
5         K5  A5       NaN  NaN
```
