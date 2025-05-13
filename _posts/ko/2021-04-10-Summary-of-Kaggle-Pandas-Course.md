---
title: Kaggle-Pandas 코스 내용 정리
description: Kaggle 공개 코스 중 Pandas 미니 코스의 내용을 요약하였다.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---
# Pandas
Solve short hands-on challenges to perfect your data manipulation skills.

## Lesson 1. Creating, Reading and Writing
### 판다스 불러오기
```python
import pandas as pd
```
판다스에는 **데이터프레임(DataFrame)**과 **시리즈(Series)**라는 2개의 핵심적인 객체가 있다.

### 데이터프레임
데이터프레임(DataFrame)은 표이다. 개별 *항목들(entries)*로 이루어진 행렬을 포함하는데, 이때 각 항목은 특정 *값(value)*을 가지며 하나의 *행*(*row* 또는 *record*)과 열(*column*)에 대응한다. 데이터프레임 항목들은 꼭 정수일 필요는 없다.
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```
데이터프레임의 선언은 파이썬의 딕셔너리(dictionary) 형식으로 한다. 키(key)에는 열 이름, 값(value)에는 기재할 항목들로 구성된 리스트(list)를 넣는다.

보통 데이터프레임 선언 시 열 레이블에는 그 열의 이름이 할당되지만, 행 레이블에는 0, 1, 2...의 정수가 할당된다. 필요하다면 행 레이블을 수동으로 지정해줄 수 있다. 데이터프레임에서 행 레이블들의 리스트를 **인덱스(Index)**라고 하며, ```index``` 매개변수를 사용하여 값을 지정할 수 있다.
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

### 시리즈
시리즈(Series)는 데이터 값들로 이루어진 수열(sequence)이다.
```python
pd.Series([1, 2, 3, 4, 5])
```
시리즈는 본질적으로 데이터프레임의 단일 열과 같다. 따라서 마찬가지로 인덱스를 지정할 수 있다. 다만 차이점은, '열 이름' 대신 '이름', ```name```을 가진다는 것이다.
```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```
시리즈와 데이터프레임은 밀접한 관련이 있다. 데이터프레임을 그냥 시리즈들의 묶음이라고 생각하면 이해하는 데 도움이 된다.

### 데이터 파일 읽어들이기
많은 경우에 데이터를 직접 작성하기보다는 이미 있는 데이터를 가져와서 사용한다. 데이터는 다양한 형식으로 저장되어 있을 수 있는데, 가장 기본적인 형태는 CSV 파일이다. CSV 파일의 내용물은 보통 아래와 같다.
```
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```
즉 CSV 파일은 각 값들을 쉼표(comma)로 구분하는 표이다. 그래서 이름이 "Comma-Separated Values", CSV이다.

CSV 파일 형식의 데이터를 데이터프레임으로 불러올 때는 ```pd.read_csv()``` 함수를 사용한다.

```shape``` 속성을 사용하여 데이터프레임의 크기를 확인할 수 있다.

```head()``` 명령을 사용하여 데이터프레임의 첫 다섯 행을 확인할 수 있다.

```pd.read_csv()``` 함수에는 30개가 넘는 매개변수들이 있다. 예를 들어 불러오려는 CSV 파일이 자체적으로 인덱스를 포함할 경우, ```index_col``` 매개변수의 값을 지정하여 판다스에서 자동으로 인덱스를 매기는 대신 해당 열을 인덱스로 사용하도록 할 수 있다.

### 데이터 기록하기
```to_csv()``` 메서드를 사용하면 데이터프레임을 CSV 파일로 내보낼 수 있다. 다음과 같이 사용한다.
```python
(데이터프레임 이름).to_csv("(CSV 파일 경로)")
```

## Lesson 2. Indexing, Selecting & Assigning
판다스 데이터프레임 또는 시리즈에서 사용할 특정 값들을 선택하는 것은 거의 모든 데이터를 이용하는 작업에서 거치는 단계이다.
