---
title: "Kaggle-機械学習入門コースの内容まとめ"
description: >-
  Kaggleの公開コース「Intro to Machine Learning」の内容を要約しました。
categories: [Data Science, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
toc: true
toc_sticky: true
---

[Kaggleの公開コース](https://www.kaggle.com/learn/overview)を勉強することにしました。
各コースを修了するたびに、そのコースの内容を簡単にまとめる予定です。最初の記事は**Intro to Machine Learning**コースの要約です。

# Intro to Machine Learning
機械学習の核心的なアイデアを学び、最初のモデルを構築します。

## Lesson 1. How Models Work
最初は負担なく軽く始めます。機械学習モデルがどのように動作し、どのように使用されるかについての内容です。不動産価格予測をしなければならない状況を想定しながら、簡単な決定木(Decision Tree)分類モデルを例に説明しています。

データからパターンを見つけ出すことをモデルを**訓練**すると言います(**fitting** or **training** the model)。モデルを訓練する際に使用するデータを**訓練データ(training data)**と言います。訓練が終わると、このモデルを新しいデータに適用して**予測(predict)**することができます。

## Lesson 2. Basic Data Exploration
どんな機械学習プロジェクトでも、最初にすべきことは開発者自身がそのデータに慣れることです。データがどのような特性を持っているかをまず把握しなければ、それに適したモデルを設計することができません。データを探索し操作する用途でほぼ必須的にパンダス(Pandas)ライブラリを使用しますが、このパンダスに関する基本的な内容です。

パンダスライブラリの核心はデータフレーム(DataFrame)ですが、このデータフレームは一種の表のようなものだと考えればいいです。ExcelのシートやSQLデータベースのテーブルに似ています。read_csvメソッドを使用してCSV形式のデータを読み込むことができます。
```python
# 必要なときに簡単にアクセスできるようにファイルパスを変数として保存するのが良いです。
file_path = '(ファイルパス)'
# データを読み込んで'data_1'という名前のデータフレームとして保存します(もちろん実際には分かりやすい名前を使うのが良いです)。
data_1 = pd.read_csv(file_path)
```
describeメソッドを使用してデータの要約情報を確認できます。
```python
data_1.describe()
```
すると8項目の情報を確認できます。
- **count**: 実際の値が入っている行の数(値が欠落しているものは除外)
- **mean**: 平均
- **std**: 標準偏差
- **min**: 最小値
- **25%**: 下位25%の値
- **50%**: 中央値
- **75%**: 下位75%の値
- **max**: 最大値

## Lesson 3. Your First Machine Learning Model
### データ加工
与えられたデータからどの変数をモデリングに活用するかを決定する必要があります。データフレームの**columns**属性を利用して列ラベルを確認できます。
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
与えられたデータから必要な部分を選び出す方法は様々ですが、Kaggleの[Pandas Micro-Course](https://www.kaggle.com/learn/pandas)で深く扱うそうです(この内容も後でまとめる予定です)。ここでは次の2つの方法を使用します。
1. Dot notation
2. リストの使用

まず、**dot-notation**で**予測対象(prediction target)**に該当する列を選び出します。このとき、この単一の列は**シリーズ(Series)**に保存します。シリーズは大まかに1つの列だけで構成されたデータフレームだと考えればいいです。慣習的に予測対象は**y**で表します。
```python
y = melbourne_data.Price
```

予測のためにモデルに入力する列を「特徴量(features)」と言います。例として与えられたメルボルンの家価格データの場合は、家価格予測に使用する列になります。与えられたデータから予測対象を除いたすべての列を特徴量として使用することもあれば、その中から一部だけを選び出して使用する方が良い場合もあります。  
以下のようにリストを使用して複数の特徴量を選び出すことができます。このときこのリストのすべての要素は文字列でなければなりません。
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
慣習的にこのデータは**X**で表します。
```python
X = melbourne_data[melbourne_features]
```

データを分析する際にdescribe以外に有用に使用できるメソッドとしてheadもあります。最初の5行を表示します。
```python
X.head()
```

### モデル設計
モデリング段階では通常**scikit-learn**ライブラリをよく使用します。モデルを設計し使用するプロセスは大きく次のようになります。
- **モデル定義(Define)**: モデルの種類とパラメータを決定します。
- **訓練(Fit)**: 与えられたデータから規則性を見つけ出します。モデリングの核心です。
- **予測(Predict)**: 訓練を経たモデルで予測を行います。
- **検証(Evaluate)**: モデルの予測がどれほど正確かを評価します。

以下はscikit-learnでモデルを定義し訓練する例です。
```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

多くの機械学習モデルは訓練過程である程度のランダム性を持っています。```random_state```値を指定することで、毎回の実行で同じ結果を得るようにすることができ、特別な理由がなければ指定するのが良い習慣です。どの値を使用しても構いません。

モデル訓練を完了すると、次のように予測を行うことができます。
```python
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
```

## Lesson 4. Model Validation
### モデル検証方法
モデルを繰り返し改善していくには、モデルの性能を測定する必要があります。あるモデルを使用して予測を行った場合、当たる場合もあれば外れる場合もあるでしょう。このとき、このモデルの予測性能を確認するための指標が必要です。様々な種類の指標がありますが、ここでは**MAE(Mean Absolute Error, 平均絶対誤差)**を使用します。

メルボルンの家価格予測の場合、それぞれの家価格に対する予測誤差は次のようになります。  
```
error=actual−predicted
```
MAEは各予測誤差の絶対値を取り、この絶対誤差の平均を求めることで計算します。scikit-learnで次のように実装できます。
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### 訓練データを検証に使用することの問題点
上のコードでは1つのデータセットでモデル訓練と検証を両方行いました。しかし、このようにしてはいけません。このコースでは1つの例を挙げて理由を説明しています。

> 実際の不動産市場ではドアの色は家価格とは無関係です。
> 
> しかし、偶然にも訓練に使用したデータでは緑色のドアを持つ家はすべて非常に高価だとします。モデルの役割はデータから家価格予測に活用できるような規則性を見つけ出すことなので、この場合、我々のモデルはこの規則性を検出し、緑のドアを持つ家は価格が高いと予測するでしょう。
> 
> このように予測を行えば、与えられた訓練データに対しては正確に見えるでしょう。
> 
> しかし、「緑のドアを持つ家は高価だ」というルールが通用しない新しいデータに対して予測を行うと、このモデルは非常に不正確になるでしょう。

モデルは新しいデータから予測を行ってこそ意味があるので、我々はモデル訓練に使用していないデータを使用して検証を行う必要があります。最も簡単な方法は、モデリング過程で一部のデータを分離して性能測定用として使用することです。このデータを**検証データ(validation data)**と言います。

### 検証データセットの分離
scikit-learnライブラリにはデータを2つに分割する```train_test_split```関数があります。以下のコードはデータを2つに分割し、1つは訓練用として使用し、もう1つは```mean_absolute_error```測定のための検証用として使用するコードです。
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
### 過学習と過少学習
- **過学習(overfitting)**: モデルが訓練データセットにのみ非常に正確に適合し、検証データセットや他の新しいデータに対しては適切に予測できない現象
- **過少学習(underfitting)**: モデルが与えられたデータから重要な特徴と規則性を見つけ出せず、訓練データセットでも適切に予測できない現象

以下の画像の緑色の線が過学習したモデルを表し、黒色の線が望ましいモデルを表します。
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *画像出典*
> - 作者: スペインのウィキペディアユーザー [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - ライセンス: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

我々にとって重要なのは新しいデータでの予測精度であり、検証データセットを用いて新しいデータでの予測性能を推定します。過少学習と過学習の間の最適点(sweet spot)を見つけることが目標です。  
![](https://i.imgur.com/2q85n9s.png)  
このコースでは引き続き決定木分類モデルを例に説明していますが、過学習と過少学習はすべての機械学習モデルに適用される概念です。

### ハイパーパラメータ(hyperparameter)チューニング
以下の例は決定木モデルの*max_leaf_nodes*引数の値を変えながらモデルの性能を比較測定するコードです。(データを読み込み、検証データセットを分離する部分は省略)
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
ハイパーパラメータチューニングを完了したら、最後に全データでモデルを訓練させて性能を最大化します。もはや検証データセットを分離しておく必要がないためです。

## Lesson 6. Random Forests
異なる複数のモデルを一緒に使用すると、単一モデルよりも良い性能を出すことができます