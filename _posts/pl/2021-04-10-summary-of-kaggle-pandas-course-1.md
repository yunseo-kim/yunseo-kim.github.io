---
title: "Podsumowanie kursu Kaggle „Pandas” (1) — lekcje 1–3"
description: "Podsumowanie wykorzystania biblioteki Pandas do czyszczenia i przetwarzania danych. Streszczenie kursu Kaggle „Pandas” z drobnymi uzupełnieniami; część 1 obejmuje lekcje 1–3."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Poniżej porządkuję notatki z nauki na kursie Kaggle [Pandas](https://www.kaggle.com/learn/pandas).  
Ponieważ materiału jest całkiem sporo, podzieliłem go na 2 części.
- Część 1: lekcje 1–3 (ten wpis)
- [Część 2: lekcje 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Certyfikat ukończenia](/assets/img/kaggle-pandas/certificate.png)

## Lekcja 1. Tworzenie, odczyt i zapis
### Import Pandas

```python
import pandas as pd
```

W Pandas są dwa kluczowe obiekty: **DataFrame** i **Series**.

### DataFrame
[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) można traktować jak tabelę albo [macierz](/posts/vector-spaces-subspaces-and-matrices/#macierze-i-przestrzen-macierzy). Składa się z macierzy niezależnych *wpisów (entries)*; każdy wpis ma pewną *wartość (value)* i odpowiada jednemu *wierszowi (row)* lub *rekordowi (record)* oraz jednej *kolumnie (column)*.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

Wpisy w DataFrame nie muszą być liczbami; poniżej przykład DataFrame z wartościami tekstowymi (recenzje pozostawione przez użytkowników).

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

Aby utworzyć obiekt DataFrame, używa się konstruktora `pd.DataFrame()` i składni słownika (dictionary) Pythona. Klucze (key) to nazwy kolumn, a wartości (value) to listy (list) elementów do wpisania. Jest to standardowy sposób deklarowania nowego DataFrame.

Przy tworzeniu DataFrame etykiety kolumn nadaje się jako nazwy kolumn, natomiast jeśli nie podasz osobno etykiet wierszy, Pandas przypisze liczby całkowite 0, 1, 2, .... W razie potrzeby etykiety wierszy można ustawić ręcznie. Lista etykiet wierszy w DataFrame nazywa się [**indeksem (Index)**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html) i można ją podać parametrem `index` w konstruktorze.

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
[Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) to ciąg (sequence) wartości danych, czyli inaczej [wektor](/posts/vector-spaces-subspaces-and-matrices/#wektory-wierszowe-i-kolumnowe).

```python
pd.Series([1, 2, 3, 4, 5])
```

Series jest w istocie pojedynczą kolumną DataFrame. Dlatego tak samo można określić [indeks](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html), a zamiast „nazwy kolumny” ma po prostu „nazwę” ([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series i DataFrame są ze sobą ściśle powiązane. Pomaga myśleć o DataFrame jak o „wiązce” (zbiorze) obiektów Series.

### Wczytywanie plików z danymi
W wielu przypadkach zamiast pisać dane ręcznie, wczytuje się istniejące dane. Dane mogą być zapisane w różnych formatach, ale najbardziej podstawowy to CSV. Zawartość pliku CSV zwykle wygląda tak:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

Czyli CSV to tabela, w której wartości są rozdzielane przecinkami (comma). Stąd nazwa „Comma-Separated Values”, CSV.

Aby wczytać dane w formacie CSV do DataFrame, używa się funkcji [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

Atrybut [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) pozwala sprawdzić wymiary DataFrame.

```python
product_reviews.shape
```

```
(129971, 14)
```

Powyższy wynik oznacza, że DataFrame ma 129971 rekordów i 14 kolumn.

Metoda [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) pozwala podejrzeć pierwsze pięć wierszy DataFrame.

```python
product_reviews.head()
```

[Funkcja `pd.read_csv()` ma ponad 30 parametrów](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Na przykład, jeśli wczytywany plik CSV sam zawiera indeks, można ustawić parametr `index_col`, aby zamiast automatycznego indeksowania Pandas użył wskazanej kolumny jako indeksu.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Zapisywanie plików z danymi
Metoda [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) pozwala wyeksportować DataFrame do pliku CSV. Użycie wygląda następująco:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lekcja 2. Indeksowanie, wybieranie i przypisywanie
Wybieranie konkretnych wartości z DataFrame lub Series to etap, przez który przechodzi praktycznie każde przetwarzanie danych. Dlatego w pierwszej kolejności warto nauczyć się szybko i efektywnie wybierać potrzebne punkty danych.

### Dostępory (accessors) wbudowane w Pythona
Natywne obiekty Pythona oferują świetne sposoby indeksowania danych, a Pandas zapewnia te same mechanizmy.

#### Atrybuty obiektu
W Pythonie do wartości atrybutu (property) obiektu można dostać się przez jego nazwę (attribute). Na przykład jeśli obiekt `example_obj` ma atrybut `title`, to można go odczytać jako `example_obj.title`. Analogicznie można odwoływać się do kolumn DataFrame.

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

#### Indeksowanie jak w słowniku
W przypadku słownika w Pythonie do wartości można uzyskać dostęp operatorem indeksowania (`[]`). Tę samą metodę można stosować również do kolumn DataFrame.

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

Obie metody (dostęp przez atrybut i indeksowanie jak słownik) są poprawne, ale indeksowanie słownikowe ma tę zaletę, że radzi sobie z nazwami kolumn zawierającymi znaki zastrzeżone, np. spacje (np. `reviews['country providence']` jest możliwe, natomiast `reviews.country providence` — nie).

Tak wybraną Series można dalej indeksować operatorem `[]`, aby odczytać pojedynczą wartość.

```python
reviews['country'][0]
```

```
'Italy'
```

### Dostępory specyficzne dla Pandas
Podejścia opisane wyżej świetnie „współgrają” z resztą ekosystemu Pythona, ale Pandas udostępnia też własne, charakterystyczne dostępory: [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) i [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Wybór oparty o indeks (pozycję)
Korzystając z `iloc`, można wykonywać **wybór oparty o indeks/pozycję (index-based selection)**. Wybiera się dane, wskazując pozycje jako liczby całkowite.

Na przykład w ten sposób wybierzesz pierwszy wiersz DataFrame:

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

W odróżnieniu od natywnego podejścia Pythona, gdzie najczęściej wybiera się najpierw kolumnę, a potem wiersz, `iloc` wybiera najpierw wiersze, a dopiero potem kolumny. Pierwszą kolumnę DataFrame można wybrać tak:

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

W powyższym przykładzie użyto operatora `:`, aby wybrać wszystkie wiersze, a następnie w ich obrębie pierwszą kolumnę. Jeśli chcesz wybrać 2. (`1`) i 3. (`2`) wiersz pierwszej kolumny, zrób to tak:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Możesz też przekazać listę:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Można używać liczb ujemnych, aby wybierać dane „od końca”. Poniższy przykład wybiera ostatnie 5 wierszy:

```python
reviews.iloc[-5:]
```

#### Wybór oparty o etykiety
Inną metodą jest użycie `loc` do wykonania **wyboru opartego o etykiety (label-based selection)**. W tym przypadku wybiera się dane nie po położeniu, tylko po wartościach indeksu.

Na przykład, aby uzyskać wpis z kolumny `country` dla wiersza o indeksie 0:

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignoruje wartości indeksu zbioru danych i traktuje całość jak jedną dużą macierz — dostęp do pojedynczych wpisów zależy wyłącznie od pozycji. Z kolei `loc` wykorzystuje informacje o indeksie. Ponieważ indeks często niesie istotną informację, w wielu sytuacjach `loc` jest bardziej intuicyjny niż `iloc`.

#### Różnica w sposobie wyznaczania zakresów w `iloc` i `loc`
`iloc` używa standardowego schematu indeksowania z biblioteki standardowej Pythona, więc `0:10` oznacza przedział domknięto-otwarty: od 0 do 10 **bez** 10, czyli `0,...,9`.

Natomiast `loc` traktuje zakres jako domknięty, więc `0:10` oznacza od 0 do 10 **włącznie**, czyli `0,...,10`.

Powód jest taki, że `loc` pozwala używać jako indeksu nie tylko liczb całkowitych, ale też dowolnych standardowych typów danych. Załóżmy np., że masz DataFrame z indeksami w rodzaju `Apples, ..., Potatoes, ...` i chcesz wybrać uprawy od „Apples” do „Potatoes” włącznie w porządku alfabetycznym. Ponieważ po „Potatoes” może pojawić się ciąg znaków „Potatoet”, zapis „od 'Apples' do przed 'Potatoet'” (`df.loc['Apples':'Potatoet']`) jest mniej intuicyjny niż po prostu „od 'Apples' do 'Potatoes'” (`df.loc['Apples':'Potatoes']`). Dla indeksów niebędących liczbami całkowitymi zwykle bardziej intuicyjny jest ten drugi zapis — dlatego `loc` stosuje domknięty zakres.

Poza tym reszta zachowania jest zasadniczo taka sama.

> Osobiście, jeśli muszę wyznaczać zakres operatorem `:` w zbiorze danych z rosnącym, całkowitoliczbowym indeksem, wolę `iloc`, żeby uniknąć zamieszania wynikającego z różnic w domknięciu zakresu. W pozostałych przypadkach częściej wybieram bardziej intuicyjne `loc`.
{: .prompt-tip }

### Modyfikowanie indeksu
Indeks można również dostosowywać. Metoda [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) pozwala — jak w przykładzie poniżej — ustawić wybraną kolumnę jako nowy indeks.

```python
reviews.set_index("title")
```

### Wybór warunkowy
Powyższe podejścia dotyczyły wybierania i przetwarzania danych na podstawie strukturalnych własności DataFrame. Można jednak iść dalej i wybierać dane spełniające bardziej złożone warunki.

Załóżmy na przykład, że w DataFrame z informacjami o winach chcesz wybrać tylko wina z Włoch, które mają ocenę co najmniej 90.

```python
reviews.country == 'Italy'
```

To wyrażenie zwraca Series z wartościami boolowskimi `True`/`False`.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` jest domyślnie oparty o etykiety, ale może też przyjmować tablice boolowskie albo sortowalne Series boolowskie](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). Dlatego można w ten sposób wybrać tylko wina z Włoch:

```python
reviews.loc[reviews.country == 'Italy']
```

Wiele warunków można łączyć operatorami `&` albo `|`. Aby wybrać wina, które są z Włoch **i jednocześnie** mają co najmniej 90 punktów:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Aby wybrać wina, które są z Włoch **lub** mają co najmniej 90 punktów:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas ma też kilka wbudowanych selektorów warunkowych, w szczególności `isin` oraz `isnull`/`notnull`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) zwraca maskę boolowską (`True` albo `False`) informującą, czy dana wartość należy do (is in) podanej listy. Można jej użyć do wyboru danych. Na przykład, aby wybrać wina z Włoch lub z Francji:

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) służą do wybierania danych z brakami (`NaN`) lub bez braków. Na przykład, aby wybrać tylko wina, dla których cena nie jest brakująca:

```python
reviews.loc[reviews.price.notna()]
```

> Dla porządku: to nie było w oryginalnym kursie Kaggle, ale [`iloc` również może przyjmować tablice boolowskie (array)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Jednak w przeciwieństwie do `loc` wspiera tylko tablice, a nie Series, więc trudniej to wykorzystać w podobny sposób jak powyżej.
{: .prompt-tip }

### Przypisywanie danych
Do DataFrame można też przypisywać nowe dane albo nadpisywać istniejące.

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

## Lekcja 3. Funkcje podsumowujące i mapowania
### Podgląd ogólnej charakterystyki danych
Metoda [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) daje wysokopoziomowe podsumowanie danej kolumny.

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

Wyjście `describe()` zależy od typu danych. Dla danych tekstowych (string) wynik wygląda np. tak:

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

Można też wyciągać wybrane statystyki.

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

Jeśli chcesz wiedzieć, ile razy występuje każda unikalna wartość w DataFrame, użyj metody [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

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

### Odwzorowania (Maps)
**Odwzorowanie (map)** to termin zapożyczony z matematyki i oznacza funkcję, która przyporządkowuje elementy jednego zbioru elementom innego zbioru. W data science często zachodzi potrzeba przekształcania danych do innej postaci — i wtedy używa się odwzorowań, więc jest to bardzo ważne.

Najczęściej używa się dwóch metod.

Metoda [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) przyjmuje funkcję przekształcającą pojedynczą <u>wartość</u> w inną pojedynczą wartość, stosuje ją zbiorczo do wszystkich wartości w danej <u>Series</u>, a następnie zwraca nową Series. Przykładowo, jeśli chcesz odjąć średnią od wszystkich ocen win, aby otrzymać odchylenia:

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

Metoda [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) służy wtedy, gdy chcesz wywołać własną funkcję dla każdego <u>wiersza</u> i zastosować przekształcenie do całego <u>DataFrame</u>.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Jeśli wywołasz `apply()` z parametrem `axis='index'`, możesz zastosować funkcję nie do wierszy, lecz do kolumn.

Zarówno `Series.map()`, jak i `DataFrame.apply()` zwracają odpowiednio nową (przekształconą) Series i DataFrame, nie modyfikując oryginalnych danych.

| Metoda | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Obiekt docelowy | Series | DataFrame |
| Jednostka zastosowania | Zastosowanie do pojedynczych wartości <br>(jeśli traktować Series jako [wektor kolumnowy](/posts/vector-spaces-subspaces-and-matrices/#wektory-wierszowe-i-kolumnowe), to zastosowanie „wierszami”) | Domyślnie zastosowanie do wierszy <br> po ustawieniu opcji możliwe też do kolumn |

> Dla porządku: istnieją też [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) oraz [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html).
> - `Series.apply()`:
>   - `by_row='compat'` (domyślnie): działa tak samo jak `Series.map()`
>   - `by_row=False`: przekazuje całą Series jako jedno wejście funkcji (podobnie do działania `DataFrame.apply()` dla `axis='index'`)
> - `DataFrame.map()`: stosuje funkcję do pojedynczych wartości w DataFrame (analogicznie do `Series.map()`, z tą różnicą, że obiektem jest DataFrame, a nie Series)
{: .prompt-tip }

W praktyce Pandas wspiera wiele często używanych odwzorowań „wbudowanie”. Przykład z poprzedniej sekcji można zrealizować dużo prościej, a Pandas i tak poprawnie zinterpretuje intencję:

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

Co więcej, Pandas wspiera też operacje pomiędzy Series o tej samej długości. W przykładzie z winami można np. połączyć tekstowo informację o kraju i regionie produkcji:

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

Te operacje są szybsze niż `map()` czy `apply()`, ponieważ wykorzystują wbudowane mechanizmy przyspieszania obliczeń w Pandas. Pandas potrafi działać w ten sposób dla wszystkich standardowych operatorów Pythona (`>`, `<`, `==` itd.). Mimo to `map()` i `apply()` są bardziej elastyczne i pozwalają wykonać bardziej złożone zadania — warto więc je znać.
