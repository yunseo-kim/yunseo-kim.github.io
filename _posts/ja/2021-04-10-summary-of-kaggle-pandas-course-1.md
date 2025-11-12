---
title: "Kaggle「Pandas」講座の内容整理（1）- Lesson 1-3"
description: "データ整形・加工に必須のPandas活用法を体系的に整理。Kaggle公開コース「Pandas」を要約し要点を補足。本記事はLesson 1–3（作成/読み書き、選択、集約）を解説。"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Kaggleの[Pandas](https://www.kaggle.com/learn/pandas)講座で学んだ内容をここに整理します。  
分量が多いため 2 回に分けました。
- 第1編: Lesson 1-3（本文）
- [第2編: Lesson 4-6](/posts/summary-of-kaggle-pandas-course-2/)

![修了証明書](/assets/img/kaggle-pandas/certificate.png)

## Lesson 1. Creating, Reading and Writing
### Pandasの読み込み

```python
import pandas as pd
```

Pandas には**データフレーム（DataFrame）**と**シリーズ（Series）**という 2 つの中核オブジェクトがある。

### データフレーム
[データフレーム（DataFrame）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)は表、あるいは[行列](/posts/vector-spaces-subspaces-and-matrices/#行列と行列空間)と考えられる。独立した*エントリ（entries）*で構成される行列で、各エントリは特定の*値（value）*を持ち、1 つの*行（row）*または*レコード（record）*、そして 1 つの*列（column）*に対応する。

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

データフレームのエントリは必ずしも数値である必要はない。次は文字列の値（ユーザーのレビュー）を持つデータフレームの例。

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

データフレームを生成するときは `pd.DataFrame()` コンストラクタ（constructor）を使い、Python の辞書（dictionary）記法で宣言する。キー（key）に列名、値（value）に各列の項目を並べたリスト（list）を渡す。これは新しいデータフレームを宣言する標準的な方法である。

データフレーム宣言時、列ラベルには列名を指定するが、行ラベルを別途指定しない場合は 0, 1, 2, ... の整数が割り当てられる。必要に応じて行ラベルを手動で指定できる。データフレームにおける行ラベルのリストを[**インデックス（Index）**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html)と呼び、コンストラクタの `index` 引数で指定できる。

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

| | Bob | Sue |
| --- | --- | --- |
| Product A | I liked it. | Pretty good. |
| Product B | It was awful. | Bland. |

### シリーズ
[シリーズ（Series）](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)はデータ値からなる数列（sequence）、あるいは[ベクトル](/posts/vector-spaces-subspaces-and-matrices/#行ベクトルと列ベクトル)である。

```python
pd.Series([1, 2, 3, 4, 5])
```

シリーズは本質的にデータフレームの単一列と同じである。したがって同様に[インデックス](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html)を指定でき、単に「列名」の代わりに「名前」（[`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)）を持つだけである。

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

シリーズとデータフレームは密接に関連している。データフレームをシリーズの束と考えると理解しやすい。

### データファイルの読み込み
多くの場合、データは自分で作るのではなく既存のデータを取り込んで使う。データはさまざまな形式で保存されるが、最も基本的なのは CSV ファイルである。典型的な CSV の中身は次のようになる。

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

すなわち CSV は各値をカンマ（comma）で区切る表である。名前の由来は “Comma-Separated Values”、CSV だ。

CSV 形式のデータをデータフレームに読み込むには[`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)関数を使う。

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

[`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html)属性でデータフレームの形状を確認できる。

```python
product_reviews.shape
```

```
(129971, 14)
```

この出力は 129971 行、14 列を持つことを意味する。

[`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)メソッドで先頭 5 行を確認できる。

```python
product_reviews.head()
```

[ `pd.read_csv()` には 30 個を超える引数がある](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)。たとえば読み込む CSV が独自のインデックス列を含む場合、`index_col` 引数を指定して自動採番の代わりにその列をインデックスとして使える。

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### データファイルの書き出し
[`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html)メソッドでデータフレームを CSV に書き出せる。使い方は次のとおり。

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lesson 2. Indexing, Selecting & Assigning
Pandas のデータフレームやシリーズから特定の値を選ぶ操作は、ほぼすべてのデータ処理で通る工程なので、必要なデータポイントを素早く効率よく選ぶ方法を優先して身につけるべきである。

### Python標準のアクセス方法
ネイティブ Python オブジェクトは優れたデータのインデクシング手段を提供しており、Pandas もそれらを同様に提供する。

#### オブジェクト属性
Python ではオブジェクトのプロパティ（property）に属性名（attribute）でアクセスできる。たとえば `example_obj` が `title` 属性を持つなら `example_obj.title` と呼べる。Pandas データフレームの列にも同様にアクセスできる。

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

#### 辞書型のインデクシング
また Python の辞書型はインデクシング演算子（`[]`）で値にアクセスできる。Pandas データフレームの列にも同じ方法でアクセスできる。

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

属性アクセスと辞書式アクセスはいずれも有効だが、辞書式は空白のような属性名に使えない文字（例: `reviews['country providence']` は可だが `reviews.country providence` は不可）を含む列名も扱える利点がある。

取得した Pandas シリーズの中でも、さらにインデクシング演算子で個々の値にアクセスできる。

```python
reviews['country'][0]
```

```
'Italy'
```

### Pandas固有のアクセサ
上のようなインデクシングや属性アクセスは他の Python エコシステムと自然に馴染む点で優れているが、Pandas にはこれ以外に独自のアクセサである[`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)と[`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)がある。

#### インデックス（位置）ベースの選択
`iloc` では**インデックス（位置）ベースの選択（index-based selection）**を行う。データ内の位置を整数で指定して取り出す。

たとえばデータフレームの最初の行は次のように選べる。

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

ネイティブ Python の「まず列を選び、その後に行を選ぶ」流儀と異なり、`iloc` は「まず行、その後に列」を選ぶ。データフレームの最初の列は次のように選べる。

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

ここでは `:` 演算子で全行を選んだうえで、最初の列を選んでいる。最初の列のうち 2 行目（`1`）と 3 行目（`2`）だけ選びたいなら次のとおり。

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

リストを渡すこともできる。

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

負のインデックスで末尾側から選ぶことも可能。次は末尾 5 行を選ぶ例。

```python
reviews.iloc[-5:]
```

#### ラベルベースの選択
もう一つの方法は `loc` を使う**ラベルベースの選択（label-based selection）**である。位置ではなく、インデックスの値で選ぶ。

たとえばインデックス値が 0 の行の 'country' 列のエントリは次のように得られる。

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` はデータセットのインデックス値を無視して 1 つの大きな行列のようにみなし、位置に基づいてエントリにアクセスする。一方 `loc` はインデックス情報を活用して動作する。多くの場合、インデックス自体にも意味のある情報があり、`loc` のほうが `iloc` より直感的なことが多い。

#### `iloc` と `loc` のスライス範囲の違い
`iloc` は Python 標準ライブラリのインデクシング規則に従い、`0:10` は 0 以上 10 未満の半開区間、すなわち `0,...,9` を意味する。

一方 `loc` は区間を閉区間として解釈するので、`0:10` は 0 以上 10 以下、すなわち `0,...,10` を意味する。

この差がある理由は、`loc` は整数だけでなくあらゆる標準的な型をインデックスに使えるためである。たとえばインデックスが 'Apples, ..., Potatoes, ...' のような並びで、この範囲（アルファベット順）に該当する作物を選ぶとき、'Potatoes' の直後にあり得る文字列 'Potatoet' を作って「'Apples' から 'Potatoet' の手前まで」（`df.loc['Apples':'Potatoet']`）と指定するより、単に「'Apples' から 'Potatoes' まで」（`df.loc['Apples':'Potatoes']`）と書けたほうが直感的だ。整数以外の型のインデックスでは後者のほうが一般に直感的なので、`loc` はこの規則を採用している。

それ以外の動作は基本的に同じである。

> 個人的には、昇順の整数インデックスを持つデータセットで `:` による範囲指定をする場合、上記の範囲規則の違いによる混乱を避けるために `iloc` を、それ以外ではより直感的な `loc` を使うことが多い。
{: .prompt-tip }

### インデックスの操作
必要に応じてインデックスを調整できる。[`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html)を使うと、次のようにデータ内の特定の列を新しいインデックスにできる。

```python
reviews.set_index("title")
```

### 条件付き選択
ここまでの内容はデータフレーム自体の構造的な属性を使ってデータを加工・選択する方法だった。さらに踏み込んで、より複雑な条件を満たすデータだけを選ぶこともできる。

たとえばワイン製品のデータフレームから、評価が 90 点以上のイタリア産ワインだけを選ぶとしよう。

```python
reviews.country == 'Italy'
```

この条件式は `True`/`False` のブール値からなるシリーズを返す。

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[ `loc` は基本的にラベルベースだが、ブール配列やソート可能なブールシリーズも受け付ける](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)。したがって次のようにイタリア産ワインだけを選べる。

```python
reviews.loc[reviews.country == 'Italy']
```

複数条件は `&` や `|` で結合できる。イタリア産「かつ」評価が 90 点以上なら次のとおり。

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

イタリア産「または」評価が 90 点以上なら次のとおり。

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas にはいくつかの組み込み条件セレクタがあり、代表的なのが `isin` と `isnull` / `notnull` である。

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html)は、指定したリスト「の中にある（is in）」値かどうかを表すブールのマスクシリーズを返し、これでデータを選別できる。たとえばイタリア産またはフランス産のワインは次のように選べる。

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html)は欠損値（`NaN`）を持つか否かで絞り込むときに使う。たとえば価格が欠損していないワインだけ選ぶには次のとおり。

```python
reviews.loc[reviews.price.notna()]
```

> ちなみに Kaggle 講座には出てこないが、[`iloc` もブール配列（array）を受け付ける](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)。ただし `loc` と異なり配列のみ対応でシリーズは不可のため、上のような応用は難しい。
{: .prompt-tip }

### データの代入
データフレームに新しいデータを代入したり、上書きしたりできる。

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
### データ概要の確認
[`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)は、指定した列の高レベルな要約を提供する。

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

`describe()` の出力は入力の型によって異なる。数値ではない文字列データに対しては次のような出力になる。

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

特定の統計量だけを取り出すこともできる。

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

データフレーム内で各ユニーク値の出現回数を知りたい場合は、[`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html)を使う。

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

### 写像（Maps）
**写像（map）**は数学の用語で、一方の集合を別の集合へ対応させる関数を意味する。データサイエンスでは、与えられたデータを別の表現形式に変換する必要がしばしばあり、その際に写像を使うため非常に重要である。

主に次の 2 つのメソッドを使う場面が多い。

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)は 1 つの<u>値</u>を別の単一値に変換する関数を受け取り、その関数を指定した<u>シリーズ</u>内のすべての値に一括適用し、新しいシリーズを返す。たとえばワインの評価から一律に平均値を引いて偏差を得たいなら次のとおり。

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)は各<u>行</u>に対してカスタム関数を呼び出し、<u>データフレーム</u>全体に変換を適用したいときに使う。

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

`apply()` を `axis='index'` で呼べば、行ではなく列に対して関数を適用できる。

`Series.map()` と `DataFrame.apply()` は、それぞれ変換後の新しいシリーズとデータフレームを返し、元のデータは変更しない。

| メソッド | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| 適用対象 | シリーズ | データフレーム |
| 適用単位 | 個々の値に適用<br>（シリーズを[列ベクトル](/posts/vector-spaces-subspaces-and-matrices/#行ベクトルと列ベクトル)と見れば行方向に適用） | 既定では行方向に適用<br>オプション指定で列方向も可 |

> ちなみに[`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html)と[`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html)も存在する。
> - `Series.apply()`:
>   - `by_row='compat'`（既定）: `Series.map()`と同様に動作
>   - `by_row=False`: シリーズ全体を一度に関数へ渡す（`axis='index'` 指定時の `DataFrame.apply()` に類似）
> - `DataFrame.map()`：データフレーム内の個々の値に関数を適用（対象がシリーズかデータフレームか以外は `Series.map()` に近い）
{: .prompt-tip }

実のところ、Pandas にはよく使う写像が多数組み込まれている。上の例は次の、より簡潔なコードでも実現でき、この場合も Pandas は意図どおりに動作する。

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

さらに、Pandas は同じ長さのシリーズ同士の演算もサポートする。ワインの例で、原産国と産地の情報を次のように文字列連結することも可能だ。

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

これらの演算は Pandas の内蔵ベクトル化による高速化を利用するため、`map()` や `apply()` より高速であり、Pandas はすべての Python 標準の演算子（`>`, `<`, `==` など）に対してこの方式で動作できる。それでも `map()` と `apply()` はより柔軟で複雑な処理に対応できるため、使い分けを知っておくと有用である。
