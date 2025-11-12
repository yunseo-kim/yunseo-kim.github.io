---
title: "Kaggle 'Pandas' 교육과정 내용 정리 (2) - Lesson 4-6"
description: "데이터를 정제, 가공하기 위한 Pandas 라이브러리의 활용법을 정리한다. Kaggle의 'Pandas' 공개 교육과정의 내용을 요약하고, 필요에 따라 일부 보강하였다. 이 포스트는 해당 교육과정의 후반부(Lesson 4-6)의 내용을 다룬다."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
---

Kaggle의 [Pandas](https://www.kaggle.com/learn/pandas) 교육과정을 통해 공부한 내용을 여기에 정리한다.  
분량이 제법 되기 때문에 2편으로 분리하였다.
- [1편: Lesson 1-3](/posts/summary-of-kaggle-pandas-course-1/)
- 2편: Lesson 4-6 (본문)

![Certificate of Completion](/assets/img/kaggle-pandas/certificate.png)

## Lesson 4. Grouping and Sorting
종종 데이터를 분류하고 집단별로 어떤 조작을 가해야 하거나, 특정 기준에 따라 정렬해야 할 때가 있다.

### 집단별 분석
[`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) 메서드를 사용하면 특정 열의 값이 같은 데이터끼리 묶고, 이후 각 집단별로 개요 확인 또는 조작을 수행할 수 있다.

앞서 [`value_counts()` 메서드](/posts/summary-of-kaggle-pandas-course-1/#데이터-개요-확인)를 알아보았는데, 동일한 동작을 `groupby()` 메서드로는 다음과 같이 구현할 수 있다.

```python
reviews.groupby('taster_name').size()
```

1. `reviews` 데이터프레임을 `taster_name` 열의 값이 같은 데이터들끼리 묶음
2. 그렇게 묶은 각 집단의 크기(속한 데이터 수)를 시리즈로 반환

또는

```python
reviews.groupby('taster_name').taster_name.count()
```

1. `reviews` 데이터프레임을 `taster_name` 열의 값이 같은 데이터들끼리 묶음
2. 그렇게 묶은 각 집단별로 `taster_name` 열에 해당하는 데이터를 선택
3. 해당하는 결측치를 제외한 데이터 수를 시리즈로 반환

즉, `value_counts()` 메서드는 사실 위와 같은 동작에 대한 단축어인 것이다. [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) 메서드 이외에도 어떤 개요 함수든지 이런 식으로 활용할 수 있다. 가령, 와인 데이터로부터 평점별 최저가를 확인하려면 다음과 같이 할 수 있다.

```python
reviews.groupby('points').price.min()
```

```
points
80      5.0
81      5.0
       ... 
99     44.0
100    80.0
Name: price, Length: 21, dtype: float64
```

1. `reviews` 데이터프레임을 `points` 열의 값이 같은 데이터들끼리 묶음
2. 그렇게 묶은 각 집단별로 `price` 열에 해당하는 데이터를 선택
3. 해당하는 데이터 중 최소값을 시리즈로 반환

둘 이상의 열을 기준으로 데이터를 분류하는 것도 가능하다. 국가별, 주별로 평점이 가장 높은 와인의 정보만을 선택하려면 다음과 같이 할 수 있다.

```python
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
```

또다른 알아두면 좋을 DataFrameGroupBy 객체의 메서드는 [`agg()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html)이다. 이를 사용하면 데이터를 묶은 후에 각 집단별로 여러 개의 함수를 동시에 실행하는 것이 가능하다.

> 이때 인자로는 
> - 함수
> - 함수명을 담은 문자열
> - 함수 또는 함수명 문자열을 담은 리스트
> - 축 레이블을 키, 해당 축에 대해 적용할 함수 또는 함수 목록을 값으로 갖는 딕셔너리
>
> 를 전달할 수 있으며, 여기서 함수는
> - 데이터프레임을 입력으로 받을 수 있거나
> - [앞서 다뤘던](/posts/summary-of-kaggle-pandas-course-1/#사상-maps) [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) 메서드에 인자로 전달 가능한
>
> 함수여야 한다. 원래의 Kaggle 교육과정에는 나와 있지 않던 설명으로, 판다스 공식 문서를 참고하여 보강 서술하였다.
{: .prompt-tip }

예를 들어 다음과 같이 국가별 가격 통계량을 산출할 수 있다.

```python
reviews.groupby(['country']).price.agg([len, min, max])
```

> 여기서 `len`은 파이썬 내장 함수 [`len()`](https://docs.python.org/3/library/functions.html#len)을 의미하며, 지금의 예시에서는 <u>결측치를 포함한</u> 묶음(`country`)별 가격(`price`) 데이터 수를 출력하기 위해 사용하였다. 데이터프레임 또는 시리즈를 입력으로 받아 동작 가능한 함수이기 때문에 이와 같이 사용이 가능하다.
>
> 판다스에서 제공하는 [`count()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html) 메서드는 <u>결측치를 제외한 유효한 값들의 수만</u> 세서 반환한다는 점에서 동작에 차이가 있다.
>
> 원래의 Kaggle 교육과정에는 나와 있지 않던 설명으로, 파이썬과 판다스 공식 문서를 참고하여 보강 서술하였다.
{: .prompt-tip }

### 다중 인덱스

`groupby()` 메서드를 활용한 데이터 가공 및 분석을 하다 보면, 단일 레이블이 아니라 둘 이상의 단계로 구성된 다중 인덱스를 갖는 데이터프레임을 반환받을 때가 있다.

```python
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
```

<table>
  <tr>
    <th></th>
    <th></th>
    <th>len</th>
  </tr>
  <tr>
    <th>Country</th>
    <th>province</th>
    <th></th>
  </tr>
  <tr>
    <td rowspan="2">Argentina</td>
    <td>Mendoza Province</td>
    <td>3264</td>
  </tr>
  <tr>
    <td>Other</td>
    <td>536</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td rowspan="2">Uruguay</td>
    <td>San Jose</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Uruguay</td>
    <td>24</td>
  </tr>
</table>

```python
mi = countries_reviewed.index
type(mi)
```

```
pandas.core.indexes.multi.MultiIndex
```

다중 인덱스는 계층 구조를 다루기 위한, 단일 인덱스에는 없는 몇몇 메서드들을 지닌다. 다중 인덱스에 대한 자세한 사용례와 지침은 [pandas User Guide의 MultiIndex / advanced indexing 섹션](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)에 자세히 나와 있다.

다만, 보통 다중 인덱스에 대해 제일 자주 사용하게 될 메서드는 아래와 같이 보통의 인덱스로 되돌리기 위한 [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)일 것이다.

```python
countries_reviewed.reset_index()
```

| | country | province | len |
| --- | --- | --- | --- |
| 0 | Argentina | Mendoza Province | 3264 |
| 1 | Argentina | Other | 536 |
| ... | ... | ... | ... |
| 423 | Uruguay | San Jose | 3 |
| 424 | Uruguay | Uruguay | 24 |

### 정렬

계속해서 예시로 살펴보고 있는 `countries_reviewed`를 가만히 보면 데이터를 묶은 결과물은 인덱스 순서로 반환됨을 알 수 있다. 즉 `groupby` 결과물의 행 순서는 데이터 내용물이 아닌 인덱스 값에 의해 결정된다.

필요에 따라 데이터를 다른 방식으로 직접 정렬할 수 있다. 이럴 때는 [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) 메서드를 사용하면 편리하다. 예를 들어 아래와 같이 포함한 데이터 수('len') 기준으로 국가와 주 정보를 오름차순 정렬할 수 있다.

```python
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')
```

| | country | province | len |
| --- | --- | --- | --- |
| 179 | Greece | Muscat of Kefallonian | 1 |
| 192 | Greece | Sterea Ellada | 1 |
| ... | ... | ... | ... |
| 415 | US | Washington | 8639 |
| 392 | US | California | 36247 |

`sort_values()`는 기본적으로 오름차순 정렬(낮은 값부터 높아지는 순서)을 수행하나, 다음과 같이 옵션을 지정하면 내림차순 정렬(높은 값부터 낮아지는 순서)도 가능하다.

```python
countries_reviewed.sort_values(by='len', ascending=False)
```

| | country | province | len |
| --- | --- | --- | --- |
| 392 | US | California | 36247 |
| 415 | US | Washington | 8639 |
| ... | ... | ... | ... |
| 63 | Chile | Coelemu | 1 |
| 149 | Greece | Beotia | 1 |

인덱스 기준으로 정렬하려면 [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html) 메서드를 사용하면 된다. `sort_values()`와 동일한 인자 및 기본 정렬 순서(내림차순)를 가지므로 사용법은 동일하다.

```python
countries_reviewed.sort_index()
```

| | country | province | len |
| --- | --- | --- | --- |
| 0 | Argentina | Mendoza Province | 3264 |
| 1 | Argentina | Other | 536 |
| ... | ... | ... | ... |
| 423 | Uruguay | San Jose | 3 |
| 424 | Uruguay | Uruguay | 24 |

마지막으로, 다음과 같이 한번에 둘 이상의 열을 기준으로 정렬하는 것도 가능하다.

```python
countries_reviewed.sort_values(by=['country', 'len'])
```

## Lesson 5. Data Types and Missing Values

현실적으로 다루어야 하는 데이터가 항상 잘 정제되어 있으리란 보장은 없으며, 오히려 자료형이 원하는 것과 달라 변환해 주어야 하거나 결측값이 중간중간에 있어 누락된 부분을 적절히 처리해 줘야 하는 경우가 대부분이다. 데이터를 가공하고 분석할 때 거의 대부분 최대 난관이 바로 이 단계이다.

### 자료형

데이터프레임의 특정 열, 또는 시리즈의 자료형을 **dtype**이라고 한다. `dtype` 속성을 통해 주어진 데이터프레임의 특정 열의 자료형을 확인할 수 있다. 다음은 `reviews` 데이터프레임의 `price` 열의 `dtype`을 확인하는 예시이다.

```python
reviews.price.dtype
```

```
dtype('float64')
```

혹은 `dtypes` 속성을 통해 다음과 같이 데이터프레임 내 모든 열의 `dtype`을 한번에 확인할 수 있다.

```python
reviews.dtypes
```

```
country        object
description    object
                ...  
variety        object
winery         object
Length: 13, dtype: object
```

자료형은 판다스가 내부적으로 해당 데이터를 어떻게 저장하고 있는지를 나타낸다. 가령 `float64`는 64비트 부동소수점 실수, `int64`는 64비트 정수를 의미한다.

또한 한 가지 특이한 점은, 문자열로만 구성된 열은 자체적인 자료형을 갖지 않고 단지 객체(`object`)로 간주된다.

[`astype()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html)을 사용하면 어느 한 자료형의 열을 다른 자료형으로 변환할 수 있다. 예를 들어, 앞선 예시에서 `int64` 자료형이었던 `points` 열을 `float64` 자료형으로 변환할 수 있다.

```python
reviews.points.astype('float64')
```

```
0         87.0
1         87.0
          ... 
129969    90.0
129970    90.0
Name: points, Length: 129971, dtype: float64
```

데이터프레임 혹은 시리즈의 인덱스 역시 마찬가지로 자료형을 가진다.

```python
reviews.index.dtype
```

```
dtype('int64')
```

판다스는 이 외에도 범주형 데이터나 시계열 데이터와 같은 외부 자료형 역시 지원한다.

### 결측값

값이 없는, 비어 있는 엔트리들은 `NaN`("Not a Number"의 축약어) 값을 부여받는다. 기술적인 이유로 `NaN`은 항상 `float64` 자료형이다.

판다스는 결측값에 특화된 몇몇 함수들을 지원한다. [이전에도 비슷한 걸 잠깐 본 적 있는데](/posts/summary-of-kaggle-pandas-course-1/#조건부-선택), 메서드가 아닌 판다스 내 독립적인 함수로도 [`pd.isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html)와 [`pd.notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html)가 존재한다. 이들 함수는 주어진 엔트리가 결측값인지(혹은 결측값이 아닌지)를 단일 불리언 값 또는 불리언 배열로 반환하며, 다음과 같이 응용할 수 있다.

```python
reviews[pd.isna(reviews.country)]
```

보통은 주어진 데이터에 결측값이 있는지 확인하고, 있다면 이를 적절히 채워 넣을 필요가 있다. 이럴 때 쓸 수 있는 전략은 여러 가지가 있는데, 우선 [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html) 메서드를 사용하면 결측값을 어떤 적당한 값으로 대체하여 채워 넣을 수 있다. 다음은 주어진 `reviews` 데이터프레임의 `region_2` 열에서 모든 `NaN`을 `"Unknown"`으로 바꿔 넣는 예시이다.

```python
reviews.region_2.fillna("Unknown")
```

혹은, 결측값이 있을 때 그 앞쪽이나 뒤쪽에서 가장 가까운 유효한 값을 가져와 채워 넣는 forward fill 또는 backward fill 전략을 사용할 수 있다. 각각 [`ffill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html),  [`bfill()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html) 메서드로 구현할 수 있다.

> 예전에는 `fillna()` 메서드에 `method` 인자로 `'ffill'`, `'bfill'` 문자열을 전달하여 사용할 수도 있었으나, 판다스 2.1.0 버전부터 해당 방법은 deprecated되어 사용을 권장하지 않으므로 대신 `ffill()`이나 `bfill()` 메서드를 상황에 맞게 사용해야 한다.
{: .prompt-danger }

그리고 경우에 따라서는 결측값이 아니더라도 어떤 값을 다른 값으로 일괄 대치해야 할 수 있다. 원래의 Kaggle 교육과정에서는 리뷰 데이터셋에서 특정 리뷰어의 트위터 핸들이 변경된 상황을 예시로 들고 있는데, 이것도 훌륭한 예시지만 한국인들 입장에서 좀 더 와닿을 다른 예시를 생각해보자면 다음과 같다.

대한민국에서 경기도 북부를 분할하여 **경기북도**라는 새로운 행정구역을 설치하였고 해당 명칭을 반영한 데이터셋이 있는데, 여기서 누군가가 갑자기 **경기북도**라는 멀쩡한 이름을 **평화누리특별자치도**로 바꾸자는 정신나간 발상을 해내고 그걸 기어이 관철해 버린 가상의 상황을 생각해 보자. ~~가상의 상황이지만, 자칫 이 비슷한 상황이 진짜 일어날 수도 있었다는 게 참 무서운 부분이다.~~ 그렇다면 이를 반영하여 기존 데이터셋에서 `"Gyeonggibuk-do"`를 `"Pyeonghwanuri State"` 내지는 `"Pyeonghwanuri Special Self-Governing Province"` 같은 새로운 값으로 대치해야 할 것이다. 판다스로 이러한 작업을 수행하는 한 가지 방법은 바로 [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html) 메서드를 사용하는 것이다.

```python
rok_2030_census.province.replace("Gyeonggibuk-do", "Pyeonghwanuri Special Self-Governing Province")
```

위의 예제 코드를 활용하면 `rok_2030_census` 데이터셋의 `province` 열에서 모든 `"Gyeonggibuk-do"` 문자열을 효과적으로 '그 긴 거'로 일괄 대치할 수 있다. ~~이딴 코드를 누군가가 진짜로 돌려야만 했을 상황이 현실에서 벌어지지 않았다는 사실에 다시금 그저 안도하게 된다.~~

이와 같은 문자열 대치는 결측값 처리 및 데이터 정제 과정에서도 유효한데, 결측값이 `NaN`이 아니라 `"Unknown"`, `"Undisclosed"`, `"Invalid"` 같은 문자열로 주어지는 경우도 흔하기 때문이다. 현실에서 과거 작성된 공문서 등을 OCR 스캔하여 데이터셋으로 만드는 것과 같은 작업에서는 오히려 이런 경우가 대부분일 수 있다.

## Lesson 6. Renaming and Combining

때로는 데이터셋 내 특정 열이나 인덱스의 이름을 변경해야 할 수 있다. 또한 여러 개의 데이터프레임이나 시리즈를 결합해야 하는 상황도 자주 있다.

### 이름 변경

[`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) 메서드를 사용하면 데이터셋 내 특정 열 또는 인덱스의 이름을 변경할 수 있다. `rename()` 메서드는 다양한 입력 형식을 지원하지만, 대개 파이썬 딕셔너리를 이용하는 것이 제일 편리하다. 다음은 각각 `reviews` 데이터프레임에서 `points` 열의 이름을 `score`로 변경하고, 인덱스 중 `0`, `1`을 `firstEntry`, `secondEntry`로 변경하는 예시이다. 

```python
reviews.rename(columns={'points': 'score'})
```

```python
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
```

사실 열 이름을 변경할 일은 자주 있지만, 인덱스 값의 이름을 변경할 일은 거의 없다. 그리고 그런 용도로는 보통 [전에 본 것처럼](/posts/summary-of-kaggle-pandas-course-1/#인덱스-조작하기) [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) 메서드를 사용하는 게 더 편하다.

행 인덱스와 열 인덱스는 스스로도 `name` 속성을 가지며, `rename_axis()` 메서드를 사용하면 이 축 이름을 변경하는 것도 가능하다. 가령 주어진 데이터셋의 인덱스 축에는 `wines`, 열 축에는 `fields`라고 이름을 붙일 수 있다.

```python
reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
```

### 데이터셋 결합하기

때로는 데이터프레임들끼리, 혹은 시리즈들끼리 결합해야 하는 경우가 있다. 판다스는 이러한 작업을 위해 세 가지 핵심 함수를 제공하는데, 단순한 것부터 복잡해지는 순서대로 쓰면 [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), [`join()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html), 그리고 [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)이다. Kaggle 교육과정에서는 `merge()`로 할 수 있는 일의 대부분은 `join()`으로 더 간단하게 할 수 있으므로 앞의 둘에만 집중하겠다고 밝히고 있다.

`concat()` 함수는 제일 단순한데, 여러 개의 데이터프레임 혹은 시리즈를 어느 한 축을 따라서 그대로 이어붙인다. 병합 대상인 데이터프레임 혹은 시리즈들이 같은 필드(열)들을 가지는 경우에 유용하다. 기본적으로는 인덱스 축을 따라 이어붙이며, `axis=1` 또는 `axis='columns'` 옵션을 지정하면 열 축을 따라 이어붙일 수도 있다.

```python
>>> s1 = pd.Series(['a', 'b'])
>>> s2 = pd.Series(['c', 'd'])
>>> pd.concat([s1, s2])
0    a
1    b
0    c
1    d
dtype: object
```

```python
>>> df1 = pd.DataFrame([['a', 1], ['b', 2]],
...                    columns=['letter', 'number'])
>>> df1
  letter  number
0      a       1
1      b       2
>>> df2 = pd.DataFrame([['c', 3], ['d', 4]],
...                    columns=['letter', 'number'])
>>> df2
  letter  number
0      c       3
1      d       4
>>> pd.concat([df1, df2])
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
>>> df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
...                    columns=['animal', 'name'])
>>> df4
   animal    name
0    bird   polly
1  monkey  george
>>> pd.concat([df1, df4], axis=1)
  letter  number  animal    name
0      a       1    bird   polly
1      b       2  monkey  george
```

> [판다스 공식 문서]((https://pandas.pydata.org/docs/reference/api/pandas.concat.html))에 따르면 여러 개의 행을 합쳐서 하나의 데이터프레임으로 만들어야 하는 경우 반복문 안에서 개별 행을 하나씩 더하는 것은 권장하지 않으며, 합쳐야 하는 행들을 리스트로 만든 다음 단일 `concat()`로 한번에 합쳐야 한다.
{: .prompt-tip }

`join()` 메서드는 좀 더 복잡한데, 인덱스를 기준으로 한 데이터프레임에 또다른 데이터프레임을 이어붙인다. 이때 이름이 겹치는 열이 있을 경우, `lsuffix`와 `rsuffix` 인자로 두 데이터프레임의 겹치는 열 이름 뒤에 구분을 위해 붙일 접미사를 각각 지정해 주어야 한다.

```python
>>> df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
...                    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
>>> df
  key   A
0  K0  A0
1  K1  A1
2  K2  A2
3  K3  A3
4  K4  A4
5  K5  A5
>>> other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
...                       'B': ['B0', 'B1', 'B2']})
>>> other
  key   B
0  K0  B0
1  K1  B1
2  K2  B2
>>> df.join(other, lsuffix='_caller', rsuffix='_other')
  key_caller   A key_other    B
0         K0  A0        K0   B0
1         K1  A1        K1   B1
2         K2  A2        K2   B2
3         K3  A3       NaN  NaN
4         K4  A4       NaN  NaN
5         K5  A5       NaN  NaN
```
