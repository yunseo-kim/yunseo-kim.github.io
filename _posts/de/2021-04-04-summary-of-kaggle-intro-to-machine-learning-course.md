---
title: "Zusammenfassung des Kaggle-Kurses 'Intro to Machine Learning'"
description: "Kernkonzepte des Machine Learning und Grundlagen zu pandas und scikit-learn kompakt erklärt. Zusammenfassung des Kaggle-Kurses Intro to Machine Learning."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

Ich habe beschlossen, die [Kaggle-Lernkurse](https://www.kaggle.com/learn) durchzuarbeiten.
Nach jedem abgeschlossenen Kurs werde ich die wichtigsten Inhalte kurz zusammenfassen. Der erste Beitrag ist eine Zusammenfassung des Kurses [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning).

![Abschlusszertifikat](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lesson 1. How Models Work
Zum Einstieg beginnen wir ganz entspannt. Es geht darum, wie Machine-Learning-Modelle funktionieren und wofür sie verwendet werden. Anhand der Aufgabe, Immobilienpreise vorherzusagen, wird ein einfaches Entscheidungsbaum-Klassifikationsmodell (Decision Tree) als Beispiel erläutert.

Das Auffinden von Mustern in Daten nennt man ein Modell **anpassen (fitting)** oder **trainieren (training)**. Die Daten, mit denen das Modell trainiert wird, heißen **Trainingsdaten (training data)**. Nach dem Training kann man das Modell auf neue Daten anwenden und **vorhersagen (predict)**.

## Lesson 2. Basic Data Exploration
In jedem Machine-Learning-Projekt steht am Anfang, dass man sich selbst mit den Daten vertraut macht. Nur wenn man die Eigenschaften der Daten versteht, kann man ein geeignetes Modell entwerfen. Zum Erkunden und Transformieren von Daten verwendet man in der Regel die Bibliothek [Pandas](https://pandas.pydata.org/).

```python
import pandas as pd
```

Der Kern von pandas ist das DataFrame, das man sich wie eine Tabelle vorstellen kann – ähnlich einem Excel-Arbeitsblatt oder einer SQL-Tabelle. Mit der Methode read_csv lässt sich CSV-formatierte Daten einlesen.

```python
# Es ist sinnvoll, den Dateipfad in einer Variablen zu speichern, um bei Bedarf leicht darauf zuzugreifen.
file_path = "(파일 경로)"
# Daten einlesen und als DataFrame unter dem Namen 'example_data' speichern
# (in der Praxis natürlich einen aussagekräftigeren Namen wählen).
example_data = pd.read_csv(file_path)
```

Mit der Methode describe kann man zusammenfassende Statistiken der Daten abrufen.

```python
example_data.describe()
```

Dabei erhält man 8 Kennzahlen:
- **count**: Anzahl der Zeilen mit tatsächlichen Werten (fehlende Werte ausgeschlossen)
- **mean**: Durchschnitt
- **std**: Standardabweichung
- **min**: Minimum
- **25%**: 25%-Perzentil
- **50%**: Median (50%-Perzentil)
- **75%**: 75%-Perzentil
- **max**: Maximum

## Lesson 3. Your First Machine Learning Model
### Datenaufbereitung
Man muss entscheiden, welche Variablen aus den gegebenen Daten für das Modell genutzt werden sollen. Über das Attribut **columns** eines DataFrames lassen sich die Spaltenlabels anzeigen.

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

Es gibt verschiedene Wege, die benötigten Teile aus den Daten auszuwählen; ausführlicher behandelt das der [Pandas Micro-Course](https://www.kaggle.com/learn/pandas) von Kaggle (das habe ich in [einem separaten Beitrag](/posts/summary-of-kaggle-pandas-course/) zusammengefasst). Hier verwenden wir zwei Methoden:
1. Dot-Notation
2. Verwendung einer Liste

Zuerst wählen wir mit der **Dot-Notation** die **Zielgröße (prediction target)** als **Series** aus. Eine Series kann man sich als DataFrame mit nur einer Spalte vorstellen. Üblicherweise bezeichnen wir die Zielgröße mit **y**.

```python
y = melbourne_data.Price
```

Die für die Vorhersage verwendeten Spalten nennt man „Merkmale“ bzw. „Features“. Beim Melbourne-Datensatz sind das die Spalten, die zur Preisvorhersage genutzt werden. Manchmal verwendet man alle Spalten außer der Zielgröße, oft ist es aber besser, nur eine Teilmenge zu wählen.  
Mit einer Liste lassen sich mehrere Features auswählen. Alle Listenelemente müssen Strings sein.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

Diese Daten bezeichnen wir konventionell mit **X**.

```python
X = melbourne_data[melbourne_features]
```

Neben describe ist auch die Methode head nützlich; sie zeigt die ersten 5 Zeilen.

```python
X.head()
```

### Modellentwurf
Für das Modellieren nutzt man je nach Fall verschiedene Bibliotheken; eine häufig verwendete ist [scikit-learn](https://scikit-learn.org/stable/). Der Ablauf besteht grob aus:
- **Modell definieren (Define)**: Modelltyp und Hyperparameter festlegen.
- **Trainieren (Fit)**: Aus den Daten Regelmäßigkeiten lernen – der Kern des Modellierens.
- **Vorhersagen (Predict)**: Mit dem trainierten Modell Prognosen erstellen.
- **Bewerten (Evaluate)**: Prüfen, wie genau die Vorhersagen sind.

Unten ein Beispiel, wie man mit scikit-learn ein Modell definiert und trainiert:

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

Viele Machine-Learning-Modelle enthalten im Training einen gewissen Zufallsanteil. Durch Setzen von `random_state` erhält man bei jedem Lauf dieselben Ergebnisse; wenn kein besonderer Grund dagegen spricht, ist das eine gute Praxis. Welcher Wert gewählt wird, ist egal.

Nach dem Training kann man Vorhersagen wie folgt durchführen:

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
### Modellvalidierung
Um ein Modell iterativ zu verbessern, muss seine Leistung gemessen werden. Bei Vorhersagen eines Modells wird manches richtig und manches falsch sein. Dafür braucht man einen Leistungsindikator. Es gibt viele Metriken; hier verwenden wir die **MAE (Mean Absolute Error, mittlerer absoluter Fehler)**.

Beim Beispiel der Preisvorhersage für Melbourne ist der Fehler für jedes Haus:

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

Die MAE berechnet man, indem man den Betrag jedes Vorhersagefehlers nimmt und den Durchschnitt dieser absoluten Fehler bildet:

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

Mit scikit-learn geht das so:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Warum man Trainingsdaten nicht zur Validierung verwenden sollte
Im obigen Code wurden Training und Validierung auf einem einzigen Datensatz durchgeführt. Das sollte man jedoch vermeiden. Der Kaggle-Kurs erklärt den Grund mit folgendem Beispiel:

> In der realen Immobilienwelt hat die Farbe der Haustür nichts mit dem Preis zu tun.  
> 
> Doch zufällig waren in den Trainingsdaten alle Häuser mit grüner Tür sehr teuer. Da ein Modell Regelmäßigkeiten in den Daten finden soll, „lernt“ unser Modell in diesem Fall, dass Häuser mit grüner Tür teuer sind.
>
> Auf den Trainingsdaten wirkt das überzeugend genau.
>
> Aber auf neuen Daten, in denen die Regel „Grüne Tür = teuer“ nicht gilt, wäre das Modell sehr ungenau.

Da ein Modell auf neuen Daten sinnvoll vorhersagen soll, müssen wir zur Bewertung Daten verwenden, die nicht zum Training genutzt wurden. Am einfachsten hält man während des Modellierens einen Teil der Daten für die Leistungsbewertung zurück – diese nennt man **Validierungsdaten (validation data)**.

### Validierungsdatensatz abtrennen
In scikit-learn gibt es die Funktion `train_test_split`, um Daten zu teilen. Der folgende Code trennt die Daten in Trainings- und Validierungssätze; letzterer wird zur Messung der MAE (`mean_absolute_error`) verwendet.

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
### Unteranpassung und Überanpassung
- **Überanpassung (overfitting)**: Das Modell passt extrem gut auf die Trainingsdaten, scheitert aber bei Validierungs- oder völlig neuen Daten.
- **Unteranpassung (underfitting)**: Das Modell extrahiert nicht genügend wichtige Eigenschaften und Regelmäßigkeiten; selbst auf den Trainingsdaten ist die Leistung unzureichend.

Betrachten wir eine Situation, in der ein Modell rote und blaue Punkte wie im folgenden Bild trennen soll. Die grüne Linie wäre überangepasst, die schwarze Linie beschreibt ein wünschenswertes Modell.
![Überanpassung](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Bildquelle*
> - Autor: Spanischer Wikipedia-Nutzer [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Wichtig ist uns die Genauigkeit auf neuen Daten; diese schätzen wir mit einem Validierungsdatensatz. Ziel ist es, den optimalen Punkt zwischen Unter- und Überanpassung (sweet spot) zu finden.  
![](https://i.imgur.com/2q85n9s.png)  
Der Kaggle-Kurs verwendet weiterhin Entscheidungsbäume als Beispiel, aber die Konzepte Unter- und Überanpassung gelten für alle ML-Modelle.

### Hyperparameter-Tuning
Im folgenden Beispiel wird der Wert des Arguments *max_leaf_nodes* eines Entscheidungsbaum-Modells variiert und die Leistung verglichen (Einlesen der Daten und Abtrennen des Validierungsdatensatzes sind ausgelassen):

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

Nach dem Hyperparameter-Tuning trainiert man das finale Modell auf allen verfügbaren Daten, um die Leistung zu maximieren. Ein separater Validierungsabzug ist dann nicht mehr nötig.

## Lesson 6. Random Forests
Mehrere unterschiedliche Modelle gemeinsam zu nutzen, kann bessere Leistung bringen als ein einzelnes Modell. Das nennt man **Ensemble**; ein gutes Beispiel ist der **Random Forest**.

Ein Random Forest besteht aus vielen Entscheidungsbäumen; die endgültige Vorhersage ist das Mittel der Vorhersagen der einzelnen Bäume. In vielen Fällen ist die Genauigkeit höher als bei einem einzelnen Entscheidungsbaum.
