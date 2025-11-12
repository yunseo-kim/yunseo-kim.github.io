---
title: "Résumé du cours « Pandas » de Kaggle (2) – Leçons 4‑6"
description: "Guide pratique de pandas pour nettoyer et transformer les données: résumé enrichi du cours « Pandas » de Kaggle. Cette seconde partie couvre les Leçons 4–6 (groupby, tri, dtypes, NaN, renommage, concat/join)."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Je regroupe ici mes notes issues du cours [Pandas](https://www.kaggle.com/learn/pandas) de Kaggle.  
Le volume étant conséquent, j’ai scindé l’article en deux parties.
- [Partie 1 : Leçons 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- Partie 2 : Leçons 4–6 (ce billet)

![Certificat d’achèvement](/assets/img/kaggle-pandas/certificate.png)

## Lesson 4. Grouping and Sorting
Il arrive souvent qu’on doive regrouper les données et appliquer des opérations par groupe, ou encore trier selon certains critères.

### Analyse par groupe
La méthode [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) regroupe les lignes partageant la même valeur dans une colonne donnée, puis permet d’inspecter ou de transformer chaque groupe.

Nous avons déjà vu la [méthode `value_counts()`](/posts/summary-of-kaggle-pandas-course-1/#obtenir-un-apercu-des-donnees). On peut reproduire un comportement équivalent avec `groupby()` comme suit:

```python
reviews.groupby('taster_name').size()
```

1. regrouper le DataFrame `reviews` par valeurs égales de la colonne `taster_name`
2. renvoyer une Series avec la taille (nombre de lignes) de chaque groupe

Ou bien:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. regrouper le DataFrame `reviews` par valeurs égales de la colonne `taster_name`
2. dans chaque groupe, sélectionner la colonne `taster_name`
3. renvoyer le nombre de valeurs non manquantes sous forme de Series

Autrement dit, `value_counts()` est un raccourci pour ce type d’opération. Outre [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html), on peut utiliser toute fonction de synthèse de la même manière. Par exemple, pour obtenir le prix minimal par note:

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

1. regrouper le DataFrame `reviews` par valeurs égales de la colonne `points`
2. dans chaque groupe, sélectionner la colonne `price`
3. renvoyer la valeur minimale sous forme de Series

On peut aussi regrouper selon plusieurs colonnes. Pour sélectionner, par pays et par province, le vin ayant la note la plus élevée:

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Une autre méthode utile des objets DataFrameGroupBy est [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html). Elle permet d’exécuter plusieurs fonctions à la fois sur chaque groupe.

> En argument, on peut passer:
> - une fonction
> - une chaîne avec le nom de la fonction
> - une liste de fonctions et/ou de noms de fonctions
> - un dictionnaire dont les clés sont des étiquettes d’axe et les valeurs des fonctions (ou listes de fonctions) à appliquer à cet axe
>
> Les fonctions doivent pouvoir:
> - accepter un DataFrame en entrée, ou
> - être passées en argument à la méthode [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) [vue plus haut](/posts/summary-of-kaggle-pandas-course-1/#applications-maps)
>
> Cet éclaircissement n’apparaît pas dans le cours Kaggle original; il est ajouté d’après la documentation officielle de pandas.
{: .prompt-tip }

Par exemple, pour calculer des statistiques de prix par pays:

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> Ici, `len` désigne la fonction Python intégrée [`len()`](https://docs.python.org/3/library/functions.html#len). Dans cet exemple, on l’utilise pour afficher le nombre de valeurs de prix (`price`) par groupe (`country`), en <u>incluant les valeurs manquantes</u>. Comme la fonction accepte DataFrame/Series en entrée, elle est applicable ici.
>
> La méthode [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) de pandas, elle, compte uniquement les <u>valeurs valides (non manquantes)</u>, d’où une différence de comportement.
>
> Cette précision, absente du cours Kaggle, s’appuie sur la documentation officielle de Python et de pandas.
{: .prompt-tip }

### Index multi-niveaux

Avec `groupby()`, on obtient parfois en sortie des DataFrame indexés par un index à plusieurs niveaux (MultiIndex) plutôt qu’un simple index plat.

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

Le MultiIndex offre des méthodes spécifiques aux structures hiérarchiques. Le guide utilisateur de pandas détaille les cas d’usage et bonnes pratiques dans la section [MultiIndex / advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

Cela dit, la méthode la plus fréquemment utilisée sera sans doute [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html) pour aplatir l’index en index simple.

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

### Tri

Si l’on observe `countries_reviewed`, on constate que le résultat d’un `groupby` est renvoyé dans l’ordre des valeurs d’index. Autrement dit, l’ordre des lignes provient des étiquettes d’index, pas du contenu.

On peut trier explicitement autrement avec [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). Par exemple, trier pays et provinces par le nombre d’entrées (‘len’) croissant:

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

Par défaut, `sort_values()` trie par ordre croissant; on peut obtenir l’ordre décroissant via:

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

Pour trier par index, utilisez [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html), avec la même interface et le même ordre par défaut (décroissant).

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

Enfin, on peut trier selon plusieurs colonnes en une fois:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lesson 5. Data Types and Missing Values

Dans la pratique, les données ne sont pas toujours bien nettoyées; il faut souvent convertir les types vers ceux attendus, et gérer des valeurs manquantes. Lors d’un traitement ou d’une analyse, c’est très souvent l’étape la plus chronophage.

### Types de données

Le type d’une colonne de DataFrame, ou d’une Series, est son **dtype**. On le consulte via l’attribut `dtype`. Exemple sur la colonne `price` de `reviews`:

```python
reviews.price.dtype
```

```
dtype('float64')
```

On peut aussi consulter d’un coup le `dtype` de toutes les colonnes via `dtypes`:

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

Le dtype indique la représentation interne utilisée par pandas. Par exemple, `float64` pour un flottant 64 bits, `int64` pour un entier 64 bits.

Point notable: une colonne purement textuelle n’a pas un type « chaîne » natif; elle est typée génériquement `object`.

Avec [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html), on convertit une colonne d’un type à un autre. Par exemple, convertir `points` (en `int64`) en `float64`:

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

L’index d’un DataFrame ou d’une Series possède lui aussi un type:

```python
reviews.index.dtype
```

```
dtype('int64')
```

Pandas gère également des types externes, comme les catégories (categorical) et les séries temporelles (datetime).

### Valeurs manquantes

Les entrées vides reçoivent la valeur `NaN` (abréviation de « Not a Number »). Pour des raisons techniques, `NaN` est toujours de type `float64`.

Pandas fournit des fonctions pour détecter les manquants. [Nous avons effleuré cela précédemment](/posts/summary-of-kaggle-pandas-course-1/#selection-conditionnelle): en plus des méthodes, il existe les fonctions autonomes [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) et [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). Elles renvoient un booléen (ou un tableau de booléens) indiquant si l’entrée est manquante ou non, et s’emploient ainsi:

```python
reviews[pd.isna(reviews.country)]
```

Souvent, il faut détecter les manquants et les imputer. Une stratégie consiste à remplacer par une valeur fixe avec [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html). Exemple: remplacer tous les `NaN` de `reviews.region_2` par `"Unknown"`:

```python
reviews.region_2.fillna("Unknown")
```

On peut aussi propager vers l’avant (forward fill) ou l’arrière (backward fill) la valeur valide la plus proche, respectivement via [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) et [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html).

> Autrefois, on pouvait utiliser `fillna()` avec le paramètre `method='ffill'`/`'bfill'`. Depuis pandas 2.1.0, cette approche est dépréciée; privilégiez `ffill()`/`bfill()` selon le besoin.
{: .prompt-danger }

Parfois, même sans manquants, il faut remplacer en masse certaines valeurs par d’autres. Le cours Kaggle illustre cela avec le changement de handle Twitter d’un critique; pour un exemple plus parlant côté coréen, imaginons ceci.

En République de Corée, on scinde le nord de la province du Gyeonggi pour créer une nouvelle entité administrative, **Gyeonggibuk-do**, et un jeu de données adopte ce nom. Quelqu’un propose ensuite, de manière farfelue, de renommer **Gyeonggibuk-do** en **Pyeonghwanuri Special Self-Governing Province** et parvient à l’imposer dans notre scénario fictif. ~~Fictif, certes, mais la ressemblance avec une situation réelle potentielle fait froid dans le dos.~~ Il faut alors remplacer dans le jeu de données la chaîne `"Gyeonggibuk-do"` par `"Pyeonghwanuri State"` ou `"Pyeonghwanuri Special Self-Governing Province"`. En pandas, une manière simple est d’utiliser [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html).

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

Ce code remplace efficacement toutes les occurrences de `"Gyeonggibuk-do"` par « le truc interminable » dans la colonne `province` du DataFrame `rok_2030_census`. ~~On se contente de soupirer de soulagement à l’idée que personne n’ait eu à exécuter ça dans la vraie vie.~~

Ce type de remplacement textuel sert aussi au nettoyage des manquants quand ceux-ci sont encodés par des chaînes comme `"Unknown"`, `"Undisclosed"`, `"Invalid"`, ce qui est courant dans des jeux construits par OCR d’anciens documents administratifs.

## Lesson 6. Renaming and Combining

Il arrive de devoir renommer une colonne ou un index, et de devoir combiner des DataFrame ou des Series.

### Renommer

La méthode [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) renomme des colonnes ou des index. Plusieurs formats d’arguments sont possibles, mais un dictionnaire Python est souvent le plus simple. Exemple: renommer la colonne `points` en `score`, et les index `0`, `1` en `firstEntry`, `secondEntry` dans `reviews`:

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

Renommer des colonnes est courant; renommer des index l’est beaucoup moins. Pour ce dernier cas, on préfère en général [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html), [comme vu précédemment](/posts/summary-of-kaggle-pandas-course-1/#manipuler-lindex).

Les axes de lignes et de colonnes possèdent un attribut `name`. Avec `rename_axis()`, on peut aussi renommer ces axes. Par exemple, appeler l’axe des lignes `wines` et celui des colonnes `fields`:

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Combiner des jeux de données

Pandas propose trois fonctions clés pour combiner des DataFrame/Series, de la plus simple à la plus riche: [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) et [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). Le cours Kaggle se concentre sur `concat()` et `join()`, la plupart des usages de `merge()` pouvant être couverts plus simplement par `join()`.

`concat()` est la plus simple: elle « colle » plusieurs DataFrame/Series le long d’un axe. Utile quand les objets à concaténer partagent les mêmes colonnes. Par défaut, la concaténation se fait sur l’axe des lignes; avec `axis=1` ou `axis='columns'`, on concatène sur l’axe des colonnes.

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

> D’après la [documentation officielle de pandas]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html)), si vous devez assembler plusieurs lignes en un seul DataFrame, évitez d’ajouter ligne par ligne dans une boucle; stockez les lignes dans une liste puis concaténez-les en une fois avec `concat()`.
{: .prompt-tip }

`join()` est plus riche: il joint un autre DataFrame sur l’index. Si des noms de colonnes se chevauchent, il faut fournir `lsuffix` et `rsuffix` pour distinguer les colonnes communes des deux DataFrame.

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
