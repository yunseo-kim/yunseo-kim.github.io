---
title: "Resumen del curso 'Pandas' de Kaggle (2) - Lecciones 4–6"
description: "Resumen práctico de pandas para limpiar y transformar datos. Sintetiza y amplía el curso abierto de Kaggle; esta segunda parte cubre las lecciones 4–6."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Recojo aquí lo estudiado a través del curso de [Pandas](https://www.kaggle.com/learn/pandas) de Kaggle.  
Como la extensión es considerable, lo separé en 2 partes.
- [Parte 1: Lecciones 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- Parte 2: Lecciones 4–6 (este artículo)

![Certificado de finalización](/assets/img/kaggle-pandas/certificate.png)

## Lección 4. Agrupar y ordenar
A veces necesitamos clasificar los datos, aplicar operaciones por grupo o reordenarlos según un criterio.

### Análisis por grupos
Con el método [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) puedes agrupar las filas cuyo valor en una columna sea igual y, después, obtener resúmenes u operar por grupo.

Antes vimos el [método `value_counts()`](/posts/summary-of-kaggle-pandas-course-1/#vision-general-de-los-datos); lo mismo puede implementarse con `groupby()` así:

```python
reviews.groupby('taster_name').size()
```

1. Agrupa el DataFrame `reviews` por filas con el mismo valor en la columna `taster_name`
2. Devuelve como Series el tamaño de cada grupo (número de filas incluidas)

O bien:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. Agrupa el DataFrame `reviews` por filas con el mismo valor en la columna `taster_name`
2. En cada grupo, selecciona la columna `taster_name`
3. Devuelve como Series el número de valores no nulos

Es decir, `value_counts()` es un atajo de operaciones como las anteriores. Además de [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html), puedes usar cualquier función de resumen de forma análoga. Por ejemplo, para ver el precio mínimo por puntuación:

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

1. Agrupa `reviews` por valores iguales en la columna `points`
2. Selecciona la columna `price` en cada grupo
3. Devuelve como Series el mínimo de cada grupo

También puedes agrupar por más de una columna. Para seleccionar, por país y provincia, el vino con la puntuación máxima:

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Otro método útil de los objetos DataFrameGroupBy es [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html). Permite ejecutar múltiples funciones a la vez sobre cada grupo.

> Como argumento puedes pasar:
> - una función
> - una cadena con el nombre de una función
> - una lista de funciones o de nombres de función
> - un diccionario que mapea etiquetas de ejes a función o lista de funciones a aplicar sobre ese eje
>
> Y dichas funciones deben:
> - aceptar un DataFrame como entrada, o
> - ser válidas como argumento de [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) [visto antes](/posts/summary-of-kaggle-pandas-course-1/#mapeos-maps).
>
> Esta aclaración no aparece en el curso original de Kaggle; la he ampliado consultando la documentación oficial de pandas.
{: .prompt-tip }

Por ejemplo, para obtener estadísticas de precio por país:

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> Aquí `len` es la función incorporada de Python [`len()`](https://docs.python.org/3/library/functions.html#len). En este ejemplo la usamos para imprimir el número de datos de precio (`price`) por cada grupo (`country`), <u>incluyendo valores nulos</u>. Como acepta DataFrame o Series como entrada, puede usarse así.
>
> El método [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) de pandas, en cambio, devuelve <u>solo el número de valores no nulos</u>, por lo que su comportamiento difiere.
>
> Esta aclaración no aparece en el curso original de Kaggle; la he ampliado consultando la documentación oficial de Python y pandas.
{: .prompt-tip }

### Índice múltiple

Al agrupar y analizar con `groupby()`, a veces obtendrás un DataFrame con índice de múltiples niveles en lugar de etiquetas simples.

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

El índice múltiple añade métodos para tratar jerarquías que no existen en el índice simple. Puedes ver ejemplos y pautas en la sección MultiIndex / advanced indexing de la [guía de usuario de pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

El método que más usarás probablemente será [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html) para volver a un índice normal:

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

### Ordenación

Si observas `countries_reviewed`, verás que el resultado del agrupado vuelve ordenado por el valor del índice. Es decir, las filas del resultado de `groupby` se ordenan por los valores del índice, no por el contenido.

Puedes ordenar manualmente según convenga con [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). Por ejemplo, para ordenar país y provincia por el número de filas ('len') en orden ascendente:

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

`sort_values()` ordena de forma ascendente por defecto; con la opción siguiente puedes ordenar en descendente:

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

Para ordenar por índice, usa [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html). Tiene los mismos argumentos y el mismo orden por defecto (descendente) que `sort_values()`.

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

Por último, puedes ordenar por varias columnas a la vez:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lección 5. Tipos de datos y valores faltantes

En la práctica, los datos rara vez vienen perfectamente limpios; a menudo hay que convertir tipos o tratar valores ausentes. En la preparación y el análisis, esta fase suele ser el mayor escollo.

### Tipos de datos

El tipo de una columna de un DataFrame o de una Series se llama **dtype**. Con el atributo `dtype` puedes ver el tipo de una columna. Por ejemplo, para ver el `dtype` de `price` en `reviews`:

```python
reviews.price.dtype
```

```
dtype('float64')
```

Con el atributo `dtypes` ves todos los tipos de las columnas a la vez:

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

El tipo indica cómo almacena internamente pandas los datos. Por ejemplo, `float64` es coma flotante de 64 bits; `int64`, entero de 64 bits.

Un detalle: las columnas de cadenas no tienen tipo propio; se consideran objetos (`object`).

Con [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) puedes convertir una columna de un tipo a otro. Por ejemplo, convertir `points` (antes `int64`) a `float64`:

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

El índice de un DataFrame o de una Series también tiene tipo:

```python
reviews.index.dtype
```

```
dtype('int64')
```

Además, pandas soporta otros tipos como categórico o series temporales.

### Valores faltantes

Las entradas vacías o sin valor reciben `NaN` (de “Not a Number”). Por razones técnicas, `NaN` es siempre de tipo `float64`.

Pandas ofrece funciones específicas para tratar valores faltantes. [Ya vimos algo parecido](/posts/summary-of-kaggle-pandas-course-1/#seleccion-condicional): además de métodos, existen las funciones independientes [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) y [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). Indican con booleanos si una entrada es (o no) faltante, y se pueden usar así:

```python
reviews[pd.isna(reviews.country)]
```

A menudo conviene detectar valores faltantes y rellenarlos adecuadamente. Con [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) puedes reemplazarlos por un valor conveniente. Por ejemplo, para sustituir todos los `NaN` de `region_2` por `"Unknown"`:

```python
reviews.region_2.fillna("Unknown")
```

También puedes usar las estrategias forward fill y backward fill, que rellenan con el valor válido más cercano anterior o posterior, con [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) y [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html), respectivamente.

> Antes podía usarse `fillna()` con el argumento `method='ffill'` o `'bfill'`, pero desde pandas 2.1.0 ese uso está en desuso (deprecated). Se recomienda usar `ffill()` o `bfill()` según corresponda.
{: .prompt-danger }

A veces, aunque no haya faltantes, hay que reemplazar sistemáticamente unos valores por otros. En el curso original de Kaggle se da el ejemplo de cambiar el handle de Twitter de un revisor; buen ejemplo, pero para un caso más cercano: supongamos que Corea del Sur crea una nueva división administrativa al norte de Gyeonggi, **경기북도**, y tenemos un dataset con ese nombre oficial. Ahora imaginemos que alguien propone, y logra imponer, renombrarlo como **평화누리특별자치도**. ~~Es hipotético, pero daba miedo que algo parecido pudiera ocurrir de verdad.~~ Para reflejarlo en el dataset habría que cambiar `"Gyeonggibuk-do"` por `"Pyeonghwanuri State"` o `"Pyeonghwanuri Special Self-Governing Province"`. Una forma de hacerlo en pandas es con [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html):

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

Con este código, en la columna `province` de `rok_2030_census` todas las instancias de `"Gyeonggibuk-do"` se reemplazan eficazmente por ‘el nombre largo’. ~~Alivia saber que nadie tuvo que ejecutar este cambio en la vida real.~~

Estos reemplazos de texto también son útiles al limpiar datos y tratar faltantes, ya que a menudo los valores ausentes aparecen como cadenas como `"Unknown"`, `"Undisclosed"` o `"Invalid"` en lugar de `NaN`. En datasets generados con OCR de documentación antigua, esto es incluso lo más habitual.

## Lección 6. Renombrar y combinar

A veces hay que cambiar nombres de columnas o del índice, y a menudo hay que combinar varios DataFrames o Series.

### Cambiar nombres

Con [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) puedes renombrar columnas o índices. Acepta varios formatos de entrada, pero lo más cómodo suele ser un diccionario de Python. Por ejemplo, para cambiar la columna `points` a `score` y renombrar los índices `0`, `1` a `firstEntry`, `secondEntry`:

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

En realidad, es más común renombrar columnas que valores del índice; y para lo segundo suele ser más práctico usar [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) [como vimos antes](/posts/summary-of-kaggle-pandas-course-1/#manipular-el-indice).

Las etiquetas del eje de filas y el de columnas tienen su propia propiedad `name`, y con `rename_axis()` puedes renombrar estos ejes. Por ejemplo, nombrar el eje de filas como `wines` y el de columnas como `fields`:

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Combinar datasets

A veces hay que unir DataFrames entre sí, o Series entre sí. Para ello, pandas ofrece tres funciones clave, de más simple a más compleja: [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) y [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). El curso de Kaggle señala que la mayoría de cosas que haces con `merge()` pueden hacerse de forma más sencilla con `join()`, por lo que se centra en las dos primeras.

`concat()` es la más simple: concatena varios DataFrames o Series a lo largo de un eje. Es útil cuando los objetos a unir comparten los mismos campos (columnas). Por defecto concatena a lo largo del eje de filas; con `axis=1` o `axis='columns'` lo hace por columnas.

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

> Según la [documentación oficial de pandas](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), si tienes que unir muchas filas en un solo DataFrame, no es recomendable añadirlas una a una dentro de un bucle; es mejor construir una lista con todas y concatenarlas de una sola vez con `concat()`.
{: .prompt-tip }

`join()` es algo más complejo: añade a un DataFrame otro DataFrame alineando por el índice. Si hay nombres de columnas duplicados, especifica sufijos con `lsuffix` y `rsuffix` para distinguirlas.

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
