---
title: "Zusammenfassung des Kaggle-Pandas-Kurses"
description: >-
  Ich habe den Inhalt des Pandas-Minikurses aus den öffentlichen Kaggle-Kursen zusammengefasst.
categories: [Data Science, Machine Learning]
tags: [Kaggle Courses, Pandas]
toc: true
toc_sticky: true
---

# Pandas
Lösen Sie kurze praktische Aufgaben, um Ihre Datenmanipulationsfähigkeiten zu perfektionieren.

## Lektion 1. Erstellen, Lesen und Schreiben
### Pandas importieren
```python
import pandas as pd
```
Pandas hat zwei zentrale Objekte: **DataFrame** und **Series**.

### DataFrame
Ein DataFrame ist eine Tabelle. Es enthält eine Matrix aus einzelnen *Einträgen*, wobei jeder Eintrag einen bestimmten *Wert* hat und einer *Zeile* (*row* oder *record*) und einer Spalte (*column*) entspricht. Die Einträge in einem DataFrame müssen nicht unbedingt Ganzzahlen sein.
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```
Die Deklaration eines DataFrames erfolgt im Python-Dictionary-Format. Die Schlüssel (keys) sind die Spaltennamen, die Werte (values) sind Listen der einzutragenden Elemente.

Normalerweise werden bei der DataFrame-Deklaration den Spaltenbeschriftungen die Namen der Spalten zugewiesen, aber den Zeilenbeschriftungen werden die Ganzzahlen 0, 1, 2... zugewiesen. Bei Bedarf können die Zeilenbeschriftungen manuell festgelegt werden. Die Liste der Zeilenbeschriftungen in einem DataFrame wird als **Index** bezeichnet und kann mit dem Parameter ```index``` festgelegt werden.
```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
```

### Series
Eine Series ist eine Sequenz von Datenwerten.
```python
pd.Series([1, 2, 3, 4, 5])
```
Eine Series ist im Wesentlichen wie eine einzelne Spalte eines DataFrames. Daher kann auch hier ein Index festgelegt werden. Der Unterschied besteht darin, dass sie statt eines 'Spaltennamens' einen 'Namen', ```name```, hat.
```python
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
```
Series und DataFrames sind eng miteinander verwandt. Es ist hilfreich, sich einen DataFrame als eine Sammlung von Series vorzustellen.

### Datendateien einlesen
In vielen Fällen werden vorhandene Daten verwendet, anstatt sie direkt zu erstellen. Daten können in verschiedenen Formaten gespeichert sein, wobei das grundlegendste Format die CSV-Datei ist. Der Inhalt einer CSV-Datei sieht normalerweise wie folgt aus:
```
Product A,Product B,Product C,
30,21,9,
35,34,1,
41,11,11
```
Eine CSV-Datei ist also eine Tabelle, in der die einzelnen Werte durch Kommas (comma) getrennt sind. Daher der Name "Comma-Separated Values", CSV.

Um Daten im CSV-Dateiformat in einen DataFrame zu laden, verwendet man die Funktion ```pd.read_csv()```.

Mit dem Attribut ```shape``` kann man die Größe des DataFrames überprüfen.

Mit dem Befehl ```head()``` können die ersten fünf Zeilen des DataFrames angezeigt werden.

Die Funktion ```pd.read_csv()``` hat über 30 Parameter. Wenn beispielsweise die zu ladende CSV-Datei einen eigenen Index enthält, kann man den Wert des Parameters ```index_col``` festlegen, damit Pandas diese Spalte als Index verwendet, anstatt automatisch einen Index zu erstellen.

### Daten schreiben
Mit der Methode ```to_csv()``` kann ein DataFrame in eine CSV-Datei exportiert werden. Sie wird wie folgt verwendet:
```python
(DataFrame-Name).to_csv("(CSV-Dateipfad)")
```

## Lektion 2. Indexieren, Auswählen & Zuweisen
Die Auswahl bestimmter Werte aus einem Pandas DataFrame oder einer Series ist ein Schritt, der in fast allen Datenverarbeitungsaufgaben vorkommt.