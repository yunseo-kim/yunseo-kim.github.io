---
title: Summary of Kaggle-Pandas Course Content
description: Summarized the content of the Pandas mini-course among Kaggle's public courses.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.jpg
---
# Pandas
Solve short hands-on challenges to perfect your data manipulation skills.

## Lesson 1. Creating, Reading and Writing
### Importing Pandas
```python
import pandas as pd
```
Pandas has two core objects: **DataFrame** and **Series**.

### DataFrame
A DataFrame is a table. It contains an array of individual *entries*, each of which has a certain *value*. Each entry corresponds to a *row* (or *record*) and a *column*. DataFrame entries don't need to be integers.
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```
DataFrames are declared using Python's dictionary format. The keys are column names, and the values are lists of items to be entered.

Usually when declaring a DataFrame, column labels are assigned the name of that column, but row labels are assigned integers 0, 1, 2... If needed, row labels can be manually specified. The list of row labels in a DataFrame is called the **Index**, and can be set using the ```index``` parameter.
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

### Series
A Series is a sequence of data values.
```python
pd.Series([1, 2, 3, 4, 5])
```
A Series is essentially a single column of a DataFrame. Therefore, you can also specify an index. The difference is that instead of a 'column name', it has a 'name', ```name```.
```python
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
```
Series and DataFrames are closely related. It helps to think of a DataFrame as just a bunch of Series put together.

### Reading Data Files
In many cases, rather than creating data directly, you use existing data. Data can be stored in various formats, but the most basic form is a CSV file. The contents of a CSV file typically look like this:
```
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```
A CSV file is a table where each value is separated by commas (comma). That's why it's called "Comma-Separated Values", CSV.

To load data in CSV file format into a DataFrame, use the ```pd.read_csv()``` function.

You can check the size of a DataFrame using the ```shape``` attribute.

You can view the first five rows of a DataFrame using the ```head()``` command.

The ```pd.read_csv()``` function has over 30 parameters. For example, if the CSV file you're trying to load contains its own index, you can specify the value of the ```index_col``` parameter to use that column as the index instead of Pandas automatically assigning an index.

### Writing Data
You can export a DataFrame to a CSV file using the ```to_csv()``` method. Use it like this:
```python
(DataFrame name).to_csv("(CSV file path)")
```

## Lesson 2. Indexing, Selecting & Assigning
Selecting specific values to use from a Pandas DataFrame or Series is a step in almost every data-using task.
