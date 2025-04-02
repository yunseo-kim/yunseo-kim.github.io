---
title: Résumé du cours Pandas de Kaggle
description: Un résumé du mini-cours Pandas des cours publics de Kaggle.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.jpg
---
# Pandas
Résolvez de courts défis pratiques pour perfectionner vos compétences en manipulation de données.

## Leçon 1. Création, Lecture et Écriture
### Importation de pandas
```python
import pandas as pd
```
Pandas possède deux objets fondamentaux : le **DataFrame** et la **Series**.

### DataFrame
Un DataFrame est un tableau. Il contient une matrice d'*entrées* individuelles, chacune ayant une *valeur* spécifique et correspondant à une *ligne* (*row* ou *record*) et une colonne. Les entrées d'un DataFrame ne sont pas nécessairement des entiers.
```python
pd.DataFrame({'Bob': ['Je l\'ai aimé.', 'C\'était horrible.'], 'Sue': ['Plutôt bon.', 'Fade.']})
```
La déclaration d'un DataFrame se fait sous forme de dictionnaire Python. Les clés sont les noms des colonnes, et les valeurs sont des listes contenant les entrées.

Généralement, lors de la déclaration d'un DataFrame, des étiquettes de colonnes sont attribuées, mais les étiquettes de lignes sont des entiers (0, 1, 2...). Si nécessaire, on peut spécifier manuellement les étiquettes de lignes. La liste des étiquettes de lignes dans un DataFrame est appelée **Index**, et peut être définie avec le paramètre ```index```.
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
Une Series est essentiellement équivalente à une seule colonne d'un DataFrame. On peut donc également spécifier un index. La différence est qu'au lieu d'un 'nom de colonne', elle a un ```name```.
```python
pd.Series([30, 35, 40], index=['Ventes 12015', 'Ventes 12016', 'Ventes 12017'], name='Produit A')
```
Les Series et les DataFrames sont étroitement liés. Il peut être utile de penser à un DataFrame comme à un ensemble de Series.

### Lecture de fichiers de données
Dans de nombreux cas, on importe des données existantes plutôt que de les créer directement. Les données peuvent être stockées dans divers formats, le plus basique étant le fichier CSV. Le contenu d'un fichier CSV ressemble généralement à ceci :
```
Produit A,Produit B,Produit C,
30,21,9,
35,34,1,
41,11,11
```
Un fichier CSV est donc un tableau où chaque valeur est séparée par une virgule (comma). D'où le nom "Comma-Separated Values", CSV.

Pour charger des données au format CSV dans un DataFrame, on utilise la fonction ```pd.read_csv()```.

L'attribut ```shape``` permet de vérifier la taille d'un DataFrame.

La commande ```head()``` permet d'afficher les cinq premières lignes d'un DataFrame.

La fonction ```pd.read_csv()``` possède plus de 30 paramètres. Par exemple, si le fichier CSV à importer contient son propre index, on peut spécifier la valeur du paramètre ```index_col``` pour utiliser cette colonne comme index au lieu de laisser pandas en générer un automatiquement.

### Écriture de données
La méthode ```to_csv()``` permet d'exporter un DataFrame vers un fichier CSV. On l'utilise comme suit :
```python
(nom du DataFrame).to_csv("(chemin du fichier CSV)")
```

## Leçon 2. Indexation, Sélection et Affectation
La sélection de valeurs spécifiques à utiliser dans un DataFrame ou une Series pandas est une étape présente dans presque toutes les opérations de traitement de données.
