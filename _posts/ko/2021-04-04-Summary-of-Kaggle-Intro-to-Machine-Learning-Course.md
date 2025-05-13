---
title: Kaggle-Intro to Machine Learning 코스 내용 정리
description: Kaggle 공개 코스 중 'Intro to Machine Learning'의 내용을 요약하였다.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
---
[Kaggle 공개 코스들](https://www.kaggle.com/learn/overview)을 공부하기로 했다.
각 코스를 수료할 때마다 해당 코스의 내용을 간단히 정리할 계획이다. 첫 번째 글은 **Intro to Machine Learning** 코스의 요약이다.

# Intro to Machine Learning
Learn the core ideas in machine learning, and build your first models.

## Lesson 1. How Models Work
처음에는 부담 없이 가볍게 시작한다. 머신러닝 모델들이 어떻게 작동하고, 어떻게 사용되는지에 관한 내용이다. 부동산 가격 예측을 해야 하는 상황을 가정하면서 간단한 결정 트리(Decision Tree) 분류 모델을 예로 들어 설명하고 있다.

데이터로부터 패턴을 찾아내는 것을 모델을 **훈련**한다고 한다(**fitting** or **training** the model). 모델을 훈련할 때 사용하는 데이터를 **훈련 데이터(training data)**라고 한다. 훈련을 마치면 이 모델을 새로운 데이터에 적용해서 **예측(predict)**할 수 있다.

## Lesson 2. Basic Data Exploration
어떤 머신러닝 프로젝트에서든 가장 먼저 해야 할 일은 개발자 본인이 그 데이터에 익숙해지는 것이다. 데이터가 어떤 특성을 지니는지를 먼저 파악해야 그에 적합한 모델을 설계할 수 있다. 데이터를 탐색하고 조작하는 용도로 거의 필수적으로 판다스(Pandas) 라이브러리를 사용하는데, 이 판다스에 관한 기본적인 내용이다.

판다스 라이브러리의 핵심은 데이터프레임(DataFrame)인데, 이 데이터프레임은 일종의 표 같은 거라고 생각하면 된다. 엑셀의 시트나 SQL 데이터베이스의 테이블과 비슷하다. read_csv 메서드를 사용해서 CSV 형식 데이터를 불러올 수 있다.
```python
# 필요할 때마다 쉽게 접근하기 위해 파일 경로를 변수로 저장하는 것이 좋다.
file_path = '(파일 경로)'
# 데이터를 읽어들여서 'data_1'이라는 이름의 데이터프레임으로 저장한다(물론 실제로는 알아보기 쉬운 이름을 쓰는 것이 좋다).
data_1 = pd.read_csv(file_path)
```
describe 메서드를 사용해서 데이터의 요약 정보를 확인할 수 있다.
```python
data_1.describe()
```
그러면 8항목의 정보를 확인 가능하다.
- **count**: 실제 값이 들어 있는 행의 개수(값이 누락된 것은 제외)
- **mean**: 평균
- **std**: 표준편차
- **min**: 최솟값
- **25%**: 하위 25%의 값
- **50%**: 중간값
- **75%**: 하위 75%의 값
- **max**: 최댓값

## Lesson 3. Your First Machine Learning Model
### 데이터 가공
주어진 데이터에서 어떤 변수들을 모델링에 활용할 것인지 결정해야 한다. 데이터프레임의 **columns** 속성을 이용하여 열 레이블을 확인할 수 있다.
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
주어진 데이터에서 필요한 부분을 골라내는 방법은 여러 가지인데, 캐글의 [Pandas Micro-Course](https://www.kaggle.com/learn/pandas)에서 깊이 있게 다룬다고 한다(이 내용도 나중에 정리할 것이다). 여기서는 다음의 두 가지 방법을 사용한다.
1. Dot notation
2. 리스트 사용

우선, **dot-notation**으로 **예측 대상(prediction target)**에 해당하는 열을 골라낸다. 이때 이 단일 열은 **시리즈(Series)**에 저장한다. 시리즈는 대략 하나의 열로만 구성된 데이터프레임이라 생각하면 된다. 관습적으로 예측 대상은 **y**로 지칭한다.
```python
y = melbourne_data.Price
```

예측을 위해 모델에 입력하는 열들을 "특성(features)"이라고 한다. 예제로 주어진 멜버른 집값 데이터의 경우에는 집값 예측에 사용할 열들이 된다. 주어진 데이터에서 예측 대상을 제외한 모든 열들을 특성으로 사용할 때도 있고, 그 중 일부만 골라내어 사용하는 게 더 나을 때도 있다.  
아래와 같이 리스트를 사용하여 여러 개의 특성들을 골라낼 수 있다. 이때 이 리스트의 모든 요소들은 문자열이어야 한다.
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
관습적으로 이 데이터는 **X**로 지칭한다.
```python
X = melbourne_data[melbourne_features]
```

데이터를 분석할 때 describe 이외에 유용하게 사용할 수 있는 메서드로 head도 있다. 처음 5개의 행을 보여준다.
```python
X.head()
```

### 모델 설계
모델링 단계에서는 보통 **사이킷런(scikit-learn)** 라이브러리를 많이 사용한다. 모델을 설계하고 사용하는 과정은 크게 다음과 같다.
- **모델 정의(Define)**: 모델의 종류와 매개변수들(parameters)을 결정한다.
- **훈련(Fit)**: 주어진 데이터에서 규칙성을 찾아낸다. 모델링의 핵심이다.
- **예측(Predict)**: 훈련을 거친 모델로 예측을 수행한다.
- **검증(Evaluate)**: 모델의 예측이 얼마나 정확한지 평가한다.

아래는 사이킷런으로 모델을 정의하고 훈련하는 예시이다.
```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

많은 머신러닝 모델들은 훈련 과정에서 어느 정도 무작위성을 지니고 있다. ```random_state```값을 지정함으로써 매 실행마다 같은 결과를 얻도록 할 수 있으며, 특별한 이유가 없다면 지정하는 것이 좋은 습관이다. 어떤 값을 사용하든 상관없다.

모델 훈련을 완료하면 다음과 같이 예측을 수행할 수 있다.
```python
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
```

## Lesson 4. Model Validation
### 모델 검증 방법
모델을 반복적으로 개선해 나가려면 모델의 성능을 측정해야 한다. 어떤 모델을 이용하여 예측을 했을 때, 맞춘 경우도 있고 틀린 경우도 있을 것이다. 이때 이 모델의 예측 성능을 확인하기 위한 지표가 필요하다. 다양한 종류의 지표가 있는데, 여기서는 **MAE(Mean Absolute Error, 평균 절대 오차)**를 사용한다.

멜버른 집값 예측의 경우에, 각각의 집값에 대한 예측 오차는 다음과 같다.  
```
error=actual−predicted
```
MAE는 각각의 예측 오차의 절대값을 취하여 이 절대 오차들의 평균을 구함으로써 계산한다. 사이킷런으로 다음과 같이 구현할 수 있다.
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### 훈련 데이터를 검증에 사용하는 것의 문제점
위의 코드에서는 하나의 데이터셋으로 모델 훈련과 검증을 모두 수행하였다. 그런데 이렇게 하면 안 된다. 이 코스에서는 하나의 예시를 들어 이유를 설명하고 있다.

> 실제 부동산 시장에서 문의 색깔은 집값과는 무관하다.  
> 
>그러나 우연히도 훈련에 사용한 데이터에서는 초록색 문을 가진 집들은 모두 매우 비싸다고 한다. 모델의 역할은 데이터에서 집값 예측에 활용할 만한 규칙성을 찾아내는 것이므로, 이 경우 우리의 모델은 이 규칙성을 감지하고 초록 문을 가진 집은 가격이 비싸다고 예측할 것이다. 
>
> 이와 같이 예측을 수행한다면, 주어진 훈련 데이터에 대해서는 정확한 것처럼 보일 것이다.
>
> 그러나 "초록 문을 가진 집은 비싸다"라는 규칙이 통하지 않는 새로운 데이터에 대해 예측을 수행하면, 이 모델은 매우 부정확할 것이다.

모델은 새로운 데이터로부터 예측을 수행해야 의미가 있는 것이므로, 우리는 모델 훈련에 사용하지 않은 데이터를 사용하여 검증을 수행해야 한다. 가장 간단한 방법은 모델링 과정에서 일부 데이터를 분리하여 성능 측정용으로 사용하는 것이다. 이 데이터를 **검증 데이터(validation data)**라고 한다.

### 검증 데이터셋 분리
사이킷런 라이브러리에는 데이터를 둘로 분리하는 ```train_test_split``` 함수가 있다. 아래의 코드는 데이터를 둘로 분리하여 하나는 훈련용으로 사용하고, 다른 하나는 ```mean_absolute_error``` 측정을 위한 검증용으로 사용하는 코드이다.
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
### 과대적합과 과소적합
- **과대적합(overfitting)**: 모델이 훈련 데이터셋에만 매우 정확하게 들어맞고, 검증 데이터셋이나 다른 새로운 데이터에 대해서는 제대로 예측을 하지 못하는 현상
- **과소적합(underfitting)**: 모델이 주어진 데이터에서 중요한 특성과 규칙성을 찾아내지 못하여, 훈련 데이터셋에서도 제대로 예측을 하지 못하는 현상

아래 이미지의 초록색 선이 과대적합된 모델을 나타내며, 검은색 선이 바람직한 모델을 나타낸다.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *이미지 출처*
> - 저작자: 에스파냐 위키피디아 유저 [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - 라이선스: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

우리에게 중요한 것은 새로운 데이터에서의 예측 정확도이며, 검증 데이터셋을 이용하여 새로운 데이터에서의 예측 성능을 추산한다. 과소적합과 과대적합 간의 최적점(sweet spot)을 찾는 것이 목표이다.  
![](https://i.imgur.com/2q85n9s.png)  
이 코스에서는 계속해서 결정 트리 분류 모델을 예로 들어 설명하고 있지만, 과대적합과 과소적합은 모든 머신러닝 모델에 적용되는 개념이다.

### 하이퍼파라미터(hyperparameter) 튜닝
아래의 예시는 결정 트리 모델의 *max_leaf_nodes* 인수의 값을 바꿔 보면서 모델의 성능을 비교 측정하는 코드이다.(데이터를 불러오고, 검증 데이터셋을 떼어내는 부분은 생략)
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
하이퍼파라미터 튜닝을 완료하면, 마지막으로 전체 데이터로 모델을 훈련시켜 성능을 극대화한다. 더 이상 검증 데이터셋을 떼어 놓을 필요가 없기 때문이다.

## Lesson 6. Random Forests
서로 다른 여러 모델을 함께 사용하면 단일 모델모다 더 좋은 성능을 낼 수 있다. **랜덤 포레스트(random forest)**가 좋은 예시이다.

랜덤 포레스트는 수많은 결정 트리들로 구성되어 있으며, 각 트리의 예측값의 평균을 내어 최종 예측을 한다. 많은 경우에 단일 결정 트리보다 더 나은 예측 정확도를 보이며, 매개변수들을 기본값 그대로 사용하여도 잘 작동한다.
