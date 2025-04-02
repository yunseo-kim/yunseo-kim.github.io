---
title: Kaggle-Pandas 課程內容整理
description: 整理了 Kaggle 公開課程中 Pandas 迷你課程的內容。
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.jpg
---
# Pandas
通過解決簡短的實踐挑戰來完善你的數據操作技能。

## 課程 1. 創建、讀取和寫入
### 導入 Pandas
```python
import pandas as pd
```
Pandas 有兩個核心對象：**數據框（DataFrame）**和**序列（Series）**。

### 數據框
數據框（DataFrame）是一個表格。它包含一個由個別*條目（entries）*組成的矩陣，每個條目都有一個特定的*值（value）*，並對應於一個*行*（*row* 或 *record*）和一個列（column）。數據框的條目不一定要是整數。
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```
數據框的聲明使用 Python 的字典（dictionary）格式。鍵（key）是列名，值（value）是由要填入的項目組成的列表（list）。

通常在聲明數據框時，列標籤會被分配該列的名稱，但行標籤會被分配 0、1、2...等整數。如果需要，可以手動指定行標籤。在數據框中，行標籤的列表被稱為**索引（Index）**，可以使用 ```index``` 參數來指定值。
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

### 序列
序列（Series）是一個由數據值組成的序列。
```python
pd.Series([1, 2, 3, 4, 5])
```
序列本質上與數據框的單一列相同。因此，同樣可以指定索引。不過，區別在於它有一個 '名稱'，```name```，而不是 '列名'。
```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```
序列和數據框密切相關。可以將數據框視為序列的集合，這有助於理解。

### 讀取數據文件
在許多情況下，我們會使用已有的數據而不是直接創建數據。數據可能以各種格式存儲，最基本的形式是 CSV 文件。CSV 文件的內容通常如下所示：
```
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```
也就是說，CSV 文件是一個用逗號（comma）分隔每個值的表格。這就是為什麼它被稱為 "逗號分隔值"（Comma-Separated Values），即 CSV。

當讀取 CSV 格式的數據到數據框時，我們使用 ```pd.read_csv()``` 函數。

可以使用 ```shape``` 屬性來檢查數據框的大小。

可以使用 ```head()``` 命令來查看數據框的前五行。

```pd.read_csv()``` 函數有超過 30 個參數。例如，如果要讀取的 CSV 文件本身包含索引，可以指定 ```index_col``` 參數的值，使 Pandas 使用該列作為索引，而不是自動生成索引。

### 寫入數據
可以使用 ```to_csv()``` 方法將數據框導出為 CSV 文件。使用方法如下：
```python
(數據框名稱).to_csv("(CSV 文件路徑)")
```

## 課程 2. 索引、選擇和賦值
從 Pandas 數據框或序列中選擇特定的值是幾乎所有數據操作工作中的一個步驟。
