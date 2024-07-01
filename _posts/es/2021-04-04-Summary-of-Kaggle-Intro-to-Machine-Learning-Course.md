---
title: "Resumen del curso Kaggle-Intro to Machine Learning"
description: >-
  He resumido el contenido del curso público de Kaggle 'Intro to Machine Learning'.
categories: [Ciencia de Datos, Aprendizaje Automático]
tags: [Cursos de Kaggle, Pandas, scikit-learn]
toc: true
toc_sticky: true
---

Decidí estudiar los [cursos públicos de Kaggle](https://www.kaggle.com/learn/overview).
Planeo resumir brevemente el contenido de cada curso a medida que los complete. Este primer artículo es un resumen del curso **Intro to Machine Learning**.

# Intro to Machine Learning
Aprende las ideas fundamentales del aprendizaje automático y construye tus primeros modelos.

## Lección 1. Cómo funcionan los modelos
Comienza de manera ligera y sin presiones. Trata sobre cómo funcionan y se utilizan los modelos de aprendizaje automático. Utiliza el ejemplo de un modelo simple de árbol de decisión (Decision Tree) para clasificación, suponiendo una situación en la que se necesita predecir precios inmobiliarios.

El proceso de encontrar patrones en los datos se llama **entrenar** el modelo (**fitting** o **training** the model). Los datos utilizados para entrenar el modelo se denominan **datos de entrenamiento (training data)**. Una vez entrenado, el modelo se puede aplicar a nuevos datos para hacer **predicciones (predict)**.

## Lección 2. Exploración básica de datos
Lo primero que hay que hacer en cualquier proyecto de aprendizaje automático es familiarizarse con los datos. Primero hay que entender las características de los datos para poder diseñar un modelo adecuado. La biblioteca Pandas se utiliza casi siempre para explorar y manipular datos, y esta lección cubre los conceptos básicos de Pandas.

El núcleo de la biblioteca Pandas es el DataFrame, que se puede pensar como una especie de tabla. Es similar a una hoja de Excel o una tabla de base de datos SQL. Se puede cargar datos en formato CSV utilizando el método read_csv.
```python
# Es buena práctica guardar la ruta del archivo en una variable para facilitar el acceso.
file_path = '(ruta del archivo)'
# Lee los datos y los guarda en un DataFrame llamado 'data_1' (en la práctica, es mejor usar un nombre más descriptivo).
data_1 = pd.read_csv(file_path)
```
Se puede usar el método describe para ver un resumen de la información de los datos.
```python
data_1.describe()
```
Esto mostrará 8 elementos de información:
- **count**: número de filas con valores reales (excluyendo valores faltantes)
- **mean**: promedio
- **std**: desviación estándar
- **min**: valor mínimo
- **25%**: valor del 25% inferior
- **50%**: valor medio
- **75%**: valor del 75% inferior
- **max**: valor máximo

## Lección 3. Tu primer modelo de aprendizaje automático
### Procesamiento de datos
Hay que decidir qué variables de los datos dados se utilizarán para el modelado. Se puede usar el atributo **columns** del DataFrame para ver las etiquetas de las columnas.
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
Hay varias formas de seleccionar las partes necesarias de los datos dados, que se tratan en profundidad en el [Curso Micro de Pandas](https://www.kaggle.com/learn/pandas) de Kaggle (también resumiré este contenido más adelante). Aquí se utilizan dos métodos:
1. Notación de punto
2. Uso de listas

Primero, se selecciona la columna correspondiente al **objetivo de predicción (prediction target)** usando la **notación de punto**. Esta columna única se almacena en una **Serie (Series)**. Una Serie se puede pensar aproximadamente como un DataFrame compuesto por una sola columna. Por convención, el objetivo de predicción se denomina **y**.
```python
y = melbourne_data.Price
```

Las columnas que se introducen en el modelo para hacer predicciones se llaman "características (features)". En el caso de los datos de precios de viviendas de Melbourne dados como ejemplo, serían las columnas utilizadas para predecir los precios de las viviendas. A veces se utilizan todas las columnas de los datos dados como características, excluyendo el objetivo de predicción, y otras veces es mejor seleccionar solo algunas de ellas.  
Se pueden seleccionar múltiples características usando una lista como se muestra a continuación. Todos los elementos de esta lista deben ser cadenas.
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
Por convención, estos datos se denominan **X**.
```python
X = melbourne_data[melbourne_features]
```

Además de describe, otro método útil para analizar datos es head. Muestra las primeras 5 filas.
```python
X.head()
```

### Diseño del modelo
En la etapa de modelado, generalmente se utiliza mucho la biblioteca **scikit-learn**. El proceso de diseñar y usar un modelo generalmente consta de los siguientes pasos:
- **Definir (Define)**: Determinar el tipo de modelo y sus parámetros.
- **Entrenar (Fit)**: Encontrar patrones en los datos dados. Este es el núcleo del modelado.
- **Predecir (Predict)**: Realizar predicciones utilizando el modelo entrenado.
- **Evaluar (Evaluate)**: Evaluar qué tan precisas son las predicciones del modelo.

A continuación se muestra un ejemplo de cómo definir y entrenar un modelo usando scikit-learn:
```python
from sklearn.tree import DecisionTreeRegressor

# Define el modelo. Especifica un número para random_state para asegurar los mismos resultados en cada ejecución
melbourne_model = DecisionTreeRegressor(random_state=1)

# Entrena el modelo
melbourne_model.fit(X, y)
```

Muchos modelos de aprendizaje automático tienen cierto grado de aleatoriedad en su proceso de entrenamiento. Al especificar un valor para ```random_state```, se puede obtener el mismo resultado en cada ejecución, y es una buena práctica especificarlo a menos que haya una razón específica para no hacerlo. No importa qué valor se use.

Una vez completado el entrenamiento del modelo, se pueden realizar predicciones de la siguiente manera:
```python
print("Haciendo predicciones para las siguientes 5 casas:")
print(X.head())
print("Las predicciones son")
print(melbourne_model.predict(X.head()))
```

## Lección 4. Validación del modelo
### Métodos de validación del modelo
Para mejorar continuamente un modelo, es necesario medir su rendimiento. Cuando se hacen predicciones utilizando un modelo, habrá casos en los que acierte y casos en los que se equivoque. Se necesita un indicador para verificar el rendimiento predictivo de este modelo. Hay varios tipos de indicadores, pero aquí se utiliza el **MAE (Mean Absolute Error, Error Absoluto Medio)**.

En el caso de la predicción de precios de viviendas en Melbourne, el error de predicción para cada precio de vivienda es el siguiente:  
```
error = real - predicho
```
El MAE se calcula tomando el valor absoluto de cada error de predicción y luego calculando el promedio de estos errores absolutos. Se puede implementar en scikit-learn de la siguiente manera:
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Problemas de usar datos de entrenamiento para la validación
En el código anterior, se realizó tanto el entrenamiento del modelo como la validación utilizando un solo conjunto de datos. Pero esto no se debe hacer. Este curso explica la razón con un ejemplo.

> En el mercado inmobiliario real, el color de la puerta no tiene relación con el precio de la casa.  
> 
> Sin embargo, por casualidad, en los datos utilizados para el entrenamiento, todas las casas con puertas verdes son muy caras. Como el papel del modelo es encontrar patrones en los datos que se puedan utilizar para predecir los precios de las casas, en este caso nuestro modelo detectará este patrón y predecirá que las casas con puertas verdes son caras. 
>
> Si se realizan predicciones de esta manera, parecerá preciso para los datos de entrenamiento dados.
>
> Sin embargo, cuando se realicen predicciones sobre nuevos datos donde la regla "las casas con puertas verdes son caras" no se aplica, este modelo será muy impreciso.

Como el modelo debe realizar predicciones a partir de nuevos datos para que tenga sentido, debemos realizar la validación utilizando datos que no se utilizaron para el entrenamiento del modelo. El método más simple es separar algunos datos durante el proceso de modelado y utilizarlos para medir el rendimiento. Estos datos se llaman **datos de validación (validation data)**.

### Separación del conjunto de datos de validación
La biblioteca scikit-learn tiene una función ```train_test_split``` que divide los datos en dos. El siguiente código divide los datos en dos, utilizando uno para entrenamiento y el otro para validación usando ```mean_absolute_error```:
```python
from sklearn.model_selection import train_test_split

# divide los datos en datos de entrenamiento y validación, tanto para características como para objetivo
# La división se basa en un generador de números aleatorios. Proporcionar un valor numérico al
# argumento random_state garantiza que obtengamos la misma división cada vez que
# ejecutemos este script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define el modelo
melbourne_model = DecisionTreeRegressor()
# Entrena el modelo
melbourne_model.fit(train_X, train_y)

# obtiene precios predichos en los datos de validación
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## Lección 5. Sobreajuste y subajuste
### Sobreajuste y subajuste
- **Sobreajuste (overfitting)**: Fenómeno en el que el modelo se ajusta muy precisamente solo al conjunto de datos de entrenamiento, pero no puede hacer predicciones adecuadas en el conjunto de datos de validación u otros datos nuevos.
- **Subajuste (underfitting)**: Fenómeno en el que el modelo no logra encontrar características y patrones importantes en los datos dados, y por lo tanto no puede hacer predicciones adecuadas incluso en el conjunto de datos de entrenamiento.

En la imagen de abajo, la línea verde representa un modelo sobreajustado, mientras que la línea negra representa un modelo deseable.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia en español [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Lo que nos importa es la precisión de la predicción en nuevos datos, y usamos el conjunto de datos de validación para estimar el rendimiento predictivo en nuevos datos. El objetivo es encontrar el punto óptimo (sweet spot) entre el subajuste y el sobreajuste.  
![](https://i.imgur.com/2q85n9s.png)  
Aunque este curso sigue utilizando el modelo de clasificación de árbol de decisión como ejemplo, los conceptos de sobreajuste y subajuste se aplican a todos los modelos de aprendizaje automático.

### Ajuste de hiperparámetros (hyperparameter tuning)
El siguiente ejemplo es un código que compara y mide el rendimiento del modelo cambiando el valor del argumento *max_leaf_nodes* del modelo de árbol de decisión. (Se omite la parte de cargar los datos y separar el conjunto de datos de validación)
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
# compara MAE con diferentes valores de max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
```
Una vez completado el ajuste de hiperparámetros, finalmente se entrena el modelo con todos los datos para maximizar el rendimiento. Ya no es necesario separar un conjunto de datos de validación.

## Lección 6. Bosques aleatorios
Usar varios modelos diferentes juntos puede dar mejor rendimiento que un solo modelo. Los **bosques aleatorios (random forests)** son un buen ejemplo.

Un bosque aleatorio está compuesto por numerosos árboles de decisión y hace la predicción final promediando los valores de predicción de cada árbol. En muchos casos, muestra una mejor precisión de predicción que un solo árbol de decisión, y funciona bien incluso cuando se usan los parámetros predeterminados.