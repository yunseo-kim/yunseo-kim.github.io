---
title: "Kaggle「Pandas」課程內容整理（1）— Lesson 1–3"
description: "整理用於資料清理與處理的 pandas 函式庫實務用法，摘要 Kaggle「Pandas」公開課程並視需要補充。本文涵蓋 Lesson 1–3：建立／讀寫、索引與選取／指派、摘要函式與映射。"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

透過 Kaggle 的 [Pandas](https://www.kaggle.com/learn/pandas) 課程學習後，將要點整理於此。  
篇幅頗長，因此分成兩篇。
- 第 1 篇：Lesson 1–3（本文）
- [第 2 篇：Lesson 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![結業證書](/assets/img/kaggle-pandas/certificate.png)

## Lesson 1. Creating, Reading and Writing
### 匯入 pandas

```python
import pandas as pd
```

pandas 有兩個核心物件：**資料框（DataFrame）**與**序列（Series）**。

### 資料框
[資料框（DataFrame）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)可以視為表格，或是[矩陣](/posts/vector-spaces-subspaces-and-matrices/#矩陣與矩陣空間)。它由獨立的*項目（entries）*構成的矩陣組成，其中每個項目具有一個*值（value）*，並對應到一個*行（row）*或*紀錄（record）*與一個*列（column）*。

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

資料框的項目不一定是數值。以下是具有字串值（使用者留下的評價）的資料框範例。

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

建立資料框時使用 `pd.DataFrame()` 建構子（constructor），並以 Python 的字典（dictionary）語法宣告。鍵（key）放欄名，值（value）放欲填入的列表（list）。這是宣告新資料框的標準方式。

宣告資料框時，欄標籤（列名）由你自定；若未另行指定列（row）標籤，則自動指派 0, 1, 2, ... 的整數。必要時也可手動指定列標籤。資料框的列標籤列表稱為[**索引（Index）**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html)，可透過建構子的 `index` 參數指定。

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

| | Bob | Sue |
| --- | --- | --- |
| Product A | I liked it. | Pretty good. |
| Product B | It was awful. | Bland. |

### 序列
[序列（Series）](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)是一個由資料值組成的序列（sequence），或[向量](/posts/vector-spaces-subspaces-and-matrices/#行向量與列向量)。

```python
pd.Series([1, 2, 3, 4, 5])
```

序列本質上等同於資料框的一個欄。因此同樣可以指定[索引](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html)，但它不叫「欄名」而僅稱為「名稱」（[`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)）。

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

序列與資料框關係緊密。把資料框視為一組序列的集合會更好理解。

### 讀取資料檔
多數情況下，我們不會手寫資料，而是匯入既有資料。資料可有多種格式，最基本的是 CSV 檔。其內容通常如下：

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

也就是以逗號（comma）分隔各值的表格，因此稱為「逗號分隔值（Comma-Separated Values, CSV）」。

要把 CSV 讀成資料框，使用 [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)。

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

可用 [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) 屬性檢視資料框的形狀。

```python
product_reviews.shape
```

```
(129971, 14)
```

上述輸出表示該資料框有 129971 筆紀錄、14 個欄位。

使用 [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) 方法可檢視前五列。

```python
product_reviews.head()
```

[`pd.read_csv()` 有超過 30 個參數](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)。例如，若 CSV 本身包含索引欄，可透過 `index_col` 指定該欄作為索引，避免 pandas 另行自動編索引。

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### 寫出資料檔
使用 [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) 方法可將資料框輸出為 CSV 檔，使用方式如下：

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lesson 2. Indexing, Selecting & Assigning
在 pandas 的資料框或序列中選取特定值，是幾乎所有資料處理工作都會經過的步驟。因此，先學會如何快速有效地挑出需要的資料點非常重要。

### Python 原生取用
原生 Python 物件提供了良好的資料索引方式，pandas 也同樣支援這些方式。

#### 物件屬性
在 Python 中可透過屬性名稱（attribute）存取物件的屬性值（property）。例如物件 `example_obj` 有屬性 `title`，即可用 `example_obj.title` 取用。對 pandas 資料框的欄也可同樣存取。

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

#### 字典式索引
Python 的字典型別可用索引運算子（`[]`）存取內部值。對 pandas 資料框的欄，同樣可用此法。

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

兩種方式皆可。不過字典式索引的優點是能處理包含空白等保留字元的欄名（例如 `reviews['country providence']` 可行，但 `reviews.country providence` 不可）。

在取出的 pandas 序列內，還可以再用索引運算子讀取個別值。

```python
reviews['country'][0]
```

```
'Italy'
```

### pandas 專用取用器
上述以索引運算子或物件屬性取用的作法，能自然地融入 Python 生態系，非常好用。不過 pandas 另提供兩個專用取用器：[`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) 與 [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)。

#### 以位置索引為基礎的選取
使用 `iloc` 可進行**以索引為基礎的選取（index-based selection）**，也就是以整數位置指定資料。

例如，選取資料框的第一列：

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

不同於原生 Python 先選欄後選列的方式，`iloc` 是先選列，再選欄。選取資料框的第一欄如下：

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

上述用 `:` 先選全部列，再選第一欄。若要選第一欄的第二（`1`）與第三（`2`）列：

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

也可傳入列表：

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

可使用負數自尾端選取。以下例子為最後 5 列：

```python
reviews.iloc[-5:]
```

#### 以標籤為基礎的選取
另一種方式是用 `loc` 進行**以標籤為基礎的選取（label-based selection）**。此時不是用位置，而是用索引值來選取。

例如，取出索引值為 0 的列之 'country' 欄位：

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` 會忽略資料集的索引值，把資料視為單一大矩陣，依位置取用。相對地，`loc` 會利用索引資訊。由於索引通常具有語義，因此多數情況 `loc` 比 `iloc` 直覺。

#### `iloc` 與 `loc` 的區間差異
`iloc` 採用 Python 標準的索引規則，因此 `0:10` 表示 0 以上 10「未滿」的半開區間，即 `0,...,9`。

相反地，`loc` 將區間視為閉區間，因此 `0:10` 表示 0 以上 10「以下」，即 `0,...,10`。

之所以如此，是因為 `loc` 的索引不僅能是整數，也可以是任何標準型別。假設索引值為 `Apples, ..., Potatoes, ...`，想依字典序選取從 'Apples' 到 'Potatoes' 的作物。與其寫「從 'Apples' 到 'Potatoet' 之前」（`df.loc['Apples':'Potatoet']`，因為按字典序 s 後面是 t，'Potatoes' 的下一個可能字串是 'Potatoet'），不如直接寫「從 'Apples' 到 'Potatoes'」（`df.loc['Apples':'Potatoes']`）更直覺。對非整數索引，後者更自然，因此 `loc` 採此規則。

除此之外，其餘行為基本一致。

> 我個人習慣：當資料集為遞增整數索引，且需要用 `:` 指定範圍時，為避免上述區間差異造成混淆會用 `iloc`；其他情況下則偏好更直覺的 `loc`。
{: .prompt-tip }

### 操作索引
也可以按需要調整索引。使用 [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) 方法可將資料集中的某欄設為新索引，如下例：

```python
reviews.set_index("title")
```

### 條件式選取
上述內容是利用資料框本身的結構性屬性來處理與選取資料。更進一步，也能依較複雜的條件來篩選資料。

例如，在一個葡萄酒產品的資料框中，若要選取評分 90 分以上、且產地為義大利的酒款：

```python
reviews.country == 'Italy'
```

此條件式會回傳一個由 `True`/`False` 組成的布林序列。

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` 雖以標籤為主，但也接受布林陣列或可排序的布林序列](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)。因此可以這樣選出義大利酒：

```python
reviews.loc[reviews.country == 'Italy']
```

多個條件可用 `&` 或 `|` 結合。若要選取「是義大利產」且「評分 ≥ 90」：

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

若要選取「是義大利產」或「評分 ≥ 90」：

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

pandas 也內建幾個常用的條件式選取器，尤其是 `isin` 與 `isna`/`notna`（亦可見 `isnull`/`notnull`）。

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) 會針對是否「在列表之內（is in）」回傳布林遮罩序列，可用來篩選資料。例如選出產地為義大利或法國的酒款：

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) 用於篩選含有或不含缺失值（`NaN`）的資料。例如選出價格不缺值的酒款：

```python
reviews.loc[reviews.price.notna()]
```

> 補充：雖然 Kaggle 課程未提及，[`iloc` 也能接受布林陣列（array）](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)。但與 `loc` 不同的是，`iloc` 只支援陣列、不支援序列，因此較難像上述那樣靈活應用。
{: .prompt-tip }

### 資料指派（賦值）
也可以在資料框中新增或覆寫資料。

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
### 檢視資料概要
[`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) 方法會提供給定欄位的高層次摘要。

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

`describe()` 的輸出會依輸入型別而異。對非數值（如字串）資料，輸出如下：

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

也可以只取特定統計量。

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

若想知道各個唯一值各出現幾次，可用 [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html)。

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

### 映射（Maps）
「**映射（map）**」是數學術語，意指把一個集合對應到另一個集合的函數。在資料科學中，常需要把資料轉換成另一種表達形式；此時就會用到各種映射，因此非常重要。

主要會常用兩個方法：

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) 接受一個把單一<u>值</u>轉成另一個單一值的函式，將其套用到給定<u>序列</u>的所有值並回傳新的序列。例如要把葡萄酒評分整體減去平均值以得到偏差，可如下進行：

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) 則用於對每一<u>列</u>呼叫自訂函式，從而對整個<u>資料框</u>施加轉換。

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

把 `apply()` 的參數設為 `axis='index'` 則可改為對每一欄套用函式。

`Series.map()` 與 `DataFrame.apply()` 都會回傳新的、已轉換的序列或資料框，原始資料不會被修改。

| 方法 | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| 作用對象 | 序列 | 資料框 |
| 套用單位 | 逐值套用 <br>（若把序列視為[列向量](/posts/vector-spaces-subspaces-and-matrices/#行向量與列向量)，即按行套用） | 預設逐列套用 <br> 指定選項後可逐欄套用 |

> 補充：亦有 [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) 與 [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html)。
> - `Series.apply()`：
>   - `by_row='compat'`（預設）：行為與 `Series.map()` 相同
>   - `by_row=False`：將整個序列一次性傳入函式（類似於 `DataFrame.apply()` 設 `axis='index'` 的行為）
> - `DataFrame.map()`：對資料框中的每個單一值套用函式（除了目標是資料框而非序列外，與 `Series.map()` 類似）
{: .prompt-tip }

事實上，pandas 對許多常見的映射提供了內建支援。前述例子可用更精簡的程式達成，pandas 會正確推斷意圖並運作：

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

此外，pandas 也支援同長度序列之間的運算。在葡萄酒例子中，也可以如下把產國與產區以字串相連：

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

這些運算走的是 pandas 的向量化加速路徑，通常比 `map()` 或 `apply()` 更快。而 `map()` 與 `apply()` 更具彈性，能處理更複雜的任務，因此仍值得掌握。
