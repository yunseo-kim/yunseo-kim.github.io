---
title: "Resumo do curso 'Pandas' do Kaggle (1) - Lições 1–3"
description: "Resumo prático do uso do Pandas para limpeza e manipulação de dados. Sintetiza o curso aberto 'Pandas' do Kaggle, com complementos quando necessário. Este post cobre as Lições 1–3."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Aqui organizo o que estudei por meio do curso [Pandas](https://www.kaggle.com/learn/pandas) do Kaggle.  
Como o conteúdo é extenso, dividi em 2 partes.
- Parte 1: Lições 1–3 (este post)
- [Parte 2: Lições 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Certificado de Conclusão](/assets/img/kaggle-pandas/certificate.png)

## Lesson 1. Creating, Reading and Writing
### Importando o pandas

```python
import pandas as pd
```

No pandas há dois objetos centrais: **DataFrame** e **Series**.

### DataFrame
[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) pode ser visto como uma tabela ou uma [matriz](/posts/vector-spaces-subspaces-and-matrices/#matrizes-e-espaço-de-matrizes). É composto por uma grade de *entradas* independentes; cada entrada possui um *valor*, correspondendo a uma *linha* (ou *registro*) e a uma *coluna*.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

As entradas de um DataFrame não precisam ser numéricas; abaixo um exemplo com strings (avaliações de usuários):

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

Para criar um DataFrame, usa-se o construtor `pd.DataFrame()` e a sintaxe de dicionário em Python: chaves são os nomes das colunas, valores são listas com os itens a registrar. Esse é o método padrão para declarar um novo DataFrame.

Ao declarar um DataFrame, nomeamos as colunas; já as linhas, se não forem especificadas, recebem rótulos inteiros 0, 1, 2, ... . Se necessário, podemos rotular as linhas manualmente. A lista de rótulos de linha é o [**índice**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html), e pode ser definido pelo parâmetro `index` do construtor.

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
[Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) é uma sequência de valores, ou um [vetor](/posts/vector-spaces-subspaces-and-matrices/#vetores-linha-e-vetores-coluna).

```python
pd.Series([1, 2, 3, 4, 5])
```

Uma Series é essencialmente igual a uma única coluna de um DataFrame. Assim, também pode ter [índice](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html) e, em vez de “nome de coluna”, tem apenas um “nome” ([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series e DataFrame estão intimamente relacionados. É útil pensar um DataFrame como um conjunto de várias Series.

### Lendo arquivos de dados
Na maioria das vezes, em vez de digitar tudo do zero, importamos dados já existentes. Dados podem estar em vários formatos; o mais básico é o CSV. Um arquivo CSV costuma ser assim:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

Ou seja, um CSV é uma tabela cujos valores são separados por vírgulas. Daí o nome “Comma-Separated Values (CSV)”.

Para carregar um CSV em um DataFrame, usa-se [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

A propriedade [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) mostra o formato do DataFrame.

```python
product_reviews.shape
```

```
(129971, 14)
```

A saída acima indica 129971 registros e 14 colunas.

Com o método [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html), vemos as cinco primeiras linhas.

```python
product_reviews.head()
```

[A função `pd.read_csv()` tem mais de 30 parâmetros](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Por exemplo, se o CSV já tiver uma coluna de índice, podemos definir `index_col` para usá-la em vez do índice automático do pandas.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Escrevendo arquivos de dados
Com [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) podemos exportar um DataFrame para CSV. Exemplo:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lesson 2. Indexing, Selecting & Assigning
Selecionar valores específicos em um DataFrame ou Series é etapa comum em praticamente toda tarefa de processamento de dados; portanto, é essencial aprender a fazer seleções rápidas e eficientes.

### Acessores nativos do Python
Objetos nativos do Python oferecem bons mecanismos de indexação, e o pandas os suporta da mesma forma.

#### Atributos de objeto
Em Python, acessamos uma propriedade de um objeto pelo nome do atributo. Por exemplo, se `example_obj` tem o atributo `title`, chamamos `example_obj.title`. Com colunas de um DataFrame, o acesso funciona de modo análogo.

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

#### Indexação de dicionário
Para dicionários, usamos o operador de indexação (`[]`) para acessar valores. Em DataFrames, também funciona para colunas.

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

Ambas as formas são válidas; porém, a indexação estilo dicionário tem a vantagem de lidar com nomes de coluna que incluem caracteres reservados, como espaços (por exemplo, `reviews['country providence']` funciona, enquanto `reviews.country providence` não).

Dentro da Series selecionada, podemos novamente usar `[]` para ler um valor específico.

```python
reviews['country'][0]
```

```
'Italy'
```

### Acessores próprios do pandas
Além dos modos acima, o pandas oferece acessores próprios: [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) e [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Seleção baseada em índice
Com `iloc`, fazemos **seleção baseada em índice (index-based selection)**: escolhemos pela posição numérica.

Por exemplo, para pegar a primeira linha do DataFrame:

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

Diferente do acesso nativo (coluna depois linha), `iloc` seleciona primeiro linhas e depois colunas. Para pegar a primeira coluna:

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

Acima, `:` seleciona todas as linhas, e depois escolhemos a primeira coluna. Se quisermos as linhas 2ª (`1`) e 3ª (`2`) da primeira coluna:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Ou passando uma lista:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Também é possível usar índices negativos para selecionar a partir do fim. Exemplo: as últimas 5 linhas.

```python
reviews.iloc[-5:]
```

#### Seleção baseada em rótulos
Outra opção é `loc`, para **seleção baseada em rótulos (label-based selection)**. Aqui escolhemos pelos valores do índice.

Por exemplo, o elemento na linha de índice 0 e coluna 'country':

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignora os valores do índice e trata o conjunto como uma grande matriz, acessando por posição. Já `loc` utiliza a informação do índice; como geralmente há significado nos rótulos, `loc` costuma ser mais intuitivo.

#### Diferenças de fatiamento entre `iloc` e `loc`
`iloc` segue o padrão do Python: `0:10` significa intervalo semiaberto, 0 até 10 não-inclusivo, isto é, `0,...,9`.

`loc`, por sua vez, trata intervalos como fechados: `0:10` significa 0 até 10 inclusivo, ou `0,...,10`.

O motivo: `loc` aceita, além de inteiros, rótulos de qualquer tipo padrão. Suponha um índice em ordem alfabética com valores `Apples, ..., Potatoes, ...`. Se quisermos os itens de 'Apples' até 'Potatoes', é mais natural escrever `df.loc['Apples':'Potatoes']` do que ajustar para "'Apples' até antes de 'Potatoet'" (`df.loc['Apples':'Potatoet']`). Para rótulos não inteiros, a forma inclusiva costuma ser mais intuitiva; por isso `loc` a adota.

Fora isso, o funcionamento é análogo.

> Pessoalmente, em datasets com índice inteiro crescente e quando preciso fatias com `:`, prefiro `iloc` para evitar confusões com a diferença de intervalos; nos demais casos, uso o mais intuitivo `loc`.
{: .prompt-tip }

### Manipulando o índice
Também podemos ajustar o índice conforme necessário. Com [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html), por exemplo, definimos alguma coluna como novo índice:

```python
reviews.set_index("title")
```

### Seleção condicional
Até aqui usamos propriedades estruturais do DataFrame para selecionar e transformar dados. Podemos ir além e filtrar por condições arbitrárias.

Exemplo: num DataFrame com informações de vinhos, selecionar somente os italianos com nota a partir de 90.

```python
reviews.country == 'Italy'
```

A expressão acima retorna uma Series booleana, com `True`/`False`.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` é baseado em rótulos, mas também aceita arrays booleanos ou Series booleanas alinhadas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). Assim, podemos selecionar só os vinhos italianos:

```python
reviews.loc[reviews.country == 'Italy']
```

Podemos combinar múltiplas condições com `&` e `|`. Para italianos **e** com nota ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Para italianos **ou** com nota ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

O pandas também fornece seletores condicionais úteis como `isin` e `isnull`/`notnull`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) verifica se o valor “está em” uma lista e retorna uma máscara booleana. Exemplo: vinhos da Itália ou da França.

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) filtram valores ausentes (`NaN`). Exemplo: selecionar somente vinhos com preço informado.

```python
reviews.loc[reviews.price.notna()]
```

> Nota: embora não conste no curso do Kaggle, [`iloc` também aceita arrays booleanos](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Diferentemente de `loc`, porém, suporta apenas arrays (não Series), o que limita usos como os acima.
{: .prompt-tip }

### Atribuição de dados
Podemos criar ou sobrescrever dados em um DataFrame.

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
### Visão geral dos dados
O método [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) fornece um resumo de alto nível de uma coluna.

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

A saída depende do tipo dos dados. Para strings, por exemplo:

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

Também podemos obter estatísticas específicas.

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

Se quisermos as contagens de cada valor distinto, usamos [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

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

### Mapeamentos (Maps)
Em matemática, um **mapeamento (map)** é uma função que envia um conjunto em outro. Em ciência de dados, frequentemente transformamos dados para outra representação; usamos mapeamentos para isso, portanto são muito importantes.

Dois métodos são especialmente comuns.

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) recebe uma função que transforma um único <u>valor</u> em outro e a aplica a todos os valores da <u>Series</u>, retornando uma nova Series. Por exemplo, para subtrair a média das notas e obter desvios:

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) aplica uma função customizada a cada <u>linha</u>, transformando o <u>DataFrame</u> inteiro.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Com `axis='index'`, aplicamos por colunas em vez de por linhas.

`Series.map()` e `DataFrame.apply()` retornam novos objetos transformados; os dados originais permanecem inalterados.

| Método | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Alvo | Series | DataFrame |
| Unidade de aplicação | Aplica por valor <br>(se virmos a Series como um [vetor coluna](/posts/vector-spaces-subspaces-and-matrices/#vetores-linha-e-vetores-coluna), aplica por linha) | Por padrão, aplica por linha <br> com opção para aplicar por coluna |

> Observação: também existem [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) e [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html).
> - `Series.apply()`:
>   - `by_row='compat'` (padrão): funciona como `Series.map()`
>   - `by_row=False`: passa a Series inteira de uma vez para a função (análogo a `DataFrame.apply()` com `axis='index'`)
> - `DataFrame.map()`: aplica a função a cada valor do DataFrame (semelhante a `Series.map()`, mas no nível do DataFrame)
{: .prompt-tip }

Na verdade, o pandas já otimiza muitos mapeamentos comuns. O exemplo anterior pode ser escrito de forma bem mais simples, e o pandas entende a intenção:

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

Além disso, o pandas suporta operações entre Series de mesmo tamanho. No exemplo dos vinhos, podemos concatenar país e região diretamente como strings:

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

Essas operações são aceleradas internamente e costumam ser mais rápidas que `map()`/`apply()`. O pandas oferece esse comportamento para todos os operadores padrão do Python (`>`, `<`, `==`, etc.). Ainda assim, `map()` e `apply()` são mais flexíveis e permitem tarefas mais complexas, por isso vale a pena conhecê-los.
