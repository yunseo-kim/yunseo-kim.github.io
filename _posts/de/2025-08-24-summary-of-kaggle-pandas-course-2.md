---
title: "Zusammenfassung des Kaggle-„Pandas“-Kurses (2) – Lektion 4–6"
description: "Praxisleitfaden zu Pandas für Datenbereinigung und -aufbereitung: Gruppieren & Sortieren, Datentypen & Missing Values, Umbenennen & Kombinieren. Zusammenfassung und Ergänzungen zu Kaggle‑Lektion 4–6."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Hier fasse ich das zusammen, was ich im [Pandas](https://www.kaggle.com/learn/pandas)-Kurs von Kaggle gelernt habe.  
Da der Umfang recht groß ist, habe ich es in zwei Teile aufgeteilt.
- [Teil 1: Lektion 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- Teil 2: Lektion 4–6 (dieser Beitrag)

![Zertifikat über den Abschluss](/assets/img/kaggle-pandas/certificate.png)

## Lektion 4. Gruppieren und Sortieren
Oft muss man Daten in Gruppen einteilen und gruppenweise Operationen ausführen oder nach bestimmten Kriterien sortieren.

### Gruppenauswertung
Mit der Methode [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) lassen sich Daten mit gleichem Wert in einer bestimmten Spalte zu Gruppen zusammenfassen und anschließend gruppenweise überblicken oder transformieren.

Zuvor hatten wir bereits die [Methode `value_counts()`](/posts/summary-of-kaggle-pandas-course-1/#uberblick-uber-die-daten) kennengelernt; dasselbe Verhalten kann man mit `groupby()` wie folgt nachbilden.

```python
reviews.groupby('taster_name').size()
```

1. Den DataFrame `reviews` nach gleichen Werten in der Spalte `taster_name` gruppieren
2. Die Größe jeder Gruppe (Anzahl der Zeilen) als Series zurückgeben

Oder:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. Den DataFrame `reviews` nach gleichen Werten in der Spalte `taster_name` gruppieren
2. Pro Gruppe die Spalte `taster_name` auswählen
3. Die Anzahl der Nicht-Null-Werte als Series zurückgeben

Mit anderen Worten: `value_counts()` ist im Grunde nur eine Abkürzung für obige Operationen. Neben [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) lassen sich so beliebige Übersichts-/Aggregatfunktionen einsetzen. Möchte man z. B. den Minimalpreis je Bewertungspunkt ermitteln, geht das so:

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

1. Den DataFrame `reviews` nach gleichen Werten in der Spalte `points` gruppieren
2. Pro Gruppe die Spalte `price` auswählen
3. Den Minimalwert je Gruppe als Series zurückgeben

Man kann auch nach mehreren Spalten gruppieren. Um je Land und Provinz den Wein mit der höchsten Punktzahl auszuwählen:

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Eine weitere nützliche Methode von DataFrameGroupBy-Objekten ist [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html). Damit kann man nach dem Gruppieren mehrere Funktionen pro Gruppe gleichzeitig ausführen.

> Als Argumente sind zulässig:
> - eine Funktion
> - ein Funktionsname als String
> - eine Liste aus Funktionen oder Funktionsnamen
> - ein Dict, dessen Keys Achsenlabels sind und dessen Values je Achse eine Funktion oder Funktionsliste angeben
>
> Die Funktionen müssen
> - einen DataFrame als Eingabe akzeptieren können oder
> - mit [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) [wie zuvor behandelt](/posts/summary-of-kaggle-pandas-course-1/#abbildungen-maps) übergebbar sein.
>
> Dies stand im ursprünglichen Kaggle-Kurs nicht; es wurde anhand der offiziellen Pandas‑Doku ergänzt.
{: .prompt-tip }

Beispiel: einfache Preisstatistiken je Land berechnen.

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> `len` ist die Python‑Builtin‑Funktion [`len()`](https://docs.python.org/3/library/functions.html#len). Im obigen Beispiel liefert sie die <u>inklusive fehlender Werte</u> gezählte Anzahl der Preiswerte (`price`) pro Gruppe (`country`). Da sie mit DataFrames bzw. Series umgehen kann, ist dieser Einsatz möglich.
>
> Die Pandas‑Methode [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) zählt hingegen nur <u>nicht fehlende (gültige) Werte</u> und unterscheidet sich somit im Verhalten.
>
> Dies stand im ursprünglichen Kaggle‑Kurs nicht; es wurde anhand der Python‑ und Pandas‑Doku ergänzt.
{: .prompt-tip }

### MultiIndex
Bei gruppierungsbasierten Transformationen erhält man mitunter DataFrames mit mehrstufigem Index statt eines einfachen Index.

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

Ein MultiIndex bringt einige Methoden mit, die es für einfache Indizes nicht gibt. Ausführliche Beispiele und Richtlinien finden sich im Abschnitt „MultiIndex / advanced indexing“ des [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

Am häufigsten wird man jedoch den MultiIndex wieder zu einem normalen Index zurückführen wollen – mit [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html):

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

### Sortieren
Schaut man sich unser Beispiel `countries_reviewed` an, fällt auf: Die gruppierten Ergebnisse werden in der Reihenfolge der Indexwerte zurückgegeben. Die Zeilenreihenfolge des `groupby`-Ergebnisses wird also nicht vom Inhalt, sondern vom Index bestimmt.

Bei Bedarf kann man selbst sortieren – komfortabel mit [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). Zum Beispiel lässt sich nach der enthaltenen Anzahl („len“) aufsteigend sortieren:

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

Standardmäßig sortiert `sort_values()` aufsteigend; mit einer Option geht auch absteigend:

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

Zum Sortieren nach dem Index verwendet man [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html). Es besitzt dieselben Argumente und dieselbe Standardreihenfolge (absteigend) wie `sort_values()`; die Anwendung ist identisch.

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

Schließlich kann man auch nach mehreren Spalten gleichzeitig sortieren:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lektion 5. Datentypen und fehlende Werte
Reale Daten sind selten perfekt bereinigt. Meistens muss man Datentypen konvertieren und mit fehlenden Werten umgehen. In vielen Projekten ist genau dieser Schritt die größte Hürde.

### Datentypen
Der Datentyp einer DataFrame‑Spalte bzw. Series heißt in Pandas der **dtype**. Über das Attribut `dtype` ermittelt man den Typ einer Spalte. Beispiel: der `dtype` der Spalte `price` im DataFrame `reviews`.

```python
reviews.price.dtype
```

```
dtype('float64')
```

Mit dem Attribut `dtypes` bekommt man alle Spaltentypen auf einmal:

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

Der Datentyp gibt an, wie Pandas die Werte intern speichert: `float64` für 64‑Bit‑Gleitkommazahlen, `int64` für 64‑Bit‑Integer usw.

Eine Besonderheit: Spalten, die ausschließlich Strings enthalten, besitzen keinen eigenen String‑Typ, sondern sind vom Typ `object`.

Mit [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) lassen sich Spalten in andere Typen konvertieren. So kann man etwa die `int64`‑Spalte `points` in `float64` konvertieren:

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

Auch der Index eines DataFrames oder einer Series hat einen eigenen Datentyp:

```python
reviews.index.dtype
```

```
dtype('int64')
```

Daneben unterstützt Pandas externe Typen wie Kategoriedaten und Zeitreihen.

### Fehlende Werte
Leere Einträge (ohne Wert) werden als `NaN` („Not a Number“) markiert. Aus technischen Gründen ist `NaN` stets vom Typ `float64`.

Pandas bietet spezielle Funktionen für Missing Values. [Ähnlich wie bereits kurz gesehen](/posts/summary-of-kaggle-pandas-course-1/#bedingte-auswahl) gibt es neben Methoden auch unabhängige Funktionen: [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) und [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). Sie liefern, je nach Eingabe, einen booleschen Einzelwert oder ein boolesches Array und lassen sich so einsetzen:

```python
reviews[pd.isna(reviews.country)]
```

Oft prüft man zunächst, ob Missing Values vorhanden sind, und füllt sie anschließend sinnvoll. Eine Strategie ist [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html): fehlende Werte durch einen geeigneten Ersatzwert auffüllen. Beispiel: alle `NaN` in `reviews.region_2` durch `"Unknown"` ersetzen.

```python
reviews.region_2.fillna("Unknown")
```

Alternativ kann man mit dem jeweils nächstliegenden gültigen Wert aus der Vergangenheit/Zukunft auffüllen (Forward/Backward Fill): [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) bzw. [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html).

> Früher konnte man `fillna()` auch mit dem Parameter `method` und den Strings `'ffill'`/`'bfill'` verwenden; seit Pandas 2.1.0 ist das deprecatet. Stattdessen sollten situativ `ffill()` bzw. `bfill()` genutzt werden.
{: .prompt-danger }

Mitunter möchte man Werte – auch wenn sie nicht fehlend sind – pauschal durch andere ersetzen. Im Originalkurs wird z. B. ein geänderter Twitter‑Handle einer/s Rezensent:in erwähnt. Ein anderes Beispiel (hierzulande vielleicht greifbarer):

Angenommen, in Südkorea würde der nördliche Teil der Provinz Gyeonggi als neue Verwaltungseinheit abgetrennt und als **Gyeonggibuk-do** eingeführt, und ein Datensatz verwendet schon diesen Namen. Nun kommt jemand auf die „glorreiche“ Idee, **Gyeonggibuk-do** in **Pyeonghwanuri Special Self-Governing Province** umzubenennen – und setzt es tatsächlich durch. Dann müsste man im bestehenden Datensatz `"Gyeonggibuk-do"` durch `"Pyeonghwanuri State"` bzw. `"Pyeonghwanuri Special Self-Governing Province"` ersetzen. In Pandas bietet sich dafür die Methode [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html) an.

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

Mit dem obigen Code ersetzt man in der Spalte `province` des DataFrames `rok_2030_census` alle Vorkommen von `"Gyeonggibuk-do"` durch den langen neuen Namen. 

Solche String‑Ersetzungen sind auch bei der Datenbereinigung hilfreich: Missing Values erscheinen in der Praxis oft nicht als `NaN`, sondern als Strings wie `"Unknown"`, `"Undisclosed"` oder `"Invalid"`. Insbesondere bei OCR‑Erfassung älterer Dokumente ist das eher die Regel als die Ausnahme.

## Lektion 6. Umbenennen und Kombinieren
Mitunter möchte man Spalten- oder Indexnamen ändern. Häufig muss man auch mehrere DataFrames/Series zusammenführen.

### Umbenennen
Mit [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) lassen sich Spalten- oder Indexnamen anpassen. `rename()` akzeptiert verschiedene Eingabeformen; am bequemsten ist meist ein Python‑Dict. Beispiel: Im DataFrame `reviews` die Spalte `points` in `score` umbenennen sowie die Indexwerte `0`, `1` in `firstEntry`, `secondEntry`:

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

Spaltennamen ändert man recht häufig; Indexwerte umzubenennen ist selten und für solche Zwecke nutzt man meist – [wie zuvor gesehen](/posts/summary-of-kaggle-pandas-course-1/#mit-dem-index-arbeiten) – die Methode [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html).

Zeilen- und Spaltenachsen besitzen jeweils ein eigenes `name`‑Attribut; mit `rename_axis()` kann man diese Achsennamen setzen. Beispielsweise lässt sich die Zeilenachse `wines` und die Spaltenachse `fields` nennen:

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Datensätze kombinieren
Häufig gilt es, DataFrames oder Series zu kombinieren. Pandas bietet dafür drei zentrale Werkzeuge – vom Einfachen zum Komplexen: [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) und [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). Der Kaggle‑Kurs konzentriert sich auf `concat()` und `join()`, weil sich vieles, was mit `merge()` möglich ist, mit `join()` einfacher erledigen lässt.

`concat()` ist am einfachsten: Es hängt mehrere DataFrames/Series entlang einer Achse aneinander. Besonders nützlich, wenn die zu kombinierenden Objekte dieselben Felder (Spalten) haben. Standardmäßig wird entlang der Indexachse (Zeilen) verkettet; mit `axis=1` bzw. `axis='columns'` entlang der Spalten.

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

> Laut [Pandas‑Doku]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html)) sollte man viele Zeilen nicht in einer Schleife einzeln an einen DataFrame anhängen. Stattdessen die Zeilen in einer Liste sammeln und einmalig mit `concat()` zusammenfügen.
{: .prompt-tip }

`join()` ist etwas komplexer: Es hängt einen DataFrame anhand des Index an einen anderen an. Falls Spaltennamen kollidieren, müssen mit den Parametern `lsuffix` und `rsuffix` Suffixe angegeben werden, die an die jeweiligen Spaltennamen angehängt werden.

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
