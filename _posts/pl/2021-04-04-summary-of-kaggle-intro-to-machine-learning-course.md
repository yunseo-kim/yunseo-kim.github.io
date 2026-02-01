---
title: "Kaggle: podsumowanie kursu „Intro to Machine Learning”"
description: "Zestawienie kluczowych pojęć z uczenia maszynowego oraz podstaw użycia bibliotek pandas i scikit-learn. To skrót treści publicznego kursu Kaggle „Intro to Machine Learning”."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

Postanowiłem(-am) przerobić [publiczne kursy Kaggle](https://www.kaggle.com/learn).
Po ukończeniu każdego kursu planuję krótko podsumować to, czego się nauczyłem(-am). Pierwszy wpis jest streszczeniem kursu [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning).

![Certificate of Completion](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lesson 1. How Models Work
Na początek wchodzimy łagodnie, bez presji. To wprowadzenie do tego, jak działają modele uczenia maszynowego i jak się je wykorzystuje. Kurs omawia to na przykładzie sytuacji, w której trzeba przewidywać ceny nieruchomości, używając prostego modelu drzewa decyzyjnego (Decision Tree).

Wyszukiwanie wzorców w danych nazywa się **dopasowaniem (fitting)** albo **trenowaniem (training)** modelu. Dane używane do treningu to **dane treningowe (training data)**. Po zakończeniu treningu można zastosować model do nowych danych i wykonać **predykcję (predict)**.

## Lesson 2. Basic Data Exploration
W każdym projekcie ML pierwszą rzeczą, którą trzeba zrobić, jest oswojenie się z danymi. Dopiero gdy rozumiemy ich cechy, możemy zaprojektować odpowiedni model. Do eksploracji i manipulacji danymi zwykle używa się biblioteki [pandas](https://pandas.pydata.org/).

```python
import pandas as pd
```

Sednem pandas jest DataFrame — można go traktować jak tabelę. Jest podobny do arkusza Excela albo tabeli w bazie SQL. Metodą `read_csv` wczytujemy dane w formacie CSV.

```python
# Dobrze jest przechowywać ścieżkę pliku w zmiennej, aby łatwo się do niej odwoływać.
file_path = "(ścieżka pliku)"
# Wczytujemy dane i zapisujemy je jako DataFrame o nazwie 'example_data'
# (w praktyce warto używać bardziej opisowej nazwy).
example_data = pd.read_csv(file_path)
```

Metoda `describe` pozwala podejrzeć podsumowanie danych.

```python
example_data.describe()
```

Wtedy można sprawdzić 8 informacji:
- **count**: liczba wierszy z rzeczywistą wartością (z pominięciem braków danych)
- **mean**: średnia
- **std**: odchylenie standardowe
- **min**: minimum
- **25%**: wartość dla dolnych 25%
- **50%**: mediana
- **75%**: wartość dla dolnych 75%
- **max**: maksimum

## Lesson 3. Your First Machine Learning Model
### Przetwarzanie danych
Trzeba zdecydować, które zmienne z danych wykorzystać do modelowania. Etykiety kolumn można sprawdzić przez atrybut `columns` DataFrame.

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

Sposobów wybierania potrzebnych fragmentów danych jest kilka; bardziej szczegółowo omawia to kurs Kaggle [Pandas Micro-Course](https://www.kaggle.com/learn/pandas) (podsumowałem(-am) go w [osobnym wpisie](/posts/summary-of-kaggle-pandas-course/)). Tutaj używane są dwie metody:
1. notacja kropkowa (dot notation)
2. użycie listy

Najpierw, używając **notacji kropkowej (dot-notation)**, wybieramy kolumnę będącą **celem predykcji (prediction target)** i zapisujemy ją jako **Series**. Series można traktować jak DataFrame składający się z jednej kolumny. Zwyczajowo cel predykcji oznacza się jako **y**.

```python
y = melbourne_data.Price
```

Kolumny podawane na wejście modelu nazywa się „cechami” (*features*). W przykładzie z cenami domów w Melbourne są to kolumny, których użyjemy do przewidywania ceny. Czasem wykorzystuje się wszystkie kolumny poza celem, a czasem lepiej wybrać tylko część.  
Jak poniżej, można użyć listy do wskazania wielu cech naraz; wszystkie elementy listy muszą być stringami.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

Taki zbiór cech standardowo oznacza się jako **X**.

```python
X = melbourne_data[melbourne_features]
```

Poza `describe` przydatna jest także metoda `head`, która pokazuje pierwsze 5 wierszy danych.

```python
X.head()
```

### Projektowanie modelu
Na etapie modelowania w zależności od sytuacji korzysta się z różnych bibliotek; jedną z najczęściej używanych jest [scikit-learn](https://scikit-learn.org/stable/). Proces tworzenia i używania modelu można ująć w czterech krokach:
- **Definicja modelu (Define)**: wybór typu modelu i parametrów (parameters)
- **Trenowanie (Fit)**: znajdowanie regularności w danych — kluczowy etap
- **Predykcja (Predict)**: wykonywanie prognoz na podstawie wytrenowanego modelu
- **Ewaluacja (Evaluate)**: ocena, jak trafne są prognozy

Poniżej przykład definicji i treningu modelu w scikit-learn:

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

Wiele modeli ML ma w trakcie treningu pewien element losowości. Ustawiając `random_state`, można uzyskać ten sam wynik przy każdym uruchomieniu; jeśli nie ma szczególnego powodu, warto to robić. Konkretna wartość nie ma znaczenia.

Po zakończeniu treningu można wykonać predykcję:

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
### Metody walidacji modelu
Aby iteracyjnie ulepszać model, trzeba mierzyć jego jakość. Przy predykcjach zdarzają się trafienia i pomyłki, więc potrzebujemy metryki oceny. Istnieje wiele metryk; tutaj używana jest **MAE (Mean Absolute Error, średni błąd bezwzględny)**.

W zadaniu przewidywania cen domów w Melbourne błąd predykcji dla pojedynczego domu to:

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

MAE liczymy jako średnią z wartości bezwzględnych błędów:

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

W scikit-learn można to policzyć tak:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Problem używania danych treningowych do walidacji
W powyższym kodzie ten sam zbiór danych posłużył zarówno do treningu, jak i walidacji. W praktyce nie powinno się tak robić. Kurs Kaggle wyjaśnia to na następującym przykładzie:

> W prawdziwym rynku nieruchomości kolor drzwi nie ma związku z ceną domu.  
> 
> Jednak przypadkiem w danych treningowych wszystkie domy z zielonymi drzwiami były bardzo drogie. Ponieważ rolą modelu jest wykrywanie regularności, które mogą pomóc w przewidywaniu ceny, nasz model „zauważy” tę zależność i będzie przewidywał, że domy z zielonymi drzwiami są drogie.  
>
> Przy takich predykcjach model będzie wyglądał na bardzo dokładny na danych treningowych.  
>
> Ale gdy spróbujemy przewidywać na nowych danych, gdzie reguła „zielone drzwi = drogo” nie działa, model okaże się bardzo niedokładny.

Model ma sens tylko wtedy, gdy potrafi przewidywać dla nowych danych, więc walidację należy wykonywać na danych, które nie były użyte do treningu. Najprostsze podejście to wydzielenie części danych na potrzeby pomiaru jakości. Te dane nazywa się **danymi walidacyjnymi (validation data)**.

### Podział na zbiór treningowy i walidacyjny
W scikit-learn jest funkcja `train_test_split`, która dzieli dane na dwie części. Poniższy kod rozdziela dane na zbiór treningowy i walidacyjny, a następnie oblicza MAE (`mean_absolute_error`) na walidacji.

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
### Przeuczenie i niedouczenie
- **przeuczenie (overfitting)**: model bardzo dobrze dopasowuje się do zbioru treningowego, ale słabo przewiduje na zbiorze walidacyjnym lub innych nowych danych
- **niedouczenie (underfitting)**: model nie znajduje wystarczająco ważnych cech i regularności, więc ma słabą jakość nawet na zbiorze treningowym

Wyobraźmy sobie sytuację, w której uczymy model rozróżniania punktów czerwonych i niebieskich jak na obrazku. Zielona linia odpowiada modelowi przeuczonemu, a czarna linia pokazuje model pożądany.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Źródło obrazu*
> - autor: użytkownik hiszpańskiej Wikipedii [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - licencja: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Najważniejsza jest dla nas trafność predykcji na nowych danych, a zbiór walidacyjny służy do oszacowania tej jakości. Celem jest znalezienie optimum (sweet spot) pomiędzy niedouczeniem a przeuczeniem.  
![](https://i.imgur.com/2q85n9s.png)  
W tym kursie Kaggle przykład cały czas opiera się na drzewach decyzyjnych, ale przeuczenie i niedouczenie to pojęcia dotyczące wszystkich modeli ML.

### Strojenie hiperparametrów (hyperparameter)
Poniższy przykład porównuje jakość modelu drzewa decyzyjnego, zmieniając wartość argumentu *max_leaf_nodes* (fragment wczytywania danych i wydzielania walidacji pominięto).

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

Po zakończeniu strojenia hiperparametrów na koniec trenuje się model na całych dostępnych danych, aby zmaksymalizować jego jakość — nie trzeba już odkładać osobnego zbioru walidacyjnego.

## Lesson 6. Random Forests
Łącząc wiele różnych modeli, często da się uzyskać lepszą jakość niż dla pojedynczego modelu. Nazywa się to **ensemble**, a dobrym przykładem jest **random forest**.

Random forest składa się z wielu drzew decyzyjnych; finalna predykcja jest średnią z predykcji poszczególnych drzew. W wielu przypadkach daje to lepszą trafność niż pojedyncze drzewo decyzyjne.
