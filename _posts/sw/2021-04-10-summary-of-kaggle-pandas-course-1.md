---
title: "Muhtasari wa maudhui ya kozi ya Kaggle 'Pandas' (1) - Somo la 1-3"
description: "Muhtasari wa kutumia Pandas kusafisha na kuchakata data. Chapisho hili linafupisha sehemu ya baadaye ya kozi ya wazi ya Kaggle 'Pandas' (Somo la 1-3)."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Summary-of-Kaggle-Pandas-Course/
---

Hapa ninaweka muhtasari wa yale niliyoyasoma kupitia kozi ya [Pandas](https://www.kaggle.com/learn/pandas) ya Kaggle.  
Kwa kuwa maudhui ni mengi kiasi, nimeyagawa katika sehemu 2.
- Sehemu ya 1: Somo la 1-3 (makala hii)
- [Sehemu ya 2: Somo la 4-6](/posts/summary-of-kaggle-pandas-course-2/)

![Cheti cha Kukamilisha](/assets/img/kaggle-pandas/certificate.png)

## Somo la 1. Kuunda, Kusoma na Kuandika
### Kuingiza Pandas

```python
import pandas as pd
```

Katika Pandas kuna vitu viwili muhimu vya msingi vinavyoitwa **fremu ya data (DataFrame)** na **mfululizo (Series)**.

### Fremu ya data
[Fremu ya data (DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) inaweza kufikiriwa kama jedwali au [matrisi](/posts/vector-spaces-subspaces-and-matrices/#matrisi-na-nafasi-ya-matrisi). Inaundwa kama matrisi ya *vipengele (entries)* vilivyo huru, ambapo kila kipengele kina *thamani (value)* fulani na hulingana na *safu (row)* au *rekodi (record)* moja pamoja na *kolamu (column)* moja.

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

| | Yes | No |
| --- | --- | --- |
| 0 | 50 | 131 |
| 1 | 21 | 2 |

Vipengele vya fremu ya data si lazima viwe vya namba tu; mfano ufuatao ni fremu ya data yenye thamani za maandishi (maoni yaliyoachwa na watumiaji).

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

| | Bob | Sue |
| --- | --- | --- |
| 0 | I liked it. | Pretty good. |
| 1 | It was awful. | Bland. |

Unapounda kitu cha fremu ya data, hutumia konstrakta `pd.DataFrame()` na kuitangaza kwa sintaksia ya kamusi (dictionary) ya Python. Kwenye key huweka jina la kolamu, na kwenye value huweka orodha (list) ya vipengele vya kuandikwa. Hii ndiyo njia ya kawaida ya kutangaza fremu mpya ya data.

Unapotangaza fremu ya data, lebo za kolamu hupewa majina ya kolamu husika, lakini lebo za safu, usipozibainisha kando, hupewa nambari kamili 0, 1, 2, ... . Ikihitajika, unaweza kuzibainisha lebo za safu kwa mkono. Kwenye fremu ya data, orodha ya lebo za safu huitwa [**indeksi (Index)**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html), na unaweza kuweka thamani zake kwa kutumia kigezo cha `index` cha konstrakta.

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

| | Bob | Sue |
| --- | --- | --- |
| Product A | I liked it. | Pretty good. |
| Product B | It was awful. | Bland. |

### Mfululizo
[Mfululizo (Series)](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) ni mfuatano wa thamani za data au [vekta](/posts/vector-spaces-subspaces-and-matrices/#vekta-za-safu-na-vekta-za-kolamu).

```python
pd.Series([1, 2, 3, 4, 5])
```

Kimsingi, mfululizo ni sawa na kolamu moja ya fremu ya data. Kwa hiyo, vivyo hivyo unaweza kuweka [indeksi](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html), ila badala ya "jina la kolamu" huwa na "jina" tu ([`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html)).

```python
pd.Series([30, 35, 40], index=['12015 Sales', '12016 Sales', '12017 Sales'], name='Product A')
```

```
12015 Sales    30
12016 Sales    35
12017 Sales    40
Name: Product A, dtype: int64
```

Mfululizo na fremu ya data vina uhusiano wa karibu sana. Husaidia kuelewa ukichukulia fremu ya data kuwa mkusanyiko tu wa misururu.

### Kusoma faili za data
Mara nyingi, badala ya kuandika data moja kwa moja, huleta data iliyopo tayari na kuitumia. Data inaweza kuhifadhiwa katika miundo mbalimbali, na aina ya msingi zaidi ni faili ya CSV. Yaliyomo ndani ya faili ya CSV kwa kawaida huonekana kama yafuatayo.

```csv
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```

Yaani, faili ya CSV ni jedwali linalotenganisha kila thamani kwa koma (comma). Ndiyo maana jina lake ni "Comma-Separated Values", CSV.

Unapopakia data ya muundo wa faili ya CSV kama fremu ya data, hutumia functshi ya [`pd.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv")
```

Unaweza kukagua umbo la fremu ya data kwa kutumia sifa ya [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html).

```python
product_reviews.shape
```

```
(129971, 14)
```

Matokeo ya mfano hapo juu yanamaanisha kuwa fremu hiyo ya data ina rekodi 129971 na kolamu 14.

Unaweza kuona safu tano za kwanza za fremu ya data kwa kutumia mbinu ya [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html).

```python
product_reviews.head()
```

[Functshi ya `pd.read_csv()` ina zaidi ya vigezo 30](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Kwa mfano, ikiwa faili ya CSV unayotaka kuipakia tayari ina indeksi yake, unaweza kuweka thamani ya kigezo cha `index_col` ili Pandas itumie kolamu hiyo kama indeksi badala ya kutengeneza indeksi kiotomatiki.

```python
product_reviews = pd.read_csv("../input/product-reviews/example-data.csv", index_col=0)
```

### Kuandika faili za data
Ukitumia mbinu ya [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html), unaweza kuhamisha fremu ya data kwenda kwenye faili ya CSV. Hutumika kama ifuatavyo.

```python
product_reviews.to_csv("../output/product-reviews/example-data.csv")
```

## Somo la 2. Uwekaji Faharisi, Uteuzi & Ugawaji
Kuchagua thamani maalum za kutumia katika fremu ya data au mfululizo wa Pandas ni hatua inayopitiwa na karibu kazi zote za uchakataji wa data, kwa hiyo ni muhimu kujifunza kwanza jinsi ya kuchagua pointi za data zinazohitajika haraka na kwa ufanisi.

### Vifikiaji asilia vya Python
Vitu asilia vya Python hutoa njia bora za kuweka faharisi za data, na Pandas pia hutoa njia hizo hizo.

#### Sifa za kitu
Katika Python, unaweza kufikia thamani ya sifa (property) ya kitu kwa jina la sifa hiyo (attribute). Kwa mfano, kama kitu `example_obj` kina sifa ya `title`, unaweza kuiita kwa `example_obj.title`. Vivyo hivyo unaweza kufikia kolamu za fremu ya data ya Pandas.

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

#### Uwekaji faharisi wa kamusi
Pia, kwa aina ya data ya kamusi (dictionary) katika Python, unaweza kufikia thamani ndani ya kamusi kwa kutumia opereta wa uwekaji faharisi (`[]`). Vivyo hivyo unaweza kufikia kolamu za fremu ya data ya Pandas kwa njia hiyo.

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

Njia zote mbili, ya kufikia kwa sifa ya kitu na ya kuweka faharisi kama kamusi, ni halali; lakini njia ya uwekaji faharisi wa kamusi ina faida ya kushughulikia pia majina ya kolamu yenye alama maalum kama nafasi tupu (k.m. `reviews['country providence']` linawezekana, lakini ufikiaji kama `reviews.country providence` hauwezekani).

Hata ndani ya mfululizo wa Pandas uliouchagua kwa njia hiyo, unaweza tena kutumia opereta wa uwekaji faharisi kusoma thamani ya mtu mmoja mmoja.

```python
reviews['country'][0]
```

```
'Italy'
```

### Vifikiaji maalum vya Pandas
Ufikiaji kupitia sifa ya kitu au opereta wa uwekaji faharisi uliotajwa hapo juu ni mzuri kwa sababu unaendana kiasili na ekolojia nyingine ya Python, lakini Pandas pia hutoa vifikiaji vyake maalum, yaani [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) na [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

#### Uteuzi unaotegemea indeksi
Ukitumia `iloc`, unaweza kufanya **uteuzi unaotegemea indeksi (index-based selection)**. Huchagua data kwa kubainisha nafasi ndani ya data kwa nambari kamili.

Kwa mfano, unaweza kuchagua safu ya kwanza ya fremu ya data kama ifuatavyo.

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

Tofauti na njia ya asili ya Python ambayo huchagua kolamu kwanza kisha safu, `iloc` huchagua safu kwanza kisha kolamu. Kolamu ya kwanza ya fremu ya data inaweza kuchaguliwa kama ifuatavyo.

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

Katika mfano hapo juu, tulitumia opereta `:` kuchagua safu zote, kisha tukachagua kolamu ya kwanza ndani yake. Ikiwa unataka kuchagua safu ya pili (`1`) na ya tatu (`2`) ya kolamu ya kwanza, unaweza kufanya hivi.

```python
reviews.iloc[1:3, 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Au unaweza pia kupitisha orodha.

```python
reviews.iloc[[1, 2], 0]
```

```
1    Portugal
2          US
Name: country, dtype: object
```

Unaweza pia kutumia nambari hasi kuchagua data kuanzia mwisho. Mfano ufuatao huchagua safu 5 za mwisho za data.

```python
reviews.iloc[-5:]
```

#### Uteuzi unaotegemea lebo
Njia nyingine ni kutumia `loc` kufanya **uteuzi unaotegemea lebo (label-based selection)**. Katika hali hii, huchagua kwa kutumia thamani ya indeksi badala ya nafasi ndani ya data.

Kwa mfano, unaweza kupata kipengele kinacholingana na kolamu ya 'country' katika safu yenye thamani ya indeksi 0 kama ifuatavyo.

```python
reviews.loc[0, 'country']
```

```
'Italy'
```

`iloc` hupuuza thamani za indeksi za seti ya data na kuichukulia kama matrisi moja kubwa, hivyo hufikia vipengele binafsi kwa kutegemea nafasi. Kwa upande mwingine, `loc` hufanya kazi kwa kutumia taarifa za indeksi. Kwa kuwa mara nyingi indeksi nayo huwa na taarifa zenye maana, `loc` huwa ya kueleweka zaidi kuliko `iloc` katika hali nyingi.

#### Tofauti ya namna `iloc` na `loc` zinavyobainisha vipindi
`iloc` hutumia mfumo wa uwekaji faharisi wa maktaba ya kawaida ya Python bila kubadilika, na kwa hiyo `0:10` humaanisha kipindi nusu-wazi cha 0 hadi chini ya 10, yaani `0,...,9`.

Kwa upande mwingine, `loc` hutambua kipindi kama kilichofungwa, kwa hiyo `0:10` humaanisha 0 hadi 10 **ikiwemo**, yaani `0,...,10`.

Sababu ya tofauti hii ni kwamba `loc` inaweza kutumia si nambari kamili tu bali pia aina zote za kawaida za data kama indeksi. Kwa mfano, fikiria kuna fremu ya data yenye thamani za indeksi kama `Apples, ..., Potatoes, ...`, na hapa unahitaji kuchagua mazao yaliyo katika wigo wa kialfabeti kuanzia 'Apples' hadi 'Potatoes'. Kwa kuwa baada ya herufi s huja t, mchanganyiko wa herufi unaoweza kuja mara moja baada ya 'Potatoes' ungekuwa 'Potatoet', hivyo badala ya kubainisha "`kutoka 'Apples' hadi kabla ya 'Potatoet'`" (`df.loc['Apples':'Potatoet']`), ni rahisi zaidi na ya moja kwa moja kubainisha tu "`kutoka 'Apples' hadi 'Potatoes'`" (`df.loc['Apples':'Potatoes']`). Kwa namna hii, kwa indeksi zinazotumia aina za data zisizo nambari kamili, njia ya pili huwa ya kueleweka zaidi, na ndiyo maana `loc` hufuata mtindo huo.

Mbali na hilo, tabia zilizobaki kimsingi ni zilezile.

> Binafsi, ninapohitaji kubainisha wigo kwa kutumia opereta `:` katika seti ya data yenye indeksi za nambari kamili zilizopangwa kwa mpangilio wa kupanda, napendelea `iloc` ili kuepuka mkanganyiko unaotokana na tofauti hiyo ya namna ya kubainisha wigo; katika hali nyingine, hupendelea `loc` kwa kuwa ni ya moja kwa moja zaidi.
{: .prompt-tip }

### Kubadilisha indeksi
Inawezekana pia kurekebisha indeksi kulingana na haja. Ukilitumia mbinu ya [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html), unaweza kuteua kolamu maalum ndani ya seti ya data kama indeksi mpya, kama ilivyo kwenye mfano ufuatao.

```python
reviews.set_index("title")
```

### Uteuzi wa masharti
Maelezo yaliyoelezwa hapo juu yanahusu njia za kuchakata na kuchagua data kwa kutumia sifa za kimuundo za fremu ya data yenyewe. Hata hivyo, unaweza kwenda hatua zaidi na kuchagua data zinazotimiza masharti mahususi yaliyo changamano zaidi.

Kwa mfano, fikiria hali ambapo katika fremu ya data iliyo na taarifa za bidhaa za mvinyo, unahitaji kuchagua tu data za mvinyo wa Italia wenye alama 90 au zaidi.

```python
reviews.country == 'Italy'
```

Sharti hili hurudisha mfululizo unaoundwa na thamani za boole `True`/`False`.

```
0          True
1         False
          ...  
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
```

[`loc` kimsingi hutegemea lebo, lakini inaweza pia kupokea safu ya boole au mfululizo wa boole unaoweza kulinganishwa](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html). Kwa hiyo, unaweza kuchagua tu data za mvinyo wa Italia kama ifuatavyo.

```python
reviews.loc[reviews.country == 'Italy']
```

Unaweza kuunganisha masharti kadhaa kwa opereta `&` au `|`. Ili kuchagua data za mvinyo ambazo ni za Italia **na pia** zina alama 90 au zaidi, fanya kama ifuatavyo.

```python
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
```

Data za mvinyo ambazo ni za Italia **au** zina alama 90 au zaidi zinaweza kuchaguliwa kama ifuatavyo.

```python
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
```

Aidha, Pandas ina viteuzi vichache vya masharti vilivyojengewa ndani; miongoni mwa muhimu zaidi ni `isin` na `isnull`/`notnull`.

[`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html) hurudisha mfululizo wa maski ya boole (`True` au `False`) unaoonyesha kama thamani ni mojawapo ya zile "zilizomo ndani (is in)" ya orodha, na unaweza kuitumia kuchagua data. Kwa mfano, unaweza kuchagua data za mvinyo wa Italia au Ufaransa kama ifuatavyo.

```python
reviews.loc[reviews.country.isin(['Italy', 'France'])]
```

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html)/[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html) hutumika unapochagua data zenye au zisizo na thamani pungufu (`NaN`). Kwa mfano, unaweza kuchagua tu data za mvinyo ambazo data ya bei haijakosekana kama ifuatavyo.

```python
reviews.loc[reviews.price.notna()]
```

> Kwa taarifa, ingawa si sehemu iliyokuwa kwenye kozi ya Kaggle asilia, [`iloc` nayo pia inaweza kupokea safu ya boole (array)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html). Hata hivyo, tofauti na `loc`, inasaidia array pekee na si mfululizo, hivyo ni vigumu kuitumia kwa namna iliyopanuliwa kama hapo juu.
{: .prompt-tip }

### Ugawaji wa data
Unaweza pia kugawa data mpya kwenye fremu ya data au kuandika juu ya data iliyopo.

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

## Somo la 3. Funksheni za Muhtasari na Uambatanishaji
### Kuangalia muhtasari wa data
Mbinu ya [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) hutoa muhtasari wa kiwango cha juu wa kolamu uliyopewa.

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

Matokeo ya mbinu ya `describe()` hubadilika kulingana na aina ya data ya ingizo. Kwa data ya maandishi badala ya ya namba, hurudisha matokeo kama yafuatayo.

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

Au unaweza kupata takwimu maalum unazotaka tu.

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

Ikiwa unataka kujua ni mara ngapi kila thamani ya kipekee imejitokeza ndani ya fremu ya data, unaweza kutumia mbinu ya [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html).

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

### Uambatanishaji (Maps)
**Uambatanishaji (map)** ni neno lililokopwa kutoka hisabati, linalomaanisha functshi inayolinganisha seti moja na seti nyingine. Katika sayansi ya data, mara nyingi tunahitaji kubadilisha data iliyotolewa kuwa muundo mwingine wa uwakilishi; tunapotenda kazi hizo hutumia uambatanishaji, na kwa hiyo ni muhimu sana.

Kwa kawaida mbinu mbili hutumiwa sana.

Mbinu ya [`Series.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html) hupokea functshi inayobadilisha <u>thamani</u> moja kuwa thamani nyingine moja, kisha huitumia kwa pamoja kwa thamani zote ndani ya <u>mfululizo</u> uliotolewa, na hurudisha mfululizo mpya uliopatikana kwa njia hiyo. Kwa mfano, kama unataka kupata mkengeuko kwa kutoa wastani kutoka data ya alama za mvinyo kwa pamoja, unaweza kufanya hivi.

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

Mbinu ya [`DataFrame.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) hutumika unapotaka kuita functshi maalum kwa kila <u>safu</u> na kutumia mabadiliko hayo kwa <u>fremu nzima ya data</u>.

```python
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
```

Ukiiita mbinu ya `apply()` pamoja na kigezo cha `axis='index'`, unaweza kutumia functshi hiyo kwa kila kolamu badala ya kila safu.

`Series.map()` na `DataFrame.apply()` kila moja hurudisha mfululizo mpya uliobadilishwa au fremu mpya ya data iliyobadilishwa, na havifanyi mabadiliko yoyote kwenye data asilia.

| Mbinu | `Series.map()` | `DataFrame.apply()` |
| :---: | :---: | :---: |
| Kitu kinachotumika juu yake | Mfululizo | Fremu ya data |
| Kitengo cha matumizi | Hutumika kwa kila thamani moja moja <br>(ukichukulia mfululizo kama [vekta ya kolamu](/posts/vector-spaces-subspaces-and-matrices/#vekta-za-safu-na-vekta-za-kolamu), hutumika kwa kiwango cha safu) | Kimsingi hutumika kwa kiwango cha safu <br> Inaweza pia kutumika kwa kiwango cha kolamu ukibainisha chaguo |

> Kwa taarifa, [`Series.apply()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html) na [`DataFrame.map()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.map.html) pia zipo.
> - `Series.apply()`:
>   - `by_row='compat'` (chaguo-msingi): hufanya kazi sawa na `Series.map()`
>   - `by_row=False`: hupitisha mfululizo mzima kama ingizo la functshi mara moja (hufanana na tabia ya `DataFrame.apply()` inapowekwa `axis='index'`)
> - `DataFrame.map()`: hutumia functshi kwa kila thamani moja moja ndani ya fremu ya data (inafanana na `Series.map()`, isipokuwa tu kwamba lengo ni fremu ya data badala ya mfululizo)
{: .prompt-tip }

Kwa kweli, Pandas yenyewe tayari inaunga mkono aina nyingi za uambatanishaji zinazotumika mara kwa mara. Mfano tulioona hapo awali unaweza pia kutekelezwa kwa msimbo mfupi zaidi kama ufuatao, na hata katika hali hiyo Pandas huelewa nia na kufanya kazi ipasavyo.

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

Si hayo tu, Pandas pia inaunga mkono uendeshaji kati ya misururu yenye urefu sawa. Katika mfano wa data ya mvinyo, inawezekana pia kuunganisha taarifa za nchi ya uzalishaji na eneo la uzalishaji kama maandishi kwa njia ifuatayo.

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

Kwa kuwa operesheni hizi hutumia mbinu za kuongeza kasi ya hesabu zilizojengewa ndani ya Pandas, huwa za haraka kuliko mbinu za `map()` au `apply()`, na Pandas inaweza kufanya kazi kwa namna hii kwa opereta zote za kawaida za Python (`>`, `<`, `==` n.k.). Hata hivyo, `map()` na `apply()` ni rahisi kubadilika zaidi na zinaweza kutekeleza kazi changamano zaidi, hivyo ni vyema pia kuzifahamu.
