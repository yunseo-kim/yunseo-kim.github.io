---
title: Résumé du cours Kaggle - Introduction au Machine Learning
description: J'ai résumé le contenu du cours public de Kaggle 'Intro to Machine Learning'.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
---
J'ai décidé d'étudier les [cours publics de Kaggle](https://www.kaggle.com/learn/overview).
Je prévois de résumer brièvement le contenu de chaque cours à mesure que je les termine. Le premier article est un résumé du cours **Intro to Machine Learning**.

# Introduction au Machine Learning
Apprenez les idées fondamentales du machine learning et construisez vos premiers modèles.

## Leçon 1. Comment fonctionnent les modèles
On commence doucement et sans pression. Il s'agit de comprendre comment fonctionnent les modèles de machine learning et comment ils sont utilisés. En prenant l'exemple d'une situation où il faut prédire les prix de l'immobilier, on explique un modèle simple de classification par arbre de décision (Decision Tree).

On dit qu'on **entraîne** un modèle (**fitting** ou **training** le modèle) lorsqu'on lui fait trouver des motifs dans les données. Les données utilisées pour entraîner le modèle sont appelées **données d'entraînement (training data)**. Une fois l'entraînement terminé, on peut appliquer ce modèle à de nouvelles données pour faire des **prédictions (predict)**.

## Leçon 2. Exploration de base des données
Dans tout projet de machine learning, la première chose à faire est de se familiariser avec les données. Il faut d'abord comprendre les caractéristiques des données pour pouvoir concevoir un modèle approprié. On utilise presque toujours la bibliothèque pandas pour explorer et manipuler les données, et cette leçon couvre les bases de pandas.

L'élément central de la bibliothèque pandas est le DataFrame, qu'on peut considérer comme une sorte de tableau. C'est similaire à une feuille Excel ou une table de base de données SQL. On peut charger des données au format CSV en utilisant la méthode read_csv.
```python
# Il est bon de stocker le chemin du fichier dans une variable pour y accéder facilement si nécessaire.
file_path = '(chemin du fichier)'
# On lit les données et on les stocke dans un DataFrame nommé 'data_1' (bien sûr, il vaut mieux utiliser un nom plus descriptif en pratique).
data_1 = pd.read_csv(file_path)
```
On peut utiliser la méthode describe pour voir un résumé des informations sur les données.
```python
data_1.describe()
```
Cela affiche 8 éléments d'information :
- **count** : nombre de lignes contenant des valeurs réelles (excluant les valeurs manquantes)
- **mean** : moyenne
- **std** : écart-type
- **min** : valeur minimale
- **25%** : 25e percentile
- **50%** : valeur médiane
- **75%** : 75e percentile
- **max** : valeur maximale

## Leçon 3. Votre premier modèle de Machine Learning
### Préparation des données
Il faut décider quelles variables du jeu de données seront utilisées pour la modélisation. On peut vérifier les étiquettes des colonnes en utilisant l'attribut **columns** du DataFrame.
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
Il existe plusieurs façons de sélectionner les parties nécessaires des données, qui sont traitées en profondeur dans le [Micro-cours Pandas](https://www.kaggle.com/learn/pandas) de Kaggle (que je résumerai également plus tard). Ici, on utilise deux méthodes :
1. Notation par point
2. Utilisation d'une liste

D'abord, on sélectionne la colonne correspondant à la **cible de prédiction (prediction target)** en utilisant la **notation par point**. Cette colonne unique est stockée dans une **Série (Series)**. Une série peut être considérée comme un DataFrame composé d'une seule colonne. Par convention, la cible de prédiction est désignée par **y**.
```python
y = melbourne_data.Price
```

Les colonnes qu'on entre dans le modèle pour faire des prédictions sont appelées "caractéristiques (features)". Dans le cas des données sur les prix des maisons à Melbourne, il s'agit des colonnes utilisées pour prédire les prix des maisons. Parfois, on utilise toutes les colonnes sauf la cible de prédiction comme caractéristiques, et parfois il est préférable de n'en sélectionner que quelques-unes.  
On peut sélectionner plusieurs caractéristiques en utilisant une liste comme suit. Tous les éléments de cette liste doivent être des chaînes de caractères.
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
Par convention, ces données sont désignées par **X**.
```python
X = melbourne_data[melbourne_features]
```

En plus de describe, la méthode head est également utile pour analyser les données. Elle affiche les 5 premières lignes.
```python
X.head()
```

### Conception du modèle
À l'étape de modélisation, on utilise généralement la bibliothèque **scikit-learn**. Le processus de conception et d'utilisation d'un modèle se déroule généralement comme suit :
- **Définir (Define)** : On décide du type de modèle et de ses paramètres.
- **Ajuster (Fit)** : On trouve des régularités dans les données données. C'est le cœur de la modélisation.
- **Prédire (Predict)** : On utilise le modèle entraîné pour faire des prédictions.
- **Évaluer (Evaluate)** : On évalue la précision des prédictions du modèle.

Voici un exemple de définition et d'entraînement d'un modèle avec scikit-learn :
```python
from sklearn.tree import DecisionTreeRegressor

# Définir le modèle. Spécifier un nombre pour random_state pour assurer les mêmes résultats à chaque exécution
melbourne_model = DecisionTreeRegressor(random_state=1)

# Ajuster le modèle
melbourne_model.fit(X, y)
```

De nombreux modèles de machine learning ont une certaine part d'aléatoire dans leur processus d'entraînement. En spécifiant une valeur pour ```random_state```, on s'assure d'obtenir les mêmes résultats à chaque exécution, et c'est une bonne habitude de le faire sauf raison particulière. La valeur utilisée n'a pas d'importance.

Une fois l'entraînement du modèle terminé, on peut faire des prédictions comme suit :
```python
print("Prédictions pour les 5 maisons suivantes :")
print(X.head())
print("Les prédictions sont")
print(melbourne_model.predict(X.head()))
```

## Leçon 4. Validation du modèle
### Méthode de validation du modèle
Pour améliorer continuellement un modèle, il faut mesurer ses performances. Lorsqu'on utilise un modèle pour faire des prédictions, il y aura des cas corrects et des cas incorrects. On a besoin d'un indicateur pour vérifier les performances de prédiction de ce modèle. Il existe différents types d'indicateurs, mais ici on utilise le **MAE (Mean Absolute Error, Erreur absolue moyenne)**.

Dans le cas de la prédiction des prix des maisons à Melbourne, l'erreur de prédiction pour chaque prix de maison est calculée comme suit :  
```
erreur = réel - prédit
```
Le MAE est calculé en prenant la valeur absolue de chaque erreur de prédiction, puis en faisant la moyenne de ces erreurs absolues. On peut l'implémenter avec scikit-learn comme suit :
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Problème de l'utilisation des données d'entraînement pour la validation
Dans le code ci-dessus, on a utilisé le même jeu de données pour l'entraînement du modèle et la validation. Mais ce n'est pas la bonne façon de faire. Ce cours explique pourquoi avec un exemple.

> Dans le marché immobilier réel, la couleur de la porte n'a aucun rapport avec le prix de la maison.  
> 
> Cependant, par hasard, dans les données utilisées pour l'entraînement, toutes les maisons avec des portes vertes sont très chères. Comme le rôle du modèle est de trouver des régularités dans les données qui peuvent être utilisées pour prédire les prix des maisons, dans ce cas, notre modèle détectera cette régularité et prédira que les maisons avec des portes vertes sont chères. 
>
> Si on fait des prédictions de cette manière, elles sembleront précises pour les données d'entraînement données.
>
> Cependant, si on effectue des prédictions sur de nouvelles données où la règle "les maisons avec des portes vertes sont chères" ne s'applique pas, ce modèle sera très imprécis.

Comme le modèle doit faire des prédictions à partir de nouvelles données pour avoir un sens, nous devons effectuer la validation en utilisant des données qui n'ont pas été utilisées pour l'entraînement du modèle. La méthode la plus simple consiste à séparer une partie des données lors du processus de modélisation et à l'utiliser pour mesurer les performances. Ces données sont appelées **données de validation (validation data)**.

### Séparation du jeu de données de validation
La bibliothèque scikit-learn dispose d'une fonction ```train_test_split``` qui divise les données en deux. Voici un code qui divise les données en deux, en utilisant une partie pour l'entraînement et l'autre pour la validation avec la mesure ```mean_absolute_error``` :
```python
from sklearn.model_selection import train_test_split

# diviser les données en données d'entraînement et de validation, pour les caractéristiques et la cible
# La division est basée sur un générateur de nombres aléatoires. Fournir une valeur numérique à
# l'argument random_state garantit que nous obtenons la même division chaque fois que nous
# exécutons ce script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Définir le modèle
melbourne_model = DecisionTreeRegressor()
# Ajuster le modèle
melbourne_model.fit(train_X, train_y)

# obtenir les prix prédits sur les données de validation
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## Leçon 5. Sous-ajustement et surajustement
### Surajustement et sous-ajustement
- **Surajustement (overfitting)** : Phénomène où le modèle correspond très précisément au jeu de données d'entraînement, mais ne parvient pas à faire des prédictions correctes sur le jeu de données de validation ou d'autres nouvelles données.
- **Sous-ajustement (underfitting)** : Phénomène où le modèle ne parvient pas à trouver les caractéristiques et régularités importantes dans les données données, et ne fait donc pas de bonnes prédictions même sur le jeu de données d'entraînement.

Dans l'image ci-dessous, la ligne verte représente un modèle surajusté, tandis que la ligne noire représente un modèle souhaitable.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Source de l'image*
> - Auteur : Utilisateur Wikipédia espagnol [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Licence : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Ce qui nous importe, c'est la précision des prédictions sur de nouvelles données, et nous utilisons le jeu de données de validation pour estimer les performances de prédiction sur de nouvelles données. L'objectif est de trouver le point optimal (sweet spot) entre le sous-ajustement et le surajustement.  
![](https://i.imgur.com/2q85n9s.png)  
Ce cours continue d'utiliser le modèle de classification par arbre de décision comme exemple, mais les concepts de surajustement et de sous-ajustement s'appliquent à tous les modèles de machine learning.

### Réglage des hyperparamètres (hyperparameter tuning)
L'exemple suivant est un code qui compare les performances du modèle en modifiant la valeur de l'argument *max_leaf_nodes* du modèle d'arbre de décision. (La partie de chargement des données et de séparation du jeu de données de validation est omise)
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
# comparer le MAE avec différentes valeurs de max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Nombre max de nœuds feuilles : %d  \t\t Erreur absolue moyenne :  %d" %(max_leaf_nodes, my_mae))
```
Une fois le réglage des hyperparamètres terminé, on entraîne finalement le modèle sur l'ensemble des données pour maximiser les performances. Il n'est plus nécessaire de garder un jeu de données de validation séparé.

## Leçon 6. Forêts aléatoires
L'utilisation conjointe de plusieurs modèles différents peut donner de meilleures performances qu'un seul modèle. La **forêt aléatoire (random forest)** en est un bon exemple.

Une forêt aléatoire est composée de nombreux arbres de décision, et fait sa prédiction finale en faisant la moyenne des prédictions de chaque arbre. Dans de nombreux cas, elle montre une me
