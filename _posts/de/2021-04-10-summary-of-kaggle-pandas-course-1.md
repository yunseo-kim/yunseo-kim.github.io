---
title: "Zusammenfassung des Kaggle-„Pandas“-Kurses (1) – Lektion 1–3"
description: "Praxisleitfaden zu Pandas: Daten einlesen/schreiben, DataFrame & Series, Indexing mit loc/iloc, Filter, Zuweisungen, describe(), map/apply. Zusammenfassung der Kaggle‑Lektionen 1–3."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Hier fasse ich das zusammen, was ich im [Pandas](https://www.kaggle.com/learn/pandas)-Kurs von Kaggle gelernt habe.  
Da der Umfang recht groß ist, habe ich es in zwei Teile aufgeteilt.
- Teil 1: Lektion 1–3 (dieser Beitrag)
- [Teil 2: Lektion 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Zertifikat über den Abschluss](/assets/img/kaggle-pandas/certificate.png)

## Lektion 1. Erstellen, Lesen und Schreiben
### Pandas importieren

```python
import pandas as pd
```

Pandas hat zwei zentrale Objekttypen: **DataFrame** und **Series**.

### DataFrame
Ein [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) kann man sich als Tabelle bzw. [Matrix](/posts/vector-spaces-subspaces-and-matrices/#matrizen-und-matrixraum) vorstellen. Er besteht aus einer Matrix unabhängiger *Einträge*, wobei jeder Eintrag einen bestimmten *Wert* besitzt und genau einer *Zeile* bzw. einem *Datensatz* sowie genau einer *Spalte* zugeordnet ist.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

Einträge in einem DataFrame müssen nicht unbedingt numerisch sein. Im folgenden Beispiel enthält der DataFrame Zeichenketten (von Nutzerinnen und Nutzern hinterlassene Rezensionen).

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

Ein DataFrame wird mit dem Konstruktor `pd.DataFrame()` erzeugt und dabei mit Python-Dict-Syntax deklariert: Die Keys sind die Spaltennamen, die Values Listen mit den einzutragenden Werten. Das ist die Standardmethode, einen neuen DataFrame anzulegen.

Bei der Deklaration werden Spaltenlabels als Spaltennamen angegeben; Zeilenlabels werden, falls nicht spezifiziert, automatisch als 0, 1, 2, … vergeben. Bei Bedarf kann man die Zeilenlabels manuell festlegen. Die Liste der Zeilenlabels heißt beim DataFrame [**Index**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html) und kann über den Konstruktorparameter `index` gesetzt werden.

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
Eine [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) ist eine Folge (sequence) von Datenwerten bzw. ein [Vektor](/posts/vector-spaces-subspaces-and-matrices/#zeilen-und-spaltenvektoren).

```python
pd.Series([1, 2, 3, 4, 5])
```

Eine Series entspricht im Wesentlichen einer einzelnen Spalte eines DataFrames. Entsprechend kann man auch hier einen [Index](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html) setzen; statt eines „Spaltennamens“ hat sie jedoch lediglich einen einfachen [`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series und DataFrames sind eng miteinander verwandt. Man kann sich einen DataFrame hilfreich als Kollektion von Series denken.

### Daten aus Dateien einlesen
In vielen Fällen schreibt man Daten nicht selbst, sondern übernimmt sie aus bestehenden Quellen. Daten können in verschiedenen Formaten vorliegen; das grundlegendste ist CSV. Eine CSV-Datei sieht typischerweise so aus:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

CSV ist also eine Tabelle, in der Werte durch Kommas (comma) getrennt sind – daher „Comma-Separated Values“, CSV.

CSV-Daten liest man mit [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) in einen DataFrame ein.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

Mit dem Attribut [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) lässt sich die Form des DataFrames abfragen.

```python
product_reviews.shape
```

```
(129971, 14)
```

Die obige Ausgabe bedeutet: 129971 Datensätze (Zeilen) und 14 Spalten.

Mit der Methode [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) sieht man die ersten fünf Zeilen.

```python
product_reviews.head()
```

[Die Funktion `pd.read_csv()` besitzt über 30 Parameter](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Enthält die CSV-Datei z. B. bereits einen eigenen Index, kann man mit `index_col` angeben, dass diese Spalte als Index verwendet wird, statt dass Pandas automatisch indiziert.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Daten in Dateien schreiben
Mit der Methode [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) kann man einen DataFrame als CSV exportieren. Beispiel:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lektion 2. Indexing, Selecting & Assigning
Das Auswählen bestimmter Werte aus einem Pandas-DataFrame oder einer Series ist Schritt in fast jeder Datenaufgabe. Es ist daher wichtig, früh effizient auswählen zu lernen.

### Python-native Zugriffe
Native Python-Objekte bieten gute Indexing-Mechanismen, und Pandas stellt dieselben Mechanismen bereit.

#### Objekteigenschaften
In Python greift man auf den Wert einer Objekteigenschaft über deren Namen zu. Hat z. B. das Objekt `example_obj` ein Attribut `title`, kann man `example_obj.title` schreiben. Für DataFrame-Spalten gilt dasselbe.

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

#### Dict-Indexierung
Beim Dict-Typ greift man mit dem Indexoperator (`[]`) auf Werte zu. Für DataFrame-Spalten gilt das ebenso.

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

Beide Varianten – Attributzugriff und Dict-Indexierung – sind gültig. Der Dict-Stil hat den Vorteil, dass er auch Spaltennamen mit Leerzeichen oder anderen reservierten Zeichen unterstützt (z. B. geht `reviews['country providence']`, während `reviews.country providence` nicht funktioniert).

Auch innerhalb der so ausgewählten Series kann man wiederum mit dem Indexoperator auf Einzelwerte zugreifen.

```python
reviews['country'][0]
```

```
'Italy'
```

### Pandas-spezifische Zugriffe
Neben den oben beschriebenen Zugriffen bietet Pandas die speziellen Zugriffsattribute [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) und [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Positionsbasiertes Auswählen
Mit `iloc` führt man eine **positionsbasierte Auswahl (index-based selection)** durch. Man wählt anhand der ganzzahligen Position im Datenraster.

Beispielsweise wählt Folgendes die erste Zeile:

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

Im Gegensatz zum Python-Stil (zuerst Spalte, dann Zeile) wählt `iloc` zuerst Zeilen, dann Spalten. Die erste Spalte erhält man so:

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

Hier wählt `:` alle Zeilen, danach wird die erste Spalte ausgewählt. Möchte man z. B. die zweite (`1`) und dritte (`2`) Zeile der ersten Spalte, schreibt man:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Oder man übergibt eine Liste:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Mit negativen Indizes kann man vom Ende aus wählen, z. B. die letzten fünf Zeilen:

```python
reviews.iloc[-5:]
```

#### Labelbasierte Auswahl
Mit `loc` führt man eine **labelbasierte Auswahl (label-based selection)** durch. Hier wird nicht die Position, sondern der Wert des Index verwendet.

Beispiel: Der Eintrag in der Spalte 'country' der Zeile mit Index 0:

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignoriert den DataFrame-Index und behandelt die Daten als reine Matrix; Zugriffe erfolgen positionsbasiert. `loc` nutzt hingegen die Indexinformationen. Da Indizes oft semantisch bedeutsam sind, ist `loc` in vielen Fällen intuitiver.

#### Unterschied der Bereichsspezifikation bei `iloc` und `loc`
`iloc` verwendet die Standard-Indexierung aus der Python-Standardbibliothek: `0:10` bedeutet das halboffene Intervall 0 bis strikt kleiner 10, also `0,...,9`.

`loc` interpretiert Bereiche als geschlossen: `0:10` bedeutet 0 bis 10 einschließlich, also `0,...,10`.

Der Grund: `loc` kann neben ganzen Zahlen auch andere Standard-Datentypen als Index verwenden. Hat man z. B. Indexwerte `Apples, ..., Potatoes, ...` und möchte alle Kulturen von 'Apples' bis 'Potatoes' in alphabetischer Reihenfolge auswählen, ist es wesentlich intuitiver, `df.loc['Apples':'Potatoes']` zu schreiben als über einen „künstlichen“ oberen Schrankenwert wie 'Potatoet' zu gehen. Für Nicht-Integer-Indizes ist die geschlossene Intervallschreibweise meist natürlicher, daher folgt `loc` dieser Konvention.

Abgesehen davon verhalten sich beide ansonsten gleich.

> Persönlich verwende ich bei aufsteigend sortierten Integer-Indizes und Bereichsauswahlen mit `:` oft `iloc`, um Verwechslungen wegen der unterschiedlichen Bereichssemantik zu vermeiden; in anderen Fällen bevorzuge ich das intuitivere `loc`.
{: .prompt-tip }

### Mit dem Index arbeiten
Man kann den Index nach Bedarf anpassen. Mit [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) lässt sich z. B. eine bestimmte Spalte als neuer Index setzen:

```python
reviews.set_index("title")
```

### Bedingte Auswahl
Bisher haben wir über strukturelle Eigenschaften des DataFrames selektiert. Darüber hinaus kann man Daten nach komplexeren Bedingungen filtern.

Beispiel: Aus einem DataFrame mit Weininformationen sollen nur die italienischen Weine mit einer Bewertung ab 90 Punkten ausgewählt werden.

```python
reviews.country == 'Italy'
```

Die Bedingung ergibt eine Series aus `True`/`False`-Werten.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` ist zwar labelbasiert, akzeptiert aber auch boolesche Arrays oder sortierbare boolesche Series](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). So selektiert man die italienischen Weine:

```python
reviews.loc[reviews.country == 'Italy']
```

Mehrere Bedingungen lassen sich mit `&` bzw. `|` verknüpfen. Italienisch **und** mindestens 90 Punkte:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Italienisch **oder** mindestens 90 Punkte:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas bringt zudem einige eingebaute Selektoren mit, u. a. `isin` und `isnull`/`notnull`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) prüft, ob ein Wert in einer Liste enthalten ist, und liefert eine boolesche Maske, mit der man filtern kann. Beispiel: italienische oder französische Weine:

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) filtern nach fehlenden (`NaN`) bzw. nicht fehlenden Werten. Beispiel: nur Weine mit vorhandenem Preis:

```python
reviews.loc[reviews.price.notna()]
```

> Anmerkung: Im ursprünglichen Kaggle-Kurs nicht erwähnt, aber [`iloc` akzeptiert ebenfalls boolesche Arrays](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Im Unterschied zu `loc` werden jedoch nur Arrays, nicht Series unterstützt, wodurch sich obige Muster weniger bequem anwenden lassen.
{: .prompt-tip }

### Zuweisungen
Man kann in einem DataFrame neue Daten zuweisen oder bestehende überschreiben.

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

## Lektion 3. Summary Functions and Maps
### Überblick über die Daten
Die Methode [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) liefert einen hochrangigen Überblick über eine gegebene Spalte.

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

Die Ausgabe von `describe()` hängt vom Datentyp ab. Für Strings (nicht-numerische Daten) sieht sie z. B. so aus:

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

Man kann auch gezielt einzelne Statistiken abfragen.

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

Möchte man wissen, wie oft jeder eindeutige Wert in einer Spalte vorkommt, verwendet man [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

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

### Abbildungen (Maps)
Eine **Abbildung (map)** ist ein Begriff aus der Mathematik und bezeichnet eine Funktion, die eine Menge auf eine andere abbildet. In der Data Science müssen Daten oft in andere Repräsentationen transformiert werden; dafür nutzt man Abbildungen – entsprechend sind sie sehr wichtig.

Zwei Methoden werden besonders häufig verwendet.

Die Methode [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) nimmt eine Funktion, die jeweils einen einzelnen <u>Wert</u> auf einen anderen Einzelwert abbildet, und wendet sie auf alle Werte der <u>Series</u> an; zurück kommt eine neue Series. Beispiel: Von allen Weinbewertungen den Mittelwert subtrahieren, um Abweichungen zu erhalten.

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

Mit [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) wendet man eine benutzerdefinierte Funktion auf jede <u>Zeile</u> an, um den gesamten <u>DataFrame</u> zu transformieren.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Mit `apply()` und `axis='index'` kann man statt zeilenweise auch spaltenweise arbeiten.

`Series.map()` und `DataFrame.apply()` liefern jeweils neue, transformierte Objekte zurück und verändern die Originaldaten nicht.

| Methode | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Ziel | Series | DataFrame |
| Anwendungseinheit | Anwendung auf Einzelwerte <br>(interpretiert man eine Series als [Spaltenvektor](/posts/vector-spaces-subspaces-and-matrices/#zeilen-und-spaltenvektoren), entspricht das einer zeilenweisen Anwendung) | standardmäßig zeilenweise <br> optional spaltenweise mit `axis='index'` |

> Hinweis: Es gibt auch [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) und [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html).
> - `Series.apply()`:
>   - `by_row='compat'` (Standard): verhält sich wie `Series.map()`
>   - `by_row=False`: übergibt die gesamte Series als ein Argument (ähnlich `DataFrame.apply()` mit `axis='index'`)
> - `DataFrame.map()`: wendet eine Funktion auf Einzelwerte im DataFrame an (ähnlich `Series.map()`, nur auf DataFrames)
{: .prompt-tip }

Pandas unterstützt viele gängige Abbildungen bereits direkt. Das obige Beispiel lässt sich z. B. deutlich einfacher schreiben; Pandas erkennt die Absicht und führt es korrekt aus.

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

Außerdem unterstützt Pandas auch Operationen zwischen Series gleicher Länge. Im Weinbeispiel kann man z. B. Herkunftsland und Region einfach als Strings konkatenieren:

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

Diese Operationen sind durch eingebaute Optimierungen meist schneller als `map()` oder `apply()`. Pandas unterstützt dieses Verhalten für alle Standardoperatoren (`>`, `<`, `==` usw.). `map()` und `apply()` bleiben dennoch wichtig, da sie flexibler sind und komplexere Aufgaben erlauben.
