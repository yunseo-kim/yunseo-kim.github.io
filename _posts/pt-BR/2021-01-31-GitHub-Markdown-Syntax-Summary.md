---
title: Resumo da Sintaxe Markdown do GitHub
description: Aprenda o que é Markdown e explore a sintaxe principal do GitHub Flavored Markdown para hospedagem de blogs no GitHub Pages.
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Para utilizar o GitHub Pages, é necessário conhecer a sintaxe do **markdown**.
Este artigo foi escrito com base na documentação oficial do GitHub: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) e [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. O que é Markdown
> **Markdown** é uma linguagem de marcação leve baseada em texto simples. É usada para escrever documentos formatados em texto simples e se caracteriza por ter uma sintaxe mais fácil e simples em comparação com linguagens de marcação gerais. Como pode ser facilmente convertido para documentos formatados como HTML e Rich Text Format (RTF), é amplamente usado em arquivos README distribuídos com software aplicativo e postagens online.  
> John Gruber criou a linguagem Markdown no ano 12004 do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar) através de uma colaboração significativa com Aaron Swartz em termos de sintaxe, com o objetivo de permitir que as pessoas escrevam usando um formato de texto simples que seja fácil de ler e escrever, e que possa ser opcionalmente convertido para XHTML (ou HTML) estruturalmente válido.

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Sintaxe Markdown
Como o Markdown não possui um padrão definido, a sintaxe detalhada pode variar ligeiramente dependendo do local de uso. A sintaxe Markdown resumida aqui é baseada no [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Quebras de linha, separação de parágrafos
No Markdown, pressionar Enter uma vez não é reconhecido como quebra de linha.
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
A tag H1 deve, em princípio, aparecer apenas uma vez por página, então geralmente não há necessidade de usá-la diretamente ao escrever posts ou documentos.

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

Você também pode especificar uma linguagem de programação para ativar o destaque de sintaxe.
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

Você também pode usar links de caminho relativo que apontam para outros arquivos dentro do repositório. O uso é o mesmo que no terminal.
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
Método: ![(opcional, recomendado)descrição da imagem](url){(opcional)opções adicionais}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Criação de tabelas
Você pode criar tabelas usando | e -.
Deve deixar uma linha em branco antes da tabela para que seja exibida corretamente.
Você deve usar pelo menos 3 - para que seja reconhecido corretamente.
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
