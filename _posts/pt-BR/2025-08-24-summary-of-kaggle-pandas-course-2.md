---
title: "Resumo do curso 'Pandas' do Kaggle (2) - Lições 4–6"
description: "Resumo do uso do Pandas para limpar e transformar dados. Síntese do curso 'Pandas' do Kaggle, com complementos. Parte 2: Lições 4–6 — groupby, ordenação, dtypes/NaN e joins."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Aqui organizo o que estudei por meio do curso [Pandas](https://www.kaggle.com/learn/pandas) do Kaggle.  
Como o conteúdo é extenso, dividi em 2 partes.
- [Parte 1: Lições 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- Parte 2: Lições 4–6 (este post)

![Certificado de Conclusão](/assets/img/kaggle-pandas/certificate.png)

## Lesson 4. Grouping and Sorting
Às vezes, é preciso agrupar dados e aplicar operações por grupo ou ordená-los por algum critério.

### Análise por grupo
Com o método [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html), podemos agrupar registros cujos valores em determinada coluna sejam iguais e, em seguida, obter visões gerais ou aplicar transformações por grupo.

Vimos antes o [método `value_counts()`](/posts/summary-of-kaggle-pandas-course-1/#visão-geral-dos-dados); o mesmo comportamento pode ser implementado com `groupby()` assim:

```python
reviews.groupby('taster_name').size()
```

1. Agrupa o DataFrame `reviews` por valores iguais na coluna `taster_name`
2. Retorna uma Series com o tamanho (número de registros) de cada grupo

Ou então:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. Agrupa o DataFrame `reviews` por valores iguais na coluna `taster_name`
2. Em cada grupo, seleciona a coluna `taster_name`
3. Retorna uma Series com a contagem de valores não nulos

Ou seja, o método `value_counts()` é um atalho para a lógica acima. Além de [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html), podemos usar qualquer função de resumo. Por exemplo, para obter o menor preço por nota:

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

1. Agrupa o DataFrame `reviews` por valores iguais na coluna `points`
2. Em cada grupo, seleciona a coluna `price`
3. Retorna uma Series com o valor mínimo em cada grupo

Também é possível agrupar por mais de uma coluna. Para selecionar, por país e estado/província, apenas o vinho com maior nota:

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Outro método útil do objeto DataFrameGroupBy é [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html), que permite aplicar várias funções ao mesmo tempo em cada grupo.

> Como argumento, podem ser passados:
> - uma função
> - uma string com o nome da função
> - uma lista de funções ou de nomes de função
> - um dicionário cujo rótulo do eixo é a chave e a(s) função(ões) a aplicar nesse eixo é o valor
>
> A função deve:
> - aceitar um DataFrame como entrada ou
> - ser utilizável como argumento de [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html), [visto anteriormente](/posts/summary-of-kaggle-pandas-course-1/#mapeamentos-maps)
>
> Esta explicação não consta no curso original do Kaggle; foi complementada a partir da documentação oficial do pandas.
{: .prompt-tip }

Exemplo: estatísticas de preço por país.

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> Aqui, `len` é a função nativa do Python [`len()`](https://docs.python.org/3/library/functions.html#len). No exemplo, foi usada para retornar a contagem de registros de preço (`price`) por agrupamento (`country`), <u>incluindo valores ausentes</u>. Como `len` aceita DataFrames/Series, seu uso é válido nesse contexto.
>
> Já o método [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) do pandas retorna a contagem de <u>valores não nulos</u>, o que difere do comportamento acima.
>
> Esta nota também não está no curso original; foi complementada com base na documentação oficial de Python e pandas.
{: .prompt-tip }

### Índice múltiplo

Ao usar `groupby()` em transformações/análises, muitas vezes obtemos DataFrames com índice em múltiplos níveis (MultiIndex), em vez de rótulos simples.

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

Um MultiIndex tem métodos próprios para lidar com hierarquia, inexistentes em índices simples. Veja a seção MultiIndex / advanced indexing no [User Guide do pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html) para exemplos e diretrizes detalhadas.

O método mais usado no dia a dia é [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html), para voltar a um índice “plano”.

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

### Ordenação

Observando `countries_reviewed`, percebemos que o resultado do agrupamento vem ordenado pelo índice. Ou seja, a ordem das linhas do `groupby` é determinada pelos valores do índice, não pelo conteúdo dos dados.

Se necessário, podemos ordenar manualmente de outra forma. O método [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) é conveniente. Por exemplo, para ordenar país e estado pelo número de registros (“len”) em ordem crescente:

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

`sort_values()` usa ordem crescente por padrão, mas podemos inverter com `ascending=False`:

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

Para ordenar pelo índice, use [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html). Ele tem os mesmos parâmetros e ordem padrão de classificação que `sort_values()`.

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

Por fim, é possível ordenar de uma só vez por mais de uma coluna:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lesson 5. Data Types and Missing Values

Na prática, os dados raramente chegam perfeitamente limpos. Muitas vezes é preciso converter tipos, e lidar com valores ausentes no meio do caminho é a parte mais trabalhosa do pipeline de análise.

### Tipos de dados

O tipo de uma coluna (ou de uma Series) em um DataFrame é o **dtype**. A propriedade `dtype` permite inspecionar o tipo de uma coluna. Exemplo: verificar o `dtype` da coluna `price` do DataFrame `reviews`.

```python
reviews.price.dtype
```

```
dtype('float64')
```

Também podemos inspecionar os tipos de todas as colunas de uma vez, via `dtypes`:

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

O `dtype` indica como o pandas armazena internamente os dados. `float64` é ponto flutuante de 64 bits; `int64` é inteiro de 64 bits.

Uma particularidade: colunas de strings não têm um tipo próprio, sendo tratadas como objetos (`object`).

Com [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html), podemos converter o tipo de uma coluna. Por exemplo, converter a coluna `points` (antes `int64`) para `float64`:

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

O índice de um DataFrame/Series também tem tipo:

```python
reviews.index.dtype
```

```
dtype('int64')
```

O pandas também oferece suporte a tipos externos, como dados categóricos e séries temporais.

### Valores ausentes

Entradas vazias são representadas por `NaN` (de “Not a Number”). Por razões técnicas, `NaN` tem sempre tipo `float64`.

O pandas fornece funções específicas para ausência de dados. [Já vimos algo semelhante](/posts/summary-of-kaggle-pandas-course-1/#seleção-condicional): existem as funções independentes [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) e [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). Elas retornam um booleano (ou array booleano) indicando se a entrada é ausente (ou não) e podem ser usadas assim:

```python
reviews[pd.isna(reviews.country)]
```

Geralmente, verificamos se há ausências e, caso haja, definimos uma estratégia para preenchê-las. Com [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html), substituímos `NaN` por um valor conveniente. Exemplo: trocar todos os `NaN` de `reviews.region_2` por `"Unknown"`:

```python
reviews.region_2.fillna("Unknown")
```

Outra estratégia é copiar o valor válido mais próximo antes (forward fill) ou depois (backward fill). Use [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) e [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html).

> Antigamente, podia-se usar `fillna()` com o parâmetro `method='ffill'`/`'bfill'`. Desde o pandas 2.1.0, essa forma foi depreciada; prefira `ffill()`/`bfill()` conforme o caso.
{: .prompt-danger }

Em outras situações, mesmo não sendo ausências, pode ser necessário substituir valores em massa. No curso do Kaggle, o exemplo é a troca do handle do Twitter de um revisor. Um exemplo mais próximo da realidade brasileira: imagine que o norte da província de Gyeonggi, na Coreia do Sul, foi separado para formar a nova unidade administrativa **Gyeonggibuk-do**; existe um dataset com esse nome, mas alguém decide renomeá-la para **Pyeonghwanuri Special Self-Governing Province** e consegue emplacar essa ideia. ~~É um cenário hipotético, mas assusta pensar que algo parecido quase aconteceu.~~ Para refletir essa mudança no dataset, teríamos que substituir `"Gyeonggibuk-do"` por `"Pyeonghwanuri State"` ou `"Pyeonghwanuri Special Self-Governing Province"`. Uma forma de fazer isso no pandas é com [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html):

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

Com o código acima, trocamos eficientemente todas as ocorrências de `"Gyeonggibuk-do"` na coluna `province` do dataset `rok_2030_census` por “aquele nome comprido”. ~~Reconforta saber que ninguém precisou realmente rodar um código desses.~~

Substituições de strings também são úteis na limpeza de ausências quando elas aparecem como textos como `"Unknown"`, `"Undisclosed"`, `"Invalid"`, em vez de `NaN`. Em fluxos que digitalizam documentos antigos via OCR, isso é até mais comum.

## Lesson 6. Renaming and Combining

Às vezes, precisamos renomear colunas ou o índice de um dataset. Também é comum combinar DataFrames e Series.

### Renomeando

Com [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html), renomeamos colunas ou o índice. Embora aceite formatos variados, o mais prático costuma ser um dicionário Python. Exemplos: renomear a coluna `points` para `score` e, no índice, trocar `0`, `1` por `firstEntry`, `secondEntry`:

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

Renomear colunas é comum; renomear valores do índice, nem tanto. Para esse fim, geralmente é mais conveniente usar [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html), como [vimos antes](/posts/summary-of-kaggle-pandas-course-1/#manipulando-o-índice).

As dimensões de linhas e colunas também têm a propriedade `name`. Com `rename_axis()`, podemos nomear esses eixos. Ex.: chamar o eixo do índice de `wines` e o das colunas de `fields`:

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Combinando datasets

Com frequência, é preciso combinar DataFrames ou Series. O pandas oferece três funções principais, em ordem crescente de complexidade: [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) e [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). O curso do Kaggle observa que a maior parte do que se faz com `merge()` pode ser feita de modo mais simples com `join()`, então foca nos dois primeiros.

`concat()` é a mais simples: concatena DataFrames/Series ao longo de um eixo. É útil quando todos têm as mesmas colunas. Por padrão, concatena ao longo do eixo do índice; com `axis=1` ou `axis='columns'`, concatena por colunas.

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

> De acordo com a [documentação oficial do pandas]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html)), ao construir um DataFrame a partir de várias linhas, evite adicionar uma a uma dentro de um loop. Em vez disso, junte as linhas em uma lista e faça uma única chamada a `concat()`.
{: .prompt-tip }

`join()` é um pouco mais complexo: ele “anexa” um DataFrame a outro, alinhando pelo índice. Se houver nomes de colunas em conflito, use os parâmetros `lsuffix` e `rsuffix` para definir sufixos distintos e evitar colisões.

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
