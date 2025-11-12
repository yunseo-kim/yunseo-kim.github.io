---
title: "Summary of Kaggle 'Pandas' Course (1) - Lessons 1–3"
description: "Summarizes practical ways to use the Pandas library for data cleaning and wrangling, based on Kaggle’s free 'Pandas' course with added notes. This post covers Lessons 1–3."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

I summarize here what I studied through Kaggle’s [Pandas](https://www.kaggle.com/learn/pandas) course.  
Since it’s fairly long, I split it into two parts.
- Part 1: Lessons 1–3 (this post)
- [Part 2: Lessons 4–6](/posts/summary-of-kaggle-pandas-course-2/)

![Certificate of Completion](/assets/img/kaggle-pandas/certificate.png)

## Lesson 1. Creating, Reading and Writing
### Importing pandas

```python
import pandas as pd
```

Pandas has two core objects: the **DataFrame** and the **Series**.

### DataFrame
A [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) can be thought of as a table or a [matrix](/posts/vector-spaces-subspaces-and-matrices/#matrices-and-matrix-spaces). It consists of a matrix of independent *entries*, where each entry has a specific *value* and corresponds to a single *row* (or *record*) and a *column*.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

DataFrame entries don’t have to be numeric; the following is an example DataFrame with string values (user reviews).

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

To create a DataFrame, use the `pd.DataFrame()` constructor and pass a Python dictionary. Put column names as keys and lists of values as dictionary values. This is the standard way to declare a new DataFrame.

When creating a DataFrame, you typically specify column labels (column names). If you don’t specify row labels, pandas assigns integers 0, 1, 2, ... as row labels. If needed, you can set row labels manually. The list of row labels in a DataFrame is called the [**Index**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html), and you can set it via the constructor’s `index` parameter.

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
A [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) is a sequence of data values, i.e., a [vector](/posts/vector-spaces-subspaces-and-matrices/#row-and-column-vectors).

```python
pd.Series([1, 2, 3, 4, 5])
```

A Series is essentially a single column of a DataFrame. As such, it can have an [index](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html), and instead of a “column name” it simply has a [`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Series and DataFrame are closely related. You can think of a DataFrame as a collection of Series aligned by a shared index.

### Reading data files
In many cases, you’ll import existing data rather than writing it from scratch. Data can be stored in various formats; the most basic is CSV. A CSV file typically looks like this:

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

CSV stands for “Comma-Separated Values,” i.e., a table where values are separated by commas.

To read CSV data into a DataFrame, use [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

You can check a DataFrame’s shape with the [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) attribute.

```python
product_reviews.shape
```

```
(129971, 14)
```

This output means the DataFrame has 129,971 records (rows) and 14 columns.

Use the [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) method to preview the first five rows.

```python
product_reviews.head()
```

[`pd.read_csv()` has over 30 parameters](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). For example, if the CSV already contains an index column, you can use `index_col` to tell pandas to use that column instead of creating a new integer index.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Writing data files
You can export a DataFrame to CSV using the [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) method:

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lesson 2. Indexing, Selecting & Assigning
Selecting specific values from a pandas DataFrame or Series is a step you’ll perform in almost every data-processing task, so it’s essential to learn how to pick out the data points you need quickly and efficiently.

### Native Python accessors
Native Python objects provide excellent indexing methods, and pandas adopts those same mechanisms.

#### Object attributes
In Python, you access an object’s property via its attribute name. For example, if `example_obj` has an attribute `title`, you can call `example_obj.title`. The same works for DataFrame columns.

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

#### Dictionary indexing
Python dictionaries use the indexing operator (`[]`) to access values. DataFrame columns can be accessed the same way.

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

Both attribute access and dictionary-style access are valid; however, the dictionary style can handle column names containing reserved characters like spaces (e.g., `reviews['country providence']` works, whereas `reviews.country providence` does not).

You can also index into the resulting pandas Series to retrieve an individual value:

```python
reviews['country'][0]
```

```
'Italy'
```

### Pandas-specific accessors
While attribute and `[]` accessors integrate naturally with the wider Python ecosystem, pandas also provides its own dedicated accessors: [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) and [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Index-based selection
Use `iloc` for **index-based selection**—that is, selecting by integer position.

For example, select the first row of the DataFrame:

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

Unlike native Python, where you select a column first and then rows, `iloc` selects rows first, then columns. Select the first column like this:

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

Here `:` selects all rows, and `0` picks the first column. To select the second (`1`) and third (`2`) rows of the first column:

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Or pass a list:

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

You can also use negative indices to select from the end. For example, the last five rows:

```python
reviews.iloc[-5:]
```

#### Label-based selection
Alternatively, use `loc` for **label-based selection**—that is, selecting by index labels.

For example, to get the entry at row label 0 and column 'country':

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` ignores the dataset’s index labels and treats the data as one big array, accessing by position. In contrast, `loc` uses the index information, which is often more intuitive because indexes usually carry meaning.

#### Range semantics: `iloc` vs `loc`
`iloc` follows Python’s standard half-open slicing, so `0:10` means 0 up to but not including 10 (i.e., `0,...,9`).

`loc` treats slices as closed intervals, so `0:10` means 0 through 10 inclusive (i.e., `0,...,10`).

The reason is that `loc` supports not just integers but any sortable label type. For example, suppose a DataFrame has labels like `Apples, ..., Potatoes, ...`. Selecting alphabetically from 'Apples' to 'Potatoes' is more intuitive as `df.loc['Apples':'Potatoes']` than something like “from 'Apples' up to (but not including) 'Potatoet'.” For non-integer indices, closed intervals are typically more natural, hence `loc` uses them.

Otherwise, their behavior is broadly similar.

> Personally, when working with ascending integer indices and slicing with `:`, I prefer `iloc` to avoid confusion over slice semantics; in other cases, I find `loc` more intuitive.
{: .prompt-tip }

### Manipulating the index
You can adjust the index as needed. For example, use [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) to make a specific column the new index:

```python
reviews.set_index("title")
```

### Conditional selection
So far we’ve selected data using structural attributes of the DataFrame. You can also select rows that meet more complex logical conditions.

For example, suppose you have a DataFrame of wine reviews and you need wines from Italy with a score of at least 90.

```python
reviews.country == 'Italy'
```

This condition returns a Series of boolean values:

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` is label-based, but it also accepts a boolean array or an alignable boolean Series](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). Thus you can select only Italian wines like this:

```python
reviews.loc[reviews.country == 'Italy']
```

Combine multiple conditions with `&` and `|`. Italian wines with scores ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Italian wines **or** wines with scores ≥ 90:

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Pandas also provides helpful built-in selectors, notably `isin` and `isna`/`notna`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) returns a boolean mask indicating whether each value is in a given list. For example, select wines from Italy or France:

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

Use [`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) to filter missing values (`NaN`). For example, select rows with non-missing prices:

```python
reviews.loc[reviews.price.notna()]
```

> Note: Although not mentioned in the original Kaggle course, [`iloc` can also take a boolean array](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Unlike `loc`, it supports arrays but not Series, so the kinds of alignable boolean masking shown above aren’t directly applicable.
{: .prompt-tip }

### Assigning data
You can add new data to a DataFrame or overwrite existing columns.

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
### Quick summaries
The [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) method provides a high-level summary of a given column.

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

The output of `describe()` depends on the data type. For non-numeric (string) data:

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

You can also compute specific statistics directly:

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

To count occurrences of unique values, use [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html):

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

### Maps
A **map** is a function that transforms elements from one set to another. In data science, we often need to transform data into other representations; maps are essential for such tasks.

Two methods are used frequently.

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) takes a function that converts a single <u>value</u> to another single value, applies it to every value in the <u>Series</u>, and returns a new Series. For example, to subtract the mean from each wine score:

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) applies a custom function to each <u>row</u> (or column) of a <u>DataFrame</u>.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Call `apply()` with `axis='index'` to apply a function column-wise instead of row-wise.

Both `Series.map()` and `DataFrame.apply()` return new transformed objects and do not modify the original data.

| Method | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Target | Series | DataFrame |
| Granularity | Apply per value <br>(if you regard a Series as a [column vector](/posts/vector-spaces-subspaces-and-matrices/#row-and-column-vectors), this is row-wise) | Row-wise by default <br> Can be column-wise with an option |

> Note that [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) and [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html) also exist.
> - `Series.apply()`:
>   - `by_row='compat'` (default): behaves like `Series.map()`
>   - `by_row=False`: passes the entire Series to the function at once (similar to `DataFrame.apply()` with `axis='index'`)
> - `DataFrame.map()`: applies a function to each individual value in the DataFrame (analogous to `Series.map()` but for DataFrames)
{: .prompt-tip }

Pandas also provides many common vectorized transformations natively. The example above can be written much more simply, and pandas will still infer and perform the intended operation:

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

Pandas supports operations between Series of the same length, too. In the wine example, you can concatenate strings across two columns:

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

These vectorized operations use pandas’ internal acceleration and are faster than `map()` or `apply()`. Still, `map()` and `apply()` are more flexible and can handle more complex transformations, so they’re good to know.
