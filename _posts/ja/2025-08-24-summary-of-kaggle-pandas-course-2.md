---
title: "Kaggle「Pandas」講座の内容整理（2）- Lesson 4-6"
description: "データ整形・加工に役立つPandasの使い方を体系的に整理。Kaggle公開コース「Pandas」を要約し、必要に応じて補足。後編（Lesson 4–6：グループ化とソート、データ型と欠損値、リネームと結合）を解説する。"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Kaggleの[Pandas](https://www.kaggle.com/learn/pandas)講座で学んだ内容をここに整理する。  
分量が多いため 2 回に分けた。
- [第1編: Lesson 1-3](/posts/summary-of-kaggle-pandas-course-1/)
- 第2編: Lesson 4-6（本文）

![修了証明書](/assets/img/kaggle-pandas/certificate.png)

## Lesson 4. Grouping and Sorting
しばしばデータを分類し、グループごとに集計や操作を行ったり、特定の基準で並べ替える必要がある。

### グループ別の分析
[`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)メソッドを使うと、特定の列の値が同じデータ同士をまとめ、その後に各グループ単位での概要確認や操作を行える。

先に[`value_counts()` メソッド](/posts/summary-of-kaggle-pandas-course-1/#データ概要の確認)を見たが、同等の動作は `groupby()` でも次のように実装できる。

```python
reviews.groupby('taster_name').size()
```

1. データフレーム `reviews` を、`taster_name` 列の値が同じもの同士でグループ化
2. まとめた各グループの大きさ（所属レコード数）をシリーズで返す

または

```python
reviews.groupby('taster_name').taster_name.count()
```

1. データフレーム `reviews` を、`taster_name` 列の値が同じもの同士でグループ化
2. まとめた各グループについて `taster_name` 列を選択
3. 該当列の欠損を除いた有効件数をシリーズで返す

つまり `value_counts()` は、実のところ上のような一連の操作のショートカットである。[`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) 以外にも任意の概要関数をこの要領で活用できる。たとえばワインデータから評価点ごとの最安値を確認するなら次のとおり。

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

1. データフレーム `reviews` を、`points` 列の値が同じもの同士でグループ化
2. まとめた各グループについて `price` 列を選択
3. 該当データの最小値をシリーズで返す

2 列以上をキーにして分類することも可能。国別・州別に評価が最も高いワインの情報だけ選ぶなら次のとおり。

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

DataFrameGroupBy オブジェクトで覚えておくと便利なメソッドに [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html) がある。これを使うとグループ化後に各グループへ複数の関数を同時に適用できる。

> このとき引数には次を渡せる。
> - 関数
> - 関数名の文字列
> - 関数または関数名文字列のリスト
> - 軸ラベルをキー、その軸に適用する関数または関数リストを値とする辞書
>
> ここで関数は
> - データフレームを入力として受け取れるか、
> - [前述の](/posts/summary-of-kaggle-pandas-course-1/#写像maps) [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) に引数として渡せる
>
> ものである必要がある。原講座にはない補足で、Pandas 公式ドキュメントに基づき加筆した。
{: .prompt-tip }

たとえば次のように国別の価格統計量を算出できる。

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> ここでの `len` は Python 組み込み関数 [`len()`](https://docs.python.org/3/library/functions.html#len) を指す。本例では、<u>欠損を含む</u>グループ（`country`）ごとの価格（`price`）データ件数を出力するために用いている。データフレームやシリーズを入力に動作できる関数なので、このように使える。
>
> Pandas の [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) は<u>欠損を除いた有効値のみ</u>を数える点で動作が異なる。
>
> いずれも原講座にはない補足で、Python と Pandas の公式ドキュメントに基づき加筆した。
{: .prompt-tip }

### マルチインデックス

`groupby()` による加工・分析では、単一ラベルではなく 2 段以上の階層からなるマルチインデックスを持つデータフレームが返ることがある。

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

マルチインデックスは階層構造を扱うための、単一インデックスにはないメソッドをいくつか備える。詳細な用例や指針は [pandas User Guide の MultiIndex / advanced indexing セクション](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)に詳しい。

とはいえ、もっとも頻用するのは、通常のインデックスに戻すための [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html) だろう。

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

### 並べ替え（ソート）

これまで例にしてきた `countries_reviewed` を見ると、グループ化の結果はインデックス順で返っていることがわかる。すなわち `groupby` 結果の行順は内容ではなくインデックス値で決まる。

必要に応じて別の基準で明示的に並べ替えられる。その際は [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) が便利だ。たとえば次のように、含まれる件数（'len'）を基準に国と州の情報を昇順でソートできる。

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

`sort_values()` は既定で昇順（小→大）だが、次のようにオプションを指定すれば降順（大→小）も可能。

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

インデックスでソートするなら [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html)。`sort_values()` と同様の引数と既定順序（昇順）を持つ。

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

最後に、次のように複数列を同時に基準にしてソートすることも可能。

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lesson 5. Data Types and Missing Values

実務で扱うデータが常にきれいに整っている保証はない。多くの場合、型を変換したり、所々にある欠損値を適切に処理する必要がある。データの加工・分析で最大の難所になりがちなのがこの段階だ。

### データ型

データフレームの特定の列、またはシリーズのデータ型を **dtype** という。`dtype` 属性で、与えられたデータフレームの特定列の型を確認できる。次は `reviews` の `price` 列の `dtype` を確認する例。

```python
reviews.price.dtype
```

```
dtype('float64')
```

あるいは `dtypes` 属性で、データフレーム内の全列の `dtype` を一度に確認できる。

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

データ型は Pandas が内部的にどのようにデータを保持しているかを示す。たとえば `float64` は 64 ビット浮動小数、`int64` は 64 ビット整数を意味する。

もう一つの特徴として、文字列だけで構成される列は独自の型を持たず、単にオブジェクト（`object`）として扱われる。

[`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) を使うと、ある型の列を別の型へ変換できる。たとえば、先の例で `int64` 型だった `points` 列を `float64` に変換できる。

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

データフレームやシリーズのインデックスも同様にデータ型を持つ。

```python
reviews.index.dtype
```

```
dtype('int64')
```

Pandas はこのほか、カテゴリ型や時系列型といった拡張データ型もサポートする。

### 欠損値

値がなく空のエントリには `NaN`（“Not a Number” の略）が与えられる。技術的理由により `NaN` は常に `float64` 型である。

Pandas は欠損に特化した関数をいくつか提供する。[以前にも軽く触れたが](/posts/summary-of-kaggle-pandas-course-1/#条件付き選択)、メソッドではない独立関数として [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) と [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html) がある。与えられたエントリが欠損か否かを単一のブール値またはブール配列で返し、次のように応用できる。

```python
reviews[pd.isna(reviews.country)]
```

通常は、与えられたデータに欠損があるかを確認し、あれば適切に埋める必要がある。戦略はいくつかあるが、まず [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) を使えば欠損を所定の値に置き換えて埋められる。次は `reviews` の `region_2` 列のすべての `NaN` を `"Unknown"` に置き換える例。

```python
reviews.region_2.fillna("Unknown")
```

あるいは、欠損の前方または後方で最も近い有効値を持ってきて埋める forward fill / backward fill 戦略を使える。これはそれぞれ [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html)、[`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html) で実装できる。

> かつては `fillna()` の `method` 引数に `'ffill'`、`'bfill'` を渡す方法もあったが、Pandas 2.1.0 以降は非推奨（deprecated）となったため、代わりに状況に応じて `ffill()` または `bfill()` を用いるべきである。
{: .prompt-danger }

場合によっては、欠損でなくとも特定の値を一括で別の値に置換したいことがある。原講座では特定のレビュアーの Twitter ハンドルが変更された例を挙げているが、日本の読者にも身近な別例を考えてみよう。

たとえば大韓民国で京畿道北部を分割して**京畿北道**という新しい行政区を設置し、その名称を反映したデータセットがあるとする。ところが誰かが**京畿北道**というまっとうな名前を**平和ヌリ特別自治道**に変えようというトンデモ案を出して、それが強行採択されてしまった仮想の状況を想像してみてほしい。~~仮想の話だが、似たような事態が現実に起こりかけたのが怖いところだ。~~ そうなると既存データセットの `"Gyeonggibuk-do"` を `"Pyeonghwanuri State"` もしくは `"Pyeonghwanuri Special Self-Governing Province"` のような新しい値に置き換える必要がある。Pandas でこの作業を行う方法の一つが [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html) だ。

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

この例を使えば、`rok_2030_census` の `province` 列にある `"Gyeonggibuk-do"` を、その“長いほう”へ一括置換できる。~~こんなコードを本当に回さねばならない現実にならなかったことに、改めて安堵する。~~

この種の文字列置換は、欠損処理やデータクリーニングでも有効だ。というのも、欠損が `NaN` ではなく `"Unknown"`、`"Undisclosed"`、`"Invalid"` のような文字列で与えられることも多いからである。現実には、昔の公文書を OCR スキャンしてデータ化するといった作業では、むしろこの種のケースが大半を占めることもある。

## Lesson 6. Renaming and Combining

ときにはデータセット内の特定列やインデックス名を変更する必要がある。また、複数のデータフレームやシリーズを結合する場面も多い。

### 名前の変更

[`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) を使うと、データセット内の特定列やインデックス名を変更できる。入力形式はいくつかあるが、通常は Python の辞書を使うのが簡便だ。次は `reviews` データフレームで `points` 列名を `score` に変え、インデックスの `0`、`1` を `firstEntry`、`secondEntry` に変える例。

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

実際のところ列名の変更は頻繁に行うが、インデックス値のリネームはほとんどない。その用途には、[以前見たように](/posts/summary-of-kaggle-pandas-course-1/#インデックスの操作) [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) を使うほうが楽なことが多い。

行インデックスと列インデックス自体にも `name` 属性があり、`rename_axis()` を使うとこの軸名も変更できる。たとえば行インデックス軸に `wines`、列軸に `fields` と名前を付けられる。

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### データセットの結合

データフレーム同士、あるいはシリーズ同士を結合しなければならないことがある。Pandas はこのために、単純なものから複雑なものへと並べると、[`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)、[`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)、[`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html) の 3 つの中核関数を提供する。Kaggle 講座では、`merge()` でできることの大半は `join()` のほうが簡潔に書けるため、前者 2 つに焦点を当てている。

`concat()` は最も単純で、複数のデータフレームまたはシリーズを、指定した軸に沿ってそのまま連結する。同じフィールド（列）構成のデータを結合する際に有用。既定では行（インデックス）方向に連結し、`axis=1` または `axis='columns'` を指定すれば列方向に連結できる。

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

> [Pandas 公式ドキュメント]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html))によれば、複数行を 1 つのデータフレームにまとめたいとき、ループの内側で 1 行ずつ追加するのは非推奨であり、結合対象の行をリストに集めて単一の `concat()` で一度に結合すべきである。
{: .prompt-tip }

`join()` はやや複雑で、インデックスを基準に一方のデータフレームへ他方を連結する。このとき同名列が衝突する場合は、`lsuffix` と `rsuffix` 引数で両データフレームの重複列名に付ける接尾辞をそれぞれ指定する必要がある。

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
