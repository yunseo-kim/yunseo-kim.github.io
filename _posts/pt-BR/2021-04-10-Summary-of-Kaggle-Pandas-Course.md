---
title: Resumo do conteúdo do curso Kaggle-Pandas
description: Resumo do conteúdo do minicurso de Pandas dos cursos abertos do Kaggle.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.jpg
---

# Pandas
Resolva pequenos desafios práticos para aperfeiçoar suas habilidades de manipulação de dados.

## Lição 1. Criando, Lendo e Escrevendo
### Importando o pandas
```python
import pandas as pd
```
O pandas tem dois objetos principais: **DataFrame** e **Series**.

### DataFrame
Um DataFrame é uma tabela. Contém uma matriz de entradas individuais, onde cada entrada tem um valor específico e corresponde a uma linha (ou registro) e uma coluna. As entradas de um DataFrame não precisam ser necessariamente números inteiros.
```python
pd.DataFrame({'Bob': ['Eu gostei.', 'Foi horrível.'], 'Sue': ['Muito bom.', 'Sem graça.']})
```
A declaração de um DataFrame é feita no formato de dicionário Python. As chaves são os nomes das colunas e os valores são listas com os itens a serem inseridos.

Normalmente, ao declarar um DataFrame, os rótulos das colunas recebem seus nomes, mas os rótulos das linhas recebem números inteiros 0, 1, 2... Se necessário, podemos especificar manualmente os rótulos das linhas. A lista de rótulos das linhas em um DataFrame é chamada de **Index**, e podemos especificar seu valor usando o parâmetro ```index```.
```python
pd.DataFrame({'Bob': ['Eu gostei.', 'Foi horrível.'], 
              'Sue': ['Muito bom.', 'Sem graça.']},
             index=['Produto A', 'Produto B'])
```

### Series
Uma Series é uma sequência de valores de dados.
```python
pd.Series([1, 2, 3, 4, 5])
```
Uma Series é essencialmente igual a uma única coluna de um DataFrame. Portanto, também podemos especificar um índice para ela. A diferença é que, em vez de um 'nome de coluna', ela tem um 'nome', ```name```.
```python
pd.Series([30, 35, 40], index=['Vendas 2015', 'Vendas 2016', 'Vendas 2017'], name='Produto A')
```
Series e DataFrames estão intimamente relacionados. Pode ser útil pensar em um DataFrame como simplesmente um conjunto de Series.

### Lendo arquivos de dados
Em muitos casos, em vez de criar dados diretamente, usamos dados já existentes. Os dados podem estar armazenados em vários formatos, mas o mais básico é o arquivo CSV. O conteúdo de um arquivo CSV geralmente se parece com isto:
```
Produto A,Produto B,Produto C,
30,21,9,
35,34,1,
41,11,11
```
Ou seja, um arquivo CSV é uma tabela onde cada valor é separado por vírgulas. Por isso o nome "Comma-Separated Values", CSV.

Para carregar dados no formato CSV em um DataFrame, usamos a função ```pd.read_csv()```.

Podemos usar o atributo ```shape``` para verificar o tamanho do DataFrame.

O comando ```head()``` pode ser usado para visualizar as primeiras cinco linhas do DataFrame.

A função ```pd.read_csv()``` tem mais de 30 parâmetros. Por exemplo, se o arquivo CSV que queremos carregar já inclui seu próprio índice, podemos especificar o valor do parâmetro ```index_col``` para usar essa coluna como índice em vez de deixar o pandas gerar um índice automaticamente.

### Escrevendo dados
Podemos exportar um DataFrame para um arquivo CSV usando o método ```to_csv()```. Usa-se da seguinte forma:
```python
(nome do DataFrame).to_csv("(caminho do arquivo CSV)")
```

## Lição 2. Indexação, Seleção e Atribuição
Selecionar valores específicos para usar de um DataFrame ou Series do pandas é uma etapa em quase todas as operações que envolvem dados.
