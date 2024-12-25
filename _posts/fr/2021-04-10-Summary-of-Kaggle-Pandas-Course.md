---
title: Résumé du cours Kaggle-Pandas
description: J'ai résumé le contenu du mini-cours Pandas parmi les cours publics de Kaggle.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.jpg
---
# Pandas
Résolvez de courts défis pratiques pour perfectionner vos compétences en manipulation de données.

## Leçon 1. Création, lecture et écriture
### Importation de pandas
```python
import pandas as pd
```
Pandas possède deux objets fondamentaux : le **DataFrame** et la **Series**.

### DataFrame
Un DataFrame est un tableau. Il contient une matrice d'*entrées* individuelles, chacune ayant une *valeur* spécifique et correspondant à une *ligne* (*row* ou *record*) et une colonne (*column*). Les entrées d'un DataFrame ne sont pas nécessairement des entiers.
```python
pd.DataFrame({'Bob': ['Je l\'ai aimé.', 'C\'était horrible.'], 'Sue': ['Plutôt bon.', 'Fade.']})
```
La déclaration d'un DataFrame se fait au format dictionnaire (dictionary) de Python. Les clés (keys) sont les noms des colonnes, et les valeurs (values) sont des listes contenant les éléments à inscrire.

Généralement, lors de la déclaration d'un DataFrame, les étiquettes de colonnes reçoivent le nom de la colonne, mais les étiquettes de lignes reçoivent des entiers 0, 1, 2... Si nécessaire, on peut spécifier manuellement les étiquettes de lignes. La liste des étiquettes de lignes dans un DataFrame est appelée **Index**, et peut être définie en utilisant le paramètre ```index```.
```python
pd.DataFrame({'Bob': ['Je l\'ai aimé.', 'C\'était horrible.'], 
              'Sue': ['Plutôt bon.', 'Fade.']},
             index=['Produit A', 'Produit B'])
```

### Series
Une Series est une séquence de valeurs de données.
```python
pd.Series([1, 2, 3, 4, 5])
```
Une Series est essentiellement équivalente à une seule colonne d'un DataFrame. Par conséquent, on peut également spécifier un index. La différence est qu'au lieu d'un 'nom de colonne', elle a un 'nom', ```name```.
```python
pd.Series([30, 35, 40], index=['Ventes 2015', 'Ventes 2016', 'Ventes 2017'], name='Produit A')
```
Les Series et les DataFrames sont étroitement liés. Il peut être utile de penser à un DataFrame comme à un ensemble de Series.

### Lecture de fichiers de données
Dans de nombreux cas, plutôt que de créer des données directement, on utilise des données existantes. Les données peuvent être stockées dans divers formats, mais le plus basique est le fichier CSV. Le contenu d'un fichier CSV ressemble généralement à ceci :
```
Produit A,Produit B,Produit C,
30,21,9,
35,34,1,
41,11,11
```
Un fichier CSV est donc un tableau où chaque valeur est séparée par une virgule (comma). C'est pourquoi il s'appelle "Comma-Separated Values", CSV.

Pour charger des données au format CSV dans un DataFrame, on utilise la fonction ```pd.read_csv()```.

On peut vérifier la taille d'un DataFrame en utilisant l'attribut ```shape```.

On peut voir les cinq premières lignes d'un DataFrame en utilisant la commande ```head()```.

La fonction ```pd.read_csv()``` a plus de 30 paramètres. Par exemple, si le fichier CSV à charger contient son propre index, on peut spécifier la valeur du paramètre ```index_col``` pour utiliser cette colonne comme index au lieu de laisser pandas générer automatiquement un index.

### Écriture de données
On peut exporter un DataFrame vers un fichier CSV en utilisant la méthode ```to_csv()```. Elle s'utilise comme suit :
```python
(nom du DataFrame).to_csv("(chemin du fichier CSV)")
```

## Leçon 2. Indexation, sélection et affectation
La sélection de valeurs spécifiques à utiliser dans un DataFrame ou une Series pandas est une étape présente dans presque toutes les opérations utilisant des données.
