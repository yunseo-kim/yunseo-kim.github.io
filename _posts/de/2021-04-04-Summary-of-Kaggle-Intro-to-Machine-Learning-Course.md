---
title: Zusammenfassung des Kaggle-Kurses 'Einführung in maschinelles Lernen'
description: Ich habe den Inhalt des öffentlichen Kaggle-Kurses 'Intro to Machine
  Learning' zusammengefasst.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
---
Ich habe beschlossen, die [öffentlichen Kurse von Kaggle](https://www.kaggle.com/learn/overview) zu studieren.
Ich plane, den Inhalt jedes Kurses kurz zusammenzufassen, sobald ich ihn abgeschlossen habe. Der erste Artikel ist eine Zusammenfassung des Kurses **Intro to Machine Learning**.

# Einführung in maschinelles Lernen
Lernen Sie die Kernideen des maschinellen Lernens kennen und erstellen Sie Ihre ersten Modelle.

## Lektion 1. Wie Modelle funktionieren
Zu Beginn wird es leicht und unbeschwert gehalten. Es geht darum, wie maschinelle Lernmodelle funktionieren und wie sie verwendet werden. Anhand einer hypothetischen Situation der Immobilienpreisvorhersage wird ein einfaches Entscheidungsbaum-Klassifikationsmodell als Beispiel erklärt.

Das Finden von Mustern in Daten wird als **Trainieren** des Modells bezeichnet (**fitting** oder **training** the model). Die Daten, die zum Trainieren des Modells verwendet werden, werden als **Trainingsdaten (training data)** bezeichnet. Nach dem Training kann dieses Modell auf neue Daten angewendet werden, um **Vorhersagen (predict)** zu treffen.

## Lektion 2. Grundlegende Datenexploration
Das Erste, was bei jedem maschinellen Lernprojekt zu tun ist, ist, dass sich der Entwickler selbst mit den Daten vertraut macht. Man muss zuerst verstehen, welche Eigenschaften die Daten haben, um ein geeignetes Modell entwerfen zu können. Für die Erforschung und Manipulation von Daten wird fast immer die Pandas-Bibliothek verwendet, und hier geht es um die Grundlagen von Pandas.

Der Kern der Pandas-Bibliothek ist der DataFrame, den man sich als eine Art Tabelle vorstellen kann. Er ähnelt einem Excel-Blatt oder einer SQL-Datenbanktabelle. Mit der Methode read_csv können Daten im CSV-Format geladen werden.
```python
# Es ist gut, den Dateipfad als Variable zu speichern, um bei Bedarf leicht darauf zugreifen zu können.
file_path = '(Dateipfad)'
# Liest die Daten ein und speichert sie als DataFrame mit dem Namen 'data_1' (in der Praxis sollte man natürlich einen aussagekräftigeren Namen verwenden).
data_1 = pd.read_csv(file_path)
```
Mit der describe-Methode können zusammenfassende Informationen über die Daten angezeigt werden.
```python
data_1.describe()
```
Dann können 8 Informationspunkte eingesehen werden.
- **count**: Anzahl der Zeilen mit tatsächlichen Werten (ausgenommen fehlende Werte)
- **mean**: Durchschnitt
- **std**: Standardabweichung
- **min**: Minimalwert
- **25%**: Wert des unteren 25. Perzentils
- **50%**: Medianwert
- **75%**: Wert des unteren 75. Perzentils
- **max**: Maximalwert

## Lektion 3. Ihr erstes maschinelles Lernmodell
### Datenverarbeitung
Man muss entscheiden, welche Variablen aus den gegebenen Daten für die Modellierung verwendet werden sollen. Mit dem **columns**-Attribut des DataFrames können die Spaltenbeschriftungen überprüft werden.
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
Es gibt mehrere Möglichkeiten, die benötigten Teile aus den gegebenen Daten auszuwählen. Diese werden im [Pandas Micro-Course](https://www.kaggle.com/learn/pandas) von Kaggle ausführlich behandelt (ich werde diesen Inhalt später auch zusammenfassen). Hier werden zwei Methoden verwendet:
1. Dot-Notation
2. Verwendung von Listen

Zunächst wählen wir mit der **Dot-Notation** die Spalte aus, die dem **Vorhersageziel (prediction target)** entspricht. Diese einzelne Spalte wird in einer **Serie (Series)** gespeichert. Eine Serie kann man sich in etwa als einen DataFrame vorstellen, der nur aus einer Spalte besteht. Konventionell wird das Vorhersageziel als **y** bezeichnet.
```python
y = melbourne_data.Price
```

Die Spalten, die als Eingabe für das Modell zur Vorhersage verwendet werden, nennt man "Merkmale (features)". Im Fall der gegebenen Immobilienpreisdaten von Melbourne wären dies die Spalten, die zur Vorhersage der Hauspreise verwendet werden. Manchmal werden alle Spalten der gegebenen Daten außer dem Vorhersageziel als Merkmale verwendet, in anderen Fällen ist es besser, nur einige davon auszuwählen.  
Wie unten gezeigt, können mehrere Merkmale mit einer Liste ausgewählt werden. Alle Elemente dieser Liste müssen Zeichenketten sein.
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
Konventionell werden diese Daten als **X** bezeichnet.
```python
X = melbourne_data[melbourne_features]
```

Neben describe gibt es noch eine weitere nützliche Methode zur Datenanalyse: head. Sie zeigt die ersten 5 Zeilen an.
```python
X.head()
```

### Modelldesign
In der Modellierungsphase wird häufig die **scikit-learn**-Bibliothek verwendet. Der Prozess des Entwerfens und Verwendens eines Modells umfasst im Allgemeinen die folgenden Schritte:
- **Definition (Define)**: Bestimmen Sie den Typ des Modells und seine Parameter.
- **Training (Fit)**: Finden Sie Regelmäßigkeiten in den gegebenen Daten. Dies ist der Kern der Modellierung.
- **Vorhersage (Predict)**: Führen Sie Vorhersagen mit dem trainierten Modell durch.
- **Validierung (Evaluate)**: Bewerten Sie, wie genau die Vorhersagen des Modells sind.

Hier ist ein Beispiel für die Definition und das Training eines Modells mit scikit-learn:
```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

Viele maschinelle Lernmodelle weisen während des Trainingsprozesses ein gewisses Maß an Zufälligkeit auf. Durch Festlegen des ```random_state```-Wertes kann sichergestellt werden, dass bei jeder Ausführung die gleichen Ergebnisse erzielt werden. Es ist eine gute Angewohnheit, diesen Wert festzulegen, wenn es keinen besonderen Grund dagegen gibt. Welcher Wert verwendet wird, spielt keine Rolle.

Nach Abschluss des Modelltrainings können Vorhersagen wie folgt durchgeführt werden:
```python
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
```

## Lektion 4. Modellvalidierung
### Methoden zur Modellvalidierung
Um ein Modell kontinuierlich zu verbessern, muss seine Leistung gemessen werden. Bei der Verwendung eines Modells für Vorhersagen wird es Fälle geben, in denen es richtig liegt, und Fälle, in denen es falsch liegt. Hier brauchen wir einen Indikator, um die Vorhersageleistung dieses Modells zu überprüfen. Es gibt verschiedene Arten von Indikatoren, aber hier verwenden wir den **MAE (Mean Absolute Error, mittlerer absoluter Fehler)**.

Im Fall der Immobilienpreisvorhersage in Melbourne berechnet sich der Vorhersagefehler für jeden Hauspreis wie folgt:  
```
error = tatsächlich - vorhergesagt
```
Der MAE wird berechnet, indem der Absolutwert jedes Vorhersagefehlers genommen und dann der Durchschnitt dieser absoluten Fehler gebildet wird. Mit scikit-learn kann dies wie folgt implementiert werden:
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Probleme bei der Verwendung von Trainingsdaten zur Validierung
Im obigen Code wurden sowohl das Modelltraining als auch die Validierung mit einem einzigen Datensatz durchgeführt. Das sollte man jedoch nicht tun. In diesem Kurs wird anhand eines Beispiels erklärt, warum.

> In der realen Immobilienbranche hat die Farbe der Tür keinen Einfluss auf den Hauspreis.  
> 
> Aber zufälligerweise sind in den für das Training verwendeten Daten alle Häuser mit grünen Türen sehr teuer. Da es die Aufgabe des Modells ist, Regelmäßigkeiten in den Daten zu finden, die für die Vorhersage der Hauspreise nützlich sein könnten, wird unser Modell in diesem Fall diese Regelmäßigkeit erkennen und vorhersagen, dass Häuser mit grünen Türen teuer sind. 
>
> Wenn Vorhersagen auf diese Weise durchgeführt werden, scheinen sie für die gegebenen Trainingsdaten genau zu sein.
>
> Wenn jedoch Vorhersagen für neue Daten gemacht werden, bei denen die Regel "Häuser mit grünen Türen sind teuer" nicht zutrifft, wird dieses Modell sehr ungenau sein.

Da ein Modell nur dann sinnvoll ist, wenn es Vorhersagen für neue Daten treffen kann, müssen wir die Validierung mit Daten durchführen, die nicht für das Modelltraining verwendet wurden. Die einfachste Methode besteht darin, während des Modellierungsprozesses einen Teil der Daten zu separieren und für die Leistungsmessung zu verwenden. Diese Daten werden als **Validierungsdaten (validation data)** bezeichnet.

### Trennung des Validierungsdatensatzes
Die scikit-learn-Bibliothek enthält eine Funktion ```train_test_split```, die Daten in zwei Teile aufteilt. Der folgende Code teilt die Daten in zwei Teile auf, wobei einer für das Training und der andere für die Validierung mit ```mean_absolute_error``` verwendet wird.
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

## Lektion 5. Underfitting und Overfitting
### Overfitting und Underfitting
- **Overfitting (Überanpassung)**: Ein Phänomen, bei dem das Modell sehr genau auf den Trainingsdatensatz passt, aber für den Validierungsdatensatz oder andere neue Daten keine guten Vorhersagen machen kann.
- **Underfitting (Unteranpassung)**: Ein Phänomen, bei dem das Modell wichtige Merkmale und Regelmäßigkeiten in den gegebenen Daten nicht erkennt und daher selbst für den Trainingsdatensatz keine guten Vorhersagen machen kann.

In der folgenden Abbildung stellt die grüne Linie ein überangepasstes Modell dar, während die schwarze Linie ein wünschenswertes Modell darstellt.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Bildquelle*
> - Autor: Wikipedia-Benutzer [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke) aus Spanien
> - Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Wichtig für uns ist die Vorhersagegenauigkeit für neue Daten, und wir verwenden den Validierungsdatensatz, um die Vorhersageleistung für neue Daten abzuschätzen. Unser Ziel ist es, den optimalen Punkt (sweet spot) zwischen Underfitting und Overfitting zu finden.  
![](https://i.imgur.com/2q85n9s.png)  
In diesem Kurs wird weiterhin das Entscheidungsbaum-Klassifikationsmodell als Beispiel verwendet, aber die Konzepte von Overfitting und Underfitting gelten für alle maschinellen Lernmodelle.

### Hyperparameter-Tuning
Das folgende Beispiel zeigt Code, der die Leistung des Modells vergleicht und misst, indem der Wert des *max_leaf_nodes*-Arguments des Entscheidungsbaummodells variiert wird. (Der Teil, der die Daten lädt und den Validierungsdatensatz abtrennt, wurde weggelassen.)
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
for max_leaf_nodes in [5,
