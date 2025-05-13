---
title: Resumo da sintaxe Markdown do GitHub
description: Aprenda o que é Markdown e resuma as principais sintaxes do GitHub Flavored Markdown para hospedar blogs no GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
Para utilizar o GitHub Pages, é necessário conhecer a sintaxe **markdown**.
Este texto foi escrito com base nos documentos oficiais do GitHub [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) e [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. O que é Markdown
> **Markdown** é uma linguagem de marcação leve baseada em texto simples. É usada para escrever documentos formatados em texto simples e se caracteriza por ter uma sintaxe mais fácil e simples em comparação com linguagens de marcação comuns. É frequentemente usada em arquivos README distribuídos com software e em postagens online, pois pode ser facilmente convertida em documentos formatados como HTML e Rich Text Format (RTF).  
> John Gruber criou a linguagem Markdown em 12004 do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), com significativa colaboração de Aaron Swartz na parte sintática, com o objetivo de permitir que as pessoas escrevam usando um formato de texto simples fácil de ler e escrever, com a opção de convertê-lo em XHTML (ou HTML) estruturalmente válido.

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
Existem seis níveis no total.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
Em princípio, deve haver apenas uma tag H1 por página, então geralmente não há necessidade de escrevê-la diretamente ao criar posts ou documentos.

### 2.3. Ênfase
```
*This text is italicized*
_This is italicized too_

**This is bold text**
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***
```
*This text is italicized*  
_This is italicized too_

**This is bold text**  
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***

### 2.4. Citação de texto
Use \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

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

Você também pode usar links de caminho relativo para apontar para outros arquivos dentro do repositório. O uso é o mesmo que no terminal.
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
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Lista de tarefas
Para criar uma lista de tarefas, adicione \[ ] antes de cada item.
Para marcar uma tarefa como concluída, use \[x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Anexar imagens
```
Método: ![(opcional)descrição da imagem](url){(opcional)opções adicionais}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Criar tabelas
Você pode criar tabelas usando | e -.
Deve haver uma linha em branco antes da tabela para que seja exibida corretamente.
É necessário usar pelo menos três - para que seja reconhecido corretamente.
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
