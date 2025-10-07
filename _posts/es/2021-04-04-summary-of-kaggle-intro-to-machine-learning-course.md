---
title: "Resumen del contenido del curso 'Intro to Machine Learning' de Kaggle"
description: "Resumen de conceptos clave de aprendizaje automático y del uso básico de pandas y scikit‑learn, a partir del curso público de Kaggle “Intro to Machine Learning”."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

He decidido estudiar los [cursos públicos de Kaggle](https://www.kaggle.com/learn).
Cada vez que termine un curso, pienso resumir brevemente lo que he aprendido. Esta primera entrada es un resumen del curso [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning).

![Certificado de finalización](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lesson 1. How Models Work
Empezamos de forma ligera y sin presión. Trata de cómo funcionan y cómo se usan los modelos de aprendizaje automático. Partiendo del supuesto de que hay que predecir precios inmobiliarios, se explica con un ejemplo sencillo de un modelo de clasificación de árbol de decisión (Decision Tree).

Encontrar patrones a partir de los datos se denomina **ajustar (fitting)** o **entrenar (training)** el modelo. Los datos usados para entrenar el modelo se llaman **datos de entrenamiento (training data)**. Una vez entrenado, se puede aplicar el modelo a nuevos datos para **predecir (predict)**.

## Lesson 2. Basic Data Exploration
En cualquier proyecto de aprendizaje automático, lo primero es familiarizarse con los datos. Hay que entender sus características para diseñar un modelo adecuado. Para explorar y manipular datos suele usarse la biblioteca [Pandas](https://pandas.pydata.org/).

```python
import pandas as pd
```

El núcleo de la biblioteca pandas es el DataFrame, que puede pensarse como una especie de tabla, similar a una hoja de Excel o a una tabla de una base de datos SQL. Con el método read_csv se pueden cargar datos en formato CSV.

```python
# Es recomendable guardar la ruta del archivo en una variable para acceder fácilmente cuando se necesite.
file_path = "(ruta del archivo)"
# Leemos los datos y los guardamos en un DataFrame llamado 'example_data'
# (en la práctica, conviene usar un nombre más descriptivo).
example_data = pd.read_csv(file_path)
```

Con el método describe se puede consultar un resumen de la información del conjunto de datos.

```python
example_data.describe()
```

Se pueden ver 8 elementos de información:
- **count**: número de filas con valores reales (excluye valores faltantes)
- **mean**: media
- **std**: desviación estándar
- **min**: valor mínimo
- **25%**: valor del percentil 25
- **50%**: mediana
- **75%**: valor del percentil 75
- **max**: valor máximo

## Lesson 3. Your First Machine Learning Model
### Preparación de datos
Hay que decidir qué variables del conjunto de datos se usarán en el modelado. Se puede consultar las etiquetas de las columnas con el atributo **columns** del DataFrame.

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

Hay varias formas de seleccionar las partes necesarias del conjunto de datos; Kaggle lo trata con más detalle en el [Microcurso de Pandas](https://www.kaggle.com/learn/pandas) (este contenido lo he resumido en [una entrada aparte](/posts/summary-of-kaggle-pandas-course/)). Aquí usamos dos métodos:
1. Notación por punto
2. Uso de listas

Primero, usando **notación de punto (dot notation)**, seleccionamos la columna que es el **objetivo de predicción (prediction target)** y la guardamos como una **Serie (Series)**. Puedes pensar en una serie como un DataFrame compuesto por una sola columna. Por convención, el objetivo de predicción se denota como **y**.

```python
y = melbourne_data.Price
```

Las columnas que se introducen en el modelo para hacer predicciones se llaman "características (features)". En el ejemplo de los precios de la vivienda de Melbourne, serían las columnas que usaremos para predecir el precio. A veces se usan todas las columnas salvo el objetivo; otras veces conviene seleccionar solo algunas.  
Se pueden seleccionar varias características usando una lista, como se muestra a continuación. Todos los elementos de esta lista deben ser cadenas.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

Por convención, a estos datos se les llama **X**.

```python
X = melbourne_data[melbourne_features]
```

Además de describe, otro método útil para el análisis es head, que muestra las primeras 5 filas.

```python
X.head()
```

### Diseño del modelo
En la fase de modelado pueden usarse diversas bibliotecas; una muy común es [scikit-learn](https://scikit-learn.org/stable/). El proceso general para diseñar y usar un modelo es:
- **Definición (Define)**: decidir el tipo de modelo y sus parámetros.
- **Entrenamiento (Fit)**: encontrar regularidades en los datos. Es el núcleo del modelado.
- **Predicción (Predict)**: realizar predicciones con el modelo entrenado.
- **Evaluación (Evaluate)**: medir la precisión de las predicciones del modelo.

A continuación se muestra un ejemplo de cómo definir y entrenar un modelo con scikit-learn.

```python
from sklearn.tree import DecisionTreeRegressor

# Definir el modelo. Especifica un número en random_state para asegurar los mismos resultados en cada ejecución
melbourne_model = DecisionTreeRegressor(random_state=1)

# Ajustar/entrenar el modelo
melbourne_model.fit(X, y)
```

Muchos modelos de aprendizaje automático incorporan cierta aleatoriedad durante el entrenamiento. Al fijar `random_state`, garantizamos obtener el mismo resultado en cada ejecución y, salvo que haya una razón para no hacerlo, es una buena práctica. El valor concreto no importa.

Una vez entrenado el modelo, se pueden hacer predicciones así:

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
### Cómo validar un modelo
Para mejorar iterativamente un modelo, necesitamos medir su rendimiento. Cuando hacemos predicciones con un modelo, algunas serán correctas y otras no. Por ello requerimos un indicador para evaluar su desempeño. Hay muchas métricas; aquí usamos **MAE (Mean Absolute Error, error absoluto medio)**.

En la predicción de los precios de viviendas de Melbourne, el error de predicción para cada casa es:

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

El MAE se calcula tomando el valor absoluto de cada error de predicción y promediando esos errores absolutos.

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

Con scikit-learn se obtiene así:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Por qué no debe validarse con los datos de entrenamiento
En el código anterior, usamos un único conjunto de datos tanto para entrenar como para validar el modelo. En realidad, no debemos hacerlo. El curso de Kaggle explica el motivo con este ejemplo:

> En el mercado inmobiliario real, el color de la puerta no guarda relación con el precio de la vivienda.  
> 
> Sin embargo, por casualidad, en los datos de entrenamiento las casas con puertas verdes eran muy caras. Como la función del modelo es extraer regularidades útiles para predecir el precio, en este caso el modelo detectará esa pauta y predecirá que las casas con puerta verde son caras.
>
> Si hacemos predicciones de ese modo, parecerá muy preciso sobre los datos de entrenamiento.
>
> Pero cuando elabore predicciones sobre nuevos datos en los que “las casas con puerta verde son caras” no sea una regla válida, el modelo será muy impreciso.

Dado que lo que nos importa es predecir bien sobre datos nuevos, debemos validar usando datos que no se hayan empleado en el entrenamiento. El método más simple es apartar una parte de los datos durante el modelado y reservarla para medir el rendimiento. A estos datos se les llama **datos de validación (validation data)**.

### Separación del conjunto de validación
La biblioteca scikit-learn ofrece la función `train_test_split` para dividir los datos en dos partes. El siguiente código separa los datos para usar una parte en el entrenamiento y otra en la validación, donde mediremos el MAE (`mean_absolute_error`).

```python
from sklearn.model_selection import train_test_split

# dividir los datos en entrenamiento y validación, tanto para características como para objetivo
# La división se basa en un generador de números aleatorios. Proporcionar un valor numérico
# a random_state garantiza que obtengamos la misma división cada vez que ejecutemos este script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Definir el modelo
melbourne_model = DecisionTreeRegressor()
# Ajustar/entrenar el modelo
melbourne_model.fit(train_X, train_y)

# obtener las predicciones sobre los datos de validación
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## Lesson 5. Underfitting and Overfitting
### Sobreajuste y subajuste
- **Sobreajuste (overfitting)**: el modelo se ajusta extremadamente bien a los datos de entrenamiento, pero falla al predecir sobre el conjunto de validación u otros datos nuevos.
- **Subajuste (underfitting)**: el modelo no capta suficientemente las características y regularidades importantes del conjunto de datos, por lo que incluso en entrenamiento su rendimiento es insuficiente.

Pensemos en el problema de entrenar un modelo que clasifica los puntos rojos y azules en un conjunto como el de la imagen siguiente. En ese caso, la línea verde sería un modelo sobreajustado, mientras que la línea negra representa un modelo deseable.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia en español [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Lo importante es la precisión sobre datos nuevos, y estimamos ese desempeño con el conjunto de validación. El objetivo es encontrar el punto óptimo (sweet spot) entre subajuste y sobreajuste.  
![](https://i.imgur.com/2q85n9s.png)  
Aunque a lo largo de este curso de Kaggle se usa como ejemplo un modelo de clasificación con árbol de decisión, los conceptos de sobreajuste y subajuste se aplican a todos los modelos de aprendizaje automático.

### Ajuste de hiperparámetros (hyperparameter tuning)
El siguiente ejemplo compara el rendimiento del modelo variando el valor del argumento en cursiva *max_leaf_nodes* en un árbol de decisión (se omiten las partes de carga de datos y partición de validación).

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
# comparar el MAE con distintos valores de max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
```

Una vez terminado el ajuste de hiperparámetros, entrenamos el modelo con todos los datos disponibles para maximizar el rendimiento. Ya no es necesario apartar un conjunto de validación.

## Lesson 6. Random Forests
Combinar varios modelos distintos puede ofrecer mejor rendimiento que un único modelo. A esto se le llama **ensamble (Ensemble)**, y el **bosque aleatorio (Random Forest)** es un buen ejemplo.

Un bosque aleatorio está compuesto por muchos árboles de decisión, y la predicción final se obtiene promediando las predicciones de cada árbol. En muchos casos, logra mayor precisión que un árbol de decisión individual.
