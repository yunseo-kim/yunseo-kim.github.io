---
title: "Resumo da sintaxe do Markdown no GitHub"
description: "O que é Markdown? Veja um guia conciso da sintaxe, baseado no GitHub Flavored Markdown, para escrever e hospedar posts no GitHub Pages."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Para usar o GitHub Pages, é preciso conhecer a sintaxe do Markdown.
Este texto foi escrito com base na documentação oficial do GitHub: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) e [Sintaxe básica de escrita e formatação](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. O que é Markdown
> O Markdown é uma linguagem de marcação leve baseada em texto simples. É usada para escrever documentos com formatação usando texto puro e se destaca por ter uma sintaxe fácil e simples em comparação com linguagens de marcação em geral. Como pode ser facilmente convertido em documentos formatados como HTML e RTF, é muito usado em arquivos README distribuídos com softwares e em publicações online.  
> John Gruber criou a linguagem Markdown no ano 12004 do Calendário do Holoceno, em colaboração significativa com Aaron Swartz no aspecto da sintaxe, visando permitir que as pessoas escrevam usando um formato de texto simples, fácil de ler e escrever, com conversão opcional para XHTML (ou HTML) estruturalmente válido.

- [Wikipédia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Sintaxe do Markdown
Como o Markdown não possui um padrão único, detalhes da sintaxe podem variar conforme o uso. A sintaxe aqui resumida segue o padrão do [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) (GFM).

### 2.1. Quebra de linha e parágrafos
No Markdown, pressionar Enter uma vez não é interpretado como quebra de linha.
~~~
Primeira frase.
Segunda frase.
Terceira frase.
~~~
Primeira frase.
Segunda frase.
Terceira frase.

Para quebra de linha, use dois ou mais espaços no final da linha.
~~~
Primeira frase.  
Segunda frase.  
Terceira frase.
~~~
Primeira frase.  
Segunda frase.  
Terceira frase.

Separe parágrafos com uma linha em branco (duas vezes Enter).
~~~
Um parágrafo.

Outro parágrafo.
~~~
Um parágrafo.

Outro parágrafo.

### 2.2. Cabeçalhos (Headers)
Há 6 níveis.
```
# Isto é um H1
## Isto é um H2
### Isto é um H3
#### Isto é um H4
##### Isto é um H5
###### Isto é um H6
```
Em princípio, deve haver apenas um H1 por página; portanto, ao escrever posts ou documentos, raramente você o usa diretamente.

### 2.3. Ênfase
```
*Este texto está em itálico*
_Este também está em itálico_

**Este texto está em negrito**
__Este também está em negrito__

~~Este texto estava errado~~

_Você **pode** combiná-los_

***Todo este texto é importante***
```
*Este texto está em itálico*  
_Este também está em itálico_

**Este texto está em negrito**  
__Este também está em negrito__

~~Este texto estava errado~~

_Você **pode** combiná-los_

***Todo este texto é importante***

### 2.4. Citação de texto
Use \>.
```
> Esta é a primeira citação.
>> Esta é a segunda citação.
>>> Esta é a terceira citação.
```
> Esta é a primeira citação.
>> Esta é a segunda citação.
>>> Esta é a terceira citação.

### 2.5. Trechos de código
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

Você também pode especificar a linguagem de programação para habilitar realce de sintaxe.
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

Também é possível usar links relativos que apontam para outros arquivos no repositório. A forma de uso é a mesma do terminal.
```
[README](../README.md)
```

### 2.7. Lista não ordenada
Use - ou *.
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
   - Primeiro item aninhado
     - Segundo item aninhado
```
1. Primeiro item da lista
   - Primeiro item aninhado
     - Segundo item aninhado

### 2.10. Lista de tarefas
Para criar uma lista de tarefas, adicione \[ ] antes de cada item.
Para marcar como concluído, use \[x].
```
- [x] Concluir minhas alterações
- [ ] Enviar meus commits para o GitHub
- [ ] Abrir um pull request
```
- [x] Concluir minhas alterações
- [ ] Enviar meus commits para o GitHub
- [ ] Abrir um pull request

### 2.11. Inserir imagens
```
Como: ![(opcional, recomendado) descrição da imagem](url){(opcional) opções adicionais}
![Logotipo do GitHub](/images/logo.png)
![Logotipo do GitHub](/images/logo.png){: .align-center}
![Logotipo do GitHub](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tabelas
Você pode criar tabelas usando | e -.
Deixe uma linha em branco antes da tabela para que seja exibida corretamente.
Use pelo menos 3 hifens para que seja reconhecida.
```
 
| Alinhado à esquerda | Centralizado | Alinhado à direita |
| :---                |    :---:     |               ---: |
| git status          | git status   | git status         |
| git diff            | git diff     | git diff           |
```

| Alinhado à esquerda | Centralizado | Alinhado à direita |
| :---                |    :---:     |               ---: |
| git status          | git status   | git status         |
| git diff            | git diff     | git diff           |
