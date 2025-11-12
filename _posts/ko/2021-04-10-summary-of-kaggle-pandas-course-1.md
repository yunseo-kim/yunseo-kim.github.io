---
title: "Kaggle 'Pandas' 교육과정 내용 정리 (1) - Lesson 1-3"
description: "데이터를 정제, 가공하기 위한 Pandas 라이브러리의 활용법을 정리한다. Kaggle의 'Pandas' 공개 교육과정의 내용을 요약하고, 필요에 따라 일부 보강하였다. 이 포스트는 해당 교육과정의 후반부(Lesson 1-3)의 내용을 다룬다."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Kaggle의 [Pandas](https://www.kaggle.com/learn/pandas) 교육과정을 통해 공부한 내용을 여기에 정리한다.  
분량이 제법 되기 때문에 2편으로 분리하였다.
- 1편: Lesson 1-3 (본문)
- [2편: Lesson 4-6](/posts/summary-of-kaggle-pandas-course-2/)

![Certificate of Completion](/assets/img/kaggle-pandas/certificate.png)

## Lesson 1. Creating, Reading and Writing
### 판다스 불러오기

```python
import pandas as pd
```

판다스에는 **데이터프레임(DataFrame)**과 **시리즈(Series)**라는 2개의 핵심적인 객체가 있다.

### 데이터프레임
[데이터프레임(DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)은 표 내지는 [행렬](/posts/vector-spaces-subspaces-and-matrices/#행렬과-행렬공간)이라 생각할 수 있다. 독립적인 *엔트리들(entries)*로 이루어진 행렬로 구성되는데, 이때 각 엔트리는 특정 *값(value)*을 가지며 하나의 *행(row)* 또는 *레코드(record)* 그리고 하나의 *열(column)*에 대응한다.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

데이터프레임 엔트리들은 꼭 수치일 필요는 없으며, 다음은 문자열 값들(사용자들이 남긴 후기)을 갖는 데이터프레임 예시이다.

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

데이터프레임 객체를 생성할 때는 `pd.DataFrame()` 생성자(constructor)를 사용하며, 파이썬의 딕셔너리(dictionary) 문법을 통해 선언한다. 키(key)에는 열 이름, 값(value)에는 기재할 항목들로 구성된 리스트(list)를 넣는다. 이는 새로운 데이터프레임을 선언하는 표준적인 방법이다.

데이터프레임 선언 시 열 레이블에는 해당 열의 이름을 지정하지만, 행 레이블에는 별도 지정하지 않는다면 0, 1, 2, ...의 정수를 할당한다. 필요하다면 행 레이블을 수동으로 지정해줄 수 있다. 데이터프레임에서 행 레이블들의 리스트를 [**인덱스(Index)**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html)라고 하며, 생성자의 `index` 매개변수를 사용하여 값을 지정할 수 있다.

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

| | Bob | Sue |
| --- | --- | --- |
| Product A | I liked it. | Pretty good. |
| Product B | It was awful. | Bland. |

### 시리즈
[시리즈(Series)](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)는 데이터 값들로 이루어진 수열(sequence) 내지는 [벡터](/posts/vector-spaces-subspaces-and-matrices/#행벡터와-열벡터)이다.

```python
pd.Series([1, 2, 3, 4, 5])
```

시리즈는 본질적으로 데이터프레임의 단일 열과 같다. 따라서 마찬가지로 [인덱스](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html)를 지정할 수 있으며, 단지 '열 이름' 대신 그냥 '이름'([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html))을 가질 뿐이다.

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

시리즈와 데이터프레임은 서로 밀접한 관련이 있다. 데이터프레임을 그냥 시리즈들의 묶음이라고 생각하면 이해하는 데 도움이 된다.

### 데이터 파일 읽어들이기
많은 경우에 데이터를 직접 작성하기보다는 이미 있는 데이터를 가져와서 사용한다. 데이터는 다양한 형식으로 저장되어 있을 수 있는데, 가장 기본적인 형태는 CSV 파일이다. CSV 파일의 내용물은 보통 아래와 같다.

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

즉 CSV 파일은 각 값들을 쉼표(comma)로 구분하는 표이다. 그래서 이름이 "Comma-Separated Values", CSV이다.

CSV 파일 형식의 데이터를 데이터프레임으로 불러올 때는 [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) 함수를 사용한다.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

[`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) 속성을 사용하여 데이터프레임의 형태를 확인할 수 있다.

```python
product_reviews.shape
```

```
(129971, 14)
```

위의 예시 출력은 해당 데이터프레임이 129971개의 레코드, 14개의 열을 가짐을 의미한다.

[`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) 메서드를 사용하여 데이터프레임의 첫 다섯 행을 확인할 수 있다.

```python
product_reviews.head()
```

[`pd.read_csv()` 함수에는 30개가 넘는 매개변수들이 있다](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). 예를 들어 불러오려는 CSV 파일이 자체적으로 인덱스를 포함할 경우, `index_col` 매개변수의 값을 지정하여 판다스에서 자동으로 인덱스를 매기는 대신 해당 열을 인덱스로 사용하도록 할 수 있다.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### 데이터 파일 쓰기
[`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) 메서드를 사용하면 데이터프레임을 CSV 파일로 내보낼 수 있다. 다음과 같이 사용한다.

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Lesson 2. Indexing, Selecting & Assigning
판다스 데이터프레임 또는 시리즈에서 사용할 특정 값들을 선택하는 것은 거의 모든 데이터 처리 작업에서 거치는 단계이므로, 빠르고 효율적으로 필요한 데이터 포인트들을 선택하는 법을 우선적으로 익힐 필요가 있다.

### 파이썬 자체 접근자
네이티브 파이썬 객체는 훌륭한 데이터 인덱싱 방법들을 제공하며, 판다스 역시 그러한 인덱싱 방법들을 동일하게 제공한다.

#### 객체 속성
파이썬에서는 객체의 속성 값(property)에 해당 속성 이름(attribute)을 통해 접근할 수 있다. 예를 들어 `example_obj` 객체가 `title` 속성을 갖는다면 `example_obj.title`로 호출할 수 있다. 판다스 데이터프레임의 열들에 대해 동일하게 접근 가능하다.

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

#### 딕셔너리 인덱싱
또한 파이썬의 딕셔너리 자료형의 경우 인덱싱 연산자(`[]`)를 이용해 딕셔너리 내 값에 접근할 수 있다. 판다스 데이터프레임의 열들에 대해서도 동일한 방식으로 접근 가능하다.

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

객체 속성을 통한 접근법과 딕셔너리 인덱싱을 통한 접근법 둘 다 유효하나, 딕셔너리 인덱싱 방식은 공백 문자와 같은 예약 문자들을 포함하는 열 이름도 다룰 수 있다는 장점이 있다(e.g. `reviews['country providence']`는 가능하지만 `reviews.country providence`와 같은 접근은 불가능하다).

그렇게 골라낸 판다스 시리즈 안에서도 또다시 인덱싱 연산자를 사용해 개별 값을 읽어들일 수 있다.

```python
reviews['country'][0]
```

```
'Italy'
```

### 판다스 고유 접근자
상술한 인덱싱 연산자 또는 객체 속성을 통한 접근은 다른 파이썬 생태계와 자연스럽게 어울린다는 점에서 훌륭하지만, 판다스는 그 외에도 판다스만의 고유한 접근자인 [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)과 [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)을 제공한다.

#### 인덱스 기반 선택
`iloc`을 사용하면 **인덱스 기반 선택(index-based selection)**을 수행할 수 있다. 데이터 내의 위치를 정수 번호로 지정하여 골라낸다.

예를 들어, 다음과 같이 데이터프레임의 첫 번째 행을 골라낼 수 있다.

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

열을 먼저 선택하고 이후 행을 선택하는 네이티브 파이썬 방식과 달리, `iloc`은 행을 먼저 선택하고 이후 열을 선택한다. 데이터프레임의 첫 번째 열은 다음과 같이 골라낼 수 있다.

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

위의 예시에서는 `:` 연산자를 사용하여 전체 행을 선택한 후, 그 안에서 첫 번째 열을 선택하였다. 만약 첫 번째 열의 두 번째(`1`)와 세 번째(`2`) 행을 선택하고자 한다면 다음과 같이 하면 된다.

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

혹은 리스트를 전달할 수도 있다.

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

음수를 사용하여 뒤쪽에서부터 데이터를 골라낼 수도 있다. 다음 예시는 데이터의 마지막 5개 행을 골라낸 것이다.

```python
reviews.iloc[-5:]
```

#### 레이블 기반 선택
또다른 방법은 `loc`을 사용하여 **레이블 기반 선택(label-based selection)**을 수행하는 것이다. 이 경우 데이터 내의 위치가 아닌 인덱스의 값을 통해 골라낸다.

예를 들어, 인덱스 값이 0인 행의 'country' 열에 대응하는 엔트리를 다음과 같이 얻을 수 있다.

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc`은 데이터셋의 인덱스 값을 무시하고 하나의 큰 행렬처럼 간주, 위치에 의존하여 개별 엔트리에 접근한다. 반면 `loc`은 인덱스 정보를 활용하여 동작한다. 대개 인덱스에도 의미 있는 정보들이 있기 때문에, 많은 경우 `loc`이 `iloc`보다 직관적이다.

#### `iloc`과 `loc`의 범위 지정 방식 차이
`iloc`은 파이썬 표준 라이브러리의 인덱싱 체계를 동일하게 사용하며, 따라서 `0:10`은 0 이상 10 **미만**의 반닫힌구간, 즉 `0,...,9`를 의미한다.

반면 `loc`은 범위를 닫힌 구간으로 인식하기 때문에, `0:10`은 0 이상 10 **이하**, 즉 `0,...,10`을 의미한다.

이런 차이를 둔 이유는, `loc`은 정수뿐만 아니라 모든 표준 자료형을 인덱스로 사용할 수 있기 때문이다. 가령 `Apples, ..., Potatoes, ...`의 인덱스 값들을 갖는 데이터프레임이 있고 여기서 알파벳 사전순으로 'Apples'부터 'Potatoes'까지의 범위에 해당하는 작물들을 골라내야 한다고 하자. 알파벳 사전순으로 s 다음은 t, 즉 'Potatoes' 바로 다음에 올 수 있는 문자 조합이 'Potatoet'니까 "'Apples'부터 'Potatoet' 전까지"(`df.loc['Apples':'Potatoet']`)라고 지정하는 것보다, 그냥 "'Apples'부터 'Potatoes'까지"(`df.loc['Apples':'Potatoes']`)라고 지정하는 편이 훨씬 더 직관적이다. 이처럼 정수 이외의 자료형에 해당하는 인덱스에 대해서는 보통 후자의 방식이 더 직관적이기 때문에 `loc`이 해당 방식을 따르는 것이다.

이 외에는 나머지 동작 방식은 기본적으로 동일하다.

> 개인적으로는 오름차순 정렬된 정수 인덱스를 갖는 데이터셋에서 `:` 연산자를 활용해 범위 지정을 해야 하는 경우 위의 범외 지정 방식 차이에 의한 혼동을 방지하기 위해 `iloc`을, 그 외의 경우에는 보다 직관적인 `loc`을 선호하는 편이다.
{: .prompt-tip }

### 인덱스 조작하기
인덱스를 필요에 따라 조정하는 것도 가능하다. [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) 메서드를 사용하면 다음 예시와 같이 데이터셋 내 특정 열을 새로운 인덱스로 지정할 수 있다.

```python
reviews.set_index("title")
```

### 조건부 선택
상술한 내용은 데이터프레임 자체의 구조적인 속성 값들을 활용하여 데이터를 가공하고 선택하는 방법들에 관한 것이다. 그러나 더 나아가서 보다 복잡한 특정 조건을 만족하는 데이터들을 골라낼 수도 있다.

예를 들어 와인 제품들에 대한 정보를 담은 데이터프레임에서 평점이 90점 이상인 이탈리아산 와인의 데이터만을 선택해야 하는 상황을 생각해 보자.

```python
reviews.country == 'Italy'
```

위 조건문은 `True`/`False` 불리언 값들로 구성된 시리즈를 반환한다.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc`은 기본적으로 레이블 기반이지만, 불리언 배열 또는 정렬 가능한 불리언 시리즈도 입력받을 수 있다](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). 따라서 다음과 같이 이탈리아산 와인 데이터만을 선택하는 것이 가능하다.

```python
reviews.loc[reviews.country == 'Italy']
```

여러 개의 조건을 `&` 또는 `|` 연산으로 결합할 수 있다. 이탈리아산**이면서** 평점이 90점 이상인 와인 데이터를 선택하려면 다음과 같이 하면 된다.

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

이탈리아산**이거나** 평점이 90점 이상인 와인 데이터는 다음과 같이 선택할 수 있다.

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

또한 판다스는 몇 개의 내장 조건부 선택자를 갖고 있는데, 그 중 특히 `isin`과 `isnull`/`notnull`이다.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html)은 리스트 "안에 있는(is in)" 값들 중 하나를 갖는지 불리언(`True` 또는 `False`) 마스크 시리즈로 반환하며, 이를 이용하여 데이터를 골라낼 수 있다. 예를 들어 다음과 같이 이탈리아산 또는 프랑스산인 와인 데이터를 골라낼 수 있다.

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html)은 결측치(`NaN`)를 갖거나 갖지 않는 데이터를 골라낼 때 사용한다. 예를 들어 다음과 같이 가격 데이터가 누락되지 않은 와인 데이터만 골라낼 수 있다.

```python
reviews.loc[reviews.price.notna()]
```

> 참고로 원래 Kaggle 교육과정에는 나와 있지 않던 내용이지만, [`iloc`도 불리언 배열(array)은 입력받을 수 있다](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). 다만 `loc`과 달리 배열만 지원하고 시리즈는 지원하지 않아서 위와 같은 식의 응용은 어렵다.
{: .prompt-tip }

### 데이터 할당
데이터프레임에 새롭게 데이터를 할당하거나 덮어씌울 수도 있다.

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
### 데이터 개요 확인
[`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) 메서드는 주어진 열의 고수준 개요를 제공한다.

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

`describe()` 메서드의 출력은 입력 자료형에 따라 달라진다. 수치 자료가 아닌 문자열 자료에 대해서는 다음과 같은 출력을 반환한다.

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

혹은 원하는 특정 통계만 얻어낼 수도 있다.

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

데이터프레임 안에서 각각의 고유한 값이 등장한 횟수를 알고 싶다면 [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html) 메서드를 사용하면 된다.

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

### 사상 (Maps)
**사상(map)**은 수학에서 빌려온 용어로, 한 집합을 또다른 집합으로 대응시키는 함수를 의미한다. 데이터과학에서는 종종 주어진 데이터를 다른 표현 형식으로 변환해야 하는 경우가 있는데, 이러한 작업을 할 때 사상들을 사용하며 따라서 매우 중요하다.

주로 두 메서드를 자주 사용한다.

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) 메서드는 하나의 <u>값</u>을 또다른 단일 값으로 변환하는 함수를 입력받아, 해당 함수를 주어진 <u>시리즈</u> 내 모든 값들에 대해 일괄 적용한 후 그렇게 얻은 새로운 시리즈를 반환한다. 가령 와인 평점 데이터에서 일괄적으로 평균값을 빼서 편차를 얻고 싶다면 다음과 같이 할 수 있다.

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) 메서드는 각 <u>행</u>에 대해 커스텀 함수를 호출하여 <u>데이터프레임</u> 전체에 변환을 적용하고 싶을 때 사용한다.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

`apply()` 메서드를 `axis='index'` 매개변수와 함께 호출하면 각 행이 아니라 각 열에 대해 함수를 적용할 수 있다.

`Series.map()`과 `DataFrame.apply()`는 각각 새로운, 변환한 시리즈와 데이터프레임을 반환하며, 원래의 데이터에는 아무런 수정을 가하지 않는다.

| 메서드 | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| 적용 대상 | 시리즈 | 데이터프레임 |
| 적용 단위 | 개별 값 단위로 적용 <br>(시리즈를 [열벡터](/posts/vector-spaces-subspaces-and-matrices/#행벡터와-열벡터)로 본다면 행 단위로 적용) | 기본적으로 행 단위로 적용 <br> 옵션 지정 시 열 단위로 적용 가능 |

> 참고로 [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html)와 [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html)도 존재한다.
> - `Series.apply()`:
>   - `by_row='compat'`(기본값): `Series.map()`과 동일하게 동작
>   - `by_row=False`: 시리즈 전체를 한번에 함수 입력으로 전달(`axis='index'`로 지정했을 때의 `DataFrame.apply()`의 동작과 유사함)
> - `DataFrame.map()`: 데이터프레임 내 개별 값에 대해 함수 적용(시리즈가 아니라 데이터프레임이 대상이라는 점만 빼면 `Series.map()`과 유사함)
{: .prompt-tip }

사실 판다스는 자체적으로 여러 흔히 사용하는 사상들을 지원한다. 앞서 다룬 예시는 다음과 같은 훨씬 간단한 코드로도 구현 가능하며, 이 경우에도 판다스는 의도를 파악하여 정상적으로 동작한다.

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

뿐만 아니라, 판다스는 길이가 같은 시리즈들 간의 연산도 지원한다. 와인 데이터 예시에서 생산국과 생산지역 정보를 다음과 같이 문자열끼리 결합하는 것도 가능하다.

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

이들 연산은 판다스에 내장된 연산 가속 기법들을 사용하기 때문에 `map()`이나 `apply()` 메서드보다 빠르며, 판다스는 모든 파이썬 표준 연산자들(`>`, `<`, `==` 등등)에 대해 이런 식으로 동작 가능하다. 그래도 `map()`과 `apply()`는 보다 유연하고, 더 복잡한 작업들을 수행할 수 있기 때문에 이들 메서드도 알아 두면 도움이 된다.
