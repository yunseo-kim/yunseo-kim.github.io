---
title: "Summary of Kaggle 'Pandas' Course (2) - Lessons 4–6"
description: "Practical Pandas for data cleaning and wrangling: a concise summary of Kaggle’s free 'Pandas' course with added notes. This part covers Lessons 4–6—grouping/sorting, data types & missing values, renaming and combining."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

I summarize here what I studied through Kaggle’s [Pandas](https://www.kaggle.com/learn/pandas) course.  
Since it’s fairly long, I split it into two parts.
- [Part 1: Lessons 1–3](/posts/summary-of-kaggle-pandas-course-1/)
- Part 2: Lessons 4–6 (this post)

![Certificate of Completion](/assets/img/kaggle-pandas/certificate.png)

## Lesson 4. Grouping and Sorting
Sometimes you need to categorize data and perform operations per group, or sort by specific criteria.

### Group-wise analysis
Using the [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) method, you can group rows sharing the same values in a given column and then compute summaries or apply operations per group.

Previously, we saw the [`value_counts()` method](/posts/summary-of-kaggle-pandas-course-1/#quick-summaries). You can implement the same behavior with `groupby()` as follows:

```python
reviews.groupby('taster_name').size()
```

1. Group the `reviews` DataFrame by identical values in the `taster_name` column
2. Return a Series of group sizes (number of rows in each group)

Or:

```python
reviews.groupby('taster_name').taster_name.count()
```

1. Group the `reviews` DataFrame by identical values in the `taster_name` column
2. Within each group, select the `taster_name` column
3. Return a Series with the count of non-missing values

In other words, the `value_counts()` method is essentially shorthand for the behavior above. Beyond [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html), you can use any summary function similarly. For instance, to find the minimum price per score in the wine data:

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

1. Group the `reviews` DataFrame by identical values in the `points` column
2. Within each group, select the `price` column
3. Return the minimum value per group as a Series

You can also group by multiple columns. To select the highest-rated wine per country and province:

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

Another DataFrameGroupBy method worth knowing is [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html). It lets you run multiple functions per group after grouping.

> You can pass as the argument:
> - a function
> - a string with the function name
> - a list of functions or function-name strings
> - a dictionary mapping axis labels to a function or list of functions to apply on that axis
>
> The function must be able to:
> - accept a DataFrame as input, or
> - be a function acceptable to [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) [as covered earlier](/posts/summary-of-kaggle-pandas-course-1/#maps).
>
> This clarification isn’t in the original Kaggle course; I added it based on the official pandas docs.
{: .prompt-tip }

For example, compute per-country price statistics:

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> Here `len` refers to Python’s built-in [`len()`](https://docs.python.org/3/library/functions.html#len). In this example it reports the number of price (`price`) entries per group (`country`), <u>including missing values</u>. Since it accepts a DataFrame or Series as input, it can be used this way.
>
> In contrast, pandas’ [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) returns the count of <u>non-missing values only</u>.
>
> This note isn’t in the original Kaggle course; I added it based on the official Python and pandas documentation.
{: .prompt-tip }

### MultiIndex

When you perform groupby-based transformations and analyses, you’ll sometimes get a DataFrame with a MultiIndex composed of more than one level.

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

A MultiIndex provides methods not present on a simple Index to handle hierarchical structures. For detailed usage and guidelines, see the [MultiIndex / advanced indexing section of the pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

That said, the method you’ll likely use most often is [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html) to flatten back to a regular Index:

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

### Sorting

Looking at `countries_reviewed`, you’ll notice grouped results are returned in index order. That is, the row order of a `groupby` result is determined by index values, not by data content.

When needed, you can sort explicitly using [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html). For example, to sort country–province pairs in ascending order by the number of entries ('len'):

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

`sort_values()` sorts ascending by default (low to high), but you can sort descending (high to low) by specifying:

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

To sort by index instead, use [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html). It accepts the same parameters and has the same default order (descending) as `sort_values()`.

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

Lastly, you can sort by multiple columns at once:

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lesson 5. Data Types and Missing Values

In practice, data rarely comes perfectly clean. More often than not, column types aren’t what you want and need conversion, and missing values appear throughout and must be handled carefully. For most data workflows, this stage is the biggest hurdle.

### Data types

The data type of a DataFrame column or a Series is its **dtype**. Use the `dtype` attribute to check the type of a specific column. For example, to inspect the dtype of the `price` column in `reviews`:

```python
reviews.price.dtype
```

```
dtype('float64')
```

Or use the `dtypes` attribute to inspect all column dtypes at once:

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

A dtype reflects how pandas stores data internally. For instance, `float64` is a 64-bit floating-point number, and `int64` is a 64-bit integer.

One peculiarity: columns of pure strings don’t have a dedicated string type (in this context) and are treated as generic Python objects (`object`).

Use [`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html) to convert a column from one type to another. For example, convert the `points` column from `int64` to `float64`:

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

A DataFrame (or Series) index also has a dtype:

```python
reviews.index.dtype
```

```
dtype('int64')
```

Pandas also supports “extension” dtypes such as categorical and various time-series types.

### Missing values

Empty entries are represented as `NaN` (short for “Not a Number”). For technical reasons, `NaN` is always of dtype `float64`.

Pandas provides helper functions for missing data. [We briefly saw something similar before](/posts/summary-of-kaggle-pandas-course-1/#conditional-selection): in addition to methods, pandas has standalone functions [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html) and [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html). They return a single boolean or a boolean array indicating whether entries are missing (or not), and can be used like this:

```python
reviews[pd.isna(reviews.country)]
```

Often you’ll want to detect missing values and then fill them with appropriate replacements. One strategy is to use [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) to replace `NaN`s with a chosen value. For example, replace all `NaN` in the `region_2` column with `"Unknown"`:

```python
reviews.region_2.fillna("Unknown")
```

Alternatively, you can use forward fill or backward fill to propagate the nearest valid value from above or below, via [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html) and [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html), respectively.

> Previously you could pass `'ffill'`/`'bfill'` to the `method` parameter of `fillna()`, but this became deprecated starting in pandas 2.1.0. Prefer `ffill()` or `bfill()` directly instead.
{: .prompt-danger }

Sometimes you need to replace a value with another even if it’s not missing. The original Kaggle course gives an example of a reviewer changing their Twitter handle. That’s a fine example, but here’s one that may feel more relatable to Korean readers:

Suppose South Korea split the northern part of Gyeonggi-do and established a new administrative region called **Gyeonggibuk-do**, and you have a dataset reflecting that change. Now imagine someone floated the harebrained idea of renaming **Gyeonggibuk-do** to **Pyeonghwanuri Special Self-Governing Province**, and actually managed to ram it through—a purely hypothetical scenario, of course. ~~It’s scary how close something like this might have come to happening.~~ You would then need to replace `"Gyeonggibuk-do"` with a new value like `"Pyeonghwanuri State"` or `"Pyeonghwanuri Special Self-Governing Province"` in the dataset. One way to do this in pandas is with [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html):

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

With this snippet, you can effectively bulk-replace every `"Gyeonggibuk-do"` string in the `province` column of the `rok_2030_census` dataset with ‘that long one’. ~~It’s a relief no one actually had to run code like this in real life.~~

String replacement is also useful during cleaning, since missingness is often encoded as strings like `"Unknown"`, `"Undisclosed"`, or `"Invalid"` rather than `NaN`. In real-world workflows such as OCR-ing old official documents into datasets, this may be the norm rather than the exception.

## Lesson 6. Renaming and Combining

Sometimes you need to rename specific columns or index labels in a dataset. You’ll also frequently have to combine multiple DataFrames or Series.

### Renaming

Use [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) to rename columns or index labels. It supports various input formats, but a Python dictionary is usually the most convenient. The following examples rename the `points` column to `score` and relabel index entries `0` and `1` to `firstEntry` and `secondEntry`:

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

In practice, renaming columns is common, while renaming index values is rare; for that purpose, it’s usually more convenient to use [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) [as we saw earlier](/posts/summary-of-kaggle-pandas-course-1/#manipulating-the-index).

Both the row and column axes have a `name` attribute. You can rename these axis names with `rename_axis()`. For example, label the row axis as `wines` and the column axis as `fields`:

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### Combining datasets

You’ll often need to combine DataFrames or Series. Pandas provides three core tools for this, from simplest to most flexible: [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html), and [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html). The Kaggle course focuses on the first two, noting that most `merge()` tasks can be done more simply with `join()`.

`concat()` is the simplest: it stitches multiple DataFrames or Series along a given axis. It’s handy when the objects share the same fields (columns). By default, it concatenates along the index axis; specify `axis=1` or `axis='columns'` to concatenate along columns.

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

> According to the [pandas docs]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html)), when building a DataFrame from many rows, avoid appending rows one by one in a loop. Instead, collect the rows in a list and perform a single `concat()`.
{: .prompt-tip }

`join()` is more complex: it attaches another DataFrame to a base DataFrame by aligning on the index. If the two DataFrames have overlapping column names, you must specify `lsuffix` and `rsuffix` to disambiguate them.

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
