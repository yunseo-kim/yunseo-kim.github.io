---
title: "Kaggle「Intro to Machine Learning」課程內容整理"
description: "整理機器學習核心概念與 pandas、scikit-learn 的基礎用法，並摘要 Kaggle 公開課程「Intro to Machine Learning」的重點與範例程式碼，快速掌握入門要點。"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

我決定學習 [Kaggle 公開課程](https://www.kaggle.com/learn)。
每完成一門課，就簡要整理透過該課程所學的內容。第一篇是 [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) 課程的摘要。

![結業證書](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lesson 1. 模型如何運作（How Models Work）
先從輕鬆的內容開始：機器學習模型如何運作、如何被使用。以需要預測不動產價格為例，說明簡單的決策樹（Decision Tree）分類模型。

從資料找出模式的過程稱為對模型進行**訓練**（**fitting** or **training** the model）。用於訓練模型的資料稱為**訓練資料（training data）**。訓練完成後，便可將模型套用到新資料進行**預測（predict）**。

## Lesson 2. 基礎資料探索（Basic Data Exploration）
在任何機器學習專案中，第一步是讓自己熟悉資料。先掌握資料的特性，才能設計合適的模型。用於探索與操作資料通常會使用 [Pandas（Pandas）](https://pandas.pydata.org/) 函式庫。

```python
import pandas as pd
```

Pandas 的核心是資料框（DataFrame），可以把它想成一種表格，類似 Excel 的工作表或 SQL 資料庫的資料表。可用 read_csv 方法讀取 CSV 格式的資料。

```python
# 建議先把檔案路徑存成變數，之後要用更方便。
file_path = "(檔案路徑)"
# 讀取資料並存成名為 'example_data' 的資料框（實務上最好用更易懂的名稱）。
example_data = pd.read_csv(file_path)
```

使用 describe 方法可以查看資料的摘要統計。

```python
example_data.describe()
```

可看到 8 個欄位資訊：
- **count**: 含有效值的列數（排除遺漏值）
- **mean**: 平均數
- **std**: 標準差
- **min**: 最小值
- **25%**: 第 25 百分位數
- **50%**: 中位數
- **75%**: 第 75 百分位數
- **max**: 最大值

## Lesson 3. 你的第一個機器學習模型（Your First Machine Learning Model）
### 資料處理
必須決定要用哪些變數來建模。可用資料框的 **columns** 屬性查看欄標籤。

```python
import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```

```python
Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
       'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
       'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
       'Longtitude', 'Regionname', 'Propertycount'],
      dtype='object')
```

從給定資料中挑選所需部分的方法很多，Kaggle 的 [Pandas Micro-Course](https://www.kaggle.com/learn/pandas) 有更深入的說明（之後也會整理）。此處用兩種方法：
1. Dot notation
2. 使用清單（list）

首先用**dot-notation**取出**預測目標（prediction target）**對應的欄，並存為**序列（Series）**。序列可視為只包含單一欄位的資料框。慣例以 **y** 表示預測目標。

```python
y = melbourne_data.Price
```

輸入模型用來進行預測的欄位稱為「特徵（features）」。在墨爾本房價資料中，就是用來預測房價的各欄位。有時會用除預測目標外的所有欄為特徵，有時只取其中一部分。  
如下可用清單一次取出多個特徵；清單元素需為字串。

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

慣例以 **X** 表示特徵資料。

```python
X = melbourne_data[melbourne_features]
```

除了 describe，head 也是分析資料時很實用的方法，可顯示前 5 列。

```python
X.head()
```

### 模型設計
建模時會用到各種函式庫，其中常用之一是 [Scikit-learn（scikit-learn）](https://scikit-learn.org/stable/)。設計與使用模型大致包括：
- **模型定義（Define）**：決定模型種類與參數（parameters）
- **訓練（Fit）**：從資料中找出規則性，這是建模的核心
- **預測（Predict）**：用訓練後的模型進行預測
- **評估（Evaluate）**：評估模型預測的準確度

以下是用 scikit-learn 定義與訓練模型的範例。

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

許多機器學習模型在訓練過程中帶有一定隨機性。透過指定 `random_state`，可讓每次執行得到相同結果；除非有特別理由，建議固定此值，使用哪個數字皆可。

訓練完成後，可如下進行預測：

```python
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
```

```
Making predictions for the following 5 houses:
   Rooms  Bathroom  Landsize  Lattitude  Longtitude
1      2       1.0     156.0   -37.8079    144.9934
2      3       2.0     134.0   -37.8093    144.9944
4      4       1.0     120.0   -37.8072    144.9941
6      3       2.0     245.0   -37.8024    144.9993
7      2       1.0     256.0   -37.8060    144.9954
The predictions are
[1035000. 1465000. 1600000. 1876000. 1636000.]
```

## Lesson 4. 模型驗證（Model Validation）
### 模型驗證方法
若要持續改進模型，就得量測其效能。用某模型做預測時，會有對也會有錯，因此需要衡量預測表現的指標。指標很多，這裡使用 **MAE（Mean Absolute Error，平均絕對誤差）**。

以墨爾本房價為例，每筆資料的預測誤差如下：

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

MAE 是將每個預測誤差取絕對值，再對這些絕對誤差取平均：

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

在 scikit-learn 中可如下計算：

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### 用訓練資料做驗證的問題
上面的程式碼用同一個資料集同時進行訓練與驗證，但其實不該這麼做。Kaggle 課程用以下例子說明原因：

> 在真實不動產市場中，門的顏色與房價無關。  
> 
> 但恰巧在用於訓練的資料裡，擁有綠色門的房子都很貴。模型的任務是從資料中找出可用於預測房價的規則性，因此它會偵測到這個關聯，並預測綠色門的房子較昂貴。
>
> 以這種方式進行預測，對於給定的訓練資料看起來會很準確。
>
> 然而，當在新資料上這條「綠色門的房子很貴」的規則不成立時，模型就會非常不準確。

模型必須在新資料上也能做出良好預測才有意義，因此驗證時應使用未參與訓練的資料。最簡單的方法是在建模時預先保留一部分資料專供效能評估使用，稱為**驗證資料（validation data）**。

### 切分驗證資料集
scikit-learn 提供 `train_test_split` 函數可將資料分成兩部分。以下程式碼將資料切成訓練與驗證兩組，後者用來計算 MAE（`mean_absolute_error`）。

```python
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## Lesson 5. 欠擬合與過擬合（Underfitting and Overfitting）
### 過擬合與欠擬合
- **過擬合（overfitting）**：模型只在訓練資料上非常準確，對驗證或其他新資料表現不佳
- **欠擬合（underfitting）**：模型未能充分擷取資料的重要特徵與規則，以致連在訓練資料上表現也不足

想像要在下圖這樣的資料上學習一個分類紅點與藍點的模型。綠線代表過擬合模型，黑線代表較理想的模型。
![過擬合](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *圖片來源*
> - 作者：西班牙維基百科用戶 [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - 授權條款：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

我們關心的是在新資料上的預測準確度，會用驗證資料集來推估此表現。目標是找到欠擬合與過擬合之間的最佳平衡點（sweet spot）。  
![](https://i.imgur.com/2q85n9s.png)  
本 Kaggle 課程持續以決策樹分類模型為例說明，但過擬合與欠擬合是適用於所有機器學習模型的概念。

### 超參數（hyperparameter）調整
下例透過改變決策樹模型的 *max_leaf_nodes* 參數值，量測並比較模型表現（略去讀取資料與切出驗證集的部分）。

```python
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
```

```python
# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
```

完成超參數調整後，最後通常會用手上全部資料重新訓練模型以最大化效能，因為此時不再需要保留驗證集。

## Lesson 6. 隨機森林（Random Forests）
同時結合多個不同模型，往往能比單一模型得到更好的表現，這稱為**集成（Ensemble）**，而**隨機森林（random forest）**是很好的一個例子。

隨機森林由大量決策樹組成，最終預測是各樹預測值的平均。在多數情況下，比單一決策樹具有更佳的準確度。
