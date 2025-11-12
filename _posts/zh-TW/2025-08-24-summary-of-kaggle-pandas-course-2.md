---
title: "Kaggle「Pandas」課程內容整理（2）— Lesson 4–6"
description: "整理用於資料清理與處理的 pandas 函式庫實務用法；摘要 Kaggle「Pandas」公開課程並視需要補充。本文涵蓋課程後半部（Lesson 4–6）：分組與排序、資料型別與缺失值、重新命名與資料合併。"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

透過 Kaggle 的 [Pandas](https://www.kaggle.com/learn/pandas) 課程學習後，將所學整理於此。  
由於篇幅頗長，分成兩篇。
- [第 1 篇：Lesson 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- 第 2 篇：Lesson 4–6（本文）

![結業證書](/assets/img/kaggle-pandas/certificate.png)

## Lesson 4. Grouping and Sorting
有時需要先將資料分組，針對各組做彙整或操作，或依特定準則進行排序。

### 分組分析
使用 [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) 方法可把某欄值相同的資料歸為一組，之後對各組進行摘要或操作。

前面看過[《`value_counts()` 方法》](/posts/summary-of-kaggle-pandas-course-1/#檢視資料概要)，同樣的操作也可以用 `groupby()` 如下實作：

```python
reviews.groupby('taster_name').size()
```

1. 以 `taster_name` 欄把 `reviews` 資料框分組
2. 回傳每組的大小（筆數）為一個序列

或是：

```python
reviews.groupby('taster_name').taster_name.count()
```

1. 以 `taster_name` 欄把 `reviews` 資料框分組
2. 對各組選取 `taster_name` 欄
3. 回傳各組中非缺失值的數量為序列

也就是說，`value_counts()` 其實是上述動作的速記。除了 [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) 以外，其他各種摘要函式也能這麼用。比如要從葡萄酒資料中查各評分的最低價：

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

1. 以 `points` 欄把 `reviews` 分組
2. 對各組選取 `price` 欄
3. 回傳最小值為序列

也可以同時以多個欄位分組。若要挑出各「國家 × 省」中評分最高的葡萄酒資料：

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

另一個值得知道的 DataFrameGroupBy 物件方法是 [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html)。使用它可以在分組後，對各組同時執行多個函式。

> 可傳入的引數包括：
> - 函式
> - 函式名稱字串
> - 函式或函式名稱的列表
> - 字典（鍵為軸標籤、值為要套用於該軸的函式或函式列表）
>
> 其中函式必須
> - 能以資料框為輸入，或
> - 能作為[前面談過的](/posts/summary-of-kaggle-pandas-course-1/#映射maps) [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) 的參數
>
> 以上為補充說明，原 Kaggle 課程未詳述，據 pandas 官方文件增補。
{: .prompt-tip }

例如計算各國價格的統計量：

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> 這裡的 `len` 指的是 Python 內建函式 [`len()`](https://docs.python.org/3/library/functions.html#len)。此例中用來輸出各分組（以 `country` 分）之價格（`price`）資料筆數，且會<u>包含缺失值</u>。因它能以資料框或序列為輸入，故可直接使用。
>
> pandas 提供的 [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) 方法則<u>只計數非缺失值</u>，行為不同。
>
> 以上為補充說明，原 Kaggle 課程未詳述，據 Python 與 pandas 官方文件增補。
{: .prompt-tip }

### 多重索引

使用 `groupby()` 進行加工分析時，常會得到具有多層級、多標籤的多重索引資料框。

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

多重索引具備一些單層索引沒有、用來處理層級結構的便利方法。更完整的使用方式與指引可見 [pandas 使用者指南的 MultiIndex / advanced indexing 章節](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)。

不過，最常用的大概是把它還原成一般索引的 [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)。

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

### 排序

回頭看我們一直用的 `countries_reviewed`，會發現分組後的結果是依索引順序回傳。也就是說，`groupby` 結果的列順序由索引值決定，而非資料內容。

需要其他排序方式時，可用 [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) 很方便。例如以下可依資料筆數（'len'）對國家與省份資訊做遞增排序：

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

`sort_values()` 預設為遞增（由小到大），若加上選項即可改為遞減：

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

若要依索引排序則使用 [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html)。其引數與預設排序方向（內減序）與 `sort_values()` 相同，用法一致。

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

最後，也可以一次以多個欄位作為排序鍵：

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lesson 5. Data Types and Missing Values

真實世界的資料很少一開始就乾淨齊整，更多時候是欄位型別需轉換、或夾雜缺失值而必須適當處理。資料加工分析時，最大的難關往往就在這一步。

### 資料型別

資料框某欄（或序列）的型別稱為該欄的 dtype。可以由 `dtype` 屬性檢視資料框特定欄位的型別。以下例子檢視 `reviews` 的 `price` 欄之 `dtype`：

```python
reviews.price.dtype
```

```
dtype('float64')
```

或以 `dtypes` 屬性一次性檢視整個資料框所有欄位的 `dtype`：

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

`dtype` 表示 pandas 內部如何存放資料。例如 `float64` 表 64 位元浮點數，`int64` 表 64 位元整數。

一個特別之處是，純字串欄位不具獨立型別，而被視作物件（`object`）。

使用 [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) 可將某欄由一種型別轉為另一種。例如把先前 `int64` 的 `points` 欄轉成 `float64`：

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

資料框或序列的索引同樣具有型別：

```python
reviews.index.dtype
```

```
dtype('int64')
```

此外，pandas 也支援外部型別，例如類別型（categorical）或時間序列型（datetime 等）。

### 缺失值

沒有值、空白的項目會被指定為 `NaN`（“Not a Number”的縮寫）。基於技術原因，`NaN` 總是 `float64` 型別。

pandas 內建多個處理缺失值的函式。[之前也稍微看過類似的內容](/posts/summary-of-kaggle-pandas-course-1/#條件式選取)：除了方法之外，pandas 也提供獨立函式 [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) 與 [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html)。它們會對給定項目回傳布林值或布林陣列，用來表示是否為缺失值，可像下面這樣應用：

```python
reviews[pd.isna(reviews.country)]
```

通常我們要先檢查是否存在缺失值，若有則採取適當補值策略。策略很多，其中 [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) 可把缺失值替換成合適常數。以下把 `reviews` 的 `region_2` 欄內所有 `NaN` 改成 `"Unknown"`：

```python
reviews.region_2.fillna("Unknown")
```

或者，遇缺失值時以前一個或後一個最近的有效值填補（forward fill / backward fill），可分別用 [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html)、[`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html) 實現。

> 過去也能在 `fillna()` 中以 `method` 參數傳入 `'ffill'`、`'bfill'` 字串；但自 pandas 2.1.0 起該作法已被標註為 deprecated，不再建議使用，請改用情境合適的 `ffill()` 或 `bfill()` 方法。
{: .prompt-danger }

另外，有時即便不是缺失值，也可能需要把特定值整批替換成另一值。原 Kaggle 課程用的是某位評論者的 Twitter handle 更名為例。為了更貼近日常情境，我們改用另一個想像案例：

韓國將京畿道北部劃設為新的行政區，命名為**京畿北道**，並據此更新資料集。此時若有人突發奇想要把**京畿北道**這個好好的名稱改成**平和之路特別自治道**，而且還真的推行了——雖說是假設，但想想差點可能成真的情況也確實令人心驚。那麼我們就得把既有資料集中的 `"Gyeonggibuk-do"` 全部替換成新的值，如 `"Pyeonghwanuri State"` 或 `"Pyeonghwanuri Special Self-Governing Province"`。在 pandas 中可用 [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html) 來做這件事。

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

用上面的範例，便能把 `rok_2030_census` 資料集 `province` 欄內的所有 `"Gyeonggibuk-do"` 一口氣換成那個「很長的名字」。~~想到現實裡並沒有真的有人必須跑這段程式，仍不禁鬆一口氣。~~

這類字串替換在缺失值處理與資料清理時也很常見，因為缺失有時不是 `NaN`，而是以 `"Unknown"`、`"Undisclosed"`、`"Invalid"` 等字串出現。在將舊公文或表單 OCR 成資料集等現實任務中，反而經常會遇見。

## Lesson 6. Renaming and Combining

有時需要更改資料集中特定欄或索引的名稱；也常需要把多個資料框或序列結合起來。

### 重新命名

使用 [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) 可更改資料集中特定欄或索引的名稱。`rename()` 支援多種輸入形式，最常見也最方便的是使用 Python 字典。以下在 `reviews` 中把 `points` 欄改名為 `score`，並把索引值 `0`、`1` 改為 `firstEntry`、`secondEntry`：

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

實務上比較常改的是欄名，較少改索引值名稱。且若是為此目的，[如先前所見](/posts/summary-of-kaggle-pandas-course-1/#操作索引) 通常用 [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) 更方便。

列索引與欄索引本身也有 `name` 屬性；使用 `rename_axis()` 可更改軸名稱。例如將列索引命名為 `wines`、欄軸命名為 `fields`：

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### 合併資料集

有時需要把資料框與資料框、或序列與序列合併。pandas 提供三個核心工具，按由簡到繁依序是 [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)、[`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)、[`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)。Kaggle 課程指出：`merge()` 能做的大多數事，通常用 `join()` 更簡單，因此重點放在前兩者。

`concat()` 最單純：把多個資料框或序列沿某個軸直接接起來。當待合併的資料框（或序列）擁有相同欄位時特別好用。預設沿索引軸拼接；指定 `axis=1` 或 `axis='columns'` 則沿欄軸拼接。

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

> 依[官方文件]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html))，若要把多筆列合成單一資料框，不建議在迴圈中逐列追加；應先把要合併的列收成列表，再用一次 `concat()` 合併。
{: .prompt-tip }

`join()` 較複雜一些：它會依索引，把另一個資料框接到第一個資料框上。若雙方有重名欄位，須分別用 `lsuffix` 與 `rsuffix` 指定左右兩邊欄名要加上的後綴，避免衝突。

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
