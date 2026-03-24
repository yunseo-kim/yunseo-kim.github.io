---
title: "የKaggle 'Pandas' የስልጠና ኮርስ ይዘት ማጠቃለያ (1) - ትምህርት 1-3"
description: "ዳታን ለማጽዳትና ለማቀናበር የPandas ላይብረሪን እንዴት መጠቀም እንደሚቻል እንደምን እንዘርዝራለን። የKaggle 'Pandas' ነፃ ኮርስ ይዘትን እናጠቃልላለን፣ አስፈላጊ በሆኑ ቦታዎችም ተጨማሪ ማብራሪያ እንጨምራለን። ይህ ፖስት የኮርሱን ኋለኛ ክፍል(Lesson 1-3) ይሸፍናል።"
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

በካግል(Kaggle) የ[Pandas](https://www.kaggle.com/learn/pandas) ኮርስ ላይ ሲማር የተማርኩትን ይዘት እዚህ እያጠቃለልኩ እቀርባለሁ።  
መጠኑ እጅግ ብዙ ስለሆነ በ2 ክፍሎች ከፍሌዋለሁ።
- ክፍል 1: ትምህርት 1-3 (ይህ ጽሑፍ)
- [ክፍል 2: ትምህርት 4-6](/posts/summary-of-kaggle-pandas-course-2/)

![የማጠናቀቂያ ማረጋገጫ](/assets/img/kaggle-pandas/certificate.png)

## ትምህርት 1. መፍጠር፣ ማንበብ እና መጻፍ
### ፓንዳስ(Pandas) ማስመጣት

```python
import pandas as pd
```

በፓንዳስ(Pandas) ውስጥ **ዳታፍሬም(DataFrame)** እና **ሲሪዝ(Series)** የተባሉ 2 አስፈላጊ ኦብጀክቶች(objects) አሉ።

### ዳታፍሬም
[ዳታፍሬም(DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) እንደ ሰንጠረዥ ወይም [ማትሪክስ(matrix)](/posts/vector-spaces-subspaces-and-matrices/#ማትሪክስ-እና-የማትሪክስ-ስፔስ) ሊታሰብ ይችላል። እሱ ከነፃ የሆኑ *ኤንትሪዎች(entries)* የተሰራ ማትሪክስ ሲሆን፣ እያንዳንዱ ኤንትሪ የተወሰነ *እሴት(value)* ይይዛል እና አንድ *ረድፍ(row)* ወይም *ሬኮርድ(record)* እንዲሁም አንድ *አምድ(column)* ጋር ይዛመዳል።

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

የዳታፍሬም ኤንትሪዎች የግድ ቁጥሮች መሆን አያስፈልጋቸውም፤ የሚቀጥለው የጽሑፍ እሴቶችን(ተጠቃሚዎች የተዉትን ግምገማ) ያለው የዳታፍሬም ምሳሌ ነው።

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

የዳታፍሬም ኦብጀክትን ሲፈጥሩ `pd.DataFrame()` ኮንስትራክተር(constructor) ይጠቀማሉ፣ እና በፓይተን(Python) የዲክሽነሪ(dictionary) ሰነድ አጻጻፍ ይገልጹታል። በቁልፍ(key) ቦታ የአምድ ስሞችን፣ በእሴት(value) ቦታ ደግሞ ለመመዝገብ የሚፈለጉ ንጥሎች የያዙ ዝርዝሮች(list) ይገባሉ። ይህ አዲስ ዳታፍሬም ለማወጅ መደበኛው መንገድ ነው።

ዳታፍሬም ሲወጅ ለአምድ መለያዎች የአምዱን ስም ይሰጣሉ፤ ነገር ግን ለረድፍ መለያዎች በተለይ ካልገለጹ 0, 1, 2, ... የሚሉ ኢንቲጀር(integer) እሴቶችን ይመድባል። ካስፈለገ የረድፍ መለያዎችን በእጅ መግለጽ ይቻላል። በዳታፍሬም ውስጥ የረድፍ መለያዎች ዝርዝርን [**ኢንዴክስ(Index)**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html) ብለው ይጠራሉ፣ እና በኮንስትራክተሩ ውስጥ ያለውን `index` ፓራሜተር(parameter) በመጠቀም እሴቱን ማዘጋጀት ይቻላል።

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

| | Bob | Sue |
| --- | --- | --- |
| Product A | I liked it. | Pretty good. |
| Product B | It was awful. | Bland. |

### ሲሪዝ
[ሲሪዝ(Series)](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) ከዳታ እሴቶች የተሠራ ተከታታይ(sequence) ወይም [ቬክተር(vector)](/posts/vector-spaces-subspaces-and-matrices/#የረድፍ-ቬክተሮች-እና-የአምድ-ቬክተሮች) ነው።

```python
pd.Series([1, 2, 3, 4, 5])
```

ሲሪዝ በመሠረቱ እንደ ዳታፍሬም አንድ ነጠላ አምድ ነው። ስለዚህ በተመሳሳይ [ኢንዴክስ](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html) መያዝ ይችላል፣ ልዩነቱ ግን 'የአምድ ስም' ፋንታ በቀላሉ 'ስም'([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)) ያለው መሆኑ ነው።

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

ሲሪዝ እና ዳታፍሬም እርስ በርሳቸው በጣም ቅርብ ግንኙነት አላቸው። ዳታፍሬምን በቀላሉ እንደ ሲሪዞች ስብስብ ብለው ማሰብ ለመረዳት ይረዳል።

### የዳታ ፋይል ማንበብ
ብዙ ጊዜ ዳታን በቀጥታ ከመጻፍ ይልቅ ቀድሞ ያለን ዳታ አምጥተን እንጠቀማለን። ዳታ በተለያዩ ቅርጸቶች(format) ሊቀመጥ ይችላል፣ ከሁሉ መሠረታዊው ግን CSV ፋይል ነው። የCSV ፋይል ይዘት ብዙውን ጊዜ ከታች እንዳለው ይመስላል።

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

ይህም ማለት CSV ፋይል እያንዳንዱን እሴት በኮማ(comma) የሚለይ ሰንጠረዥ ነው። ስለዚህም ስሙ "Comma-Separated Values", CSV ሆኗል።

የCSV ፋይል ቅርጸት ያለውን ዳታ ወደ ዳታፍሬም ለማስገባት [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) ፋንክሽን(function) ይጠቀማሉ።

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

የዳታፍሬሙን ቅርፅ [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) ፕሮፐርቲ(property) በመጠቀም ማረጋገጥ ይችላሉ።

```python
product_reviews.shape
```

```
(129971, 14)
```

ከላይ ያለው የምሳሌ ውጤት ያ ዳታፍሬም 129971 ሬኮርዶችን እና 14 አምዶችን እንደሚይዝ ያሳያል።

[`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) ሜተድ(method) በመጠቀም የዳታፍሬሙን የመጀመሪያ አምስት ረድፎች ማየት ይችላሉ።

```python
product_reviews.head()
```

[`pd.read_csv()` ፋንክሽኑ ከ30 በላይ ፓራሜተሮች አሉት](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)። ለምሳሌ ሊጫን የሚፈለገው CSV ፋይል በራሱ ኢንዴክስን ካካተተ፣ በፓንዳስ በራሱ ኢንዴክስ እንዲያደርግ ከመተው ይልቅ `index_col` ፓራሜተሩን በመግለጽ ያ አምድ ኢንዴክስ እንዲሆን ማድረግ ይችላሉ።

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### የዳታ ፋይል መጻፍ
[`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html) ሜተድ(method) በመጠቀም ዳታፍሬምን ወደ CSV ፋይል ማውጣት ይችላሉ። እንደሚከተለው ይጠቀሙበታል።

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## ትምህርት 2. ኢንዴክሲንግ፣ መምረጥ እና መመደብ
በፓንዳስ ዳታፍሬም ወይም ሲሪዝ ውስጥ የተወሰኑ እሴቶችን መምረጥ ማለት በማንኛውም የዳታ ሂደት ውስጥ እስካልተለፈ የማይቀር እርምጃ ስለሆነ፣ አስፈላጊ የዳታ ነጥቦችን በፍጥነትና በብቃት እንዴት መምረጥ እንደሚቻል በቅድሚያ መማር ያስፈልጋል።

### የፓይተን መደበኛ መዳረሻዎች
መደበኛ የፓይተን ኦብጀክቶች በጣም ጥሩ የዳታ ኢንዴክሲንግ ዘዴዎችን ይሰጣሉ፣ እና ፓንዳስም እነዚህን ዘዴዎች በተመሳሳይ ሁኔታ ይሰጣል።

#### የኦብጀክት ባህሪ
በፓይተን ውስጥ የኦብጀክት ባህሪ እሴት(property) ወደዚያ ባህሪ ስም(attribute) በመጠቀም መድረስ ይቻላል። ለምሳሌ `example_obj` ኦብጀክት `title` የተባለ ባህሪ ካለው `example_obj.title` በማለት ሊጠራ ይችላል። በፓንዳስ ዳታፍሬም አምዶችም ላይ በተመሳሳይ ሁኔታ መድረስ ይቻላል።

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

#### የዲክሽነሪ ኢንዴክሲንግ
እንዲሁም በፓይተን የዲክሽነሪ ዳታ አይነት ላይ የኢንዴክሲንግ ኦፕሬተር(`[]`) በመጠቀም በዲክሽነሪው ውስጥ ያሉ እሴቶችን ማግኘት ይቻላል። በፓንዳስ ዳታፍሬም አምዶችም ላይ በተመሳሳይ መንገድ መድረስ ይቻላል።

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

በኦብጀክት ባህሪ መዳረሻ እና በዲክሽነሪ ኢንዴክሲንግ መዳረሻ ሁለቱም ትክክለኛ ናቸው፣ ግን የዲክሽነሪ ኢንዴክሲንግ ዘዴ እንደ ክፍት ቦታ(space) ያሉ ልዩ ቁምፊዎችን የያዙ የአምድ ስሞችንም ማስተናገድ መቻሉ ጥሩ ጥቅም አለው(e.g. `reviews['country providence']` ይቻላል፣ ነገር ግን `reviews.country providence` እንደሚል መድረስ አይቻልም)።

እንዲሁ በተመረጠው የፓንዳስ ሲሪዝ ውስጥ ደግሞ እንደገና የኢንዴክሲንግ ኦፕሬተሩን በመጠቀም የግለሰብ እሴቶችን ማንበብ ይቻላል።

```python
reviews['country'][0]
```

```
'Italy'
```

### የፓንዳስ ልዩ መዳረሻዎች
ከላይ የተጠቀሱት የኢንዴክሲንግ ኦፕሬተር ወይም የኦብጀክት ባህሪ በመጠቀም የሚደረሰው መንገድ ከሌሎች የፓይተን ኢኮሲስተም ጋር በተፈጥሮ የሚስማማ ስለሆነ ጥሩ ነው፣ ነገር ግን ፓንዳስ ከዚህ በተጨማሪ የራሱ ልዩ መዳረሻዎች የሆኑ [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) እና [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html) ይሰጣል።

#### በኢንዴክስ ላይ የተመሰረተ ምርጫ
`iloc` በመጠቀም **በኢንዴክስ ላይ የተመሰረተ ምርጫ(index-based selection)** ማድረግ ይቻላል። በዳታው ውስጥ ያለውን ቦታ በኢንቲጀር ቁጥር በመግለጽ ይመርጣል።

ለምሳሌ፣ እንደሚከተለው የዳታፍሬሙን የመጀመሪያ ረድፍ መምረጥ ይችላሉ።

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

በአምድ ላይ አስቀድመው ከዚያ በኋላ ረድፍ የሚመርጡት መደበኛ የፓይተን መንገድ በተለየ፣ `iloc` በቅድሚያ ረድፍን ከዚያ በኋላ አምድን ይመርጣል። የዳታፍሬሙን የመጀመሪያ አምድ እንደሚከተለው መምረጥ ይቻላል።

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

ከላይ ባለው ምሳሌ `:` ኦፕሬተሩን በመጠቀም ሁሉንም ረድፎች መርጠን፣ ከዚያ በውስጡ የመጀመሪያውን አምድ መርጠናል። ከዚህ በፊት የመጀመሪያው አምድ ውስጥ ሁለተኛውን(`1`) እና ሶስተኛውን(`2`) ረድፎች መምረጥ ከፈለጉ እንዲህ ያድርጉ።

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

ወይም ዝርዝር(list) ማስተላለፍ ይችላሉ።

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

አሉታዊ ቁጥሮችን በመጠቀም ከመጨረሻ ጀምሮ ያለውን ዳታ ማምረጥም ይቻላል። የሚከተለው ምሳሌ የመጨረሻዎቹን 5 ረድፎች ይመርጣል።

```python
reviews.iloc[-5:]
```

#### በመለያ ላይ የተመሰረተ ምርጫ
ሌላ መንገድ `loc` በመጠቀም **በመለያ ላይ የተመሰረተ ምርጫ(label-based selection)** ማድረግ ነው። በዚህ ጊዜ በዳታው ውስጥ ያለውን ቦታ ሳይሆን የኢንዴክሱን እሴት በመጠቀም ይመርጣል።

ለምሳሌ፣ ኢንዴክሱ 0 የሆነው ረድፍ ውስጥ ለ 'country' አምድ የሚዛመደውን ኤንትሪ እንደሚከተለው ማግኘት ይቻላል።

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` የዳታሴቱን ኢንዴክስ እሴቶች ችላ ብሎ አንድ ትልቅ ማትሪክስ እንዳለ አድርጎ በቦታ ላይ ተመስርቶ የግለሰብ ኤንትሪዎችን ይደርሳል። በሌላ በኩል `loc` ደግሞ የኢንዴክስ መረጃን በመጠቀም ይሠራል። ብዙ ጊዜ በኢንዴክስ ውስጥም ትርጉም ያለው መረጃ ስለሚኖር፣ በብዙ ሁኔታዎች `loc` ከ `iloc` የበለጠ ቀላልና ቀጥተኛ ነው።

#### `iloc` እና `loc` በክልል መግለጫ የሚከተሉት ልዩነት
`iloc` የፓይተን መደበኛ ላይብረሪ ኢንዴክሲንግ ስርዓትን በትክክል ይከተላል፣ ስለዚህ `0:10` ማለት 0 እስከ 10 **ሳይጨምር** ያለውን ግማሽ ክፍት ክልል፣ ማለትም `0,...,9` ነው።

በሌላ በኩል `loc` ክልሉን እንደ ዝግ ክልል ስለሚያየው፣ `0:10` ማለት 0 እስከ 10 **ጨምሮ**፣ ማለትም `0,...,10` ነው።

ይህ ልዩነት የተደረገው ምክንያት `loc` ከኢንቲጀር በተጨማሪ ማንኛውንም መደበኛ የዳታ አይነት እንደ ኢንዴክስ መጠቀም ስለሚችል ነው። ለምሳሌ `Apples, ..., Potatoes, ...` የሚሉ የኢንዴክስ እሴቶች ያሉት ዳታፍሬም አለን እና ከዚህ ውስጥ በፊደል ቅደም ተከተል 'Apples' እስከ 'Potatoes' ያሉትን ምርቶች መምረጥ እንፈልጋለን እንበል። በፊደል ቅደም ተከተል s በኋላ t ስለሚመጣ፣ ማለትም 'Potatoes' በቀጥታ ቀጥሎ ሊመጣ የሚችለው የፊደል ጥምረት 'Potatoet' ስለሆነ፣ "'Apples' እስከ 'Potatoet' በፊት"(`df.loc['Apples':'Potatoet']`) ብለው ከመግለጽ ይልቅ በቀላሉ "'Apples' እስከ 'Potatoes'"(`df.loc['Apples':'Potatoes']`) ብለው መግለጽ እጅግ የበለጠ ቀጥተኛ ነው። እንደዚህ ባሉ ከኢንቲጀር ውጭ የሆኑ ኢንዴክሶች ላይ ይህ ኋለኛው መንገድ ብዙ ጊዜ የበለጠ ተፈጥሯዊ ስለሆነ `loc` ይህንን አቀራረብ ይከተላል።

ከዚህ ውጭ ሌሎቹ የአሠራር መንገዶች በመሠረቱ አንድ ናቸው።

> በግል እኔ በከፍ ቅደም የተደረደሩ ኢንቲጀር ኢንዴክሶች ባሉት ዳታሴቶች ውስጥ `:` ኦፕሬተሩን በመጠቀም ክልል ማስገለጽ ሲያስፈልግ ከዚህ ልዩነት የሚመጣ ግራ መጋባት ለመከላከል `iloc` እመርጣለሁ፤ ከዚያ ውጭ ግን በቀላሉ የሚገባ በመሆኑ `loc` እመርጣለሁ።
{: .prompt-tip }

### ኢንዴክስን ማስተካከል
ኢንዴክስን እንደ ፍላጎት ማስተካከልም ይቻላል። [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) ሜተድ(method) በመጠቀም ከሚከተለው ምሳሌ እንደሚታየው በዳታሴቱ ውስጥ ያለ የተወሰነ አምድን አዲሱ ኢንዴክስ እንዲሆን መወሰን ይቻላል።

```python
reviews.set_index("title")
```

### በሁኔታ የተወሰነ ምርጫ
ከላይ የተገለጹት ዘዴዎች ዳታፍሬሙ ራሱ ያለውን መዋቅራዊ ባህሪ በመጠቀም ዳታን እንዴት ማቀናበርና መምረጥ እንደሚቻል ያሳያሉ። ነገር ግን ከዚያ በላይ በመሄድ የበለጠ ውስብስብ የሆኑ ሁኔታዎችን የሚያሟሉ ዳታዎችንም መምረጥ ይቻላል።

ለምሳሌ ስለ የወይን ምርቶች መረጃ የሚይዝ ዳታፍሬም አለን እና ከዚህ ውስጥ 90 ወይም ከዚያ በላይ ነጥብ ያገኙ የጣሊያን ወይኖችን ብቻ መምረጥ አለብን እንበል።

```python
reviews.country == 'Italy'
```

ይህ የሁኔታ ገለጻ `True`/`False` ቡሊያን(boolean) እሴቶችን የያዘ ሲሪዝ ይመልሳል።

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` በመሠረቱ በመለያ ላይ የተመሰረተ ቢሆንም፣ ቡሊያን አሬይ(array) ወይም ማዛመድ የሚችል ቡሊያን ሲሪዝ እንደ ግቤት መቀበል ይችላል](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)። ስለዚህ እንደሚከተለው የጣሊያን ወይን ዳታዎችን ብቻ መምረጥ ይቻላል።

```python
reviews.loc[reviews.country == 'Italy']
```

ብዙ ሁኔታዎችን `&` ወይም `|` ኦፕሬተሮች በመጠቀም ማጣመር ይችላሉ። የጣሊያን **እና** 90 ወይም ከዚያ በላይ ነጥብ ያለው የወይን ዳታ ለመምረጥ እንዲህ ያድርጉ።

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

የጣሊያን **ወይም** 90 ወይም ከዚያ በላይ ነጥብ ያለው የወይን ዳታ ደግሞ እንደሚከተለው መምረጥ ይቻላል።

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

በተጨማሪም ፓንዳስ ጥቂት አብሮ የተሰጡ የሁኔታ መምረጫዎችን ያለው ሲሆን፣ ከእነሱ ውስጥ በተለይ `isin` እና `isnull`/`notnull` ናቸው።

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) ዝርዝር ውስጥ ካሉ እሴቶች አንዱን ይይዛልን ወይስ አይይዝምን በሚል ቡሊያን(`True` ወይም `False`) ማስክ(mask) ሲሪዝ ይመልሳል፣ ይህን ተጠቅመውም ዳታ መምረጥ ይችላሉ። ለምሳሌ እንደሚከተለው የጣሊያን ወይም የፈረንሳይ ወይን ዳታዎችን መምረጥ ይችላሉ።

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) የጎደለ እሴት(`NaN`) ያላቸውን ወይም የሌላቸውን ዳታዎች ለመምረጥ ይጠቅማሉ። ለምሳሌ እንደሚከተለው የዋጋ ዳታ ያልጎደለባቸውን የወይን ዳታዎች ብቻ መምረጥ ይችላሉ።

```python
reviews.loc[reviews.price.notna()]
```

> ለማስታወሻ፣ በመጀመሪያው የKaggle ኮርስ ውስጥ ያልተጠቀሰ ነገር ቢሆንም [`iloc`ም ቡሊያን አሬይ(array) መቀበል ይችላል](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)። ግን `loc` እንደሚያደርገው ሲሪዝ ሳይሆን አሬይ ብቻ ስለሚደግፍ፣ ከላይ እንዳለው ዓይነት መተግበሪያ ማድረግ አስቸጋሪ ነው።
{: .prompt-tip }

### የዳታ መመደብ
ለዳታፍሬም አዲስ ዳታ መመደብ ወይም ያለውን መተካትም ይቻላል።

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

## ትምህርት 3. የማጠቃለያ ፋንክሽኖች እና ማፕ(Maps)
### የዳታ አጠቃላይ ሁኔታን ማየት
[`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) ሜተድ(method) ለተሰጠው አምድ ከፍተኛ ደረጃ አጠቃላይ ማጠቃለያ ይሰጣል።

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

የ `describe()` ሜተድ ውጤት እንደ ግቤቱ የዳታ አይነት ይለያያል። ቁጥራዊ ዳታ ሳይሆን የጽሑፍ ዳታ ሲሆን እንደሚከተለው ውጤት ይመልሳል።

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

ወይም የሚፈልጉትን የተወሰነ ስታቲስቲክስ(statistics) ብቻ ማግኘት ይችላሉ።

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

በዳታፍሬም ውስጥ እያንዳንዱ ልዩ እሴት ስንት ጊዜ እንደታየ ማወቅ ከፈለጉ [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html) ሜተድ(method) መጠቀም ይችላሉ።

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

### ማፕ(Maps)
**ማፕ(map)** የሚለው ቃል ከሒሳብ የተወሰደ ሲሆን፣ አንድ ስብስብን ከሌላ ስብስብ ጋር የሚያዛምድ ፋንክሽን ማለት ነው። በዳታ ሳይንስ ውስጥ ብዙ ጊዜ የተሰጠውን ዳታ ወደ ሌላ የአቀራረብ ቅርጽ መቀየር ያስፈልጋል፣ እና እንደዚህ ያሉ ስራዎች ሲደረጉ ማፖችን ስለሚጠቀሙ በጣም አስፈላጊ ናቸው።

በተለምዶ ሁለት ሜተዶችን ብዙ ጊዜ እንጠቀማለን።

[`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) ሜተድ(method) አንድ <u>እሴት</u> ወደ ሌላ ነጠላ እሴት የሚቀይር ፋንክሽን እንደ ግቤት ይቀበላል፣ እና ያን ፋንክሽን በተሰጠው <u>ሲሪዝ</u> ውስጥ ባሉ ሁሉም እሴቶች ላይ በጅምላ ከፈጸመ በኋላ አዲስ ሲሪዝ ይመልሳል። ለምሳሌ በወይን ነጥብ ዳታ ላይ በጅምላ የአማካይ እሴቱን ቀንሰን ልዩነት(deviation) ማግኘት ከፈለግን እንዲህ ማድረግ እንችላለን።

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

[`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) ሜተድ(method) በእያንዳንዱ <u>ረድፍ</u> ላይ የተበጀ ፋንክሽን በመጠራት በመላው <u>ዳታፍሬም</u> ላይ ለውጥ ማድረግ ሲፈልጉ ይጠቅማል።

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

`apply()` ሜተዱን `axis='index'` ፓራሜተር ጋር በመጠራት በእያንዳንዱ ረድፍ ሳይሆን በእያንዳንዱ አምድ ላይ ፋንክሽኑን መፈጸም ይችላሉ።

`Series.map()` እና `DataFrame.apply()` እያንዳንዳቸው አዲስ የተቀየረ ሲሪዝ እና ዳታፍሬም ይመልሳሉ፤ በመጀመሪያው ዳታ ላይ ግን ምንም አይነት ለውጥ አያደርጉም።

| ሜተድ | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| የሚተገበርበት ነገር | ሲሪዝ | ዳታፍሬም |
| የሚተገበርበት ክፍል | በግለሰብ እሴት ደረጃ ይተገበራል <br>(ሲሪዝን [የአምድ ቬክተር(column vector)](/posts/vector-spaces-subspaces-and-matrices/#የረድፍ-ቬክተሮች-እና-የአምድ-ቬክተሮች) ብለን ካየነው በረድፍ ደረጃ ይተገበራል) | በመሠረቱ በረድፍ ደረጃ ይተገበራል <br> አማራጭ ሲገለጽ በአምድ ደረጃ ላይም ሊተገበር ይችላል |

> ለማስታወሻ [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) እና [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html) ደግሞ አሉ።
> - `Series.apply()`:
>   - `by_row='compat'`(ነባሪ): ከ `Series.map()` ጋር በተመሳሳይ ሁኔታ ይሠራል
>   - `by_row=False`: ሙሉ ሲሪዙን በአንድ ጊዜ ለፋንክሽኑ ግቤት ያስተላልፋል(`axis='index'` ተብሎ ሲገለጽ `DataFrame.apply()` የሚሠራበትን መንገድ ይመስላል)
> - `DataFrame.map()`: በዳታፍሬም ውስጥ ባሉ የግለሰብ እሴቶች ላይ ፋንክሽንን ይተገብራል(ዒላማው ሲሪዝ ሳይሆን ዳታፍሬም መሆኑን ካስቀረን፣ ከ `Series.map()` ጋር ተመሳሳይ ነው)
{: .prompt-tip }

በእውነቱ ፓንዳስ በራሱ ብዙ ጊዜ የሚጠቀሙ ማፖችን ይደግፋል። ቀደም ብለን ያየነው ምሳሌ በሚከተለው እጅግ ቀላል ኮድም ሊተገበር ይችላል፣ በዚህ ጊዜም ፓንዳስ ዓላማውን በመረዳት በትክክል ይሠራል።

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

ከዚህም በላይ፣ ፓንዳስ ርዝመታቸው አንድ የሆኑ ሲሪዞች መካከል ኦፕሬሽኖችን ይደግፋል። በወይን ዳታ ምሳሌው ውስጥ የምርት አገርና የምርት ክልል መረጃን እንደሚከተለው በጽሑፍ ማዋሃድም ይቻላል።

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

እነዚህ ኦፕሬሽኖች በፓንዳስ ውስጥ የተገነቡ የስሌት ፍጥነት ማሻሻያ ዘዴዎችን ስለሚጠቀሙ፣ ከ `map()` ወይም `apply()` ሜተዶች የበለጠ ፈጣን ናቸው፤ እንዲሁም ፓንዳስ ለሁሉም መደበኛ የፓይተን ኦፕሬተሮች(`>`, `<`, `==` ወዘተ) በዚህ ዓይነት መንገድ መሥራት ይችላል። ቢሆንም `map()` እና `apply()` የበለጠ ተለዋዋጭ ስለሆኑ እና የበለጠ ውስብስብ ስራዎችን ማከናወን ስለሚችሉ፣ እነዚህን ሜተዶችም ማወቅ ጠቃሚ ነው።
