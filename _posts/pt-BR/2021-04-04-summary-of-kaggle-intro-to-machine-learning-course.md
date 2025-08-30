---
title: "Resumo do conteúdo do curso 'Intro to Machine Learning' do Kaggle"
description: "Resumo dos conceitos-chave de machine learning e do uso básico de Pandas e scikit‑learn, baseado no curso público da Kaggle Intro to Machine Learning."
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
image: /assets/img/technology.webp
math: true
redirect_from:
  - /posts/Summary-of-Kaggle-Intro-to-Machine-Learning-Course/
---

[Decidi estudar os cursos públicos do Kaggle](https://www.kaggle.com/learn).
A cada curso concluído, pretendo resumir brevemente o que aprendi. O primeiro post é um resumo do curso [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning).

![Certificado de Conclusão](/assets/img/kaggle-intro-to-machine-learning/certificate.png)

## Lição 1. Como os Modelos Funcionam
Começamos de forma leve. Trata de como os modelos de machine learning funcionam e como são usados. Assumindo um cenário de previsão de preços de imóveis, o curso explica usando como exemplo um modelo de classificação por árvore de decisão.

Extrair padrões a partir de dados é o que chamamos de **treinar** o modelo (fitting ou training). Os dados usados no treino são chamados de **dados de treino (training data)**. Após o treino, você aplica o modelo a novos dados para **prever (predict)**.

## Lição 2. Exploração Básica de Dados
Em qualquer projeto de machine learning, a primeira tarefa é você se familiarizar com os dados. Entender suas características é essencial para desenhar um modelo adequado. Para explorar e manipular dados, normalmente usamos a biblioteca [Pandas](https://pandas.pydata.org/).

```python
import pandas as pd
```

O núcleo do Pandas é o DataFrame, que você pode imaginar como uma tabela. É semelhante a uma planilha do Excel ou a uma tabela de banco de dados SQL. Com o método read_csv, você pode carregar dados em formato CSV.

```python
# É recomendável guardar o caminho do arquivo em uma variável para acessá-lo facilmente sempre que necessário.
file_path = "(caminho do arquivo)"
# Ler os dados e armazenar em um DataFrame chamado 'example_data' (na prática, use um nome mais descritivo).
example_data = pd.read_csv(file_path)
```

Use o método describe para ver um resumo do conjunto de dados.

```python
example_data.describe()
```

Ele exibe 8 itens:
- **count**: número de linhas com valores não nulos
- **mean**: média
- **std**: desvio padrão
- **min**: valor mínimo
- **25%**: 1º quartil (25%)
- **50%**: mediana (50%)
- **75%**: 3º quartil (75%)
- **max**: valor máximo

## Lição 3. Seu Primeiro Modelo de Machine Learning
### Preparação de dados
Você precisa decidir quais variáveis do conjunto de dados usar na modelagem. Com o atributo **columns** do DataFrame, é possível conferir os rótulos das colunas.

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

Há várias maneiras de selecionar partes relevantes dos dados; o Kaggle aprofunda isso no [Pandas Micro-Course](https://www.kaggle.com/learn/pandas) (que também pretendo resumir depois). Aqui usaremos duas:
1. Dot notation
2. Lista

Primeiro, usando dot notation, selecione a coluna que corresponde ao **alvo de previsão** e armazene como uma **Série (Series)**. Uma Série é como um DataFrame com apenas uma coluna. Por convenção, chamamos o alvo de **y**.

```python
y = melbourne_data.Price
```

As colunas usadas como entrada do modelo são chamadas de "características" ou "features". No conjunto de dados de preços de casas de Melbourne, são as colunas utilizadas para prever o preço. Às vezes usamos todas as colunas, exceto o alvo; outras vezes é melhor selecionar apenas algumas.  
Você pode selecionar várias features usando uma lista; todos os elementos da lista devem ser strings.

```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```

Por convenção, denotamos esse conjunto de dados como **X**.

```python
X = melbourne_data[melbourne_features]
```

Além de describe, outro método útil é head, que mostra as 5 primeiras linhas.

```python
X.head()
```

### Projeto do modelo
Na modelagem, usamos várias bibliotecas; uma das mais comuns é a [scikit-learn](https://scikit-learn.org/stable/). Em linhas gerais, o fluxo é:
- **Definir (Define)**: escolher o tipo de modelo e seus parâmetros.
- **Treinar (Fit)**: encontrar regularidades nos dados; é o cerne da modelagem.
- **Prever (Predict)**: usar o modelo treinado para fazer previsões.
- **Avaliar (Evaluate)**: medir a precisão das previsões do modelo.

Abaixo, um exemplo de como definir e treinar um modelo na scikit-learn.

```python
from sklearn.tree import DecisionTreeRegressor

# Defina o modelo. Especifique um número em random_state para garantir os mesmos resultados em cada execução
melbourne_model = DecisionTreeRegressor(random_state=1)

# Treine o modelo
melbourne_model.fit(X, y)
```

Muitos modelos de machine learning usam algum grau de aleatoriedade durante o treino. Ao definir `random_state`, você garante os mesmos resultados a cada execução; é uma boa prática fazê-lo, a menos que haja motivo para não definir. O valor específico não importa.

Após o treino, você pode prever assim:

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

## Lição 4. Validação do Modelo
### Como validar um modelo
Para melhorar iterativamente um modelo, precisamos medir seu desempenho. Ao fazer previsões, algumas estarão corretas e outras, não. Precisamos de uma métrica para avaliar a performance. Há várias; aqui usamos o **MAE (Mean Absolute Error, Erro Absoluto Médio)**.

No caso da previsão do preço de casas em Melbourne, o erro de previsão para cada casa é:

$$ \mathrm{error} = \mathrm{actual} − \mathrm{predicted} $$

O MAE é calculado tomando o valor absoluto de cada erro e fazendo a média desses erros absolutos:

$$ \mathrm{MAE} = \frac{\sum_{i=1}^N |\mathrm{error}|}{N} $$

Na scikit-learn:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### O problema de validar com os mesmos dados de treino
Acima, usamos um único conjunto de dados tanto para treinar quanto para validar o modelo. Na prática, isso não deve ser feito. O curso do Kaggle explica o porquê com o exemplo a seguir:

> No mercado imobiliário real, a cor da porta não tem relação com o preço.  
> 
> Mas, por acaso, no conjunto de treino as casas com porta verde eram todas muito caras. Como o papel do modelo é encontrar regularidades úteis para prever o preço, nosso modelo captará essa “regra” e preverá que casas com porta verde são caras.
>
> Assim, nesse conjunto de treino, a previsão parecerá correta.
>
> Porém, ao prever em novos dados onde “porta verde implica preço alto” não se sustenta, o modelo será muito impreciso.

Como o objetivo é prever em novos dados, devemos validar usando dados que não foram usados no treino. O método mais simples é reservar uma parte dos dados apenas para medir desempenho. Esse conjunto é o **conjunto de validação (validation data)**.

### Separar um conjunto de validação
A scikit-learn oferece a função `train_test_split` para dividir os dados. O código abaixo separa os dados em treino e validação, treina o modelo e mede o MAE (`mean_absolute_error`) no conjunto de validação.

```python
from sklearn.model_selection import train_test_split

# Divida os dados em treino e validação, tanto para as features quanto para o alvo
# A divisão usa um gerador de números aleatórios. Fornecer um valor numérico em
# random_state garante a mesma divisão a cada execução deste script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Defina o modelo
melbourne_model = DecisionTreeRegressor()
# Treine o modelo
melbourne_model.fit(train_X, train_y)

# Obtenha as previsões no conjunto de validação
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## Lição 5. Underfitting e Overfitting
### Sobreajuste e subajuste
- **Overfitting (sobreajuste)**: o modelo se ajusta muito bem ao conjunto de treino, mas tem baixo desempenho em validação ou em novos dados.
- **Underfitting (subajuste)**: o modelo não captura características e regularidades importantes, tendo baixo desempenho até mesmo no treino.

Considere treinar um modelo para classificar os pontos vermelhos e azuis na figura abaixo. A linha verde representa um modelo com sobreajuste; a linha preta representa um modelo desejável.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Fonte da imagem*
> - Autor: usuário da Wikipédia em espanhol [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Licença: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

O que importa é a acurácia em novos dados; usamos um conjunto de validação para estimá-la. O objetivo é encontrar o ponto ótimo entre subajuste e sobreajuste (sweet spot).  
![](https://i.imgur.com/2q85n9s.png)  
Embora o curso use continuamente o modelo de classificação por árvore de decisão como exemplo, sobreajuste e subajuste são conceitos que se aplicam a todos os modelos de machine learning.

### Ajuste de hiperparâmetros (hyperparameter tuning)
O exemplo abaixo compara o desempenho do modelo variando o argumento *max_leaf_nodes* de uma árvore de decisão (carregamento de dados e separação de validação omitidos).

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
# Compare o MAE para diferentes valores de max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Número máximo de nós-folha: %d  \t\t Erro Absoluto Médio:  %d" %(max_leaf_nodes, my_mae))
```

Depois de ajustar os hiperparâmetros, treine o modelo final com todos os dados disponíveis para maximizar o desempenho. Não há mais necessidade de manter um conjunto de validação separado.

## Lição 6. Random Forests
Combinar vários modelos diferentes costuma produzir melhor desempenho do que um único modelo. Esse é o conceito de **ensemble**; um bom exemplo é a **Random Forest**.

Uma Random Forest é composta por muitas árvores de decisão e faz a previsão final pela média das previsões de cada árvore. Em muitos casos, ela supera uma única árvore de decisão em acurácia.
