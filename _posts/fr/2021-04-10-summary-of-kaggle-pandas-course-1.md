---
title: "Résumé du cours « Pandas » de Kaggle (1) – Leçons 1‑3"
description: "Résumé du cours Kaggle « Pandas »: créer/lire/écrire des données, indexer et sélectionner, fonctions de synthèse et maps. Leçons 1–3, avec compléments pratiques."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Je regroupe ici mes notes issues du cours [Pandas](https://www.kaggle.com/learn/pandas) de Kaggle.  
Le volume étant conséquent, j’ai scindé l’article en deux parties.
- Partie 1 : Leçons 1–3 (billet actuel)
- [Partie 2 : Leçons 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Certificat d’achèvement](/assets/img/kaggle-pandas/certificate.png)

## Lesson 1. Creating, Reading and Writing
### Importer pandas

```python
import pandas as pd
```

Pandas expose deux objets centraux, les **DataFrame** et les **Series**.

### DataFrame
Un [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) peut être vu comme un tableau ou une [matrice](/posts/vector-spaces-subspaces-and-matrices/#matrices-et-espace-des-matrices). Il s’agit d’une matrice composée d’*entrées (entries)* indépendantes, où chaque entrée a une *valeur (value)* et correspond à une *ligne (row)* ou *enregistrement (record)* ainsi qu’à une *colonne (column)*.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

Les entrées d’un DataFrame n’ont pas besoin d’être numériques; ci‑dessous un exemple avec des valeurs textuelles (des avis d’utilisateurs).

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

On crée un DataFrame avec le constructeur `pd.DataFrame()`, en utilisant la syntaxe du dictionnaire Python: la clé est le nom de colonne et la valeur est une liste d’éléments. C’est la manière standard d’instancier un nouveau DataFrame.

Lors de la création, on fournit des étiquettes de colonnes (noms de colonnes). Si l’on ne fournit pas d’étiquettes de lignes, pandas affecte 0, 1, 2, … par défaut. On peut les définir manuellement si besoin. La liste des étiquettes de lignes s’appelle l’[**index**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html); on le fournit via le paramètre `index` du constructeur.

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
Une [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) est une suite (sequence) de valeurs, ou encore un [vecteur](/posts/vector-spaces-subspaces-and-matrices/#vecteurs-ligne-et-vecteurs-colonne).

```python
pd.Series([1, 2, 3, 4, 5])
```

Une Series est essentiellement une seule colonne d’un DataFrame. On peut donc lui attribuer un [index](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html) ; elle a un simple *nom* ([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)) au lieu d’un « nom de colonne ».

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series et DataFrame sont étroitement liés: on peut voir un DataFrame comme un regroupement de Series.

### Lire des fichiers de données
Le plus souvent, on importe des données existantes au lieu de les saisir à la main. Le format le plus basique est le CSV. Un fichier CSV ressemble à ceci:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

Chaque valeur est séparée par une virgule (Comma-Separated Values, CSV).

Pour charger un CSV en DataFrame, utilisez [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

La propriété [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) donne la forme du DataFrame.

```python
product_reviews.shape
```

```
(129971, 14)
```

Ici, le DataFrame contient 129971 enregistrements et 14 colonnes.

La méthode [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) affiche les cinq premières lignes.

```python
product_reviews.head()
```

[`pd.read_csv()` accepte plus de 30 paramètres](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Par exemple, si le CSV contient déjà une colonne d’index, on peut la réutiliser via `index_col` au lieu de laisser pandas créer un index numérique.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Écrire des fichiers de données
Avec [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html), on peut exporter un DataFrame en CSV, par exemple:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lesson 2. Indexing, Selecting & Assigning
Sélectionner des valeurs spécifiques dans un DataFrame ou une Series est une étape quasi incontournable de tout traitement de données; il est donc crucial de savoir le faire rapidement et efficacement.

### Accesseurs natifs de Python
Les objets Python offrent de bons mécanismes d’indexation, que pandas reprend.

#### Attributs d’objet
En Python, on accède à la valeur d’un attribut via son nom. Si l’objet `example_obj` possède un attribut `title`, on l’appelle par `example_obj.title`. On peut faire de même avec les colonnes d’un DataFrame pandas.

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

#### Indexation de dictionnaire
Les dictionnaires Python s’indexent avec l’opérateur `[]`. Les colonnes d’un DataFrame s’obtiennent de la même manière.

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

Les deux approches sont valides, mais l’indexation type dictionnaire gère aussi les noms de colonnes contenant des espaces ou d’autres caractères spéciaux (par ex. `reviews['country providence']` fonctionne, alors que `reviews.country providence` ne fonctionne pas).

On peut ensuite réappliquer `[]` sur la Series obtenue pour lire une valeur individuelle.

```python
reviews['country'][0]
```

```
'Italy'
```

### Accesseurs spécifiques à pandas
Outre les accesseurs compatibles avec l’écosystème Python, pandas fournit ses propres accesseurs, [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) et [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Sélection basée sur les indices
`iloc` réalise une **sélection basée sur l’index numérique (index-based selection)**: on sélectionne par position entière.

Par exemple, pour la première ligne du DataFrame:

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

Contrairement aux approches « natives » qui sélectionnent d’abord les colonnes puis les lignes, `iloc` sélectionne d’abord les lignes puis les colonnes. La première colonne se sélectionne ainsi:

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

Ici `:` signifie « toutes les lignes », puis on prend la première colonne. Pour ne prendre que les deuxième (`1`) et troisième (`2`) lignes de la première colonne:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

On peut aussi fournir une liste d’indices:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Les indices négatifs permettent de partir de la fin; ci‑dessous, les 5 dernières lignes:

```python
reviews.iloc[-5:]
```

#### Sélection basée sur les étiquettes
Avec `loc`, on fait une **sélection basée sur les étiquettes (label-based selection)**: on sélectionne par valeur d’index.

Par exemple, pour l’entrée de la ligne d’index 0 et de la colonne ‘country’:

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignore les valeurs d’index de l’objet et raisonne comme sur une grande matrice en se basant sur les positions. `loc` s’appuie au contraire sur les valeurs d’index, souvent porteuses d’information, ce qui en fait un choix plus intuitif dans bien des cas.

#### Différences de tranchage entre `iloc` et `loc`
`iloc` suit la convention Python standard: `0:10` signifie l’intervalle demi‑ouvert 0 inclus, 10 exclu, soit `0,...,9`.

`loc` considère les tranches comme fermées: `0:10` signifie « de 0 à 10 inclus », soit `0,...,10`.

Cette différence existe parce que `loc` accepte tout type standard comme indice, pas seulement les entiers. Par exemple, pour des indices lexicographiques `Apples, ..., Potatoes, ...`, sélectionner de 'Apples' à 'Potatoes' s’écrit naturellement `df.loc['Apples':'Potatoes']` plutôt que `df.loc['Apples':'Potatoet']`. Pour des indices non entiers, ce comportement est généralement plus intuitif.

Hormis cela, le fonctionnement est similaire.

> Personnellement, avec un index d’entiers triés par ordre croissant et un tranchage `:`, j’utilise `iloc` pour éviter la confusion sur les bornes; sinon, je privilégie `loc`, souvent plus intuitif.
{: .prompt-tip }

### Manipuler l’index
On peut ajuster l’index au besoin. Par exemple, avec [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html), on peut définir une colonne comme nouvel index:

```python
reviews.set_index("title")
```

### Sélection conditionnelle
Au‑delà des aspects structurels, on peut sélectionner les lignes vérifiant des conditions logiques.

Supposons un DataFrame d’informations sur des vins et que l’on veuille les vins italiens notés au moins 90.

```python
reviews.country == 'Italy'
```

Cette condition renvoie une Series booléenne `True`/`False`.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` est label‑based, mais accepte aussi un masque booléen (array ou Series triable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). On peut donc sélectionner les vins italiens ainsi:

```python
reviews.loc[reviews.country == 'Italy']
```

On combine plusieurs conditions avec `&` (ET) ou `|` (OU). Vins italiens ET note ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Vins italiens OU note ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas fournit aussi des sélecteurs intégrés, notamment `isin` et `isna`/`notna`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) renvoie un masque indiquant si la valeur « est dans » une liste donnée. Par exemple, vins italiens ou français:

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) servent à filtrer selon la présence d’une valeur manquante (`NaN`). Par exemple, ne garder que les vins dont le prix n’est pas manquant:

```python
reviews.loc[reviews.price.notna()]
```

> À noter (non mentionné dans le cours Kaggle): [`iloc` accepte aussi des tableaux booléens](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Contrairement à `loc`, il ne prend pas les Series booléennes (seulement les arrays), ce qui limite ce type d’usage.
{: .prompt-tip }

### Affectation de données
On peut créer ou écraser des colonnes.

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

## Lesson 3. Summary Functions and Maps
### Obtenir un aperçu des données
La méthode [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) fournit un résumé de haut niveau pour une colonne donnée.

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

La sortie dépend du type de données. Pour une colonne de chaînes:

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

On peut aussi demander des statistiques ciblées:

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

Pour compter les occurrences de chaque valeur unique dans une colonne, utilisez [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

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

### Applications (maps)
Une **application (map)** est, en mathématiques, une fonction qui associe les éléments d’un ensemble à ceux d’un autre. En data science, on transforme souvent les données vers d’autres représentations; ces opérations sont cruciales.

Deux méthodes sont particulièrement utilisées.

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) prend une fonction transformant une <u>valeur</u> en une autre, l’applique à toutes les valeurs de la <u>Series</u> et renvoie la nouvelle Series. Par exemple, soustraire la moyenne aux notes de vin:

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) applique une fonction personnalisée à chaque <u>ligne</u> (ou, avec une option, à chaque <u>colonne</u>) du <u>DataFrame</u>.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Avec `axis='index'`, `apply()` applique la fonction colonne par colonne.

`Series.map()` et `DataFrame.apply()` renvoient respectivement une nouvelle Series et un nouveau DataFrame; ils ne modifient pas les données d’origine.

| Méthode | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Cible | Series | DataFrame |
| Granularité d’application | Par valeur <br>(si l’on voit la Series comme un [vecteur colonne](/posts/vector-spaces-subspaces-and-matrices/#vecteurs-ligne-et-vecteurs-colonne), c’est « par ligne ») | Par défaut par ligne <br> Option possible par colonne |

> À noter qu’il existe aussi [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) et [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html).
> - `Series.apply()`:
>   - `by_row='compat'` (par défaut): se comporte comme `Series.map()`
>   - `by_row=False`: passe la Series entière à la fonction (analogue à `DataFrame.apply()` avec `axis='index'`)
> - `DataFrame.map()`: applique la fonction à chaque valeur du DataFrame (analogue à `Series.map()`, mais sur un DataFrame)
{: .prompt-tip }

Pandas fournit de nombreuses vectorisations usuelles. L’exemple précédent s’écrit bien plus simplement, pandas interprétant correctement l’intention:

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

Pandas prend aussi en charge les opérations entre Series de même longueur. Dans l’exemple des vins, on peut concaténer les chaînes « pays – région »:

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

Ces opérations vectorisées, accélérées par pandas, sont plus rapides que `map()` ou `apply()` et couvrent tous les opérateurs Python standards (`>`, `<`, `==`, etc.). Cela dit, `map()` et `apply()` restent plus flexibles pour des transformations complexes et valent la peine d’être connues.
