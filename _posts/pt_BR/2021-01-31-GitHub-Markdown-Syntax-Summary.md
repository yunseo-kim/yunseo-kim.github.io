---
title: "Resumo da sintaxe Markdown do GitHub"
description: >-
  Aprenda o que é Markdown e resuma as principais sintaxes do GitHub Flavored Markdown para hospedar blogs no GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
toc: true
toc_sticky: true
---

É necessário conhecer a sintaxe **markdown** para utilizar o GitHub Pages.
Este texto foi escrito com base nos documentos oficiais do GitHub [Dominando o Markdown](https://guides.github.com/features/mastering-markdown/) e [Sintaxe básica de escrita e formatação](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. O que é Markdown
> **Markdown** é uma linguagem de marcação leve baseada em texto simples. É usada para criar documentos formatados usando texto simples e se caracteriza por ter uma sintaxe mais fácil e simples em comparação com linguagens de marcação comuns. É muito utilizada em arquivos README distribuídos com software e em postagens online, pois pode ser facilmente convertida em HTML e Rich Text Format (RTF), entre outros formatos de documentos.
>> John Gruber criou a linguagem Markdown em 2004, com uma colaboração significativa de Aaron Swartz na sintaxe, com o objetivo de permitir que as pessoas "escrevam usando um formato de texto simples fácil de ler e escrever", e que possa ser opcionalmente convertido em XHTML (ou HTML) estruturalmente válido.

-[Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Sintaxe Markdown
Como não há um padrão definido para Markdown, a sintaxe detalhada pode variar um pouco dependendo de onde é usada. A sintaxe Markdown resumida aqui é baseada no [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Quebra de linha, separação de parágrafos
No Markdown, pressionar Enter uma vez não é reconhecido como uma quebra de linha.
~~~
Primeira frase.
Segunda frase.
Terceira frase.
~~~
Primeira frase.
Segunda frase.
Terceira frase.

A quebra de linha é aplicada quando você insere dois ou mais espaços consecutivos.
~~~
Primeira frase.  
Segunda frase.  
Terceira frase.
~~~
Primeira frase.  
Segunda frase.  
Terceira frase.

Os parágrafos são separados por uma linha em branco (pressionar Enter duas vezes).
~~~
Um parágrafo.

Outro parágrafo.
~~~
Um parágrafo.

Outro parágrafo.

### 2.2. Cabeçalhos
Existem 6 níveis no total.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6

### 2.3. Ênfase
```
*Este texto está em itálico*
_Este também está em itálico_

**Este texto está em negrito**
__Este também está em negrito__

~~Este texto foi riscado~~

_Você **pode** combiná-los_

***Todo este texto é importante***
```
*Este texto está em itálico*  
_Este também está em itálico_

**Este texto está em negrito**  
__Este também está em negrito__

~~Este texto foi riscado~~

_Você **pode** combiná-los_

***Todo este texto é importante***

### 2.4. Citação de texto
Use \>.
```
> Esta é uma citação de primeiro nível.
>> Esta é uma citação de segundo nível.
>>> Esta é uma citação de terceiro nível.
```
> Esta é uma citação de primeiro nível.
>> Esta é uma citação de segundo nível.
>>> Esta é uma citação de terceiro nível.

### 2.5. Citação de código
Use \``` ou \~~~.
~~~
```
git status
git add
git commit
```
~~~
```
git status
git add
git commit
```

Você também pode especificar a linguagem de programação para ativar o realce de sintaxe.
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### 2.6. Links
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

Você também pode usar links de caminho relativo para apontar para outros arquivos no repositório. O uso é o mesmo que no terminal.
```
[README](../README.md)
```

### 2.7. Lista não ordenada
Use \- ou \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Lista ordenada
Use números.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Lista aninhada
```
1. Primeiro item da lista
   - Primeiro item da lista aninhada
     - Segundo item da lista aninhada
```
1. Primeiro item da lista
   - Primeiro item da lista aninhada
     - Segundo item da lista aninhada

### 2.10. Lista de tarefas
Para criar uma lista de tarefas, adicione \[ ] antes de cada item.
Para marcar uma tarefa como concluída, use \[x].
```
- [x] Finalizar minhas alterações
- [ ] Enviar meus commits para o GitHub
- [ ] Abrir um pull request
```
- [x] Finalizar minhas alterações
- [ ] Enviar meus commits para o GitHub
- [ ] Abrir um pull request

### 2.11. Anexar imagens
```
Método: ![(opcional)descrição da imagem](url){(opcional)opções adicionais}
![Logo do GitHub](/images/logo.png)
![Logo do GitHub](/images/logo.png){: .align-center}
![Logo do GitHub](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Criar tabelas
Você pode criar tabelas usando | e -.
Deixe uma linha em branco antes da tabela para que ela seja exibida corretamente.
Use pelo menos três - para que seja reconhecido corretamente.
```

| Alinhado à esquerda | Centralizado | Alinhado à direita |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Alinhado à esquerda | Centralizado | Alinhado à direita |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |