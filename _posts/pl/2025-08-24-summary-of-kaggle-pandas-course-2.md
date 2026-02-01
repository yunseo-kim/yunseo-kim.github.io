---
title: "Podsumowanie kursu Kaggle „Pandas” (2) — lekcje 4–6"
description: "Podsumowanie wykorzystania biblioteki Pandas do czyszczenia i przetwarzania danych. Streszczenie kursu Kaggle „Pandas” z uzupełnieniami; część 2 obejmuje lekcje 4–6."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Poniżej porządkuję notatki z nauki na kursie Kaggle [Pandas](https://www.kaggle.com/learn/pandas).  
Ponieważ materiału jest całkiem sporo, podzieliłem go na 2 części.
- [Część 1: lekcje 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- Część 2: lekcje 4–6 (ten wpis)

![Certyfikat ukończenia](/assets/img/kaggle-pandas/certificate.png)

## Lekcja 4. Grupowanie i sortowanie
Czasem trzeba sklasyfikować dane i wykonać pewne operacje osobno dla każdej grupy, albo posortować je według określonego kryterium.

### Analiza grupowa
Metoda [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) pozwala grupować rekordy o tych samych wartościach w wybranej kolumnie, a następnie dla każdej grupy wykonać podgląd lub przekształcenia.

Wcześniej omawialiśmy [metodę `value_counts()`](/posts/summary-of-kaggle-pandas-course-1/#podglad-ogolnej-charakterystyki-danych); to samo działanie da się zrealizować metodą `groupby()` w następujący sposób:

```python
reviews.groupby('taster_name').size()
```

1. Grupuje DataFrame `reviews` według jednakowych wartości w kolumnie `taster_name`
2. Zwraca Series z rozmiarem (liczbą rekordów) każdej grupy

Albo:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. Grupuje DataFrame `reviews` według jednakowych wartości w kolumnie `taster_name`
2. Dla każdej grupy wybiera dane z kolumny `taster_name`
3. Zwraca Series z liczbą wartości niepustych (bez braków) w każdej grupie

Czyli `value_counts()` jest w istocie skrótem dla zachowania podobnego do powyższego. Poza metodą [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) można w ten sposób wykorzystywać dowolną funkcję podsumowującą. Na przykład, aby z danych o winach sprawdzić minimalną cenę dla każdego wyniku punktowego:

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

1. Grupuje DataFrame `reviews` według jednakowych wartości w kolumnie `points`
2. Dla każdej grupy wybiera dane z kolumny `price`
3. Zwraca Series z minimalną wartością w każdej grupie

Można też grupować po więcej niż jednej kolumnie. Aby wybrać wyłącznie informacje o winie z najwyższą oceną dla każdej pary (kraj, prowincja/stan):

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Kolejną przydatną metodą obiektu `DataFrameGroupBy` jest [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html). Pozwala ona po zgrupowaniu danych uruchomić jednocześnie kilka funkcji dla każdej grupy.

> W tym przypadku jako argument można przekazać:
> - funkcję,
> - napis z nazwą funkcji,
> - listę funkcji lub nazw funkcji,
> - słownik, gdzie kluczem jest etykieta osi, a wartością jest funkcja lub lista funkcji do zastosowania na tej osi.
>
> Sama funkcja musi:
> - przyjmować DataFrame jako wejście, albo
> - być możliwa do przekazania jako argument do (omawianej wcześniej) metody [`DataFrame.apply()`](/posts/summary-of-kaggle-pandas-course-1/#odwzorowania-maps) ([`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)).
>
> To uzupełnienie nie występowało w oryginalnym kursie Kaggle; dopisałem je, opierając się na oficjalnej dokumentacji Pandas.
{: .prompt-tip }

Na przykład w ten sposób można policzyć statystyki cen w podziale na kraje:

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> Tutaj `len` oznacza wbudowaną funkcję Pythona [`len()`](https://docs.python.org/3/library/functions.html#len); w tym przykładzie użyłem jej do wypisania liczby rekordów ceny (`price`) w każdej grupie (`country`) <u>łącznie z brakami danych</u>.
>
> Metoda [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) z Pandas różni się tym, że zwraca <u>wyłącznie liczbę poprawnych (niepustych) wartości</u>, z pominięciem braków.
>
> To uzupełnienie nie występowało w oryginalnym kursie Kaggle; dopisałem je, opierając się na oficjalnej dokumentacji Pythona i Pandas.
{: .prompt-tip }

### Indeks wielopoziomowy (MultiIndex)

Gdy przetwarza się i analizuje dane metodą `groupby()`, czasem zamiast zwykłych etykiet otrzymuje się DataFrame z indeksem wielopoziomowym (złożonym z dwóch lub więcej poziomów).

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

Indeks wielopoziomowy ma pewne metody przeznaczone do pracy ze strukturą hierarchiczną, których nie ma zwykły indeks. Szczegółowe przykłady i zalecenia dotyczące MultiIndex znajdziesz w sekcji [MultiIndex / advanced indexing w pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

W praktyce jednak najczęściej używaną metodą dla MultiIndex bywa [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html), która „spłaszcza” indeks z powrotem do zwykłego.

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

### Sortowanie

Jeśli przyjrzysz się `countries_reviewed`, zauważysz, że wynik grupowania jest zwracany w kolejności indeksu. Innymi słowy: kolejność wierszy w wyniku `groupby` jest wyznaczana nie przez „zawartość” danych, tylko przez wartości indeksu.

W razie potrzeby możesz ręcznie posortować dane w inny sposób. W tym celu wygodnie użyć metody [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). Na przykład poniżej sortujemy rosnąco według liczby rekordów (`len`):

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

`sort_values()` domyślnie sortuje rosnąco (od mniejszych do większych wartości). Jeśli ustawisz opcję, możesz sortować malejąco (od większych do mniejszych):

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

Aby sortować według indeksu, użyj metody [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html). Ma te same argumenty i domyślny kierunek sortowania co `sort_values()`, więc sposób użycia jest analogiczny.

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

Na koniec: można też sortować jednocześnie po więcej niż jednej kolumnie, np.:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lekcja 5. Typy danych i braki danych

W praktyce rzadko zdarza się, by dane były zawsze idealnie wyczyszczone. Często trzeba konwertować typy (bo nie są takie, jakich oczekujemy) albo radzić sobie z brakami danych i poprawnie je obsłużyć. Przy przetwarzaniu i analizie danych to zwykle najtrudniejszy etap.

### Typy danych

Typ danych konkretnej kolumny w DataFrame (albo typu danych Series) nazywa się **dtype**. Za pomocą atrybutu `dtype` można sprawdzić typ danej kolumny. Poniżej przykład dla kolumny `price` w DataFrame `reviews`:

```python
reviews.price.dtype
```

```
dtype('float64')
```

Można też użyć atrybutu `dtypes`, aby jednocześnie sprawdzić `dtype` wszystkich kolumn w DataFrame:

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

Typ danych mówi, jak Pandas przechowuje dane wewnętrznie. Na przykład `float64` oznacza 64-bitową liczbę zmiennoprzecinkową, a `int64` — 64-bitową liczbę całkowitą.

Warto też zauważyć jedną specyfikę: kolumny złożone wyłącznie z napisów (string) nie mają osobnego typu tekstowego i są po prostu traktowane jako obiekty (`object`).

Metoda [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) pozwala przekonwertować kolumnę z jednego typu na inny. Na przykład można przekonwertować kolumnę `points` z typu `int64` na `float64`:

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

Indeks DataFrame lub Series również ma typ danych:

```python
reviews.index.dtype
```

```
dtype('int64')
```

Poza tym Pandas wspiera także typy „zewnętrzne”, np. dane kategoryczne czy szeregi czasowe.

### Braki danych

Wpisy bez wartości (puste) dostają wartość `NaN` (skrót od „Not a Number”). Z powodów technicznych `NaN` zawsze ma typ `float64`.

Pandas udostępnia kilka funkcji wyspecjalizowanych do pracy z brakami danych. [Wcześniej widzieliśmy coś podobnego](/posts/summary-of-kaggle-pandas-course-1/#wybor-warunkowy): poza metodami istnieją też niezależne funkcje [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) oraz [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). Zwracają one informację, czy dany wpis jest brakiem (albo czy nim nie jest) — jako pojedynczą wartość boolowską albo tablicę wartości boolowskich — i można je wykorzystać np. tak:

```python
reviews[pd.isna(reviews.country)]
```

Zwykle najpierw trzeba sprawdzić, czy w danych są braki, a jeśli są — uzupełnić je w odpowiedni sposób. Istnieje kilka strategii. Po pierwsze, metoda [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) pozwala zastąpić braki jakąś sensowną wartością. Poniżej przykład, w którym wszystkie `NaN` w kolumnie `region_2` zastępujemy napisem `"Unknown"`:

```python
reviews.region_2.fillna("Unknown")
```

Można też zastosować strategię forward fill lub backward fill, czyli uzupełniać braki najbliższą poprawną wartością odpowiednio z przodu albo z tyłu. Da się to zrobić metodami [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) oraz [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html).

> Dawniej można było używać `fillna()` z argumentem `method` ustawionym na napisy `'ffill'` i `'bfill'`, ale od Pandas 2.1.0 ta metoda jest deprecated i nie jest zalecana. Zamiast tego należy używać `ffill()` lub `bfill()` odpowiednio do sytuacji.
{: .prompt-danger }

Bywa też tak, że nawet jeśli nie mamy braków danych, trzeba masowo zamienić jedną wartość na inną. W oryginalnym kursie Kaggle jako przykład podano sytuację, w której w zbiorze recenzji zmienił się twitterowy handle konkretnego recenzenta. To dobry przykład, ale spróbujmy wymyślić inny, bardziej „namacalny” w polskim (i nie tylko) kontekście.

Wyobraźmy sobie hipotetyczną sytuację, w której w Korei Południowej wydzielono północną część prowincji Gyeonggi-do jako nową jednostkę administracyjną pod nazwą **Gyeonggibuk-do**, i istnieje już zbiór danych, w którym ta nazwa figuruje. Następnie ktoś wpada na absurdalny pomysł, żeby tę całkiem sensowną nazwę **Gyeonggibuk-do** zmienić na **Pyeonghwanuri Special Self-Governing Province**, i jakimś cudem doprowadza do formalnego wdrożenia tej zmiany. ~~To tylko hipotetyczny scenariusz, ale przerażające jest to, że coś podobnego mogło się wydarzyć naprawdę.~~ Wtedy trzeba byłoby w istniejącym zbiorze danych masowo zamienić `"Gyeonggibuk-do"` na nowe wartości, np. `"Pyeonghwanuri State"` albo `"Pyeonghwanuri Special Self-Governing Province"`. Jednym ze sposobów wykonania takiej operacji w Pandas jest metoda [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html).

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

Korzystając z powyższego kodu, można skutecznie zamienić wszystkie wystąpienia `"Gyeonggibuk-do"` w kolumnie `province` zbioru `rok_2030_census` na „to długie coś”. ~~I z ulgą można stwierdzić, że na szczęście w realnym świecie nikt nie musiał tego naprawdę uruchamiać.~~

Tego typu zamiany napisów są przydatne również przy czyszczeniu danych i obsłudze braków, bo braki danych nie zawsze są zapisane jako `NaN` — często pojawiają się jako napisy typu `"Unknown"`, `"Undisclosed"`, `"Invalid"` itd. W realnych projektach, np. gdy tworzy się zbiory danych przez OCR starych dokumentów urzędowych, takie przypadki mogą wręcz dominować.

## Lekcja 6. Zmiana nazw i łączenie

Czasem trzeba zmienić nazwy kolumn lub indeksu w zbiorze danych. Równie często pojawia się potrzeba łączenia wielu DataFrame lub Series.

### Zmiana nazw

Metoda [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) pozwala zmieniać nazwy wybranych kolumn lub indeksu w zbiorze danych. `rename()` obsługuje różne formaty wejścia, ale najwygodniej zwykle użyć słownika Pythona. Poniżej przykład: zmieniamy nazwę kolumny `points` na `score` w DataFrame `reviews`, a także zmieniamy etykiety indeksu `0` i `1` na `firstEntry` oraz `secondEntry`.

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

W praktyce często zmienia się nazwy kolumn, ale bardzo rzadko zmienia się konkretne wartości indeksu. Do takich zastosowań zwykle wygodniej użyć (jak widzieliśmy wcześniej) metody [`set_index()`](/posts/summary-of-kaggle-pandas-course-1/#modyfikowanie-indeksu) ([`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)).

Indeks wierszy i indeks kolumn mają też własny atrybut `name`; metodą `rename_axis()` można zmienić nazwę osi. Na przykład: osi indeksu można nadać nazwę `wines`, a osi kolumn — `fields`.

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Łączenie zbiorów danych

Czasem trzeba łączyć DataFrame z DataFrame albo Series z Series. Pandas udostępnia do tego trzy kluczowe funkcje; od najprostszej do najbardziej złożonej są to: [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) oraz [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). Kurs Kaggle zaznacza, że większość tego, co da się zrobić `merge()`, można prościej zrobić `join()`, więc skupia się na dwóch pierwszych.

Funkcja `concat()` jest najprostsza: „dokleja” wiele DataFrame lub Series wzdłuż wybranej osi. Jest przydatna, gdy łączone obiekty mają te same pola (kolumny). Domyślnie konkatenacja idzie wzdłuż osi indeksu; można też ustawić `axis=1` lub `axis='columns'`, żeby sklejać wzdłuż osi kolumn.

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

> Według [oficjalnej dokumentacji Pandas]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html)) nie zaleca się tworzenia DataFrame przez dodawanie pojedynczych wierszy w pętli. Jeśli trzeba połączyć wiele wierszy, lepiej zebrać je w listę i scalić jedną operacją `concat()`.
{: .prompt-tip }

Metoda `join()` jest nieco bardziej złożona: dokleja jeden DataFrame do drugiego na podstawie indeksu. Jeśli występują kolumny o tych samych nazwach, trzeba podać argumenty `lsuffix` i `rsuffix`, aby dodać odpowiednie sufiksy rozróżniające nakładające się nazwy kolumn.

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
