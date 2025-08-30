---
title: "Kaggle「Intro to Machine Learning」講座の内容まとめ"
description: "機械学習の主要概念とpandas・scikit-learnの基本的な使い方を整理。Kaggleの公開講座「Intro to Machine Learning」の内容を日本語で簡潔に要約します。"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

[Kaggle 公開コース](https://www.kaggle.com/learn)を学ぶことにした。
各コースを修了するたびに、その過程で学んだ内容を簡単にまとめる予定だ。最初の記事は [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) コースの要約である。

![修了証明書](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lesson 1. How Models Work
まずは肩慣らしとして、機械学習モデルがどのように動作し、どのように使われるかを概観する。住宅価格予測を行う状況を仮定し、簡単な決定木（Decision Tree）分類モデルを例に説明している。

データから規則性を見つけ出すことをモデルを**訓練**する（**fitting** or **training** the model）という。モデルの訓練に用いるデータを**訓練データ（training data）**と呼ぶ。訓練が終わると、このモデルを新しいデータに適用して**予測（predict）**できる。

## Lesson 2. Basic Data Exploration
どんな機械学習プロジェクトでも、最初にすべきことは、開発者自身がそのデータに慣れることだ。データの特性を把握してこそ、適切なモデルを設計できる。データの探索や加工には、通常 [パンダス（Pandas）](https://pandas.pydata.org/) ライブラリを用いる。

```python
import pandas as pd
```

パンダスの中核はデータフレーム（DataFrame）で、表計算のシートやSQLデータベースのテーブルに似ている。read_csvメソッドを使ってCSV形式のデータを読み込める。

```python
# 必要なときに簡単に参照できるよう、ファイルパスを変数に保存しておくとよい。
file_path = "(ファイルパス)"
# データを読み込み、'example_data' という名前のデータフレームに保存する（実際にはもっと分かりやすい名前にするのが望ましい）。
example_data = pd.read_csv(file_path)
```

describeメソッドでデータの要約統計を確認できる。

```python
example_data.describe()
```

すると8項目の情報が得られる。
- **count**: 実値が入っている行数（欠損は除外）
- **mean**: 平均
- **std**: 標準偏差
- **min**: 最小値
- **25%**: 第25百分位数
- **50%**: 中央値
- **75%**: 第75百分位数
- **max**: 最大値

## Lesson 3. Your First Machine Learning Model
### データ加工
与えられたデータから、どの変数をモデル化に使うかを決める。データフレームの**columns**属性で列ラベルを確認できる。

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

必要な部分を抽出する方法は複数あるが、Kaggle の [Pandas マイクロコース](https://www.kaggle.com/learn/pandas)でより深く扱われている（これも後日まとめる予定）。ここでは次の2つを使う。
1. ドット表記
2. リストの使用

まず**ドット表記**で**予測対象（prediction target）**に当たる列を抜き出して**シリーズ（Series）**として保存する。シリーズは1列だけで構成されたデータフレームのようなものだ。予測対象は**y**と表すのが慣習である。

```python
y = melbourne_data.Price
```

予測のためモデルに入力する列を「特徴量（features）」という。メルボルンの住宅価格データでは、価格予測に使う各列がそれに当たる。予測対象以外のすべての列を特徴量にしてもよいし、その一部だけを選ぶほうがよい場合もある。  
以下のようにリストで複数の特徴量を選べる。このリストの要素はすべて文字列でなければならない。

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

このデータは**X**と表すのが慣習である。

```python
X = melbourne_data[melbourne_features]
```

データ解析では、describe以外にheadも便利だ。先頭5行を表示する。

```python
X.head()
```

### モデル設計
モデリング段階では状況に応じてさまざまなライブラリを使うが、よく使われるもののひとつが[サイキットラーン（scikit-learn）](https://scikit-learn.org/stable/)である。モデルの設計と利用は大きく次の流れになる。
- **定義（Define）**: モデルの種類とパラメータ（parameters）を決める。
- **訓練（Fit）**: 与えられたデータから規則性を見つける。モデリングの中核だ。
- **予測（Predict）**: 訓練済みモデルで予測する。
- **評価（Evaluate）**: 予測の正確さを評価する。

以下はサイキットラーンでモデルを定義し訓練する例である。

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

多くの機械学習モデルは訓練過程にある程度のランダム性を持つ。`random_state`を指定すれば、毎回同じ結果を再現できる。特別な理由がなければ指定しておくのがよい習慣だ。値は何でもよい。

訓練が完了したら、次のように予測を行える。

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

## Lesson 4. Model Validation
### モデル検証の方法
モデルを反復的に改善するには、その性能を測る必要がある。あるモデルで予測すれば、当たることも外れることもある。そこで予測性能を評価する指標が必要だ。指標は様々あるが、ここでは**MAE（Mean Absolute Error, 平均絶対誤差）**を用いる。

メルボルンの住宅価格予測では、各住宅の予測誤差は次のようになる。

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

MAEは各予測誤差の絶対値を取り、その絶対誤差の平均を求めることで計算する。

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

サイキットラーンでは次のように求められる。

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### 訓練データで検証することの問題点
上のコードでは、ひとつのデータセットで訓練と検証を両方行っている。しかし実はこれは避けるべきだ。Kaggleの講座では次の例で理由を説明している。

> 実際の不動産市場では、ドアの色は価格と無関係だ。  
> 
> ところが、たまたま訓練に使ったデータでは緑色のドアの家がどれも非常に高価だった。モデルの役割は、データから価格予測に使える規則性を見つけることなので、この場合モデルはその規則を検知し、緑のドアの家は高いと予測してしまう。 
>
> このように予測すれば、与えられた訓練データに対しては正確に見えるだろう。
>
> しかし「緑のドアの家は高い」という規則が通用しない新しいデータに対しては、このモデルは非常に不正確になる。

モデルは新しいデータで予測してこそ意味がある。したがって、訓練に使っていないデータで検証すべきだ。最も簡単なのは、モデリングの途中で一部のデータを切り出して性能測定専用に使う方法である。このデータを**検証データ（validation data）**という。

### 検証データセットの分割
サイキットラーンにはデータを2分割する`train_test_split`関数がある。次のコードは、データを訓練用と検証用に分け、後者でMAE（`mean_absolute_error`）を測る例である。

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

## Lesson 5. Underfitting and Overfitting
### 過学習と過少適合
- **過学習（overfitting）**: モデルが訓練データにだけ非常にうまく当てはまり、検証データや他の未知データでは予測できない現象
- **過少適合（underfitting）**: モデルが重要な特徴や規則性を十分に捉えられず、訓練データでさえ性能が不足する現象

下図のようなデータで、赤点と青点を分類するモデルを学習させる状況を考える。この場合、緑の線は過学習したモデルで、黒の線が望ましいモデルを表す。
![過学習](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *画像出典*
> - 著作者: スペイン語版ウィキペディアのユーザー イグナシオ・イッケ（Ignacio Icke）
> - ライセンス: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

重要なのは未知データでの予測精度であり、検証データセットを使って未知データでの性能を推定する。過少適合と過学習のあいだの最適点（sweet spot）を見つけるのが目標だ。  
![](https://i.imgur.com/2q85n9s.png)  
このKaggle講座では引き続き決定木分類モデルを例に説明しているが、過学習と過少適合はあらゆる機械学習モデルに当てはまる概念である。

### ハイパーパラメータ（hyperparameter）チューニング
以下は決定木モデルの*max_leaf_nodes*引数の値を変えながら、性能を比較測定するコード例である（データの読み込みや検証データセットの分割は省略）。

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

ハイパーパラメータのチューニングを終えたら、最後は手元の全データでモデルを訓練して性能を最大化する。もはや検証データセットを取り分ける必要はないからだ。

## Lesson 6. Random Forests
複数の異なるモデルを組み合わせると、単一モデルより良い性能を出せることがある。これを**アンサンブル（Ensemble）**といい、**ランダムフォレスト（random forest）**が代表例である。

ランダムフォレストは多数の決定木で構成され、各木の予測値の平均をとって最終予測を出す。多くの場合、単一の決定木より高い予測精度を示す。
