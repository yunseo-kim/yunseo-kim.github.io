---
title: "Synthèse du cours Kaggle « Intro to Machine Learning »"
description: "Synthèse des notions clés du machine learning et des bases de pandas et scikit-learn, d’après le cours gratuit Kaggle « Intro to Machine Learning »."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

J’ai décidé d’étudier les [cours publics de Kaggle](https://www.kaggle.com/learn).
À chaque fois que je terminerai un cours, je publierai un bref récapitulatif de ce que j’y ai appris. Ce premier billet est un résumé du cours [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning).

![Certificat d’achèvement](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Leçon 1. How Models Work
On commence en douceur. Il s’agit de comprendre comment les modèles de machine learning fonctionnent et comment ils s’emploient. En partant d’un scénario d’estimation de prix immobiliers, le cours prend l’exemple d’un simple modèle de classification par arbre de décision.

Apprendre des motifs à partir des données revient à dire qu’on **ajuste (fitting)** ou qu’on **entraîne (training)** le modèle. Les données utilisées pendant l’entraînement sont appelées **données d’entraînement (training data)**. Une fois l’entraînement terminé, on peut appliquer le modèle à de nouvelles données pour **prédire (predict)**.

## Leçon 2. Basic Data Exploration
Dans tout projet de machine learning, la première étape consiste à se familiariser avec les données. Il faut en comprendre les caractéristiques pour concevoir un modèle adapté. Pour explorer et manipuler les données, on utilise généralement la bibliothèque [pandas](https://pandas.pydata.org/).

```python
import pandas as pd
```

L’objet central de pandas est le DataFrame, que l’on peut voir comme un tableau, similaire à une feuille Excel ou à une table SQL. La méthode read_csv permet de charger des données au format CSV.

```python
# Il est pratique d’enregistrer le chemin du fichier dans une variable
# pour y accéder facilement quand on en a besoin.
file_path = "(파일 경로)"
# On lit les données et on les stocke dans un DataFrame nommé 'example_data'
# (dans la pratique, utilisez un nom plus explicite).
example_data = pd.read_csv(file_path)
```

La méthode describe permet d’obtenir un résumé statistique des données.

```python
example_data.describe()
```

On y trouve notamment 8 informations:
- **count**: nombre de lignes contenant une valeur (hors valeurs manquantes)
- **mean**: moyenne
- **std**: écart-type
- **min**: minimum
- **25%**: 1er quartile
- **50%**: médiane
- **75%**: 3e quartile
- **max**: maximum

## Leçon 3. Your First Machine Learning Model
### Préparation des données
Il faut choisir quelles variables du jeu de données serviront au modèle. On peut consulter les étiquettes de colonnes via l’attribut **columns** du DataFrame.

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

Il existe plusieurs façons de sélectionner des sous-ensembles des données; le [Micro-cours Pandas](https://www.kaggle.com/learn/pandas) de Kaggle les explore en détail (j’en ai fait un [billet séparé](/posts/summary-of-kaggle-pandas-course/)). Ici, nous en utilisons deux:
1. Dot notation
2. Utiliser une liste

D’abord, via la **dot notation**, on sélectionne la **cible de prédiction (prediction target)** et on la stocke comme **série (Series)**. Une série est, en quelque sorte, un DataFrame composé d’une seule colonne. Par convention, on note la cible **y**.

```python
y = melbourne_data.Price
```

Les colonnes utilisées comme entrées pour la prédiction s’appellent des "caractéristiques (features)". Dans l’exemple des prix des maisons de Melbourne, ce sont les colonnes employées pour prédire le prix. On peut utiliser toutes les colonnes sauf la cible, ou n’en sélectionner qu’un sous-ensemble.  
On peut choisir plusieurs caractéristiques avec une liste; tous ses éléments doivent être des chaînes.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

Par convention, on note ces données **X**.

```python
X = melbourne_data[melbourne_features]
```

Outre describe, la méthode head est utile pour un aperçu rapide: elle affiche les 5 premières lignes.

```python
X.head()
```

### Conception du modèle
Parmi les bibliothèques fréquemment utilisées pour la modélisation figure [scikit-learn](https://scikit-learn.org/stable/). Le flux général est:
- **Définir (Define)**: choisir le type de modèle et ses paramètres.
- **Entraîner (Fit)**: extraire les régularités à partir des données; c’est le cœur de la modélisation.
- **Prédire (Predict)**: produire des prédictions avec le modèle entraîné.
- **Évaluer (Evaluate)**: mesurer la précision des prédictions.

Exemple de définition et d’entraînement d’un modèle avec scikit-learn:

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
```

Beaucoup de modèles de machine learning comportent une part de hasard pendant l’entraînement. En fixant `random_state`, on garantit des résultats reproductibles à chaque exécution; c’est une bonne habitude en l’absence de raison contraire. La valeur choisie importe peu.

Une fois le modèle entraîné, on peut prédire comme suit:

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

## Leçon 4. Model Validation
### Comment valider un modèle
Pour améliorer un modèle de manière itérative, il faut mesurer ses performances. Sur un ensemble de prédictions, certaines seront correctes et d’autres non; il nous faut donc un indicateur. Parmi de nombreux choix possibles, nous utilisons ici la **MAE (Mean Absolute Error, erreur absolue moyenne)**.

Dans la prédiction des prix à Melbourne, l’erreur pour chaque maison est:

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

La MAE se calcule comme la moyenne des valeurs absolues des erreurs:

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

Avec scikit-learn:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Pourquoi il ne faut pas valider sur les données d’entraînement
Dans le code ci-dessus, on a utilisé un seul jeu de données à la fois pour l’entraînement et la validation. En réalité, il ne faut pas procéder ainsi. Kaggle donne l’exemple suivant pour l’expliquer.

> Dans le marché immobilier réel, la couleur de la porte n’influence pas le prix.  
> 
> Mais il se trouve que, par hasard, toutes les maisons aux portes vertes dans les données d’entraînement étaient très chères. Comme le rôle d’un modèle est de découvrir des régularités exploitables pour la prédiction, notre modèle détectera ce motif et prédira qu’une porte verte implique un prix élevé.
>
> Dans les données d’entraînement, cela peut sembler très précis.
>
> Mais sur de nouvelles données où “les portes vertes sont chères” n’est pas une règle valable, le modèle sera très imprécis.

Puisque le modèle doit bien prédire sur des données inédites, il faut l’évaluer sur des données non utilisées à l’entraînement. La méthode la plus simple consiste à mettre de côté une partie des données pour la mesure de performance: ce sont les **données de validation (validation data)**.

### Séparer un jeu de validation
La fonction `train_test_split` de scikit-learn sépare les données en deux. Le code suivant utilise une partie pour l’entraînement et l’autre pour mesurer la MAE (`mean_absolute_error`).

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

## Leçon 5. Underfitting and Overfitting
### Surapprentissage et sous-apprentissage
- **Surapprentissage (overfitting)**: le modèle colle trop aux données d’entraînement et généralise mal aux données de validation ou à d’autres données nouvelles.
- **Sous-apprentissage (underfitting)**: le modèle n’extrait pas suffisamment les caractéristiques et régularités importantes; il performe déjà mal sur l’entraînement.

Considérons un problème de classification séparant les points rouges des bleus comme ci-dessous. La courbe verte illustre un modèle en surapprentissage, tandis que la courbe noire représente un modèle préférable.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Crédits de l’image*
> - Auteur: utilisateur de Wikipédia en espagnol [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Ce qui nous importe, c’est la précision sur des données nouvelles; on l’estime via le jeu de validation. L’objectif est de trouver le point optimal (sweet spot) entre sous- et surapprentissage.  
![](https://i.imgur.com/2q85n9s.png)  
Le cours Kaggle illustre cela avec des arbres de décision, mais ces notions valent pour tous les modèles de machine learning.

### Réglage des hyperparamètres (hyperparameter tuning)
L’exemple ci-dessous compare la performance d’un arbre de décision en faisant varier le paramètre *max_leaf_nodes* (chargement des données et séparation validation non inclus).

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

Après le réglage des hyperparamètres, on réentraîne généralement un modèle final sur l’ensemble complet des données pour maximiser la performance; il n’est alors plus nécessaire de réserver un jeu de validation.

## Leçon 6. Random Forests
Combiner plusieurs modèles différents peut surpasser un modèle unique. On parle d’**ensemble (Ensemble)**, et la **forêt aléatoire (random forest)** en est un bon exemple.

Une forêt aléatoire est composée d’un grand nombre d’arbres de décision. La prédiction finale est la moyenne des prédictions de chaque arbre. Dans bien des cas, elle surpasse un arbre de décision unique en précision.
