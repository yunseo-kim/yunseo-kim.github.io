---
title: "Resumo do curso Kaggle - Introdução ao Aprendizado de Máquina"
description: >-
  Resumo do conteúdo do curso público do Kaggle 'Introdução ao Aprendizado de Máquina'.
categories: [Data Science, Machine Learning]
tags: [Kaggle Courses, Pandas, scikit-learn]
toc: true
toc_sticky: true
---

Decidi estudar os [cursos públicos do Kaggle](https://www.kaggle.com/learn/overview).
Planejo resumir brevemente o conteúdo de cada curso à medida que os concluir. O primeiro artigo é um resumo do curso **Introdução ao Aprendizado de Máquina**.

# Introdução ao Aprendizado de Máquina
Aprenda as ideias centrais do aprendizado de máquina e construa seus primeiros modelos.

## Lição 1. Como os Modelos Funcionam
Começamos de forma leve e sem pressão. Trata-se de como os modelos de aprendizado de máquina funcionam e como são usados. Usando a situação hipotética de prever preços de imóveis, explica-se usando um modelo simples de árvore de decisão (Decision Tree) como exemplo.

Encontrar padrões nos dados é chamado de **treinar** o modelo (**fitting** ou **training** the model). Os dados usados para treinar o modelo são chamados de **dados de treinamento (training data)**. Após o treinamento, podemos aplicar este modelo a novos dados para fazer **previsões (predict)**.

## Lição 2. Exploração Básica de Dados
A primeira coisa a fazer em qualquer projeto de aprendizado de máquina é familiarizar-se com os dados. Primeiro, é preciso entender as características dos dados para projetar um modelo adequado. O conteúdo básico é sobre a biblioteca Pandas, que é quase essencial para explorar e manipular dados.

O núcleo da biblioteca Pandas é o DataFrame, que pode ser pensado como uma espécie de tabela. É semelhante a uma planilha do Excel ou uma tabela de banco de dados SQL. Podemos carregar dados no formato CSV usando o método read_csv.
```python
# É uma boa prática armazenar o caminho do arquivo em uma variável para fácil acesso quando necessário.
file_path = '(caminho do arquivo)'
# Lê os dados e os armazena em um DataFrame chamado 'data_1' (na prática, é melhor usar um nome mais descritivo).
data_1 = pd.read_csv(file_path)
```
Podemos verificar as informações resumidas dos dados usando o método describe.
```python
data_1.describe()
```
Isso mostrará 8 itens de informação:
- **count**: número de linhas com valores reais (excluindo valores ausentes)
- **mean**: média
- **std**: desvio padrão
- **min**: valor mínimo
- **25%**: valor do quartil inferior
- **50%**: valor mediano
- **75%**: valor do quartil superior
- **max**: valor máximo

## Lição 3. Seu Primeiro Modelo de Aprendizado de Máquina
### Processamento de Dados
Precisamos decidir quais variáveis usar para modelagem a partir dos dados fornecidos. Podemos verificar os rótulos das colunas usando o atributo **columns** do DataFrame.
```python
import pandas as pd

file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
data_1 = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
```
Existem várias maneiras de selecionar as partes necessárias dos dados fornecidos, que são abordadas em profundidade no [Curso Micro de Pandas](https://www.kaggle.com/learn/pandas) do Kaggle (também resumirei este conteúdo mais tarde). Aqui, usamos dois métodos:
1. Notação de ponto
2. Uso de listas

Primeiro, selecionamos a coluna correspondente ao **alvo de previsão (prediction target)** usando a **notação de ponto**. Neste caso, esta única coluna é armazenada em uma **Série (Series)**. Uma Série pode ser pensada aproximadamente como um DataFrame composto por apenas uma coluna. Convencionalmente, o alvo de previsão é denominado **y**.
```python
y = melbourne_data.Price
```

As colunas usadas como entrada para o modelo para fazer previsões são chamadas de "características (features)". No caso dos dados de preços de casas em Melbourne fornecidos como exemplo, seriam as colunas usadas para prever os preços das casas. Às vezes, usamos todas as colunas dos dados fornecidos, exceto o alvo de previsão, como características, e outras vezes pode ser melhor selecionar apenas algumas delas.  
Podemos selecionar várias características usando uma lista, como mostrado abaixo. Todos os elementos desta lista devem ser strings.
```python
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
Convencionalmente, estes dados são denominados **X**.
```python
X = melbourne_data[melbourne_features]
```

Além de describe, outro método útil ao analisar dados é head. Ele mostra as primeiras 5 linhas.
```python
X.head()
```

### Projeto do Modelo
Na fase de modelagem, geralmente usamos muito a biblioteca **scikit-learn**. O processo de projetar e usar um modelo geralmente segue estas etapas:
- **Definir (Define)**: Decidir o tipo de modelo e seus parâmetros.
- **Treinar (Fit)**: Encontrar padrões nos dados fornecidos. Esta é a parte central da modelagem.
- **Prever (Predict)**: Usar o modelo treinado para fazer previsões.
- **Avaliar (Evaluate)**: Avaliar quão precisas são as previsões do modelo.

Abaixo está um exemplo de como definir e treinar um modelo usando scikit-learn:
```python
from sklearn.tree import DecisionTreeRegressor

# Define o modelo. Especifique um número para random_state para garantir os mesmos resultados em cada execução
melbourne_model = DecisionTreeRegressor(random_state=1)

# Treina o modelo
melbourne_model.fit(X, y)
```

Muitos modelos de aprendizado de máquina têm algum grau de aleatoriedade no processo de treinamento. Ao especificar um valor para ```random_state```, podemos obter os mesmos resultados em cada execução, e é uma boa prática especificá-lo a menos que haja uma razão específica para não fazê-lo. Qualquer valor pode ser usado.

Após concluir o treinamento do modelo, podemos fazer previsões da seguinte maneira:
```python
print("Fazendo previsões para as seguintes 5 casas:")
print(X.head())
print("As previsões são")
print(melbourne_model.predict(X.head()))
```

## Lição 4. Validação do Modelo
### Método de Validação do Modelo
Para melhorar continuamente um modelo, precisamos medir seu desempenho. Quando usamos um modelo para fazer previsões, haverá casos em que acertamos e casos em que erramos. Neste ponto, precisamos de uma métrica para verificar o desempenho preditivo deste modelo. Existem vários tipos de métricas, mas aqui usamos o **MAE (Mean Absolute Error, Erro Absoluto Médio)**.

No caso da previsão de preços de casas em Melbourne, o erro de previsão para cada preço de casa é calculado da seguinte forma:  
```
erro = real - previsto
```
O MAE é calculado tomando o valor absoluto de cada erro de previsão e então calculando a média desses erros absolutos. Pode ser implementado usando scikit-learn da seguinte maneira:
```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

### Problemas em Usar Dados de Treinamento para Validação
No código acima, realizamos tanto o treinamento do modelo quanto a validação usando o mesmo conjunto de dados. Mas isso não deve ser feito. Este curso explica o motivo usando um exemplo.

> No mercado imobiliário real, a cor da porta não tem relação com o preço da casa.  
> 
> No entanto, por coincidência, nos dados usados para treinamento, todas as casas com portas verdes são muito caras. Como o papel do modelo é encontrar padrões nos dados que possam ser usados para prever os preços das casas, neste caso, nosso modelo detectará essa regularidade e preverá que casas com portas verdes são caras. 
>
> Se fizermos previsões dessa maneira, parecerá preciso para os dados de treinamento fornecidos.
>
> No entanto, quando aplicarmos previsões a novos dados onde a regra "casas com portas verdes são caras" não se aplica, este modelo será muito impreciso.

Como o modelo deve fazer previsões a partir de novos dados para ter significado, devemos realizar a validação usando dados que não foram usados no treinamento do modelo. O método mais simples é separar alguns dados durante o processo de modelagem para usar na medição de desempenho. Esses dados são chamados de **dados de validação (validation data)**.

### Separação do Conjunto de Dados de Validação
A biblioteca scikit-learn tem uma função ```train_test_split``` que divide os dados em dois. O código abaixo divide os dados em dois, usando um para treinamento e o outro para validação usando ```mean_absolute_error```.
```python
from sklearn.model_selection import train_test_split

# divide os dados em dados de treinamento e validação, tanto para características quanto para o alvo
# A divisão é baseada em um gerador de números aleatórios. Fornecer um valor numérico para
# o argumento random_state garante que obtenhamos a mesma divisão toda vez que executamos este script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define o modelo
melbourne_model = DecisionTreeRegressor()
# Treina o modelo
melbourne_model.fit(train_X, train_y)

# obtém preços previstos nos dados de validação
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

## Lição 5. Underfitting e Overfitting
### Overfitting e Underfitting
- **Overfitting (sobreajuste)**: Fenômeno em que o modelo se ajusta muito precisamente apenas ao conjunto de dados de treinamento, mas não consegue fazer previsões adequadas para o conjunto de dados de validação ou outros novos dados.
- **Underfitting (subajuste)**: Fenômeno em que o modelo não consegue encontrar características e regularidades importantes nos dados fornecidos, resultando em previsões inadequadas mesmo para o conjunto de dados de treinamento.

Na imagem abaixo, a linha verde representa um modelo com overfitting, enquanto a linha preta representa um modelo desejável.
![Overfitting](https://upload.wikimedia.org/wikipedia/commons/1/19/Overfitting.svg)
> *Fonte da imagem*
> - Autor: Usuário da Wikipédia espanhola [Ignacio Icke](https://commons.wikimedia.org/wiki/User:Ignacio_Icke)
> - Licença: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

O que é importante para nós é a precisão da previsão em novos dados, e usamos o conjunto de dados de validação para estimar o desempenho preditivo em novos dados. O objetivo é encontrar o ponto ótimo (sweet spot) entre underfitting e overfitting.  
![](https://i.imgur.com/2q85n9s.png)  
Embora este curso continue usando o modelo de classificação de árvore de decisão como exemplo, os conceitos de overfitting e underfitting se aplicam a todos os modelos de aprendizado de máquina.

### Ajuste de Hiperparâmetros (hyperparameter tuning)
O exemplo abaixo é um código que compara e mede o desempenho do modelo alterando o valor do argumento *max_leaf_nodes* do modelo de árvore de decisão. (A parte de carregamento dos dados e separação do conjunto de dados de validação foi omitida)
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
# compara MAE com diferentes valores de max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
```
Após concluir o ajuste de hiperparâmetros, finalmente treinamos o modelo com todos os dados para maximizar o desempenho. Isso porque não há mais necessidade de manter um conjunto de dados de validação separado.

## Lição 6. Florestas Aleatórias
Usar vários modelos diferentes juntos pode resultar em um desempenho melhor do que um único modelo. As **florestas aleatórias (random forests)** são um bom exemplo disso.

Uma floresta aleatória é composta por numerosas árvores de decisão e faz a previsão final calculando a média dos valores previstos por cada árvore. Em muitos casos, mostra uma precisão preditiva melhor do que uma única árvore de decisão e funciona bem mesmo quando os parâmetros são deixados em seus valores padrão.