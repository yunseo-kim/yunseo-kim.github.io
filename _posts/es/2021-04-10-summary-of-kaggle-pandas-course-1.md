---
title: "Resumen del curso 'Pandas' de Kaggle (1) - Lecciones 1–3"
description: "Resumen práctico del uso de la librería Pandas para limpiar y transformar datos. Sintetizamos y, cuando conviene, ampliamos el curso abierto de Kaggle. Esta entrada cubre las lecciones 1–3."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Aquí recopilo lo estudiado a través del curso de [Pandas](https://www.kaggle.com/learn/pandas) de Kaggle.  
Como la extensión es considerable, lo he separado en 2 partes.
- Parte 1: Lecciones 1–3 (este artículo)
- [Parte 2: Lecciones 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Certificate of Completion](/assets/img/kaggle-pandas/certificate.png)

## Lección 1. Creación, lectura y escritura
### Importar pandas

```python
import pandas as pd
```

En pandas hay dos objetos fundamentales: **DataFrame** y **Series**.

### DataFrame
Un [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) puede verse como una tabla o una [matriz](/posts/vector-spaces-subspaces-and-matrices/#matrices-y-espacio-de-matrices). Está compuesto por una matriz de *entradas* independientes, donde cada entrada tiene un *valor* y corresponde a una *fila* o *registro* y a una *columna*.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

Las entradas de un DataFrame no tienen por qué ser numéricas; por ejemplo, este DataFrame contiene cadenas (reseñas de usuarios):

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

Para crear un DataFrame se usa el constructor `pd.DataFrame()` y se declara con la sintaxis de diccionario de Python: la clave es el nombre de la columna y el valor es una lista con los elementos de esa columna. Es el método estándar para declarar un DataFrame nuevo.

Al declarar un DataFrame, puedes especificar etiquetas de columnas; si no especificas etiquetas de filas, se asignan enteros 0, 1, 2, ... Puedes establecer manualmente las etiquetas de fila cuando lo necesites. La lista de etiquetas de fila se llama [**índice**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html) y se puede fijar con el parámetro `index` del constructor.

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
Una [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) es una secuencia de valores, o un [vector](/posts/vector-spaces-subspaces-and-matrices/#vectores-fila-y-columna).

```python
pd.Series([1, 2, 3, 4, 5])
```

Una Series es, en esencia, equivalente a una única columna de un DataFrame. Puedes asignarle igualmente un [índice](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html), y en lugar de “nombre de columna” tiene simplemente un “nombre” ([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series y DataFrame están estrechamente relacionados; puedes pensar en un DataFrame como un conjunto de Series.

### Leer archivos de datos
En muchos casos no crearemos los datos a mano, sino que cargaremos datos existentes. Los datos pueden almacenarse en muchos formatos; el más básico es CSV. Un CSV suele verse así:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

Es decir, un CSV es una tabla con valores separados por comas (Comma-Separated Values, CSV).

Para cargar un CSV en un DataFrame se usa [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

Con la propiedad [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) puedes ver la forma del DataFrame.

```python
product_reviews.shape
```

```
(129971, 14)
```

La salida anterior indica que el DataFrame tiene 129971 registros y 14 columnas.

Con el método [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) ves las primeras cinco filas.

```python
product_reviews.head()
```

[La función `pd.read_csv()` tiene más de 30 parámetros](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Por ejemplo, si el CSV ya contiene un índice, puedes usar el parámetro `index_col` para indicar qué columna debe usarse como índice en lugar de que pandas cree uno automáticamente.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Escribir archivos de datos
Con el método [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) puedes exportar un DataFrame a un archivo CSV. Por ejemplo:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lección 2. Indexación, selección y asignación
Seleccionar valores concretos en un DataFrame o una Series es un paso casi universal en el procesamiento de datos; conviene aprender a seleccionar rápidamente los puntos de datos que necesitas.

### Accesos nativos de Python
Los objetos nativos de Python ofrecen buenas formas de indexación, y pandas adopta esos mismos métodos.

#### Atributos del objeto
En Python, accedemos al valor de un atributo de un objeto con su nombre. Si `example_obj` tiene el atributo `title`, lo llamamos como `example_obj.title`. Podemos hacer lo mismo con las columnas de un DataFrame de pandas:

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

#### Indexación de diccionarios
El tipo diccionario de Python permite acceder a sus valores con el operador de indexación (`[]`). Igual con las columnas de un DataFrame:

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

Ambos métodos son válidos, pero la indexación estilo diccionario permite manejar nombres de columnas con caracteres especiales como el espacio en blanco (p. ej., `reviews['country providence']` es posible, mientras que `reviews.country providence` no lo es).

Dentro de la Series resultante, puedes volver a usar `[]` para leer valores individuales:

```python
reviews['country'][0]
```

```
'Italy'
```

### Accesos propios de pandas
Además de los métodos anteriores, pandas ofrece dos accesores específicos: [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) y [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Selección basada en índice
Con `iloc` haces **selección basada en índice**: eliges por posición (enteros).

Por ejemplo, para seleccionar la primera fila del DataFrame:

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

A diferencia del estilo Python nativo (columna primero y luego fila), `iloc` selecciona primero filas y luego columnas. Para la primera columna:

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

En el ejemplo anterior, `:` selecciona todas las filas y luego tomamos la primera columna. Para seleccionar la segunda (`1`) y tercera (`2`) fila de la primera columna:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

O pasando una lista:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

También puedes usar índices negativos para contar desde el final. Por ejemplo, las últimas 5 filas:

```python
reviews.iloc[-5:]
```

#### Selección basada en etiqueta
Con `loc` haces **selección basada en etiqueta**: eliges por el valor del índice.

Por ejemplo, para obtener la entrada de la fila con índice 0 y la columna 'country':

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignora los valores del índice y trata el dataset como una gran matriz; `loc` utiliza la información del índice. Dado que el índice suele contener información significativa, `loc` suele ser más intuitivo.

#### Diferencias en los rangos de `iloc` y `loc`
`iloc` sigue la convención estándar de Python: `0:10` significa 0 inclusivo y 10 exclusivo, es decir, `0,...,9`.

`loc` interpreta los rangos como cerrados: `0:10` significa de 0 a 10 inclusive, `0,...,10`.

La razón es que `loc` admite índices de cualquier tipo estándar, no solo enteros. Por ejemplo, si el índice es alfabético y quieres seleccionar de 'Apples' a 'Potatoes', resulta más natural escribir `df.loc['Apples':'Potatoes']` que calcular manualmente el límite superior exclusivo.

Por lo demás, su comportamiento es similar.

> En datasets con índices enteros ordenados ascendentemente, cuando necesito rangos con `:`, prefiero `iloc` para evitar confusiones por la diferencia de inclusividad; en otros casos, `loc` me resulta más intuitivo.
{: .prompt-tip }

### Manipular el índice
Puedes ajustar el índice según convenga. Con [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) puedes establecer una columna como nuevo índice:

```python
reviews.set_index("title")
```

### Selección condicional
Hasta ahora hemos usado propiedades estructurales del DataFrame para seleccionar datos. También podemos filtrar por condiciones más complejas.

Por ejemplo, en un DataFrame con información de vinos, supongamos que queremos los vinos italianos con puntuación ≥ 90.

```python
reviews.country == 'Italy'
```

La condición devuelve una Series booleana de `True`/`False`:

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` es basado en etiquetas, pero también acepta arrays booleanos o Series booleanas alineables](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). Por tanto, podemos seleccionar solo vinos de Italia:

```python
reviews.loc[reviews.country == 'Italy']
```

Puedes combinar varias condiciones con `&` u `|`. Para vinos de Italia **y** con puntuación ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Para vinos de Italia **o** con puntuación ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas incluye selectores condicionales muy útiles como `isin` e `isnull`/`notnull`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) devuelve una máscara booleana que indica si el valor está “en” una lista dada. Por ejemplo, para seleccionar vinos de Italia o Francia:

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) sirven para filtrar valores faltantes (`NaN`). Por ejemplo, para quedarnos solo con vinos cuyo precio no está ausente:

```python
reviews.loc[reviews.price.notna()]
```

> Nota: aunque no aparece en el curso de Kaggle, [`iloc` también acepta arrays booleanos](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). A diferencia de `loc`, solo admite arrays y no Series, por lo que su uso en composiciones como las anteriores es más limitado.
{: .prompt-tip }

### Asignación de datos
Puedes crear o sobrescribir columnas en un DataFrame.

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

## Lección 3. Funciones de resumen y maps
### Visión general de los datos
El método [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) ofrece un resumen de alto nivel de una columna dada.

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

La salida de `describe()` depende del tipo. Para datos de texto, devuelve:

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

También puedes obtener estadísticas puntuales:

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

Para contar apariciones de cada valor único en un DataFrame, usa [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

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

### Mapeos (Maps)
Un **mapeo (map)** es un término tomado de las matemáticas que significa una función que asocia un conjunto con otro. En ciencia de datos, a menudo transformamos datos a otra representación; para ello usamos mapeos, que son fundamentales.

Los dos métodos más usados son:

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) recibe una función que transforma un <u>valor</u> en otro valor y la aplica a todos los valores de la <u>Series</u>, devolviendo una Series nueva. Por ejemplo, para restar la media a todas las puntuaciones:

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) aplica una función personalizada a cada <u>fila</u>, transformando el <u>DataFrame</u> completo.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Con `axis='index'`, `apply()` aplica la función a cada columna en lugar de a cada fila.

Tanto `Series.map()` como `DataFrame.apply()` devuelven un objeto nuevo (transformado) y no modifican los datos originales.

| Método | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Ámbito | Series | DataFrame |
| Unidad de aplicación | Valor a valor <br>(si consideras la Series como [vector columna](/posts/vector-spaces-subspaces-and-matrices/#vectores-fila-y-columna), se aplica por filas) | Por filas por defecto <br> Con opción para aplicar por columnas |

> Nota: también existen [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) y [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html).
> - `Series.apply()`:
>   - `by_row='compat'` (valor por defecto): funciona como `Series.map()`
>   - `by_row=False`: pasa la Series completa a la función (similar a `DataFrame.apply()` con `axis='index'`)
> - `DataFrame.map()`: aplica función a cada valor del DataFrame (análogo a `Series.map()`, pero a nivel de DataFrame)
{: .prompt-tip }

De hecho, pandas admite de forma nativa muchas operaciones típicas de mapeo. El ejemplo anterior puede escribirse de forma mucho más simple, y pandas entenderá la intención:

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

Además, pandas permite operaciones entre Series de la misma longitud. En el ejemplo de vinos, podemos concatenar país y región como cadenas:

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

Estas operaciones usan optimizaciones internas, por lo que suelen ser más rápidas que `map()` o `apply()`. Aun así, `map()` y `apply()` son más flexibles y permiten tareas más complejas; conviene conocerlos.
