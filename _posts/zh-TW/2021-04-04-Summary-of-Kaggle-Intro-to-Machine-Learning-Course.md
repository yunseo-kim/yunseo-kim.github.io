---
title: Kaggle-機器學習入門課程內容整理
description: 總結了Kaggle公開課程中'機器學習入門'的內容。
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
---
我決定要學習[Kaggle公開課程](https://www.kaggle.com/learn/overview)。
每完成一門課程，我計劃簡單總結該課程的內容。第一篇文章是**機器學習入門**課程的摘要。

# 機器學習入門
學習機器學習的核心概念，並建立你的第一個模型。

## 第1課. 模型如何運作
一開始輕鬆地入門。這是關於機器學習模型如何運作以及如何使用的內容。以需要預測房地產價格的情況為例，用簡單的決策樹（Decision Tree）分類模型來解釋。

從數據中找出模式被稱為**訓練**模型（**fitting** or **training** the model）。用於訓練模型的數據稱為**訓練數據（training data）**。完成訓練後，可以將此模型應用於新數據進行**預測（predict）**。

## 第2課. 基本數據探索
在任何機器學習項目中，首先要做的是讓開發者自己熟悉數據。首先要了解數據具有什麼特性，才能設計適合的模型。為了探索和操作數據，幾乎必須使用Pandas（pandas）庫，這裡介紹了關於Pandas的基本內容。

Pandas庫的核心是數據框（DataFrame），可以將數據框想像成一種表格。它類似於Excel的工作表或SQL數據庫的表格。可以使用read_csv方法來讀取CSV格式的數據。
```python
# 將文件路徑保存為變量以便隨時輕鬆訪問是個好習慣。
file_path = '（文件路徑）'
# 讀取數據並保存為名為'data_1'的數據框（當然，實際上最好使用易於理解的名稱）。
data_1 = pd.read_csv(file_path)
```
可以使用describe方法查看數據的摘要信息。
```python
data_1.describe()
```
然後可以查看8項信息：
- **count**：實際包含值的行數（不包括缺失值）
- **mean**：平均值
- **std**：標準差
- **min**：最小值
- **25%**：下四分位數
- **50%**：中位數
- **75%**：上四分位數
- **max**：最大值

## 第3課. 你的第一個機器學習模型
### 數據處理
需要決定在給定的數據中使用哪些變量進行建模。可以使用數據框的**columns**屬性來查看列標籤。
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
從給定數據中選擇所需部分的方法有多種，Kaggle的[Pandas微課程](https://www.kaggle.com/learn/pandas)中會深入討論（我稍後也會總結這個內容）。這裡使用以下兩種方法：
1. 點符號
2. 使用列表

首先，使用**點符號**選擇對應於**預測目標（prediction target）**的列。這時，這個單列存儲在**序列（Series）**中。序列大致可以理解為只由一列組成的數據框。按慣例，預測目標稱為**y**。
```python
y = melbourne_data.Price
```

輸入到模型中用於預測的列稱為"特徵（features）"。對於給定的墨爾本房價數據，這些將是用於預測房價的列。有時會使用給定數據中除預測目標外的所有列作為特徵，有時選擇其中的一部分可能更好。  
可以像下面這樣使用列表選擇多個特徵。這時，列表中的所有元素都必須是字符串。
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
按慣例，這個數據稱為**X**。
```python
X = melbourne_data[melbourne_features]
```

分析數據時，除了describe之外，head也是一個有用的方法。它顯示前5行。
```python
X.head()
```

### 模型設計
在建模階段，通常使用**scikit-learn（scikit-learn）**庫。設計和使用模型的過程大致如下：
- **定義（Define）**：決定模型的類型和參數（parameters）。
- **訓練（Fit）**：從給定數據中找出規律性。這是建模的核心。
- **預測（Predict）**：使用經過訓練的模型進行預測。
- **驗證（Evaluate）**：評估模型預測的準確度。

以下是使用scikit-learn定義和訓練模型的示例：
```python
from sklearn.tree import DecisionTreeRegressor

# 定義模型。指定random_state的數值以確保每次運行都得到相同的結果
melbourne_model = DecisionTreeRegressor(random_state=1)

# 訓練模型
melbourne_model.fit(X, y)
```

許多機器學習模型在訓練過程中具有一定程度的隨機性。通過指定```random_state```值，可以確保每次運行都得到相同的結果，除非有特殊原因，否則指定它是個好習慣。使用任何值都可以。

完成模型訓練後，可以像這樣進行預測：
```python
print("對以下5棟房子進行預測：")
print(X.head())
print("預測結果是")
print(melbourne_model.predict(X.head()))
```

## 第4課. 模型驗證
### 模型驗證方法
要不斷改進模型，就需要衡量模型的性能。使用某個模型進行預測時，會有正確的情況，也會有錯誤的情況。這時需要一個指標來檢查這個模型的預測性能。有各種類型的指標，這裡使用**MAE（Mean Absolute Error，平均絕對誤差）**。

對於墨爾本房價預測，每個房價的預測誤差如下：  
```
error = actual - predicted
```
MAE是通過取每個預測誤差的絕對值，然後計算這些絕對誤差的平均值來計算的。可以用scikit-learn這樣實現：
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### 使用訓練數據進行驗證的問題
在上面的代碼中，我們使用同一個數據集進行了模型訓練和驗證。但這樣做是不對的。這門課程舉了一個例子來解釋原因。

> 在實際的房地產市場中，門的顏色與房價無關。  
> 
> 然而，碰巧在用於訓練的數據中，所有有綠色門的房子都非常昂貴。模型的作用是從數據中找出可用於預測房價的規律性，所以在這種情況下，我們的模型會檢測到這種規律性，並預測有綠色門的房子價格會很高。
> 
> 如果這樣進行預測，對於給定的訓練數據來說，看起來會很準確。
> 
> 然而，當對"有綠色門的房子很貴"這個規則不適用的新數據進行預測時，這個模型會非常不準確。

模型只有在對新數據進行預測時才有意義，所以我們應該使用未用於模型訓練的數據進行驗證。最簡單的方法是在建模過程中分離出一部分數據用於性能測量。這些數據稱為**驗證數據（validation data）**。

### 分離驗證數據集
scikit-learn庫有一個```train_test_split```函數可以將數據分成兩部分。以下代碼將數據分成兩部分，一部分用於訓練，另一部分用於```mean_absolute_error```測量的驗證：
```python
from sklearn.model_selection import train_test_split

# 將特徵和目標都分割為訓練和驗證數據
# 分割基於隨機數生成器。為random_state參數提供一個數值可以確保
# 每次運行此腳本時都得到相同的分割。
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# 定義模型
melbourne_model = DecisionTreeRegressor()
# 訓練模型
melbourne_model.fit(train_X, train_y)

# 在驗證數據上獲取預測價格
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## 第5課. 欠擬合和過擬合
### 過擬合和欠擬合
- **過擬合（overfitting）**：模型非常準確地適應訓練數據集，但對驗證數據集或其他新數據無法進行正確預測的現象
- **欠擬合（underfitting）**：模型無法找到給定數據中重要的特徵和規律性，導致即使在訓練數據集上也無法進行正確預測的現象

下圖中的綠線表示過擬合的模型，黑線表示理想的模型。
![過擬合](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *圖片來源*
> - 作者：西班牙維基百科用戶 [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - 許可：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

對我們來說重要的是新數據的預測準確度，我們使用驗證數據集來估計新數據的預測性能。我們的目標是找到欠擬合和過擬合之間的最佳點（sweet spot）。  
![](https://i.imgur.com/2q85n9s.png)  
這門課程一直以決策樹分類模型為例進行解釋，但過擬合和欠擬合是適用於所有機器學習模型的概念。

### 超參數（hyperparameter）調整
以下示例是通過改變決策樹模型的*max_leaf_nodes*參數值來比較測量模型性能的代碼。（省略了加載數據和分離驗證數據集的部分）
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
# 比較不同max_leaf_nodes值的MAE
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("最大葉節點數：%d  \t\t 平均絕對誤差：  %d" %(max_leaf_nodes, my_mae))
```
完成超參數調整後，最後用全部數據訓練模型以最大化性能。因為不再需要分離驗證數據集。

## 第6課. 隨機森林
同時使用多個不同的模型可以比單一模型表現更好。**隨機森林（random forest）**就是一個很好的例子。

隨機森林由眾多決策樹組成，通過取每棵樹的預測值的平均來進行最終預測。在許多情況下，它比單一決策樹有更好的預測準確度，即使使用默認參數也能很好地工作。
