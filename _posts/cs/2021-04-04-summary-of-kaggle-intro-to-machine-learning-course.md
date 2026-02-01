---
title: "Kaggle: Shrnutí kurzu „Intro to Machine Learning“"
description: "Shrnuji hlavní koncepty strojového učení a základní použití knihoven pandas a scikit-learn. Jde o souhrn veřejného kurzu Kaggle „Intro to Machine Learning“."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

Rozhodl jsem se studovat [veřejné vzdělávací kurzy Kaggle](https://www.kaggle.com/learn).
Po dokončení každého kurzu plánuji stručně sepsat, co jsem se v něm naučil. První článek je shrnutím kurzu [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning).

![Certificate of Completion](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lesson 1. Jak fungují modely
Začíná se zlehka a bez zbytečné zátěže. Jde o to, jak modely strojového učení fungují a jak se používají. Výklad je veden na jednoduchém příkladu rozhodovacího stromu (Decision Tree) v situaci, kdy potřebujeme predikovat ceny nemovitostí.

Hledání vzorů v datech se označuje jako **přizpůsobení (fitting)** nebo **trénování (training)** modelu. Data použitá při trénování se nazývají **trénovací data (training data)**. Po dokončení trénování lze model aplikovat na nová data a provádět **predikce (predict)**.

## Lesson 2. Základní průzkum dat
V jakémkoli projektu strojového učení je prvním krokem to, aby se vývojář s daty dobře seznámil. Teprve když pochopíme, jaké vlastnosti data mají, můžeme navrhnout vhodný model. K průzkumu a manipulaci s daty se obvykle používá knihovna [pandas](https://pandas.pydata.org/).

```python
import pandas as pd
```

Jádrem pandas je datový rámec (DataFrame), který si lze představit jako tabulku. Je podobný listu v Excelu nebo tabulce v SQL databázi. Pomocí metody `read_csv` lze načíst data ve formátu CSV.

```python
# Je dobré ukládat si cestu k souboru do proměnné, aby se k ní dalo snadno vracet.
file_path = "(cesta k souboru)"
# Načteme data a uložíme je do DataFrame s názvem 'example_data'
# (v praxi je samozřejmě lepší zvolit výstižnější jméno).
example_data = pd.read_csv(file_path)
```

Pomocí metody `describe` lze zobrazit souhrnné informace o datech.

```python
example_data.describe()
```

Tím získáme 8 položek:
- **count**: počet řádků se skutečnou hodnotou (bez chybějících hodnot)
- **mean**: průměr
- **std**: směrodatná odchylka
- **min**: minimum
- **25%**: 25. percentil
- **50%**: medián
- **75%**: 75. percentil
- **max**: maximum

## Lesson 3. Váš první model strojového učení
### Příprava dat
Je potřeba rozhodnout, které proměnné z daných dat použijeme pro modelování. Pomocí atributu **columns** u DataFrame lze zkontrolovat názvy sloupců.

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

Způsobů, jak z dat vybrat potřebné části, je víc; Kaggle to rozebírá do hloubky v kurzu [Pandas Micro-Course](https://www.kaggle.com/learn/pandas) (já jsem to shrnul v [samostatném článku](/posts/summary-of-kaggle-pandas-course/)). Tady použijeme dvě metody:
1. tečkovou notaci (dot notation)
2. použití seznamu (list)

Nejprve pomocí **dot-notation** vybereme sloupec odpovídající **predikovanému cíli (prediction target)** a uložíme ho jako **Series**. Series lze chápat jako DataFrame složený pouze z jednoho sloupce. Predikovaný cíl se typicky označuje jako **y**.

```python
y = melbourne_data.Price
```

Sloupce, které dáváme modelu na vstup pro predikci, se nazývají „**features**“ (česky obvykle *příznaky*). V příkladu s melbournskými cenami domů jsou to sloupce, které chceme použít k predikci ceny. Někdy se jako features použijí všechny sloupce kromě cíle, jindy je lepší vybrat jen jejich podmnožinu.  
Níže vybereme více features pomocí seznamu; všechny prvky seznamu musí být řetězce.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

Tato data se obvykle označují jako **X**.

```python
X = melbourne_data[melbourne_features]
```

Kromě `describe` se při analýze dat hodí i metoda `head`, která ukáže prvních 5 řádků.

```python
X.head()
```

### Návrh modelu
Ve fázi modelování se podle situace používají různé knihovny; jednou z nejčastějších je [scikit-learn](https://scikit-learn.org/stable/). Postup návrhu a použití modelu se dá shrnout takto:
- **Definice modelu (Define)**: zvolíme typ modelu a jeho parametry (parameters).
- **Trénování (Fit)**: nalezneme pravidelnosti v datech; to je jádro modelování.
- **Predikce (Predict)**: provedeme predikci pomocí natrénovaného modelu.
- **Vyhodnocení (Evaluate)**: zhodnotíme, jak přesné predikce jsou.

Níže je příklad, jak ve scikit-learn definovat a natrénovat model:

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

Mnoho modelů strojového učení obsahuje v procesu trénování určitý prvek náhodnosti. Nastavením hodnoty `random_state` lze zajistit, že při každém spuštění dostaneme stejné výsledky; pokud k tomu není zvláštní důvod, je dobrým zvykem ji nastavovat. Na konkrétní hodnotě nezáleží.

Po natrénování lze provést predikci takto:

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

## Lesson 4. Validace modelu
### Jak model validovat
Chceme-li model opakovaně zlepšovat, musíme měřit jeho výkon. Když s nějakým modelem děláme predikce, někdy se trefíme a někdy ne. Potřebujeme tedy metriku, která výkon predikcí vyjádří. Metrik existuje více; zde použijeme **MAE (Mean Absolute Error, průměrná absolutní chyba)**.

V případě predikce cen domů v Melbourne je chyba pro konkrétní dům:

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

MAE se spočítá tak, že vezmeme absolutní hodnotu každé chyby a zprůměrujeme ji:

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

Ve scikit-learn to lze získat takto:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Problém použití trénovacích dat pro validaci
V uvedeném kódu jsme pro trénování i validaci použili stejný dataset. To ale ve skutečnosti dělat nemáme. Kaggle to vysvětluje na následujícím příkladu:

> Ve skutečném realitním trhu barva vstupních dveří s cenou domu nijak nesouvisí.  
> 
> Ale shodou okolností v trénovacích datech byly všechny domy se zelenými dveřmi velmi drahé. Úkolem modelu je najít v datech pravidelnosti, které lze použít k predikci ceny, takže náš model v takové situaci tuto „pravidelnost“ zachytí a bude predikovat, že domy se zelenými dveřmi jsou drahé.
>
> Tímto způsobem budou predikce na trénovacích datech vypadat přesně.
>
> Jenže když budeme predikovat na nových datech, kde pravidlo „zelené dveře = drahý dům“ neplatí, model bude velmi nepřesný.

Model má smysl jen tehdy, když predikuje na nových datech, takže validaci musíme dělat na datech, která nebyla použita při trénování. Nejjednodušší způsob je během modelování část dat oddělit a použít ji jen pro měření výkonu. Tato data se nazývají **validační data (validation data)**.

### Oddělení validačního datasetu
Ve scikit-learn existuje funkce `train_test_split`, která data rozdělí na dvě části. Následující kód rozdělí data na trénovací část a validační část, přičemž validační část použijeme pro měření MAE (`mean_absolute_error`):

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

## Lesson 5. Underfitting a overfitting
### Přeučení a podučení
- **přeučení (overfitting)**: model se velmi přesně přizpůsobí trénovacímu datasetu, ale na validačním datasetu nebo jiných nových datech selhává
- **podučení (underfitting)**: model nedokáže z dat dostatečně vytěžit důležité příznaky a pravidelnosti, takže má slabý výkon i na trénovacím datasetu

Představme si situaci, kdy učíme model rozlišovat dvě třídy v datech zobrazených jako červené a modré body. V takovém případě lze zelenou křivku považovat za přeučený model, zatímco černá křivka představuje žádoucí model.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Zdroj obrázku*
> - autor: uživatel španělské Wikipedie [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Důležitá je pro nás přesnost na nových datech; výkon na nových datech odhadujeme pomocí validačního datasetu. Cílem je najít optimální bod (sweet spot) mezi podučením a přeučením.  
![](https://i.imgur.com/2q85n9s.png)  
V tomto kurzu Kaggle se jako příklad stále používá rozhodovací strom, ale přeučení a podučení jsou pojmy, které se týkají všech modelů strojového učení.

### Ladění hyperparametrů (hyperparameter tuning)
Následující příklad ukazuje, jak porovnat výkon modelu rozhodovacího stromu při změně hodnoty argumentu *max_leaf_nodes* (část načítání dat a oddělení validačního datasetu je vynechána):

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

Po dokončení ladění hyperparametrů se nakonec model natrénuje na všech dostupných datech, aby se maximalizoval výkon. Není už totiž potřeba držet validační dataset stranou.

## Lesson 6. Náhodné lesy (Random Forests)
Když zkombinujeme více různých modelů, často dosáhneme lepšího výkonu než s jedním modelem. Tomu se říká **ensemble (ansámbl)** a dobrým příkladem je **random forest**.

Random forest se skládá z mnoha rozhodovacích stromů a finální predikci získá jako průměr jejich predikcí. V mnoha případech dosahuje lepší přesnosti než jeden rozhodovací strom.
